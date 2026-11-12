"""Treść kursu: hiszpański dla Polaków."""

PUNCT = {"!", "?", ".", ",", ":", "¿", "¡"}

TRACKS = {"wymowa": "PRONUNCIACIÓN · WYMOWA", "jezyk": "LENGUA · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "Ñ", "track": "wymowa",
     "letters": [
         ("j", "[x]: twarde ch, jak w „chata”", "jamón (szynka)"),
         ("g przed e, i", "[x]: jak polskie ch", "gente (ludzie)"),
         ("g przed a, o, u", "[g]: jak polskie g", "gato (kot)"),
         ("gu przed e, i", "[g]: u nie czytasz", "guerra (wojna)"),
         ("ll", "[j]: jak polskie j", "calle (ulica)"),
         ("ñ", "[ɲ]: jak polskie ń", "niño (dziecko)"),
         ("c przed e, i", "[θ] lub [s]: jak angielskie th lub s (cena)", "cena (kolacja)"),
         ("c przed a, o, u", "[k]: jak polskie k", "casa (dom)"),
         ("qu", "[k]: u nie czytasz", "queso (ser)"),
         ("h", "nie czytasz go wcale", "hola (cześć)"),
         ("v", "[b]: jak polskie b", "vino (wino)"),
         ("rr", "mocne, drżące r", "perro (pies)"),
         ("z", "[θ] lub [s]: zawsze jak s", "zapato (but)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "H", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("hola", "cześć", None, None),
         ("adiós", "do widzenia", None, "Dosł. „do Boga”."),
         ("gracias", "dziękuję", "gracje", None),
         ("por favor", "proszę", None, None),
         ("sí", "tak", None, None),
         ("no", "nie", None, None),
         ("buenos días", "dzień dobry", None, None),
         ("buenas noches", "dobranoc; dobry wieczór", None, None),
         ("mucho", "bardzo; dużo", None, None),
         ("perdón", "przepraszam", "pardon", None),
         ("de nada", "nie ma za co", None, None),
         ("bien", "dobrze", None, None),
         ("y", "i", None, None),
     ],
     "sentences": [
         (["hola", "!"], "Cześć!", {"adiós": "adiós to „do widzenia”."}),
         (["adiós", "!"], "Do widzenia!", {"hola": "hola to „cześć”."}),
         (["¡", "buenos días", "!"], "Dzień dobry!", {"buenas noches": "buenas noches to „dobranoc”."}),
         (["¡", "buenas noches", "!"], "Dobranoc!", {}),
         (["gracias", ",", "mucho"], "Dziękuję bardzo.", {"de nada": "de nada to „nie ma za co”."}),
         (["sí", ",", "gracias"], "Tak, dziękuję.", {"no": "no to „nie”."}),
         (["no", ",", "gracias"], "Nie, dziękuję.", {"sí": "sí to „tak”."}),
         (["perdón", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "S", "track": "jezyk",
     "words": [
         ("yo", "ja", None, None),
         ("tú", "ty", None, None),
         ("él", "on", None, None),
         ("ella", "ona", None, None),
         ("soy", "jestem", None, None),
         ("eres", "jesteś", None, None),
         ("es", "jest", None, None),
         ("polaco", "Polak", None, None),
         ("polaca", "Polka", None, None),
         ("estudiante", "student", "student", None),
         ("profesor", "nauczyciel", "profesor", None),
         ("de", "z; od", None, None),
         ("Polonia", "Polska", None, None),
         ("España", "Hiszpania", None, None),
     ],
     "sentences": [
         (["yo", "soy", "estudiante"], "Jestem studentem.", {"eres": "eres to „jesteś”. O sobie: soy."}),
         (["tú", "eres", "profesor"], "Jesteś nauczycielem.", {"soy": "soy to „jestem”. Do „tú”: eres."}),
         (["él", "es", "polaco"], "On jest Polakiem.", {"polaca": "Dla mężczyzny: polaco."}),
         (["ella", "es", "polaca"], "Ona jest Polką.", {"polaco": "Dla kobiety: polaca."}),
         (["yo", "soy", "de", "Polonia"], "Jestem z Polski.", {"España": "España to Hiszpania."}),
         (["ella", "es", "de", "España"], "Ona jest z Hiszpanii.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "F", "track": "jezyk",
     "words": [
         ("el", "(rodzajnik męski)", None, None),
         ("la", "(rodzajnik żeński)", None, None),
         ("un", "jakiś (męski)", None, None),
         ("una", "jakaś (żeński)", None, None),
         ("madre", "matka", None, None),
         ("padre", "ojciec", None, None),
         ("niño", "chłopiec; dziecko", None, None),
         ("amigo", "przyjaciel", None, None),
         ("mujer", "kobieta; żona", None, None),
         ("hombre", "mężczyzna", None, None),
         ("hermano", "brat", None, None),
         ("hermana", "siostra", None, None),
         ("tengo", "mam", None, None),
         ("tienes", "masz", None, None),
         ("pequeño", "mały", None, None),
         ("bueno", "dobry", None, None),
     ],
     "sentences": [
         (["el", "hermano", "es", "pequeño"], "Brat jest mały.", {"la": "hermano jest męskie: el."}),
         (["la", "madre", "es", "una", "mujer"], "Matka jest kobietą.", {"el": "madre jest żeńska: la."}),
         (["el", "niño", "es", "pequeño"], "Chłopiec jest mały.", {}),
         (["tengo", "un", "hermano"], "Mam brata.", {"tienes": "tienes to „masz”. O sobie: tengo.", "una": "hermano jest męskie: un."}),
         (["tú", "tienes", "una", "hermana"], "Masz siostrę.", {"tengo": "tengo to „mam”. Do „tú”: tienes.", "un": "hermana jest żeńska: una."}),
         (["el", "padre", "es", "un", "hombre"], "Ojciec jest mężczyzną.", {}),
         (["el", "amigo", "es", "bueno"], "Przyjaciel jest dobry.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "P", "track": "jezyk",
     "words": [
         ("agua", "woda", "akwarium", None),
         ("café", "kawa", None, None),
         ("té", "herbata", None, None),
         ("pan", "chleb", None, None),
         ("queso", "ser", None, None),
         ("vino", "wino", None, None),
         ("leche", "mleko", None, None),
         ("pescado", "ryba (jako jedzenie)", None, None),
         ("manzana", "jabłko", None, None),
         ("manzanas", "jabłka", None, "Mnoga: dodaj -s."),
         ("quiero", "chcę", None, None),
         ("quieres", "chcesz", None, None),
         ("ahora", "teraz", None, None),
         ("muy", "bardzo", None, None),
     ],
     "sentences": [
         (["quiero", "un", "café"], "Chcę kawę.", {"una": "café jest męskie: un."}),
         (["quiero", "un", "té", ",", "por favor"], "Poproszę herbatę.", {}),
         (["tú", "quieres", "una", "manzana"], "Chcesz jabłko.", {"quiero": "quiero to „chcę”. Do „tú”: quieres.", "un": "manzana jest żeńska: una."}),
         (["quiero", "el", "pan"], "Chcę chleb.", {}),
         (["el", "pescado", "es", "muy", "bueno"], "Ryba jest bardzo dobra.", {}),
         (["ahora", "quiero", "agua"], "Teraz chcę wodę.", {}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("dos", "dwa", None, None),
         ("tres", "trzy", None, None),
         ("cuatro", "cztery", None, None),
         ("cinco", "pięć", None, None),
         ("diez", "dziesięć", None, None),
         ("niños", "dzieci", None, "Mnoga: dodaj -s."),
         ("hoy", "dziś", None, None),
         ("mañana", "jutro; rano", None, None),
         ("ayer", "wczoraj", None, None),
         ("hora", "godzina", None, None),
         ("las", "(rodzajnik żeński mnogi)", None, None),
         ("son", "są; jest (godzina)", None, None),
         ("qué", "jaki; co", None, None),
     ],
     "sentences": [
         (["tengo", "dos", "niños"], "Mam dwoje dzieci.", {}),
         (["quiero", "tres", "manzanas"], "Chcę trzy jabłka.", {"dos": "dos to „dwa”. Chcesz trzy: tres."}),
         (["¿", "qué", "hora", "es", "?"], "Która jest godzina?", {}),
         (["son", "las", "diez"], "Jest dziesiąta.", {}),
         (["hoy", "quiero", "un", "café"], "Dziś chcę kawę.", {"mañana": "mañana to „jutro”. Tu „dziś”: hoy."}),
         (["mañana", "quiero", "el", "pescado"], "Jutro chcę rybę.", {"ayer": "ayer to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "V", "track": "jezyk",
     "words": [
         ("casa", "dom", None, None),
         ("ciudad", "miasto", None, None),
         ("calle", "ulica", None, None),
         ("escuela", "szkoła", None, None),
         ("mar", "morze", None, None),
         ("taxi", "taksówka", "taksówka", None),
         ("hotel", "hotel", "hotel", None),
         ("dónde", "gdzie", None, None),
         ("aquí", "tu", None, None),
         ("allí", "tam", None, None),
         ("voy", "idę; jadę", None, None),
         ("está", "jest (o miejscu)", None, None),
         ("a", "do; w", None, None),
         ("Madrid", "Madryt", None, None),
         ("derecha", "prawa; w prawo", None, None),
         ("izquierda", "lewa; w lewo", None, None),
     ],
     "sentences": [
         (["¿", "dónde", "está", "el", "hotel", "?"], "Gdzie jest hotel?", {"aquí": "aquí to „tu”. Pytasz „gdzie”: dónde."}),
         (["el", "hotel", "está", "allí"], "Hotel jest tam.", {"aquí": "aquí to „tu”. Tu „tam”: allí."}),
         (["voy", "a", "casa"], "Idę do domu.", {}),
         (["voy", "a", "Madrid"], "Jadę do Madrytu.", {}),
         (["el", "taxi", "está", "a", "la", "derecha"], "Taksówka jest po prawej.", {"izquierda": "izquierda to „lewa”."}),
         (["la", "escuela", "está", "allí"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Hiszpański czyta się, jak jest", "chain": [],
                "text": "Każda litera ma stały dźwięk. Cichym znakiem jest h (hola [ola]), a j i g przed e, i czytamy jak polskie ch. Pytania i wykrzyknienia otwierasz odwróconym znakiem: ¿ ¡."}],
    "ja": [{"title": "Czasownik zastępuje zaimek", "chain": [
                ("Jestem studentem.", ["yo", "soy", "estudiante"], "Do „yo” pasuje soy."),
                ("Jesteś nauczycielem.", ["tú", "eres", "profesor"], "Do „tú” pasuje eres."),
            ],
            "text": "Końcówka mówi, kto działa: soy, eres, es. Zaimek yo, tú często znika: „soy estudiante”."}],
    "ludzie": [{"title": "El, la, un, una", "chain": [],
                "text": "Rzeczowniki są męskie (el, un) lub żeńskie (la, una). Zwykle -o to męski, -a to żeński: el hermano, la hermana."}],
    "jedzenie": [{"title": "Quiero i quieres", "chain": [],
                  "text": "Czasownik querer zmienia się w e → ie: quiero (chcę), quieres (chcesz). W barze dodaj „por favor”."}],
}

ENDINGS_INSIGHT = {"title": "Rodzajniki i formy czasowników",
                   "text": "Ćwiczysz rodzaj (el/la, un/una) i formy czasownika (soy, eres, es). Tu to robisz."}

ENDINGS = [
    ("", "buen", "os días", "", ["os días", "as noches"], "dzień dobry", "días to „dni”: buenos días.", "slowa"),
    ("yo ", "", "soy", " estudiante", ["soy", "eres", "es"], "ja jestem", "Do „yo” pasuje soy.", "ja"),
    ("tú ", "", "eres", " profesor", ["soy", "eres", "es"], "ty jesteś", "Do „tú” pasuje eres.", "ja"),
    ("él ", "", "es", " polaco", ["soy", "eres", "es"], "on jest", "Do „él” pasuje es.", "ja"),
    ("", "", "el", " padre", ["el", "la"], "ten ojciec", "padre jest męski: el.", "ludzie"),
    ("", "", "la", " madre", ["el", "la"], "ta matka", "madre jest żeńska: la.", "ludzie"),
    ("tengo ", "", "un", " hermano", ["un", "una"], "jakiś brat", "hermano jest męski: un.", "ludzie"),
    ("tienes ", "", "una", " hermana", ["un", "una"], "jakaś siostra", "hermana jest żeńska: una.", "ludzie"),
    ("quiero ", "", "un", " café", ["un", "una"], "jakaś kawa", "café jest męskie: un.", "jedzenie"),
    ("quiero ", "", "una", " manzana", ["un", "una"], "jakieś jabłko", "manzana jest żeńska: una.", "jedzenie"),
    ("yo ", "", "quiero", " agua", ["quiero", "quieres"], "ja chcę", "Do „yo” pasuje quiero.", "jedzenie"),
    ("tú ", "", "quieres", " agua", ["quiero", "quieres"], "ty chcesz", "Do „tú” pasuje quieres.", "jedzenie"),
    ("voy ", "", "a", " Madrid", ["a", "de"], "do Madrytu", "a to „do, w”, de to „z, od”.", "miejsca"),
    ("soy ", "", "de", " Polonia", ["a", "de"], "z Polski", "de to „z, od”.", "miejsca"),
]

CHAT_EXTRA = {"Lucía": "Lucía (imię)", "Pablo": "Pablo (imię)", "señor": "pan",
              "cuál": "który"}

CHATS = [
    {"id": "bar", "title": "W barze", "partner": "Lucía", "avatar": "L", "requires": "jedzenie",
     "turns": [
         {"bot": ["¡", "buenos días", "!"], "en": "Dzień dobry!",
          "options": [(["¡", "buenos días", "!"], True, None), (["¡", "buenas noches", "!"], False, "buenas noches to „dobranoc”. Jest dzień.")]},
         {"bot": ["¿", "un", "café", "?"], "en": "Kawę?",
          "options": [(["sí", ",", "quiero", "un", "café"], True, None),
                      (["sí", ",", "quiero", "una", "café"], False, "café jest męskie: un, nie una.")]},
         {"bot": ["¿", "y", "el", "pan", "?"], "en": "I chleb?",
          "options": [(["no", ",", "gracias"], True, None),
                      (["de nada", "!"], False, "de nada to „nie ma za co”. Odmów: no, gracias.")]},
         {"bot": ["bien", "!"], "build": (["gracias", ",", "mucho"], "Dziękuję bardzo."), "en": "Dobrze!"},
     ]},
    {"id": "conocernos", "title": "Poznajemy się", "partner": "Pablo", "avatar": "P", "requires": "ludzie",
     "turns": [
         {"bot": ["hola", "!"], "en": "Cześć!",
          "options": [(["hola", "!"], True, None), (["perdón", "!"], False, "perdón to „przepraszam”. Powitaj: hola.")]},
         {"bot": ["¿", "eres", "de", "España", "?"], "en": "Jesteś z Hiszpanii?",
          "options": [(["no", ",", "soy", "de", "Polonia"], True, None),
                      (["no", ",", "eres", "de", "Polonia"], False, "eres jest do „tú”. O sobie: soy.")]},
         {"bot": ["¿", "tienes", "un", "hermano", "?"], "en": "Masz brata?",
          "options": [(["sí", ",", "tengo", "un", "hermano"], True, None),
                      (["sí", ",", "tienes", "un", "hermano"], False, "tienes to „masz”. O sobie: tengo.")]},
         {"bot": ["¡", "buenas noches", "!"], "build": (["buenas noches"], "Dobranoc."), "en": "Dobranoc!"},
     ]},
    {"id": "taxi", "title": "W taksówce", "partner": "señor", "avatar": "T", "requires": "miejsca",
     "turns": [
         {"bot": ["¡", "buenas noches", "!"], "en": "Dobry wieczór!",
          "options": [(["¡", "buenas noches", "!"], True, None), (["¡", "buenos días", "!"], False, "buenos días to „dzień dobry”. Jest wieczór.")]},
         {"bot": ["¿", "dónde", "?"], "en": "Dokąd?",
          "options": [(["voy", "a", "Madrid"], True, None),
                      (["soy", "a", "Madrid"], False, "soy to „jestem”. Jedziesz: voy.")]},
         {"bot": ["el", "hotel", "está", "allí", "."], "en": "Hotel jest tam.",
          "options": [(["a", "la", "derecha", "?"], True, None), (["aquí", "?"], False, "Pytasz o kierunek: a la derecha.")]},
         {"bot": ["sí", "!"], "build": (["gracias", ",", "mucho"], "Dziękuję bardzo."), "en": "Tak!"},
     ]},
]

# === BULK: generowane z langs/bulk/spanish.txt (nie edytuj ręcznie) ===
UNITS += [{'id': 'f01', 'title': 'Wzór: Quiero … i Tengo …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['quiero', 'agua', '.'], 'Chcę wodę.', {}), (['quiero', 'queso', '.'], 'Chcę ser.', {}), (['quiero', 'leche', '.'], 'Chcę mleko.', {}), (['quiero', 'una', 'manzana', '.'], 'Chcę jabłko.', {}), (['quiero', 'vino', '.'], 'Chcę wino.', {}), (['quiero', 'té', '.'], 'Chcę herbatę.', {}), (['quiero', 'pescado', '.'], 'Chcę rybę.', {}), (['tengo', 'una', 'hermana', '.'], 'Mam siostrę.', {}), (['tengo', 'un', 'amigo', '.'], 'Mam przyjaciela.', {}), (['tengo', 'una', 'casa', '.'], 'Mam dom.', {}), (['tengo', 'tres', 'manzanas', '.'], 'Mam trzy jabłka.', {}), (['tengo', 'cinco', 'manzanas', '.'], 'Mam pięć jabłek.', {}), (['tengo', 'un', 'hotel', '.'], 'Mam hotel.', {})]}, {'id': 'f02', 'title': 'Wzór: ¿Dónde está …? i Voy a …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['¿', 'dónde', 'está', 'la', 'escuela', '?'], 'Gdzie jest szkoła?', {}), (['¿', 'dónde', 'está', 'la', 'calle', '?'], 'Gdzie jest ulica?', {}), (['¿', 'dónde', 'está', 'la', 'casa', '?'], 'Gdzie jest dom?', {}), (['¿', 'dónde', 'está', 'el', 'taxi', '?'], 'Gdzie jest taksówka?', {}), (['¿', 'dónde', 'está', 'la', 'ciudad', '?'], 'Gdzie jest miasto?', {}), (['¿', 'dónde', 'está', 'el', 'mar', '?'], 'Gdzie jest morze?', {}), (['¿', 'dónde', 'está', 'Madrid', '?'], 'Gdzie jest Madryt?', {}), (['voy', 'a', 'la', 'escuela', '.'], 'Idę do szkoły.', {}), (['voy', 'a', 'la', 'ciudad', '.'], 'Idę do miasta.', {}), (['voy', 'a', 'Madrid', '.'], 'Idę do Madrytu.', {}), (['voy', 'a', 'Polonia', '.'], 'Idę do Polski.', {}), (['voy', 'a', 'España', '.'], 'Idę do Hiszpanii.', {}), (['voy', 'a', 'el', 'mar', '.'], 'Idę do morza.', {}), (['voy', 'a', 'el', 'hotel', '.'], 'Idę do hotelu.', {}), (['hoy', 'voy', 'a', 'la', 'escuela', '.'], 'Dziś idę do szkoły.', {}), (['mañana', 'voy', 'a', 'Madrid', '.'], 'Jutro idę do Madrytu.', {}), (['ahora', 'voy', 'a', 'la', 'casa', '.'], 'Teraz idę do domu.', {}), (['hoy', 'voy', 'a', 'el', 'mar', '.'], 'Dziś idę do morza.', {})]}, {'id': 'f03', 'title': 'Wzór: Soy … Eres … Es …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['yo', 'soy', 'polaco', '.'], 'Ja jestem Polakiem.', {}), (['tú', 'eres', 'estudiante', '.'], 'Ty jesteś studentem.', {}), (['él', 'es', 'profesor', '.'], 'On jest nauczycielem.', {}), (['yo', 'soy', 'estudiante', '.'], 'Ja jestem studentem.', {}), (['tú', 'eres', 'polaco', '.'], 'Ty jesteś Polakiem.', {})]}, {'id': 'f04', 'title': 'Zdania złożone: pero i porque', 'icon': 'Z', 'track': 'jezyk', 'words': [('pero', 'ale', None, None), ('porque', 'ponieważ, bo', None, None)], 'sentences': [(['tengo', 'pan', ',', 'pero', 'no', 'tengo', 'queso', '.'], 'Mam chleb, ale nie mam sera.', {}), (['tengo', 'agua', ',', 'pero', 'no', 'tengo', 'leche', '.'], 'Mam wodę, ale nie mam mleka.', {}), (['tengo', 'un', 'hermano', ',', 'pero', 'no', 'tengo', 'una', 'hermana', '.'], 'Mam brata, ale nie mam siostry.', {}), (['tengo', 'café', ',', 'pero', 'no', 'tengo', 'té', '.'], 'Mam kawę, ale nie mam herbaty.', {}), (['quiero', 'pan', ',', 'porque', 'es', 'bueno', '.'], 'Chcę chleb, bo jest dobry.', {}), (['quiero', 'queso', ',', 'porque', 'es', 'bueno', '.'], 'Chcę ser, bo jest dobry.', {}), (['quiero', 'vino', ',', 'porque', 'es', 'bueno', '.'], 'Chcę wino, bo jest dobry.', {}), (['quiero', 'pescado', ',', 'porque', 'es', 'bueno', '.'], 'Chcę rybę, bo jest dobry.', {})]}]
INSIGHTS.setdefault('f01', []).append({'title': 'Wzór: Quiero … i Tengo …', 'text': 'Ten sam szkielet, inne komponenty: Quiero + to, czego chcesz. Tengo + to, co masz. Rodzajnik jest nieokreślony: un (męski), una (żeński).\n\nPrzykład: Quiero agua. = Chcę wodę.', 'chain': []})
INSIGHTS.setdefault('f02', []).append({'title': 'Wzór: ¿Dónde está …? i Voy a …', 'text': 'Pytanie o miejsce: ¿Dónde está + rzeczownik? Kierunek: Voy a + miejsce. Zmieniasz tylko miejsce, reszta zostaje.\n\nPrzykład: ¿ dónde está la escuela? = Gdzie jest szkoła?', 'chain': []})
INSIGHTS.setdefault('f03', []).append({'title': 'Wzór: Soy … Eres … Es …', 'text': 'Kto jest kim: osoba + czasownik ser + zawód lub narodowość. Soy (ja), eres (ty), es (on, ona).\n\nPrzykład: Yo soy polaco. = Ja jestem Polakiem.', 'chain': []})
INSIGHTS.setdefault('f04', []).append({'title': 'Zdania złożone: pero i porque', 'text': 'Dwa zdania łączysz przecinkiem i słowem pero (ale) albo porque (bo). Zdania podrzędne w hiszpańskim mają zwykły szyk, czasownik nie ucieka na koniec.\n\nPrzykład: Tengo pan, pero no tengo queso. = Mam chleb, ale nie mam sera.', 'chain': []})
# === /BULK ===

# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['yo', 'tú', 'él/ella', 'nosotros', 'vosotros', 'ellos/ellas'],
    'rodz': ['męski lp.', 'żeński lp.', 'męski lm.', 'żeński lm.'],
    'pp': ['hablar', 'comer', 'vivir', 'ser', 'hacer', 'decir', 'ver', 'escribir', 'poner', 'volver'],
    'ger': ['hablar', 'comer', 'vivir', 'ser', 'ir', 'decir'],
    't_serestar': ['Yo ___ polaco. (kim jestem)', 'Yo ___ en casa. (gdzie)', 'Ella ___ cansada. (stan)', 'Él ___ médico. (zawód)', 'Madrid ___ en España. (położenie)', 'La sopa ___ fría. (stan)', 'Nosotros ___ amigos. (kim)', '¿Cómo ___ tú? (samopoczucie)'],
    't_porpara': ['Este regalo es ___ ti.', 'Gracias ___ todo.', 'Salgo ___ Madrid. (cel podróży)', 'Paso ___ el parque.', 'Estudio ___ aprender.', 'Lo compré ___ diez euros.'],
    't_rodz': ['problema', 'mano', 'día', 'mapa', 'foto', 'agua', 'idioma', 'noche'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'hablar (mówić)', 'os', 'hablo; hablas; habla; hablamos; habláis; hablan', 'Koniugacja -ar.'),
    ('conj', 'Wzory koniugacji', 'comer (jeść)', 'os', 'como; comes; come; comemos; coméis; comen', 'Koniugacja -er.'),
    ('conj', 'Wzory koniugacji', 'vivir (żyć, mieszkać)', 'os', 'vivo; vives; vive; vivimos; vivís; viven', 'Koniugacja -ir.'),
    ('conj', 'Wyjątki', 'querer (chcieć)', 'os', 'quiero; quieres; quiere; queremos; queréis; quieren', 'e → ie pod akcentem (poza nosotros i vosotros).'),
    ('conj', 'Wyjątki', 'poder (móc)', 'os', 'puedo; puedes; puede; podemos; podéis; pueden', 'o → ue pod akcentem.'),
    ('conj', 'Czasowniki nieregularne', 'ser (być: kim, jaki)', 'os', 'soy; eres; es; somos; sois; son', None),
    ('conj', 'Czasowniki nieregularne', 'estar (być: gdzie, w jakim stanie)', 'os', 'estoy; estás; está; estamos; estáis; están', None),
    ('conj', 'Czasowniki nieregularne', 'tener (mieć)', 'os', 'tengo; tienes; tiene; tenemos; tenéis; tienen', None),
    ('conj', 'Czasowniki nieregularne', 'ir (iść)', 'os', 'voy; vas; va; vamos; vais; van', None),
    ('conj', 'Czasowniki nieregularne', 'hacer (robić)', 'os', 'hago; haces; hace; hacemos; hacéis; hacen', None),
    ('conj', 'Czasowniki nieregularne', 'decir (mówić)', 'os', 'digo; dices; dice; decimos; decís; dicen', None),
    ('decl', 'Przymiotniki: rodzaj i liczba', 'bueno (dobry)', 'rodz', 'bueno; buena; buenos; buenas', None),
    ('decl', 'Przymiotniki: rodzaj i liczba', 'pequeño (mały)', 'rodz', 'pequeño; pequeña; pequeños; pequeñas', None),
    ('decl', 'Wyjątki', 'grande (duży)', 'rodz', 'grande; grande; grandes; grandes', 'Przymiotniki na -e mają jedną formę dla obu rodzajów.'),
    ('decl', 'Rodzajnik określony', 'el, la', 'rodz', 'el; la; los; las', None),
    ('form', 'Imiesłowy', 'Participio', 'pp', 'hablado; comido; vivido; sido; hecho; dicho; visto; escrito; puesto; vuelto', '-ar → -ado, -er i -ir → -ido.'),
    ('form', 'Imiesłowy', 'Gerundio', 'ger', 'hablando; comiendo; viviendo; siendo; yendo; diciendo', None),
    ('conj', 'Czas przeszły', 'hablar: pretérito perfecto', 'os', 'he hablado; has hablado; ha hablado; hemos hablado; habéis hablado; han hablado', 'haber + participio.'),
    ('conj', 'Czas przeszły', 'hablar: pretérito indefinido', 'os', 'hablé; hablaste; habló; hablamos; hablasteis; hablaron', None),
    ('conj', 'Czas przeszły', 'comer: pretérito indefinido', 'os', 'comí; comiste; comió; comimos; comisteis; comieron', None),
    ('conj', 'Czas przeszły', 'ser, ir: pretérito indefinido', 'os', 'fui; fuiste; fue; fuimos; fuisteis; fueron', 'ser i ir mają w tym czasie te same formy.'),
    ('conj', 'Czas przeszły', 'hablar: imperfecto', 'os', 'hablaba; hablabas; hablaba; hablábamos; hablabais; hablaban', None),
    ('conj', 'Czas przyszły', 'hablar: futuro', 'os', 'hablaré; hablarás; hablará; hablaremos; hablaréis; hablarán', None),
    ('form', 'Typowe trudności', 'Ser czy estar?', 't_serestar', 'soy; estoy; está; es; está; está; somos; estás', None),
    ('form', 'Typowe trudności', 'Por czy para?', 't_porpara', 'para; por; para; por; para; por', None),
    ('form', 'Typowe trudności', 'Rodzaj: el czy la?', 't_rodz', 'el; la; el; el; la; el; el; la', None),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['embarazada', 'la carta', 'largo', 'el éxito', 'constipado', 'la ropa', 'el vaso'],
    't_m1': ['está', 'esta', 'sí', 'si', 'él', 'el', 'tú', 'tu'],
    't_m2': ['___ el café.', '___ los libros.', '___ bailar.', '___ las manzanas.', '___ la música.', '___ los perros.'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Fałszywi przyjaciele: co to znaczy?', 't_m0', 'w ciąży; list; długi; sukces; przeziębiony; ubranie; szklanka', None),
    ('form', 'Typowe trudności', 'Akcent graficzny: co to znaczy?', 't_m1', 'jest; ta; tak; jeśli; on; (rodzajnik); ty; twój', 'Kreska odróżnia słowa, które brzmią prawie tak samo.'),
    ('form', 'Typowe trudności', 'Gustar: me gusta czy me gustan?', 't_m2', 'me gusta; me gustan; me gusta; me gustan; me gusta; me gustan', 'Dosłownie „podoba mi się”: czasownik zgadza się z rzeczą, nie z osobą. Rodzajnik jest obowiązkowy.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['Nie mam pieniędzy.', 'Widzę go.', 'Chcę to zjeść.', 'Lubię kawę.', 'To duży dom.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: zaimki i przeczenie', 't_s0', 'No tengo dinero.|Tengo no dinero.|No dinero tengo.|Tengo dinero no.; Lo veo.|Veo lo.|Lo yo veo.|Yo veo lo.; Quiero comerlo.|Quiero comer lo.|Quiero lo comer.|Lo comer quiero.; Me gusta el café.|Gusta me el café.|Me el café gusta.|El café gusta me.; Es una casa grande.|Es una grande casa.|Es grande una casa.|Es casa una grande.', 'No stoi tuż przed czasownikiem. Zaimek stoi przed odmienionym czasownikiem albo przyklejony do bezokolicznika.'),
]
