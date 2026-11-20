"""Treść kursu: rosyjski dla Polaków.

Wymowa polskimi literami; ś/ć/ń oznaczają miękkie spółgłoski. Akcent wyrazowy jest zaznaczony kreską nad samogłoską (вода́). W zwykłych tekstach się go nie pisze.
"""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"alfabet": "АЛФАВИТ · ALFABET", "jezyk": "ЯЗЫК · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Litery I", "icon": "А", "track": "alfabet",
     "letters": [
         ("а", "[a]: jak polskie a", "дом (dom)"),
         ("б", "[b]: jak polskie b", "брат (brat)"),
         ("в", "[w]: jak polskie w", "вода́ (woda)"),
         ("г", "[g]: jak polskie g", "год (rok)"),
         ("д", "[d]: jak polskie d", "да (tak)"),
         ("е", "[je] lub [ie]: jak polskie je; zmiękcza poprzednią", "нет (nie)"),
         ("ё", "[jo] lub [io]: jak polskie jo; zawsze akcentowane", "ёлка (choinka)"),
         ("ж", "[ż]: twarde ż, jak w „żaba”", "жена́ (żona)"),
     ]},
    {"id": "wymowa2", "title": "Litery II", "icon": "З", "track": "alfabet",
     "letters": [
         ("з", "[z]: jak polskie z", "зима́ (zima)"),
         ("и", "[i]: jak polskie i", "мир (pokój)"),
         ("й", "[j]: krótkie j po samogłosce", "чай (herbata)"),
         ("к", "[k]: jak polskie k", "кот (kot)"),
         ("л", "[ł] lub [l]: twarde ł; przed i, e miękkie l", "ла́мпа (lampa)"),
         ("м", "[m]: jak polskie m", "ма́ма (mama)"),
         ("н", "[n]: jak polskie n", "нос (nos)"),
         ("о", "[o]: jak polskie o (bez akcentu brzmi jak a)", "молоко́ (mleko)"),
     ]},
    {"id": "wymowa3", "title": "Litery III", "icon": "П", "track": "alfabet",
     "letters": [
         ("п", "[p]: jak polskie p", "па́па (tata)"),
         ("р", "[r]: wibrujące r, jak polskie", "ры́ба (ryba)"),
         ("с", "[s]: jak polskie s", "сыр (ser)"),
         ("т", "[t]: jak polskie t", "там (tam)"),
         ("у", "[u]: jak polskie u", "муж (mąż)"),
         ("ф", "[f]: jak polskie f", "фо́то (zdjęcie)"),
         ("х", "[ch]: jak polskie ch", "хлеб (chleb)"),
         ("ц", "[c]: jak polskie c", "цена́ (cena)"),
     ]},
    {"id": "wymowa4", "title": "Litery IV", "icon": "Ч", "track": "alfabet",
     "letters": [
         ("ч", "[ć]: miękkie cz, jak „ć” w „ćma”", "чай (herbata)"),
         ("ш", "[sz]: twarde sz, jak polskie sz", "шко́ла (szkoła)"),
         ("щ", "[śś]: długie miękkie sz, jak „szcz” bez t", "борщ (barszcz)"),
         ("ъ", "twardy znak: nie jest dźwiękiem, rozdziela", "объе́кт (obiekt)"),
         ("ы", "[y]: jak polskie y", "ты (ty)"),
         ("ь", "miękki znak: zmiękcza poprzednią spółgłoskę", "день (dzień)"),
         ("э", "[e]: twarde e, jak polskie e", "э́то (to)"),
         ("ю", "[ju] lub [iu]: jak polskie ju; zmiękcza", "люблю́ (kocham)"),
         ("я", "[ja] lub [ia]: jak polskie ja; zmiękcza", "я (ja)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "П", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("приве́т", "cześć", None, None),
         ("пока́", "pa; na razie", None, None),
         ("спаси́бо", "dziękuję", None, "Z „spasi bog”: niech Bóg zbawi."),
         ("пожа́луйста", "proszę; nie ma za co", None, None),
         ("да", "tak", None, None),
         ("нет", "nie", None, None),
         ("до́брый", "dobry (męski)", None, None),
         ("день", "dzień", None, None),
         ("до́брой", "dobrej (żeński)", None, None),
         ("но́чи", "nocy", None, None),
         ("извини́те", "przepraszam", None, None),
         ("хорошо́", "dobrze", None, None),
         ("о́чень", "bardzo", None, None),
         ("и", "i", None, None),
     ],
     "sentences": [
         (["приве́т", "!"], "Cześć!", {"пока́": "пока́ to „pa”."}),
         (["пока́", "!"], "Pa!", {"приве́т": "приве́т to „cześć”."}),
         (["до́брый", "день", "!"], "Dzień dobry!", {"но́чи": "но́чи to „nocy”."}),
         (["до́брой", "но́чи", "!"], "Dobranoc!", {"день": "день to „dzień”."}),
         (["спаси́бо", "!"], "Dziękuję!", {"пожа́луйста": "пожа́луйста to „proszę”. Tu dziękujesz."}),
         (["да", ",", "спаси́бо"], "Tak, dziękuję.", {"нет": "нет to „nie”."}),
         (["нет", ",", "спаси́бо"], "Nie, dziękuję.", {"да": "да to „tak”."}),
         (["извини́те", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "Я", "track": "jezyk",
     "words": [
         ("я", "ja", None, None),
         ("ты", "ty", None, None),
         ("он", "on", None, None),
         ("она́", "ona", None, None),
         ("студе́нт", "student", "student", None),
         ("учи́тель", "nauczyciel", None, None),
         ("поля́к", "Polak", None, None),
         ("по́лька", "Polka", None, None),
         ("из", "z", None, None),
         ("По́льши", "Polski (z Polski)", None, None),
         ("Росси́и", "Rosji (z Rosji)", None, None),
         ("э́то", "to (jest)", None, None),
     ],
     "sentences": [
         (["я", "студе́нт"], "Jestem studentem.", {"ты": "ty to „ты”. O sobie: я."}),
         (["ты", "учи́тель"], "Jesteś nauczycielem.", {"я": "я to „ja”. Do „ты” mówisz o nim."}),
         (["он", "поля́к"], "On jest Polakiem.", {"по́лька": "Dla mężczyzny: поля́к."}),
         (["она́", "по́лька"], "Ona jest Polką.", {"поля́к": "Dla kobiety: по́лька."}),
         (["я", "из", "По́льши"], "Jestem z Polski.", {"Росси́и": "Росси́и to „Rosji”."}),
         (["она́", "из", "Росси́и"], "Ona jest z Rosji.", {}),
         (["э́то", "студе́нт"], "To jest student.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "С", "track": "jezyk",
     "words": [
         ("мой", "mój (męski)", None, None),
         ("моя́", "moja (żeński)", None, None),
         ("ма́ма", "mama", None, None),
         ("па́па", "tata", None, None),
         ("брат", "brat", None, None),
         ("сестра́", "siostra", None, None),
         ("ма́льчик", "chłopiec", None, None),
         ("друг", "przyjaciel", None, None),
         ("же́нщина", "kobieta", None, None),
         ("мужчи́на", "mężczyzna", None, None),
         ("у", "u; przy", None, "„У меня́ есть” = „mam”."),
         ("меня́", "mnie", None, None),
         ("тебя́", "ciebie", None, None),
         ("есть", "jest; ma się", None, None),
         ("ма́ленький", "mały (męski)", None, None),
         ("ма́ленькая", "mała (żeński)", None, None),
         ("до́брая", "dobra (żeński)", None, None),
     ],
     "sentences": [
         (["мой", "брат", "ма́ленький"], "Mój brat jest mały.", {"моя́": "брат jest męski: мой."}),
         (["моя́", "сестра́", "ма́ленькая"], "Moja siostra jest mała.", {"мой": "сестра́ jest żeńska: моя́."}),
         (["моя́", "ма́ма", "до́брая"], "Moja mama jest dobra.", {}),
         (["у", "меня́", "есть", "брат"], "Mam brata.", {"тебя́": "тебя́ to „ciebie”. O sobie: меня́."}),
         (["у", "тебя́", "есть", "сестра́"], "Masz siostrę.", {"меня́": "меня́ to „mnie”. Do „ты”: тебя́."}),
         (["па́па", "мужчи́на"], "Tata jest mężczyzną.", {}),
         (["мой", "друг", "до́брый"], "Mój przyjaciel jest dobry.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "Е", "track": "jezyk",
     "words": [
         ("вода́", "woda", None, None),
         ("во́ду", "wodę", None, "Biernik: -а → -у."),
         ("ко́фе", "kawa", None, None),
         ("чай", "herbata", None, None),
         ("хлеб", "chleb", None, None),
         ("сыр", "ser", None, None),
         ("молоко́", "mleko", None, None),
         ("ры́ба", "ryba", None, None),
         ("ры́бу", "rybę", None, None),
         ("я́блоко", "jabłko", None, None),
         ("хочу́", "chcę", None, None),
         ("хо́чешь", "chcesz", None, None),
         ("вку́сная", "smaczna", None, None),
         ("сейча́с", "teraz", None, None),
     ],
     "sentences": [
         (["я", "хочу́", "ко́фе"], "Chcę kawę.", {"хо́чешь": "хо́чешь to „chcesz”. O sobie: хочу́."}),
         (["ты", "хо́чешь", "чай", "?"], "Chcesz herbatę?", {"хочу́": "хочу́ to „chcę”. Do „ты”: хо́чешь."}),
         (["я", "хочу́", "хлеб"], "Chcę chleb.", {}),
         (["ты", "хо́чешь", "я́блоко", "?"], "Chcesz jabłko?", {}),
         (["ры́ба", "о́чень", "вку́сная"], "Ryba jest bardzo smaczna.", {}),
         (["сейча́с", "я", "хочу́", "во́ду"], "Teraz chcę wodę.", {"вода́": "Po „хочу́” biernik: во́ду."}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("два", "dwa", None, None),
         ("три", "trzy", None, None),
         ("четы́ре", "cztery", None, None),
         ("пять", "pięć", None, None),
         ("де́сять", "dziesięć", None, None),
         ("бра́та", "braci (2–4)", None, "Po 2–4: dopełniacz lp."),
         ("де́ти", "dzieci", None, None),
         ("сего́дня", "dziś", None, None),
         ("за́втра", "jutro", None, None),
         ("вчера́", "wczoraj", None, None),
         ("часо́в", "godzin", None, None),
         ("ско́лько", "ile", None, None),
         ("вре́мени", "czasu", None, None),
     ],
     "sentences": [
         (["у", "меня́", "два", "бра́та"], "Mam dwóch braci.", {}),
         (["у", "меня́", "есть", "де́ти"], "Mam dzieci.", {}),
         (["ско́лько", "вре́мени", "?"], "Która jest godzina?", {}),
         (["сейча́с", "де́сять", "часо́в"], "Jest dziesiąta.", {}),
         (["сего́дня", "я", "хочу́", "ко́фе"], "Dziś chcę kawę.", {"за́втра": "за́втра to „jutro”. Tu „dziś”: сего́дня."}),
         (["за́втра", "я", "хочу́", "ры́бу"], "Jutro chcę rybę.", {"вчера́": "вчера́ to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "М", "track": "jezyk",
     "words": [
         ("дом", "dom", None, None),
         ("домо́й", "do domu", None, None),
         ("го́род", "miasto", None, None),
         ("у́лица", "ulica", None, None),
         ("шко́ла", "szkoła", None, None),
         ("мо́ре", "morze", None, None),
         ("такси́", "taksówka", "taksówka", None),
         ("гости́ница", "hotel", None, None),
         ("где", "gdzie", None, None),
         ("здесь", "tu", None, None),
         ("там", "tam", None, None),
         ("иду́", "idę (pieszo)", None, None),
         ("е́ду", "jadę (pojazdem)", None, None),
         ("в", "do; w", None, None),
         ("Москву́", "do Moskwy", None, None),
         ("напра́во", "w prawo", None, None),
         ("нале́во", "w lewo", None, None),
     ],
     "sentences": [
         (["где", "гости́ница", "?"], "Gdzie jest hotel?", {"здесь": "здесь to „tu”. Pytasz „gdzie”: где."}),
         (["гости́ница", "там"], "Hotel jest tam.", {"здесь": "здесь to „tu”. Tu „tam”: там."}),
         (["я", "иду́", "домо́й"], "Idę do domu.", {"е́ду": "Pieszo: иду́. Pojazdem: е́ду."}),
         (["я", "е́ду", "в", "Москву́"], "Jadę do Moskwy.", {}),
         (["такси́", "напра́во"], "Taksówka jest w prawo.", {"нале́во": "нале́во to „w lewo”."}),
         (["шко́ла", "там"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Cyrylica ma tylko 33 litery", "chain": [],
                "text": "Wiele liter znasz: а, к, м, о, т. Zmylić mogą в (czytane [v]), н ([n]), р ([r]), с ([s]), у ([u]). Miękkie samogłoski (е, ё, ю, я) zmiękczają spółgłoskę przed sobą. Kreska nad samogłoską (вода́) pokazuje akcent: w rosyjskim jest ruchomy i trzeba go zapamiętać razem ze słowem. W zwykłych tekstach się go nie pisze."}],
    "ja": [{"title": "Brak „jest”", "chain": [
                ("Jestem studentem.", ["я", "студе́нт"], "Bez „jestem”: po prostu я студе́нт."),
                ("Jesteś nauczycielem.", ["ты", "учи́тель"], "Bez „jesteś”."),
            ],
            "text": "W czasie teraźniejszym nie mówi się „jestem, jest”. Mówisz po prostu: я студе́нт, он поля́к."}],
    "ludzie": [{"title": "Mój i moja", "chain": [],
                "text": "Przymiotniki i „mój” zgadzają się z rodzajem: мой брат (m), моя́ сестра́ (ż). Posiadanie wyrażasz: у меня́ есть… (u mnie jest = mam)."}],
    "jedzenie": [{"title": "Хочу́ i хо́чешь", "chain": [],
                  "text": "Czasownik zmienia końcówkę: я хочу́, ты хо́чешь. Po „хочу́” rzeczownik żeński kończący się na -а przyjmuje -у: вода́ → во́ду."}],
}

ENDINGS_INSIGHT = {"title": "Rodzaj i forma czasownika",
                   "text": "Ćwiczysz rodzaj (мой/моя́) i formy czasownika (хочу́/хо́чешь). Tu to robisz."}

ENDINGS = [
    ("", "", "мой", " брат", ["мой", "моя́"], "mój (męski)", "брат jest męski: мой.", "ludzie"),
    ("", "", "моя́", " сестра́", ["мой", "моя́"], "moja (żeński)", "сестра́ jest żeńska: моя́.", "ludzie"),
    ("", "", "мой", " друг", ["мой", "моя́"], "mój (męski)", "друг jest męski: мой.", "ludzie"),
    ("", "", "моя́", " ма́ма", ["мой", "моя́"], "moja (żeński)", "ма́ма jest żeńska: моя́.", "ludzie"),
    ("у ", "", "меня́", " есть брат", ["меня́", "тебя́"], "u mnie", "O sobie: меня́.", "ludzie"),
    ("у ", "", "тебя́", " есть сестра́", ["меня́", "тебя́"], "u ciebie", "Do „ты”: тебя́.", "ludzie"),
    ("я ", "", "хочу́", " ко́фе", ["хочу́", "хо́чешь"], "ja chcę", "Do „я” pasuje хочу́.", "jedzenie"),
    ("ты ", "", "хо́чешь", " чай", ["хочу́", "хо́чешь"], "ty chcesz", "Do „ты” pasuje хо́чешь.", "jedzenie"),
    ("он ", "", "поля́к", "", ["поля́к", "по́лька"], "Polak (on)", "Mężczyzna: поля́к.", "ja"),
    ("она́ ", "", "по́лька", "", ["поля́к", "по́лька"], "Polka (ona)", "Kobieta: по́лька.", "ja"),
    ("я ", "", "из", " По́льши", ["из", "в"], "z Polski", "из to „z”, в to „do, w”.", "miejsca"),
    ("я е́ду ", "", "в", " Москву́", ["из", "в"], "do Moskwy", "в to „do, w”.", "miejsca"),
]

CHAT_EXTRA = {"А́нна": "Anna (imię)", "Ива́н": "Iwan (imię)", "води́тель": "kierowca", "куда́": "dokąd", "большо́е": "duże"}

CHATS = [
    {"id": "kafe", "title": "W kawiarni", "partner": "А́нна", "avatar": "А", "requires": "jedzenie",
     "turns": [
         {"bot": ["до́брый", "день", "!"], "en": "Dzień dobry!",
          "options": [(["до́брый", "день", "!"], True, None), (["до́брой", "но́чи", "!"], False, "до́брой но́чи to „dobranoc”. Jest dzień.")]},
         {"bot": ["ко́фе", "?"], "en": "Kawę?",
          "options": [(["да", ",", "я", "хочу́", "ко́фе"], True, None),
                      (["да", ",", "ты", "хо́чешь", "ко́фе"], False, "хо́чешь jest do „ты”. O sobie: хочу́.")]},
         {"bot": ["и", "хлеб", "?"], "en": "I chleb?",
          "options": [(["нет", ",", "спаси́бо"], True, None),
                      (["пожа́луйста", "!"], False, "пожа́луйста to „proszę”. Odmów: нет, спаси́бо.")]},
         {"bot": ["хорошо́", "!"], "build": (["спаси́бо", "!"], "Dziękuję!"), "en": "Dobrze!"},
     ]},
    {"id": "znakomstvo", "title": "Poznajemy się", "partner": "Ива́н", "avatar": "И", "requires": "ludzie",
     "turns": [
         {"bot": ["приве́т", "!"], "en": "Cześć!",
          "options": [(["приве́т", "!"], True, None), (["извини́те", "!"], False, "извини́те to „przepraszam”. Powitaj: приве́т.")]},
         {"bot": ["ты", "из", "Росси́и", "?"], "en": "Jesteś z Rosji?",
          "options": [(["нет", ",", "я", "из", "По́льши"], True, None),
                      (["нет", ",", "ты", "из", "По́льши"], False, "ты to „ty”. O sobie: я.")]},
         {"bot": ["у", "тебя́", "есть", "брат", "?"], "en": "Masz brata?",
          "options": [(["да", ",", "у", "меня́", "есть", "брат"], True, None),
                      (["да", ",", "у", "тебя́", "есть", "брат"], False, "тебя́ to „ciebie”. O sobie: меня́.")]},
         {"bot": ["пока́", "!"], "build": (["пока́", "!"], "Pa!"), "en": "Pa!"},
     ]},
    {"id": "taksi", "title": "W taksówce", "partner": "води́тель", "avatar": "В", "requires": "miejsca",
     "turns": [
         {"bot": ["до́брый", "день", "!"], "en": "Dzień dobry!",
          "options": [(["до́брый", "день", "!"], True, None), (["до́брой", "но́чи", "!"], False, "до́брой но́чи to „dobranoc”. Jest dzień.")]},
         {"bot": ["куда́", "?"], "en": "Dokąd?",
          "options": [(["я", "е́ду", "в", "Москву́"], True, None),
                      (["я", "иду́", "в", "Москву́"], False, "иду́ to „idę pieszo”. Taksówką: е́ду.")]},
         {"bot": ["гости́ница", "там", "."], "en": "Hotel jest tam.",
          "options": [(["напра́во", "?"], True, None), (["здесь", "?"], False, "Pytasz o kierunek: напра́во.")]},
         {"bot": ["да", "!"], "build": (["спаси́бо", "!"], "Dziękuję!"), "en": "Tak!"},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['я', 'ты', 'он/она́', 'мы', 'вы', 'они́'],
    'przesz': ['он', 'она́', 'оно́', 'они́'],
    'przyp': ['mianownik', 'dopełniacz', 'celownik', 'biernik', 'narzędnik', 'miejscownik (о…)'],
    'im': ['czynny teraźniejszy (który robi)', 'czynny przeszły (który robił)', 'bierny teraźniejszy (robiony)', 'bierny przeszły (zrobiony)', 'przysłówkowy współczesny (robiąc)', 'przysłówkowy uprzedni (zrobiwszy)'],
    'krotka': ['on', 'ona', 'ono', 'oni'],
    'rozk': ['чита́ть', 'говори́ть', 'писа́ть', 'идти́', 'есть', 'быть', 'дать', 'пить'],
    'ruch': ['iść (teraz, w jedną stronę)', 'chodzić (wielokrotnie)', 'jechać', 'jeździć', 'lecieć', 'latać', 'nieść', 'nosić'],
    'stopn': ['хоро́ший', 'плохо́й', 'большо́й', 'ма́ленький', 'краси́вый', 'дорого́й', 'молодо́й', 'ста́рый'],
    'setki': ['200', '300', '400', '500', '600', '700', '800', '900'],
    'liczrz': ['1', '2', '3', '4', '5', '11', '21', '22', '100'],
    't_ff': ['дива́н', 'ковёр', 'запо́мнить', 'забы́ть', 'неде́ля', 'у́тро', 'ско́ро', 'кра́сный'],
    't_rekcja': ['благодари́ть (dziękować)', 'поздравля́ть (gratulować)', 'боле́ть (chorować)', 'учи́ться (uczyć się)', 'интересова́ться (interesować się)', 'ждать (czekać)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'де́лать (robić)', 'os', 'де́лаю; де́лаешь; де́лает; де́лаем; де́лаете; де́лают', 'I koniugacja: -ю, -ешь, -ет, -ем, -ете, -ют.'),
    ('conj', 'Wzory koniugacji', 'чита́ть (czytać)', 'os', 'чита́ю; чита́ешь; чита́ет; чита́ем; чита́ете; чита́ют', None),
    ('conj', 'Wzory koniugacji', 'говори́ть (mówić)', 'os', 'говорю́; говори́шь; говори́т; говори́м; говори́те; говоря́т', 'II koniugacja: -ю, -ишь, -ит, -им, -ите, -ят.'),
    ('conj', 'Wyjątki', 'люби́ть (kochać)', 'os', 'люблю́; лю́бишь; лю́бит; лю́бим; лю́бите; лю́бят', 'W 1. osobie wtrącone л i akcent na końcówce: люблю́.'),
    ('conj', 'Wyjątki', 'жить (żyć)', 'os', 'живу́; живёшь; живёт; живём; живёте; живу́т', 'Temat жив-, końcówki z ё.'),
    ('conj', 'Czasowniki nieregularne', 'хоте́ть (chcieć)', 'os', 'хочу́; хо́чешь; хо́чет; хоти́м; хоти́те; хотя́т', 'Liczba pojedyncza z ч, mnoga z т.'),
    ('conj', 'Czasowniki nieregularne', 'есть (jeść)', 'os', 'ем; ешь; ест; еди́м; еди́те; едя́т', None),
    ('conj', 'Czasowniki nieregularne', 'идти́ (iść)', 'os', 'иду́; идёшь; идёт; идём; идёте; иду́т', None),
    ('conj', 'Czasowniki nieregularne', 'е́хать (jechać)', 'os', 'е́ду; е́дешь; е́дет; е́дем; е́дете; е́дут', None),
    ('conj', 'Czasowniki nieregularne', 'мочь (móc)', 'os', 'могу́; мо́жешь; мо́жет; мо́жем; мо́жете; мо́гут', None),
    ('conj', 'Czasowniki nieregularne', 'быть (być): czas przeszły', 'przesz', 'был; была́; бы́ло; бы́ли', 'Czas przeszły odmienia się przez rodzaj, nie przez osobę.'),
    ('decl', 'Wzory deklinacji', 'брат (brat): męski żywotny', 'przyp', 'брат; бра́та; бра́ту; бра́та; бра́том; бра́те', 'U żywotnych biernik = dopełniacz.'),
    ('decl', 'Wzory deklinacji', 'стол (stół): męski nieżywotny', 'przyp', 'стол; стола́; столу́; стол; столо́м; столе́', 'U nieżywotnych biernik = mianownik.'),
    ('decl', 'Wzory deklinacji', 'ма́ма (mama): żeński na -а', 'przyp', 'ма́ма; ма́мы; ма́ме; ма́му; ма́мой; ма́ме', None),
    ('decl', 'Wzory deklinacji', 'окно́ (okno): nijaki na -о', 'przyp', 'окно́; окна́; окну́; окно́; окно́м; окне́', None),
    ('decl', 'Wzory deklinacji', 'мо́ре (morze): nijaki na -е', 'przyp', 'мо́ре; мо́ря; мо́рю; мо́ре; мо́рем; мо́ре', None),
    ('decl', 'Wyjątki', 'вода́ (woda): ruchomy akcent', 'przyp', 'вода́; воды́; воде́; во́ду; водо́й; воде́', 'W bierniku akcent przeskakuje na temat: во́ду.'),
    ('decl', 'Wyjątki', 'вре́мя (czas)', 'przyp', 'вре́мя; вре́мени; вре́мени; вре́мя; вре́менем; вре́мени', 'Rzeczowniki nijakie na -мя rozszerzają temat o -ен-.'),
    ('decl', 'Wyjątki', 'мать (matka)', 'przyp', 'мать; ма́тери; ма́тери; мать; ма́терью; ма́тери', 'Temat rozszerzony o -ер-.'),
    ('decl', 'Zaimki', 'я (ja)', 'przyp', 'я; меня́; мне; меня́; мной; мне', None),
    ('decl', 'Zaimki', 'ты (ty)', 'przyp', 'ты; тебя́; тебе́; тебя́; тобо́й; тебе́', None),
    ('form', 'Imiesłowy', 'чита́ть / прочита́ть (czytać)', 'im', 'чита́ющий; чита́вший; чита́емый; прочи́танный; чита́я; прочита́в', 'Czynne: -ющий, -вший. Bierne: -емый, -нный. Przysłówkowe: -я, -в. Imiesłów bierny przeszły tworzy się od czasownika dokonanego.'),
    ('form', 'Imiesłowy', 'де́лать / сде́лать (robić)', 'im', 'де́лающий; де́лавший; де́лаемый; сде́ланный; де́лая; сде́лав', None),
    ('form', 'Imiesłowy', 'изуча́ть / изучи́ть (studiować)', 'im', 'изуча́ющий; изуча́вший; изуча́емый; изу́ченный; изуча́я; изучи́в', None),
    ('form', 'Imiesłowy', 'ви́деть / уви́деть (widzieć)', 'im', 'ви́дящий; ви́девший; ви́димый; уви́денный; ви́дя; уви́дев', 'II koniugacja: -ящий, -имый.'),
    ('decl', 'Imiesłowy: odmiana', 'чита́ющий (czytający): rodzaj męski', 'przyp', 'чита́ющий; чита́ющего; чита́ющему; чита́ющий; чита́ющим; чита́ющем', 'Imiesłów odmienia się jak przymiotnik. Po ж, ш, ч, щ pisze się и, nie ы.'),
    ('decl', 'Imiesłowy: odmiana', 'чита́ющая (czytająca): rodzaj żeński', 'przyp', 'чита́ющая; чита́ющей; чита́ющей; чита́ющую; чита́ющей; чита́ющей', None),
    ('form', 'Imiesłowy: forma krótka', 'сде́ланный (zrobiony)', 'krotka', 'сде́лан; сде́лана; сде́лано; сде́ланы', 'W orzeczeniu używa się formy krótkiej, z jednym н: дом сде́лан.'),
    ('form', 'Imiesłowy: forma krótka', 'откры́тый (otwarty)', 'krotka', 'откры́т; откры́та; откры́то; откры́ты', None),
    ('form', 'Tryb rozkazujący', 'Tryb rozkazujący: ty', 'rozk', 'чита́й; говори́; пиши́; иди́; ешь; будь; дай; пей', 'Po samogłosce -й, po spółgłosce -и (pod akcentem) albo -ь. Liczba mnoga i forma grzecznościowa: + -те.'),
    ('form', 'Czasowniki ruchu', 'Pary czasowników ruchu', 'ruch', 'идти́; ходи́ть; е́хать; е́здить; лете́ть; лета́ть; нести́; носи́ть', 'Każdy ruch ma dwa czasowniki: jednokierunkowy (teraz, do celu) i wielokierunkowy (zwykle, tam i z powrotem).'),
    ('conj', 'Czasowniki ruchu', 'ходи́ть (chodzić)', 'os', 'хожу́; хо́дишь; хо́дит; хо́дим; хо́дите; хо́дят', 'W 1. osobie д → ж.'),
    ('conj', 'Czasowniki ruchu', 'е́здить (jeździć)', 'os', 'е́зжу; е́здишь; е́здит; е́здим; е́здите; е́здят', None),
    ('conj', 'Wyjątki', 'пить (pić)', 'os', 'пью; пьёшь; пьёт; пьём; пьёте; пьют', 'Tak samo: бить, лить, шить.'),
    ('conj', 'Wyjątki', 'писа́ть (pisać)', 'os', 'пишу́; пи́шешь; пи́шет; пи́шем; пи́шете; пи́шут', 'Wymiana с → ш we wszystkich osobach.'),
    ('form', 'Stopniowanie', 'Stopień wyższy przymiotników', 'stopn', 'лу́чше; ху́же; бо́льше; ме́ньше; краси́вее; доро́же; моло́же; ста́рше', 'Regularnie: -ее. Częste przymiotniki mają formy nieregularne.'),
    ('decl', 'Zaimki', 'мой (mój)', 'przyp', 'мой; моего́; моему́; мой; мои́м; моём', None),
    ('decl', 'Zaimki', 'э́тот (ten)', 'przyp', 'э́тот; э́того; э́тому; э́тот; э́тим; э́том', None),
    ('decl', 'Zaimki', 'кто (kto)', 'przyp', 'кто; кого́; кому́; кого́; кем; ком', None),
    ('decl', 'Zaimki', 'что (co)', 'przyp', 'что; чего́; чему́; что; чем; чём', None),
    ('form', 'Liczebniki', 'Setki', 'setki', 'две́сти; три́ста; четы́реста; пятьсо́т; шестьсо́т; семьсо́т; восемьсо́т; девятьсо́т', None),
    ('decl', 'Liczebniki', 'оди́н (jeden): rodzaj męski', 'przyp', 'оди́н; одного́; одному́; оди́н; одни́м; одно́м', 'Odmienia się jak zaimek э́тот.'),
    ('decl', 'Liczebniki', 'одна́ (jedna): rodzaj żeński', 'przyp', 'одна́; одно́й; одно́й; одну́; одно́й; одно́й', None),
    ('decl', 'Liczebniki', 'два (dwa)', 'przyp', 'два; двух; двум; два; двумя́; двух', 'Z rzeczownikiem żywotnym biernik = dopełniacz: двух бра́тьев.'),
    ('decl', 'Liczebniki', 'три (trzy)', 'przyp', 'три; трёх; трём; три; тремя́; трёх', None),
    ('decl', 'Liczebniki', 'четы́ре (cztery)', 'przyp', 'четы́ре; четырёх; четырём; четы́ре; четырьмя́; четырёх', None),
    ('decl', 'Liczebniki', 'пять (pięć)', 'przyp', 'пять; пяти́; пяти́; пять; пятью́; пяти́', '5–20 i 30 odmieniają się jak rzeczowniki żeńskie na -ь; akcent pada na końcówkę.'),
    ('decl', 'Liczebniki', 'во́семь (osiem)', 'przyp', 'во́семь; восьми́; восьми́; во́семь; восемью́; восьми́', 'W temacie znika е: восьми́.'),
    ('decl', 'Liczebniki', 'со́рок (czterdzieści)', 'przyp', 'со́рок; сорока́; сорока́; со́рок; сорока́; сорока́', 'Tylko dwie formy: со́рок i сорока́. Tak samo девяно́сто i сто.'),
    ('decl', 'Liczebniki', 'сто (sto)', 'przyp', 'сто; ста; ста; сто; ста; ста', None),
    ('decl', 'Liczebniki', 'пятьдеся́т (pięćdziesiąt)', 'przyp', 'пятьдеся́т; пяти́десяти; пяти́десяти; пятьдеся́т; пятью́десятью; пяти́десяти', '50–80: odmieniają się obie części.'),
    ('decl', 'Liczebniki', 'две́сти (dwieście)', 'przyp', 'две́сти; двухсо́т; двумста́м; две́сти; двумяста́ми; двухста́х', 'W setkach odmieniają się obie części.'),
    ('decl', 'Liczebniki', 'ты́сяча (tysiąc)', 'przyp', 'ты́сяча; ты́сячи; ты́сяче; ты́сячу; ты́сячей; ты́сяче', 'Odmienia się jak rzeczownik żeński.'),
    ('decl', 'Liczebniki', 'дво́е (dwoje): zbiorowy', 'przyp', 'дво́е; двои́х; двои́м; дво́е; двои́ми; двои́х', None),
    ('decl', 'Liczebniki', 'о́ба (obaj)', 'przyp', 'о́ба; обо́их; обо́им; о́ба; обо́ими; обо́их', 'Rodzaj żeński: о́бе, обе́их.'),
    ('form', 'Liczebniki', 'Liczebnik + rzeczownik: год (rok)', 'liczrz', 'оди́н год; два го́да; три го́да; четы́ре го́да; пять лет; оди́ннадцать лет; два́дцать оди́н год; два́дцать два го́да; сто лет', 'Po 1: mianownik lp. Po 2–4: dopełniacz lp. Po 5–20: dopełniacz lm. O formie decyduje ostatnie słowo liczebnika.'),
    ('form', 'Liczebniki', 'Liczebnik + rzeczownik: кни́га (książka)', 'liczrz', 'одна́ кни́га; две кни́ги; три кни́ги; четы́ре кни́ги; пять книг; оди́ннадцать книг; два́дцать одна́ кни́га; два́дцать две кни́ги; сто книг', 'W rodzaju żeńskim: одна́, две.'),
    ('form', 'Typowe trudności', 'Fałszywi przyjaciele: co to znaczy?', 't_ff', 'kanapa; dywan; zapamiętać; zapomnieć; tydzień; rano; wkrótce; czerwony', None),
    ('form', 'Typowe trudności', 'Rekcja: jaki przypadek po czasowniku?', 't_rekcja', 'кого́ (biernik); кого́ с чем; чем (narzędnik); чему́ (celownik); чем (narzędnik); кого́, что (bez przyimka)', 'Po polsku: czekać na kogoś; po rosyjsku bez przyimka: ждать дру́га.'),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['окно́', 'письмо́', 'сестра́', 'го́род', 'дом', 'учи́тель', 'рука́', 'гора́'],
    't_m1': ['я', 'ты', 'он', 'она́', 'мы', 'вы', 'они́'],
    't_m2': ['он у́чи…ся (3. osoba)', 'на́до учи́…ся (bezokolicznik)', 'она́ смеё…ся (3. osoba)', 'хочу́ улыба́…ся (bezokolicznik)', 'они́ верну́…ся (3. osoba)', 'ну́жно верну́…ся (bezokolicznik)'],
    't_m3': ['ж…знь (życie)', 'ш…на (opona)', 'ч…сто (często)', 'щ…ка (szczupak)', 'ч…до (cud)', 'маш…на (samochód)'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Ruchomy akcent: liczba mnoga', 't_m0', 'о́кна; пи́сьма; сёстры; города́; дома́; учителя́; ру́ки; го́ры', 'W liczbie mnogiej akcent często przeskakuje. Część rzeczowników męskich ma w lm. akcentowane -а́, -я́.'),
    ('form', 'Typowe trudności', '„Mam”: у кого́ есть?', 't_m1', 'у меня́; у тебя́; у него́; у неё; у нас; у вас; у них', 'Zamiast „mam” mówi się „u mnie jest”: у меня́ есть брат.'),
    ('form', 'Typowe trudności', 'Pisownia: -тся czy -ться?', 't_m2', '-тся; -ться; -тся; -ться; -тся; -ться', 'Zapytaj: что де́лает? (bez ь) czy что де́лать? (z ь).'),
    ('form', 'Typowe trudności', 'Pisownia po ж, ш, ч, щ', 't_m3', 'и; и; а; у; у; и', 'Po ж, ш, ч, щ pisze się и, а, у, nigdy ы, я, ю.'),
]

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'мой брат': 'mój brat', 'моя́ сестра́': 'moja siostra', 'мой друг': 'mój przyjaciel', 'моя́ ма́ма': 'moja mama'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'хоро́ший (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'хоро́ший; лу́чше; лу́чший', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'большо́й (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'большо́й; бо́льше; са́мый большо́й', None),
    ('form', 'Stopniowanie', 'ма́ленький (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'ма́ленький; ме́ньше; са́мый ма́ленький', None),
    ('form', 'Stopniowanie', 'плохо́й (zły)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'плохо́й; ху́же; ху́дший', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'высо́кий (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'высо́кий; вы́ше; са́мый высо́кий', 'Zmiana spółgłoski: к → ш.'),
    ('form', 'Stopniowanie', 'краси́вый (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'краси́вый; краси́вее; са́мый краси́вый', 'Regularne: -ее.'),
    ('form', 'Stopniowanie', 'ста́рый (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'ста́рый; ста́рше; са́мый ста́рый', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 1 (generowane) ===
PARADIGMS += [
    ('form', 'Aspekt czasownika', 'aspekt: robić', ['niedokonany', 'dokonany'], 'де́лать; сде́лать', 'Niedokonany: czynność trwa lub się powtarza. Dokonany: czynność zakończona z wynikiem.'),
    ('form', 'Aspekt czasownika', 'aspekt: pisać', ['niedokonany', 'dokonany'], 'писа́ть; написа́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: czytać', ['niedokonany', 'dokonany'], 'чита́ть; прочита́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: mówić', ['niedokonany', 'dokonany'], 'говори́ть; сказа́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: kupować', ['niedokonany', 'dokonany'], 'покупа́ть; купи́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: brać', ['niedokonany', 'dokonany'], 'брать; взять', None),
    ('form', 'Aspekt czasownika', 'aspekt: dawać', ['niedokonany', 'dokonany'], 'дава́ть; дать', None),
    ('form', 'Aspekt czasownika', 'aspekt: widzieć', ['niedokonany', 'dokonany'], 'ви́деть; уви́деть', None),
    ('form', 'Aspekt czasownika', 'aspekt: otwierać', ['niedokonany', 'dokonany'], 'открыва́ть; откры́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: decydować', ['niedokonany', 'dokonany'], 'реша́ть; реши́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: opowiadać', ['niedokonany', 'dokonany'], 'расска́зывать; рассказа́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: zaczynać', ['niedokonany', 'dokonany'], 'начина́ть; нача́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: zapominać', ['niedokonany', 'dokonany'], 'забыва́ть; забы́ть', None),
    ('form', 'Aspekt czasownika', 'aspekt: jeść', ['niedokonany', 'dokonany'], 'есть; съесть', None),
    ('form', 'Aspekt czasownika', 'aspekt: pić', ['niedokonany', 'dokonany'], 'пить; вы́пить', None),
    ('form', 'Aspekt czasownika', 'aspekt: uczyć się', ['niedokonany', 'dokonany'], 'учи́ться; научи́ться', None),
    ('form', 'Aspekt czasownika', 'aspekt: odpowiadać', ['niedokonany', 'dokonany'], 'отвеча́ть; отве́тить', None),
    ('form', 'Aspekt czasownika', 'aspekt: pytać', ['niedokonany', 'dokonany'], 'спра́шивать; спроси́ть', None),
    ('form', 'Czas przeszły', 'czas przeszły: чита́ть (czytać)', ['r. męski', 'r. żeński', 'r. nijaki', 'liczba mnoga'], 'чита́л; чита́ла; чита́ло; чита́ли', None),
    ('form', 'Czas przeszły', 'czas przeszły: идти́ (iść)', ['r. męski', 'r. żeński', 'r. nijaki', 'liczba mnoga'], 'шёл; шла; шло; шли', None),
    ('form', 'Czas przeszły', 'czas przeszły: мочь (móc)', ['r. męski', 'r. żeński', 'r. nijaki', 'liczba mnoga'], 'мог; могла́; могло́; могли́', None),
    ('form', 'Czas przeszły', 'czas przeszły: хоте́ть (chcieć)', ['r. męski', 'r. żeński', 'r. nijaki', 'liczba mnoga'], 'хоте́л; хоте́ла; хоте́ло; хоте́ли', None),
    ('form', 'Czas przeszły', 'czas przeszły: жить (żyć)', ['r. męski', 'r. żeński', 'r. nijaki', 'liczba mnoga'], 'жил; жила́; жи́ло; жи́ли', None),
    ('form', 'Czas przeszły', 'czas przeszły: говори́ть (mówić)', ['r. męski', 'r. żeński', 'r. nijaki', 'liczba mnoga'], 'говори́л; говори́ла; говори́ло; говори́ли', None),
    ('form', 'Czas przeszły', 'czas przeszły: писа́ть (pisać)', ['r. męski', 'r. żeński', 'r. nijaki', 'liczba mnoga'], 'писа́л; писа́ла; писа́ло; писа́ли', None),
    ('conj', 'Czasowniki nieregularne', 'быть: czas przyszły', ['я', 'ты', 'он / она', 'мы', 'вы', 'они'], 'бу́ду; бу́дешь; бу́дет; бу́дем; бу́дете; бу́дут', None),
    ('conj', 'Czasowniki nieregularne', 'учи́ться (uczyć się)', ['я', 'ты', 'он / она', 'мы', 'вы', 'они'], 'учу́сь; у́чишься; у́чится; у́чимся; у́читесь; у́чатся', None),
    ('conj', 'Czasowniki nieregularne', 'дать (dać): dokonany', ['я', 'ты', 'он / она', 'мы', 'вы', 'они'], 'дам; дашь; даст; дади́м; дади́те; даду́т', None),
    ('form', 'Liczba mnoga', 'mnoga: друг (przyjaciel)', ['liczba pojedyncza', 'liczba mnoga'], 'друг; друзья́', 'Nieregularna liczba mnoga.'),
    ('form', 'Liczba mnoga', 'mnoga: ребёнок (dziecko)', ['liczba pojedyncza', 'liczba mnoga'], 'ребёнок; де́ти', 'Nieregularna liczba mnoga.'),
    ('form', 'Liczba mnoga', 'mnoga: челове́к (człowiek)', ['liczba pojedyncza', 'liczba mnoga'], 'челове́к; лю́ди', 'Nieregularna liczba mnoga.'),
    ('form', 'Liczba mnoga', 'mnoga: брат (brat)', ['liczba pojedyncza', 'liczba mnoga'], 'брат; бра́тья', 'Nieregularna liczba mnoga.'),
    ('form', 'Liczba mnoga', 'mnoga: мать (matka)', ['liczba pojedyncza', 'liczba mnoga'], 'мать; ма́тери', 'Nieregularna liczba mnoga.'),
    ('form', 'Liczba mnoga', 'mnoga: сын (syn)', ['liczba pojedyncza', 'liczba mnoga'], 'сын; сыновья́', 'Nieregularna liczba mnoga.'),
    ('form', 'Liczba mnoga', 'mnoga: стул (krzesło)', ['liczba pojedyncza', 'liczba mnoga'], 'стул; сту́лья', 'Nieregularna liczba mnoga.'),
    ('form', 'Liczba mnoga', 'mnoga: дерево (drzewo)', ['liczba pojedyncza', 'liczba mnoga'], 'де́рево; дере́вья', 'Nieregularna liczba mnoga.'),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: кни́га (książka)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'кни́га; книг', 'Używa się go po liczebnikach 5 i więcej oraz po słowach „мно́го”, „ма́ло”.'),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: окно́ (okno)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'окно́; о́кон', None),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: де́вушка (dziewczyna)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'де́вушка; де́вушек', None),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: рубль (rubel)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'рубль; рубле́й', None),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: студе́нт (student)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'студе́нт; студе́нтов', None),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: день (dzień)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'день; дней', None),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: друг (przyjaciel)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'друг; друзе́й', None),
    ('form', 'Dopełniacz liczby mnogiej', 'dop. mnoga: мать (matka)', ['mianownik l. poj.', 'dopełniacz l. mn.'], 'мать; матере́й', None),
    ('form', 'Typowe trudności', 'Przyimek: jaki przypadek?', ['Я иду́ в ___ (шко́ла)', 'Я в ___ (шко́ла)', 'Я иду́ из ___ (шко́ла)', 'Я иду́ к ___ (друг)', 'Я иду́ с ___ (друг)', 'Я ду́маю о ___ (друг)'], 'шко́лу; шко́ле; шко́лы; дру́гу; дру́гом; дру́ге', 'в + biernik (dokąd?), в + miejscownik (gdzie?), из + dopełniacz, к + celownik, с + narzędnik, о + miejscownik.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 1 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('ребёнок', 'dziecko', None, 'rodzaj męski'), ('де́вочка', 'dziewczynka', None, 'rodzaj żeński'), ('челове́к', 'człowiek', None, 'rodzaj męski'), ('лю́ди', 'ludzie', None, None), ('семья́', 'rodzina', None, 'rodzaj żeński'), ('мать', 'matka', None, 'rodzaj żeński'), ('оте́ц', 'ojciec', None, 'rodzaj męski'), ('сын', 'syn', None, 'rodzaj męski'), ('дочь', 'córka', None, 'rodzaj żeński'), ('де́душка', 'dziadek', None, 'rodzaj męski'), ('ба́бушка', 'babcia', None, 'rodzaj żeński'), ('вну́к', 'wnuk', None, 'rodzaj męski'), ('дя́дя', 'wujek', None, 'rodzaj męski'), ('тётя', 'ciocia', None, 'rodzaj żeński'), ('двою́родный брат', 'kuzyn', None, 'rodzaj męski'), ('муж', 'mąż', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('жена́', 'żona', None, 'rodzaj żeński'), ('сосе́д', 'sąsiad', None, 'rodzaj męski'), ('гость', 'gość', None, 'rodzaj męski'), ('нача́льник', 'szef', None, 'rodzaj męski'), ('колле́га', 'kolega', None, 'rodzaj męski'), ('враг', 'wróg', None, 'rodzaj męski'), ('коро́ль', 'król', None, 'rodzaj męski'), ('короле́ва', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('голова́', 'głowa', None, 'rodzaj żeński'), ('лицо́', 'twarz', None, 'rodzaj nijaki'), ('глаз', 'oko', None, 'rodzaj męski'), ('у́хо', 'ucho', None, 'rodzaj nijaki'), ('нос', 'nos', None, 'rodzaj męski'), ('рот', 'usta', None, 'rodzaj męski'), ('зуб', 'ząb', None, 'rodzaj męski'), ('язы́к', 'język (narząd)', None, 'rodzaj męski'), ('во́лосы', 'włosy', None, None), ('ше́я', 'szyja', None, 'rodzaj żeński'), ('рука́ (ramię)', 'ramię', None, 'rodzaj żeński'), ('кисть', 'ręka', None, 'rodzaj żeński'), ('па́лец', 'palec', None, 'rodzaj męski'), ('нога́', 'noga', None, 'rodzaj żeński'), ('стопа́', 'stopa', None, 'rodzaj żeński'), ('коле́но', 'kolano', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('спина́', 'plecy', None, 'rodzaj żeński'), ('живо́т', 'brzuch', None, 'rodzaj męski'), ('се́рдце', 'serce', None, 'rodzaj nijaki'), ('кровь', 'krew', None, 'rodzaj żeński'), ('кость', 'kość', None, 'rodzaj żeński'), ('ко́жа', 'skóra', None, 'rodzaj żeński'), ('го́лос', 'głos', None, 'rodzaj męski'), ('те́ло', 'ciało', None, 'rodzaj nijaki'), ('желу́док', 'żołądek', None, 'rodzaj męski'), ('борода́', 'broda', None, 'rodzaj żeński'), ('губа́', 'warga', None, 'rodzaj żeński'), ('но́готь', 'paznokieć', None, 'rodzaj męski'), ('грудь', 'pierś', None, 'rodzaj żeński'), ('мозг', 'mózg', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('ма́сло', 'masło', None, 'rodzaj nijaki'), ('яйцо́', 'jajko', None, 'rodzaj nijaki'), ('мя́со', 'mięso', None, 'rodzaj nijaki'), ('ку́рица', 'kurczak', None, 'rodzaj żeński'), ('свини́на', 'wieprzowina', None, 'rodzaj żeński'), ('суп', 'zupa', None, 'rodzaj męski'), ('сала́т', 'sałatka', None, 'rodzaj męski'), ('рис', 'ryż', None, 'rodzaj męski'), ('макаро́ны', 'makaron', None, None), ('карто́фель', 'ziemniak', None, 'rodzaj męski'), ('морко́вь', 'marchewka', None, 'rodzaj żeński'), ('лук', 'cebula', None, 'rodzaj męski'), ('чесно́к', 'czosnek', None, 'rodzaj męski'), ('помидо́р', 'pomidor', None, 'rodzaj męski'), ('огуре́ц', 'ogórek', None, 'rodzaj męski'), ('гру́ша', 'gruszka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('бана́н', 'banan', None, 'rodzaj męski'), ('апельси́н', 'pomarańcza', None, 'rodzaj męski'), ('лимо́н', 'cytryna', None, 'rodzaj męski'), ('клубни́ка', 'truskawka', None, 'rodzaj żeński'), ('виногра́д', 'winogrono', None, 'rodzaj męski'), ('са́хар', 'cukier', None, 'rodzaj męski'), ('соль', 'sól', None, 'rodzaj żeński'), ('пе́рец', 'pieprz', None, 'rodzaj męski'), ('ма́сло (olej)', 'olej', None, 'rodzaj nijaki'), ('мука́', 'mąka', None, 'rodzaj żeński'), ('мёд', 'miód', None, 'rodzaj męski'), ('шокола́д', 'czekolada', None, 'rodzaj męski'), ('моро́женое', 'lody', None, 'rodzaj nijaki'), ('торт', 'ciasto (tort)', None, 'rodzaj męski'), ('пече́нье', 'ciastko', None, 'rodzaj nijaki'), ('за́втрак', 'śniadanie', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('обе́д', 'obiad', None, 'rodzaj męski'), ('у́жин', 'kolacja', None, 'rodzaj męski'), ('заку́ска', 'przekąska', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('сок', 'sok', None, 'rodzaj męski'), ('пи́во', 'piwo', None, 'rodzaj nijaki'), ('вино́', 'wino', None, 'rodzaj nijaki'), ('напи́ток', 'napój', None, 'rodzaj męski'), ('стака́н', 'szklanka', None, 'rodzaj męski'), ('ча́шка', 'filiżanka', None, 'rodzaj żeński'), ('таре́лка', 'talerz', None, 'rodzaj żeński'), ('нож', 'nóż', None, 'rodzaj męski'), ('ви́лка', 'widelec', None, 'rodzaj żeński'), ('ло́жка', 'łyżka', None, 'rodzaj żeński'), ('буты́лка', 'butelka', None, 'rodzaj żeński'), ('меню́', 'menu', None, 'rodzaj nijaki'), ('счёт', 'rachunek', None, 'rodzaj męski'), ('чаевы́е', 'napiwek', None, None), ('сто́лик', 'stolik', None, 'rodzaj męski'), ('официа́нт', 'kelner', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('по́вар', 'kucharz', None, 'rodzaj męski'), ('голо́дный', 'głodny', None, None), ('хотя́щий пить', 'spragniony', None, None), ('вку́сный', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('кварти́ра', 'mieszkanie', None, 'rodzaj żeński'), ('ко́мната', 'pokój', None, 'rodzaj żeński'), ('ку́хня', 'kuchnia', None, 'rodzaj żeński'), ('ва́нная', 'łazienka', None, 'rodzaj żeński'), ('спа́льня', 'sypialnia', None, 'rodzaj żeński'), ('гости́ная', 'salon', None, 'rodzaj żeński'), ('сад', 'ogród', None, 'rodzaj męski'), ('дверь', 'drzwi', None, 'rodzaj żeński'), ('окно́', 'okno', None, 'rodzaj nijaki'), ('стена́', 'ściana', None, 'rodzaj żeński'), ('пол', 'podłoga', None, 'rodzaj męski'), ('крыша', 'dach', None, 'rodzaj żeński'), ('ле́стница', 'schody', None, 'rodzaj żeński'), ('ключ', 'klucz', None, 'rodzaj męski'), ('стол', 'stół', None, 'rodzaj męski'), ('стул', 'krzesło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('крова́ть', 'łóżko', None, 'rodzaj żeński'), ('шкаф', 'szafa', None, 'rodzaj męski'), ('ла́мпа', 'lampa', None, 'rodzaj żeński'), ('ковёр', 'dywan', None, 'rodzaj męski'), ('зе́ркало', 'lustro', None, 'rodzaj nijaki'), ('телеви́зор', 'telewizor', None, 'rodzaj męski'), ('телефо́н', 'telefon', None, 'rodzaj męski'), ('компью́тер', 'komputer', None, 'rodzaj męski'), ('часы́', 'zegar', None, None), ('поду́шка', 'poduszka', None, 'rodzaj żeński'), ('одея́ло', 'koc', None, 'rodzaj nijaki'), ('полоте́нце', 'ręcznik', None, 'rodzaj nijaki'), ('мы́ло', 'mydło', None, 'rodzaj nijaki'), ('зубна́я щётка', 'szczoteczka do zębów', None, 'rodzaj żeński'), ('холоди́льник', 'lodówka', None, 'rodzaj męski'), ('печь', 'piec', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('стира́льная маши́на', 'pralka', None, 'rodzaj żeński'), ('му́сор', 'śmieci', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('оде́жда', 'ubranie', None, 'rodzaj żeński'), ('руба́шка', 'koszula', None, 'rodzaj żeński'), ('брюки', 'spodnie', None, None), ('пла́тье', 'sukienka', None, 'rodzaj nijaki'), ('ю́бка', 'spódnica', None, 'rodzaj żeński'), ('ку́ртка', 'kurtka', None, 'rodzaj żeński'), ('пальто́', 'płaszcz', None, 'rodzaj nijaki'), ('сви́тер', 'sweter', None, 'rodzaj męski'), ('о́бувь', 'buty', None, 'rodzaj żeński'), ('носки́', 'skarpetki', None, None), ('ша́пка', 'czapka', None, 'rodzaj żeński'), ('шля́па', 'kapelusz', None, 'rodzaj żeński'), ('перча́тки', 'rękawiczki', None, None), ('шарф', 'szalik', None, 'rodzaj męski'), ('су́мка', 'torba', None, 'rodzaj żeński'), ('рюкза́к', 'plecak', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('кошелёк', 'portfel', None, 'rodzaj męski'), ('очки́', 'okulary', None, None), ('нару́чные часы́', 'zegarek', None, None), ('кольцо́', 'pierścionek', None, 'rodzaj nijaki'), ('бельё', 'bielizna', None, 'rodzaj nijaki'), ('пижа́ма', 'piżama', None, 'rodzaj żeński'), ('реме́нь', 'pasek', None, 'rodzaj męski'), ('га́лстук', 'krawat', None, 'rodzaj męski'), ('костю́м', 'garnitur', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('кра́сный', 'czerwony', None, None), ('си́ний', 'niebieski', None, None), ('зелёный', 'zielony', None, None), ('жёлтый', 'żółty', None, None), ('чёрный', 'czarny', None, None), ('бе́лый', 'biały', None, None), ('се́рый', 'szary', None, None), ('коричневый', 'brązowy', None, None), ('ро́зовый', 'różowy', None, None), ('фиоле́товый', 'fioletowy', None, None), ('цвет', 'kolor', None, 'rodzaj męski'), ('кру́глый', 'okrągły', None, None), ('квадра́тный', 'kwadratowy', None, None), ('прямо́й', 'prosty', None, None), ('криво́й', 'krzywy', None, None), ('ли́ния', 'linia', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('то́чка', 'punkt', None, 'rodzaj żeński'), ('круг', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('ноль', 'zero', None, None), ('оди́ннадцать', 'jedenaście', None, None), ('двена́дцать', 'dwanaście', None, None), ('трина́дцать', 'trzynaście', None, None), ('четы́рнадцать', 'czternaście', None, None), ('пятна́дцать', 'piętnaście', None, None), ('шестна́дцать', 'szesnaście', None, None), ('семна́дцать', 'siedemnaście', None, None), ('восемна́дцать', 'osiemnaście', None, None), ('девятна́дцать', 'dziewiętnaście', None, None), ('два́дцать', 'dwadzieścia', None, None), ('три́дцать', 'trzydzieści', None, None), ('со́рок', 'czterdzieści', None, None), ('пятьдеся́т', 'pięćdziesiąt', None, None), ('шестьдеся́т', 'sześćdziesiąt', None, None), ('се́мьдесят', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('во́семьдесят', 'osiemdziesiąt', None, None), ('девяно́сто', 'dziewięćdziesiąt', None, None), ('сто', 'sto', None, None), ('ты́сяча', 'tysiąc', None, None), ('миллио́н', 'milion', None, None), ('пе́рвый', 'pierwszy', None, None), ('второ́й', 'drugi', None, None), ('тре́тий', 'trzeci', None, None), ('полови́на', 'połowa', None, 'rodzaj żeński'), ('па́ра', 'para', None, 'rodzaj żeński'), ('не́сколько', 'kilka', None, None), ('мно́го', 'wiele', None, None), ('ма́ло', 'mało', None, None), ('весь', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('секу́нда', 'sekunda', None, 'rodzaj żeński'), ('мину́та', 'minuta', None, 'rodzaj żeński'), ('час', 'godzina', None, 'rodzaj męski'), ('ночь', 'noc', None, 'rodzaj żeński'), ('неде́ля', 'tydzień', None, 'rodzaj żeński'), ('ме́сяц', 'miesiąc', None, 'rodzaj męski'), ('год', 'rok', None, 'rodzaj męski'), ('весна́', 'wiosna', None, 'rodzaj żeński'), ('ле́то', 'lato', None, 'rodzaj nijaki'), ('о́сень', 'jesień', None, 'rodzaj żeński'), ('зима́', 'zima', None, 'rodzaj żeński'), ('понеде́льник', 'poniedziałek', None, 'rodzaj męski'), ('вто́рник', 'wtorek', None, 'rodzaj męski'), ('среда́', 'środa', None, 'rodzaj żeński'), ('четве́рг', 'czwartek', None, 'rodzaj męski'), ('пя́тница', 'piątek', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('суббо́та', 'sobota', None, 'rodzaj żeński'), ('воскресе́нье', 'niedziela', None, 'rodzaj nijaki'), ('янва́рь', 'styczeń', None, 'rodzaj męski'), ('февра́ль', 'luty', None, 'rodzaj męski'), ('март', 'marzec', None, 'rodzaj męski'), ('апре́ль', 'kwiecień', None, 'rodzaj męski'), ('май', 'maj', None, 'rodzaj męski'), ('ию́нь', 'czerwiec', None, 'rodzaj męski'), ('ию́ль', 'lipiec', None, 'rodzaj męski'), ('а́вгуст', 'sierpień', None, 'rodzaj męski'), ('сентя́брь', 'wrzesień', None, 'rodzaj męski'), ('октя́брь', 'październik', None, 'rodzaj męski'), ('ноя́брь', 'listopad', None, 'rodzaj męski'), ('дека́брь', 'grudzień', None, 'rodzaj męski'), ('у́тро', 'rano (pora dnia)', None, 'rodzaj nijaki'), ('полдень', 'południe', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('ве́чером', 'wieczorem', None, None), ('всегда́', 'zawsze', None, None), ('никогда́', 'nigdy', None, None), ('иногда́', 'czasem', None, None), ('ча́сто', 'często', None, None), ('уже́', 'już', None, None), ('ещё', 'jeszcze', None, None), ('ско́ро', 'wkrótce', None, None), ('по́зже', 'później', None, None), ('ра́но', 'wcześnie', None, None), ('по́здно', 'późno', None, None), ('когда́', 'kiedy (pytanie)', None, None), ('да́та', 'data', None, 'rodzaj żeński'), ('про́шлое', 'przeszłość', None, 'rodzaj nijaki'), ('бу́дущее', 'przyszłość', None, 'rodzaj nijaki'), ('день рожде́ния', 'urodziny', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('пра́здник', 'święto', None, 'rodzaj męski'), ('о́тпуск', 'wakacje', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('со́лнце', 'słońce', None, 'rodzaj nijaki'), ('луна́', 'księżyc', None, 'rodzaj żeński'), ('звезда́', 'gwiazda', None, 'rodzaj żeński'), ('не́бо', 'niebo', None, 'rodzaj nijaki'), ('о́блако', 'chmura', None, 'rodzaj nijaki'), ('дождь', 'deszcz', None, 'rodzaj męski'), ('снег', 'śnieg', None, 'rodzaj męski'), ('ве́тер', 'wiatr', None, 'rodzaj męski'), ('гроза́', 'burza', None, 'rodzaj żeński'), ('тума́н', 'mgła', None, 'rodzaj męski'), ('лёд', 'lód', None, 'rodzaj męski'), ('ого́нь', 'ogień', None, None), ('земля́', 'grunt)', None, 'rodzaj żeński'), ('река́', 'rzeka', None, 'rodzaj żeński'), ('о́зеро', 'jezioro', None, 'rodzaj nijaki'), ('гора́', 'góra', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('лес', 'las', None, 'rodzaj męski'), ('де́рево', 'drzewo', None, 'rodzaj nijaki'), ('цвето́к', 'kwiat', None, 'rodzaj męski'), ('трава́', 'trawa', None, 'rodzaj żeński'), ('лист', 'liść', None, 'rodzaj męski'), ('по́ле', 'pole', None, 'rodzaj nijaki'), ('о́стров', 'wyspa', None, 'rodzaj męski'), ('пляж', 'plaża', None, 'rodzaj męski'), ('пусты́ня', 'pustynia', None, 'rodzaj żeński'), ('ска́ла', 'skała', None, 'rodzaj żeński'), ('ка́мень', 'kamień', None, 'rodzaj męski'), ('пого́да', 'pogoda', None, 'rodzaj żeński'), ('температу́ра', 'temperatura', None, 'rodzaj żeński'), ('холо́дный', 'zimny', None, None), ('тёплый', 'ciepły', None, None), ('горя́чий', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('соба́ка', 'pies', None, 'rodzaj żeński'), ('кот', 'kot', None, 'rodzaj męski'), ('ло́шадь', 'koń', None, 'rodzaj żeński'), ('коро́ва', 'krowa', None, 'rodzaj żeński'), ('свинья́', 'świnia', None, 'rodzaj żeński'), ('овца́', 'owca', None, 'rodzaj żeński'), ('коза́', 'koza', None, 'rodzaj żeński'), ('ку́рица (ptak)', 'kura', None, 'rodzaj żeński'), ('у́тка', 'kaczka', None, 'rodzaj żeński'), ('пти́ца', 'ptak', None, 'rodzaj żeński'), ('мышь', 'mysz', None, 'rodzaj żeński'), ('крыса', 'szczur', None, 'rodzaj żeński'), ('змея́', 'wąż', None, 'rodzaj żeński'), ('лягу́шка', 'żaba', None, 'rodzaj żeński'), ('лев', 'lew', None, 'rodzaj męski'), ('тигр', 'tygrys', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('слон', 'słoń', None, 'rodzaj męski'), ('медве́дь', 'niedźwiedź', None, 'rodzaj męski'), ('волк', 'wilk', None, 'rodzaj męski'), ('лиса́', 'lis', None, 'rodzaj żeński'), ('за́яц', 'zając', None, 'rodzaj męski'), ('оле́нь', 'jeleń', None, 'rodzaj męski'), ('обезья́на', 'małpa', None, 'rodzaj żeński'), ('ба́бочка', 'motyl', None, 'rodzaj żeński'), ('пчела́', 'pszczoła', None, 'rodzaj żeński'), ('му́ха', 'mucha', None, 'rodzaj żeński'), ('паук', 'pająk', None, 'rodzaj męski'), ('живо́тное', 'zwierzę', None, 'rodzaj nijaki'), ('насеко́мое', 'owad', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('дере́вня', 'wieś', None, 'rodzaj żeński'), ('доро́га', 'droga', None, 'rodzaj żeński'), ('пло́щадь', 'plac', None, 'rodzaj żeński'), ('мост', 'most', None, 'rodzaj męski'), ('парк', 'park', None, 'rodzaj męski'), ('магази́н', 'sklep', None, 'rodzaj męski'), ('ры́нок', 'targ', None, 'rodzaj męski'), ('супермарке́т', 'supermarket', None, 'rodzaj męski'), ('банк', 'bank', None, 'rodzaj męski'), ('по́чта', 'poczta', None, 'rodzaj żeński'), ('больни́ца', 'szpital', None, 'rodzaj żeński'), ('апте́ка', 'apteka', None, 'rodzaj żeński'), ('университе́т', 'uniwersytet', None, 'rodzaj męski'), ('библиоте́ка', 'biblioteka', None, 'rodzaj żeński'), ('музе́й', 'muzeum', None, 'rodzaj męski'), ('це́рковь', 'kościół', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('рестора́н', 'restauracja', None, 'rodzaj męski'), ('кафе́', 'kawiarnia', None, 'rodzaj nijaki'), ('аэропо́рт', 'lotnisko', None, 'rodzaj męski'), ('вокза́л', 'dworzec', None, 'rodzaj męski'), ('остано́вка', 'przystanek', None, 'rodzaj żeński'), ('кино́', 'kino', None, 'rodzaj nijaki'), ('теа́тр', 'teatr', None, 'rodzaj męski'), ('поли́ция', 'policja', None, 'rodzaj żeński'), ('о́фис', 'biuro', None, 'rodzaj męski'), ('заво́д', 'fabryka', None, 'rodzaj męski'), ('зда́ние', 'budynek', None, 'rodzaj nijaki'), ('ба́шня', 'wieża', None, 'rodzaj żeński'), ('центр', 'centrum', None, 'rodzaj męski'), ('а́дрес', 'adres', None, 'rodzaj męski'), ('ка́рта', 'mapa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('маши́на', 'samochód', None, 'rodzaj żeński'), ('авто́бус', 'autobus', None, 'rodzaj męski'), ('по́езд', 'pociąg', None, 'rodzaj męski'), ('трамва́й', 'tramwaj', None, 'rodzaj męski'), ('метро́', 'metro', None, 'rodzaj nijaki'), ('самолёт', 'samolot', None, 'rodzaj męski'), ('кора́бль', 'statek', None, 'rodzaj męski'), ('велосипе́д', 'rower', None, 'rodzaj męski'), ('мотоци́кл', 'motocykl', None, 'rodzaj męski'), ('биле́т', 'bilet', None, 'rodzaj męski'), ('путеше́ствие', 'podróż', None, 'rodzaj nijaki'), ('экскурсия', 'wycieczka', None, 'rodzaj żeński'), ('па́спорт', 'paszport', None, 'rodzaj męski'), ('чемода́н', 'walizka', None, 'rodzaj męski'), ('бензи́н', 'benzyna', None, 'rodzaj męski'), ('парко́вка', 'parking', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('перекрёсток', 'skrzyżowanie', None, 'rodzaj męski'), ('светофо́р', 'światła', None, 'rodzaj męski'), ('води́тельские права́', 'prawo jazdy', None, None), ('води́тель', 'kierowca', None, 'rodzaj męski'), ('пассажи́р', 'pasażer', None, 'rodzaj męski'), ('въезд', 'wjazd', None, 'rodzaj męski'), ('вы́езд', 'wyjazd', None, 'rodzaj męski'), ('желе́зная доро́га', 'kolej', None, 'rodzaj żeński'), ('порт', 'port', None, 'rodzaj męski'), ('грани́ца', 'granica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('рабо́та', 'praca', None, 'rodzaj żeński'), ('профе́ссия', 'zawód', None, 'rodzaj żeński'), ('врач', 'lekarz', None, 'rodzaj męski'), ('медсестра́', 'pielęgniarka', None, 'rodzaj żeński'), ('учениќ', 'uczeń', None, 'rodzaj męski'), ('инжене́р', 'inżynier', None, 'rodzaj męski'), ('юри́ст', 'prawnik', None, 'rodzaj męski'), ('полице́йский', 'policjant', None, 'rodzaj męski'), ('солда́т', 'żołnierz', None, 'rodzaj męski'), ('фе́рмер', 'rolnik', None, 'rodzaj męski'), ('продаве́ц', 'sprzedawca', None, 'rodzaj męski'), ('касси́р', 'kasjer', None, 'rodzaj męski'), ('актёр', 'aktor', None, 'rodzaj męski'), ('писа́тель', 'pisarz', None, 'rodzaj męski'), ('худо́жник', 'malarz', None, 'rodzaj męski'), ('музыка́нт', 'muzyk', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('арти́ст', 'artysta', None, 'rodzaj męski'), ('фи́рма', 'firma', None, 'rodzaj żeński'), ('де́ньги', 'pieniądze', None, None), ('зарпла́та', 'pensja', None, 'rodzaj żeński'), ('догово́р', 'umowa', None, 'rodzaj męski'), ('встре́ча', 'spotkanie', None, 'rodzaj żeński'), ('уро́к', 'lekcja', None, 'rodzaj męski'), ('экза́мен', 'egzamin', None, 'rodzaj męski'), ('отме́тка', 'ocena', None, 'rodzaj żeński'), ('класс', 'klasa', None, 'rodzaj męski'), ('кни́га', 'książka', None, 'rodzaj żeński'), ('тетра́дь', 'zeszyt', None, 'rodzaj żeński'), ('ру́чка', 'długopis', None, 'rodzaj żeński'), ('карандаш', 'ołówek', None, 'rodzaj męski'), ('бума́га', 'papier', None, 'rodzaj żeński'), ('доска́', 'tablica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('слова́рь', 'słownik', None, 'rodzaj męski'), ('вопро́с', 'pytanie', None, 'rodzaj męski'), ('отве́т', 'odpowiedź', None, 'rodzaj męski'), ('зада́ние', 'zadanie', None, 'rodzaj nijaki'), ('тест', 'test', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('цена́', 'cena', None, 'rodzaj żeński'), ('ка́рта (płatnicza)', 'karta (płatnicza)', None, 'rodzaj żeński'), ('нали́чные', 'gotówka', None, None), ('моне́та', 'moneta', None, 'rodzaj żeński'), ('банкно́та', 'banknot', None, 'rodzaj żeński'), ('сда́ча', 'reszta', None, 'rodzaj żeński'), ('ски́дка', 'zniżka', None, 'rodzaj żeński'), ('корзи́на', 'koszyk', None, 'rodzaj żeński'), ('чек', 'paragon', None, 'rodzaj męski'), ('това́р', 'towar', None, 'rodzaj męski'), ('поку́пка', 'zakup', None, 'rodzaj żeński'), ('прода́жа', 'sprzedaż', None, 'rodzaj żeński'), ('сто́имость', 'wartość', None, 'rodzaj żeński'), ('креди́т', 'kredyt', None, 'rodzaj męski'), ('долг', 'dług', None, 'rodzaj męski'), ('нало́г', 'podatek', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('бога́тство', 'bogactwo', None, 'rodzaj nijaki'), ('бе́дный', 'biedny', None, None), ('бога́тый', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('здоро́вье', 'zdrowie', None, 'rodzaj nijaki'), ('боле́знь', 'choroba', None, 'rodzaj żeński'), ('боль', 'ból', None, 'rodzaj żeński'), ('температу́ра (gorączka)', 'gorączka', None, 'rodzaj żeński'), ('ка́шель', 'kaszel', None, 'rodzaj męski'), ('на́сморк', 'katar', None, 'rodzaj męski'), ('лека́рство', 'lekarstwo', None, 'rodzaj nijaki'), ('табле́тка', 'tabletka', None, 'rodzaj żeński'), ('опера́ция', 'operacja', None, 'rodzaj żeński'), ('ра́на', 'rana', None, 'rodzaj żeński'), ('несча́стный слу́чай', 'wypadek', None, 'rodzaj męski'), ('здоро́вый', 'zdrowy', None, None), ('больно́й', 'chory', None, None), ('уста́лый', 'zmęczony', None, None), ('со́нный', 'śpiący', None, None), ('си́льный', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('сла́бый', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('ра́дость', 'radość', None, 'rodzaj żeński'), ('гру́сть', 'smutek', None, 'rodzaj żeński'), ('страх', 'strach', None, 'rodzaj męski'), ('гнев', 'gniew', None, 'rodzaj męski'), ('любо́вь', 'miłość', None, 'rodzaj żeński'), ('не́нависть', 'nienawiść', None, 'rodzaj żeński'), ('наде́жда', 'nadzieja', None, 'rodzaj żeński'), ('мечта́', 'marzenie', None, 'rodzaj żeński'), ('сча́стье', 'szczęście', None, 'rodzaj nijaki'), ('стыд', 'wstyd', None, 'rodzaj męski'), ('удивле́ние', 'zdziwienie', None, 'rodzaj nijaki'), ('любопы́тство', 'ciekawość', None, 'rodzaj nijaki'), ('терпе́ние', 'cierpliwość', None, 'rodzaj nijaki'), ('хра́брость', 'odwaga', None, 'rodzaj żeński'), ('и́скренний', 'szczery', None, None), ('ми́лый', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('ве́жливый', 'grzeczny', None, None), ('глу́пый', 'głupi', None, None), ('у́мный', 'mądry', None, None), ('ле́нивый', 'leniwy', None, None), ('трудолюби́вый', 'pracowity', None, None), ('интере́сный', 'ciekawy', None, None), ('ску́чный', 'nudny', None, None), ('весёлый', 'wesoły', None, None), ('гру́стный', 'smutny', None, None), ('злой', 'zły (rozgniewany)', None, None), ('счастли́вый', 'szczęśliwy', None, None), ('влюблённый', 'zakochany', None, None), ('одино́кий', 'samotny', None, None), ('споко́йный', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('большо́й', 'duży', None, None), ('дли́нный', 'długi', None, None), ('коро́ткий', 'krótki', None, None), ('высо́кий', 'wysoki', None, None), ('ни́зкий', 'niski', None, None), ('широ́кий', 'szeroki', None, None), ('у́зкий', 'wąski', None, None), ('то́лстый', 'gruby', None, None), ('худо́й', 'chudy', None, None), ('тяжёлый', 'ciężki', None, None), ('лёгкий', 'lekki', None, None), ('бы́стрый', 'szybki', None, None), ('ме́дленный', 'wolny', None, None), ('твёрдый', 'twardy', None, None), ('мя́гкий', 'miękki', None, None), ('мо́крый', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('сухо́й', 'suchy', None, None), ('чи́стый', 'czysty', None, None), ('гря́зный', 'brudny', None, None), ('по́лный', 'pełny', None, None), ('пусто́й', 'pusty', None, None), ('о́стрый', 'ostry', None, None), ('гро́мкий', 'głośny', None, None), ('ти́хий', 'cichy', None, None), ('све́тлый', 'jasny', None, None), ('тёмный', 'ciemny', None, None), ('молодо́й', 'młody', None, None), ('ста́рый', 'stary', None, None), ('но́вый', 'nowy', None, None), ('хоро́ший', 'dobry', None, None), ('плохо́й', 'zły (niedobry)', None, None), ('краси́вый', 'ładny', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('некраси́вый', 'brzydki', None, None), ('лёгкий (łatwy)', 'łatwy', None, None), ('тру́дный', 'trudny', None, None), ('ва́жный', 'ważny', None, None), ('возмо́жный', 'możliwy', None, None), ('настоя́щий', 'prawdziwy', None, None), ('ло́жный', 'fałszywy', None, None), ('дорого́й', 'drogi', None, None), ('дешёвый', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('быть', 'być', None, None), ('име́ть', 'mieć', None, None), ('де́лать', 'robić', None, None), ('идти́', 'iść', None, None), ('е́хать', 'jechać', None, None), ('приходи́ть', 'przyjść', None, None), ('выходи́ть', 'wyjść', None, None), ('входи́ть', 'wejść', None, None), ('возвраща́ться', 'wrócić', None, None), ('бежа́ть', 'biec', None, None), ('стоя́ть', 'stać', None, None), ('сиде́ть', 'siedzieć', None, None), ('лежа́ть', 'leżeć', None, None), ('спать', 'spać', None, None), ('встава́ть', 'wstać', None, None), ('пить', 'pić', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('гото́вить', 'gotować', None, None), ('мыть', 'myć', None, None), ('одева́ться', 'ubierać się', None, None), ('говори́ть', 'mówić', None, None), ('сказа́ть', 'powiedzieć', None, None), ('спра́шивать', 'pytać', None, None), ('отвеча́ть', 'odpowiadać', None, None), ('слы́шать', 'słyszeć', None, None), ('слу́шать', 'słuchać', None, None), ('ви́деть', 'widzieć', None, None), ('смотре́ть', 'patrzeć', None, None), ('чита́ть', 'czytać', None, None), ('писа́ть', 'pisać', None, None), ('учи́ться', 'uczyć się', None, None), ('учи́ть', 'uczyć (kogoś)', None, None), ('понима́ть', 'rozumieć', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('знать', 'wiedzieć', None, None), ('знако́м быть', 'znać', None, None), ('ду́мать', 'myśleć', None, None), ('помни́ть', 'pamiętać', None, None), ('забыва́ть', 'zapominać', None, None), ('хоте́ть', 'chcieć', None, None), ('люби́ть', 'lubić', None, None), ('обожа́ть', 'kochać', None, None), ('нужда́ться', 'potrzebować', None, None), ('мочь', 'móc', None, None), ('быть до́лжным', 'musieć', None, None), ('дава́ть', 'dawać', None, None), ('брать', 'brać', None, None), ('покупа́ть', 'kupować', None, None), ('продава́ть', 'sprzedawać', None, None), ('плати́ть', 'płacić', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('открыва́ть', 'otwierać', None, None), ('закрыва́ть', 'zamykać', None, None), ('начина́ть', 'zaczynać', None, None), ('конча́ть', 'kończyć', None, None), ('рабо́тать', 'pracować', None, None), ('игра́ть', 'grać', None, None), ('петь', 'śpiewać', None, None), ('танцева́ть', 'tańczyć', None, None), ('пла́вать', 'pływać', None, None), ('лета́ть', 'latać', None, None), ('класть', 'kłaść', None, None), ('иска́ть', 'szukać', None, None), ('находи́ть', 'znajdować', None, None), ('ждать', 'czekać', None, None), ('помога́ть', 'pomagać', None, None), ('проси́ть', 'prosić', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('извиня́ться', 'przepraszać', None, None), ('разреша́ть', 'pozwalać', None, None), ('пыта́ться', 'próbować', None, None), ('меня́ть', 'zmieniać', None, None), ('носи́ть', 'nosić', None, None), ('держа́ть', 'trzymać', None, None), ('броса́ть', 'rzucać', None, None), ('лови́ть', 'łapać', None, None), ('бить', 'bić', None, None), ('убива́ть', 'zabijać', None, None), ('умира́ть', 'umierać', None, None), ('жить', 'żyć', None, None), ('проживать', 'mieszkać', None, None), ('встреча́ть', 'spotykać', None, None), ('звони́ть', 'dzwonić', None, None), ('посыла́ть', 'wysyłać', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('получа́ть', 'dostawać', None, None), ('пока́зывать', 'pokazywać', None, None), ('приглаша́ть', 'zapraszać', None, None), ('посеща́ть', 'odwiedzać', None, None), ('пла́кать', 'płakać', None, None), ('смея́ться', 'śmiać się', None, None), ('улыба́ться', 'uśmiechać się', None, None), ('боя́ться', 'bać się', None, None), ('ра́доваться', 'cieszyć się', None, None), ('ве́рить', 'wierzyć', None, None), ('соглаша́ться', 'zgadzać się', None, None), ('выбира́ть', 'wybierać', None, None), ('реша́ть', 'decydować', None, None), ('счита́ть', 'liczyć', None, None), ('взве́шивать', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('ходи́ть', 'chodzić', None, None), ('е́здить', 'jeździć', None, None), ('сади́ться', 'wsiadać', None, None), ('выходи́ть (z pojazdu)', 'wysiadać', None, None), ('поверну́ть', 'skręcać', None, None), ('остана́вливаться', 'zatrzymywać się', None, None), ('опа́здывать', 'spóźniać się', None, None), ('спеши́ть', 'spieszyć się', None, None), ('отдыха́ть', 'odpoczywać', None, None), ('игра́ть (bawić się)', 'bawić się', None, None), ('рисова́ть', 'rysować', None, None), ('стро́ить', 'budować', None, None), ('чини́ть', 'naprawiać', None, None), ('ре́зать', 'ciąć', None, None), ('жа́рить', 'smażyć', None, None), ('печь (piec)', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('меша́ть', 'mieszać', None, None), ('налива́ть', 'nalewać', None, None), ('убира́ть', 'sprzątać', None, None), ('стира́ть', 'prać', None, None), ('гла́дить', 'prasować', None, None), ('бри́ться', 'golić się', None, None), ('причёсывать', 'czesać', None, None), ('купа́ться', 'kąpać się', None, None), ('просыпа́ться', 'budzić się', None, None), ('засыпа́ть', 'zasypiać', None, None), ('мечта́ть', 'marzyć', None, None), ('сниться', 'śnić', None, None), ('упражня́ться', 'ćwiczyć', None, None), ('тренирова́ться', 'trenować', None, None), ('выи́грывать', 'wygrywać', None, None), ('проигрывать', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('дви́гать', 'ruszać', None, None), ('тяну́ть', 'ciągnąć', None, None), ('толка́ть', 'pchać', None, None), ('поднима́ть', 'podnosić', None, None), ('па́дать', 'spadać', None, None), ('пры́гать', 'skakać', None, None), ('лезть', 'wspinać się', None, None), ('пря́тать', 'ukrywać', None, None), ('красть', 'kraść', None, None), ('отдава́ть', 'oddawać', None, None), ('одолжи́ть', 'pożyczać', None, None), ('тра́тить', 'wydawać', None, None), ('экономи́ть', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('тот', 'ten', None, None), ('вон тот', 'tamten', None, None), ('как', 'jak', None, None), ('почему́', 'dlaczego', None, None), ('что', 'co', None, None), ('кто', 'kto', None, None), ('кото́рый', 'który', None, None), ('како́й', 'jaki', None, None), ('но', 'ale', None, None), ('и́ли', 'lub', None, None), ('потому́ что', 'bo', None, None), ('е́сли', 'jeśli', None, None), ('что (spójnik)', 'że', None, None), ('поэ́тому', 'więc', None, None), ('тоже', 'też', None, None), ('то́лько', 'tylko', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('немно́го', 'trochę', None, None), ('мно́го (dużo)', 'dużo', None, None), ('всё', 'wszystko', None, None), ('ничего́', 'nic', None, None), ('что-то', 'coś', None, None), ('кто-то', 'ktoś', None, None), ('никто́', 'nikt', None, None), ('ка́ждый', 'każdy', None, None), ('друго́й', 'inny', None, None), ('тот же', 'ten sam', None, None), ('мо́жет быть', 'może (być)', None, None), ('наве́рное', 'na pewno', None, None), ('вме́сте', 'razem', None, None), ('сам', 'sam', None, None), ('без', 'bez', None, None), ('с', 'z (towarzysząc)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('на', 'na (powierzchni)', None, None), ('к', 'do (kierunek)', None, None), ('от', 'od', None, None), ('для', 'dla', None, None), ('через', 'przez', None, None), ('по́сле', 'po (czas)', None, None), ('пе́ред', 'przed', None, None), ('за', 'za (z tyłu)', None, None), ('над', 'nad', None, None), ('под', 'pod', None, None), ('ря́дом с', 'obok', None, None), ('ме́жду', 'między', None, None), ('про́тив', 'przeciw', None, None), ('о', 'o (temat)', None, None), ('о́коло', 'około', None, None), ('почти́', 'prawie', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('да́же', 'nawet', None, None), ('ещё раз', 'jeszcze raz', None, None), ('тогда́', 'wtedy', None, None), ('где́-то', 'gdzieś', None, None), ('нигде́', 'nigdzie', None, None), ('везде́', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('жизнь', 'życie', None, 'rodzaj żeński'), ('смерть', 'śmierć', None, 'rodzaj żeński'), ('мир', 'świat', None, 'rodzaj męski'), ('страна́', 'kraj', None, 'rodzaj żeński'), ('госуда́рство', 'państwo', None, 'rodzaj nijaki'), ('язы́к (mowa)', 'język (mowa)', None, 'rodzaj męski'), ('сло́во', 'słowo', None, 'rodzaj nijaki'), ('предложе́ние', 'zdanie', None, 'rodzaj nijaki'), ('и́мя', 'imię', None, 'rodzaj nijaki'), ('фами́лия', 'nazwisko', None, 'rodzaj żeński'), ('во́зраст', 'wiek', None, 'rodzaj męski'), ('исто́рия', 'historia', None, 'rodzaj żeński'), ('культу́ра', 'kultura', None, 'rodzaj żeński'), ('рели́гия', 'religia', None, 'rodzaj żeński'), ('Бог', 'Bóg', None, 'rodzaj męski'), ('война́', 'wojna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('мир (pokój)', 'pokój (brak wojny)', None, 'rodzaj męski'), ('зако́н', 'prawo (przepis)', None, 'rodzaj męski'), ('свобо́да', 'wolność', None, 'rodzaj żeński'), ('власть', 'władza', None, 'rodzaj żeński'), ('прави́тельство', 'rząd', None, 'rodzaj nijaki'), ('вы́боры', 'wybory', None, None), ('пробле́ма', 'problem', None, 'rodzaj żeński'), ('иде́я', 'pomysł', None, 'rodzaj żeński'), ('причи́на', 'powód', None, 'rodzaj żeński'), ('результа́т', 'wynik', None, 'rodzaj męski'), ('спо́соб', 'sposób', None, 'rodzaj męski'), ('нача́ло', 'początek', None, 'rodzaj nijaki'), ('коне́ц', 'koniec', None, 'rodzaj męski'), ('часть', 'część', None, 'rodzaj żeński'), ('ме́сто', 'miejsce', None, 'rodzaj nijaki'), ('вещь', 'rzecz', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('дело́', 'sprawa', None, 'rodzaj nijaki'), ('информа́ция', 'informacja', None, 'rodzaj żeński'), ('сообще́ние', 'wiadomość', None, 'rodzaj nijaki'), ('письмо́', 'list', None, 'rodzaj nijaki'), ('газе́та', 'gazeta', None, 'rodzaj żeński'), ('фильм', 'film', None, 'rodzaj męski'), ('му́зыка', 'muzyka', None, 'rodzaj żeński'), ('пе́сня', 'piosenka', None, 'rodzaj żeński'), ('карти́на', 'obraz', None, 'rodzaj żeński'), ('игра́', 'gra', None, 'rodzaj żeński'), ('спорт', 'sport', None, 'rodzaj męski'), ('матч', 'mecz', None, 'rodzaj męski'), ('кома́нда', 'drużyna', None, 'rodzaj żeński'), ('мяч', 'piłka', None, 'rodzaj męski'), ('весе́лье', 'zabawa', None, 'rodzaj nijaki'), ('ве́чер', 'impreza', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('пода́рок', 'prezent', None, 'rodzaj męski'), ('сон', 'sen', None, 'rodzaj męski'), ('план', 'plan', None, 'rodzaj męski'), ('вы́бор', 'wybór', None, 'rodzaj męski'), ('оши́бка', 'błąd', None, 'rodzaj żeński'), ('пра́вда', 'prawda', None, 'rodzaj żeński'), ('ложь', 'kłamstwo', None, 'rodzaj żeński'), ('та́йна', 'tajemnica', None, 'rodzaj żeński'), ('си́ла', 'siła', None, 'rodzaj żeński'), ('эне́ргия', 'energia', None, 'rodzaj żeński'), ('свет', 'światło', None, 'rodzaj męski'), ('звук', 'dźwięk', None, 'rodzaj męski'), ('тишина́', 'cisza', None, 'rodzaj żeński'), ('движе́ние', 'ruch', None, 'rodzaj nijaki'), ('переме́на', 'zmiana', None, 'rodzaj żeński'), ('ра́зница', 'różnica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('приме́р', 'przykład', None, 'rodzaj męski'), ('це́лое', 'całość', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('интерне́т', 'internet', None, 'rodzaj męski'), ('электро́нная по́чта', 'e-mail', None, 'rodzaj żeński'), ('пароль', 'hasło', None, 'rodzaj męski'), ('сайт', 'strona internetowa', None, 'rodzaj męski'), ('програ́мма', 'program', None, 'rodzaj żeński'), ('приложе́ние', 'aplikacja', None, 'rodzaj nijaki'), ('экра́н', 'ekran', None, 'rodzaj męski'), ('клавиату́ра', 'klawiatura', None, 'rodzaj żeński'), ('мышь (komputerowa)', 'myszka komputerowa', None, 'rodzaj żeński'), ('файл', 'plik', None, 'rodzaj męski'), ('фо́то', 'zdjęcie', None, 'rodzaj nijaki'), ('ка́мера', 'kamera', None, 'rodzaj żeński'), ('батаре́йка', 'bateria', None, 'rodzaj żeński'), ('электри́чество', 'prąd', None, 'rodzaj nijaki'), ('ка́бель', 'kabel', None, 'rodzaj męski'), ('маши́на (urządzenie)', 'maszyna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('инструме́нт', 'narzędzie', None, 'rodzaj męski'), ('молото́к', 'młotek', None, 'rodzaj męski'), ('при́нтер', 'drukarka', None, 'rodzaj męski'), ('заря́дное устро́йство', 'ładowarka', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('се́вер', 'północ', None, 'rodzaj męski'), ('юг', 'południe (kierunek)', None, 'rodzaj męski'), ('восто́к', 'wschód', None, 'rodzaj męski'), ('за́пад', 'zachód', None, 'rodzaj męski'), ('По́льша', 'Polska', None, 'rodzaj żeński'), ('Евро́па', 'Europa', None, 'rodzaj żeński'), ('Герма́ния', 'Niemcy', None, 'rodzaj żeński'), ('Фра́нция', 'Francja', None, 'rodzaj żeński'), ('Ита́лия', 'Włochy', None, 'rodzaj żeński'), ('Испа́ния', 'Hiszpania', None, 'rodzaj żeński'), ('Росси́я', 'Rosja', None, 'rodzaj żeński'), ('А́нглия', 'Anglia', None, 'rodzaj żeński'), ('Аме́рика', 'Ameryka', None, 'rodzaj żeński'), ('Кита́й', 'Chiny', None, 'rodzaj męski'), ('Япо́ния', 'Japonia', None, 'rodzaj żeński'), ('А́фрика', 'Afryka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('А́зия', 'Azja', None, 'rodzaj żeński'), ('контине́нт', 'kontynent', None, 'rodzaj męski'), ('столи́ца', 'stolica', None, 'rodzaj żeński'), ('гражданин', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('кусо́к', 'kawałek', None, 'rodzaj męski'), ('ка́пля', 'kropla', None, 'rodzaj żeński'), ('коро́бка', 'pudełko', None, 'rodzaj żeński'), ('мешо́к', 'worek', None, 'rodzaj męski'), ('ни́тка', 'nić', None, 'rodzaj żeński'), ('про́вод', 'drut', None, 'rodzaj męski'), ('игла́', 'igła', None, 'rodzaj żeński'), ('ножницы', 'nożyczki', None, None), ('па́лка', 'kij', None, 'rodzaj żeński'), ('верёвка', 'lina', None, 'rodzaj żeński'), ('цепь', 'łańcuch', None, 'rodzaj żeński'), ('винт', 'śruba', None, 'rodzaj męski'), ('гвоздь', 'gwóźdź', None, 'rodzaj męski'), ('клей', 'klej', None, 'rodzaj męski'), ('кра́ска', 'farba', None, 'rodzaj żeński'), ('стекло́', 'szkło', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('де́рево (materiał)', 'drewno', None, 'rodzaj nijaki'), ('мета́лл', 'metal', None, 'rodzaj męski'), ('зо́лото', 'złoto', None, 'rodzaj nijaki'), ('серебро́', 'srebro', None, 'rodzaj nijaki'), ('желе́зо', 'żelazo', None, 'rodzaj nijaki'), ('пла́стик', 'plastik', None, 'rodzaj męski'), ('ко́жа (materiał)', 'skóra (materiał)', None, 'rodzaj żeński'), ('хло́пок', 'bawełna', None, 'rodzaj męski'), ('шерсть', 'wełna', None, 'rodzaj żeński'), ('песо́к', 'piasek', None, 'rodzaj męski'), ('грязь', 'błoto', None, 'rodzaj żeński'), ('пыль', 'kurz', None, 'rodzaj żeński'), ('дым', 'dym', None, 'rodzaj męski'), ('пар', 'para (wodna)', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('вверх', 'góra (kierunek)', None, None), ('вниз', 'dół', None, None), ('впереди́', 'przód', None, None), ('сза́ди', 'tył', None, None), ('середи́на', 'środek', None, 'rodzaj żeński'), ('бок', 'bok', None, 'rodzaj męski'), ('внутри́', 'wewnątrz', None, None), ('снару́жи', 'na zewnątrz', None, None), ('далеко́', 'daleko', None, None), ('бли́зко', 'blisko', None, None), ('высоко́', 'wysoko', None, None), ('ни́зко', 'nisko', None, None), ('бы́стро', 'szybko', None, None), ('ме́дленно', 'wolno', None, None), ('пло́хо', 'źle', None, None), ('легко́', 'łatwo', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('трудно́', 'trudno', None, None), ('отде́льно', 'osobno', None, None), ('напро́тив', 'naprzeciw', None, None), ('вдоль', 'wzdłuż', None, None), ('поперёк', 'w poprzek', None, None), ('вокру́г', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('капу́ста', 'kapusta', None, 'rodzaj żeński'), ('горо́шек', 'groszek', None, 'rodzaj męski'), ('фасо́ль', 'fasola', None, 'rodzaj żeński'), ('гриб', 'grzyb', None, 'rodzaj męski'), ('оре́х', 'orzech', None, 'rodzaj męski'), ('сли́ва', 'śliwka', None, 'rodzaj żeński'), ('вишня', 'wiśnia', None, 'rodzaj żeński'), ('пе́рсик', 'brzoskwinia', None, 'rodzaj męski'), ('арбу́з', 'arbuz', None, 'rodzaj męski'), ('мали́на', 'malina', None, 'rodzaj żeński'), ('колбаса́', 'kiełbasa', None, 'rodzaj żeński'), ('ветчина́', 'szynka', None, 'rodzaj żeński'), ('бу́лочка', 'bułka', None, 'rodzaj żeński'), ('бутербро́д', 'kanapka', None, 'rodzaj męski'), ('блин', 'naleśnik', None, 'rodzaj męski'), ('йо́гурт', 'jogurt', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('смета́на', 'śmietana', None, 'rodzaj żeński'), ('соус', 'sos', None, 'rodzaj męski'), ('у́ксус', 'ocet', None, 'rodzaj męski'), ('дрожжи́', 'drożdże', None, None), ('кисе́ль', 'kisiel', None, 'rodzaj męski'), ('желе́', 'galaretka', None, 'rodzaj nijaki'), ('изю́м', 'rodzynek', None, 'rodzaj męski'), ('минда́ль', 'migdał', None, 'rodzaj męski'), ('петру́шка', 'pietruszka', None, 'rodzaj żeński'), ('укро́п', 'koperek', None, 'rodzaj męski'), ('пе́рец (warzywo)', 'papryka', None, 'rodzaj męski'), ('листово́й сала́т', 'sałata', None, 'rodzaj męski'), ('шпина́т', 'szpinak', None, 'rodzaj męski'), ('свёкла', 'burak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('тесть', 'teść', None, 'rodzaj męski'), ('тёща', 'teściowa', None, 'rodzaj żeński'), ('зять', 'szwagier', None, 'rodzaj męski'), ('племя́нник', 'bratanek', None, 'rodzaj męski'), ('племя́нница', 'siostrzenica', None, 'rodzaj żeński'), ('сирота́', 'sierota', None, 'rodzaj żeński'), ('вдова́', 'wdowa', None, 'rodzaj żeński'), ('жени́х', 'narzeczony', None, 'rodzaj męski'), ('сва́дьба', 'ślub', None, 'rodzaj żeński'), ('разво́д', 'rozwód', None, 'rodzaj męski'), ('рожде́ние', 'urodzenie', None, 'rodzaj nijaki'), ('по́хороны', 'pogrzeb', None, None), ('парикма́хер', 'fryzjer', None, 'rodzaj męski'), ('пека́рь', 'piekarz', None, 'rodzaj męski'), ('мясни́к', 'rzeźnik', None, 'rodzaj męski'), ('официа́нтка', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('почтальо́н', 'listonosz', None, 'rodzaj męski'), ('пожа́рный', 'strażak', None, 'rodzaj męski'), ('судья́', 'sędzia', None, 'rodzaj męski'), ('дире́ктор', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
