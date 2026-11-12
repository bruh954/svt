"""Most między silnikami kursów (czysty Python) a interfejsem w przeglądarce.

Wszystkie funkcje przyjmują i zwracają napisy JSON (albo proste typy), żeby łatwo je wołać z JavaScriptu.
Postęp każdego kursu zapisuje JavaScript (funkcja `save_hook`), tu nie dotykamy dysku.
"""
import importlib
import json
import random
import time

COURSE_IDS = ["hanzi_hero", "glagol", "ave", "logos", "abba", "kaszeby", "hangeul", "han", "kana", "nihon",
              "greek", "german", "french", "italian", "spanish", "russian", "turkish", "norse", "estonian", "serbian", "finnish"]
NEW = {"greek", "german", "french", "italian", "spanish", "russian", "turkish", "norse", "estonian", "serbian", "finnish"}
SOURCE_LANG = {"hanzi_hero": "en"}  # pozostałe kursy mają treść źródłową po polsku

save_hook = None   # ustawia JavaScript: save_hook(course_id, json_string)
tz_shift = 0       # sekundy do odjęcia od czasu UTC, żeby „dzień" był lokalny

_cur = {"cid": None, "lang": None, "E": None, "C": None, "state": None, "session": None, "kind": None}
_modules = {}


def set_env(shift_seconds, hook):
    global tz_shift, save_hook
    tz_shift = int(shift_seconds)
    save_hook = hook


def _now():
    return time.time() - tz_shift


def _load(cid, lang, variant=None):
    key = (cid, lang, variant)
    if key in _modules:
        return _modules[key]
    src = SOURCE_LANG.get(cid, "pl")
    suffix = "" if lang == src else "_" + lang
    if variant:   # np. serbski cyrylicą: courses/serbian/engine_cyr.py
        E = importlib.import_module("courses.%s.engine_%s" % (cid, variant))
        C = importlib.import_module("courses.%s.content_%s" % (cid, variant))
        _modules[key] = (E, C)
        return E, C
    try:
        E = importlib.import_module("courses.%s.engine%s" % (cid, suffix))
        C = importlib.import_module("courses.%s.content%s" % (cid, suffix))
    except ImportError:  # kurs bez wersji w tym języku: używamy podstawowej
        E = importlib.import_module("courses.%s.engine" % cid)
        C = importlib.import_module("courses.%s.content" % cid)
    _modules[key] = (E, C)
    return E, C


# Serbski: łacinka <-> cyrylica (identyfikatory słów w zapisie postępu są zawsze łacińskie)
_SR = [("lj", "љ"), ("nj", "њ"), ("dž", "џ"), ("a", "а"), ("b", "б"), ("v", "в"), ("g", "г"), ("d", "д"), ("đ", "ђ"),
       ("e", "е"), ("ž", "ж"), ("z", "з"), ("i", "и"), ("j", "ј"), ("k", "к"), ("l", "л"), ("m", "м"), ("n", "н"),
       ("o", "о"), ("p", "п"), ("r", "р"), ("s", "с"), ("t", "т"), ("ć", "ћ"), ("u", "у"), ("f", "ф"), ("h", "х"),
       ("c", "ц"), ("č", "ч"), ("š", "ш")]


def _sr_cyr(text):
    out, i, low = "", 0, text.lower()
    while i < len(text):
        for a, b in _SR:
            if low.startswith(a, i):
                out += b.upper() if text[i].isupper() else b
                i += len(a)
                break
        else:
            out += text[i]
            i += 1
    return out


def _sr_lat(text):
    out = ""
    for ch in text:
        for a, b in _SR:
            if ch.lower() == b:
                out += (a[0].upper() + a[1:]) if ch.isupper() else a
                break
        else:
            out += ch
    return out


def _bare(t):
    return t.replace("\u0301", "")


def _is_hanzi():
    return _cur["cid"] == "hanzi_hero"


# ---------------------------------------------------------------------------
# Otwieranie kursu / zapis
# ---------------------------------------------------------------------------


