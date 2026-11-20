"""Treść kursu: francuski dla Polaków.

Słowo:    (forma, znaczenie, polskie słowo pokrewne lub None, skojarzenie lub None, wymowa polskimi literami)
Wymowa: ü = francuskie u (usta jak do „u”, mów „i”), ö = francuskie eu, ń po samogłosce = nosowe (jak w „bon”).
"""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "PRONONCIATION · WYMOWA", "jezyk": "LANGUE · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "É", "track": "wymowa",
     "letters": [
         ("ou", "[u]: jak polskie u", "nous (my)"),
         ("oi", "[wa]: jak polskie ła", "moi (ja)"),
         ("eu, œu", "[ø]: usta jak do „o”, mów „e”", "deux (dwa)"),
         ("ch", "[ʃ]: jak polskie sz", "chat (kot)"),
         ("gn", "[ɲ]: jak polskie ń", "montagne (góra)"),
         ("ç", "[s]: jak polskie s", "français (francuski)"),
         ("an, en", "[ɑ̃]: nosowe, jak „an” w „bądź”", "enfant (dziecko)"),
         ("on", "[ɔ̃]: nosowe, jak „oń”", "bon (dobry)"),
         ("in, ain", "[ɛ̃]: nosowe, jak „eń”", "pain (chleb)"),
         ("é", "[e]: jak polskie e, zamknięte", "été (lato)"),
         ("u", "[y]: usta jak do „u”, mów „i”", "tu (ty)"),
         ("au, eau", "[o]: jak polskie o", "eau (woda)"),
         ("j, ge", "[ʒ]: jak polskie ż", "jour (dzień)"),
         ("h", "nie czytasz go wcale", "homme (mężczyzna)"),
         ("-s, -t, -d, -x", "na końcu słowa zwykle milczą", "petit (mały)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "B", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("bonjour", "dzień dobry", None, "Dosłownie „dobry dzień”."),
         ("bonsoir", "dobry wieczór", None, None),
         ("bonne", "dobra (przed nuit)", None, "Nuit jest żeńskie, więc bonne."),
         ("nuit", "noc", None, None),
         ("salut", "cześć", None, "Od łacińskiego salus: zdrowie. Jak polskie „salut”."),
         ("merci", "dziękuję", None, None),
         ("s'il", "jeśli (to) (część „s'il vous plaît”)", None, None),
         ("vous", "wy; pan, pani", None, None),
         ("plaît", "podoba się (część „s'il vous plaît”)", None, None),
         ("oui", "tak", None, None),
         ("non", "nie", None, None),
         ("beaucoup", "bardzo; dużo", None, None),
         ("pardon", "przepraszam", "pardon", None),
         ("au", "do; w (au revoir)", None, None),
         ("revoir", "zobaczyć znów (au revoir = do widzenia)", None, None),
     ],
     "sentences": [
         (["salut", "!"], "Cześć!", {"bonjour": "bonjour to „dzień dobry”. Wśród znajomych: salut."}),
         (["bonjour", "!"], "Dzień dobry!", {"bonsoir": "bonsoir to „dobry wieczór”."}),
         (["bonsoir", "!"], "Dobry wieczór!", {"bonjour": "bonjour to „dzień dobry”."}),
         (["bonne", "nuit", "!"], "Dobranoc!", {"bon": "Nuit jest żeńskie: bonne."}),
         (["merci", "beaucoup"], "Dziękuję bardzo.", {}),
         (["s'il", "vous", "plaît"], "Proszę.", {"merci": "merci to „dziękuję”."}),
         (["oui", ",", "merci"], "Tak, dziękuję.", {"non": "non to „nie”."}),
         (["non", ",", "merci"], "Nie, dziękuję.", {"oui": "oui to „tak”."}),
         (["au", "revoir", "!"], "Do widzenia!", {}),
         (["pardon", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "J", "track": "jezyk",
     "words": [
         ("je", "ja", None, None),
         ("tu", "ty", None, None),
         ("il", "on", None, None),
         ("elle", "ona", None, None),
         ("suis", "jestem", None, "Je suis czytasz „że süi”."),
         ("es", "jesteś", None, None),
         ("est", "jest", None, "Brzmi tak samo jak „es”: [e]."),
         ("polonais", "Polak; polski", None, None),
         ("polonaise", "Polka; polska", None, None),
         ("étudiant", "student", None, None),
         ("professeur", "nauczyciel; profesor", "profesor", None),
         ("de", "z; od", None, None),
         ("Pologne", "Polska", None, None),
         ("France", "Francja", None, None),
     ],
     "sentences": [
         (["je", "suis", "étudiant"], "Jestem studentem.", {"es": "es to „jesteś”. O sobie: suis."}),
         (["tu", "es", "professeur"], "Jesteś nauczycielem.", {"suis": "suis to „jestem”. Do „tu”: es."}),
         (["il", "est", "polonais"], "On jest Polakiem.", {"polonaise": "Dla mężczyzny: polonais."}),
         (["elle", "est", "polonaise"], "Ona jest Polką.", {"polonais": "Dla kobiety: polonaise."}),
         (["je", "suis", "de", "Pologne"], "Jestem z Polski.", {"France": "France to Francja."}),
         (["elle", "est", "de", "France"], "Ona jest z Francji.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "L", "track": "jezyk",
     "words": [
         ("le", "(rodzajnik męski)", None, "Le père, le frère."),
         ("la", "(rodzajnik żeński)", None, "La mère, la sœur."),
         ("un", "jakiś; jeden (męski)", None, None),
         ("une", "jakaś; jedna (żeński)", None, None),
         ("mère", "matka", None, None),
         ("père", "ojciec", None, None),
         ("l'enfant", "dziecko", None, "Przed samogłoską le/la skracają się do l'."),
         ("ami", "przyjaciel", None, None),
         ("femme", "kobieta; żona", None, None),
         ("homme", "mężczyzna", None, "H nie czytamy: [om]."),
         ("frère", "brat", None, None),
         ("sœur", "siostra", None, None),
         ("j'ai", "mam", None, "Je + ai: skrócone do j'ai."),
         ("as", "masz", None, None),
         ("petit", "mały", None, None),
         ("bon", "dobry", None, None),
     ],
     "sentences": [
         (["le", "frère", "est", "petit"], "Brat jest mały.", {"la": "frère jest męski: le."}),
         (["la", "mère", "est", "une", "femme"], "Matka jest kobietą.", {"le": "mère jest żeńska: la."}),
         (["l'enfant", "est", "petit"], "Dziecko jest małe.", {}),
         (["j'ai", "un", "frère"], "Mam brata.", {"as": "as to „masz”. O sobie: j'ai.", "une": "frère jest męski: un."}),
         (["tu", "as", "une", "sœur"], "Masz siostrę.", {"j'ai": "j'ai to „mam”. Do „tu”: as.", "un": "sœur jest żeńska: une."}),
         (["le", "père", "est", "un", "homme"], "Ojciec jest mężczyzną.", {}),
         (["l'enfant", "est", "bon"], "Dziecko jest dobre.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "K", "track": "jezyk",
     "words": [
         ("eau", "woda", None, "Eau czytasz [o]."),
         ("café", "kawa; kawiarnia", None, "Stąd „kafejka”."),
         ("thé", "herbata", None, None),
         ("pain", "chleb", None, None),
         ("fromage", "ser", None, None),
         ("vin", "wino", None, None),
         ("lait", "mleko", None, None),
         ("poisson", "ryba", None, None),
         ("pomme", "jabłko", None, None),
         ("pommes", "jabłka", None, "Mnoga: dodajesz -s, ale go nie czytasz."),
         ("voudrais", "chciałbym; chciałabym", None, "Grzeczne „chcę”."),
         ("très", "bardzo", None, None),
         ("maintenant", "teraz", None, None),
     ],
     "sentences": [
         (["je", "voudrais", "un", "café"], "Poproszę kawę.", {"une": "café jest męski: un."}),
         (["je", "voudrais", "un", "thé", ",", "s'il", "vous", "plaît"], "Poproszę herbatę.", {}),
         (["tu", "voudrais", "une", "pomme"], "Chciałbyś jabłko.", {"un": "pomme jest żeńskie: une."}),
         (["je", "voudrais", "un", "pain"], "Poproszę chleb.", {}),
         (["le", "poisson", "est", "très", "bon"], "Ryba jest bardzo dobra.", {}),
         (["je", "voudrais", "une", "eau", "maintenant"], "Chcę teraz wodę.", {}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("deux", "dwa", "duet", None),
         ("trois", "trzy", "trio", None),
         ("quatre", "cztery", None, None),
         ("cinq", "pięć", None, None),
         ("dix", "dziesięć", "dekada (z greki)", None),
         ("enfants", "dzieci", None, None),
         ("aujourd'hui", "dziś", None, None),
         ("demain", "jutro", None, None),
         ("hier", "wczoraj", None, None),
         ("heure", "godzina", None, "H nie czytamy: [ör]."),
         ("heures", "godziny (po liczbie)", None, None),
         ("quelle", "jaka", None, None),
         ("est-il", "czy jest on (pytanie)", None, "Odwracasz szyk: il est → est-il."),
     ],
     "sentences": [
         (["j'ai", "deux", "enfants"], "Mam dwoje dzieci.", {}),
         (["je", "voudrais", "trois", "pommes"], "Chcę trzy jabłka.", {"deux": "deux to „dwa”. Chcesz trzy: trois."}),
         (["quelle", "heure", "est-il", "?"], "Która jest godzina?", {}),
         (["il", "est", "dix", "heures"], "Jest dziesiąta.", {}),
         (["aujourd'hui", "je", "voudrais", "un", "café"], "Dziś chcę kawę.", {"demain": "demain to „jutro”. Tu „dziś”."}),
         (["demain", "je", "voudrais", "un", "poisson"], "Jutro chcę rybę.", {"hier": "hier to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "V", "track": "jezyk",
     "words": [
         ("maison", "dom", None, None),
         ("ville", "miasto", None, None),
         ("rue", "ulica", None, None),
         ("l'école", "szkoła", None, None),
         ("mer", "morze", None, None),
         ("taxi", "taksówka", "taksówka", None),
         ("l'hôtel", "hotel", "hotel", None),
         ("où", "gdzie", None, None),
         ("ici", "tu", None, None),
         ("là", "tam", None, None),
         ("vais", "idę; jadę", None, None),
         ("à", "do; w", None, None),
         ("Paris", "Paryż", None, None),
         ("droite", "prawa; w prawo (à droite)", None, None),
         ("gauche", "lewa; w lewo (à gauche)", None, "Gauche to także „lewicowy” (lewica w polityce)."),
     ],
     "sentences": [
         (["où", "est", "l'hôtel", "?"], "Gdzie jest hotel?", {"ici": "ici to „tu”, a pytasz „gdzie”: où."}),
         (["l'hôtel", "est", "là"], "Hotel jest tam.", {"ici": "ici to „tu”. Tu mówimy „tam”: là."}),
         (["je", "vais", "à", "la", "maison"], "Idę do domu.", {"le": "maison jest żeńskie: la."}),
         (["je", "vais", "à", "Paris"], "Jadę do Paryża.", {}),
         (["le", "taxi", "est", "à", "droite"], "Taksówka jest po prawej.", {"gauche": "gauche to „lewa”."}),
         (["l'école", "est", "là"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Pisze się więcej, niż się czyta", "chain": [],
                "text": "Po francusku na końcu słowa zwykle nie czytasz spółgłosek: petit to [pəti], vous to [vu]. Kilka grup liter warto znać: é czytasz [e], ou [u], oi [wa]. Reszty nauczysz się z przykładów."}],
    "ja": [{"title": "Je suis, tu es, il est", "chain": [
                ("Jestem studentem.", ["je", "suis", "étudiant"], "Do „je” pasuje suis."),
                ("Jesteś nauczycielem.", ["tu", "es", "professeur"], "Do „tu” pasuje es."),
            ],
            "text": "Zaimek jest obowiązkowy: je suis, tu es, il est. Es i est brzmią tak samo ([e]), więc słuchaj kontekstu."}],
    "ludzie": [{"title": "Le, la, l'", "chain": [],
                "text": "Rzeczowniki są męskie (le, un) lub żeńskie (la, une). Przed samogłoską le i la zlewają się w l': l'enfant, l'ami. Uczysz się słowa razem z rodzajnikiem."}],
    "jedzenie": [{"title": "Grzecznie: je voudrais", "chain": [],
                  "text": "Zamiast „je veux” (chcę) w sklepie mówi się grzecznie „je voudrais” (chciałbym). Do tego „s'il vous plaît” i masz poprawne zamówienie."}],
}

ENDINGS_INSIGHT = {"title": "Rodzajniki i formy czasowników",
                   "text": "Po francusku ćwiczysz rodzaj (le/la, un/une) i formy czasownika (suis, es, est). Tu to robisz."}

ENDINGS = [
    ("", "bon", "jour", "", ["jour", "soir", "nuit"], "dzień dobry", "jour to „dzień”, soir „wieczór”, nuit „noc”.", "slowa"),
    ("", "bon", "soir", "", ["jour", "soir", "nuit"], "dobry wieczór", "soir to „wieczór”.", "slowa"),
    ("", "bonne ", "nuit", "", ["jour", "soir", "nuit"], "dobranoc", "nuit to „noc” (żeńskie, więc bonne).", "slowa"),
    ("je ", "", "suis", " étudiant", ["suis", "es", "est"], "ja jestem", "Do „je” pasuje suis.", "ja"),
    ("tu ", "", "es", " professeur", ["suis", "es", "est"], "ty jesteś", "Do „tu” pasuje es.", "ja"),
    ("il ", "", "est", " polonais", ["suis", "es", "est"], "on jest", "Do „il” pasuje est.", "ja"),
    ("", "", "le", " père", ["le", "la"], "ten ojciec", "père jest męski: le.", "ludzie"),
    ("", "", "la", " mère", ["le", "la"], "ta matka", "mère jest żeńska: la.", "ludzie"),
    ("j'ai ", "", "un", " frère", ["un", "une"], "jakiś brat", "frère jest męski: un.", "ludzie"),
    ("tu as ", "", "une", " sœur", ["un", "une"], "jakaś siostra", "sœur jest żeńska: une.", "ludzie"),
    ("je voudrais ", "", "un", " café", ["un", "une"], "jakaś kawa (męski)", "café jest męski: un.", "jedzenie"),
    ("je voudrais ", "", "une", " pomme", ["un", "une"], "jakieś jabłko (żeński)", "pomme jest żeńskie: une.", "jedzenie"),
    ("je voudrais ", "", "un", " pain", ["un", "une"], "jakiś chleb (męski)", "pain jest męski: un.", "jedzenie"),
    ("je vais ", "", "à", " Paris", ["à", "de"], "do Paryża", "à to „do, w”, de to „z”.", "miejsca"),
    ("je suis ", "", "de", " Pologne", ["à", "de"], "z Polski", "de to „z”.", "miejsca"),
]

CHAT_EXTRA = {"Marie": "Marie (imię)", "Luc": "Luc (imię)", "monsieur": "pan", "quoi": "co", "veux": "chcesz (tu veux)",
              "allez": "idziecie; jedziecie", "où": "gdzie", "et": "i", "bien": "dobrze"}

CHATS = [
    {"id": "cafe", "title": "W kawiarni", "partner": "Marie", "avatar": "M", "requires": "jedzenie",
     "turns": [
         {"bot": ["bonjour", "!"], "en": "Dzień dobry!",
          "options": [(["bonjour", "!"], True, None), (["bonne", "nuit", "!"], False, "bonne nuit to „dobranoc”. Jest dzień.")]},
         {"bot": ["un", "café", "?"], "en": "Kawę?",
          "options": [(["oui", ",", "je", "voudrais", "un", "café"], True, None),
                      (["oui", ",", "je", "voudrais", "une", "café"], False, "café jest męski: un, nie une.")]},
         {"bot": ["et", "un", "pain", "?"], "en": "I chleb?",
          "options": [(["non", ",", "merci"], True, None),
                      (["s'il", "vous", "plaît"], False, "s'il vous plaît to „proszę”. Odmów: non, merci.")]},
         {"bot": ["très", "bien", "!"], "build": (["merci", "beaucoup"], "Dziękuję bardzo."), "en": "Bardzo dobrze!"},
     ]},
    {"id": "rencontre", "title": "Poznajemy się", "partner": "Luc", "avatar": "L", "requires": "ludzie",
     "turns": [
         {"bot": ["salut", "!"], "en": "Cześć!",
          "options": [(["salut", "!"], True, None), (["pardon", "!"], False, "pardon to „przepraszam”. Powitaj: salut.")]},
         {"bot": ["tu", "es", "de", "France", "?"], "en": "Jesteś z Francji?",
          "options": [(["non", ",", "je", "suis", "de", "Pologne"], True, None),
                      (["non", ",", "je", "es", "de", "Pologne"], False, "es jest do „tu”. O sobie: suis.")]},
         {"bot": ["tu", "as", "un", "frère", "?"], "en": "Masz brata?",
          "options": [(["oui", ",", "j'ai", "un", "frère"], True, None),
                      (["oui", ",", "j'ai", "une", "frère"], False, "frère jest męski: un.")]},
         {"bot": ["bonsoir", "!"], "build": (["bonsoir"], "Dobry wieczór."), "en": "Dobry wieczór!"},
     ]},
    {"id": "taxi", "title": "W taksówce", "partner": "monsieur", "avatar": "T", "requires": "miejsca",
     "turns": [
         {"bot": ["bonsoir", "!"], "en": "Dobry wieczór!",
          "options": [(["bonsoir", "!"], True, None), (["bonjour", "!"], False, "bonjour to „dzień dobry”. Jest wieczór.")]},
         {"bot": ["où", "allez", "?"], "en": "Dokąd jedziecie?",
          "options": [(["je", "vais", "à", "Paris"], True, None),
                      (["je", "suis", "à", "Paris"], False, "suis to „jestem”. Jedziesz: je vais.")]},
         {"bot": ["l'hôtel", "est", "là", "."], "en": "Hotel jest tam.",
          "options": [(["à", "droite", "?"], True, None), (["ici", "?"], False, "Pytasz o kierunek: à droite (w prawo).")]},
         {"bot": ["oui", "!"], "build": (["merci", "beaucoup"], "Dziękuję bardzo."), "en": "Tak!"},
     ]},
]

# === BULK: generowane z langs/bulk/french.txt (nie edytuj ręcznie) ===
UNITS += [{'id': 'f01', 'title': "Wzór: Je voudrais … i J'ai …", 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['je', 'voudrais', 'un', 'fromage', '.'], 'Poproszę ser.', {}), (['je', 'voudrais', 'une', 'pomme', '.'], 'Poproszę jabłko.', {}), (['je', 'voudrais', 'un', 'poisson', '.'], 'Poproszę rybę.', {}), (['je', 'voudrais', 'deux', 'pommes', '.'], 'Poproszę dwa jabłka.', {}), (['je', 'voudrais', 'un', 'vin', '.'], 'Poproszę wino.', {}), (['je', 'voudrais', 'un', 'lait', '.'], 'Poproszę mleko.', {}), (["j'ai", 'une', 'sœur', '.'], 'Mam siostrę.', {}), (["j'ai", 'un', 'ami', '.'], 'Mam przyjaciela.', {}), (["j'ai", 'une', 'maison', '.'], 'Mam dom.', {}), (["j'ai", 'trois', 'pommes', '.'], 'Mam trzy jabłka.', {}), (["j'ai", 'cinq', 'pommes', '.'], 'Mam pięć jabłek.', {})]}, {'id': 'f02', 'title': 'Wzór: Où est …? i Je vais à …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['où', 'est', "l'école", '?'], 'Gdzie jest szkoła?', {}), (['où', 'est', 'la', 'maison', '?'], 'Gdzie jest dom?', {}), (['où', 'est', 'la', 'rue', '?'], 'Gdzie jest ulica?', {}), (['où', 'est', 'la', 'ville', '?'], 'Gdzie jest miasto?', {}), (['où', 'est', 'le', 'taxi', '?'], 'Gdzie jest taksówka?', {}), (['où', 'est', 'la', 'mer', '?'], 'Gdzie jest morze?', {}), (['où', 'est', 'Paris', '?'], 'Gdzie jest Paryż?', {}), (['je', 'vais', 'à', "l'école", '.'], 'Idę do szkoły.', {}), (['je', 'vais', 'à', 'la', 'mer', '.'], 'Idę do morza.', {}), (['je', 'vais', 'à', 'Paris', '.'], 'Idę do Paryża.', {}), (['je', 'vais', 'à', "l'hôtel", '.'], 'Idę do hotelu.', {}), (['je', 'vais', 'à', 'la', 'ville', '.'], 'Idę do miasta.', {}), (["aujourd'hui", 'je', 'vais', 'à', 'la', 'maison', '.'], 'Dziś idę do domu.', {}), (['demain', 'je', 'vais', 'à', 'Paris', '.'], 'Jutro idę do Paryża.', {}), (['maintenant', 'je', 'vais', 'à', "l'école", '.'], 'Teraz idę do szkoły.', {}), (["aujourd'hui", 'je', 'vais', 'à', 'la', 'mer', '.'], 'Dziś idę do morza.', {})]}, {'id': 'f03', 'title': 'Wzór: Je suis … Tu es … Il est …', 'icon': 'W', 'track': 'jezyk', 'words': [], 'sentences': [(['je', 'suis', 'polonais', '.'], 'Ja jestem Polakiem.', {}), (['tu', 'es', 'étudiant', '.'], 'Ty jesteś studentem.', {}), (['il', 'est', 'professeur', '.'], 'On jest nauczycielem.', {}), (['je', 'suis', 'étudiant', '.'], 'Ja jestem studentem.', {}), (['tu', 'es', 'polonais', '.'], 'Ty jesteś Polakiem.', {})]}]
INSIGHTS.setdefault('f01', []).append({'title': "Wzór: Je voudrais … i J'ai …", 'text': "Ten sam szkielet, inne komponenty: Je voudrais + to, co chcesz zamówić. J'ai + to, co masz. Rodzajnik: un (męski), une (żeński).\n\nPrzykład: Je voudrais un fromage. = Poproszę ser.", 'chain': []})
INSIGHTS.setdefault('f02', []).append({'title': 'Wzór: Où est …? i Je vais à …', 'text': "Pytanie o miejsce: Où est + rzeczownik ? Kierunek: Je vais à + miejsce. Zmieniasz tylko miejsce.\n\nPrzykład: Où est l'école? = Gdzie jest szkoła?", 'chain': []})
INSIGHTS.setdefault('f03', []).append({'title': 'Wzór: Je suis … Tu es … Il est …', 'text': 'Kto jest kim: osoba + être + zawód lub narodowość. Je suis (ja), tu es (ty), il est (on), elle est (ona).\n\nPrzykład: Je suis polonais. = Ja jestem Polakiem.', 'chain': []})
# === /BULK ===

# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['je', 'tu', 'il/elle', 'nous', 'vous', 'ils/elles'],
    'rodz': ['męski lp.', 'żeński lp.', 'męski lm.', 'żeński lm.'],
    'dzier': ['przed rzecz. męskim', 'przed rzecz. żeńskim', 'przed liczbą mnogą'],
    'pp': ['parler', 'finir', 'vendre', 'être', 'avoir', 'faire', 'prendre', 'venir', 'voir', 'pouvoir'],
    'ppres': ['parler', 'finir', 'vendre', 'être', 'avoir', 'faire'],
    'rozk': ['tu', 'nous', 'vous'],
    't_aux': ['aller', 'manger', 'venir', 'voir', 'partir', 'faire', 'rester', 'prendre'],
    't_rodz': ['problème (problem)', 'maison (dom)', 'livre (książka)', 'voiture (samochód)', 'musée (muzeum)', 'mer (morze)', 'soleil (słońce)', 'lune (księżyc)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'parler (mówić)', 'os', 'parle; parles; parle; parlons; parlez; parlent', 'Grupa -er: -e, -es, -e, -ons, -ez, -ent. Końcówek -e, -es, -ent nie słychać.'),
    ('conj', 'Wzory koniugacji', 'aimer (lubić, kochać)', 'os', 'aime; aimes; aime; aimons; aimez; aiment', None),
    ('conj', 'Wzory koniugacji', 'finir (kończyć)', 'os', 'finis; finis; finit; finissons; finissez; finissent', 'Grupa -ir: w liczbie mnogiej pojawia się -iss-.'),
    ('conj', 'Wzory koniugacji', 'vendre (sprzedawać)', 'os', 'vends; vends; vend; vendons; vendez; vendent', 'Grupa -re: w 3. osobie lp. brak końcówki.'),
    ('conj', 'Wyjątki', 'manger (jeść)', 'os', 'mange; manges; mange; mangeons; mangez; mangent', 'Przed -ons zostaje e, żeby g brzmiało miękko: mangeons.'),
    ('conj', 'Czasowniki nieregularne', 'être (być)', 'os', 'suis; es; est; sommes; êtes; sont', None),
    ('conj', 'Czasowniki nieregularne', 'avoir (mieć)', 'os', 'ai; as; a; avons; avez; ont', None),
    ('conj', 'Czasowniki nieregularne', 'aller (iść)', 'os', 'vais; vas; va; allons; allez; vont', None),
    ('conj', 'Czasowniki nieregularne', 'faire (robić)', 'os', 'fais; fais; fait; faisons; faites; font', None),
    ('conj', 'Czasowniki nieregularne', 'vouloir (chcieć)', 'os', 'veux; veux; veut; voulons; voulez; veulent', None),
    ('conj', 'Czasowniki nieregularne', 'pouvoir (móc)', 'os', 'peux; peux; peut; pouvons; pouvez; peuvent', None),
    ('conj', 'Czasowniki nieregularne', 'venir (przychodzić)', 'os', 'viens; viens; vient; venons; venez; viennent', None),
    ('conj', 'Czasowniki nieregularne', 'prendre (brać)', 'os', 'prends; prends; prend; prenons; prenez; prennent', None),
    ('decl', 'Przymiotniki: rodzaj i liczba', 'petit (mały)', 'rodz', 'petit; petite; petits; petites', 'Żeński: +e. Mnoga: +s.'),
    ('decl', 'Przymiotniki: rodzaj i liczba', 'grand (duży)', 'rodz', 'grand; grande; grands; grandes', None),
    ('decl', 'Wyjątki', 'beau (piękny)', 'rodz', 'beau; belle; beaux; belles', None),
    ('decl', 'Wyjątki', 'bon (dobry)', 'rodz', 'bon; bonne; bons; bonnes', 'Podwojenie spółgłoski w rodzaju żeńskim.'),
    ('decl', 'Zaimki dzierżawcze', 'mon (mój)', 'dzier', 'mon; ma; mes', None),
    ('decl', 'Zaimki dzierżawcze', 'ton (twój)', 'dzier', 'ton; ta; tes', None),
    ('decl', 'Zaimki dzierżawcze', 'son (jego, jej)', 'dzier', 'son; sa; ses', None),
    ('form', 'Imiesłowy', 'Participe passé', 'pp', 'parlé; fini; vendu; été; eu; fait; pris; venu; vu; pu', '-er → -é, -ir → -i, -re → -u. Częste czasowniki mają formy nieregularne.'),
    ('form', 'Imiesłowy', 'Participe présent', 'ppres', 'parlant; finissant; vendant; étant; ayant; faisant', 'Temat od nous + -ant.'),
    ('conj', 'Czas przeszły', 'parler: passé composé', 'os', 'ai parlé; as parlé; a parlé; avons parlé; avez parlé; ont parlé', 'avoir w czasie teraźniejszym + participe passé.'),
    ('conj', 'Czas przeszły', 'aller: passé composé', 'os', 'suis allé; es allé; est allé; sommes allés; êtes allés; sont allés', 'Czasowniki ruchu łączą się z être, a participe zgadza się z podmiotem (allé, allée, allés, allées).'),
    ('conj', 'Czas przeszły', 'parler: imparfait', 'os', 'parlais; parlais; parlait; parlions; parliez; parlaient', None),
    ('conj', 'Czas przeszły', 'être: imparfait', 'os', 'étais; étais; était; étions; étiez; étaient', None),
    ('conj', 'Czas przyszły', 'parler: futur simple', 'os', 'parlerai; parleras; parlera; parlerons; parlerez; parleront', 'Bezokolicznik + końcówki avoir: -ai, -as, -a, -ons, -ez, -ont.'),
    ('conj', 'Czas przyszły', 'être: futur simple', 'os', 'serai; seras; sera; serons; serez; seront', None),
    ('conj', 'Czas przyszły', 'avoir: futur simple', 'os', 'aurai; auras; aura; aurons; aurez; auront', None),
    ('conj', 'Czas przyszły', 'parler: futur proche', 'os', 'vais parler; vas parler; va parler; allons parler; allez parler; vont parler', 'aller + bezokolicznik.'),
    ('conj', 'Czasowniki zwrotne', 'se laver (myć się)', 'os', 'me lave; te laves; se lave; nous lavons; vous lavez; se lavent', None),
    ('form', 'Tryb rozkazujący', 'parler', 'rozk', 'parle; parlons; parlez', 'W 2. osobie lp. czasowniki na -er tracą -s.'),
    ('form', 'Tryb rozkazujący', 'être', 'rozk', 'sois; soyons; soyez', None),
    ('form', 'Tryb rozkazujący', 'avoir', 'rozk', 'aie; ayons; ayez', None),
    ('form', 'Typowe trudności', 'Passé composé: être czy avoir?', 't_aux', 'être; avoir; être; avoir; être; avoir; être; avoir', 'Z être łączą się czasowniki ruchu i zmiany stanu oraz wszystkie zwrotne.'),
    ('form', 'Typowe trudności', 'Rodzaj: le czy la?', 't_rodz', 'le; la; le; la; le; la; le; la', 'Rzeczowniki na -age, -ment, -eau są zwykle męskie; na -tion, -té, -ure żeńskie.'),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ["penser ___ quelqu'un (myśleć o kimś)", 'parler ___ quelque chose (mówić o czymś)', 'jouer ___ un jeu (grać w grę)', 'avoir besoin ___ (potrzebować)', "téléphoner ___ quelqu'un (dzwonić do)", "s'occuper ___ (zajmować się)"],
    't_m1': ['Je bois ___ café.', 'Je mange ___ salade.', "J'aime ___ café. (lubię w ogóle)", "J'achète ___ pommes.", 'Je ne bois pas ___ café.', 'Je bois ___ eau.'],
    't_m2': ['tu', 'tout', 'rue', 'roue', 'vu', 'vous', 'dessus', 'dessous'],
    't_m3': ['je parle, tu parles, il parle, ils parlent', 'nous parlons', 'vous parlez', 'il est, tu es', 'ils sont, ils ont', 'a, à'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Czasownik + przyimek: à czy de?', 't_m0', 'à; de; à; de; à; de', 'Przyimka nie tłumaczy się z polskiego: trzeba go znać razem z czasownikiem.'),
    ('form', 'Typowe trudności', 'Rodzajnik: du, de la, des, le czy de?', 't_m1', "du; de la; le; des; de; de l'", 'Nieokreślona ilość: du, de la, des. Po przeczeniu samo de. Po aimer rodzajnik określony.'),
    ('form', 'Typowe trudności', 'u czy ou: co to znaczy?', 't_m2', 'ty; wszystko; ulica; koło; widziany; wy; na wierzchu; pod spodem', 'u [y] i ou [u] to dwa różne dźwięki.'),
    ('form', 'Typowe trudności', 'Czyta się tak samo? Liczba form w mowie', 't_m3', 'jedna wymowa; inna; inna; jedna wymowa; różne (s i z); jedna wymowa', 'Końcówek -e, -es, -ent się nie czyta. Ils sont [s] i ils ont [z] różni tylko łączenie.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['Widzę go.', 'Nie mówię po francusku.', 'Daję mu książkę.', 'Chcę to zjeść.'],
    't_s1': ['To duży dom.', 'To czerwony samochód.', 'To dobry film.', 'Mam francuską książkę.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: zaimki i przeczenie', 't_s0', 'Je le vois.|Je vois le.|Le je vois.|Je vois lui.; Je ne parle pas français.|Je parle ne pas français.|Je ne pas parle français.|Je parle pas ne français.; Je lui donne le livre.|Je donne lui le livre.|Je lui le livre donne.|Je donne le livre lui.; Je veux le manger.|Je le veux manger.|Je veux manger le.|Je veux manger lui.', 'Zaimek dopełnienia stoi przed czasownikiem, do którego się odnosi. Przeczenie ne … pas otacza odmieniony czasownik.'),
    ('form', 'Szyk zdania', 'Szyk: przymiotnik przed czy po?', 't_s1', "C'est une grande maison.|C'est une maison grande.|C'est grande une maison.|C'est maison une grande.; C'est une voiture rouge.|C'est une rouge voiture.|C'est rouge une voiture.|C'est voiture une rouge.; C'est un bon film.|C'est un film bon.|C'est bon un film.|C'est film un bon.; J'ai un livre français.|J'ai un français livre.|J'ai français un livre.|J'ai livre un français.", 'Krótkie, częste przymiotniki (grand, petit, bon, beau, nouveau) stoją przed rzeczownikiem. Kolory i narodowości po nim.'),
]

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'me, te, le… (dopełnienie bliższe)', 'os', 'me; te; le, la; nous; vous; les', 'Stoją przed czasownikiem: je le vois.'),
    ('decl', 'Zaimki', 'me, te, lui… (dopełnienie dalsze)', 'os', 'me; te; lui; nous; vous; leur', None),
    ('decl', 'Zaimki', 'moi, toi… (zaimki akcentowane)', 'os', 'moi; toi; lui, elle; nous; vous; eux, elles', "Po przyimku i do podkreślenia: avec moi, c'est toi."),
    ('decl', 'Zaimki', 'me, te, se… (zwrotne)', 'os', 'me; te; se; nous; vous; se', None),
    ('decl', 'Zaimki', 'notre (nasz)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'liczba mnoga'], 'notre; notre; nos', None),
    ('decl', 'Zaimki', 'votre (wasz)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'liczba mnoga'], 'votre; votre; vos', None),
    ('decl', 'Zaimki', 'leur (ich)', ['rodzaj męski lp.', 'rodzaj żeński lp.', 'liczba mnoga'], 'leur; leur; leurs', None),
    ('decl', 'Zaimki', 'ce (ten)', ['rodzaj męski lp.', 'rodzaj męski przed samogłoską', 'rodzaj żeński lp.', 'liczba mnoga'], 'ce; cet; cette; ces', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'mauvais (zły)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'mauvais; pire; le pire', 'Obok też plus mauvais.'),
    ('form', 'Stopniowanie', 'bien (dobrze)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'bien; mieux; le mieux', 'Przysłówek: nieregularny.'),
    ('form', 'Stopniowanie', 'rapide (szybki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'rapide; plus rapide; le plus rapide', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 1 (generowane) ===
PARADIGMS += [
    ('conj', 'Tryb warunkowy', 'parler: conditionnel', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'parlerais; parlerais; parlerait; parlerions; parleriez; parleraient', None),
    ('conj', 'Tryb warunkowy', 'être: conditionnel', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'serais; serais; serait; serions; seriez; seraient', None),
    ('conj', 'Tryb warunkowy', 'avoir: conditionnel', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'aurais; aurais; aurait; aurions; auriez; auraient', None),
    ('conj', 'Tryb warunkowy', 'aller: conditionnel', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'irais; irais; irait; irions; iriez; iraient', None),
    ('conj', 'Tryb warunkowy', 'faire: conditionnel', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'ferais; ferais; ferait; ferions; feriez; feraient', None),
    ('conj', 'Tryb warunkowy', 'pouvoir: conditionnel', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'pourrais; pourrais; pourrait; pourrions; pourriez; pourraient', None),
    ('conj', 'Tryb warunkowy', 'vouloir: conditionnel', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'voudrais; voudrais; voudrait; voudrions; voudriez; voudraient', 'Grzeczna prośba: je voudrais un café.'),
    ('conj', 'Tryb łączący', 'parler: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'parle; parles; parle; parlions; parliez; parlent', None),
    ('conj', 'Tryb łączący', 'être: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'sois; sois; soit; soyons; soyez; soient', 'Po „il faut que”, „je veux que”: Il faut que tu viennes.'),
    ('conj', 'Tryb łączący', 'avoir: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'aie; aies; ait; ayons; ayez; aient', None),
    ('conj', 'Tryb łączący', 'aller: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'aille; ailles; aille; allions; alliez; aillent', None),
    ('conj', 'Tryb łączący', 'faire: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'fasse; fasses; fasse; fassions; fassiez; fassent', None),
    ('conj', 'Tryb łączący', 'pouvoir: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'puisse; puisses; puisse; puissions; puissiez; puissent', None),
    ('conj', 'Tryb łączący', 'vouloir: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'veuille; veuilles; veuille; voulions; vouliez; veuillent', None),
    ('conj', 'Tryb łączący', 'finir: subjonctif', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'finisse; finisses; finisse; finissions; finissiez; finissent', None),
    ('conj', 'Czas przyszły', 'aller: futur simple', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'irai; iras; ira; irons; irez; iront', None),
    ('conj', 'Czas przyszły', 'faire: futur simple', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'ferai; feras; fera; ferons; ferez; feront', None),
    ('conj', 'Czas przyszły', 'pouvoir: futur simple', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'pourrai; pourras; pourra; pourrons; pourrez; pourront', None),
    ('conj', 'Czas przyszły', 'vouloir: futur simple', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'voudrai; voudras; voudra; voudrons; voudrez; voudront', None),
    ('conj', 'Czas przyszły', 'venir: futur simple', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'viendrai; viendras; viendra; viendrons; viendrez; viendront', None),
    ('conj', 'Czas przyszły', 'voir: futur simple', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'verrai; verras; verra; verrons; verrez; verront', None),
    ('conj', 'Czas przeszły', 'avoir: imparfait', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'avais; avais; avait; avions; aviez; avaient', None),
    ('conj', 'Czas przeszły', 'faire: imparfait', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'faisais; faisais; faisait; faisions; faisiez; faisaient', None),
    ('conj', 'Czas przeszły', 'aller: imparfait', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'allais; allais; allait; allions; alliez; allaient', None),
    ('conj', 'Czas przeszły', 'finir: imparfait', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'finissais; finissais; finissait; finissions; finissiez; finissaient', None),
    ('conj', 'Czas przeszły', 'finir: passé composé', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'ai fini; as fini; a fini; avons fini; avez fini; ont fini', None),
    ('conj', 'Czas przeszły', 'venir: passé composé', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'suis venu; es venu; est venu; sommes venus; êtes venus; sont venus', None),
    ('conj', 'Czas przeszły', 'se lever: passé composé', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], "me suis levé; t'es levé; s'est levé; nous sommes levés; vous êtes levés; se sont levés", None),
    ('conj', 'Czas przeszły', 'faire: passé composé', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'ai fait; as fait; a fait; avons fait; avez fait; ont fait', None),
    ('conj', 'Czasowniki nieregularne', 'devoir (musieć)', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'dois; dois; doit; devons; devez; doivent', None),
    ('conj', 'Czasowniki nieregularne', 'savoir (wiedzieć)', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'sais; sais; sait; savons; savez; savent', None),
    ('conj', 'Czasowniki nieregularne', 'dire (mówić)', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'dis; dis; dit; disons; dites; disent', None),
    ('conj', 'Czasowniki nieregularne', 'voir (widzieć)', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'vois; vois; voit; voyons; voyez; voient', None),
    ('conj', 'Wyjątki', 'appeler (nazywać): podwojone l', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'appelle; appelles; appelle; appelons; appelez; appellent', 'Zmiany pisowni w temacie: forma „nous” i „vous” często zachowuje formę z bezokolicznika.'),
    ('conj', 'Wyjątki', 'acheter (kupować): è', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'achète; achètes; achète; achetons; achetez; achètent', 'Zmiany pisowni w temacie: forma „nous” i „vous” często zachowuje formę z bezokolicznika.'),
    ('conj', 'Wyjątki', 'commencer (zaczynać): ç', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'commence; commences; commence; commençons; commencez; commencent', 'Zmiany pisowni w temacie: forma „nous” i „vous” często zachowuje formę z bezokolicznika.'),
    ('conj', 'Wyjątki', 'payer (płacić): y → i', ['je', 'tu', 'il / elle', 'nous', 'vous', 'ils / elles'], 'paie; paies; paie; payons; payez; paient', 'Zmiany pisowni w temacie: forma „nous” i „vous” często zachowuje formę z bezokolicznika.'),
    ('form', 'Rodzajniki', 'rodzajnik określony', ['rodzaj męski', 'rodzaj żeński', 'przed samogłoską', 'liczba mnoga'], "le; la; l'; les", None),
    ('form', 'Rodzajniki', 'rodzajnik nieokreślony', ['rodzaj męski', 'rodzaj żeński', 'liczba mnoga'], 'un; une; des', None),
    ('form', 'Rodzajniki', 'rodzajnik cząstkowy (część, trochę)', ['rodzaj męski', 'rodzaj żeński', 'przed samogłoską', 'liczba mnoga'], "du; de la; de l'; des", 'W przeczeniu: pas de café.'),
    ('form', 'Rodzajniki', 'à + rodzajnik', ['rodzaj męski', 'rodzaj żeński', 'przed samogłoską', 'liczba mnoga'], "au; à la; à l'; aux", None),
    ('form', 'Rodzajniki', 'de + rodzajnik', ['rodzaj męski', 'rodzaj żeński', 'przed samogłoską', 'liczba mnoga'], "du; de la; de l'; des", None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 1 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('enfant', 'dziecko', None, 'rodzaj męski'), ('garçon', 'chłopiec', None, 'rodzaj męski'), ('fille', 'dziewczynka', None, 'rodzaj żeński'), ('être humain', 'człowiek', None, 'rodzaj męski'), ('gens', 'ludzie', None, 'rodzaj męski'), ('famille', 'rodzina', None, 'rodzaj żeński'), ('fils', 'syn', None, 'rodzaj męski'), ('fille (córka)', 'córka', None, 'rodzaj żeński'), ('grand-père', 'dziadek', None, 'rodzaj męski'), ('grand-mère', 'babcia', None, 'rodzaj żeński'), ('petit-fils', 'wnuk', None, 'rodzaj męski'), ('oncle', 'wujek', None, 'rodzaj męski'), ('tante', 'ciocia', None, 'rodzaj żeński'), ('cousin', 'kuzyn', None, 'rodzaj męski'), ('mari', 'mąż', None, 'rodzaj męski'), ('épouse', 'żona', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('voisin', 'sąsiad', None, 'rodzaj męski'), ('invité', 'gość', None, 'rodzaj męski'), ('chef', 'szef', None, 'rodzaj męski'), ('collègue', 'kolega', None, 'rodzaj męski'), ('ennemi', 'wróg', None, 'rodzaj męski'), ('roi', 'król', None, 'rodzaj męski'), ('reine', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('tête', 'głowa', None, 'rodzaj żeński'), ('visage', 'twarz', None, 'rodzaj męski'), ('œil', 'oko', None, 'rodzaj męski'), ('oreille', 'ucho', None, 'rodzaj żeński'), ('nez', 'nos', None, 'rodzaj męski'), ('bouche', 'usta', None, 'rodzaj żeński'), ('dent', 'ząb', None, 'rodzaj żeński'), ('langue', 'język (narząd)', None, 'rodzaj żeński'), ('cheveux', 'włosy', None, 'rodzaj męski'), ('cou', 'szyja', None, 'rodzaj męski'), ('bras', 'ramię', None, 'rodzaj męski'), ('main', 'ręka', None, 'rodzaj żeński'), ('doigt', 'palec', None, 'rodzaj męski'), ('jambe', 'noga', None, 'rodzaj żeński'), ('pied', 'stopa', None, 'rodzaj męski'), ('genou', 'kolano', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('dos', 'plecy', None, 'rodzaj męski'), ('ventre', 'brzuch', None, 'rodzaj męski'), ('cœur', 'serce', None, 'rodzaj męski'), ('sang', 'krew', None, 'rodzaj męski'), ('os', 'kość', None, 'rodzaj męski'), ('peau', 'skóra', None, 'rodzaj żeński'), ('voix', 'głos', None, 'rodzaj żeński'), ('corps', 'ciało', None, 'rodzaj męski'), ('estomac', 'żołądek', None, 'rodzaj męski'), ('barbe', 'broda', None, 'rodzaj żeński'), ('lèvre', 'warga', None, 'rodzaj żeński'), ('ongle', 'paznokieć', None, 'rodzaj męski'), ('poitrine', 'pierś', None, 'rodzaj żeński'), ('cerveau', 'mózg', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('beurre', 'masło', None, 'rodzaj męski'), ('œuf', 'jajko', None, 'rodzaj męski'), ('viande', 'mięso', None, 'rodzaj żeński'), ('poulet', 'kurczak', None, 'rodzaj męski'), ('porc', 'wieprzowina', None, 'rodzaj męski'), ('soupe', 'zupa', None, 'rodzaj żeński'), ('salade', 'sałatka', None, 'rodzaj żeński'), ('riz', 'ryż', None, 'rodzaj męski'), ('pâtes', 'makaron', None, 'rodzaj żeński'), ('pomme de terre', 'ziemniak', None, 'rodzaj żeński'), ('carotte', 'marchewka', None, 'rodzaj żeński'), ('oignon', 'cebula', None, 'rodzaj męski'), ('ail', 'czosnek', None, 'rodzaj męski'), ('tomate', 'pomidor', None, 'rodzaj żeński'), ('concombre', 'ogórek', None, 'rodzaj męski'), ('poire', 'gruszka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('banane', 'banan', None, 'rodzaj żeński'), ('orange', 'pomarańcza', None, 'rodzaj żeński'), ('citron', 'cytryna', None, 'rodzaj męski'), ('fraise', 'truskawka', None, 'rodzaj żeński'), ('raisin', 'winogrono', None, 'rodzaj męski'), ('sucre', 'cukier', None, 'rodzaj męski'), ('sel', 'sól', None, 'rodzaj męski'), ('poivre', 'pieprz', None, 'rodzaj męski'), ('huile', 'olej', None, 'rodzaj żeński'), ('farine', 'mąka', None, 'rodzaj żeński'), ('miel', 'miód', None, 'rodzaj męski'), ('chocolat', 'czekolada', None, 'rodzaj męski'), ('glace', 'lody', None, 'rodzaj żeński'), ('gâteau', 'ciasto (tort)', None, 'rodzaj męski'), ('biscuit', 'ciastko', None, 'rodzaj męski'), ('petit-déjeuner', 'śniadanie', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('déjeuner', 'obiad', None, 'rodzaj męski'), ('dîner', 'kolacja', None, 'rodzaj męski'), ('en-cas', 'przekąska', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('jus', 'sok', None, 'rodzaj męski'), ('bière', 'piwo', None, 'rodzaj żeński'), ('boisson', 'napój', None, 'rodzaj żeński'), ('verre', 'szklanka', None, 'rodzaj męski'), ('tasse', 'filiżanka', None, 'rodzaj żeński'), ('assiette', 'talerz', None, 'rodzaj żeński'), ('couteau', 'nóż', None, 'rodzaj męski'), ('fourchette', 'widelec', None, 'rodzaj żeński'), ('cuillère', 'łyżka', None, 'rodzaj żeński'), ('bouteille', 'butelka', None, 'rodzaj żeński'), ('carte', 'menu', None, 'rodzaj żeński'), ('addition', 'rachunek', None, 'rodzaj żeński'), ('pourboire', 'napiwek', None, 'rodzaj męski'), ('table', 'stolik', None, 'rodzaj żeński'), ('serveur', 'kelner', None, 'rodzaj męski'), ('cuisinier', 'kucharz', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('affamé', 'głodny', None, None), ('assoiffé', 'spragniony', None, None), ('délicieux', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('appartement', 'mieszkanie', None, 'rodzaj męski'), ('chambre', 'pokój', None, 'rodzaj żeński'), ('cuisine', 'kuchnia', None, 'rodzaj żeński'), ('salle de bain', 'łazienka', None, 'rodzaj żeński'), ('chambre à coucher', 'sypialnia', None, 'rodzaj żeński'), ('salon', 'salon', None, 'rodzaj męski'), ('jardin', 'ogród', None, 'rodzaj męski'), ('porte', 'drzwi', None, 'rodzaj żeński'), ('fenêtre', 'okno', None, 'rodzaj żeński'), ('mur', 'ściana', None, 'rodzaj męski'), ('sol', 'podłoga', None, 'rodzaj męski'), ('toit', 'dach', None, 'rodzaj męski'), ('escalier', 'schody', None, 'rodzaj męski'), ('clé', 'klucz', None, 'rodzaj żeński'), ('table (stół)', 'stół', None, 'rodzaj żeński'), ('chaise', 'krzesło', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('lit', 'łóżko', None, 'rodzaj męski'), ('armoire', 'szafa', None, 'rodzaj żeński'), ('lampe', 'lampa', None, 'rodzaj żeński'), ('tapis', 'dywan', None, 'rodzaj męski'), ('miroir', 'lustro', None, 'rodzaj męski'), ('télévision', 'telewizor', None, 'rodzaj żeński'), ('téléphone', 'telefon', None, 'rodzaj męski'), ('ordinateur', 'komputer', None, 'rodzaj męski'), ('horloge', 'zegar', None, 'rodzaj żeński'), ('oreiller', 'poduszka', None, 'rodzaj męski'), ('couverture', 'koc', None, 'rodzaj żeński'), ('serviette', 'ręcznik', None, 'rodzaj żeński'), ('savon', 'mydło', None, 'rodzaj męski'), ('brosse à dents', 'szczoteczka do zębów', None, 'rodzaj żeński'), ('réfrigérateur', 'lodówka', None, 'rodzaj męski'), ('four', 'piec', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('machine à laver', 'pralka', None, 'rodzaj żeński'), ('ordures', 'śmieci', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('vêtement', 'ubranie', None, 'rodzaj męski'), ('chemise', 'koszula', None, 'rodzaj żeński'), ('pantalon', 'spodnie', None, 'rodzaj męski'), ('robe', 'sukienka', None, 'rodzaj żeński'), ('jupe', 'spódnica', None, 'rodzaj żeński'), ('veste', 'kurtka', None, 'rodzaj żeński'), ('manteau', 'płaszcz', None, 'rodzaj męski'), ('pull', 'sweter', None, 'rodzaj męski'), ('chaussure', 'buty', None, 'rodzaj żeński'), ('chaussette', 'skarpetki', None, 'rodzaj żeński'), ('bonnet', 'czapka', None, 'rodzaj męski'), ('chapeau', 'kapelusz', None, 'rodzaj męski'), ('gant', 'rękawiczki', None, 'rodzaj męski'), ('écharpe', 'szalik', None, 'rodzaj żeński'), ('sac', 'torba', None, 'rodzaj męski'), ('sac à dos', 'plecak', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('portefeuille', 'portfel', None, 'rodzaj męski'), ('lunettes', 'okulary', None, 'rodzaj żeński'), ('montre', 'zegarek', None, 'rodzaj żeński'), ('bague', 'pierścionek', None, 'rodzaj żeński'), ('sous-vêtements', 'bielizna', None, 'rodzaj męski'), ('pyjama', 'piżama', None, 'rodzaj męski'), ('ceinture', 'pasek', None, 'rodzaj żeński'), ('cravate', 'krawat', None, 'rodzaj żeński'), ('costume', 'garnitur', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('rouge', 'czerwony', None, None), ('bleu', 'niebieski', None, None), ('vert', 'zielony', None, None), ('jaune', 'żółty', None, None), ('noir', 'czarny', None, None), ('blanc', 'biały', None, None), ('gris', 'szary', None, None), ('marron', 'brązowy', None, None), ('rose', 'różowy', None, None), ('violet', 'fioletowy', None, None), ('couleur', 'kolor', None, 'rodzaj żeński'), ('rond', 'okrągły', None, None), ('carré', 'kwadratowy', None, None), ('droit', 'prosty', None, None), ('tordu', 'krzywy', None, None), ('ligne', 'linia', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('point', 'punkt', None, 'rodzaj męski'), ('cercle', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('zéro', 'zero', None, None), ('onze', 'jedenaście', None, None), ('douze', 'dwanaście', None, None), ('treize', 'trzynaście', None, None), ('quatorze', 'czternaście', None, None), ('quinze', 'piętnaście', None, None), ('seize', 'szesnaście', None, None), ('dix-sept', 'siedemnaście', None, None), ('dix-huit', 'osiemnaście', None, None), ('dix-neuf', 'dziewiętnaście', None, None), ('vingt', 'dwadzieścia', None, None), ('trente', 'trzydzieści', None, None), ('quarante', 'czterdzieści', None, None), ('cinquante', 'pięćdziesiąt', None, None), ('soixante', 'sześćdziesiąt', None, None), ('soixante-dix', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('quatre-vingts', 'osiemdziesiąt', None, None), ('quatre-vingt-dix', 'dziewięćdziesiąt', None, None), ('cent', 'sto', None, None), ('mille', 'tysiąc', None, None), ('million', 'milion', None, 'rodzaj męski'), ('premier', 'pierwszy', None, None), ('deuxième', 'drugi', None, None), ('troisième', 'trzeci', None, None), ('moitié', 'połowa', None, 'rodzaj żeński'), ('paire', 'para', None, 'rodzaj żeński'), ('quelques', 'kilka', None, None), ('peu', 'mało', None, None), ('entier', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('seconde', 'sekunda', None, 'rodzaj żeński'), ('minute', 'minuta', None, 'rodzaj żeński'), ('jour', 'dzień', None, 'rodzaj męski'), ('semaine', 'tydzień', None, 'rodzaj żeński'), ('mois', 'miesiąc', None, 'rodzaj męski'), ('an', 'rok', None, 'rodzaj męski'), ('printemps', 'wiosna', None, 'rodzaj męski'), ('été', 'lato', None, 'rodzaj męski'), ('automne', 'jesień', None, 'rodzaj męski'), ('hiver', 'zima', None, 'rodzaj męski'), ('lundi', 'poniedziałek', None, 'rodzaj męski'), ('mardi', 'wtorek', None, 'rodzaj męski'), ('mercredi', 'środa', None, 'rodzaj męski'), ('jeudi', 'czwartek', None, 'rodzaj męski'), ('vendredi', 'piątek', None, 'rodzaj męski'), ('samedi', 'sobota', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('dimanche', 'niedziela', None, 'rodzaj męski'), ('janvier', 'styczeń', None, 'rodzaj męski'), ('février', 'luty', None, 'rodzaj męski'), ('mars', 'marzec', None, 'rodzaj męski'), ('avril', 'kwiecień', None, 'rodzaj męski'), ('mai', 'maj', None, 'rodzaj męski'), ('juin', 'czerwiec', None, 'rodzaj męski'), ('juillet', 'lipiec', None, 'rodzaj męski'), ('août', 'sierpień', None, 'rodzaj męski'), ('septembre', 'wrzesień', None, 'rodzaj męski'), ('octobre', 'październik', None, 'rodzaj męski'), ('novembre', 'listopad', None, 'rodzaj męski'), ('décembre', 'grudzień', None, 'rodzaj męski'), ('matin', 'rano (pora dnia)', None, 'rodzaj męski'), ('midi', 'południe', None, 'rodzaj męski'), ('le soir', 'wieczorem', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('toujours', 'zawsze', None, None), ('jamais', 'nigdy', None, None), ('parfois', 'czasem', None, None), ('souvent', 'często', None, None), ('déjà', 'już', None, None), ('encore', 'jeszcze', None, None), ('bientôt', 'wkrótce', None, None), ('plus tard', 'później', None, None), ('tôt', 'wcześnie', None, None), ('tard', 'późno', None, None), ('quand', 'kiedy (pytanie)', None, None), ('date', 'data', None, 'rodzaj żeński'), ('passé', 'przeszłość', None, 'rodzaj męski'), ('avenir', 'przyszłość', None, 'rodzaj męski'), ('anniversaire', 'urodziny', None, 'rodzaj męski'), ('fête', 'święto', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('vacances', 'wakacje', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('soleil', 'słońce', None, 'rodzaj męski'), ('lune', 'księżyc', None, 'rodzaj żeński'), ('étoile', 'gwiazda', None, 'rodzaj żeński'), ('ciel', 'niebo', None, 'rodzaj męski'), ('nuage', 'chmura', None, 'rodzaj męski'), ('pluie', 'deszcz', None, 'rodzaj żeński'), ('neige', 'śnieg', None, 'rodzaj żeński'), ('vent', 'wiatr', None, 'rodzaj męski'), ('orage', 'burza', None, 'rodzaj męski'), ('brouillard', 'mgła', None, 'rodzaj męski'), ('glace (lód)', 'lód', None, 'rodzaj żeński'), ('feu', 'ogień', None, None), ('terre', 'grunt)', None, 'rodzaj żeński'), ('rivière', 'rzeka', None, 'rodzaj żeński'), ('lac', 'jezioro', None, 'rodzaj męski'), ('montagne', 'góra', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('forêt', 'las', None, 'rodzaj żeński'), ('arbre', 'drzewo', None, 'rodzaj męski'), ('fleur', 'kwiat', None, 'rodzaj żeński'), ('herbe', 'trawa', None, 'rodzaj żeński'), ('feuille', 'liść', None, 'rodzaj żeński'), ('champ', 'pole', None, 'rodzaj męski'), ('île', 'wyspa', None, 'rodzaj żeński'), ('plage', 'plaża', None, 'rodzaj żeński'), ('désert', 'pustynia', None, 'rodzaj męski'), ('roche', 'skała', None, 'rodzaj żeński'), ('pierre', 'kamień', None, 'rodzaj żeński'), ('temps', 'pogoda', None, 'rodzaj męski'), ('température', 'temperatura', None, 'rodzaj żeński'), ('froid', 'zimny', None, None), ('chaud', 'ciepły', None, None), ('brûlant', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('chien', 'pies', None, 'rodzaj męski'), ('chat', 'kot', None, 'rodzaj męski'), ('cheval', 'koń', None, 'rodzaj męski'), ('vache', 'krowa', None, 'rodzaj żeński'), ('cochon', 'świnia', None, 'rodzaj męski'), ('mouton', 'owca', None, 'rodzaj męski'), ('chèvre', 'koza', None, 'rodzaj żeński'), ('poule', 'kura', None, 'rodzaj żeński'), ('canard', 'kaczka', None, 'rodzaj męski'), ('oiseau', 'ptak', None, 'rodzaj męski'), ('souris', 'mysz', None, 'rodzaj żeński'), ('rat', 'szczur', None, 'rodzaj męski'), ('serpent', 'wąż', None, 'rodzaj męski'), ('grenouille', 'żaba', None, 'rodzaj żeński'), ('lion', 'lew', None, 'rodzaj męski'), ('tigre', 'tygrys', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('éléphant', 'słoń', None, 'rodzaj męski'), ('ours', 'niedźwiedź', None, 'rodzaj męski'), ('loup', 'wilk', None, 'rodzaj męski'), ('renard', 'lis', None, 'rodzaj męski'), ('lièvre', 'zając', None, 'rodzaj męski'), ('cerf', 'jeleń', None, 'rodzaj męski'), ('singe', 'małpa', None, 'rodzaj męski'), ('papillon', 'motyl', None, 'rodzaj męski'), ('abeille', 'pszczoła', None, 'rodzaj żeński'), ('mouche', 'mucha', None, 'rodzaj żeński'), ('araignée', 'pająk', None, 'rodzaj żeński'), ('animal', 'zwierzę', None, 'rodzaj męski'), ('insecte', 'owad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('village', 'wieś', None, 'rodzaj męski'), ('route', 'droga', None, 'rodzaj żeński'), ('place', 'plac', None, 'rodzaj żeński'), ('pont', 'most', None, 'rodzaj męski'), ('parc', 'park', None, 'rodzaj męski'), ('magasin', 'sklep', None, 'rodzaj męski'), ('marché', 'targ', None, 'rodzaj męski'), ('supermarché', 'supermarket', None, 'rodzaj męski'), ('banque', 'bank', None, 'rodzaj żeński'), ('poste', 'poczta', None, 'rodzaj żeński'), ('hôpital', 'szpital', None, 'rodzaj męski'), ('pharmacie', 'apteka', None, 'rodzaj żeński'), ('université', 'uniwersytet', None, 'rodzaj żeński'), ('bibliothèque', 'biblioteka', None, 'rodzaj żeński'), ('musée', 'muzeum', None, 'rodzaj męski'), ('église', 'kościół', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('restaurant', 'restauracja', None, 'rodzaj męski'), ('café (lokal)', 'kawiarnia', None, 'rodzaj męski'), ('aéroport', 'lotnisko', None, 'rodzaj męski'), ('gare', 'dworzec', None, 'rodzaj żeński'), ('arrêt', 'przystanek', None, 'rodzaj męski'), ('cinéma', 'kino', None, 'rodzaj męski'), ('théâtre', 'teatr', None, 'rodzaj męski'), ('police', 'policja', None, 'rodzaj żeński'), ('bureau', 'biuro', None, 'rodzaj męski'), ('usine', 'fabryka', None, 'rodzaj żeński'), ('bâtiment', 'budynek', None, 'rodzaj męski'), ('tour', 'wieża', None, 'rodzaj żeński'), ('centre', 'centrum', None, 'rodzaj męski'), ('adresse', 'adres', None, 'rodzaj żeński'), ('carte (mapa)', 'mapa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('voiture', 'samochód', None, 'rodzaj żeński'), ('autobus', 'autobus', None, 'rodzaj męski'), ('train', 'pociąg', None, 'rodzaj męski'), ('tramway', 'tramwaj', None, 'rodzaj męski'), ('métro', 'metro', None, 'rodzaj męski'), ('avion', 'samolot', None, 'rodzaj męski'), ('bateau', 'statek', None, 'rodzaj męski'), ('vélo', 'rower', None, 'rodzaj męski'), ('moto', 'motocykl', None, 'rodzaj żeński'), ('billet', 'bilet', None, 'rodzaj męski'), ('voyage', 'podróż', None, 'rodzaj męski'), ('excursion', 'wycieczka', None, 'rodzaj żeński'), ('passeport', 'paszport', None, 'rodzaj męski'), ('valise', 'walizka', None, 'rodzaj żeński'), ('essence', 'benzyna', None, 'rodzaj żeński'), ('parking', 'parking', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('carrefour', 'skrzyżowanie', None, 'rodzaj męski'), ('feu rouge', 'światła', None, 'rodzaj męski'), ('permis de conduire', 'prawo jazdy', None, 'rodzaj męski'), ('conducteur', 'kierowca', None, 'rodzaj męski'), ('passager', 'pasażer', None, 'rodzaj męski'), ('entrée', 'wjazd', None, 'rodzaj żeński'), ('sortie', 'wyjazd', None, 'rodzaj żeński'), ('chemin de fer', 'kolej', None, 'rodzaj męski'), ('port', 'port', None, 'rodzaj męski'), ('frontière', 'granica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('travail', 'praca', None, 'rodzaj męski'), ('profession', 'zawód', None, 'rodzaj żeński'), ('médecin', 'lekarz', None, 'rodzaj męski'), ('infirmière', 'pielęgniarka', None, 'rodzaj żeński'), ('enseignant', 'nauczyciel', None, 'rodzaj męski'), ('élève', 'uczeń', None, 'rodzaj męski'), ('étudiant (student)', 'student', None, 'rodzaj męski'), ('ingénieur', 'inżynier', None, 'rodzaj męski'), ('avocat', 'prawnik', None, 'rodzaj męski'), ('policier', 'policjant', None, 'rodzaj męski'), ('soldat', 'żołnierz', None, 'rodzaj męski'), ('agriculteur', 'rolnik', None, 'rodzaj męski'), ('vendeur', 'sprzedawca', None, 'rodzaj męski'), ('caissier', 'kasjer', None, 'rodzaj męski'), ('acteur', 'aktor', None, 'rodzaj męski'), ('écrivain', 'pisarz', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('peintre', 'malarz', None, 'rodzaj męski'), ('musicien', 'muzyk', None, 'rodzaj męski'), ('artiste', 'artysta', None, 'rodzaj męski'), ('entreprise', 'firma', None, 'rodzaj żeński'), ('argent', 'pieniądze', None, 'rodzaj męski'), ('salaire', 'pensja', None, 'rodzaj męski'), ('contrat', 'umowa', None, 'rodzaj męski'), ('réunion', 'spotkanie', None, 'rodzaj żeński'), ('leçon', 'lekcja', None, 'rodzaj żeński'), ('examen', 'egzamin', None, 'rodzaj męski'), ('note', 'ocena', None, 'rodzaj żeński'), ('classe', 'klasa', None, 'rodzaj żeński'), ('livre', 'książka', None, 'rodzaj męski'), ('cahier', 'zeszyt', None, 'rodzaj męski'), ('stylo', 'długopis', None, 'rodzaj męski'), ('crayon', 'ołówek', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('papier', 'papier', None, 'rodzaj męski'), ('tableau', 'tablica', None, 'rodzaj męski'), ('dictionnaire', 'słownik', None, 'rodzaj męski'), ('question', 'pytanie', None, 'rodzaj żeński'), ('réponse', 'odpowiedź', None, 'rodzaj żeński'), ('exercice', 'zadanie', None, 'rodzaj męski'), ('test', 'test', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('prix', 'cena', None, 'rodzaj męski'), ('carte bancaire', 'karta (płatnicza)', None, 'rodzaj żeński'), ('espèces', 'gotówka', None, 'rodzaj żeński'), ('pièce', 'moneta', None, 'rodzaj żeński'), ('billet (banknot)', 'banknot', None, 'rodzaj męski'), ('monnaie', 'reszta', None, 'rodzaj żeński'), ('réduction', 'zniżka', None, 'rodzaj żeński'), ('panier', 'koszyk', None, 'rodzaj męski'), ('ticket de caisse', 'paragon', None, 'rodzaj męski'), ('marchandise', 'towar', None, 'rodzaj żeński'), ('achat', 'zakup', None, 'rodzaj męski'), ('vente', 'sprzedaż', None, 'rodzaj żeński'), ('valeur', 'wartość', None, 'rodzaj żeński'), ('crédit', 'kredyt', None, 'rodzaj męski'), ('dette', 'dług', None, 'rodzaj żeński'), ('impôt', 'podatek', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('richesse', 'bogactwo', None, 'rodzaj żeński'), ('pauvre', 'biedny', None, None), ('riche', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('santé', 'zdrowie', None, 'rodzaj żeński'), ('maladie', 'choroba', None, 'rodzaj żeński'), ('douleur', 'ból', None, 'rodzaj żeński'), ('fièvre', 'gorączka', None, 'rodzaj żeński'), ('toux', 'kaszel', None, 'rodzaj żeński'), ('rhume', 'katar', None, 'rodzaj męski'), ('médicament', 'lekarstwo', None, 'rodzaj męski'), ('comprimé', 'tabletka', None, 'rodzaj męski'), ('opération', 'operacja', None, 'rodzaj żeński'), ('blessure', 'rana', None, 'rodzaj żeński'), ('accident', 'wypadek', None, 'rodzaj męski'), ('en bonne santé', 'zdrowy', None, None), ('malade', 'chory', None, None), ('fatigué', 'zmęczony', None, None), ('somnolent', 'śpiący', None, None), ('fort', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('faible', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('joie', 'radość', None, 'rodzaj żeński'), ('tristesse', 'smutek', None, 'rodzaj żeński'), ('peur', 'strach', None, 'rodzaj żeński'), ('colère', 'gniew', None, 'rodzaj żeński'), ('amour', 'miłość', None, 'rodzaj męski'), ('haine', 'nienawiść', None, 'rodzaj żeński'), ('espoir', 'nadzieja', None, 'rodzaj męski'), ('rêve', 'marzenie', None, 'rodzaj męski'), ('bonheur', 'szczęście', None, 'rodzaj męski'), ('honte', 'wstyd', None, 'rodzaj żeński'), ('surprise', 'zdziwienie', None, 'rodzaj żeński'), ('curiosité', 'ciekawość', None, 'rodzaj żeński'), ('patience', 'cierpliwość', None, 'rodzaj żeński'), ('courage', 'odwaga', None, 'rodzaj męski'), ('sincère', 'szczery', None, None), ('gentil', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('poli', 'grzeczny', None, None), ('bête', 'głupi', None, None), ('intelligent', 'mądry', None, None), ('paresseux', 'leniwy', None, None), ('travailleur', 'pracowity', None, None), ('intéressant', 'ciekawy', None, None), ('ennuyeux', 'nudny', None, None), ('joyeux', 'wesoły', None, None), ('triste', 'smutny', None, None), ('fâché', 'zły (rozgniewany)', None, None), ('heureux', 'szczęśliwy', None, None), ('amoureux', 'zakochany', None, None), ('seul', 'samotny', None, None), ('calme', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('grand', 'duży', None, None), ('long', 'długi', None, None), ('court', 'krótki', None, None), ('haut', 'wysoki', None, None), ('bas', 'niski', None, None), ('large', 'szeroki', None, None), ('étroit', 'wąski', None, None), ('gros', 'gruby', None, None), ('maigre', 'chudy', None, None), ('lourd', 'ciężki', None, None), ('léger', 'lekki', None, None), ('rapide', 'szybki', None, None), ('lent', 'wolny', None, None), ('dur', 'twardy', None, None), ('mou', 'miękki', None, None), ('mouillé', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('sec', 'suchy', None, None), ('propre', 'czysty', None, None), ('sale', 'brudny', None, None), ('plein', 'pełny', None, None), ('vide', 'pusty', None, None), ('aigu', 'ostry', None, None), ('bruyant', 'głośny', None, None), ('silencieux', 'cichy', None, None), ('clair', 'jasny', None, None), ('sombre', 'ciemny', None, None), ('jeune', 'młody', None, None), ('vieux', 'stary', None, None), ('nouveau', 'nowy', None, None), ('mauvais', 'zły (niedobry)', None, None), ('joli', 'ładny', None, None), ('laid', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('facile', 'łatwy', None, None), ('difficile', 'trudny', None, None), ('important', 'ważny', None, None), ('possible', 'możliwy', None, None), ('vrai', 'prawdziwy', None, None), ('faux', 'fałszywy', None, None), ('cher', 'drogi', None, None), ('bon marché', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('être', 'być', None, None), ('avoir', 'mieć', None, None), ('faire', 'robić', None, None), ('aller', 'iść', None, None), ('rouler', 'jechać', None, None), ('venir', 'przyjść', None, None), ('sortir', 'wyjść', None, None), ('entrer', 'wejść', None, None), ('revenir', 'wrócić', None, None), ('courir', 'biec', None, None), ('se tenir debout', 'stać', None, None), ('être assis', 'siedzieć', None, None), ('être allongé', 'leżeć', None, None), ('dormir', 'spać', None, None), ('se lever', 'wstać', None, None), ('manger', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('boire', 'pić', None, None), ('cuisiner', 'gotować', None, None), ('laver', 'myć', None, None), ("s'habiller", 'ubierać się', None, None), ('parler', 'mówić', None, None), ('dire', 'powiedzieć', None, None), ('demander', 'pytać', None, None), ('répondre', 'odpowiadać', None, None), ('entendre', 'słyszeć', None, None), ('écouter', 'słuchać', None, None), ('voir', 'widzieć', None, None), ('regarder', 'patrzeć', None, None), ('lire', 'czytać', None, None), ('écrire', 'pisać', None, None), ('apprendre', 'uczyć się', None, None), ('enseigner', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('comprendre', 'rozumieć', None, None), ('savoir', 'wiedzieć', None, None), ('connaître', 'znać', None, None), ('penser', 'myśleć', None, None), ('se souvenir', 'pamiętać', None, None), ('oublier', 'zapominać', None, None), ('vouloir', 'chcieć', None, None), ('aimer', 'lubić', None, None), ('adorer', 'kochać', None, None), ('avoir besoin', 'potrzebować', None, None), ('pouvoir', 'móc', None, None), ('devoir', 'musieć', None, None), ('donner', 'dawać', None, None), ('prendre', 'brać', None, None), ('acheter', 'kupować', None, None), ('vendre', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('payer', 'płacić', None, None), ('ouvrir', 'otwierać', None, None), ('fermer', 'zamykać', None, None), ('commencer', 'zaczynać', None, None), ('finir', 'kończyć', None, None), ('travailler', 'pracować', None, None), ('jouer', 'grać', None, None), ('chanter', 'śpiewać', None, None), ('danser', 'tańczyć', None, None), ('nager', 'pływać', None, None), ('voler', 'latać', None, None), ('poser', 'kłaść', None, None), ('chercher', 'szukać', None, None), ('trouver', 'znajdować', None, None), ('attendre', 'czekać', None, None), ('aider', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('prier', 'prosić', None, None), ("s'excuser", 'przepraszać', None, None), ('permettre', 'pozwalać', None, None), ('essayer', 'próbować', None, None), ('changer', 'zmieniać', None, None), ('porter', 'nosić', None, None), ('tenir', 'trzymać', None, None), ('jeter', 'rzucać', None, None), ('attraper', 'łapać', None, None), ('frapper', 'bić', None, None), ('tuer', 'zabijać', None, None), ('mourir', 'umierać', None, None), ('vivre', 'żyć', None, None), ('habiter', 'mieszkać', None, None), ('rencontrer', 'spotykać', None, None), ('téléphoner', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('envoyer', 'wysyłać', None, None), ('recevoir', 'dostawać', None, None), ('montrer', 'pokazywać', None, None), ('inviter', 'zapraszać', None, None), ('visiter', 'odwiedzać', None, None), ('pleurer', 'płakać', None, None), ('rire', 'śmiać się', None, None), ('sourire', 'uśmiechać się', None, None), ('avoir peur', 'bać się', None, None), ('se réjouir', 'cieszyć się', None, None), ('croire', 'wierzyć', None, None), ("être d'accord", 'zgadzać się', None, None), ('choisir', 'wybierać', None, None), ('décider', 'decydować', None, None), ('compter', 'liczyć', None, None), ('peser', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('marcher', 'chodzić', None, None), ('se déplacer', 'jeździć', None, None), ('monter', 'wsiadać', None, None), ('descendre', 'wysiadać', None, None), ('tourner', 'skręcać', None, None), ("s'arrêter", 'zatrzymywać się', None, None), ('être en retard', 'spóźniać się', None, None), ('se dépêcher', 'spieszyć się', None, None), ('se reposer', 'odpoczywać', None, None), ("s'amuser", 'bawić się', None, None), ('dessiner', 'rysować', None, None), ('construire', 'budować', None, None), ('réparer', 'naprawiać', None, None), ('couper', 'ciąć', None, None), ('frire', 'smażyć', None, None), ('cuire au four', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('mélanger', 'mieszać', None, None), ('verser', 'nalewać', None, None), ('ranger', 'sprzątać', None, None), ('laver le linge', 'prać', None, None), ('repasser', 'prasować', None, None), ('se raser', 'golić się', None, None), ('peigner', 'czesać', None, None), ('se baigner', 'kąpać się', None, None), ('se réveiller', 'budzić się', None, None), ("s'endormir", 'zasypiać', None, None), ('rêver', 'marzyć', None, None), ('rêver (we śnie)', 'śnić', None, None), ("s'exercer", 'ćwiczyć', None, None), ("s'entraîner", 'trenować', None, None), ('gagner', 'wygrywać', None, None), ('perdre', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('bouger', 'ruszać', None, None), ('tirer', 'ciągnąć', None, None), ('pousser', 'pchać', None, None), ('lever', 'podnosić', None, None), ('tomber', 'spadać', None, None), ('sauter', 'skakać', None, None), ('grimper', 'wspinać się', None, None), ('cacher', 'ukrywać', None, None), ('voler (kraść)', 'kraść', None, None), ('rendre', 'oddawać', None, None), ('prêter', 'pożyczać', None, None), ('dépenser', 'wydawać', None, None), ('économiser', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('ce', 'ten', None, None), ('celui-là', 'tamten', None, None), ('comment', 'jak', None, None), ('pourquoi', 'dlaczego', None, None), ('quoi', 'co', None, None), ('qui', 'kto', None, None), ('quel', 'który', None, None), ('quel genre', 'jaki', None, None), ('combien', 'ile (policzalne)', None, None), ('mais', 'ale', None, None), ('ou', 'lub', None, None), ('parce que', 'bo', None, None), ('si', 'jeśli', None, None), ('que', 'że', None, None), ('donc', 'więc', None, None), ('aussi', 'też', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('seulement', 'tylko', None, None), ('un peu', 'trochę', None, None), ('beaucoup de', 'dużo', None, None), ('tout', 'wszystko', None, None), ('rien', 'nic', None, None), ('quelque chose', 'coś', None, None), ("quelqu'un", 'ktoś', None, None), ('personne', 'nikt', None, None), ('chacun', 'każdy', None, None), ('autre', 'inny', None, None), ('le même', 'ten sam', None, None), ('peut-être', 'może (być)', None, None), ('sûrement', 'na pewno', None, None), ('ensemble', 'razem', None, None), ('seul (sam)', 'sam', None, None), ('sans', 'bez', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('avec', 'z (towarzysząc)', None, None), ('dans', 'w (miejsce)', None, None), ('sur', 'na (powierzchni)', None, None), ('vers', 'do (kierunek)', None, None), ('depuis', 'od', None, None), ('pour', 'dla', None, None), ('par', 'przez', None, None), ('après', 'po (czas)', None, None), ('avant', 'przed', None, None), ('derrière', 'za (z tyłu)', None, None), ('au-dessus de', 'nad', None, None), ('sous', 'pod', None, None), ('à côté de', 'obok', None, None), ('entre', 'między', None, None), ('contre', 'przeciw', None, None), ('au sujet de', 'o (temat)', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('chez', 'u (przy)', None, None), ('environ', 'około', None, None), ('presque', 'prawie', None, None), ('même', 'nawet', None, None), ('encore une fois', 'jeszcze raz', None, None), ('alors', 'wtedy', None, None), ('quelque part', 'gdzieś', None, None), ('nulle part', 'nigdzie', None, None), ('partout', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('vie', 'życie', None, 'rodzaj żeński'), ('mort', 'śmierć', None, 'rodzaj żeński'), ('monde', 'świat', None, 'rodzaj męski'), ('pays', 'kraj', None, 'rodzaj męski'), ('État', 'państwo', None, 'rodzaj męski'), ('langue (mowa)', 'język (mowa)', None, 'rodzaj żeński'), ('mot', 'słowo', None, 'rodzaj męski'), ('phrase', 'zdanie', None, 'rodzaj żeński'), ('prénom', 'imię', None, 'rodzaj męski'), ('nom', 'nazwisko', None, 'rodzaj męski'), ('âge', 'wiek', None, 'rodzaj męski'), ('histoire', 'historia', None, 'rodzaj żeński'), ('culture', 'kultura', None, 'rodzaj żeński'), ('religion', 'religia', None, 'rodzaj żeński'), ('Dieu', 'Bóg', None, 'rodzaj męski'), ('guerre', 'wojna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('paix', 'pokój (brak wojny)', None, 'rodzaj żeński'), ('loi', 'prawo (przepis)', None, 'rodzaj żeński'), ('liberté', 'wolność', None, 'rodzaj żeński'), ('pouvoir (władza)', 'władza', None, 'rodzaj męski'), ('gouvernement', 'rząd', None, 'rodzaj męski'), ('élections', 'wybory', None, 'rodzaj żeński'), ('problème', 'problem', None, 'rodzaj męski'), ('idée', 'pomysł', None, 'rodzaj żeński'), ('raison', 'powód', None, 'rodzaj żeński'), ('résultat', 'wynik', None, 'rodzaj męski'), ('manière', 'sposób', None, 'rodzaj żeński'), ('début', 'początek', None, 'rodzaj męski'), ('fin', 'koniec', None, 'rodzaj żeński'), ('partie', 'część', None, 'rodzaj żeński'), ('lieu', 'miejsce', None, 'rodzaj męski'), ('chose', 'rzecz', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('affaire', 'sprawa', None, 'rodzaj żeński'), ('information', 'informacja', None, 'rodzaj żeński'), ('message', 'wiadomość', None, 'rodzaj męski'), ('lettre', 'list', None, 'rodzaj żeński'), ('journal', 'gazeta', None, 'rodzaj męski'), ('film', 'film', None, 'rodzaj męski'), ('musique', 'muzyka', None, 'rodzaj żeński'), ('chanson', 'piosenka', None, 'rodzaj żeński'), ('tableau (obraz)', 'obraz', None, 'rodzaj męski'), ('jeu', 'gra', None, 'rodzaj męski'), ('sport', 'sport', None, 'rodzaj męski'), ('match', 'mecz', None, 'rodzaj męski'), ('équipe', 'drużyna', None, 'rodzaj żeński'), ('ballon', 'piłka', None, 'rodzaj męski'), ('amusement', 'zabawa', None, 'rodzaj męski'), ('fête (impreza)', 'impreza', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('cadeau', 'prezent', None, 'rodzaj męski'), ('rêve (nocny)', 'sen', None, 'rodzaj męski'), ('plan', 'plan', None, 'rodzaj męski'), ('choix', 'wybór', None, 'rodzaj męski'), ('erreur', 'błąd', None, 'rodzaj żeński'), ('vérité', 'prawda', None, 'rodzaj żeński'), ('mensonge', 'kłamstwo', None, 'rodzaj męski'), ('secret', 'tajemnica', None, 'rodzaj męski'), ('force', 'siła', None, 'rodzaj żeński'), ('énergie', 'energia', None, 'rodzaj żeński'), ('lumière', 'światło', None, 'rodzaj żeński'), ('son', 'dźwięk', None, 'rodzaj męski'), ('silence', 'cisza', None, 'rodzaj męski'), ('mouvement', 'ruch', None, 'rodzaj męski'), ('changement', 'zmiana', None, 'rodzaj męski'), ('différence', 'różnica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('exemple', 'przykład', None, 'rodzaj męski'), ('ensemble (całość)', 'całość', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, 'rodzaj męski'), ('courriel', 'e-mail', None, 'rodzaj męski'), ('mot de passe', 'hasło', None, 'rodzaj męski'), ('site web', 'strona internetowa', None, 'rodzaj męski'), ('programme', 'program', None, 'rodzaj męski'), ('application', 'aplikacja', None, 'rodzaj żeński'), ('écran', 'ekran', None, 'rodzaj męski'), ('clavier', 'klawiatura', None, 'rodzaj męski'), ("souris d'ordinateur", 'myszka komputerowa', None, 'rodzaj żeński'), ('fichier', 'plik', None, 'rodzaj męski'), ('photo', 'zdjęcie', None, 'rodzaj żeński'), ('caméra', 'kamera', None, 'rodzaj żeński'), ('pile', 'bateria', None, 'rodzaj żeński'), ('courant', 'prąd', None, 'rodzaj męski'), ('câble', 'kabel', None, 'rodzaj męski'), ('machine', 'maszyna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('outil', 'narzędzie', None, 'rodzaj męski'), ('marteau', 'młotek', None, 'rodzaj męski'), ('imprimante', 'drukarka', None, 'rodzaj żeński'), ('chargeur', 'ładowarka', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('nord', 'północ', None, 'rodzaj męski'), ('sud', 'południe (kierunek)', None, 'rodzaj męski'), ('ouest', 'zachód', None, 'rodzaj męski'), ('Europe', 'Europa', None, 'rodzaj żeński'), ('Allemagne', 'Niemcy', None, 'rodzaj żeński'), ('Italie', 'Włochy', None, 'rodzaj żeński'), ('Espagne', 'Hiszpania', None, 'rodzaj żeński'), ('Russie', 'Rosja', None, 'rodzaj żeński'), ('Angleterre', 'Anglia', None, 'rodzaj żeński'), ('Amérique', 'Ameryka', None, 'rodzaj żeński'), ('Chine', 'Chiny', None, 'rodzaj żeński'), ('Japon', 'Japonia', None, 'rodzaj męski'), ('Afrique', 'Afryka', None, 'rodzaj żeński'), ('Asie', 'Azja', None, 'rodzaj żeński'), ('continent', 'kontynent', None, 'rodzaj męski'), ('capitale', 'stolica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('citoyen', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('morceau', 'kawałek', None, 'rodzaj męski'), ('goutte', 'kropla', None, 'rodzaj żeński'), ('boîte', 'pudełko', None, 'rodzaj żeński'), ('sac (worek)', 'worek', None, 'rodzaj męski'), ('fil', 'nić', None, 'rodzaj męski'), ('fil de fer', 'drut', None, 'rodzaj męski'), ('aiguille', 'igła', None, 'rodzaj żeński'), ('ciseaux', 'nożyczki', None, 'rodzaj męski'), ('bâton', 'kij', None, 'rodzaj męski'), ('corde', 'lina', None, 'rodzaj żeński'), ('chaîne', 'łańcuch', None, 'rodzaj żeński'), ('vis', 'śruba', None, 'rodzaj żeński'), ('clou', 'gwóźdź', None, 'rodzaj męski'), ('colle', 'klej', None, 'rodzaj żeński'), ('peinture', 'farba', None, 'rodzaj żeński'), ('verre (materiał)', 'szkło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('bois', 'drewno', None, 'rodzaj męski'), ('métal', 'metal', None, 'rodzaj męski'), ('or', 'złoto', None, 'rodzaj męski'), ('argent (metal)', 'srebro', None, 'rodzaj męski'), ('fer', 'żelazo', None, 'rodzaj męski'), ('plastique', 'plastik', None, 'rodzaj męski'), ('cuir', 'skóra (materiał)', None, 'rodzaj męski'), ('coton', 'bawełna', None, 'rodzaj męski'), ('laine', 'wełna', None, 'rodzaj żeński'), ('sable', 'piasek', None, 'rodzaj męski'), ('boue', 'błoto', None, 'rodzaj żeński'), ('poussière', 'kurz', None, 'rodzaj żeński'), ('fumée', 'dym', None, 'rodzaj żeński'), ('vapeur', 'para (wodna)', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('en haut', 'góra (kierunek)', None, None), ('en bas', 'dół', None, None), ('devant', 'przód', None, None), ('derrière (tył)', 'tył', None, None), ('milieu', 'środek', None, 'rodzaj męski'), ('côté', 'bok', None, 'rodzaj męski'), ("à l'intérieur", 'wewnątrz', None, None), ('dehors', 'na zewnątrz', None, None), ('loin', 'daleko', None, None), ('près', 'blisko', None, None), ('haut (przysłówek)', 'wysoko', None, None), ('bas (przysłówek)', 'nisko', None, None), ('vite', 'szybko', None, None), ('lentement', 'wolno', None, None), ('bien', 'dobrze', None, None), ('mal', 'źle', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('facilement', 'łatwo', None, None), ('difficilement', 'trudno', None, None), ('séparément', 'osobno', None, None), ('en face', 'naprzeciw', None, None), ('le long de', 'wzdłuż', None, None), ('en travers', 'w poprzek', None, None), ('autour', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('chou', 'kapusta', None, 'rodzaj męski'), ('petit pois', 'groszek', None, 'rodzaj męski'), ('haricot', 'fasola', None, 'rodzaj męski'), ('champignon', 'grzyb', None, 'rodzaj męski'), ('noix', 'orzech', None, 'rodzaj żeński'), ('prune', 'śliwka', None, 'rodzaj żeński'), ('cerise', 'wiśnia', None, 'rodzaj żeński'), ('pêche', 'brzoskwinia', None, 'rodzaj żeński'), ('pastèque', 'arbuz', None, 'rodzaj żeński'), ('framboise', 'malina', None, 'rodzaj żeński'), ('saucisse', 'kiełbasa', None, 'rodzaj żeński'), ('jambon', 'szynka', None, 'rodzaj męski'), ('petit pain', 'bułka', None, 'rodzaj męski'), ('sandwich', 'kanapka', None, 'rodzaj męski'), ('crêpe', 'naleśnik', None, 'rodzaj żeński'), ('yaourt', 'jogurt', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('crème', 'śmietana', None, 'rodzaj żeński'), ('sauce', 'sos', None, 'rodzaj żeński'), ('vinaigre', 'ocet', None, 'rodzaj męski'), ('levure', 'drożdże', None, 'rodzaj żeński'), ('gelée de fruits', 'kisiel', None, 'rodzaj żeński'), ('gelée', 'galaretka', None, 'rodzaj żeński'), ('raisin sec', 'rodzynek', None, 'rodzaj męski'), ('amande', 'migdał', None, 'rodzaj żeński'), ('persil', 'pietruszka', None, 'rodzaj męski'), ('aneth', 'koperek', None, 'rodzaj męski'), ('poivron', 'papryka', None, 'rodzaj męski'), ('laitue', 'sałata', None, 'rodzaj żeński'), ('épinards', 'szpinak', None, 'rodzaj męski'), ('betterave', 'burak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('beau-père', 'teść', None, 'rodzaj męski'), ('belle-mère', 'teściowa', None, 'rodzaj żeński'), ('beau-frère', 'szwagier', None, 'rodzaj męski'), ('neveu', 'bratanek', None, 'rodzaj męski'), ('nièce', 'siostrzenica', None, 'rodzaj żeński'), ('orphelin', 'sierota', None, 'rodzaj męski'), ('veuve', 'wdowa', None, 'rodzaj żeński'), ('fiancé', 'narzeczony', None, 'rodzaj męski'), ('mariage', 'ślub', None, 'rodzaj męski'), ('divorce', 'rozwód', None, 'rodzaj męski'), ('naissance', 'urodzenie', None, 'rodzaj żeński'), ('enterrement', 'pogrzeb', None, 'rodzaj męski'), ('coiffeur', 'fryzjer', None, 'rodzaj męski'), ('boulanger', 'piekarz', None, 'rodzaj męski'), ('boucher', 'rzeźnik', None, 'rodzaj męski'), ('serveuse', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('facteur', 'listonosz', None, 'rodzaj męski'), ('pompier', 'strażak', None, 'rodzaj męski'), ('juge', 'sędzia', None, 'rodzaj męski'), ('directeur', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
