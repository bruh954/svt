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

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('moški', 'mężczyzna', None, 'rodzaj męski'), ('ženska', 'kobieta', None, 'rodzaj żeński'), ('fant', 'chłopiec', None, 'rodzaj męski'), ('deklica', 'dziewczynka', None, 'rodzaj żeński'), ('človek', 'człowiek', None, 'rodzaj męski'), ('ljudje', 'ludzie', None, None), ('družina', 'rodzina', None, 'rodzaj żeński'), ('mati', 'matka', None, 'rodzaj żeński'), ('sin', 'syn', None, 'rodzaj męski'), ('hči', 'córka', None, 'rodzaj żeński'), ('dedek', 'dziadek', None, 'rodzaj męski'), ('babica', 'babcia', None, 'rodzaj żeński'), ('vnuk', 'wnuk', None, 'rodzaj męski'), ('stric', 'wujek', None, 'rodzaj męski'), ('teta', 'ciocia', None, 'rodzaj żeński'), ('bratranec', 'kuzyn', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('mož', 'mąż', None, 'rodzaj męski'), ('žena', 'żona', None, 'rodzaj żeński'), ('sosed', 'sąsiad', None, 'rodzaj męski'), ('gost', 'gość', None, 'rodzaj męski'), ('šef', 'szef', None, 'rodzaj męski'), ('kolega', 'kolega', None, 'rodzaj męski'), ('sovražnik', 'wróg', None, 'rodzaj męski'), ('kralj', 'król', None, 'rodzaj męski'), ('kraljica', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('glava', 'głowa', None, 'rodzaj żeński'), ('obraz', 'twarz', None, 'rodzaj męski'), ('oko', 'oko', None, 'rodzaj nijaki'), ('uho', 'ucho', None, 'rodzaj nijaki'), ('nos', 'nos', None, 'rodzaj męski'), ('usta', 'usta', None, None), ('zob', 'ząb', None, 'rodzaj męski'), ('jezik', 'język (narząd)', None, 'rodzaj męski'), ('lasje', 'włosy', None, None), ('vrat', 'szyja', None, 'rodzaj męski'), ('rama', 'ramię', None, 'rodzaj nijaki'), ('roka', 'ręka', None, 'rodzaj żeński'), ('prst', 'palec', None, 'rodzaj męski'), ('noga', 'noga', None, 'rodzaj żeński'), ('stopalo', 'stopa', None, 'rodzaj nijaki'), ('koleno', 'kolano', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('hrbet', 'plecy', None, 'rodzaj męski'), ('trebuh', 'brzuch', None, 'rodzaj męski'), ('srce', 'serce', None, 'rodzaj nijaki'), ('kri', 'krew', None, 'rodzaj żeński'), ('kost', 'kość', None, 'rodzaj żeński'), ('koža', 'skóra', None, 'rodzaj żeński'), ('glas', 'głos', None, 'rodzaj męski'), ('telo', 'ciało', None, 'rodzaj nijaki'), ('želodec', 'żołądek', None, 'rodzaj męski'), ('brada', 'broda', None, 'rodzaj żeński'), ('ustnica', 'warga', None, 'rodzaj żeński'), ('noht', 'paznokieć', None, 'rodzaj męski'), ('prsi', 'pierś', None, None), ('možgani', 'mózg', None, None)], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('maslo', 'masło', None, 'rodzaj nijaki'), ('jajce', 'jajko', None, 'rodzaj nijaki'), ('riba', 'ryba', None, 'rodzaj żeński'), ('piščanec', 'kurczak', None, 'rodzaj męski'), ('svinjina', 'wieprzowina', None, 'rodzaj żeński'), ('juha', 'zupa', None, 'rodzaj żeński'), ('solata', 'sałatka', None, 'rodzaj żeński'), ('riž', 'ryż', None, 'rodzaj męski'), ('testenine', 'makaron', None, None), ('krompir', 'ziemniak', None, 'rodzaj męski'), ('korenček', 'marchewka', None, 'rodzaj męski'), ('čebula', 'cebula', None, 'rodzaj żeński'), ('česen', 'czosnek', None, 'rodzaj męski'), ('paradižnik', 'pomidor', None, 'rodzaj męski'), ('kumara', 'ogórek', None, 'rodzaj żeński'), ('hruška', 'gruszka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('banana', 'banan', None, 'rodzaj żeński'), ('pomaranča', 'pomarańcza', None, 'rodzaj żeński'), ('limona', 'cytryna', None, 'rodzaj żeński'), ('jagoda', 'truskawka', None, 'rodzaj żeński'), ('grozdje', 'winogrono', None, 'rodzaj nijaki'), ('sladkor', 'cukier', None, 'rodzaj męski'), ('sol', 'sól', None, 'rodzaj żeński'), ('poper', 'pieprz', None, 'rodzaj męski'), ('olje', 'olej', None, 'rodzaj nijaki'), ('moka', 'mąka', None, 'rodzaj żeński'), ('med', 'miód', None, 'rodzaj męski'), ('čokolada', 'czekolada', None, 'rodzaj żeński'), ('sladoled', 'lody', None, 'rodzaj męski'), ('torta', 'ciasto (tort)', None, 'rodzaj żeński'), ('piškot', 'ciastko', None, 'rodzaj męski'), ('zajtrk', 'śniadanie', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('kosilo', 'obiad', None, 'rodzaj nijaki'), ('večerja', 'kolacja', None, 'rodzaj żeński'), ('malica', 'przekąska', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('voda', 'woda', None, 'rodzaj żeński'), ('sok', 'sok', None, 'rodzaj męski'), ('pivo', 'piwo', None, 'rodzaj nijaki'), ('vino', 'wino', None, 'rodzaj nijaki'), ('pijača', 'napój', None, 'rodzaj żeński'), ('kozarec', 'szklanka', None, 'rodzaj męski'), ('skodelica', 'filiżanka', None, 'rodzaj żeński'), ('krožnik', 'talerz', None, 'rodzaj męski'), ('nož', 'nóż', None, 'rodzaj męski'), ('vilica', 'widelec', None, 'rodzaj żeński'), ('žlica', 'łyżka', None, 'rodzaj żeński'), ('steklenica', 'butelka', None, 'rodzaj żeński'), ('jedilnik', 'menu', None, 'rodzaj męski'), ('račun', 'rachunek', None, 'rodzaj męski'), ('napitnina', 'napiwek', None, 'rodzaj żeński'), ('miza (w restauracji)', 'stolik', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('natakar', 'kelner', None, 'rodzaj męski'), ('kuhar', 'kucharz', None, 'rodzaj męski'), ('lačen', 'głodny', None, None), ('žejen', 'spragniony', None, None), ('okusen', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('stanovanje', 'mieszkanie', None, 'rodzaj nijaki'), ('soba', 'pokój', None, 'rodzaj żeński'), ('kuhinja', 'kuchnia', None, 'rodzaj żeński'), ('kopalnica', 'łazienka', None, 'rodzaj żeński'), ('spalnica', 'sypialnia', None, 'rodzaj żeński'), ('dnevna soba', 'salon', None, 'rodzaj żeński'), ('vrt', 'ogród', None, 'rodzaj męski'), ('vrata', 'drzwi', None, None), ('okno', 'okno', None, 'rodzaj nijaki'), ('stena', 'ściana', None, 'rodzaj żeński'), ('tla', 'podłoga', None, None), ('streha', 'dach', None, 'rodzaj żeński'), ('stopnice', 'schody', None, None), ('ključ', 'klucz', None, 'rodzaj męski'), ('miza', 'stół', None, 'rodzaj żeński'), ('stol', 'krzesło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('postelja', 'łóżko', None, 'rodzaj żeński'), ('omara', 'szafa', None, 'rodzaj żeński'), ('svetilka', 'lampa', None, 'rodzaj żeński'), ('preproga', 'dywan', None, 'rodzaj żeński'), ('ogledalo', 'lustro', None, 'rodzaj nijaki'), ('televizor', 'telewizor', None, 'rodzaj męski'), ('telefon', 'telefon', None, 'rodzaj męski'), ('računalnik', 'komputer', None, 'rodzaj męski'), ('ura', 'zegar', None, 'rodzaj żeński'), ('blazina', 'poduszka', None, 'rodzaj żeński'), ('odeja', 'koc', None, 'rodzaj żeński'), ('brisača', 'ręcznik', None, 'rodzaj żeński'), ('milo', 'mydło', None, 'rodzaj nijaki'), ('zobna ščetka', 'szczoteczka do zębów', None, 'rodzaj żeński'), ('hladilnik', 'lodówka', None, 'rodzaj męski'), ('peč', 'piec', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('pralni stroj', 'pralka', None, 'rodzaj męski'), ('smeti', 'śmieci', None, None)], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('oblačilo', 'ubranie', None, 'rodzaj nijaki'), ('srajca', 'koszula', None, 'rodzaj żeński'), ('hlače', 'spodnie', None, None), ('obleka', 'sukienka', None, 'rodzaj żeński'), ('krilo', 'spódnica', None, 'rodzaj nijaki'), ('jakna', 'kurtka', None, 'rodzaj żeński'), ('plašč', 'płaszcz', None, 'rodzaj męski'), ('pulover', 'sweter', None, 'rodzaj męski'), ('čevlji', 'buty', None, None), ('nogavice', 'skarpetki', None, None), ('kapa', 'czapka', None, 'rodzaj żeński'), ('klobuk', 'kapelusz', None, 'rodzaj męski'), ('rokavice', 'rękawiczki', None, None), ('šal', 'szalik', None, 'rodzaj męski'), ('torba', 'torba', None, 'rodzaj żeński'), ('nahrbtnik', 'plecak', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('denarnica', 'portfel', None, 'rodzaj żeński'), ('očala', 'okulary', None, None), ('ročna ura', 'zegarek', None, 'rodzaj żeński'), ('prstan', 'pierścionek', None, 'rodzaj męski'), ('spodnje perilo', 'bielizna', None, 'rodzaj nijaki'), ('pižama', 'piżama', None, 'rodzaj żeński'), ('pas', 'pasek', None, 'rodzaj męski'), ('kravata', 'krawat', None, 'rodzaj żeński'), ('obleka (garnitur)', 'garnitur', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('rdeč', 'czerwony', None, None), ('moder', 'niebieski', None, None), ('zelen', 'zielony', None, None), ('rumen', 'żółty', None, None), ('črn', 'czarny', None, None), ('bel', 'biały', None, None), ('siv', 'szary', None, None), ('rjav', 'brązowy', None, None), ('roza', 'różowy', None, None), ('vijoličen', 'fioletowy', None, None), ('barva', 'kolor', None, 'rodzaj żeński'), ('okrogel', 'okrągły', None, None), ('kvadraten', 'kwadratowy', None, None), ('raven', 'prosty', None, None), ('kriv', 'krzywy', None, None), ('črta', 'linia', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('točka', 'punkt', None, 'rodzaj żeński'), ('krog', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('nič', 'zero', None, None), ('enajst', 'jedenaście', None, None), ('dvanajst', 'dwanaście', None, None), ('trinajst', 'trzynaście', None, None), ('štirinajst', 'czternaście', None, None), ('petnajst', 'piętnaście', None, None), ('šestnajst', 'szesnaście', None, None), ('sedemnajst', 'siedemnaście', None, None), ('osemnajst', 'osiemnaście', None, None), ('devetnajst', 'dziewiętnaście', None, None), ('dvajset', 'dwadzieścia', None, None), ('trideset', 'trzydzieści', None, None), ('štirideset', 'czterdzieści', None, None), ('petdeset', 'pięćdziesiąt', None, None), ('šestdeset', 'sześćdziesiąt', None, None), ('sedemdeset', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('osemdeset', 'osiemdziesiąt', None, None), ('devetdeset', 'dziewięćdziesiąt', None, None), ('sto', 'sto', None, None), ('tisoč', 'tysiąc', None, None), ('milijon', 'milion', None, None), ('prvi', 'pierwszy', None, None), ('drugi', 'drugi', None, None), ('tretji', 'trzeci', None, None), ('polovica', 'połowa', None, 'rodzaj żeński'), ('par', 'para', None, 'rodzaj męski'), ('nekaj', 'kilka', None, None), ('veliko', 'wiele', None, None), ('malo', 'mało', None, None), ('ves', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('sekunda', 'sekunda', None, 'rodzaj żeński'), ('minuta', 'minuta', None, 'rodzaj żeński'), ('ura (godzina)', 'godzina', None, 'rodzaj żeński'), ('teden', 'tydzień', None, 'rodzaj męski'), ('mesec', 'miesiąc', None, 'rodzaj męski'), ('leto', 'rok', None, 'rodzaj nijaki'), ('pomlad', 'wiosna', None, 'rodzaj żeński'), ('poletje', 'lato', None, 'rodzaj nijaki'), ('jesen', 'jesień', None, 'rodzaj żeński'), ('zima', 'zima', None, 'rodzaj żeński'), ('ponedeljek', 'poniedziałek', None, 'rodzaj męski'), ('torek', 'wtorek', None, 'rodzaj męski'), ('sreda', 'środa', None, 'rodzaj żeński'), ('četrtek', 'czwartek', None, 'rodzaj męski'), ('petek', 'piątek', None, 'rodzaj męski'), ('sobota', 'sobota', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('nedelja', 'niedziela', None, 'rodzaj żeński'), ('januar', 'styczeń', None, 'rodzaj męski'), ('februar', 'luty', None, 'rodzaj męski'), ('marec', 'marzec', None, 'rodzaj męski'), ('april', 'kwiecień', None, 'rodzaj męski'), ('maj', 'maj', None, 'rodzaj męski'), ('junij', 'czerwiec', None, 'rodzaj męski'), ('julij', 'lipiec', None, 'rodzaj męski'), ('avgust', 'sierpień', None, 'rodzaj męski'), ('september', 'wrzesień', None, 'rodzaj męski'), ('oktober', 'październik', None, 'rodzaj męski'), ('november', 'listopad', None, 'rodzaj męski'), ('december', 'grudzień', None, 'rodzaj męski'), ('poldne', 'południe', None, 'rodzaj nijaki'), ('zvečer', 'wieczorem', None, None), ('vedno', 'zawsze', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('nikoli', 'nigdy', None, None), ('včasih', 'czasem', None, None), ('pogosto', 'często', None, None), ('že', 'już', None, None), ('še', 'jeszcze', None, None), ('kmalu', 'wkrótce', None, None), ('pozneje', 'później', None, None), ('zgodaj', 'wcześnie', None, None), ('pozno', 'późno', None, None), ('kdaj', 'kiedy (pytanie)', None, None), ('datum', 'data', None, 'rodzaj męski'), ('preteklost', 'przeszłość', None, 'rodzaj żeński'), ('prihodnost', 'przyszłość', None, 'rodzaj żeński'), ('rojstni dan', 'urodziny', None, 'rodzaj męski'), ('praznik', 'święto', None, 'rodzaj męski'), ('počitnice', 'wakacje', None, None)], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('sonce', 'słońce', None, 'rodzaj nijaki'), ('luna', 'księżyc', None, 'rodzaj żeński'), ('zvezda', 'gwiazda', None, 'rodzaj żeński'), ('nebo', 'niebo', None, 'rodzaj nijaki'), ('oblak', 'chmura', None, 'rodzaj męski'), ('dež', 'deszcz', None, 'rodzaj męski'), ('sneg', 'śnieg', None, 'rodzaj męski'), ('veter', 'wiatr', None, 'rodzaj męski'), ('nevihta', 'burza', None, 'rodzaj żeński'), ('megla', 'mgła', None, 'rodzaj żeński'), ('led', 'lód', None, 'rodzaj męski'), ('ogenj', 'ogień', None, None), ('zemlja', 'grunt)', None, 'rodzaj żeński'), ('reka', 'rzeka', None, 'rodzaj żeński'), ('jezero', 'jezioro', None, 'rodzaj nijaki'), ('gora', 'góra', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('gozd', 'las', None, 'rodzaj męski'), ('drevo', 'drzewo', None, 'rodzaj nijaki'), ('cvetlica', 'kwiat', None, 'rodzaj żeński'), ('trava', 'trawa', None, 'rodzaj żeński'), ('list', 'liść', None, 'rodzaj męski'), ('polje', 'pole', None, 'rodzaj nijaki'), ('otok', 'wyspa', None, 'rodzaj męski'), ('plaža', 'plaża', None, 'rodzaj żeński'), ('puščava', 'pustynia', None, 'rodzaj żeński'), ('skala', 'skała', None, 'rodzaj żeński'), ('kamen', 'kamień', None, 'rodzaj męski'), ('vreme', 'pogoda', None, 'rodzaj nijaki'), ('temperatura', 'temperatura', None, 'rodzaj żeński'), ('mrzel', 'zimny', None, None), ('topel', 'ciepły', None, None), ('vroč', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('pes', 'pies', None, 'rodzaj męski'), ('mačka', 'kot', None, 'rodzaj żeński'), ('konj', 'koń', None, 'rodzaj męski'), ('krava', 'krowa', None, 'rodzaj żeński'), ('svinja', 'świnia', None, 'rodzaj żeński'), ('ovca', 'owca', None, 'rodzaj żeński'), ('koza', 'koza', None, 'rodzaj żeński'), ('kokoš', 'kura', None, 'rodzaj żeński'), ('raca', 'kaczka', None, 'rodzaj żeński'), ('ptica', 'ptak', None, 'rodzaj żeński'), ('miš', 'mysz', None, 'rodzaj żeński'), ('podgana', 'szczur', None, 'rodzaj żeński'), ('kača', 'wąż', None, 'rodzaj żeński'), ('žaba', 'żaba', None, 'rodzaj żeński'), ('lev', 'lew', None, 'rodzaj męski'), ('tiger', 'tygrys', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('slon', 'słoń', None, 'rodzaj męski'), ('medved', 'niedźwiedź', None, 'rodzaj męski'), ('volk', 'wilk', None, 'rodzaj męski'), ('lisica', 'lis', None, 'rodzaj żeński'), ('zajec', 'zając', None, 'rodzaj męski'), ('jelen', 'jeleń', None, 'rodzaj męski'), ('opica', 'małpa', None, 'rodzaj żeński'), ('metulj', 'motyl', None, 'rodzaj męski'), ('čebela', 'pszczoła', None, 'rodzaj żeński'), ('muha', 'mucha', None, 'rodzaj żeński'), ('pajek', 'pająk', None, 'rodzaj męski'), ('žival', 'zwierzę', None, 'rodzaj żeński'), ('žuželka', 'owad', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('vas', 'wieś', None, 'rodzaj żeński'), ('cesta', 'droga', None, 'rodzaj żeński'), ('trg', 'plac', None, 'rodzaj męski'), ('most', 'most', None, 'rodzaj męski'), ('park', 'park', None, 'rodzaj męski'), ('trgovina', 'sklep', None, 'rodzaj żeński'), ('tržnica', 'targ', None, 'rodzaj żeński'), ('supermarket', 'supermarket', None, 'rodzaj męski'), ('banka', 'bank', None, 'rodzaj żeński'), ('pošta', 'poczta', None, 'rodzaj żeński'), ('bolnišnica', 'szpital', None, 'rodzaj żeński'), ('lekarna', 'apteka', None, 'rodzaj żeński'), ('univerza', 'uniwersytet', None, 'rodzaj żeński'), ('knjižnica', 'biblioteka', None, 'rodzaj żeński'), ('muzej', 'muzeum', None, 'rodzaj męski'), ('cerkev', 'kościół', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('restavracija', 'restauracja', None, 'rodzaj żeński'), ('kavarna', 'kawiarnia', None, 'rodzaj żeński'), ('letališče', 'lotnisko', None, 'rodzaj nijaki'), ('postaja', 'dworzec', None, 'rodzaj żeński'), ('postajališče', 'przystanek', None, 'rodzaj nijaki'), ('kino', 'kino', None, 'rodzaj nijaki'), ('gledališče', 'teatr', None, 'rodzaj nijaki'), ('policija', 'policja', None, 'rodzaj żeński'), ('pisarna', 'biuro', None, 'rodzaj żeński'), ('tovarna', 'fabryka', None, 'rodzaj żeński'), ('zgradba', 'budynek', None, 'rodzaj żeński'), ('stolp', 'wieża', None, 'rodzaj męski'), ('središče', 'centrum', None, 'rodzaj nijaki'), ('naslov', 'adres', None, 'rodzaj męski'), ('zemljevid', 'mapa', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('avto', 'samochód', None, 'rodzaj męski'), ('avtobus', 'autobus', None, 'rodzaj męski'), ('vlak', 'pociąg', None, 'rodzaj męski'), ('tramvaj', 'tramwaj', None, 'rodzaj męski'), ('podzemna železnica', 'metro', None, 'rodzaj żeński'), ('letalo', 'samolot', None, 'rodzaj nijaki'), ('ladja', 'statek', None, 'rodzaj żeński'), ('kolo', 'rower', None, 'rodzaj nijaki'), ('motor', 'motocykl', None, 'rodzaj męski'), ('vozovnica', 'bilet', None, 'rodzaj żeński'), ('potovanje', 'podróż', None, 'rodzaj nijaki'), ('izlet', 'wycieczka', None, 'rodzaj męski'), ('potni list', 'paszport', None, 'rodzaj męski'), ('kovček', 'walizka', None, 'rodzaj męski'), ('bencin', 'benzyna', None, 'rodzaj męski'), ('parkirišče', 'parking', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('križišče', 'skrzyżowanie', None, 'rodzaj nijaki'), ('semafor', 'światła', None, 'rodzaj męski'), ('vozniško dovoljenje', 'prawo jazdy', None, 'rodzaj nijaki'), ('voznik', 'kierowca', None, 'rodzaj męski'), ('potnik', 'pasażer', None, 'rodzaj męski'), ('vhod (wjazd)', 'wjazd', None, 'rodzaj męski'), ('izhod (wyjazd)', 'wyjazd', None, 'rodzaj męski'), ('železnica', 'kolej', None, 'rodzaj żeński'), ('pristanišče', 'port', None, 'rodzaj nijaki'), ('meja', 'granica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('delo', 'praca', None, 'rodzaj nijaki'), ('poklic', 'zawód', None, 'rodzaj męski'), ('zdravnik', 'lekarz', None, 'rodzaj męski'), ('medicinska sestra', 'pielęgniarka', None, 'rodzaj żeński'), ('študent', 'student', None, 'rodzaj męski'), ('inženir', 'inżynier', None, 'rodzaj męski'), ('pravnik', 'prawnik', None, 'rodzaj męski'), ('policist', 'policjant', None, 'rodzaj męski'), ('vojak', 'żołnierz', None, 'rodzaj męski'), ('kmet', 'rolnik', None, 'rodzaj męski'), ('prodajalec', 'sprzedawca', None, 'rodzaj męski'), ('blagajnik', 'kasjer', None, 'rodzaj męski'), ('igralec', 'aktor', None, 'rodzaj męski'), ('pisatelj', 'pisarz', None, 'rodzaj męski'), ('slikar', 'malarz', None, 'rodzaj męski'), ('glasbenik', 'muzyk', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('umetnik', 'artysta', None, 'rodzaj męski'), ('podjetje', 'firma', None, 'rodzaj nijaki'), ('denar', 'pieniądze', None, 'rodzaj męski'), ('plača', 'pensja', None, 'rodzaj żeński'), ('pogodba', 'umowa', None, 'rodzaj żeński'), ('sestanek', 'spotkanie', None, 'rodzaj męski'), ('lekcija', 'lekcja', None, 'rodzaj żeński'), ('izpit', 'egzamin', None, 'rodzaj męski'), ('ocena', 'ocena', None, 'rodzaj żeński'), ('razred', 'klasa', None, 'rodzaj męski'), ('knjiga', 'książka', None, 'rodzaj żeński'), ('zvezek', 'zeszyt', None, 'rodzaj męski'), ('kemični svinčnik', 'długopis', None, 'rodzaj męski'), ('svinčnik', 'ołówek', None, 'rodzaj męski'), ('papir', 'papier', None, 'rodzaj męski'), ('tabla', 'tablica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('slovar', 'słownik', None, 'rodzaj męski'), ('vprašanje', 'pytanie', None, 'rodzaj nijaki'), ('odgovor', 'odpowiedź', None, 'rodzaj męski'), ('naloga', 'zadanie', None, 'rodzaj żeński'), ('test', 'test', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('cena', 'cena', None, 'rodzaj żeński'), ('plačilna kartica', 'karta (płatnicza)', None, 'rodzaj żeński'), ('gotovina', 'gotówka', None, 'rodzaj żeński'), ('kovanec', 'moneta', None, 'rodzaj męski'), ('bankovec', 'banknot', None, 'rodzaj męski'), ('drobiž', 'reszta', None, 'rodzaj męski'), ('popust', 'zniżka', None, 'rodzaj męski'), ('košarica', 'koszyk', None, 'rodzaj żeński'), ('blagajniški račun', 'paragon', None, 'rodzaj męski'), ('blago', 'towar', None, 'rodzaj nijaki'), ('nakup', 'zakup', None, 'rodzaj męski'), ('prodaja', 'sprzedaż', None, 'rodzaj żeński'), ('vrednost', 'wartość', None, 'rodzaj żeński'), ('posojilo', 'kredyt', None, 'rodzaj nijaki'), ('dolg', 'dług', None, 'rodzaj męski'), ('davek', 'podatek', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('bogastvo', 'bogactwo', None, 'rodzaj nijaki'), ('reven', 'biedny', None, None), ('bogat', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('zdravje', 'zdrowie', None, 'rodzaj nijaki'), ('bolezen', 'choroba', None, 'rodzaj żeński'), ('bolečina', 'ból', None, 'rodzaj żeński'), ('vročina', 'gorączka', None, 'rodzaj żeński'), ('kašelj', 'kaszel', None, 'rodzaj męski'), ('smrkavost', 'katar', None, 'rodzaj żeński'), ('zdravilo', 'lekarstwo', None, 'rodzaj nijaki'), ('tableta', 'tabletka', None, 'rodzaj żeński'), ('operacija', 'operacja', None, 'rodzaj żeński'), ('rana', 'rana', None, 'rodzaj żeński'), ('nesreča', 'wypadek', None, 'rodzaj żeński'), ('zdrav', 'zdrowy', None, None), ('bolan', 'chory', None, None), ('utrujen', 'zmęczony', None, None), ('zaspan', 'śpiący', None, None), ('močan', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('šibek', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('veselje', 'radość', None, 'rodzaj nijaki'), ('žalost', 'smutek', None, 'rodzaj żeński'), ('strah', 'strach', None, 'rodzaj męski'), ('jeza', 'gniew', None, 'rodzaj żeński'), ('ljubezen', 'miłość', None, 'rodzaj żeński'), ('sovraštvo', 'nienawiść', None, 'rodzaj nijaki'), ('upanje', 'nadzieja', None, 'rodzaj nijaki'), ('sanje (marzenie)', 'marzenie', None, 'rodzaj żeński'), ('sreča', 'szczęście', None, 'rodzaj żeński'), ('sram', 'wstyd', None, 'rodzaj męski'), ('presenečenje', 'zdziwienie', None, 'rodzaj nijaki'), ('radovednost', 'ciekawość', None, 'rodzaj żeński'), ('potrpežljivost', 'cierpliwość', None, 'rodzaj żeński'), ('pogum', 'odwaga', None, 'rodzaj męski'), ('iskren', 'szczery', None, None), ('prijazen', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('vljuden', 'grzeczny', None, None), ('neumen', 'głupi', None, None), ('len', 'leniwy', None, None), ('delaven', 'pracowity', None, None), ('zanimiv', 'ciekawy', None, None), ('dolgočasen', 'nudny', None, None), ('vesel', 'wesoły', None, None), ('žalosten', 'smutny', None, None), ('jezen', 'zły (rozgniewany)', None, None), ('srečen', 'szczęśliwy', None, None), ('zaljubljen', 'zakochany', None, None), ('osamljen', 'samotny', None, None), ('miren', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('velik', 'duży', None, None), ('majhen', 'mały', None, None), ('kratek', 'krótki', None, None), ('visok', 'wysoki', None, None), ('nizek', 'niski', None, None), ('širok', 'szeroki', None, None), ('ozek', 'wąski', None, None), ('debel', 'gruby', None, None), ('suh', 'chudy', None, None), ('težek', 'ciężki', None, None), ('lahek', 'lekki', None, None), ('hiter', 'szybki', None, None), ('počasen', 'wolny', None, None), ('trd', 'twardy', None, None), ('mehek', 'miękki', None, None), ('moker', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('suh (suchy)', 'suchy', None, None), ('čist', 'czysty', None, None), ('umazan', 'brudny', None, None), ('poln', 'pełny', None, None), ('prazen', 'pusty', None, None), ('oster', 'ostry', None, None), ('glasen', 'głośny', None, None), ('tih', 'cichy', None, None), ('svetel', 'jasny', None, None), ('temen', 'ciemny', None, None), ('mlad', 'młody', None, None), ('star', 'stary', None, None), ('nov', 'nowy', None, None), ('slab', 'zły (niedobry)', None, None), ('lep', 'ładny', None, None), ('grd', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('enostaven', 'łatwy', None, None), ('težaven', 'trudny', None, None), ('pomemben', 'ważny', None, None), ('možen', 'możliwy', None, None), ('resničen', 'prawdziwy', None, None), ('lažen', 'fałszywy', None, None), ('drag', 'drogi', None, None), ('poceni', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('biti', 'być', None, None), ('imeti', 'mieć', None, None), ('delati', 'robić', None, None), ('iti', 'iść', None, None), ('voziti se', 'jechać', None, None), ('priti', 'przyjść', None, None), ('oditi', 'wyjść', None, None), ('vstopiti', 'wejść', None, None), ('vrniti se', 'wrócić', None, None), ('teči', 'biec', None, None), ('stati', 'stać', None, None), ('sedeti', 'siedzieć', None, None), ('ležati', 'leżeć', None, None), ('spati', 'spać', None, None), ('vstati', 'wstać', None, None), ('jesti', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('piti', 'pić', None, None), ('kuhati', 'gotować', None, None), ('umivati', 'myć', None, None), ('oblačiti se', 'ubierać się', None, None), ('govoriti', 'mówić', None, None), ('reči', 'powiedzieć', None, None), ('spraševati', 'pytać', None, None), ('odgovarjati', 'odpowiadać', None, None), ('slišati', 'słyszeć', None, None), ('poslušati', 'słuchać', None, None), ('videti', 'widzieć', None, None), ('gledati', 'patrzeć', None, None), ('brati', 'czytać', None, None), ('pisati', 'pisać', None, None), ('učiti se', 'uczyć się', None, None), ('poučevati', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('razumeti', 'rozumieć', None, None), ('vedeti', 'wiedzieć', None, None), ('poznati', 'znać', None, None), ('misliti', 'myśleć', None, None), ('spominjati se', 'pamiętać', None, None), ('pozabljati', 'zapominać', None, None), ('hoteti', 'chcieć', None, None), ('imeti rad', 'lubić', None, None), ('ljubiti', 'kochać', None, None), ('potrebovati', 'potrzebować', None, None), ('moči', 'móc', None, None), ('morati', 'musieć', None, None), ('dajati', 'dawać', None, None), ('jemati', 'brać', None, None), ('kupovati', 'kupować', None, None), ('prodajati', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('plačevati', 'płacić', None, None), ('odpirati', 'otwierać', None, None), ('zapirati', 'zamykać', None, None), ('začenjati', 'zaczynać', None, None), ('končevati', 'kończyć', None, None), ('delati (pracować)', 'pracować', None, None), ('igrati', 'grać', None, None), ('peti', 'śpiewać', None, None), ('plesati', 'tańczyć', None, None), ('plavati', 'pływać', None, None), ('leteti', 'latać', None, None), ('polagati', 'kłaść', None, None), ('iskati', 'szukać', None, None), ('najti', 'znajdować', None, None), ('čakati', 'czekać', None, None), ('pomagati', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('prositi', 'prosić', None, None), ('opravičevati se', 'przepraszać', None, None), ('dovoljevati', 'pozwalać', None, None), ('poskušati', 'próbować', None, None), ('spreminjati', 'zmieniać', None, None), ('nositi', 'nosić', None, None), ('držati', 'trzymać', None, None), ('metati', 'rzucać', None, None), ('loviti', 'łapać', None, None), ('tepsti', 'bić', None, None), ('ubijati', 'zabijać', None, None), ('umirati', 'umierać', None, None), ('živeti', 'żyć', None, None), ('stanovati', 'mieszkać', None, None), ('srečevati', 'spotykać', None, None), ('telefonirati', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('pošiljati', 'wysyłać', None, None), ('dobivati', 'dostawać', None, None), ('kazati', 'pokazywać', None, None), ('vabiti', 'zapraszać', None, None), ('obiskovati', 'odwiedzać', None, None), ('jokati', 'płakać', None, None), ('smejati se', 'śmiać się', None, None), ('nasmihati se', 'uśmiechać się', None, None), ('bati se', 'bać się', None, None), ('veseliti se', 'cieszyć się', None, None), ('verjeti', 'wierzyć', None, None), ('strinjati se', 'zgadzać się', None, None), ('izbirati', 'wybierać', None, None), ('odločati', 'decydować', None, None), ('šteti', 'liczyć', None, None), ('tehtati', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('hoditi', 'chodzić', None, None), ('voziti', 'jeździć', None, None), ('vstopati', 'wsiadać', None, None), ('izstopati', 'wysiadać', None, None), ('zavijati', 'skręcać', None, None), ('ustavljati se', 'zatrzymywać się', None, None), ('zamujati', 'spóźniać się', None, None), ('muditi se', 'spieszyć się', None, None), ('počivati', 'odpoczywać', None, None), ('zabavati se', 'bawić się', None, None), ('risati', 'rysować', None, None), ('graditi', 'budować', None, None), ('popravljati', 'naprawiać', None, None), ('rezati', 'ciąć', None, None), ('cvreti', 'smażyć', None, None), ('peči', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('mešati', 'mieszać', None, None), ('točiti', 'nalewać', None, None), ('pospravljati', 'sprzątać', None, None), ('prati', 'prać', None, None), ('likati', 'prasować', None, None), ('briti se', 'golić się', None, None), ('česati', 'czesać', None, None), ('kopati se', 'kąpać się', None, None), ('prebujati se', 'budzić się', None, None), ('zaspati', 'zasypiać', None, None), ('sanjariti', 'marzyć', None, None), ('sanjati', 'śnić', None, None), ('vaditi', 'ćwiczyć', None, None), ('trenirati', 'trenować', None, None), ('zmagovati', 'wygrywać', None, None), ('izgubljati', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('premikati', 'ruszać', None, None), ('vleči', 'ciągnąć', None, None), ('potiskati', 'pchać', None, None), ('dvigati', 'podnosić', None, None), ('padati', 'spadać', None, None), ('skakati', 'skakać', None, None), ('plezati', 'wspinać się', None, None), ('skrivati', 'ukrywać', None, None), ('krasti', 'kraść', None, None), ('vračati', 'oddawać', None, None), ('posojati', 'pożyczać', None, None), ('zapravljati', 'wydawać', None, None), ('varčevati', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('ta', 'ten', None, None), ('tisti', 'tamten', None, None), ('kako', 'jak', None, None), ('zakaj', 'dlaczego', None, None), ('kaj', 'co', None, None), ('kdo', 'kto', None, None), ('kateri', 'który', None, None), ('kakšen', 'jaki', None, None), ('ampak', 'ale', None, None), ('ali', 'lub', None, None), ('ker', 'bo', None, None), ('če', 'jeśli', None, None), ('torej', 'więc', None, None), ('tudi', 'też', None, None), ('samo', 'tylko', None, None), ('malo (trochę)', 'trochę', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('veliko (dużo)', 'dużo', None, None), ('vse', 'wszystko', None, None), ('nič (nic)', 'nic', None, None), ('nekaj (coś)', 'coś', None, None), ('nekdo', 'ktoś', None, None), ('nihče', 'nikt', None, None), ('vsak', 'każdy', None, None), ('drug', 'inny', None, None), ('isti', 'ten sam', None, None), ('morda', 'może (być)', None, None), ('zagotovo', 'na pewno', None, None), ('skupaj', 'razem', None, None), ('sam', 'sam', None, None), ('brez', 'bez', None, None), ('z', 'z (towarzysząc)', None, None), ('na', 'na (powierzchni)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('do', 'do (kierunek)', None, None), ('od', 'od', None, None), ('za', 'dla', None, None), ('skozi', 'przez', None, None), ('po', 'po (czas)', None, None), ('pred', 'przed', None, None), ('za (z tyłu)', 'za (z tyłu)', None, None), ('nad', 'nad', None, None), ('pod', 'pod', None, None), ('poleg', 'obok', None, None), ('proti', 'przeciw', None, None), ('o', 'o (temat)', None, None), ('pri', 'u (przy)', None, None), ('okoli', 'około', None, None), ('skoraj', 'prawie', None, None), ('celo', 'nawet', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('še enkrat', 'jeszcze raz', None, None), ('zdaj', 'teraz', None, None), ('takrat', 'wtedy', None, None), ('nekje', 'gdzieś', None, None), ('nikjer', 'nigdzie', None, None), ('povsod', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('življenje', 'życie', None, 'rodzaj nijaki'), ('smrt', 'śmierć', None, 'rodzaj żeński'), ('svet', 'świat', None, 'rodzaj męski'), ('dežela', 'kraj', None, 'rodzaj żeński'), ('država', 'państwo', None, 'rodzaj żeński'), ('govor', 'język (mowa)', None, 'rodzaj męski'), ('beseda', 'słowo', None, 'rodzaj żeński'), ('stavek', 'zdanie', None, 'rodzaj męski'), ('ime', 'imię', None, 'rodzaj nijaki'), ('priimek', 'nazwisko', None, 'rodzaj męski'), ('starost', 'wiek', None, 'rodzaj żeński'), ('zgodovina', 'historia', None, 'rodzaj żeński'), ('kultura', 'kultura', None, 'rodzaj żeński'), ('vera', 'religia', None, 'rodzaj żeński'), ('Bog', 'Bóg', None, 'rodzaj męski'), ('vojna', 'wojna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('mir', 'pokój (brak wojny)', None, 'rodzaj męski'), ('zakon', 'prawo (przepis)', None, 'rodzaj męski'), ('svoboda', 'wolność', None, 'rodzaj żeński'), ('oblast', 'władza', None, 'rodzaj żeński'), ('vlada', 'rząd', None, 'rodzaj żeński'), ('volitve', 'wybory', None, None), ('problem', 'problem', None, 'rodzaj męski'), ('zamisel', 'pomysł', None, 'rodzaj żeński'), ('razlog', 'powód', None, 'rodzaj męski'), ('rezultat', 'wynik', None, 'rodzaj męski'), ('način', 'sposób', None, 'rodzaj męski'), ('začetek', 'początek', None, 'rodzaj męski'), ('konec', 'koniec', None, 'rodzaj męski'), ('del', 'część', None, 'rodzaj męski'), ('kraj', 'miejsce', None, 'rodzaj męski'), ('stvar', 'rzecz', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('zadeva', 'sprawa', None, 'rodzaj żeński'), ('informacija', 'informacja', None, 'rodzaj żeński'), ('sporočilo', 'wiadomość', None, 'rodzaj nijaki'), ('pismo', 'list', None, 'rodzaj nijaki'), ('časopis', 'gazeta', None, 'rodzaj męski'), ('film', 'film', None, 'rodzaj męski'), ('glasba', 'muzyka', None, 'rodzaj żeński'), ('pesem', 'piosenka', None, 'rodzaj żeński'), ('slika', 'obraz', None, 'rodzaj żeński'), ('igra', 'gra', None, 'rodzaj żeński'), ('šport', 'sport', None, 'rodzaj męski'), ('tekma', 'mecz', None, 'rodzaj żeński'), ('ekipa', 'drużyna', None, 'rodzaj żeński'), ('žoga', 'piłka', None, 'rodzaj żeński'), ('zabava', 'zabawa', None, 'rodzaj żeński'), ('zabava (impreza)', 'impreza', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('darilo', 'prezent', None, 'rodzaj nijaki'), ('sen', 'sen', None, 'rodzaj męski'), ('načrt', 'plan', None, 'rodzaj męski'), ('izbira', 'wybór', None, 'rodzaj żeński'), ('napaka', 'błąd', None, 'rodzaj żeński'), ('resnica', 'prawda', None, 'rodzaj żeński'), ('laž', 'kłamstwo', None, 'rodzaj żeński'), ('skrivnost', 'tajemnica', None, 'rodzaj żeński'), ('moč', 'siła', None, 'rodzaj żeński'), ('energija', 'energia', None, 'rodzaj żeński'), ('svetloba', 'światło', None, 'rodzaj żeński'), ('zvok', 'dźwięk', None, 'rodzaj męski'), ('tišina', 'cisza', None, 'rodzaj żeński'), ('gibanje', 'ruch', None, 'rodzaj nijaki'), ('sprememba', 'zmiana', None, 'rodzaj żeński'), ('razlika', 'różnica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('primer', 'przykład', None, 'rodzaj męski'), ('celota', 'całość', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, 'rodzaj męski'), ('e-pošta', 'e-mail', None, 'rodzaj żeński'), ('geslo', 'hasło', None, 'rodzaj nijaki'), ('spletna stran', 'strona internetowa', None, 'rodzaj żeński'), ('program', 'program', None, 'rodzaj męski'), ('aplikacija', 'aplikacja', None, 'rodzaj żeński'), ('zaslon', 'ekran', None, 'rodzaj męski'), ('tipkovnica', 'klawiatura', None, 'rodzaj żeński'), ('računalniška miška', 'myszka komputerowa', None, 'rodzaj żeński'), ('datoteka', 'plik', None, 'rodzaj żeński'), ('fotografija', 'zdjęcie', None, 'rodzaj żeński'), ('kamera', 'kamera', None, 'rodzaj żeński'), ('baterija', 'bateria', None, 'rodzaj żeński'), ('elektrika', 'prąd', None, 'rodzaj żeński'), ('kabel', 'kabel', None, 'rodzaj męski'), ('stroj', 'maszyna', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('orodje', 'narzędzie', None, 'rodzaj nijaki'), ('kladivo', 'młotek', None, 'rodzaj nijaki'), ('tiskalnik', 'drukarka', None, 'rodzaj męski'), ('polnilec', 'ładowarka', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('sever', 'północ', None, 'rodzaj męski'), ('jug', 'południe (kierunek)', None, 'rodzaj męski'), ('vzhod', 'wschód', None, 'rodzaj męski'), ('zahod', 'zachód', None, 'rodzaj męski'), ('Poljska', 'Polska', None, 'rodzaj żeński'), ('Evropa', 'Europa', None, 'rodzaj żeński'), ('Nemčija', 'Niemcy', None, 'rodzaj żeński'), ('Francija', 'Francja', None, 'rodzaj żeński'), ('Italija', 'Włochy', None, 'rodzaj żeński'), ('Španija', 'Hiszpania', None, 'rodzaj żeński'), ('Rusija', 'Rosja', None, 'rodzaj żeński'), ('Anglija', 'Anglia', None, 'rodzaj żeński'), ('Amerika', 'Ameryka', None, 'rodzaj żeński'), ('Kitajska', 'Chiny', None, 'rodzaj żeński'), ('Japonska', 'Japonia', None, 'rodzaj żeński'), ('Afrika', 'Afryka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('Azija', 'Azja', None, 'rodzaj żeński'), ('celina', 'kontynent', None, 'rodzaj żeński'), ('glavno mesto', 'stolica', None, 'rodzaj nijaki'), ('državljan', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('kos', 'kawałek', None, 'rodzaj męski'), ('kaplja', 'kropla', None, 'rodzaj żeński'), ('škatla', 'pudełko', None, 'rodzaj żeński'), ('vreča', 'worek', None, 'rodzaj żeński'), ('nit', 'nić', None, 'rodzaj żeński'), ('žica', 'drut', None, 'rodzaj żeński'), ('igla', 'igła', None, 'rodzaj żeński'), ('škarje', 'nożyczki', None, None), ('palica', 'kij', None, 'rodzaj żeński'), ('vrv', 'lina', None, 'rodzaj żeński'), ('veriga', 'łańcuch', None, 'rodzaj żeński'), ('vijak', 'śruba', None, 'rodzaj męski'), ('žebelj', 'gwóźdź', None, 'rodzaj męski'), ('lepilo', 'klej', None, 'rodzaj nijaki'), ('barva (farba)', 'farba', None, 'rodzaj żeński'), ('steklo', 'szkło', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('les', 'drewno', None, 'rodzaj męski'), ('kovina', 'metal', None, 'rodzaj żeński'), ('zlato', 'złoto', None, 'rodzaj nijaki'), ('srebro', 'srebro', None, 'rodzaj nijaki'), ('železo', 'żelazo', None, 'rodzaj nijaki'), ('plastika', 'plastik', None, 'rodzaj żeński'), ('usnje', 'skóra (materiał)', None, 'rodzaj nijaki'), ('bombaž', 'bawełna', None, 'rodzaj męski'), ('volna', 'wełna', None, 'rodzaj żeński'), ('pesek', 'piasek', None, 'rodzaj męski'), ('blato', 'błoto', None, 'rodzaj nijaki'), ('prah', 'kurz', None, 'rodzaj męski'), ('dim', 'dym', None, 'rodzaj męski'), ('para', 'para (wodna)', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('zgoraj', 'góra (kierunek)', None, None), ('spodaj', 'dół', None, None), ('spredaj', 'przód', None, None), ('zadaj', 'tył', None, None), ('sredina', 'środek', None, 'rodzaj żeński'), ('stran', 'bok', None, 'rodzaj żeński'), ('znotraj', 'wewnątrz', None, None), ('zunaj', 'na zewnątrz', None, None), ('daleč', 'daleko', None, None), ('blizu', 'blisko', None, None), ('visoko', 'wysoko', None, None), ('nizko', 'nisko', None, None), ('hitro', 'szybko', None, None), ('počasi', 'wolno', None, None), ('slabo', 'źle', None, None), ('težko', 'trudno', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('posebej', 'osobno', None, None), ('nasproti', 'naprzeciw', None, None), ('vzdolž', 'wzdłuż', None, None), ('počez', 'w poprzek', None, None), ('naokrog', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('zelje', 'kapusta', None, 'rodzaj nijaki'), ('grah', 'groszek', None, 'rodzaj męski'), ('fižol', 'fasola', None, 'rodzaj męski'), ('goba', 'grzyb', None, 'rodzaj żeński'), ('oreh', 'orzech', None, 'rodzaj męski'), ('sliva', 'śliwka', None, 'rodzaj żeński'), ('češnja', 'wiśnia', None, 'rodzaj żeński'), ('breskev', 'brzoskwinia', None, 'rodzaj żeński'), ('lubenica', 'arbuz', None, 'rodzaj żeński'), ('malina', 'malina', None, 'rodzaj żeński'), ('klobasa', 'kiełbasa', None, 'rodzaj żeński'), ('šunka', 'szynka', None, 'rodzaj żeński'), ('žemlja', 'bułka', None, 'rodzaj żeński'), ('sendvič', 'kanapka', None, 'rodzaj męski'), ('palačinka', 'naleśnik', None, 'rodzaj żeński'), ('jogurt', 'jogurt', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('smetana', 'śmietana', None, 'rodzaj żeński'), ('omaka', 'sos', None, 'rodzaj żeński'), ('kis', 'ocet', None, 'rodzaj męski'), ('kvas', 'drożdże', None, 'rodzaj męski'), ('žele (kisiel)', 'kisiel', None, 'rodzaj męski'), ('žele', 'galaretka', None, 'rodzaj męski'), ('rozina', 'rodzynek', None, 'rodzaj żeński'), ('mandelj', 'migdał', None, 'rodzaj męski'), ('peteršilj', 'pietruszka', None, 'rodzaj męski'), ('koper', 'koperek', None, 'rodzaj męski'), ('paprika', 'papryka', None, 'rodzaj żeński'), ('zelena solata', 'sałata', None, 'rodzaj żeński'), ('špinača', 'szpinak', None, 'rodzaj żeński'), ('pesa', 'burak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('tast', 'teść', None, 'rodzaj męski'), ('tašča', 'teściowa', None, 'rodzaj żeński'), ('svak', 'szwagier', None, 'rodzaj męski'), ('nečak', 'bratanek', None, 'rodzaj męski'), ('nečakinja', 'siostrzenica', None, 'rodzaj żeński'), ('sirota', 'sierota', None, 'rodzaj żeński'), ('vdova', 'wdowa', None, 'rodzaj żeński'), ('zaročenec', 'narzeczony', None, 'rodzaj męski'), ('poroka', 'ślub', None, 'rodzaj żeński'), ('razveza', 'rozwód', None, 'rodzaj żeński'), ('rojstvo', 'urodzenie', None, 'rodzaj nijaki'), ('pogreb', 'pogrzeb', None, 'rodzaj męski'), ('frizer', 'fryzjer', None, 'rodzaj męski'), ('pek', 'piekarz', None, 'rodzaj męski'), ('mesar', 'rzeźnik', None, 'rodzaj męski'), ('natakarica', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('poštar', 'listonosz', None, 'rodzaj męski'), ('gasilec', 'strażak', None, 'rodzaj męski'), ('sodnik', 'sędzia', None, 'rodzaj męski'), ('direktor', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