def open_course(cid, lang, saved_json=None):
    loaded = None
    if saved_json:
        try:
            loaded = json.loads(saved_json)
        except ValueError:
            loaded = None
    cyr = cid == "serbian" and bool(loaded and loaded.get("settings", {}).get("cyr"))
    E, C = _load(cid, lang, "cyr" if cyr else None)
    st = E.State(path=None, now=_now)
    if loaded:
        d = E._default()
        d.update(loaded)
        d["settings"] = {**E._default()["settings"], **loaded.get("settings", {})}
        words = d.get("words") or {}
        if cyr:
            words = {(k if k.startswith("lit:") else _sr_cyr(k)): v for k, v in words.items()}
        if any(k not in E.WORDS for k in words):   # starsze zapisy: słowa bez znaku akcentu
            by_bare = {_bare(k): k for k in E.WORDS}
            words = {(k if k in E.WORDS else by_bare.get(_bare(k), k)): v for k, v in words.items()}
        d["words"] = words
        st.data = d

    def save():
        if save_hook:
            data = st.data
            if cyr:
                data = dict(data, words={(k if k.startswith("lit:") else _sr_lat(k)): v for k, v in data["words"].items()})
            save_hook(cid, json.dumps(data, ensure_ascii=False))
    st.save = save
    _cur.update(cid=cid, lang=lang, E=E, C=C, state=st, session=None, kind=None)
    st.check_streak()
    st.hearts()
    return True


def course_progress(cid, saved_json):
    """Mały skrót do kafelka na ekranie głównym: (korony, liczba działów, xp)."""
    try:
        d = json.loads(saved_json)
    except (TypeError, ValueError):
        return json.dumps({"crowns": 0, "xp": 0, "streak": 0})
    crowns = sum(u.get("crowns", 0) for u in d.get("units", {}).values())
    return json.dumps({"crowns": crowns, "xp": d.get("xp_total", 0), "streak": d.get("streak", 0)})


# ---------------------------------------------------------------------------
# Słowa i tokeny
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# IPA dla kursów bez syntezatora mowy, w których zapis (transliteracja) jest częścią nauki
# ---------------------------------------------------------------------------
_OCS_IPA = [("ль", "ʎ"), ("нь", "ɲ"), ("рь", "rʲ"), ("оу", "u"), ("ꙋ", "u"), ("ѹ", "u"), ("у", "u"), ("а", "a"),
            ("б", "b"), ("в", "v"), ("г", "ɡ"), ("д", "d"), ("ѥ", "jɛ"), ("е", "ɛ"), ("ж", "ʒ"), ("ѕ", "dz"),
            ("ꙃ", "dz"), ("з", "z"), ("ꙁ", "z"), ("и", "i"), ("і", "i"), ("к", "k"), ("л", "l"), ("м", "m"),
            ("н", "n"), ("о", "ɔ"), ("п", "p"), ("р", "r"), ("с", "s"), ("т", "t"), ("ф", "f"), ("х", "x"),
            ("ѡ", "ɔː"), ("щ", "ʃt"), ("ц", "ts"), ("ч", "tʃ"), ("ш", "ʃ"), ("ъ", "ʊ"), ("ꙑ", "ɨ"), ("ь", "ɪ"),
            ("ѣ", "æ"), ("ю", "ju"), ("ꙗ", "ja"), ("ѩ", "jɛ̃"), ("ѧ", "ɛ̃"), ("ѭ", "jɔ̃"), ("ѫ", "ɔ̃"),
            ("ѯ", "ks"), ("ѱ", "ps"), ("ѳ", "f"), ("ѵ", "i")]
_SYR_IPA = [("p̄", "f"), ("ʾ", "ʔ"), ("ʿ", "ʕ"), ("ḥ", "ħ"), ("ṭ", "tˤ"), ("ṣ", "sˤ"), ("š", "ʃ"), ("ḇ", "v"),
            ("ḡ", "ɣ"), ("ḏ", "ð"), ("ḵ", "x"), ("ṯ", "θ"), ("ĕ", "ə"), ("ə", "ə"), ("ă", "a"), ("ā", "ɑː"),
            ("ē", "eː"), ("ī", "iː"), ("ō", "oː"), ("ū", "uː"), ("e", "ɛ"), ("y", "j"), ("g", "ɡ")]


