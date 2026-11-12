import json, random, sys
sys.path.insert(0, "/home/claude/svietovit"); sys.path.insert(0, "/home/claude/svietovit-web/src")
import bridge as B
B.set_env(0, lambda cid, js: None)
import os
for cid in [c for c in B.COURSE_IDS if os.path.isdir('/home/claude/svietovit/courses/'+c)] if not sys.argv[1:] else sys.argv[1:]:
    for lang in ("pl", "en"):
        if lang == "en" and cid in B.NEW: continue
        B.open_course(cid, lang)
        h = json.loads(B.home())
        n_ex = 0
        for kind, unit in [("lesson", 0), ("lesson", min(2, len(h["units"]) - 1)), ("practice", None), ("sound", None)]:
            if kind == "sound" and not h["has_sounds"]: continue
            B.start(kind, unit)
            guard = 0
            while True:
                cur = json.loads(B.current())
                if cur.get("finished"): break
                guard += 1; assert guard < 200, (cid, "loop")
                ex = cur["ex"]; E = B._cur["E"]; raw = B._cur["session"].current; t = ex["type"]
                n_ex += 1
                if t in ("intro", "insight"): ok = None
                else:
                    wrong = random.random() < 0.2
                    if t == "choice": p = {"value": raw["answer"] if not wrong else "zzz"}
                    elif t == "tone": p = {"value": raw["answer"]}
                    elif t == "tone_pair": p = {"value": raw["answer"]}
                    elif t == "build": p = {"tokens": list(raw["answer"]) if not wrong else list(reversed(raw["answer"]))}
                    elif t == "type": p = {"text": raw["answer"] if not wrong else "x"}
                    elif t == "match": p = {}
                    else: p = {}
                    r = json.loads(B.check(json.dumps(p)))
                    ok = r["ok"]
                    if ok == "self": ok = True
                a = json.loads(B.advance(ok))
                if a["out_of_hearts"]: B._cur["state"].data["hearts"] = 5
            ev = json.loads(B.finish())
        for c in h["chats"][:3]:
            ch = json.loads(B.chat_get(c["id"]))
            for i, t in enumerate(ch["turns"]):
                if "build" in t:
                    r = json.loads(B.chat_check(c["id"], i, t["build"]["answer"])); assert r["ok"]
            B.chat_finish(c["id"], 0)
        B.home()
        print(cid, lang, "ok", n_ex, "ex", len(h["units"]), "units", len(h["chats"]), "chats")
