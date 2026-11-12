"""Generuje courses/<id>/engine.py (+ __init__.py) dla nowych kursów językowych na bazie silnika łaciny.
Użycie: python3 make.py   (treść: content_<id>.py w tym folderze -> courses/<id>/content.py)"""
import os, re, shutil, sys
SRC = os.environ.get("SV_SRC", "/home/claude/svietovit")
HERE = os.path.dirname(os.path.abspath(__file__))
AVE = open(os.path.join(SRC, "courses", "ave", "engine.py"), encoding="utf-8").read()

MODE = {"norse": "ipa"}   # pozostałe: bez zapisu wymowy (są syntezatory mowy)

LANGS = {
    # id: (nazwa po polsku w bierniku "na ...", "po ...", extra plain map, wielka litera na początku zdania)
    "greek":   ("na nowogrecki", "po grecku", {}, True),
    "german":  ("na niemiecki", "po niemiecku", {"ß": "ss"}, True),
    "french":  ("na francuski", "po francusku", {"œ": "oe", "æ": "ae"}, True),
    "italian": ("na włoski", "po włosku", {}, True),
    "spanish": ("na hiszpański", "po hiszpańsku", {"ñ": "n"}, True),
    "russian": ("na rosyjski", "po rosyjsku", {"ё": "е"}, True),
    "turkish": ("na turecki", "po turecku", {"ı": "i", "İ": "i", "ş": "s", "ğ": "g", "ç": "c", "ö": "o", "ü": "u"}, True),
    "estonian": ("na estoński", "po estońsku", {"õ": "o", "ä": "a", "ö": "o", "ü": "u", "š": "s", "ž": "z"}, True),
    "serbian": ("na serbski", "po serbsku", dict({"đ": "d", "Đ": "d", "ђ": "d", "љ": "lj", "њ": "nj", "џ": "dz", "ћ": "c", "ч": "c", "ш": "s", "ж": "z",
                 "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "з": "z", "и": "i", "ј": "j", "к": "k", "л": "l", "м": "m", "н": "n",
                 "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c"}), True),
    "finnish": ("na fiński", "po fińsku", {"å": "a"}, True),
    "czech":   ("na czeski", "po czesku", {}, True),
    "slovak":  ("na słowacki", "po słowacku", {}, True),
    "norse":   ("na staronordycki", "po staronordycku", {"þ": "th", "ð": "d", "æ": "ae", "ø": "o", "ǫ": "o", "œ": "oe"}, True),
}

LANGS["serbian"][2].update({k.upper(): v for k, v in list(LANGS["serbian"][2].items()) if k.upper() != k})

PRON_BLOCK = '''import unicodedata
_SPECIAL = %(special)r
CAP_FIRST = %(cap)r
OPEN_PUNCT = {"¿", "¡"}
GLAGOLITIC = set()


def plain(text):
    """Bez znaków diakrytycznych i wielkości liter (do porównywania wpisanych odpowiedzi)."""
    out = "".join(_SPECIAL.get(c, c) for c in text)
    out = unicodedata.normalize("NFD", out)
    return "".join(c for c in out if unicodedata.category(c) != "Mn")


def pron(text, style=None):
    return text


def translit(text):
    return WORDS[text]["tr"] if text in WORDS else text


def check_typed(text, answer):
    """'correct' (znaki diakrytyczne są nieobowiązkowe) albo 'wrong'."""
    a = " ".join(plain(text).lower().split())
    b = plain(answer).lower()
    return "correct" if a == b else "wrong"
'''