def _ipa_convert(text, table):
    out, i, low = "", 0, text.lower()
    while i < len(low):
        for src, dst in table:
            if low.startswith(src, i):
                out += dst; i += len(src); break
        else:
            out += low[i]; i += 1
    return out


def _ipa(cid, w):
    """IPA słowa (przybliżona rekonstrukcja) albo None."""
    if w.get("letter"):
        return None
    try:
        if cid == "glagol":
            return "/" + _ipa_convert(w["form"], _OCS_IPA) + "/"
        if cid == "abba":
            t = _ipa_convert(w["tr"], _SYR_IPA)
            import re as _re
            t = _re.sub(r"([bdkpstzlmnrqfʃħɡ])\1", r"\1ː", t)
            return "/" + t + "/"
    except Exception:
        return None
    return None


def _word_view(h):
    E = _cur["E"]
    w = E.WORDS[h]
    if _is_hanzi():
        return {"form": w["hanzi"], "tr": w["pinyin"], "meaning": w["english"], "cog": None, "hook": w.get("hook"),
                "letter": False, "name": None}
    ipa = _ipa(_cur.get("cid"), w)
    return {"form": w["form"], "tr": (w["tr"] + "   " + ipa) if ipa else w["tr"], "meaning": w["pl"], "cog": w.get("cog"), "hook": w.get("hook"),
            "letter": bool(w.get("letter")), "name": w.get("name")}


def _join(toks):
    E = _cur["E"]
    return E.join(toks) if hasattr(E, "join") else "".join(toks)


def _tok_sub(tok):
    E = _cur["E"]
    if _is_hanzi():
        n = E.token_num(tok)
        return E.to_marked(n) if n else None
    try:
        return E.token_tr(tok)
    except Exception:
        return None


def _sent_sub(toks):
    E = _cur["E"]
    if _is_hanzi():
        return E.sentence_pinyin(toks)
    return E.sentence_tr(toks)


def _tiles(toks):
    return [{"v": t, "sub": _tok_sub(t)} for t in toks]


# ---------------------------------------------------------------------------
# Ekran główny kursu
# ---------------------------------------------------------------------------
def home():
    E, C, st = _cur["E"], _cur["C"], _cur["state"]
    units = []
    for i, u in enumerate(E.UNITS):
        un = st.unlocked(i)
        units.append({
            "i": i, "id": u["id"], "title": u["title"], "icon": u.get("icon"), "color": u.get("color"),
            "track": u.get("track"), "crowns": st.crowns(u["id"]), "lessons": st.lessons(u["id"]),
            "unlocked": bool(un), "reason": None if un else st.unlock_reason(i),
            "cracked": bool(st.cracked(i)), "strength": st.unit_strength(i)})
    current = next((u["i"] for u in units if u["unlocked"] and u["crowns"] == 0), None)
    chats = [{"id": c["id"], "title": c["title"], "partner": c["partner"], "avatar": c["avatar"],
              "stars": st.chat_stars(c["id"]), "unlocked": bool(st.chat_unlocked(c))} for c in C.CHATS]
    d = st.data
    lvl, lxp, lneed = st.level()
    return json.dumps({
        "units": units, "tracks": getattr(C, "TRACKS", {}), "current": current, "chats": chats,
        "hearts": st.hearts(), "heart_max": E.HEART_MAX, "next_heart": st.seconds_to_next_heart(),
        "gems": d["gems"], "streak": d["streak"], "longest": d["longest_streak"], "freezes": d["freezes"],
        "xp_today": st.xp_today(), "goal": d["daily_goal"], "xp_total": d["xp_total"],
        "level": lvl, "level_xp": lxp, "level_need": lneed, "week": st.week_xp(),
        "onboarded": d["onboarded"], "settings": d["settings"], "words_learned": len(st.learned_words()),
        "words_total": len(E.WORDS), "goals": E.GOALS, "max_crowns": E.MAX_CROWNS,
        "freeze_cost": E.FREEZE_COST, "refill_cost": E.REFILL_COST, "max_freezes": E.MAX_FREEZES,
        "has_sounds": hasattr(E, "make_sound_training") or hasattr(E, "make_tone_training"),
        "hanzi": _is_hanzi(),
        "lessons_completed": d["lessons_completed"],
    }, ensure_ascii=False)


