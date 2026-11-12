"""Treść kursu: niemiecki dla Polaków.

Słowo:    (forma, znaczenie, polskie słowo pokrewne lub None, skojarzenie lub None, wymowa polskimi literami)
Litera:   (zapis, jak czytać, przykład)
Zdanie:   (lista słów, tłumaczenie, {pułapka: wyjaśnienie})
Końcówka: (przed, temat, końcówka, po, [opcje], podpowiedź, wyjaśnienie, id działu)
"""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "AUSSPRACHE · WYMOWA", "jezyk": "SPRACHE · JĘZYK"}

# Rodzajnik pokazywany przy rzeczowniku w ćwiczeniach na słowa (w zdaniach tokeny zostają bez zmian).
ARTICLES = {
    "Morgen": "der", "Tag": "der", "Abend": "der", "Nacht": "die",
    "Pole": "der", "Polin": "die", "Student": "der", "Lehrer": "der",
    "Mutter": "die", "Vater": "der", "Kind": "das", "Freund": "der", "Frau": "die", "Mann": "der",
    "Bruder": "der", "Schwester": "die",
    "Wasser": "das", "Kaffee": "der", "Tee": "der", "Brot": "das", "Käse": "der", "Wein": "der",
    "Milch": "die", "Fisch": "der", "Apfel": "der",
    "Kinder": "die", "Äpfel": "die", "Uhr": "die",
    "Haus": "das", "Stadt": "die", "Straße": "die", "Schule": "die", "Meer": "das", "Taxi": "das", "Hotel": "das",
}

# Liczba mnoga podawana od razu przy rzeczowniku (wyświetla się „der Tag, die Tage”).
PLURALS = {
    "Morgen": "die Morgen", "Tag": "die Tage", "Abend": "die Abende", "Nacht": "die Nächte",
    "Pole": "die Polen", "Polin": "die Polinnen", "Student": "die Studenten", "Lehrer": "die Lehrer",
    "Mutter": "die Mütter", "Vater": "die Väter", "Kind": "die Kinder", "Freund": "die Freunde",
    "Frau": "die Frauen", "Mann": "die Männer", "Bruder": "die Brüder", "Schwester": "die Schwestern",
    "Wasser": "die Wasser", "Kaffee": "die Kaffees", "Tee": "die Tees", "Brot": "die Brote",
    "Käse": "die Käse", "Wein": "die Weine", "Fisch": "die Fische", "Apfel": "die Äpfel",
    "Uhr": "die Uhren", "Haus": "die Häuser", "Stadt": "die Städte", "Straße": "die Straßen",
    "Schule": "die Schulen", "Meer": "die Meere", "Taxi": "die Taxis", "Hotel": "die Hotels",
}

