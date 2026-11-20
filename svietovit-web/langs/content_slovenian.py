"""Treść kursu: słoweński dla Polaków."""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "GLAS · WYMOWA", "jezyk": "JEZIK · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "Š", "track": "wymowa",
     "letters": [
         ("č", "[tʃ]: jak polskie cz", "čaj (herbata)"),
         ("š", "[ʃ]: jak polskie sz", "šola (szkoła)"),
         ("ž", "[ʒ]: jak polskie ż", "živjo (cześć)"),
         ("c", "[ts]: jak polskie c", "cesta (droga)"),
         ("j", "[j]: jak polskie j", "jabolko (jabłko)"),
         ("v", "[ʋ]: jak polskie w; na końcu sylaby brzmi jak [w] (ł)", "voda (woda)"),
         ("l na końcu sylaby", "[w]: l na końcu słowa lub przed spółgłoską brzmi jak polskie ł", "dal (dał)"),
         ("h", "[x]: jak polskie ch", "hiša (dom)"),
         ("lj, nj", "[ʎ], [ɲ]: jak miękkie l i ń", "Ljubljana (stolica)"),
         ("r", "[r]: toczone; może stać między spółgłoskami jak samogłoska", "prst (palec)"),
         ("e, o", "mogą być krótkie i otwarte albo długie i zamknięte (pisownia tego nie pokazuje)", "dober (dobry)"),
         ("akcent", "nie jest zaznaczany w piśmie; wymawiasz słowo naturalnie, uczysz się go razem ze słowem", "mama (mama)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "Z", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("živjo", "cześć", None, None),
         ("nasvidenje", "do widzenia", None, "Dosł. „na zobaczenie”."),
         ("hvala", "dziękuję", None, None),
         ("prosim", "proszę", None, None),
         ("da", "tak", None, None),
         ("ne", "nie", None, None),
         ("dober", "dobry", None, None),
         ("dan", "dzień", None, None),
         ("večer", "wieczór", None, None),
         ("jutro", "rano; poranek", None, "„Jutro” to poranek. „Jutro” w sensie dnia to „jutri”."),
         ("noč", "noc", None, None),
         ("lahko", "łatwo; lekko", None, "„Lahko noč” = dobranoc, dosł. „lekka noc”."),
         ("dobro", "dobrze; dobry (n.)", None, None),
         ("oprosti", "przepraszam", None, None),
         ("zelo", "bardzo", None, None),
         ("in", "i", None, None),
     ],
     "sentences": [
         (["živjo", "!"], "Cześć!", {"nasvidenje": "nasvidenje to „do widzenia”."}),
         (["nasvidenje", "!"], "Do widzenia!", {"živjo": "živjo to „cześć”."}),
         (["dober", "dan", "!"], "Dzień dobry!", {"noč": "noč to „noc”."}),
         (["dobro", "jutro", "!"], "Dzień dobry (rano)!", {"večer": "večer to „wieczór”."}),
         (["lahko", "noč", "!"], "Dobranoc!", {"jutro": "jutro to „rano”."}),
         (["hvala", "!"], "Dziękuję!", {"prosim": "prosim to „proszę”. Tu dziękujesz."}),
         (["da", ",", "hvala"], "Tak, dziękuję.", {"ne": "ne to „nie”."}),
         (["ne", ",", "hvala"], "Nie, dziękuję.", {"da": "da to „tak”."}),
         (["oprosti", "!"], "Przepraszam!", {}),
         (["zelo", "dobro", "!"], "Bardzo dobrze!", {}),
         (["dober", "večer", "!"], "Dobry wieczór!", {"dan": "dan to „dzień”."}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "J", "track": "jezyk",
     "words": [
         ("jaz", "ja", None, None),
         ("ti", "ty", None, None),
         ("on", "on", None, None),
         ("ona", "ona", None, None),
         ("mi", "my", None, None),
         ("sem", "jestem", None, None),
         ("si", "jesteś", None, None),
         ("je", "jest", None, None),
         ("smo", "jesteśmy", None, None),
         ("midva", "my dwaj (my dwoje)", None, "Słoweński ma liczbę podwójną: midva = my dwaj."),
         ("sva", "jesteśmy (my dwaj)", None, "Forma dla dwóch osób."),
         ("učenec", "uczeń", None, None),
         ("učenca", "dwaj uczniowie", None, "Liczba podwójna: dwóch uczniów."),
         ("učitelj", "nauczyciel", None, None),
         ("Poljak", "Polak", None, None),
         ("Poljakinja", "Polka", None, None),
         ("iz", "z", None, None),
         ("Poljske", "z Polski (dopełniacz)", None, "Po „iz” rzeczownik jest w dopełniaczu."),
         ("Slovenije", "ze Słowenii (dopełniacz)", None, "Po „iz” rzeczownik jest w dopełniaczu."),
     ],
     "sentences": [
         (["jaz", "sem", "učenec"], "Jestem uczniem.", {"si": "si to „jesteś”. O sobie: sem."}),
         (["ti", "si", "učitelj"], "Jesteś nauczycielem.", {"sem": "sem to „jestem”. Do „ti”: si."}),
         (["on", "je", "Poljak"], "On jest Polakiem.", {"Poljakinja": "Dla mężczyzny: Poljak."}),
         (["ona", "je", "Poljakinja"], "Ona jest Polką.", {"Poljak": "Dla kobiety: Poljakinja."}),
         (["jaz", "sem", "iz", "Poljske"], "Jestem z Polski.", {"Slovenije": "Slovenije to „ze Słowenii”."}),
         (["on", "je", "iz", "Slovenije"], "On jest ze Słowenii.", {}),
         (["mi", "smo", "učenci"], "Jesteśmy uczniami.", {"sva": "sva dotyczy tylko dwóch osób."}),
         (["midva", "sva", "učenca"], "My dwaj jesteśmy uczniami.", {"smo": "smo to „jesteśmy” (więcej niż dwie osoby)."}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "R", "track": "jezyk",
     "words": [
         ("mama", "mama", None, None),
         ("oče", "ojciec", None, None),
         ("brat", "brat", None, None),
         ("sestra", "siostra", None, None),
         ("otrok", "dziecko", None, None),
         ("prijatelj", "przyjaciel", None, None),
         ("moj", "mój", None, None),
         ("moja", "moja", None, None),
         ("tvoj", "twój", None, None),
         ("tvoja", "twoja", None, None),
         ("imam", "mam", None, None),
         ("imaš", "masz", None, None),
         ("ima", "ma", None, None),
         ("brata", "brata (biernik)", None, "Po „imam” rzeczownik w bierniku: brat → brata."),
         ("sestro", "siostrę (biernik)", None, "Biernik żeński: sestra → sestro."),
         ("prijatelja", "przyjaciela (biernik)", None, "Biernik męski osoby: prijatelj → prijatelja."),
         ("učiteljica", "nauczycielka", None, None),
     ],
     "sentences": [
         (["jaz", "imam", "brata"], "Mam brata.", {"imaš": "imaš to „masz”. O sobie: imam."}),
         (["ti", "imaš", "sestro"], "Masz siostrę.", {"imam": "imam to „mam”. Do „ti”: imaš."}),
         (["on", "ima", "prijatelja"], "On ma przyjaciela.", {}),
         (["moj", "brat", "je", "učitelj"], "Mój brat jest nauczycielem.", {"moja": "moja jest przy rzeczowniku żeńskim."}),
         (["moja", "mama", "je", "učiteljica"], "Moja mama jest nauczycielką.", {"moj": "moj jest przy rzeczowniku męskim."}),
         (["tvoja", "sestra", "je", "učiteljica"], "Twoja siostra jest nauczycielką.", {"tvoj": "tvoj jest przy rzeczowniku męskim."}),
         (["moj", "oče", "je", "Poljak"], "Mój ojciec jest Polakiem.", {}),
         (["ti", "imaš", "otroka"], "Masz dziecko.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "K", "track": "jezyk",
     "words": [
         ("kavo", "kawę (biernik)", None, "Biernik: kava → kavo."),
         ("čaj", "herbata", None, None),
         ("vodo", "wodę (biernik)", None, "Biernik: voda → vodo."),
         ("mleko", "mleko", None, None),
         ("kruh", "chleb", None, None),
         ("sir", "ser", None, None),
         ("jabolko", "jabłko", "jabłko", None),
         ("ribo", "rybę (biernik)", None, "Biernik: riba → ribo."),
         ("meso", "mięso", None, None),
         ("želim", "chcę", None, None),
         ("želiš", "chcesz", None, None),
         ("pijem", "piję", None, None),
         ("piješ", "pijesz", None, None),
         ("jem", "jem", None, None),
         ("rad", "chętnie; lubiący (m.)", None, "„Rad imam” = lubię. Kobieta mówi „rada imam”."),
     ],
     "sentences": [
         (["želim", "kavo", ",", "prosim"], "Poproszę kawę.", {"želiš": "želiš to „chcesz”. O sobie: želim."}),
         (["jaz", "pijem", "čaj"], "Piję herbatę.", {"piješ": "piješ to „pijesz”. O sobie: pijem."}),
         (["ti", "piješ", "vodo"], "Pijesz wodę.", {"pijem": "pijem to „piję”. Do „ti”: piješ."}),
         (["jaz", "jem", "kruh", "in", "sir"], "Jem chleb i ser.", {}),
         (["želim", "mleko", "in", "kruh"], "Chcę mleko i chleb.", {}),
         (["ti", "želiš", "ribo"], "Chcesz rybę.", {"želim": "želim to „chcę”. Do „ti”: želiš."}),
         (["rad", "imam", "sir"], "Lubię ser.", {}),
         (["jaz", "jem", "meso"], "Jem mięso.", {}),
         (["jaz", "jem", "jabolko"], "Jem jabłko.", {}),
     ]},
    {"id": "liczby", "title": "Liczby i pieniądze", "icon": "1", "track": "jezyk",
     "words": [
         ("en", "jeden", None, None),
         ("dva", "dwa", None, None),
         ("tri", "trzy", None, None),
         ("štiri", "cztery", None, None),
         ("pet", "pięć", None, None),
         ("šest", "sześć", None, None),
         ("sedem", "siedem", None, None),
         ("osem", "osiem", None, None),
         ("devet", "dziewięć", None, None),
         ("deset", "dziesięć", None, None),
         ("koliko", "ile", None, None),
         ("stane", "kosztuje", None, None),
         ("evro", "euro (1)", None, None),
         ("evra", "euro (2)", None, "Po „dva” liczba podwójna: dva evra."),
         ("evre", "euro (3, 4)", None, "Po „tri”, „štiri”: tri evre."),
         ("evrov", "euro (5 i więcej)", None, "Od pięciu w górę: dopełniacz liczby mnogiej."),
         ("danes", "dziś", None, None),
     ],
     "sentences": [
         (["koliko", "stane", "kava", "?"], "Ile kosztuje kawa?", {}),
         (["kruh", "stane", "en", "evro"], "Chleb kosztuje jedno euro.", {"evra": "evra jest po „dva”."}),
         (["čaj", "stane", "dva", "evra"], "Herbata kosztuje dwa euro.", {"evro": "evro jest po „en”."}),
         (["sir", "stane", "tri", "evre"], "Ser kosztuje trzy euro.", {"evrov": "evrov jest od „pet”."}),
         (["meso", "stane", "pet", "evrov"], "Mięso kosztuje pięć euro.", {"evre": "evre jest po „tri”, „štiri”."}),
         (["mleko", "stane", "deset", "evrov"], "Mleko kosztuje dziesięć euro.", {}),
         (["danes", "želim", "šest", "jabolk"], "Dziś chcę sześć jabłek.", {}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "L", "track": "jezyk",
     "words": [
         ("hiša", "dom (budynek)", None, None),
         ("doma", "w domu", None, None),
         ("domov", "do domu", None, None),
         ("mesto", "miasto", None, None),
         ("ulica", "ulica", "ulica", None),
         ("šola", "szkoła", None, None),
         ("morje", "morze", None, None),
         ("hotel", "hotel", "hotel", None),
         ("taksi", "taksówka", "taksówka", None),
         ("kje", "gdzie", None, None),
         ("tukaj", "tu", None, None),
         ("tam", "tam", None, None),
         ("grem", "idę; jadę", None, None),
         ("greš", "idziesz; jedziesz", None, None),
         ("desno", "w prawo; po prawej", None, None),
         ("levo", "w lewo; po lewej", None, None),
         ("v", "w; do", None, None),
         ("Ljubljano", "do Lublany (biernik)", None, "Po „v” pytanie „dokąd” = biernik: Ljubljana → Ljubljano."),
     ],
     "sentences": [
         (["kje", "je", "hotel", "?"], "Gdzie jest hotel?", {"tukaj": "tukaj to „tu”. Pytasz „gdzie”: kje."}),
         (["hotel", "je", "tam"], "Hotel jest tam.", {"tukaj": "tukaj to „tu”. Tu „tam”: tam."}),
         (["jaz", "grem", "domov"], "Idę do domu.", {"doma": "doma to „w domu”. Ruch: domov."}),
         (["jaz", "grem", "v", "Ljubljano"], "Jadę do Lublany.", {}),
         (["ti", "greš", "v", "šolo"], "Idziesz do szkoły.", {}),
         (["taksi", "je", "desno"], "Taksówka jest po prawej.", {"levo": "levo to „po lewej”."}),
         (["šola", "je", "tukaj"], "Szkoła jest tu.", {}),
         (["mama", "je", "doma"], "Mama jest w domu.", {"domov": "domov to „do domu”. Tu jest w domu: doma."}),
     ]},
]

# Poprawka: słowa używane w zdaniach, a dodane w działach (patrz CHAT_EXTRA).
UNITS[3]["words"] += [("otroka", "dziecko (biernik)", None, None)]
UNITS[2]["words"] += [("učenci", "uczniowie", None, "Liczba mnoga: uczniowie.")]
UNITS[5]["words"] += [("kava", "kawa", None, None), ("jabolk", "jabłek (dopełniacz lm.)", None, None)]
UNITS[6]["words"] += [("šolo", "do szkoły (biernik)", None, "Biernik: šola → šolo.")]

INSIGHTS = {
    "wymowa": [{"title": "Pisze się tak, jak się mówi", "chain": [],
                "text": "Słoweński zapisuje się łacinką z trzema znakami, które znasz z polskiego ze słuchu: č = cz, š = sz, ž = ż. Wymowa jest prawie fonetyczna, a l na końcu sylaby brzmi jak ł."}],
    "ja": [{"title": "Liczba podwójna", "chain": [
                ("Jesteśmy uczniami.", ["mi", "smo", "učenci"], "„mi” = my (więcej niż dwóch)."),
                ("My dwaj jesteśmy uczniami.", ["midva", "sva", "učenca"], "„midva” = my dwaj, osobna forma."),
            ],
            "text": "Oprócz liczby pojedynczej i mnogiej słoweński ma liczbę podwójną dla dwóch osób lub rzeczy: midva sva (my dwaj jesteśmy), vidva sta (wy dwaj jesteście)."}],
    "ludzie": [{"title": "Mam i biernik", "chain": [],
                "text": "Po „imam” rzeczownik stoi w bierniku: imam brata, imam sestro. Rzeczownik żeński kończy się wtedy na -o: sestra → sestro."}],
    "jedzenie": [{"title": "Biernik żeński -o", "chain": [],
                  "text": "Po „želim”, „pijem”, „jem” rzeczownik jest w bierniku. Żeńskie na -a zmieniają -a na -o: kava → kavo, voda → vodo, riba → ribo. Męskie i nijakie bez zmian: kruh, sir, mleko."}],
    "liczby": [{"title": "Euro po liczebnikach", "chain": [],
                "text": "Po „en” rzeczownik w liczbie pojedynczej, po „dva” w podwójnej, po „tri” i „štiri” w mnogiej, od „pet” w dopełniaczu mnogim: en evro, dva evra, tri evre, pet evrov."}],
}

ENDINGS_INSIGHT = {"title": "Formy osobowe",
                   "text": "Po słoweńsku czasownik zmienia końcówkę: sem, si, je; pijem, piješ. Tu to ćwiczysz."}

ENDINGS = [
    ("jaz ", "", "sem", " učenec", ["sem", "si"], "ja jestem", "Do „jaz” pasuje sem.", "ja"),
    ("ti ", "", "si", " učitelj", ["sem", "si"], "ty jesteś", "Do „ti” pasuje si.", "ja"),
    ("jaz ", "ima", "m", " brata", ["m", "š"], "ja mam", "Do „jaz” pasuje -m.", "ludzie"),
    ("ti ", "ima", "š", " sestro", ["m", "š"], "ty masz", "Do „ti” pasuje -š.", "ludzie"),
    ("jaz ", "pije", "m", " čaj", ["m", "š"], "ja piję", "Do „jaz” pasuje -m.", "jedzenie"),
    ("ti ", "pije", "š", " vodo", ["m", "š"], "ty pijesz", "Do „ti” pasuje -š.", "jedzenie"),
    ("jaz grem ", "", "domov", "", ["domov", "doma"], "idę do domu", "Ruch: domov.", "miejsca"),
    ("mama je ", "", "doma", "", ["domov", "doma"], "mama jest w domu", "Miejsce: doma.", "miejsca"),
    ("kava stane dva ", "", "evra", "", ["evra", "evre"], "po „dva”", "Po „dva”: evra.", "liczby"),
]

CHAT_EXTRA = {"Maja": "Maja (imię)", "Luka": "Luka (imię)", "taksist": "taksówkarz", "kam": "dokąd", "ime": "imię", "kava": "kawa", "kruh": "chleb"}

CHATS = [
    {"id": "kavarna", "title": "W kawiarni", "partner": "Maja", "avatar": "M", "requires": "jedzenie",
     "turns": [
         {"bot": ["dober", "dan", "!"], "en": "Dzień dobry!",
          "options": [(["dober", "dan", "!"], True, None), (["lahko", "noč", "!"], False, "lahko noč to „dobranoc”. Jest dzień.")]},
         {"bot": ["kavo", "?"], "en": "Kawę?",
          "options": [(["da", ",", "jaz", "želim", "kavo"], True, None),
                      (["da", ",", "ti", "želiš", "kavo"], False, "želiš jest do „ti”. O sobie: želim.")]},
         {"bot": ["in", "kruh", "?"], "en": "I chleb?",
          "options": [(["ne", ",", "hvala"], True, None),
                      (["prosim", "!"], False, "prosim to „proszę”. Odmów: ne, hvala.")]},
         {"bot": ["dobro", "!"], "build": (["hvala", "!"], "Dziękuję!"), "en": "Dobrze!"},
     ]},
    {"id": "spoznavanje", "title": "Poznajemy się", "partner": "Luka", "avatar": "L", "requires": "ludzie",
     "turns": [
         {"bot": ["živjo", "!"], "en": "Cześć!",
          "options": [(["živjo", "!"], True, None), (["oprosti", "!"], False, "oprosti to „przepraszam”. Powitaj: živjo.")]},
         {"bot": ["ti", "si", "iz", "Slovenije", "?"], "en": "Jesteś ze Słowenii?",
          "options": [(["ne", ",", "jaz", "sem", "iz", "Poljske"], True, None),
                      (["ne", ",", "jaz", "si", "iz", "Poljske"], False, "si jest do „ti”. O sobie: sem.")]},
         {"bot": ["ti", "imaš", "brata", "?"], "en": "Masz brata?",
          "options": [(["da", ",", "jaz", "imam", "brata"], True, None),
                      (["da", ",", "jaz", "imaš", "brata"], False, "imaš jest do „ti”. O sobie: imam.")]},
         {"bot": ["nasvidenje", "!"], "build": (["nasvidenje", "!"], "Do widzenia!"), "en": "Do widzenia!"},
     ]},
    {"id": "taksi", "title": "W taksówce", "partner": "taksist", "avatar": "T", "requires": "miejsca",
     "turns": [
         {"bot": ["dober", "dan", "!"], "en": "Dzień dobry!",
          "options": [(["dober", "dan", "!"], True, None), (["lahko", "noč", "!"], False, "lahko noč to „dobranoc”. Jest dzień.")]},
         {"bot": ["kam", "greš", "?"], "en": "Dokąd jedziesz?",
          "options": [(["jaz", "grem", "v", "Ljubljano"], True, None),
                      (["jaz", "greš", "v", "Ljubljano"], False, "greš jest do „ti”. O sobie: grem.")]},
         {"bot": ["hotel", "je", "tam", "."], "en": "Hotel jest tam.",
          "options": [(["desno", "?"], True, None), (["tukaj", "?"], False, "Pytasz o kierunek: desno.")]},
         {"bot": ["da", "!"], "build": (["hvala", "!"], "Dziękuję!"), "en": "Tak!"},
     ]},
]

PARADIGM_LABELS = {
    'os': ['jaz', 'ti', 'on / ona', 'mi', 'vi', 'oni'],
    'dv': ['midva (my dwaj)', 'vidva (wy dwaj)', 'onadva (oni dwaj)'],
    'przyp': ['imenovalnik (kdo? kaj?)', 'rodilnik (koga? česa?)', 'dajalnik (komu? čemu?)', 'tožilnik (koga? kaj?)', 'mestnik (o kom? o čem?)', 'orodnik (s kom? s čim?)'],
    'lic': ['ednina (1)', 'dvojina (2)', 'množina (3 i więcej)'],
    't_ev': ['en ___', 'dva ___', 'tri ___', 'štiri ___', 'pet ___'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'biti (być)', 'os', 'sem; si; je; smo; ste; so', 'Czasownik „być”.'),
    ('conj', 'Wzory koniugacji', 'biti: liczba podwójna', 'dv', 'sva; sta; sta', 'Dla dwóch osób.'),
    ('conj', 'Wzory koniugacji', 'imeti (mieć)', 'os', 'imam; imaš; ima; imamo; imate; imajo', None),
    ('conj', 'Wzory koniugacji', 'iti (iść)', 'os', 'grem; greš; gre; gremo; greste; gredo', 'Forma nieregularna.'),
    ('conj', 'Wzory koniugacji', 'piti (pić)', 'os', 'pijem; piješ; pije; pijemo; pijete; pijejo', None),
    ('conj', 'Wzory koniugacji', 'jesti (jeść)', 'os', 'jem; ješ; je; jemo; jeste; jedo', None),
    ('conj', 'Wzory koniugacji', 'želeti (chcieć)', 'os', 'želim; želiš; želi; želimo; želite; želijo', None),
    ('decl', 'Deklinacja', 'mesto (miasto)', 'przyp', 'mesto; mesta; mestu; mesto; mestu; mestom', None),
    ('decl', 'Deklinacja', 'brat (brat)', 'przyp', 'brat; brata; bratu; brata; bratu; bratom', 'Rzeczownik męski żywotny: biernik = dopełniacz.'),
    ('decl', 'Deklinacja', 'hiša (dom)', 'przyp', 'hiša; hiše; hiši; hišo; hiši; hišo', None),
    ('form', 'Liczba', 'knjiga (książka)', 'lic', 'knjiga; knjigi; knjige', None),
    ('form', 'Liczba', 'mesto (miasto)', 'lic', 'mesto; mesti; mesta', None),
    ('form', 'Liczba', 'brat (brat)', 'lic', 'brat; brata; bratje', None),
    ('form', 'Typowe trudności', 'Liczba + evro', 't_ev', 'evro; evra; evre; evre; evrov', 'Po 1 jedn., po 2 podwójna, po 3 i 4 mnoga, od 5 dopełniacz mnogi.'),
]

LARPS = []

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'jaz (ja)', 'przyp', 'jaz; mene; meni; mene; meni; menoj', 'Krótkie formy: me, mi.'),
    ('decl', 'Zaimki', 'ti (ty)', 'przyp', 'ti; tebe; tebi; tebe; tebi; teboj', 'Krótkie formy: te, ti.'),
    ('decl', 'Zaimki', 'on (on)', 'przyp', 'on; njega; njemu; njega; njem; njim', None),
    ('decl', 'Zaimki', 'ona (ona)', 'przyp', 'ona; nje; njej; njo; njej; njo', None),
    ('decl', 'Zaimki', 'mi (my)', 'przyp', 'mi; nas; nam; nas; nas; nami', None),
    ('decl', 'Zaimki', 'vi (wy)', 'przyp', 'vi; vas; vam; vas; vas; vami', None),
    ('decl', 'Zaimki', 'oni (oni)', 'przyp', 'oni; njih; njim; njih; njih; njimi', None),
    ('decl', 'Zaimki', 'ta (ten)', 'przyp', 'ta; tega; temu; ta; tem; tem', 'Rodzaj męski: biernik = mianownik, gdy rzecz jest nieożywiona.'),
    ('decl', 'Zaimki', 'kdo (kto)', 'przyp', 'kdo; koga; komu; koga; kom; kom', None),
    ('decl', 'Zaimki', 'kaj (co)', 'przyp', 'kaj; česa; čemu; kaj; čem; čim', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'kava stane dva evra': 'Kawa kosztuje dwa euro.'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'dober (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'dober; boljši; najboljši', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'velik (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'velik; večji; največji', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'majhen (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'majhen; manjši; najmanjši', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'slab (zły)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'slab; slabši; najslabši', None),
    ('form', 'Stopniowanie', 'visok (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'visok; višji; najvišji', None),
    ('form', 'Stopniowanie', 'lep (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'lep; lepši; najlepši', None),
    ('form', 'Stopniowanie', 'star (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'star; starejši; najstarejši', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 2 (generowane) ===
PARADIGMS += [
    ('form', 'Czas przeszły', 'biti: preteklik', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'bil sem; bila sem; bil je; bila je; bili smo; bili so', None),
    ('form', 'Czas przeszły', 'imeti: preteklik', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'imel sem; imela sem; imel je; imela je; imeli smo; imeli so', None),
    ('form', 'Czas przeszły', 'govoriti: preteklik', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'govoril sem; govorila sem; govoril je; govorila je; govorili smo; govorili so', None),
    ('conj', 'Czas przyszły', 'biti: prihodnik', ['jaz', 'ti', 'on / ona', 'mi', 'vi', 'oni'], 'bom; boš; bo; bomo; boste; bodo', None),
    ('conj', 'Czas przyszły', 'govoriti: prihodnik', ['jaz', 'ti', 'on / ona', 'mi', 'vi', 'oni'], 'bom govoril; boš govoril; bo govoril; bomo govorili; boste govorili; bodo govorili', 'Przyszłość = bom + imiesłów na -l.'),
    ('form', 'Liczba podwójna', 'imeti: dvojina', ['1. osoba (my dwaj)', '2. osoba (wy dwaj)', '3. osoba (oni dwaj)'], 'imava; imata; imata', None),
    ('form', 'Liczba podwójna', 'govoriti: dvojina', ['1. osoba (my dwaj)', '2. osoba (wy dwaj)', '3. osoba (oni dwaj)'], 'govoriva; govorita; govorita', None),
    ('form', 'Deklinacja rzeczowników', 'miza (stół, ż.)', ['mianownik', 'dopełniacz', 'celownik', 'biernik', 'miejscownik', 'narzędnik'], 'miza; mize; mizi; mizo; mizi; mizo', None),
    ('form', 'Deklinacja rzeczowników', 'knjiga (książka, ż.)', ['mianownik', 'dopełniacz', 'celownik', 'biernik', 'miejscownik', 'narzędnik'], 'knjiga; knjige; knjigi; knjigo; knjigi; knjigo', None),
    ('form', 'Deklinacja rzeczowników', 'človek (człowiek, m.)', ['mianownik', 'dopełniacz', 'celownik', 'biernik', 'miejscownik', 'narzędnik'], 'človek; človeka; človeku; človeka; človeku; človekom', None),
    ('form', 'Deklinacja rzeczowników', 'okno (okno, n.)', ['mianownik', 'dopełniacz', 'celownik', 'biernik', 'miejscownik', 'narzędnik'], 'okno; okna; oknu; okno; oknu; oknom', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 2 ===
