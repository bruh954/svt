"""Hurtowe słownictwo: langs/vocab/<cid>.txt -> blok VOCAB w langs/content_<cid>.py.
Format pliku: '## Temat' i pary 'znaczenie=forma' oddzielone ', ' (opcjonalnie 'forma~dodatek':
rodzajnik dla niemieckiego, zapis wymowy dla kursów z MODE=ipa). Użycie: python3 vocab_apply.py <cid> [...]"""
import importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
START = "# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===\n"; END = "# === /SŁOWNICTWO ===\n"
CHUNK = 16
TRACK = {"han": "znaki", "nihon": "start", "kana": "kanji"}
COURSES = os.environ.get("SV_SRC", "/home/claude/svietovit")
M1 = "# === CZYTANIA (generowane) ===\n"; M2 = "# === /CZYTANIA ===\n"

def _strip(src, a_m, b_m):
    a = src.find(a_m)
    if a >= 0:
        src = src[:a].rstrip("\n") + "\n" + src[src.index(b_m, a) + len(b_m):]
    return src

JP_FIX = {'人': 'ひと', '月': 'つき', '日': 'ひ', '瓶': 'びん', '檻': 'おり', '漆': 'うるし'}

def readings_jp(units):
    import pykakasi
    kks = pykakasi.kakasi(); out = {}
    for u in units:
        for w in u["words"]:
            f = w[0]
            if any("\u4e00" <= ch <= "\u9fff" for ch in f):
                out[f] = "".join(x["hira"] for x in kks.convert(f))
    out.update({k: v for k, v in JP_FIX.items() if k in out})
    return out

def pinyin_zh(units):
    from pypinyin import lazy_pinyin, Style
    out = {}
    for u in units:
        for w in u["words"]:
            f = w[0]
            out[f] = " ".join(lazy_pinyin(f, style=Style.TONE3, neutral_tone_with_five=True))
    return out

def parse(path):
    blocks, cur = [], None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#!"):
            continue
        if line.startswith("## "):
            cur = (line[3:].strip(), []); blocks.append(cur); continue
        for pair in re.split(r",\s+(?=[^=,]+=)", line):
            if "=" not in pair:
                print("  ? bez '=':", pair); continue
            g, f = pair.split("=", 1)
            extra = None
            if "~" in f:
                f, extra = f.split("~", 1)
            cur[1].append((g.strip(), f.strip(), (extra or "").strip()))
    return blocks

def run(cid):
    path = os.path.join(HERE, "content_%s.py" % cid)
    if not os.path.exists(path):
        path = os.path.join(os.environ.get("SV_SRC", "/home/claude/svietovit"), "courses", cid, "content.py")
    vp = os.path.join(HERE, "vocab", "%s.txt" % cid)
    src = open(path, encoding="utf-8").read()
    a = src.find(START)
    if a >= 0:
        src = src[:a].rstrip("\n") + "\n" + src[src.index(END, a) + len(END):]
    open("/tmp/_v.py", "w", encoding="utf-8").write(src)
    sp = importlib.util.spec_from_file_location("c", "/tmp/_v.py"); c = importlib.util.module_from_spec(sp); sp.loader.exec_module(c)
    have = set()
    for u in c.UNITS:
        for w in u.get("words", []):
            have.add(w[0])
    ipa = cid in ("norse", "thai", "polish")
    units, arts, total, skipped = [], {}, 0, 0
    for bi, (title, pairs) in enumerate(parse(vp), 1):
        keep = []
        for g, f, x in pairs:
            if f in have:
                skipped += 1; continue
            have.add(f); keep.append((g, f, x))
        for k in range(0, len(keep), CHUNK):
            part = keep[k:k + CHUNK]; n = k // CHUNK + 1
            words = []
            for g, f, x in part:
                if cid == "german" and x:
                    arts[f] = x; x = ""
                hook = {"m": "rodzaj męski", "f": "rodzaj żeński", "n": "rodzaj nijaki"}.get(x) if not ipa else None
                words.append((f, g, None, hook, x) if ipa else (f, g, None, hook))
            units.append({"id": "v%02d%s" % (bi, "abcdefghij"[n - 1]), "title": title + (" %d" % n if len(keep) > CHUNK else ""),
                          "icon": title[0], "track": TRACK.get(cid, "jezyk"), "words": words, "sentences": []})
            total += len(words)
    block = START + "UNITS += %r\n" % (units,)
    if arts:
        block += "ARTICLES.update(%r)\n" % (arts,)
    block += END
    src = _strip(src, M1, M2)
    if cid in ("kana", "nihon"):
        block += M1 + "READINGS.update(%r)\n" % (readings_jp(units),) + M2
    open(path, "w", encoding="utf-8").write(src.rstrip("\n") + "\n\n" + block)
    if cid == "han":
        pp = os.path.join(COURSES, "courses", "han", "pinyin_data.py")
        ps = _strip(open(pp, encoding="utf-8").read(), M1, M2)
        open(pp, "w", encoding="utf-8").write(ps.rstrip("\n") + "\n\n" + M1 + "PINYIN.update(%r)\n" % (pinyin_zh(units),) + M2)
    print(cid, total, "słów w", len(units), "działach; pominięte duplikaty:", skipped)

for cid in sys.argv[1:]:
    run(cid)
