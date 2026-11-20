"""Treść kursu: czeski dla Polaków."""

PUNCT = {'!', ',', '.', ':', '?'}

TRACKS = {'wymowa': 'VÝSLOVNOST · WYMOWA', 'jezyk': 'JAZYK · JĘZYK'}

UNITS = [
    {'id': 'wymowa', 'title': 'Wymowa', 'icon': 'Ř', 'track': 'wymowa',
     'letters': [
         ('ř', '[r̝]: r i ż wymówione jednocześnie', 'řeka (rzeka)'),
         ('ě', '[jɛ]: je; zmiękcza poprzednią spółgłoskę (dě, tě, ně)', 'město (miasto)'),
         ('ů', '[uː]: długie u (kółko zamiast kreski)', 'dům (dom)'),
         ('á, é, í, ó, ú, ý', 'kreska oznacza długą samogłoskę, nie akcent', 'káva (kawa)'),
         ('č', '[tʃ]: jak polskie cz', 'čaj (herbata)'),
         ('š', '[ʃ]: jak polskie sz', 'škola (szkoła)'),
         ('ž', '[ʒ]: jak polskie ż', 'žena (kobieta)'),
         ('ch', '[x]: jak polskie ch; w słowniku osobna litera po h', 'chléb (chleb)'),
         ('h', '[ɦ]: dźwięczne h, tam gdzie po polsku g', 'hora (góra)'),
         ('ď, ť, ň', '[ɟ], [c], [ɲ]: miękkie d, t, n', 'ťukat (stukać)'),
         ('y, ý', '[ɪ], [iː]: czytane tak samo jak i, í', 'ryba (ryba)'),
         ('ou', '[ou̯]: dwugłoska, jedno o-u', 'mouka (mąka)'),
         ('akcent', 'zawsze na pierwszej sylabie słowa', 'Polsko (Polska)'),
     ],
    },
    {'id': 'slowa', 'title': 'Pierwsze słowa', 'icon': 'A', 'track': 'jezyk', 'requires': 'wymowa',
     'words': [
         ('ahoj', 'cześć', None, None),
         ('dobrý', 'dobry', None, None),
         ('den', 'dzień', None, None),
         ('dobrou', 'dobrą (biernik)', None, None),
         ('noc', 'noc', None, None),
         ('děkuji', 'dziękuję', None, None),
         ('prosím', 'proszę', None, None),
         ('ano', 'tak', None, None),
         ('ne', 'nie', None, None),
         ('promiňte', 'przepraszam', None, None),
         ('na', 'na; do', None, None),
         ('shledanou', 'zobaczenie (w „na shledanou”)', None, '„Na shledanou” = do widzenia.'),
         ('dobře', 'dobrze', None, None),
         ('moc', 'bardzo; dużo', None, 'Nie „moc”, tylko „bardzo”: děkuji moc.'),
     ],
     'sentences': [
         (['ahoj', '!'], 'Cześć!', {'promiňte': 'promiňte to „przepraszam”.'}),
         (['dobrý', 'den', '!'], 'Dzień dobry!', {'noc': 'noc to „noc”.'}),
         (['dobrou', 'noc', '!'], 'Dobranoc!', {'den': 'den to „dzień”.'}),
         (['děkuji', '!'], 'Dziękuję!', {'prosím': 'prosím to „proszę”. Tu dziękujesz.'}),
         (['ano', ',', 'děkuji'], 'Tak, dziękuję.', {'ne': 'ne to „nie”.'}),
         (['ne', ',', 'děkuji'], 'Nie, dziękuję.', {'ano': 'ano to „tak”.'}),
         (['promiňte', '!'], 'Przepraszam!', {}),
         (['na', 'shledanou', '!'], 'Do widzenia!', {}),
         (['děkuji', 'moc'], 'Dziękuję bardzo.', {}),
     ],
    },
    {'id': 'ja', 'title': 'Ja, ty, on', 'icon': 'J', 'track': 'jezyk',
     'words': [
         ('já', 'ja', None, None),
         ('ty', 'ty', None, None),
         ('on', 'on', None, None),
         ('ona', 'ona', None, None),
         ('jsem', 'jestem', None, 'j na początku zwykle się nie wymawia: [sem].'),
         ('jsi', 'jesteś', None, None),
         ('je', 'jest', None, None),
         ('student', 'student', 'student', None),
         ('učitel', 'nauczyciel', None, None),
         ('Polák', 'Polak', None, None),
         ('Polka', 'Polka', None, None),
         ('z', 'z', None, None),
         ('Polska', 'Polski', None, 'Po „z”: dopełniacz.'),
         ('Česka', 'Czech', None, 'Po „z”: dopełniacz.'),
     ],
     'sentences': [
         (['já', 'jsem', 'student'], 'Jestem studentem.', {'jsi': 'jsi to „jesteś”. O sobie: jsem.'}),
         (['ty', 'jsi', 'učitel'], 'Jesteś nauczycielem.', {'jsem': 'jsem to „jestem”. Do „ty”: jsi.'}),
         (['on', 'je', 'Polák'], 'On jest Polakiem.', {'Polka': 'Dla mężczyzny: Polák.'}),
         (['ona', 'je', 'Polka'], 'Ona jest Polką.', {'Polák': 'Dla kobiety: Polka.'}),
         (['já', 'jsem', 'z', 'Polska'], 'Jestem z Polski.', {'Česka': 'Česka to „Czech”.'}),
         (['ona', 'je', 'z', 'Česka'], 'Ona jest z Czech.', {}),
     ],
    },
    {'id': 'ludzie', 'title': 'Ludzie i rodzina', 'icon': 'R', 'track': 'jezyk',
     'words': [
         ('matka', 'matka', None, None),
         ('otec', 'ojciec', None, None),
         ('bratr', 'brat', None, None),
         ('bratra', 'brata', None, 'Biernik: -a.'),
         ('sestra', 'siostra', None, None),
         ('sestru', 'siostrę', None, 'Biernik: -a → -u.'),
         ('dítě', 'dziecko', None, None),
         ('přítel', 'przyjaciel', None, None),
         ('žena', 'kobieta; żona', None, None),
         ('muž', 'mężczyzna; mąż', None, None),
         ('můj', 'mój (męski)', None, None),
         ('moje', 'moja (żeński)', None, None),
         ('mám', 'mam', None, None),
         ('máš', 'masz', None, None),
         ('malý', 'mały (męski)', None, None),
         ('malá', 'mała (żeński)', None, None),
         ('dobrá', 'dobra (żeński)', None, None),
     ],
     'sentences': [
         (['můj', 'bratr', 'je', 'malý'], 'Mój brat jest mały.', {'moje': 'bratr jest męski: můj.'}),
         (['moje', 'sestra', 'je', 'malá'], 'Moja siostra jest mała.', {'můj': 'sestra jest żeńska: moje.'}),
         (['matka', 'je', 'dobrá'], 'Matka jest dobra.', {}),
         (['mám', 'bratra'], 'Mam brata.', {'máš': 'máš to „masz”. O sobie: mám.'}),
         (['máš', 'sestru'], 'Masz siostrę.', {'mám': 'mám to „mam”. Do „ty”: máš.'}),
         (['otec', 'je', 'muž'], 'Ojciec jest mężczyzną.', {}),
         (['můj', 'přítel', 'je', 'dobrý'], 'Mój przyjaciel jest dobry.', {}),
     ],
    },
    {'id': 'jedzenie', 'title': 'Jedzenie i picie', 'icon': 'K', 'track': 'jezyk',
     'words': [
         ('voda', 'woda', None, None),
         ('vodu', 'wodę', None, 'Biernik: -a → -u.'),
         ('káva', 'kawa', None, None),
         ('kávu', 'kawę', None, None),
         ('čaj', 'herbata', None, None),
         ('chléb', 'chleb', None, None),
         ('sýr', 'ser', None, None),
         ('mléko', 'mleko', None, None),
         ('ryba', 'ryba', None, None),
         ('rybu', 'rybę', None, None),
         ('jablko', 'jabłko', None, None),
         ('chci', 'chcę', None, None),
         ('chceš', 'chcesz', None, None),
         ('chutná', 'smaczna', None, None),
         ('velmi', 'bardzo', None, None),
         ('teď', 'teraz', None, None),
     ],
     'sentences': [
         (['já', 'chci', 'kávu'], 'Chcę kawę.', {'chceš': 'chceš to „chcesz”. O sobie: chci.'}),
         (['ty', 'chceš', 'čaj'], 'Chcesz herbatę.', {'chci': 'chci to „chcę”. Do „ty”: chceš.'}),
         (['já', 'chci', 'chléb'], 'Chcę chleb.', {}),
         (['ty', 'chceš', 'jablko'], 'Chcesz jabłko.', {}),
         (['ryba', 'je', 'velmi', 'chutná'], 'Ryba jest bardzo smaczna.', {}),
         (['teď', 'chci', 'vodu'], 'Teraz chcę wodę.', {'voda': 'Po „chci” biernik: vodu.'}),
     ],
    },
    {'id': 'liczby', 'title': 'Liczby i czas', 'icon': '1', 'track': 'jezyk',
     'words': [
         ('dva', 'dwa', None, None),
         ('tři', 'trzy', None, None),
         ('čtyři', 'cztery', None, None),
         ('pět', 'pięć', None, None),
         ('deset', 'dziesięć', None, None),
         ('bratry', 'braci (biernik lm.)', None, None),
         ('jablka', 'jabłka', None, None),
         ('dnes', 'dziś', None, None),
         ('zítra', 'jutro', None, None),
         ('včera', 'wczoraj', None, None),
         ('hodin', 'godzin', None, None),
         ('kolik', 'ile', None, None),
     ],
     'sentences': [
         (['mám', 'dva', 'bratry'], 'Mam dwóch braci.', {}),
         (['já', 'chci', 'tři', 'jablka'], 'Chcę trzy jabłka.', {'dva': 'dva to „dwa”. Chcesz trzy: tři.'}),
         (['kolik', 'je', 'hodin', '?'], 'Która jest godzina?', {}),
         (['teď', 'je', 'deset', 'hodin'], 'Jest dziesiąta.', {'pět': 'pět to „pięć”.'}),
         (['dnes', 'chci', 'kávu'], 'Dziś chcę kawę.', {'zítra': 'zítra to „jutro”. Tu „dziś”: dnes.'}),
         (['zítra', 'chci', 'rybu'], 'Jutro chcę rybę.', {'včera': 'včera to „wczoraj”.'}),
     ],
    },
    {'id': 'miejsca', 'title': 'Miejsca i podróż', 'icon': 'M', 'track': 'jezyk',
     'words': [
         ('dům', 'dom', None, None),
         ('domů', 'do domu', None, None),
         ('město', 'miasto', None, None),
         ('ulice', 'ulica', None, None),
         ('škola', 'szkoła', None, None),
         ('moře', 'morze', None, None),
         ('taxi', 'taksówka', 'taksówka', None),
         ('hotel', 'hotel', 'hotel', None),
         ('kde', 'gdzie', None, None),
         ('tady', 'tu', None, None),
         ('tam', 'tam', None, None),
         ('jdu', 'idę (pieszo)', None, None),
         ('jedu', 'jadę (pojazdem)', None, None),
         ('do', 'do', None, None),
         ('Prahy', 'Pragi (do Pragi)', None, 'Po „do”: dopełniacz.'),
         ('vpravo', 'w prawo; po prawej', None, None),
         ('vlevo', 'w lewo; po lewej', None, None),
     ],
     'sentences': [
         (['kde', 'je', 'hotel', '?'], 'Gdzie jest hotel?', {'tady': 'tady to „tu”. Pytasz „gdzie”: kde.'}),
         (['hotel', 'je', 'tam'], 'Hotel jest tam.', {'tady': 'tady to „tu”. Tu „tam”: tam.'}),
         (['jdu', 'domů'], 'Idę do domu.', {'jedu': 'Pieszo: jdu. Pojazdem: jedu.'}),
         (['jedu', 'do', 'Prahy'], 'Jadę do Pragi.', {}),
         (['taxi', 'je', 'vpravo'], 'Taksówka jest po prawej.', {'vlevo': 'vlevo to „po lewej”.'}),
         (['škola', 'je', 'tam'], 'Szkoła jest tam.', {}),
     ],
    },
]

