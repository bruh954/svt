"""Treść kursu: włoski dla Polaków.

Słowo:    (forma, znaczenie, polskie słowo pokrewne lub None, skojarzenie lub None, wymowa polskimi literami)
"""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "PRONUNCIA · WYMOWA", "jezyk": "LINGUA · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "Ç", "track": "wymowa",
     "letters": [
         ("c przed e, i", "[tʃ]: jak polskie cz", "ciao (cześć)"),
         ("c przed a, o, u", "[k]: jak polskie k", "casa (dom)"),
         ("ch", "[k]: jak polskie k (przed e, i)", "che (że)"),
         ("g przed e, i", "[dʒ]: jak polskie dż", "gelato (lody)"),
         ("g przed a, o, u", "[g]: jak polskie g", "gatto (kot)"),
         ("gh", "[g]: jak polskie g (przed e, i)", "spaghetti (spaghetti)"),
         ("gn", "[ɲ]: jak polskie ń", "lasagna (lasagne)"),
         ("gl", "[ʎ]: jak polskie lj, miękkie l", "famiglia (rodzina)"),
         ("sc przed e, i", "[ʃ]: jak polskie sz", "pesce (ryba)"),
         ("z", "[ts] lub [dz]: jak polskie c lub dz", "grazie (dziękuję)"),
         ("h", "nie czytasz go wcale", "ho (mam)"),
         ("podwójne litery", "wymawiasz je długo: tt, pp, ll", "pizza (pizza)"),
         ("qu", "[kw]: jak polskie kł", "quattro (cztery)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "C", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("ciao", "cześć (witaj i żegnaj)", None, "Z weneckiego „s'ciào vostro”: „jestem Twoim sługą”."),
         ("buongiorno", "dzień dobry", None, "Dosłownie „dobry dzień”."),
         ("buonasera", "dobry wieczór", None, None),
         ("buonanotte", "dobranoc", None, None),
         ("grazie", "dziękuję", "gracje", "Od łacińskiego gratia: łaska, wdzięk."),
         ("prego", "proszę; nie ma za co", None, None),
         ("sì", "tak", None, "Z akcentem to „tak”; bez (si) to „się”."),
         ("no", "nie", None, None),
         ("molto", "bardzo; dużo", None, None),
         ("scusa", "przepraszam (nieformalnie)", None, None),
         ("arrivederci", "do widzenia", None, None),
         ("e", "i", None, None),
         ("va bene", "w porządku", None, None),
     ],
     "sentences": [
         (["ciao", "!"], "Cześć!", {"arrivederci": "arrivederci to „do widzenia”."}),
         (["buongiorno", "!"], "Dzień dobry!", {"buonasera": "buonasera to „dobry wieczór”."}),
         (["buonasera", "!"], "Dobry wieczór!", {"buongiorno": "buongiorno to „dzień dobry”."}),
         (["buonanotte", "!"], "Dobranoc!", {}),
         (["grazie", "molto"], "Dziękuję bardzo.", {"prego": "prego to „proszę”. Tu dziękujesz."}),
         (["sì", ",", "grazie"], "Tak, dziękuję.", {"no": "no to „nie”."}),
         (["no", ",", "grazie"], "Nie, dziękuję.", {"sì": "sì to „tak”."}),
         (["scusa", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "S", "track": "jezyk",
     "words": [
         ("io", "ja", None, None),
         ("tu", "ty", None, None),
         ("lui", "on", None, None),
         ("lei", "ona", None, None),
         ("sono", "jestem", None, "Ta sama forma znaczy też „są”."),
         ("sei", "jesteś", None, None),
         ("è", "jest", None, "Z akcentem: [e], „jest”. Bez akcentu e to „i”."),
         ("polacco", "Polak", None, None),
         ("polacca", "Polka", None, None),
         ("studente", "student", "student", None),
         ("insegnante", "nauczyciel", None, None),
         ("di", "z; od", None, None),
         ("Polonia", "Polska", None, None),
         ("Italia", "Włochy", None, None),
     ],
     "sentences": [
         (["io", "sono", "studente"], "Jestem studentem.", {"sei": "sei to „jesteś”. O sobie: sono."}),
         (["tu", "sei", "insegnante"], "Jesteś nauczycielem.", {"sono": "sono to „jestem”. Do „tu”: sei."}),
         (["lui", "è", "polacco"], "On jest Polakiem.", {"polacca": "Dla mężczyzny: polacco."}),
         (["lei", "è", "polacca"], "Ona jest Polką.", {"polacco": "Dla kobiety: polacca."}),
         (["io", "sono", "di", "Polonia"], "Jestem z Polski.", {"Italia": "Italia to Włochy."}),
         (["lei", "è", "di", "Italia"], "Ona jest z Włoch.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "F", "track": "jezyk",
     "words": [
         ("il", "(rodzajnik męski)", None, "Il padre, il fratello."),
         ("la", "(rodzajnik żeński)", None, "La madre, la sorella."),
         ("un", "jakiś; jeden (męski)", None, None),
         ("una", "jakaś; jedna (żeński)", None, None),
         ("madre", "matka", None, None),
         ("padre", "ojciec", "patriarcha", None),
         ("bambino", "dziecko; chłopiec", "bambino", "Po polsku też bywa „bambino”."),
         ("amico", "przyjaciel", None, None),
         ("l'amico", "(ten) przyjaciel", None, None),
         ("donna", "kobieta", "madonna (moja pani)", "Madonna = „moja pani”."),
         ("uomo", "mężczyzna", None, None),
         ("fratello", "brat", None, None),
         ("sorella", "siostra", None, None),
         ("ho", "mam", None, "H nie czytamy: [o]."),
         ("hai", "masz", None, None),
         ("piccolo", "mały", None, None),
         ("buono", "dobry", None, None),
     ],
     "sentences": [
         (["il", "fratello", "è", "piccolo"], "Brat jest mały.", {"la": "fratello jest męskie: il."}),
         (["la", "madre", "è", "una", "donna"], "Matka jest kobietą.", {"il": "madre jest żeńska: la."}),
         (["il", "bambino", "è", "piccolo"], "Dziecko jest małe.", {}),
         (["ho", "un", "fratello"], "Mam brata.", {"hai": "hai to „masz”. O sobie: ho.", "una": "fratello jest męskie: un."}),
         (["tu", "hai", "una", "sorella"], "Masz siostrę.", {"ho": "ho to „mam”. Do „tu”: hai.", "un": "sorella jest żeńska: una."}),
         (["il", "padre", "è", "un", "uomo"], "Ojciec jest mężczyzną.", {}),
         (["l'amico", "è", "buono"], "Przyjaciel jest dobry.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "P", "track": "jezyk",
     "words": [
         ("acqua", "woda", "akwarium", None),
         ("caffè", "kawa", None, None),
         ("tè", "herbata", None, None),
         ("pane", "chleb", None, None),
         ("formaggio", "ser", None, None),
         ("vino", "wino", None, None),
         ("latte", "mleko", "latte", None),
         ("pesce", "ryba", None, None),
         ("mela", "jabłko", None, None),
         ("mele", "jabłka", None, "Mnoga żeńska: -a → -e."),
         ("vorrei", "chciałbym; chciałabym", None, "Grzeczne „chcę”."),
         ("vorresti", "chciałbyś; chciałabyś", None, None),
         ("dell'acqua", "wody", None, None),
         ("adesso", "teraz", None, None),
     ],
     "sentences": [
         (["vorrei", "un", "caffè"], "Poproszę kawę.", {"una": "caffè jest męskie: un."}),
         (["vorrei", "un", "tè", ",", "grazie"], "Poproszę herbatę.", {}),
         (["tu", "vorresti", "una", "mela"], "Chciałbyś jabłko.", {"un": "mela jest żeńskie: una."}),
         (["vorrei", "il", "pane"], "Poproszę chleb.", {}),
         (["il", "pesce", "è", "molto", "buono"], "Ryba jest bardzo dobra.", {}),
         (["adesso", "vorrei", "dell'acqua"], "Teraz poproszę wodę.", {}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("due", "dwa", "duet", None),
         ("tre", "trzy", "trio", None),
         ("quattro", "cztery", None, None),
         ("cinque", "pięć", None, None),
         ("dieci", "dziesięć", "dekada", None),
         ("bambini", "dzieci", None, "Mnoga: -o → -i."),
         ("oggi", "dziś", None, None),
         ("domani", "jutro", None, None),
         ("ieri", "wczoraj", None, None),
         ("ora", "godzina; teraz", None, None),
         ("ore", "godziny", None, None),
         ("che", "jaki; co", None, None),
         ("le", "(rodzajnik żeński mnogi)", None, None),
     ],
     "sentences": [
         (["ho", "due", "bambini"], "Mam dwoje dzieci.", {}),
         (["vorrei", "tre", "mele"], "Chcę trzy jabłka.", {"due": "due to „dwa”. Chcesz trzy: tre."}),
         (["che", "ora", "è", "?"], "Która jest godzina?", {}),
         (["sono", "le", "dieci"], "Jest dziesiąta.", {}),
         (["oggi", "vorrei", "un", "caffè"], "Dziś chcę kawę.", {"domani": "domani to „jutro”. Tu „dziś”: oggi."}),
         (["domani", "vorrei", "il", "pesce"], "Jutro chcę rybę.", {"ieri": "ieri to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "V", "track": "jezyk",
     "words": [
         ("casa", "dom", "kasyno (mały dom)", None),
         ("città", "miasto", None, None),
         ("strada", "ulica; droga", "strada (autostrada)", None),
         ("scuola", "szkoła", None, None),
         ("mare", "morze", None, None),
         ("taxi", "taksówka", "taksówka", None),
         ("albergo", "hotel", None, None),
         ("l'albergo", "(ten) hotel", None, None),
         ("dov'è", "gdzie jest", None, "Dove + è skrócone."),
         ("qui", "tu", None, None),
         ("lì", "tam", None, None),
         ("vado", "idę; jadę", None, None),
         ("a", "do; w", None, None),
         ("Roma", "Rzym", None, None),
         ("destra", "prawa; w prawo", None, None),
         ("sinistra", "lewa; w lewo", None, None),
     ],
     "sentences": [
         (["dov'è", "l'albergo", "?"], "Gdzie jest hotel?", {"qui": "qui to „tu”, a pytasz „gdzie”: dov'è."}),
         (["l'albergo", "è", "lì"], "Hotel jest tam.", {"qui": "qui to „tu”. Tu mówimy „tam”: lì."}),
         (["vado", "a", "casa"], "Idę do domu.", {}),
         (["vado", "a", "Roma"], "Jadę do Rzymu.", {}),
         (["il", "taxi", "è", "a", "destra"], "Taksówka jest po prawej.", {"sinistra": "sinistra to „lewa”."}),
         (["la", "scuola", "è", "lì"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Cichy znak: c i g", "chain": [],
                "text": "Włoski czyta się tak, jak jest napisany, ale c i g zmieniają dźwięk przed e, i: ciao [tʃao], gelato [dʒelato]. Żeby zachować twarde k i g przed e, i, wstawia się h: che [ke], spaghetti [spaɡeti]."}],
    "ja": [{"title": "Czasownik zastępuje zaimek", "chain": [
                ("Jestem studentem.", ["io", "sono", "studente"], "Do „io” pasuje sono."),
                ("Jesteś nauczycielem.", ["tu", "sei", "insegnante"], "Do „tu” pasuje sei."),
            ],
            "text": "Po włosku końcówka mówi, kto działa: sono (jestem), sei (jesteś), è (jest). Zaimek io, tu można pominąć: „sono studente”."}],
    "ludzie": [{"title": "Il, la, un, una", "chain": [],
                "text": "Rzeczowniki są męskie (il, un) lub żeńskie (la, una). Najczęściej -o to męski, -a to żeński. Przed samogłoską: l'amico, l'acqua."}],
    "jedzenie": [{"title": "Grzecznie: vorrei", "chain": [],
                  "text": "W barze mówi się „vorrei” (chciałbym) zamiast „voglio” (chcę): vorrei un caffè, per favore. Brzmi to uprzejmie i naturalnie."}],
}

ENDINGS_INSIGHT = {"title": "Rodzajniki i formy czasowników",
                   "text": "Po włosku ćwiczysz rodzaj (il/la, un/una) i formy czasownika (sono, sei, è). Tu to robisz."}

ENDINGS = [
    ("", "buon", "giorno", "", ["giorno", "sera", "notte"], "dzień dobry", "giorno to „dzień”, sera „wieczór”, notte „noc”.", "slowa"),
    ("", "buona", "sera", "", ["giorno", "sera", "notte"], "dobry wieczór", "sera to „wieczór”.", "slowa"),
    ("", "buona", "notte", "", ["giorno", "sera", "notte"], "dobranoc", "notte to „noc”.", "slowa"),
    ("io ", "", "sono", " studente", ["sono", "sei", "è"], "ja jestem", "Do „io” pasuje sono.", "ja"),
    ("tu ", "", "sei", " insegnante", ["sono", "sei", "è"], "ty jesteś", "Do „tu” pasuje sei.", "ja"),
    ("lui ", "", "è", " polacco", ["sono", "sei", "è"], "on jest", "Do „lui” pasuje è.", "ja"),
    ("", "", "il", " padre", ["il", "la"], "ten ojciec", "padre jest męski: il.", "ludzie"),
    ("", "", "la", " madre", ["il", "la"], "ta matka", "madre jest żeńska: la.", "ludzie"),
    ("ho ", "", "un", " fratello", ["un", "una"], "jakiś brat", "fratello jest męski: un.", "ludzie"),
    ("hai ", "", "una", " sorella", ["un", "una"], "jakaś siostra", "sorella jest żeńska: una.", "ludzie"),
    ("vorrei ", "", "un", " caffè", ["un", "una"], "jakaś kawa (męski)", "caffè jest męskie: un.", "jedzenie"),
    ("vorrei ", "", "una", " mela", ["un", "una"], "jakieś jabłko (żeński)", "mela jest żeńska: una.", "jedzenie"),
    ("vorrei ", "", "un", " tè", ["un", "una"], "jakaś herbata (męski)", "tè jest męskie: un.", "jedzenie"),
    ("vado ", "", "a", " Roma", ["a", "di"], "do Rzymu", "a to „do, w”, di to „z, od”.", "miejsca"),
    ("sono ", "", "di", " Polonia", ["a", "di"], "z Polski", "di to „z, od”.", "miejsca"),
]

CHAT_EXTRA = {"Giulia": "Giulia (imię)", "Marco": "Marco (imię)", "signore": "pan", "bene": "dobrze", "vuole": "chce (pan, pani)",
              "dove": "gdzie", "vai": "idziesz; jedziesz", "per": "dla; do", "favore": "łaska (per favore: proszę)"}

CHATS = [
    {"id": "bar", "title": "W barze", "partner": "Giulia", "avatar": "G", "requires": "jedzenie",
     "turns": [
         {"bot": ["buongiorno", "!"], "en": "Dzień dobry!",
          "options": [(["buongiorno", "!"], True, None), (["buonanotte", "!"], False, "buonanotte to „dobranoc”. Jest dzień.")]},
         {"bot": ["un", "caffè", "?"], "en": "Kawę?",
          "options": [(["sì", ",", "vorrei", "un", "caffè"], True, None),
                      (["sì", ",", "vorrei", "una", "caffè"], False, "caffè jest męskie: un, nie una.")]},
         {"bot": ["e", "il", "pane", "?"], "en": "I chleb?",
          "options": [(["no", ",", "grazie"], True, None),
                      (["prego", "!"], False, "prego to „proszę” (gdy coś podajesz). Odmów: no, grazie.")]},
         {"bot": ["bene", "!"], "build": (["grazie", "molto"], "Dziękuję bardzo."), "en": "Dobrze!"},
     ]},
    {"id": "conoscersi", "title": "Poznajemy się", "partner": "Marco", "avatar": "M", "requires": "ludzie",
     "turns": [
         {"bot": ["ciao", "!"], "en": "Cześć!",
          "options": [(["ciao", "!"], True, None), (["scusa", "!"], False, "scusa to „przepraszam”. Powitaj: ciao.")]},
         {"bot": ["sei", "di", "Italia", "?"], "en": "Jesteś z Włoch?",
          "options": [(["no", ",", "sono", "di", "Polonia"], True, None),
                      (["no", ",", "sei", "di", "Polonia"], False, "sei jest do „tu”. O sobie: sono.")]},
         {"bot": ["hai", "un", "fratello", "?"], "en": "Masz brata?",
          "options": [(["sì", ",", "ho", "un", "fratello"], True, None),
                      (["sì", ",", "hai", "un", "fratello"], False, "hai to „masz”. O sobie: ho.")]},
         {"bot": ["buonasera", "!"], "build": (["buonasera"], "Dobry wieczór."), "en": "Dobry wieczór!"},
     ]},
    {"id": "taxi", "title": "W taksówce", "partner": "signore", "avatar": "T", "requires": "miejsca",
     "turns": [
         {"bot": ["buonasera", "!"], "en": "Dobry wieczór!",
          "options": [(["buonasera", "!"], True, None), (["buongiorno", "!"], False, "buongiorno to „dzień dobry”. Jest wieczór.")]},
         {"bot": ["dove", "vai", "?"], "en": "Dokąd jedziesz?",
          "options": [(["vado", "a", "Roma"], True, None),
                      (["sono", "a", "Roma"], False, "sono to „jestem”. Jedziesz: vado.")]},
         {"bot": ["l'albergo", "è", "lì", "."], "en": "Hotel jest tam.",
          "options": [(["a", "destra", "?"], True, None), (["qui", "?"], False, "Pytasz o kierunek: a destra (w prawo).")]},
         {"bot": ["sì", "!"], "build": (["grazie", "molto"], "Dziękuję bardzo."), "en": "Tak!"},
     ]},
]

# === BULK: generowane z langs/bulk/italian.txt (nie edytuj ręcznie) ===
UNITS += [{'id': 'f01', 'title': 'Wzór: Vorrei … i Ho …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['vorrei', 'un', 'formaggio', '.'], 'Poproszę ser.', {}), (['vorrei', 'una', 'mela', '.'], 'Poproszę jabłko.', {}), (['vorrei', 'un', 'pesce', '.'], 'Poproszę rybę.', {}), (['vorrei', 'due', 'mele', '.'], 'Poproszę dwa jabłka.', {}), (['vorrei', 'un', 'vino', '.'], 'Poproszę wino.', {}), (['ho', 'una', 'sorella', '.'], 'Mam siostrę.', {}), (['ho', 'un', 'amico', '.'], 'Mam przyjaciela.', {}), (['ho', 'una', 'casa', '.'], 'Mam dom.', {}), (['ho', 'tre', 'mele', '.'], 'Mam trzy jabłka.', {}), (['ho', 'cinque', 'mele', '.'], 'Mam pięć jabłek.', {})]}, {'id': 'f02', 'title': "Wzór: Dov'è …? i Vado a …", 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(["dov'è", 'la', 'scuola', '?'], 'Gdzie jest szkoła?', {}), (["dov'è", 'la', 'casa', '?'], 'Gdzie jest dom?', {}), (["dov'è", 'la', 'strada', '?'], 'Gdzie jest ulica?', {}), (["dov'è", 'la', 'città', '?'], 'Gdzie jest miasto?', {}), (["dov'è", 'il', 'taxi', '?'], 'Gdzie jest taksówka?', {}), (["dov'è", 'il', 'mare', '?'], 'Gdzie jest morze?', {}), (["dov'è", 'Roma', '?'], 'Gdzie jest Rzym?', {}), (['vado', 'a', 'Roma', '.'], 'Idę do Rzymu.', {}), (['vado', 'a', 'scuola', '.'], 'Idę do szkoły.', {}), (['oggi', 'vado', 'a', 'casa', '.'], 'Dziś idę do domu.', {}), (['domani', 'vado', 'a', 'Roma', '.'], 'Jutro idę do Rzymu.', {}), (['adesso', 'vado', 'a', 'scuola', '.'], 'Teraz idę do szkoły.', {}), (['oggi', 'vado', 'a', 'scuola', '.'], 'Dziś idę do szkoły.', {})]}, {'id': 'f03', 'title': 'Wzór: Sono … Sei … È …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['io', 'sono', 'polacco', '.'], 'Ja jestem Polakiem.', {}), (['tu', 'sei', 'studente', '.'], 'Ty jesteś studentem.', {}), (['lui', 'è', 'insegnante', '.'], 'On jest nauczycielem.', {}), (['io', 'sono', 'studente', '.'], 'Ja jestem studentem.', {}), (['tu', 'sei', 'polacco', '.'], 'Ty jesteś Polakiem.', {})]}]
INSIGHTS.setdefault('f01', []).append({'title': 'Wzór: Vorrei … i Ho …', 'text': 'Ten sam szkielet, inne komponenty: Vorrei + to, co chcesz zamówić. Ho + to, co masz. Rodzajnik: un (męski), una (żeński).\n\nPrzykład: Vorrei un formaggio. = Poproszę ser.', 'chain': []})
INSIGHTS.setdefault('f02', []).append({'title': "Wzór: Dov'è …? i Vado a …", 'text': "Pytanie o miejsce: Dov'è + rzeczownik? Kierunek: Vado a + miejsce. Zmieniasz tylko miejsce.\n\nPrzykład: Dov'è la scuola? = Gdzie jest szkoła?", 'chain': []})
INSIGHTS.setdefault('f03', []).append({'title': 'Wzór: Sono … Sei … È …', 'text': 'Kto jest kim: osoba + essere + zawód lub narodowość. Sono (ja), sei (ty), è (on, ona).\n\nPrzykład: Io sono polacco. = Ja jestem Polakiem.', 'chain': []})
# === /BULK ===

# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['io', 'tu', 'lui/lei', 'noi', 'voi', 'loro'],
    'rodz': ['męski lp.', 'żeński lp.', 'męski lm.', 'żeński lm.'],
    'art': ['męski lp. (zwykły)', 'męski lp. przed z, s+spółgł.', 'żeński lp.', 'męski lm. (zwykły)', 'męski lm. przed z, s+spółgł.', 'żeński lm.'],
    'pp': ['parlare', 'credere', 'dormire', 'essere', 'avere', 'fare', 'dire', 'vedere', 'prendere', 'venire'],
    'ger': ['parlare', 'credere', 'dormire', 'essere', 'avere', 'fare'],
    't_aux': ['andare', 'mangiare', 'venire', 'vedere', 'partire', 'fare', 'restare', 'essere'],
    't_art': ['studente', 'libro', 'casa', 'amico', 'zio', 'ragazzo', 'acqua', 'scuola'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'parlare (mówić)', 'os', 'parlo; parli; parla; parliamo; parlate; parlano', 'Koniugacja -are.'),
    ('conj', 'Wzory koniugacji', 'credere (wierzyć)', 'os', 'credo; credi; crede; crediamo; credete; credono', 'Koniugacja -ere.'),
    ('conj', 'Wzory koniugacji', 'dormire (spać)', 'os', 'dormo; dormi; dorme; dormiamo; dormite; dormono', 'Koniugacja -ire.'),
    ('conj', 'Wyjątki', 'capire (rozumieć)', 'os', 'capisco; capisci; capisce; capiamo; capite; capiscono', 'Część czasowników na -ire wstawia -isc- (poza noi i voi).'),
    ('conj', 'Czasowniki nieregularne', 'essere (być)', 'os', 'sono; sei; è; siamo; siete; sono', None),
    ('conj', 'Czasowniki nieregularne', 'avere (mieć)', 'os', 'ho; hai; ha; abbiamo; avete; hanno', None),
    ('conj', 'Czasowniki nieregularne', 'andare (iść)', 'os', 'vado; vai; va; andiamo; andate; vanno', None),
    ('conj', 'Czasowniki nieregularne', 'fare (robić)', 'os', 'faccio; fai; fa; facciamo; fate; fanno', None),
    ('conj', 'Czasowniki nieregularne', 'stare (być, czuć się)', 'os', 'sto; stai; sta; stiamo; state; stanno', None),
    ('conj', 'Czasowniki nieregularne', 'volere (chcieć)', 'os', 'voglio; vuoi; vuole; vogliamo; volete; vogliono', None),
    ('conj', 'Czasowniki nieregularne', 'potere (móc)', 'os', 'posso; puoi; può; possiamo; potete; possono', None),
    ('conj', 'Czasowniki nieregularne', 'venire (przychodzić)', 'os', 'vengo; vieni; viene; veniamo; venite; vengono', None),
    ('decl', 'Przymiotniki: rodzaj i liczba', 'nuovo (nowy)', 'rodz', 'nuovo; nuova; nuovi; nuove', '-o, -a, -i, -e.'),
    ('decl', 'Przymiotniki: rodzaj i liczba', 'piccolo (mały)', 'rodz', 'piccolo; piccola; piccoli; piccole', None),
    ('decl', 'Wyjątki', 'grande (duży)', 'rodz', 'grande; grande; grandi; grandi', 'Przymiotniki na -e mają jedną formę dla obu rodzajów.'),
    ('decl', 'Rodzajnik określony', 'il, lo, la', 'art', 'il; lo; la; i; gli; le', None),
    ('form', 'Imiesłowy', 'Participio passato', 'pp', 'parlato; creduto; dormito; stato; avuto; fatto; detto; visto; preso; venuto', '-are → -ato, -ere → -uto, -ire → -ito.'),
    ('form', 'Imiesłowy', 'Gerundio', 'ger', 'parlando; credendo; dormendo; essendo; avendo; facendo', None),
    ('conj', 'Czas przeszły', 'parlare: passato prossimo', 'os', 'ho parlato; hai parlato; ha parlato; abbiamo parlato; avete parlato; hanno parlato', None),
    ('conj', 'Czas przeszły', 'andare: passato prossimo', 'os', 'sono andato; sei andato; è andato; siamo andati; siete andati; sono andati', 'Z essere imiesłów zgadza się z podmiotem: andato, andata, andati, andate.'),
    ('conj', 'Czas przeszły', 'parlare: imperfetto', 'os', 'parlavo; parlavi; parlava; parlavamo; parlavate; parlavano', None),
    ('conj', 'Czas przeszły', 'essere: imperfetto', 'os', 'ero; eri; era; eravamo; eravate; erano', None),
    ('conj', 'Czas przyszły', 'parlare: futuro', 'os', 'parlerò; parlerai; parlerà; parleremo; parlerete; parleranno', None),
    ('conj', 'Czas przyszły', 'essere: futuro', 'os', 'sarò; sarai; sarà; saremo; sarete; saranno', None),
    ('form', 'Typowe trudności', 'Passato prossimo: essere czy avere?', 't_aux', 'essere; avere; essere; avere; essere; avere; essere; essere', None),
    ('form', 'Typowe trudności', "Rodzajnik: il, lo, la czy l'?", 't_art', "lo; il; la; l'; lo; il; l'; la", None),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['di + il', 'a + la', 'in + il', 'su + il', 'da + i', 'a + gli', 'di + la', 'in + la'],
    't_m1': ['pala', 'palla', 'caro', 'carro', 'nono', 'nonno', 'sete', 'sette'],
    't_m2': ['libro', 'casa', 'amico', 'amica', 'città', 'uomo', 'problema', 'mano'],
    't_m3': ['tavola', 'musica', 'telefono', 'città', 'amico', 'caffè', 'parlano', 'andiamo'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Przyimek + rodzajnik', 't_m0', 'del; alla; nel; sul; dai; agli; della; nella', 'Przyimek zlewa się z rodzajnikiem w jedno słowo.'),
    ('form', 'Typowe trudności', 'Podwójna spółgłoska: co to znaczy?', 't_m1', 'łopata; piłka; drogi; wóz; dziewiąty; dziadek; pragnienie; siedem', 'Na podwójnej spółgłosce trzeba się zatrzymać.'),
    ('form', 'Typowe trudności', 'Liczba mnoga', 't_m2', 'libri; case; amici; amiche; città; uomini; problemi; mani', '-o → -i, -a → -e. Słowa akcentowane na końcu się nie zmieniają; uomo, mano i słowa na -ma to wyjątki.'),
    ('form', 'Typowe trudności', 'Akcent: która sylaba?', 't_m3', 'tà-vola; mù-sica; telè-fono; cit-tà; a-mì-co; caf-fè; pàr-lano; an-dià-mo', 'Akcent często pada na trzecią sylabę od końca, a w 3. osobie lm. nawet dalej: pàrlano.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['Nie mam czasu.', 'Widzę go.', 'Chcę to zjeść.', 'Lubię kawę.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: zaimki i przeczenie', 't_s0', 'Non ho tempo.|Ho non tempo.|Non tempo ho.|Ho tempo non.; Lo vedo.|Vedo lo.|Lo io vedo.|Io vedo lo.; Voglio mangiarlo.|Voglio mangiare lo.|Voglio lo mangiare.|Lo mangiare voglio.; Mi piace il caffè.|Piace mi il caffè.|Mi il caffè piace.|Il caffè piace mi.', 'Non stoi przed czasownikiem. Zaimek stoi przed odmienionym czasownikiem albo przyklejony do bezokolicznika.'),
]