def build(cid):
    acc, po, special, cap = LANGS[cid]
    s = AVE
    s = s.replace('"""Logika kursu łaciny:', '"""Logika kursu (%s):' % cid)
    a = s.index("_PLAIN = str.maketrans"); b = s.index("# ---------------------------------------------------------------------------\n# Słowa")
    s = s[:a] + PRON_BLOCK % {"special": special, "cap": cap} + "\n\n" + s[b:]
    # słowa
    s = s.replace('''    for _l, _pl, _ex in _u.get("letters", []):''', '''    for _l, _pl, _ex, *_lt in _u.get("letters", []):''')
    s = s.replace('''"hook": "Przykład: %s, czytaj „%s”." % (_ex, pron(_ex)), "unit": _ui,''', '''"hook": "Przykład: %s." % _ex, "unit": _ui,''')
    s = s.replace('''    for _f, _pl, _cog, _hook in _u.get("words", []):''', '''    for _f, _pl, _cog, _hook, *_t in _u.get("words", []):''')
    s = s.replace('''"form": _f, "tr": pron(_f), "pl": _pl,''', '''"form": _f, "tr": (_t[0] if _t and _t[0] else _f), "pl": _pl,''')
    # join z wielką literą i znakami otwierającymi
    a = s.index("def join(tokens):"); b = s.index("def sentence_tr")
    s = s[:a] + '''def _cap(c):
    return "İ" if (c == "i" and %r) else c.upper()


def join(tokens):
    out = ""
    for t in tokens:
        if t in PUNCT:
            out += t
        elif out.endswith(tuple(OPEN_PUNCT)):
            out += t
        else:
            out += (" " if out else "") + t
    if CAP_FIRST:
        for i, c in enumerate(out):
            if c.isalpha():
                out = out[:i] + _cap(c) + out[i + 1:]
                break
    return out


''' % (cid == "turkish") + s[b:]
    s = s.replace('''    return join([t if t in PUNCT else translit(t) for t in tokens])''', '''    return join([t if (t in PUNCT or t in OPEN_PUNCT) else translit(t) for t in tokens])''')
    s = s.replace("    if t in PUNCT:\n        return None\n    return translit(t)", "    if t in PUNCT or t in OPEN_PUNCT:\n        return None\n    return translit(t)")
    # reading
    a = s.index("    def reading(self, h, pool=None):"); b = s.index("    def cognate(self")
    s = s[:a] + '''    def reading(self, h, pool=None):
        """Jak to się czyta? Pułapką jest czytanie jak po polsku."""
        w = WORDS[h]
        right = w["tr"]
        opts = []
        naive = plain(w["form"]).lower()
        if naive and naive != right:
            opts.append(naive)
        for o in self._distract(h, 3, lambda x: x["tr"], pool, avoid=set(opts) | {right}):
            if len(opts) == 3:
                break
            opts.append(WORDS[o]["tr"])
        return {"type": "choice", "mode": "reading", "word": h, "title": "Jak to się czyta?",
                "prompt": w["form"], "options": self._options(right, opts[:3]), "answer": right,
                "solution": "%s czytaj „%s” (%s)" % (w["form"], right, w["pl"])}

''' + s[b:]
    s = s.replace('"Przetłumacz na łacinę"', '"Przetłumacz %s"' % acc).replace('"Napisz po łacinie"', '"Napisz %s"' % po)
    s = s.replace('"polskie słowo z łaciny: %s" % w["cog"]', '"podobne polskie słowo: %s" % w["cog"]')
    s = s.replace('drills = [e for e in ENDINGS if e[7] in open_units] or [e for e in ENDINGS if e[7] == "slowa"]', 'drills = [e for e in ENDINGS if e[7] in open_units] or list(ENDINGS)')
    if MODE.get(cid, "none") == "none":
        for a, b in [
            ('"tr": (_t[0] if _t and _t[0] else _f)', '"tr": ""'),
            ("    if t in PUNCT or t in OPEN_PUNCT:\n        return None\n    return translit(t)", "    return None"),
            ("    return join([t if (t in PUNCT or t in OPEN_PUNCT) else translit(t) for t in tokens])", "    return \"\""),
            ('"solution": join(tokens) + "\\n" + sentence_tr(tokens)}', '"solution": join(tokens)}'),
            ('"solution": "%s (%s): %s" % (w["form"], w["tr"], w["pl"])}', '"solution": "%s: %s" % (w["form"], w["pl"])}'),
            ('"solution": "%s (%s)" % (w["form"], w["tr"])}', '"solution": w["form"]}'),
            ('"reading": 2 if vocab else 0,', '"reading": 0,'),
        ]:
            assert a in s, a
            s = s.replace(a, b)
    else:  # IPA: bez zapisu "naiwnego" czytania i bez wielkiej litery w transkrypcji zdania
        a = '        if naive and naive != right:\n            opts.append(naive)\n'
        assert a in s
        s = s.replace(a, "")
        a = "    return join([t if (t in PUNCT or t in OPEN_PUNCT) else translit(t) for t in tokens])"
        assert a in s
        s = s.replace(a, '    return " ".join(translit(t) for t in tokens if not (t in PUNCT or t in OPEN_PUNCT))')
    # rodzajniki: w ćwiczeniach na słowa rzeczownik pokazujemy zawsze z rodzajnikiem (ARTICLES w treści)
    a = "def token_tr(t):"
    assert a in s
    s = s.replace(a, '''try:
    from .content import ARTICLES
except ImportError:
    ARTICLES = {}
try:
    from .content import PLURALS
except ImportError:
    PLURALS = {}
for _f, _a in ARTICLES.items():
    if _f in WORDS:
        WORDS[_f]["form"] = _a + " " + _f + (", " + PLURALS[_f] if _f in PLURALS else "")


def token_tr(t):''', 1)
    assert "łacin" not in s.lower().replace("łaciny:", ""), [m.start() for m in re.finditer("łacin", s)]
    return s

