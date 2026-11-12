"""Treść kursu: słowacki dla Polaków."""

PUNCT = {'!', ',', '.', ':', '?'}

TRACKS = {'wymowa': 'VÝSLOVNOSŤ · WYMOWA', 'jezyk': 'JAZYK · JĘZYK'}

UNITS = [
    {'id': 'wymowa', 'title': 'Wymowa', 'icon': 'Ľ', 'track': 'wymowa',
     'letters': [
         ('ä', '[ɛ]: szerokie e; występuje po b, p, m, v', 'mäso (mięso)'),
         ('ô', '[u̯o]: dwugłoska uo', 'stôl (stół)'),
         ('ľ', '[ʎ]: miękkie l', 'ľad (lód)'),
         ('ĺ, ŕ', 'długie l i r, tworzą sylabę', 'vŕba (wierzba)'),
         ('á, é, í, ó, ú, ý', 'kreska oznacza długą samogłoskę, nie akcent', 'káva (kawa)'),
         ('č', '[tʃ]: jak polskie cz', 'čaj (herbata)'),
         ('š', '[ʃ]: jak polskie sz', 'škola (szkoła)'),
         ('ž', '[ʒ]: jak polskie ż', 'žena (kobieta)'),
         ('dz, dž', '[dz], [dʒ]: jak polskie dz i dż', 'džem (dżem)'),
         ('ch', '[x]: jak polskie ch; osobna litera po h', 'chlieb (chleb)'),
         ('h', '[ɦ]: dźwięczne h, tam gdzie po polsku g', 'hora (góra)'),
         ('ď, ť, ň', '[ɟ], [c], [ɲ]: miękkie d, t, n; przed e, i miękną bez znaczka', 'deň (dzień)'),
         ('ia, ie, iu', 'dwugłoski: jedna sylaba', 'mlieko (mleko)'),
         ('akcent', 'zawsze na pierwszej sylabie słowa', 'Slovensko (Słowacja)'),
     ],
    },
    {'id': 'slowa', 'title': 'Pierwsze słowa', 'icon': 'A', 'track': 'jezyk', 'requires': 'wymowa',
     'words': [
         ('ahoj', 'cześć', None, None),
         ('dobrý', 'dobry', None, None),
         ('deň', 'dzień', None, None),
         ('dobrú', 'dobrą (biernik)', None, None),
         ('noc', 'noc', None, None),
         ('ďakujem', 'dziękuję', None, None),
         ('prosím', 'proszę', None, None),
         ('áno', 'tak', None, None),
         ('nie', 'nie', None, None),
         ('prepáčte', 'przepraszam', None, None),
         ('dovidenia', 'do widzenia', None, None),
         ('dobre', 'dobrze', None, None),
         ('veľmi', 'bardzo', None, None),
     ],
     'sentences': [
         (['ahoj', '!'], 'Cześć!', {'prepáčte': 'prepáčte to „przepraszam”.'}),
         (['dobrý', 'deň', '!'], 'Dzień dobry!', {'noc': 'noc to „noc”.'}),
         (['dobrú', 'noc', '!'], 'Dobranoc!', {'deň': 'deň to „dzień”.'}),
         (['ďakujem', '!'], 'Dziękuję!', {'prosím': 'prosím to „proszę”. Tu dziękujesz.'}),
         (['áno', ',', 'ďakujem'], 'Tak, dziękuję.', {'nie': 'nie to „nie”.'}),
         (['nie', ',', 'ďakujem'], 'Nie, dziękuję.', {'áno': 'áno to „tak”.'}),
         (['prepáčte', '!'], 'Przepraszam!', {}),
         (['dovidenia', '!'], 'Do widzenia!', {}),
         (['veľmi', 'ďakujem'], 'Bardzo dziękuję.', {}),
     ],
    },
    {'id': 'ja', 'title': 'Ja, ty, on', 'icon': 'J', 'track': 'jezyk',
     'words': [
         ('ja', 'ja', None, None),
         ('ty', 'ty', None, None),
         ('on', 'on', None, None),
         ('ona', 'ona', None, None),
         ('som', 'jestem', None, None),
         ('si', 'jesteś', None, None),
         ('je', 'jest', None, None),
         ('študent', 'student', 'student', None),
         ('učiteľ', 'nauczyciel', None, None),
         ('Poliak', 'Polak', None, None),
         ('Poľka', 'Polka', None, None),
         ('z', 'z', None, None),
         ('zo', 'z (przed s, z, š, ž)', None, None),
         ('Poľska', 'Polski', None, 'Po „z”: dopełniacz.'),
         ('Slovenska', 'Słowacji', None, 'Po „zo”: dopełniacz.'),
     ],
     'sentences': [
         (['ja', 'som', 'študent'], 'Jestem studentem.', {'si': 'si to „jesteś”. O sobie: som.'}),
         (['ty', 'si', 'učiteľ'], 'Jesteś nauczycielem.', {'som': 'som to „jestem”. Do „ty”: si.'}),
         (['on', 'je', 'Poliak'], 'On jest Polakiem.', {'Poľka': 'Dla mężczyzny: Poliak.'}),
         (['ona', 'je', 'Poľka'], 'Ona jest Polką.', {'Poliak': 'Dla kobiety: Poľka.'}),
         (['ja', 'som', 'z', 'Poľska'], 'Jestem z Polski.', {'Slovenska': 'Slovenska to „Słowacji”.'}),
         (['ona', 'je', 'zo', 'Slovenska'], 'Ona jest ze Słowacji.', {'z': 'Przed s- mówi się zo.'}),
     ],
    },
    {'id': 'ludzie', 'title': 'Ludzie i rodzina', 'icon': 'R', 'track': 'jezyk',
     'words': [
         ('matka', 'matka', None, None),
         ('otec', 'ojciec', None, None),
         ('brat', 'brat', None, None),
         ('brata', 'brata', None, 'Biernik: -a.'),
         ('sestra', 'siostra', None, None),
         ('sestru', 'siostrę', None, 'Biernik: -a → -u.'),
         ('dieťa', 'dziecko', None, None),
         ('priateľ', 'przyjaciel', None, None),
         ('žena', 'kobieta; żona', None, None),
         ('muž', 'mężczyzna; mąż', None, None),
         ('môj', 'mój (męski)', None, None),
         ('moja', 'moja (żeński)', None, None),
         ('mám', 'mam', None, None),
         ('máš', 'masz', None, None),
         ('malý', 'mały (męski)', None, None),
         ('malá', 'mała (żeński)', None, None),
         ('dobrá', 'dobra (żeński)', None, None),
     ],
     'sentences': [
         (['môj', 'brat', 'je', 'malý'], 'Mój brat jest mały.', {'moja': 'brat jest męski: môj.'}),
         (['moja', 'sestra', 'je', 'malá'], 'Moja siostra jest mała.', {'môj': 'sestra jest żeńska: moja.'}),
         (['matka', 'je', 'dobrá'], 'Matka jest dobra.', {}),
         (['mám', 'brata'], 'Mam brata.', {'máš': 'máš to „masz”. O sobie: mám.'}),
         (['máš', 'sestru'], 'Masz siostrę.', {'mám': 'mám to „mam”. Do „ty”: máš.'}),
         (['otec', 'je', 'muž'], 'Ojciec jest mężczyzną.', {}),
         (['môj', 'priateľ', 'je', 'dobrý'], 'Mój przyjaciel jest dobry.', {}),
     ],
    },
    {'id': 'jedzenie', 'title': 'Jedzenie i picie', 'icon': 'K', 'track': 'jezyk',
     'words': [
         ('voda', 'woda', None, None),
         ('vodu', 'wodę', None, 'Biernik: -a → -u.'),
         ('káva', 'kawa', None, None),
         ('kávu', 'kawę', None, None),
         ('čaj', 'herbata', None, None),
         ('chlieb', 'chleb', None, None),
         ('syr', 'ser', None, None),
         ('mlieko', 'mleko', None, None),
         ('ryba', 'ryba', None, None),
         ('rybu', 'rybę', None, None),
         ('jablko', 'jabłko', None, None),
         ('chcem', 'chcę', None, None),
         ('chceš', 'chcesz', None, None),
         ('chutná', 'smaczna', None, None),
         ('teraz', 'teraz', None, None),
     ],
     'sentences': [
         (['ja', 'chcem', 'kávu'], 'Chcę kawę.', {'chceš': 'chceš to „chcesz”. O sobie: chcem.'}),
         (['ty', 'chceš', 'čaj'], 'Chcesz herbatę.', {'chcem': 'chcem to „chcę”. Do „ty”: chceš.'}),
         (['ja', 'chcem', 'chlieb'], 'Chcę chleb.', {}),
         (['ty', 'chceš', 'jablko'], 'Chcesz jabłko.', {}),
         (['ryba', 'je', 'veľmi', 'chutná'], 'Ryba jest bardzo smaczna.', {}),
         (['teraz', 'chcem', 'vodu'], 'Teraz chcę wodę.', {'voda': 'Po „chcem” biernik: vodu.'}),
     ],
    },
    {'id': 'liczby', 'title': 'Liczby i czas', 'icon': '1', 'track': 'jezyk',
     'words': [
         ('dva', 'dwa', None, None),
         ('dvoch', 'dwóch (męskoosobowy)', None, None),
         ('tri', 'trzy', None, None),
         ('štyri', 'cztery', None, None),
         ('päť', 'pięć', None, None),
         ('desať', 'dziesięć', None, None),
         ('bratov', 'braci (biernik lm.)', None, None),
         ('jablká', 'jabłka', None, None),
         ('dnes', 'dziś', None, None),
         ('zajtra', 'jutro', None, None),
         ('včera', 'wczoraj', None, None),
         ('hodín', 'godzin', None, None),
         ('koľko', 'ile', None, None),
     ],
     'sentences': [
         (['mám', 'dvoch', 'bratov'], 'Mam dwóch braci.', {'dva': 'O mężczyznach w bierniku: dvoch.'}),
         (['ja', 'chcem', 'tri', 'jablká'], 'Chcę trzy jabłka.', {'dva': 'dva to „dwa”. Chcesz trzy: tri.'}),
         (['koľko', 'je', 'hodín', '?'], 'Która jest godzina?', {}),
         (['teraz', 'je', 'desať', 'hodín'], 'Jest dziesiąta.', {'päť': 'päť to „pięć”.'}),
         (['dnes', 'chcem', 'kávu'], 'Dziś chcę kawę.', {'zajtra': 'zajtra to „jutro”. Tu „dziś”: dnes.'}),
         (['zajtra', 'chcem', 'rybu'], 'Jutro chcę rybę.', {'včera': 'včera to „wczoraj”.'}),
     ],
    },
    {'id': 'miejsca', 'title': 'Miejsca i podróż', 'icon': 'M', 'track': 'jezyk',
     'words': [
         ('dom', 'dom', None, None),
         ('domov', 'do domu', None, None),
         ('mesto', 'miasto', None, None),
         ('ulica', 'ulica', None, None),
         ('škola', 'szkoła', None, None),
         ('more', 'morze', None, None),
         ('taxi', 'taksówka', 'taksówka', None),
         ('hotel', 'hotel', 'hotel', None),
         ('kde', 'gdzie', None, None),
         ('tu', 'tu', None, None),
         ('tam', 'tam', None, None),
         ('idem', 'idę; jadę', None, None),
         ('do', 'do', None, None),
         ('Bratislavy', 'Bratysławy (do Bratysławy)', None, 'Po „do”: dopełniacz.'),
         ('vpravo', 'w prawo; po prawej', None, None),
         ('vľavo', 'w lewo; po lewej', None, None),
     ],
     'sentences': [
         (['kde', 'je', 'hotel', '?'], 'Gdzie jest hotel?', {'tu': 'tu to „tu”. Pytasz „gdzie”: kde.'}),
         (['hotel', 'je', 'tam'], 'Hotel jest tam.', {'tu': 'tu to „tu”. Tu „tam”: tam.'}),
         (['idem', 'domov'], 'Idę do domu.', {}),
         (['idem', 'do', 'Bratislavy'], 'Jadę do Bratysławy.', {}),
         (['taxi', 'je', 'vpravo'], 'Taksówka jest po prawej.', {'vľavo': 'vľavo to „po lewej”.'}),
         (['škola', 'je', 'tam'], 'Szkoła jest tam.', {}),
     ],
    },
]

