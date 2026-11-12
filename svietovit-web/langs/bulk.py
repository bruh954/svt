#!/usr/bin/env python3
"""Rozbudowa słownictwa z list frekwencyjnych.

  python3 bulk.py <kurs>            wczytuje bulk/<kurs>.txt i wstawia działy do content_<kurs>.py
  python3 bulk.py <kurs> --report   ile razy każde słowo pada w zdaniach (cel: 7)
  python3 bulk.py <kurs> --freq 500 najczęstsze słowa, których jeszcze nie ma w kursie

Format pliku bulk/<kurs>.txt (puste linie i # ignorowane):
  == Tytuł działu | ikona
  w Haus | dom | das | die Häuser     słowo | znaczenie | (rodzajnik) | (liczba mnoga, tylko niemiecki)
  s Ich habe ein Haus. | Mam dom.     zdanie | tłumaczenie
Zdanie może używać tylko słów z wcześniejszych działów i z własnego działu.
Każda forma fleksyjna to osobne słowo (habe, hast, hat).
"""
import importlib.util, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
START, END = "# === BULK: generowane z langs/bulk/%s.txt (nie edytuj ręcznie) ===\n", "# === /BULK ===\n"
GRAM = "\n# ---------------------------------------------------------------------------\n# Gramatyka"
FREQ = {"german": "de", "french": "fr", "italian": "it", "spanish": "es", "russian": "ru", "turkish": "tr", "finnish": "fi",
        "czech": "cs", "slovak": "sk", "greek": "el", "serbian": "sh"}
OPEN = {"¿", "¡"}


def strip_block(src, cid):
    a = src.find(START % cid)
    if a < 0:
        return src
    b = src.index(END, a) + len(END)
    return src[:a].rstrip("\n") + "\n" + src[b:]


def load(path, src):
    import tempfile
    d = tempfile.mkdtemp()
    p = os.path.join(d, "c.py")
    open(p, "w", encoding="utf-8").write(src)
    spec = importlib.util.spec_from_file_location("bulk_c", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def parse(path):
    secs = []
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("=="):
            parts = [x.strip() for x in line[2:].split("|")]
            secs.append({"title": parts[0], "icon": (parts[1] if len(parts) > 1 else parts[0][:1]), "w": [], "s": []})
        elif line[:2] in ("w ", "s ") and secs:
            parts = [x.strip() for x in line[2:].split("|")]
            if len(parts) < 2 or not parts[0] or not parts[1]:
                raise SystemExit("linia %d: brak znaczenia/tłumaczenia: %s" % (n, line))
            secs[-1][line[0]].append((n, parts))
        else:
            raise SystemExit("linia %d: nieznany format: %s" % (n, line))
    return secs


def tokenize(text, known, punct):
    toks = []
    for raw in text.split():
        pre, post = [], []
        while raw and raw[0] in OPEN:
            pre.append(raw[0]); raw = raw[1:]
        while raw and raw[-1] in punct:
            post.insert(0, raw[-1]); raw = raw[:-1]
        toks += pre + ([raw] if raw else []) + post
    for i, t in enumerate(toks):                       # początek zdania: wielka litera to nie część słowa
        if t not in known and t.lower() in known and (i == 0 or toks[i - 1] in OPEN):
            toks[i] = t.lower()
        elif t not in known and t[:1].isupper() is False and t.capitalize() in known:
            toks[i] = t.capitalize()
    return toks


def build(cid):
    path = os.path.join(HERE, "content_%s.py" % cid)
    src = open(path, encoding="utf-8").read()
    base = strip_block(src, cid)
    C = load(path, base)
    punct = set(C.PUNCT) | OPEN
    known = {w[0] for u in C.UNITS for w in u.get("words", [])}
    existing = set(known)
    secs = parse(os.path.join(HERE, "bulk", cid + ".txt"))
    units, art, plu, errors = [], {}, {}, []
    for i, sec in enumerate(secs, 1):
        words = []
        for n, p in sec["w"]:
            if p[0] in existing:
                errors.append("linia %d: słowo „%s” już jest w kursie" % (n, p[0])); continue
            existing.add(p[0]); words.append((p[0], p[1], None, None))
            if len(p) > 2 and p[2]:
                art[p[0]] = p[2]
            if len(p) > 3 and p[3]:
                plu[p[0]] = p[3]
        known |= {w[0] for w in words}
        sents = []
        for n, p in sec["s"]:
            toks = tokenize(p[0], known, punct)
            bad = [t for t in toks if t not in known and t not in punct]
            if bad:
                errors.append("linia %d: nieznane słowa %s w: %s" % (n, bad, p[0])); continue
            sents.append((toks, p[1], {}))
        units.append({"id": "f%02d" % i, "title": sec["title"], "icon": sec["icon"], "track": "jezyk", "words": words, "sentences": sents})
    return src, base, units, art, plu, errors, C


def write(cid):
    src, base, units, art, plu, errors, C = build(cid)
    if errors:
        print("\n".join(errors[:60])); print("błędów: %d (nic nie zapisano)" % len(errors)); sys.exit(1)
    block = START % cid + "UNITS += %r\n" % (units,)
    if art:
        block += "ARTICLES.update(%r)\n" % (art,)
    if plu:
        block += "PLURALS.update(%r)\n" % (plu,)
    block += END
    i = base.find(GRAM)
    out = (base[:i].rstrip("\n") + "\n\n" + block + base[i:]) if i >= 0 else base.rstrip("\n") + "\n\n" + block
    open(os.path.join(HERE, "content_%s.py" % cid), "w", encoding="utf-8").write(out)
    nw = sum(len(u["words"]) for u in units); ns = sum(len(u["sentences"]) for u in units)
    print("%s: +%d działów, +%d słów, +%d zdań" % (cid, len(units), nw, ns))


def report(cid, goal=7):
    path = os.path.join(HERE, "content_%s.py" % cid)
    C = load(path, open(path, encoding="utf-8").read())
    words = [w[0] for u in C.UNITS for w in u.get("words", [])]
    cnt = Counter(t for u in C.UNITS for s in u.get("sentences", []) for t in s[0])
    low = [(w, cnt[w]) for w in words if cnt[w] < goal]
    print("%s: %d słów, %d zdań, słów z ≥%d użyciami w zdaniach: %d (%d%%)" % (
        cid, len(words), sum(len(u.get("sentences", [])) for u in C.UNITS), goal, len(words) - len(low), 100 * (len(words) - len(low)) // max(1, len(words))))
    print("za mało użyć:", ", ".join("%s(%d)" % x for x in sorted(low, key=lambda x: x[1])[:80]))


def freq(cid, n):
    from wordfreq import top_n_list
    path = os.path.join(HERE, "content_%s.py" % cid)
    C = load(path, open(path, encoding="utf-8").read())
    known = {w[0].lower() for u in C.UNITS for w in u.get("words", [])}
    out = [w for w in top_n_list(FREQ[cid], n) if w.isalpha() and w not in known]
    print("%d z %d najczęstszych słów jeszcze nie ma w kursie:" % (len(out), n)); print(" ".join(out))


if __name__ == "__main__":
    cid = sys.argv[1]
    if "--report" in sys.argv:
        report(cid)
    elif "--freq" in sys.argv:
        freq(cid, int(sys.argv[sys.argv.index("--freq") + 1]))
    else:
        write(cid)
