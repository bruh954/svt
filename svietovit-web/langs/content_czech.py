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