INSIGHTS = {
    'wymowa': [
        {'title': 'Kreska to długość, nie akcent', 'chain': [], 'text': 'Akcent pada zawsze na pierwszą sylabę. Kreska nad samogłoską oznacza długość. Słowacki pilnuje rytmu: dwie długie sylaby zwykle nie stoją obok siebie (dlatego krásny, a nie krásný). Przed e, i litery d, t, n, l czyta się miękko bez znaczka: deti [ďeťi].'},
    ],
    'slowa': [
        {'title': 'Fałszywi przyjaciele', 'chain': [], 'text': 'Słowacki jest bardzo bliski polskiemu, ale uwaga na pułapki: čerstvý to „świeży”, obchod to „sklep”, pivnica to „piwnica”, pozor to „uwaga”, chudý to „szczupły”, a hľadať znaczy „szukać”.'},
    ],
    'ja': [
        {'title': 'Som, si, je', 'chain': [('Jestem studentem.', ['ja', 'som', 'študent'], 'Do „ja” pasuje som.'), ('Jesteś nauczycielem.', ['ty', 'si', 'učiteľ'], 'Do „ty” pasuje si.')], 'text': 'Zaimek ja, ty zwykle się pomija: „Som študent”. Po czasowniku „być” stoi mianownik: som študent, nie „študentom”. Przed s, z, š, ž przyimek z brzmi zo: zo Slovenska.'},
    ],
    'ludzie': [
        {'title': 'Biernik prawie jak po polsku', 'chain': [], 'text': 'Rzeczowniki żeńskie na -a mają w bierniku -u: sestra → sestru. Męskie żywotne dostają -a: brat → brata. Słowacki nie ma wołacza: woła się mianownikiem.'},
    ],
    'jedzenie': [
        {'title': 'Chcem i chceš', 'chain': [], 'text': 'W 1. osobie prawie wszystkie czasowniki kończą się na -m: chcem, mám, robím, som. Grzeczniej w kawiarni: „Prosím si kávu”.'},
    ],
}

