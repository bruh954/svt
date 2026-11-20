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

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'me, te, lo… (dopełnienie bliższe)', 'os', 'me; te; lo, la; nos; os; los, las', 'Stoją przed odmienionym czasownikiem: lo veo.'),
    ('decl', 'Zaimki', 'me, te, le… (dopełnienie dalsze)', 'os', 'me; te; le; nos; os; les', 'Przed lo i la le zmienia się w se: se lo doy.'),
    ('decl', 'Zaimki', 'me, te, se… (zwrotne)', 'os', 'me; te; se; nos; os; se', None),
    ('decl', 'Zaimki', 'mí, ti… (po przyimku)', 'os', 'mí; ti; él, ella; nosotros; vosotros; ellos, ellas', 'Po przyimku: para mí. Wyjątek: conmigo, contigo.'),
    ('decl', 'Zaimki', 'mi, tu, su… (mój, twój…)', 'os', 'mi; tu; su; nuestro; vuestro; su', 'Stoi przed rzeczownikiem i zgadza się z nim: mis amigos.'),
    ('decl', 'Zaimki', 'este (ten tu)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'rodzaj męski lm.', 'rodzaj żeński lm.'], 'este; esta; estos; estas', None),
    ('decl', 'Zaimki', 'ese (ten)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'rodzaj męski lm.', 'rodzaj żeński lm.'], 'ese; esa; esos; esas', None),
    ('decl', 'Zaimki', 'aquel (tamten)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'rodzaj męski lm.', 'rodzaj żeński lm.'], 'aquel; aquella; aquellos; aquellas', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'tienes una hermana': 'Masz siostrę.', 'yo quiero agua': 'Chcę wody.', 'tú quieres agua': 'Chcesz wody.', 'soy de Polonia': 'Jestem z Polski.'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'malo (zły)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'malo; peor; el peor', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'alto (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'alto; más alto; el más alto', None),
    ('form', 'Stopniowanie', 'bonito (ładny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'bonito; más bonito; el más bonito', None),
    ('form', 'Stopniowanie', 'rápido (szybki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'rápido; más rápido; el más rápido', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 1 (generowane) ===
PARADIGMS += [
    ('conj', 'Tryb łączący', 'hablar: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'hable; hables; hable; hablemos; habléis; hablen', None),
    ('conj', 'Tryb łączący', 'comer: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'coma; comas; coma; comamos; comáis; coman', None),
    ('conj', 'Tryb łączący', 'vivir: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'viva; vivas; viva; vivamos; viváis; vivan', None),
    ('conj', 'Tryb łączący', 'ser: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'sea; seas; sea; seamos; seáis; sean', 'Po „quiero que”, „es importante que”: quiero que vengas.'),
    ('conj', 'Tryb łączący', 'tener: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'tenga; tengas; tenga; tengamos; tengáis; tengan', None),
    ('conj', 'Tryb łączący', 'ir: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'vaya; vayas; vaya; vayamos; vayáis; vayan', None),
    ('conj', 'Tryb łączący', 'hacer: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'haga; hagas; haga; hagamos; hagáis; hagan', None),
    ('conj', 'Tryb łączący', 'estar: subjuntivo', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'esté; estés; esté; estemos; estéis; estén', None),
    ('conj', 'Tryb warunkowy', 'hablar: condicional', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'hablaría; hablarías; hablaría; hablaríamos; hablaríais; hablarían', None),
    ('conj', 'Tryb warunkowy', 'comer: condicional', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'comería; comerías; comería; comeríamos; comeríais; comerían', None),
    ('conj', 'Tryb warunkowy', 'ser: condicional', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'sería; serías; sería; seríamos; seríais; serían', None),
    ('conj', 'Tryb warunkowy', 'tener: condicional', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'tendría; tendrías; tendría; tendríamos; tendríais; tendrían', None),
    ('conj', 'Tryb warunkowy', 'poder: condicional', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'podría; podrías; podría; podríamos; podríais; podrían', None),
    ('conj', 'Tryb warunkowy', 'querer: condicional', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'querría; querrías; querría; querríamos; querríais; querrían', None),
    ('form', 'Tryb rozkazujący', 'hablar: imperativo', ['tú (twierdząco)', 'tú (przeczenie)', 'usted', 'nosotros', 'vosotros (twierdząco)', 'ustedes'], 'habla; no hables; hable; hablemos; hablad; hablen', None),
    ('form', 'Tryb rozkazujący', 'comer: imperativo', ['tú (twierdząco)', 'tú (przeczenie)', 'usted', 'nosotros', 'vosotros (twierdząco)', 'ustedes'], 'come; no comas; coma; comamos; comed; coman', None),
    ('form', 'Tryb rozkazujący', 'vivir: imperativo', ['tú (twierdząco)', 'tú (przeczenie)', 'usted', 'nosotros', 'vosotros (twierdząco)', 'ustedes'], 'vive; no vivas; viva; vivamos; vivid; vivan', None),
    ('form', 'Tryb rozkazujący', 'ser: imperativo', ['tú (twierdząco)', 'tú (przeczenie)', 'usted', 'nosotros', 'vosotros (twierdząco)', 'ustedes'], 'sé; no seas; sea; seamos; sed; sean', None),
    ('form', 'Tryb rozkazujący', 'ir: imperativo', ['tú (twierdząco)', 'tú (przeczenie)', 'usted', 'nosotros', 'vosotros (twierdząco)', 'ustedes'], 've; no vayas; vaya; vayamos; id; vayan', None),
    ('form', 'Tryb rozkazujący', 'tener: imperativo', ['tú (twierdząco)', 'tú (przeczenie)', 'usted', 'nosotros', 'vosotros (twierdząco)', 'ustedes'], 'ten; no tengas; tenga; tengamos; tened; tengan', None),
    ('form', 'Tryb rozkazujący', 'hacer: imperativo', ['tú (twierdząco)', 'tú (przeczenie)', 'usted', 'nosotros', 'vosotros (twierdząco)', 'ustedes'], 'haz; no hagas; haga; hagamos; haced; hagan', None),
    ('conj', 'Czas przeszły', 'tener: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'tuve; tuviste; tuvo; tuvimos; tuvisteis; tuvieron', None),
    ('conj', 'Czas przeszły', 'hacer: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'hice; hiciste; hizo; hicimos; hicisteis; hicieron', None),
    ('conj', 'Czas przeszły', 'estar: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'estuve; estuviste; estuvo; estuvimos; estuvisteis; estuvieron', None),
    ('conj', 'Czas przeszły', 'decir: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'dije; dijiste; dijo; dijimos; dijisteis; dijeron', None),
    ('conj', 'Czas przeszły', 'poder: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'pude; pudiste; pudo; pudimos; pudisteis; pudieron', None),
    ('conj', 'Czas przeszły', 'venir: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'vine; viniste; vino; vinimos; vinisteis; vinieron', None),
    ('conj', 'Czas przeszły', 'dar: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'di; diste; dio; dimos; disteis; dieron', None),
    ('conj', 'Czas przeszły', 'ver: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'vi; viste; vio; vimos; visteis; vieron', None),
    ('conj', 'Czas przeszły', 'querer: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'quise; quisiste; quiso; quisimos; quisisteis; quisieron', None),
    ('conj', 'Czas przeszły', 'vivir: pretérito indefinido', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'viví; viviste; vivió; vivimos; vivisteis; vivieron', None),
    ('conj', 'Czas przeszły', 'comer: imperfecto', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'comía; comías; comía; comíamos; comíais; comían', None),
    ('conj', 'Czas przeszły', 'vivir: imperfecto', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'vivía; vivías; vivía; vivíamos; vivíais; vivían', None),
    ('conj', 'Czas przeszły', 'ser: imperfecto', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'era; eras; era; éramos; erais; eran', 'Trzy czasowniki mają nieregularny imperfecto: ser, ir, ver.'),
    ('conj', 'Czas przeszły', 'ir: imperfecto', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'iba; ibas; iba; íbamos; ibais; iban', None),
    ('conj', 'Czas przeszły', 'ver: imperfecto', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'veía; veías; veía; veíamos; veíais; veían', None),
    ('conj', 'Czas przyszły', 'tener: futuro', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'tendré; tendrás; tendrá; tendremos; tendréis; tendrán', 'Nieregularne futuro: rdzeń się skraca, końcówki są zwykłe.'),
    ('conj', 'Czas przyszły', 'hacer: futuro', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'haré; harás; hará; haremos; haréis; harán', None),
    ('conj', 'Czas przyszły', 'poder: futuro', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'podré; podrás; podrá; podremos; podréis; podrán', None),
    ('conj', 'Czas przyszły', 'decir: futuro', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'diré; dirás; dirá; diremos; diréis; dirán', None),
    ('conj', 'Czas przyszły', 'venir: futuro', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'vendré; vendrás; vendrá; vendremos; vendréis; vendrán', None),
    ('conj', 'Czas przyszły', 'salir: futuro', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'saldré; saldrás; saldrá; saldremos; saldréis; saldrán', None),
    ('conj', 'Czas przyszły', 'querer: futuro', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'querré; querrás; querrá; querremos; querréis; querrán', None),
    ('conj', 'Czasowniki zwrotne', 'levantarse (wstawać)', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'me levanto; te levantas; se levanta; nos levantamos; os levantáis; se levantan', None),
    ('conj', 'Czasowniki zwrotne', 'llamarse (nazywać się)', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'me llamo; te llamas; se llama; nos llamamos; os llamáis; se llaman', None),
    ('conj', 'Czasowniki zwrotne', 'ducharse (brać prysznic)', ['yo', 'tú', 'él / ella', 'nosotros', 'vosotros', 'ellos / ellas'], 'me ducho; te duchas; se ducha; nos duchamos; os ducháis; se duchan', None),
    ('form', 'Typowe czasowniki', 'gustar (podobać się)', ['(a mí)', '(a ti)', '(a él / ella)', '(a nosotros)', '(a vosotros)', '(a ellos / ellas)'], 'me gusta; te gusta; le gusta; nos gusta; os gusta; les gusta', 'Uzgadnia się z tym, co się podoba: me gusta el café, me gustan los libros.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 1 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('chico', 'chłopiec', None, 'rodzaj męski'), ('niña', 'dziewczynka', None, 'rodzaj żeński'), ('persona', 'człowiek', None, 'rodzaj żeński'), ('gente', 'ludzie', None, 'rodzaj żeński'), ('familia', 'rodzina', None, 'rodzaj żeński'), ('hijo', 'syn', None, 'rodzaj męski'), ('hija', 'córka', None, 'rodzaj żeński'), ('abuelo', 'dziadek', None, 'rodzaj męski'), ('abuela', 'babcia', None, 'rodzaj żeński'), ('nieto', 'wnuk', None, 'rodzaj męski'), ('tío', 'wujek', None, 'rodzaj męski'), ('tía', 'ciocia', None, 'rodzaj żeński'), ('primo', 'kuzyn', None, 'rodzaj męski'), ('marido', 'mąż', None, 'rodzaj męski'), ('esposa', 'żona', None, 'rodzaj żeński'), ('vecino', 'sąsiad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('invitado', 'gość', None, 'rodzaj męski'), ('jefe', 'szef', None, 'rodzaj męski'), ('colega', 'kolega', None, 'rodzaj męski'), ('enemigo', 'wróg', None, 'rodzaj męski'), ('rey', 'król', None, 'rodzaj męski'), ('reina', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('cabeza', 'głowa', None, 'rodzaj żeński'), ('cara', 'twarz', None, 'rodzaj żeński'), ('ojo', 'oko', None, 'rodzaj męski'), ('oreja', 'ucho', None, 'rodzaj żeński'), ('nariz', 'nos', None, 'rodzaj żeński'), ('boca', 'usta', None, 'rodzaj żeński'), ('diente', 'ząb', None, 'rodzaj męski'), ('lengua', 'język (narząd)', None, 'rodzaj żeński'), ('pelo', 'włosy', None, 'rodzaj męski'), ('cuello', 'szyja', None, 'rodzaj męski'), ('brazo', 'ramię', None, 'rodzaj męski'), ('mano', 'ręka', None, 'rodzaj żeński'), ('dedo', 'palec', None, 'rodzaj męski'), ('pierna', 'noga', None, 'rodzaj żeński'), ('pie', 'stopa', None, 'rodzaj męski'), ('rodilla', 'kolano', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('espalda', 'plecy', None, 'rodzaj żeński'), ('barriga', 'brzuch', None, 'rodzaj żeński'), ('corazón', 'serce', None, 'rodzaj męski'), ('sangre', 'krew', None, 'rodzaj żeński'), ('hueso', 'kość', None, 'rodzaj męski'), ('piel', 'skóra', None, 'rodzaj żeński'), ('voz', 'głos', None, 'rodzaj żeński'), ('cuerpo', 'ciało', None, 'rodzaj męski'), ('estómago', 'żołądek', None, 'rodzaj męski'), ('barba', 'broda', None, 'rodzaj żeński'), ('labio', 'warga', None, 'rodzaj męski'), ('uña', 'paznokieć', None, 'rodzaj żeński'), ('pecho', 'pierś', None, 'rodzaj męski'), ('cerebro', 'mózg', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('mantequilla', 'masło', None, 'rodzaj żeński'), ('huevo', 'jajko', None, 'rodzaj męski'), ('carne', 'mięso', None, 'rodzaj żeński'), ('pollo', 'kurczak', None, 'rodzaj męski'), ('cerdo', 'wieprzowina', None, 'rodzaj męski'), ('sopa', 'zupa', None, 'rodzaj żeński'), ('ensalada', 'sałatka', None, 'rodzaj żeński'), ('arroz', 'ryż', None, 'rodzaj męski'), ('pasta', 'makaron', None, 'rodzaj żeński'), ('patata', 'ziemniak', None, 'rodzaj żeński'), ('zanahoria', 'marchewka', None, 'rodzaj żeński'), ('cebolla', 'cebula', None, 'rodzaj żeński'), ('ajo', 'czosnek', None, 'rodzaj męski'), ('tomate', 'pomidor', None, 'rodzaj męski'), ('pepino', 'ogórek', None, 'rodzaj męski'), ('pera', 'gruszka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('plátano', 'banan', None, 'rodzaj męski'), ('naranja', 'pomarańcza', None, 'rodzaj żeński'), ('limón', 'cytryna', None, 'rodzaj męski'), ('fresa', 'truskawka', None, 'rodzaj żeński'), ('uva', 'winogrono', None, 'rodzaj żeński'), ('azúcar', 'cukier', None, 'rodzaj męski'), ('sal', 'sól', None, 'rodzaj żeński'), ('pimienta', 'pieprz', None, 'rodzaj żeński'), ('aceite', 'olej', None, 'rodzaj męski'), ('harina', 'mąka', None, 'rodzaj żeński'), ('miel', 'miód', None, 'rodzaj żeński'), ('chocolate', 'czekolada', None, 'rodzaj męski'), ('helado', 'lody', None, 'rodzaj męski'), ('pastel', 'ciasto (tort)', None, 'rodzaj męski'), ('galleta', 'ciastko', None, 'rodzaj żeński'), ('desayuno', 'śniadanie', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('almuerzo', 'obiad', None, 'rodzaj męski'), ('cena', 'kolacja', None, 'rodzaj żeński'), ('tentempié', 'przekąska', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('zumo', 'sok', None, 'rodzaj męski'), ('cerveza', 'piwo', None, 'rodzaj żeński'), ('bebida', 'napój', None, 'rodzaj żeński'), ('vaso', 'szklanka', None, 'rodzaj męski'), ('taza', 'filiżanka', None, 'rodzaj żeński'), ('plato', 'talerz', None, 'rodzaj męski'), ('cuchillo', 'nóż', None, 'rodzaj męski'), ('tenedor', 'widelec', None, 'rodzaj męski'), ('cuchara', 'łyżka', None, 'rodzaj żeński'), ('botella', 'butelka', None, 'rodzaj żeński'), ('carta', 'menu', None, 'rodzaj żeński'), ('cuenta', 'rachunek', None, 'rodzaj żeński'), ('propina', 'napiwek', None, 'rodzaj żeński'), ('mesa', 'stolik', None, 'rodzaj żeński'), ('camarero', 'kelner', None, 'rodzaj męski'), ('cocinero', 'kucharz', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('hambriento', 'głodny', None, None), ('sediento', 'spragniony', None, None), ('sabroso', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('piso', 'mieszkanie', None, 'rodzaj męski'), ('habitación', 'pokój', None, 'rodzaj żeński'), ('cocina', 'kuchnia', None, 'rodzaj żeński'), ('baño', 'łazienka', None, 'rodzaj męski'), ('dormitorio', 'sypialnia', None, 'rodzaj męski'), ('salón', 'salon', None, 'rodzaj męski'), ('jardín', 'ogród', None, 'rodzaj męski'), ('puerta', 'drzwi', None, 'rodzaj żeński'), ('ventana', 'okno', None, 'rodzaj żeński'), ('pared', 'ściana', None, 'rodzaj żeński'), ('suelo', 'podłoga', None, 'rodzaj męski'), ('tejado', 'dach', None, 'rodzaj męski'), ('escalera', 'schody', None, 'rodzaj żeński'), ('llave', 'klucz', None, 'rodzaj żeński'), ('mesa (stół)', 'stół', None, 'rodzaj żeński'), ('silla', 'krzesło', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('cama', 'łóżko', None, 'rodzaj żeński'), ('armario', 'szafa', None, 'rodzaj męski'), ('lámpara', 'lampa', None, 'rodzaj żeński'), ('alfombra', 'dywan', None, 'rodzaj żeński'), ('espejo', 'lustro', None, 'rodzaj męski'), ('televisor', 'telewizor', None, 'rodzaj męski'), ('teléfono', 'telefon', None, 'rodzaj męski'), ('ordenador', 'komputer', None, 'rodzaj męski'), ('reloj', 'zegar', None, 'rodzaj męski'), ('almohada', 'poduszka', None, 'rodzaj żeński'), ('manta', 'koc', None, 'rodzaj żeński'), ('toalla', 'ręcznik', None, 'rodzaj żeński'), ('jabón', 'mydło', None, 'rodzaj męski'), ('cepillo de dientes', 'szczoteczka do zębów', None, 'rodzaj męski'), ('nevera', 'lodówka', None, 'rodzaj żeński'), ('horno', 'piec', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('lavadora', 'pralka', None, 'rodzaj żeński'), ('basura', 'śmieci', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('ropa', 'ubranie', None, 'rodzaj żeński'), ('camisa', 'koszula', None, 'rodzaj żeński'), ('pantalón', 'spodnie', None, 'rodzaj męski'), ('vestido', 'sukienka', None, 'rodzaj męski'), ('falda', 'spódnica', None, 'rodzaj żeński'), ('chaqueta', 'kurtka', None, 'rodzaj żeński'), ('abrigo', 'płaszcz', None, 'rodzaj męski'), ('jersey', 'sweter', None, 'rodzaj męski'), ('zapato', 'buty', None, 'rodzaj męski'), ('calcetín', 'skarpetki', None, 'rodzaj męski'), ('gorro', 'czapka', None, 'rodzaj męski'), ('sombrero', 'kapelusz', None, 'rodzaj męski'), ('guante', 'rękawiczki', None, 'rodzaj męski'), ('bufanda', 'szalik', None, 'rodzaj żeński'), ('bolso', 'torba', None, 'rodzaj męski'), ('mochila', 'plecak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('cartera', 'portfel', None, 'rodzaj żeński'), ('gafas', 'okulary', None, 'rodzaj żeński'), ('reloj de pulsera', 'zegarek', None, 'rodzaj męski'), ('anillo', 'pierścionek', None, 'rodzaj męski'), ('ropa interior', 'bielizna', None, 'rodzaj żeński'), ('pijama', 'piżama', None, 'rodzaj męski'), ('cinturón', 'pasek', None, 'rodzaj męski'), ('corbata', 'krawat', None, 'rodzaj żeński'), ('traje', 'garnitur', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('rojo', 'czerwony', None, None), ('azul', 'niebieski', None, None), ('verde', 'zielony', None, None), ('amarillo', 'żółty', None, None), ('negro', 'czarny', None, None), ('blanco', 'biały', None, None), ('gris', 'szary', None, None), ('marrón', 'brązowy', None, None), ('rosa', 'różowy', None, None), ('morado', 'fioletowy', None, None), ('color', 'kolor', None, 'rodzaj męski'), ('redondo', 'okrągły', None, None), ('cuadrado', 'kwadratowy', None, None), ('recto', 'prosty', None, None), ('torcido', 'krzywy', None, None), ('línea', 'linia', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('punto', 'punkt', None, 'rodzaj męski'), ('círculo', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('cero', 'zero', None, None), ('once', 'jedenaście', None, None), ('doce', 'dwanaście', None, None), ('trece', 'trzynaście', None, None), ('catorce', 'czternaście', None, None), ('quince', 'piętnaście', None, None), ('dieciséis', 'szesnaście', None, None), ('diecisiete', 'siedemnaście', None, None), ('dieciocho', 'osiemnaście', None, None), ('diecinueve', 'dziewiętnaście', None, None), ('veinte', 'dwadzieścia', None, None), ('treinta', 'trzydzieści', None, None), ('cuarenta', 'czterdzieści', None, None), ('cincuenta', 'pięćdziesiąt', None, None), ('sesenta', 'sześćdziesiąt', None, None), ('setenta', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('ochenta', 'osiemdziesiąt', None, None), ('noventa', 'dziewięćdziesiąt', None, None), ('cien', 'sto', None, None), ('mil', 'tysiąc', None, None), ('millón', 'milion', None, 'rodzaj męski'), ('primero', 'pierwszy', None, None), ('segundo', 'drugi', None, None), ('tercero', 'trzeci', None, None), ('mitad', 'połowa', None, 'rodzaj żeński'), ('par', 'para', None, 'rodzaj męski'), ('algunos', 'kilka', None, None), ('muchos', 'wiele', None, None), ('poco', 'mało', None, None), ('entero', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('minuto', 'minuta', None, 'rodzaj męski'), ('día', 'dzień', None, 'rodzaj męski'), ('noche', 'noc', None, 'rodzaj żeński'), ('semana', 'tydzień', None, 'rodzaj żeński'), ('mes', 'miesiąc', None, 'rodzaj męski'), ('año', 'rok', None, 'rodzaj męski'), ('primavera', 'wiosna', None, 'rodzaj żeński'), ('verano', 'lato', None, 'rodzaj męski'), ('otoño', 'jesień', None, 'rodzaj męski'), ('invierno', 'zima', None, 'rodzaj męski'), ('lunes', 'poniedziałek', None, 'rodzaj męski'), ('martes', 'wtorek', None, 'rodzaj męski'), ('miércoles', 'środa', None, 'rodzaj męski'), ('jueves', 'czwartek', None, 'rodzaj męski'), ('viernes', 'piątek', None, 'rodzaj męski'), ('sábado', 'sobota', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('domingo', 'niedziela', None, 'rodzaj męski'), ('enero', 'styczeń', None, 'rodzaj męski'), ('febrero', 'luty', None, 'rodzaj męski'), ('marzo', 'marzec', None, 'rodzaj męski'), ('abril', 'kwiecień', None, 'rodzaj męski'), ('mayo', 'maj', None, 'rodzaj męski'), ('junio', 'czerwiec', None, 'rodzaj męski'), ('julio', 'lipiec', None, 'rodzaj męski'), ('agosto', 'sierpień', None, 'rodzaj męski'), ('septiembre', 'wrzesień', None, 'rodzaj męski'), ('octubre', 'październik', None, 'rodzaj męski'), ('noviembre', 'listopad', None, 'rodzaj męski'), ('diciembre', 'grudzień', None, 'rodzaj męski'), ('mediodía', 'południe', None, 'rodzaj męski'), ('por la tarde', 'wieczorem', None, None), ('siempre', 'zawsze', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('nunca', 'nigdy', None, None), ('a veces', 'czasem', None, None), ('a menudo', 'często', None, None), ('ya', 'już', None, None), ('todavía', 'jeszcze', None, None), ('pronto', 'wkrótce', None, None), ('más tarde', 'później', None, None), ('temprano', 'wcześnie', None, None), ('tarde', 'późno', None, None), ('cuándo', 'kiedy (pytanie)', None, None), ('fecha', 'data', None, 'rodzaj żeński'), ('pasado', 'przeszłość', None, 'rodzaj męski'), ('futuro', 'przyszłość', None, 'rodzaj męski'), ('cumpleaños', 'urodziny', None, 'rodzaj męski'), ('fiesta', 'święto', None, 'rodzaj żeński'), ('vacaciones', 'wakacje', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('sol', 'słońce', None, 'rodzaj męski'), ('luna', 'księżyc', None, 'rodzaj żeński'), ('estrella', 'gwiazda', None, 'rodzaj żeński'), ('cielo', 'niebo', None, 'rodzaj męski'), ('nube', 'chmura', None, 'rodzaj żeński'), ('lluvia', 'deszcz', None, 'rodzaj żeński'), ('nieve', 'śnieg', None, 'rodzaj żeński'), ('viento', 'wiatr', None, 'rodzaj męski'), ('tormenta', 'burza', None, 'rodzaj żeński'), ('niebla', 'mgła', None, 'rodzaj żeński'), ('hielo', 'lód', None, 'rodzaj męski'), ('fuego', 'ogień', None, None), ('tierra', 'grunt)', None, 'rodzaj żeński'), ('río', 'rzeka', None, 'rodzaj męski'), ('lago', 'jezioro', None, 'rodzaj męski'), ('montaña', 'góra', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('bosque', 'las', None, 'rodzaj męski'), ('árbol', 'drzewo', None, 'rodzaj męski'), ('flor', 'kwiat', None, 'rodzaj żeński'), ('hierba', 'trawa', None, 'rodzaj żeński'), ('hoja', 'liść', None, 'rodzaj żeński'), ('campo', 'pole', None, 'rodzaj męski'), ('isla', 'wyspa', None, 'rodzaj żeński'), ('playa', 'plaża', None, 'rodzaj żeński'), ('desierto', 'pustynia', None, 'rodzaj męski'), ('roca', 'skała', None, 'rodzaj żeński'), ('piedra', 'kamień', None, 'rodzaj żeński'), ('tiempo', 'pogoda', None, 'rodzaj męski'), ('temperatura', 'temperatura', None, 'rodzaj żeński'), ('frío', 'zimny', None, None), ('cálido', 'ciepły', None, None), ('caliente', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('perro', 'pies', None, 'rodzaj męski'), ('gato', 'kot', None, 'rodzaj męski'), ('caballo', 'koń', None, 'rodzaj męski'), ('vaca', 'krowa', None, 'rodzaj żeński'), ('cerdo (zwierzę)', 'świnia', None, 'rodzaj męski'), ('oveja', 'owca', None, 'rodzaj żeński'), ('cabra', 'koza', None, 'rodzaj żeński'), ('gallina', 'kura', None, 'rodzaj żeński'), ('pato', 'kaczka', None, 'rodzaj męski'), ('pájaro', 'ptak', None, 'rodzaj męski'), ('ratón', 'mysz', None, 'rodzaj męski'), ('rata', 'szczur', None, 'rodzaj żeński'), ('serpiente', 'wąż', None, 'rodzaj żeński'), ('rana', 'żaba', None, 'rodzaj żeński'), ('león', 'lew', None, 'rodzaj męski'), ('tigre', 'tygrys', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('elefante', 'słoń', None, 'rodzaj męski'), ('oso', 'niedźwiedź', None, 'rodzaj męski'), ('lobo', 'wilk', None, 'rodzaj męski'), ('zorro', 'lis', None, 'rodzaj męski'), ('liebre', 'zając', None, 'rodzaj żeński'), ('ciervo', 'jeleń', None, 'rodzaj męski'), ('mono', 'małpa', None, 'rodzaj męski'), ('mariposa', 'motyl', None, 'rodzaj żeński'), ('abeja', 'pszczoła', None, 'rodzaj żeński'), ('mosca', 'mucha', None, 'rodzaj żeński'), ('araña', 'pająk', None, 'rodzaj żeński'), ('animal', 'zwierzę', None, 'rodzaj męski'), ('insecto', 'owad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('pueblo', 'wieś', None, 'rodzaj męski'), ('camino', 'droga', None, 'rodzaj męski'), ('plaza', 'plac', None, 'rodzaj żeński'), ('puente', 'most', None, 'rodzaj męski'), ('parque', 'park', None, 'rodzaj męski'), ('tienda', 'sklep', None, 'rodzaj żeński'), ('mercado', 'targ', None, 'rodzaj męski'), ('supermercado', 'supermarket', None, 'rodzaj męski'), ('banco', 'bank', None, 'rodzaj męski'), ('correos', 'poczta', None, 'rodzaj męski'), ('hospital', 'szpital', None, 'rodzaj męski'), ('farmacia', 'apteka', None, 'rodzaj żeński'), ('universidad', 'uniwersytet', None, 'rodzaj żeński'), ('biblioteca', 'biblioteka', None, 'rodzaj żeński'), ('museo', 'muzeum', None, 'rodzaj męski'), ('iglesia', 'kościół', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('restaurante', 'restauracja', None, 'rodzaj męski'), ('cafetería', 'kawiarnia', None, 'rodzaj żeński'), ('aeropuerto', 'lotnisko', None, 'rodzaj męski'), ('estación', 'dworzec', None, 'rodzaj żeński'), ('parada', 'przystanek', None, 'rodzaj żeński'), ('cine', 'kino', None, 'rodzaj męski'), ('teatro', 'teatr', None, 'rodzaj męski'), ('policía', 'policja', None, 'rodzaj żeński'), ('oficina', 'biuro', None, 'rodzaj żeński'), ('fábrica', 'fabryka', None, 'rodzaj żeński'), ('edificio', 'budynek', None, 'rodzaj męski'), ('torre', 'wieża', None, 'rodzaj żeński'), ('centro', 'centrum', None, 'rodzaj męski'), ('dirección', 'adres', None, 'rodzaj żeński'), ('mapa', 'mapa', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('coche', 'samochód', None, 'rodzaj męski'), ('autobús', 'autobus', None, 'rodzaj męski'), ('tren', 'pociąg', None, 'rodzaj męski'), ('tranvía', 'tramwaj', None, 'rodzaj męski'), ('metro', 'metro', None, 'rodzaj męski'), ('avión', 'samolot', None, 'rodzaj męski'), ('barco', 'statek', None, 'rodzaj męski'), ('bicicleta', 'rower', None, 'rodzaj żeński'), ('moto', 'motocykl', None, 'rodzaj żeński'), ('billete', 'bilet', None, 'rodzaj męski'), ('viaje', 'podróż', None, 'rodzaj męski'), ('excursión', 'wycieczka', None, 'rodzaj żeński'), ('pasaporte', 'paszport', None, 'rodzaj męski'), ('maleta', 'walizka', None, 'rodzaj żeński'), ('gasolina', 'benzyna', None, 'rodzaj żeński'), ('aparcamiento', 'parking', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('cruce', 'skrzyżowanie', None, 'rodzaj męski'), ('semáforo', 'światła', None, 'rodzaj męski'), ('carné de conducir', 'prawo jazdy', None, 'rodzaj męski'), ('conductor', 'kierowca', None, 'rodzaj męski'), ('pasajero', 'pasażer', None, 'rodzaj męski'), ('entrada', 'wjazd', None, 'rodzaj żeński'), ('salida', 'wyjazd', None, 'rodzaj żeński'), ('ferrocarril', 'kolej', None, 'rodzaj męski'), ('puerto', 'port', None, 'rodzaj męski'), ('frontera', 'granica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('trabajo', 'praca', None, 'rodzaj męski'), ('profesión', 'zawód', None, 'rodzaj żeński'), ('médico', 'lekarz', None, 'rodzaj męski'), ('enfermera', 'pielęgniarka', None, 'rodzaj żeński'), ('maestro', 'nauczyciel', None, 'rodzaj męski'), ('alumno', 'uczeń', None, 'rodzaj męski'), ('universitario', 'student', None, 'rodzaj męski'), ('ingeniero', 'inżynier', None, 'rodzaj męski'), ('abogado', 'prawnik', None, 'rodzaj męski'), ('policía (osoba)', 'policjant', None, 'rodzaj męski'), ('soldado', 'żołnierz', None, 'rodzaj męski'), ('agricultor', 'rolnik', None, 'rodzaj męski'), ('vendedor', 'sprzedawca', None, 'rodzaj męski'), ('cajero', 'kasjer', None, 'rodzaj męski'), ('actor', 'aktor', None, 'rodzaj męski'), ('escritor', 'pisarz', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('pintor', 'malarz', None, 'rodzaj męski'), ('músico', 'muzyk', None, 'rodzaj męski'), ('artista', 'artysta', None, 'rodzaj męski'), ('empresa', 'firma', None, 'rodzaj żeński'), ('dinero', 'pieniądze', None, 'rodzaj męski'), ('sueldo', 'pensja', None, 'rodzaj męski'), ('contrato', 'umowa', None, 'rodzaj męski'), ('reunión', 'spotkanie', None, 'rodzaj żeński'), ('lección', 'lekcja', None, 'rodzaj żeński'), ('examen', 'egzamin', None, 'rodzaj męski'), ('nota', 'ocena', None, 'rodzaj żeński'), ('clase', 'klasa', None, 'rodzaj żeński'), ('libro', 'książka', None, 'rodzaj męski'), ('cuaderno', 'zeszyt', None, 'rodzaj męski'), ('bolígrafo', 'długopis', None, 'rodzaj męski'), ('lápiz', 'ołówek', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('papel', 'papier', None, 'rodzaj męski'), ('pizarra', 'tablica', None, 'rodzaj żeński'), ('diccionario', 'słownik', None, 'rodzaj męski'), ('pregunta', 'pytanie', None, 'rodzaj żeński'), ('respuesta', 'odpowiedź', None, 'rodzaj żeński'), ('tarea', 'zadanie', None, 'rodzaj żeński'), ('prueba', 'test', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('precio', 'cena', None, 'rodzaj męski'), ('tarjeta', 'karta (płatnicza)', None, 'rodzaj żeński'), ('efectivo', 'gotówka', None, 'rodzaj męski'), ('moneda', 'moneta', None, 'rodzaj żeński'), ('billete (banknot)', 'banknot', None, 'rodzaj męski'), ('cambio', 'reszta', None, 'rodzaj męski'), ('descuento', 'zniżka', None, 'rodzaj męski'), ('cesta', 'koszyk', None, 'rodzaj żeński'), ('recibo', 'paragon', None, 'rodzaj męski'), ('mercancía', 'towar', None, 'rodzaj żeński'), ('compra', 'zakup', None, 'rodzaj żeński'), ('venta', 'sprzedaż', None, 'rodzaj żeński'), ('valor', 'wartość', None, 'rodzaj męski'), ('crédito', 'kredyt', None, 'rodzaj męski'), ('deuda', 'dług', None, 'rodzaj żeński'), ('impuesto', 'podatek', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('riqueza', 'bogactwo', None, 'rodzaj żeński'), ('pobre', 'biedny', None, None), ('rico', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('salud', 'zdrowie', None, 'rodzaj żeński'), ('enfermedad', 'choroba', None, 'rodzaj żeński'), ('dolor', 'ból', None, 'rodzaj męski'), ('fiebre', 'gorączka', None, 'rodzaj żeński'), ('tos', 'kaszel', None, 'rodzaj żeński'), ('resfriado', 'katar', None, 'rodzaj męski'), ('medicina', 'lekarstwo', None, 'rodzaj żeński'), ('pastilla', 'tabletka', None, 'rodzaj żeński'), ('operación', 'operacja', None, 'rodzaj żeński'), ('herida', 'rana', None, 'rodzaj żeński'), ('accidente', 'wypadek', None, 'rodzaj męski'), ('sano', 'zdrowy', None, None), ('enfermo', 'chory', None, None), ('cansado', 'zmęczony', None, None), ('soñoliento', 'śpiący', None, None), ('fuerte', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('débil', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('alegría', 'radość', None, 'rodzaj żeński'), ('tristeza', 'smutek', None, 'rodzaj żeński'), ('miedo', 'strach', None, 'rodzaj męski'), ('ira', 'gniew', None, 'rodzaj żeński'), ('amor', 'miłość', None, 'rodzaj męski'), ('odio', 'nienawiść', None, 'rodzaj męski'), ('esperanza', 'nadzieja', None, 'rodzaj żeński'), ('sueño', 'marzenie', None, 'rodzaj męski'), ('felicidad', 'szczęście', None, 'rodzaj żeński'), ('vergüenza', 'wstyd', None, 'rodzaj żeński'), ('sorpresa', 'zdziwienie', None, 'rodzaj żeński'), ('curiosidad', 'ciekawość', None, 'rodzaj żeński'), ('paciencia', 'cierpliwość', None, 'rodzaj żeński'), ('valor (odwaga)', 'odwaga', None, 'rodzaj męski'), ('sincero', 'szczery', None, None), ('amable', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('educado', 'grzeczny', None, None), ('tonto', 'głupi', None, None), ('listo', 'mądry', None, None), ('perezoso', 'leniwy', None, None), ('trabajador', 'pracowity', None, None), ('interesante', 'ciekawy', None, None), ('aburrido', 'nudny', None, None), ('alegre', 'wesoły', None, None), ('triste', 'smutny', None, None), ('enfadado', 'zły (rozgniewany)', None, None), ('feliz', 'szczęśliwy', None, None), ('enamorado', 'zakochany', None, None), ('solo', 'samotny', None, None), ('tranquilo', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('grande', 'duży', None, None), ('largo', 'długi', None, None), ('corto', 'krótki', None, None), ('alto', 'wysoki', None, None), ('bajo', 'niski', None, None), ('ancho', 'szeroki', None, None), ('estrecho', 'wąski', None, None), ('gordo', 'gruby', None, None), ('delgado', 'chudy', None, None), ('pesado', 'ciężki', None, None), ('ligero', 'lekki', None, None), ('rápido', 'szybki', None, None), ('lento', 'wolny', None, None), ('duro', 'twardy', None, None), ('blando', 'miękki', None, None), ('mojado', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('seco', 'suchy', None, None), ('limpio', 'czysty', None, None), ('sucio', 'brudny', None, None), ('lleno', 'pełny', None, None), ('vacío', 'pusty', None, None), ('afilado', 'ostry', None, None), ('ruidoso', 'głośny', None, None), ('silencioso', 'cichy', None, None), ('claro', 'jasny', None, None), ('oscuro', 'ciemny', None, None), ('joven', 'młody', None, None), ('viejo', 'stary', None, None), ('nuevo', 'nowy', None, None), ('malo', 'zły (niedobry)', None, None), ('bonito', 'ładny', None, None), ('feo', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('fácil', 'łatwy', None, None), ('difícil', 'trudny', None, None), ('importante', 'ważny', None, None), ('posible', 'możliwy', None, None), ('verdadero', 'prawdziwy', None, None), ('falso', 'fałszywy', None, None), ('caro', 'drogi', None, None), ('barato', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('ser', 'być', None, None), ('tener', 'mieć', None, None), ('hacer', 'robić', None, None), ('ir', 'iść', None, None), ('conducir', 'jechać', None, None), ('venir', 'przyjść', None, None), ('salir', 'wyjść', None, None), ('entrar', 'wejść', None, None), ('volver', 'wrócić', None, None), ('correr', 'biec', None, None), ('estar de pie', 'stać', None, None), ('estar sentado', 'siedzieć', None, None), ('estar tumbado', 'leżeć', None, None), ('dormir', 'spać', None, None), ('levantarse', 'wstać', None, None), ('comer', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('beber', 'pić', None, None), ('cocinar', 'gotować', None, None), ('lavar', 'myć', None, None), ('vestirse', 'ubierać się', None, None), ('hablar', 'mówić', None, None), ('decir', 'powiedzieć', None, None), ('preguntar', 'pytać', None, None), ('responder', 'odpowiadać', None, None), ('oír', 'słyszeć', None, None), ('escuchar', 'słuchać', None, None), ('ver', 'widzieć', None, None), ('mirar', 'patrzeć', None, None), ('leer', 'czytać', None, None), ('escribir', 'pisać', None, None), ('aprender', 'uczyć się', None, None), ('enseñar', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('entender', 'rozumieć', None, None), ('saber', 'wiedzieć', None, None), ('conocer', 'znać', None, None), ('pensar', 'myśleć', None, None), ('recordar', 'pamiętać', None, None), ('olvidar', 'zapominać', None, None), ('querer', 'chcieć', None, None), ('gustar', 'lubić', None, None), ('amar', 'kochać', None, None), ('necesitar', 'potrzebować', None, None), ('poder', 'móc', None, None), ('deber', 'musieć', None, None), ('dar', 'dawać', None, None), ('tomar', 'brać', None, None), ('comprar', 'kupować', None, None), ('vender', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('pagar', 'płacić', None, None), ('abrir', 'otwierać', None, None), ('cerrar', 'zamykać', None, None), ('empezar', 'zaczynać', None, None), ('terminar', 'kończyć', None, None), ('trabajar', 'pracować', None, None), ('jugar', 'grać', None, None), ('cantar', 'śpiewać', None, None), ('bailar', 'tańczyć', None, None), ('nadar', 'pływać', None, None), ('volar', 'latać', None, None), ('poner', 'kłaść', None, None), ('buscar', 'szukać', None, None), ('encontrar', 'znajdować', None, None), ('esperar', 'czekać', None, None), ('ayudar', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('pedir', 'prosić', None, None), ('disculparse', 'przepraszać', None, None), ('permitir', 'pozwalać', None, None), ('intentar', 'próbować', None, None), ('cambiar', 'zmieniać', None, None), ('llevar', 'nosić', None, None), ('sostener', 'trzymać', None, None), ('lanzar', 'rzucać', None, None), ('atrapar', 'łapać', None, None), ('golpear', 'bić', None, None), ('matar', 'zabijać', None, None), ('morir', 'umierać', None, None), ('vivir', 'żyć', None, None), ('habitar', 'mieszkać', None, None), ('encontrarse', 'spotykać', None, None), ('llamar', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('enviar', 'wysyłać', None, None), ('recibir', 'dostawać', None, None), ('mostrar', 'pokazywać', None, None), ('invitar', 'zapraszać', None, None), ('visitar', 'odwiedzać', None, None), ('llorar', 'płakać', None, None), ('reír', 'śmiać się', None, None), ('sonreír', 'uśmiechać się', None, None), ('temer', 'bać się', None, None), ('alegrarse', 'cieszyć się', None, None), ('creer', 'wierzyć', None, None), ('estar de acuerdo', 'zgadzać się', None, None), ('elegir', 'wybierać', None, None), ('decidir', 'decydować', None, None), ('contar', 'liczyć', None, None), ('pesar', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('caminar', 'chodzić', None, None), ('desplazarse', 'jeździć', None, None), ('subir', 'wsiadać', None, None), ('bajar', 'wysiadać', None, None), ('girar', 'skręcać', None, None), ('pararse', 'zatrzymywać się', None, None), ('llegar tarde', 'spóźniać się', None, None), ('darse prisa', 'spieszyć się', None, None), ('descansar', 'odpoczywać', None, None), ('divertirse', 'bawić się', None, None), ('dibujar', 'rysować', None, None), ('construir', 'budować', None, None), ('reparar', 'naprawiać', None, None), ('cortar', 'ciąć', None, None), ('freír', 'smażyć', None, None), ('hornear', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('mezclar', 'mieszać', None, None), ('servir', 'nalewać', None, None), ('limpiar', 'sprzątać', None, None), ('lavar la ropa', 'prać', None, None), ('planchar', 'prasować', None, None), ('afeitarse', 'golić się', None, None), ('peinar', 'czesać', None, None), ('bañarse', 'kąpać się', None, None), ('despertarse', 'budzić się', None, None), ('dormirse', 'zasypiać', None, None), ('soñar despierto', 'marzyć', None, None), ('soñar', 'śnić', None, None), ('practicar', 'ćwiczyć', None, None), ('entrenar', 'trenować', None, None), ('ganar', 'wygrywać', None, None), ('perder', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('mover', 'ruszać', None, None), ('tirar', 'ciągnąć', None, None), ('empujar', 'pchać', None, None), ('levantar', 'podnosić', None, None), ('caer', 'spadać', None, None), ('saltar', 'skakać', None, None), ('trepar', 'wspinać się', None, None), ('esconder', 'ukrywać', None, None), ('robar', 'kraść', None, None), ('devolver', 'oddawać', None, None), ('prestar', 'pożyczać', None, None), ('gastar', 'wydawać', None, None), ('ahorrar', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('este', 'ten', None, None), ('aquel', 'tamten', None, None), ('cómo', 'jak', None, None), ('por qué', 'dlaczego', None, None), ('quién', 'kto', None, None), ('cuál', 'który', None, None), ('qué tipo de', 'jaki', None, None), ('cuántos', 'ile (policzalne)', None, None), ('o', 'lub', None, None), ('si', 'jeśli', None, None), ('que', 'że', None, None), ('entonces', 'więc', None, None), ('también', 'też', None, None), ('un poco', 'trochę', None, None), ('todo', 'wszystko', None, None), ('nada', 'nic', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('algo', 'coś', None, None), ('alguien', 'ktoś', None, None), ('nadie', 'nikt', None, None), ('cada', 'każdy', None, None), ('otro', 'inny', None, None), ('el mismo', 'ten sam', None, None), ('quizás', 'może (być)', None, None), ('seguro', 'na pewno', None, None), ('juntos', 'razem', None, None), ('solo (sam)', 'sam', None, None), ('sin', 'bez', None, None), ('con', 'z (towarzysząc)', None, None), ('en', 'w (miejsce)', None, None), ('sobre', 'na (powierzchni)', None, None), ('hacia', 'do (kierunek)', None, None), ('desde', 'od', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('para', 'dla', None, None), ('por', 'przez', None, None), ('después de', 'po (czas)', None, None), ('antes de', 'przed', None, None), ('detrás de', 'za (z tyłu)', None, None), ('encima de', 'nad', None, None), ('debajo de', 'pod', None, None), ('al lado de', 'obok', None, None), ('entre', 'między', None, None), ('contra', 'przeciw', None, None), ('sobre (temat)', 'o (temat)', None, None), ('junto a', 'u (przy)', None, None), ('alrededor de', 'około', None, None), ('casi', 'prawie', None, None), ('incluso', 'nawet', None, None), ('otra vez', 'jeszcze raz', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('entonces (czas)', 'wtedy', None, None), ('en alguna parte', 'gdzieś', None, None), ('en ninguna parte', 'nigdzie', None, None), ('en todas partes', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('vida', 'życie', None, 'rodzaj żeński'), ('muerte', 'śmierć', None, 'rodzaj żeński'), ('mundo', 'świat', None, 'rodzaj męski'), ('país', 'kraj', None, 'rodzaj męski'), ('estado', 'państwo', None, 'rodzaj męski'), ('idioma', 'język (mowa)', None, 'rodzaj męski'), ('palabra', 'słowo', None, 'rodzaj żeński'), ('frase', 'zdanie', None, 'rodzaj żeński'), ('nombre', 'imię', None, 'rodzaj męski'), ('apellido', 'nazwisko', None, 'rodzaj męski'), ('edad', 'wiek', None, 'rodzaj żeński'), ('historia', 'historia', None, 'rodzaj żeński'), ('cultura', 'kultura', None, 'rodzaj żeński'), ('religión', 'religia', None, 'rodzaj żeński'), ('Dios', 'Bóg', None, 'rodzaj męski'), ('guerra', 'wojna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('paz', 'pokój (brak wojny)', None, 'rodzaj żeński'), ('ley', 'prawo (przepis)', None, 'rodzaj żeński'), ('libertad', 'wolność', None, 'rodzaj żeński'), ('gobierno', 'rząd', None, 'rodzaj męski'), ('elecciones', 'wybory', None, 'rodzaj żeński'), ('problema', 'problem', None, 'rodzaj męski'), ('idea', 'pomysł', None, 'rodzaj żeński'), ('razón', 'powód', None, 'rodzaj żeński'), ('resultado', 'wynik', None, 'rodzaj męski'), ('manera', 'sposób', None, 'rodzaj żeński'), ('comienzo', 'początek', None, 'rodzaj męski'), ('fin', 'koniec', None, 'rodzaj męski'), ('parte', 'część', None, 'rodzaj żeński'), ('lugar', 'miejsce', None, 'rodzaj męski'), ('cosa', 'rzecz', None, 'rodzaj żeński'), ('asunto', 'sprawa', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('información', 'informacja', None, 'rodzaj żeński'), ('mensaje', 'wiadomość', None, 'rodzaj męski'), ('carta (list)', 'list', None, 'rodzaj żeński'), ('periódico', 'gazeta', None, 'rodzaj męski'), ('película', 'film', None, 'rodzaj żeński'), ('música', 'muzyka', None, 'rodzaj żeński'), ('canción', 'piosenka', None, 'rodzaj żeński'), ('cuadro', 'obraz', None, 'rodzaj męski'), ('juego', 'gra', None, 'rodzaj męski'), ('deporte', 'sport', None, 'rodzaj męski'), ('partido', 'mecz', None, 'rodzaj męski'), ('equipo', 'drużyna', None, 'rodzaj męski'), ('pelota', 'piłka', None, 'rodzaj żeński'), ('diversión', 'zabawa', None, 'rodzaj żeński'), ('fiesta (impreza)', 'impreza', None, 'rodzaj żeński'), ('regalo', 'prezent', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('sueño (nocny)', 'sen', None, 'rodzaj męski'), ('plan', 'plan', None, 'rodzaj męski'), ('elección', 'wybór', None, 'rodzaj żeński'), ('error', 'błąd', None, 'rodzaj męski'), ('verdad', 'prawda', None, 'rodzaj żeński'), ('mentira', 'kłamstwo', None, 'rodzaj żeński'), ('secreto', 'tajemnica', None, 'rodzaj męski'), ('fuerza', 'siła', None, 'rodzaj żeński'), ('energía', 'energia', None, 'rodzaj żeński'), ('luz', 'światło', None, 'rodzaj żeński'), ('sonido', 'dźwięk', None, 'rodzaj męski'), ('silencio', 'cisza', None, 'rodzaj męski'), ('movimiento', 'ruch', None, 'rodzaj męski'), ('cambio (zmiana)', 'zmiana', None, 'rodzaj męski'), ('diferencia', 'różnica', None, 'rodzaj żeński'), ('ejemplo', 'przykład', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('conjunto', 'całość', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, 'rodzaj męski'), ('correo electrónico', 'e-mail', None, 'rodzaj męski'), ('contraseña', 'hasło', None, 'rodzaj żeński'), ('página web', 'strona internetowa', None, 'rodzaj żeński'), ('programa', 'program', None, 'rodzaj męski'), ('aplicación', 'aplikacja', None, 'rodzaj żeński'), ('pantalla', 'ekran', None, 'rodzaj żeński'), ('teclado', 'klawiatura', None, 'rodzaj męski'), ('ratón de ordenador', 'myszka komputerowa', None, 'rodzaj męski'), ('archivo', 'plik', None, 'rodzaj męski'), ('foto', 'zdjęcie', None, 'rodzaj żeński'), ('cámara', 'kamera', None, 'rodzaj żeński'), ('batería', 'bateria', None, 'rodzaj żeński'), ('corriente', 'prąd', None, 'rodzaj żeński'), ('cable', 'kabel', None, 'rodzaj męski'), ('máquina', 'maszyna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('herramienta', 'narzędzie', None, 'rodzaj żeński'), ('martillo', 'młotek', None, 'rodzaj męski'), ('impresora', 'drukarka', None, 'rodzaj żeński'), ('cargador', 'ładowarka', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('norte', 'północ', None, 'rodzaj męski'), ('sur', 'południe (kierunek)', None, 'rodzaj męski'), ('oeste', 'zachód', None, 'rodzaj męski'), ('Europa', 'Europa', None, 'rodzaj żeński'), ('Alemania', 'Niemcy', None, 'rodzaj żeński'), ('Francia', 'Francja', None, 'rodzaj żeński'), ('Italia', 'Włochy', None, 'rodzaj żeński'), ('Rusia', 'Rosja', None, 'rodzaj żeński'), ('Inglaterra', 'Anglia', None, 'rodzaj żeński'), ('América', 'Ameryka', None, 'rodzaj żeński'), ('China', 'Chiny', None, 'rodzaj żeński'), ('Japón', 'Japonia', None, 'rodzaj męski'), ('África', 'Afryka', None, 'rodzaj żeński'), ('Asia', 'Azja', None, 'rodzaj żeński'), ('continente', 'kontynent', None, 'rodzaj męski'), ('capital', 'stolica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('ciudadano', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('trozo', 'kawałek', None, 'rodzaj męski'), ('gota', 'kropla', None, 'rodzaj żeński'), ('caja', 'pudełko', None, 'rodzaj żeński'), ('saco', 'worek', None, 'rodzaj męski'), ('hilo', 'nić', None, 'rodzaj męski'), ('alambre', 'drut', None, 'rodzaj męski'), ('aguja', 'igła', None, 'rodzaj żeński'), ('tijeras', 'nożyczki', None, 'rodzaj żeński'), ('palo', 'kij', None, 'rodzaj męski'), ('cuerda', 'lina', None, 'rodzaj żeński'), ('cadena', 'łańcuch', None, 'rodzaj żeński'), ('tornillo', 'śruba', None, 'rodzaj męski'), ('clavo', 'gwóźdź', None, 'rodzaj męski'), ('pegamento', 'klej', None, 'rodzaj męski'), ('pintura', 'farba', None, 'rodzaj żeński'), ('vidrio', 'szkło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('madera', 'drewno', None, 'rodzaj żeński'), ('metal', 'metal', None, 'rodzaj męski'), ('oro', 'złoto', None, 'rodzaj męski'), ('plata', 'srebro', None, 'rodzaj żeński'), ('hierro', 'żelazo', None, 'rodzaj męski'), ('plástico', 'plastik', None, 'rodzaj męski'), ('cuero', 'skóra (materiał)', None, 'rodzaj męski'), ('algodón', 'bawełna', None, 'rodzaj męski'), ('lana', 'wełna', None, 'rodzaj żeński'), ('arena', 'piasek', None, 'rodzaj żeński'), ('barro', 'błoto', None, 'rodzaj męski'), ('polvo', 'kurz', None, 'rodzaj męski'), ('humo', 'dym', None, 'rodzaj męski'), ('vapor', 'para (wodna)', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('arriba', 'góra (kierunek)', None, None), ('abajo', 'dół', None, None), ('delante', 'przód', None, None), ('detrás', 'tył', None, None), ('medio', 'środek', None, 'rodzaj męski'), ('lado', 'bok', None, 'rodzaj męski'), ('dentro', 'wewnątrz', None, None), ('fuera', 'na zewnątrz', None, None), ('lejos', 'daleko', None, None), ('cerca', 'blisko', None, None), ('en lo alto', 'wysoko', None, None), ('en lo bajo', 'nisko', None, None), ('rápido (przysłówek)', 'szybko', None, None), ('despacio', 'wolno', None, None), ('mal', 'źle', None, None), ('fácilmente', 'łatwo', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('difícilmente', 'trudno', None, None), ('por separado', 'osobno', None, None), ('enfrente', 'naprzeciw', None, None), ('a lo largo de', 'wzdłuż', None, None), ('a través', 'w poprzek', None, None), ('alrededor', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('col', 'kapusta', None, 'rodzaj żeński'), ('guisante', 'groszek', None, 'rodzaj męski'), ('judía', 'fasola', None, 'rodzaj żeński'), ('seta', 'grzyb', None, 'rodzaj żeński'), ('nuez', 'orzech', None, 'rodzaj żeński'), ('ciruela', 'śliwka', None, 'rodzaj żeński'), ('cereza', 'wiśnia', None, 'rodzaj żeński'), ('melocotón', 'brzoskwinia', None, 'rodzaj męski'), ('sandía', 'arbuz', None, 'rodzaj żeński'), ('frambuesa', 'malina', None, 'rodzaj żeński'), ('salchicha', 'kiełbasa', None, 'rodzaj żeński'), ('jamón', 'szynka', None, 'rodzaj męski'), ('panecillo', 'bułka', None, 'rodzaj męski'), ('bocadillo', 'kanapka', None, 'rodzaj męski'), ('crepe', 'naleśnik', None, 'rodzaj męski'), ('yogur', 'jogurt', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('nata', 'śmietana', None, 'rodzaj żeński'), ('salsa', 'sos', None, 'rodzaj żeński'), ('vinagre', 'ocet', None, 'rodzaj męski'), ('levadura', 'drożdże', None, 'rodzaj żeński'), ('gelatina de frutas', 'kisiel', None, 'rodzaj żeński'), ('gelatina', 'galaretka', None, 'rodzaj żeński'), ('pasa', 'rodzynek', None, 'rodzaj żeński'), ('almendra', 'migdał', None, 'rodzaj żeński'), ('perejil', 'pietruszka', None, 'rodzaj męski'), ('eneldo', 'koperek', None, 'rodzaj męski'), ('pimiento', 'papryka', None, 'rodzaj męski'), ('lechuga', 'sałata', None, 'rodzaj żeński'), ('espinaca', 'szpinak', None, 'rodzaj żeński'), ('remolacha', 'burak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('suegro', 'teść', None, 'rodzaj męski'), ('suegra', 'teściowa', None, 'rodzaj żeński'), ('cuñado', 'szwagier', None, 'rodzaj męski'), ('sobrino', 'bratanek', None, 'rodzaj męski'), ('sobrina', 'siostrzenica', None, 'rodzaj żeński'), ('huérfano', 'sierota', None, 'rodzaj męski'), ('viuda', 'wdowa', None, 'rodzaj żeński'), ('prometido', 'narzeczony', None, 'rodzaj męski'), ('boda', 'ślub', None, 'rodzaj żeński'), ('divorcio', 'rozwód', None, 'rodzaj męski'), ('nacimiento', 'urodzenie', None, 'rodzaj męski'), ('entierro', 'pogrzeb', None, 'rodzaj męski'), ('peluquero', 'fryzjer', None, 'rodzaj męski'), ('panadero', 'piekarz', None, 'rodzaj męski'), ('carnicero', 'rzeźnik', None, 'rodzaj męski'), ('camarera', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('cartero', 'listonosz', None, 'rodzaj męski'), ('bombero', 'strażak', None, 'rodzaj męski'), ('juez', 'sędzia', None, 'rodzaj męski'), ('director', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