def main():
    for cid in LANGS:
        src_content = os.path.join(HERE, "content_%s.py" % cid)
        if not os.path.exists(src_content):
            continue
        d = os.path.join(SRC, "courses", cid)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "__init__.py"), "w").close()
        open(os.path.join(d, "engine.py"), "w", encoding="utf-8").write(build(cid))
        shutil.copy(src_content, os.path.join(d, "content.py"))
        print("ok", cid)


# ---------------------------------------------------------------------------
# Serbski: druga wersja treści w cyrylicy (ta sama nauka, inne pismo)
# ---------------------------------------------------------------------------
_SR = [("lj", "љ"), ("nj", "њ"), ("dž", "џ"), ("a", "а"), ("b", "б"), ("v", "в"), ("g", "г"), ("d", "д"), ("đ", "ђ"),
       ("e", "е"), ("ž", "ж"), ("z", "з"), ("i", "и"), ("j", "ј"), ("k", "к"), ("l", "л"), ("m", "м"), ("n", "н"),
       ("o", "о"), ("p", "п"), ("r", "р"), ("s", "с"), ("t", "т"), ("ć", "ћ"), ("u", "у"), ("f", "ф"), ("h", "х"),
       ("c", "ц"), ("č", "ч"), ("š", "ш")]


def sr_cyr(text):
    """Łacinka serbska -> cyrylica (znak akcentu U+0301 zostaje na swoim miejscu)."""
    out, i, low = "", 0, text.lower()
    while i < len(text):
        for a, b in _SR:
            if low.startswith(a, i):
                out += b.upper() if text[i].isupper() else b
                i += len(a)
                break
        else:
            out += text[i]
            i += 1
    return out


def sr_lat(text):
    """Cyrylica serbska -> łacinka."""
    out = ""
    for ch in text:
        for a, b in _SR:
            if ch.lower() == b:
                out += (a[0].upper() + a[1:]) if ch.isupper() else a
                break
        else:
            out += ch
    return out


def _ptitle(p, tok):
    """W tytule wzoru zamieniamy tylko hasło w języku kursu (pierwsze słowo), nie polski opis."""
    t = p[2]
    if p[0] in ("conj", "decl") or p[3] == "lpart":
        i = min([x for x in (t.find(" "), t.find(":")) if x >= 0] or [len(t)])
        return tok(t[:i]) + t[i:]
    if ": " in t and " (" in t and t.startswith("Liczebnik"):
        a, b = t.split(": ", 1)
        w, rest = b.split(" (", 1)
        return a + ": " + tok(w) + " (" + rest
    return t


def transform(C, tok, expl):
    """Kopia treści kursu: tok() zmienia słowa w języku kursu, expl() polskie objaśnienia z cytatami."""
    P = set(C.PUNCT)
    T = lambda t: t if t in P else tok(t)
    L = lambda toks: [T(t) for t in toks]
    units = []
    for u in C.UNITS:
        n = {k: v for k, v in u.items() if k not in ("letters", "words", "sentences")}
        if "letters" in u:
            n["letters"] = [tuple(x) for x in u["letters"]]
        if "words" in u:
            n["words"] = [(tok(w[0]),) + tuple(w[1:3]) + (expl(w[3]) if w[3] else w[3],) + tuple(w[4:]) for w in u["words"]]
        if "sentences" in u:
            n["sentences"] = [(L(t), pl, {tok(k): expl(v) for k, v in tr.items()}) for t, pl, tr in u["sentences"]]
        units.append(n)
    ins = {k: [dict(i, chain=[(pl, L(t), expl(h)) for pl, t, h in i["chain"]], text=expl(i["text"])) for i in v]
           for k, v in C.INSIGHTS.items()}
    ends = [(tok(e[0]), tok(e[1]), tok(e[2]), tok(e[3]), [tok(o) for o in e[4]], e[5], expl(e[6]), e[7]) for e in C.ENDINGS]
    extra = {tok(k): v for k, v in C.CHAT_EXTRA.items()}
    chats = []
    for c in C.CHATS:
        turns = []
        for t in c["turns"]:
            n = dict(t, bot=L(t["bot"]))
            if "options" in t:
                n["options"] = [(L(o[0]), o[1], expl(o[2]) if o[2] else o[2]) for o in t["options"]]
            if "build" in t:
                n["build"] = (L(t["build"][0]), t["build"][1])
            turns.append(n)
        chats.append(dict(c, partner=tok(c["partner"]), avatar=tok(c["avatar"]), turns=turns))
    return {"PUNCT": set(C.PUNCT), "TRACKS": dict(C.TRACKS), "UNITS": units, "INSIGHTS": ins,
            "ENDINGS_INSIGHT": dict(C.ENDINGS_INSIGHT), "ENDINGS": ends, "CHAT_EXTRA": extra, "CHATS": chats,
            "ARTICLES": dict(getattr(C, "ARTICLES", {})), "PLURALS": dict(getattr(C, "PLURALS", {})),
            "PARADIGM_LABELS": {k: ([tok(x) for x in v] if k in ("os", "t_ff") or k.startswith("t_m") else list(v)) for k, v in getattr(C, "PARADIGM_LABELS", {}).items()},
            "PARADIGMS": [(p[0], p[1], _ptitle(p, tok), p[3], (p[4] if p[3] == "t_ff" else "; ".join(tok(f) for f in p[4].split("; "))), expl(p[5]) if p[5] else p[5])
                          for p in getattr(C, "PARADIGMS", [])]}


