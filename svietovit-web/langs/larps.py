#!/usr/bin/env python3
"""Larpy z poziomami (lekcja w larpie + scena). Użycie: python3 larps.py <kurs>

Plik larps/<kurs>.txt (puste linie i # ignorowane):
  @larp id | Tytuł | Rozmówca | Awatar | Scena | Cel ucznia
  fee 0 / reward 15 / strict yes / disclaimer … / win … / partial … / fail …        (ustawienia larpa)
  @level 1 | Tytuł poziomu | patience=6 typed=0 extra=1 hint=none reward=10        (typed: ułamek odpowiedzi pisanych z klawiatury,
                                                                                  hint: bank | letters | none, extra: zbędne klocki)
  w Kellner | kelner | der | die Kellner | z czego składa się   nowe słowo (jak w bulk.py); samo „w słowo” = słowo już jest w kursie
  t bot | bot po polsku | odpowiedź ucznia | odpowiedź po polsku | dlaczego (opcjonalnie) | wariant ; wariant
  e bot | bot po polsku                                                              (zakończenie sceny)
Poziom może używać słów z poprzednich poziomów i z kursu. Pisze też plik DO-SPRAWDZENIA-larpy-<kurs>.md.
"""
import os, re, sys
import bulk

HERE = os.path.dirname(os.path.abspath(__file__))
START, END = "# === LARPS: generowane z langs/larps/%s.txt (nie edytuj ręcznie) ===\n", "# === /LARPS ===\n"


def strip(src, cid):
    a = src.find(START % cid)
    if a < 0:
        return src
    b = src.index(END, a) + len(END)
    return src[:a].rstrip("\n") + "\n" + src[b:]


import unicodedata
MISSING = None          # tryb --missing: zbiera nieznane słowa (poziom -> lista)
PLAIN = {}              # forma bez akcentów -> forma z kursu (np. serbskie „dobar” -> „dóbar”)


def _plain(w):
    return "".join(c for c in unicodedata.normalize("NFD", w) if unicodedata.category(c) != "Mn")


def canon(w, known):
    if w in known:
        return w
    c = PLAIN.get(_plain(w))
    return c if c and c in known else w


def tok(text, known, punct):
    t = bulk.tokenize(text, known, punct)
    for i in range(1, len(t)):
        if t[i - 1] in ".!?" and t[i] not in known and t[i].lower() in known:
            t[i] = t[i].lower()
    t = [x if x in punct else canon(x, known) for x in t]
    if MISSING is not None:
        for x in t:
            if x not in known and x not in punct:
                MISSING.append(x); known.add(x)
    return t


def parse(path):
    larps, cur, lv = [], None, None
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("@larp"):
            p = [x.strip() for x in line[5:].split("|")]
            if len(p) != 6:
                raise SystemExit("linia %d: @larp id | tytuł | rozmówca | awatar | scena | cel" % n)
            cur = {"id": p[0], "title": p[1], "partner": p[2], "avatar": p[3], "scene": p[4], "goal": p[5], "fee": 0, "levels": [], "endings": {}}
            larps.append(cur); lv = None
        elif line.startswith("@level"):
            p = [x.strip() for x in line[6:].split("|")]
            lv = {"title": p[1] if len(p) > 1 else "", "n": int(p[0]), "rows": [], "line": n}
            for kv in (p[2].split() if len(p) > 2 else []):
                k, v = kv.split("=", 1); lv[k] = v
            cur["levels"].append(lv)
        elif lv is None and cur is not None:
            k, _, v = line.partition(" ")
            if k in ("win", "partial", "fail"):
                cur["endings"][k] = v.strip()
            elif k in ("fee", "reward"):
                cur[k] = int(v)
            elif k == "strict":
                cur["strict"] = v.strip() in ("yes", "tak", "1")
            elif k in ("disclaimer", "requires"):
                cur[k] = v.strip()
            else:
                raise SystemExit("linia %d: nieznane ustawienie: %s" % (n, line))
        elif lv is not None and line[:2] in ("w ", "t ", "e ", "x "):
            lv["rows"].append((n, line[0], [x.strip() for x in line[2:].split("|")]))
        else:
            raise SystemExit("linia %d: nieznany format: %s" % (n, line))
    return larps


