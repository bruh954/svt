"""Most między silnikami kursów (czysty Python) a interfejsem w przeglądarce.

Wszystkie funkcje przyjmują i zwracają napisy JSON (albo proste typy), żeby łatwo je wołać z JavaScriptu.
Postęp każdego kursu zapisuje JavaScript (funkcja `save_hook`), tu nie dotykamy dysku.
"""
import importlib
import json
import random
import time

COURSE_IDS = ["hanzi_hero", "glagol", "ave", "logos", "abba", "kaszeby", "hangeul", "han", "kana", "nihon"]
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


def _load(cid, lang):
    key = (cid, lang)
    if key in _modules:
        return _modules[key]
    src = SOURCE_LANG.get(cid, "pl")
    suffix = "" if lang == src else "_" + lang
    E = importlib.import_module("courses.%s.engine%s" % (cid, suffix))
    C = importlib.import_module("courses.%s.content%s" % (cid, suffix))
    _modules[key] = (E, C)
    return E, C


def _is_hanzi():
    return _cur["cid"] == "hanzi_hero"


# ---------------------------------------------------------------------------
# Otwieranie kursu / zapis
# ---------------------------------------------------------------------------
def open_course(cid, lang, saved_json=None):
    E, C = _load(cid, lang)
    st = E.State(path=None, now=_now)
    if saved_json:
        try:
            loaded = json.loads(saved_json)
            d = E._default()
            d.update(loaded)
            d["settings"] = {**E._default()["settings"], **loaded.get("settings", {})}
            st.data = d
        except ValueError:
            pass

    def save():
        if save_hook:
            save_hook(cid, json.dumps(st.data, ensure_ascii=False))
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
def _word_view(h):
    E = _cur["E"]
    w = E.WORDS[h]
    if _is_hanzi():
        return {"form": w["hanzi"], "tr": w["pinyin"], "meaning": w["english"], "cog": None, "hook": w.get("hook"),
                "letter": False, "name": None}
    return {"form": w["form"], "tr": w["tr"], "meaning": w["pl"], "cog": w.get("cog"), "hook": w.get("hook"),
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
            bank = list(toks) + extra[:2]
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
    ok = _join(given) == _join(toks)
    why = None
    if not ok:
        try:
            why = E.explain_mistake(given, toks) if _is_hanzi() else E.explain_mistake(given, toks)
        except TypeError:
            why = None
    return json.dumps({"ok": ok, "why": why, "sub": _sent_sub(given) if given else ""}, ensure_ascii=False)


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
