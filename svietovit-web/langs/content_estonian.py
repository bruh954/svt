"""Treść kursu: estoński dla Polaków."""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "HÄÄL · WYMOWA", "jezyk": "KEEL · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "Õ", "track": "wymowa",
     "letters": [
         ("õ", "[ɤ]: nie ma odpowiednika w polskim; coś między y a o, usta niezaokrąglone", "põld (pole)"),
         ("ä", "[æ]: szerokie e, jak w ang. „cat”", "päev (dzień)"),
         ("ö", "[ø]: jak niemieckie ö: o z ustami ułożonymi do e", "töö (praca)"),
         ("ü", "[y]: jak niemieckie ü: u z ustami ułożonymi do i", "tüdruk (dziewczynka)"),
         ("š", "[ʃ]: jak polskie sz (w słowach obcych)", "šokolaad (czekolada)"),
         ("ž", "[ʒ]: jak polskie ż (w słowach obcych)", "žest (gest)"),
         ("h", "[h]: lekkie, wymawiaj zawsze", "hea (dobry)"),
         ("j", "[j]: jak polskie j", "jah (tak)"),
         ("v", "[ʋ]: jak polskie w", "vesi (woda)"),
         ("r", "[r]: toczone, jak polskie", "raamat (książka)"),
         ("aa, ee, ii, oo, uu", "długa samogłoska: wymawiasz ją dwa razy dłużej", "maa (kraj)"),
         ("k, p, t", "[k], [p], [t]: bez dmuchnięcia, jak polskie, czasem brzmią jak g, b, d", "tuba (pokój)"),
         ("pojedyncze i podwójne spółgłoski", "dłuższa spółgłoska zmienia znaczenie słowa", "kala (ryba)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "T", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("tere", "cześć", None, None),
         ("nägemist", "do widzenia", None, "Dosł. „do zobaczenia”.", ),
         ("aitäh", "dziękuję", None, None),
         ("palun", "proszę", None, None),
         ("jah", "tak", None, None),
         ("ei", "nie", None, None),
         ("head", "dobre; dobrego", None, None),
         ("ööd", "nocy", None, None),
         ("hommikust", "rano (dzień dobry rano)", None, None),
         ("vabandust", "przepraszam", None, None),
         ("väga", "bardzo", None, None),
         ("ja", "i", None, None),
         ("okei", "dobrze; ok", "okej", None),
     ],
     "sentences": [
         (["tere", "!"], "Cześć!", {"nägemist": "nägemist to „do widzenia”."}),
         (["nägemist", "!"], "Do widzenia!", {"tere": "tere to „cześć”."}),
         (["tere", "hommikust", "!"], "Dzień dobry (rano)!", {"ööd": "ööd to „nocy”."}),
         (["head", "ööd", "!"], "Dobranoc!", {"hommikust": "hommikust to „rano”."}),
         (["aitäh", "!"], "Dziękuję!", {"palun": "palun to „proszę”. Tu dziękujesz."}),
         (["jah", ",", "aitäh"], "Tak, dziękuję.", {"ei": "ei to „nie”."}),
         (["ei", ",", "aitäh"], "Nie, dziękuję.", {"jah": "jah to „tak”."}),
         (["vabandust", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "M", "track": "jezyk",
     "words": [
         ("mina", "ja", None, None),
         ("sina", "ty", None, None),
         ("tema", "on; ona", None, "Nie ma rodzaju: „tema” znaczy on i ona."),
         ("olen", "jestem", None, None),
         ("oled", "jesteś", None, None),
         ("on", "jest", None, None),
         ("õpilane", "uczeń; student", None, None),
         ("õpetaja", "nauczyciel", None, None),
         ("poolakas", "Polak", None, None),
         ("poolatar", "Polka", None, None),
         ("pärit", "pochodzący", None, None),
         ("Poolast", "z Polski", None, "Końcówka -st = „z”."),
         ("Eestist", "z Estonii", None, "Końcówka -st = „z”."),
     ],
     "sentences": [
         (["mina", "olen", "õpilane"], "Jestem uczniem.", {"oled": "oled to „jesteś”. O sobie: olen."}),
         (["sina", "oled", "õpetaja"], "Jesteś nauczycielem.", {"olen": "olen to „jestem”. Do „sina”: oled."}),
         (["tema", "on", "poolakas"], "On jest Polakiem.", {"poolatar": "Dla mężczyzny: poolakas."}),
         (["tema", "on", "poolatar"], "Ona jest Polką.", {"poolakas": "Dla kobiety: poolatar."}),
         (["mina", "olen", "pärit", "Poolast"], "Jestem z Polski.", {"Eestist": "Eestist to „z Estonii”."}),
         (["tema", "on", "pärit", "Eestist"], "On jest z Estonii.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "E", "track": "jezyk",
     "words": [
         ("ema", "mama", None, None),
         ("isa", "tata", None, None),
         ("vend", "brat", None, None),
         ("õde", "siostra", None, None),
         ("laps", "dziecko", None, None),
         ("sõber", "przyjaciel", None, None),
         ("naine", "kobieta", None, None),
         ("mees", "mężczyzna", None, None),
         ("minu", "mój; moja", None, "Estoński nie ma rodzaju."),
         ("sinu", "twój; twoja", None, None),
         ("mul", "u mnie (mam)", None, "„Mul on vend” = mam brata."),
         ("sul", "u ciebie (masz)", None, None),
         ("väike", "mały", None, None),
         ("hea", "dobry", None, None),
     ],
     "sentences": [
         (["minu", "vend", "on", "väike"], "Mój brat jest mały.", {"sinu": "sinu to „twój”. O sobie: minu."}),
         (["minu", "õde", "on", "hea"], "Moja siostra jest dobra.", {}),
         (["minu", "ema", "on", "naine"], "Moja mama jest kobietą.", {}),
         (["mul", "on", "vend"], "Mam brata.", {"sul": "sul to „u ciebie”. O sobie: mul."}),
         (["sul", "on", "õde"], "Masz siostrę.", {"mul": "mul to „u mnie”. Do „sina”: sul."}),
         (["isa", "on", "mees"], "Tata jest mężczyzną.", {}),
         (["minu", "sõber", "on", "hea"], "Mój przyjaciel jest dobry.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "K", "track": "jezyk",
     "words": [
         ("vesi", "woda", None, None),
         ("vett", "wodę", None, "Cząstkowy (partitiiv): po „tahan”."),
         ("kohv", "kawa", None, None),
         ("kohvi", "kawę", None, "Partitiiv."),
         ("tee", "herbata", None, None),
         ("teed", "herbatę", None, "Partitiiv."),
         ("leib", "chleb", None, None),
         ("leiba", "chleb (partitiiv)", None, None),
         ("kala", "ryba", None, None),
         ("õun", "jabłko", None, None),
         ("õuna", "jabłko (partitiiv)", None, None),
         ("tahan", "chcę", None, None),
         ("tahad", "chcesz", None, None),
         ("maitsev", "smaczny", None, None),
         ("nüüd", "teraz", None, None),
     ],
     "sentences": [
         (["mina", "tahan", "kohvi"], "Chcę kawę.", {"tahad": "tahad to „chcesz”. O sobie: tahan."}),
         (["sina", "tahad", "teed"], "Chcesz herbatę.", {"tahan": "tahan to „chcę”. Do „sina”: tahad."}),
         (["mina", "tahan", "leiba"], "Chcę chleb.", {}),
         (["sina", "tahad", "õuna"], "Chcesz jabłko.", {}),
         (["kala", "on", "väga", "maitsev"], "Ryba jest bardzo smaczna.", {}),
         (["nüüd", "tahan", "vett"], "Teraz chcę wodę.", {}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("kaks", "dwa", None, None),
         ("kolm", "trzy", None, None),
         ("neli", "cztery", None, None),
         ("viis", "pięć", None, None),
         ("kümme", "dziesięć", None, None),
         ("last", "dzieci (partitiiv)", None, "Po liczbie: partitiiv."),
         ("täna", "dziś", None, None),
         ("homme", "jutro", None, None),
         ("eile", "wczoraj", None, None),
         ("kell", "godzina; zegar", None, None),
         ("mis", "co; jaki", None, None),
     ],
     "sentences": [
         (["mul", "on", "kaks", "last"], "Mam dwoje dzieci.", {}),
         (["mina", "tahan", "kolm", "õuna"], "Chcę trzy jabłka.", {"kaks": "kaks to „dwa”. Chcesz trzy: kolm."}),
         (["mis", "kell", "on", "?"], "Która jest godzina?", {}),
         (["kell", "on", "kümme"], "Jest dziesiąta.", {"viis": "viis to „pięć”."}),
         (["täna", "tahan", "kohvi"], "Dziś chcę kawę.", {"homme": "homme to „jutro”. Tu „dziś”: täna."}),
         (["homme", "tahan", "kala"], "Jutro chcę rybę.", {"eile": "eile to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "L", "track": "jezyk",
     "words": [
         ("kodu", "dom", None, None),
         ("koju", "do domu", None, None),
         ("linn", "miasto", None, None),
         ("tänav", "ulica", None, None),
         ("kool", "szkoła", None, None),
         ("meri", "morze", None, None),
         ("takso", "taksówka", "taksówka", None),
         ("hotell", "hotel", "hotel", None),
         ("kus", "gdzie", None, None),
         ("siin", "tu", None, None),
         ("seal", "tam", None, None),
         ("lähen", "idę; jadę", None, None),
         ("Tallinna", "do Tallina", None, "Końcówka -sse/-a = „do”."),
         ("paremal", "po prawej", None, None),
         ("vasakul", "po lewej", None, None),
     ],
     "sentences": [
         (["kus", "on", "hotell", "?"], "Gdzie jest hotel?", {"siin": "siin to „tu”. Pytasz „gdzie”: kus."}),
         (["hotell", "on", "seal"], "Hotel jest tam.", {"siin": "siin to „tu”. Tu „tam”: seal."}),
         (["mina", "lähen", "koju"], "Idę do domu.", {}),
         (["mina", "lähen", "Tallinna"], "Jadę do Tallina.", {}),
         (["takso", "on", "paremal"], "Taksówka jest po prawej.", {"vasakul": "vasakul to „po lewej”."}),
         (["kool", "on", "seal"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Trzy długości", "chain": [],
                "text": "Estoński ma trzy długości głosek: krótką, długą i bardzo długą. Dłuższa głoska zmienia słowo. Samogłoski ä, ö, ü, õ są osobnymi literami, a õ nie ma odpowiednika po polsku."}],
    "ja": [{"title": "Brak rodzaju", "chain": [
                ("On jest Polakiem.", ["tema", "on", "poolakas"], "„tema” = on lub ona."),
                ("Ona jest Polką.", ["tema", "on", "poolatar"], "Ten sam zaimek."),
            ],
            "text": "Po estońsku nie ma rodzaju ani rodzajników. „Tema” znaczy on i ona. Czasownik „być”: olen, oled, on."}],
    "ludzie": [{"title": "Mam = u mnie jest", "chain": [],
                "text": "Nie ma czasownika „mieć”. Mówisz „u mnie jest”: mul on vend (mam brata), sul on õde (masz siostrę)."}],
    "jedzenie": [{"title": "Partitiiv", "chain": [],
                  "text": "Po „chcę” rzeczownik dostaje formę cząstkową (partitiiv): kohv → kohvi, tee → teed, vesi → vett. Uczysz się jej razem ze słowem."}],
}

ENDINGS_INSIGHT = {"title": "Formy osobowe",
                   "text": "Po estońsku czasownik zmienia końcówkę: olen, oled, on; tahan, tahad. Tu to ćwiczysz."}

ENDINGS = [
    ("mina ", "ol", "en", " õpilane", ["en", "ed"], "ja jestem", "Do „mina” pasuje -en.", "ja"),
    ("sina ", "ol", "ed", " õpetaja", ["en", "ed"], "ty jesteś", "Do „sina” pasuje -ed.", "ja"),
    ("mina ", "tah", "an", " kohvi", ["an", "ad"], "ja chcę", "Do „mina” pasuje -an.", "jedzenie"),
    ("sina ", "tah", "ad", " teed", ["an", "ad"], "ty chcesz", "Do „sina” pasuje -ad.", "jedzenie"),
    ("", "", "minu", " vend", ["minu", "sinu"], "mój", "minu to „mój”, sinu to „twój”.", "ludzie"),
    ("", "", "sinu", " õde", ["minu", "sinu"], "twój", "sinu to „twój”.", "ludzie"),
    ("", "", "mul", " on vend", ["mul", "sul"], "u mnie", "mul to „u mnie”.", "ludzie"),
    ("", "", "sul", " on õde", ["mul", "sul"], "u ciebie", "sul to „u ciebie”.", "ludzie"),
    ("mina ", "", "olen", " pärit Poolast", ["olen", "oled"], "ja jestem", "Do „mina” pasuje olen.", "ja"),
]

CHAT_EXTRA = {"Mari": "Mari (imię)", "Jaan": "Jaan (imię)", "taksojuht": "kierowca", "kuhu": "dokąd", "lähed": "idziesz; jedziesz"}

CHATS = [
    {"id": "kohvik", "title": "W kawiarni", "partner": "Mari", "avatar": "M", "requires": "jedzenie",
     "turns": [
         {"bot": ["tere", "hommikust", "!"], "en": "Dzień dobry!",
          "options": [(["tere", "hommikust", "!"], True, None), (["head", "ööd", "!"], False, "head ööd to „dobranoc”. Jest rano.")]},
         {"bot": ["kohvi", "?"], "en": "Kawy?",
          "options": [(["jah", ",", "mina", "tahan", "kohvi"], True, None),
                      (["jah", ",", "sina", "tahad", "kohvi"], False, "tahad jest do „sina”. O sobie: tahan.")]},
         {"bot": ["ja", "leiba", "?"], "en": "I chleba?",
          "options": [(["ei", ",", "aitäh"], True, None),
                      (["palun", "!"], False, "palun to „proszę”. Odmów: ei, aitäh.")]},
         {"bot": ["okei", "!"], "build": (["aitäh", "!"], "Dziękuję!"), "en": "Dobrze!"},
     ]},
    {"id": "tutvus", "title": "Poznajemy się", "partner": "Jaan", "avatar": "J", "requires": "ludzie",
     "turns": [
         {"bot": ["tere", "!"], "en": "Cześć!",
          "options": [(["tere", "!"], True, None), (["vabandust", "!"], False, "vabandust to „przepraszam”. Powitaj: tere.")]},
         {"bot": ["sina", "oled", "pärit", "Eestist", "?"], "en": "Jesteś z Estonii?",
          "options": [(["ei", ",", "mina", "olen", "pärit", "Poolast"], True, None),
                      (["ei", ",", "mina", "oled", "pärit", "Poolast"], False, "oled jest do „sina”. O sobie: olen.")]},
         {"bot": ["sul", "on", "vend", "?"], "en": "Masz brata?",
          "options": [(["jah", ",", "mul", "on", "vend"], True, None),
                      (["jah", ",", "sul", "on", "vend"], False, "sul to „u ciebie”. O sobie: mul.")]},
         {"bot": ["nägemist", "!"], "build": (["nägemist", "!"], "Do widzenia!"), "en": "Do widzenia!"},
     ]},
    {"id": "takso", "title": "W taksówce", "partner": "taksojuht", "avatar": "T", "requires": "miejsca",
     "turns": [
         {"bot": ["tere", "hommikust", "!"], "en": "Dzień dobry!",
          "options": [(["tere", "hommikust", "!"], True, None), (["head", "ööd", "!"], False, "head ööd to „dobranoc”. Jest rano.")]},
         {"bot": ["kuhu", "sina", "lähed", "?"], "en": "Dokąd jedziesz?",
          "options": [(["mina", "lähen", "Tallinna"], True, None),
                      (["mina", "lähed", "Tallinna"], False, "lähed to „idziesz”. O sobie: lähen.")]},
         {"bot": ["hotell", "on", "seal", "."], "en": "Hotel jest tam.",
          "options": [(["paremal", "?"], True, None), (["siin", "?"], False, "Pytasz o kierunek: paremal.")]},
         {"bot": ["jah", "!"], "build": (["aitäh", "!"], "Dziękuję!"), "en": "Tak!"},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['mina', 'sina', 'tema', 'meie', 'teie', 'nemad'],
    'przyp': ['nimetav (kto? co?)', 'omastav (czyj?)', 'osastav (kogo? czego?)'],
    'miejsc': ['sisseütlev (do środka)', 'seesütlev (w)', 'seestütlev (ze środka)', 'alaleütlev (na, do)', 'alalütlev (na, u)', 'alaltütlev (z, od)'],
    'im': ['-v (czynny teraźniejszy)', '-nud (czynny przeszły)', '-tav (bierny teraźniejszy)', '-tud (bierny przeszły)'],
    't_osastav': ['raamat (książka)', 'vesi (woda)', 'laps (dziecko)', 'kool (szkoła)', 'käsi (ręka)', 'mees (mężczyzna)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'elama (żyć, mieszkać)', 'os', 'elan; elad; elab; elame; elate; elavad', 'Końcówki: -n, -d, -b, -me, -te, -vad.'),
    ('conj', 'Wzory koniugacji', 'tahtma (chcieć)', 'os', 'tahan; tahad; tahab; tahame; tahate; tahavad', None),
    ('conj', 'Wzory koniugacji', 'rääkima (mówić)', 'os', 'räägin; räägid; räägib; räägime; räägite; räägivad', 'Wymiana stopnia: kk → g w temacie.'),
    ('conj', 'Czasowniki nieregularne', 'olema (być)', 'os', 'olen; oled; on; oleme; olete; on', '3. osoba ma tę samą formę w obu liczbach: on.'),
    ('conj', 'Czasowniki nieregularne', 'minema (iść)', 'os', 'lähen; lähed; läheb; läheme; lähete; lähevad', 'Temat teraźniejszy jest inny niż bezokolicznik: lähe-.'),
    ('conj', 'Czasowniki nieregularne', 'tulema (przychodzić)', 'os', 'tulen; tuled; tuleb; tuleme; tulete; tulevad', None),
    ('conj', 'Czasowniki nieregularne', 'tegema (robić)', 'os', 'teen; teed; teeb; teeme; teete; teevad', None),
    ('conj', 'Czasowniki nieregularne', 'nägema (widzieć)', 'os', 'näen; näed; näeb; näeme; näete; näevad', None),
    ('conj', 'Czasowniki nieregularne', 'sööma (jeść)', 'os', 'söön; sööd; sööb; sööme; sööte; söövad', None),
    ('decl', 'Trzy główne przypadki', 'raamat (książka)', 'przyp', 'raamat; raamatu; raamatut', 'Te trzy formy trzeba znać dla każdego słowa; reszta przypadków powstaje z dopełniacza.'),
    ('decl', 'Trzy główne przypadki', 'kool (szkoła)', 'przyp', 'kool; kooli; kooli', None),
    ('decl', 'Trzy główne przypadki', 'laps (dziecko)', 'przyp', 'laps; lapse; last', None),
    ('decl', 'Trzy główne przypadki', 'õpilane (uczeń)', 'przyp', 'õpilane; õpilase; õpilast', 'Słowa na -ne: -se, -st.'),
    ('decl', 'Wyjątki', 'vesi (woda)', 'przyp', 'vesi; vee; vett', None),
    ('decl', 'Wyjątki', 'käsi (ręka)', 'przyp', 'käsi; käe; kätt', None),
    ('decl', 'Wyjątki', 'sõber (przyjaciel)', 'przyp', 'sõber; sõbra; sõpra', 'Wymiana stopnia: b → p w osastav.'),
    ('decl', 'Wyjątki', 'mees (mężczyzna)', 'przyp', 'mees; mehe; meest', None),
    ('decl', 'Przypadki miejsca', 'maja (dom): gdzie?', 'miejsc', 'majja; majas; majast; majale; majal; majalt', 'Końcówki dokleja się do dopełniacza: -s, -st, -le, -l, -lt.'),
    ('decl', 'Przypadki miejsca', 'kool (szkoła): gdzie?', 'miejsc', 'kooli; koolis; koolist; koolile; koolil; koolilt', None),
    ('form', 'Imiesłowy', 'lugema (czytać)', 'im', 'lugev; lugenud; loetav; loetud', None),
    ('form', 'Imiesłowy', 'tegema (robić)', 'im', 'tegev; teinud; tehtav; tehtud', None),
    ('form', 'Imiesłowy', 'kirjutama (pisać)', 'im', 'kirjutav; kirjutanud; kirjutatav; kirjutatud', None),
    ('conj', 'Czas przeszły', 'olema: czas przeszły', 'os', 'olin; olid; oli; olime; olite; olid', None),
    ('conj', 'Czas przeszły', 'elama: czas przeszły', 'os', 'elasin; elasid; elas; elasime; elasite; elasid', 'Znak czasu przeszłego: -si-.'),
    ('form', 'Typowe trudności', 'Partitiiv: jaka forma?', 't_osastav', 'raamatut; vett; last; kooli; kätt; meest', None),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['olen', 'elan', 'tahan', 'lähen', 'teen', 'näen'],
    't_m1': ['üks (1)', 'kaks (2)', 'kolm (3)', 'viis (5)', 'kümme (10)', 'mitu (ile)'],
    't_m2': ['sõber (przyjaciel)', 'tuba (pokój)', 'poeg (syn)', 'jalg (noga)', 'leib (chleb)', 'kapp (szafa)'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Przeczenie: ei + temat', 't_m0', 'ei ole; ei ela; ei taha; ei lähe; ei tee; ei näe', 'W przeczeniu forma jest jedna dla wszystkich osób: mina ei ole, sina ei ole.'),
    ('form', 'Typowe trudności', 'Liczba + rzeczownik', 't_m1', 'üks raamat; kaks raamatut; kolm raamatut; viis raamatut; kümme raamatut; mitu raamatut', 'Po liczbach od 2 w górę stoi partitiiv liczby pojedynczej.'),
    ('form', 'Typowe trudności', 'Wymiana stopni: omastav', 't_m2', 'sõbra; toa; poja; jala; leiva; kapi', 'Temat słabnie w dopełniaczu: b znika lub zmienia się w v, g znika, pp → p.'),
]

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'mina (ja)', 'przyp', 'mina; minu; mind', 'Krótkie formy: ma, mu, mind.'),
    ('decl', 'Zaimki', 'sina (ty)', 'przyp', 'sina; sinu; sind', None),
    ('decl', 'Zaimki', 'tema (on, ona)', 'przyp', 'tema; tema; teda', None),
    ('decl', 'Zaimki', 'meie (my)', 'przyp', 'meie; meie; meid', None),
    ('decl', 'Zaimki', 'teie (wy)', 'przyp', 'teie; teie; teid', None),
    ('decl', 'Zaimki', 'nemad (oni)', 'przyp', 'nemad; nende; neid', None),
    ('decl', 'Zaimki', 'see (ten, to)', 'przyp', 'see; selle; seda', None),
    ('decl', 'Zaimki', 'kes (kto)', 'przyp', 'kes; kelle; keda', None),
    ('decl', 'Zaimki', 'mis (co)', 'przyp', 'mis; mille; mida', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'minu vend': 'mój brat', 'sinu õde': 'twoja siostra'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'hea (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'hea; parem; parim', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'suur (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'suur; suurem; suurim', None),
    ('form', 'Stopniowanie', 'väike (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'väike; väiksem; väikseim', None),
    ('form', 'Stopniowanie', 'vana (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'vana; vanem; vanim', None),
    ('form', 'Stopniowanie', 'ilus (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'ilus; ilusam; kõige ilusam', 'Najczęściej: kõige + stopień wyższy.'),
    ('form', 'Stopniowanie', 'kiire (szybki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'kiire; kiirem; kõige kiirem', 'Najczęściej: kõige + stopień wyższy.'),
    ('form', 'Stopniowanie', 'pikk (długi)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'pikk; pikem; pikim', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 2 (generowane) ===
PARADIGMS += [
    ('conj', 'Wzory koniugacji', 'minema: lihtminevik (poszedłem)', ['mina', 'sina', 'tema', 'meie', 'teie', 'nemad'], 'läksin; läksid; läks; läksime; läksite; läksid', None),
    ('conj', 'Wzory koniugacji', 'tegema: lihtminevik (zrobiłem)', ['mina', 'sina', 'tema', 'meie', 'teie', 'nemad'], 'tegin; tegid; tegi; tegime; tegite; tegid', None),
    ('conj', 'Wzory koniugacji', 'oskama (umieć)', ['mina', 'sina', 'tema', 'meie', 'teie', 'nemad'], 'oskan; oskad; oskab; oskame; oskate; oskavad', None),
    ('conj', 'Tryb warunkowy', 'tahtma: konditsionaal', ['mina', 'sina', 'tema', 'meie', 'teie', 'nemad'], 'tahaksin; tahaksid; tahaks; tahaksime; tahaksite; tahaksid', 'Grzeczna prośba: Ma tahaksin kohvi.'),
    ('form', 'Przypadki (10)', 'auto (samochód)', ['nimetav', 'omastav', 'osastav', 'seesütlev (w)', 'seestütlev (z)', 'sisseütlev (do)', 'alalütlev (na)', 'alaltütlev (z)', 'allaütlev (na, do)', 'saav (w co)'], 'auto; auto; autot; autos; autost; autosse; autol; autolt; autole; autoks', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 2 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('poiss', 'chłopiec', None, None), ('tüdruk', 'dziewczynka', None, None), ('inimene', 'człowiek', None, None), ('inimesed', 'ludzie', None, None), ('perekond', 'rodzina', None, None), ('poeg', 'syn', None, None), ('tütar', 'córka', None, None), ('vanaisa', 'dziadek', None, None), ('vanaema', 'babcia', None, None), ('lapselaps', 'wnuk', None, None), ('onu', 'wujek', None, None), ('tädi', 'ciocia', None, None), ('nõbu', 'kuzyn', None, None), ('abikaasa (mąż)', 'mąż', None, None), ('naine (żona)', 'żona', None, None), ('naaber', 'sąsiad', None, None)], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('külaline', 'gość', None, None), ('ülemus', 'szef', None, None), ('kolleeg', 'kolega', None, None), ('vaenlane', 'wróg', None, None), ('kuningas', 'król', None, None), ('kuninganna', 'królowa', None, None)], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('pea', 'głowa', None, None), ('nägu', 'twarz', None, None), ('silm', 'oko', None, None), ('kõrv', 'ucho', None, None), ('nina', 'nos', None, None), ('suu', 'usta', None, None), ('hammas', 'ząb', None, None), ('keel', 'język (narząd)', None, None), ('juuksed', 'włosy', None, None), ('kael', 'szyja', None, None), ('õlg', 'ramię', None, None), ('käsi', 'ręka', None, None), ('sõrm', 'palec', None, None), ('jalg', 'noga', None, None), ('jalalaba', 'stopa', None, None), ('põlv', 'kolano', None, None)], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('selg', 'plecy', None, None), ('kõht', 'brzuch', None, None), ('süda', 'serce', None, None), ('veri', 'krew', None, None), ('luu', 'kość', None, None), ('nahk', 'skóra', None, None), ('hääl', 'głos', None, None), ('keha', 'ciało', None, None), ('magu', 'żołądek', None, None), ('habe', 'broda', None, None), ('huul', 'warga', None, None), ('küüs', 'paznokieć', None, None), ('rind', 'pierś', None, None), ('aju', 'mózg', None, None)], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('või', 'masło', None, None), ('juust', 'ser', None, None), ('piim', 'mleko', None, None), ('muna', 'jajko', None, None), ('liha', 'mięso', None, None), ('kana', 'kurczak', None, None), ('sealiha', 'wieprzowina', None, None), ('supp', 'zupa', None, None), ('salat', 'sałatka', None, None), ('riis', 'ryż', None, None), ('makaronid', 'makaron', None, None), ('kartul', 'ziemniak', None, None), ('porgand', 'marchewka', None, None), ('sibul', 'cebula', None, None), ('küüslauk', 'czosnek', None, None), ('tomat', 'pomidor', None, None)], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('kurk', 'ogórek', None, None), ('pirn', 'gruszka', None, None), ('banaan', 'banan', None, None), ('apelsin', 'pomarańcza', None, None), ('sidrun', 'cytryna', None, None), ('maasikas', 'truskawka', None, None), ('viinamari', 'winogrono', None, None), ('suhkur', 'cukier', None, None), ('sool', 'sól', None, None), ('pipar', 'pieprz', None, None), ('õli', 'olej', None, None), ('jahu', 'mąka', None, None), ('mesi', 'miód', None, None), ('šokolaad', 'czekolada', None, None), ('jäätis', 'lody', None, None), ('tort', 'ciasto (tort)', None, None)], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('küpsis', 'ciastko', None, None), ('hommikusöök', 'śniadanie', None, None), ('lõunasöök', 'obiad', None, None), ('õhtusöök', 'kolacja', None, None), ('suupiste', 'przekąska', None, None)], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('mahl', 'sok', None, None), ('õlu', 'piwo', None, None), ('vein', 'wino', None, None), ('jook', 'napój', None, None), ('klaas', 'szklanka', None, None), ('tass', 'filiżanka', None, None), ('taldrik', 'talerz', None, None), ('nuga', 'nóż', None, None), ('kahvel', 'widelec', None, None), ('lusikas', 'łyżka', None, None), ('pudel', 'butelka', None, None), ('menüü', 'menu', None, None), ('arve', 'rachunek', None, None), ('jootraha', 'napiwek', None, None), ('laud (w restauracji)', 'stolik', None, None), ('ettekandja', 'kelner', None, None)], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('kokk', 'kucharz', None, None), ('näljane', 'głodny', None, None), ('janune', 'spragniony', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('maja', 'dom', None, None), ('korter', 'mieszkanie', None, None), ('tuba', 'pokój', None, None), ('köök', 'kuchnia', None, None), ('vannituba', 'łazienka', None, None), ('magamistuba', 'sypialnia', None, None), ('elutuba', 'salon', None, None), ('aed', 'ogród', None, None), ('uks', 'drzwi', None, None), ('aken', 'okno', None, None), ('sein', 'ściana', None, None), ('põrand', 'podłoga', None, None), ('katus', 'dach', None, None), ('trepp', 'schody', None, None), ('võti', 'klucz', None, None), ('laud', 'stół', None, None)], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('tool', 'krzesło', None, None), ('voodi', 'łóżko', None, None), ('kapp', 'szafa', None, None), ('lamp', 'lampa', None, None), ('vaip', 'dywan', None, None), ('peegel', 'lustro', None, None), ('teler', 'telewizor', None, None), ('telefon', 'telefon', None, None), ('arvuti', 'komputer', None, None), ('padi', 'poduszka', None, None), ('tekk', 'koc', None, None), ('rätik', 'ręcznik', None, None), ('seep', 'mydło', None, None), ('hambahari', 'szczoteczka do zębów', None, None), ('külmkapp', 'lodówka', None, None), ('ahi', 'piec', None, None)], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('pesumasin', 'pralka', None, None), ('prügi', 'śmieci', None, None)], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('rõivas', 'ubranie', None, None), ('särk', 'koszula', None, None), ('püksid', 'spodnie', None, None), ('kleit', 'sukienka', None, None), ('seelik', 'spódnica', None, None), ('jope', 'kurtka', None, None), ('mantel', 'płaszcz', None, None), ('kampsun', 'sweter', None, None), ('jalatsid', 'buty', None, None), ('sokid', 'skarpetki', None, None), ('müts', 'czapka', None, None), ('kübar', 'kapelusz', None, None), ('kindad', 'rękawiczki', None, None), ('sall', 'szalik', None, None), ('kott', 'torba', None, None), ('seljakott', 'plecak', None, None)], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('rahakott', 'portfel', None, None), ('prillid', 'okulary', None, None), ('käekell', 'zegarek', None, None), ('sõrmus', 'pierścionek', None, None), ('aluspesu', 'bielizna', None, None), ('pidžaama', 'piżama', None, None), ('vöö', 'pasek', None, None), ('lips', 'krawat', None, None), ('ülikond', 'garnitur', None, None)], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('punane', 'czerwony', None, None), ('sinine', 'niebieski', None, None), ('roheline', 'zielony', None, None), ('kollane', 'żółty', None, None), ('must', 'czarny', None, None), ('valge', 'biały', None, None), ('hall', 'szary', None, None), ('pruun', 'brązowy', None, None), ('roosa', 'różowy', None, None), ('lilla', 'fioletowy', None, None), ('värv', 'kolor', None, None), ('ümmargune', 'okrągły', None, None), ('ruudukujuline', 'kwadratowy', None, None), ('sirge', 'prosty', None, None), ('viltu', 'krzywy', None, None), ('joon', 'linia', None, None)], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('punkt', 'punkt', None, None), ('ring', 'koło', None, None)], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('null', 'zero', None, None), ('üksteist', 'jedenaście', None, None), ('kaksteist', 'dwanaście', None, None), ('kolmteist', 'trzynaście', None, None), ('neliteist', 'czternaście', None, None), ('viisteist', 'piętnaście', None, None), ('kuusteist', 'szesnaście', None, None), ('seitseteist', 'siedemnaście', None, None), ('kaheksateist', 'osiemnaście', None, None), ('üheksateist', 'dziewiętnaście', None, None), ('kakskümmend', 'dwadzieścia', None, None), ('kolmkümmend', 'trzydzieści', None, None), ('nelikümmend', 'czterdzieści', None, None), ('viiskümmend', 'pięćdziesiąt', None, None), ('kuuskümmend', 'sześćdziesiąt', None, None), ('seitsekümmend', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('kaheksakümmend', 'osiemdziesiąt', None, None), ('üheksakümmend', 'dziewięćdziesiąt', None, None), ('sada', 'sto', None, None), ('tuhat', 'tysiąc', None, None), ('miljon', 'milion', None, None), ('esimene', 'pierwszy', None, None), ('teine', 'drugi', None, None), ('kolmas', 'trzeci', None, None), ('pool', 'połowa', None, None), ('paar', 'para', None, None), ('mõned', 'kilka', None, None), ('palju', 'wiele', None, None), ('vähe', 'mało', None, None), ('terve', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('sekund', 'sekunda', None, None), ('minut', 'minuta', None, None), ('tund', 'godzina', None, None), ('päev', 'dzień', None, None), ('öö', 'noc', None, None), ('nädal', 'tydzień', None, None), ('kuu (miesiąc)', 'miesiąc', None, None), ('aasta', 'rok', None, None), ('kevad', 'wiosna', None, None), ('suvi', 'lato', None, None), ('sügis', 'jesień', None, None), ('talv', 'zima', None, None), ('esmaspäev', 'poniedziałek', None, None), ('teisipäev', 'wtorek', None, None), ('kolmapäev', 'środa', None, None), ('neljapäev', 'czwartek', None, None)], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('reede', 'piątek', None, None), ('laupäev', 'sobota', None, None), ('pühapäev', 'niedziela', None, None), ('jaanuar', 'styczeń', None, None), ('veebruar', 'luty', None, None), ('märts', 'marzec', None, None), ('aprill', 'kwiecień', None, None), ('mai', 'maj', None, None), ('juuni', 'czerwiec', None, None), ('juuli', 'lipiec', None, None), ('august', 'sierpień', None, None), ('september', 'wrzesień', None, None), ('oktoober', 'październik', None, None), ('november', 'listopad', None, None), ('detsember', 'grudzień', None, None), ('hommik', 'rano (pora dnia)', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('keskpäev', 'południe', None, None), ('õhtul', 'wieczorem', None, None), ('alati', 'zawsze', None, None), ('mitte kunagi', 'nigdy', None, None), ('mõnikord', 'czasem', None, None), ('sageli', 'często', None, None), ('juba', 'już', None, None), ('veel', 'jeszcze', None, None), ('varsti', 'wkrótce', None, None), ('hiljem', 'później', None, None), ('vara', 'wcześnie', None, None), ('hilja', 'późno', None, None), ('millal', 'kiedy (pytanie)', None, None), ('kuupäev', 'data', None, None), ('minevik', 'przeszłość', None, None), ('tulevik', 'przyszłość', None, None)], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('sünnipäev', 'urodziny', None, None), ('püha', 'święto', None, None), ('puhkus', 'wakacje', None, None)], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('päike', 'słońce', None, None), ('kuu', 'księżyc', None, None), ('täht', 'gwiazda', None, None), ('taevas', 'niebo', None, None), ('pilv', 'chmura', None, None), ('vihm', 'deszcz', None, None), ('lumi', 'śnieg', None, None), ('tuul', 'wiatr', None, None), ('torm', 'burza', None, None), ('udu', 'mgła', None, None), ('jää', 'lód', None, None), ('tuli, ziemia (planeta', 'ogień', None, None), ('maa', 'grunt)', None, None), ('jõgi', 'rzeka', None, None), ('järv', 'jezioro', None, None), ('mägi', 'góra', None, None)], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('mets', 'las', None, None), ('puu', 'drzewo', None, None), ('lill', 'kwiat', None, None), ('rohi', 'trawa', None, None), ('leht', 'liść', None, None), ('põld', 'pole', None, None), ('saar', 'wyspa', None, None), ('rand', 'plaża', None, None), ('kõrb', 'pustynia', None, None), ('kalju', 'skała', None, None), ('kivi', 'kamień', None, None), ('ilm', 'pogoda', None, None), ('temperatuur', 'temperatura', None, None), ('külm', 'zimny', None, None), ('soe', 'ciepły', None, None), ('kuum', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('koer', 'pies', None, None), ('kass', 'kot', None, None), ('hobune', 'koń', None, None), ('lehm', 'krowa', None, None), ('siga', 'świnia', None, None), ('lammas', 'owca', None, None), ('kits', 'koza', None, None), ('kana (kura)', 'kura', None, None), ('part', 'kaczka', None, None), ('lind', 'ptak', None, None), ('hiir', 'mysz', None, None), ('rott', 'szczur', None, None), ('madu', 'wąż', None, None), ('konn', 'żaba', None, None), ('lõvi', 'lew', None, None), ('tiiger', 'tygrys', None, None)], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('elevant', 'słoń', None, None), ('karu', 'niedźwiedź', None, None), ('hunt', 'wilk', None, None), ('rebane', 'lis', None, None), ('jänes', 'zając', None, None), ('hirv', 'jeleń', None, None), ('ahv', 'małpa', None, None), ('liblikas', 'motyl', None, None), ('mesilane', 'pszczoła', None, None), ('kärbes', 'mucha', None, None), ('ämblik', 'pająk', None, None), ('loom', 'zwierzę', None, None), ('putukas', 'owad', None, None)], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('küla', 'wieś', None, None), ('väljak', 'plac', None, None), ('sild', 'most', None, None), ('park', 'park', None, None), ('pood', 'sklep', None, None), ('turg', 'targ', None, None), ('supermarket', 'supermarket', None, None), ('pank', 'bank', None, None), ('postkontor', 'poczta', None, None), ('haigla', 'szpital', None, None), ('apteek', 'apteka', None, None), ('ülikool', 'uniwersytet', None, None), ('raamatukogu', 'biblioteka', None, None), ('muuseum', 'muzeum', None, None), ('kirik', 'kościół', None, None), ('restoran', 'restauracja', None, None)], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('kohvik', 'kawiarnia', None, None), ('lennujaam', 'lotnisko', None, None), ('jaam', 'dworzec', None, None), ('peatus', 'przystanek', None, None), ('kino', 'kino', None, None), ('teater', 'teatr', None, None), ('politsei', 'policja', None, None), ('kontor', 'biuro', None, None), ('vabrik', 'fabryka', None, None), ('hoone', 'budynek', None, None), ('torn', 'wieża', None, None), ('kesklinn', 'centrum', None, None), ('aadress', 'adres', None, None), ('kaart', 'mapa', None, None)], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('auto', 'samochód', None, None), ('buss', 'autobus', None, None), ('rong', 'pociąg', None, None), ('tramm', 'tramwaj', None, None), ('metroo', 'metro', None, None), ('lennuk', 'samolot', None, None), ('laev', 'statek', None, None), ('jalgratas', 'rower', None, None), ('mootorratas', 'motocykl', None, None), ('pilet', 'bilet', None, None), ('reis', 'podróż', None, None), ('ekskursioon', 'wycieczka', None, None), ('pass', 'paszport', None, None), ('kohver', 'walizka', None, None), ('bensiin', 'benzyna', None, None), ('parkla', 'parking', None, None)], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('ristmik', 'skrzyżowanie', None, None), ('foor', 'światła', None, None), ('juhiluba', 'prawo jazdy', None, None), ('juht', 'kierowca', None, None), ('reisija', 'pasażer', None, None), ('sissesõit', 'wjazd', None, None), ('väljasõit', 'wyjazd', None, None), ('raudtee', 'kolej', None, None), ('sadam', 'port', None, None), ('piir', 'granica', None, None)], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('töö', 'praca', None, None), ('amet', 'zawód', None, None), ('arst', 'lekarz', None, None), ('õde (pielęgniarka)', 'pielęgniarka', None, None), ('üliõpilane', 'student', None, None), ('insener', 'inżynier', None, None), ('jurist', 'prawnik', None, None), ('politseinik', 'policjant', None, None), ('sõdur', 'żołnierz', None, None), ('põllumees', 'rolnik', None, None), ('müüja', 'sprzedawca', None, None), ('kassapidaja', 'kasjer', None, None), ('näitleja', 'aktor', None, None), ('kirjanik', 'pisarz', None, None), ('maalikunstnik', 'malarz', None, None), ('muusik', 'muzyk', None, None)], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('kunstnik', 'artysta', None, None), ('firma', 'firma', None, None), ('raha', 'pieniądze', None, None), ('palk', 'pensja', None, None), ('leping', 'umowa', None, None), ('kohtumine', 'spotkanie', None, None), ('tund (lekcja)', 'lekcja', None, None), ('eksam', 'egzamin', None, None), ('hinne', 'ocena', None, None), ('klass', 'klasa', None, None), ('raamat', 'książka', None, None), ('vihik', 'zeszyt', None, None), ('pastakas', 'długopis', None, None), ('pliiats', 'ołówek', None, None), ('paber', 'papier', None, None), ('tahvel', 'tablica', None, None)], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('sõnaraamat', 'słownik', None, None), ('küsimus', 'pytanie', None, None), ('vastus', 'odpowiedź', None, None), ('ülesanne', 'zadanie', None, None), ('test', 'test', None, None)], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('hind', 'cena', None, None), ('pangakaart', 'karta (płatnicza)', None, None), ('sularaha', 'gotówka', None, None), ('münt', 'moneta', None, None), ('pangatäht', 'banknot', None, None), ('tagasiraha', 'reszta', None, None), ('allahindlus', 'zniżka', None, None), ('korv', 'koszyk', None, None), ('tšekk', 'paragon', None, None), ('kaup', 'towar', None, None), ('ost', 'zakup', None, None), ('müük', 'sprzedaż', None, None), ('väärtus', 'wartość', None, None), ('laen', 'kredyt', None, None), ('võlg', 'dług', None, None), ('maks', 'podatek', None, None)], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('rikkus', 'bogactwo', None, None), ('vaene', 'biedny', None, None), ('rikas', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie', 'icon': 'Z', 'track': 'jezyk', 'words': [('tervis', 'zdrowie', None, None), ('haigus', 'choroba', None, None), ('valu', 'ból', None, None), ('palavik', 'gorączka', None, None), ('köha', 'kaszel', None, None), ('nohu', 'katar', None, None), ('ravim', 'lekarstwo', None, None), ('tablett', 'tabletka', None, None), ('operatsioon', 'operacja', None, None), ('haav', 'rana', None, None), ('õnnetus', 'wypadek', None, None), ('haige', 'chory', None, None), ('väsinud', 'zmęczony', None, None), ('unine', 'śpiący', None, None), ('tugev', 'silny', None, None), ('nõrk', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('rõõm', 'radość', None, None), ('kurbus', 'smutek', None, None), ('hirm', 'strach', None, None), ('viha', 'gniew', None, None), ('armastus', 'miłość', None, None), ('vihkamine', 'nienawiść', None, None), ('lootus', 'nadzieja', None, None), ('unistus', 'marzenie', None, None), ('õnn', 'szczęście', None, None), ('häbi', 'wstyd', None, None), ('üllatus', 'zdziwienie', None, None), ('uudishimu', 'ciekawość', None, None), ('kannatlikkus', 'cierpliwość', None, None), ('julgus', 'odwaga', None, None), ('siiras', 'szczery', None, None), ('sõbralik', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('viisakas', 'grzeczny', None, None), ('rumal', 'głupi', None, None), ('tark', 'mądry', None, None), ('laisk', 'leniwy', None, None), ('töökas', 'pracowity', None, None), ('huvitav', 'ciekawy', None, None), ('igav', 'nudny', None, None), ('rõõmsameelne', 'wesoły', None, None), ('kurb', 'smutny', None, None), ('vihane', 'zły (rozgniewany)', None, None), ('õnnelik', 'szczęśliwy', None, None), ('armunud', 'zakochany', None, None), ('üksildane', 'samotny', None, None), ('rahulik', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('suur', 'duży', None, None), ('pikk', 'długi', None, None), ('lühike', 'krótki', None, None), ('kõrge', 'wysoki', None, None), ('madal', 'niski', None, None), ('lai', 'szeroki', None, None), ('kitsas', 'wąski', None, None), ('paks', 'gruby', None, None), ('kõhn', 'chudy', None, None), ('raske', 'ciężki', None, None), ('kerge', 'lekki', None, None), ('kiire', 'szybki', None, None), ('aeglane', 'wolny', None, None), ('kõva', 'twardy', None, None), ('pehme', 'miękki', None, None), ('märg', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('kuiv', 'suchy', None, None), ('puhas', 'czysty', None, None), ('määrdunud', 'brudny', None, None), ('täis', 'pełny', None, None), ('tühi', 'pusty', None, None), ('terav', 'ostry', None, None), ('vali', 'głośny', None, None), ('vaikne', 'cichy', None, None), ('hele', 'jasny', None, None), ('tume', 'ciemny', None, None), ('noor', 'młody', None, None), ('vana', 'stary', None, None), ('uus', 'nowy', None, None), ('halb', 'zły (niedobry)', None, None), ('ilus', 'ładny', None, None), ('inetu', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('lihtne', 'łatwy', None, None), ('raske (trudny)', 'trudny', None, None), ('oluline', 'ważny', None, None), ('võimalik', 'możliwy', None, None), ('tõeline', 'prawdziwy', None, None), ('vale', 'fałszywy', None, None), ('kallis', 'drogi', None, None), ('odav', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('olema', 'być', None, None), ('omama', 'mieć', None, None), ('tegema', 'robić', None, None), ('minema', 'iść', None, None), ('sõitma', 'jechać', None, None), ('tulema', 'przyjść', None, None), ('lahkuma', 'wyjść', None, None), ('sisenema', 'wejść', None, None), ('tagasi tulema', 'wrócić', None, None), ('jooksma', 'biec', None, None), ('seisma', 'stać', None, None), ('istuma', 'siedzieć', None, None), ('lamama', 'leżeć', None, None), ('magama', 'spać', None, None), ('tõusma', 'wstać', None, None), ('sööma', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('jooma', 'pić', None, None), ('keetma', 'gotować', None, None), ('pesema', 'myć', None, None), ('riietuma', 'ubierać się', None, None), ('rääkima', 'mówić', None, None), ('ütlema', 'powiedzieć', None, None), ('küsima', 'pytać', None, None), ('vastama', 'odpowiadać', None, None), ('kuulma', 'słyszeć', None, None), ('kuulama', 'słuchać', None, None), ('nägema', 'widzieć', None, None), ('vaatama', 'patrzeć', None, None), ('lugema', 'czytać', None, None), ('kirjutama', 'pisać', None, None), ('õppima', 'uczyć się', None, None), ('õpetama', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('mõistma', 'rozumieć', None, None), ('teadma', 'wiedzieć', None, None), ('tundma', 'znać', None, None), ('mõtlema', 'myśleć', None, None), ('mäletama', 'pamiętać', None, None), ('unustama', 'zapominać', None, None), ('tahtma', 'chcieć', None, None), ('meeldima', 'lubić', None, None), ('armastama', 'kochać', None, None), ('vajama', 'potrzebować', None, None), ('saama', 'móc', None, None), ('pidama', 'musieć', None, None), ('andma', 'dawać', None, None), ('võtma', 'brać', None, None), ('ostma', 'kupować', None, None), ('müüma', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('maksma', 'płacić', None, None), ('avama', 'otwierać', None, None), ('sulgema', 'zamykać', None, None), ('alustama', 'zaczynać', None, None), ('lõpetama', 'kończyć', None, None), ('töötama', 'pracować', None, None), ('mängima', 'grać', None, None), ('laulma', 'śpiewać', None, None), ('tantsima', 'tańczyć', None, None), ('ujuma', 'pływać', None, None), ('lendama', 'latać', None, None), ('panema', 'kłaść', None, None), ('otsima', 'szukać', None, None), ('leidma', 'znajdować', None, None), ('ootama', 'czekać', None, None), ('aitama', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('paluma', 'prosić', None, None), ('vabandama', 'przepraszać', None, None), ('lubama', 'pozwalać', None, None), ('proovima', 'próbować', None, None), ('muutma', 'zmieniać', None, None), ('kandma', 'nosić', None, None), ('hoidma', 'trzymać', None, None), ('viskama', 'rzucać', None, None), ('püüdma', 'łapać', None, None), ('lööma', 'bić', None, None), ('tapma', 'zabijać', None, None), ('surema', 'umierać', None, None), ('elama', 'żyć', None, None), ('elama (mieszkać)', 'mieszkać', None, None), ('kohtama', 'spotykać', None, None), ('helistama', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('saatma', 'wysyłać', None, None), ('saama (dostawać)', 'dostawać', None, None), ('näitama', 'pokazywać', None, None), ('kutsuma', 'zapraszać', None, None), ('külastama', 'odwiedzać', None, None), ('nutma', 'płakać', None, None), ('naerma', 'śmiać się', None, None), ('naeratama', 'uśmiechać się', None, None), ('kartma', 'bać się', None, None), ('rõõmustama', 'cieszyć się', None, None), ('uskuma', 'wierzyć', None, None), ('nõustuma', 'zgadzać się', None, None), ('valima', 'wybierać', None, None), ('otsustama', 'decydować', None, None), ('lugema (liczyć)', 'liczyć', None, None), ('kaaluma', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('kõndima', 'chodzić', None, None), ('sõitma (jeździć)', 'jeździć', None, None), ('peale astuma', 'wsiadać', None, None), ('maha astuma', 'wysiadać', None, None), ('pöörama', 'skręcać', None, None), ('peatuma', 'zatrzymywać się', None, None), ('hilinema', 'spóźniać się', None, None), ('kiirustama', 'spieszyć się', None, None), ('puhkama', 'odpoczywać', None, None), ('mängima (bawić się)', 'bawić się', None, None), ('joonistama', 'rysować', None, None), ('ehitama', 'budować', None, None), ('parandama', 'naprawiać', None, None), ('lõikama', 'ciąć', None, None), ('praadima', 'smażyć', None, None), ('küpsetama', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('segama', 'mieszać', None, None), ('valama', 'nalewać', None, None), ('koristama', 'sprzątać', None, None), ('pesema (prać)', 'prać', None, None), ('triikima', 'prasować', None, None), ('habet ajama', 'golić się', None, None), ('kammima', 'czesać', None, None), ('suplema', 'kąpać się', None, None), ('ärkama', 'budzić się', None, None), ('uinuma', 'zasypiać', None, None), ('unistama', 'marzyć', None, None), ('unenägu nägema', 'śnić', None, None), ('harjutama', 'ćwiczyć', None, None), ('treenima', 'trenować', None, None), ('võitma', 'wygrywać', None, None), ('kaotama', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('liigutama', 'ruszać', None, None), ('tõmbama', 'ciągnąć', None, None), ('lükkama', 'pchać', None, None), ('tõstma', 'podnosić', None, None), ('kukkuma', 'spadać', None, None), ('hüppama', 'skakać', None, None), ('ronima', 'wspinać się', None, None), ('peitma', 'ukrywać', None, None), ('varastama', 'kraść', None, None), ('tagastama', 'oddawać', None, None), ('laenama', 'pożyczać', None, None), ('kulutama', 'wydawać', None, None), ('säästma', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('see', 'ten', None, None), ('too', 'tamten', None, None), ('kuidas', 'jak', None, None), ('miks', 'dlaczego', None, None), ('kes', 'kto', None, None), ('mis (który)', 'który', None, None), ('missugune', 'jaki', None, None), ('mitu', 'ile (policzalne)', None, None), ('aga', 'ale', None, None), ('sest', 'bo', None, None), ('kui', 'jeśli', None, None), ('et', 'że', None, None), ('seega', 'więc', None, None), ('ka', 'też', None, None), ('ainult', 'tylko', None, None), ('natuke', 'trochę', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('palju (dużo)', 'dużo', None, None), ('kõik', 'wszystko', None, None), ('mitte midagi', 'nic', None, None), ('miski', 'coś', None, None), ('keegi', 'ktoś', None, None), ('mitte keegi', 'nikt', None, None), ('iga', 'każdy', None, None), ('sama', 'ten sam', None, None), ('võib-olla', 'może (być)', None, None), ('kindlasti', 'na pewno', None, None), ('koos', 'razem', None, None), ('ise', 'sam', None, None), ('ilma', 'bez', None, None), ('koos (z)', 'z (towarzysząc)', None, None), ('sees', 'w (miejsce)', None, None), ('peal', 'na (powierzchni)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('kuni', 'do (kierunek)', None, None), ('alates', 'od', None, None), ('jaoks', 'dla', None, None), ('läbi', 'przez', None, None), ('pärast', 'po (czas)', None, None), ('enne', 'przed', None, None), ('taga', 'za (z tyłu)', None, None), ('kohal', 'nad', None, None), ('all', 'pod', None, None), ('kõrval', 'obok', None, None), ('vahel', 'między', None, None), ('vastu', 'przeciw', None, None), ('kohta', 'o (temat)', None, None), ('juures', 'u (przy)', None, None), ('umbes', 'około', None, None), ('peaaegu', 'prawie', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('isegi', 'nawet', None, None), ('jälle', 'jeszcze raz', None, None), ('praegu', 'teraz', None, None), ('siis', 'wtedy', None, None), ('kuskil', 'gdzieś', None, None), ('mitte kusagil', 'nigdzie', None, None), ('kõikjal', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('elu', 'życie', None, None), ('surm', 'śmierć', None, None), ('maailm', 'świat', None, None), ('riik', 'kraj', None, None), ('riigivõim', 'państwo', None, None), ('keel (mowa)', 'język (mowa)', None, None), ('sõna', 'słowo', None, None), ('lause', 'zdanie', None, None), ('eesnimi', 'imię', None, None), ('perekonnanimi', 'nazwisko', None, None), ('vanus', 'wiek', None, None), ('ajalugu', 'historia', None, None), ('kultuur', 'kultura', None, None), ('religioon', 'religia', None, None), ('Jumal', 'Bóg', None, None), ('sõda', 'wojna', None, None)], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('rahu', 'pokój (brak wojny)', None, None), ('seadus', 'prawo (przepis)', None, None), ('vabadus', 'wolność', None, None), ('võim', 'władza', None, None), ('valitsus', 'rząd', None, None), ('valimised', 'wybory', None, None), ('probleem', 'problem', None, None), ('idee', 'pomysł', None, None), ('põhjus', 'powód', None, None), ('tulemus', 'wynik', None, None), ('algus', 'początek', None, None), ('lõpp', 'koniec', None, None), ('osa', 'część', None, None), ('koht', 'miejsce', None, None), ('asi', 'rzecz', None, None), ('juhtum', 'sprawa', None, None)], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('teave', 'informacja', None, None), ('sõnum', 'wiadomość', None, None), ('kiri', 'list', None, None), ('ajaleht', 'gazeta', None, None), ('film', 'film', None, None), ('muusika', 'muzyka', None, None), ('laul', 'piosenka', None, None), ('maal', 'obraz', None, None), ('mäng', 'gra', None, None), ('sport', 'sport', None, None), ('mäng (mecz)', 'mecz', None, None), ('meeskond', 'drużyna', None, None), ('pall', 'piłka', None, None), ('lõbu', 'zabawa', None, None), ('pidu', 'impreza', None, None), ('kingitus', 'prezent', None, None)], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('uni', 'sen', None, None), ('plaan', 'plan', None, None), ('valik', 'wybór', None, None), ('viga', 'błąd', None, None), ('tõde', 'prawda', None, None), ('vale (kłamstwo)', 'kłamstwo', None, None), ('saladus', 'tajemnica', None, None), ('jõud', 'siła', None, None), ('energia', 'energia', None, None), ('valgus', 'światło', None, None), ('heli', 'dźwięk', None, None), ('vaikus', 'cisza', None, None), ('liikumine', 'ruch', None, None), ('muutus', 'zmiana', None, None), ('erinevus', 'różnica', None, None), ('näide', 'przykład', None, None)], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('tervik', 'całość', None, None)], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, None), ('e-post', 'e-mail', None, None), ('parool', 'hasło', None, None), ('veebileht', 'strona internetowa', None, None), ('programm', 'program', None, None), ('rakendus', 'aplikacja', None, None), ('ekraan', 'ekran', None, None), ('klaviatuur', 'klawiatura', None, None), ('arvutihiir', 'myszka komputerowa', None, None), ('fail', 'plik', None, None), ('foto', 'zdjęcie', None, None), ('kaamera', 'kamera', None, None), ('aku', 'bateria', None, None), ('elekter', 'prąd', None, None), ('kaabel', 'kabel', None, None), ('masin', 'maszyna', None, None)], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('tööriist', 'narzędzie', None, None), ('haamer', 'młotek', None, None), ('printer', 'drukarka', None, None), ('laadija', 'ładowarka', None, None)], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('põhi', 'północ', None, None), ('lõuna', 'południe (kierunek)', None, None), ('ida', 'wschód', None, None), ('lääs', 'zachód', None, None), ('Poola', 'Polska', None, None), ('Euroopa', 'Europa', None, None), ('Saksamaa', 'Niemcy', None, None), ('Prantsusmaa', 'Francja', None, None), ('Itaalia', 'Włochy', None, None), ('Hispaania', 'Hiszpania', None, None), ('Venemaa', 'Rosja', None, None), ('Inglismaa', 'Anglia', None, None), ('Ameerika', 'Ameryka', None, None), ('Hiina', 'Chiny', None, None), ('Jaapan', 'Japonia', None, None), ('Aafrika', 'Afryka', None, None)], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('Aasia', 'Azja', None, None), ('mandrid', 'kontynent', None, None), ('pealinn', 'stolica', None, None), ('kodanik', 'obywatel', None, None)], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('tükk', 'kawałek', None, None), ('tilk', 'kropla', None, None), ('karp', 'pudełko', None, None), ('kott (worek)', 'worek', None, None), ('niit', 'nić', None, None), ('traat', 'drut', None, None), ('nõel', 'igła', None, None), ('käärid', 'nożyczki', None, None), ('kepp', 'kij', None, None), ('köis', 'lina', None, None), ('kett', 'łańcuch', None, None), ('kruvi', 'śruba', None, None), ('nael', 'gwóźdź', None, None), ('liim', 'klej', None, None), ('värv (farba)', 'farba', None, None), ('klaas (szkło)', 'szkło', None, None)], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('puit', 'drewno', None, None), ('metall', 'metal', None, None), ('kuld', 'złoto', None, None), ('hõbe', 'srebro', None, None), ('raud', 'żelazo', None, None), ('plast', 'plastik', None, None), ('nahk (materiał)', 'skóra (materiał)', None, None), ('puuvill', 'bawełna', None, None), ('vill', 'wełna', None, None), ('liiv', 'piasek', None, None), ('muda', 'błoto', None, None), ('tolm', 'kurz', None, None), ('suits', 'dym', None, None), ('aur', 'para (wodna)', None, None)], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('üleval', 'góra (kierunek)', None, None), ('ees', 'przód', None, None), ('taga (tył)', 'tył', None, None), ('keskel', 'środek', None, None), ('külg', 'bok', None, None), ('sees (wewnątrz)', 'wewnątrz', None, None), ('väljas', 'na zewnątrz', None, None), ('kaugel', 'daleko', None, None), ('lähedal', 'blisko', None, None), ('kõrgel', 'wysoko', None, None), ('madalal', 'nisko', None, None), ('kiiresti', 'szybko', None, None), ('aeglaselt', 'wolno', None, None), ('hästi', 'dobrze', None, None), ('halvasti', 'źle', None, None), ('lihtsalt', 'łatwo', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('raskelt', 'trudno', None, None), ('eraldi', 'osobno', None, None), ('vastas', 'naprzeciw', None, None), ('mööda', 'wzdłuż', None, None), ('risti', 'w poprzek', None, None), ('ümber', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('kapsas', 'kapusta', None, None), ('hernes', 'groszek', None, None), ('uba', 'fasola', None, None), ('seen', 'grzyb', None, None), ('pähkel', 'orzech', None, None), ('ploom', 'śliwka', None, None), ('kirss', 'wiśnia', None, None), ('virsik', 'brzoskwinia', None, None), ('arbuus', 'arbuz', None, None), ('vaarikas', 'malina', None, None), ('vorst', 'kiełbasa', None, None), ('sink', 'szynka', None, None), ('sai', 'bułka', None, None), ('võileib', 'kanapka', None, None), ('pannkook', 'naleśnik', None, None), ('jogurt', 'jogurt', None, None)], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('koor', 'śmietana', None, None), ('kaste', 'sos', None, None), ('äädikas', 'ocet', None, None), ('pärm', 'drożdże', None, None), ('tarretis (kisiel)', 'kisiel', None, None), ('tarretis', 'galaretka', None, None), ('rosin', 'rodzynek', None, None), ('mandel', 'migdał', None, None), ('petersell', 'pietruszka', None, None), ('till', 'koperek', None, None), ('paprika', 'papryka', None, None), ('salat (sałata)', 'sałata', None, None), ('spinat', 'szpinak', None, None), ('peet', 'burak', None, None)], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('äi', 'teść', None, None), ('ämm', 'teściowa', None, None), ('õemees', 'szwagier', None, None), ('vennapoeg', 'bratanek', None, None), ('õetütar', 'siostrzenica', None, None), ('orb', 'sierota', None, None), ('lesk', 'wdowa', None, None), ('peigmees', 'narzeczony', None, None), ('pulm', 'ślub', None, None), ('lahutus', 'rozwód', None, None), ('sünd', 'urodzenie', None, None), ('matus', 'pogrzeb', None, None), ('juuksur', 'fryzjer', None, None), ('pagar', 'piekarz', None, None), ('lihunik', 'rzeźnik', None, None), ('ettekandja (kelnerka)', 'kelnerka', None, None)], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('postiljon', 'listonosz', None, None), ('tuletõrjuja', 'strażak', None, None), ('kohtunik', 'sędzia', None, None), ('direktor', 'dyrektor', None, None)], 'sentences': []}]
# === /SŁOWNICTWO ===
