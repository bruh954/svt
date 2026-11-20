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

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'εγώ (ja)', ['mianownik', 'dopełniacz', 'biernik'], 'εγώ; μου; με', None),
    ('decl', 'Zaimki', 'εσύ (ty)', ['mianownik', 'dopełniacz', 'biernik'], 'εσύ; σου; σε', None),
    ('decl', 'Zaimki', 'αυτός (on)', ['mianownik', 'dopełniacz', 'biernik'], 'αυτός; αυτού; αυτόν', 'Krótkie formy: του, τον.'),
    ('decl', 'Zaimki', 'αυτή (ona)', ['mianownik', 'dopełniacz', 'biernik'], 'αυτή; αυτής; αυτήν', 'Krótkie formy: της, την.'),
    ('decl', 'Zaimki', 'αυτό (ono)', ['mianownik', 'dopełniacz', 'biernik'], 'αυτό; αυτού; αυτό', None),
    ('decl', 'Zaimki', 'εμείς (my)', ['mianownik', 'dopełniacz', 'biernik'], 'εμείς; μας; μας', None),
    ('decl', 'Zaimki', 'εσείς (wy)', ['mianownik', 'dopełniacz', 'biernik'], 'εσείς; σας; σας', None),
    ('decl', 'Zaimki', 'αυτοί (oni)', ['mianownik', 'dopełniacz', 'biernik'], 'αυτοί; αυτών; αυτούς', 'Krótkie formy: τους, τους.'),
    ('decl', 'Zaimki', 'αυτές (one)', ['mianownik', 'dopełniacz', 'biernik'], 'αυτές; αυτών; αυτές', None),
    ('decl', 'Zaimki', 'μου, σου, του… (krótkie formy dopełniacza)', 'os', 'μου; σου; του, της; μας; σας; τους', 'Znaczą też „mój, twój”: το σπίτι μου.'),
    ('decl', 'Zaimki', 'ποιος (kto)', ['mianownik', 'dopełniacz', 'biernik'], 'ποιος; ποιου; ποιον', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'εγώ θέλω καφέ': 'Chcę kawę.'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'καλός (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'καλός; καλύτερος; ο καλύτερος', 'Najwyższy: rodzajnik + stopień wyższy.'),
    ('form', 'Stopniowanie', 'μεγάλος (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'μεγάλος; μεγαλύτερος; ο μεγαλύτερος', None),
    ('form', 'Stopniowanie', 'μικρός (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'μικρός; μικρότερος; ο μικρότερος', None),
    ('form', 'Stopniowanie', 'όμορφος (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'όμορφος; ομορφότερος; ο ομορφότερος', None),
    ('form', 'Stopniowanie', 'παλιός (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'παλιός; παλιότερος; ο παλιότερος', None),
    ('form', 'Stopniowanie', 'ψηλός (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'ψηλός; ψηλότερος; ο ψηλότερος', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 2 (generowane) ===
PARADIGMS += [
    ('conj', 'Czas przeszły', 'πηγαίνω: αόριστος (poszedłem)', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'πήγα; πήγες; πήγε; πήγαμε; πήγατε; πήγαν', None),
    ('conj', 'Czas przeszły', 'λέω: αόριστος (powiedziałem)', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'είπα; είπες; είπε; είπαμε; είπατε; είπαν', None),
    ('conj', 'Czas przeszły', 'τρώω: αόριστος (zjadłem)', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'έφαγα; έφαγες; έφαγε; φάγαμε; φάγατε; έφαγαν', None),
    ('conj', 'Czas przeszły', 'μιλώ: παρατατικός (mówiłem, trwało)', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'μιλούσα; μιλούσες; μιλούσε; μιλούσαμε; μιλούσατε; μιλούσαν', 'Aoryst: czynność zakończona. Paratatikos: czynność trwała lub się powtarzała.'),
    ('conj', 'Czas przyszły', 'μιλώ: μέλλοντας (będę mówić)', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'θα μιλήσω; θα μιλήσεις; θα μιλήσει; θα μιλήσουμε; θα μιλήσετε; θα μιλήσουν', 'Przyszłość = θα + forma teraźniejsza lub dokonana.'),
    ('conj', 'Czas przyszły', 'είμαι: μέλλοντας', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'θα είμαι; θα είσαι; θα είναι; θα είμαστε; θα είστε; θα είναι', None),
    ('conj', 'Strona bierna i dopełniająca', 'έρχομαι (przychodzić): strona bierna', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'έρχομαι; έρχεσαι; έρχεται; ερχόμαστε; έρχεστε; έρχονται', 'Wiele greckich czasowników występuje tylko w formie na -μαι, choć znaczą czynność.'),
    ('conj', 'Strona bierna i dopełniająca', 'κάθομαι (siedzieć)', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'κάθομαι; κάθεσαι; κάθεται; καθόμαστε; κάθεστε; κάθονται', None),
    ('conj', 'Strona bierna i dopełniająca', 'σκέφτομαι (myśleć)', ['εγώ', 'εσύ', 'αυτός / αυτή', 'εμείς', 'εσείς', 'αυτοί'], 'σκέφτομαι; σκέφτεσαι; σκέφτεται; σκεφτόμαστε; σκέφτεστε; σκέφτονται', None),
    ('form', 'Rodzajniki', 'rodzajnik określony: mianownik', ['r. męski l. poj.', 'r. żeński l. poj.', 'r. nijaki l. poj.', 'r. męski l. mn.', 'r. żeński l. mn.', 'r. nijaki l. mn.'], 'ο; η; το; οι; οι; τα', None),
    ('form', 'Rodzajniki', 'rodzajnik określony: biernik', ['r. męski l. poj.', 'r. żeński l. poj.', 'r. nijaki l. poj.', 'r. męski l. mn.', 'r. żeński l. mn.', 'r. nijaki l. mn.'], 'τον; την; το; τους; τις; τα', None),
    ('form', 'Rodzajniki', 'rodzajnik określony: dopełniacz', ['r. męski l. poj.', 'r. żeński l. poj.', 'r. nijaki l. poj.', 'r. męski l. mn.', 'r. żeński l. mn.', 'r. nijaki l. mn.'], 'του; της; του; των; των; των', None),
    ('form', 'Rodzajniki', 'rodzajnik nieokreślony', ['r. męski', 'r. żeński', 'r. nijaki'], 'ένας; μία; ένα', None),
    ('form', 'Przymiotniki i liczebniki', 'νέος (nowy, młody)', ['r. męski', 'r. żeński', 'r. nijaki'], 'νέος; νέα; νέο', None),
    ('form', 'Przymiotniki i liczebniki', 'ωραίος (piękny)', ['r. męski', 'r. żeński', 'r. nijaki'], 'ωραίος; ωραία; ωραίο', None),
    ('form', 'Przymiotniki i liczebniki', 'πολύς (dużo)', ['r. męski', 'r. żeński', 'r. nijaki'], 'πολύς; πολλή; πολύ', None),
    ('form', 'Przymiotniki i liczebniki', 'τρεις (trzy)', ['r. męski', 'r. żeński', 'r. nijaki'], 'τρεις; τρεις; τρία', None),
    ('form', 'Zaimki', 'zaimek dzierżawczy (słaby): μου, σου…', ['mój', 'twój', 'jego', 'jej', 'nasz', 'wasz'], 'μου; σου; του; της; μας; σας', 'Stoi po rzeczowniku: το σπίτι μου.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 2 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('άνδρας', 'mężczyzna', None, 'rodzaj męski'), ('αγόρι', 'chłopiec', None, 'rodzaj nijaki'), ('κορίτσι', 'dziewczynka', None, 'rodzaj nijaki'), ('άνθρωποι', 'ludzie', None, None), ('οικογένεια', 'rodzina', None, 'rodzaj żeński'), ('γιος', 'syn', None, 'rodzaj męski'), ('κόρη', 'córka', None, 'rodzaj żeński'), ('παππούς', 'dziadek', None, 'rodzaj męski'), ('γιαγιά', 'babcia', None, 'rodzaj żeński'), ('εγγονός', 'wnuk', None, 'rodzaj męski'), ('θείος', 'wujek', None, 'rodzaj męski'), ('θεία', 'ciocia', None, 'rodzaj żeński'), ('ξάδελφος', 'kuzyn', None, 'rodzaj męski'), ('σύζυγος', 'mąż', None, 'rodzaj męski'), ('σύζυγος (żona)', 'żona', None, 'rodzaj żeński'), ('γείτονας', 'sąsiad', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('επισκέπτης', 'gość', None, 'rodzaj męski'), ('αφεντικό', 'szef', None, 'rodzaj nijaki'), ('συνάδελφος', 'kolega', None, 'rodzaj męski'), ('εχθρός', 'wróg', None, 'rodzaj męski'), ('βασιλιάς', 'król', None, 'rodzaj męski'), ('βασίλισσα', 'królowa', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('κεφάλι', 'głowa', None, 'rodzaj nijaki'), ('πρόσωπο', 'twarz', None, 'rodzaj nijaki'), ('μάτι', 'oko', None, 'rodzaj nijaki'), ('αυτί', 'ucho', None, 'rodzaj nijaki'), ('μύτη', 'nos', None, 'rodzaj żeński'), ('στόμα', 'usta', None, 'rodzaj nijaki'), ('δόντι', 'ząb', None, 'rodzaj nijaki'), ('γλώσσα (narząd)', 'język (narząd)', None, 'rodzaj żeński'), ('μαλλιά', 'włosy', None, None), ('λαιμός', 'szyja', None, 'rodzaj męski'), ('ώμος', 'ramię', None, 'rodzaj męski'), ('χέρι', 'ręka', None, 'rodzaj nijaki'), ('δάχτυλο', 'palec', None, 'rodzaj nijaki'), ('πόδι', 'noga', None, 'rodzaj nijaki'), ('πατούσα', 'stopa', None, 'rodzaj żeński'), ('γόνατο', 'kolano', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('πλάτη', 'plecy', None, 'rodzaj żeński'), ('κοιλιά', 'brzuch', None, 'rodzaj żeński'), ('καρδιά', 'serce', None, 'rodzaj żeński'), ('αίμα', 'krew', None, 'rodzaj nijaki'), ('κόκαλο', 'kość', None, 'rodzaj nijaki'), ('δέρμα', 'skóra', None, 'rodzaj nijaki'), ('φωνή', 'głos', None, 'rodzaj żeński'), ('σώμα', 'ciało', None, 'rodzaj nijaki'), ('στομάχι', 'żołądek', None, 'rodzaj nijaki'), ('γένια', 'broda', None, None), ('χείλος', 'warga', None, 'rodzaj nijaki'), ('νύχι', 'paznokieć', None, 'rodzaj nijaki'), ('στήθος', 'pierś', None, 'rodzaj nijaki'), ('εγκέφαλος', 'mózg', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('βούτυρο', 'masło', None, 'rodzaj nijaki'), ('αβγό', 'jajko', None, 'rodzaj nijaki'), ('κρέας', 'mięso', None, 'rodzaj nijaki'), ('κοτόπουλο', 'kurczak', None, 'rodzaj nijaki'), ('χοιρινό', 'wieprzowina', None, 'rodzaj nijaki'), ('σούπα', 'zupa', None, 'rodzaj żeński'), ('σαλάτα', 'sałatka', None, 'rodzaj żeński'), ('ρύζι', 'ryż', None, 'rodzaj nijaki'), ('μακαρόνια', 'makaron', None, None), ('πατάτα', 'ziemniak', None, 'rodzaj żeński'), ('καρότο', 'marchewka', None, 'rodzaj nijaki'), ('κρεμμύδι', 'cebula', None, 'rodzaj nijaki'), ('σκόρδο', 'czosnek', None, 'rodzaj nijaki'), ('ντομάτα', 'pomidor', None, 'rodzaj żeński'), ('αγγούρι', 'ogórek', None, 'rodzaj nijaki'), ('αχλάδι', 'gruszka', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('μπανάνα', 'banan', None, 'rodzaj żeński'), ('πορτοκάλι', 'pomarańcza', None, 'rodzaj nijaki'), ('λεμόνι', 'cytryna', None, 'rodzaj nijaki'), ('φράουλα', 'truskawka', None, 'rodzaj żeński'), ('σταφύλι', 'winogrono', None, 'rodzaj nijaki'), ('ζάχαρη', 'cukier', None, 'rodzaj żeński'), ('αλάτι', 'sól', None, 'rodzaj nijaki'), ('πιπέρι', 'pieprz', None, 'rodzaj nijaki'), ('λάδι', 'olej', None, 'rodzaj nijaki'), ('αλεύρι', 'mąka', None, 'rodzaj nijaki'), ('μέλι', 'miód', None, 'rodzaj nijaki'), ('σοκολάτα', 'czekolada', None, 'rodzaj żeński'), ('παγωτό', 'lody', None, 'rodzaj nijaki'), ('τούρτα', 'ciasto (tort)', None, 'rodzaj żeński'), ('μπισκότο', 'ciastko', None, 'rodzaj nijaki'), ('πρωινό', 'śniadanie', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('μεσημεριανό', 'obiad', None, 'rodzaj nijaki'), ('βραδινό', 'kolacja', None, 'rodzaj nijaki'), ('σνακ', 'przekąska', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('χυμός', 'sok', None, 'rodzaj męski'), ('μπίρα', 'piwo', None, 'rodzaj żeński'), ('ποτό', 'napój', None, 'rodzaj nijaki'), ('ποτήρι', 'szklanka', None, 'rodzaj nijaki'), ('φλιτζάνι', 'filiżanka', None, 'rodzaj nijaki'), ('πιάτο', 'talerz', None, 'rodzaj nijaki'), ('μαχαίρι', 'nóż', None, 'rodzaj nijaki'), ('πιρούνι', 'widelec', None, 'rodzaj nijaki'), ('κουτάλι', 'łyżka', None, 'rodzaj nijaki'), ('μπουκάλι', 'butelka', None, 'rodzaj nijaki'), ('μενού', 'menu', None, 'rodzaj nijaki'), ('λογαριασμός', 'rachunek', None, 'rodzaj męski'), ('φιλοδώρημα', 'napiwek', None, 'rodzaj nijaki'), ('τραπέζι (w restauracji)', 'stolik', None, 'rodzaj nijaki'), ('σερβιτόρος', 'kelner', None, 'rodzaj męski'), ('μάγειρας', 'kucharz', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('πεινασμένος', 'głodny', None, None), ('διψασμένος', 'spragniony', None, None), ('νόστιμος', 'smaczny', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('διαμέρισμα', 'mieszkanie', None, 'rodzaj nijaki'), ('δωμάτιο', 'pokój', None, 'rodzaj nijaki'), ('κουζίνα', 'kuchnia', None, 'rodzaj żeński'), ('μπάνιο', 'łazienka', None, 'rodzaj nijaki'), ('υπνοδωμάτιο', 'sypialnia', None, 'rodzaj nijaki'), ('σαλόνι', 'salon', None, 'rodzaj nijaki'), ('κήπος', 'ogród', None, 'rodzaj męski'), ('πόρτα', 'drzwi', None, 'rodzaj żeński'), ('παράθυρο', 'okno', None, 'rodzaj nijaki'), ('τοίχος', 'ściana', None, 'rodzaj męski'), ('πάτωμα', 'podłoga', None, 'rodzaj nijaki'), ('στέγη', 'dach', None, 'rodzaj żeński'), ('σκάλες', 'schody', None, None), ('κλειδί', 'klucz', None, 'rodzaj nijaki'), ('τραπέζι', 'stół', None, 'rodzaj nijaki'), ('καρέκλα', 'krzesło', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('κρεβάτι', 'łóżko', None, 'rodzaj nijaki'), ('ντουλάπα', 'szafa', None, 'rodzaj żeński'), ('λάμπα', 'lampa', None, 'rodzaj żeński'), ('χαλί', 'dywan', None, 'rodzaj nijaki'), ('καθρέφτης', 'lustro', None, 'rodzaj męski'), ('τηλεόραση', 'telewizor', None, 'rodzaj żeński'), ('τηλέφωνο', 'telefon', None, 'rodzaj nijaki'), ('υπολογιστής', 'komputer', None, 'rodzaj męski'), ('ρολόι', 'zegar', None, 'rodzaj nijaki'), ('μαξιλάρι', 'poduszka', None, 'rodzaj nijaki'), ('κουβέρτα', 'koc', None, 'rodzaj żeński'), ('πετσέτα', 'ręcznik', None, 'rodzaj żeński'), ('σαπούνι', 'mydło', None, 'rodzaj nijaki'), ('οδοντόβουρτσα', 'szczoteczka do zębów', None, 'rodzaj żeński'), ('ψυγείο', 'lodówka', None, 'rodzaj nijaki'), ('φούρνος', 'piec', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('πλυντήριο', 'pralka', None, 'rodzaj nijaki'), ('σκουπίδια', 'śmieci', None, None)], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('ρούχο', 'ubranie', None, 'rodzaj nijaki'), ('πουκάμισο', 'koszula', None, 'rodzaj nijaki'), ('παντελόνι', 'spodnie', None, 'rodzaj nijaki'), ('φόρεμα', 'sukienka', None, 'rodzaj nijaki'), ('φούστα', 'spódnica', None, 'rodzaj żeński'), ('μπουφάν', 'kurtka', None, 'rodzaj nijaki'), ('παλτό', 'płaszcz', None, 'rodzaj nijaki'), ('πουλόβερ', 'sweter', None, 'rodzaj nijaki'), ('παπούτσια', 'buty', None, None), ('κάλτσες', 'skarpetki', None, None), ('σκουφί', 'czapka', None, 'rodzaj nijaki'), ('καπέλο', 'kapelusz', None, 'rodzaj nijaki'), ('γάντια', 'rękawiczki', None, None), ('κασκόλ', 'szalik', None, 'rodzaj nijaki'), ('τσάντα', 'torba', None, 'rodzaj żeński'), ('σακίδιο', 'plecak', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('πορτοφόλι', 'portfel', None, 'rodzaj nijaki'), ('γυαλιά', 'okulary', None, None), ('ρολόι χειρός', 'zegarek', None, 'rodzaj nijaki'), ('δαχτυλίδι', 'pierścionek', None, 'rodzaj nijaki'), ('εσώρουχα', 'bielizna', None, None), ('πιτζάμα', 'piżama', None, 'rodzaj żeński'), ('ζώνη', 'pasek', None, 'rodzaj żeński'), ('γραβάτα', 'krawat', None, 'rodzaj żeński'), ('κοστούμι', 'garnitur', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('κόκκινος', 'czerwony', None, None), ('μπλε', 'niebieski', None, None), ('πράσινος', 'zielony', None, None), ('κίτρινος', 'żółty', None, None), ('μαύρος', 'czarny', None, None), ('άσπρος', 'biały', None, None), ('γκρι', 'szary', None, None), ('ροζ', 'różowy', None, None), ('μωβ', 'fioletowy', None, None), ('χρώμα', 'kolor', None, 'rodzaj nijaki'), ('στρογγυλός', 'okrągły', None, None), ('τετράγωνος', 'kwadratowy', None, None), ('ίσιος', 'prosty', None, None), ('στραβός', 'krzywy', None, None), ('γραμμή', 'linia', None, 'rodzaj żeński'), ('τελεία', 'punkt', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('κύκλος', 'koło', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('μηδέν', 'zero', None, None), ('έντεκα', 'jedenaście', None, None), ('δώδεκα', 'dwanaście', None, None), ('δεκατρία', 'trzynaście', None, None), ('δεκατέσσερα', 'czternaście', None, None), ('δεκαπέντε', 'piętnaście', None, None), ('δεκαέξι', 'szesnaście', None, None), ('δεκαεπτά', 'siedemnaście', None, None), ('δεκαοκτώ', 'osiemnaście', None, None), ('δεκαεννιά', 'dziewiętnaście', None, None), ('είκοσι', 'dwadzieścia', None, None), ('τριάντα', 'trzydzieści', None, None), ('σαράντα', 'czterdzieści', None, None), ('πενήντα', 'pięćdziesiąt', None, None), ('εξήντα', 'sześćdziesiąt', None, None), ('εβδομήντα', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('ογδόντα', 'osiemdziesiąt', None, None), ('ενενήντα', 'dziewięćdziesiąt', None, None), ('εκατό', 'sto', None, None), ('χίλια', 'tysiąc', None, None), ('εκατομμύριο', 'milion', None, None), ('πρώτος', 'pierwszy', None, None), ('δεύτερος', 'drugi', None, None), ('τρίτος', 'trzeci', None, None), ('μισό', 'połowa', None, 'rodzaj nijaki'), ('ζευγάρι', 'para', None, 'rodzaj nijaki'), ('μερικά', 'kilka', None, None), ('πολλά', 'wiele', None, None), ('ολόκληρος', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('δευτερόλεπτο', 'sekunda', None, 'rodzaj nijaki'), ('λεπτό', 'minuta', None, 'rodzaj nijaki'), ('ημέρα', 'dzień', None, 'rodzaj żeński'), ('νύχτα', 'noc', None, 'rodzaj żeński'), ('εβδομάδα', 'tydzień', None, 'rodzaj żeński'), ('μήνας', 'miesiąc', None, 'rodzaj męski'), ('έτος', 'rok', None, 'rodzaj nijaki'), ('άνοιξη', 'wiosna', None, 'rodzaj żeński'), ('καλοκαίρι', 'lato', None, 'rodzaj nijaki'), ('φθινόπωρο', 'jesień', None, 'rodzaj nijaki'), ('χειμώνας', 'zima', None, 'rodzaj męski'), ('Δευτέρα', 'poniedziałek', None, 'rodzaj żeński'), ('Τρίτη', 'wtorek', None, 'rodzaj żeński'), ('Τετάρτη', 'środa', None, 'rodzaj żeński'), ('Πέμπτη', 'czwartek', None, 'rodzaj żeński'), ('Παρασκευή', 'piątek', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('Σάββατο', 'sobota', None, 'rodzaj nijaki'), ('Κυριακή', 'niedziela', None, 'rodzaj żeński'), ('Ιανουάριος', 'styczeń', None, 'rodzaj męski'), ('Φεβρουάριος', 'luty', None, 'rodzaj męski'), ('Μάρτιος', 'marzec', None, 'rodzaj męski'), ('Απρίλιος', 'kwiecień', None, 'rodzaj męski'), ('Μάιος', 'maj', None, 'rodzaj męski'), ('Ιούνιος', 'czerwiec', None, 'rodzaj męski'), ('Ιούλιος', 'lipiec', None, 'rodzaj męski'), ('Αύγουστος', 'sierpień', None, 'rodzaj męski'), ('Σεπτέμβριος', 'wrzesień', None, 'rodzaj męski'), ('Οκτώβριος', 'październik', None, 'rodzaj męski'), ('Νοέμβριος', 'listopad', None, 'rodzaj męski'), ('Δεκέμβριος', 'grudzień', None, 'rodzaj męski'), ('πρωί', 'rano (pora dnia)', None, 'rodzaj nijaki'), ('μεσημέρι', 'południe', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('βράδυ', 'wieczorem', None, None), ('πάντα', 'zawsze', None, None), ('ποτέ', 'nigdy', None, None), ('μερικές φορές', 'czasem', None, None), ('συχνά', 'często', None, None), ('ήδη', 'już', None, None), ('ακόμα', 'jeszcze', None, None), ('σύντομα', 'wkrótce', None, None), ('αργότερα', 'później', None, None), ('νωρίς', 'wcześnie', None, None), ('αργά', 'późno', None, None), ('πότε', 'kiedy (pytanie)', None, None), ('ημερομηνία', 'data', None, 'rodzaj żeński'), ('παρελθόν', 'przeszłość', None, 'rodzaj nijaki'), ('μέλλον', 'przyszłość', None, 'rodzaj nijaki'), ('γενέθλια', 'urodziny', None, None)], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('γιορτή', 'święto', None, 'rodzaj żeński'), ('διακοπές', 'wakacje', None, None)], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('ήλιος', 'słońce', None, 'rodzaj męski'), ('φεγγάρι', 'księżyc', None, 'rodzaj nijaki'), ('αστέρι', 'gwiazda', None, 'rodzaj nijaki'), ('ουρανός', 'niebo', None, 'rodzaj męski'), ('σύννεφο', 'chmura', None, 'rodzaj nijaki'), ('βροχή', 'deszcz', None, 'rodzaj żeński'), ('χιόνι', 'śnieg', None, 'rodzaj nijaki'), ('άνεμος', 'wiatr', None, 'rodzaj męski'), ('καταιγίδα', 'burza', None, 'rodzaj żeński'), ('ομίχλη', 'mgła', None, 'rodzaj żeński'), ('πάγος', 'lód', None, 'rodzaj męski'), ('φωτιά', 'ogień', None, None), ('γη', 'grunt)', None, 'rodzaj żeński'), ('ποτάμι', 'rzeka', None, 'rodzaj nijaki'), ('λίμνη', 'jezioro', None, 'rodzaj żeński'), ('βουνό', 'góra', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('δάσος', 'las', None, 'rodzaj nijaki'), ('δέντρο', 'drzewo', None, 'rodzaj nijaki'), ('λουλούδι', 'kwiat', None, 'rodzaj nijaki'), ('γρασίδι', 'trawa', None, 'rodzaj nijaki'), ('φύλλο', 'liść', None, 'rodzaj nijaki'), ('χωράφι', 'pole', None, 'rodzaj nijaki'), ('νησί', 'wyspa', None, 'rodzaj nijaki'), ('παραλία', 'plaża', None, 'rodzaj żeński'), ('έρημος', 'pustynia', None, 'rodzaj żeński'), ('βράχος', 'skała', None, 'rodzaj męski'), ('πέτρα', 'kamień', None, 'rodzaj żeński'), ('καιρός', 'pogoda', None, 'rodzaj męski'), ('θερμοκρασία', 'temperatura', None, 'rodzaj żeński'), ('κρύος', 'zimny', None, None), ('ζεστός', 'ciepły', None, None), ('καυτός', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('σκύλος', 'pies', None, 'rodzaj męski'), ('γάτα', 'kot', None, 'rodzaj żeński'), ('άλογο', 'koń', None, 'rodzaj nijaki'), ('αγελάδα', 'krowa', None, 'rodzaj żeński'), ('γουρούνι', 'świnia', None, 'rodzaj nijaki'), ('πρόβατο', 'owca', None, 'rodzaj nijaki'), ('κατσίκα', 'koza', None, 'rodzaj żeński'), ('κότα', 'kura', None, 'rodzaj żeński'), ('πάπια', 'kaczka', None, 'rodzaj żeński'), ('πουλί', 'ptak', None, 'rodzaj nijaki'), ('ποντίκι', 'mysz', None, 'rodzaj nijaki'), ('αρουραίος', 'szczur', None, 'rodzaj męski'), ('φίδι', 'wąż', None, 'rodzaj nijaki'), ('βάτραχος', 'żaba', None, 'rodzaj męski'), ('λιοντάρι', 'lew', None, 'rodzaj nijaki'), ('τίγρη', 'tygrys', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('ελέφαντας', 'słoń', None, 'rodzaj męski'), ('αρκούδα', 'niedźwiedź', None, 'rodzaj żeński'), ('λύκος', 'wilk', None, 'rodzaj męski'), ('αλεπού', 'lis', None, 'rodzaj żeński'), ('λαγός', 'zając', None, 'rodzaj męski'), ('ελάφι', 'jeleń', None, 'rodzaj nijaki'), ('μαϊμού', 'małpa', None, 'rodzaj żeński'), ('πεταλούδα', 'motyl', None, 'rodzaj żeński'), ('μέλισσα', 'pszczoła', None, 'rodzaj żeński'), ('μύγα', 'mucha', None, 'rodzaj żeński'), ('αράχνη', 'pająk', None, 'rodzaj żeński'), ('ζώο', 'zwierzę', None, 'rodzaj nijaki'), ('έντομο', 'owad', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('χωριό', 'wieś', None, 'rodzaj nijaki'), ('οδός', 'droga', None, 'rodzaj żeński'), ('πλατεία', 'plac', None, 'rodzaj żeński'), ('γέφυρα', 'most', None, 'rodzaj żeński'), ('πάρκο', 'park', None, 'rodzaj nijaki'), ('μαγαζί', 'sklep', None, 'rodzaj nijaki'), ('αγορά', 'targ', None, 'rodzaj żeński'), ('σούπερ μάρκετ', 'supermarket', None, 'rodzaj nijaki'), ('τράπεζα', 'bank', None, 'rodzaj żeński'), ('ταχυδρομείο', 'poczta', None, 'rodzaj nijaki'), ('νοσοκομείο', 'szpital', None, 'rodzaj nijaki'), ('φαρμακείο', 'apteka', None, 'rodzaj nijaki'), ('πανεπιστήμιο', 'uniwersytet', None, 'rodzaj nijaki'), ('βιβλιοθήκη', 'biblioteka', None, 'rodzaj żeński'), ('μουσείο', 'muzeum', None, 'rodzaj nijaki'), ('εκκλησία', 'kościół', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('εστιατόριο', 'restauracja', None, 'rodzaj nijaki'), ('καφετέρια', 'kawiarnia', None, 'rodzaj żeński'), ('αεροδρόμιο', 'lotnisko', None, 'rodzaj nijaki'), ('σταθμός', 'dworzec', None, 'rodzaj męski'), ('στάση', 'przystanek', None, 'rodzaj żeński'), ('κινηματογράφος', 'kino', None, 'rodzaj męski'), ('θέατρο', 'teatr', None, 'rodzaj nijaki'), ('αστυνομία', 'policja', None, 'rodzaj żeński'), ('γραφείο', 'biuro', None, 'rodzaj nijaki'), ('εργοστάσιο', 'fabryka', None, 'rodzaj nijaki'), ('κτίριο', 'budynek', None, 'rodzaj nijaki'), ('πύργος', 'wieża', None, 'rodzaj męski'), ('κέντρο', 'centrum', None, 'rodzaj nijaki'), ('διεύθυνση', 'adres', None, 'rodzaj żeński'), ('χάρτης', 'mapa', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('αυτοκίνητο', 'samochód', None, 'rodzaj nijaki'), ('λεωφορείο', 'autobus', None, 'rodzaj nijaki'), ('τρένο', 'pociąg', None, 'rodzaj nijaki'), ('τραμ', 'tramwaj', None, 'rodzaj nijaki'), ('μετρό', 'metro', None, 'rodzaj nijaki'), ('αεροπλάνο', 'samolot', None, 'rodzaj nijaki'), ('πλοίο', 'statek', None, 'rodzaj nijaki'), ('ποδήλατο', 'rower', None, 'rodzaj nijaki'), ('μηχανή', 'motocykl', None, 'rodzaj żeński'), ('εισιτήριο', 'bilet', None, 'rodzaj nijaki'), ('ταξίδι', 'podróż', None, 'rodzaj nijaki'), ('εκδρομή', 'wycieczka', None, 'rodzaj żeński'), ('διαβατήριο', 'paszport', None, 'rodzaj nijaki'), ('βαλίτσα', 'walizka', None, 'rodzaj żeński'), ('βενζίνη', 'benzyna', None, 'rodzaj żeński'), ('πάρκινγκ', 'parking', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('διασταύρωση', 'skrzyżowanie', None, 'rodzaj żeński'), ('φανάρι', 'światła', None, 'rodzaj nijaki'), ('δίπλωμα οδήγησης', 'prawo jazdy', None, 'rodzaj nijaki'), ('οδηγός', 'kierowca', None, 'rodzaj męski'), ('επιβάτης', 'pasażer', None, 'rodzaj męski'), ('είσοδος', 'wjazd', None, 'rodzaj żeński'), ('έξοδος', 'wyjazd', None, 'rodzaj żeński'), ('σιδηρόδρομος', 'kolej', None, 'rodzaj męski'), ('λιμάνι', 'port', None, 'rodzaj nijaki'), ('σύνορο', 'granica', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('δουλειά', 'praca', None, 'rodzaj żeński'), ('επάγγελμα', 'zawód', None, 'rodzaj nijaki'), ('γιατρός', 'lekarz', None, 'rodzaj męski'), ('νοσοκόμα', 'pielęgniarka', None, 'rodzaj żeński'), ('μαθητής', 'uczeń', None, 'rodzaj męski'), ('μηχανικός', 'inżynier', None, 'rodzaj męski'), ('δικηγόρος', 'prawnik', None, 'rodzaj męski'), ('αστυνομικός', 'policjant', None, 'rodzaj męski'), ('στρατιώτης', 'żołnierz', None, 'rodzaj męski'), ('αγρότης', 'rolnik', None, 'rodzaj męski'), ('πωλητής', 'sprzedawca', None, 'rodzaj męski'), ('ταμίας', 'kasjer', None, 'rodzaj męski'), ('ηθοποιός', 'aktor', None, 'rodzaj męski'), ('συγγραφέας', 'pisarz', None, 'rodzaj męski'), ('ζωγράφος', 'malarz', None, 'rodzaj męski'), ('μουσικός', 'muzyk', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('καλλιτέχνης', 'artysta', None, 'rodzaj męski'), ('εταιρεία', 'firma', None, 'rodzaj żeński'), ('λεφτά', 'pieniądze', None, None), ('μισθός', 'pensja', None, 'rodzaj męski'), ('συμβόλαιο', 'umowa', None, 'rodzaj nijaki'), ('συνάντηση', 'spotkanie', None, 'rodzaj żeński'), ('μάθημα', 'lekcja', None, 'rodzaj nijaki'), ('εξέταση', 'egzamin', None, 'rodzaj żeński'), ('βαθμός', 'ocena', None, 'rodzaj męski'), ('τάξη', 'klasa', None, 'rodzaj żeński'), ('βιβλίο', 'książka', None, 'rodzaj nijaki'), ('τετράδιο', 'zeszyt', None, 'rodzaj nijaki'), ('στυλό', 'długopis', None, 'rodzaj nijaki'), ('μολύβι', 'ołówek', None, 'rodzaj nijaki'), ('χαρτί', 'papier', None, 'rodzaj nijaki'), ('πίνακας', 'tablica', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('λεξικό', 'słownik', None, 'rodzaj nijaki'), ('ερώτηση', 'pytanie', None, 'rodzaj żeński'), ('απάντηση', 'odpowiedź', None, 'rodzaj żeński'), ('άσκηση', 'zadanie', None, 'rodzaj żeński'), ('τεστ', 'test', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('τιμή', 'cena', None, 'rodzaj żeński'), ('κάρτα', 'karta (płatnicza)', None, 'rodzaj żeński'), ('μετρητά', 'gotówka', None, None), ('κέρμα', 'moneta', None, 'rodzaj nijaki'), ('χαρτονόμισμα', 'banknot', None, 'rodzaj nijaki'), ('ρέστα', 'reszta', None, None), ('έκπτωση', 'zniżka', None, 'rodzaj żeński'), ('καλάθι', 'koszyk', None, 'rodzaj nijaki'), ('απόδειξη', 'paragon', None, 'rodzaj żeński'), ('εμπόρευμα', 'towar', None, 'rodzaj nijaki'), ('αγορά (zakup)', 'zakup', None, 'rodzaj żeński'), ('πώληση', 'sprzedaż', None, 'rodzaj żeński'), ('αξία', 'wartość', None, 'rodzaj żeński'), ('δάνειο', 'kredyt', None, 'rodzaj nijaki'), ('χρέος', 'dług', None, 'rodzaj nijaki'), ('φόρος', 'podatek', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('πλούτος', 'bogactwo', None, 'rodzaj męski'), ('φτωχός', 'biedny', None, None), ('πλούσιος', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('υγεία', 'zdrowie', None, 'rodzaj żeński'), ('ασθένεια', 'choroba', None, 'rodzaj żeński'), ('πόνος', 'ból', None, 'rodzaj męski'), ('πυρετός', 'gorączka', None, 'rodzaj męski'), ('βήχας', 'kaszel', None, 'rodzaj męski'), ('συνάχι', 'katar', None, 'rodzaj nijaki'), ('φάρμακο', 'lekarstwo', None, 'rodzaj nijaki'), ('χάπι', 'tabletka', None, 'rodzaj nijaki'), ('εγχείρηση', 'operacja', None, 'rodzaj żeński'), ('πληγή', 'rana', None, 'rodzaj żeński'), ('ατύχημα', 'wypadek', None, 'rodzaj nijaki'), ('υγιής', 'zdrowy', None, None), ('άρρωστος', 'chory', None, None), ('κουρασμένος', 'zmęczony', None, None), ('νυσταγμένος', 'śpiący', None, None), ('δυνατός', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('αδύναμος', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('χαρά', 'radość', None, 'rodzaj żeński'), ('λύπη', 'smutek', None, 'rodzaj żeński'), ('φόβος', 'strach', None, 'rodzaj męski'), ('θυμός', 'gniew', None, 'rodzaj męski'), ('αγάπη', 'miłość', None, 'rodzaj żeński'), ('μίσος', 'nienawiść', None, 'rodzaj nijaki'), ('ελπίδα', 'nadzieja', None, 'rodzaj żeński'), ('όνειρο', 'marzenie', None, 'rodzaj nijaki'), ('ευτυχία', 'szczęście', None, 'rodzaj żeński'), ('ντροπή', 'wstyd', None, 'rodzaj żeński'), ('έκπληξη', 'zdziwienie', None, 'rodzaj żeński'), ('περιέργεια', 'ciekawość', None, 'rodzaj żeński'), ('υπομονή', 'cierpliwość', None, 'rodzaj żeński'), ('θάρρος', 'odwaga', None, 'rodzaj nijaki'), ('ειλικρινής', 'szczery', None, None), ('ευγενικός', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('ευγενής', 'grzeczny', None, None), ('ηλίθιος', 'głupi', None, None), ('έξυπνος', 'mądry', None, None), ('τεμπέλης', 'leniwy', None, None), ('εργατικός', 'pracowity', None, None), ('ενδιαφέρων', 'ciekawy', None, None), ('βαρετός', 'nudny', None, None), ('χαρούμενος', 'wesoły', None, None), ('λυπημένος', 'smutny', None, None), ('θυμωμένος', 'zły (rozgniewany)', None, None), ('ευτυχισμένος', 'szczęśliwy', None, None), ('ερωτευμένος', 'zakochany', None, None), ('μοναχικός', 'samotny', None, None), ('ήρεμος', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('μεγάλος', 'duży', None, None), ('μικρός', 'mały', None, None), ('μακρύς', 'długi', None, None), ('κοντός', 'krótki', None, None), ('ψηλός', 'wysoki', None, None), ('χαμηλός', 'niski', None, None), ('φαρδύς', 'szeroki', None, None), ('στενός', 'wąski', None, None), ('χοντρός', 'gruby', None, None), ('αδύνατος', 'chudy', None, None), ('βαρύς', 'ciężki', None, None), ('ελαφρύς', 'lekki', None, None), ('γρήγορος', 'szybki', None, None), ('αργός', 'wolny', None, None), ('σκληρός', 'twardy', None, None), ('μαλακός', 'miękki', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('βρεγμένος', 'mokry', None, None), ('στεγνός', 'suchy', None, None), ('καθαρός', 'czysty', None, None), ('βρώμικος', 'brudny', None, None), ('γεμάτος', 'pełny', None, None), ('άδειος', 'pusty', None, None), ('κοφτερός', 'ostry', None, None), ('δυνατός (głośny)', 'głośny', None, None), ('ήσυχος', 'cichy', None, None), ('φωτεινός', 'jasny', None, None), ('σκοτεινός', 'ciemny', None, None), ('νέος', 'młody', None, None), ('γέρος', 'stary', None, None), ('καινούριος', 'nowy', None, None), ('καλός', 'dobry', None, None), ('κακός', 'zły (niedobry)', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('όμορφος', 'ładny', None, None), ('άσχημος', 'brzydki', None, None), ('εύκολος', 'łatwy', None, None), ('δύσκολος', 'trudny', None, None), ('σημαντικός', 'ważny', None, None), ('δυνατός (możliwy)', 'możliwy', None, None), ('αληθινός', 'prawdziwy', None, None), ('ψεύτικος', 'fałszywy', None, None), ('ακριβός', 'drogi', None, None), ('φθηνός', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('κάνω', 'robić', None, None), ('πηγαίνω', 'iść', None, None), ('ταξιδεύω', 'jechać', None, None), ('έρχομαι', 'przyjść', None, None), ('βγαίνω', 'wyjść', None, None), ('μπαίνω', 'wejść', None, None), ('επιστρέφω', 'wrócić', None, None), ('τρέχω', 'biec', None, None), ('στέκομαι', 'stać', None, None), ('κάθομαι', 'siedzieć', None, None), ('ξαπλώνω', 'leżeć', None, None), ('κοιμάμαι', 'spać', None, None), ('σηκώνομαι', 'wstać', None, None), ('τρώω', 'jeść', None, None), ('πίνω', 'pić', None, None), ('μαγειρεύω', 'gotować', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('πλένω', 'myć', None, None), ('ντύνομαι', 'ubierać się', None, None), ('μιλάω', 'mówić', None, None), ('λέω', 'powiedzieć', None, None), ('ρωτάω', 'pytać', None, None), ('απαντάω', 'odpowiadać', None, None), ('ακούω', 'słyszeć', None, None), ('ακούω (słuchać)', 'słuchać', None, None), ('βλέπω', 'widzieć', None, None), ('κοιτάζω', 'patrzeć', None, None), ('διαβάζω', 'czytać', None, None), ('γράφω', 'pisać', None, None), ('μαθαίνω', 'uczyć się', None, None), ('διδάσκω', 'uczyć (kogoś)', None, None), ('καταλαβαίνω', 'rozumieć', None, None), ('ξέρω', 'wiedzieć', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('γνωρίζω', 'znać', None, None), ('σκέφτομαι', 'myśleć', None, None), ('θυμάμαι', 'pamiętać', None, None), ('ξεχνάω', 'zapominać', None, None), ('μου αρέσει', 'lubić', None, None), ('αγαπάω', 'kochać', None, None), ('χρειάζομαι', 'potrzebować', None, None), ('μπορώ', 'móc', None, None), ('πρέπει', 'musieć', None, None), ('δίνω', 'dawać', None, None), ('παίρνω', 'brać', None, None), ('αγοράζω', 'kupować', None, None), ('πουλάω', 'sprzedawać', None, None), ('πληρώνω', 'płacić', None, None), ('ανοίγω', 'otwierać', None, None), ('κλείνω', 'zamykać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('αρχίζω', 'zaczynać', None, None), ('τελειώνω', 'kończyć', None, None), ('δουλεύω', 'pracować', None, None), ('παίζω', 'grać', None, None), ('τραγουδάω', 'śpiewać', None, None), ('χορεύω', 'tańczyć', None, None), ('κολυμπάω', 'pływać', None, None), ('πετάω', 'latać', None, None), ('βάζω', 'kłaść', None, None), ('ψάχνω', 'szukać', None, None), ('βρίσκω', 'znajdować', None, None), ('περιμένω', 'czekać', None, None), ('βοηθάω', 'pomagać', None, None), ('ζητάω', 'prosić', None, None), ('συγγνώμη (przepraszać)', 'przepraszać', None, 'rodzaj żeński'), ('επιτρέπω', 'pozwalać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('προσπαθώ', 'próbować', None, None), ('αλλάζω', 'zmieniać', None, None), ('φοράω', 'nosić', None, None), ('κρατάω', 'trzymać', None, None), ('ρίχνω', 'rzucać', None, None), ('πιάνω', 'łapać', None, None), ('χτυπάω', 'bić', None, None), ('σκοτώνω', 'zabijać', None, None), ('πεθαίνω', 'umierać', None, None), ('ζω', 'żyć', None, None), ('μένω', 'mieszkać', None, None), ('συναντάω', 'spotykać', None, None), ('τηλεφωνώ', 'dzwonić', None, None), ('στέλνω', 'wysyłać', None, None), ('παίρνω (dostawać)', 'dostawać', None, None), ('δείχνω', 'pokazywać', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('προσκαλώ', 'zapraszać', None, None), ('επισκέπτομαι', 'odwiedzać', None, None), ('κλαίω', 'płakać', None, None), ('γελάω', 'śmiać się', None, None), ('χαμογελάω', 'uśmiechać się', None, None), ('φοβάμαι', 'bać się', None, None), ('χαίρομαι', 'cieszyć się', None, None), ('πιστεύω', 'wierzyć', None, None), ('συμφωνώ', 'zgadzać się', None, None), ('επιλέγω', 'wybierać', None, None), ('αποφασίζω', 'decydować', None, None), ('μετράω', 'liczyć', None, None), ('ζυγίζω', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('περπατάω', 'chodzić', None, None), ('οδηγώ', 'jeździć', None, None), ('επιβιβάζομαι', 'wsiadać', None, None), ('αποβιβάζομαι', 'wysiadać', None, None), ('στρίβω', 'skręcać', None, None), ('σταματάω', 'zatrzymywać się', None, None), ('αργώ', 'spóźniać się', None, None), ('βιάζομαι', 'spieszyć się', None, None), ('ξεκουράζομαι', 'odpoczywać', None, None), ('διασκεδάζω', 'bawić się', None, None), ('ζωγραφίζω', 'rysować', None, None), ('χτίζω', 'budować', None, None), ('επισκευάζω', 'naprawiać', None, None), ('κόβω', 'ciąć', None, None), ('τηγανίζω', 'smażyć', None, None), ('ψήνω', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('ανακατεύω', 'mieszać', None, None), ('ρίχνω (nalewać)', 'nalewać', None, None), ('καθαρίζω', 'sprzątać', None, None), ('πλένω ρούχα', 'prać', None, None), ('σιδερώνω', 'prasować', None, None), ('ξυρίζομαι', 'golić się', None, None), ('χτενίζω', 'czesać', None, None), ('κάνω μπάνιο', 'kąpać się', None, None), ('ξυπνάω', 'budzić się', None, None), ('αποκοιμιέμαι', 'zasypiać', None, None), ('ονειρεύομαι', 'marzyć', None, None), ('βλέπω όνειρο', 'śnić', None, None), ('γυμνάζομαι', 'ćwiczyć', None, None), ('προπονούμαι', 'trenować', None, None), ('κερδίζω', 'wygrywać', None, None), ('χάνω', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('κινώ', 'ruszać', None, None), ('τραβάω', 'ciągnąć', None, None), ('σπρώχνω', 'pchać', None, None), ('σηκώνω', 'podnosić', None, None), ('πέφτω', 'spadać', None, None), ('πηδάω', 'skakać', None, None), ('σκαρφαλώνω', 'wspinać się', None, None), ('κρύβω', 'ukrywać', None, None), ('κλέβω', 'kraść', None, None), ('επιστρέφω (oddawać)', 'oddawać', None, None), ('δανείζω', 'pożyczać', None, None), ('ξοδεύω', 'wydawać', None, None), ('εξοικονομώ', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('εκείνος', 'tamten', None, None), ('πώς', 'jak', None, None), ('γιατί', 'dlaczego', None, None), ('ποιος', 'kto', None, None), ('ο οποίος', 'który', None, None), ('ποιος (jaki)', 'jaki', None, None), ('πόσο', 'ile (policzalne)', None, None), ('αλλά', 'ale', None, None), ('ή', 'lub', None, None), ('επειδή', 'bo', None, None), ('αν', 'jeśli', None, None), ('ότι', 'że', None, None), ('λοιπόν', 'więc', None, None), ('επίσης', 'też', None, None), ('μόνο', 'tylko', None, None), ('λίγο (trochę)', 'trochę', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('όλα', 'wszystko', None, None), ('τίποτα', 'nic', None, None), ('κάτι', 'coś', None, None), ('κάποιος', 'ktoś', None, None), ('κανείς', 'nikt', None, None), ('κάθε', 'każdy', None, None), ('άλλος', 'inny', None, None), ('ίδιος', 'ten sam', None, None), ('ίσως', 'może (być)', None, None), ('σίγουρα', 'na pewno', None, None), ('μαζί', 'razem', None, None), ('μόνος', 'sam', None, None), ('χωρίς', 'bez', None, None), ('με', 'z (towarzysząc)', None, None), ('σε', 'w (miejsce)', None, None), ('πάνω σε', 'na (powierzchni)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('προς', 'do (kierunek)', None, None), ('για', 'dla', None, None), ('μέσω', 'przez', None, None), ('μετά', 'po (czas)', None, None), ('πριν', 'przed', None, None), ('πίσω', 'za (z tyłu)', None, None), ('πάνω από', 'nad', None, None), ('κάτω από', 'pod', None, None), ('δίπλα', 'obok', None, None), ('ανάμεσα', 'między', None, None), ('εναντίον', 'przeciw', None, None), ('για (o)', 'o (temat)', None, None), ('κοντά', 'u (przy)', None, None), ('περίπου', 'około', None, None), ('σχεδόν', 'prawie', None, None), ('ακόμη και', 'nawet', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('ξανά', 'jeszcze raz', None, None), ('τότε', 'wtedy', None, None), ('κάπου', 'gdzieś', None, None), ('πουθενά', 'nigdzie', None, None), ('παντού', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('ζωή', 'życie', None, 'rodzaj żeński'), ('θάνατος', 'śmierć', None, 'rodzaj męski'), ('κόσμος', 'świat', None, 'rodzaj męski'), ('χώρα', 'kraj', None, 'rodzaj żeński'), ('κράτος', 'państwo', None, 'rodzaj nijaki'), ('γλώσσα (mowa)', 'język (mowa)', None, 'rodzaj żeński'), ('λέξη', 'słowo', None, 'rodzaj żeński'), ('πρόταση', 'zdanie', None, 'rodzaj żeński'), ('όνομα', 'imię', None, 'rodzaj nijaki'), ('επώνυμο', 'nazwisko', None, 'rodzaj nijaki'), ('ηλικία', 'wiek', None, 'rodzaj żeński'), ('ιστορία', 'historia', None, 'rodzaj żeński'), ('πολιτισμός', 'kultura', None, 'rodzaj męski'), ('θρησκεία', 'religia', None, 'rodzaj żeński'), ('Θεός', 'Bóg', None, 'rodzaj męski'), ('πόλεμος', 'wojna', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('ειρήνη', 'pokój (brak wojny)', None, 'rodzaj żeński'), ('νόμος', 'prawo (przepis)', None, 'rodzaj męski'), ('ελευθερία', 'wolność', None, 'rodzaj żeński'), ('εξουσία', 'władza', None, 'rodzaj żeński'), ('κυβέρνηση', 'rząd', None, 'rodzaj żeński'), ('εκλογές', 'wybory', None, None), ('πρόβλημα', 'problem', None, 'rodzaj nijaki'), ('ιδέα', 'pomysł', None, 'rodzaj żeński'), ('λόγος', 'powód', None, 'rodzaj męski'), ('αποτέλεσμα', 'wynik', None, 'rodzaj nijaki'), ('τρόπος', 'sposób', None, 'rodzaj męski'), ('αρχή', 'początek', None, 'rodzaj żeński'), ('τέλος', 'koniec', None, 'rodzaj nijaki'), ('μέρος', 'część', None, 'rodzaj nijaki'), ('τόπος', 'miejsce', None, 'rodzaj męski'), ('πράγμα', 'rzecz', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('υπόθεση', 'sprawa', None, 'rodzaj żeński'), ('πληροφορία', 'informacja', None, 'rodzaj żeński'), ('μήνυμα', 'wiadomość', None, 'rodzaj nijaki'), ('γράμμα', 'list', None, 'rodzaj nijaki'), ('εφημερίδα', 'gazeta', None, 'rodzaj żeński'), ('ταινία', 'film', None, 'rodzaj żeński'), ('μουσική', 'muzyka', None, 'rodzaj żeński'), ('τραγούδι', 'piosenka', None, 'rodzaj nijaki'), ('εικόνα', 'obraz', None, 'rodzaj żeński'), ('παιχνίδι', 'gra', None, 'rodzaj nijaki'), ('άθλημα', 'sport', None, 'rodzaj nijaki'), ('αγώνας', 'mecz', None, 'rodzaj męski'), ('ομάδα', 'drużyna', None, 'rodzaj żeński'), ('μπάλα', 'piłka', None, 'rodzaj żeński'), ('διασκέδαση', 'zabawa', None, 'rodzaj żeński'), ('πάρτι', 'impreza', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('δώρο', 'prezent', None, 'rodzaj nijaki'), ('όνειρο (sen)', 'sen', None, 'rodzaj nijaki'), ('σχέδιο', 'plan', None, 'rodzaj nijaki'), ('επιλογή', 'wybór', None, 'rodzaj żeński'), ('λάθος', 'błąd', None, 'rodzaj nijaki'), ('αλήθεια', 'prawda', None, 'rodzaj żeński'), ('ψέμα', 'kłamstwo', None, 'rodzaj nijaki'), ('μυστικό', 'tajemnica', None, 'rodzaj nijaki'), ('δύναμη', 'siła', None, 'rodzaj żeński'), ('ενέργεια', 'energia', None, 'rodzaj żeński'), ('φως', 'światło', None, 'rodzaj nijaki'), ('ήχος', 'dźwięk', None, 'rodzaj męski'), ('σιωπή', 'cisza', None, 'rodzaj żeński'), ('κίνηση', 'ruch', None, 'rodzaj żeński'), ('αλλαγή', 'zmiana', None, 'rodzaj żeński'), ('διαφορά', 'różnica', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('παράδειγμα', 'przykład', None, 'rodzaj nijaki'), ('σύνολο', 'całość', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('διαδίκτυο', 'internet', None, 'rodzaj nijaki'), ('ηλεκτρονικό ταχυδρομείο', 'e-mail', None, 'rodzaj nijaki'), ('κωδικός', 'hasło', None, 'rodzaj męski'), ('ιστοσελίδα', 'strona internetowa', None, 'rodzaj żeński'), ('πρόγραμμα', 'program', None, 'rodzaj nijaki'), ('εφαρμογή', 'aplikacja', None, 'rodzaj żeński'), ('οθόνη', 'ekran', None, 'rodzaj żeński'), ('πληκτρολόγιο', 'klawiatura', None, 'rodzaj nijaki'), ('ποντίκι υπολογιστή', 'myszka komputerowa', None, 'rodzaj nijaki'), ('αρχείο', 'plik', None, 'rodzaj nijaki'), ('φωτογραφία', 'zdjęcie', None, 'rodzaj żeński'), ('κάμερα', 'kamera', None, 'rodzaj żeński'), ('μπαταρία', 'bateria', None, 'rodzaj żeński'), ('ρεύμα', 'prąd', None, 'rodzaj nijaki'), ('καλώδιο', 'kabel', None, 'rodzaj nijaki'), ('μηχανή (maszyna)', 'maszyna', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('εργαλείο', 'narzędzie', None, 'rodzaj nijaki'), ('σφυρί', 'młotek', None, 'rodzaj nijaki'), ('εκτυπωτής', 'drukarka', None, 'rodzaj męski'), ('φορτιστής', 'ładowarka', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('βορράς', 'północ', None, 'rodzaj męski'), ('νότος', 'południe (kierunek)', None, 'rodzaj męski'), ('ανατολή', 'wschód', None, 'rodzaj żeński'), ('δύση', 'zachód', None, 'rodzaj żeński'), ('Ευρώπη', 'Europa', None, 'rodzaj żeński'), ('Γερμανία', 'Niemcy', None, 'rodzaj żeński'), ('Γαλλία', 'Francja', None, 'rodzaj żeński'), ('Ιταλία', 'Włochy', None, 'rodzaj żeński'), ('Ισπανία', 'Hiszpania', None, 'rodzaj żeński'), ('Ρωσία', 'Rosja', None, 'rodzaj żeński'), ('Αγγλία', 'Anglia', None, 'rodzaj żeński'), ('Αμερική', 'Ameryka', None, 'rodzaj żeński'), ('Κίνα', 'Chiny', None, 'rodzaj żeński'), ('Ιαπωνία', 'Japonia', None, 'rodzaj żeński'), ('Αφρική', 'Afryka', None, 'rodzaj żeński'), ('Ασία', 'Azja', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('ήπειρος', 'kontynent', None, 'rodzaj żeński'), ('πρωτεύουσα', 'stolica', None, 'rodzaj żeński'), ('πολίτης', 'obywatel', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('κομμάτι', 'kawałek', None, 'rodzaj nijaki'), ('σταγόνα', 'kropla', None, 'rodzaj żeński'), ('κουτί', 'pudełko', None, 'rodzaj nijaki'), ('σάκος', 'worek', None, 'rodzaj męski'), ('κλωστή', 'nić', None, 'rodzaj żeński'), ('σύρμα', 'drut', None, 'rodzaj nijaki'), ('βελόνα', 'igła', None, 'rodzaj żeński'), ('ψαλίδι', 'nożyczki', None, 'rodzaj nijaki'), ('ραβδί', 'kij', None, 'rodzaj nijaki'), ('σκοινί', 'lina', None, 'rodzaj nijaki'), ('αλυσίδα', 'łańcuch', None, 'rodzaj żeński'), ('βίδα', 'śruba', None, 'rodzaj żeński'), ('καρφί', 'gwóźdź', None, 'rodzaj nijaki'), ('κόλλα', 'klej', None, 'rodzaj żeński'), ('μπογιά', 'farba', None, 'rodzaj żeński'), ('γυαλί', 'szkło', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('ξύλο', 'drewno', None, 'rodzaj nijaki'), ('μέταλλο', 'metal', None, 'rodzaj nijaki'), ('χρυσός', 'złoto', None, 'rodzaj męski'), ('ασήμι', 'srebro', None, 'rodzaj nijaki'), ('σίδερο', 'żelazo', None, 'rodzaj nijaki'), ('πλαστικό', 'plastik', None, 'rodzaj nijaki'), ('δέρμα (materiał)', 'skóra (materiał)', None, 'rodzaj nijaki'), ('βαμβάκι', 'bawełna', None, 'rodzaj nijaki'), ('μαλλί', 'wełna', None, 'rodzaj nijaki'), ('άμμος', 'piasek', None, 'rodzaj żeński'), ('λάσπη', 'błoto', None, 'rodzaj żeński'), ('σκόνη', 'kurz', None, 'rodzaj żeński'), ('καπνός', 'dym', None, 'rodzaj męski'), ('ατμός', 'para (wodna)', None, 'rodzaj męski')], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('πάνω', 'góra (kierunek)', None, None), ('κάτω', 'dół', None, None), ('μπροστά', 'przód', None, None), ('πίσω (tył)', 'tył', None, None), ('μέση', 'środek', None, 'rodzaj żeński'), ('πλευρά', 'bok', None, 'rodzaj żeński'), ('μέσα', 'wewnątrz', None, None), ('έξω', 'na zewnątrz', None, None), ('μακριά', 'daleko', None, None), ('κοντά (blisko)', 'blisko', None, None), ('ψηλά', 'wysoko', None, None), ('χαμηλά', 'nisko', None, None), ('γρήγορα', 'szybko', None, None), ('αργά (wolno)', 'wolno', None, None), ('καλά', 'dobrze', None, None), ('άσχημα', 'źle', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('εύκολα', 'łatwo', None, None), ('δύσκολα', 'trudno', None, None), ('χωριστά', 'osobno', None, None), ('απέναντι', 'naprzeciw', None, None), ('κατά μήκος', 'wzdłuż', None, None), ('κατά πλάτος', 'w poprzek', None, None), ('γύρω', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('λάχανο', 'kapusta', None, 'rodzaj nijaki'), ('αρακάς', 'groszek', None, 'rodzaj męski'), ('φασόλια', 'fasola', None, None), ('μανιτάρι', 'grzyb', None, 'rodzaj nijaki'), ('καρύδι', 'orzech', None, 'rodzaj nijaki'), ('δαμάσκηνο', 'śliwka', None, 'rodzaj nijaki'), ('κεράσι', 'wiśnia', None, 'rodzaj nijaki'), ('ροδάκινο', 'brzoskwinia', None, 'rodzaj nijaki'), ('καρπούζι', 'arbuz', None, 'rodzaj nijaki'), ('σμέουρο', 'malina', None, 'rodzaj nijaki'), ('λουκάνικο', 'kiełbasa', None, 'rodzaj nijaki'), ('ζαμπόν', 'szynka', None, 'rodzaj nijaki'), ('ψωμάκι', 'bułka', None, 'rodzaj nijaki'), ('σάντουιτς', 'kanapka', None, 'rodzaj nijaki'), ('κρέπα', 'naleśnik', None, 'rodzaj żeński'), ('γιαούρτι', 'jogurt', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('κρέμα γάλακτος', 'śmietana', None, 'rodzaj żeński'), ('σάλτσα', 'sos', None, 'rodzaj żeński'), ('ξίδι', 'ocet', None, 'rodzaj nijaki'), ('μαγιά', 'drożdże', None, 'rodzaj żeński'), ('ζελέ (kisiel)', 'kisiel', None, 'rodzaj nijaki'), ('ζελέ', 'galaretka', None, 'rodzaj nijaki'), ('σταφίδα', 'rodzynek', None, 'rodzaj żeński'), ('αμύγδαλο', 'migdał', None, 'rodzaj nijaki'), ('μαϊντανός', 'pietruszka', None, 'rodzaj męski'), ('άνηθος', 'koperek', None, 'rodzaj męski'), ('πιπεριά', 'papryka', None, 'rodzaj żeński'), ('μαρούλι', 'sałata', None, 'rodzaj nijaki'), ('σπανάκι', 'szpinak', None, 'rodzaj nijaki'), ('παντζάρι', 'burak', None, 'rodzaj nijaki')], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('πεθερός', 'teść', None, 'rodzaj męski'), ('πεθερά', 'teściowa', None, 'rodzaj żeński'), ('κουνιάδος', 'szwagier', None, 'rodzaj męski'), ('ανιψιός', 'bratanek', None, 'rodzaj męski'), ('ανιψιά', 'siostrzenica', None, 'rodzaj żeński'), ('ορφανό', 'sierota', None, 'rodzaj nijaki'), ('χήρα', 'wdowa', None, 'rodzaj żeński'), ('αρραβωνιαστικός', 'narzeczony', None, 'rodzaj męski'), ('γάμος', 'ślub', None, 'rodzaj męski'), ('διαζύγιο', 'rozwód', None, 'rodzaj nijaki'), ('γέννηση', 'urodzenie', None, 'rodzaj żeński'), ('κηδεία', 'pogrzeb', None, 'rodzaj żeński'), ('κομμωτής', 'fryzjer', None, 'rodzaj męski'), ('φούρναρης', 'piekarz', None, 'rodzaj męski'), ('κρεοπώλης', 'rzeźnik', None, 'rodzaj męski'), ('σερβιτόρα', 'kelnerka', None, 'rodzaj żeński')], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('ταχυδρόμος', 'listonosz', None, 'rodzaj męski'), ('πυροσβέστης', 'strażak', None, 'rodzaj męski'), ('δικαστής', 'sędzia', None, 'rodzaj męski'), ('διευθυντής', 'dyrektor', None, 'rodzaj męski')], 'sentences': []}]
# === /SŁOWNICTWO ===