def onboard(goal):
    st = _cur["state"]
    st.data["daily_goal"] = int(goal)
    st.data["onboarded"] = True
    st.save()
    return True


def set_goal(goal):
    st = _cur["state"]
    st.data["daily_goal"] = int(goal)
    st.save()
    return True


def tone_map():
    """Chiński: {zapis znakami: [tony kolejnych znaków]} dla słów kursu (do kolorowania wg tonu)."""
    E = _cur["E"]
    out = {}
    cid = _cur["cid"]
    try:
        if cid == "hanzi_hero":
            for w in E.WORDS.values():
                tones = [t for _s, t in w["syllables"]]
                if len(tones) == len(w["hanzi"]):
                    out[w["hanzi"]] = tones
            for k, v in getattr(E, "CHAT_EXTRA", {}).items():
                tones = [E.split_syllable(x)[1] for x in str(v[0]).split()]
                if len(tones) == len(k):
                    out.setdefault(k, tones)
        elif cid == "han":
            for w in E.WORDS.values():
                pn = w.get("pn")
                if pn and not w.get("letter") and len(pn.split()) == len(w["form"]):
                    out[w["form"]] = [int(x[-1]) if x[-1].isdigit() else 5 for x in pn.split()]
    except Exception:
        pass
    return json.dumps(out, ensure_ascii=False)


def set_setting(key, value):
    st = _cur["state"]
    st.data["settings"][key] = bool(value)
    st.save()
    return True


def buy(what):
    st = _cur["state"]
    ok = st.buy_freeze() if what == "freeze" else st.buy_refill()
    st.save()
    return bool(ok)


def reset_progress():
    _cur["state"].reset()
    return True


# ---------------------------------------------------------------------------
# Sesje
# ---------------------------------------------------------------------------
def start(kind, unit=None):
    E, st = _cur["E"], _cur["state"]
    rng = random.Random()
    if kind == "lesson":
        exs = E.make_lesson(st, int(unit), audio=True, rng=rng) if _is_hanzi() else E.make_lesson(st, int(unit), rng)
        sess = E.Session(exs, "lesson", int(unit), hearts=True)
    elif kind == "practice":
        exs = E.make_practice(st, audio=True, rng=rng) if _is_hanzi() else E.make_practice(st, rng)
        sess = E.Session(exs, "practice", None, hearts=False)
    else:
        if _is_hanzi():
            exs = E.make_tone_training(st, audio=True, rng=rng)
        else:
            exs = E.make_sound_training(st, rng)
        sess = E.Session(exs, "sound", None, hearts=False)
    _cur["session"], _cur["kind"] = sess, kind
    return len(exs)


def _render(ex):
    t = ex["type"]
    out = {"type": t, "title": ex.get("title"), "retry": bool(ex.get("_retry"))}
    if t == "intro":
        out.update(_word_view(ex["word"]))
        out["audio"] = ex.get("audio")
    elif t == "insight":
        out.update(text=ex["text"])
    elif t == "choice":
        out.update(mode=ex["mode"], prompt=ex.get("prompt"), prompt_sub=ex.get("prompt_sub"),
                   options=ex["options"], option_subs=ex.get("option_subs"), audio=ex.get("audio"),
                   autoplay=bool(ex.get("autoplay")))
        if ex["mode"] == "sentence":
            toks = ex.get("words") or []
            out["sentence"] = _join(toks) if not _is_hanzi() else "".join(toks)
            out["sentence_sub"] = _sent_sub(toks) if toks else None
        if ex.get("word"):
            out["word_view"] = _word_view(ex["word"])
    elif t == "match":
        out.update(pairs=[list(p) for p in ex["pairs"]])
    elif t == "build":
        out.update(prompt=ex["prompt"], bank=_tiles(ex["bank"]), think=ex.get("think"), audio=ex.get("audio"),
                   insight=ex.get("insight"))
    elif t == "type":
        out.update(prompt=ex["prompt"], prompt_sub=ex.get("prompt_sub"))
    elif t == "draw":
        w = _word_view(ex["word"]) if ex.get("word") else {}
        out.update(prompt=ex["prompt"], prompt_sub=ex.get("prompt_sub"), glyph=ex["answer"],
                   hook=ex.get("hook") or w.get("hook"), meaning=w.get("meaning"), audio=ex.get("audio"))
    elif t == "tone":
        out.update(hum=ex.get("hum"), prompt=ex.get("prompt"), prompt_sub=ex.get("prompt_sub"),
                   meaning=_word_view(ex["word"])["meaning"] if ex.get("word") else None,
                   autoplay=bool(ex.get("autoplay")))
    elif t == "tone_pair":
        out.update(prompt=ex["prompt"], prompt_sub=ex.get("prompt_sub"), options=[list(o) for o in ex["options"]],
                   meaning=_word_view(ex["word"])["meaning"] if ex.get("word") else None)
    else:
        out.update(prompt=ex.get("prompt"))
    return out


