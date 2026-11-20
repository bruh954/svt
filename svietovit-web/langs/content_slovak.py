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
ENDINGS_PL = {'môj brat': 'mój brat', 'moja sestra': 'moja siostra', 'som z Poľska': 'Jestem z Polski.'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'dobrý (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'dobrý; lepší; najlepší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'veľký (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'veľký; väčší; najväčší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'malý (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'malý; menší; najmenší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'zlý (zły)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'zlý; horší; najhorší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'vysoký (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'vysoký; vyšší; najvyšší', None),
    ('form', 'Stopniowanie', 'krásny (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'krásny; krajší; najkrajší', 'Nieregularne: krajší.'),
    ('form', 'Stopniowanie', 'starý (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'starý; starší; najstarší', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 2 (generowane) ===
PARADIGMS += [
    ('form', 'Czas przeszły', 'byť: minulý čas', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'bol som; bola som; bol; bola; boli sme; boli', None),
    ('form', 'Czas przeszły', 'robiť: minulý čas', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'robil som; robila som; robil; robila; robili sme; robili', None),
    ('form', 'Czas przeszły', 'mať: minulý čas', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'mal som; mala som; mal; mala; mali sme; mali', None),
    ('conj', 'Czas przyszły', 'robiť: budúci čas', ['ja', 'ty', 'on / ona', 'my', 'vy', 'oni'], 'budem robiť; budeš robiť; bude robiť; budeme robiť; budete robiť; budú robiť', None),
    ('form', 'Tryb warunkowy', 'byť: kondicionál', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'bol by som; bola by som; bol by; bola by; boli by sme; boli by', 'Grzeczna prośba: Chcel by som kávu.'),
    ('conj', 'Czasowniki nieregularne', 'musieť (musieć)', ['ja', 'ty', 'on / ona', 'my', 'vy', 'oni'], 'musím; musíš; musí; musíme; musíte; musia', None),
    ('form', 'Vid (aspekt)', 'vid: robić', ['nedokonavý', 'dokonavý'], 'robiť; urobiť', None),
    ('form', 'Vid (aspekt)', 'vid: pisać', ['nedokonavý', 'dokonavý'], 'písať; napísať', None),
    ('form', 'Vid (aspekt)', 'vid: czytać', ['nedokonavý', 'dokonavý'], 'čítať; prečítať', None),
    ('form', 'Vid (aspekt)', 'vid: kupować', ['nedokonavý', 'dokonavý'], 'kupovať; kúpiť', None),
    ('form', 'Vid (aspekt)', 'vid: dawać', ['nedokonavý', 'dokonavý'], 'dávať; dať', None),
    ('form', 'Vid (aspekt)', 'vid: widzieć', ['nedokonavý', 'dokonavý'], 'vidieť; uvidieť', None),
    ('form', 'Vid (aspekt)', 'vid: otwierać', ['nedokonavý', 'dokonavý'], 'otvárať; otvoriť', None),
    ('form', 'Vid (aspekt)', 'vid: jeść', ['nedokonavý', 'dokonavý'], 'jesť; zjesť', None),
    ('form', 'Vid (aspekt)', 'vid: pić', ['nedokonavý', 'dokonavý'], 'piť; vypiť', None),
    ('form', 'Vid (aspekt)', 'vid: mówić, powiedzieć', ['nedokonavý', 'dokonavý'], 'hovoriť; povedať', None),
    ('form', 'Vid (aspekt)', 'vid: brać', ['nedokonavý', 'dokonavý'], 'brať; vziať', None),
    ('form', 'Vid (aspekt)', 'vid: zaczynać', ['nedokonavý', 'dokonavý'], 'začínať; začať', None),
    ('form', 'Typowe trudności', 'Przyimek: jaki przypadek?', ['Idem do ___ (škola)', 'Som v ___ (škola)', 'Idem k ___ (kamarát)', 'Idem s ___ (kamarát)', 'Hovorím o ___ (kamarát)', 'Vidím ___ (kamarát)'], 'školy; škole; kamarátovi; kamarátom; kamarátovi; kamaráta', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 2 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('chlapec', 'chłopiec', None, 'rodzaj męski'), ('dievčatko', 'dziewczynka', None, 'rodzaj nijaki'), ('človek', 'człowiek', None, 'rodzaj męski'), ('ľudia', 'ludzie', None, None), ('rodina', 'rodzina', None, 'rodzaj żeński'), ('syn', 'syn', None, 'rodzaj męski'), ('dcéra', 'córka', None, 'rodzaj żeński'), ('dedo', 'dziadek', None, 'rodzaj męski'), ('babka', 'babcia', None, 'rodzaj żeński'), ('vnuk', 'wnuk', None, 'rodzaj męski'), ('strýko', 'wujek', None, 'rodzaj męski'), ('teta', 'ciocia', None, 'rodzaj żeński'), ('bratranec', 'kuzyn', None, 'rodzaj męski'), ('manžel', 'mąż', None, 'rodzaj męski'), ('manželka', 'żona', None, 'rodzaj żeński'), ('sused', 'sąsiad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('hosť', 'gość', None, 'rodzaj męski'), ('šéf', 'szef', None, 'rodzaj męski'), ('kolega', 'kolega', None, 'rodzaj męski'), ('nepriateľ', 'wróg', None, 'rodzaj męski'), ('kráľ', 'król', None, 'rodzaj męski'), ('kráľovná', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('hlava', 'głowa', None, 'rodzaj żeński'), ('tvár', 'twarz', None, 'rodzaj żeński'), ('oko', 'oko', None, 'rodzaj nijaki'), ('ucho', 'ucho', None, 'rodzaj nijaki'), ('nos', 'nos', None, 'rodzaj męski'), ('ústa', 'usta', None, None), ('zub', 'ząb', None, 'rodzaj męski'), ('jazyk', 'język (narząd)', None, 'rodzaj męski'), ('vlasy', 'włosy', None, None), ('krk', 'szyja', None, 'rodzaj męski'), ('rameno', 'ramię', None, 'rodzaj nijaki'), ('ruka', 'ręka', None, 'rodzaj żeński'), ('prst', 'palec', None, 'rodzaj męski'), ('noha', 'noga', None, 'rodzaj żeński'), ('chodidlo', 'stopa', None, 'rodzaj nijaki'), ('koleno', 'kolano', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('chrbát', 'plecy', None, 'rodzaj męski'), ('brucho', 'brzuch', None, 'rodzaj nijaki'), ('srdce', 'serce', None, 'rodzaj nijaki'), ('krv', 'krew', None, 'rodzaj żeński'), ('kosť', 'kość', None, 'rodzaj żeński'), ('koža', 'skóra', None, 'rodzaj żeński'), ('hlas', 'głos', None, 'rodzaj męski'), ('telo', 'ciało', None, 'rodzaj nijaki'), ('žalúdok', 'żołądek', None, 'rodzaj męski'), ('brada', 'broda', None, 'rodzaj żeński'), ('pera', 'warga', None, 'rodzaj żeński'), ('necht', 'paznokieć', None, 'rodzaj męski'), ('hruď', 'pierś', None, 'rodzaj żeński'), ('mozog', 'mózg', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('maslo', 'masło', None, 'rodzaj nijaki'), ('vajce', 'jajko', None, 'rodzaj nijaki'), ('mäso', 'mięso', None, 'rodzaj nijaki'), ('kura', 'kurczak', None, 'rodzaj żeński'), ('bravčové', 'wieprzowina', None, 'rodzaj nijaki'), ('polievka', 'zupa', None, 'rodzaj żeński'), ('šalát', 'sałatka', None, 'rodzaj męski'), ('ryža', 'ryż', None, 'rodzaj żeński'), ('cestoviny', 'makaron', None, None), ('zemiak', 'ziemniak', None, 'rodzaj męski'), ('mrkva', 'marchewka', None, 'rodzaj żeński'), ('cibuľa', 'cebula', None, 'rodzaj żeński'), ('cesnak', 'czosnek', None, 'rodzaj męski'), ('paradajka', 'pomidor', None, 'rodzaj żeński'), ('uhorka', 'ogórek', None, 'rodzaj żeński'), ('hruška', 'gruszka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('banán', 'banan', None, 'rodzaj męski'), ('pomaranč', 'pomarańcza', None, 'rodzaj męski'), ('citrón', 'cytryna', None, 'rodzaj męski'), ('jahoda', 'truskawka', None, 'rodzaj żeński'), ('hrozno', 'winogrono', None, 'rodzaj nijaki'), ('cukor', 'cukier', None, 'rodzaj męski'), ('soľ', 'sól', None, 'rodzaj żeński'), ('korenie', 'pieprz', None, 'rodzaj nijaki'), ('olej', 'olej', None, 'rodzaj męski'), ('múka', 'mąka', None, 'rodzaj żeński'), ('med', 'miód', None, 'rodzaj męski'), ('čokoláda', 'czekolada', None, 'rodzaj żeński'), ('zmrzlina', 'lody', None, 'rodzaj żeński'), ('torta', 'ciasto (tort)', None, 'rodzaj żeński'), ('sušienka', 'ciastko', None, 'rodzaj żeński'), ('raňajky', 'śniadanie', None, None)], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('obed', 'obiad', None, 'rodzaj męski'), ('večera', 'kolacja', None, 'rodzaj żeński'), ('desiata', 'przekąska', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('šťava', 'sok', None, 'rodzaj żeński'), ('pivo', 'piwo', None, 'rodzaj nijaki'), ('víno', 'wino', None, 'rodzaj nijaki'), ('nápoj', 'napój', None, 'rodzaj męski'), ('pohár', 'szklanka', None, 'rodzaj męski'), ('šálka', 'filiżanka', None, 'rodzaj żeński'), ('tanier', 'talerz', None, 'rodzaj męski'), ('nôž', 'nóż', None, 'rodzaj męski'), ('vidlička', 'widelec', None, 'rodzaj żeński'), ('lyžica', 'łyżka', None, 'rodzaj żeński'), ('fľaša', 'butelka', None, 'rodzaj żeński'), ('jedálny lístok', 'menu', None, 'rodzaj męski'), ('účet', 'rachunek', None, 'rodzaj męski'), ('sprepitné', 'napiwek', None, 'rodzaj nijaki'), ('stôl (w restauracji)', 'stolik', None, 'rodzaj męski'), ('čašník', 'kelner', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('kuchár', 'kucharz', None, 'rodzaj męski'), ('hladný', 'głodny', None, None), ('smädný', 'spragniony', None, None), ('chutný', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('byt', 'mieszkanie', None, 'rodzaj męski'), ('izba', 'pokój', None, 'rodzaj żeński'), ('kuchyňa', 'kuchnia', None, 'rodzaj żeński'), ('kúpeľňa', 'łazienka', None, 'rodzaj żeński'), ('spálňa', 'sypialnia', None, 'rodzaj żeński'), ('obývačka', 'salon', None, 'rodzaj żeński'), ('záhrada', 'ogród', None, 'rodzaj żeński'), ('dvere', 'drzwi', None, None), ('okno', 'okno', None, 'rodzaj nijaki'), ('stena', 'ściana', None, 'rodzaj żeński'), ('podlaha', 'podłoga', None, 'rodzaj żeński'), ('strecha', 'dach', None, 'rodzaj żeński'), ('schody', 'schody', None, None), ('kľúč', 'klucz', None, 'rodzaj męski'), ('stôl', 'stół', None, 'rodzaj męski'), ('stolička', 'krzesło', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('posteľ', 'łóżko', None, 'rodzaj żeński'), ('skriňa', 'szafa', None, 'rodzaj żeński'), ('lampa', 'lampa', None, 'rodzaj żeński'), ('koberec', 'dywan', None, 'rodzaj męski'), ('zrkadlo', 'lustro', None, 'rodzaj nijaki'), ('televízor', 'telewizor', None, 'rodzaj męski'), ('telefón', 'telefon', None, 'rodzaj męski'), ('počítač', 'komputer', None, 'rodzaj męski'), ('hodiny', 'zegar', None, None), ('vankúš', 'poduszka', None, 'rodzaj męski'), ('prikrývka', 'koc', None, 'rodzaj żeński'), ('uterák', 'ręcznik', None, 'rodzaj męski'), ('mydlo', 'mydło', None, 'rodzaj nijaki'), ('zubná kefka', 'szczoteczka do zębów', None, 'rodzaj żeński'), ('chladnička', 'lodówka', None, 'rodzaj żeński'), ('pec', 'piec', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('práčka', 'pralka', None, 'rodzaj żeński'), ('odpadky', 'śmieci', None, None)], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('oblečenie', 'ubranie', None, 'rodzaj nijaki'), ('košeľa', 'koszula', None, 'rodzaj żeński'), ('nohavice', 'spodnie', None, None), ('šaty', 'sukienka', None, None), ('sukňa', 'spódnica', None, 'rodzaj żeński'), ('bunda', 'kurtka', None, 'rodzaj żeński'), ('kabát', 'płaszcz', None, 'rodzaj męski'), ('sveter', 'sweter', None, 'rodzaj męski'), ('topánky', 'buty', None, None), ('ponožky', 'skarpetki', None, None), ('čiapka', 'czapka', None, 'rodzaj żeński'), ('klobúk', 'kapelusz', None, 'rodzaj męski'), ('rukavice', 'rękawiczki', None, None), ('šál', 'szalik', None, 'rodzaj męski'), ('taška', 'torba', None, 'rodzaj żeński'), ('batoh', 'plecak', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('peňaženka', 'portfel', None, 'rodzaj żeński'), ('okuliare', 'okulary', None, None), ('hodinky', 'zegarek', None, None), ('prsteň', 'pierścionek', None, 'rodzaj męski'), ('bielizeň', 'bielizna', None, 'rodzaj żeński'), ('pyžama', 'piżama', None, 'rodzaj żeński'), ('opasok', 'pasek', None, 'rodzaj męski'), ('kravata', 'krawat', None, 'rodzaj żeński'), ('oblek', 'garnitur', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('červený', 'czerwony', None, None), ('modrý', 'niebieski', None, None), ('zelený', 'zielony', None, None), ('žltý', 'żółty', None, None), ('čierny', 'czarny', None, None), ('biely', 'biały', None, None), ('sivý', 'szary', None, None), ('hnedý', 'brązowy', None, None), ('ružový', 'różowy', None, None), ('fialový', 'fioletowy', None, None), ('farba', 'kolor', None, 'rodzaj żeński'), ('okrúhly', 'okrągły', None, None), ('štvorcový', 'kwadratowy', None, None), ('rovný', 'prosty', None, None), ('krivý', 'krzywy', None, None), ('čiara', 'linia', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('bod', 'punkt', None, 'rodzaj męski'), ('kruh', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('nula', 'zero', None, None), ('jedenásť', 'jedenaście', None, None), ('dvanásť', 'dwanaście', None, None), ('trinásť', 'trzynaście', None, None), ('štrnásť', 'czternaście', None, None), ('pätnásť', 'piętnaście', None, None), ('šestnásť', 'szesnaście', None, None), ('sedemnásť', 'siedemnaście', None, None), ('osemnásť', 'osiemnaście', None, None), ('devätnásť', 'dziewiętnaście', None, None), ('dvadsať', 'dwadzieścia', None, None), ('tridsať', 'trzydzieści', None, None), ('štyridsať', 'czterdzieści', None, None), ('päťdesiat', 'pięćdziesiąt', None, None), ('šesťdesiat', 'sześćdziesiąt', None, None), ('sedemdesiat', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('osemdesiat', 'osiemdziesiąt', None, None), ('deväťdesiat', 'dziewięćdziesiąt', None, None), ('sto', 'sto', None, None), ('tisíc', 'tysiąc', None, None), ('milión', 'milion', None, None), ('prvý', 'pierwszy', None, None), ('druhý', 'drugi', None, None), ('tretí', 'trzeci', None, None), ('polovica', 'połowa', None, 'rodzaj żeński'), ('pár', 'para', None, 'rodzaj męski'), ('niekoľko', 'kilka', None, None), ('veľa', 'wiele', None, None), ('málo', 'mało', None, None), ('celý', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('sekunda', 'sekunda', None, 'rodzaj żeński'), ('minúta', 'minuta', None, 'rodzaj żeński'), ('hodina', 'godzina', None, 'rodzaj żeński'), ('týždeň', 'tydzień', None, 'rodzaj męski'), ('mesiac', 'miesiąc', None, 'rodzaj męski'), ('rok', 'rok', None, 'rodzaj męski'), ('jar', 'wiosna', None, 'rodzaj żeński'), ('leto', 'lato', None, 'rodzaj nijaki'), ('jeseň', 'jesień', None, 'rodzaj żeński'), ('zima', 'zima', None, 'rodzaj żeński'), ('pondelok', 'poniedziałek', None, 'rodzaj męski'), ('utorok', 'wtorek', None, 'rodzaj męski'), ('streda', 'środa', None, 'rodzaj żeński'), ('štvrtok', 'czwartek', None, 'rodzaj męski'), ('piatok', 'piątek', None, 'rodzaj męski'), ('sobota', 'sobota', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('nedeľa', 'niedziela', None, 'rodzaj żeński'), ('január', 'styczeń', None, 'rodzaj męski'), ('február', 'luty', None, 'rodzaj męski'), ('marec', 'marzec', None, 'rodzaj męski'), ('apríl', 'kwiecień', None, 'rodzaj męski'), ('máj', 'maj', None, 'rodzaj męski'), ('jún', 'czerwiec', None, 'rodzaj męski'), ('júl', 'lipiec', None, 'rodzaj męski'), ('august', 'sierpień', None, 'rodzaj męski'), ('september', 'wrzesień', None, 'rodzaj męski'), ('október', 'październik', None, 'rodzaj męski'), ('november', 'listopad', None, 'rodzaj męski'), ('december', 'grudzień', None, 'rodzaj męski'), ('ráno', 'rano (pora dnia)', None, 'rodzaj nijaki'), ('poludnie', 'południe', None, 'rodzaj nijaki'), ('večer', 'wieczorem', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('vždy', 'zawsze', None, None), ('nikdy', 'nigdy', None, None), ('niekedy', 'czasem', None, None), ('často', 'często', None, None), ('už', 'już', None, None), ('ešte', 'jeszcze', None, None), ('čoskoro', 'wkrótce', None, None), ('neskôr', 'później', None, None), ('skoro', 'wcześnie', None, None), ('neskoro', 'późno', None, None), ('kedy', 'kiedy (pytanie)', None, None), ('dátum', 'data', None, 'rodzaj męski'), ('minulosť', 'przeszłość', None, 'rodzaj żeński'), ('budúcnosť', 'przyszłość', None, 'rodzaj żeński'), ('narodeniny', 'urodziny', None, None), ('sviatok', 'święto', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('prázdniny', 'wakacje', None, None)], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('slnko', 'słońce', None, 'rodzaj nijaki'), ('mesiac (ciało niebieskie)', 'księżyc', None, 'rodzaj męski'), ('hviezda', 'gwiazda', None, 'rodzaj żeński'), ('nebo', 'niebo', None, 'rodzaj nijaki'), ('oblak', 'chmura', None, 'rodzaj męski'), ('dážď', 'deszcz', None, 'rodzaj męski'), ('sneh', 'śnieg', None, 'rodzaj męski'), ('vietor', 'wiatr', None, 'rodzaj męski'), ('búrka', 'burza', None, 'rodzaj żeński'), ('hmla', 'mgła', None, 'rodzaj żeński'), ('ľad', 'lód', None, 'rodzaj męski'), ('oheň', 'ogień', None, None), ('zem', 'grunt)', None, 'rodzaj żeński'), ('rieka', 'rzeka', None, 'rodzaj żeński'), ('jazero', 'jezioro', None, 'rodzaj nijaki'), ('hora', 'góra', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('les', 'las', None, 'rodzaj męski'), ('strom', 'drzewo', None, 'rodzaj męski'), ('kvetina', 'kwiat', None, 'rodzaj żeński'), ('tráva', 'trawa', None, 'rodzaj żeński'), ('list', 'liść', None, 'rodzaj męski'), ('pole', 'pole', None, 'rodzaj nijaki'), ('ostrov', 'wyspa', None, 'rodzaj męski'), ('pláž', 'plaża', None, 'rodzaj żeński'), ('púšť', 'pustynia', None, 'rodzaj żeński'), ('skala', 'skała', None, 'rodzaj żeński'), ('kameň', 'kamień', None, 'rodzaj męski'), ('počasie', 'pogoda', None, 'rodzaj nijaki'), ('teplota', 'temperatura', None, 'rodzaj żeński'), ('studený', 'zimny', None, None), ('teplý', 'ciepły', None, None), ('horúci', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('pes', 'pies', None, 'rodzaj męski'), ('mačka', 'kot', None, 'rodzaj żeński'), ('kôň', 'koń', None, 'rodzaj męski'), ('krava', 'krowa', None, 'rodzaj żeński'), ('prasa', 'świnia', None, 'rodzaj nijaki'), ('ovca', 'owca', None, 'rodzaj żeński'), ('koza', 'koza', None, 'rodzaj żeński'), ('sliepka', 'kura', None, 'rodzaj żeński'), ('kačica', 'kaczka', None, 'rodzaj żeński'), ('vták', 'ptak', None, 'rodzaj męski'), ('myš', 'mysz', None, 'rodzaj żeński'), ('potkan', 'szczur', None, 'rodzaj męski'), ('had', 'wąż', None, 'rodzaj męski'), ('žaba', 'żaba', None, 'rodzaj żeński'), ('lev', 'lew', None, 'rodzaj męski'), ('tiger', 'tygrys', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('slon', 'słoń', None, 'rodzaj męski'), ('medveď', 'niedźwiedź', None, 'rodzaj męski'), ('vlk', 'wilk', None, 'rodzaj męski'), ('líška', 'lis', None, 'rodzaj żeński'), ('zajac', 'zając', None, 'rodzaj męski'), ('jeleň', 'jeleń', None, 'rodzaj męski'), ('opica', 'małpa', None, 'rodzaj żeński'), ('motýľ', 'motyl', None, 'rodzaj męski'), ('včela', 'pszczoła', None, 'rodzaj żeński'), ('mucha', 'mucha', None, 'rodzaj żeński'), ('pavúk', 'pająk', None, 'rodzaj męski'), ('zviera', 'zwierzę', None, 'rodzaj nijaki'), ('hmyz', 'owad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('dedina', 'wieś', None, 'rodzaj żeński'), ('cesta', 'droga', None, 'rodzaj żeński'), ('námestie', 'plac', None, 'rodzaj nijaki'), ('most', 'most', None, 'rodzaj męski'), ('park', 'park', None, 'rodzaj męski'), ('obchod', 'sklep', None, 'rodzaj męski'), ('trh', 'targ', None, 'rodzaj męski'), ('supermarket', 'supermarket', None, 'rodzaj męski'), ('banka', 'bank', None, 'rodzaj żeński'), ('pošta', 'poczta', None, 'rodzaj żeński'), ('nemocnica', 'szpital', None, 'rodzaj żeński'), ('lekáreň', 'apteka', None, 'rodzaj żeński'), ('univerzita', 'uniwersytet', None, 'rodzaj żeński'), ('knižnica', 'biblioteka', None, 'rodzaj żeński'), ('múzeum', 'muzeum', None, 'rodzaj nijaki'), ('kostol', 'kościół', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('reštaurácia', 'restauracja', None, 'rodzaj żeński'), ('kaviareň', 'kawiarnia', None, 'rodzaj żeński'), ('letisko', 'lotnisko', None, 'rodzaj nijaki'), ('stanica', 'dworzec', None, 'rodzaj żeński'), ('zastávka', 'przystanek', None, 'rodzaj żeński'), ('kino', 'kino', None, 'rodzaj nijaki'), ('divadlo', 'teatr', None, 'rodzaj nijaki'), ('polícia', 'policja', None, 'rodzaj żeński'), ('kancelária', 'biuro', None, 'rodzaj żeński'), ('továreň', 'fabryka', None, 'rodzaj żeński'), ('budova', 'budynek', None, 'rodzaj żeński'), ('veža', 'wieża', None, 'rodzaj żeński'), ('centrum', 'centrum', None, 'rodzaj nijaki'), ('adresa', 'adres', None, 'rodzaj żeński'), ('mapa', 'mapa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('auto', 'samochód', None, 'rodzaj nijaki'), ('autobus', 'autobus', None, 'rodzaj męski'), ('vlak', 'pociąg', None, 'rodzaj męski'), ('električka', 'tramwaj', None, 'rodzaj żeński'), ('metro', 'metro', None, 'rodzaj nijaki'), ('lietadlo', 'samolot', None, 'rodzaj nijaki'), ('loď', 'statek', None, 'rodzaj żeński'), ('bicykel', 'rower', None, 'rodzaj męski'), ('motorka', 'motocykl', None, 'rodzaj żeński'), ('taxík', 'taksówka', None, 'rodzaj męski'), ('cestovný lístok', 'bilet', None, 'rodzaj męski'), ('cesta (podróż)', 'podróż', None, 'rodzaj żeński'), ('výlet', 'wycieczka', None, 'rodzaj męski'), ('pas', 'paszport', None, 'rodzaj męski'), ('kufor', 'walizka', None, 'rodzaj męski'), ('benzín', 'benzyna', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('parkovisko', 'parking', None, 'rodzaj nijaki'), ('križovatka', 'skrzyżowanie', None, 'rodzaj żeński'), ('semafor', 'światła', None, 'rodzaj męski'), ('vodičský preukaz', 'prawo jazdy', None, 'rodzaj męski'), ('vodič', 'kierowca', None, 'rodzaj męski'), ('cestujúci', 'pasażer', None, 'rodzaj męski'), ('vjazd', 'wjazd', None, 'rodzaj męski'), ('výjazd', 'wyjazd', None, 'rodzaj męski'), ('železnica', 'kolej', None, 'rodzaj żeński'), ('prístav', 'port', None, 'rodzaj męski'), ('hranica', 'granica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('práca', 'praca', None, 'rodzaj żeński'), ('povolanie', 'zawód', None, 'rodzaj nijaki'), ('lekár', 'lekarz', None, 'rodzaj męski'), ('zdravotná sestra', 'pielęgniarka', None, 'rodzaj żeński'), ('žiak', 'uczeń', None, 'rodzaj męski'), ('inžinier', 'inżynier', None, 'rodzaj męski'), ('právnik', 'prawnik', None, 'rodzaj męski'), ('policajt', 'policjant', None, 'rodzaj męski'), ('vojak', 'żołnierz', None, 'rodzaj męski'), ('roľník', 'rolnik', None, 'rodzaj męski'), ('predavač', 'sprzedawca', None, 'rodzaj męski'), ('pokladník', 'kasjer', None, 'rodzaj męski'), ('herec', 'aktor', None, 'rodzaj męski'), ('spisovateľ', 'pisarz', None, 'rodzaj męski'), ('maliar', 'malarz', None, 'rodzaj męski'), ('hudobník', 'muzyk', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('umelec', 'artysta', None, 'rodzaj męski'), ('firma', 'firma', None, 'rodzaj żeński'), ('peniaze', 'pieniądze', None, None), ('plat', 'pensja', None, 'rodzaj męski'), ('zmluva', 'umowa', None, 'rodzaj żeński'), ('stretnutie', 'spotkanie', None, 'rodzaj nijaki'), ('lekcia', 'lekcja', None, 'rodzaj żeński'), ('skúška', 'egzamin', None, 'rodzaj żeński'), ('známka', 'ocena', None, 'rodzaj żeński'), ('trieda', 'klasa', None, 'rodzaj żeński'), ('kniha', 'książka', None, 'rodzaj żeński'), ('zošit', 'zeszyt', None, 'rodzaj męski'), ('pero', 'długopis', None, 'rodzaj nijaki'), ('ceruzka', 'ołówek', None, 'rodzaj żeński'), ('papier', 'papier', None, 'rodzaj męski'), ('tabuľa', 'tablica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('slovník', 'słownik', None, 'rodzaj męski'), ('otázka', 'pytanie', None, 'rodzaj żeński'), ('odpoveď', 'odpowiedź', None, 'rodzaj żeński'), ('úloha', 'zadanie', None, 'rodzaj żeński'), ('test', 'test', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('cena', 'cena', None, 'rodzaj żeński'), ('platobná karta', 'karta (płatnicza)', None, 'rodzaj żeński'), ('hotovosť', 'gotówka', None, 'rodzaj żeński'), ('minca', 'moneta', None, 'rodzaj żeński'), ('bankovka', 'banknot', None, 'rodzaj żeński'), ('drobné', 'reszta', None, None), ('zľava', 'zniżka', None, 'rodzaj żeński'), ('košík', 'koszyk', None, 'rodzaj męski'), ('pokladničný doklad', 'paragon', None, 'rodzaj męski'), ('tovar', 'towar', None, 'rodzaj męski'), ('nákup', 'zakup', None, 'rodzaj męski'), ('predaj', 'sprzedaż', None, 'rodzaj męski'), ('hodnota', 'wartość', None, 'rodzaj żeński'), ('úver', 'kredyt', None, 'rodzaj męski'), ('dlh', 'dług', None, 'rodzaj męski'), ('daň', 'podatek', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('bohatstvo', 'bogactwo', None, 'rodzaj nijaki'), ('chudobný', 'biedny', None, None), ('bohatý', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('zdravie', 'zdrowie', None, 'rodzaj nijaki'), ('choroba', 'choroba', None, 'rodzaj żeński'), ('bolesť', 'ból', None, 'rodzaj żeński'), ('horúčka', 'gorączka', None, 'rodzaj żeński'), ('kašeľ', 'kaszel', None, 'rodzaj męski'), ('nádcha', 'katar', None, 'rodzaj żeński'), ('liek', 'lekarstwo', None, 'rodzaj męski'), ('tabletka', 'tabletka', None, 'rodzaj żeński'), ('operácia', 'operacja', None, 'rodzaj żeński'), ('rana', 'rana', None, 'rodzaj żeński'), ('nehoda', 'wypadek', None, 'rodzaj żeński'), ('zdravý', 'zdrowy', None, None), ('chorý', 'chory', None, None), ('unavený', 'zmęczony', None, None), ('ospalý', 'śpiący', None, None), ('silný', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('slabý', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('radosť', 'radość', None, 'rodzaj żeński'), ('smútok', 'smutek', None, 'rodzaj męski'), ('strach', 'strach', None, 'rodzaj męski'), ('hnev', 'gniew', None, 'rodzaj męski'), ('láska', 'miłość', None, 'rodzaj żeński'), ('nenávisť', 'nienawiść', None, 'rodzaj żeński'), ('nádej', 'nadzieja', None, 'rodzaj żeński'), ('sen (marzenie)', 'marzenie', None, 'rodzaj męski'), ('šťastie', 'szczęście', None, 'rodzaj nijaki'), ('hanba', 'wstyd', None, 'rodzaj żeński'), ('prekvapenie', 'zdziwienie', None, 'rodzaj nijaki'), ('zvedavosť', 'ciekawość', None, 'rodzaj żeński'), ('trpezlivosť', 'cierpliwość', None, 'rodzaj żeński'), ('odvaha', 'odwaga', None, 'rodzaj żeński'), ('úprimný', 'szczery', None, None), ('milý', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('slušný', 'grzeczny', None, None), ('hlúpy', 'głupi', None, None), ('múdry', 'mądry', None, None), ('lenivý', 'leniwy', None, None), ('pracovitý', 'pracowity', None, None), ('zaujímavý', 'ciekawy', None, None), ('nudný', 'nudny', None, None), ('veselý', 'wesoły', None, None), ('smutný', 'smutny', None, None), ('nahnevaný', 'zły (rozgniewany)', None, None), ('šťastný', 'szczęśliwy', None, None), ('zamilovaný', 'zakochany', None, None), ('osamelý', 'samotny', None, None), ('pokojný', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('veľký', 'duży', None, None), ('dlhý', 'długi', None, None), ('krátky', 'krótki', None, None), ('vysoký', 'wysoki', None, None), ('nízky', 'niski', None, None), ('široký', 'szeroki', None, None), ('úzky', 'wąski', None, None), ('hrubý', 'gruby', None, None), ('chudý', 'chudy', None, None), ('ťažký', 'ciężki', None, None), ('ľahký', 'lekki', None, None), ('rýchly', 'szybki', None, None), ('pomalý', 'wolny', None, None), ('tvrdý', 'twardy', None, None), ('mäkký', 'miękki', None, None), ('mokrý', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('suchý', 'suchy', None, None), ('čistý', 'czysty', None, None), ('špinavý', 'brudny', None, None), ('plný', 'pełny', None, None), ('prázdny', 'pusty', None, None), ('ostrý', 'ostry', None, None), ('hlučný', 'głośny', None, None), ('tichý', 'cichy', None, None), ('svetlý', 'jasny', None, None), ('tmavý', 'ciemny', None, None), ('mladý', 'młody', None, None), ('starý', 'stary', None, None), ('nový', 'nowy', None, None), ('zlý', 'zły (niedobry)', None, None), ('pekný', 'ładny', None, None), ('škaredý', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('jednoduchý', 'łatwy', None, None), ('ťažký (trudny)', 'trudny', None, None), ('dôležitý', 'ważny', None, None), ('možný', 'możliwy', None, None), ('pravdivý', 'prawdziwy', None, None), ('falošný', 'fałszywy', None, None), ('drahý', 'drogi', None, None), ('lacný', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('byť', 'być', None, None), ('mať', 'mieć', None, None), ('robiť', 'robić', None, None), ('ísť', 'iść', None, None), ('ísť (jechać)', 'jechać', None, None), ('prísť', 'przyjść', None, None), ('vyjsť', 'wyjść', None, None), ('vojsť', 'wejść', None, None), ('vrátiť sa', 'wrócić', None, None), ('bežať', 'biec', None, None), ('stáť', 'stać', None, None), ('sedieť', 'siedzieć', None, None), ('ležať', 'leżeć', None, None), ('spať', 'spać', None, None), ('vstať', 'wstać', None, None), ('jesť', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('piť', 'pić', None, None), ('variť', 'gotować', None, None), ('umývať', 'myć', None, None), ('obliekať sa', 'ubierać się', None, None), ('hovoriť', 'mówić', None, None), ('povedať', 'powiedzieć', None, None), ('pýtať sa', 'pytać', None, None), ('odpovedať', 'odpowiadać', None, None), ('počuť', 'słyszeć', None, None), ('počúvať', 'słuchać', None, None), ('vidieť', 'widzieć', None, None), ('pozerať sa', 'patrzeć', None, None), ('čítať', 'czytać', None, None), ('písať', 'pisać', None, None), ('učiť sa', 'uczyć się', None, None), ('učiť', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('rozumieť', 'rozumieć', None, None), ('vedieť', 'wiedzieć', None, None), ('poznať', 'znać', None, None), ('myslieť', 'myśleć', None, None), ('pamätať', 'pamiętać', None, None), ('zabúdať', 'zapominać', None, None), ('chcieť', 'chcieć', None, None), ('mať rád', 'lubić', None, None), ('milovať', 'kochać', None, None), ('potrebovať', 'potrzebować', None, None), ('môcť', 'móc', None, None), ('musieť', 'musieć', None, None), ('dávať', 'dawać', None, None), ('brať', 'brać', None, None), ('kupovať', 'kupować', None, None), ('predávať', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('platiť', 'płacić', None, None), ('otvárať', 'otwierać', None, None), ('zatvárať', 'zamykać', None, None), ('začínať', 'zaczynać', None, None), ('končiť', 'kończyć', None, None), ('pracovať', 'pracować', None, None), ('hrať', 'grać', None, None), ('spievať', 'śpiewać', None, None), ('tancovať', 'tańczyć', None, None), ('plávať', 'pływać', None, None), ('lietať', 'latać', None, None), ('klásť', 'kłaść', None, None), ('hľadať', 'szukać', None, None), ('nachádzať', 'znajdować', None, None), ('čakať', 'czekać', None, None), ('pomáhať', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('prosiť', 'prosić', None, None), ('ospravedlňovať sa', 'przepraszać', None, None), ('dovoľovať', 'pozwalać', None, None), ('skúšať', 'próbować', None, None), ('meniť', 'zmieniać', None, None), ('nosiť', 'nosić', None, None), ('držať', 'trzymać', None, None), ('hádzať', 'rzucać', None, None), ('chytať', 'łapać', None, None), ('biť', 'bić', None, None), ('zabíjať', 'zabijać', None, None), ('umierať', 'umierać', None, None), ('žiť', 'żyć', None, None), ('bývať', 'mieszkać', None, None), ('stretávať', 'spotykać', None, None), ('volať', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('posielať', 'wysyłać', None, None), ('dostávať', 'dostawać', None, None), ('ukazovať', 'pokazywać', None, None), ('pozývať', 'zapraszać', None, None), ('navštevovať', 'odwiedzać', None, None), ('plakať', 'płakać', None, None), ('smiať sa', 'śmiać się', None, None), ('usmievať sa', 'uśmiechać się', None, None), ('báť sa', 'bać się', None, None), ('tešiť sa', 'cieszyć się', None, None), ('veriť', 'wierzyć', None, None), ('súhlasiť', 'zgadzać się', None, None), ('vyberať', 'wybierać', None, None), ('rozhodovať', 'decydować', None, None), ('počítať', 'liczyć', None, None), ('vážiť', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('chodiť', 'chodzić', None, None), ('jazdiť', 'jeździć', None, None), ('nastupovať', 'wsiadać', None, None), ('vystupovať', 'wysiadać', None, None), ('odbočovať', 'skręcać', None, None), ('zastavovať', 'zatrzymywać się', None, None), ('meškať', 'spóźniać się', None, None), ('ponáhľať sa', 'spieszyć się', None, None), ('odpočívať', 'odpoczywać', None, None), ('baviť sa', 'bawić się', None, None), ('kresliť', 'rysować', None, None), ('stavať', 'budować', None, None), ('opravovať', 'naprawiać', None, None), ('rezať', 'ciąć', None, None), ('smažiť', 'smażyć', None, None), ('piecť', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('miešať', 'mieszać', None, None), ('nalievať', 'nalewać', None, None), ('upratovať', 'sprzątać', None, None), ('prať', 'prać', None, None), ('žehliť', 'prasować', None, None), ('holiť sa', 'golić się', None, None), ('česať', 'czesać', None, None), ('kúpať sa', 'kąpać się', None, None), ('zobúdzať sa', 'budzić się', None, None), ('zaspávať', 'zasypiać', None, None), ('snívať', 'marzyć', None, None), ('snívať sa', 'śnić', None, None), ('cvičiť', 'ćwiczyć', None, None), ('trénovať', 'trenować', None, None), ('vyhrávať', 'wygrywać', None, None), ('prehrávať', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('hýbať', 'ruszać', None, None), ('ťahať', 'ciągnąć', None, None), ('tlačiť', 'pchać', None, None), ('dvíhať', 'podnosić', None, None), ('padať', 'spadać', None, None), ('skákať', 'skakać', None, None), ('liezť', 'wspinać się', None, None), ('skrývať', 'ukrywać', None, None), ('kradnúť', 'kraść', None, None), ('vracať', 'oddawać', None, None), ('požičiavať', 'pożyczać', None, None), ('míňať', 'wydawać', None, None), ('šetriť', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('ten', 'ten', None, None), ('tamten', 'tamten', None, None), ('ako', 'jak', None, None), ('prečo', 'dlaczego', None, None), ('čo', 'co', None, None), ('kto', 'kto', None, None), ('ktorý', 'który', None, None), ('aký', 'jaki', None, None), ('ale', 'ale', None, None), ('alebo', 'lub', None, None), ('pretože', 'bo', None, None), ('ak', 'jeśli', None, None), ('že', 'że', None, None), ('teda', 'więc', None, None), ('tiež', 'też', None, None), ('len', 'tylko', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('trochu', 'trochę', None, None), ('veľa (dużo)', 'dużo', None, None), ('všetko', 'wszystko', None, None), ('nič', 'nic', None, None), ('niečo', 'coś', None, None), ('niekto', 'ktoś', None, None), ('nikto', 'nikt', None, None), ('každý', 'każdy', None, None), ('iný', 'inny', None, None), ('ten istý', 'ten sam', None, None), ('možno', 'może (być)', None, None), ('určite', 'na pewno', None, None), ('spolu', 'razem', None, None), ('sám', 'sam', None, None), ('bez', 'bez', None, None), ('s', 'z (towarzysząc)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('v', 'w (miejsce)', None, None), ('na', 'na (powierzchni)', None, None), ('od', 'od', None, None), ('pre', 'dla', None, None), ('cez', 'przez', None, None), ('po', 'po (czas)', None, None), ('pred', 'przed', None, None), ('za', 'za (z tyłu)', None, None), ('nad', 'nad', None, None), ('pod', 'pod', None, None), ('vedľa', 'obok', None, None), ('medzi', 'między', None, None), ('proti', 'przeciw', None, None), ('o', 'o (temat)', None, None), ('u', 'u (przy)', None, None), ('okolo', 'około', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('takmer', 'prawie', None, None), ('dokonca', 'nawet', None, None), ('ešte raz', 'jeszcze raz', None, None), ('vtedy', 'wtedy', None, None), ('niekde', 'gdzieś', None, None), ('nikde', 'nigdzie', None, None), ('všade', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('život', 'życie', None, 'rodzaj męski'), ('smrť', 'śmierć', None, 'rodzaj żeński'), ('svet', 'świat', None, 'rodzaj męski'), ('krajina', 'kraj', None, 'rodzaj żeński'), ('štát', 'państwo', None, 'rodzaj męski'), ('reč', 'język (mowa)', None, 'rodzaj żeński'), ('slovo', 'słowo', None, 'rodzaj nijaki'), ('veta', 'zdanie', None, 'rodzaj żeński'), ('meno', 'imię', None, 'rodzaj nijaki'), ('priezvisko', 'nazwisko', None, 'rodzaj nijaki'), ('vek', 'wiek', None, 'rodzaj męski'), ('história', 'historia', None, 'rodzaj żeński'), ('kultúra', 'kultura', None, 'rodzaj żeński'), ('náboženstvo', 'religia', None, 'rodzaj nijaki'), ('Boh', 'Bóg', None, 'rodzaj męski'), ('vojna', 'wojna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('mier', 'pokój (brak wojny)', None, 'rodzaj męski'), ('zákon', 'prawo (przepis)', None, 'rodzaj męski'), ('sloboda', 'wolność', None, 'rodzaj żeński'), ('moc', 'władza', None, 'rodzaj żeński'), ('vláda', 'rząd', None, 'rodzaj żeński'), ('voľby', 'wybory', None, None), ('problém', 'problem', None, 'rodzaj męski'), ('nápad', 'pomysł', None, 'rodzaj męski'), ('dôvod', 'powód', None, 'rodzaj męski'), ('výsledok', 'wynik', None, 'rodzaj męski'), ('spôsob', 'sposób', None, 'rodzaj męski'), ('začiatok', 'początek', None, 'rodzaj męski'), ('koniec', 'koniec', None, 'rodzaj męski'), ('časť', 'część', None, 'rodzaj żeński'), ('miesto', 'miejsce', None, 'rodzaj nijaki'), ('vec', 'rzecz', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('záležitosť', 'sprawa', None, 'rodzaj żeński'), ('informácia', 'informacja', None, 'rodzaj żeński'), ('správa', 'wiadomość', None, 'rodzaj żeński'), ('list (korespondencja)', 'list', None, 'rodzaj męski'), ('noviny', 'gazeta', None, None), ('film', 'film', None, 'rodzaj męski'), ('hudba', 'muzyka', None, 'rodzaj żeński'), ('pesnička', 'piosenka', None, 'rodzaj żeński'), ('obraz', 'obraz', None, 'rodzaj męski'), ('hra', 'gra', None, 'rodzaj żeński'), ('šport', 'sport', None, 'rodzaj męski'), ('zápas', 'mecz', None, 'rodzaj męski'), ('tím', 'drużyna', None, 'rodzaj męski'), ('lopta', 'piłka', None, 'rodzaj żeński'), ('zábava', 'zabawa', None, 'rodzaj żeński'), ('oslava', 'impreza', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('darček', 'prezent', None, 'rodzaj męski'), ('sen', 'sen', None, 'rodzaj męski'), ('plán', 'plan', None, 'rodzaj męski'), ('výber', 'wybór', None, 'rodzaj męski'), ('chyba', 'błąd', None, 'rodzaj żeński'), ('pravda', 'prawda', None, 'rodzaj żeński'), ('lož', 'kłamstwo', None, 'rodzaj żeński'), ('tajomstvo', 'tajemnica', None, 'rodzaj nijaki'), ('sila', 'siła', None, 'rodzaj żeński'), ('energia', 'energia', None, 'rodzaj żeński'), ('svetlo', 'światło', None, 'rodzaj nijaki'), ('zvuk', 'dźwięk', None, 'rodzaj męski'), ('ticho', 'cisza', None, 'rodzaj nijaki'), ('pohyb', 'ruch', None, 'rodzaj męski'), ('zmena', 'zmiana', None, 'rodzaj żeński'), ('rozdiel', 'różnica', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('príklad', 'przykład', None, 'rodzaj męski'), ('celok', 'całość', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, 'rodzaj męski'), ('e-mail', 'e-mail', None, 'rodzaj męski'), ('heslo', 'hasło', None, 'rodzaj nijaki'), ('webová stránka', 'strona internetowa', None, 'rodzaj żeński'), ('program', 'program', None, 'rodzaj męski'), ('aplikácia', 'aplikacja', None, 'rodzaj żeński'), ('obrazovka', 'ekran', None, 'rodzaj żeński'), ('klávesnica', 'klawiatura', None, 'rodzaj żeński'), ('počítačová myš', 'myszka komputerowa', None, 'rodzaj żeński'), ('súbor', 'plik', None, 'rodzaj męski'), ('fotka', 'zdjęcie', None, 'rodzaj żeński'), ('kamera', 'kamera', None, 'rodzaj żeński'), ('batéria', 'bateria', None, 'rodzaj żeński'), ('elektrina', 'prąd', None, 'rodzaj żeński'), ('kábel', 'kabel', None, 'rodzaj męski'), ('stroj', 'maszyna', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('nástroj', 'narzędzie', None, 'rodzaj męski'), ('kladivo', 'młotek', None, 'rodzaj nijaki'), ('tlačiareň', 'drukarka', None, 'rodzaj żeński'), ('nabíjačka', 'ładowarka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('sever', 'północ', None, 'rodzaj męski'), ('juh', 'południe (kierunek)', None, 'rodzaj męski'), ('východ', 'wschód', None, 'rodzaj męski'), ('západ', 'zachód', None, 'rodzaj męski'), ('Poľsko', 'Polska', None, 'rodzaj nijaki'), ('Európa', 'Europa', None, 'rodzaj żeński'), ('Nemecko', 'Niemcy', None, 'rodzaj nijaki'), ('Francúzsko', 'Francja', None, 'rodzaj nijaki'), ('Taliansko', 'Włochy', None, 'rodzaj nijaki'), ('Španielsko', 'Hiszpania', None, 'rodzaj nijaki'), ('Rusko', 'Rosja', None, 'rodzaj nijaki'), ('Anglicko', 'Anglia', None, 'rodzaj nijaki'), ('Amerika', 'Ameryka', None, 'rodzaj żeński'), ('Čína', 'Chiny', None, 'rodzaj żeński'), ('Japonsko', 'Japonia', None, 'rodzaj nijaki'), ('Afrika', 'Afryka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('Ázia', 'Azja', None, 'rodzaj żeński'), ('kontinent', 'kontynent', None, 'rodzaj męski'), ('hlavné mesto', 'stolica', None, 'rodzaj nijaki'), ('občan', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('kus', 'kawałek', None, 'rodzaj męski'), ('kvapka', 'kropla', None, 'rodzaj żeński'), ('krabica', 'pudełko', None, 'rodzaj żeński'), ('vrece', 'worek', None, 'rodzaj nijaki'), ('niť', 'nić', None, 'rodzaj żeński'), ('drôt', 'drut', None, 'rodzaj męski'), ('ihla', 'igła', None, 'rodzaj żeński'), ('nožnice', 'nożyczki', None, None), ('palica', 'kij', None, 'rodzaj żeński'), ('lano', 'lina', None, 'rodzaj nijaki'), ('reťaz', 'łańcuch', None, 'rodzaj żeński'), ('skrutka', 'śruba', None, 'rodzaj żeński'), ('klinec', 'gwóźdź', None, 'rodzaj męski'), ('lepidlo', 'klej', None, 'rodzaj nijaki'), ('farba (farba)', 'farba', None, 'rodzaj żeński'), ('sklo', 'szkło', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('drevo', 'drewno', None, 'rodzaj nijaki'), ('kov', 'metal', None, 'rodzaj męski'), ('zlato', 'złoto', None, 'rodzaj nijaki'), ('striebro', 'srebro', None, 'rodzaj nijaki'), ('železo', 'żelazo', None, 'rodzaj nijaki'), ('plast', 'plastik', None, 'rodzaj męski'), ('koža (materiał)', 'skóra (materiał)', None, 'rodzaj żeński'), ('bavlna', 'bawełna', None, 'rodzaj żeński'), ('vlna', 'wełna', None, 'rodzaj żeński'), ('piesok', 'piasek', None, 'rodzaj męski'), ('blato', 'błoto', None, 'rodzaj nijaki'), ('prach', 'kurz', None, 'rodzaj męski'), ('dym', 'dym', None, 'rodzaj męski'), ('para', 'para (wodna)', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('hore', 'góra (kierunek)', None, None), ('dole', 'dół', None, None), ('vpredu', 'przód', None, None), ('vzadu', 'tył', None, None), ('stred', 'środek', None, 'rodzaj męski'), ('bok', 'bok', None, 'rodzaj męski'), ('vnútri', 'wewnątrz', None, None), ('vonku', 'na zewnątrz', None, None), ('ďaleko', 'daleko', None, None), ('blízko', 'blisko', None, None), ('vysoko', 'wysoko', None, None), ('nízko', 'nisko', None, None), ('rýchlo', 'szybko', None, None), ('pomaly', 'wolno', None, None), ('zle', 'źle', None, None), ('ľahko', 'łatwo', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('ťažko', 'trudno', None, None), ('osobitne', 'osobno', None, None), ('oproti', 'naprzeciw', None, None), ('pozdĺž', 'wzdłuż', None, None), ('naprieč', 'w poprzek', None, None), ('dookola', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('kapusta', 'kapusta', None, 'rodzaj żeński'), ('hrášok', 'groszek', None, 'rodzaj męski'), ('fazuľa', 'fasola', None, 'rodzaj żeński'), ('huba', 'grzyb', None, 'rodzaj żeński'), ('orech', 'orzech', None, 'rodzaj męski'), ('slivka', 'śliwka', None, 'rodzaj żeński'), ('čerešňa', 'wiśnia', None, 'rodzaj żeński'), ('broskyňa', 'brzoskwinia', None, 'rodzaj żeński'), ('melón', 'arbuz', None, 'rodzaj męski'), ('malina', 'malina', None, 'rodzaj żeński'), ('klobása', 'kiełbasa', None, 'rodzaj żeński'), ('šunka', 'szynka', None, 'rodzaj żeński'), ('žemľa', 'bułka', None, 'rodzaj żeński'), ('sendvič', 'kanapka', None, 'rodzaj męski'), ('palacinka', 'naleśnik', None, 'rodzaj żeński'), ('jogurt', 'jogurt', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('smotana', 'śmietana', None, 'rodzaj żeński'), ('omáčka', 'sos', None, 'rodzaj żeński'), ('ocot', 'ocet', None, 'rodzaj męski'), ('droždie', 'drożdże', None, 'rodzaj nijaki'), ('rosol', 'kisiel', None, 'rodzaj męski'), ('želé', 'galaretka', None, 'rodzaj nijaki'), ('hrozienko', 'rodzynek', None, 'rodzaj nijaki'), ('mandľa', 'migdał', None, 'rodzaj żeński'), ('petržlen', 'pietruszka', None, 'rodzaj męski'), ('kôpor', 'koperek', None, 'rodzaj męski'), ('paprika', 'papryka', None, 'rodzaj żeński'), ('hlávkový šalát', 'sałata', None, 'rodzaj męski'), ('špenát', 'szpinak', None, 'rodzaj męski'), ('cvikla', 'burak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('svokor', 'teść', None, 'rodzaj męski'), ('svokra', 'teściowa', None, 'rodzaj żeński'), ('švagor', 'szwagier', None, 'rodzaj męski'), ('synovec', 'bratanek', None, 'rodzaj męski'), ('neter', 'siostrzenica', None, 'rodzaj żeński'), ('sirota', 'sierota', None, 'rodzaj żeński'), ('vdova', 'wdowa', None, 'rodzaj żeński'), ('snúbenec', 'narzeczony', None, 'rodzaj męski'), ('svadba', 'ślub', None, 'rodzaj żeński'), ('rozvod', 'rozwód', None, 'rodzaj męski'), ('narodenie', 'urodzenie', None, 'rodzaj nijaki'), ('pohreb', 'pogrzeb', None, 'rodzaj męski'), ('kaderník', 'fryzjer', None, 'rodzaj męski'), ('pekár', 'piekarz', None, 'rodzaj męski'), ('mäsiar', 'rzeźnik', None, 'rodzaj męski'), ('čašníčka', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('poštár', 'listonosz', None, 'rodzaj męski'), ('hasič', 'strażak', None, 'rodzaj męski'), ('sudca', 'sędzia', None, 'rodzaj męski'), ('riaditeľ', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
