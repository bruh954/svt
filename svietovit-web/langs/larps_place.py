#!/usr/bin/env python3
"""Przenosi linie `w` z góry poziomu tuż przed pierwszą kwestię `t`, w której słowo występuje.
Użycie: python3 larps_place.py <kurs>   (piszesz `w` na początku poziomu, a skrypt ustawia je przy kwestiach)"""
import re, sys
p = "larps/%s.txt" % sys.argv[1]
lines = open(p, encoding="utf-8").read().split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    if not ln.startswith("@level"):
        out.append(ln); i += 1; continue
    out.append(ln); i += 1
    block = []
    while i < len(lines) and not lines[i].startswith(("@level", "@larp")):
        block.append(lines[i]); i += 1
    ws = [l for l in block if l.startswith("w ")]
    ts = [l for l in block if l[:2] in ("t ", "e ")]
    assign = {k: [] for k in range(len(ts))}
    for w in ws:
        word = w[2:].split("|")[0].strip()
        pat = re.compile(r"(?<!\w)" + re.escape(word) + r"(?!\w)", re.I)
        def hit(t):
            f = t[2:].split("|")
            return pat.search(f[0]) or (t[0] == "t" and len(f) > 2 and pat.search(f[2]))
        k = next((k for k, t in enumerate(ts) if hit(t)), 0)
        assign[k].append(w)
    for k, t in enumerate(ts):
        out += assign[k]; out.append(t)
    out.append("")
open(p, "w", encoding="utf-8").write("\n".join(out))
