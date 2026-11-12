"""Treść kursu: nowogrecki (dimotiki) dla Polaków.

Słowo:    (forma, znaczenie po polsku, polskie słowo pokrewne lub None, skojarzenie lub None, wymowa polskimi literami)
Litera:   (litera, nazwa i dźwięk, przykład)
Zdanie:   (lista słów, tłumaczenie, {pułapka: wyjaśnienie})
Końcówka: (przed, temat, końcówka, po, [opcje], podpowiedź po polsku, wyjaśnienie, id działu)

Wymowa zapisana polskimi literami: dh = [ð] jak angielskie th w „this”, th = [θ] jak w „think”,
gh = [ɣ] miękkie „g” (przed e, i: j), w = [v].
"""

PUNCT = {"!", ";", ":", "?", ".", ","}

TRACKS = {"alfabet": "ΑΛΦΑΒΗΤΟ · ALFABET", "jezyk": "ΓΛΩΣΣΑ · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Litery I", "icon": "Α", "track": "alfabet",
     "letters": [
         ("α", "alfa [a]: jak polskie a", "αγάπη (miłość)"),
         ("β", "wita [v]: jak polskie w", "βιβλίο (książka)"),
         ("γ", "gama [ɣ]: miękkie g; przed e, i brzmi jak j", "γάλα (mleko)"),
         ("δ", "delta [ð]: jak angielskie th w „this”", "δρόμος (droga)"),
         ("ε", "epsilon [e]: jak polskie e", "ένα (jeden)"),
         ("ζ", "zita [z]: jak polskie z", "ζωή (życie)"),
         ("η", "ita [i]: jak polskie i", "ήλιος (słońce)"),
         ("θ", "thita [θ]: jak angielskie th w „think”", "θάλασσα (morze)"),
     ]},
    {"id": "wymowa2", "title": "Litery II", "icon": "Ι", "track": "alfabet",
     "letters": [
         ("ι", "jota [i]: jak polskie i", "ίσως (może)"),
         ("κ", "kapa [k]: jak polskie k", "καλός (dobry)"),
         ("λ", "lamda [l]: jak polskie l", "λάθος (błąd)"),
         ("μ", "mi [m]: jak polskie m", "μητέρα (matka)"),
         ("ν", "ni [n]: jak polskie n", "νερό (woda)"),
         ("ξ", "ksi [ks]: jak polskie ks", "ξένος (obcy)"),
         ("ο", "omikron [o]: jak polskie o", "όχι (nie)"),
         ("π", "pi [p]: jak polskie p", "πατέρας (ojciec)"),
     ]},
    {"id": "wymowa3", "title": "Litery III", "icon": "Ρ", "track": "alfabet",
     "letters": [
         ("ρ", "ro [r]: dźwięczne r, jak polskie", "ρολόι (zegar)"),
         ("σ", "sigma [s]: jak polskie s (na końcu słowa ς)", "σπίτι (dom)"),
         ("τ", "taf [t]: jak polskie t", "τυρί (ser)"),
         ("υ", "ipsilon [i]: jak polskie i", "υπέροχος (wspaniały)"),
         ("φ", "fi [f]: jak polskie f", "φίλος (przyjaciel)"),
         ("χ", "chi [x]: jak polskie ch", "χαρά (radość)"),
         ("ψ", "psi [ps]: jak polskie ps", "ψωμί (chleb)"),
         ("ω", "omega [o]: jak polskie o (tak samo jak ο)", "ώρα (godzina)"),
     ]},
    {"id": "wymowa4", "title": "Dwuznaki", "icon": "ου", "track": "alfabet",
     "letters": [
         ("ει", "[i]: jak polskie i (tak samo jak η)", "είμαι (jestem)"),
         ("οι", "[i]: jak polskie i", "οι φίλοι (przyjaciele)"),
         ("αι", "[e]: jak polskie e", "και (i)"),
         ("ου", "[u]: jak polskie u", "ουρανός (niebo)"),
         ("μπ", "[b] na początku słowa; w środku [mb]", "μπάνιο (kąpiel)"),
         ("ντ", "[d] na początku słowa; w środku [nd]", "ντομάτα (pomidor)"),
         ("γκ", "[g] na początku słowa; w środku [ng]", "γκρι (szary)"),
         ("τσ", "[ts]: jak polskie c", "τσάι (herbata)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "Γ", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("γεια", "cześć (na powitanie i pożegnanie)", None, "Dosłownie „zdrowie”. Gdy ktoś kicha: γεια σου!"),
         ("καλημέρα", "dzień dobry (rano)", None, "Kali = dobra, mera = dzień."),
         ("καλησπέρα", "dobry wieczór", None, "Kali + spera („wieczór”)."),
         ("καληνύχτα", "dobranoc", None, "Kali + nichta („noc”)."),
         ("ευχαριστώ", "dziękuję", "Eucharystia (= dziękczynienie)", "Eucharystia to po grecku „dziękczynienie”!"),
         ("παρακαλώ", "proszę; nie ma za co", None, None),
         ("ναι", "tak", None, "Uwaga: ναι [ne] brzmi jak polskie „nie”, ale znaczy „tak”!"),
         ("όχι", "nie", None, None),
         ("συγγνώμη", "przepraszam", None, None),
         ("και", "i", None, "αι czyta się [e]: ke."),
         ("πολύ", "bardzo; dużo", "poli-", "Jak w „polimery” (wiele części)."),
         ("εντάξει", "w porządku, okej", None, "Najczęstsze „okej” po grecku."),
     ],
     "sentences": [
         (["γεια"], "Cześć!", {}),
         (["καλημέρα", "!"], "Dzień dobry!", {"καλησπέρα": "καλησπέρα to „dobry wieczór”. Rano: καλημέρα."}),
         (["ευχαριστώ", "πολύ"], "Dziękuję bardzo.", {"παρακαλώ": "παρακαλώ to „proszę”. Tu dziękujesz."}),
         (["ναι", ",", "εντάξει"], "Tak, w porządku.", {"όχι": "όχι to „nie”. ναι znaczy „tak”, choć brzmi „ne”."}),
         (["όχι", ",", "ευχαριστώ"], "Nie, dziękuję.", {"ναι": "ναι znaczy „tak”. Tu odmawiasz: όχι."}),
         (["συγγνώμη", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "Ε", "track": "jezyk",
     "words": [
         ("εγώ", "ja", "ego, egoista", None),
         ("εσύ", "ty", None, None),
         ("αυτός", "on", None, "αυ przed „t” czyta się [af]: aftos."),
         ("αυτή", "ona", None, None),
         ("είμαι", "jestem", None, None),
         ("είσαι", "jesteś", None, None),
         ("είναι", "jest; są", None, "Jedna forma na „on, ona, ono” i na „oni, one”."),
         ("Έλληνας", "Grek", "Hellada", None),
         ("Πολωνός", "Polak", "Polonia", None),
         ("φοιτητής", "student", None, None),
         ("δάσκαλος", "nauczyciel", None, None),
         ("από", "z; od", "apo-", "Jak w „apogeum”: daleko od Ziemi."),
         ("την", "(rodzajnik żeński w bierniku)", None, "Po „από” rodzajnik stoi w bierniku: από την Πολωνία."),
         ("Πολωνία", "Polska", "Polonia", None),
         ("Ελλάδα", "Grecja", "Hellada", None),
     ],
     "sentences": [
         (["εγώ", "είμαι", "φοιτητής"], "Jestem studentem.", {"είσαι": "είσαι to „jesteś”. O sobie: είμαι."}),
         (["εσύ", "είσαι", "δάσκαλος"], "Jesteś nauczycielem.", {"είμαι": "είμαι to „jestem”. Do „ty”: είσαι."}),
         (["αυτός", "είναι", "Έλληνας"], "On jest Grekiem.", {"είσαι": "είσαι to „jesteś”. O „on”: είναι."}),
         (["εγώ", "είμαι", "Πολωνός"], "Jestem Polakiem.", {}),
         (["είμαι", "από", "την", "Πολωνία"], "Jestem z Polski.", {"Ελλάδα": "Ελλάδα to Grecja. Z Polski: την Πολωνία."}),
         (["αυτή", "είναι", "από", "την", "Ελλάδα"], "Ona jest z Grecji.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "Μ", "track": "jezyk",
     "words": [
         ("ο", "(rodzajnik męski: ten)", None, "Grecy mówią „ten Nikos”: ο Νίκος."),
         ("η", "(rodzajnik żeński: ta)", None, "Nie mylić z literą η: też brzmi [i]."),
         ("το", "(rodzajnik nijaki: to)", None, None),
         ("άνθρωπος", "człowiek", "antropologia", None),
         ("μητέρα", "matka", "metropolia (miasto-matka)", None),
         ("πατέρας", "ojciec", "patriarcha, patron", None),
         ("παιδί", "dziecko", "pedagog (prowadzi dziecko)", None),
         ("παιδιά", "dzieci", None, "Liczba mnoga: -ιά."),
         ("φίλος", "przyjaciel", "filozof, filantrop", "Filos = miłujący: filozof miłuje mądrość."),
         ("γυναίκα", "kobieta; żona", "ginekolog", None),
         ("άντρας", "mężczyzna; mąż", "androgyniczny", None),
         ("αδελφός", "brat", "Filadelfia (miasto braterskiej miłości)", None),
         ("αδελφό", "brata (biernik)", None, "Po „mam” rzeczownik idzie w bierniku: bez końcowego -ς."),
         ("αδελφή", "siostra; siostrę", None, None),
         ("έχω", "mam", None, None),
         ("έχεις", "masz", None, None),
         ("μικρό", "małe", "mikroskop", None),
         ("καλό", "dobre", "kaligrafia", None),
     ],
     "sentences": [
         (["ο", "φίλος", "είναι", "άνθρωπος"], "Przyjaciel jest człowiekiem.", {"η": "φίλος jest męski, więc ο."}),
         (["η", "μητέρα", "είναι", "γυναίκα"], "Matka jest kobietą.", {"ο": "μητέρα jest żeńska, więc η."}),
         (["το", "παιδί", "είναι", "μικρό"], "Dziecko jest małe.", {"η": "παιδί jest nijakie, więc το."}),
         (["εγώ", "έχω", "αδελφό"], "Mam brata.", {"έχεις": "έχεις to „masz”. O sobie: έχω.", "αδελφός": "Po „mam” biernik: αδελφό, bez -ς."}),
         (["εσύ", "έχεις", "αδελφή"], "Masz siostrę.", {"έχω": "έχω to „mam”. Do „ty”: έχεις."}),
         (["ο", "πατέρας", "είναι", "άντρας"], "Ojciec jest mężczyzną.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "Ψ", "track": "jezyk",
     "words": [
         ("νερό", "woda", None, None),
         ("καφές", "kawa", "kawa (to samo słowo, przez turecki)", None),
         ("καφέ", "kawę (biernik)", None, "Biernik męski traci końcowe -ς."),
         ("τσάι", "herbata", None, "Rosyjskie czaj i polskie „czaj” mają to samo źródło."),
         ("ψωμί", "chleb", None, None),
         ("τυρί", "ser", None, None),
         ("κρασί", "wino", None, None),
         ("γάλα", "mleko", "galaktyka (Droga Mleczna)", "Galaktyka = „mleczna”: Droga Mleczna."),
         ("ψάρι", "ryba", None, None),
         ("μήλο", "jabłko", None, None),
         ("μήλα", "jabłka", None, None),
         ("θέλω", "chcę", None, None),
         ("θέλεις", "chcesz", None, None),
         ("ένα", "jeden; jakiś (nijaki)", None, None),
         ("λίγο", "trochę", None, None),
         ("τώρα", "teraz", None, None),
     ],
     "sentences": [
         (["θέλω", "ένα", "καφέ"], "Chcę kawę.", {"θέλεις": "θέλεις to „chcesz”. O sobie: θέλω.", "καφές": "Po „chcę” biernik: καφέ."}),
         (["θέλω", "νερό", ",", "παρακαλώ"], "Poproszę wodę.", {}),
         (["εσύ", "θέλεις", "τσάι"], "Chcesz herbatę.", {"θέλω": "θέλω to „chcę”. Do „ty”: θέλεις."}),
         (["θέλω", "λίγο", "ψωμί"], "Chcę trochę chleba.", {}),
         (["το", "ψάρι", "είναι", "πολύ", "καλό"], "Ryba jest bardzo dobra.", {}),
         (["θέλω", "τώρα", "μήλα"], "Chcę teraz jabłka.", {"μήλο": "Tu liczba mnoga: μήλα."}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("δύο", "dwa", "duet, dualizm", None),
         ("τρία", "trzy", "trio, triada", None),
         ("τέσσερα", "cztery", "tetrada, tetralogia", None),
         ("πέντε", "pięć", "pentagon, pentatlon", None),
         ("έξι", "sześć", "heksagon", None),
         ("δέκα", "dziesięć", "dekada, dekalog", None),
         ("σήμερα", "dziś", None, None),
         ("αύριο", "jutro", None, "αυ przed samogłoską: [av]: avrio."),
         ("χθες", "wczoraj", None, None),
         ("τι", "co; jaki", None, None),
         ("ώρα", "godzina; pora", "horoskop, zegar „hora”", "Horoskop = „obserwacja godziny”."),
     ],
     "sentences": [
         (["έχω", "δύο", "παιδιά"], "Mam dwoje dzieci.", {}),
         (["θέλω", "τρία", "μήλα"], "Chcę trzy jabłka.", {"δύο": "δύο to „dwa”. Chcesz trzy: τρία."}),
         (["τι", "ώρα", "είναι", ";"], "Która jest godzina?", {}),
         (["είναι", "δέκα"], "Jest dziesiąta.", {}),
         (["σήμερα", "θέλω", "καφέ"], "Dziś chcę kawę.", {"αύριο": "αύριο to „jutro”. Tu „dziś”: σήμερα."}),
         (["αύριο", "θέλω", "ψάρι"], "Jutro chcę rybę.", {"χθες": "χθες to „wczoraj”. Tu „jutro”: αύριο."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "Π", "track": "jezyk",
     "words": [
         ("σπίτι", "dom", None, None),
         ("πόλη", "miasto", "metropolia, policja", "Polis = miasto: polityka, policja, metropolia."),
         ("δρόμος", "droga; ulica", "hipodrom, aerodrom", None),
         ("σχολείο", "szkoła", "szkoła (to samo słowo!)", "Σχολείο i polska „szkoła” to jedno słowo."),
         ("θάλασσα", "morze", "talasoterapia", None),
         ("ταξί", "taksówka", "taksówka", None),
         ("ξενοδοχείο", "hotel", None, "Ξένος = obcy, gość: ksenofobia."),
         ("πού", "gdzie", None, None),
         ("εδώ", "tu", None, None),
         ("εκεί", "tam", None, None),
         ("πάω", "idę; jadę", None, None),
         ("στο", "do; w (nijaki i męski)", None, None),
         ("στην", "do; w (żeński)", None, None),
         ("δεξιά", "w prawo", None, None),
         ("αριστερά", "w lewo", None, None),
     ],
     "sentences": [
         (["πού", "είναι", "το", "ξενοδοχείο", ";"], "Gdzie jest hotel?", {"εδώ": "εδώ to „tu”, a pytasz „gdzie”: πού."}),
         (["το", "ξενοδοχείο", "είναι", "εκεί"], "Hotel jest tam.", {"εδώ": "εδώ to „tu”. Tu mówimy „tam”: εκεί."}),
         (["πάω", "στο", "σπίτι"], "Idę do domu.", {"στην": "σπίτι jest nijakie, więc στο."}),
         (["πάω", "στην", "πόλη"], "Jadę do miasta.", {"στο": "πόλη jest żeńskie, więc στην."}),
         (["το", "ταξί", "είναι", "δεξιά"], "Taksówka jest po prawej.", {"αριστερά": "αριστερά to „w lewo”."}),
         (["η", "θάλασσα", "είναι", "εκεί"], "Morze jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Trzy litery, jeden dźwięk", "chain": [],
                "text": "Po grecku [i] zapisuje się na pięć sposobów: η, ι, υ, ει, οι. To pozostałość dawnej wymowy. Nie szukaj w tym logiki: zapamiętuj słowa razem z pisownią."}],
    "wymowa4": [{"title": "Przed dźwięcznymi się dźwięczy", "chain": [],
                 "text": "Grecy nie mają osobnych liter na [b], [d], [g], więc piszą μπ, ντ, γκ. Na początku słowa czytasz je jako b, d, g; w środku często jak mb, nd, ng."}],
    "ja": [{"title": "Czasownik zawiera osobę", "chain": [
                ("Jestem studentem.", ["εγώ", "είμαι", "φοιτητής"], "Do „ja” pasuje końcówka -μαι."),
                ("Jesteś nauczycielem.", ["εσύ", "είσαι", "δάσκαλος"], "Do „ty” pasuje -σαι."),
            ],
            "text": "Po grecku końcówka mówi, kto działa: είμαι (ja), είσαι (ty), είναι (on, ona, ono). Zaimek εγώ, εσύ można więc często pominąć: „είμαι φοιτητής”."}],
    "ludzie": [{"title": "Trzy rodzaje, trzy rodzajniki", "chain": [],
                "text": "Każdy rzeczownik ma rodzaj: męski (ο), żeński (η) lub nijaki (το). Najczęściej poznasz go po końcówce: -ος, -ας to męski; -α, -η to żeński; -ο, -ι, -μα to nijaki. Uczysz się więc słowa razem z rodzajnikiem."}],
    "jedzenie": [{"title": "Biernik gubi -ς", "chain": [],
                  "text": "Po „chcę”, „mam” i „widzę” rzeczownik stoi w bierniku. U rzeczowników męskich oznacza to utratę końcowego -ς: ο καφές → θέλω καφέ, ο αδελφός → έχω αδελφό."}],
}

ENDINGS_INSIGHT = {"title": "Końcówki i rodzajniki",
                   "text": "Po grecku końcówki mówią, kto działa (-ω, -εις, -ει) i jaki jest rodzaj (ο, η, το). Tu ćwiczysz właśnie to."}

ENDINGS = [
    ("", "καλη", "μέρα", "", ["μέρα", "σπέρα", "νύχτα"], "dzień dobry (rano)", "μέρα to „dzień”, σπέρα „wieczór”, νύχτα „noc”.", "slowa"),
    ("", "καλη", "σπέρα", "", ["μέρα", "σπέρα", "νύχτα"], "dobry wieczór", "σπέρα to „wieczór”.", "slowa"),
    ("", "καλη", "νύχτα", "", ["μέρα", "σπέρα", "νύχτα"], "dobranoc", "νύχτα to „noc”.", "slowa"),
    ("εγώ ", "", "είμαι", " φοιτητής", ["είμαι", "είσαι", "είναι"], "ja jestem", "Do „εγώ” pasuje είμαι.", "ja"),
    ("εσύ ", "", "είσαι", " δάσκαλος", ["είμαι", "είσαι", "είναι"], "ty jesteś", "Do „εσύ” pasuje είσαι.", "ja"),
    ("αυτός ", "", "είναι", " Έλληνας", ["είμαι", "είσαι", "είναι"], "on jest", "Do „αυτός” pasuje είναι.", "ja"),
    ("", "", "ο", " άντρας", ["ο", "η", "το"], "ten mężczyzna", "άντρας jest męski: ο.", "ludzie"),
    ("", "", "η", " γυναίκα", ["ο", "η", "το"], "ta kobieta", "γυναίκα jest żeńska: η.", "ludzie"),
    ("", "", "το", " παιδί", ["ο", "η", "το"], "to dziecko", "παιδί jest nijakie: το.", "ludzie"),
    ("εγώ ", "έχ", "ω", " αδελφό", ["ω", "εις", "ει"], "ja mam", "Do „ja” pasuje -ω.", "ludzie"),
    ("εσύ ", "έχ", "εις", " αδελφή", ["ω", "εις", "ει"], "ty masz", "Do „ty” pasuje -εις.", "ludzie"),
    ("εγώ ", "θέλ", "ω", " καφέ", ["ω", "εις", "ει"], "ja chcę", "Do „ja” pasuje -ω.", "jedzenie"),
    ("εσύ ", "θέλ", "εις", " τσάι", ["ω", "εις", "ει"], "ty chcesz", "Do „ty” pasuje -εις.", "jedzenie"),
    ("πάω ", "", "στο", " σπίτι", ["στο", "στην"], "do domu", "σπίτι jest nijakie: στο.", "miejsca"),
    ("πάω ", "", "στην", " πόλη", ["στο", "στην"], "do miasta", "πόλη jest żeńskie: στην.", "miejsca"),
]

CHAT_EXTRA = {"Νίκος": "Nikos (imię)", "Μαρία": "Maria (imię)", "πάς": "idziesz; jedziesz", "Γιώργος": "Giorgos (imię)",
              "λέγομαι": "nazywam się", "τηλέφωνο": "telefon"}

CHATS = [
    {"id": "kafeneio", "title": "W kafenejo", "partner": "Μαρία", "avatar": "Μ", "requires": "jedzenie",
     "turns": [
         {"bot": ["καλημέρα", "!"], "en": "Dzień dobry!",
          "options": [(["καλημέρα", "!"], True, None), (["καληνύχτα", "!"], False, "καληνύχτα to „dobranoc”. Jest rano!")]},
         {"bot": ["θέλεις", "καφέ", ";"], "en": "Chcesz kawę?",
          "options": [(["ναι", ",", "θέλω", "καφέ"], True, None),
                      (["ναι", ",", "θέλεις", "καφέ"], False, "θέλεις to „chcesz”. O sobie: θέλω.")]},
         {"bot": ["και", "ψωμί", ";"], "en": "I chleb?",
          "options": [(["όχι", ",", "ευχαριστώ"], True, None),
                      (["παρακαλώ", "!"], False, "παρακαλώ to „proszę”; pytają, czy chcesz chleb. Odmów: όχι, ευχαριστώ.")]},
         {"bot": ["εντάξει", "!"], "build": (["ευχαριστώ", "πολύ"], "Dziękuję bardzo."), "en": "W porządku!"},
     ]},
    {"id": "gnorimia", "title": "Poznajemy się", "partner": "Νίκος", "avatar": "Ν", "requires": "ludzie",
     "turns": [
         {"bot": ["γεια", "!"], "en": "Cześć!",
          "options": [(["γεια", "!"], True, None), (["συγγνώμη", "!"], False, "συγγνώμη to „przepraszam”. Powitaj: γεια.")]},
         {"bot": ["είσαι", "από", "την", "Ελλάδα", ";"], "en": "Jesteś z Grecji?",
          "options": [(["όχι", ",", "είμαι", "από", "την", "Πολωνία"], True, None),
                      (["όχι", ",", "είσαι", "από", "την", "Πολωνία"], False, "είσαι to „jesteś”. O sobie: είμαι.")]},
         {"bot": ["έχεις", "αδελφό", ";"], "en": "Masz brata?",
          "options": [(["ναι", ",", "έχω", "αδελφό"], True, None),
                      (["ναι", ",", "έχεις", "αδελφό"], False, "έχεις to „masz”. O sobie: έχω.")]},
         {"bot": ["καλησπέρα", "!"], "build": (["καλησπέρα"], "Dobry wieczór."), "en": "Dobry wieczór!"},
     ]},
    {"id": "taxi", "title": "W taksówce", "partner": "Γιώργος", "avatar": "Γ", "requires": "miejsca",
     "turns": [
         {"bot": ["καλησπέρα", "!"], "en": "Dobry wieczór!",
          "options": [(["καλησπέρα", "!"], True, None), (["καλημέρα", "!"], False, "καλημέρα to „dzień dobry” (rano). Jest wieczór.")]},
         {"bot": ["πού", "πάς", ";"], "en": "Dokąd jedziesz?",
          "options": [(["πάω", "στο", "ξενοδοχείο"], True, None),
                      (["πάω", "στην", "ξενοδοχείο"], False, "ξενοδοχείο jest nijakie: στο, nie στην.")]},
         {"bot": ["εντάξει", ".", "το", "ξενοδοχείο", "είναι", "εκεί", "."], "en": "W porządku. Hotel jest tam.",
          "options": [(["δεξιά", ";"], True, None), (["εδώ", ";"], False, "Tam, nie tu: pytasz o kierunek, więc δεξιά ;")]},
         {"bot": ["ναι", "!"], "build": (["ευχαριστώ", "πολύ"], "Dziękuję bardzo."), "en": "Tak!"},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['εγώ', 'εσύ', 'αυτός/αυτή', 'εμείς', 'εσείς', 'αυτοί/αυτές'],
    'przyp': ['mianownik lp.', 'dopełniacz lp.', 'biernik lp.', 'mianownik lm.', 'dopełniacz lm.', 'biernik lm.'],
    'pp': ['γράφω (piszę)', 'κλείνω (zamykam)', 'ανοίγω (otwieram)', 'κουράζω (męczę)', 'παντρεύω (żenię)'],
    't_art': ['φίλος (przyjaciel)', 'μητέρα (matka)', 'παιδί (dziecko)', 'βιβλίο (książka)', 'άντρας (mężczyzna)', 'θάλασσα (morze)', 'νερό (woda)', 'πατέρας (ojciec)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'θέλω (chcę)', 'os', 'θέλω; θέλεις; θέλει; θέλουμε; θέλετε; θέλουν', 'Typ A: -ω, -εις, -ει, -ουμε, -ετε, -ουν.'),
    ('conj', 'Wzory koniugacji', 'έχω (mam)', 'os', 'έχω; έχεις; έχει; έχουμε; έχετε; έχουν', None),
    ('conj', 'Wzory koniugacji', 'μιλάω (mówię)', 'os', 'μιλάω; μιλάς; μιλάει; μιλάμε; μιλάτε; μιλάνε', 'Typ B1: akcent na końcówce, -άω, -άς, -άει.'),
    ('conj', 'Wzory koniugacji', 'μπορώ (mogę)', 'os', 'μπορώ; μπορείς; μπορεί; μπορούμε; μπορείτε; μπορούν', 'Typ B2: -ώ, -είς, -εί, -ούμε, -είτε, -ούν.'),
    ('conj', 'Czasowniki nieregularne', 'είμαι (jestem)', 'os', 'είμαι; είσαι; είναι; είμαστε; είστε; είναι', None),
    ('conj', 'Czasowniki nieregularne', 'πάω (idę)', 'os', 'πάω; πας; πάει; πάμε; πάτε; πάνε', None),
    ('conj', 'Czasowniki nieregularne', 'λέω (mówię)', 'os', 'λέω; λες; λέει; λέμε; λέτε; λένε', None),
    ('conj', 'Czasowniki nieregularne', 'τρώω (jem)', 'os', 'τρώω; τρως; τρώει; τρώμε; τρώτε; τρώνε', None),
    ('decl', 'Wzory deklinacji', 'ο φίλος (przyjaciel)', 'przyp', 'ο φίλος; του φίλου; τον φίλο; οι φίλοι; των φίλων; τους φίλους', 'Męskie na -ος.'),
    ('decl', 'Wzory deklinacji', 'ο άντρας (mężczyzna)', 'przyp', 'ο άντρας; του άντρα; τον άντρα; οι άντρες; των αντρών; τους άντρες', 'Męskie na -ας: w dopełniaczu i bierniku lp. znika -ς.'),
    ('decl', 'Wzory deklinacji', 'η μητέρα (matka)', 'przyp', 'η μητέρα; της μητέρας; τη μητέρα; οι μητέρες; των μητέρων; τις μητέρες', 'Żeńskie na -α.'),
    ('decl', 'Wzory deklinacji', 'το βιβλίο (książka)', 'przyp', 'το βιβλίο; του βιβλίου; το βιβλίο; τα βιβλία; των βιβλίων; τα βιβλία', 'Nijakie na -ο.'),
    ('decl', 'Wzory deklinacji', 'το παιδί (dziecko)', 'przyp', 'το παιδί; του παιδιού; το παιδί; τα παιδιά; των παιδιών; τα παιδιά', 'Nijakie na -ι.'),
    ('form', 'Imiesłowy', 'Imiesłów bierny na -μένος', 'pp', 'γραμμένος; κλεισμένος; ανοιγμένος; κουρασμένος; παντρεμένος', 'Odmienia się jak przymiotnik: -μένος, -μένη, -μένο.'),
    ('conj', 'Czas przeszły', 'είμαι: czas przeszły', 'os', 'ήμουν; ήσουν; ήταν; ήμασταν; ήσασταν; ήταν', None),
    ('conj', 'Czas przeszły', 'έχω: czas przeszły', 'os', 'είχα; είχες; είχε; είχαμε; είχατε; είχαν', None),
    ('conj', 'Czas przeszły', 'κάνω (robię): aoryst', 'os', 'έκανα; έκανες; έκανε; κάναμε; κάνατε; έκαναν', 'Akcent na trzeciej sylabie od końca; gdy jej brak, dochodzi ε- (augment).'),
    ('conj', 'Czas przeszły', 'μιλάω: aoryst', 'os', 'μίλησα; μίλησες; μίλησε; μιλήσαμε; μιλήσατε; μίλησαν', None),
    ('conj', 'Czas przyszły', 'πάω: czas przyszły', 'os', 'θα πάω; θα πας; θα πάει; θα πάμε; θα πάτε; θα πάνε', 'θα + forma czasownika.'),
    ('form', 'Typowe trudności', 'Rodzajnik: ο, η czy το?', 't_art', 'ο; η; το; το; ο; η; το; ο', '-ος i -ας zwykle męskie, -α i -η żeńskie, -ο, -ι, -μα nijakie.'),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['πότε', 'ποτέ', 'γέρος', 'γερός', 'νόμος', 'νομός'],
    't_m1': ['ο φίλος', 'η μητέρα', 'το παιδί', 'οι φίλοι', 'οι μητέρες', 'τα παιδιά'],
    't_m2': ['ει', 'οι', 'η', 'υ', 'αι', 'ου', 'μπ', 'ντ'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Akcent odróżnia słowa', 't_m0', 'kiedy; nigdy; starzec; krzepki; prawo; prefektura', 'Akcent jest zawsze zapisany i tylko tam pada nacisk.'),
    ('form', 'Typowe trudności', 'Biernik po „widzę”', 't_m1', 'τον φίλο; τη μητέρα; το παιδί; τους φίλους; τις μητέρες; τα παιδιά', 'W bierniku rodzaju męskiego znika końcowe -ς, a rodzajnik zmienia się w τον.'),
    ('form', 'Typowe trudności', 'Jak to się czyta? (zapisy dźwięku i, e)', 't_m2', 'i; i (jak οι); i (jak η); i (jak υ); e; u; b; d', 'Pięć zapisów czyta się [i]. Dźwięki b i d zapisuje się dwiema literami.'),
]