def _progress():
    s = _cur["session"]
    st = _cur["state"]
    return {"progress": s.progress, "combo": s.combo, "hearts": st.hearts(), "use_hearts": s.use_hearts,
            "left": len(s.queue), "kind": _cur["kind"]}


def current():
    s = _cur["session"]
    if s is None:
        return json.dumps({"none": True})
    if s.finished:
        return json.dumps({"finished": True, **_progress()})
    return json.dumps({"ex": _render(s.current), **_progress()}, ensure_ascii=False)


def check(payload_json):
    """Sprawdza odpowiedź na bieżące ćwiczenie. Nie zmienia sesji (to robi `advance`)."""
    E = _cur["E"]
    s = _cur["session"]
    ex = s.current
    p = json.loads(payload_json) if isinstance(payload_json, str) else payload_json
    t = ex["type"]
    why, ok = None, None
    solution = ex.get("solution")
    if t in ("intro", "insight"):
        return json.dumps({"ok": None})
    if t == "choice":
        ok = p.get("value") == ex["answer"]
        why = None if ok else ex.get("why")
    elif t == "tone":
        ok = int(p.get("value")) == int(ex["answer"])
        return json.dumps({"ok": ok, "solution": solution, "answer_tone": int(ex["answer"])}, ensure_ascii=False)
    elif t == "tone_pair":
        ok = list(p.get("value")) == list(ex["answer"])
        return json.dumps({"ok": ok, "solution": solution, "answer_pair": list(ex["answer"])}, ensure_ascii=False)
    elif t == "build":
        given = p.get("tokens", [])
        if _join(given) == _join(ex["answer"]):
            ok = True
        else:
            ok = False
            try:
                why = E.explain_mistake(given, ex["answer"], ex.get("traps")) if not _is_hanzi() \
                    else E.explain_mistake(given, ex["answer"])
            except TypeError:
                why = E.explain_mistake(given, ex["answer"])
        if not ok:
            solution = _join(ex["answer"]) + "\n" + _sent_sub(ex["answer"])
    elif t == "type":
        if _is_hanzi():
            res = E.check_typed_pinyin(p.get("text", ""), ex["answer"])
            ok = res == "correct"
            why = None if ok else ("Litery dobrze, ale tony nie." if _cur["lang"] == "pl" else "Letters are right, but the tones are off.") if res == "tones" else None
            res = "correct" if ok else "wrong"
        else:
            res = E.check_typed(p.get("text", ""), ex["answer"])
            ok = res in ("correct", "close")
        if res == "close":
            why = None
            solution = "Pełny zapis: %s" % ex["answer"]
    elif t == "match":
        ok = True
    elif t == "draw":
        return json.dumps({"ok": "self", "solution": ex["answer"]}, ensure_ascii=False)
    return json.dumps({"ok": ok, "why": why, "solution": solution, "answer": ex.get("answer") if t in ("choice",) else None},
                      ensure_ascii=False)