ENDINGS_INSIGHT = {'title': 'Rodzaj i forma czasownika', 'text': 'Po słowacku ćwiczysz rodzaj (môj/moja) i formy czasownika (som, si, je; chcem, chceš). Tu to robisz.'}

ENDINGS = [
    ('ja ', '', 'som', ' študent', ['som', 'si', 'je'], 'ja jestem', 'Do „ja” pasuje som.', 'ja'),
    ('ty ', '', 'si', ' učiteľ', ['som', 'si', 'je'], 'ty jesteś', 'Do „ty” pasuje si.', 'ja'),
    ('on ', '', 'je', ' Poliak', ['som', 'si', 'je'], 'on jest', 'Do „on” pasuje je.', 'ja'),
    ('', '', 'môj', ' brat', ['môj', 'moja'], 'mój (męski)', 'brat jest męski: môj.', 'ludzie'),
    ('', '', 'moja', ' sestra', ['môj', 'moja'], 'moja (żeński)', 'sestra jest żeńska: moja.', 'ludzie'),
    ('', '', 'mám', ' brata', ['mám', 'máš'], 'ja mam', 'Do „ja” pasuje mám.', 'ludzie'),
    ('', '', 'máš', ' sestru', ['mám', 'máš'], 'ty masz', 'Do „ty” pasuje máš.', 'ludzie'),
    ('ja ', '', 'chcem', ' kávu', ['chcem', 'chceš'], 'ja chcę', 'Do „ja” pasuje chcem.', 'jedzenie'),
    ('ty ', '', 'chceš', ' čaj', ['chcem', 'chceš'], 'ty chcesz', 'Do „ty” pasuje chceš.', 'jedzenie'),
    ('som ', '', 'z', ' Poľska', ['z', 'do'], 'z', 'z to „z”, do to „do”.', 'miejsca'),
    ('idem ', '', 'do', ' Bratislavy', ['z', 'do'], 'do', 'do to „do”.', 'miejsca'),
]