def build(cid):
    path = os.path.join(HERE, "content_%s.py" % cid)
    base = strip(open(path, encoding="utf-8").read(), cid)
    C = bulk.load(path, base)
    punct = set(C.PUNCT) | bulk.OPEN
    known = {w[0] for u in C.UNITS for w in u.get("words", [])}
    PLAIN.clear()
    for k in known:
        PLAIN.setdefault(_plain(k), k)
    seen = {x[1] for u in C.UNITS for x in u.get("sentences", [])}
    seen_tok = {tuple(x[0]) for u in C.UNITS for x in u.get("sentences", [])}
    larps = parse(os.path.join(HERE, "larps", cid + ".txt"))
    errors, units, art, plu, prt, review = [], [], {}, {}, {}, []
    out = []
    for lp in larps:
        levels = []
        review.append("\n## %s (%s)\n\n**Scena:** %s  \n**Cel:** %s  \n**Rozmówca:** %s  \n**Zakończenia:** win: %s · partial: %s · fail: %s  \n" % (
            lp["title"], lp["id"], lp["scene"], lp["goal"], lp["partner"], lp["endings"].get("win"), lp["endings"].get("partial"), lp["endings"].get("fail")))
        for lv in sorted(lp["levels"], key=lambda x: x["n"]):
            words, lex, sents, nodes, order = [], [], [], {}, []
            if MISSING is not None:
                MISSING.append("== poziom %d:" % lv["n"])
            rows = [r for r in lv["rows"] if r[1] in ("t", "e")]
            keys = ["n%d" % i for i in range(len(rows))]
            beat = {"new": [], "pool": [], "sents": []}      # to, co wpisano od poprzedniej kwestii (w, x)
            ri = 0
            for n, kind, p in lv["rows"]:
                if kind == "w":
                    p[0] = canon(p[0], known)
                    if len(p) == 1 or p[0] in known:
                        if p[0] not in known:
                            errors.append("linia %d: „%s” nie ma w kursie (podaj znaczenie)" % (n, p[0]))
                        beat["pool"].append(p[0]); lex.append(p[0]); continue
                    known.add(p[0]); beat["new"].append((p[0], p[1], None, None)); beat["pool"].append(p[0]); lex.append(p[0])
                    if len(p) > 2 and p[2]: art[p[0]] = p[2]
                    if len(p) > 3 and p[3]: plu[p[0]] = p[3]
                    if len(p) > 4 and p[4]: prt[p[0]] = p[4]
                    continue
                if kind == "x":
                    if len(p) < 2:
                        errors.append("linia %d: x zdanie | tłumaczenie" % n); continue
                    xt = tok(p[0], known, punct)
                    badx = [t for t in xt if t not in known and t not in punct]
                    if badx:
                        errors.append("linia %d: nieznane słowa %s w: %s" % (n, badx, p[0])); continue
                    beat["sents"].append((xt, p[1], {})); continue
                i = ri; ri += 1
                need = 2 if kind == "e" else 4
                if len(p) < need:
                    errors.append("linia %d: za mało pól" % n); continue
                bt = tok(p[0], known, punct)
                bad = [t for t in bt if t not in known and t not in punct]
                if bad:
                    errors.append("linia %d: nieznane słowa %s w: %s" % (n, bad, p[0])); continue
                node = {"bot": bt, "pl": p[1]}
                key = keys[i]
                bsents = list(beat["sents"])
                if kind == "e":
                    node["end"] = True
                else:
                    at = tok(p[2], known, punct)
                    bad = [t for t in at if t not in known and t not in punct]
                    if bad:
                        errors.append("linia %d: nieznane słowa %s w odpowiedzi: %s" % (n, bad, p[2])); continue
                    node["build"] = (at, p[3])
                    node["next"] = keys[i + 1] if i + 1 < len(keys) else None
                    if len(p) > 4 and p[4]:
                        node["why"] = p[4]
                    alts = []
                    for a_ in (p[5].split(";") if len(p) > 5 and p[5] else []):
                        ta = tok(a_.strip(), known, punct)
                        badt = [t for t in ta if t not in known and t not in punct]
                        if badt:
                            errors.append("linia %d: nieznane słowa %s w wariancie: %s" % (n, badt, a_)); continue
                        alts.append(ta)
                    if alts:
                        node["alts"] = alts
                    bsents += [(at, p[3], {})]
                if kind == "t":
                    bsents += [(bt, p[1], {})]
                uniq = []
                for tk, pl, tr in bsents:
                    if pl not in seen and tuple(tk) not in seen_tok:
                        seen.add(pl); seen_tok.add(tuple(tk)); uniq.append((tk, pl, tr))
                if kind == "t" and not beat["pool"]:       # kwestia bez nowych słów: ćwiczymy słowa z odpowiedzi
                    beat["pool"] = list(dict.fromkeys(t for t in at if t not in punct and len(t) > 2))
                if beat["pool"] and (kind == "t" or beat["new"]):
                    uid = "lp_%s_%d_%d" % (lp["id"], lv["n"], i + 1)
                    units.append({"id": uid, "title": "%s · poziom %d · kwestia %d" % (lp["title"], lv["n"], i + 1), "icon": "🎭", "track": "jezyk", "hidden": True,
                                  "words": beat["new"], "sentences": uniq})
                    if kind == "t":
                        node["unit"] = uid
                        node["pool"] = list(beat["pool"])
                words += beat["new"]; sents += uniq
                beat = {"new": [], "pool": [], "sents": []}
                nodes[key] = node; order.append(key)
            if not order or not nodes[order[-1]].get("end"):
                errors.append("poziom %d larpa %s: ostatni wiersz musi być „e” (zakończenie)" % (lv["n"], lp["id"]))
            cfg = {"title": lv["title"], "start": order[0] if order else None, "nodes": nodes, "lexicon": lex,
                   "patience": int(lv.get("patience", 5)), "typed": float(lv.get("typed", 0)), "extra": int(lv.get("extra", 3))}
            cfg["lexicon"] = []
            if lv.get("hint", "none") != "none":
                cfg["hint"] = lv["hint"]
            if lv.get("reward"):
                cfg["reward"] = int(lv["reward"])
            levels.append(cfg)
            review.append("\n### Poziom %d: %s  (typed=%s, hint=%s, cierpliwość %s)\n\nNowe słowa: %s\n\n| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |\n|---|---|---|---|\n" % (
                lv["n"], lv["title"], lv.get("typed", 0), lv.get("hint", "none"), lv.get("patience", 5),
                ", ".join("%s = %s" % (w[0], w[1]) for w in words) or "(brak)"))
            rows = [r for r in rows if r[1] in ("t", "e")]
            for i, (n, kind, p) in enumerate(rows, 1):
                review.append("| %d | %s *(%s)* | %s | %s |\n" % (i, p[0], p[1], ("**" + p[2] + "** *(" + p[3] + ")*" + (" · warianty: " + p[5] if len(p) > 5 and p[5] else "")) if kind == "t" else "—", (p[4] if len(p) > 4 and kind == "t" else "") or ""))
        lp2 = {k: v for k, v in lp.items() if k != "levels"}
        lp2["levels"] = levels
        lp2["scene"], lp2["goal"] = lp["scene"], lp["goal"]
        lp2["patience"] = levels[0]["patience"] if levels else 5
        out.append(lp2)
    return base, units, art, plu, prt, out, errors, review