def advance(ok):
    """Zalicza odpowiedź (True / False / None dla kart bez oceny), zwraca stan po niej."""
    s, st = _cur["session"], _cur["state"]
    ex = s.current
    ok = None if ok in (None, "null") else (ok is True or ok == "1")
    graded = ex["type"] not in ("intro", "insight")
    if graded and ok is False and s.use_hearts:
        st.lose_heart()
    milestone = s.answer(None if not graded else bool(ok))
    out_of_hearts = bool(s.use_hearts and st.hearts() <= 0 and not s.finished)
    st.save()
    return json.dumps({"milestone": milestone, "out_of_hearts": out_of_hearts, "finished": s.finished,
                       **_progress()})


def finish():
    s, st = _cur["session"], _cur["state"]
    ev = st.finish(s)
    ev["kind"] = _cur["kind"]
    ev["mistakes"] = s.mistakes
    ev["max_combo"] = s.max_combo
    ev["accuracy"] = s.accuracy
    ev["gems_total"] = st.data["gems"]
    _cur["session"] = None
    return json.dumps(ev, ensure_ascii=False, default=list)


def abandon():
    _cur["session"] = None
    return True


# ---------------------------------------------------------------------------
# Rozmowy
# ---------------------------------------------------------------------------
def _chat(cid):
    return next(c for c in _cur["C"].CHATS if c["id"] == cid)


def _punct():
    E, C = _cur["E"], _cur["C"]
    out = set(getattr(C, "PUNCT", None) or getattr(E, "PUNCT", None) or ())
    out |= set(getattr(E, "OPEN_PUNCT", ()) or ())
    return out | set("!?.,:;¿¡。！？，、")


def _no_punct(toks):
    p = _punct()
    return [t for t in toks if t not in p]


def chat_get(cid):
    c = _chat(cid)
    E, st = _cur["E"], _cur["state"]
    turns = []
    learned = [h for h in st.learned_words() if (_is_hanzi() or not E.WORDS[h]["letter"])]
    for t in c["turns"]:
        item = {"bot": _tiles(t["bot"]), "bot_text": _join(t["bot"]), "bot_sub": _sent_sub(t["bot"]), "en": t["en"],
                "note": t.get("note")}
        if "options" in t:
            item["options"] = [{"tiles": _tiles(o[0]), "text": _join(o[0]), "sub": _sent_sub(o[0]),
                                "ok": bool(o[1]), "why": o[2]} for o in t["options"]]
        else:
            toks, pl = t["build"]
            extra = [h for h in learned if h not in toks]
            random.shuffle(extra)
            bank = _no_punct(toks) + extra[:2]   # interpunkcji nie trzeba układać
            random.shuffle(bank)
            item["build"] = {"prompt": pl, "bank": _tiles(bank), "answer": list(toks), "text": _join(toks)}
        turns.append(item)
    return json.dumps({"id": c["id"], "title": c["title"], "partner": c["partner"], "avatar": c["avatar"],
                       "turns": turns}, ensure_ascii=False)


def chat_check(cid, turn, tokens):
    c = _chat(cid)
    E = _cur["E"]
    toks, _pl = c["turns"][int(turn)]["build"]
    given = list(tokens)
    ok = _join(_no_punct(given)) == _join(_no_punct(toks))
    why = None
    if not ok:
        try:
            why = E.explain_mistake(given, toks) if _is_hanzi() else E.explain_mistake(given, toks)
        except TypeError:
            why = None
    return json.dumps({"ok": ok, "why": why, "text": _join(toks) if ok else _join(given), "sub": _sent_sub(toks if ok else given) if given else ""}, ensure_ascii=False)


def chat_finish(cid, mistakes):
    st = _cur["state"]
    had_full = st.hearts() >= _cur["E"].HEART_MAX
    ev = st.finish_chat(_chat(cid), int(mistakes))
    ev["had_full"] = had_full
    return json.dumps(ev, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Opis ścieżki dźwięku tonów (do syntezy w przeglądarce)
# ---------------------------------------------------------------------------
def tone_contours():
    return json.dumps({"1": [[0, 5], [1, 5]], "2": [[0, 3], [1, 5]], "3": [[0, 2], [0.5, 1], [1, 4]],
                       "4": [[0, 5], [1, 1]]})
