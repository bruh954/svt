"""Treść kursu: fiński dla Polaków."""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "ÄÄNNE · WYMOWA", "jezyk": "KIELI · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "Ä", "track": "wymowa",
     "letters": [
         ("ä", "[æ]: szerokie e, jak w ang. „cat”", "äiti (mama)"),
         ("ö", "[ø]: jak niemieckie ö: o z ustami ułożonymi do e", "työ (praca)"),
         ("y", "[y]: jak niemieckie ü: u z ustami ułożonymi do i", "kylä (wieś)"),
         ("h", "[h]: lekkie; przed spółgłoską twardsze", "hyvä (dobry)"),
         ("j", "[j]: jak polskie j", "joki (rzeka)"),
         ("v", "[ʋ]: jak polskie w", "vesi (woda)"),
         ("r", "[r]: mocno toczone", "ruoka (jedzenie)"),
         ("s", "[s]: zawsze jak polskie s, nigdy z", "sana (słowo)"),
         ("aa, ee, ii, oo, uu, yy, ää, öö", "długa samogłoska: dwa razy dłuższa", "maa (kraj)"),
         ("kk, pp, tt", "długa spółgłoska: zatrzymaj się na niej", "kukka (kwiat)"),
         ("ng", "[ŋŋ]: jak w polskim „bank” bez k", "kenkä (but)"),
         ("akcent", "zawsze na pierwszej sylabie", "kaupunki (miasto)"),
         ("harmonia samogłosek", "w słowie nie łączy się a, o, u z ä, ö, y", "kala, kylä"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "H", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("hei", "cześć", None, None),
         ("näkemiin", "do widzenia", None, "Dosł. „do zobaczenia”."),
         ("kiitos", "dziękuję", None, None),
         ("anteeksi", "przepraszam", None, None),
         ("kyllä", "tak", None, None),
         ("ei", "nie", None, None),
         ("hyvää", "dobrego", None, None),
         ("huomenta", "poranka", None, None),
         ("yötä", "nocy", None, None),
         ("paljon", "dużo; bardzo", None, None),
         ("ja", "i", None, None),
         ("selvä", "jasne; ok", None, None),
     ],
     "sentences": [
         (["hei", "!"], "Cześć!", {"näkemiin": "näkemiin to „do widzenia”."}),
         (["näkemiin", "!"], "Do widzenia!", {"hei": "hei to „cześć”."}),
         (["hyvää", "huomenta", "!"], "Dzień dobry (rano)!", {"yötä": "yötä to „nocy”."}),
         (["hyvää", "yötä", "!"], "Dobranoc!", {"huomenta": "huomenta to „poranka”."}),
         (["kiitos", "!"], "Dziękuję!", {}),
         (["kyllä", ",", "kiitos"], "Tak, dziękuję.", {"ei": "ei to „nie”."}),
         (["ei", ",", "kiitos"], "Nie, dziękuję.", {"kyllä": "kyllä to „tak”."}),
         (["kiitos", "paljon"], "Dziękuję bardzo.", {}),
         (["anteeksi", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "M", "track": "jezyk",
     "words": [
         ("minä", "ja", None, None),
         ("sinä", "ty", None, None),
         ("hän", "on; ona", None, "Nie ma rodzaju: „hän” znaczy on i ona."),
         ("olen", "jestem", None, None),
         ("olet", "jesteś", None, None),
         ("on", "jest", None, None),
         ("opiskelija", "student", None, None),
         ("opettaja", "nauczyciel", None, None),
         ("puolalainen", "Polak; Polka", None, None),
         ("Puolasta", "z Polski", None, "Końcówka -sta = „z”."),
         ("Suomesta", "z Finlandii", None, "Końcówka -sta = „z”."),
     ],
     "sentences": [
         (["minä", "olen", "opiskelija"], "Jestem studentem.", {"olet": "olet to „jesteś”. O sobie: olen."}),
         (["sinä", "olet", "opettaja"], "Jesteś nauczycielem.", {"olen": "olen to „jestem”. Do „sinä”: olet."}),
         (["hän", "on", "puolalainen"], "On jest Polakiem.", {}),
         (["minä", "olen", "puolalainen"], "Jestem Polakiem.", {}),
         (["minä", "olen", "Puolasta"], "Jestem z Polski.", {"Suomesta": "Suomesta to „z Finlandii”."}),
         (["hän", "on", "Suomesta"], "On jest z Finlandii.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "I", "track": "jezyk",
     "words": [
         ("äiti", "mama", None, None),
         ("isä", "tata", None, None),
         ("veli", "brat", None, None),
         ("sisko", "siostra", None, None),
         ("lapsi", "dziecko", None, None),
         ("ystävä", "przyjaciel", None, None),
         ("nainen", "kobieta", None, None),
         ("mies", "mężczyzna", None, None),
         ("minulla", "u mnie (mam)", None, "„Minulla on veli” = mam brata."),
         ("sinulla", "u ciebie (masz)", None, None),
         ("pieni", "mały", None, None),
         ("hyvä", "dobry", None, None),
     ],
     "sentences": [
         (["veli", "on", "pieni"], "Brat jest mały.", {}),
         (["sisko", "on", "hyvä"], "Siostra jest dobra.", {}),
         (["äiti", "on", "nainen"], "Mama jest kobietą.", {"mies": "mies to „mężczyzna”."}),
         (["minulla", "on", "veli"], "Mam brata.", {"sinulla": "sinulla to „u ciebie”. O sobie: minulla."}),
         (["sinulla", "on", "sisko"], "Masz siostrę.", {"minulla": "minulla to „u mnie”. Do „sinä”: sinulla."}),
         (["isä", "on", "mies"], "Tata jest mężczyzną.", {}),
         (["ystävä", "on", "hyvä"], "Przyjaciel jest dobry.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "K", "track": "jezyk",
     "words": [
         ("vesi", "woda", None, None),
         ("vettä", "wody", None, "Partitiivi: po „haluan”."),
         ("kahvi", "kawa", None, None),
         ("kahvia", "kawy", None, "Partitiivi."),
         ("tee", "herbata", None, None),
         ("teetä", "herbaty", None, "Partitiivi."),
         ("leipä", "chleb", None, None),
         ("leipää", "chleba", None, "Partitiivi."),
         ("kala", "ryba", None, None),
         ("kalaa", "ryby", None, "Partitiivi."),
         ("omena", "jabłko", None, None),
         ("omenaa", "jabłka", None, "Partitiivi."),
         ("haluan", "chcę", None, None),
         ("haluat", "chcesz", None, None),
         ("maukas", "smaczny", None, None),
         ("hyvin", "bardzo; dobrze", None, None),
         ("nyt", "teraz", None, None),
     ],
     "sentences": [
         (["minä", "haluan", "kahvia"], "Chcę kawę.", {"haluat": "haluat to „chcesz”. O sobie: haluan."}),
         (["sinä", "haluat", "teetä"], "Chcesz herbatę.", {"haluan": "haluan to „chcę”. Do „sinä”: haluat."}),
         (["minä", "haluan", "leipää"], "Chcę chleb.", {}),
         (["sinä", "haluat", "omenaa"], "Chcesz jabłko.", {}),
         (["kala", "on", "hyvin", "maukas"], "Ryba jest bardzo smaczna.", {}),
         (["nyt", "haluan", "vettä"], "Teraz chcę wodę.", {}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("kaksi", "dwa", None, None),
         ("kolme", "trzy", None, None),
         ("neljä", "cztery", None, None),
         ("viisi", "pięć", None, None),
         ("kymmenen", "dziesięć", None, None),
         ("lasta", "dzieci", None, "Po liczbie: partitiivi."),
         ("tänään", "dziś", None, None),
         ("huomenna", "jutro", None, None),
         ("eilen", "wczoraj", None, None),
         ("kello", "godzina; zegar", None, None),
         ("paljonko", "ile", None, None),
     ],
     "sentences": [
         (["minulla", "on", "kaksi", "lasta"], "Mam dwoje dzieci.", {}),
         (["minä", "haluan", "kolme", "omenaa"], "Chcę trzy jabłka.", {"kaksi": "kaksi to „dwa”. Chcesz trzy: kolme."}),
         (["paljonko", "kello", "on", "?"], "Która jest godzina?", {}),
         (["kello", "on", "kymmenen"], "Jest dziesiąta.", {"viisi": "viisi to „pięć”."}),
         (["tänään", "haluan", "kahvia"], "Dziś chcę kawę.", {"huomenna": "huomenna to „jutro”. Tu „dziś”: tänään."}),
         (["huomenna", "haluan", "kalaa"], "Jutro chcę rybę.", {"eilen": "eilen to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "P", "track": "jezyk",
     "words": [
         ("koti", "dom", None, None),
         ("kotiin", "do domu", None, "Końcówka -iin = „do”."),
         ("kaupunki", "miasto", None, None),
         ("katu", "ulica", None, None),
         ("koulu", "szkoła", None, None),
         ("meri", "morze", None, None),
         ("taksi", "taksówka", "taksówka", None),
         ("hotelli", "hotel", "hotel", None),
         ("missä", "gdzie", None, None),
         ("täällä", "tu", None, None),
         ("siellä", "tam", None, None),
         ("menen", "idę; jadę", None, None),
         ("Helsinkiin", "do Helsinek", None, None),
         ("oikealla", "po prawej", None, None),
         ("vasemmalla", "po lewej", None, None),
     ],
     "sentences": [
         (["missä", "hotelli", "on", "?"], "Gdzie jest hotel?", {"täällä": "täällä to „tu”. Pytasz „gdzie”: missä."}),
         (["hotelli", "on", "siellä"], "Hotel jest tam.", {"täällä": "täällä to „tu”. Tu „tam”: siellä."}),
         (["minä", "menen", "kotiin"], "Idę do domu.", {}),
         (["minä", "menen", "Helsinkiin"], "Jadę do Helsinek.", {}),
         (["taksi", "on", "oikealla"], "Taksówka jest po prawej.", {"vasemmalla": "vasemmalla to „po lewej”."}),
         (["koulu", "on", "siellä"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Czytaj tak, jak jest napisane", "chain": [],
                "text": "Fiński jest w pełni fonetyczny: jedna litera to jeden dźwięk, a akcent zawsze pada na pierwszą sylabę. Długość się liczy: tuli (ogień), tuuli (wiatr), tulli (cło) to trzy różne słowa."}],
    "ja": [{"title": "Brak rodzaju", "chain": [
                ("On jest Polakiem.", ["hän", "on", "puolalainen"], "„hän” = on lub ona."),
            ],
            "text": "Po fińsku nie ma rodzaju ani rodzajników. „Hän” znaczy on i ona. Czasownik „być”: olen, olet, on."}],
    "ludzie": [{"title": "Mam = u mnie jest", "chain": [],
                "text": "Nie ma czasownika „mieć”. Mówisz „u mnie jest”: minulla on veli (mam brata), sinulla on sisko (masz siostrę)."}],
    "jedzenie": [{"title": "Partitiivi", "chain": [],
                  "text": "Po „haluan” rzeczownik dostaje formę cząstkową: kahvi → kahvia, tee → teetä, vesi → vettä. Uczysz się jej razem ze słowem."}],
}

ENDINGS_INSIGHT = {"title": "Formy osobowe",
                   "text": "Po fińsku czasownik zmienia końcówkę: olen, olet, on; haluan, haluat. Tu to ćwiczysz."}

ENDINGS = [
    ("minä ", "ole", "n", " opiskelija", ["n", "t"], "ja jestem", "Do „minä” pasuje -n.", "ja"),
    ("sinä ", "ole", "t", " opettaja", ["n", "t"], "ty jesteś", "Do „sinä” pasuje -t.", "ja"),
    ("minä ", "halua", "n", " kahvia", ["n", "t"], "ja chcę", "Do „minä” pasuje -n.", "jedzenie"),
    ("sinä ", "halua", "t", " teetä", ["n", "t"], "ty chcesz", "Do „sinä” pasuje -t.", "jedzenie"),
    ("", "minul", "la", " on veli", ["la", "lla"], "u mnie", "minulla: -lla = „u”.", "ludzie"),
    ("", "sinul", "la", " on sisko", ["la", "lla"], "u ciebie", "sinulla: -lla = „u”.", "ludzie"),
    ("minä menen ", "", "kotiin", "", ["kotiin", "kotona"], "do domu", "-iin = „do”.", "miejsca"),
]

CHAT_EXTRA = {"Aino": "Aino (imię)", "Mikko": "Mikko (imię)", "taksikuski": "kierowca", "minne": "dokąd", "menet": "idziesz; jedziesz", "kotona": "w domu"}

CHATS = [
    {"id": "kahvila", "title": "W kawiarni", "partner": "Aino", "avatar": "A", "requires": "jedzenie",
     "turns": [
         {"bot": ["hyvää", "huomenta", "!"], "en": "Dzień dobry!",
          "options": [(["hyvää", "huomenta", "!"], True, None), (["hyvää", "yötä", "!"], False, "hyvää yötä to „dobranoc”. Jest rano.")]},
         {"bot": ["kahvia", "?"], "en": "Kawy?",
          "options": [(["kyllä", ",", "minä", "haluan", "kahvia"], True, None),
                      (["kyllä", ",", "sinä", "haluat", "kahvia"], False, "haluat jest do „sinä”. O sobie: haluan.")]},
         {"bot": ["ja", "leipää", "?"], "en": "I chleba?",
          "options": [(["ei", ",", "kiitos"], True, None),
                      (["anteeksi", "!"], False, "anteeksi to „przepraszam”. Odmów: ei, kiitos.")]},
         {"bot": ["selvä", "!"], "build": (["kiitos", "!"], "Dziękuję!"), "en": "Jasne!"},
     ]},
    {"id": "tutustuminen", "title": "Poznajemy się", "partner": "Mikko", "avatar": "M", "requires": "ludzie",
     "turns": [
         {"bot": ["hei", "!"], "en": "Cześć!",
          "options": [(["hei", "!"], True, None), (["anteeksi", "!"], False, "anteeksi to „przepraszam”. Powitaj: hei.")]},
         {"bot": ["sinä", "olet", "Suomesta", "?"], "en": "Jesteś z Finlandii?",
          "options": [(["ei", ",", "minä", "olen", "Puolasta"], True, None),
                      (["ei", ",", "minä", "olet", "Puolasta"], False, "olet jest do „sinä”. O sobie: olen.")]},
         {"bot": ["sinulla", "on", "veli", "?"], "en": "Masz brata?",
          "options": [(["kyllä", ",", "minulla", "on", "veli"], True, None),
                      (["kyllä", ",", "sinulla", "on", "veli"], False, "sinulla to „u ciebie”. O sobie: minulla.")]},
         {"bot": ["näkemiin", "!"], "build": (["näkemiin", "!"], "Do widzenia!"), "en": "Do widzenia!"},
     ]},
    {"id": "taksi", "title": "W taksówce", "partner": "taksikuski", "avatar": "T", "requires": "miejsca",
     "turns": [
         {"bot": ["hyvää", "huomenta", "!"], "en": "Dzień dobry!",
          "options": [(["hyvää", "huomenta", "!"], True, None), (["hyvää", "yötä", "!"], False, "hyvää yötä to „dobranoc”. Jest rano.")]},
         {"bot": ["minne", "sinä", "menet", "?"], "en": "Dokąd jedziesz?",
          "options": [(["minä", "menen", "Helsinkiin"], True, None),
                      (["minä", "menet", "Helsinkiin"], False, "menet to „idziesz”. O sobie: menen.")]},
         {"bot": ["hotelli", "on", "siellä", "."], "en": "Hotel jest tam.",
          "options": [(["oikealla", "?"], True, None), (["täällä", "?"], False, "Pytasz o kierunek: oikealla.")]},
         {"bot": ["kyllä", "!"], "build": (["kiitos", "!"], "Dziękuję!"), "en": "Tak!"},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['minä', 'sinä', 'hän', 'me', 'te', 'he'],
    'przyp': ['nominatiivi', 'genetiivi (czyj?)', 'partitiivi', 'inessiivi (w)', 'elatiivi (z)', 'illatiivi (do)', 'adessiivi (na, u)', 'ablatiivi (od)', 'allatiivi (na, komu)'],
    'im': ['-va (czynny teraźniejszy)', '-nut (czynny przeszły)', '-ttava (bierny teraźniejszy)', '-ttu (bierny przeszły)'],
    't_part': ['talo (dom)', 'vesi (woda)', 'kahvi (kawa)', 'tee (herbata)', 'leipä (chleb)', 'nainen (kobieta)'],
    't_harm': ['talo (dom)', 'kylä (wieś)', 'koulu (szkoła)', 'metsä (las)', 'kauppa (sklep)', 'työ (praca)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'puhua (mówić): typ 1', 'os', 'puhun; puhut; puhuu; puhumme; puhutte; puhuvat', 'Końcówki: -n, -t, wydłużenie samogłoski, -mme, -tte, -vat.'),
    ('conj', 'Wzory koniugacji', 'asua (mieszkać): typ 1', 'os', 'asun; asut; asuu; asumme; asutte; asuvat', None),
    ('conj', 'Wzory koniugacji', 'syödä (jeść): typ 2', 'os', 'syön; syöt; syö; syömme; syötte; syövät', 'Typ 2 (-da/-dä): w 3. osobie bez wydłużenia.'),
    ('conj', 'Wzory koniugacji', 'tulla (przychodzić): typ 3', 'os', 'tulen; tulet; tulee; tulemme; tulette; tulevat', 'Typ 3: przed końcówką pojawia się -e-.'),
    ('conj', 'Wzory koniugacji', 'mennä (iść): typ 3', 'os', 'menen; menet; menee; menemme; menette; menevät', None),
    ('conj', 'Wzory koniugacji', 'haluta (chcieć): typ 4', 'os', 'haluan; haluat; haluaa; haluamme; haluatte; haluavat', 'Typ 4: -ta odpada, dochodzi -a-.'),
    ('conj', 'Czasowniki nieregularne', 'olla (być)', 'os', 'olen; olet; on; olemme; olette; ovat', None),
    ('conj', 'Czasowniki nieregularne', 'tehdä (robić)', 'os', 'teen; teet; tekee; teemme; teette; tekevät', 'k wraca w 3. osobie: tekee, tekevät.'),
    ('conj', 'Czasowniki nieregularne', 'nähdä (widzieć)', 'os', 'näen; näet; näkee; näemme; näette; näkevät', None),
    ('conj', 'Przeczenie', 'olla: nie być', 'os', 'en ole; et ole; ei ole; emme ole; ette ole; eivät ole', 'Odmienia się słowo przeczące, czasownik zostaje w temacie.'),
    ('decl', 'Wzory deklinacji', 'talo (dom)', 'przyp', 'talo; talon; taloa; talossa; talosta; taloon; talolla; talolta; talolle', None),
    ('decl', 'Wzory deklinacji', 'koulu (szkoła)', 'przyp', 'koulu; koulun; koulua; koulussa; koulusta; kouluun; koululla; koululta; koululle', None),
    ('decl', 'Wyjątki', 'kaupunki (miasto)', 'przyp', 'kaupunki; kaupungin; kaupunkia; kaupungissa; kaupungista; kaupunkiin; kaupungilla; kaupungilta; kaupungille', 'Wymiana stopnia: nk → ng w zamkniętej sylabie.'),
    ('decl', 'Wyjątki', 'vesi (woda)', 'przyp', 'vesi; veden; vettä; vedessä; vedestä; veteen; vedellä; vedeltä; vedelle', None),
    ('decl', 'Wyjątki', 'käsi (ręka)', 'przyp', 'käsi; käden; kättä; kädessä; kädestä; käteen; kädellä; kädeltä; kädelle', None),
    ('decl', 'Wyjątki', 'nainen (kobieta)', 'przyp', 'nainen; naisen; naista; naisessa; naisesta; naiseen; naisella; naiselta; naiselle', 'Słowa na -nen: temat -se-.'),
    ('decl', 'Zaimki', 'minä (ja)', 'przyp', 'minä; minun; minua; minussa; minusta; minuun; minulla; minulta; minulle', None),
    ('form', 'Imiesłowy', 'puhua (mówić)', 'im', 'puhuva; puhunut; puhuttava; puhuttu', None),
    ('form', 'Imiesłowy', 'syödä (jeść)', 'im', 'syövä; syönyt; syötävä; syöty', None),
    ('form', 'Imiesłowy', 'tehdä (robić)', 'im', 'tekevä; tehnyt; tehtävä; tehty', None),
    ('conj', 'Czas przeszły', 'puhua: imperfekti', 'os', 'puhuin; puhuit; puhui; puhuimme; puhuitte; puhuivat', 'Znak czasu przeszłego: -i-.'),
    ('conj', 'Czas przeszły', 'olla: imperfekti', 'os', 'olin; olit; oli; olimme; olitte; olivat', None),
    ('form', 'Typowe trudności', 'Partitiivi: jaka forma?', 't_part', 'taloa; vettä; kahvia; teetä; leipää; naista', None),
    ('form', 'Typowe trudności', 'Harmonia: „w…” (-ssa czy -ssä)', 't_harm', 'talossa; kylässä; koulussa; metsässä; kaupassa; työssä', 'Zwróć uwagę na kauppa → kaupassa: pp słabnie do p.'),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['kauppa (sklep)', 'katu (ulica)', 'kaupunki (miasto)', 'pöytä (stół)', 'kukka (kwiat)', 'tyttö (dziewczyna)', 'lintu (ptak)', 'ranta (brzeg)'],
    't_m1': ['tuli', 'tuuli', 'tulli', 'tapaan', 'tapan', 'kuka', 'kukka', 'mutta'],
    't_m2': ['minä', 'sinä', 'hän', 'me', 'te', 'he'],
    't_m3': ['yksi (1)', 'kaksi (2)', 'kolme (3)', 'viisi (5)', 'kymmenen (10)', 'monta (ile)'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Stopniowanie spółgłosek: genetiivi', 't_m0', 'kaupan; kadun; kaupungin; pöydän; kukan; tytön; linnun; rannan', 'pp → p, t → d, nk → ng, kk → k, tt → t, nt → nn.'),
    ('form', 'Typowe trudności', 'Długość: co to znaczy?', 't_m1', 'ogień; wiatr; cło; spotykam; zabijam; kto; kwiat; ale', 'Podwójną literę trzeba wymówić wyraźnie dłużej.'),
    ('form', 'Typowe trudności', 'Przeczenie: puhua', 't_m2', 'en puhu; et puhu; ei puhu; emme puhu; ette puhu; eivät puhu', 'Odmienia się słowo przeczące, czasownik zostaje w temacie.'),
    ('form', 'Typowe trudności', 'Liczba + rzeczownik', 't_m3', 'yksi talo; kaksi taloa; kolme taloa; viisi taloa; kymmenen taloa; monta taloa', 'Po liczbach od 2 w górę stoi partitiivi liczby pojedynczej.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['To jest mały dom.', 'Nie mam czasu.', 'Nie mówię po fińsku.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: przeczenie i przymiotnik', 't_s0', 'Tämä on pieni talo.|Tämä on talo pieni.|On tämä pieni talo.|Tämä pieni on talo.; Minulla ei ole aikaa.|Minulla on ei aikaa.|Minulla ole ei aikaa.|Minulla ei on aikaa.; En puhu suomea.|Puhu en suomea.|En suomea puhu.|Suomea puhu en.', 'Przymiotnik przed rzeczownikiem. Przeczenie jest odmienianym czasownikiem (en, et, ei), a główny czasownik zostaje w temacie.'),
]

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'sinä (ty)', 'przyp', 'sinä; sinun; sinua; sinussa; sinusta; sinuun; sinulla; sinulta; sinulle', None),
    ('decl', 'Zaimki', 'hän (on, ona)', 'przyp', 'hän; hänen; häntä; hänessä; hänestä; häneen; hänellä; häneltä; hänelle', 'Hän to osoba; „to” o rzeczy to se.'),
    ('decl', 'Zaimki', 'me (my)', 'przyp', 'me; meidän; meitä; meissä; meistä; meihin; meillä; meiltä; meille', None),
    ('decl', 'Zaimki', 'te (wy)', 'przyp', 'te; teidän; teitä; teissä; teistä; teihin; teillä; teiltä; teille', None),
    ('decl', 'Zaimki', 'he (oni)', 'przyp', 'he; heidän; heitä; heissä; heistä; heihin; heillä; heiltä; heille', None),
    ('decl', 'Zaimki', 'se (to, ono)', 'przyp', 'se; sen; sitä; siinä; siitä; siihen; sillä; siltä; sille', 'Mówiąc o rzeczach i w mowie potocznej o ludziach.'),
    ('decl', 'Zaimki', 'tämä (ten tu)', 'przyp', 'tämä; tämän; tätä; tässä; tästä; tähän; tällä; tältä; tälle', None),
    ('decl', 'Zaimki', 'kuka (kto)', 'przyp', 'kuka; kenen; ketä; kenessä; kenestä; keneen; kenellä; keneltä; kenelle', None),
    ('decl', 'Zaimki', 'mikä (co, który)', 'przyp', 'mikä; minkä; mitä; missä; mistä; mihin; millä; miltä; mille', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'hyvä (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'hyvä; parempi; paras', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'suuri (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'suuri; suurempi; suurin', None),
    ('form', 'Stopniowanie', 'pieni (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'pieni; pienempi; pienin', None),
    ('form', 'Stopniowanie', 'vanha (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'vanha; vanhempi; vanhin', None),
    ('form', 'Stopniowanie', 'kaunis (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'kaunis; kauniimpi; kaunein', 'Temat kauniin- przed -mpi.'),
    ('form', 'Stopniowanie', 'nopea (szybki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'nopea; nopeampi; nopein', None),
    ('form', 'Stopniowanie', 'korkea (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'korkea; korkeampi; korkein', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 2 (generowane) ===
PARADIGMS += [
    ('conj', 'Czas przeszły', 'puhua: perfekti (powiedziałem)', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'olen puhunut; olet puhunut; on puhunut; olemme puhuneet; olette puhuneet; ovat puhuneet', None),
    ('conj', 'Czas przeszły', 'mennä: imperfekti (poszedłem)', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'menin; menit; meni; menimme; menitte; menivät', None),
    ('conj', 'Czas przeszły', 'tulla: imperfekti (przyszedłem)', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'tulin; tulit; tuli; tulimme; tulitte; tulivat', None),
    ('conj', 'Czas przeszły', 'syödä: imperfekti (zjadłem)', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'söin; söit; söi; söimme; söitte; söivät', None),
    ('conj', 'Tryb warunkowy', 'puhua: kondicionaali', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'puhuisin; puhuisit; puhuisi; puhuisimme; puhuisitte; puhuisivat', None),
    ('conj', 'Tryb warunkowy', 'olla: kondicionaali', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'olisin; olisit; olisi; olisimme; olisitte; olisivat', None),
    ('conj', 'Tryb warunkowy', 'haluta: kondicionaali', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'haluaisin; haluaisit; haluaisi; haluaisimme; haluaisitte; haluaisivat', 'Grzeczna prośba: Haluaisin kahvia.'),
    ('conj', 'Wzory koniugacji', 'lukea (czytać): typ 3', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'luen; luet; lukee; luemme; luette; lukevat', None),
    ('conj', 'Wzory koniugacji', 'tarvita (potrzebować): typ 5', ['minä', 'sinä', 'hän', 'me', 'te', 'he'], 'tarvitsen; tarvitset; tarvitsee; tarvitsemme; tarvitsette; tarvitsevat', None),
    ('form', 'Przypadki (10)', 'kala (ryba)', ['mianownik', 'dopełniacz', 'partitiivi', 'inessiivi (w)', 'elatiivi (z)', 'illatiivi (do)', 'adessiivi (na, u)', 'ablatiivi (od)', 'allatiivi (na, do)', 'translatiivi (w co)'], 'kala; kalan; kalaa; kalassa; kalasta; kalaan; kalalla; kalalta; kalalle; kalaksi', None),
    ('form', 'Przypadki (10)', 'kirja (książka)', ['mianownik', 'dopełniacz', 'partitiivi', 'inessiivi (w)', 'elatiivi (z)', 'illatiivi (do)', 'adessiivi (na, u)', 'ablatiivi (od)', 'allatiivi (na, do)', 'translatiivi (w co)'], 'kirja; kirjan; kirjaa; kirjassa; kirjasta; kirjaan; kirjalla; kirjalta; kirjalle; kirjaksi', None),
    ('form', 'Przypadki (10)', 'päivä (dzień)', ['mianownik', 'dopełniacz', 'partitiivi', 'inessiivi (w)', 'elatiivi (z)', 'illatiivi (do)', 'adessiivi (na, u)', 'ablatiivi (od)', 'allatiivi (na, do)', 'translatiivi (w co)'], 'päivä; päivän; päivää; päivässä; päivästä; päivään; päivällä; päivältä; päivälle; päiväksi', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 2 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('poika', 'chłopiec', None, None), ('tyttö', 'dziewczynka', None, None), ('ihminen', 'człowiek', None, None), ('ihmiset', 'ludzie', None, None), ('perhe', 'rodzina', None, None), ('poika (syn)', 'syn', None, None), ('tytär', 'córka', None, None), ('isoisä', 'dziadek', None, None), ('isoäiti', 'babcia', None, None), ('lapsenlapsi', 'wnuk', None, None), ('setä', 'wujek', None, None), ('täti', 'ciocia', None, None), ('serkku', 'kuzyn', None, None), ('aviomies', 'mąż', None, None), ('vaimo', 'żona', None, None), ('naapuri', 'sąsiad', None, None)], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('vieras', 'gość', None, None), ('pomo', 'szef', None, None), ('työkaveri', 'kolega', None, None), ('vihollinen', 'wróg', None, None), ('kuningas', 'król', None, None), ('kuningatar', 'królowa', None, None)], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('pää', 'głowa', None, None), ('kasvot', 'twarz', None, None), ('silmä', 'oko', None, None), ('korva', 'ucho', None, None), ('nenä', 'nos', None, None), ('suu', 'usta', None, None), ('hammas', 'ząb', None, None), ('kieli', 'język (narząd)', None, None), ('hiukset', 'włosy', None, None), ('kaula', 'szyja', None, None), ('olkapää', 'ramię', None, None), ('käsi', 'ręka', None, None), ('sormi', 'palec', None, None), ('jalka', 'noga', None, None), ('jalkaterä', 'stopa', None, None), ('polvi', 'kolano', None, None)], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('selkä', 'plecy', None, None), ('vatsa', 'brzuch', None, None), ('sydän', 'serce', None, None), ('veri', 'krew', None, None), ('luu', 'kość', None, None), ('iho', 'skóra', None, None), ('ääni', 'głos', None, None), ('keho', 'ciało', None, None), ('maha', 'żołądek', None, None), ('parta', 'broda', None, None), ('huuli', 'warga', None, None), ('kynsi', 'paznokieć', None, None), ('rinta', 'pierś', None, None), ('aivot', 'mózg', None, None)], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('voi', 'masło', None, None), ('juusto', 'ser', None, None), ('maito', 'mleko', None, None), ('muna', 'jajko', None, None), ('liha', 'mięso', None, None), ('kana', 'kurczak', None, None), ('sianliha', 'wieprzowina', None, None), ('keitto', 'zupa', None, None), ('salaatti', 'sałatka', None, None), ('riisi', 'ryż', None, None), ('pasta', 'makaron', None, None), ('peruna', 'ziemniak', None, None), ('porkkana', 'marchewka', None, None), ('sipuli', 'cebula', None, None), ('valkosipuli', 'czosnek', None, None), ('tomaatti', 'pomidor', None, None)], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('kurkku', 'ogórek', None, None), ('päärynä', 'gruszka', None, None), ('banaani', 'banan', None, None), ('appelsiini', 'pomarańcza', None, None), ('sitruuna', 'cytryna', None, None), ('mansikka', 'truskawka', None, None), ('viinirypäle', 'winogrono', None, None), ('sokeri', 'cukier', None, None), ('suola', 'sól', None, None), ('pippuri', 'pieprz', None, None), ('öljy', 'olej', None, None), ('jauho', 'mąka', None, None), ('hunaja', 'miód', None, None), ('suklaa', 'czekolada', None, None), ('jäätelö', 'lody', None, None), ('kakku', 'ciasto (tort)', None, None)], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('keksi', 'ciastko', None, None), ('aamiainen', 'śniadanie', None, None), ('lounas', 'obiad', None, None), ('illallinen', 'kolacja', None, None), ('välipala', 'przekąska', None, None)], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('mehu', 'sok', None, None), ('olut', 'piwo', None, None), ('viini', 'wino', None, None), ('juoma', 'napój', None, None), ('lasi', 'szklanka', None, None), ('kuppi', 'filiżanka', None, None), ('lautanen', 'talerz', None, None), ('veitsi', 'nóż', None, None), ('haarukka', 'widelec', None, None), ('lusikka', 'łyżka', None, None), ('pullo', 'butelka', None, None), ('ruokalista', 'menu', None, None), ('lasku', 'rachunek', None, None), ('juomaraha', 'napiwek', None, None), ('pöytä (w restauracji)', 'stolik', None, None), ('tarjoilija', 'kelner', None, None)], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('kokki', 'kucharz', None, None), ('nälkäinen', 'głodny', None, None), ('janoinen', 'spragniony', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('talo', 'dom', None, None), ('asunto', 'mieszkanie', None, None), ('huone', 'pokój', None, None), ('keittiö', 'kuchnia', None, None), ('kylpyhuone', 'łazienka', None, None), ('makuuhuone', 'sypialnia', None, None), ('olohuone', 'salon', None, None), ('puutarha', 'ogród', None, None), ('ovi', 'drzwi', None, None), ('ikkuna', 'okno', None, None), ('seinä', 'ściana', None, None), ('lattia', 'podłoga', None, None), ('katto', 'dach', None, None), ('portaat', 'schody', None, None), ('avain', 'klucz', None, None), ('pöytä', 'stół', None, None)], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('tuoli', 'krzesło', None, None), ('sänky', 'łóżko', None, None), ('kaappi', 'szafa', None, None), ('lamppu', 'lampa', None, None), ('matto', 'dywan', None, None), ('peili', 'lustro', None, None), ('televisio', 'telewizor', None, None), ('puhelin', 'telefon', None, None), ('tietokone', 'komputer', None, None), ('tyyny', 'poduszka', None, None), ('peitto', 'koc', None, None), ('pyyhe', 'ręcznik', None, None), ('saippua', 'mydło', None, None), ('hammasharja', 'szczoteczka do zębów', None, None), ('jääkaappi', 'lodówka', None, None), ('uuni', 'piec', None, None)], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('pesukone', 'pralka', None, None), ('roskat', 'śmieci', None, None)], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('vaate', 'ubranie', None, None), ('paita', 'koszula', None, None), ('housut', 'spodnie', None, None), ('mekko', 'sukienka', None, None), ('hame', 'spódnica', None, None), ('takki', 'kurtka', None, None), ('päällystakki', 'płaszcz', None, None), ('villapaita', 'sweter', None, None), ('kengät', 'buty', None, None), ('sukat', 'skarpetki', None, None), ('lakki', 'czapka', None, None), ('hattu', 'kapelusz', None, None), ('hanskat', 'rękawiczki', None, None), ('huivi', 'szalik', None, None), ('laukku', 'torba', None, None), ('reppu', 'plecak', None, None)], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('lompakko', 'portfel', None, None), ('silmälasit', 'okulary', None, None), ('rannekello', 'zegarek', None, None), ('sormus', 'pierścionek', None, None), ('alusvaatteet', 'bielizna', None, None), ('pyjama', 'piżama', None, None), ('vyö', 'pasek', None, None), ('solmio', 'krawat', None, None), ('puku', 'garnitur', None, None)], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('punainen', 'czerwony', None, None), ('sininen', 'niebieski', None, None), ('vihreä', 'zielony', None, None), ('keltainen', 'żółty', None, None), ('musta', 'czarny', None, None), ('valkoinen', 'biały', None, None), ('harmaa', 'szary', None, None), ('ruskea', 'brązowy', None, None), ('vaaleanpunainen', 'różowy', None, None), ('violetti', 'fioletowy', None, None), ('väri', 'kolor', None, None), ('pyöreä', 'okrągły', None, None), ('neliö (kwadratowy)', 'kwadratowy', None, None), ('suora', 'prosty', None, None), ('vino', 'krzywy', None, None), ('viiva', 'linia', None, None)], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('piste', 'punkt', None, None), ('ympyrä', 'koło', None, None)], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('nolla', 'zero', None, None), ('yksitoista', 'jedenaście', None, None), ('kaksitoista', 'dwanaście', None, None), ('kolmetoista', 'trzynaście', None, None), ('neljätoista', 'czternaście', None, None), ('viisitoista', 'piętnaście', None, None), ('kuusitoista', 'szesnaście', None, None), ('seitsemäntoista', 'siedemnaście', None, None), ('kahdeksantoista', 'osiemnaście', None, None), ('yhdeksäntoista', 'dziewiętnaście', None, None), ('kaksikymmentä', 'dwadzieścia', None, None), ('kolmekymmentä', 'trzydzieści', None, None), ('neljäkymmentä', 'czterdzieści', None, None), ('viisikymmentä', 'pięćdziesiąt', None, None), ('kuusikymmentä', 'sześćdziesiąt', None, None), ('seitsemänkymmentä', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('kahdeksankymmentä', 'osiemdziesiąt', None, None), ('yhdeksänkymmentä', 'dziewięćdziesiąt', None, None), ('sata', 'sto', None, None), ('tuhat', 'tysiąc', None, None), ('miljoona', 'milion', None, None), ('ensimmäinen', 'pierwszy', None, None), ('toinen', 'drugi', None, None), ('kolmas', 'trzeci', None, None), ('puolikas', 'połowa', None, None), ('pari', 'para', None, None), ('muutama', 'kilka', None, None), ('monta', 'wiele', None, None), ('vähän', 'mało', None, None), ('koko', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('sekunti', 'sekunda', None, None), ('minuutti', 'minuta', None, None), ('tunti', 'godzina', None, None), ('päivä', 'dzień', None, None), ('yö', 'noc', None, None), ('viikko', 'tydzień', None, None), ('kuukausi', 'miesiąc', None, None), ('vuosi', 'rok', None, None), ('kevät', 'wiosna', None, None), ('kesä', 'lato', None, None), ('syksy', 'jesień', None, None), ('talvi', 'zima', None, None), ('maanantai', 'poniedziałek', None, None), ('tiistai', 'wtorek', None, None), ('keskiviikko', 'środa', None, None), ('torstai', 'czwartek', None, None)], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('perjantai', 'piątek', None, None), ('lauantai', 'sobota', None, None), ('sunnuntai', 'niedziela', None, None), ('tammikuu', 'styczeń', None, None), ('helmikuu', 'luty', None, None), ('maaliskuu', 'marzec', None, None), ('huhtikuu', 'kwiecień', None, None), ('toukokuu', 'maj', None, None), ('kesäkuu', 'czerwiec', None, None), ('heinäkuu', 'lipiec', None, None), ('elokuu', 'sierpień', None, None), ('syyskuu', 'wrzesień', None, None), ('lokakuu', 'październik', None, None), ('marraskuu', 'listopad', None, None), ('joulukuu', 'grudzień', None, None), ('aamu', 'rano (pora dnia)', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('keskipäivä', 'południe', None, None), ('illalla', 'wieczorem', None, None), ('aina', 'zawsze', None, None), ('ei koskaan', 'nigdy', None, None), ('joskus', 'czasem', None, None), ('usein', 'często', None, None), ('jo', 'już', None, None), ('vielä', 'jeszcze', None, None), ('pian', 'wkrótce', None, None), ('myöhemmin', 'później', None, None), ('aikaisin', 'wcześnie', None, None), ('myöhään', 'późno', None, None), ('milloin', 'kiedy (pytanie)', None, None), ('päivämäärä', 'data', None, None), ('menneisyys', 'przeszłość', None, None), ('tulevaisuus', 'przyszłość', None, None)], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('syntymäpäivä', 'urodziny', None, None), ('juhla', 'święto', None, None), ('loma', 'wakacje', None, None)], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('aurinko', 'słońce', None, None), ('kuu', 'księżyc', None, None), ('tähti', 'gwiazda', None, None), ('taivas', 'niebo', None, None), ('pilvi', 'chmura', None, None), ('sade', 'deszcz', None, None), ('lumi', 'śnieg', None, None), ('tuuli', 'wiatr', None, None), ('myrsky', 'burza', None, None), ('sumu', 'mgła', None, None), ('jää', 'lód', None, None), ('tuli, ziemia (planeta', 'ogień', None, None), ('maa', 'grunt)', None, None), ('joki', 'rzeka', None, None), ('järvi', 'jezioro', None, None), ('vuori', 'góra', None, None)], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('metsä', 'las', None, None), ('puu', 'drzewo', None, None), ('kukka', 'kwiat', None, None), ('ruoho', 'trawa', None, None), ('lehti', 'liść', None, None), ('pelto', 'pole', None, None), ('saari', 'wyspa', None, None), ('ranta', 'plaża', None, None), ('autiomaa', 'pustynia', None, None), ('kallio', 'skała', None, None), ('kivi', 'kamień', None, None), ('sää', 'pogoda', None, None), ('lämpötila', 'temperatura', None, None), ('kylmä', 'zimny', None, None), ('lämmin', 'ciepły', None, None), ('kuuma', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('koira', 'pies', None, None), ('kissa', 'kot', None, None), ('hevonen', 'koń', None, None), ('lehmä', 'krowa', None, None), ('sika', 'świnia', None, None), ('lammas', 'owca', None, None), ('vuohi', 'koza', None, None), ('kana (kura)', 'kura', None, None), ('ankka', 'kaczka', None, None), ('lintu', 'ptak', None, None), ('hiiri', 'mysz', None, None), ('rotta', 'szczur', None, None), ('käärme', 'wąż', None, None), ('sammakko', 'żaba', None, None), ('leijona', 'lew', None, None), ('tiikeri', 'tygrys', None, None)], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('norsu', 'słoń', None, None), ('karhu', 'niedźwiedź', None, None), ('susi', 'wilk', None, None), ('kettu', 'lis', None, None), ('jänis', 'zając', None, None), ('hirvi', 'jeleń', None, None), ('apina', 'małpa', None, None), ('perhonen', 'motyl', None, None), ('mehiläinen', 'pszczoła', None, None), ('kärpänen', 'mucha', None, None), ('hämähäkki', 'pająk', None, None), ('eläin', 'zwierzę', None, None), ('hyönteinen', 'owad', None, None)], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('kylä', 'wieś', None, None), ('tie', 'droga', None, None), ('tori', 'plac', None, None), ('silta', 'most', None, None), ('puisto', 'park', None, None), ('kauppa', 'sklep', None, None), ('kauppahalli', 'targ', None, None), ('supermarketti', 'supermarket', None, None), ('pankki', 'bank', None, None), ('posti', 'poczta', None, None), ('sairaala', 'szpital', None, None), ('apteekki', 'apteka', None, None), ('yliopisto', 'uniwersytet', None, None), ('kirjasto', 'biblioteka', None, None), ('museo', 'muzeum', None, None), ('kirkko', 'kościół', None, None)], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('ravintola', 'restauracja', None, None), ('kahvila', 'kawiarnia', None, None), ('lentokenttä', 'lotnisko', None, None), ('asema', 'dworzec', None, None), ('pysäkki', 'przystanek', None, None), ('elokuvateatteri', 'kino', None, None), ('teatteri', 'teatr', None, None), ('poliisi', 'policja', None, None), ('toimisto', 'biuro', None, None), ('tehdas', 'fabryka', None, None), ('rakennus', 'budynek', None, None), ('torni', 'wieża', None, None), ('keskusta', 'centrum', None, None), ('osoite', 'adres', None, None), ('kartta', 'mapa', None, None)], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('auto', 'samochód', None, None), ('bussi', 'autobus', None, None), ('juna', 'pociąg', None, None), ('raitiovaunu', 'tramwaj', None, None), ('metro', 'metro', None, None), ('lentokone', 'samolot', None, None), ('laiva', 'statek', None, None), ('polkupyörä', 'rower', None, None), ('moottoripyörä', 'motocykl', None, None), ('lippu', 'bilet', None, None), ('matka', 'podróż', None, None), ('retki', 'wycieczka', None, None), ('passi', 'paszport', None, None), ('matkalaukku', 'walizka', None, None), ('bensiini', 'benzyna', None, None), ('pysäköinti', 'parking', None, None)], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('risteys', 'skrzyżowanie', None, None), ('liikennevalot', 'światła', None, None), ('ajokortti', 'prawo jazdy', None, None), ('kuljettaja', 'kierowca', None, None), ('matkustaja', 'pasażer', None, None), ('sisäänajo', 'wjazd', None, None), ('uloskäynti', 'wyjazd', None, None), ('rautatie', 'kolej', None, None), ('satama', 'port', None, None), ('raja', 'granica', None, None)], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('työ', 'praca', None, None), ('ammatti', 'zawód', None, None), ('lääkäri', 'lekarz', None, None), ('sairaanhoitaja', 'pielęgniarka', None, None), ('oppilas', 'uczeń', None, None), ('insinööri', 'inżynier', None, None), ('lakimies', 'prawnik', None, None), ('poliisi (policjant)', 'policjant', None, None), ('sotilas', 'żołnierz', None, None), ('maanviljelijä', 'rolnik', None, None), ('myyjä', 'sprzedawca', None, None), ('kassa (kasjer)', 'kasjer', None, None), ('näyttelijä', 'aktor', None, None), ('kirjailija', 'pisarz', None, None), ('taidemaalari', 'malarz', None, None), ('muusikko', 'muzyk', None, None)], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('taiteilija', 'artysta', None, None), ('yritys', 'firma', None, None), ('raha', 'pieniądze', None, None), ('palkka', 'pensja', None, None), ('sopimus', 'umowa', None, None), ('tapaaminen', 'spotkanie', None, None), ('oppitunti', 'lekcja', None, None), ('koe', 'egzamin', None, None), ('arvosana', 'ocena', None, None), ('luokka', 'klasa', None, None), ('kirja', 'książka', None, None), ('vihko', 'zeszyt', None, None), ('kuulakärkikynä', 'długopis', None, None), ('lyijykynä', 'ołówek', None, None), ('paperi', 'papier', None, None), ('taulu', 'tablica', None, None)], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('sanakirja', 'słownik', None, None), ('kysymys', 'pytanie', None, None), ('vastaus', 'odpowiedź', None, None), ('tehtävä', 'zadanie', None, None), ('testi', 'test', None, None)], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('hinta', 'cena', None, None), ('maksukortti', 'karta (płatnicza)', None, None), ('käteinen', 'gotówka', None, None), ('kolikko', 'moneta', None, None), ('seteli', 'banknot', None, None), ('vaihtoraha', 'reszta', None, None), ('alennus', 'zniżka', None, None), ('kori', 'koszyk', None, None), ('kuitti', 'paragon', None, None), ('tavara', 'towar', None, None), ('osto', 'zakup', None, None), ('myynti', 'sprzedaż', None, None), ('arvo', 'wartość', None, None), ('laina', 'kredyt', None, None), ('velka', 'dług', None, None), ('vero', 'podatek', None, None)], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('rikkaus', 'bogactwo', None, None), ('köyhä', 'biedny', None, None), ('rikas', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('terveys', 'zdrowie', None, None), ('sairaus', 'choroba', None, None), ('kipu', 'ból', None, None), ('kuume', 'gorączka', None, None), ('yskä', 'kaszel', None, None), ('nuha', 'katar', None, None), ('lääke', 'lekarstwo', None, None), ('tabletti', 'tabletka', None, None), ('leikkaus', 'operacja', None, None), ('haava', 'rana', None, None), ('onnettomuus', 'wypadek', None, None), ('terve', 'zdrowy', None, None), ('sairas', 'chory', None, None), ('väsynyt', 'zmęczony', None, None), ('uninen', 'śpiący', None, None), ('vahva', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('heikko', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('ilo', 'radość', None, None), ('suru', 'smutek', None, None), ('pelko', 'strach', None, None), ('viha', 'gniew', None, None), ('rakkaus', 'miłość', None, None), ('viha (nienawiść)', 'nienawiść', None, None), ('toivo', 'nadzieja', None, None), ('unelma', 'marzenie', None, None), ('onni', 'szczęście', None, None), ('häpeä', 'wstyd', None, None), ('hämmästys', 'zdziwienie', None, None), ('uteliaisuus', 'ciekawość', None, None), ('kärsivällisyys', 'cierpliwość', None, None), ('rohkeus', 'odwaga', None, None), ('vilpitön', 'szczery', None, None), ('mukava', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('kohtelias', 'grzeczny', None, None), ('tyhmä', 'głupi', None, None), ('viisas', 'mądry', None, None), ('laiska', 'leniwy', None, None), ('ahkera', 'pracowity', None, None), ('mielenkiintoinen', 'ciekawy', None, None), ('tylsä', 'nudny', None, None), ('iloinen', 'wesoły', None, None), ('surullinen', 'smutny', None, None), ('vihainen', 'zły (rozgniewany)', None, None), ('onnellinen', 'szczęśliwy', None, None), ('rakastunut', 'zakochany', None, None), ('yksinäinen', 'samotny', None, None), ('rauhallinen', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('iso', 'duży', None, None), ('pitkä', 'długi', None, None), ('lyhyt', 'krótki', None, None), ('korkea', 'wysoki', None, None), ('matala', 'niski', None, None), ('leveä', 'szeroki', None, None), ('kapea', 'wąski', None, None), ('paksu', 'gruby', None, None), ('laiha', 'chudy', None, None), ('raskas', 'ciężki', None, None), ('kevyt', 'lekki', None, None), ('nopea', 'szybki', None, None), ('hidas', 'wolny', None, None), ('kova', 'twardy', None, None), ('pehmeä', 'miękki', None, None), ('märkä', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('kuiva', 'suchy', None, None), ('puhdas', 'czysty', None, None), ('likainen', 'brudny', None, None), ('täysi', 'pełny', None, None), ('tyhjä', 'pusty', None, None), ('terävä', 'ostry', None, None), ('äänekäs', 'głośny', None, None), ('hiljainen', 'cichy', None, None), ('kirkas', 'jasny', None, None), ('tumma', 'ciemny', None, None), ('nuori', 'młody', None, None), ('vanha', 'stary', None, None), ('uusi', 'nowy', None, None), ('huono', 'zły (niedobry)', None, None), ('kaunis', 'ładny', None, None), ('ruma', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('helppo', 'łatwy', None, None), ('vaikea', 'trudny', None, None), ('tärkeä', 'ważny', None, None), ('mahdollinen', 'możliwy', None, None), ('oikea', 'prawdziwy', None, None), ('väärä', 'fałszywy', None, None), ('kallis', 'drogi', None, None), ('halpa', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('olla', 'być', None, None), ('omistaa', 'mieć', None, None), ('tehdä', 'robić', None, None), ('mennä', 'iść', None, None), ('ajaa', 'jechać', None, None), ('tulla', 'przyjść', None, None), ('lähteä', 'wyjść', None, None), ('astua sisään', 'wejść', None, None), ('palata', 'wrócić', None, None), ('juosta', 'biec', None, None), ('seistä', 'stać', None, None), ('istua', 'siedzieć', None, None), ('maata', 'leżeć', None, None), ('nukkua', 'spać', None, None), ('nousta', 'wstać', None, None), ('syödä', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('juoda', 'pić', None, None), ('keittää', 'gotować', None, None), ('pestä', 'myć', None, None), ('pukeutua', 'ubierać się', None, None), ('puhua', 'mówić', None, None), ('sanoa', 'powiedzieć', None, None), ('kysyä', 'pytać', None, None), ('vastata', 'odpowiadać', None, None), ('kuulla', 'słyszeć', None, None), ('kuunnella', 'słuchać', None, None), ('nähdä', 'widzieć', None, None), ('katsoa', 'patrzeć', None, None), ('lukea', 'czytać', None, None), ('kirjoittaa', 'pisać', None, None), ('opiskella', 'uczyć się', None, None), ('opettaa', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('ymmärtää', 'rozumieć', None, None), ('tietää', 'wiedzieć', None, None), ('tuntea', 'znać', None, None), ('ajatella', 'myśleć', None, None), ('muistaa', 'pamiętać', None, None), ('unohtaa', 'zapominać', None, None), ('haluta', 'chcieć', None, None), ('pitää', 'lubić', None, None), ('rakastaa', 'kochać', None, None), ('tarvita', 'potrzebować', None, None), ('voida', 'móc', None, None), ('täytyä', 'musieć', None, None), ('antaa', 'dawać', None, None), ('ottaa', 'brać', None, None), ('ostaa', 'kupować', None, None), ('myydä', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('maksaa', 'płacić', None, None), ('avata', 'otwierać', None, None), ('sulkea', 'zamykać', None, None), ('aloittaa', 'zaczynać', None, None), ('lopettaa', 'kończyć', None, None), ('työskennellä', 'pracować', None, None), ('pelata', 'grać', None, None), ('laulaa', 'śpiewać', None, None), ('tanssia', 'tańczyć', None, None), ('uida', 'pływać', None, None), ('lentää', 'latać', None, None), ('laittaa', 'kłaść', None, None), ('etsiä', 'szukać', None, None), ('löytää', 'znajdować', None, None), ('odottaa', 'czekać', None, None), ('auttaa', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('pyytää', 'prosić', None, None), ('pyytää anteeksi', 'przepraszać', None, None), ('sallia', 'pozwalać', None, None), ('yrittää', 'próbować', None, None), ('muuttaa', 'zmieniać', None, None), ('kantaa', 'nosić', None, None), ('pitää kädessä', 'trzymać', None, None), ('heittää', 'rzucać', None, None), ('ottaa kiinni', 'łapać', None, None), ('lyödä', 'bić', None, None), ('tappaa', 'zabijać', None, None), ('kuolla', 'umierać', None, None), ('elää', 'żyć', None, None), ('asua', 'mieszkać', None, None), ('tavata', 'spotykać', None, None), ('soittaa', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('lähettää', 'wysyłać', None, None), ('saada', 'dostawać', None, None), ('näyttää', 'pokazywać', None, None), ('kutsua', 'zapraszać', None, None), ('vierailla', 'odwiedzać', None, None), ('itkeä', 'płakać', None, None), ('nauraa', 'śmiać się', None, None), ('hymyillä', 'uśmiechać się', None, None), ('pelätä', 'bać się', None, None), ('iloita', 'cieszyć się', None, None), ('uskoa', 'wierzyć', None, None), ('olla samaa mieltä', 'zgadzać się', None, None), ('valita', 'wybierać', None, None), ('päättää', 'decydować', None, None), ('laskea', 'liczyć', None, None), ('punnita', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('kävellä', 'chodzić', None, None), ('matkustaa', 'jeździć', None, None), ('nousta kyytiin', 'wsiadać', None, None), ('nousta pois', 'wysiadać', None, None), ('kääntyä', 'skręcać', None, None), ('pysähtyä', 'zatrzymywać się', None, None), ('myöhästyä', 'spóźniać się', None, None), ('kiirehtiä', 'spieszyć się', None, None), ('levätä', 'odpoczywać', None, None), ('leikkiä', 'bawić się', None, None), ('piirtää', 'rysować', None, None), ('rakentaa', 'budować', None, None), ('korjata', 'naprawiać', None, None), ('leikata', 'ciąć', None, None), ('paistaa', 'smażyć', None, None), ('leipoa', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('sekoittaa', 'mieszać', None, None), ('kaataa', 'nalewać', None, None), ('siivota', 'sprzątać', None, None), ('pestä pyykkiä', 'prać', None, None), ('silittää', 'prasować', None, None), ('ajaa parta', 'golić się', None, None), ('kammata', 'czesać', None, None), ('kylpeä', 'kąpać się', None, None), ('herätä', 'budzić się', None, None), ('nukahtaa', 'zasypiać', None, None), ('haaveilla', 'marzyć', None, None), ('nähdä unta', 'śnić', None, None), ('harjoitella', 'ćwiczyć', None, None), ('treenata', 'trenować', None, None), ('voittaa', 'wygrywać', None, None), ('hävitä', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('liikuttaa', 'ruszać', None, None), ('vetää', 'ciągnąć', None, None), ('työntää', 'pchać', None, None), ('nostaa', 'podnosić', None, None), ('pudota', 'spadać', None, None), ('hypätä', 'skakać', None, None), ('kiivetä', 'wspinać się', None, None), ('piilottaa', 'ukrywać', None, None), ('varastaa', 'kraść', None, None), ('palauttaa', 'oddawać', None, None), ('lainata', 'pożyczać', None, None), ('kuluttaa', 'wydawać', None, None), ('säästää', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('tämä', 'ten', None, None), ('tuo', 'tamten', None, None), ('tässä', 'tutaj', None, None), ('miten', 'jak', None, None), ('miksi', 'dlaczego', None, None), ('mikä', 'co', None, None), ('kuka', 'kto', None, None), ('joka', 'który', None, None), ('millainen', 'jaki', None, None), ('kuinka monta', 'ile (policzalne)', None, None), ('mutta', 'ale', None, None), ('tai', 'lub', None, None), ('koska', 'bo', None, None), ('jos', 'jeśli', None, None), ('että', 'że', None, None), ('siis', 'więc', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('myös', 'też', None, None), ('vain', 'tylko', None, None), ('hieman', 'trochę', None, None), ('kaikki', 'wszystko', None, None), ('ei mitään', 'nic', None, None), ('jokin', 'coś', None, None), ('joku', 'ktoś', None, None), ('ei kukaan', 'nikt', None, None), ('jokainen', 'każdy', None, None), ('toinen (inny)', 'inny', None, None), ('sama', 'ten sam', None, None), ('ehkä', 'może (być)', None, None), ('varmasti', 'na pewno', None, None), ('yhdessä', 'razem', None, None), ('itse', 'sam', None, None), ('ilman', 'bez', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('kanssa', 'z (towarzysząc)', None, None), ('sisällä', 'w (miejsce)', None, None), ('päällä', 'na (powierzchni)', None, None), ('asti', 'do (kierunek)', None, None), ('alkaen', 'od', None, None), ('varten', 'dla', None, None), ('läpi', 'przez', None, None), ('jälkeen', 'po (czas)', None, None), ('ennen', 'przed', None, None), ('takana', 'za (z tyłu)', None, None), ('yläpuolella', 'nad', None, None), ('alla', 'pod', None, None), ('vieressä', 'obok', None, None), ('välissä', 'między', None, None), ('vastaan', 'przeciw', None, None), ('aiheesta', 'o (temat)', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('luona', 'u (przy)', None, None), ('noin', 'około', None, None), ('melkein', 'prawie', None, None), ('jopa', 'nawet', None, None), ('uudestaan', 'jeszcze raz', None, None), ('silloin', 'wtedy', None, None), ('jossakin', 'gdzieś', None, None), ('ei missään', 'nigdzie', None, None), ('kaikkialla', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('elämä', 'życie', None, None), ('kuolema', 'śmierć', None, None), ('maailma', 'świat', None, None), ('maa (kraj)', 'kraj', None, None), ('valtio', 'państwo', None, None), ('kieli (mowa)', 'język (mowa)', None, None), ('sana', 'słowo', None, None), ('lause', 'zdanie', None, None), ('etunimi', 'imię', None, None), ('sukunimi', 'nazwisko', None, None), ('ikä', 'wiek', None, None), ('historia', 'historia', None, None), ('kulttuuri', 'kultura', None, None), ('uskonto', 'religia', None, None), ('Jumala', 'Bóg', None, None), ('sota', 'wojna', None, None)], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('rauha', 'pokój (brak wojny)', None, None), ('laki', 'prawo (przepis)', None, None), ('vapaus', 'wolność', None, None), ('valta', 'władza', None, None), ('hallitus', 'rząd', None, None), ('vaalit', 'wybory', None, None), ('ongelma', 'problem', None, None), ('idea', 'pomysł', None, None), ('syy', 'powód', None, None), ('tulos', 'wynik', None, None), ('tapa', 'sposób', None, None), ('alku', 'początek', None, None), ('loppu', 'koniec', None, None), ('osa', 'część', None, None), ('paikka', 'miejsce', None, None), ('asia', 'rzecz', None, None)], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('asia (sprawa)', 'sprawa', None, None), ('tieto', 'informacja', None, None), ('viesti', 'wiadomość', None, None), ('kirje', 'list', None, None), ('sanomalehti', 'gazeta', None, None), ('elokuva', 'film', None, None), ('musiikki', 'muzyka', None, None), ('laulu', 'piosenka', None, None), ('maalaus', 'obraz', None, None), ('peli', 'gra', None, None), ('urheilu', 'sport', None, None), ('ottelu', 'mecz', None, None), ('joukkue', 'drużyna', None, None), ('pallo', 'piłka', None, None), ('hauskanpito', 'zabawa', None, None), ('juhlat', 'impreza', None, None)], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('lahja', 'prezent', None, None), ('uni', 'sen', None, None), ('suunnitelma', 'plan', None, None), ('valinta', 'wybór', None, None), ('virhe', 'błąd', None, None), ('totuus', 'prawda', None, None), ('valhe', 'kłamstwo', None, None), ('salaisuus', 'tajemnica', None, None), ('voima', 'siła', None, None), ('energia', 'energia', None, None), ('valo', 'światło', None, None), ('ääni (dźwięk)', 'dźwięk', None, None), ('hiljaisuus', 'cisza', None, None), ('liike', 'ruch', None, None), ('muutos', 'zmiana', None, None), ('ero', 'różnica', None, None)], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('esimerkki', 'przykład', None, None), ('kokonaisuus', 'całość', None, None)], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, None), ('sähköposti', 'e-mail', None, None), ('salasana', 'hasło', None, None), ('verkkosivu', 'strona internetowa', None, None), ('ohjelma', 'program', None, None), ('sovellus', 'aplikacja', None, None), ('näyttö', 'ekran', None, None), ('näppäimistö', 'klawiatura', None, None), ('tiedosto', 'plik', None, None), ('valokuva', 'zdjęcie', None, None), ('kamera', 'kamera', None, None), ('akku', 'bateria', None, None), ('sähkö', 'prąd', None, None), ('johto', 'kabel', None, None), ('kone', 'maszyna', None, None), ('työkalu', 'narzędzie', None, None)], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('vasara', 'młotek', None, None), ('tulostin', 'drukarka', None, None), ('laturi', 'ładowarka', None, None)], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('pohjoinen', 'północ', None, None), ('etelä', 'południe (kierunek)', None, None), ('itä', 'wschód', None, None), ('länsi', 'zachód', None, None), ('Puola', 'Polska', None, None), ('Eurooppa', 'Europa', None, None), ('Saksa', 'Niemcy', None, None), ('Ranska', 'Francja', None, None), ('Italia', 'Włochy', None, None), ('Espanja', 'Hiszpania', None, None), ('Venäjä', 'Rosja', None, None), ('Englanti', 'Anglia', None, None), ('Amerikka', 'Ameryka', None, None), ('Kiina', 'Chiny', None, None), ('Japani', 'Japonia', None, None), ('Afrikka', 'Afryka', None, None)], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('Aasia', 'Azja', None, None), ('manner', 'kontynent', None, None), ('pääkaupunki', 'stolica', None, None), ('kansalainen', 'obywatel', None, None)], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('pala', 'kawałek', None, None), ('pisara', 'kropla', None, None), ('laatikko', 'pudełko', None, None), ('säkki', 'worek', None, None), ('lanka', 'nić', None, None), ('lanka (drut)', 'drut', None, None), ('neula', 'igła', None, None), ('sakset', 'nożyczki', None, None), ('keppi', 'kij', None, None), ('köysi', 'lina', None, None), ('ketju', 'łańcuch', None, None), ('ruuvi', 'śruba', None, None), ('naula', 'gwóźdź', None, None), ('liima', 'klej', None, None), ('maali', 'farba', None, None), ('lasi (szkło)', 'szkło', None, None)], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('puu (drewno)', 'drewno', None, None), ('metalli', 'metal', None, None), ('kulta', 'złoto', None, None), ('hopea', 'srebro', None, None), ('rauta', 'żelazo', None, None), ('muovi', 'plastik', None, None), ('nahka', 'skóra (materiał)', None, None), ('puuvilla', 'bawełna', None, None), ('villa', 'wełna', None, None), ('hiekka', 'piasek', None, None), ('muta', 'błoto', None, None), ('pöly', 'kurz', None, None), ('savu', 'dym', None, None), ('höyry', 'para (wodna)', None, None)], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('ylhäällä', 'góra (kierunek)', None, None), ('alhaalla', 'dół', None, None), ('edessä', 'przód', None, None), ('takana (tył)', 'tył', None, None), ('keskellä', 'środek', None, None), ('sivu', 'bok', None, None), ('sisällä (wewnątrz)', 'wewnątrz', None, None), ('ulkona', 'na zewnątrz', None, None), ('kaukana', 'daleko', None, None), ('lähellä', 'blisko', None, None), ('korkealla', 'wysoko', None, None), ('matalalla', 'nisko', None, None), ('nopeasti', 'szybko', None, None), ('hitaasti', 'wolno', None, None), ('huonosti', 'źle', None, None), ('helposti', 'łatwo', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('vaikeasti', 'trudno', None, None), ('erikseen', 'osobno', None, None), ('vastapäätä', 'naprzeciw', None, None), ('pitkin', 'wzdłuż', None, None), ('poikki', 'w poprzek', None, None), ('ympäri', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('kaali', 'kapusta', None, None), ('herne', 'groszek', None, None), ('pavut', 'fasola', None, None), ('sieni', 'grzyb', None, None), ('pähkinä', 'orzech', None, None), ('luumu', 'śliwka', None, None), ('kirsikka', 'wiśnia', None, None), ('persikka', 'brzoskwinia', None, None), ('vesimeloni', 'arbuz', None, None), ('vadelma', 'malina', None, None), ('makkara', 'kiełbasa', None, None), ('kinkku', 'szynka', None, None), ('sämpylä', 'bułka', None, None), ('voileipä', 'kanapka', None, None), ('letti', 'naleśnik', None, None), ('jogurtti', 'jogurt', None, None)], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('kerma', 'śmietana', None, None), ('kastike', 'sos', None, None), ('etikka', 'ocet', None, None), ('hiiva', 'drożdże', None, None), ('hyytelö (kisiel)', 'kisiel', None, None), ('hyytelö', 'galaretka', None, None), ('rusina', 'rodzynek', None, None), ('manteli', 'migdał', None, None), ('persilja', 'pietruszka', None, None), ('tilli', 'koperek', None, None), ('paprika', 'papryka', None, None), ('salaatti (sałata)', 'sałata', None, None), ('pinaatti', 'szpinak', None, None), ('punajuuri', 'burak', None, None)], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('appi', 'teść', None, None), ('anoppi', 'teściowa', None, None), ('lanko', 'szwagier', None, None), ('veljenpoika', 'bratanek', None, None), ('sisarentytär', 'siostrzenica', None, None), ('orpo', 'sierota', None, None), ('leski', 'wdowa', None, None), ('sulhanen', 'narzeczony', None, None), ('häät', 'ślub', None, None), ('avioero', 'rozwód', None, None), ('syntymä', 'urodzenie', None, None), ('hautajaiset', 'pogrzeb', None, None), ('kampaaja', 'fryzjer', None, None), ('leipuri', 'piekarz', None, None), ('teurastaja', 'rzeźnik', None, None), ('tarjoilija (kelnerka)', 'kelnerka', None, None)], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('postinkantaja', 'listonosz', None, None), ('palomies', 'strażak', None, None), ('tuomari', 'sędzia', None, None), ('johtaja', 'dyrektor', None, None)], 'sentences': []}]
# === /SŁOWNICTWO ===
