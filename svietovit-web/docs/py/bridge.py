"""Most między silnikami kursów (czysty Python) a interfejsem w przeglądarce.

Wszystkie funkcje przyjmują i zwracają napisy JSON (albo proste typy), żeby łatwo je wołać z JavaScriptu.
Postęp każdego kursu zapisuje JavaScript (funkcja `save_hook`), tu nie dotykamy dysku.
"""
import importlib
import json
import random
import time

COURSE_IDS = ["hanzi_hero", "glagol", "ave", "logos", "abba", "kaszeby", "hangeul", "han", "kana", "nihon",
              "greek", "german", "french", "italian", "spanish", "russian", "turkish", "norse", "estonian", "serbian", "finnish", "czech", "slovak"]
NEW = {"greek", "german", "french", "italian", "spanish", "russian", "turkish", "norse", "estonian", "serbian", "finnish", "czech", "slovak"}
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
    parts = (_by_lang(getattr(_cur["C"], "PARTS", {})) or {}).get(h)
    return {"parts": parts, "form": w["form"], "tr": (w["tr"] + "   " + ipa) if ipa else w["tr"], "meaning": w["pl"], "cog": w.get("cog"), "hook": w.get("hook"),
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
        if u.get("hidden"):               # słowa larpów: istnieją w kursie, ale nie ma ich na ścieżce
            continue
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
    larps = []
    for lp in getattr(C, "LARPS", []):
        try:
            un = bool(st.chat_unlocked(lp))
        except Exception:
            un = True
        larps.append({"id": lp["id"], "title": lp["title"], "partner": lp["partner"], "avatar": lp["avatar"],
                      "fee": lp["fee"], "scene": lp["scene"], "goal": lp["goal"], "unlocked": un,
                      "best": d.get("larps", {}).get(lp["id"]), "can_pay": d["xp_total"] >= lp["fee"],
                      "levels": _larp_levels_view(lp), "disclaimer": lp.get("disclaimer"), "reward": lp.get("reward")})
    return json.dumps({"larps": larps, "paradigms": _paradigm_list(),
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
def _larp_round_exs(rng):
    """Seria ćwiczeń (jak w zwykłej lekcji) z tematu bieżącej kwestii larpa: karty nowych słów + ok. 10 ćwiczeń."""
    E, st = _cur["E"], _cur["state"]
    cfg, lvl = _larp["cfg"], _larp["lvl"]
    n = cfg["nodes"][_larp["node"]]
    uidx = next(i for i, u in enumerate(E.UNITS) if u["id"] == n["unit"])
    pool = [h for h in n["pool"] if h in E.WORDS]
    known = list(dict.fromkeys([h for h in E.WORDS if E.WORDS[h]["unit"] < uidx] + pool))
    gen = E.Gen(known, rng)
    learned = set(st.learned_words())
    exs = [gen.intro(h) for h in pool if h not in learned]
    P = set(_cur["C"].PUNCT)
    ks = set(known)
    mine = [x for j, u in enumerate(E.UNITS) if j <= uidx and u["id"].startswith("lp_%s_" % _larp["id"]) for x in u.get("sentences", [])]
    sents = [x for x in mine if all(t in ks or t in P for t in x[0])]
    sents.sort(key=lambda x: -sum(1 for t in x[0] if t in pool))
    ans = {tuple(m["build"][0]) for m in cfg["nodes"].values() if m.get("build")}   # odpowiedzi kelnerowi nie wchodzą do serii
    sents = [x for x in sents if tuple(x[0]) not in ans and any(t in pool for t in x[0])][:8]     # odpowiedź kelnerowi pada dopiero na końcu, nie w serii
    bq, mq = list(sents), list(reversed(sents))              # każde zdanie najwyżej raz w danym typie ćwiczenia
    rng.shuffle(bq)
    extra = [h for h in known if h not in pool]
    rng.shuffle(extra)
    dpool = pool + extra[:6]
    typed_p = [0, 0.15, 0.3, 0.45, 0.6][max(0, min(4, lvl - 1))]
    graded = []
    if len(pool) >= 4:
        graded.append(gen.match(pool[:5], "pl"))
    i = 0
    while len(graded) < 10 and pool:
        h = pool[i % len(pool)]; i += 1
        r = rng.random()
        if r < typed_p:
            graded.append(gen.typing(h))
        elif bq and r < typed_p + 0.4:
            toks, pl, tr = bq.pop()
            graded.append(gen.build(toks, pl, tr))
        elif mq and r < typed_p + 0.55:
            toks, pl, tr = mq.pop(0)
            graded.append(gen.sentence_meaning(toks, pl, E.all_sentence_pl()))
        else:
            graded.append(gen.meaning(h, dpool) if rng.random() < 0.5 else gen.form(h, dpool))
    rng.shuffle(graded)
    return exs + graded


def _larp_round_finish():
    s, st = _cur["session"], _cur["state"]
    lp = _larp_def(_larp["id"])
    n = _larp["cfg"]["nodes"][_larp["node"]]
    acc = s.accuracy
    for h, ok in s.word_results:
        st.record_word(h, ok)
    for h in n.get("pool", []):
        st.data["words"].setdefault(h, {"box": 0, "last": st.now(), "right": 0, "wrong": 0})
    _larp["rounds"].add(_larp["node"])
    if acc >= 0.9:
        verdict = "great"
    elif acc >= 0.7:
        verdict = "ok"; _larp["weak"] += 1
    else:
        verdict = "bad"; _larp["mistakes"] += 1; _larp["patience"] -= 1
    res = {"kind": "larp", "acc": acc, "verdict": verdict, "patience": _larp["patience"], "mistakes": s.mistakes}
    if _larp["patience"] <= 0:
        res["end"] = _larp_finish(lp, "fail")
    st.save()
    _cur["session"] = None
    return json.dumps(res, ensure_ascii=False)


def start(kind, unit=None):
    E, st = _cur["E"], _cur["state"]
    rng = random.Random()
    if kind == "larp":
        exs = _larp_round_exs(rng)
        sess = E.Session(exs, "practice", None, hearts=False)
        _cur["session"], _cur["kind"] = sess, kind
        return len(exs)
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
    if kind == "practice" and _cur.get("cid") in DEAD_LANGS:
        _plant_demon(exs, rng)
    _cur["session"], _cur["kind"] = sess, kind
    return len(exs)


DEAD_LANGS = {"ave", "logos", "abba", "norse", "glagol"}


def _plant_demon(exs, rng):
    """W językach wymarłych jedno zdanie w serii losowych ćwiczeń naprawdę wzywa demona (kończy serię przed końcem),
    a ostrzeżenie „to zdanie może wezwać demona” dostaje ono i jeszcze 2–3 niewinne zdania w losowej kolejności."""
    ok = [i for i, e in enumerate(exs) if i >= 2 and e["type"] in ("build", "type", "choice") and (e["type"] != "choice" or e.get("mode") == "sentence")]
    if len(exs) < 6 or len(ok) < 3:
        return
    d = rng.choice(ok)
    decoys = rng.sample([i for i in ok if i != d], min(len(ok) - 1, 2 + (len(exs) > 12)))
    exs[d]["_demon"] = True
    for i in [d] + decoys:
        exs[i]["_warn"] = True


def _render(ex):
    t = ex["type"]
    out = {"type": t, "title": ex.get("title"), "retry": bool(ex.get("_retry")), "warn": bool(ex.get("_warn"))}
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
            out["sentence"] = _larp_disp(toks) if not _is_hanzi() else "".join(toks)
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
        note = None
        if _join(given) == _join(ex["answer"]):
            ok = True
        elif _join(_no_punct(given)) == _join(_no_punct(ex["answer"])):
            ok = True        # brak interpunkcji nie jest błędem, ale zwracamy uwagę
            pl = _cur["lang"] == "pl"
            comma = "," in ex["answer"]
            note = (("Zaliczone, ale w zdaniu powinien być %s: %s\nPrzecinek bywa ważny: „Idziemy jeść, babciu” to nie to samo co „Idziemy jeść babciu”."
                     if comma else "Zaliczone, ale pamiętaj o interpunkcji: %s")
                    if pl else
                    ("Accepted, but the sentence needs a %s: %s\nA comma can change the meaning: “Let's eat, grandma” is not “Let's eat grandma”."
                     if comma else "Accepted, but mind the punctuation: %s")) % ((("przecinek" if pl else "comma"), _join(ex["answer"])) if comma else (_join(ex["answer"]),))
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
    return json.dumps({"ok": ok, "why": why, "solution": solution, "note": locals().get("note"), "answer": ex.get("answer") if t in ("choice",) else None},
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
    demon = bool(ex.get("_demon"))
    if demon:
        s.queue.clear()          # demon przerywa serię przed ostatnim ćwiczeniem
    out_of_hearts = bool(s.use_hearts and st.hearts() <= 0 and not s.finished)
    st.save()
    return json.dumps({"milestone": milestone, "out_of_hearts": out_of_hearts, "finished": s.finished, "demon": demon,
                       **_progress()})


def finish():
    s, st = _cur["session"], _cur["state"]
    if _cur.get("kind") == "larp":
        return _larp_round_finish()
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


# ---------------------------------------------------------------------------
# Larpy: scena ze stawką (wpisowe w XP, cierpliwość rozmówcy, pytania „jedna szansa")
# ---------------------------------------------------------------------------
_larp = {"id": None, "lvl": 1, "cfg": None, "node": None, "patience": 0, "weak": 0, "mistakes": 0, "done": True, "typed": set(), "rounds": set()}


def _larp_def(lid):
    return next(x for x in _cur["C"].LARPS if x["id"] == lid)


def _larp_cfg(lp, lvl=1):
    """Larp z poziomami ma lp["levels"]; stary larp (jedna scena) jest sam swoim jedynym poziomem."""
    lv = lp.get("levels")
    return lv[max(1, min(int(lvl), len(lv))) - 1] if lv else lp


def _larp_rank(lid, lvl):
    return (_cur["state"].data.get("larp_lv", {}).get(lid) or {}).get(str(lvl))


def _larp_levels_view(lp):
    lv = lp.get("levels")
    if not lv:
        return None
    out = []
    for i, c in enumerate(lv, 1):
        out.append({"lvl": i, "title": c.get("title"), "best": _larp_rank(lp["id"], i),
                    "unlocked": i == 1 or (_larp_rank(lp["id"], i - 1) or 0) >= 1})
    return out


def _larp_chain(cfg):
    keys, k, seen = [], cfg["start"], set()
    while k and k not in seen and not cfg["nodes"][k].get("end"):
        keys.append(k); seen.add(k)
        k = cfg["nodes"][k].get("next")
    return keys


def _larp_disp(toks):
    """Zdanie do pokazania: wielka litera na początku każdego zdania (tokeny po kropce są zapisane małą literą)."""
    import re as _re
    s = _join(toks)
    if getattr(_cur["E"], "CAP_FIRST", False):
        s = _re.sub(r"([.!?]\s+)(\w)", lambda m: m.group(1) + m.group(2).upper(), s)
    return s


def _larp_norm(text):
    """Do porównania: początki zdań małą literą (to nie błąd), bez interpunkcji, pojedyncze spacje."""
    import re as _re
    text = _re.sub(r"(^|[.!?]\s*)(\w)", lambda m: m.group(1) + m.group(2).lower(), text.strip())
    P = set(_cur["C"].PUNCT)
    t = "".join(" " if c in P else c for c in text)
    return " ".join(t.split())


def _larp_plain(text):
    E = _cur["E"]
    if hasattr(E, "plain"):
        return E.plain(text).lower()
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(c) != "Mn")


def _larp_node(lp, key):
    cfg = _larp["cfg"]
    n = cfg["nodes"][key]
    out = {"key": key, "bot_text": _larp_disp(n["bot"]), "bot_sub": _sent_sub(n["bot"]), "pl": n.get("pl"),
           "deadly": bool(n.get("deadly")), "note": n.get("note")}
    if n.get("unit") and key not in _larp["rounds"]:
        out["lesson"] = True            # najpierw seria ćwiczeń z tematu tej kwestii
    if n.get("end"):
        out["end"] = True
    elif "options" in n:
        out["options"] = [{"i": i, "text": _join(o[0]), "sub": _sent_sub(o[0])} for i, o in enumerate(n["options"])]
    else:
        toks, pl = n["build"]
        st = _cur["state"]
        E = _cur["E"]
        if key in _larp["typed"]:
            words = _no_punct(toks)
            hint = cfg.get("hint")
            hs = ""
            if hint == "bank":
                w2 = list(words); random.shuffle(w2); hs = "  ·  ".join(w2)
            elif hint == "letters":
                hs = "  ".join(w[:1] + "…" for w in words)
            out["typed"] = {"prompt": pl, "hint": hs}
            return out
        pool = [h for h in (cfg.get("lexicon") or []) if h in E.WORDS and h not in toks]
        learned = [h for h in st.learned_words() if (_is_hanzi() or not E.WORDS[h].get("letter")) and h not in toks and h not in pool]
        random.shuffle(pool); random.shuffle(learned)
        bank = _no_punct(toks) + (pool + learned)[:int(cfg.get("extra", 3))]
        random.shuffle(bank)
        out["build"] = {"prompt": pl, "bank": _tiles(bank)}
    return out


def larp_start(lid, lvl=1):
    lp = _larp_def(lid)
    lvl = int(lvl or 1)
    cfg = _larp_cfg(lp, lvl)
    st = _cur["state"]
    d = st.data
    if lvl > 1 and not (lp.get("levels") and (_larp_rank(lid, lvl - 1) or 0) >= 1):
        return json.dumps({"ok": False, "reason": "locked"})
    if d["xp_total"] < lp["fee"]:
        return json.dumps({"ok": False, "reason": "xp"})
    d["xp_total"] -= lp["fee"]
    E = _cur["E"]
    lex = []
    for h in (cfg.get("lexicon") or []):
        if h in E.WORDS:
            d["words"].setdefault(h, {"box": 0, "last": st.now(), "right": 0, "wrong": 0})
            lex.append(_word_view(h))
    st.save()
    frac = float(cfg.get("typed", 0))
    keys = _larp_chain(cfg)
    typed = {k for i, k in enumerate(keys) if "build" in cfg["nodes"][k] and int((i + 1) * frac + 1e-9) > int(i * frac + 1e-9)}
    _larp.update(id=lid, lvl=lvl, cfg=cfg, node=cfg["start"], patience=cfg.get("patience", lp.get("patience", 3)), weak=0, mistakes=0, done=False, typed=typed, rounds=set())
    return json.dumps({"ok": True, "fee": lp["fee"], "patience": _larp["patience"], "max_patience": _larp["patience"], "level": lvl,
                       "lexicon": lex, "disclaimer": lp.get("disclaimer"), "level_title": cfg.get("title") if cfg is not lp else None,
                       "scene": cfg.get("scene", lp["scene"]), "goal": cfg.get("goal", lp["goal"]), "partner": lp["partner"], "avatar": lp["avatar"],
                       "title": lp["title"], "node": _larp_node(lp, cfg["start"])}, ensure_ascii=False)


def _larp_finish(lp, outcome):
    st = _cur["state"]
    d = st.data
    cfg, lvl = _larp["cfg"], _larp["lvl"]
    fee = lp["fee"]
    reward = cfg.get("reward") or lp.get("reward") or fee * 3
    gain = 0
    streak = False
    if outcome == "win":
        gain = reward
        streak = st.add_xp(gain)
        d["gems"] += 5
    elif outcome == "partial":
        if fee:
            gain = fee
            d["xp_total"] += fee           # sam zwrot wpisowego
        else:
            gain = reward // 3
            streak = st.add_xp(gain)
    rank = {"fail": 0, "partial": 1, "win": 2}[outcome]
    best = d.setdefault("larps", {})
    best[lp["id"]] = max(rank, best.get(lp["id"], 0))
    lv = d.setdefault("larp_lv", {}).setdefault(lp["id"], {})
    lv[str(lvl)] = max(rank, lv.get(str(lvl), 0))
    _larp["done"] = True
    st.save()
    nxt = lvl + 1 if lp.get("levels") and lvl < len(lp["levels"]) and outcome != "fail" else None
    endings = cfg.get("endings") or lp["endings"]
    return {"outcome": outcome, "fee": fee, "gain": gain, "net": gain - fee, "text": endings[outcome], "level": lvl, "next_level": nxt,
            "gems": 5 if outcome == "win" else 0, "streak_extended": bool(streak), "streak": d["streak"],
            "mistakes": _larp["mistakes"], "weak": _larp["weak"]}


def larp_answer(payload_json):
    """Odpowiedź w bieżącym węźle: {"option": i}, {"tokens": [...]} (klocki) albo {"text": "..."} (wpisana z klawiatury)."""
    if _larp["done"]:
        return json.dumps({"error": "done"})
    lp = _larp_def(_larp["id"])
    cfg = _larp["cfg"]
    n = cfg["nodes"][_larp["node"]]
    p = json.loads(payload_json)
    res = {"verdict": None, "why": None, "text": None, "sub": None}
    nxt = None
    if "options" in n:
        toks, verdict, target, why = n["options"][int(p["option"])]
        res.update(verdict=verdict, why=why, text=_join(toks), sub=_sent_sub(toks))
        if verdict != "bad":
            nxt = target
    else:
        toks, _pl = n["build"]
        cands = [toks] + list(n.get("alts") or [])
        want = [_larp_norm(_larp_disp(c)) for c in cands]
        disp = _larp_disp(toks)
        if "text" in p:
            raw = str(p.get("text") or "")
            given_s = _larp_norm(raw)
            if given_s in want:
                verdict = "good"
            elif given_s.lower() in [w.lower() for w in want]:
                verdict, res["why"] = "weak", "Wielkie i małe litery: " + disp
            elif _larp_plain(given_s) in [_larp_plain(w) for w in want]:
                verdict, res["why"] = "weak", "Brakuje znaków diakrytycznych: " + disp
            else:
                verdict = "bad"
            shown = raw.strip()
            sub = ""
        else:
            given = list(p.get("tokens", []))
            given_s = _larp_norm(_larp_disp(given))
            verdict = "good" if given_s in want else "bad"
            shown = disp if verdict == "good" else _larp_disp(given)
            sub = _sent_sub(toks if verdict == "good" else given) if given else ""
        res.update(verdict=verdict, text=shown if shown else "…", sub=sub if verdict != "bad" or "text" not in p else "")
        if verdict == "bad":
            res["why"] = n.get("why") or None
            res["answer"] = disp
        else:
            nxt = n["next"]
    if res["verdict"] == "weak":
        _larp["weak"] += 1
    if res["verdict"] == "bad":
        _larp["mistakes"] += 1
        if n.get("deadly"):
            _larp["patience"] = 0
        else:
            _larp["patience"] -= 1
        if _larp["patience"] <= 0:
            res["patience"] = 0
            res["end"] = _larp_finish(lp, "fail")
            return json.dumps(res, ensure_ascii=False)
    res["patience"] = _larp["patience"]
    if nxt:
        _larp["node"] = nxt
        node = _larp_node(lp, nxt)
        res["node"] = node
        if node.get("end"):
            clean = _larp["weak"] == 0 and (_larp["mistakes"] == 0 or not lp.get("strict"))
            res["end"] = _larp_finish(lp, "win" if clean else "partial")
    return json.dumps(res, ensure_ascii=False)


def larp_abandon():
    _larp["done"] = True
    return True


# ---------------------------------------------------------------------------
# Gramatyka: wzory odmian (koniugacje, deklinacje, wyjątki)
# ---------------------------------------------------------------------------
def _pid(p):
    pid = p[0] + ":" + p[2]
    return _sr_lat(pid) if _cur["E"].__name__.endswith("_cyr") else pid


def _by_lang(x):
    """Treść gramatyki może być słownikiem {język: ...} (kurs chiński ma źródło po angielsku)."""
    if isinstance(x, dict) and ("pl" in x or "en" in x):
        return x.get(_cur["lang"]) or x.get("pl") or x.get("en")
    return x


def _paradigms():
    return list(_by_lang(getattr(_cur["C"], "PARADIGMS", [])) or [])


def _paradigm_list():
    d = _cur["state"].data
    best = d.get("paradigms", {})
    return [{"id": _pid(p), "kind": p[0], "group": p[1], "title": p[2], "n": len(p[4].split("; ")),
             "best": best.get(_pid(p))} for p in _paradigms()]


def paradigm_get(pid):
    C = _cur["C"]
    ps = _paradigms()
    p = next(x for x in ps if _pid(x) == pid)
    labels = p[3] if isinstance(p[3], (list, tuple)) else _by_lang(C.PARADIGM_LABELS)[p[3]]
    raw = [f.split("|") for f in p[4].split("; ")]     # „dobra|zła|zła”: własne błędne odpowiedzi
    forms = [r[0] for r in raw]
    alts = [r[1:] for r in raw]
    same, kind = [], []                        # dystraktory: najpierw z wzorów o tych samych etykietach
    for x in ps:
        if x is p:
            continue
        if x[3] == p[3]:
            same += [f.split("|")[0] for f in x[4].split("; ")]
        elif x[0] == p[0]:
            kind += [f.split("|")[0] for f in x[4].split("; ")]
    random.shuffle(same)
    random.shuffle(kind)
    pool = [f for f in dict.fromkeys(same + kind) if f not in forms][:8]
    if isinstance(p[3], str) and p[3].startswith("t_") and len(set(forms)) > 1:
        pool = []          # ćwiczenie celowane: wybór tylko spośród własnych odpowiedzi
    return json.dumps({"id": pid, "kind": p[0], "group": p[1], "title": p[2], "note": p[5],
                       "labels": list(labels), "forms": forms, "alts": alts, "extra": pool}, ensure_ascii=False)


def paradigm_done(pid, mistakes):
    """Zalicza przejście całego wzoru: XP i gwiazdki (3 = bez błędu)."""
    st = _cur["state"]
    d = st.data
    mistakes = int(mistakes)
    stars = 3 if mistakes == 0 else (2 if mistakes <= 2 else 1)
    best = d.setdefault("paradigms", {})
    first = pid not in best
    best[pid] = max(stars, best.get(pid, 0))
    xp = (8 if first else 4) + (2 if mistakes == 0 else 0)
    streak = st.add_xp(xp)
    st.save()
    return json.dumps({"xp": xp, "stars": stars, "streak_extended": bool(streak), "streak": d["streak"]}, ensure_ascii=False)