INSIGHTS = {
    'wymowa': [
        {'title': 'Kreska to długość, nie akcent', 'chain': [], 'text': 'Akcent pada zawsze na pierwszą sylabę. Kreska nad samogłoską (á, é, í) i kółko (ů) oznaczają, że samogłoska jest długa, i mogą zmieniać znaczenie słowa. Najtrudniejszy dźwięk to ř: r i ż wymówione jednocześnie.'},
    ],
    'slowa': [
        {'title': 'Fałszywi przyjaciele', 'chain': [], 'text': 'Czeski brzmi znajomo, ale uwaga na pułapki: čerstvý to „świeży”, sklep to „piwnica”, květen to „maj”, záchod to „toaleta”, pozor to „uwaga”, a šukat jest wulgarne (szukać to hledat). Słowo „moc” znaczy „bardzo”.'},
    ],
    'ja': [
        {'title': 'Jsem, jsi, je', 'chain': [('Jestem studentem.', ['já', 'jsem', 'student'], 'Do „já” pasuje jsem.'), ('Jesteś nauczycielem.', ['ty', 'jsi', 'učitel'], 'Do „ty” pasuje jsi.')], 'text': 'Zaimek já, ty zwykle się pomija: „Jsem student”. Po czasowniku „być” stoi mianownik, nie narzędnik: jsem student, nie „studentem”.'},
    ],
    'ludzie': [
        {'title': 'Biernik prawie jak po polsku', 'chain': [], 'text': 'Rzeczowniki żeńskie na -a mają w bierniku -u: sestra → sestru. Męskie żywotne dostają -a: bratr → bratra. Zaimek „mój” zgadza się z rodzajem: můj bratr, moje sestra.'},
    ],
    'jedzenie': [
        {'title': 'Chci i chceš', 'chain': [], 'text': 'Czasownik chtít: chci (chcę), chceš (chcesz). Grzeczniej w kawiarni: „Dám si kávu” (wezmę kawę) albo „Prosím kávu”.'},
    ],
}

ENDINGS_INSIGHT = {'title': 'Rodzaj i forma czasownika', 'text': 'Po czesku ćwiczysz rodzaj (můj/moje) i formy czasownika (jsem, jsi, je; chci, chceš). Tu to robisz.'}

ENDINGS = [
    ('já ', '', 'jsem', ' student', ['jsem', 'jsi', 'je'], 'ja jestem', 'Do „já” pasuje jsem.', 'ja'),
    ('ty ', '', 'jsi', ' učitel', ['jsem', 'jsi', 'je'], 'ty jesteś', 'Do „ty” pasuje jsi.', 'ja'),
    ('on ', '', 'je', ' Polák', ['jsem', 'jsi', 'je'], 'on jest', 'Do „on” pasuje je.', 'ja'),
    ('', '', 'můj', ' bratr', ['můj', 'moje'], 'mój (męski)', 'bratr jest męski: můj.', 'ludzie'),
    ('', '', 'moje', ' sestra', ['můj', 'moje'], 'moja (żeński)', 'sestra jest żeńska: moje.', 'ludzie'),
    ('', '', 'mám', ' bratra', ['mám', 'máš'], 'ja mam', 'Do „já” pasuje mám.', 'ludzie'),
    ('', '', 'máš', ' sestru', ['mám', 'máš'], 'ty masz', 'Do „ty” pasuje máš.', 'ludzie'),
    ('já ', '', 'chci', ' kávu', ['chci', 'chceš'], 'ja chcę', 'Do „já” pasuje chci.', 'jedzenie'),
    ('ty ', '', 'chceš', ' čaj', ['chci', 'chceš'], 'ty chcesz', 'Do „ty” pasuje chceš.', 'jedzenie'),
    ('jsem ', '', 'z', ' Polska', ['z', 'do'], 'z', 'z to „z”, do to „do”.', 'miejsca'),
    ('jedu ', '', 'do', ' Prahy', ['z', 'do'], 'do', 'do to „do”.', 'miejsca'),
]

CHAT_EXTRA = {'a': 'i', 'Jana': 'Jana (imię)', 'Petr': 'Petr (imię)', 'taxikář': 'taksówkarz', 'kam': 'dokąd', 'jedeš': 'jedziesz'}

