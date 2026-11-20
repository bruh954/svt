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

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'mi, ti, lo… (dopełnienie bliższe)', 'os', 'mi; ti; lo, la; ci; vi; li, le', 'Stoją przed czasownikiem: lo vedo.'),
    ('decl', 'Zaimki', 'mi, ti, gli… (dopełnienie dalsze)', 'os', 'mi; ti; gli, le; ci; vi; gli', None),
    ('decl', 'Zaimki', 'me, te, lui… (zaimki akcentowane)', 'os', 'me; te; lui, lei; noi; voi; loro', 'Po przyimku i do podkreślenia: per me.'),
    ('decl', 'Zaimki', 'mi, ti, si… (zwrotne)', 'os', 'mi; ti; si; ci; vi; si', None),
    ('decl', 'Zaimki', 'mio, tuo, suo… (mój, twój…)', 'os', 'mio; tuo; suo; nostro; vostro; loro', 'Zwykle z rodzajnikiem: il mio libro.'),
    ('decl', 'Zaimki', 'questo (ten tu)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'rodzaj męski lm.', 'rodzaj żeński lm.'], 'questo; questa; questi; queste', None),
    ('decl', 'Zaimki', 'quello (tamten)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'rodzaj męski lm.', 'rodzaj żeński lm.'], 'quel; quella; quei; quelle', 'Odmienia się jak rodzajnik: quel libro, quello studente.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'hai una sorella': 'Masz siostrę.', 'vorrei un tè': 'Poproszę herbatę.', 'sono di Polonia': 'Jestem z Polski.'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'buono (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'buono; migliore; il migliore', 'Nieregularne; też più buono.'),
    ('form', 'Stopniowanie', 'bello (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'bello; più bello; il più bello', None),
    ('form', 'Stopniowanie', 'alto (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'alto; più alto; il più alto', None),
    ('form', 'Stopniowanie', 'bene (dobrze)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'bene; meglio; il meglio', 'Przysłówek: nieregularny.'),
    ('form', 'Stopniowanie', 'veloce (szybki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'veloce; più veloce; il più veloce', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 1 (generowane) ===
PARADIGMS += [
    ('conj', 'Czas przeszły', 'avere: imperfetto', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'avevo; avevi; aveva; avevamo; avevate; avevano', None),
    ('conj', 'Czas przeszły', 'fare: imperfetto', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'facevo; facevi; faceva; facevamo; facevate; facevano', None),
    ('conj', 'Czas przeszły', 'andare: imperfetto', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'andavo; andavi; andava; andavamo; andavate; andavano', None),
    ('conj', 'Czas przeszły', 'credere: imperfetto', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'credevo; credevi; credeva; credevamo; credevate; credevano', None),
    ('conj', 'Czas przeszły', 'dormire: imperfetto', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'dormivo; dormivi; dormiva; dormivamo; dormivate; dormivano', None),
    ('conj', 'Czas przeszły', 'essere: passato prossimo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'sono stato; sei stato; è stato; siamo stati; siete stati; sono stati', None),
    ('conj', 'Czas przeszły', 'avere: passato prossimo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'ho avuto; hai avuto; ha avuto; abbiamo avuto; avete avuto; hanno avuto', None),
    ('conj', 'Czas przeszły', 'fare: passato prossimo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'ho fatto; hai fatto; ha fatto; abbiamo fatto; avete fatto; hanno fatto', None),
    ('conj', 'Czas przeszły', 'venire: passato prossimo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'sono venuto; sei venuto; è venuto; siamo venuti; siete venuti; sono venuti', None),
    ('conj', 'Czas przyszły', 'avere: futuro', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'avrò; avrai; avrà; avremo; avrete; avranno', None),
    ('conj', 'Czas przyszły', 'andare: futuro', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'andrò; andrai; andrà; andremo; andrete; andranno', None),
    ('conj', 'Czas przyszły', 'fare: futuro', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'farò; farai; farà; faremo; farete; faranno', None),
    ('conj', 'Czas przyszły', 'potere: futuro', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'potrò; potrai; potrà; potremo; potrete; potranno', None),
    ('conj', 'Czas przyszły', 'volere: futuro', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'vorrò; vorrai; vorrà; vorremo; vorrete; vorranno', None),
    ('conj', 'Czas przyszły', 'venire: futuro', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'verrò; verrai; verrà; verremo; verrete; verranno', None),
    ('conj', 'Tryb warunkowy', 'parlare: condizionale', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'parlerei; parleresti; parlerebbe; parleremmo; parlereste; parlerebbero', None),
    ('conj', 'Tryb warunkowy', 'essere: condizionale', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'sarei; saresti; sarebbe; saremmo; sareste; sarebbero', None),
    ('conj', 'Tryb warunkowy', 'avere: condizionale', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'avrei; avresti; avrebbe; avremmo; avreste; avrebbero', None),
    ('conj', 'Tryb warunkowy', 'andare: condizionale', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'andrei; andresti; andrebbe; andremmo; andreste; andrebbero', None),
    ('conj', 'Tryb warunkowy', 'fare: condizionale', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'farei; faresti; farebbe; faremmo; fareste; farebbero', None),
    ('conj', 'Tryb warunkowy', 'potere: condizionale', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'potrei; potresti; potrebbe; potremmo; potreste; potrebbero', None),
    ('conj', 'Tryb warunkowy', 'volere: condizionale', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'vorrei; vorresti; vorrebbe; vorremmo; vorreste; vorrebbero', 'Grzeczna prośba: vorrei un caffè.'),
    ('conj', 'Tryb łączący', 'parlare: congiuntivo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'parli; parli; parli; parliamo; parliate; parlino', None),
    ('conj', 'Tryb łączący', 'credere: congiuntivo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'creda; creda; creda; crediamo; crediate; credano', None),
    ('conj', 'Tryb łączący', 'dormire: congiuntivo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'dorma; dorma; dorma; dormiamo; dormiate; dormano', None),
    ('conj', 'Tryb łączący', 'essere: congiuntivo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'sia; sia; sia; siamo; siate; siano', 'Po „penso che”, „voglio che”: penso che sia vero.'),
    ('conj', 'Tryb łączący', 'avere: congiuntivo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'abbia; abbia; abbia; abbiamo; abbiate; abbiano', None),
    ('conj', 'Tryb łączący', 'andare: congiuntivo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'vada; vada; vada; andiamo; andiate; vadano', None),
    ('conj', 'Tryb łączący', 'fare: congiuntivo', ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro'], 'faccia; faccia; faccia; facciamo; facciate; facciano', None),
    ('form', 'Tryb rozkazujący', 'parlare: imperativo', ['tu', 'Lei', 'noi', 'voi'], 'parla; parli; parliamo; parlate', None),
    ('form', 'Tryb rozkazujący', 'credere: imperativo', ['tu', 'Lei', 'noi', 'voi'], 'credi; creda; crediamo; credete', None),
    ('form', 'Tryb rozkazujący', 'dormire: imperativo', ['tu', 'Lei', 'noi', 'voi'], 'dormi; dorma; dormiamo; dormite', None),
    ('form', 'Tryb rozkazujący', 'essere: imperativo', ['tu', 'Lei', 'noi', 'voi'], 'sii; sia; siamo; siate', None),
    ('form', 'Tryb rozkazujący', 'avere: imperativo', ['tu', 'Lei', 'noi', 'voi'], 'abbi; abbia; abbiamo; abbiate', None),
    ('form', 'Tryb rozkazujący', 'andare: imperativo', ['tu', 'Lei', 'noi', 'voi'], "va'; vada; andiamo; andate", None),
    ('form', 'Tryb rozkazujący', 'fare: imperativo', ['tu', 'Lei', 'noi', 'voi'], "fa'; faccia; facciamo; fate", None),
    ('form', 'Przyimki z rodzajnikiem', 'a + rodzajnik', ['il', 'lo', 'la', "l'", 'i', 'gli', 'le'], "al; allo; alla; all'; ai; agli; alle", 'Przyimek łączy się z rodzajnikiem w jedno słowo.'),
    ('form', 'Przyimki z rodzajnikiem', 'di + rodzajnik', ['il', 'lo', 'la', "l'", 'i', 'gli', 'le'], "del; dello; della; dell'; dei; degli; delle", None),
    ('form', 'Przyimki z rodzajnikiem', 'in + rodzajnik', ['il', 'lo', 'la', "l'", 'i', 'gli', 'le'], "nel; nello; nella; nell'; nei; negli; nelle", None),
    ('form', 'Przyimki z rodzajnikiem', 'su + rodzajnik', ['il', 'lo', 'la', "l'", 'i', 'gli', 'le'], "sul; sullo; sulla; sull'; sui; sugli; sulle", None),
    ('form', 'Przyimki z rodzajnikiem', 'da + rodzajnik', ['il', 'lo', 'la', "l'", 'i', 'gli', 'le'], "dal; dallo; dalla; dall'; dai; dagli; dalle", None),
    ('form', 'Przyimki z rodzajnikiem', 'con + rodzajnik', ['il', 'lo', 'la', "l'", 'i', 'gli', 'le'], "col; con lo; con la; con l'; coi; con gli; con le", None),
    ('form', 'Rodzajnik nieokreślony', 'un, uno, una', ['rodzaj męski', 'rodzaj męski (s+spółgł., z, gn)', 'rodzaj żeński', 'żeński przed samogłoską'], "un; uno; una; un'", None),
    ('form', 'Typowe czasowniki', 'piacere (podobać się)', ['(a me)', '(a te)', '(a lui / lei)', '(a noi)', '(a voi)', '(a loro)'], 'mi piace; ti piace; gli / le piace; ci piace; vi piace; piace loro', 'Uzgadnia się z tym, co się podoba: mi piace il caffè, mi piacciono i libri.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 1 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('ragazzo', 'chłopiec', None, 'rodzaj męski'), ('bambina', 'dziewczynka', None, 'rodzaj żeński'), ('persona', 'człowiek', None, 'rodzaj żeński'), ('gente', 'ludzie', None, 'rodzaj żeński'), ('famiglia', 'rodzina', None, 'rodzaj żeński'), ('figlio', 'syn', None, 'rodzaj męski'), ('figlia', 'córka', None, 'rodzaj żeński'), ('nonno', 'dziadek', None, 'rodzaj męski'), ('nonna', 'babcia', None, 'rodzaj żeński'), ('nipote', 'wnuk', None, 'rodzaj męski'), ('zio', 'wujek', None, 'rodzaj męski'), ('zia', 'ciocia', None, 'rodzaj żeński'), ('cugino', 'kuzyn', None, 'rodzaj męski'), ('marito', 'mąż', None, 'rodzaj męski'), ('moglie', 'żona', None, 'rodzaj żeński'), ('vicino', 'sąsiad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('ospite', 'gość', None, 'rodzaj męski'), ('capo', 'szef', None, 'rodzaj męski'), ('collega', 'kolega', None, 'rodzaj męski'), ('nemico', 'wróg', None, 'rodzaj męski'), ('re', 'król', None, 'rodzaj męski'), ('regina', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('testa', 'głowa', None, 'rodzaj żeński'), ('faccia', 'twarz', None, 'rodzaj żeński'), ('occhio', 'oko', None, 'rodzaj męski'), ('orecchio', 'ucho', None, 'rodzaj męski'), ('naso', 'nos', None, 'rodzaj męski'), ('bocca', 'usta', None, 'rodzaj żeński'), ('dente', 'ząb', None, 'rodzaj męski'), ('lingua', 'język (narząd)', None, 'rodzaj żeński'), ('capelli', 'włosy', None, 'rodzaj męski'), ('collo', 'szyja', None, 'rodzaj męski'), ('braccio', 'ramię', None, 'rodzaj męski'), ('mano', 'ręka', None, 'rodzaj żeński'), ('dito', 'palec', None, 'rodzaj męski'), ('gamba', 'noga', None, 'rodzaj żeński'), ('piede', 'stopa', None, 'rodzaj męski'), ('ginocchio', 'kolano', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('schiena', 'plecy', None, 'rodzaj żeński'), ('pancia', 'brzuch', None, 'rodzaj żeński'), ('cuore', 'serce', None, 'rodzaj męski'), ('sangue', 'krew', None, 'rodzaj męski'), ('osso', 'kość', None, 'rodzaj męski'), ('pelle', 'skóra', None, 'rodzaj żeński'), ('voce', 'głos', None, 'rodzaj żeński'), ('corpo', 'ciało', None, 'rodzaj męski'), ('stomaco', 'żołądek', None, 'rodzaj męski'), ('barba', 'broda', None, 'rodzaj żeński'), ('labbro', 'warga', None, 'rodzaj męski'), ('unghia', 'paznokieć', None, 'rodzaj żeński'), ('petto', 'pierś', None, 'rodzaj męski'), ('cervello', 'mózg', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('burro', 'masło', None, 'rodzaj męski'), ('uovo', 'jajko', None, 'rodzaj męski'), ('carne', 'mięso', None, 'rodzaj żeński'), ('pollo', 'kurczak', None, 'rodzaj męski'), ('maiale', 'wieprzowina', None, 'rodzaj męski'), ('zuppa', 'zupa', None, 'rodzaj żeński'), ('insalata', 'sałatka', None, 'rodzaj żeński'), ('riso', 'ryż', None, 'rodzaj męski'), ('pasta', 'makaron', None, 'rodzaj żeński'), ('patata', 'ziemniak', None, 'rodzaj żeński'), ('carota', 'marchewka', None, 'rodzaj żeński'), ('cipolla', 'cebula', None, 'rodzaj żeński'), ('aglio', 'czosnek', None, 'rodzaj męski'), ('pomodoro', 'pomidor', None, 'rodzaj męski'), ('cetriolo', 'ogórek', None, 'rodzaj męski'), ('pera', 'gruszka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('banana', 'banan', None, 'rodzaj żeński'), ('arancia', 'pomarańcza', None, 'rodzaj żeński'), ('limone', 'cytryna', None, 'rodzaj męski'), ('fragola', 'truskawka', None, 'rodzaj żeński'), ('uva', 'winogrono', None, 'rodzaj żeński'), ('zucchero', 'cukier', None, 'rodzaj męski'), ('sale', 'sól', None, 'rodzaj męski'), ('pepe', 'pieprz', None, 'rodzaj męski'), ('olio', 'olej', None, 'rodzaj męski'), ('farina', 'mąka', None, 'rodzaj żeński'), ('miele', 'miód', None, 'rodzaj męski'), ('cioccolato', 'czekolada', None, 'rodzaj męski'), ('gelato', 'lody', None, 'rodzaj męski'), ('torta', 'ciasto (tort)', None, 'rodzaj żeński'), ('biscotto', 'ciastko', None, 'rodzaj męski'), ('colazione', 'śniadanie', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('pranzo', 'obiad', None, 'rodzaj męski'), ('cena', 'kolacja', None, 'rodzaj żeński'), ('spuntino', 'przekąska', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('succo', 'sok', None, 'rodzaj męski'), ('birra', 'piwo', None, 'rodzaj żeński'), ('bevanda', 'napój', None, 'rodzaj żeński'), ('bicchiere', 'szklanka', None, 'rodzaj męski'), ('tazza', 'filiżanka', None, 'rodzaj żeński'), ('piatto', 'talerz', None, 'rodzaj męski'), ('coltello', 'nóż', None, 'rodzaj męski'), ('forchetta', 'widelec', None, 'rodzaj żeński'), ('cucchiaio', 'łyżka', None, 'rodzaj męski'), ('bottiglia', 'butelka', None, 'rodzaj żeński'), ('menù', 'menu', None, 'rodzaj męski'), ('conto', 'rachunek', None, 'rodzaj męski'), ('mancia', 'napiwek', None, 'rodzaj żeński'), ('tavolo', 'stolik', None, 'rodzaj męski'), ('cameriere', 'kelner', None, 'rodzaj męski'), ('cuoco', 'kucharz', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('affamato', 'głodny', None, None), ('assetato', 'spragniony', None, None), ('gustoso', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('appartamento', 'mieszkanie', None, 'rodzaj męski'), ('camera', 'pokój', None, 'rodzaj żeński'), ('cucina', 'kuchnia', None, 'rodzaj żeński'), ('bagno', 'łazienka', None, 'rodzaj męski'), ('camera da letto', 'sypialnia', None, 'rodzaj żeński'), ('salotto', 'salon', None, 'rodzaj męski'), ('giardino', 'ogród', None, 'rodzaj męski'), ('porta', 'drzwi', None, 'rodzaj żeński'), ('finestra', 'okno', None, 'rodzaj żeński'), ('parete', 'ściana', None, 'rodzaj żeński'), ('pavimento', 'podłoga', None, 'rodzaj męski'), ('tetto', 'dach', None, 'rodzaj męski'), ('scala', 'schody', None, 'rodzaj żeński'), ('chiave', 'klucz', None, 'rodzaj żeński'), ('tavolo (stół)', 'stół', None, 'rodzaj męski'), ('sedia', 'krzesło', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('letto', 'łóżko', None, 'rodzaj męski'), ('armadio', 'szafa', None, 'rodzaj męski'), ('lampada', 'lampa', None, 'rodzaj żeński'), ('tappeto', 'dywan', None, 'rodzaj męski'), ('specchio', 'lustro', None, 'rodzaj męski'), ('televisore', 'telewizor', None, 'rodzaj męski'), ('telefono', 'telefon', None, 'rodzaj męski'), ('computer', 'komputer', None, 'rodzaj męski'), ('orologio', 'zegar', None, 'rodzaj męski'), ('cuscino', 'poduszka', None, 'rodzaj męski'), ('coperta', 'koc', None, 'rodzaj żeński'), ('asciugamano', 'ręcznik', None, 'rodzaj męski'), ('sapone', 'mydło', None, 'rodzaj męski'), ('spazzolino', 'szczoteczka do zębów', None, 'rodzaj męski'), ('frigorifero', 'lodówka', None, 'rodzaj męski'), ('forno', 'piec', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('lavatrice', 'pralka', None, 'rodzaj żeński'), ('spazzatura', 'śmieci', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('vestito', 'ubranie', None, 'rodzaj męski'), ('camicia', 'koszula', None, 'rodzaj żeński'), ('pantaloni', 'spodnie', None, 'rodzaj męski'), ('abito', 'sukienka', None, 'rodzaj męski'), ('gonna', 'spódnica', None, 'rodzaj żeński'), ('giacca', 'kurtka', None, 'rodzaj żeński'), ('cappotto', 'płaszcz', None, 'rodzaj męski'), ('maglione', 'sweter', None, 'rodzaj męski'), ('scarpa', 'buty', None, 'rodzaj żeński'), ('calzino', 'skarpetki', None, 'rodzaj męski'), ('berretto', 'czapka', None, 'rodzaj męski'), ('cappello', 'kapelusz', None, 'rodzaj męski'), ('guanto', 'rękawiczki', None, 'rodzaj męski'), ('sciarpa', 'szalik', None, 'rodzaj żeński'), ('borsa', 'torba', None, 'rodzaj żeński'), ('zaino', 'plecak', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('portafoglio', 'portfel', None, 'rodzaj męski'), ('occhiali', 'okulary', None, 'rodzaj męski'), ('orologio da polso', 'zegarek', None, 'rodzaj męski'), ('anello', 'pierścionek', None, 'rodzaj męski'), ('biancheria', 'bielizna', None, 'rodzaj żeński'), ('pigiama', 'piżama', None, 'rodzaj męski'), ('cintura', 'pasek', None, 'rodzaj żeński'), ('cravatta', 'krawat', None, 'rodzaj żeński'), ('completo', 'garnitur', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('rosso', 'czerwony', None, None), ('azzurro', 'niebieski', None, None), ('verde', 'zielony', None, None), ('giallo', 'żółty', None, None), ('nero', 'czarny', None, None), ('bianco', 'biały', None, None), ('grigio', 'szary', None, None), ('marrone', 'brązowy', None, None), ('rosa', 'różowy', None, None), ('viola', 'fioletowy', None, None), ('colore', 'kolor', None, 'rodzaj męski'), ('rotondo', 'okrągły', None, None), ('quadrato', 'kwadratowy', None, None), ('dritto', 'prosty', None, None), ('storto', 'krzywy', None, None), ('linea', 'linia', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('punto', 'punkt', None, 'rodzaj męski'), ('cerchio', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('zero', 'zero', None, None), ('undici', 'jedenaście', None, None), ('dodici', 'dwanaście', None, None), ('tredici', 'trzynaście', None, None), ('quattordici', 'czternaście', None, None), ('quindici', 'piętnaście', None, None), ('sedici', 'szesnaście', None, None), ('diciassette', 'siedemnaście', None, None), ('diciotto', 'osiemnaście', None, None), ('diciannove', 'dziewiętnaście', None, None), ('venti', 'dwadzieścia', None, None), ('trenta', 'trzydzieści', None, None), ('quaranta', 'czterdzieści', None, None), ('cinquanta', 'pięćdziesiąt', None, None), ('sessanta', 'sześćdziesiąt', None, None), ('settanta', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('ottanta', 'osiemdziesiąt', None, None), ('novanta', 'dziewięćdziesiąt', None, None), ('cento', 'sto', None, None), ('mille', 'tysiąc', None, None), ('milione', 'milion', None, 'rodzaj męski'), ('primo', 'pierwszy', None, None), ('secondo', 'drugi', None, None), ('terzo', 'trzeci', None, None), ('metà', 'połowa', None, 'rodzaj żeński'), ('paio', 'para', None, 'rodzaj męski'), ('alcuni', 'kilka', None, None), ('molti', 'wiele', None, None), ('poco', 'mało', None, None), ('intero', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('minuto', 'minuta', None, 'rodzaj męski'), ('giorno', 'dzień', None, 'rodzaj męski'), ('notte', 'noc', None, 'rodzaj żeński'), ('settimana', 'tydzień', None, 'rodzaj żeński'), ('mese', 'miesiąc', None, 'rodzaj męski'), ('anno', 'rok', None, 'rodzaj męski'), ('primavera', 'wiosna', None, 'rodzaj żeński'), ('estate', 'lato', None, 'rodzaj żeński'), ('autunno', 'jesień', None, 'rodzaj męski'), ('inverno', 'zima', None, 'rodzaj męski'), ('lunedì', 'poniedziałek', None, 'rodzaj męski'), ('martedì', 'wtorek', None, 'rodzaj męski'), ('mercoledì', 'środa', None, 'rodzaj męski'), ('giovedì', 'czwartek', None, 'rodzaj męski'), ('venerdì', 'piątek', None, 'rodzaj męski'), ('sabato', 'sobota', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('domenica', 'niedziela', None, 'rodzaj żeński'), ('gennaio', 'styczeń', None, 'rodzaj męski'), ('febbraio', 'luty', None, 'rodzaj męski'), ('marzo', 'marzec', None, 'rodzaj męski'), ('aprile', 'kwiecień', None, 'rodzaj męski'), ('maggio', 'maj', None, 'rodzaj męski'), ('giugno', 'czerwiec', None, 'rodzaj męski'), ('luglio', 'lipiec', None, 'rodzaj męski'), ('agosto', 'sierpień', None, 'rodzaj męski'), ('settembre', 'wrzesień', None, 'rodzaj męski'), ('ottobre', 'październik', None, 'rodzaj męski'), ('novembre', 'listopad', None, 'rodzaj męski'), ('dicembre', 'grudzień', None, 'rodzaj męski'), ('mattina', 'rano (pora dnia)', None, 'rodzaj żeński'), ('mezzogiorno', 'południe', None, 'rodzaj męski'), ('di sera', 'wieczorem', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('sempre', 'zawsze', None, None), ('mai', 'nigdy', None, None), ('a volte', 'czasem', None, None), ('spesso', 'często', None, None), ('già', 'już', None, None), ('ancora', 'jeszcze', None, None), ('presto', 'wkrótce', None, None), ('più tardi', 'później', None, None), ('presto (wcześnie)', 'wcześnie', None, None), ('tardi', 'późno', None, None), ('quando', 'kiedy (pytanie)', None, None), ('data', 'data', None, 'rodzaj żeński'), ('passato', 'przeszłość', None, 'rodzaj męski'), ('futuro', 'przyszłość', None, 'rodzaj męski'), ('compleanno', 'urodziny', None, 'rodzaj męski'), ('festa', 'święto', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('vacanze', 'wakacje', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('sole', 'słońce', None, 'rodzaj męski'), ('luna', 'księżyc', None, 'rodzaj żeński'), ('stella', 'gwiazda', None, 'rodzaj żeński'), ('cielo', 'niebo', None, 'rodzaj męski'), ('nuvola', 'chmura', None, 'rodzaj żeński'), ('pioggia', 'deszcz', None, 'rodzaj żeński'), ('neve', 'śnieg', None, 'rodzaj żeński'), ('vento', 'wiatr', None, 'rodzaj męski'), ('temporale', 'burza', None, 'rodzaj męski'), ('nebbia', 'mgła', None, 'rodzaj żeński'), ('ghiaccio', 'lód', None, 'rodzaj męski'), ('fuoco', 'ogień', None, None), ('terra', 'grunt)', None, 'rodzaj żeński'), ('fiume', 'rzeka', None, 'rodzaj męski'), ('lago', 'jezioro', None, 'rodzaj męski'), ('montagna', 'góra', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('bosco', 'las', None, 'rodzaj męski'), ('albero', 'drzewo', None, 'rodzaj męski'), ('fiore', 'kwiat', None, 'rodzaj męski'), ('erba', 'trawa', None, 'rodzaj żeński'), ('foglia', 'liść', None, 'rodzaj żeński'), ('campo', 'pole', None, 'rodzaj męski'), ('isola', 'wyspa', None, 'rodzaj żeński'), ('spiaggia', 'plaża', None, 'rodzaj żeński'), ('deserto', 'pustynia', None, 'rodzaj męski'), ('roccia', 'skała', None, 'rodzaj żeński'), ('pietra', 'kamień', None, 'rodzaj żeński'), ('tempo', 'pogoda', None, 'rodzaj męski'), ('temperatura', 'temperatura', None, 'rodzaj żeński'), ('freddo', 'zimny', None, None), ('tiepido', 'ciepły', None, None), ('caldo', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('cane', 'pies', None, 'rodzaj męski'), ('gatto', 'kot', None, 'rodzaj męski'), ('cavallo', 'koń', None, 'rodzaj męski'), ('mucca', 'krowa', None, 'rodzaj żeński'), ('maiale (zwierzę)', 'świnia', None, 'rodzaj męski'), ('pecora', 'owca', None, 'rodzaj żeński'), ('capra', 'koza', None, 'rodzaj żeński'), ('gallina', 'kura', None, 'rodzaj żeński'), ('anatra', 'kaczka', None, 'rodzaj żeński'), ('uccello', 'ptak', None, 'rodzaj męski'), ('topo', 'mysz', None, 'rodzaj męski'), ('ratto', 'szczur', None, 'rodzaj męski'), ('serpente', 'wąż', None, 'rodzaj męski'), ('rana', 'żaba', None, 'rodzaj żeński'), ('leone', 'lew', None, 'rodzaj męski'), ('tigre', 'tygrys', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('elefante', 'słoń', None, 'rodzaj męski'), ('orso', 'niedźwiedź', None, 'rodzaj męski'), ('lupo', 'wilk', None, 'rodzaj męski'), ('volpe', 'lis', None, 'rodzaj żeński'), ('lepre', 'zając', None, 'rodzaj żeński'), ('cervo', 'jeleń', None, 'rodzaj męski'), ('scimmia', 'małpa', None, 'rodzaj żeński'), ('farfalla', 'motyl', None, 'rodzaj żeński'), ('ape', 'pszczoła', None, 'rodzaj żeński'), ('mosca', 'mucha', None, 'rodzaj żeński'), ('ragno', 'pająk', None, 'rodzaj męski'), ('animale', 'zwierzę', None, 'rodzaj męski'), ('insetto', 'owad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('paese', 'wieś', None, 'rodzaj męski'), ('via', 'droga', None, 'rodzaj żeński'), ('piazza', 'plac', None, 'rodzaj żeński'), ('ponte', 'most', None, 'rodzaj męski'), ('parco', 'park', None, 'rodzaj męski'), ('negozio', 'sklep', None, 'rodzaj męski'), ('mercato', 'targ', None, 'rodzaj męski'), ('supermercato', 'supermarket', None, 'rodzaj męski'), ('banca', 'bank', None, 'rodzaj żeński'), ('posta', 'poczta', None, 'rodzaj żeński'), ('ospedale', 'szpital', None, 'rodzaj męski'), ('farmacia', 'apteka', None, 'rodzaj żeński'), ('università', 'uniwersytet', None, 'rodzaj żeński'), ('biblioteca', 'biblioteka', None, 'rodzaj żeński'), ('museo', 'muzeum', None, 'rodzaj męski'), ('chiesa', 'kościół', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('ristorante', 'restauracja', None, 'rodzaj męski'), ('bar', 'kawiarnia', None, 'rodzaj męski'), ('aeroporto', 'lotnisko', None, 'rodzaj męski'), ('stazione', 'dworzec', None, 'rodzaj żeński'), ('fermata', 'przystanek', None, 'rodzaj żeński'), ('cinema', 'kino', None, 'rodzaj męski'), ('teatro', 'teatr', None, 'rodzaj męski'), ('polizia', 'policja', None, 'rodzaj żeński'), ('ufficio', 'biuro', None, 'rodzaj męski'), ('fabbrica', 'fabryka', None, 'rodzaj żeński'), ('edificio', 'budynek', None, 'rodzaj męski'), ('torre', 'wieża', None, 'rodzaj żeński'), ('centro', 'centrum', None, 'rodzaj męski'), ('indirizzo', 'adres', None, 'rodzaj męski'), ('mappa', 'mapa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('macchina', 'samochód', None, 'rodzaj żeński'), ('autobus', 'autobus', None, 'rodzaj męski'), ('treno', 'pociąg', None, 'rodzaj męski'), ('tram', 'tramwaj', None, 'rodzaj męski'), ('metropolitana', 'metro', None, 'rodzaj żeński'), ('aereo', 'samolot', None, 'rodzaj męski'), ('nave', 'statek', None, 'rodzaj żeński'), ('bicicletta', 'rower', None, 'rodzaj żeński'), ('moto', 'motocykl', None, 'rodzaj żeński'), ('biglietto', 'bilet', None, 'rodzaj męski'), ('viaggio', 'podróż', None, 'rodzaj męski'), ('gita', 'wycieczka', None, 'rodzaj żeński'), ('passaporto', 'paszport', None, 'rodzaj męski'), ('valigia', 'walizka', None, 'rodzaj żeński'), ('benzina', 'benzyna', None, 'rodzaj żeński'), ('parcheggio', 'parking', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('incrocio', 'skrzyżowanie', None, 'rodzaj męski'), ('semaforo', 'światła', None, 'rodzaj męski'), ('patente', 'prawo jazdy', None, 'rodzaj żeński'), ('autista', 'kierowca', None, 'rodzaj męski'), ('passeggero', 'pasażer', None, 'rodzaj męski'), ('entrata', 'wjazd', None, 'rodzaj żeński'), ('uscita', 'wyjazd', None, 'rodzaj żeński'), ('ferrovia', 'kolej', None, 'rodzaj żeński'), ('porto', 'port', None, 'rodzaj męski'), ('confine', 'granica', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('lavoro', 'praca', None, 'rodzaj męski'), ('professione', 'zawód', None, 'rodzaj żeński'), ('medico', 'lekarz', None, 'rodzaj męski'), ('infermiera', 'pielęgniarka', None, 'rodzaj żeński'), ('maestro', 'nauczyciel', None, 'rodzaj męski'), ('alunno', 'uczeń', None, 'rodzaj męski'), ('ingegnere', 'inżynier', None, 'rodzaj męski'), ('avvocato', 'prawnik', None, 'rodzaj męski'), ('poliziotto', 'policjant', None, 'rodzaj męski'), ('soldato', 'żołnierz', None, 'rodzaj męski'), ('contadino', 'rolnik', None, 'rodzaj męski'), ('commesso', 'sprzedawca', None, 'rodzaj męski'), ('cassiere', 'kasjer', None, 'rodzaj męski'), ('attore', 'aktor', None, 'rodzaj męski'), ('scrittore', 'pisarz', None, 'rodzaj męski'), ('pittore', 'malarz', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('musicista', 'muzyk', None, 'rodzaj męski'), ('artista', 'artysta', None, 'rodzaj męski'), ('azienda', 'firma', None, 'rodzaj żeński'), ('soldi', 'pieniądze', None, 'rodzaj męski'), ('stipendio', 'pensja', None, 'rodzaj męski'), ('contratto', 'umowa', None, 'rodzaj męski'), ('riunione', 'spotkanie', None, 'rodzaj żeński'), ('lezione', 'lekcja', None, 'rodzaj żeński'), ('esame', 'egzamin', None, 'rodzaj męski'), ('voto', 'ocena', None, 'rodzaj męski'), ('classe', 'klasa', None, 'rodzaj żeński'), ('libro', 'książka', None, 'rodzaj męski'), ('quaderno', 'zeszyt', None, 'rodzaj męski'), ('penna', 'długopis', None, 'rodzaj żeński'), ('matita', 'ołówek', None, 'rodzaj żeński'), ('carta', 'papier', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('lavagna', 'tablica', None, 'rodzaj żeński'), ('dizionario', 'słownik', None, 'rodzaj męski'), ('domanda', 'pytanie', None, 'rodzaj żeński'), ('risposta', 'odpowiedź', None, 'rodzaj żeński'), ('compito', 'zadanie', None, 'rodzaj męski'), ('test', 'test', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('prezzo', 'cena', None, 'rodzaj męski'), ('carta di credito', 'karta (płatnicza)', None, 'rodzaj żeński'), ('contanti', 'gotówka', None, 'rodzaj męski'), ('moneta', 'moneta', None, 'rodzaj żeński'), ('banconota', 'banknot', None, 'rodzaj żeński'), ('resto', 'reszta', None, 'rodzaj męski'), ('sconto', 'zniżka', None, 'rodzaj męski'), ('cestino', 'koszyk', None, 'rodzaj męski'), ('scontrino', 'paragon', None, 'rodzaj męski'), ('merce', 'towar', None, 'rodzaj żeński'), ('acquisto', 'zakup', None, 'rodzaj męski'), ('vendita', 'sprzedaż', None, 'rodzaj żeński'), ('valore', 'wartość', None, 'rodzaj męski'), ('credito', 'kredyt', None, 'rodzaj męski'), ('debito', 'dług', None, 'rodzaj męski'), ('tassa', 'podatek', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('ricchezza', 'bogactwo', None, 'rodzaj żeński'), ('povero', 'biedny', None, None), ('ricco', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('salute', 'zdrowie', None, 'rodzaj żeński'), ('malattia', 'choroba', None, 'rodzaj żeński'), ('dolore', 'ból', None, 'rodzaj męski'), ('febbre', 'gorączka', None, 'rodzaj żeński'), ('tosse', 'kaszel', None, 'rodzaj żeński'), ('raffreddore', 'katar', None, 'rodzaj męski'), ('medicina', 'lekarstwo', None, 'rodzaj żeński'), ('pastiglia', 'tabletka', None, 'rodzaj żeński'), ('operazione', 'operacja', None, 'rodzaj żeński'), ('ferita', 'rana', None, 'rodzaj żeński'), ('incidente', 'wypadek', None, 'rodzaj męski'), ('sano', 'zdrowy', None, None), ('malato', 'chory', None, None), ('stanco', 'zmęczony', None, None), ('assonnato', 'śpiący', None, None), ('forte', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('debole', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('gioia', 'radość', None, 'rodzaj żeński'), ('tristezza', 'smutek', None, 'rodzaj żeński'), ('paura', 'strach', None, 'rodzaj żeński'), ('rabbia', 'gniew', None, 'rodzaj żeński'), ('amore', 'miłość', None, 'rodzaj męski'), ('odio', 'nienawiść', None, 'rodzaj męski'), ('speranza', 'nadzieja', None, 'rodzaj żeński'), ('sogno', 'marzenie', None, 'rodzaj męski'), ('felicità', 'szczęście', None, 'rodzaj żeński'), ('vergogna', 'wstyd', None, 'rodzaj żeński'), ('sorpresa', 'zdziwienie', None, 'rodzaj żeński'), ('curiosità', 'ciekawość', None, 'rodzaj żeński'), ('pazienza', 'cierpliwość', None, 'rodzaj żeński'), ('coraggio', 'odwaga', None, 'rodzaj męski'), ('sincero', 'szczery', None, None), ('gentile', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('educato', 'grzeczny', None, None), ('stupido', 'głupi', None, None), ('intelligente', 'mądry', None, None), ('pigro', 'leniwy', None, None), ('lavoratore', 'pracowity', None, None), ('interessante', 'ciekawy', None, None), ('noioso', 'nudny', None, None), ('allegro', 'wesoły', None, None), ('triste', 'smutny', None, None), ('arrabbiato', 'zły (rozgniewany)', None, None), ('felice', 'szczęśliwy', None, None), ('innamorato', 'zakochany', None, None), ('solo', 'samotny', None, None), ('tranquillo', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('grande', 'duży', None, None), ('lungo', 'długi', None, None), ('corto', 'krótki', None, None), ('alto', 'wysoki', None, None), ('basso', 'niski', None, None), ('largo', 'szeroki', None, None), ('stretto', 'wąski', None, None), ('grasso', 'gruby', None, None), ('magro', 'chudy', None, None), ('pesante', 'ciężki', None, None), ('leggero', 'lekki', None, None), ('veloce', 'szybki', None, None), ('lento', 'wolny', None, None), ('duro', 'twardy', None, None), ('morbido', 'miękki', None, None), ('bagnato', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('asciutto', 'suchy', None, None), ('pulito', 'czysty', None, None), ('sporco', 'brudny', None, None), ('pieno', 'pełny', None, None), ('vuoto', 'pusty', None, None), ('affilato', 'ostry', None, None), ('rumoroso', 'głośny', None, None), ('silenzioso', 'cichy', None, None), ('chiaro', 'jasny', None, None), ('scuro', 'ciemny', None, None), ('giovane', 'młody', None, None), ('vecchio', 'stary', None, None), ('nuovo', 'nowy', None, None), ('cattivo', 'zły (niedobry)', None, None), ('bello', 'ładny', None, None), ('brutto', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('facile', 'łatwy', None, None), ('difficile', 'trudny', None, None), ('importante', 'ważny', None, None), ('possibile', 'możliwy', None, None), ('vero', 'prawdziwy', None, None), ('falso', 'fałszywy', None, None), ('caro', 'drogi', None, None), ('economico', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('essere', 'być', None, None), ('avere', 'mieć', None, None), ('fare', 'robić', None, None), ('andare', 'iść', None, None), ('guidare', 'jechać', None, None), ('venire', 'przyjść', None, None), ('uscire', 'wyjść', None, None), ('entrare', 'wejść', None, None), ('tornare', 'wrócić', None, None), ('correre', 'biec', None, None), ('stare in piedi', 'stać', None, None), ('stare seduto', 'siedzieć', None, None), ('stare sdraiato', 'leżeć', None, None), ('dormire', 'spać', None, None), ('alzarsi', 'wstać', None, None), ('mangiare', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('bere', 'pić', None, None), ('cucinare', 'gotować', None, None), ('lavare', 'myć', None, None), ('vestirsi', 'ubierać się', None, None), ('parlare', 'mówić', None, None), ('dire', 'powiedzieć', None, None), ('chiedere', 'pytać', None, None), ('rispondere', 'odpowiadać', None, None), ('sentire', 'słyszeć', None, None), ('ascoltare', 'słuchać', None, None), ('vedere', 'widzieć', None, None), ('guardare', 'patrzeć', None, None), ('leggere', 'czytać', None, None), ('scrivere', 'pisać', None, None), ('imparare', 'uczyć się', None, None), ('insegnare', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('capire', 'rozumieć', None, None), ('sapere', 'wiedzieć', None, None), ('conoscere', 'znać', None, None), ('pensare', 'myśleć', None, None), ('ricordare', 'pamiętać', None, None), ('dimenticare', 'zapominać', None, None), ('volere', 'chcieć', None, None), ('piacere', 'lubić', None, None), ('amare', 'kochać', None, None), ('aver bisogno', 'potrzebować', None, None), ('potere', 'móc', None, None), ('dovere', 'musieć', None, None), ('dare', 'dawać', None, None), ('prendere', 'brać', None, None), ('comprare', 'kupować', None, None), ('vendere', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('pagare', 'płacić', None, None), ('aprire', 'otwierać', None, None), ('chiudere', 'zamykać', None, None), ('cominciare', 'zaczynać', None, None), ('finire', 'kończyć', None, None), ('lavorare', 'pracować', None, None), ('giocare', 'grać', None, None), ('cantare', 'śpiewać', None, None), ('ballare', 'tańczyć', None, None), ('nuotare', 'pływać', None, None), ('volare', 'latać', None, None), ('mettere', 'kłaść', None, None), ('cercare', 'szukać', None, None), ('trovare', 'znajdować', None, None), ('aspettare', 'czekać', None, None), ('aiutare', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('pregare', 'prosić', None, None), ('scusarsi', 'przepraszać', None, None), ('permettere', 'pozwalać', None, None), ('provare', 'próbować', None, None), ('cambiare', 'zmieniać', None, None), ('portare', 'nosić', None, None), ('tenere', 'trzymać', None, None), ('lanciare', 'rzucać', None, None), ('afferrare', 'łapać', None, None), ('picchiare', 'bić', None, None), ('uccidere', 'zabijać', None, None), ('morire', 'umierać', None, None), ('vivere', 'żyć', None, None), ('abitare', 'mieszkać', None, None), ('incontrare', 'spotykać', None, None), ('telefonare', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('mandare', 'wysyłać', None, None), ('ricevere', 'dostawać', None, None), ('mostrare', 'pokazywać', None, None), ('invitare', 'zapraszać', None, None), ('visitare', 'odwiedzać', None, None), ('piangere', 'płakać', None, None), ('ridere', 'śmiać się', None, None), ('sorridere', 'uśmiechać się', None, None), ('temere', 'bać się', None, None), ('rallegrarsi', 'cieszyć się', None, None), ('credere', 'wierzyć', None, None), ("essere d'accordo", 'zgadzać się', None, None), ('scegliere', 'wybierać', None, None), ('decidere', 'decydować', None, None), ('contare', 'liczyć', None, None), ('pesare', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('camminare', 'chodzić', None, None), ('spostarsi', 'jeździć', None, None), ('salire', 'wsiadać', None, None), ('scendere', 'wysiadać', None, None), ('girare', 'skręcać', None, None), ('fermarsi', 'zatrzymywać się', None, None), ('essere in ritardo', 'spóźniać się', None, None), ('affrettarsi', 'spieszyć się', None, None), ('riposare', 'odpoczywać', None, None), ('divertirsi', 'bawić się', None, None), ('disegnare', 'rysować', None, None), ('costruire', 'budować', None, None), ('riparare', 'naprawiać', None, None), ('tagliare', 'ciąć', None, None), ('friggere', 'smażyć', None, None), ('infornare', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('mescolare', 'mieszać', None, None), ('versare', 'nalewać', None, None), ('pulire', 'sprzątać', None, None), ('fare il bucato', 'prać', None, None), ('stirare', 'prasować', None, None), ('radersi', 'golić się', None, None), ('pettinare', 'czesać', None, None), ('fare il bagno', 'kąpać się', None, None), ('svegliarsi', 'budzić się', None, None), ('addormentarsi', 'zasypiać', None, None), ('sognare a occhi aperti', 'marzyć', None, None), ('sognare', 'śnić', None, None), ('esercitarsi', 'ćwiczyć', None, None), ('allenarsi', 'trenować', None, None), ('vincere', 'wygrywać', None, None), ('perdere', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('muovere', 'ruszać', None, None), ('tirare', 'ciągnąć', None, None), ('spingere', 'pchać', None, None), ('sollevare', 'podnosić', None, None), ('cadere', 'spadać', None, None), ('saltare', 'skakać', None, None), ('arrampicarsi', 'wspinać się', None, None), ('nascondere', 'ukrywać', None, None), ('rubare', 'kraść', None, None), ('restituire', 'oddawać', None, None), ('prestare', 'pożyczać', None, None), ('spendere', 'wydawać', None, None), ('risparmiare', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('questo', 'ten', None, None), ('quello', 'tamten', None, None), ('dove', 'gdzie (pytanie)', None, None), ('come', 'jak', None, None), ('perché', 'dlaczego', None, None), ('che cosa', 'co', None, None), ('chi', 'kto', None, None), ('quale', 'który', None, None), ('che tipo di', 'jaki', None, None), ('quanti', 'ile (policzalne)', None, None), ('ma', 'ale', None, None), ('o', 'lub', None, None), ('perché (bo)', 'bo', None, None), ('se', 'jeśli', None, None), ('quindi', 'więc', None, None), ('anche', 'też', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [("un po'", 'trochę', None, None), ('tutto', 'wszystko', None, None), ('niente', 'nic', None, None), ('qualcosa', 'coś', None, None), ('qualcuno', 'ktoś', None, None), ('nessuno', 'nikt', None, None), ('ogni', 'każdy', None, None), ('altro', 'inny', None, None), ('lo stesso', 'ten sam', None, None), ('forse', 'może (być)', None, None), ('sicuramente', 'na pewno', None, None), ('insieme', 'razem', None, None), ('da solo', 'sam', None, None), ('senza', 'bez', None, None), ('con', 'z (towarzysząc)', None, None), ('in', 'w (miejsce)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('su', 'na (powierzchni)', None, None), ('verso', 'do (kierunek)', None, None), ('da', 'od', None, None), ('per', 'dla', None, None), ('attraverso', 'przez', None, None), ('dopo', 'po (czas)', None, None), ('prima di', 'przed', None, None), ('dietro', 'za (z tyłu)', None, None), ('sopra', 'nad', None, None), ('sotto', 'pod', None, None), ('accanto a', 'obok', None, None), ('tra', 'między', None, None), ('contro', 'przeciw', None, None), ('riguardo a', 'o (temat)', None, None), ('presso', 'u (przy)', None, None), ('circa', 'około', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('quasi', 'prawie', None, None), ('perfino', 'nawet', None, None), ('ancora una volta', 'jeszcze raz', None, None), ('allora', 'wtedy', None, None), ('da qualche parte', 'gdzieś', None, None), ('da nessuna parte', 'nigdzie', None, None), ('dappertutto', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('vita', 'życie', None, 'rodzaj żeński'), ('morte', 'śmierć', None, 'rodzaj żeński'), ('mondo', 'świat', None, 'rodzaj męski'), ('paese (kraj)', 'kraj', None, 'rodzaj męski'), ('stato', 'państwo', None, 'rodzaj męski'), ('lingua (mowa)', 'język (mowa)', None, 'rodzaj żeński'), ('parola', 'słowo', None, 'rodzaj żeński'), ('frase', 'zdanie', None, 'rodzaj żeński'), ('nome', 'imię', None, 'rodzaj męski'), ('cognome', 'nazwisko', None, 'rodzaj męski'), ('età', 'wiek', None, 'rodzaj żeński'), ('storia', 'historia', None, 'rodzaj żeński'), ('cultura', 'kultura', None, 'rodzaj żeński'), ('religione', 'religia', None, 'rodzaj żeński'), ('Dio', 'Bóg', None, 'rodzaj męski'), ('guerra', 'wojna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('pace', 'pokój (brak wojny)', None, 'rodzaj żeński'), ('legge', 'prawo (przepis)', None, 'rodzaj żeński'), ('libertà', 'wolność', None, 'rodzaj żeński'), ('governo', 'rząd', None, 'rodzaj męski'), ('elezioni', 'wybory', None, 'rodzaj żeński'), ('problema', 'problem', None, 'rodzaj męski'), ('idea', 'pomysł', None, 'rodzaj żeński'), ('motivo', 'powód', None, 'rodzaj męski'), ('risultato', 'wynik', None, 'rodzaj męski'), ('modo', 'sposób', None, 'rodzaj męski'), ('inizio', 'początek', None, 'rodzaj męski'), ('fine', 'koniec', None, 'rodzaj żeński'), ('parte', 'część', None, 'rodzaj żeński'), ('luogo', 'miejsce', None, 'rodzaj męski'), ('cosa', 'rzecz', None, 'rodzaj żeński'), ('questione', 'sprawa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('informazione', 'informacja', None, 'rodzaj żeński'), ('messaggio', 'wiadomość', None, 'rodzaj męski'), ('lettera', 'list', None, 'rodzaj żeński'), ('giornale', 'gazeta', None, 'rodzaj męski'), ('film', 'film', None, 'rodzaj męski'), ('musica', 'muzyka', None, 'rodzaj żeński'), ('canzone', 'piosenka', None, 'rodzaj żeński'), ('quadro', 'obraz', None, 'rodzaj męski'), ('gioco', 'gra', None, 'rodzaj męski'), ('sport', 'sport', None, 'rodzaj męski'), ('partita', 'mecz', None, 'rodzaj żeński'), ('squadra', 'drużyna', None, 'rodzaj żeński'), ('palla', 'piłka', None, 'rodzaj żeński'), ('divertimento', 'zabawa', None, 'rodzaj męski'), ('festa (impreza)', 'impreza', None, 'rodzaj żeński'), ('regalo', 'prezent', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('sogno (nocny)', 'sen', None, 'rodzaj męski'), ('piano', 'plan', None, 'rodzaj męski'), ('scelta', 'wybór', None, 'rodzaj żeński'), ('errore', 'błąd', None, 'rodzaj męski'), ('verità', 'prawda', None, 'rodzaj żeński'), ('bugia', 'kłamstwo', None, 'rodzaj żeński'), ('segreto', 'tajemnica', None, 'rodzaj męski'), ('forza', 'siła', None, 'rodzaj żeński'), ('energia', 'energia', None, 'rodzaj żeński'), ('luce', 'światło', None, 'rodzaj żeński'), ('suono', 'dźwięk', None, 'rodzaj męski'), ('silenzio', 'cisza', None, 'rodzaj męski'), ('movimento', 'ruch', None, 'rodzaj męski'), ('cambiamento', 'zmiana', None, 'rodzaj męski'), ('differenza', 'różnica', None, 'rodzaj żeński'), ('esempio', 'przykład', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('insieme (całość)', 'całość', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, 'rodzaj męski'), ('e-mail', 'e-mail', None, 'rodzaj żeński'), ('password', 'hasło', None, 'rodzaj żeński'), ('sito web', 'strona internetowa', None, 'rodzaj męski'), ('programma', 'program', None, 'rodzaj męski'), ('applicazione', 'aplikacja', None, 'rodzaj żeński'), ('schermo', 'ekran', None, 'rodzaj męski'), ('tastiera', 'klawiatura', None, 'rodzaj żeński'), ('mouse', 'myszka komputerowa', None, 'rodzaj męski'), ('file', 'plik', None, 'rodzaj męski'), ('foto', 'zdjęcie', None, 'rodzaj żeński'), ('telecamera', 'kamera', None, 'rodzaj żeński'), ('batteria', 'bateria', None, 'rodzaj żeński'), ('corrente', 'prąd', None, 'rodzaj żeński'), ('cavo', 'kabel', None, 'rodzaj męski'), ('macchina (urządzenie)', 'maszyna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('attrezzo', 'narzędzie', None, 'rodzaj męski'), ('martello', 'młotek', None, 'rodzaj męski'), ('stampante', 'drukarka', None, 'rodzaj żeński'), ('caricabatterie', 'ładowarka', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('nord', 'północ', None, 'rodzaj męski'), ('sud', 'południe (kierunek)', None, 'rodzaj męski'), ('est', 'wschód', None, 'rodzaj męski'), ('ovest', 'zachód', None, 'rodzaj męski'), ('Europa', 'Europa', None, 'rodzaj żeński'), ('Germania', 'Niemcy', None, 'rodzaj żeński'), ('Francia', 'Francja', None, 'rodzaj żeński'), ('Spagna', 'Hiszpania', None, 'rodzaj żeński'), ('Russia', 'Rosja', None, 'rodzaj żeński'), ('Inghilterra', 'Anglia', None, 'rodzaj żeński'), ('America', 'Ameryka', None, 'rodzaj żeński'), ('Cina', 'Chiny', None, 'rodzaj żeński'), ('Giappone', 'Japonia', None, 'rodzaj męski'), ('Africa', 'Afryka', None, 'rodzaj żeński'), ('Asia', 'Azja', None, 'rodzaj żeński'), ('continente', 'kontynent', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('capitale', 'stolica', None, 'rodzaj żeński'), ('cittadino', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('pezzo', 'kawałek', None, 'rodzaj męski'), ('goccia', 'kropla', None, 'rodzaj żeński'), ('scatola', 'pudełko', None, 'rodzaj żeński'), ('sacco', 'worek', None, 'rodzaj męski'), ('filo', 'nić', None, 'rodzaj męski'), ('filo di ferro', 'drut', None, 'rodzaj męski'), ('ago', 'igła', None, 'rodzaj męski'), ('forbici', 'nożyczki', None, 'rodzaj żeński'), ('bastone', 'kij', None, 'rodzaj męski'), ('corda', 'lina', None, 'rodzaj żeński'), ('catena', 'łańcuch', None, 'rodzaj żeński'), ('vite', 'śruba', None, 'rodzaj żeński'), ('chiodo', 'gwóźdź', None, 'rodzaj męski'), ('colla', 'klej', None, 'rodzaj żeński'), ('vernice', 'farba', None, 'rodzaj żeński'), ('vetro', 'szkło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('legno', 'drewno', None, 'rodzaj męski'), ('metallo', 'metal', None, 'rodzaj męski'), ('oro', 'złoto', None, 'rodzaj męski'), ('argento', 'srebro', None, 'rodzaj męski'), ('ferro', 'żelazo', None, 'rodzaj męski'), ('plastica', 'plastik', None, 'rodzaj żeński'), ('cuoio', 'skóra (materiał)', None, 'rodzaj męski'), ('cotone', 'bawełna', None, 'rodzaj męski'), ('lana', 'wełna', None, 'rodzaj żeński'), ('sabbia', 'piasek', None, 'rodzaj żeński'), ('fango', 'błoto', None, 'rodzaj męski'), ('polvere', 'kurz', None, 'rodzaj żeński'), ('fumo', 'dym', None, 'rodzaj męski'), ('vapore', 'para (wodna)', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('giù', 'dół', None, None), ('davanti', 'przód', None, None), ('dietro (tył)', 'tył', None, None), ('mezzo', 'środek', None, 'rodzaj męski'), ('lato', 'bok', None, 'rodzaj męski'), ('dentro', 'wewnątrz', None, None), ('fuori', 'na zewnątrz', None, None), ('lontano', 'daleko', None, None), ('vicino (blisko)', 'blisko', None, None), ('in alto', 'wysoko', None, None), ('in basso', 'nisko', None, None), ('velocemente', 'szybko', None, None), ('lentamente', 'wolno', None, None), ('bene', 'dobrze', None, None), ('male', 'źle', None, None), ('facilmente', 'łatwo', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('difficilmente', 'trudno', None, None), ('separatamente', 'osobno', None, None), ('di fronte', 'naprzeciw', None, None), ('di traverso', 'w poprzek', None, None), ('intorno', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('cavolo', 'kapusta', None, 'rodzaj męski'), ('pisello', 'groszek', None, 'rodzaj męski'), ('fagiolo', 'fasola', None, 'rodzaj męski'), ('fungo', 'grzyb', None, 'rodzaj męski'), ('noce', 'orzech', None, 'rodzaj żeński'), ('prugna', 'śliwka', None, 'rodzaj żeński'), ('ciliegia', 'wiśnia', None, 'rodzaj żeński'), ('pesca', 'brzoskwinia', None, 'rodzaj żeński'), ('anguria', 'arbuz', None, 'rodzaj żeński'), ('lampone', 'malina', None, 'rodzaj męski'), ('salsiccia', 'kiełbasa', None, 'rodzaj żeński'), ('prosciutto', 'szynka', None, 'rodzaj męski'), ('panino', 'bułka', None, 'rodzaj męski'), ('tramezzino', 'kanapka', None, 'rodzaj męski'), ('crespella', 'naleśnik', None, 'rodzaj żeński'), ('yogurt', 'jogurt', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('panna', 'śmietana', None, 'rodzaj żeński'), ('salsa', 'sos', None, 'rodzaj żeński'), ('aceto', 'ocet', None, 'rodzaj męski'), ('lievito', 'drożdże', None, 'rodzaj męski'), ('gelatina di frutta', 'kisiel', None, 'rodzaj żeński'), ('gelatina', 'galaretka', None, 'rodzaj żeński'), ('uvetta', 'rodzynek', None, 'rodzaj żeński'), ('mandorla', 'migdał', None, 'rodzaj żeński'), ('prezzemolo', 'pietruszka', None, 'rodzaj męski'), ('aneto', 'koperek', None, 'rodzaj męski'), ('peperone', 'papryka', None, 'rodzaj męski'), ('lattuga', 'sałata', None, 'rodzaj żeński'), ('spinaci', 'szpinak', None, 'rodzaj męski'), ('barbabietola', 'burak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('suocero', 'teść', None, 'rodzaj męski'), ('suocera', 'teściowa', None, 'rodzaj żeński'), ('cognato', 'szwagier', None, 'rodzaj męski'), ('nipote (bratanek)', 'bratanek', None, 'rodzaj męski'), ('nipote (siostrzenica)', 'siostrzenica', None, 'rodzaj żeński'), ('orfano', 'sierota', None, 'rodzaj męski'), ('vedova', 'wdowa', None, 'rodzaj żeński'), ('fidanzato', 'narzeczony', None, 'rodzaj męski'), ('matrimonio', 'ślub', None, 'rodzaj męski'), ('divorzio', 'rozwód', None, 'rodzaj męski'), ('nascita', 'urodzenie', None, 'rodzaj żeński'), ('funerale', 'pogrzeb', None, 'rodzaj męski'), ('parrucchiere', 'fryzjer', None, 'rodzaj męski'), ('panettiere', 'piekarz', None, 'rodzaj męski'), ('macellaio', 'rzeźnik', None, 'rodzaj męski'), ('cameriera', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('postino', 'listonosz', None, 'rodzaj męski'), ('pompiere', 'strażak', None, 'rodzaj męski'), ('giudice', 'sędzia', None, 'rodzaj męski'), ('direttore', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