def write(cid):
    base, units, art, plu, prt, larps, errors, review = build(cid)
    if errors:
        print("\n".join(errors[:60])); print("błędów: %d (nic nie zapisano)" % len(errors)); sys.exit(1)
    block = START % cid + "UNITS += %r\n" % (units,)
    if art: block += "ARTICLES.update(%r)\n" % (art,)
    if plu: block += "PLURALS.update(%r)\n" % (plu,)
    if prt: block += "PARTS.update(%r)\n" % (prt,)
    block += "LARPS.extend(%r)\n" % (larps,) + END
    i = base.find(bulk.GRAM)
    out = (base[:i].rstrip("\n") + "\n\n" + block + base[i:]) if i >= 0 else base.rstrip("\n") + "\n\n" + block
    open(os.path.join(HERE, "content_%s.py" % cid), "w", encoding="utf-8").write(out)
    rp = os.path.join(HERE, "larps", "DO-SPRAWDZENIA-%s.md" % cid)
    open(rp, "w", encoding="utf-8").write("# Larpy (%s): do sprawdzenia przez natywnego speakera\n\nSprawdź naturalność, formę grzecznościową, pisownię i czy wyjaśnienia są prawdziwe. "
        "Wszystko napisane z głowy przez AI. Poprawki wpisz w tabelę albo komentarzem.\n" % cid + "".join(review))
    print("%s: %d larpów, %d poziomów, %d słów; raport: %s" % (cid, len(larps), sum(len(l["levels"]) for l in larps), sum(len(u["words"]) for u in units), rp))


if __name__ == "__main__":
    if "--missing" in sys.argv:
        MISSING = []
        r = build(sys.argv[1])
        print("\n".join(r[6])); print(" ".join(MISSING).replace(" == ", "\n== ")); sys.exit(0)
    write(sys.argv[1])