CHAT_EXTRA = {'a': 'i', 'Jana': 'Jana (imię)', 'Peter': 'Peter (imię)', 'taxikár': 'taksówkarz', 'kam': 'dokąd', 'ideš': 'idziesz; jedziesz'}

CHATS = [
    {'id': 'kaviaren', 'title': 'W kawiarni', 'partner': 'Jana', 'avatar': 'J', 'requires': 'jedzenie',
     'turns': [
         {'bot': ['dobrý', 'deň', '!'], 'en': 'Dzień dobry!', 'options': [(['dobrý', 'deň', '!'], True, None), (['dobrú', 'noc', '!'], False, 'dobrú noc to „dobranoc”. Jest dzień.')]},
         {'bot': ['kávu', '?'], 'en': 'Kawę?', 'options': [(['áno', ',', 'ja', 'chcem', 'kávu'], True, None), (['áno', ',', 'ty', 'chceš', 'kávu'], False, 'chceš jest do „ty”. O sobie: chcem.')]},
         {'bot': ['a', 'chlieb', '?'], 'en': 'I chleb?', 'options': [(['nie', ',', 'ďakujem'], True, None), (['prosím', '!'], False, 'prosím to „proszę”. Odmów: nie, ďakujem.')]},
         {'bot': ['dobre', '!'], 'build': (['ďakujem', '!'], 'Dziękuję!'), 'en': 'Dobrze!'},
     ]},
    {'id': 'zoznamenie', 'title': 'Poznajemy się', 'partner': 'Peter', 'avatar': 'P', 'requires': 'ludzie',
     'turns': [
         {'bot': ['ahoj', '!'], 'en': 'Cześć!', 'options': [(['ahoj', '!'], True, None), (['prepáčte', '!'], False, 'prepáčte to „przepraszam”. Powitaj: ahoj.')]},
         {'bot': ['ty', 'si', 'zo', 'Slovenska', '?'], 'en': 'Jesteś ze Słowacji?', 'options': [(['nie', ',', 'ja', 'som', 'z', 'Poľska'], True, None), (['nie', ',', 'ja', 'si', 'z', 'Poľska'], False, 'si jest do „ty”. O sobie: som.')]},
         {'bot': ['máš', 'brata', '?'], 'en': 'Masz brata?', 'options': [(['áno', ',', 'mám', 'brata'], True, None), (['áno', ',', 'máš', 'brata'], False, 'máš to „masz”. O sobie: mám.')]},
         {'bot': ['dovidenia', '!'], 'build': (['dovidenia', '!'], 'Do widzenia!'), 'en': 'Do widzenia!'},
     ]},
    {'id': 'taxi', 'title': 'W taksówce', 'partner': 'taxikár', 'avatar': 'T', 'requires': 'miejsca',
     'turns': [
         {'bot': ['dobrý', 'deň', '!'], 'en': 'Dzień dobry!', 'options': [(['dobrý', 'deň', '!'], True, None), (['dobrú', 'noc', '!'], False, 'dobrú noc to „dobranoc”. Jest dzień.')]},
         {'bot': ['kam', 'ideš', '?'], 'en': 'Dokąd jedziesz?', 'options': [(['idem', 'do', 'Bratislavy'], True, None), (['ideš', 'do', 'Bratislavy'], False, 'ideš to „idziesz”. O sobie: idem.')]},
         {'bot': ['hotel', 'je', 'tam', '.'], 'en': 'Hotel jest tam.', 'options': [(['vpravo', '?'], True, None), (['tu', '?'], False, 'Pytasz o kierunek: vpravo.')]},
         {'bot': ['áno', '!'], 'build': (['ďakujem', '!'], 'Dziękuję!'), 'en': 'Tak!'},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['ja', 'ty', 'on/ona', 'my', 'vy', 'oni'],
    'przyp': ['nominatív', 'genitív', 'datív', 'akuzatív', 'lokál (o…)', 'inštrumentál'],
    'lpart': ['męski lp.', 'żeński lp.', 'nijaki lp.', 'liczba mnoga'],
    'trp': ['robiť', 'volať', 'niesť', 'písať', 'otvoriť'],
    'liczrz': ['1', '2', '3', '4', '5', '10', '21', '100'],
    't_ff': ['čerstvý', 'obchod', 'pivnica', 'pozor', 'hľadať', 'chudý', 'sprostý', 'frajer'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'volať (wołać): -ám', 'os', 'volám; voláš; volá; voláme; voláte; volajú', None),
    ('conj', 'Wzory koniugacji', 'robiť (robić): -ím', 'os', 'robím; robíš; robí; robíme; robíte; robia', None),
    ('conj', 'Wzory koniugacji', 'pracovať (pracować): -ujem', 'os', 'pracujem; pracuješ; pracuje; pracujeme; pracujete; pracujú', None),
    ('conj', 'Wzory koniugacji', 'niesť (nieść): -iem', 'os', 'nesiem; nesieš; nesie; nesieme; nesiete; nesú', None),
    ('conj', 'Wyjątki', 'rozumieť (rozumieć)', 'os', 'rozumiem; rozumieš; rozumie; rozumieme; rozumiete; rozumejú', '3. osoba lm. na -ejú.'),
    ('conj', 'Czasowniki nieregularne', 'byť (być)', 'os', 'som; si; je; sme; ste; sú', None),
    ('conj', 'Czasowniki nieregularne', 'mať (mieć)', 'os', 'mám; máš; má; máme; máte; majú', None),
    ('conj', 'Czasowniki nieregularne', 'chcieť (chcieć)', 'os', 'chcem; chceš; chce; chceme; chcete; chcú', None),
    ('conj', 'Czasowniki nieregularne', 'ísť (iść)', 'os', 'idem; ideš; ide; ideme; idete; idú', None),
    ('conj', 'Czasowniki nieregularne', 'jesť (jeść)', 'os', 'jem; ješ; je; jeme; jete; jedia', None),
    ('conj', 'Czasowniki nieregularne', 'vedieť (wiedzieć)', 'os', 'viem; vieš; vie; vieme; viete; vedia', None),
    ('conj', 'Czasowniki nieregularne', 'môcť (móc)', 'os', 'môžem; môžeš; môže; môžeme; môžete; môžu', None),
    ('conj', 'Czas przeszły', 'robiť: czas przeszły', 'os', 'robil som; robil si; robil; robili sme; robili ste; robili', 'Imiesłów na -l + byť; w 3. osobie bez byť.'),
    ('conj', 'Czas przyszły', 'byť: czas przyszły', 'os', 'budem; budeš; bude; budeme; budete; budú', 'Czas przyszły niedokonany: budem + bezokolicznik.'),
    ('form', 'Imiesłowy', 'robiť: imiesłów na -l', 'lpart', 'robil; robila; robilo; robili', 'W liczbie mnogiej jedna forma dla wszystkich rodzajów.'),
    ('form', 'Imiesłowy', 'byť: imiesłów na -l', 'lpart', 'bol; bola; bolo; boli', None),
    ('form', 'Imiesłowy', 'ísť (wyjątek): imiesłów na -l', 'lpart', 'išiel; išla; išlo; išli', None),
    ('form', 'Imiesłowy', 'Imiesłów bierny', 'trp', 'robený; volaný; nesený; písaný; otvorený', None),
    ('decl', 'Wzory deklinacji', 'chlap (chłop, facet): męski żywotny', 'przyp', 'chlap; chlapa; chlapovi; chlapa; chlapovi; chlapom', 'Słowacki nie ma wołacza.'),
    ('decl', 'Wzory deklinacji', 'dub (dąb): męski nieżywotny', 'przyp', 'dub; duba; dubu; dub; dube; dubom', None),
    ('decl', 'Wzory deklinacji', 'žena (kobieta): żeński twardy', 'przyp', 'žena; ženy; žene; ženu; žene; ženou', None),
    ('decl', 'Wzory deklinacji', 'ulica (ulica): żeński miękki', 'przyp', 'ulica; ulice; ulici; ulicu; ulici; ulicou', None),
    ('decl', 'Wzory deklinacji', 'mesto (miasto): nijaki twardy', 'przyp', 'mesto; mesta; mestu; mesto; meste; mestom', None),
    ('decl', 'Wzory deklinacji', 'srdce (serce): nijaki miękki', 'przyp', 'srdce; srdca; srdcu; srdce; srdci; srdcom', None),
    ('decl', 'Wyjątki', 'otec (ojciec)', 'przyp', 'otec; otca; otcovi; otca; otcovi; otcom', 'Ruchome e: otec → otca.'),
    ('decl', 'Wyjątki', 'dieťa (dziecko)', 'przyp', 'dieťa; dieťaťa; dieťaťu; dieťa; dieťati; dieťaťom', 'Temat rozszerzony o -ať-.'),
    ('decl', 'Wyjątki', 'kosť (kość)', 'przyp', 'kosť; kosti; kosti; kosť; kosti; kosťou', None),
    ('decl', 'Zaimki', 'ja (ja)', 'przyp', 'ja; mňa; mne; mňa; mne; mnou', None),
    ('decl', 'Zaimki', 'ty (ty)', 'przyp', 'ty; teba; tebe; teba; tebe; tebou', None),
    ('decl', 'Liczebniki', 'jeden (jeden): rodzaj męski', 'przyp', 'jeden; jedného; jednému; jeden; jednom; jedným', None),
    ('decl', 'Liczebniki', 'jedna (jedna): rodzaj żeński', 'przyp', 'jedna; jednej; jednej; jednu; jednej; jednou', None),
    ('decl', 'Liczebniki', 'dva (dwa): nieosobowy', 'przyp', 'dva; dvoch; dvom; dva; dvoch; dvoma', 'O mężczyznach: dvaja, w bierniku dvoch.'),
    ('decl', 'Liczebniki', 'traja (trzej): męskoosobowy', 'przyp', 'traja; troch; trom; troch; troch; tromi', None),
    ('decl', 'Liczebniki', 'tri (trzy)', 'przyp', 'tri; troch; trom; tri; troch; tromi', None),
    ('decl', 'Liczebniki', 'štyri (cztery)', 'przyp', 'štyri; štyroch; štyrom; štyri; štyroch; štyrmi', None),
    ('decl', 'Liczebniki', 'päť (pięć)', 'przyp', 'päť; piatich; piatim; päť; piatich; piatimi', 'ä → ia w przypadkach zależnych.'),
    ('form', 'Liczebniki', 'Liczebnik + rzeczownik: rok', 'liczrz', 'jeden rok; dva roky; tri roky; štyri roky; päť rokov; desať rokov; dvadsaťjeden rokov; sto rokov', 'Po 2–4: mianownik lm. Od 5: dopełniacz lm.'),
    ('form', 'Typowe trudności', 'Fałszywi przyjaciele: co to znaczy?', 't_ff', 'świeży; sklep; piwnica; uwaga; szukać; szczupły; głupi; chłopak', None),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['góra', 'głowa', 'noga', 'gwiazda', 'głos', 'gość', 'ogień', 'gęś'],
    't_m1': ['dobr…', 'krásn…', 'mal…', 'múdr…', 'star…', 'biel…', 'nov…', 'krátk…'],
    't_m2': ['___ Poľska (z)', '___ Slovenska (z)', '___ školy (z)', '___ Bratislavy (z)', '___ Varšave (w)', '___ vode (w)'],
    't_m3': ['deti', 'ten', 'teraz', 'nie', 'leto', 'telefón'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Polskie g, słowackie h', 't_m0', 'hora; hlava; noha; hviezda; hlas; hosť; oheň; hus', None),
    ('form', 'Typowe trudności', 'Reguła rytmiczna: -ý czy -y?', 't_m1', 'dobrý; krásny; malý; múdry; starý; biely; nový; krátky', 'Po długiej sylabie końcówka jest krótka.'),
    ('form', 'Typowe trudności', 'z czy zo, v czy vo?', 't_m2', 'z; zo; zo; z; vo; vo', 'Przed s, z, š, ž mówi się zo; przed v, f mówi się vo.'),
    ('form', 'Typowe trudności', 'Miękko czy twardo? (de, te, ne, le)', 't_m3', 'miękko; twardo (wyjątek); twardo (wyjątek); miękko; miękko; twardo (słowo obce)', 'Przed e, i litery d, t, n, l czyta się miękko. Wyjątkami są zaimki (ten, tento), teraz i słowa obce.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['Dziś uczę się po słowacku.', 'Dałem mu książkę.', 'Wczoraj go widziałem.', 'Chcę się z tobą spotkać.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: krótkie słowa na 2. miejscu', 't_s0', 'Dnes sa učím po slovensky.|Dnes učím sa po slovensky.|Sa dnes učím po slovensky.|Dnes učím po slovensky sa.; Dal som mu knihu.|Dal mu som knihu.|Som mu dal knihu.|Dal som knihu mu.; Včera som ho videl.|Včera ho som videl.|Včera videl som ho.|Som ho včera videl.; Chcem sa s tebou stretnúť.|Chcem stretnúť sa s tebou.|Sa chcem s tebou stretnúť.|Chcem s tebou sa stretnúť.', 'Krótkie słowa (sa, si, som, ho, mu) stoją na drugim miejscu zdania, a nie na samym początku.'),
]
