"""Scala /tmp/cand_<cid>.txt z /tmp/gl_<cid>.txt ('N glosa' lub 'N glosa~tag') do vocab/<cid>.txt jako nowy dział."""
import os, re, sys
cid, theme = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
cand = {}
for line in open("/tmp/cand_%s.txt" % cid, encoding="utf-8"):
    n, w = line.rstrip("\n").split(" ", 1); cand[int(n)] = w
pairs, used = [], []
for line in open("/tmp/gl_%s.txt" % cid, encoding="utf-8"):
    line = line.strip()
    if not line: continue
    m = re.match(r"(\d+)\s+(.+)$", line)
    if not m or int(m.group(1)) not in cand: print("?", line); continue
    n = int(m.group(1)); g = m.group(2).strip(); tag = ""
    if "~" in g: g, tag = g.split("~", 1)
    g = g.replace("=", "").replace(", ", "; ")
    pairs.append("%s=%s%s" % (g, cand[n], ("~" + tag) if tag else "")); used.append(n)
# wszystkie pokazane kandydaty uznajemy za przetworzone (pominięte = świadomie odrzucone)
with open("/tmp/cand_done_%s.txt" % cid, "a", encoding="utf-8") as f:
    for n, w in cand.items():
        if n <= max(used): f.write(w + "\n")
vp = os.path.join(HERE, "vocab", cid + ".txt")
with open(vp, "a", encoding="utf-8") as f:
    f.write("## %s\n%s\n" % (theme, ", ".join(pairs)))
print("dopisano", len(pairs), "z", len(cand))
