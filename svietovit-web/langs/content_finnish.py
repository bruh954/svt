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
