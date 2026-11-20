"""Składa gotową stronę do folderu docs/ (GitHub Pages). Uruchom: python3 build.py"""
import json, os, shutil, zipfile, hashlib
SRC = os.environ.get("SV_SRC", "/home/claude/svietovit")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "docs")
shutil.rmtree(OUT, ignore_errors=True)
for d in ("py", "fonts", "pyodide"):
    os.makedirs(os.path.join(OUT, d))
# kursy -> osobne male zipy (ladowane dopiero po wejsciu w kurs)
def mkzip(name, pick):
    with zipfile.ZipFile(os.path.join(OUT, "py", name), "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(os.path.join(SRC, "courses")):
            for f in sorted(files):
                if not f.endswith(".py"): continue
                full = os.path.join(root, f); rel = os.path.relpath(full, SRC)
                if pick(rel.split(os.sep)): z.write(full, rel)
mkzip("core.zip", lambda p: len(p) == 2 and p[1] in ("__init__.py", "config.py"))
for cid in ("hanzi_hero","glagol","ave","logos","abba","kaszeby","hangeul","han","kana","nihon","greek","german","french","italian","spanish","russian","turkish","norse","estonian","serbian","finnish","czech","slovak","slovenian","thai"):
    mkzip(cid + ".zip", lambda p, cid=cid: len(p) == 3 and p[1] == cid and not p[2].startswith(("ui", "audio")))
shutil.copy(os.path.join(HERE, "src", "bridge.py"), os.path.join(OUT, "py", "bridge.py"))
for f in ("pyodide.js", "pyodide.asm.js", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json"):
    shutil.copy(os.path.join(HERE, "node_modules", "pyodide", f), os.path.join(OUT, "pyodide", f))
for f in ("index.html", "style.css", "app.js", "config.js", "manifest.webmanifest", "icon-192.png", "icon-512.png"):
    shutil.copy(os.path.join(HERE, "web", f), os.path.join(OUT, f))
# czcionki
F = lambda c, n: os.path.join(SRC, "courses", c, "fonts", n)
def serif(c): return (F(c, "UI-Serif.ttf"), F(c, "UI-SerifBold.ttf"))
TH = "/usr/share/fonts/opentype/tlwg/Loma.otf"; TH_B = "/usr/share/fonts/opentype/tlwg/Loma-Bold.otf"
COURSES = [
 dict(id="hanzi_hero", native="中文", sub={"pl":"znaki, tony, idiomy, chiński klasyczny","en":"characters, tones, idioms, Classical Chinese"}, glyph="汉", paper="#F2EADB", accent="#B8352A", tts="zh-CN", fonts=(F("hanzi_hero","HanziSerif-Regular.ttf"),F("hanzi_hero","HanziSerif-Bold.ttf")), x=F("hanzi_hero","HanziSerif-Regular.ttf")),
 dict(id="glagol", native="Словѣньскъ ѩзыкъ", sub={"pl":"cyrylica i głagolica, Ewangelia","en":"Cyrillic and Glagolitic, the Gospel"}, glyph="Ⰳ", paper="#EFE2C6", accent="#A8321E", tts=None, fonts=serif("glagol"), x=F("glagol","Old-Regular.ttf")),
 dict(id="ave", native="Lingua Latina", sub={"pl":"trzy wymowy, końcówki, sentencje","en":"three pronunciations, endings, sayings"}, glyph="A", paper="#ECE8DF", accent="#9E2B25", tts="it-IT", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="logos", native="Ἑλληνικὴ γλῶσσα", sub={"pl":"pismo politoniczne, maksymy, Ewangelia","en":"polytonic script, maxims, the Gospel"}, glyph="Λ", paper="#F1E2CC", accent="#B5532D", tts=None, fonts=serif("logos"), x=F("logos","UI-Serif.ttf")),
 dict(id="abba", native="ܠܫܢܐ ܐܪܡܝܐ", sub={"pl":"pismo syryjskie, Peszitta, Daniel","en":"Syriac script, Peshitta, Daniel"}, glyph="ܐ", paper="#EEE3CF", accent="#1F7A78", tts=None, fonts=serif("abba"), x=F("abba","Syr.ttf")),
 dict(id="kaszeby", native="Kaszëbsczi jãzëk", sub={"pl":"nowe litery, kaszubienie, rozmowy","en":"new letters, sound rules, conversations"}, glyph="Ò", paper="#EEF0EA", accent="#1C4F8A", tts="pl-PL", fonts=serif("kaszeby"), x=F("kaszeby","UI-Serif.ttf")),
 dict(id="hangeul", native="한국어", sub={"pl":"hangul, słowa, rozmowy","en":"Hangul, words, conversations"}, glyph="한", paper="#F2EEE4", accent="#1C4F8A", tts="ko-KR", fonts=(F("hangeul","HangeulSerif-Regular.ttf"),F("hangeul","HangeulSerif-Bold.ttf")), x=F("hangeul","HangeulSerif-Regular.ttf")),
 dict(id="han", native="汉字", sub={"pl":"od jednej kreski do złożonych znaków","en":"from a single stroke to compound characters"}, glyph="字", paper="#F0E6D8", accent="#8C3B1E", tts="zh-CN", fonts=(F("han","HanSerif-Regular.ttf"),F("han","HanSerif-Bold.ttf")), x=F("han","HanSerif-Regular.ttf")),
 dict(id="kana", native="かな・漢字", sub={"pl":"hiragana, katakana, kanji","en":"hiragana, katakana, kanji"}, glyph="あ", paper="#F4E8EA", accent="#A83257", tts="ja-JP", fonts=(F("kana","KanaSerif-Regular.ttf"),F("kana","KanaSerif-Bold.ttf")), x=F("kana","KanaSerif-Regular.ttf")),
 dict(id="nihon", native="日本語", sub={"pl":"słowa, zdania, rozmowy","en":"words, sentences, conversations"}, glyph="日", paper="#F3EAE4", accent="#B3261E", tts="ja-JP", fonts=(F("nihon","NihonSerif-Regular.ttf"),F("nihon","NihonSerif-Bold.ttf")), x=F("nihon","NihonSerif-Regular.ttf")),
 dict(id="greek", native="Ελληνικά", sub={"pl":"nowogrecki: alfabet, słowa, rozmowy","en":"Modern Greek: alphabet, words, conversations"}, glyph="Ω", paper="#E9EEF2", accent="#1F5FA8", tts="el-GR", fonts=serif("logos"), x=F("logos","UI-Serif.ttf")),
 dict(id="german", native="Deutsch", sub={"pl":"niemiecki: rodzajniki, słowa, rozmowy","en":"German: articles, words, conversations"}, glyph="ß", paper="#EFEBE3", accent="#B8892A", tts="de-DE", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="french", native="Français", sub={"pl":"francuski: wymowa, słowa, rozmowy","en":"French: pronunciation, words, conversations"}, glyph="É", paper="#EDEBF2", accent="#2F4C9A", tts="fr-FR", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="italian", native="Italiano", sub={"pl":"włoski: wymowa, słowa, rozmowy","en":"Italian: pronunciation, words, conversations"}, glyph="Ç", paper="#EEF0E6", accent="#2E7D4F", tts="it-IT", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="spanish", native="Español", sub={"pl":"hiszpański: wymowa, słowa, rozmowy","en":"Spanish: pronunciation, words, conversations"}, glyph="Ñ", paper="#F4EBDD", accent="#C2432B", tts="es-ES", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="russian", native="Русский", sub={"pl":"rosyjski: cyrylica, słowa, rozmowy","en":"Russian: Cyrillic, words, conversations"}, glyph="Я", paper="#EEE9EE", accent="#7A2E5E", tts="ru-RU", fonts=serif("glagol"), x=F("glagol","UI-Serif.ttf")),
 dict(id="turkish", native="Türkçe", sub={"pl":"turecki: końcówki, słowa, rozmowy","en":"Turkish: suffixes, words, conversations"}, glyph="Ş", paper="#F3E8E4", accent="#B3261E", tts="tr-TR", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="norse", native="Norrœnt mál", sub={"pl":"staronordycki: runy, słowa, rozmowy","en":"Old Norse: sounds, words, conversations"}, glyph="Þ", paper="#E9E8E2", accent="#4E5E3A", tts=None, fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="estonian", native="Eesti keel", sub={"pl":"estoński: wymowa, słowa, rozmowy","en":"Estonian: pronunciation, words, conversations"}, glyph="Õ", paper="#E8EEF0", accent="#1E6FA8", tts="et-EE", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="serbian", native="Српски / Srpski", sub={"pl":"serbski: łacinka, cyrylica, rozmowy","en":"Serbian: Latin, Cyrillic, conversations"}, glyph="Ћ", paper="#F0E8E8", accent="#A8232F", tts="sr-RS", fonts=serif("glagol"), x=F("glagol","UI-Serif.ttf")),
 dict(id="finnish", native="Suomi", sub={"pl":"fiński: wymowa, słowa, rozmowy","en":"Finnish: pronunciation, words, conversations"}, glyph="Ä", paper="#EAF0F2", accent="#2A5FA8", tts="fi-FI", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="czech", native="Čeština", sub={"pl":"czeski: wymowa, słowa, rozmowy","en":"Czech: pronunciation, words, conversations"}, glyph="Ř", paper="#EEF0F4", accent="#11457E", tts="cs-CZ", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="slovak", native="Slovenčina", sub={"pl":"słowacki: wymowa, słowa, rozmowy","en":"Slovak: pronunciation, words, conversations"}, glyph="Ľ", paper="#F0EEF2", accent="#0B4EA2", tts="sk-SK", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="slovenian", native="Slovenščina", sub={"pl":"słoweński: wymowa, słowa, rozmowy","en":"Slovene: pronunciation, words, conversations"}, glyph="Š", paper="#EEF2F0", accent="#1C6E8C", tts="sl-SI", fonts=serif("ave"), x=F("ave","UI-Serif.ttf")),
 dict(id="thai", native="ภาษาไทย", sub={"pl":"tajski: pismo, tony, słowa, rozmowy","en":"Thai: script, tones, words, conversations"}, glyph="ก", paper="#F3EAE0", accent="#A8322E", tts="th-TH", fonts=(TH, TH_B), x=TH),
]
css, meta, done = [], [], {}
def put(src, name):
    if src not in done:
        shutil.copy(src, os.path.join(OUT, "fonts", name)); done[src] = name
    return done[src]
shutil.copy(os.path.join(SRC, "fonts", "Sviet-Regular.ttf"), os.path.join(OUT, "fonts", "Sviet-Regular.ttf"))
shutil.copy(os.path.join(SRC, "fonts", "Sviet-Bold.ttf"), os.path.join(OUT, "fonts", "Sviet-Bold.ttf"))
css.append('@font-face{font-family:"Sviet";src:url(fonts/Sviet-Regular.ttf);font-weight:400}@font-face{font-family:"Sviet";src:url(fonts/Sviet-Bold.ttf);font-weight:700}')
for c in COURSES:
    r = put(c["fonts"][0], c["id"] + "-r.ttf"); b = put(c["fonts"][1], c["id"] + "-b.ttf"); x = put(c["x"], c["id"] + "-x.ttf")
    css.append('@font-face{font-family:"F-%s";src:url(fonts/%s);font-weight:400}@font-face{font-family:"F-%s";src:url(fonts/%s);font-weight:700}@font-face{font-family:"F-%s-x";src:url(fonts/%s)}' % (c["id"], r, c["id"], b, c["id"], x))
    meta.append({k: c[k] for k in ("id", "native", "sub", "glyph", "paper", "accent", "tts")})
# glagol: stary alfabet z osobnego fontu jako zapas dla znaków, których UI-Serif nie ma
open(os.path.join(OUT, "fonts.css"), "w").write("\n".join(css))
json.dump(meta, open(os.path.join(OUT, "courses.json"), "w"), ensure_ascii=False)
# service worker z listą plików
files = []
for root, _, fs in os.walk(OUT):
    for f in fs:
        files.append(os.path.relpath(os.path.join(root, f), OUT).replace(os.sep, "/"))
files = sorted(x for x in files if x != "sw.js")
h = hashlib.sha1()
for f in files: h.update(open(os.path.join(OUT, f), "rb").read())
shell = [f for f in files if not (f.startswith("py/") and f not in ("py/core.zip", "py/bridge.py")) and not (f.startswith("fonts/") and f != "fonts/Sviet-Regular.ttf" and f != "fonts/Sviet-Bold.ttf")]
sw = open(os.path.join(HERE, "web", "sw.js")).read().replace("__VERSION__", h.hexdigest()[:10]).replace("__FILES__", json.dumps(["./"] + shell))
open(os.path.join(OUT, "sw.js"), "w").write(sw)
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print(len(files) + 1, "plików,", round(sum(os.path.getsize(os.path.join(OUT, f)) for f in files) / 1e6, 1), "MB")