def dump(D, doc):
    """Zapis treści jako czytelny plik .py (jeden wpis w wierszu)."""
    o = ['"""%s"""' % doc, "", "PUNCT = {%s}" % ", ".join(repr(x) for x in sorted(D["PUNCT"])), "",
         "TRACKS = %r" % D["TRACKS"], "", "UNITS = ["]
    for u in D["UNITS"]:
        head = ", ".join("%r: %r" % (k, v) for k, v in u.items() if k not in ("letters", "words", "sentences"))
        o.append("    {" + head + ",")
        for key in ("letters", "words", "sentences"):
            if key in u:
                o.append("     %r: [" % key)
                o += ["         %r," % (x,) for x in u[key]]
                o.append("     ],")
        o.append("    },")
    o += ["]", "", "INSIGHTS = {"]
    for k, v in D["INSIGHTS"].items():
        o.append("    %r: [" % k)
        o += ["        %r," % i for i in v]
        o.append("    ],")
    o += ["}", "", "ENDINGS_INSIGHT = %r" % D["ENDINGS_INSIGHT"], "", "ENDINGS = ["]
    o += ["    %r," % (e,) for e in D["ENDINGS"]]
    o += ["]", "", "CHAT_EXTRA = %r" % D["CHAT_EXTRA"], "", "CHATS = ["]
    for c in D["CHATS"]:
        o.append("    {" + ", ".join("%r: %r" % (k, v) for k, v in c.items() if k != "turns") + ",")
        o.append("     'turns': [")
        o += ["         %r," % t for t in c["turns"]]
        o += ["     ]},"]
    o += ["]"]
    if D.get("ARTICLES"):
        o += ["", "ARTICLES = %r" % D["ARTICLES"]]
    if D.get("PLURALS"):
        o += ["", "PLURALS = %r" % D["PLURALS"]]
    if D.get("PARADIGMS"):
        o += ["", "PARADIGM_LABELS = {"] + ["    %r: %r," % kv for kv in D["PARADIGM_LABELS"].items()] + ["}", "", "PARADIGMS = ["]
        o += ["    %r," % (p,) for p in D["PARADIGMS"]] + ["]"]
    return "\n".join(o) + "\n"


def _load_content(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("_c", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def make_serbian_cyr():
    """courses/serbian/content_cyr.py + engine_cyr.py: te same słowa zapisane cyrylicą."""
    src = os.path.join(HERE, "content_serbian.py")
    if not os.path.exists(src):
        return
    C = _load_content(src)
    import re as _re
    vocab = set()
    for u in C.UNITS:
        vocab |= {w[0] for w in u.get("words", [])}
    vocab |= set(C.CHAT_EXTRA)
    polish = {"dobra", "mala", "mali", "ona", "more", "sada", "student", "hotel", "taksi", "voda", "moja", "dobro",
              "cena", "brata", "jutro", "mleko", "ulica", "mama", "oko", "tata", "zima", "ja", "da", "ne", "i", "u",
              "je", "on", "sam", "si", "dan", "iz", "brat", "ti", "sati", "more", "sir", "pet", "tri", "dva", "grad"}
    plainv = {v.replace("\u0301", ""): v for v in vocab}

    def expl(text):   # w polskim objaśnieniu zamień tylko jednoznacznie serbskie słowa
        def rep(m):
            w = m.group(0)
            k = w.replace("\u0301", "")
            return sr_cyr(w) if (k in plainv and k.lower() not in polish) else w
        return _re.sub(r"[A-Za-zčćđšžČĆĐŠŽ\u0301]+", rep, text) if text else text
    D = transform(C, sr_cyr, expl)
    d = os.path.join(SRC, "courses", "serbian")
    open(os.path.join(d, "content_cyr.py"), "w", encoding="utf-8").write(
        dump(D, "Serbski cyrylicą. PLIK GENEROWANY z content_serbian.py przez make.py: nie edytuj."))
    eng = open(os.path.join(d, "engine.py"), encoding="utf-8").read()
    assert "from .content import" in eng
    open(os.path.join(d, "engine_cyr.py"), "w", encoding="utf-8").write(eng.replace("from .content import", "from .content_cyr import"))
    print("ok serbian (cyrylica)")


if __name__ == "__main__":
    main()
    make_serbian_cyr()
