import importlib.util, sys
def load(cid):
    sys.path.insert(0, "/home/claude/svietovit"); sys.modules.pop("courses.%s.engine" % cid, None)
    return importlib.import_module("courses.%s.engine" % cid), importlib.import_module("courses.%s.content" % cid)
def check(cid):
    E, C = load(cid); W = E.WORDS; errs = []
    def ok(t): return t in W or t in C.PUNCT or t in E.OPEN_PUNCT
    seen = set()
    for ui, u in enumerate(E.UNITS):
        known = {h for h in W if W[h]["unit"] <= ui}
        for toks, pl, traps in u.get("sentences", []):
            for t in toks:
                if not ok(t): errs.append("zdanie %s: brak '%s'" % (u["id"], t))
                elif t in W and W[t]["unit"] > ui: errs.append("zdanie %s: '%s' z późniejszego działu" % (u["id"], t))
            if tuple(toks) in seen: errs.append("zdanie podwójne " + pl)
            seen.add(tuple(toks))
            for tr in traps:
                if tr in toks: errs.append("pułapka %s jest w odpowiedzi (%s)" % (tr, pl))
        for ins in C.INSIGHTS.get(u["id"], []):
            for pl, toks, hint in ins["chain"]:
                for t in toks:
                    if not ok(t): errs.append("wgląd %s: brak '%s'" % (u["id"], t))
    uids = {u["id"] for u in E.UNITS}
    for e in C.ENDINGS:
        if len(e) != 8 or e[7] not in uids or e[2] not in e[4]: errs.append("końcówka błędna: %r" % (e,))
    for c in C.CHATS:
        if c["requires"] not in uids: errs.append("czat requires " + c["id"])
        for t in c["turns"]:
            toks = list(t["bot"]) + [x for o in t.get("options", []) for x in o[0]] + (list(t["build"][0]) if "build" in t else [])
            for x in toks:
                if not (ok(x) or x in C.CHAT_EXTRA): errs.append("czat %s: brak '%s'" % (c["id"], x))
            if "options" in t and sum(1 for o in t["options"] if o[1]) != 1: errs.append("czat %s: nie 1 poprawna" % c["id"])
            if "options" in t:
                for o in t["options"]:
                    if not o[1] and not o[2]: errs.append("czat %s: brak wyjaśnienia" % c["id"])
    for u in E.UNITS:
        if u.get("requires") and u["requires"] not in uids: errs.append("requires " + u["id"])
    # sprawdz brak duplikatow opisow liter
    pls = [w["pl"] for w in W.values() if w["letter"]]
    if len(pls) != len(set(pls)): errs.append("powtórzone opisy liter")
    print(cid, len(W), "słów", sum(len(u.get("sentences", [])) for u in E.UNITS), "zdań", len(C.ENDINGS), "końcówek", len(C.CHATS), "czatów")
    for e in errs: print("  BŁĄD", e)
    return errs
if __name__ == "__main__":
    for c in sys.argv[1:]: check(c)
