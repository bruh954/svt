"""Kandydaci zh/ja z angielskimi glosami: python3 cands_cjk.py han|nihon [ile] -> /tmp/cand_<cid>.txt (N słowo) + /tmp/show_<cid>.txt (N słowo | angielski)."""
import importlib.util, os, pickle, re, sys
from wordfreq import top_n_list
cid = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
SRC = os.environ.get("SV_SRC", "/home/claude/svietovit")
HERE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(HERE, "content_%s.py" % cid)
if not os.path.exists(path): path = os.path.join(SRC, "courses", cid, "content.py")
sp = importlib.util.spec_from_file_location("c", path); c = importlib.util.module_from_spec(sp); sp.loader.exec_module(c)
have = {w[0] for u in c.UNITS for w in u.get("words", [])}
vp = os.path.join(HERE, "vocab", cid + ".txt")
if os.path.exists(vp):
    for line in open(vp, encoding="utf-8"):
        if line.startswith("##"): continue
        for it in re.split(r",\s+(?=[^=,]+=)", line.strip()):
            if "=" in it: have.add(it.split("=", 1)[1].split("~")[0].strip())
state = "/tmp/cand_done_%s.txt" % cid
done = set(open(state, encoding="utf-8").read().split("\n")) if os.path.exists(state) else set()
out = []
if cid == "han":
    import cedict_utils, cedict_utils.cedict as cd
    lines = pickle.load(open(cd.DATA_PATH, "rb"))
    D = {}
    for l in lines:
        m = re.match(r"(\S+) (\S+) \[([^\]]*)\] /(.*)/", l.strip())
        if not m: continue
        trad, simp, py, defs = m.groups()
        g = [x for x in defs.split("/") if not x.startswith(("CL:", "see ", "variant of", "old variant", "surname", "abbr. for", "also written"))]
        if not g or any(x.startswith("(Tw)") for x in g[:1]): continue
        D.setdefault(simp, []).append(g[0])
    seen = set()
    for w in top_n_list("zh", 60000):
        if not re.fullmatch(r"[一-鿿]{1,4}", w) or w in have or w in done or w in seen or w not in D: continue
        g = D[w][0]
        if re.search(r"\b(surname|Kingdom|Dynasty|County|Province|District|City)\b", g) or g[0].isupper() and len(g) < 25 and " " not in g and False: continue
        seen.add(w); out.append((w, "; ".join(D[w][:2])[:60]))
        if len(out) >= N: break
else:
    from jamdict import Jamdict
    j = Jamdict(); seen = set()
    GOOD = {"news1", "news2", "ichi1", "ichi2", "spec1", "spec2", "gai1", "gai2"}
    for w in top_n_list("ja", 80000):
        if w in have or w in done or w in seen or not re.fullmatch(r"[぀-ヿ一-鿿ー]{2,6}", w): continue
        if re.fullmatch(r"[぀-ゟ]+", w): continue   # same hiragana: pomijamy (partykuły, końcówki)
        r = j.lookup(w, strict_lookup=True)
        if not r.entries: continue
        e = r.entries[0]
        pri = {p for k in e.kanji_forms for p in k.pri} | {p for k in e.kana_forms for p in k.pri}
        if not (pri & GOOD): continue
        pos = " ".join(sorted({p for s in e.senses[:1] for p in s.pos}))
        if "proper noun" in pos or "prefix" in pos or "suffix" in pos or "counter" in pos: continue
        g = "; ".join(x.text for x in e.senses[0].gloss[:2])[:60]
        seen.add(w); out.append((w, g))
        if len(out) >= N: break
open("/tmp/cand_%s.txt" % cid, "w", encoding="utf-8").write("\n".join("%d %s" % (i + 1, w) for i, (w, g) in enumerate(out)))
open("/tmp/show_%s.txt" % cid, "w", encoding="utf-8").write("\n".join("%d %s | %s" % (i + 1, w, g) for i, (w, g) in enumerate(out)))
print(len(out), "kandydatów")
