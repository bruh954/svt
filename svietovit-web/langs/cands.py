"""Kandydaci na słownictwo wg częstości: python3 cands.py <cid> [ile] -> /tmp/cand_<cid>.txt (numerowane, bez słów już w kursie).
Potem: napisz /tmp/gl_<cid>.txt z liniami 'N glosa' i uruchom gloss_apply.py <cid> <temat>."""
import importlib.util, os, re, sys
from wordfreq import top_n_list
cid = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
SRC = os.environ.get("SV_SRC", "/home/claude/svietovit")
LANG = {"english": "en", "russian": "ru", "polish": "pl", "serbian": "sh", "han": "zh"}[cid]
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_%s.py" % cid)
if not os.path.exists(path): path = os.path.join(SRC, "courses", cid, "content.py")
sp = importlib.util.spec_from_file_location("c", path); c = importlib.util.module_from_spec(sp); sp.loader.exec_module(c)
strip = lambda s: s.lower().replace("́", "")
have = {strip(w[0]) for u in c.UNITS for w in u.get("words", [])}
# też słowa z pliku vocab (jeszcze nie zastosowane)
vp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vocab", cid + ".txt")
if os.path.exists(vp):
    for line in open(vp, encoding="utf-8"):
        if line.startswith("##"): continue
        for it in re.split(r",\s+(?=[^=,]+=)", line.strip()):
            if "=" in it: have.add(strip(it.split("=", 1)[1].split("~")[0]))
state = os.path.join("/tmp", "cand_done_%s.txt" % cid)
done = set(open(state, encoding="utf-8").read().split("\n")) if os.path.exists(state) else set()
out, seen = [], set()
rx = {"en": r"[a-z]{3,}", "ru": r"[а-яё]{3,}", "pl": r"[a-ząćęłńóśźż]{3,}", "sh": r"[a-zčćđšž]{3,}", "zh": r"[一-鿿]{1,4}"}[LANG]
try:
    import simplemma
    lem = (lambda w: simplemma.lemmatize(w, lang=LANG)) if LANG in ("en", "ru", "pl") else (lambda w: w)
except Exception:
    lem = lambda w: w
allw = top_n_list(LANG, 150000); wset = set(allw)
for w in allw:
    if not re.fullmatch(rx, w): continue
    l = lem(w)
    if l != l.lower() or (LANG in ('en','ru','pl') and l not in wset): continue
    if l in seen or l in have or l in done: continue
    seen.add(l); out.append(l)
    if len(out) >= N: break
open("/tmp/cand_%s.txt" % cid, "w", encoding="utf-8").write("\n".join("%d %s" % (i + 1, w) for i, w in enumerate(out)))
print(len(out), "kandydatów")