CHATS = [
    {'id': 'kavarna', 'title': 'W kawiarni', 'partner': 'Jana', 'avatar': 'J', 'requires': 'jedzenie',
     'turns': [
         {'bot': ['dobrý', 'den', '!'], 'en': 'Dzień dobry!', 'options': [(['dobrý', 'den', '!'], True, None), (['dobrou', 'noc', '!'], False, 'dobrou noc to „dobranoc”. Jest dzień.')]},
         {'bot': ['kávu', '?'], 'en': 'Kawę?', 'options': [(['ano', ',', 'já', 'chci', 'kávu'], True, None), (['ano', ',', 'ty', 'chceš', 'kávu'], False, 'chceš jest do „ty”. O sobie: chci.')]},
         {'bot': ['a', 'chléb', '?'], 'en': 'I chleb?', 'options': [(['ne', ',', 'děkuji'], True, None), (['prosím', '!'], False, 'prosím to „proszę”. Odmów: ne, děkuji.')]},
         {'bot': ['dobře', '!'], 'build': (['děkuji', '!'], 'Dziękuję!'), 'en': 'Dobrze!'},
     ]},
    {'id': 'seznameni', 'title': 'Poznajemy się', 'partner': 'Petr', 'avatar': 'P', 'requires': 'ludzie',
     'turns': [
         {'bot': ['ahoj', '!'], 'en': 'Cześć!', 'options': [(['ahoj', '!'], True, None), (['promiňte', '!'], False, 'promiňte to „przepraszam”. Powitaj: ahoj.')]},
         {'bot': ['ty', 'jsi', 'z', 'Česka', '?'], 'en': 'Jesteś z Czech?', 'options': [(['ne', ',', 'já', 'jsem', 'z', 'Polska'], True, None), (['ne', ',', 'já', 'jsi', 'z', 'Polska'], False, 'jsi jest do „ty”. O sobie: jsem.')]},
         {'bot': ['máš', 'bratra', '?'], 'en': 'Masz brata?', 'options': [(['ano', ',', 'mám', 'bratra'], True, None), (['ano', ',', 'máš', 'bratra'], False, 'máš to „masz”. O sobie: mám.')]},
         {'bot': ['na', 'shledanou', '!'], 'build': (['na', 'shledanou', '!'], 'Do widzenia!'), 'en': 'Do widzenia!'},
     ]},
    {'id': 'taxi', 'title': 'W taksówce', 'partner': 'taxikář', 'avatar': 'T', 'requires': 'miejsca',
     'turns': [
         {'bot': ['dobrý', 'den', '!'], 'en': 'Dzień dobry!', 'options': [(['dobrý', 'den', '!'], True, None), (['dobrou', 'noc', '!'], False, 'dobrou noc to „dobranoc”. Jest dzień.')]},
         {'bot': ['kam', 'jedeš', '?'], 'en': 'Dokąd jedziesz?', 'options': [(['jedu', 'do', 'Prahy'], True, None), (['jedeš', 'do', 'Prahy'], False, 'jedeš to „jedziesz”. O sobie: jedu.')]},
         {'bot': ['hotel', 'je', 'tam', '.'], 'en': 'Hotel jest tam.', 'options': [(['vpravo', '?'], True, None), (['tady', '?'], False, 'Pytasz o kierunek: vpravo.')]},
         {'bot': ['ano', '!'], 'build': (['děkuji', '!'], 'Dziękuję!'), 'en': 'Tak!'},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['já', 'ty', 'on/ona', 'my', 'vy', 'oni'],
    'przyp': ['nominativ', 'genitiv', 'dativ', 'akuzativ', 'vokativ', 'lokál (o…)', 'instrumentál'],
    'przyp6': ['nominativ', 'genitiv', 'dativ', 'akuzativ', 'lokál (o…)', 'instrumentál'],
    'lpart': ['męski lp.', 'żeński lp.', 'nijaki lp.', 'męski żywotny lm.', 'żeński lm.'],
    'trp': ['dělat', 'prosit', 'nést', 'psát', 'otevřít'],
    'liczrz': ['1', '2', '3', '4', '5', '10', '21', '100'],
    't_ff': ['čerstvý', 'sklep', 'květen', 'záchod', 'pozor', 'hledat', 'chudý', 'divák'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'dělat (robić): -ám', 'os', 'dělám; děláš; dělá; děláme; děláte; dělají', None),
    ('conj', 'Wzory koniugacji', 'mluvit (mówić): -ím', 'os', 'mluvím; mluvíš; mluví; mluvíme; mluvíte; mluví', '3. osoba lm. = 3. osoba lp.'),
    ('conj', 'Wzory koniugacji', 'pracovat (pracować): -uji', 'os', 'pracuji; pracuješ; pracuje; pracujeme; pracujete; pracují', 'Potocznie też: pracuju, pracujou.'),
    ('conj', 'Wzory koniugacji', 'nést (nieść): -u', 'os', 'nesu; neseš; nese; neseme; nesete; nesou', None),
    ('conj', 'Wyjątki', 'rozumět (rozumieć)', 'os', 'rozumím; rozumíš; rozumí; rozumíme; rozumíte; rozumějí', 'Jak mluvit, ale 3. osoba lm. na -ějí.'),
    ('conj', 'Czasowniki nieregularne', 'být (być)', 'os', 'jsem; jsi; je; jsme; jste; jsou', None),
    ('conj', 'Czasowniki nieregularne', 'mít (mieć)', 'os', 'mám; máš; má; máme; máte; mají', None),
    ('conj', 'Czasowniki nieregularne', 'chtít (chcieć)', 'os', 'chci; chceš; chce; chceme; chcete; chtějí', None),
    ('conj', 'Czasowniki nieregularne', 'jít (iść)', 'os', 'jdu; jdeš; jde; jdeme; jdete; jdou', None),
    ('conj', 'Czasowniki nieregularne', 'jet (jechać)', 'os', 'jedu; jedeš; jede; jedeme; jedete; jedou', None),
    ('conj', 'Czasowniki nieregularne', 'jíst (jeść)', 'os', 'jím; jíš; jí; jíme; jíte; jedí', None),
    ('conj', 'Czasowniki nieregularne', 'vědět (wiedzieć)', 'os', 'vím; víš; ví; víme; víte; vědí', None),
    ('conj', 'Czasowniki nieregularne', 'moci (móc)', 'os', 'mohu; můžeš; může; můžeme; můžete; mohou', None),
    ('conj', 'Czas przeszły', 'dělat: czas przeszły', 'os', 'dělal jsem; dělal jsi; dělal; dělali jsme; dělali jste; dělali', 'Imiesłów na -l + být; w 3. osobie bez být.'),
    ('conj', 'Czas przyszły', 'být: czas przyszły', 'os', 'budu; budeš; bude; budeme; budete; budou', 'Czas przyszły niedokonany: budu + bezokolicznik.'),
    ('form', 'Imiesłowy', 'dělat: imiesłów na -l', 'lpart', 'dělal; dělala; dělalo; dělali; dělaly', None),
    ('form', 'Imiesłowy', 'být: imiesłów na -l', 'lpart', 'byl; byla; bylo; byli; byly', None),
    ('form', 'Imiesłowy', 'jít (wyjątek): imiesłów na -l', 'lpart', 'šel; šla; šlo; šli; šly', None),
    ('form', 'Imiesłowy', 'Imiesłów bierny', 'trp', 'dělán; prošen; nesen; psán; otevřen', '-n, -en; w przydawce forma długa: dělaný, otevřený.'),
    ('decl', 'Wzory deklinacji', 'pán (pan): męski żywotny twardy', 'przyp', 'pán; pána; pánovi; pána; pane; pánovi; pánem', None),
    ('decl', 'Wzory deklinacji', 'hrad (zamek): męski nieżywotny', 'przyp', 'hrad; hradu; hradu; hrad; hrade; hradu; hradem', 'U nieżywotnych biernik = mianownik.'),
    ('decl', 'Wzory deklinacji', 'muž (mężczyzna): męski żywotny miękki', 'przyp', 'muž; muže; muži; muže; muži; muži; mužem', None),
    ('decl', 'Wzory deklinacji', 'žena (kobieta): żeński twardy', 'przyp', 'žena; ženy; ženě; ženu; ženo; ženě; ženou', None),
    ('decl', 'Wzory deklinacji', 'růže (róża): żeński miękki', 'przyp', 'růže; růže; růži; růži; růže; růži; růží', None),
    ('decl', 'Wzory deklinacji', 'město (miasto): nijaki twardy', 'przyp', 'město; města; městu; město; město; městě; městem', None),
    ('decl', 'Wzory deklinacji', 'moře (morze): nijaki miękki', 'przyp', 'moře; moře; moři; moře; moře; moři; mořem', None),
    ('decl', 'Wyjątki', 'otec (ojciec)', 'przyp', 'otec; otce; otci; otce; otče; otci; otcem', 'Ruchome e: otec → otce. Wołacz: otče.'),
    ('decl', 'Wyjątki', 'dům (dom)', 'przyp', 'dům; domu; domu; dům; dome; domě; domem', 'ů → o w pozostałych przypadkach.'),
    ('decl', 'Zaimki', 'já (ja)', 'przyp6', 'já; mě; mně; mě; mně; mnou', None),
    ('decl', 'Zaimki', 'ty (ty)', 'przyp6', 'ty; tebe; tobě; tebe; tobě; tebou', None),
    ('decl', 'Liczebniki', 'jeden (jeden): rodzaj męski', 'przyp6', 'jeden; jednoho; jednomu; jeden; jednom; jedním', None),
    ('decl', 'Liczebniki', 'jedna (jedna): rodzaj żeński', 'przyp6', 'jedna; jedné; jedné; jednu; jedné; jednou', None),
    ('decl', 'Liczebniki', 'dva (dwa)', 'przyp6', 'dva; dvou; dvěma; dva; dvou; dvěma', 'Pozostałość liczby podwójnej; tak samo oba.'),
    ('decl', 'Liczebniki', 'tři (trzy)', 'przyp6', 'tři; tří; třem; tři; třech; třemi', None),
    ('decl', 'Liczebniki', 'čtyři (cztery)', 'przyp6', 'čtyři; čtyř; čtyřem; čtyři; čtyřech; čtyřmi', None),
    ('decl', 'Liczebniki', 'pět (pięć)', 'przyp6', 'pět; pěti; pěti; pět; pěti; pěti', '5–99: jedna forma -i we wszystkich przypadkach zależnych.'),
    ('decl', 'Liczebniki', 'sto (sto)', 'przyp6', 'sto; sta; stu; sto; stu; stem', 'Odmienia się jak město.'),
    ('form', 'Liczebniki', 'Liczebnik + rzeczownik: rok', 'liczrz', 'jeden rok; dva roky; tři roky; čtyři roky; pět let; deset let; dvacet jedna let; sto let', 'Po 2–4: mianownik lm. Od 5: dopełniacz lm. (rok → let).'),
    ('form', 'Typowe trudności', 'Fałszywi przyjaciele: co to znaczy?', 't_ff', 'świeży; piwnica; maj; toaleta; uwaga; szukać; biedny; widz', None),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['byt', 'být', 'dal', 'dál', 'rada', 'ráda'],
    't_m1': ['góra', 'głowa', 'gęś', 'noga', 'gwiazda', 'głos', 'gość', 'ogień'],
    't_m2': ['pan', 'Petr', 'Jana', 'muž', 'otec', 'Tomáš', 'učitel', 'Marie'],
    't_m3': ['Jestem studentem.', 'On jest nauczycielem.', 'Ona jest Polką.', 'Jesteś lekarzem.', 'To jest pies.', 'Jesteśmy przyjaciółmi.'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Długość: co to znaczy?', 't_m0', 'mieszkanie; być; dał; dalej; rada; chętnie (ona)', 'Kreska to długość, nie akcent.'),
    ('form', 'Typowe trudności', 'Polskie g, czeskie h', 't_m1', 'hora; hlava; husa; noha; hvězda; hlas; host; oheň', None),
    ('form', 'Typowe trudności', 'Wołacz', 't_m2', 'pane; Petře; Jano; muži; otče; Tomáši; učiteli; Marie', 'Po czesku wołacza używa się zawsze, także z imionami.'),
    ('form', 'Typowe trudności', 'Mianownik po „być”', 't_m3', 'Jsem student.; Je učitel.; Je Polka.; Jsi lékař.; To je pes.; Jsme přátelé.', 'Po polsku narzędnik, po czesku zwykle mianownik.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['Dziś uczę się po czesku.', 'Dałem mu książkę.', 'Wczoraj go widziałem.', 'Chcę się z tobą spotkać.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: krótkie słowa na 2. miejscu', 't_s0', 'Dnes se učím česky.|Dnes učím se česky.|Se dnes učím česky.|Dnes učím česky se.; Dal jsem mu knihu.|Dal mu jsem knihu.|Jsem mu dal knihu.|Dal jsem knihu mu.; Včera jsem ho viděl.|Včera ho jsem viděl.|Včera viděl jsem ho.|Jsem ho včera viděl.; Chci se s tebou setkat.|Chci setkat se s tebou.|Se chci s tebou setkat.|Chci s tebou se setkat.', 'Krótkie słowa (se, si, jsem, ho, mu) stoją na drugim miejscu zdania, w kolejności: jsem, potem se/si, potem mu/ho. Na początku zdania stać nie mogą.'),
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
ENDINGS_PL = {'můj bratr': 'mój brat', 'moje sestra': 'moja siostra', 'jsem z Polska': 'Jestem z Polski.'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'dobrý (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'dobrý; lepší; nejlepší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'velký (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'velký; větší; největší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'malý (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'malý; menší; nejmenší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'špatný (zły)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'špatný; horší; nejhorší', 'Nieregularne.'),
    ('form', 'Stopniowanie', 'vysoký (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'vysoký; vyšší; nejvyšší', None),
    ('form', 'Stopniowanie', 'krásný (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'krásný; krásnější; nejkrásnější', 'Regularne: -ější.'),
    ('form', 'Stopniowanie', 'starý (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'starý; starší; nejstarší', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 2 (generowane) ===
PARADIGMS += [
    ('form', 'Czas przeszły', 'být: minulý čas', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'byl jsem; byla jsem; byl; byla; byli jsme; byli', 'W 3. osobie nie ma „jsem, jsi”: on byl, ona byla.'),
    ('form', 'Czas przeszły', 'dělat: minulý čas', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'dělal jsem; dělala jsem; dělal; dělala; dělali jsme; dělali', None),
    ('form', 'Czas przeszły', 'mít: minulý čas', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'měl jsem; měla jsem; měl; měla; měli jsme; měli', None),
    ('form', 'Czas przeszły', 'jít: minulý čas', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'šel jsem; šla jsem; šel; šla; šli jsme; šli', None),
    ('conj', 'Czas przyszły', 'dělat: budoucí čas', ['já', 'ty', 'on / ona', 'my', 'vy', 'oni'], 'budu dělat; budeš dělat; bude dělat; budeme dělat; budete dělat; budou dělat', None),
    ('form', 'Tryb warunkowy', 'být: kondicionál', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'byl bych; byla bych; byl by; byla by; byli bychom; byli by', None),
    ('form', 'Tryb warunkowy', 'chtít: kondicionál', ['já (m.)', 'já (ż.)', 'on', 'ona', 'my (m.)', 'oni (m.)'], 'chtěl bych; chtěla bych; chtěl by; chtěla by; chtěli bychom; chtěli by', 'Grzeczna prośba: Chtěl bych kávu.'),
    ('conj', 'Czasowniki nieregularne', 'moct (móc)', ['já', 'ty', 'on / ona', 'my', 'vy', 'oni'], 'můžu; můžeš; může; můžeme; můžete; můžou', None),
    ('conj', 'Czasowniki nieregularne', 'muset (musieć)', ['já', 'ty', 'on / ona', 'my', 'vy', 'oni'], 'musím; musíš; musí; musíme; musíte; musí', None),
    ('form', 'Vid (aspekt)', 'vid: robić', ['nedokonavý', 'dokonavý'], 'dělat; udělat', 'Podobnie jak po polsku: dokonavý opisuje zakończony wynik.'),
    ('form', 'Vid (aspekt)', 'vid: pisać', ['nedokonavý', 'dokonavý'], 'psát; napsat', None),
    ('form', 'Vid (aspekt)', 'vid: czytać', ['nedokonavý', 'dokonavý'], 'číst; přečíst', None),
    ('form', 'Vid (aspekt)', 'vid: kupować', ['nedokonavý', 'dokonavý'], 'kupovat; koupit', None),
    ('form', 'Vid (aspekt)', 'vid: dawać', ['nedokonavý', 'dokonavý'], 'dávat; dát', None),
    ('form', 'Vid (aspekt)', 'vid: widzieć', ['nedokonavý', 'dokonavý'], 'vidět; uvidět', None),
    ('form', 'Vid (aspekt)', 'vid: otwierać', ['nedokonavý', 'dokonavý'], 'otevírat; otevřít', None),
    ('form', 'Vid (aspekt)', 'vid: jeść', ['nedokonavý', 'dokonavý'], 'jíst; sníst', None),
    ('form', 'Vid (aspekt)', 'vid: pić', ['nedokonavý', 'dokonavý'], 'pít; vypít', None),
    ('form', 'Vid (aspekt)', 'vid: mówić, powiedzieć', ['nedokonavý', 'dokonavý'], 'říkat; říct', None),
    ('form', 'Vid (aspekt)', 'vid: brać', ['nedokonavý', 'dokonavý'], 'brát; vzít', None),
    ('form', 'Vid (aspekt)', 'vid: zaczynać', ['nedokonavý', 'dokonavý'], 'začínat; začít', None),
    ('form', 'Typowe trudności', 'Przyimek: jaki przypadek?', ['Jdu do ___ (škola)', 'Jsem ve ___ (škola)', 'Jdu ke ___ (kamarád)', 'Jedu s ___ (kamarád)', 'Mluvím o ___ (kamarád)', 'Vidím ___ (kamarád)'], 'školy; škole; kamarádovi; kamarádem; kamarádovi; kamaráda', 'Po polsku podobnie: do + dopełniacz, w + miejscownik, k + celownik, s + narzędnik.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 2 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('chlapec', 'chłopiec', None, 'rodzaj męski'), ('holčička', 'dziewczynka', None, 'rodzaj żeński'), ('člověk', 'człowiek', None, 'rodzaj męski'), ('lidé', 'ludzie', None, None), ('rodina', 'rodzina', None, 'rodzaj żeński'), ('syn', 'syn', None, 'rodzaj męski'), ('dcera', 'córka', None, 'rodzaj żeński'), ('děda', 'dziadek', None, 'rodzaj męski'), ('babička', 'babcia', None, 'rodzaj żeński'), ('vnuk', 'wnuk', None, 'rodzaj męski'), ('strýc', 'wujek', None, 'rodzaj męski'), ('teta', 'ciocia', None, 'rodzaj żeński'), ('bratranec', 'kuzyn', None, 'rodzaj męski'), ('manžel', 'mąż', None, 'rodzaj męski'), ('manželka', 'żona', None, 'rodzaj żeński'), ('soused', 'sąsiad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('host', 'gość', None, 'rodzaj męski'), ('šéf', 'szef', None, 'rodzaj męski'), ('kolega', 'kolega', None, 'rodzaj męski'), ('nepřítel', 'wróg', None, 'rodzaj męski'), ('král', 'król', None, 'rodzaj męski'), ('královna', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('hlava', 'głowa', None, 'rodzaj żeński'), ('obličej', 'twarz', None, 'rodzaj męski'), ('oko', 'oko', None, 'rodzaj nijaki'), ('ucho', 'ucho', None, 'rodzaj nijaki'), ('nos', 'nos', None, 'rodzaj męski'), ('ústa', 'usta', None, None), ('zub', 'ząb', None, 'rodzaj męski'), ('jazyk', 'język (narząd)', None, 'rodzaj męski'), ('vlasy', 'włosy', None, None), ('krk', 'szyja', None, 'rodzaj męski'), ('rameno', 'ramię', None, 'rodzaj nijaki'), ('ruka', 'ręka', None, 'rodzaj żeński'), ('prst', 'palec', None, 'rodzaj męski'), ('noha', 'noga', None, 'rodzaj żeński'), ('chodidlo', 'stopa', None, 'rodzaj nijaki'), ('koleno', 'kolano', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('záda', 'plecy', None, None), ('břicho', 'brzuch', None, 'rodzaj nijaki'), ('srdce', 'serce', None, 'rodzaj nijaki'), ('krev', 'krew', None, 'rodzaj żeński'), ('kost', 'kość', None, 'rodzaj żeński'), ('kůže', 'skóra', None, 'rodzaj żeński'), ('hlas', 'głos', None, 'rodzaj męski'), ('tělo', 'ciało', None, 'rodzaj nijaki'), ('žaludek', 'żołądek', None, 'rodzaj męski'), ('brada', 'broda', None, 'rodzaj żeński'), ('ret', 'warga', None, 'rodzaj męski'), ('nehet', 'paznokieć', None, 'rodzaj męski'), ('hruď', 'pierś', None, 'rodzaj żeński'), ('mozek', 'mózg', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('máslo', 'masło', None, 'rodzaj nijaki'), ('vejce', 'jajko', None, 'rodzaj nijaki'), ('maso', 'mięso', None, 'rodzaj nijaki'), ('kuře', 'kurczak', None, 'rodzaj nijaki'), ('vepřové', 'wieprzowina', None, 'rodzaj nijaki'), ('polévka', 'zupa', None, 'rodzaj żeński'), ('salát', 'sałatka', None, 'rodzaj męski'), ('rýže', 'ryż', None, 'rodzaj żeński'), ('těstoviny', 'makaron', None, None), ('brambor', 'ziemniak', None, 'rodzaj męski'), ('mrkev', 'marchewka', None, 'rodzaj żeński'), ('cibule', 'cebula', None, 'rodzaj żeński'), ('česnek', 'czosnek', None, 'rodzaj męski'), ('rajče', 'pomidor', None, 'rodzaj nijaki'), ('okurka', 'ogórek', None, 'rodzaj żeński'), ('hruška', 'gruszka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('banán', 'banan', None, 'rodzaj męski'), ('pomeranč', 'pomarańcza', None, 'rodzaj męski'), ('citron', 'cytryna', None, 'rodzaj męski'), ('jahoda', 'truskawka', None, 'rodzaj żeński'), ('hrozen', 'winogrono', None, 'rodzaj męski'), ('cukr', 'cukier', None, 'rodzaj męski'), ('sůl', 'sól', None, 'rodzaj żeński'), ('pepř', 'pieprz', None, 'rodzaj męski'), ('olej', 'olej', None, 'rodzaj męski'), ('mouka', 'mąka', None, 'rodzaj żeński'), ('med', 'miód', None, 'rodzaj męski'), ('čokoláda', 'czekolada', None, 'rodzaj żeński'), ('zmrzlina', 'lody', None, 'rodzaj żeński'), ('dort', 'ciasto (tort)', None, 'rodzaj męski'), ('sušenka', 'ciastko', None, 'rodzaj żeński'), ('snídaně', 'śniadanie', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('oběd', 'obiad', None, 'rodzaj męski'), ('večeře', 'kolacja', None, 'rodzaj żeński'), ('svačina', 'przekąska', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('šťáva', 'sok', None, 'rodzaj żeński'), ('pivo', 'piwo', None, 'rodzaj nijaki'), ('víno', 'wino', None, 'rodzaj nijaki'), ('nápoj', 'napój', None, 'rodzaj męski'), ('sklenice', 'szklanka', None, 'rodzaj żeński'), ('šálek', 'filiżanka', None, 'rodzaj męski'), ('talíř', 'talerz', None, 'rodzaj męski'), ('nůž', 'nóż', None, 'rodzaj męski'), ('vidlička', 'widelec', None, 'rodzaj żeński'), ('lžíce', 'łyżka', None, 'rodzaj żeński'), ('láhev', 'butelka', None, 'rodzaj żeński'), ('jídelní lístek', 'menu', None, 'rodzaj męski'), ('účet', 'rachunek', None, 'rodzaj męski'), ('spropitné', 'napiwek', None, 'rodzaj nijaki'), ('stůl (w restauracji)', 'stolik', None, 'rodzaj męski'), ('číšník', 'kelner', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('kuchař', 'kucharz', None, 'rodzaj męski'), ('hladový', 'głodny', None, None), ('žíznivý', 'spragniony', None, None), ('chutný', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('byt', 'mieszkanie', None, 'rodzaj męski'), ('pokoj', 'pokój', None, 'rodzaj męski'), ('kuchyně', 'kuchnia', None, 'rodzaj żeński'), ('koupelna', 'łazienka', None, 'rodzaj żeński'), ('ložnice', 'sypialnia', None, 'rodzaj żeński'), ('obývák', 'salon', None, 'rodzaj męski'), ('zahrada', 'ogród', None, 'rodzaj żeński'), ('dveře', 'drzwi', None, None), ('okno', 'okno', None, 'rodzaj nijaki'), ('zeď', 'ściana', None, 'rodzaj żeński'), ('podlaha', 'podłoga', None, 'rodzaj żeński'), ('střecha', 'dach', None, 'rodzaj żeński'), ('schody', 'schody', None, None), ('klíč', 'klucz', None, 'rodzaj męski'), ('stůl', 'stół', None, 'rodzaj męski'), ('židle', 'krzesło', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('postel', 'łóżko', None, 'rodzaj żeński'), ('skříň', 'szafa', None, 'rodzaj żeński'), ('lampa', 'lampa', None, 'rodzaj żeński'), ('koberec', 'dywan', None, 'rodzaj męski'), ('zrcadlo', 'lustro', None, 'rodzaj nijaki'), ('televize', 'telewizor', None, 'rodzaj żeński'), ('telefon', 'telefon', None, 'rodzaj męski'), ('počítač', 'komputer', None, 'rodzaj męski'), ('hodiny', 'zegar', None, None), ('polštář', 'poduszka', None, 'rodzaj męski'), ('přikrývka', 'koc', None, 'rodzaj żeński'), ('ručník', 'ręcznik', None, 'rodzaj męski'), ('mýdlo', 'mydło', None, 'rodzaj nijaki'), ('zubní kartáček', 'szczoteczka do zębów', None, 'rodzaj męski'), ('lednička', 'lodówka', None, 'rodzaj żeński'), ('kamna', 'piec', None, None)], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('pračka', 'pralka', None, 'rodzaj żeński'), ('odpadky', 'śmieci', None, None)], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('oblečení', 'ubranie', None, 'rodzaj nijaki'), ('košile', 'koszula', None, 'rodzaj żeński'), ('kalhoty', 'spodnie', None, None), ('šaty', 'sukienka', None, None), ('sukně', 'spódnica', None, 'rodzaj żeński'), ('bunda', 'kurtka', None, 'rodzaj żeński'), ('kabát', 'płaszcz', None, 'rodzaj męski'), ('svetr', 'sweter', None, 'rodzaj męski'), ('boty', 'buty', None, None), ('ponožky', 'skarpetki', None, None), ('čepice', 'czapka', None, 'rodzaj żeński'), ('klobouk', 'kapelusz', None, 'rodzaj męski'), ('rukavice', 'rękawiczki', None, None), ('šála', 'szalik', None, 'rodzaj żeński'), ('taška', 'torba', None, 'rodzaj żeński'), ('batoh', 'plecak', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('peněženka', 'portfel', None, 'rodzaj żeński'), ('brýle', 'okulary', None, None), ('hodinky', 'zegarek', None, None), ('prsten', 'pierścionek', None, 'rodzaj męski'), ('prádlo', 'bielizna', None, 'rodzaj nijaki'), ('pyžamo', 'piżama', None, 'rodzaj nijaki'), ('opasek', 'pasek', None, 'rodzaj męski'), ('kravata', 'krawat', None, 'rodzaj żeński'), ('oblek', 'garnitur', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('červený', 'czerwony', None, None), ('modrý', 'niebieski', None, None), ('zelený', 'zielony', None, None), ('žlutý', 'żółty', None, None), ('černý', 'czarny', None, None), ('bílý', 'biały', None, None), ('šedý', 'szary', None, None), ('hnědý', 'brązowy', None, None), ('růžový', 'różowy', None, None), ('fialový', 'fioletowy', None, None), ('barva', 'kolor', None, 'rodzaj żeński'), ('kulatý', 'okrągły', None, None), ('čtvercový', 'kwadratowy', None, None), ('rovný', 'prosty', None, None), ('křivý', 'krzywy', None, None), ('čára', 'linia', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('bod', 'punkt', None, 'rodzaj męski'), ('kruh', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('nula', 'zero', None, None), ('jedenáct', 'jedenaście', None, None), ('dvanáct', 'dwanaście', None, None), ('třináct', 'trzynaście', None, None), ('čtrnáct', 'czternaście', None, None), ('patnáct', 'piętnaście', None, None), ('šestnáct', 'szesnaście', None, None), ('sedmnáct', 'siedemnaście', None, None), ('osmnáct', 'osiemnaście', None, None), ('devatenáct', 'dziewiętnaście', None, None), ('dvacet', 'dwadzieścia', None, None), ('třicet', 'trzydzieści', None, None), ('čtyřicet', 'czterdzieści', None, None), ('padesát', 'pięćdziesiąt', None, None), ('šedesát', 'sześćdziesiąt', None, None), ('sedmdesát', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('osmdesát', 'osiemdziesiąt', None, None), ('devadesát', 'dziewięćdziesiąt', None, None), ('sto', 'sto', None, None), ('tisíc', 'tysiąc', None, None), ('milion', 'milion', None, None), ('první', 'pierwszy', None, None), ('druhý', 'drugi', None, None), ('třetí', 'trzeci', None, None), ('polovina', 'połowa', None, 'rodzaj żeński'), ('pár', 'para', None, 'rodzaj męski'), ('několik', 'kilka', None, None), ('mnoho', 'wiele', None, None), ('málo', 'mało', None, None), ('celý', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('sekunda', 'sekunda', None, 'rodzaj żeński'), ('minuta', 'minuta', None, 'rodzaj żeński'), ('hodina', 'godzina', None, 'rodzaj żeński'), ('týden', 'tydzień', None, 'rodzaj męski'), ('měsíc', 'miesiąc', None, 'rodzaj męski'), ('rok', 'rok', None, 'rodzaj męski'), ('jaro', 'wiosna', None, 'rodzaj nijaki'), ('léto', 'lato', None, 'rodzaj nijaki'), ('podzim', 'jesień', None, 'rodzaj męski'), ('zima', 'zima', None, 'rodzaj żeński'), ('pondělí', 'poniedziałek', None, 'rodzaj nijaki'), ('úterý', 'wtorek', None, 'rodzaj nijaki'), ('středa', 'środa', None, 'rodzaj żeński'), ('čtvrtek', 'czwartek', None, 'rodzaj męski'), ('pátek', 'piątek', None, 'rodzaj męski'), ('sobota', 'sobota', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('neděle', 'niedziela', None, 'rodzaj żeński'), ('leden', 'styczeń', None, 'rodzaj męski'), ('únor', 'luty', None, 'rodzaj męski'), ('březen', 'marzec', None, 'rodzaj męski'), ('duben', 'kwiecień', None, 'rodzaj męski'), ('květen', 'maj', None, 'rodzaj męski'), ('červen', 'czerwiec', None, 'rodzaj męski'), ('červenec', 'lipiec', None, 'rodzaj męski'), ('srpen', 'sierpień', None, 'rodzaj męski'), ('září', 'wrzesień', None, 'rodzaj nijaki'), ('říjen', 'październik', None, 'rodzaj męski'), ('listopad', 'listopad', None, 'rodzaj męski'), ('prosinec', 'grudzień', None, 'rodzaj męski'), ('ráno', 'rano (pora dnia)', None, 'rodzaj nijaki'), ('poledne', 'południe', None, 'rodzaj nijaki'), ('večer', 'wieczorem', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('vždy', 'zawsze', None, None), ('nikdy', 'nigdy', None, None), ('někdy', 'czasem', None, None), ('často', 'często', None, None), ('už', 'już', None, None), ('ještě', 'jeszcze', None, None), ('brzy', 'wkrótce', None, None), ('později', 'później', None, None), ('brzo', 'wcześnie', None, None), ('pozdě', 'późno', None, None), ('kdy', 'kiedy (pytanie)', None, None), ('datum', 'data', None, 'rodzaj nijaki'), ('minulost', 'przeszłość', None, 'rodzaj żeński'), ('budoucnost', 'przyszłość', None, 'rodzaj żeński'), ('narozeniny', 'urodziny', None, None), ('svátek', 'święto', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('prázdniny', 'wakacje', None, None)], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('slunce', 'słońce', None, 'rodzaj nijaki'), ('měsíc (ciało niebieskie)', 'księżyc', None, 'rodzaj męski'), ('hvězda', 'gwiazda', None, 'rodzaj żeński'), ('nebe', 'niebo', None, 'rodzaj nijaki'), ('mrak', 'chmura', None, 'rodzaj męski'), ('déšť', 'deszcz', None, 'rodzaj męski'), ('sníh', 'śnieg', None, 'rodzaj męski'), ('vítr', 'wiatr', None, 'rodzaj męski'), ('bouřka', 'burza', None, 'rodzaj żeński'), ('mlha', 'mgła', None, 'rodzaj żeński'), ('led', 'lód', None, 'rodzaj męski'), ('oheň', 'ogień', None, None), ('země', 'grunt)', None, 'rodzaj żeński'), ('řeka', 'rzeka', None, 'rodzaj żeński'), ('jezero', 'jezioro', None, 'rodzaj nijaki'), ('hora', 'góra', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('les', 'las', None, 'rodzaj męski'), ('strom', 'drzewo', None, 'rodzaj męski'), ('květina', 'kwiat', None, 'rodzaj żeński'), ('tráva', 'trawa', None, 'rodzaj żeński'), ('list', 'liść', None, 'rodzaj męski'), ('pole', 'pole', None, 'rodzaj nijaki'), ('ostrov', 'wyspa', None, 'rodzaj męski'), ('pláž', 'plaża', None, 'rodzaj żeński'), ('poušť', 'pustynia', None, 'rodzaj żeński'), ('skála', 'skała', None, 'rodzaj żeński'), ('kámen', 'kamień', None, 'rodzaj męski'), ('počasí', 'pogoda', None, 'rodzaj nijaki'), ('teplota', 'temperatura', None, 'rodzaj żeński'), ('studený', 'zimny', None, None), ('teplý', 'ciepły', None, None), ('horký', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('pes', 'pies', None, 'rodzaj męski'), ('kočka', 'kot', None, 'rodzaj żeński'), ('kůň', 'koń', None, 'rodzaj męski'), ('kráva', 'krowa', None, 'rodzaj żeński'), ('prase', 'świnia', None, 'rodzaj nijaki'), ('ovce', 'owca', None, 'rodzaj żeński'), ('koza', 'koza', None, 'rodzaj żeński'), ('slepice', 'kura', None, 'rodzaj żeński'), ('kachna', 'kaczka', None, 'rodzaj żeński'), ('pták', 'ptak', None, 'rodzaj męski'), ('myš', 'mysz', None, 'rodzaj żeński'), ('potkan', 'szczur', None, 'rodzaj męski'), ('had', 'wąż', None, 'rodzaj męski'), ('žába', 'żaba', None, 'rodzaj żeński'), ('lev', 'lew', None, 'rodzaj męski'), ('tygr', 'tygrys', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('slon', 'słoń', None, 'rodzaj męski'), ('medvěd', 'niedźwiedź', None, 'rodzaj męski'), ('vlk', 'wilk', None, 'rodzaj męski'), ('liška', 'lis', None, 'rodzaj żeński'), ('zajíc', 'zając', None, 'rodzaj męski'), ('jelen', 'jeleń', None, 'rodzaj męski'), ('opice', 'małpa', None, 'rodzaj żeński'), ('motýl', 'motyl', None, 'rodzaj męski'), ('včela', 'pszczoła', None, 'rodzaj żeński'), ('moucha', 'mucha', None, 'rodzaj żeński'), ('pavouk', 'pająk', None, 'rodzaj męski'), ('zvíře', 'zwierzę', None, 'rodzaj nijaki'), ('hmyz', 'owad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('vesnice', 'wieś', None, 'rodzaj żeński'), ('cesta', 'droga', None, 'rodzaj żeński'), ('náměstí', 'plac', None, 'rodzaj nijaki'), ('most', 'most', None, 'rodzaj męski'), ('park', 'park', None, 'rodzaj męski'), ('obchod', 'sklep', None, 'rodzaj męski'), ('trh', 'targ', None, 'rodzaj męski'), ('supermarket', 'supermarket', None, 'rodzaj męski'), ('banka', 'bank', None, 'rodzaj żeński'), ('pošta', 'poczta', None, 'rodzaj żeński'), ('nemocnice', 'szpital', None, 'rodzaj żeński'), ('lékárna', 'apteka', None, 'rodzaj żeński'), ('univerzita', 'uniwersytet', None, 'rodzaj żeński'), ('knihovna', 'biblioteka', None, 'rodzaj żeński'), ('muzeum', 'muzeum', None, 'rodzaj nijaki'), ('kostel', 'kościół', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('restaurace', 'restauracja', None, 'rodzaj żeński'), ('kavárna', 'kawiarnia', None, 'rodzaj żeński'), ('letiště', 'lotnisko', None, 'rodzaj nijaki'), ('nádraží', 'dworzec', None, 'rodzaj nijaki'), ('zastávka', 'przystanek', None, 'rodzaj żeński'), ('kino', 'kino', None, 'rodzaj nijaki'), ('divadlo', 'teatr', None, 'rodzaj nijaki'), ('policie', 'policja', None, 'rodzaj żeński'), ('kancelář', 'biuro', None, 'rodzaj żeński'), ('továrna', 'fabryka', None, 'rodzaj żeński'), ('budova', 'budynek', None, 'rodzaj żeński'), ('věž', 'wieża', None, 'rodzaj żeński'), ('centrum', 'centrum', None, 'rodzaj nijaki'), ('adresa', 'adres', None, 'rodzaj żeński'), ('mapa', 'mapa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('auto', 'samochód', None, 'rodzaj nijaki'), ('autobus', 'autobus', None, 'rodzaj męski'), ('vlak', 'pociąg', None, 'rodzaj męski'), ('tramvaj', 'tramwaj', None, 'rodzaj żeński'), ('metro', 'metro', None, 'rodzaj nijaki'), ('letadlo', 'samolot', None, 'rodzaj nijaki'), ('loď', 'statek', None, 'rodzaj żeński'), ('kolo (rower)', 'rower', None, 'rodzaj nijaki'), ('motorka', 'motocykl', None, 'rodzaj żeński'), ('jízdenka', 'bilet', None, 'rodzaj żeński'), ('cesta (podróż)', 'podróż', None, 'rodzaj żeński'), ('výlet', 'wycieczka', None, 'rodzaj męski'), ('pas', 'paszport', None, 'rodzaj męski'), ('kufr', 'walizka', None, 'rodzaj męski'), ('benzín', 'benzyna', None, 'rodzaj męski'), ('parkoviště', 'parking', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('křižovatka', 'skrzyżowanie', None, 'rodzaj żeński'), ('semafor', 'światła', None, 'rodzaj męski'), ('řidičský průkaz', 'prawo jazdy', None, 'rodzaj męski'), ('řidič', 'kierowca', None, 'rodzaj męski'), ('cestující', 'pasażer', None, 'rodzaj męski'), ('vjezd', 'wjazd', None, 'rodzaj męski'), ('výjezd', 'wyjazd', None, 'rodzaj męski'), ('železnice', 'kolej', None, 'rodzaj żeński'), ('přístav', 'port', None, 'rodzaj męski'), ('hranice', 'granica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('práce', 'praca', None, 'rodzaj żeński'), ('povolání', 'zawód', None, 'rodzaj nijaki'), ('lékař', 'lekarz', None, 'rodzaj męski'), ('zdravotní sestra', 'pielęgniarka', None, 'rodzaj żeński'), ('žák', 'uczeń', None, 'rodzaj męski'), ('inženýr', 'inżynier', None, 'rodzaj męski'), ('právník', 'prawnik', None, 'rodzaj męski'), ('policista', 'policjant', None, 'rodzaj męski'), ('voják', 'żołnierz', None, 'rodzaj męski'), ('zemědělec', 'rolnik', None, 'rodzaj męski'), ('prodavač', 'sprzedawca', None, 'rodzaj męski'), ('pokladní', 'kasjer', None, 'rodzaj męski'), ('herec', 'aktor', None, 'rodzaj męski'), ('spisovatel', 'pisarz', None, 'rodzaj męski'), ('malíř', 'malarz', None, 'rodzaj męski'), ('hudebník', 'muzyk', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('umělec', 'artysta', None, 'rodzaj męski'), ('firma', 'firma', None, 'rodzaj żeński'), ('peníze', 'pieniądze', None, None), ('plat', 'pensja', None, 'rodzaj męski'), ('smlouva', 'umowa', None, 'rodzaj żeński'), ('schůzka', 'spotkanie', None, 'rodzaj żeński'), ('lekce', 'lekcja', None, 'rodzaj żeński'), ('zkouška', 'egzamin', None, 'rodzaj żeński'), ('známka', 'ocena', None, 'rodzaj żeński'), ('třída', 'klasa', None, 'rodzaj żeński'), ('kniha', 'książka', None, 'rodzaj żeński'), ('sešit', 'zeszyt', None, 'rodzaj męski'), ('propisovačka', 'długopis', None, 'rodzaj żeński'), ('tužka', 'ołówek', None, 'rodzaj żeński'), ('papír', 'papier', None, 'rodzaj męski'), ('tabule', 'tablica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('slovník', 'słownik', None, 'rodzaj męski'), ('otázka', 'pytanie', None, 'rodzaj żeński'), ('odpověď', 'odpowiedź', None, 'rodzaj żeński'), ('úkol', 'zadanie', None, 'rodzaj męski'), ('test', 'test', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('cena', 'cena', None, 'rodzaj żeński'), ('platební karta', 'karta (płatnicza)', None, 'rodzaj żeński'), ('hotovost', 'gotówka', None, 'rodzaj żeński'), ('mince', 'moneta', None, 'rodzaj żeński'), ('bankovka', 'banknot', None, 'rodzaj żeński'), ('drobné', 'reszta', None, None), ('sleva', 'zniżka', None, 'rodzaj żeński'), ('košík', 'koszyk', None, 'rodzaj męski'), ('účtenka', 'paragon', None, 'rodzaj żeński'), ('zboží', 'towar', None, 'rodzaj nijaki'), ('nákup', 'zakup', None, 'rodzaj męski'), ('prodej', 'sprzedaż', None, 'rodzaj męski'), ('hodnota', 'wartość', None, 'rodzaj żeński'), ('úvěr', 'kredyt', None, 'rodzaj męski'), ('dluh', 'dług', None, 'rodzaj męski'), ('daň', 'podatek', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('bohatství', 'bogactwo', None, 'rodzaj nijaki'), ('chudý', 'biedny', None, None), ('bohatý', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('zdraví', 'zdrowie', None, 'rodzaj nijaki'), ('nemoc', 'choroba', None, 'rodzaj żeński'), ('bolest', 'ból', None, 'rodzaj żeński'), ('horečka', 'gorączka', None, 'rodzaj żeński'), ('kašel', 'kaszel', None, 'rodzaj męski'), ('rýma', 'katar', None, 'rodzaj żeński'), ('lék', 'lekarstwo', None, 'rodzaj męski'), ('tableta', 'tabletka', None, 'rodzaj żeński'), ('operace', 'operacja', None, 'rodzaj żeński'), ('rána', 'rana', None, 'rodzaj żeński'), ('nehoda', 'wypadek', None, 'rodzaj żeński'), ('zdravý', 'zdrowy', None, None), ('nemocný', 'chory', None, None), ('unavený', 'zmęczony', None, None), ('ospalý', 'śpiący', None, None), ('silný', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('slabý', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('radost', 'radość', None, 'rodzaj żeński'), ('smutek', 'smutek', None, 'rodzaj męski'), ('strach', 'strach', None, 'rodzaj męski'), ('hněv', 'gniew', None, 'rodzaj męski'), ('láska', 'miłość', None, 'rodzaj żeński'), ('nenávist', 'nienawiść', None, 'rodzaj żeński'), ('naděje', 'nadzieja', None, 'rodzaj żeński'), ('sen (marzenie)', 'marzenie', None, 'rodzaj męski'), ('štěstí', 'szczęście', None, 'rodzaj nijaki'), ('stud', 'wstyd', None, 'rodzaj męski'), ('překvapení', 'zdziwienie', None, 'rodzaj nijaki'), ('zvědavost', 'ciekawość', None, 'rodzaj żeński'), ('trpělivost', 'cierpliwość', None, 'rodzaj żeński'), ('odvaha', 'odwaga', None, 'rodzaj żeński'), ('upřímný', 'szczery', None, None), ('milý', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('slušný', 'grzeczny', None, None), ('hloupý', 'głupi', None, None), ('moudrý', 'mądry', None, None), ('líný', 'leniwy', None, None), ('pracovitý', 'pracowity', None, None), ('zajímavý', 'ciekawy', None, None), ('nudný', 'nudny', None, None), ('veselý', 'wesoły', None, None), ('smutný', 'smutny', None, None), ('naštvaný', 'zły (rozgniewany)', None, None), ('šťastný', 'szczęśliwy', None, None), ('zamilovaný', 'zakochany', None, None), ('osamělý', 'samotny', None, None), ('klidný', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('velký', 'duży', None, None), ('dlouhý', 'długi', None, None), ('krátký', 'krótki', None, None), ('vysoký', 'wysoki', None, None), ('nízký', 'niski', None, None), ('široký', 'szeroki', None, None), ('úzký', 'wąski', None, None), ('tlustý', 'gruby', None, None), ('hubený', 'chudy', None, None), ('těžký', 'ciężki', None, None), ('lehký', 'lekki', None, None), ('rychlý', 'szybki', None, None), ('pomalý', 'wolny', None, None), ('tvrdý', 'twardy', None, None), ('měkký', 'miękki', None, None), ('mokrý', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('suchý', 'suchy', None, None), ('čistý', 'czysty', None, None), ('špinavý', 'brudny', None, None), ('plný', 'pełny', None, None), ('prázdný', 'pusty', None, None), ('ostrý', 'ostry', None, None), ('hlučný', 'głośny', None, None), ('tichý', 'cichy', None, None), ('světlý', 'jasny', None, None), ('tmavý', 'ciemny', None, None), ('mladý', 'młody', None, None), ('starý', 'stary', None, None), ('nový', 'nowy', None, None), ('špatný', 'zły (niedobry)', None, None), ('hezký', 'ładny', None, None), ('ošklivý', 'brzydki', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('snadný', 'łatwy', None, None), ('obtížný', 'trudny', None, None), ('důležitý', 'ważny', None, None), ('možný', 'możliwy', None, None), ('pravdivý', 'prawdziwy', None, None), ('falešný', 'fałszywy', None, None), ('drahý', 'drogi', None, None), ('levný', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('být', 'być', None, None), ('mít', 'mieć', None, None), ('dělat', 'robić', None, None), ('jít', 'iść', None, None), ('jet', 'jechać', None, None), ('přijít', 'przyjść', None, None), ('vyjít', 'wyjść', None, None), ('vejít', 'wejść', None, None), ('vrátit se', 'wrócić', None, None), ('běžet', 'biec', None, None), ('stát', 'stać', None, None), ('sedět', 'siedzieć', None, None), ('ležet', 'leżeć', None, None), ('spát', 'spać', None, None), ('vstát', 'wstać', None, None), ('jíst', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('pít', 'pić', None, None), ('vařit', 'gotować', None, None), ('mýt', 'myć', None, None), ('oblékat se', 'ubierać się', None, None), ('mluvit', 'mówić', None, None), ('říct', 'powiedzieć', None, None), ('ptát se', 'pytać', None, None), ('odpovídat', 'odpowiadać', None, None), ('slyšet', 'słyszeć', None, None), ('poslouchat', 'słuchać', None, None), ('vidět', 'widzieć', None, None), ('dívat se', 'patrzeć', None, None), ('číst', 'czytać', None, None), ('psát', 'pisać', None, None), ('učit se', 'uczyć się', None, None), ('učit', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('rozumět', 'rozumieć', None, None), ('vědět', 'wiedzieć', None, None), ('znát', 'znać', None, None), ('myslet', 'myśleć', None, None), ('pamatovat', 'pamiętać', None, None), ('zapomínat', 'zapominać', None, None), ('chtít', 'chcieć', None, None), ('mít rád', 'lubić', None, None), ('milovat', 'kochać', None, None), ('potřebovat', 'potrzebować', None, None), ('moci', 'móc', None, None), ('muset', 'musieć', None, None), ('dávat', 'dawać', None, None), ('brát', 'brać', None, None), ('kupovat', 'kupować', None, None), ('prodávat', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('platit', 'płacić', None, None), ('otevírat', 'otwierać', None, None), ('zavírat', 'zamykać', None, None), ('začínat', 'zaczynać', None, None), ('končit', 'kończyć', None, None), ('pracovat', 'pracować', None, None), ('hrát', 'grać', None, None), ('zpívat', 'śpiewać', None, None), ('tančit', 'tańczyć', None, None), ('plavat', 'pływać', None, None), ('létat', 'latać', None, None), ('klást', 'kłaść', None, None), ('hledat', 'szukać', None, None), ('nacházet', 'znajdować', None, None), ('čekat', 'czekać', None, None), ('pomáhat', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('prosit', 'prosić', None, None), ('omlouvat se', 'przepraszać', None, None), ('povolovat', 'pozwalać', None, None), ('zkoušet', 'próbować', None, None), ('měnit', 'zmieniać', None, None), ('nosit', 'nosić', None, None), ('držet', 'trzymać', None, None), ('házet', 'rzucać', None, None), ('chytat', 'łapać', None, None), ('bít', 'bić', None, None), ('zabíjet', 'zabijać', None, None), ('umírat', 'umierać', None, None), ('žít', 'żyć', None, None), ('bydlet', 'mieszkać', None, None), ('potkávat', 'spotykać', None, None), ('volat', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('posílat', 'wysyłać', None, None), ('dostávat', 'dostawać', None, None), ('ukazovat', 'pokazywać', None, None), ('zvát', 'zapraszać', None, None), ('navštěvovat', 'odwiedzać', None, None), ('plakat', 'płakać', None, None), ('smát se', 'śmiać się', None, None), ('usmívat se', 'uśmiechać się', None, None), ('bát se', 'bać się', None, None), ('radovat se', 'cieszyć się', None, None), ('věřit', 'wierzyć', None, None), ('souhlasit', 'zgadzać się', None, None), ('vybírat', 'wybierać', None, None), ('rozhodovat', 'decydować', None, None), ('počítat', 'liczyć', None, None), ('vážit', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('chodit', 'chodzić', None, None), ('jezdit', 'jeździć', None, None), ('nastupovat', 'wsiadać', None, None), ('vystupovat', 'wysiadać', None, None), ('zatáčet', 'skręcać', None, None), ('zastavovat', 'zatrzymywać się', None, None), ('zpožďovat se', 'spóźniać się', None, None), ('spěchat', 'spieszyć się', None, None), ('odpočívat', 'odpoczywać', None, None), ('bavit se', 'bawić się', None, None), ('kreslit', 'rysować', None, None), ('stavět', 'budować', None, None), ('opravovat', 'naprawiać', None, None), ('řezat', 'ciąć', None, None), ('smažit', 'smażyć', None, None), ('péct', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('míchat', 'mieszać', None, None), ('nalévat', 'nalewać', None, None), ('uklízet', 'sprzątać', None, None), ('prát', 'prać', None, None), ('žehlit', 'prasować', None, None), ('holit se', 'golić się', None, None), ('česat', 'czesać', None, None), ('koupat se', 'kąpać się', None, None), ('probouzet se', 'budzić się', None, None), ('usínat', 'zasypiać', None, None), ('snít', 'marzyć', None, None), ('zdát se', 'śnić', None, None), ('cvičit', 'ćwiczyć', None, None), ('trénovat', 'trenować', None, None), ('vyhrávat', 'wygrywać', None, None), ('prohrávat', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('hýbat', 'ruszać', None, None), ('táhnout', 'ciągnąć', None, None), ('tlačit', 'pchać', None, None), ('zvedat', 'podnosić', None, None), ('padat', 'spadać', None, None), ('skákat', 'skakać', None, None), ('lézt', 'wspinać się', None, None), ('schovávat', 'ukrywać', None, None), ('krást', 'kraść', None, None), ('vracet', 'oddawać', None, None), ('půjčovat', 'pożyczać', None, None), ('utrácet', 'wydawać', None, None), ('šetřit', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('ten', 'ten', None, None), ('tamten', 'tamten', None, None), ('jak', 'jak', None, None), ('proč', 'dlaczego', None, None), ('co', 'co', None, None), ('kdo', 'kto', None, None), ('který', 'który', None, None), ('jaký', 'jaki', None, None), ('ale', 'ale', None, None), ('nebo', 'lub', None, None), ('protože', 'bo', None, None), ('jestli', 'jeśli', None, None), ('že', 'że', None, None), ('tedy', 'więc', None, None), ('také', 'też', None, None), ('jen', 'tylko', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('trochu', 'trochę', None, None), ('hodně', 'dużo', None, None), ('všechno', 'wszystko', None, None), ('nic', 'nic', None, None), ('něco', 'coś', None, None), ('někdo', 'ktoś', None, None), ('nikdo', 'nikt', None, None), ('každý', 'każdy', None, None), ('jiný', 'inny', None, None), ('stejný', 'ten sam', None, None), ('možná', 'może (być)', None, None), ('určitě', 'na pewno', None, None), ('společně', 'razem', None, None), ('sám', 'sam', None, None), ('bez', 'bez', None, None), ('s', 'z (towarzysząc)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('v', 'w (miejsce)', None, None), ('od', 'od', None, None), ('pro', 'dla', None, None), ('přes', 'przez', None, None), ('po', 'po (czas)', None, None), ('před', 'przed', None, None), ('za', 'za (z tyłu)', None, None), ('nad', 'nad', None, None), ('pod', 'pod', None, None), ('vedle', 'obok', None, None), ('mezi', 'między', None, None), ('proti', 'przeciw', None, None), ('o', 'o (temat)', None, None), ('u', 'u (przy)', None, None), ('kolem', 'około', None, None), ('skoro', 'prawie', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('dokonce', 'nawet', None, None), ('ještě jednou', 'jeszcze raz', None, None), ('tehdy', 'wtedy', None, None), ('někde', 'gdzieś', None, None), ('nikde', 'nigdzie', None, None), ('všude', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('život', 'życie', None, 'rodzaj męski'), ('smrt', 'śmierć', None, 'rodzaj żeński'), ('svět', 'świat', None, 'rodzaj męski'), ('země (kraj)', 'kraj', None, 'rodzaj żeński'), ('řeč', 'język (mowa)', None, 'rodzaj żeński'), ('slovo', 'słowo', None, 'rodzaj nijaki'), ('věta', 'zdanie', None, 'rodzaj żeński'), ('jméno', 'imię', None, 'rodzaj nijaki'), ('příjmení', 'nazwisko', None, 'rodzaj nijaki'), ('věk', 'wiek', None, 'rodzaj męski'), ('historie', 'historia', None, 'rodzaj żeński'), ('kultura', 'kultura', None, 'rodzaj żeński'), ('náboženství', 'religia', None, 'rodzaj nijaki'), ('Bůh', 'Bóg', None, 'rodzaj męski'), ('válka', 'wojna', None, 'rodzaj żeński'), ('mír', 'pokój (brak wojny)', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('zákon', 'prawo (przepis)', None, 'rodzaj męski'), ('svoboda', 'wolność', None, 'rodzaj żeński'), ('moc (władza)', 'władza', None, 'rodzaj żeński'), ('vláda', 'rząd', None, 'rodzaj żeński'), ('volby', 'wybory', None, None), ('problém', 'problem', None, 'rodzaj męski'), ('nápad', 'pomysł', None, 'rodzaj męski'), ('důvod', 'powód', None, 'rodzaj męski'), ('výsledek', 'wynik', None, 'rodzaj męski'), ('způsob', 'sposób', None, 'rodzaj męski'), ('začátek', 'początek', None, 'rodzaj męski'), ('konec', 'koniec', None, 'rodzaj męski'), ('část', 'część', None, 'rodzaj żeński'), ('místo', 'miejsce', None, 'rodzaj nijaki'), ('věc', 'rzecz', None, 'rodzaj żeński'), ('záležitost', 'sprawa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('informace', 'informacja', None, 'rodzaj żeński'), ('zpráva', 'wiadomość', None, 'rodzaj żeński'), ('dopis', 'list', None, 'rodzaj męski'), ('noviny', 'gazeta', None, None), ('film', 'film', None, 'rodzaj męski'), ('hudba', 'muzyka', None, 'rodzaj żeński'), ('písnička', 'piosenka', None, 'rodzaj żeński'), ('obraz', 'obraz', None, 'rodzaj męski'), ('hra', 'gra', None, 'rodzaj żeński'), ('sport', 'sport', None, 'rodzaj męski'), ('zápas', 'mecz', None, 'rodzaj męski'), ('tým', 'drużyna', None, 'rodzaj męski'), ('míč', 'piłka', None, 'rodzaj męski'), ('zábava', 'zabawa', None, 'rodzaj żeński'), ('oslava', 'impreza', None, 'rodzaj żeński'), ('dárek', 'prezent', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('sen', 'sen', None, 'rodzaj męski'), ('plán', 'plan', None, 'rodzaj męski'), ('výběr', 'wybór', None, 'rodzaj męski'), ('chyba', 'błąd', None, 'rodzaj żeński'), ('pravda', 'prawda', None, 'rodzaj żeński'), ('lež', 'kłamstwo', None, 'rodzaj żeński'), ('tajemství', 'tajemnica', None, 'rodzaj nijaki'), ('síla', 'siła', None, 'rodzaj żeński'), ('energie', 'energia', None, 'rodzaj żeński'), ('světlo', 'światło', None, 'rodzaj nijaki'), ('zvuk', 'dźwięk', None, 'rodzaj męski'), ('ticho', 'cisza', None, 'rodzaj nijaki'), ('pohyb', 'ruch', None, 'rodzaj męski'), ('změna', 'zmiana', None, 'rodzaj żeński'), ('rozdíl', 'różnica', None, 'rodzaj męski'), ('příklad', 'przykład', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('celek', 'całość', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, 'rodzaj męski'), ('e-mail', 'e-mail', None, 'rodzaj męski'), ('heslo', 'hasło', None, 'rodzaj nijaki'), ('webová stránka', 'strona internetowa', None, 'rodzaj żeński'), ('program', 'program', None, 'rodzaj męski'), ('aplikace', 'aplikacja', None, 'rodzaj żeński'), ('obrazovka', 'ekran', None, 'rodzaj żeński'), ('klávesnice', 'klawiatura', None, 'rodzaj żeński'), ('počítačová myš', 'myszka komputerowa', None, 'rodzaj żeński'), ('soubor', 'plik', None, 'rodzaj męski'), ('fotka', 'zdjęcie', None, 'rodzaj żeński'), ('kamera', 'kamera', None, 'rodzaj żeński'), ('baterie', 'bateria', None, 'rodzaj żeński'), ('elektřina', 'prąd', None, 'rodzaj żeński'), ('kabel', 'kabel', None, 'rodzaj męski'), ('stroj', 'maszyna', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('nástroj', 'narzędzie', None, 'rodzaj męski'), ('kladivo', 'młotek', None, 'rodzaj nijaki'), ('tiskárna', 'drukarka', None, 'rodzaj żeński'), ('nabíječka', 'ładowarka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('sever', 'północ', None, 'rodzaj męski'), ('jih', 'południe (kierunek)', None, 'rodzaj męski'), ('východ', 'wschód', None, 'rodzaj męski'), ('západ', 'zachód', None, 'rodzaj męski'), ('Polsko', 'Polska', None, 'rodzaj nijaki'), ('Evropa', 'Europa', None, 'rodzaj żeński'), ('Německo', 'Niemcy', None, 'rodzaj nijaki'), ('Francie', 'Francja', None, 'rodzaj żeński'), ('Itálie', 'Włochy', None, 'rodzaj żeński'), ('Španělsko', 'Hiszpania', None, 'rodzaj nijaki'), ('Rusko', 'Rosja', None, 'rodzaj nijaki'), ('Anglie', 'Anglia', None, 'rodzaj żeński'), ('Amerika', 'Ameryka', None, 'rodzaj żeński'), ('Čína', 'Chiny', None, 'rodzaj żeński'), ('Japonsko', 'Japonia', None, 'rodzaj nijaki'), ('Afrika', 'Afryka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('Asie', 'Azja', None, 'rodzaj żeński'), ('kontinent', 'kontynent', None, 'rodzaj męski'), ('hlavní město', 'stolica', None, 'rodzaj nijaki'), ('občan', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('kus', 'kawałek', None, 'rodzaj męski'), ('kapka', 'kropla', None, 'rodzaj żeński'), ('krabice', 'pudełko', None, 'rodzaj żeński'), ('pytel', 'worek', None, 'rodzaj męski'), ('nit', 'nić', None, 'rodzaj żeński'), ('drát', 'drut', None, 'rodzaj męski'), ('jehla', 'igła', None, 'rodzaj żeński'), ('nůžky', 'nożyczki', None, None), ('hůl', 'kij', None, 'rodzaj żeński'), ('lano', 'lina', None, 'rodzaj nijaki'), ('řetěz', 'łańcuch', None, 'rodzaj męski'), ('šroub', 'śruba', None, 'rodzaj męski'), ('hřebík', 'gwóźdź', None, 'rodzaj męski'), ('lepidlo', 'klej', None, 'rodzaj nijaki'), ('barva (farba)', 'farba', None, 'rodzaj żeński'), ('sklo', 'szkło', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('dřevo', 'drewno', None, 'rodzaj nijaki'), ('kov', 'metal', None, 'rodzaj męski'), ('zlato', 'złoto', None, 'rodzaj nijaki'), ('stříbro', 'srebro', None, 'rodzaj nijaki'), ('železo', 'żelazo', None, 'rodzaj nijaki'), ('plast', 'plastik', None, 'rodzaj męski'), ('kůže (materiał)', 'skóra (materiał)', None, 'rodzaj żeński'), ('bavlna', 'bawełna', None, 'rodzaj żeński'), ('vlna', 'wełna', None, 'rodzaj żeński'), ('písek', 'piasek', None, 'rodzaj męski'), ('bláto', 'błoto', None, 'rodzaj nijaki'), ('prach', 'kurz', None, 'rodzaj męski'), ('kouř', 'dym', None, 'rodzaj męski'), ('pára', 'para (wodna)', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('nahoře', 'góra (kierunek)', None, None), ('dole', 'dół', None, None), ('vpředu', 'przód', None, None), ('vzadu', 'tył', None, None), ('střed', 'środek', None, 'rodzaj męski'), ('bok', 'bok', None, 'rodzaj męski'), ('uvnitř', 'wewnątrz', None, None), ('venku', 'na zewnątrz', None, None), ('daleko', 'daleko', None, None), ('blízko', 'blisko', None, None), ('vysoko', 'wysoko', None, None), ('nízko', 'nisko', None, None), ('rychle', 'szybko', None, None), ('pomalu', 'wolno', None, None), ('špatně', 'źle', None, None), ('snadno', 'łatwo', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('těžko', 'trudno', None, None), ('zvlášť', 'osobno', None, None), ('naproti', 'naprzeciw', None, None), ('podél', 'wzdłuż', None, None), ('napříč', 'w poprzek', None, None), ('dokola', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('zelí', 'kapusta', None, 'rodzaj nijaki'), ('hrášek', 'groszek', None, 'rodzaj męski'), ('fazole', 'fasola', None, 'rodzaj żeński'), ('houba', 'grzyb', None, 'rodzaj żeński'), ('ořech', 'orzech', None, 'rodzaj męski'), ('švestka', 'śliwka', None, 'rodzaj żeński'), ('třešeň', 'wiśnia', None, 'rodzaj żeński'), ('broskev', 'brzoskwinia', None, 'rodzaj żeński'), ('meloun', 'arbuz', None, 'rodzaj męski'), ('malina', 'malina', None, 'rodzaj żeński'), ('klobása', 'kiełbasa', None, 'rodzaj żeński'), ('šunka', 'szynka', None, 'rodzaj żeński'), ('houska', 'bułka', None, 'rodzaj żeński'), ('sendvič', 'kanapka', None, 'rodzaj męski'), ('palačinka', 'naleśnik', None, 'rodzaj żeński'), ('jogurt', 'jogurt', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('smetana', 'śmietana', None, 'rodzaj żeński'), ('omáčka', 'sos', None, 'rodzaj żeński'), ('ocet', 'ocet', None, 'rodzaj męski'), ('droždí', 'drożdże', None, 'rodzaj nijaki'), ('rosol', 'kisiel', None, 'rodzaj męski'), ('želé', 'galaretka', None, 'rodzaj nijaki'), ('rozinka', 'rodzynek', None, 'rodzaj żeński'), ('mandle', 'migdał', None, 'rodzaj żeński'), ('petržel', 'pietruszka', None, 'rodzaj żeński'), ('kopr', 'koperek', None, 'rodzaj męski'), ('paprika', 'papryka', None, 'rodzaj żeński'), ('hlávkový salát', 'sałata', None, 'rodzaj męski'), ('špenát', 'szpinak', None, 'rodzaj męski'), ('červená řepa', 'burak', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('tchán', 'teść', None, 'rodzaj męski'), ('tchyně', 'teściowa', None, 'rodzaj żeński'), ('švagr', 'szwagier', None, 'rodzaj męski'), ('synovec', 'bratanek', None, 'rodzaj męski'), ('neteř', 'siostrzenica', None, 'rodzaj żeński'), ('sirotek', 'sierota', None, 'rodzaj męski'), ('vdova', 'wdowa', None, 'rodzaj żeński'), ('snoubenec', 'narzeczony', None, 'rodzaj męski'), ('svatba', 'ślub', None, 'rodzaj żeński'), ('rozvod', 'rozwód', None, 'rodzaj męski'), ('narození', 'urodzenie', None, 'rodzaj nijaki'), ('pohřeb', 'pogrzeb', None, 'rodzaj męski'), ('kadeřník', 'fryzjer', None, 'rodzaj męski'), ('pekař', 'piekarz', None, 'rodzaj męski'), ('řezník', 'rzeźnik', None, 'rodzaj męski'), ('servírka', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('listonoš', 'listonosz', None, 'rodzaj męski'), ('hasič', 'strażak', None, 'rodzaj męski'), ('soudce', 'sędzia', None, 'rodzaj męski'), ('ředitel', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