# Z czego składa się słowo (karta nowego słowa)
PARTS = {
    "Wohnung": "wohn- (mieszkać; wohnen) + -ung (zamienia czasownik w rzeczownik) → „mieszkanie”",
    "Entschuldigung": "ent- (zdjąć, odjąć) + Schuld (wina) + -ung (rzeczownik) → „zdjęcie z siebie winy”",
    "Antwort": "ant- (w odpowiedzi, wobec) + Wort (słowo) → „słowo w odpowiedzi”",
    "Sprache": "sprech- (mówić; sprechen) + -e (rzeczownik) → „to, czym się mówi”",
}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "Ä", "track": "wymowa",
     "letters": [
         ("ch", "[x] po a, o, u; [ç] (jak ś/ch) po e, i", "Buch (buch), ich (ih)"),
         ("sch", "[ʃ]: jak polskie sz", "Schule (szkoła)"),
         ("sp, st", "na początku słowa: [ʃp], [ʃt], czyli szp, szt", "Sport (szport), Stadt (sztat)"),
         ("ei", "[aj]: jak polskie aj", "Eis (lód)"),
         ("ie", "[iː]: długie i (to nie „ie”!)", "Liebe (miłość)"),
         ("eu, äu", "[ɔj]: jak polskie oj", "neun (dziewięć)"),
         ("z", "[ts]: jak polskie c", "Zeit (czas)"),
         ("v", "[f] w słowach niemieckich", "Vater (ojciec)"),
         ("w", "[v]: jak polskie w", "Wasser (woda)"),
         ("ä", "[ɛ]: jak polskie e", "Käse (ser)"),
         ("ö", "[ø]: jak francuskie eu; usta jak do „o”, mów „e”", "schön (ładny)"),
         ("ü", "[y]: usta jak do „u”, mów „i”", "Tür (drzwi)"),
         ("ß", "[s]: długie, ostre s (ss po krótkiej samogłosce)", "Straße (ulica)"),
         ("j", "[j]: jak polskie j", "ja (tak)"),
         ("s", "przed samogłoską [z]: jak polskie z", "Sonne (słońce)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "H", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("hallo", "cześć", "halo", None),
         ("tschüss", "pa", None, "Z hiszpańskiego „adiós” przez dolnoniemiecki."),
         ("guten", "dobry (do Morgen, Tag, Abend)", None, None),
         ("gute", "dobra (do Nacht)", None, "Nacht jest żeńskie, więc gute."),
         ("Morgen", "ranek", "morga (miara pola)", "Morga to tyle ziemi, ile zaorze się w jeden ranek."),
         ("Tag", "dzień", None, None),
         ("Abend", "wieczór", None, None),
         ("Nacht", "noc", None, None),
         ("danke", "dziękuję", None, None),
         ("bitte", "proszę", None, None),
         ("ja", "tak", None, None),
         ("nein", "nie", None, None),
         ("sehr", "bardzo", None, None),
         ("und", "i", None, None),
         ("Entschuldigung", "przepraszam", None, None),
     ],
     "sentences": [
         (["hallo", "!"], "Cześć!", {"tschüss": "tschüss to „pa” na pożegnanie."}),
         (["guten", "Morgen", "!"], "Dzień dobry (rano)!", {"Abend": "Abend to „wieczór”. Rano: Morgen."}),
         (["guten", "Abend", "!"], "Dobry wieczór!", {"Morgen": "Morgen to „ranek”."}),
         (["gute", "Nacht", "!"], "Dobranoc!", {"guten": "Nacht jest żeńskie, więc gute, nie guten."}),
         (["danke", "sehr"], "Dziękuję bardzo.", {"bitte": "bitte to „proszę”. Tu dziękujesz."}),
         (["ja", ",", "danke"], "Tak, dziękuję.", {"nein": "nein to „nie”."}),
         (["nein", ",", "danke"], "Nie, dziękuję.", {"ja": "ja to „tak”."}),
         (["Entschuldigung", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "I", "track": "jezyk",
     "words": [
         ("ich", "ja", None, "Czytaj [ih], z miękkim ch."),
         ("du", "ty", None, None),
         ("er", "on", None, None),
         ("sie", "ona; oni", None, "Czytaj [zi], nie „sie”."),
         ("bin", "jestem", None, None),
         ("bist", "jesteś", None, None),
         ("ist", "jest", None, None),
         ("Pole", "Polak", None, None),
         ("Polin", "Polka", None, None),
         ("Student", "student", "student", None),
         ("Lehrer", "nauczyciel", None, None),
         ("aus", "z", None, None),
         ("Polen", "Polska", None, None),
         ("Deutschland", "Niemcy", None, "Deutsch znaczy dosłownie „ludowy” (język ludu)."),
     ],
     "sentences": [
         (["ich", "bin", "Student"], "Jestem studentem.", {"bist": "bist to „jesteś”. O sobie: bin."}),
         (["du", "bist", "Lehrer"], "Jesteś nauczycielem.", {"bin": "bin to „jestem”. Do „du”: bist."}),
         (["er", "ist", "Pole"], "On jest Polakiem.", {"bist": "bist to „jesteś”. O „er”: ist."}),
         (["sie", "ist", "Polin"], "Ona jest Polką.", {"Pole": "Dla kobiety: Polin."}),
         (["ich", "bin", "aus", "Polen"], "Jestem z Polski.", {"Deutschland": "Deutschland to Niemcy."}),
         (["sie", "ist", "aus", "Deutschland"], "Ona jest z Niemiec.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "D", "track": "jezyk",
     "words": [
         ("der", "(rodzajnik męski)", None, "Der Vater, der Mann, der Freund."),
         ("die", "(rodzajnik żeński)", None, "Die Mutter, die Frau, die Schwester."),
         ("das", "(rodzajnik nijaki)", None, "Das Kind, das Haus."),
         ("Mutter", "matka", None, None),
         ("Vater", "ojciec", None, None),
         ("Kind", "dziecko", None, "Po angielsku kinder-garten: ogród dla dzieci."),
         ("Freund", "przyjaciel", None, None),
         ("Frau", "kobieta; żona", None, None),
         ("Mann", "mężczyzna; mąż", None, None),
         ("Bruder", "brat", None, None),
         ("Schwester", "siostra", None, None),
         ("habe", "mam", None, None),
         ("hast", "masz", None, None),
         ("klein", "mały", None, None),
         ("gut", "dobry", None, None),
         ("einen", "jakiegoś (biernik, rodzaj męski)", None, None),
         ("eine", "jakąś (rodzaj żeński)", None, None),
         ("ein", "jakiś (nijaki); jeden", None, None),
     ],
     "sentences": [
         (["der", "Freund", "ist", "gut"], "Przyjaciel jest dobry.", {"die": "Freund jest męski: der."}),
         (["die", "Mutter", "ist", "eine", "Frau"], "Matka jest kobietą.", {"der": "Mutter jest żeńska: die."}),
         (["das", "Kind", "ist", "klein"], "Dziecko jest małe.", {"die": "Kind jest nijakie: das."}),
         (["ich", "habe", "einen", "Bruder"], "Mam brata.", {"hast": "hast to „masz”. O sobie: habe.", "eine": "Bruder jest męski, więc w bierniku: einen."}),
         (["du", "hast", "eine", "Schwester"], "Masz siostrę.", {"habe": "habe to „mam”. Do „du”: hast.", "einen": "Schwester jest żeńska: eine."}),
         (["der", "Vater", "ist", "ein", "Mann"], "Ojciec jest mężczyzną.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "K", "track": "jezyk",
     "words": [
         ("Wasser", "woda", None, None),
         ("Kaffee", "kawa", None, None),
         ("Tee", "herbata", None, None),
         ("Brot", "chleb", None, None),
         ("Käse", "ser", None, None),
         ("Wein", "wino", None, None),
         ("Milch", "mleko", None, None),
         ("Fisch", "ryba", None, None),
         ("Apfel", "jabłko", None, None),
         ("möchte", "chciałbym; chciałabym", None, "Grzeczne „chcę”: ten sam rdzeń co „mogę”."),
         ("möchtest", "chciałbyś; chciałabyś", None, None),
         ("etwas", "trochę; coś", None, None),
         ("jetzt", "teraz", None, None),
     ],
     "sentences": [
         (["ich", "möchte", "einen", "Kaffee"], "Poproszę kawę.", {"möchtest": "möchtest to „chciałbyś”. O sobie: möchte.", "eine": "Kaffee jest męski, więc einen."}),
         (["ich", "möchte", "Wasser", ",", "bitte"], "Poproszę wodę.", {}),
         (["du", "möchtest", "Tee"], "Chcesz herbatę.", {"möchte": "möchte to „chciałbym”. Do „du”: möchtest."}),
         (["ich", "möchte", "etwas", "Brot"], "Chcę trochę chleba.", {}),
         (["der", "Fisch", "ist", "sehr", "gut"], "Ryba jest bardzo dobra.", {}),
         (["ich", "möchte", "jetzt", "eine", "Milch"], "Chcę teraz mleka.", {"einen": "Milch jest żeńskie: eine."}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("zwei", "dwa", None, None),
         ("drei", "trzy", None, None),
         ("vier", "cztery", None, "v czytamy f: fir."),
         ("fünf", "pięć", None, None),
         ("zehn", "dziesięć", None, None),
         ("Kinder", "dzieci", None, "Liczba mnoga od Kind."),
         ("Äpfel", "jabłka", None, "Liczba mnoga od Apfel (a → ä)."),
         ("heute", "dziś", None, None),
         ("morgen", "jutro", None, "Z małej litery to „jutro”, z dużej (Morgen) „ranek”."),
         ("gestern", "wczoraj", None, None),
         ("Uhr", "godzina; zegar", None, None),
         ("wie", "jak", None, None),
         ("spät", "późno", None, None),
         ("es", "to; ono", None, None),
     ],
     "sentences": [
         (["ich", "habe", "zwei", "Kinder"], "Mam dwoje dzieci.", {}),
         (["ich", "möchte", "drei", "Äpfel"], "Chcę trzy jabłka.", {"zwei": "zwei to „dwa”. Chcesz trzy: drei."}),
         (["wie", "spät", "ist", "es", "?"], "Która jest godzina?", {}),
         (["es", "ist", "zehn", "Uhr"], "Jest dziesiąta.", {}),
         (["heute", "möchte", "ich", "einen", "Kaffee"], "Dziś chcę kawę.", {"morgen": "morgen to „jutro”. Tu „dziś”: heute."}),
         (["morgen", "möchte", "ich", "Fisch"], "Jutro chcę rybę.", {"gestern": "gestern to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "S", "track": "jezyk",
     "words": [
         ("Haus", "dom", None, None),
         ("Stadt", "miasto", None, "Stadt i polskie „stan” mają ten sam rdzeń: coś, co stoi."),
         ("Straße", "ulica", None, "Ten sam rdzeń co angielskie „street”."),
         ("Schule", "szkoła", None, None),
         ("Meer", "morze", None, None),
         ("Taxi", "taksówka", "taksówka", None),
         ("Hotel", "hotel", "hotel", None),
         ("wo", "gdzie", None, None),
         ("hier", "tu", None, None),
         ("dort", "tam", None, None),
         ("gehe", "idę; jadę", None, None),
         ("nach", "do (kraju, domu)", None, "Nach Hause: do domu."),
         ("Hause", "domu (w nach Hause)", None, None),
         ("in", "do; w", None, None),
         ("rechts", "w prawo", None, None),
         ("links", "w lewo", None, None),
     ],
     "sentences": [
         (["wo", "ist", "das", "Hotel", "?"], "Gdzie jest hotel?", {"hier": "hier to „tu”, a pytasz „gdzie”: wo."}),
         (["das", "Hotel", "ist", "dort"], "Hotel jest tam.", {"hier": "hier to „tu”. Tu mówimy „tam”: dort."}),
         (["ich", "gehe", "nach", "Hause"], "Idę do domu.", {"in": "Do domu mówi się nach Hause."}),
         (["ich", "gehe", "in", "die", "Stadt"], "Idę do miasta.", {"das": "Stadt jest żeńskie: die."}),
         (["das", "Taxi", "ist", "rechts"], "Taksówka jest po prawej.", {"links": "links to „w lewo”."}),
         (["die", "Schule", "ist", "dort"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Czytaj, co widzisz", "chain": [],
                "text": "Niemiecki jest w większości fonetyczny, tylko z innymi regułami niż polski: ei czytasz [aɪ], ie czytasz [iː] (długie), w czytasz [v], a v zwykle [f]. Zapamiętaj te cztery pułapki, a przeczytasz prawie wszystko."}],
    "ja": [{"title": "Sein: nieregularny, ale krótki", "chain": [
                ("Jestem studentem.", ["ich", "bin", "Student"], "Do „ich” pasuje bin."),
                ("Jesteś nauczycielem.", ["du", "bist", "Lehrer"], "Do „du” pasuje bist."),
            ],
            "text": "Po niemiecku zaimek jest obowiązkowy: ich bin, du bist, er ist. Czasownik „być” jest nieregularny, więc po prostu zapamiętaj te trzy formy."}],
    "ludzie": [{"title": "Rodzajnik: der, die, das", "chain": [],
                "text": "Każdy rzeczownik ma rodzaj: der (męski), die (żeński), das (nijaki). Uczysz się go razem z rodzajnikiem: der Vater, die Mutter, das Kind. Rzeczowniki piszemy zawsze wielką literą."}],
    "jedzenie": [{"title": "Biernik: tylko męski się zmienia", "chain": [],
                  "text": "Po „möchte” i „habe” rzeczownik stoi w bierniku. Zmienia się tylko rodzaj męski: ein Kaffee → ich möchte einen Kaffee. Żeński (eine) i nijaki (ein) zostają bez zmian."}],
}

ENDINGS_INSIGHT = {"title": "Rodzajniki i końcówki",
                   "text": "Po niemiecku warto znać rodzaj (der, die, das) i formy czasownika (-e, -st, -t). Tu to ćwiczysz."}

ENDINGS = [
    ("guten ", "", "Morgen", "", ["Morgen", "Abend", "Nacht"], "dzień dobry (rano)", "Morgen to „ranek”, Abend „wieczór”; do Nacht mówi się gute.", "slowa"),
    ("guten ", "", "Abend", "", ["Morgen", "Abend", "Nacht"], "dobry wieczór", "Abend to „wieczór”.", "slowa"),
    ("gute ", "", "Nacht", "", ["Morgen", "Abend", "Nacht"], "dobranoc", "Nacht to „noc”.", "slowa"),
    ("ich ", "", "bin", " Student", ["bin", "bist", "ist"], "ja jestem", "Do „ich” pasuje bin.", "ja"),
    ("du ", "", "bist", " Lehrer", ["bin", "bist", "ist"], "ty jesteś", "Do „du” pasuje bist.", "ja"),
    ("er ", "", "ist", " Pole", ["bin", "bist", "ist"], "on jest", "Do „er” pasuje ist.", "ja"),
    ("", "", "der", " Vater", ["der", "die", "das"], "ten ojciec", "Vater jest męski: der.", "ludzie"),
    ("", "", "die", " Mutter", ["der", "die", "das"], "ta matka", "Mutter jest żeńska: die.", "ludzie"),
    ("", "", "das", " Kind", ["der", "die", "das"], "to dziecko", "Kind jest nijakie: das.", "ludzie"),
    ("ich ", "hab", "e", " einen Bruder", ["e", "st", "t"], "ja mam", "Do „ich” pasuje -e: habe.", "ludzie"),
    ("du ", "ha", "st", " eine Schwester", ["e", "st", "t"], "ty masz", "Do „du” pasuje -st: hast.", "ludzie"),
    ("ich möchte ", "", "einen", " Kaffee", ["einen", "eine", "ein"], "jakąś kawę (męski)", "Kaffee jest męski; po „möchte” biernik: einen.", "jedzenie"),
    ("ich möchte ", "", "eine", " Milch", ["einen", "eine", "ein"], "jakieś mleko (żeński)", "Milch jest żeńskie: eine.", "jedzenie"),
    ("ich möchte ", "", "ein", " Brot", ["einen", "eine", "ein"], "jakiś chleb (nijaki)", "Brot jest nijakie: ein.", "jedzenie"),
    ("ich gehe ", "", "in", " die Stadt", ["in", "nach"], "do miasta", "Do miasta: in die Stadt. Nach używa się przy krajach i „nach Hause”.", "miejsca"),
]

CHAT_EXTRA = {"Anna": "Anna (imię)", "Max": "Max (imię)", "Herr": "pan", "Kellner": "kelner", "geht": "idzie; jedzie",
              "Name": "imię; nazwisko", "heiße": "nazywam się", "wohin": "dokąd", "fahren": "jechać", "gern": "chętnie"}

CHATS = [
    {"id": "cafe", "title": "W kawiarni", "partner": "Anna", "avatar": "A", "requires": "jedzenie",
     "turns": [
         {"bot": ["guten", "Morgen", "!"], "en": "Dzień dobry!",
          "options": [(["guten", "Morgen", "!"], True, None), (["gute", "Nacht", "!"], False, "gute Nacht to „dobranoc”. Jest ranek.")]},
         {"bot": ["möchtest", "du", "einen", "Kaffee", "?"], "en": "Chcesz kawę?",
          "options": [(["ja", ",", "ich", "möchte", "einen", "Kaffee"], True, None),
                      (["ja", ",", "ich", "möchtest", "einen", "Kaffee"], False, "möchtest jest do „du”. O sobie: möchte.")]},
         {"bot": ["und", "etwas", "Brot", "?"], "en": "I trochę chleba?",
          "options": [(["nein", ",", "danke"], True, None),
                      (["bitte", "sehr"], False, "bitte sehr to „proszę bardzo” (gdy coś podajesz). Odmów: nein, danke.")]},
         {"bot": ["gut", "!"], "build": (["danke", "sehr"], "Dziękuję bardzo."), "en": "Dobrze!"},
     ]},
    {"id": "kennenlernen", "title": "Poznajemy się", "partner": "Max", "avatar": "M", "requires": "ludzie",
     "turns": [
         {"bot": ["hallo", "!"], "en": "Cześć!",
          "options": [(["hallo", "!"], True, None), (["Entschuldigung", "!"], False, "Entschuldigung to „przepraszam”. Powitaj: hallo.")]},
         {"bot": ["bist", "du", "aus", "Deutschland", "?"], "en": "Jesteś z Niemiec?",
          "options": [(["nein", ",", "ich", "bin", "aus", "Polen"], True, None),
                      (["nein", ",", "ich", "bist", "aus", "Polen"], False, "bist jest do „du”. O sobie: bin.")]},
         {"bot": ["hast", "du", "einen", "Bruder", "?"], "en": "Masz brata?",
          "options": [(["ja", ",", "ich", "habe", "einen", "Bruder"], True, None),
                      (["ja", ",", "ich", "hast", "einen", "Bruder"], False, "hast jest do „du”. O sobie: habe.")]},
         {"bot": ["guten", "Abend", "!"], "build": (["guten", "Abend"], "Dobry wieczór."), "en": "Dobry wieczór!"},
     ]},
    {"id": "taxi", "title": "W taksówce", "partner": "Herr", "avatar": "H", "requires": "miejsca",
     "turns": [
         {"bot": ["guten", "Abend", "!"], "en": "Dobry wieczór!",
          "options": [(["guten", "Abend", "!"], True, None), (["guten", "Morgen", "!"], False, "Morgen to „ranek”. Jest wieczór.")]},
         {"bot": ["wohin", "?"], "en": "Dokąd?",
          "options": [(["ich", "gehe", "in", "die", "Stadt"], True, None),
                      (["ich", "gehe", "nach", "die", "Stadt"], False, "Do miasta: in die Stadt, nie nach.")]},
         {"bot": ["das", "Hotel", "ist", "dort", "."], "en": "Hotel jest tam.",
          "options": [(["rechts", "?"], True, None), (["hier", "?"], False, "Pytasz o kierunek: rechts (w prawo) albo links.")]},
         {"bot": ["ja", "!"], "build": (["danke", "sehr"], "Dziękuję bardzo."), "en": "Tak!"},
     ]},
]

# === BULK: generowane z langs/bulk/german.txt (nie edytuj ręcznie) ===
UNITS += [{'id': 'f01', 'title': 'Małe słowa', 'icon': 'M', 'track': 'jezyk', 'words': [('nicht', 'nie', None, None), ('auch', 'też', None, None), ('aber', 'ale', None, None), ('oder', 'albo, czy', None, None), ('nur', 'tylko', None, None), ('noch', 'jeszcze', None, None), ('schon', 'już', None, None), ('immer', 'zawsze', None, None), ('wieder', 'znów', None, None), ('viel', 'dużo', None, None), ('mehr', 'więcej', None, None), ('viele', 'wiele', None, None), ('hat', 'ma (on, ona, ono)', None, None)], 'sentences': [(['ich', 'bin', 'nicht', 'klein', '.'], 'Nie jestem mały.', {}), (['du', 'bist', 'auch', 'gut', '.'], 'Ty też jesteś dobry.', {}), (['ich', 'habe', 'Kaffee', ',', 'aber', 'du', 'hast', 'Tee', '.'], 'Ja mam kawę, ale ty masz herbatę.', {}), (['möchtest', 'du', 'Kaffee', 'oder', 'Tee', '?'], 'Chcesz kawę czy herbatę?', {}), (['ich', 'habe', 'nur', 'Wasser', '.'], 'Mam tylko wodę.', {}), (['er', 'hat', 'noch', 'Milch', '.'], 'On ma jeszcze mleko.', {}), (['das', 'Kind', 'hat', 'schon', 'Brot', '.'], 'Dziecko ma już chleb.', {}), (['ich', 'habe', 'immer', 'Kaffee', '.'], 'Zawsze mam kawę.', {}), (['ich', 'habe', 'viel', 'Wasser', '.'], 'Mam dużo wody.', {}), (['möchtest', 'du', 'mehr', 'Käse', '?'], 'Chcesz więcej sera?', {}), (['heute', 'bin', 'ich', 'wieder', 'hier', '.'], 'Dzisiaj znów tu jestem.', {}), (['es', 'ist', 'nicht', 'gut', '.'], 'To nie jest dobre.', {}), (['die', 'Frau', 'hat', 'auch', 'Tee', '.'], 'Kobieta też ma herbatę.', {}), (['er', 'ist', 'noch', 'klein', ',', 'aber', 'sehr', 'gut', '.'], 'On jest jeszcze mały, ale bardzo dobry.', {}), (['ich', 'bin', 'schon', 'hier', '.'], 'Jestem już tutaj.', {}), (['du', 'hast', 'nur', 'Brot', 'und', 'Käse', '.'], 'Masz tylko chleb i ser.', {}), (['hat', 'er', 'auch', 'Wein', '?'], 'Czy on też ma wino?', {}), (['sie', 'hat', 'nicht', 'viel', 'Milch', '.'], 'Ona nie ma dużo mleka.', {})]}, {'id': 'f02', 'title': 'My, wy i mój', 'icon': 'W', 'track': 'jezyk', 'words': [('wir', 'my', None, None), ('ihr', 'wy', None, None), ('sind', 'są, jesteśmy', None, None), ('seid', 'jesteście', None, None), ('haben', 'mamy, mają', None, None), ('habt', 'macie', None, None), ('mein', 'mój', None, None), ('meine', 'moja, moje', None, None), ('dein', 'twój', None, None), ('deine', 'twoja, twoje', None, None), ('unser', 'nasz', None, None)], 'sentences': [(['wir', 'sind', 'hier', '.'], 'Jesteśmy tutaj.', {}), (['wir', 'haben', 'Kaffee', '.'], 'Mamy kawę.', {}), (['ihr', 'seid', 'gut', '.'], 'Jesteście dobrzy.', {}), (['habt', 'ihr', 'Wasser', '?'], 'Macie wodę?', {}), (['sie', 'sind', 'Lehrer', '.'], 'Oni są nauczycielami.', {}), (['meine', 'Mutter', 'ist', 'hier', '.'], 'Moja mama jest tutaj.', {}), (['mein', 'Vater', 'hat', 'ein', 'Haus', '.'], 'Mój tata ma dom.', {}), (['dein', 'Bruder', 'ist', 'nicht', 'hier', '.'], 'Twojego brata tu nie ma.', {}), (['deine', 'Schwester', 'hat', 'noch', 'Milch', '.'], 'Twoja siostra ma jeszcze mleko.', {}), (['wir', 'haben', 'ein', 'Kind', '.'], 'Mamy dziecko.', {}), (['unser', 'Haus', 'ist', 'klein', '.'], 'Nasz dom jest mały.', {}), (['mein', 'Freund', 'ist', 'nicht', 'hier', '.'], 'Mojego przyjaciela tu nie ma.', {}), (['ihr', 'habt', 'viel', 'Brot', '.'], 'Macie dużo chleba.', {}), (['wir', 'sind', 'schon', 'in', 'der', 'Stadt', '.'], 'Jesteśmy już w mieście.', {}), (['sie', 'haben', 'auch', 'ein', 'Haus', '.'], 'Oni też mają dom.', {}), (['meine', 'Schwester', 'und', 'mein', 'Bruder', 'sind', 'Lehrer', '.'], 'Moja siostra i mój brat są nauczycielami.', {})]}, {'id': 'f03', 'title': 'Pytania', 'icon': 'P', 'track': 'jezyk', 'words': [('was', 'co', None, None), ('wer', 'kto', None, None), ('wann', 'kiedy', None, None), ('warum', 'dlaczego', None, None), ('kein', 'żaden, nie (przed rzeczownikiem rodzaju męskiego i nijakiego)', None, None), ('keine', 'nie (przed rzeczownikiem rodzaju żeńskiego i w lm.)', None, None), ('keinen', 'nie (przed rzeczownikiem rodzaju męskiego, biernik)', None, None)], 'sentences': [(['was', 'ist', 'das', '?'], 'Co to jest?', {}), (['wer', 'ist', 'das', '?'], 'Kto to jest?', {}), (['wer', 'bist', 'du', '?'], 'Kim jesteś?', {}), (['was', 'hast', 'du', '?'], 'Co masz?', {}), (['wann', 'bist', 'du', 'hier', '?'], 'Kiedy tu jesteś?', {}), (['warum', 'bist', 'du', 'nicht', 'hier', '?'], 'Dlaczego cię tu nie ma?', {}), (['was', 'möchtest', 'du', '?'], 'Czego chcesz?', {}), (['wo', 'ist', 'mein', 'Kaffee', '?'], 'Gdzie jest moja kawa?', {}), (['wer', 'hat', 'Milch', '?'], 'Kto ma mleko?', {}), (['warum', 'hast', 'du', 'nur', 'Wasser', '?'], 'Dlaczego masz tylko wodę?', {}), (['was', 'haben', 'wir', 'heute', '?'], 'Co mamy dzisiaj?', {}), (['wo', 'ist', 'die', 'Schule', '?'], 'Gdzie jest szkoła?', {}), (['wer', 'ist', 'die', 'Frau', '?'], 'Kim jest ta kobieta?', {}), (['ich', 'habe', 'kein', 'Brot', '.'], 'Nie mam chleba.', {}), (['wir', 'haben', 'keine', 'Milch', '.'], 'Nie mamy mleka.', {}), (['er', 'hat', 'kein', 'Haus', '.'], 'On nie ma domu.', {}), (['wann', 'habt', 'ihr', 'Schule', '?'], 'Kiedy macie szkołę?', {}), (['warum', 'hat', 'er', 'keinen', 'Kaffee', '?'], 'Dlaczego on nie ma kawy?', {})]}, {'id': 'f04', 'title': 'Przyimki', 'icon': 'Z', 'track': 'jezyk', 'words': [('mit', 'z', None, None), ('für', 'dla', None, None), ('von', 'od, z', None, None), ('zu', 'do, u, na', None, None), ('den', '(rodzajnik: biernik r. męskiego, celownik lm.)', None, None), ('auf', 'na', None, None), ('bei', 'u, przy', None, None), ('im', 'w (w + dem)', None, None), ('am', 'przy, nad (an + dem)', None, None), ('zum', 'do (zu + dem)', None, None), ('zur', 'do (zu + der)', None, None), ('dem', 'temu (celownik: der, das)', None, None)], 'sentences': [(['ich', 'bin', 'mit', 'dem', 'Bruder', 'in', 'der', 'Stadt', '.'], 'Jestem z bratem w mieście.', {}), (['das', 'Brot', 'ist', 'für', 'das', 'Kind', '.'], 'Chleb jest dla dziecka.', {}), (['der', 'Kaffee', 'ist', 'für', 'die', 'Frau', '.'], 'Kawa jest dla kobiety.', {}), (['das', 'Haus', 'von', 'dem', 'Lehrer', 'ist', 'klein', '.'], 'Dom nauczyciela jest mały.', {}), (['ich', 'gehe', 'zum', 'Hotel', '.'], 'Idę do hotelu.', {}), (['ich', 'gehe', 'zur', 'Schule', '.'], 'Idę do szkoły.', {}), (['ich', 'bin', 'am', 'Meer', '.'], 'Jestem nad morzem.', {}), (['wir', 'sind', 'im', 'Hotel', '.'], 'Jesteśmy w hotelu.', {}), (['das', 'Kind', 'ist', 'bei', 'der', 'Mutter', '.'], 'Dziecko jest u mamy.', {}), (['der', 'Käse', 'ist', 'auf', 'dem', 'Brot', '.'], 'Ser jest na chlebie.', {}), (['ich', 'gehe', 'zu', 'dem', 'Lehrer', '.'], 'Idę do nauczyciela.', {}), (['der', 'Student', 'ist', 'im', 'Haus', '.'], 'Student jest w domu.', {}), (['ich', 'bin', 'am', 'Abend', 'zu', 'Hause', '.'], 'Wieczorem jestem w domu.', {}), (['ich', 'habe', 'Brot', 'mit', 'Käse', '.'], 'Mam chleb z serem.', {}), (['ich', 'gehe', 'mit', 'dem', 'Freund', 'in', 'die', 'Schule', '.'], 'Idę z kolegą do szkoły.', {}), (['das', 'Wasser', 'ist', 'für', 'den', 'Vater', '.'], 'Woda jest dla taty.', {}), (['meine', 'Mutter', 'ist', 'im', 'Hotel', '.'], 'Moja mama jest w hotelu.', {})]}, {'id': 'f05', 'title': 'Ja, ty i inni w zdaniu', 'icon': 'J', 'track': 'jezyk', 'words': [('mich', 'mnie', None, None), ('dich', 'ciebie', None, None), ('mir', 'mi, mnie', None, None), ('dir', 'ci, tobie', None, None), ('uns', 'nas, nam', None, None), ('ihn', 'jego (biernik)', None, None), ('ihm', 'jemu, nim', None, None), ('gehst', 'idziesz', None, None), ('geht', 'idzie, idzie się', None, None), ('gehen', 'iść, idziemy, idą', None, None)], 'sentences': [(['der', 'Kaffee', 'ist', 'für', 'mich', '.'], 'Kawa jest dla mnie.', {}), (['das', 'Wasser', 'ist', 'für', 'dich', '.'], 'Woda jest dla ciebie.', {}), (['das', 'Brot', 'ist', 'für', 'uns', '.'], 'Chleb jest dla nas.', {}), (['die', 'Milch', 'ist', 'für', 'ihn', '.'], 'Mleko jest dla niego.', {}), (['ich', 'bin', 'bei', 'dir', '.'], 'Jestem u ciebie.', {}), (['er', 'ist', 'bei', 'mir', '.'], 'On jest u mnie.', {}), (['das', 'Kind', 'ist', 'bei', 'ihm', '.'], 'Dziecko jest u niego.', {}), (['ich', 'gehe', 'mit', 'dir', '.'], 'Idę z tobą.', {}), (['gehst', 'du', 'mit', 'mir', '?'], 'Idziesz ze mną?', {}), (['wir', 'gehen', 'mit', 'ihm', '.'], 'Idziemy z nim.', {}), (['er', 'geht', 'mit', 'uns', 'in', 'die', 'Stadt', '.'], 'On idzie z nami do miasta.', {}), (['mein', 'Bruder', 'geht', 'mit', 'dir', 'in', 'die', 'Schule', '.'], 'Mój brat chodzi z tobą do szkoły.', {}), (['wie', 'geht', 'es', 'dir', '?'], 'Jak się masz?', {}), (['es', 'geht', 'mir', 'gut', '.'], 'Mam się dobrze.', {}), (['wie', 'geht', 'es', 'ihm', '?'], 'Jak on się ma?', {}), (['das', 'Taxi', 'ist', 'für', 'uns', '.'], 'Taksówka jest dla nas.', {}), (['ich', 'habe', 'ihn', 'und', 'dich', '.'], 'Mam jego i ciebie.', {}), (['gehen', 'wir', 'in', 'die', 'Stadt', '?'], 'Idziemy do miasta?', {})]}, {'id': 'f06', 'title': 'Codzienne czasowniki', 'icon': 'C', 'track': 'jezyk', 'words': [('komme', 'przychodzę, pochodzę', None, None), ('kommst', 'przychodzisz, pochodzisz', None, None), ('kommt', 'przychodzi, przychodzicie', None, None), ('kommen', 'przychodzić, przychodzimy', None, None), ('mache', 'robię', None, None), ('machst', 'robisz', None, None), ('macht', 'robi, robicie', None, None), ('machen', 'robić, robimy', None, None), ('trinke', 'piję', None, None), ('trinkst', 'pijesz', None, None), ('trinkt', 'pije, pijecie', None, None), ('trinken', 'pić, pijemy', None, None), ('esse', 'jem', None, None), ('isst', 'jesz, je', None, None), ('essen', 'jeść, jemy', None, None), ('esst', 'jecie', None, None)], 'sentences': [(['ich', 'komme', 'aus', 'Polen', '.'], 'Pochodzę z Polski.', {}), (['kommst', 'du', 'aus', 'Deutschland', '?'], 'Pochodzisz z Niemiec?', {}), (['er', 'kommt', 'heute', 'nicht', '.'], 'On dzisiaj nie przyjdzie.', {}), (['wir', 'kommen', 'am', 'Abend', '.'], 'Przyjdziemy wieczorem.', {}), (['kommt', 'ihr', 'mit', 'uns', '?'], 'Przyjdziecie z nami?', {}), (['was', 'machst', 'du', '?'], 'Co robisz?', {}), (['was', 'macht', 'er', '?'], 'Co on robi?', {}), (['ich', 'mache', 'Kaffee', '.'], 'Robię kawę.', {}), (['wir', 'machen', 'Tee', '.'], 'Robimy herbatę.', {}), (['was', 'machen', 'wir', 'heute', '?'], 'Co robimy dzisiaj?', {}), (['ich', 'trinke', 'Wasser', '.'], 'Piję wodę.', {}), (['du', 'trinkst', 'viel', 'Kaffee', '.'], 'Pijesz dużo kawy.', {}), (['das', 'Kind', 'trinkt', 'Milch', '.'], 'Dziecko pije mleko.', {}), (['sie', 'trinken', 'Tee', '.'], 'Oni piją herbatę.', {}), (['ich', 'esse', 'Brot', 'mit', 'Käse', '.'], 'Jem chleb z serem.', {}), (['er', 'isst', 'einen', 'Apfel', '.'], 'On je jabłko.', {}), (['was', 'isst', 'du', '?'], 'Co jesz?', {}), (['wir', 'essen', 'Fisch', '.'], 'Jemy rybę.', {}), (['ihr', 'trinkt', 'und', 'ihr', 'esst', '.'], 'Pijecie i jecie.', {}), (['er', 'kommt', 'auch', 'aus', 'Polen', '.'], 'On też pochodzi z Polski.', {})]}, {'id': 'f07', 'title': 'Jaki?', 'icon': 'J', 'track': 'jezyk', 'words': [('alt', 'stary', None, None), ('neu', 'nowy', None, None), ('groß', 'duży, wysoki', None, None), ('lang', 'długi', None, None), ('lange', 'długi (przed rzeczownikiem żeńskim); długo', None, None), ('schön', 'piękny', None, None), ('schnell', 'szybki, szybko', None, None), ('jung', 'młody', None, None), ('großes', 'duży (przed rzeczownikiem nijakim)', None, None), ('neues', 'nowy (przed rzeczownikiem nijakim)', None, None), ('schönes', 'piękny (przed rzeczownikiem nijakim)', None, None)], 'sentences': [(['das', 'Haus', 'ist', 'groß', '.'], 'Dom jest duży.', {}), (['das', 'Hotel', 'ist', 'neu', '.'], 'Hotel jest nowy.', {}), (['mein', 'Vater', 'ist', 'alt', ',', 'aber', 'nicht', 'sehr', 'alt', '.'], 'Mój tata jest stary, ale niezbyt.', {}), (['die', 'Stadt', 'ist', 'groß', 'und', 'schön', '.'], 'Miasto jest duże i piękne.', {}), (['das', 'Meer', 'ist', 'schön', '.'], 'Morze jest piękne.', {}), (['das', 'Taxi', 'ist', 'schnell', '.'], 'Taksówka jest szybka.', {}), (['die', 'Nacht', 'ist', 'lang', '.'], 'Noc jest długa.', {}), (['der', 'Tag', 'ist', 'lang', '.'], 'Dzień jest długi.', {}), (['meine', 'Schwester', 'ist', 'jung', '.'], 'Moja siostra jest młoda.', {}), (['das', 'ist', 'ein', 'großes', 'Haus', '.'], 'To jest duży dom.', {}), (['das', 'ist', 'ein', 'neues', 'Hotel', '.'], 'To jest nowy hotel.', {}), (['das', 'ist', 'ein', 'schönes', 'Kind', '.'], 'To jest piękne dziecko.', {}), (['ich', 'bin', 'zu', 'klein', '.'], 'Jestem za mały.', {}), (['er', 'ist', 'jung', 'und', 'schön', '.'], 'On jest młody i przystojny.', {}), (['der', 'Mann', 'ist', 'alt', '.'], 'Mężczyzna jest stary.', {}), (['das', 'Haus', 'ist', 'alt', ',', 'aber', 'schön', '.'], 'Dom jest stary, ale piękny.', {})]}, {'id': 'f08', 'title': 'Czas', 'icon': 'Z', 'track': 'jezyk', 'words': [('Zeit', 'czas', None, None), ('Jahr', 'rok', None, None), ('Jahre', 'lata', None, None), ('Woche', 'tydzień', None, None), ('Stunde', 'godzina', None, None), ('Stunden', 'godziny', None, None), ('früh', 'wcześnie', None, None), ('oft', 'często', None, None), ('nie', 'nigdy', None, None), ('manchmal', 'czasem', None, None)], 'sentences': [(['ich', 'habe', 'heute', 'keine', 'Zeit', '.'], 'Nie mam dzisiaj czasu.', {}), (['hast', 'du', 'morgen', 'Zeit', '?'], 'Masz jutro czas?', {}), (['wir', 'haben', 'viel', 'Zeit', '.'], 'Mamy dużo czasu.', {}), (['ein', 'Jahr', 'ist', 'eine', 'lange', 'Zeit', '.'], 'Rok to długi czas.', {}), (['zwei', 'Jahre', 'sind', 'lang', '.'], 'Dwa lata to długo.', {}), (['ich', 'bin', 'eine', 'Woche', 'in', 'der', 'Stadt', '.'], 'Jestem w mieście tydzień.', {}), (['ich', 'bin', 'zwei', 'Stunden', 'in', 'der', 'Schule', '.'], 'Jestem w szkole dwie godziny.', {}), (['ich', 'komme', 'morgen', 'früh', '.'], 'Przyjdę jutro rano.', {}), (['er', 'kommt', 'oft', 'zu', 'mir', '.'], 'On często do mnie przychodzi.', {}), (['ich', 'esse', 'nie', 'Fisch', '.'], 'Nigdy nie jem ryby.', {}), (['manchmal', 'trinke', 'ich', 'Wein', '.'], 'Czasem piję wino.', {}), (['mein', 'Vater', 'ist', 'oft', 'früh', 'hier', '.'], 'Mój tata jest często wcześnie tutaj.', {}), (['der', 'Lehrer', 'hat', 'nie', 'Zeit', '.'], 'Nauczyciel nigdy nie ma czasu.', {}), (['wir', 'gehen', 'morgen', 'zur', 'Schule', '.'], 'Jutro idziemy do szkoły.', {}), (['ich', 'trinke', 'immer', 'Kaffee', 'am', 'Morgen', '.'], 'Zawsze piję kawę rano.', {}), (['das', 'Kind', 'ist', 'drei', 'Jahre', 'alt', '.'], 'Dziecko ma trzy lata.', {}), (['ich', 'habe', 'viele', 'Stunden', 'Zeit', '.'], 'Mam wiele godzin czasu.', {})]}, {'id': 'f09', 'title': 'Móc, musieć, chcieć', 'icon': 'M', 'track': 'jezyk', 'words': [('kann', 'mogę, może', None, None), ('kannst', 'możesz', None, None), ('können', 'móc, możemy, mogą', None, None), ('könnt', 'możecie', None, None), ('muss', 'muszę, musi', None, None), ('musst', 'musisz', None, None), ('müssen', 'musieć, musimy, muszą', None, None), ('müsst', 'musicie', None, None), ('will', 'chcę, chce', None, None), ('willst', 'chcesz', None, None), ('wollen', 'chcieć, chcemy, chcą', None, None), ('wollt', 'chcecie', None, None)], 'sentences': [(['ich', 'kann', 'kommen', '.'], 'Mogę przyjść.', {}), (['kannst', 'du', 'morgen', 'kommen', '?'], 'Możesz jutro przyjść?', {}), (['wir', 'können', 'heute', 'nicht', 'kommen', '.'], 'Nie możemy dzisiaj przyjść.', {}), (['ich', 'muss', 'zur', 'Schule', 'gehen', '.'], 'Muszę iść do szkoły.', {}), (['du', 'musst', 'viel', 'Wasser', 'trinken', '.'], 'Musisz pić dużo wody.', {}), (['er', 'muss', 'heute', 'früh', 'kommen', '.'], 'On musi dziś przyjść wcześnie.', {}), (['wir', 'müssen', 'zu', 'Hause', 'essen', '.'], 'Musimy jeść w domu.', {}), (['ihr', 'müsst', 'nicht', 'kommen', '.'], 'Nie musicie przychodzić.', {}), (['ich', 'will', 'Kaffee', 'trinken', '.'], 'Chcę pić kawę.', {}), (['willst', 'du', 'mit', 'uns', 'essen', '?'], 'Chcesz jeść z nami?', {}), (['das', 'Kind', 'will', 'nicht', 'essen', '.'], 'Dziecko nie chce jeść.', {}), (['wir', 'wollen', 'am', 'Meer', 'essen', '.'], 'Chcemy jeść nad morzem.', {}), (['kann', 'ich', 'Wasser', 'haben', '?'], 'Czy mogę dostać wodę?', {}), (['was', 'willst', 'du', 'machen', '?'], 'Co chcesz robić?', {}), (['was', 'kann', 'ich', 'für', 'dich', 'machen', '?'], 'Co mogę dla ciebie zrobić?', {}), (['er', 'kann', 'nicht', 'gehen', '.'], 'On nie może iść.', {}), (['könnt', 'ihr', 'mit', 'uns', 'kommen', '?'], 'Możecie pójść z nami?', {}), (['ich', 'muss', 'auch', 'essen', '.'], 'Ja też muszę jeść.', {}), (['wollt', 'ihr', 'Kaffee', '?'], 'Chcecie kawy?', {})]}, {'id': 'f10', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('Bier', 'piwo', None, None), ('Suppe', 'zupa', None, None), ('Fleisch', 'mięso', None, None), ('Salat', 'sałatka, sałata', None, None), ('Kuchen', 'ciasto', None, None), ('Ei', 'jajko', None, None), ('Hunger', 'głód', None, None), ('Durst', 'pragnienie', None, None)], 'sentences': [(['ich', 'habe', 'Hunger', '.'], 'Jestem głodny.', {}), (['hast', 'du', 'Durst', '?'], 'Chce ci się pić?', {}), (['wir', 'haben', 'Hunger', 'und', 'Durst', '.'], 'Jesteśmy głodni i spragnieni.', {}), (['ich', 'möchte', 'Suppe', 'und', 'Brot', '.'], 'Poproszę zupę i chleb.', {}), (['er', 'isst', 'Fleisch', 'und', 'Salat', '.'], 'On je mięso i sałatkę.', {}), (['ich', 'esse', 'kein', 'Fleisch', '.'], 'Nie jem mięsa.', {}), (['das', 'Kind', 'möchte', 'Kuchen', '.'], 'Dziecko chce ciasto.', {}), (['möchtest', 'du', 'ein', 'Ei', '?'], 'Chcesz jajko?', {}), (['ich', 'trinke', 'Bier', '.'], 'Piję piwo.', {}), (['mein', 'Vater', 'trinkt', 'oft', 'Bier', '.'], 'Mój tata często pije piwo.', {}), (['die', 'Suppe', 'ist', 'sehr', 'gut', '.'], 'Zupa jest bardzo dobra.', {}), (['der', 'Kuchen', 'ist', 'für', 'das', 'Kind', '.'], 'Ciasto jest dla dziecka.', {}), (['ich', 'habe', 'Hunger', ',', 'aber', 'ich', 'habe', 'kein', 'Brot', '.'], 'Jestem głodny, ale nie mam chleba.', {}), (['ich', 'habe', 'Durst', ',', 'ich', 'möchte', 'Wasser', '.'], 'Chce mi się pić, chcę wody.', {}), (['wir', 'essen', 'am', 'Abend', 'Suppe', '.'], 'Wieczorem jemy zupę.', {}), (['möchtest', 'du', 'Fleisch', 'oder', 'Fisch', '?'], 'Chcesz mięso czy rybę?', {}), (['das', 'Ei', 'ist', 'für', 'mich', '.'], 'Jajko jest dla mnie.', {}), (['der', 'Salat', 'ist', 'nicht', 'groß', '.'], 'Sałatka nie jest duża.', {})]}, {'id': 'f11', 'title': 'W domu', 'icon': 'D', 'track': 'jezyk', 'words': [('Zimmer', 'pokój', None, None), ('Tür', 'drzwi', None, None), ('Tisch', 'stół', None, None), ('Stuhl', 'krzesło', None, None), ('Fenster', 'okno', None, None), ('Bett', 'łóżko', None, None), ('Stühle', 'krzesła', None, None), ('Küche', 'kuchnia', None, None), ('Wohnung', 'mieszkanie', None, None)], 'sentences': [(['das', 'Zimmer', 'ist', 'klein', ',', 'aber', 'schön', '.'], 'Pokój jest mały, ale ładny.', {}), (['die', 'Küche', 'ist', 'groß', '.'], 'Kuchnia jest duża.', {}), (['das', 'Brot', 'ist', 'auf', 'dem', 'Tisch', '.'], 'Chleb jest na stole.', {}), (['der', 'Stuhl', 'ist', 'neu', '.'], 'Krzesło jest nowe.', {}), (['die', 'Tür', 'ist', 'links', '.'], 'Drzwi są po lewej.', {}), (['das', 'Fenster', 'ist', 'rechts', '.'], 'Okno jest po prawej.', {}), (['das', 'Bett', 'ist', 'im', 'Zimmer', '.'], 'Łóżko jest w pokoju.', {}), (['mein', 'Zimmer', 'hat', 'ein', 'Fenster', 'und', 'eine', 'Tür', '.'], 'Mój pokój ma okno i drzwi.', {}), (['die', 'Wohnung', 'ist', 'in', 'der', 'Stadt', '.'], 'Mieszkanie jest w mieście.', {}), (['wir', 'haben', 'eine', 'Wohnung', 'und', 'ein', 'Haus', '.'], 'Mamy mieszkanie i dom.', {}), (['die', 'Wohnung', 'hat', 'drei', 'Zimmer', '.'], 'Mieszkanie ma trzy pokoje.', {}), (['ich', 'bin', 'in', 'der', 'Küche', '.'], 'Jestem w kuchni.', {}), (['der', 'Tisch', 'ist', 'zu', 'klein', '.'], 'Stół jest za mały.', {}), (['meine', 'Schwester', 'ist', 'im', 'Zimmer', '.'], 'Moja siostra jest w pokoju.', {}), (['wo', 'ist', 'der', 'Stuhl', '?'], 'Gdzie jest krzesło?', {}), (['das', 'Kind', 'ist', 'auf', 'dem', 'Bett', '.'], 'Dziecko jest na łóżku.', {}), (['der', 'Tisch', 'und', 'der', 'Stuhl', 'sind', 'neu', '.'], 'Stół i krzesło są nowe.', {}), (['er', 'isst', 'in', 'der', 'Küche', '.'], 'On je w kuchni.', {}), (['das', 'Zimmer', 'hat', 'zwei', 'Fenster', '.'], 'Pokój ma dwa okna.', {}), (['die', 'Küche', 'hat', 'einen', 'Tisch', 'und', 'vier', 'Stühle', '.'], 'Kuchnia ma stół i cztery krzesła.', {})]}, {'id': 'f12', 'title': 'Szkoła i język', 'icon': 'S', 'track': 'jezyk', 'words': [('Arbeit', 'praca', None, None), ('Buch', 'książka', None, None), ('Name', 'imię, nazwa', None, None), ('Wort', 'słowo', None, None), ('Wörter', 'słowa', None, None), ('Frage', 'pytanie', None, None), ('Antwort', 'odpowiedź', None, None), ('Sprache', 'język', None, None), ('Deutsch', 'niemiecki (język)', None, None), ('Anna', 'Anna', None, None), ('lerne', 'uczę się', None, None), ('lernst', 'uczysz się', None, None), ('lernt', 'uczy się, uczycie się', None, None), ('lernen', 'uczyć się, uczymy się', None, None), ('spreche', 'mówię', None, None), ('sprichst', 'mówisz', None, None), ('spricht', 'mówi', None, None), ('sprechen', 'mówić, mówimy', None, None)], 'sentences': [(['ich', 'lerne', 'Deutsch', '.'], 'Uczę się niemieckiego.', {}), (['du', 'lernst', 'Deutsch', '.'], 'Uczysz się niemieckiego.', {}), (['meine', 'Schwester', 'lernt', 'in', 'der', 'Schule', '.'], 'Moja siostra uczy się w szkole.', {}), (['wir', 'lernen', 'am', 'Abend', '.'], 'Uczymy się wieczorem.', {}), (['ich', 'spreche', 'Deutsch', '.'], 'Mówię po niemiecku.', {}), (['sprichst', 'du', 'Deutsch', '?'], 'Mówisz po niemiecku?', {}), (['der', 'Lehrer', 'spricht', 'schnell', '.'], 'Nauczyciel mówi szybko.', {}), (['wir', 'sprechen', 'nicht', 'viel', '.'], 'Nie mówimy dużo.', {}), (['das', 'Wort', 'ist', 'neu', '.'], 'To słowo jest nowe.', {}), (['das', 'Buch', 'ist', 'alt', '.'], 'Książka jest stara.', {}), (['ich', 'habe', 'eine', 'Frage', '.'], 'Mam pytanie.', {}), (['die', 'Antwort', 'ist', 'gut', '.'], 'Odpowiedź jest dobra.', {}), (['wie', 'ist', 'dein', 'Name', '?'], 'Jak masz na imię?', {}), (['mein', 'Name', 'ist', 'Anna', '.'], 'Mam na imię Anna.', {}), (['die', 'Sprache', 'ist', 'schön', '.'], 'Język jest piękny.', {}), (['meine', 'Arbeit', 'ist', 'in', 'der', 'Stadt', '.'], 'Moja praca jest w mieście.', {}), (['ich', 'habe', 'viel', 'Arbeit', '.'], 'Mam dużo pracy.', {}), (['hast', 'du', 'eine', 'Frage', 'zum', 'Buch', '?'], 'Masz pytanie do książki?', {}), (['wir', 'lernen', 'viele', 'Wörter', '.'], 'Uczymy się wielu słów.', {}), (['er', 'spricht', 'gut', 'Deutsch', '.'], 'On dobrze mówi po niemiecku.', {}), (['der', 'Student', 'lernt', 'Deutsch', 'in', 'der', 'Schule', '.'], 'Student uczy się niemieckiego w szkole.', {})]}, {'id': 'f13', 'title': 'Spójniki i myślenie', 'icon': 'S', 'track': 'jezyk', 'words': [('dass', 'że', None, None), ('wenn', 'jeśli, kiedy', None, None), ('weil', 'ponieważ, bo', None, None), ('denn', 'bo, gdyż', None, None), ('dann', 'potem, wtedy', None, None), ('also', 'więc, no', None, None), ('doch', 'przecież, jednak', None, None), ('ob', 'czy (w zdaniu podrzędnym)', None, None), ('weiß', 'wiem, wie', None, None), ('glaube', 'wierzę, myślę', None, None)], 'sentences': [(['ich', 'weiß', ',', 'dass', 'du', 'Hunger', 'hast', '.'], 'Wiem, że jesteś głodny.', {}), (['ich', 'glaube', ',', 'dass', 'er', 'morgen', 'kommt', '.'], 'Myślę, że on jutro przyjdzie.', {}), (['ich', 'weiß', 'nicht', ',', 'ob', 'er', 'kommt', '.'], 'Nie wiem, czy on przyjdzie.', {}), (['wenn', 'du', 'Hunger', 'hast', ',', 'isst', 'du', 'Brot', '.'], 'Jeśli jesteś głodny, jesz chleb.', {}), (['ich', 'esse', 'nicht', ',', 'weil', 'ich', 'keine', 'Zeit', 'habe', '.'], 'Nie jem, bo nie mam czasu.', {}), (['ich', 'kann', 'nicht', 'kommen', ',', 'denn', 'ich', 'habe', 'Arbeit', '.'], 'Nie mogę przyjść, bo mam pracę.', {}), (['ich', 'esse', 'Brot', 'und', 'dann', 'trinke', 'ich', 'Kaffee', '.'], 'Jem chleb, a potem piję kawę.', {}), (['also', 'gut', ',', 'ich', 'komme', '.'], 'No dobrze, przyjdę.', {}), (['das', 'ist', 'doch', 'gut', '!'], 'Przecież to dobre!', {}), (['wenn', 'ich', 'Zeit', 'habe', ',', 'komme', 'ich', '.'], 'Jeśli będę miał czas, przyjdę.', {}), (['ich', 'weiß', ',', 'dass', 'das', 'Kind', 'Hunger', 'hat', '.'], 'Wiem, że dziecko jest głodne.', {}), (['wenn', 'es', 'heute', 'nicht', 'geht', ',', 'komme', 'ich', 'morgen', '.'], 'Jeśli dziś się nie da, przyjdę jutro.', {}), (['ich', 'weiß', 'nicht', ',', 'was', 'er', 'macht', '.'], 'Nie wiem, co on robi.', {}), (['ich', 'weiß', 'nicht', ',', 'wo', 'die', 'Schule', 'ist', '.'], 'Nie wiem, gdzie jest szkoła.', {}), (['sie', 'weiß', ',', 'dass', 'ich', 'hier', 'bin', '.'], 'Ona wie, że tu jestem.', {}), (['ich', 'glaube', ',', 'dass', 'du', 'Durst', 'hast', '.'], 'Myślę, że chce ci się pić.', {}), (['wenn', 'du', 'kannst', ',', 'kommst', 'du', 'morgen', '.'], 'Jeśli możesz, przyjdziesz jutro.', {}), (['er', 'kommt', 'nicht', ',', 'weil', 'er', 'keine', 'Zeit', 'hat', '.'], 'On nie przyjdzie, bo nie ma czasu.', {})]}, {'id': 'f14', 'title': 'Słowa złożone', 'icon': 'Z', 'track': 'jezyk', 'words': [('Haustür', 'drzwi wejściowe', None, None), ('Schulbuch', 'podręcznik', None, None), ('Kinderzimmer', 'pokój dziecięcy', None, None), ('Käsebrot', 'kanapka z serem', None, None), ('Apfelkuchen', 'szarlotka', None, None), ('Fischsuppe', 'zupa rybna', None, None), ('Milchkaffee', 'kawa z mlekiem', None, None), ('Lehrerzimmer', 'pokój nauczycielski', None, None), ('Hotelzimmer', 'pokój hotelowy', None, None), ('Wochentag', 'dzień tygodnia', None, None), ('Abendbrot', 'kolacja', None, None), ('Wohnzimmer', 'salon', None, None), ('Küchentisch', 'stół kuchenny', None, None)], 'sentences': [(['die', 'Haustür', 'ist', 'klein', '.'], 'Drzwi wejściowe są małe.', {}), (['das', 'Kind', 'hat', 'ein', 'Schulbuch', '.'], 'Dziecko ma podręcznik.', {}), (['das', 'Kinderzimmer', 'ist', 'schön', '.'], 'Pokój dziecięcy jest ładny.', {}), (['ich', 'esse', 'ein', 'Käsebrot', '.'], 'Jem kanapkę z serem.', {}), (['ich', 'möchte', 'Apfelkuchen', '.'], 'Chcę szarlotkę.', {}), (['die', 'Fischsuppe', 'ist', 'gut', '.'], 'Zupa rybna jest dobra.', {}), (['er', 'trinkt', 'einen', 'Milchkaffee', '.'], 'On pije kawę z mlekiem.', {}), (['das', 'Lehrerzimmer', 'ist', 'dort', '.'], 'Pokój nauczycielski jest tam.', {}), (['das', 'Hotelzimmer', 'ist', 'groß', '.'], 'Pokój hotelowy jest duży.', {}), (['was', 'ist', 'ein', 'Wochentag', '?'], 'Co to jest dzień tygodnia?', {}), (['wir', 'essen', 'Abendbrot', '.'], 'Jemy kolację.', {}), (['das', 'Wohnzimmer', 'ist', 'groß', '.'], 'Salon jest duży.', {}), (['der', 'Küchentisch', 'ist', 'klein', '.'], 'Stół kuchenny jest mały.', {}), (['das', 'Kind', 'ist', 'im', 'Kinderzimmer', '.'], 'Dziecko jest w pokoju dziecięcym.', {}), (['ich', 'habe', 'ein', 'Buch', 'im', 'Wohnzimmer', '.'], 'Mam książkę w salonie.', {}), (['die', 'Lehrer', 'essen', 'im', 'Lehrerzimmer', '.'], 'Nauczyciele jedzą w pokoju nauczycielskim.', {})]}, {'id': 'f15', 'title': 'Wzór: Ich möchte … i Ich habe …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['ich', 'möchte', 'ein', 'Brot', '.'], 'Poproszę chleb.', {}), (['ich', 'möchte', 'einen', 'Tee', '.'], 'Poproszę herbatę.', {}), (['ich', 'möchte', 'Suppe', '.'], 'Poproszę zupę.', {}), (['ich', 'möchte', 'einen', 'Apfel', '.'], 'Poproszę jabłko.', {}), (['ich', 'möchte', 'ein', 'Ei', '.'], 'Poproszę jajko.', {}), (['ich', 'möchte', 'Kuchen', '.'], 'Poproszę ciasto.', {}), (['ich', 'möchte', 'einen', 'Fisch', '.'], 'Poproszę rybę.', {}), (['ich', 'möchte', 'ein', 'Bier', '.'], 'Poproszę piwo.', {}), (['ich', 'habe', 'ein', 'Haus', '.'], 'Mam dom.', {}), (['ich', 'habe', 'eine', 'Schwester', '.'], 'Mam siostrę.', {}), (['ich', 'habe', 'einen', 'Freund', '.'], 'Mam przyjaciela.', {}), (['ich', 'habe', 'ein', 'Kind', '.'], 'Mam dziecko.', {}), (['ich', 'habe', 'ein', 'Zimmer', '.'], 'Mam pokój.', {}), (['ich', 'habe', 'eine', 'Wohnung', '.'], 'Mam mieszkanie.', {}), (['ich', 'habe', 'ein', 'Buch', '.'], 'Mam książkę.', {})]}, {'id': 'f16', 'title': 'Wzór: okolicznik, czasownik, ja', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['heute', 'trinke', 'ich', 'Kaffee', '.'], 'Dziś piję kawę.', {}), (['morgen', 'esse', 'ich', 'Brot', '.'], 'Jutro jem chleb.', {}), (['jetzt', 'habe', 'ich', 'Zeit', '.'], 'Teraz mam czas.', {}), (['manchmal', 'trinke', 'ich', 'Bier', '.'], 'Czasem piję piwo.', {}), (['oft', 'trinke', 'ich', 'Tee', '.'], 'Często piję herbatę.', {}), (['heute', 'lerne', 'ich', 'Deutsch', '.'], 'Dziś uczę się niemieckiego.', {}), (['morgen', 'habe', 'ich', 'Zeit', '.'], 'Jutro mam czas.', {}), (['immer', 'trinke', 'ich', 'Wasser', '.'], 'Zawsze piję wodę.', {}), (['manchmal', 'esse', 'ich', 'Fisch', '.'], 'Czasem jem rybę.', {}), (['heute', 'gehen', 'wir', 'zur', 'Schule', '.'], 'Dziś idziemy do szkoły.', {}), (['morgen', 'kommt', 'er', 'früh', '.'], 'Jutro przychodzi on wcześnie.', {}), (['jetzt', 'essen', 'wir', 'Suppe', '.'], 'Teraz jemy my zupę.', {}), (['am', 'Abend', 'trinken', 'sie', 'Tee', '.'], 'Wieczorem piją oni herbatę.', {}), (['oft', 'kommt', 'mein', 'Vater', '.'], 'Często przychodzi mój tata.', {})]}, {'id': 'f17', 'title': 'Wzór: czasownik modalny + bezokolicznik', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['ich', 'kann', 'morgen', 'kommen', '.'], 'Mogę przyjść jutro.', {}), (['ich', 'will', 'Fisch', 'essen', '.'], 'Chcę jeść rybę.', {}), (['ich', 'kann', 'Deutsch', 'sprechen', '.'], 'Mogę mówić po niemiecku.', {}), (['ich', 'muss', 'viel', 'lernen', '.'], 'Muszę dużo się uczyć.', {}), (['ich', 'will', 'mit', 'dir', 'gehen', '.'], 'Chcę iść z tobą.', {}), (['ich', 'kann', 'Kaffee', 'machen', '.'], 'Mogę zrobić kawę.', {}), (['ich', 'will', 'in', 'die', 'Stadt', 'gehen', '.'], 'Chcę iść do miasta.', {}), (['ich', 'muss', 'Wasser', 'trinken', '.'], 'Muszę pić wodę.', {}), (['wir', 'können', 'heute', 'kommen', '.'], 'My możemy przyjść dzisiaj.', {}), (['er', 'muss', 'früh', 'kommen', '.'], 'On musi przyjść wcześnie.', {}), (['du', 'kannst', 'Deutsch', 'sprechen', '.'], 'Ty możesz mówić po niemiecku.', {}), (['ihr', 'müsst', 'viel', 'lernen', '.'], 'Wy musicie dużo się uczyć.', {}), (['sie', 'wollen', 'am', 'Meer', 'essen', '.'], 'Oni chcą jeść nad morzem.', {}), (['ihr', 'könnt', 'mit', 'uns', 'kommen', '.'], 'Wy możecie iść z nami.', {})]}, {'id': 'f18', 'title': 'Wzór: pytania', 'icon': 'P', 'track': 'jezyk', 'words': [], 'sentences': [(['wo', 'ist', 'die', 'Küche', '?'], 'Gdzie jest kuchnia?', {}), (['wo', 'ist', 'deine', 'Schwester', '?'], 'Gdzie jest twoja siostra?', {}), (['wo', 'ist', 'das', 'Taxi', '?'], 'Gdzie jest taksówka?', {}), (['wo', 'ist', 'mein', 'Buch', '?'], 'Gdzie jest moja książka?', {}), (['hast', 'du', 'Zeit', '?'], 'Masz czas?', {}), (['hast', 'du', 'ein', 'Haus', '?'], 'Masz dom?', {}), (['hast', 'du', 'eine', 'Frage', '?'], 'Masz pytanie?', {}), (['hast', 'du', 'Wasser', '?'], 'Masz wodę?', {}), (['hast', 'du', 'einen', 'Bruder', '?'], 'Masz brata?', {}), (['hast', 'du', 'Kaffee', '?'], 'Masz kawę?', {}), (['hast', 'du', 'ein', 'Zimmer', '?'], 'Masz pokój?', {}), (['hast', 'du', 'eine', 'Wohnung', '?'], 'Masz mieszkanie?', {}), (['möchtest', 'du', 'Kaffee', '?'], 'Chcesz kawę?', {}), (['möchtest', 'du', 'Tee', '?'], 'Chcesz herbatę?', {}), (['möchtest', 'du', 'Suppe', '?'], 'Chcesz zupę?', {}), (['möchtest', 'du', 'Kuchen', '?'], 'Chcesz ciasto?', {}), (['möchtest', 'du', 'Fleisch', '?'], 'Chcesz mięso?', {}), (['möchtest', 'du', 'Wein', '?'], 'Chcesz wino?', {})]}, {'id': 'f19', 'title': 'Zdania złożone: dass i ob', 'icon': 'Z', 'track': 'jezyk', 'words': [], 'sentences': [(['ich', 'weiß', ',', 'dass', 'er', 'morgen', 'kommt', '.'], 'Wiem, że on jutro przyjdzie.', {}), (['ich', 'weiß', ',', 'dass', 'wir', 'keine', 'Zeit', 'haben', '.'], 'Wiem, że nie mamy czasu.', {}), (['ich', 'weiß', ',', 'dass', 'sie', 'Lehrer', 'sind', '.'], 'Wiem, że oni są nauczycielami.', {}), (['ich', 'weiß', ',', 'dass', 'die', 'Schule', 'links', 'ist', '.'], 'Wiem, że szkoła jest po lewej.', {}), (['ich', 'weiß', ',', 'dass', 'er', 'nicht', 'kommen', 'kann', '.'], 'Wiem, że on nie może przyjść.', {}), (['ich', 'weiß', ',', 'dass', 'du', 'viel', 'Arbeit', 'hast', '.'], 'Wiem, że masz dużo pracy.', {}), (['ich', 'glaube', ',', 'dass', 'er', 'heute', 'kommt', '.'], 'Myślę, że on dziś przyjdzie.', {}), (['ich', 'glaube', ',', 'dass', 'das', 'Hotel', 'neu', 'ist', '.'], 'Myślę, że hotel jest nowy.', {}), (['ich', 'glaube', ',', 'dass', 'sie', 'in', 'der', 'Stadt', 'ist', '.'], 'Myślę, że ona jest w mieście.', {}), (['ich', 'glaube', ',', 'dass', 'wir', 'zu', 'Hause', 'essen', 'müssen', '.'], 'Myślę, że musimy jeść w domu.', {}), (['ich', 'weiß', 'nicht', ',', 'ob', 'er', 'Zeit', 'hat', '.'], 'Nie wiem, czy on ma czas.', {}), (['ich', 'weiß', 'nicht', ',', 'ob', 'das', 'Kind', 'hier', 'ist', '.'], 'Nie wiem, czy dziecko jest tutaj.', {}), (['ich', 'weiß', 'nicht', ',', 'ob', 'du', 'Hunger', 'hast', '.'], 'Nie wiem, czy jesteś głodny.', {}), (['ich', 'weiß', 'nicht', ',', 'ob', 'die', 'Schule', 'groß', 'ist', '.'], 'Nie wiem, czy szkoła jest duża.', {})]}, {'id': 'f20', 'title': 'Zdania złożone: weil, wenn, denn', 'icon': 'Z', 'track': 'jezyk', 'words': [], 'sentences': [(['ich', 'komme', 'nicht', ',', 'weil', 'ich', 'keine', 'Zeit', 'habe', '.'], 'Nie przyjdę, bo nie mam czasu.', {}), (['ich', 'komme', 'nicht', ',', 'weil', 'ich', 'Hunger', 'habe', '.'], 'Nie przyjdę, bo jestem głodny.', {}), (['ich', 'komme', 'nicht', ',', 'weil', 'mein', 'Vater', 'nicht', 'hier', 'ist', '.'], 'Nie przyjdę, bo mojego taty nie ma.', {}), (['ich', 'komme', 'nicht', ',', 'weil', 'ich', 'Arbeit', 'habe', '.'], 'Nie przyjdę, bo mam pracę.', {}), (['ich', 'komme', 'nicht', ',', 'weil', 'das', 'Kind', 'klein', 'ist', '.'], 'Nie przyjdę, bo dziecko jest małe.', {}), (['ich', 'komme', 'nicht', ',', 'weil', 'ich', 'nicht', 'kann', '.'], 'Nie przyjdę, bo nie mogę.', {}), (['wenn', 'ich', 'Durst', 'habe', ',', 'trinke', 'ich', 'Wasser', '.'], 'Jeśli chce mi się pić, piję wodę.', {}), (['wenn', 'wir', 'Zeit', 'haben', ',', 'gehen', 'wir', 'zum', 'Meer', '.'], 'Jeśli mamy czas, idziemy nad morze.', {}), (['ich', 'esse', 'viel', ',', 'denn', 'ich', 'habe', 'Hunger', '.'], 'Dużo jem, bo jestem głodny.', {}), (['wir', 'gehen', 'zur', 'Schule', ',', 'denn', 'wir', 'lernen', 'Deutsch', '.'], 'Idziemy do szkoły, bo uczymy się niemieckiego.', {}), (['ich', 'habe', 'Durst', ',', 'aber', 'ich', 'habe', 'kein', 'Wasser', '.'], 'Chce mi się pić, ale nie mam wody.', {}), (['er', 'ist', 'klein', ',', 'aber', 'er', 'ist', 'sehr', 'gut', '.'], 'Jest mały, ale jest bardzo dobry.', {}), (['das', 'Haus', 'ist', 'alt', ',', 'aber', 'es', 'ist', 'schön', '.'], 'Dom jest stary, ale jest piękny.', {}), (['ich', 'möchte', 'Kaffee', ',', 'aber', 'ich', 'habe', 'nur', 'Wasser', '.'], 'Chcę kawy, ale mam tylko wodę.', {})]}, {'id': 'f21', 'title': 'Zdania złożone: wszystko razem', 'icon': 'Z', 'track': 'jezyk', 'words': [], 'sentences': [(['ich', 'weiß', ',', 'dass', 'er', 'nicht', 'kommen', 'kann', ',', 'weil', 'er', 'Arbeit', 'hat', '.'], 'Wiem, że on nie może przyjść, bo ma pracę.', {}), (['ich', 'weiß', ',', 'dass', 'das', 'Kind', 'essen', 'will', ',', 'weil', 'es', 'Hunger', 'hat', '.'], 'Wiem, że dziecko chce jeść, bo jest głodne.', {}), (['ich', 'weiß', ',', 'dass', 'wir', 'zu', 'Hause', 'essen', 'müssen', ',', 'weil', 'wir', 'keine', 'Zeit', 'haben', '.'], 'Wiem, że musimy jeść w domu, bo nie mamy czasu.', {}), (['ich', 'weiß', ',', 'dass', 'du', 'Deutsch', 'lernen', 'musst', ',', 'weil', 'das', 'Wort', 'neu', 'ist', '.'], 'Wiem, że musisz uczyć się niemieckiego, bo to słowo jest nowe.', {}), (['wenn', 'ich', 'Zeit', 'habe', ',', 'dann', 'komme', 'ich', 'morgen', '.'], 'Jeśli mam czas, to przyjdę jutro.', {}), (['wenn', 'du', 'Hunger', 'hast', ',', 'dann', 'kannst', 'du', 'Brot', 'essen', '.'], 'Jeśli jesteś głodny, to możesz jeść chleb.', {}), (['wenn', 'es', 'heute', 'nicht', 'geht', ',', 'dann', 'müssen', 'wir', 'morgen', 'kommen', '.'], 'Jeśli dziś się nie da, to musimy przyjść jutro.', {})]}]
ARTICLES.update({'Zeit': 'die', 'Jahr': 'das', 'Woche': 'die', 'Stunde': 'die', 'Bier': 'das', 'Suppe': 'die', 'Fleisch': 'das', 'Salat': 'der', 'Kuchen': 'der', 'Ei': 'das', 'Hunger': 'der', 'Durst': 'der', 'Zimmer': 'das', 'Tür': 'die', 'Tisch': 'der', 'Stuhl': 'der', 'Fenster': 'das', 'Bett': 'das', 'Küche': 'die', 'Wohnung': 'die', 'Arbeit': 'die', 'Buch': 'das', 'Name': 'der', 'Wort': 'das', 'Frage': 'die', 'Antwort': 'die', 'Sprache': 'die', 'Haustür': 'die', 'Schulbuch': 'das', 'Kinderzimmer': 'das', 'Käsebrot': 'das', 'Apfelkuchen': 'der', 'Fischsuppe': 'die', 'Milchkaffee': 'der', 'Lehrerzimmer': 'das', 'Hotelzimmer': 'das', 'Wochentag': 'der', 'Abendbrot': 'das', 'Wohnzimmer': 'das', 'Küchentisch': 'der'})
PLURALS.update({'Zeit': '–', 'Jahr': 'die Jahre', 'Woche': 'die Wochen', 'Stunde': 'die Stunden', 'Bier': 'die Biere', 'Suppe': 'die Suppen', 'Fleisch': '–', 'Salat': 'die Salate', 'Kuchen': 'die Kuchen', 'Ei': 'die Eier', 'Hunger': '–', 'Durst': '–', 'Zimmer': 'die Zimmer', 'Tür': 'die Türen', 'Tisch': 'die Tische', 'Stuhl': 'die Stühle', 'Fenster': 'die Fenster', 'Bett': 'die Betten', 'Küche': 'die Küchen', 'Wohnung': 'die Wohnungen', 'Arbeit': '–', 'Buch': 'die Bücher', 'Name': 'die Namen', 'Wort': 'die Wörter', 'Frage': 'die Fragen', 'Antwort': 'die Antworten', 'Sprache': 'die Sprachen', 'Haustür': 'die Haustüren', 'Schulbuch': 'die Schulbücher', 'Kinderzimmer': 'die Kinderzimmer', 'Käsebrot': 'die Käsebrote', 'Apfelkuchen': 'die Apfelkuchen', 'Fischsuppe': 'die Fischsuppen', 'Milchkaffee': 'die Milchkaffees', 'Lehrerzimmer': 'die Lehrerzimmer', 'Hotelzimmer': 'die Hotelzimmer', 'Wochentag': 'die Wochentage', 'Abendbrot': '–', 'Wohnzimmer': 'die Wohnzimmer', 'Küchentisch': 'die Küchentische'})
PARTS.update({'Haustür': 'Haus (dom) + Tür (drzwi) → „drzwi domu”', 'Schulbuch': 'Schule (szkoła) + Buch (książka) → „książka szkolna”', 'Kinderzimmer': 'Kinder (dzieci) + Zimmer (pokój) → „pokój dzieci”', 'Käsebrot': 'Käse (ser) + Brot (chleb) → „chleb z serem”', 'Apfelkuchen': 'Apfel (jabłko) + Kuchen (ciasto) → „ciasto jabłkowe”', 'Fischsuppe': 'Fisch (ryba) + Suppe (zupa) → „zupa z ryby”', 'Milchkaffee': 'Milch (mleko) + Kaffee (kawa) → „kawa z mlekiem”', 'Lehrerzimmer': 'Lehrer (nauczyciel) + Zimmer (pokój) → „pokój nauczycieli”', 'Hotelzimmer': 'Hotel (hotel) + Zimmer (pokój) → „pokój w hotelu”', 'Wochentag': 'Woche (tydzień) + Tag (dzień) → „dzień tygodnia”', 'Abendbrot': 'Abend (wieczór) + Brot (chleb) → „wieczorny chleb”, czyli kolacja', 'Wohnzimmer': 'wohnen (mieszkać) + Zimmer (pokój) → „pokój do mieszkania”', 'Küchentisch': 'Küche (kuchnia) + Tisch (stół) → „stół z kuchni”'})
INSIGHTS.setdefault('f15', []).append({'title': 'Wzór: Ich möchte … i Ich habe …', 'text': 'Szkielet jest ten sam, zmieniasz tylko to, czego chcesz albo co masz. Rzeczownik po einen, ein, eine dostaje rodzaj: der Kaffee → einen Kaffee, das Brot → ein Brot.\n\nPrzykład: Ich möchte ein Brot. = Poproszę chleb.', 'chain': []})
INSIGHTS.setdefault('f16', []).append({'title': 'Wzór: okolicznik, czasownik, ja', 'text': 'Na początku może stać czas albo miejsce, ale odmieniony czasownik zawsze jest drugi. Podmiot idzie za nim: Heute trinke ich Kaffee. Pierwsze słowo możesz podmienić na inne bez zmiany reszty.\n\nPrzykład: Heute trinke ich Kaffee. = Dziś piję kawę.', 'chain': []})
INSIGHTS.setdefault('f17', []).append({'title': 'Wzór: czasownik modalny + bezokolicznik', 'text': 'Czasownik modalny jest drugi, a drugi czasownik idzie na sam koniec: Ich kann morgen kommen. Z innymi osobami zmienia się tylko forma modalnego.\n\nPrzykład: Ich kann morgen kommen. = Mogę przyjść jutro.', 'chain': []})
INSIGHTS.setdefault('f18', []).append({'title': 'Wzór: pytania', 'text': 'Pytanie bez słowa pytającego zaczyna się od czasownika: Hast du Zeit? Ze słowem pytającym czasownik jest drugi: Wo ist die Schule?\n\nPrzykład: Wo ist die Küche? = Gdzie jest kuchnia?', 'chain': []})
INSIGHTS.setdefault('f19', []).append({'title': 'Zdania złożone: dass i ob', 'text': 'Po dass, ob i słowach pytających zaczyna się zdanie podrzędne: odmieniony czasownik odchodzi na sam koniec. Dlatego Ich weiß, dass er morgen kommt, a nie „dass er kommt morgen”. Przed dass zawsze stoi przecinek.\n\nPrzykład: Ich weiß, dass er morgen kommt. = Wiem, że on jutro przyjdzie.', 'chain': []})
INSIGHTS.setdefault('f20', []).append({'title': 'Zdania złożone: weil, wenn, denn', 'text': 'Weil i wenn wysyłają czasownik na koniec: Ich komme nicht, weil ich keine Zeit habe. Denn jest inne: po nim szyk jak w zwykłym zdaniu: Ich komme nicht, denn ich habe Arbeit. Dwa zdania łączysz przecinkiem.\n\nPrzykład: Ich komme nicht, weil ich keine Zeit habe. = Nie przyjdę, bo nie mam czasu.', 'chain': []})
INSIGHTS.setdefault('f21', []).append({'title': 'Zdania złożone: wszystko razem', 'text': 'Teraz łączysz wszystko: modalny, podrzędne i przecinki. Zawsze zapytaj najpierw: gdzie jest odmieniony czasownik w każdej części?\n\nPrzykład: Ich weiß, dass er nicht kommen kann, weil er Arbeit hat. = Wiem, że on nie może przyjść, bo ma pracę.', 'chain': []})
# === /BULK ===

# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['ich', 'du', 'er/sie/es', 'wir', 'ihr', 'sie/Sie'],
    'przyp': ['Nominativ (kto? co?)', 'Akkusativ (kogo? co?)', 'Dativ (komu?)', 'Genitiv (czyj?)'],
    'przyp3': ['Nominativ', 'Akkusativ', 'Dativ'],
    'stamm': ['Präteritum (er)', 'Partizip II', 'Perfekt (er)'],
    'rozk': ['du', 'ihr', 'Sie'],
    'p1': ['machen', 'lesen', 'schlafen', 'kommen', 'spielen', 'singen'],
    't_perf': ['gehen', 'machen', 'kommen', 'essen', 'fahren', 'schlafen', 'bleiben', 'sehen'],
    't_rodz': ['Mädchen (dziewczynka)', 'Sonne (słońce)', 'Mond (księżyc)', 'Buch (książka)', 'Tisch (stół)', 'Lampe (lampa)', 'Auto (samochód)', 'Zeitung (gazeta)'],
    't_przyim': ['mit (z)', 'für (dla)', 'bei (u, przy)', 'ohne (bez)', 'nach (po, do)', 'durch (przez)', 'von (od)', 'um (wokół, o)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'machen (robić)', 'os', 'mache; machst; macht; machen; macht; machen', 'Wzór regularny: -e, -st, -t, -en, -t, -en.'),
    ('conj', 'Wzory koniugacji', 'lernen (uczyć się)', 'os', 'lerne; lernst; lernt; lernen; lernt; lernen', None),
    ('conj', 'Wzory koniugacji', 'wohnen (mieszkać)', 'os', 'wohne; wohnst; wohnt; wohnen; wohnt; wohnen', None),
    ('conj', 'Wyjątki', 'arbeiten (pracować)', 'os', 'arbeite; arbeitest; arbeitet; arbeiten; arbeitet; arbeiten', 'Temat na -t lub -d dostaje wstawione -e-: du arbeitest, er arbeitet.'),
    ('conj', 'Wyjątki', 'fahren (jechać)', 'os', 'fahre; fährst; fährt; fahren; fahrt; fahren', 'Czasownik mocny: w 2. i 3. osobie lp. a → ä.'),
    ('conj', 'Wyjątki', 'sprechen (mówić)', 'os', 'spreche; sprichst; spricht; sprechen; sprecht; sprechen', 'Czasownik mocny: w 2. i 3. osobie lp. e → i.'),
    ('conj', 'Wyjątki', 'sehen (widzieć)', 'os', 'sehe; siehst; sieht; sehen; seht; sehen', 'Czasownik mocny: e → ie.'),
    ('conj', 'Czasowniki nieregularne', 'sein (być)', 'os', 'bin; bist; ist; sind; seid; sind', None),
    ('conj', 'Czasowniki nieregularne', 'haben (mieć)', 'os', 'habe; hast; hat; haben; habt; haben', None),
    ('conj', 'Czasowniki nieregularne', 'werden (stawać się)', 'os', 'werde; wirst; wird; werden; werdet; werden', None),
    ('conj', 'Czasowniki nieregularne', 'können (móc)', 'os', 'kann; kannst; kann; können; könnt; können', 'Czasownik modalny: 1. i 3. osoba lp. są takie same i bez końcówki.'),
    ('conj', 'Czasowniki nieregularne', 'müssen (musieć)', 'os', 'muss; musst; muss; müssen; müsst; müssen', None),
    ('conj', 'Czasowniki nieregularne', 'wollen (chcieć)', 'os', 'will; willst; will; wollen; wollt; wollen', None),
    ('conj', 'Czasowniki nieregularne', 'möchten (chciałbym)', 'os', 'möchte; möchtest; möchte; möchten; möchtet; möchten', None),
    ('conj', 'Czasowniki nieregularne', 'wissen (wiedzieć)', 'os', 'weiß; weißt; weiß; wissen; wisst; wissen', None),
    ('decl', 'Wzory deklinacji', 'der Mann (mężczyzna)', 'przyp', 'der Mann; den Mann; dem Mann; des Mannes', 'Rodzaj męski: der, den, dem, des.'),
    ('decl', 'Wzory deklinacji', 'die Frau (kobieta)', 'przyp', 'die Frau; die Frau; der Frau; der Frau', 'Rodzaj żeński: die, die, der, der.'),
    ('decl', 'Wzory deklinacji', 'das Kind (dziecko)', 'przyp', 'das Kind; das Kind; dem Kind; des Kindes', 'Rodzaj nijaki: das, das, dem, des.'),
    ('decl', 'Wzory deklinacji', 'die Kinder (dzieci)', 'przyp', 'die Kinder; die Kinder; den Kindern; der Kinder', 'Liczba mnoga: w celowniku rzeczownik dostaje -n.'),
    ('decl', 'Wzory deklinacji', 'ein Mann (jakiś mężczyzna)', 'przyp', 'ein Mann; einen Mann; einem Mann; eines Mannes', None),
    ('decl', 'Wzory deklinacji', 'eine Frau (jakaś kobieta)', 'przyp', 'eine Frau; eine Frau; einer Frau; einer Frau', None),
    ('decl', 'Wyjątki', 'der Student (student)', 'przyp', 'der Student; den Studenten; dem Studenten; des Studenten', 'Deklinacja słaba (n-Deklination): wszędzie poza mianownikiem -en.'),
    ('decl', 'Zaimki', 'ich (ja)', 'przyp3', 'ich; mich; mir', None),
    ('decl', 'Zaimki', 'du (ty)', 'przyp3', 'du; dich; dir', None),
    ('decl', 'Zaimki', 'er (on)', 'przyp3', 'er; ihn; ihm', None),
    ('decl', 'Zaimki', 'sie (ona)', 'przyp3', 'sie; sie; ihr', None),
    ('decl', 'Zaimki', 'wir (my)', 'przyp3', 'wir; uns; uns', None),
    ('form', 'Formy podstawowe: słabe', 'machen (robić)', 'stamm', 'machte; gemacht; hat gemacht', 'Czasowniki słabe: -te, ge-…-t.'),
    ('form', 'Formy podstawowe: słabe', 'arbeiten (pracować)', 'stamm', 'arbeitete; gearbeitet; hat gearbeitet', None),
    ('form', 'Formy podstawowe: mocne', 'gehen (iść)', 'stamm', 'ging; gegangen; ist gegangen', 'Czasowniki ruchu i zmiany stanu tworzą Perfekt z sein.'),
    ('form', 'Formy podstawowe: mocne', 'kommen (przychodzić)', 'stamm', 'kam; gekommen; ist gekommen', None),
    ('form', 'Formy podstawowe: mocne', 'fahren (jechać)', 'stamm', 'fuhr; gefahren; ist gefahren', None),
    ('form', 'Formy podstawowe: mocne', 'sehen (widzieć)', 'stamm', 'sah; gesehen; hat gesehen', None),
    ('form', 'Formy podstawowe: mocne', 'sprechen (mówić)', 'stamm', 'sprach; gesprochen; hat gesprochen', None),
    ('form', 'Formy podstawowe: mocne', 'essen (jeść)', 'stamm', 'aß; gegessen; hat gegessen', None),
    ('form', 'Formy podstawowe: mocne', 'trinken (pić)', 'stamm', 'trank; getrunken; hat getrunken', None),
    ('form', 'Formy podstawowe: mocne', 'schreiben (pisać)', 'stamm', 'schrieb; geschrieben; hat geschrieben', None),
    ('form', 'Formy podstawowe: nieregularne', 'sein (być)', 'stamm', 'war; gewesen; ist gewesen', None),
    ('form', 'Formy podstawowe: nieregularne', 'haben (mieć)', 'stamm', 'hatte; gehabt; hat gehabt', None),
    ('form', 'Formy podstawowe: nieregularne', 'werden (stawać się)', 'stamm', 'wurde; geworden; ist geworden', None),
    ('form', 'Formy podstawowe: nieregularne', 'bringen (przynosić)', 'stamm', 'brachte; gebracht; hat gebracht', 'Czasownik mieszany: zmiana tematu i końcówki słabe.'),
    ('form', 'Imiesłowy', 'Partizip I', 'p1', 'machend; lesend; schlafend; kommend; spielend; singend', 'Bezokolicznik + -d: „robiący”. Przed rzeczownikiem odmienia się jak przymiotnik.'),
    ('conj', 'Czas przeszły', 'sein: Präteritum', 'os', 'war; warst; war; waren; wart; waren', None),
    ('conj', 'Czas przeszły', 'haben: Präteritum', 'os', 'hatte; hattest; hatte; hatten; hattet; hatten', None),
    ('conj', 'Czas przeszły', 'machen: Präteritum', 'os', 'machte; machtest; machte; machten; machtet; machten', '1. i 3. osoba lp. są takie same.'),
    ('conj', 'Czas przeszły', 'machen: Perfekt', 'os', 'habe gemacht; hast gemacht; hat gemacht; haben gemacht; habt gemacht; haben gemacht', 'haben lub sein w odpowiedniej osobie + Partizip II na końcu zdania.'),
    ('conj', 'Strona bierna', 'fragen: Passiv Präsens', 'os', 'werde gefragt; wirst gefragt; wird gefragt; werden gefragt; werdet gefragt; werden gefragt', 'werden + Partizip II.'),
    ('form', 'Tryb rozkazujący', 'machen', 'rozk', 'mach; macht; machen Sie', None),
    ('form', 'Tryb rozkazujący', 'sprechen', 'rozk', 'sprich; sprecht; sprechen Sie', 'Wymiana e → i zostaje w formie dla du.'),
    ('form', 'Tryb rozkazujący', 'sein', 'rozk', 'sei; seid; seien Sie', None),
    ('form', 'Typowe trudności', 'Perfekt: haben czy sein?', 't_perf', 'ist gegangen; hat gemacht; ist gekommen; hat gegessen; ist gefahren; hat geschlafen; ist geblieben; hat gesehen', 'sein biorą czasowniki ruchu i zmiany stanu oraz sein, bleiben, werden.'),
    ('form', 'Typowe trudności', 'Rodzaj: der, die czy das?', 't_rodz', 'das; die; der; das; der; die; das; die', 'Zdrobnienia na -chen i -lein są zawsze nijakie; rzeczowniki na -ung, -heit, -keit zawsze żeńskie.'),
    ('form', 'Typowe trudności', 'Przyimek: biernik czy celownik?', 't_przyim', 'Dativ; Akkusativ; Dativ; Akkusativ; Dativ; Akkusativ; Dativ; Akkusativ', None),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['zdanie główne: czasownik odmieniony', 'zdanie z weil: czasownik odmieniony', 'Perfekt: imiesłów (gemacht)', 'zdanie z czasownikiem modalnym: bezokolicznik', 'zdanie z dass: czasownik odmieniony', 'pytanie z wo, was, wann: czasownik odmieniony'],
    't_m1': ['Ich gehe in ___ Schule. (dokąd)', 'Ich bin in ___ Schule. (gdzie)', 'Das Buch liegt auf ___ Tisch. (gdzie)', 'Ich lege das Buch auf ___ Tisch. (dokąd)', 'Wir fahren an ___ Meer. (dokąd)', 'Wir sind an ___ Meer. (gdzie)'],
    't_m2': ['der Dom', 'die Karte', 'bekommen', 'das Gymnasium', 'die Dose', 'der Rock', 'die Mappe'],
    't_m3': ['Staat', 'Stadt', 'Miete', 'Mitte', 'Mutter', 'Mütter', 'schon', 'schön'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Szyk: gdzie stoi czasownik?', 't_m0', '2. miejsce; na końcu; na końcu; na końcu; na końcu; 2. miejsce', 'Heute lerne ich Deutsch. …, weil ich Deutsch lerne. Ich habe es gemacht. Ich will Deutsch lernen.'),
    ('form', 'Typowe trudności', 'Wechselpräpositionen: dokąd czy gdzie?', 't_m1', 'die; der; dem; den; das; dem', 'Ruch do celu: biernik. Położenie: celownik.'),
    ('form', 'Typowe trudności', 'Fałszywi przyjaciele: co to znaczy?', 't_m2', 'katedra; mapa, bilet; dostawać; liceum; puszka; spódnica; teczka', 'Dom to das Haus, a „stawać się” to werden.'),
    ('form', 'Typowe trudności', 'Długa czy krótka samogłoska: co to znaczy?', 't_m3', 'państwo; miasto; czynsz; środek; matka; matki; już; piękny', 'Długość i przegłos zmieniają znaczenie słowa.'),
]

# Klasyfikatory i liczba mnoga
PARADIGM_LABELS.update({
    't_pl0': ['der Tag', 'der Freund', 'der Fisch', 'der Hund', 'der Tisch', 'der Abend', 'der Brief', 'das Jahr'],
    't_pl1': ['der Sohn', 'die Stadt', 'die Nacht', 'der Stuhl', 'die Hand', 'der Baum', 'der Zug', 'der Platz'],
    't_pl2': ['das Kind', 'das Haus', 'das Buch', 'der Mann', 'das Wort', 'das Land', 'das Bild', 'das Glas'],
    't_pl3': ['die Frau', 'die Schule', 'die Straße', 'die Schwester', 'die Uhr', 'die Blume', 'die Polin', 'der Student'],
    't_pl4': ['der Lehrer', 'das Fenster', 'das Mädchen', 'der Apfel', 'der Bruder', 'die Mutter', 'der Vater', 'der Garten'],
    't_pl5': ['das Taxi', 'das Hotel', 'das Auto', 'das Kino', 'der Park', 'das Foto', 'das Café', 'das Handy'],
    't_pl6': ['das Kind', 'die Frau', 'der Tag', 'das Auto', 'der Lehrer', 'die Stadt', 'das Buch', 'die Blume'],
    't_pl7': ['der Tisch', 'die Stadt', 'das Haus', 'die Schwester', 'der Bruder', 'das Hotel', 'die Nacht', 'das Mädchen', 'der Mann', 'die Uhr'],
    't_pl8': ['die Kinder → mit den …', 'die Freunde → mit den …', 'die Häuser → in den …', 'die Lehrer → von den …', 'die Frauen → mit den …', 'die Autos → mit den …', 'die Tage → nach den …', 'die Männer → mit den …'],
})
PARADIGMS += [
    ('decl', 'Liczba mnoga', 'Liczba mnoga: -e', 't_pl0', 'die Tage|die Tagen|die Täge|die Tags; die Freunde|die Freunden|die Fründe|die Freunds; die Fische|die Fischen|die Fischer|die Fischs; die Hunde|die Hunden|die Hünde|die Hunder; die Tische|die Tischen|die Tischer|die Tischs; die Abende|die Abenden|die Äbende|die Abends; die Briefe|die Briefen|die Briefer|die Briefs; die Jahre|die Jahren|die Jähre|die Jahrer', 'Większość jednosylabowych rzeczowników męskich: -e, bez przegłosu.'),
    ('decl', 'Liczba mnoga', 'Liczba mnoga: przegłos + -e', 't_pl1', 'die Söhne|die Sohne|die Sohnen|die Söhner; die Städte|die Stadte|die Stadten|die Städter; die Nächte|die Nachte|die Nachten|die Nächter; die Stühle|die Stuhle|die Stuhlen|die Stühler; die Hände|die Hande|die Handen|die Händer; die Bäume|die Baume|die Baumen|die Bäumer; die Züge|die Zuge|die Zugen|die Züger; die Plätze|die Platze|die Platzen|die Plätzer', 'Jednosylabowe rzeczowniki żeńskie na -e w lm. zawsze mają przegłos; wiele męskich też.'),
    ('decl', 'Liczba mnoga', 'Liczba mnoga: (przegłos) + -er', 't_pl2', 'die Kinder|die Kinde|die Kinden|die Kinds; die Häuser|die Hause|die Hausen|die Hauser; die Bücher|die Buche|die Buchen|die Bucher; die Männer|die Manne|die Mannen|die Manner; die Wörter|die Worten|die Worter|die Wörte; die Länder|die Lande|die Landen|die Lander; die Bilder|die Bilde|die Bilden|die Bilds; die Gläser|die Glase|die Glasen|die Glaser', 'Typowe dla krótkich rzeczowników nijakich. a, o, u zawsze dostają przegłos.'),
    ('decl', 'Liczba mnoga', 'Liczba mnoga: -n, -en', 't_pl3', 'die Frauen|die Fraue|die Fräue|die Fraus; die Schulen|die Schule|die Schüle|die Schules; die Straßen|die Straße|die Sträße|die Straßes; die Schwestern|die Schwester|die Schwesteren|die Schwesters; die Uhren|die Uhre|die Ühre|die Uhrs; die Blumen|die Blume|die Blüme|die Blumes; die Polinnen|die Polinen|die Poline|die Polins; die Studenten|die Studente|die Students|die Studenter', 'Prawie wszystkie rzeczowniki żeńskie: -n lub -en, nigdy przegłos. -in → -innen. Także męskie „słabe” (Student, Junge).'),
    ('decl', 'Liczba mnoga', 'Liczba mnoga: bez końcówki', 't_pl4', 'die Lehrer|die Lehrern|die Lehrere|die Lehrers; die Fenster|die Fenstern|die Fenstere|die Fensters; die Mädchen|die Mädchens|die Mädchene|die Mädcher; die Äpfel|die Apfel|die Apfeln|die Äpfeln; die Brüder|die Bruder|die Brudern|die Brüdern; die Mütter|die Mutter|die Muttern|die Müttern; die Väter|die Vater|die Vatern|die Vätern; die Gärten|die Garten|die Gartens|die Gärtene', 'Męskie i nijakie na -er, -el, -en oraz -chen, -lein nie dostają końcówki; część ma przegłos. Mutter i Tochter też.'),
    ('decl', 'Liczba mnoga', 'Liczba mnoga: -s', 't_pl5', 'die Taxis|die Taxi|die Taxien|die Taxie; die Hotels|die Hotele|die Hotel|die Hotelen; die Autos|die Auto|die Auten|die Autoe; die Kinos|die Kino|die Kinen|die Kinoe; die Parks|die Parke|die Pärke|die Parken; die Fotos|die Foto|die Foten|die Fotoe; die Cafés|die Café|die Caféen|die Cafée; die Handys|die Handies|die Handy|die Handyen', 'Słowa obce i zakończone na samogłoskę inną niż -e.'),
    ('decl', 'Liczba mnoga', 'Która końcówka liczby mnogiej?', 't_pl6', '-er; -en; -e; -s; bez końcówki; przegłos + -e; przegłos + -er; -n', 'Liczby mnogiej trzeba uczyć się razem z rzeczownikiem, ale rodzaj i zakończenie słowa dużo podpowiadają.'),
    ('decl', 'Liczba mnoga', 'Wszystko razem: liczba mnoga', 't_pl7', 'die Tische|die Tischen|die Tischer|die Tischs; die Städte|die Stadten|die Städter|die Stadts; die Häuser|die Hause|die Hausen|die Häuse; die Schwestern|die Schwester|die Schwesteren|die Schwesters; die Brüder|die Bruder|die Brudern|die Bruders; die Hotels|die Hotele|die Hotel|die Hotelen; die Nächte|die Nachten|die Nachte|die Nächter; die Mädchen|die Mädchens|die Mädchene|die Mädcher; die Männer|die Manne|die Mannen|die Männe; die Uhren|die Uhre|die Ühre|die Uhrs', 'x'),
    ('decl', 'Liczba mnoga', 'Celownik liczby mnogiej: dodatkowe -n', 't_pl8', 'Kindern|Kinder|Kinderen; Freunden|Freunde|Freundern; Häusern|Häuser|Häusen; Lehrern|Lehrer|Lehreren; Frauen|Frauenn|Frauern; Autos|Autosn|Autosen; Tagen|Tage|Tagern; Männern|Männer|Männen', 'W celowniku lm. dochodzi -n, chyba że forma kończy się już na -n albo na -s.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['Dzisiaj uczę się niemieckiego.', 'Jutro idziemy do kina.', 'W domu piję kawę.', 'Teraz mam czas.'],
    't_s1': ['Wiem, że on jutro przychodzi.', 'Nie przyjdę, bo nie mam czasu.', 'Jeśli pada, zostaję w domu.', 'Nie wiem, gdzie jest szkoła.'],
    't_s2': ['Muszę dziś pracować.', 'Zjadłem chleb.', 'Wczoraj poszliśmy do szkoły.', 'Chcę pić wodę.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: czasownik na drugim miejscu', 't_s0', 'Heute lerne ich Deutsch.|Heute ich lerne Deutsch.|Ich heute lerne Deutsch.|Heute Deutsch ich lerne.; Morgen gehen wir ins Kino.|Morgen wir gehen ins Kino.|Wir morgen gehen ins Kino.|Morgen ins Kino gehen wir.; Zu Hause trinke ich Kaffee.|Zu Hause ich trinke Kaffee.|Ich zu Hause trinke Kaffee.|Zu Hause Kaffee trinke ich.; Jetzt habe ich Zeit.|Jetzt ich habe Zeit.|Ich jetzt habe Zeit.|Jetzt Zeit habe ich.', 'Odmieniony czasownik stoi na drugim miejscu. Jeśli na początku jest okolicznik, podmiot idzie za czasownikiem.'),
    ('form', 'Szyk zdania', 'Szyk: zdanie podrzędne', 't_s1', 'Ich weiß, dass er morgen kommt.|Ich weiß, dass er kommt morgen.|Ich weiß, dass kommt er morgen.|Ich weiß, dass morgen er kommt.; Ich komme nicht, weil ich keine Zeit habe.|Ich komme nicht, weil ich habe keine Zeit.|Ich komme nicht, weil keine Zeit ich habe.|Ich komme nicht, weil ich keine habe Zeit.; Wenn es regnet, bleibe ich zu Hause.|Wenn es regnet, ich bleibe zu Hause.|Wenn regnet es, bleibe ich zu Hause.|Wenn es regnet bleibe, ich zu Hause.; Ich weiß nicht, wo die Schule ist.|Ich weiß nicht, wo ist die Schule.|Ich weiß nicht, wo die Schule nicht ist.|Ich nicht weiß, wo die Schule ist.', 'Po dass, weil, wenn, ob i słowach pytających odmieniony czasownik idzie na sam koniec zdania podrzędnego.'),
    ('form', 'Szyk zdania', 'Szyk: rama zdania', 't_s2', 'Ich muss heute arbeiten.|Ich arbeiten muss heute.|Ich muss arbeiten heute.|Ich heute arbeiten muss.; Ich habe Brot gegessen.|Ich habe gegessen Brot.|Ich Brot habe gegessen.|Ich gegessen habe Brot.; Wir sind gestern zur Schule gegangen.|Wir sind gegangen gestern zur Schule.|Wir gestern sind zur Schule gegangen.|Wir sind gestern gegangen zur Schule.; Ich will Wasser trinken.|Ich will trinken Wasser.|Ich trinken will Wasser.|Ich Wasser will trinken.', 'Czasownik pomocniczy lub modalny stoi na 2. miejscu, a drugi czasownik (bezokolicznik, imiesłów) na końcu: tworzą ramę zdania.'),
]
