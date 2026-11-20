"""Treść kursu: turecki dla Polaków.

Wymowa polskimi literami: ı = y (bez zaokrąglenia), ö = jak niemieckie ö, ü = jak niemieckie ü
(zapisane iu / ö / ü), ğ wydłuża poprzednią samogłoskę.
"""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "SES · WYMOWA", "jezyk": "DİL · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Wymowa", "icon": "Ş", "track": "wymowa",
     "letters": [
         ("c", "[dʒ]: jak polskie dż", "cam (szkło)"),
         ("ç", "[tʃ]: jak polskie cz", "çay (herbata)"),
         ("ş", "[ʃ]: jak polskie sz", "şeker (cukier)"),
         ("ğ", "miękkie g: nie czytasz, wydłuża samogłoskę", "dağ (góra)"),
         ("ı", "[ɯ]: jak polskie y, nie zaokrąglaj ust", "ışık (światło)"),
         ("i", "[i]: jak polskie i (z kropką)", "iyi (dobry)"),
         ("ö", "[ø]: jak niemieckie ö: o z ustami do e", "göz (oko)"),
         ("ü", "[y]: jak niemieckie ü: u z ustami do i", "gül (róża)"),
         ("j", "[ʒ]: jak polskie ż", "jale (rosa)"),
         ("h", "[h]: lekkie, wymawiaj zawsze", "hava (powietrze)"),
         ("y", "[j]: jak polskie j", "yıl (rok)"),
         ("v", "[v]: jak polskie w", "var (jest)"),
         ("e", "[e]: jak polskie e", "ev (dom)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "M", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("merhaba", "cześć", None, None),
         ("hoşça", "miło (w „hoşça kal”)", None, None),
         ("kal", "zostań", None, "„Hoşça kal” = „zostań miło”, mówi to wychodzący."),
         ("teşekkürler", "dziękuję", None, None),
         ("lütfen", "proszę", None, None),
         ("evet", "tak", None, None),
         ("hayır", "nie", None, None),
         ("iyi", "dobry", None, None),
         ("günler", "dni", None, "„İyi günler” = dzień dobry."),
         ("geceler", "noce", None, "„İyi geceler” = dobranoc."),
         ("çok", "bardzo; dużo", None, None),
         ("pardon", "przepraszam", "pardon", None),
         ("tamam", "dobrze; ok", None, None),
     ],
     "sentences": [
         (["merhaba", "!"], "Cześć!", {"pardon": "pardon to „przepraszam”."}),
         (["hoşça", "kal", "!"], "Do widzenia!", {"merhaba": "merhaba to „cześć”."}),
         (["iyi", "günler", "!"], "Dzień dobry!", {"geceler": "geceler to „noce”."}),
         (["iyi", "geceler", "!"], "Dobranoc!", {"günler": "günler to „dni”."}),
         (["teşekkürler", "!"], "Dziękuję!", {"lütfen": "lütfen to „proszę”. Tu dziękujesz."}),
         (["evet", ",", "teşekkürler"], "Tak, dziękuję.", {"hayır": "hayır to „nie”."}),
         (["hayır", ",", "teşekkürler"], "Nie, dziękuję.", {"evet": "evet to „tak”."}),
         (["pardon", "!"], "Przepraszam!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "B", "track": "jezyk",
     "words": [
         ("ben", "ja", None, None),
         ("sen", "ty", None, None),
         ("o", "on; ona; ono", None, "Turecki nie rozróżnia rodzaju."),
         ("öğrenci", "student", None, None),
         ("öğrenciyim", "jestem studentem", None, None),
         ("öğrencisin", "jesteś studentem", None, None),
         ("öğretmen", "nauczyciel", None, None),
         ("öğretmenim", "jestem nauczycielem", None, None),
         ("öğretmensin", "jesteś nauczycielem", None, None),
         ("Polonyalı", "Polak; Polka", None, None),
         ("Polonyalıyım", "jestem Polakiem; Polką", None, None),
         ("Polonya'danım", "jestem z Polski", None, None),
         ("Polonya'dansın", "jesteś z Polski", None, None),
         ("Türkiye'den", "z Turcji", None, None),
     ],
     "sentences": [
         (["ben", "öğrenciyim"], "Jestem studentem.", {"öğrencisin": "-sin to „ty”. O sobie: -yim."}),
         (["sen", "öğretmensin"], "Jesteś nauczycielem.", {"öğretmenim": "-im to „ja”. Do „sen”: -sin."}),
         (["o", "Polonyalı"], "On jest Polakiem.", {"Polonyalıyım": "-yım to „ja”. O nim: bez końcówki."}),
         (["ben", "Polonyalıyım"], "Jestem Polakiem.", {}),
         (["ben", "Polonya'danım"], "Jestem z Polski.", {"Polonya'dansın": "-sın to „ty”. O sobie: -ım."}),
         (["o", "Türkiye'den"], "On jest z Turcji.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "A", "track": "jezyk",
     "words": [
         ("annem", "moja mama", None, "anne + -m = moja mama."),
         ("babam", "mój tata", None, "baba + -m = mój tata."),
         ("abim", "mój starszy brat", None, None),
         ("ablan", "twoja starsza siostra", None, "abla + -n = twoja siostra."),
         ("kardeşim", "moje rodzeństwo (młodsze)", None, None),
         ("arkadaşım", "mój przyjaciel", None, None),
         ("çocuğum", "moje dziecko", None, None),
         ("adam", "mężczyzna", None, None),
         ("kadın", "kobieta", None, None),
         ("benim", "mój; moja", None, None),
         ("senin", "twój; twoja", None, None),
         ("var", "jest; istnieje", None, "„Benim abim var” = mam starszego brata."),
         ("bir", "jeden; jakiś", None, None),
         ("küçük", "mały", None, None),
         ("güzel", "piękny; miły", None, None),
     ],
     "sentences": [
         (["annem", "güzel"], "Moja mama jest miła.", {"babam": "babam to „mój tata”."}),
         (["babam", "iyi"], "Mój tata jest dobry.", {"annem": "annem to „moja mama”."}),
         (["kardeşim", "küçük"], "Moje rodzeństwo jest małe.", {}),
         (["benim", "bir", "abim", "var"], "Mam starszego brata.", {"senin": "senin to „twój”. O sobie: benim."}),
         (["senin", "bir", "ablan", "var"], "Masz starszą siostrę.", {"benim": "benim to „mój”. Do „sen”: senin."}),
         (["arkadaşım", "iyi"], "Mój przyjaciel jest dobry.", {}),
         (["o", "bir", "adam"], "On jest mężczyzną.", {"kadın": "kadın to „kobieta”."}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "Ç", "track": "jezyk",
     "words": [
         ("su", "woda", None, None),
         ("kahve", "kawa", None, None),
         ("çay", "herbata", None, None),
         ("ekmek", "chleb", None, None),
         ("peynir", "ser", None, None),
         ("süt", "mleko", None, None),
         ("balık", "ryba", None, None),
         ("elma", "jabłko", None, None),
         ("istiyorum", "chcę", None, None),
         ("istiyorsun", "chcesz", None, None),
         ("lezzetli", "smaczny", None, None),
         ("şimdi", "teraz", None, None),
     ],
     "sentences": [
         (["bir", "kahve", "istiyorum"], "Chcę kawę.", {"istiyorsun": "-sun to „ty”. O sobie: -um."}),
         (["sen", "çay", "istiyorsun"], "Chcesz herbatę.", {"istiyorum": "-um to „ja”. Do „sen”: -sun."}),
         (["ben", "ekmek", "istiyorum"], "Chcę chleb.", {}),
         (["sen", "bir", "elma", "istiyorsun"], "Chcesz jabłko.", {}),
         (["balık", "çok", "lezzetli"], "Ryba jest bardzo smaczna.", {}),
         (["şimdi", "su", "istiyorum"], "Teraz chcę wodę.", {}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "1", "track": "jezyk",
     "words": [
         ("iki", "dwa", None, None),
         ("üç", "trzy", None, None),
         ("dört", "cztery", None, None),
         ("beş", "pięć", None, None),
         ("on", "dziesięć", None, None),
         ("bugün", "dziś", None, None),
         ("yarın", "jutro", None, None),
         ("dün", "wczoraj", None, None),
         ("saat", "godzina; zegar", None, None),
         ("kaç", "ile; która", None, None),
     ],
     "sentences": [
         (["iki", "çocuğum", "var"], "Mam dwoje dzieci.", {}),
         (["üç", "elma", "istiyorum"], "Chcę trzy jabłka.", {"iki": "iki to „dwa”. Chcesz trzy: üç."}),
         (["saat", "kaç", "?"], "Która jest godzina?", {}),
         (["saat", "on"], "Jest dziesiąta.", {"beş": "beş to „pięć”."}),
         (["bugün", "kahve", "istiyorum"], "Dziś chcę kawę.", {"yarın": "yarın to „jutro”. Tu „dziś”: bugün."}),
         (["yarın", "balık", "istiyorum"], "Jutro chcę rybę.", {"dün": "dün to „wczoraj”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "Ü", "track": "jezyk",
     "words": [
         ("ev", "dom", None, None),
         ("eve", "do domu", None, "-e = dokąd."),
         ("şehir", "miasto", None, None),
         ("sokak", "ulica", None, None),
         ("okul", "szkoła", None, None),
         ("deniz", "morze", None, None),
         ("taksi", "taksówka", "taksówka", None),
         ("otel", "hotel", "hotel", None),
         ("nerede", "gdzie", None, None),
         ("burada", "tu", None, None),
         ("orada", "tam", None, None),
         ("gidiyorum", "idę; jadę", None, None),
         ("İstanbul'a", "do Stambułu", None, None),
         ("İstanbul'dan", "ze Stambułu", None, None),
         ("sağda", "po prawej", None, None),
         ("solda", "po lewej", None, None),
     ],
     "sentences": [
         (["otel", "nerede", "?"], "Gdzie jest hotel?", {"burada": "burada to „tu”. Pytasz „gdzie”: nerede."}),
         (["otel", "orada"], "Hotel jest tam.", {"burada": "burada to „tu”. Tu „tam”: orada."}),
         (["eve", "gidiyorum"], "Idę do domu.", {}),
         (["İstanbul'a", "gidiyorum"], "Jadę do Stambułu.", {"İstanbul'dan": "-dan to „z”. Jedziesz do: -a."}),
         (["taksi", "sağda"], "Taksówka jest po prawej.", {"solda": "solda to „po lewej”."}),
         (["okul", "orada"], "Szkoła jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Jedna litera, jeden dźwięk", "chain": [],
                "text": "Turecki czyta się dokładnie tak, jak jest zapisany. Pamiętaj: c = [dʒ], ç = [tʃ], ş = [ʃ], ı = [ɯ] (bez kropki), ğ wydłuża samogłoskę."}],
    "ja": [{"title": "Końcówki zamiast „jestem”", "chain": [
                ("Jestem studentem.", ["ben", "öğrenciyim"], "-yim = jestem."),
                ("Jesteś nauczycielem.", ["sen", "öğretmensin"], "-sin = jesteś."),
            ],
            "text": "Turecki dokleja końcówki do słowa: öğrenci-yim (jestem studentem), öğretmen-sin (jesteś nauczycielem). Nie ma rodzaju: „o” znaczy on, ona, ono."}],
    "ludzie": [{"title": "Końcówki dzierżawcze", "chain": [],
                "text": "„Mój” to końcówka -m / -im: anne → annem (moja mama). „Twój” to -n / -in: abla → ablan. Samogłoska w końcówce dopasowuje się do słowa (harmonia samogłosek)."}],
    "jedzenie": [{"title": "Istiyorum i istiyorsun", "chain": [],
                  "text": "Czasownik dostaje końcówkę osoby: istiyor-um (chcę), istiyor-sun (chcesz). Zaimka ben, sen często się nie mówi."}],
}

ENDINGS_INSIGHT = {"title": "Końcówki osobowe",
                   "text": "Po turecku kto działa, mówi końcówka: -im (ja), -sin (ty), -m (mój), -n (twój). Tu to ćwiczysz."}

ENDINGS = [
    ("ben ", "öğrenci", "yim", "", ["yim", "sin"], "ja jestem", "Do „ben” pasuje -yim.", "ja"),
    ("sen ", "öğretmen", "sin", "", ["im", "sin"], "ty jesteś", "Do „sen” pasuje -sin.", "ja"),
    ("ben ", "öğretmen", "im", "", ["im", "sin"], "ja jestem", "Do „ben” pasuje -im.", "ja"),
    ("", "anne", "m", " güzel", ["m", "n"], "moja mama", "-m to „mój”.", "ludzie"),
    ("senin ", "abla", "n", " var", ["m", "n"], "twoja siostra", "-n to „twój”.", "ludzie"),
    ("", "baba", "m", " iyi", ["m", "n"], "mój tata", "-m to „mój”.", "ludzie"),
    ("", "arkadaş", "ım", " iyi", ["ım", "ın"], "mój przyjaciel", "-ım to „mój”.", "ludzie"),
    ("ben bir kahve ", "istiyor", "um", "", ["um", "sun"], "ja chcę", "Do „ben” pasuje -um.", "jedzenie"),
    ("sen çay ", "istiyor", "sun", "", ["um", "sun"], "ty chcesz", "Do „sen” pasuje -sun.", "jedzenie"),
    ("", "ev", "e", " gidiyorum", ["e", "den"], "do domu", "-e to „do”, -den to „z”.", "miejsca"),
    ("", "İstanbul'", "a", " gidiyorum", ["a", "dan"], "do Stambułu", "-a to „do”, -dan to „z”.", "miejsca"),
]

CHAT_EXTRA = {"Elif": "Elif (imię)", "Emre": "Emre (imię)", "şoför": "kierowca", "nereye": "dokąd",
              "de": "też", "kardeşin": "twoje rodzeństwo", "mı": "(partykuła pytająca)", "misin": "czy jesteś?"}

CHATS = [
    {"id": "kafe", "title": "W kawiarni", "partner": "Elif", "avatar": "E", "requires": "jedzenie",
     "turns": [
         {"bot": ["iyi", "günler", "!"], "en": "Dzień dobry!",
          "options": [(["iyi", "günler", "!"], True, None), (["iyi", "geceler", "!"], False, "iyi geceler to „dobranoc”. Jest dzień.")]},
         {"bot": ["kahve", "?"], "en": "Kawę?",
          "options": [(["evet", ",", "bir", "kahve", "istiyorum"], True, None),
                      (["evet", ",", "bir", "kahve", "istiyorsun"], False, "-sun to „ty”. O sobie: istiyorum.")]},
         {"bot": ["ekmek", "de", "?"], "en": "Chleb też?",
          "options": [(["hayır", ",", "teşekkürler"], True, None),
                      (["lütfen", "!"], False, "lütfen to „proszę”. Odmów: hayır, teşekkürler.")]},
         {"bot": ["tamam", "!"], "build": (["teşekkürler", "!"], "Dziękuję!"), "en": "Dobrze!"},
     ]},
    {"id": "tanisma", "title": "Poznajemy się", "partner": "Emre", "avatar": "E", "requires": "ludzie",
     "turns": [
         {"bot": ["merhaba", "!"], "en": "Cześć!",
          "options": [(["merhaba", "!"], True, None), (["pardon", "!"], False, "pardon to „przepraszam”. Powitaj: merhaba.")]},
         {"bot": ["sen", "Türkiye'den", "misin", "?"], "en": "Jesteś z Turcji?",
          "options": [(["hayır", ",", "ben", "Polonya'danım"], True, None),
                      (["hayır", ",", "ben", "Polonya'dansın"], False, "-sın to „ty”. O sobie: -ım.")]},
         {"bot": ["kardeşin", "var", "mı", "?"], "en": "Masz rodzeństwo?",
          "options": [(["evet", ",", "benim", "kardeşim", "var"], True, None),
                      (["evet", ",", "senin", "kardeşim", "var"], False, "senin to „twój”. O sobie: benim.")]},
         {"bot": ["hoşça", "kal", "!"], "build": (["hoşça", "kal", "!"], "Do widzenia!"), "en": "Do widzenia!"},
     ]},
    {"id": "taksi", "title": "W taksówce", "partner": "şoför", "avatar": "Ş", "requires": "miejsca",
     "turns": [
         {"bot": ["iyi", "günler", "!"], "en": "Dzień dobry!",
          "options": [(["iyi", "günler", "!"], True, None), (["iyi", "geceler", "!"], False, "iyi geceler to „dobranoc”. Jest dzień.")]},
         {"bot": ["nereye", "?"], "en": "Dokąd?",
          "options": [(["İstanbul'a", "gidiyorum"], True, None),
                      (["İstanbul'dan", "gidiyorum"], False, "-dan to „z”. Jedziesz do: -a.")]},
         {"bot": ["otel", "orada", "."], "en": "Hotel jest tam.",
          "options": [(["sağda", "?"], True, None), (["burada", "?"], False, "Pytasz o kierunek: sağda.")]},
         {"bot": ["evet", "!"], "build": (["teşekkürler", "!"], "Dziękuję!"), "en": "Tak!"},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'],
    'przyp': ['mianownik', 'biernik (-i)', 'celownik (-e: do)', 'miejscownik (-de: w)', 'ablatyw (-den: z)', 'dopełniacz (-in)'],
    'pos': ['mój', 'twój', 'jego/jej', 'nasz', 'wasz', 'ich'],
    'im': ['-en (który robi)', '-dik (który zrobiono; że robi)', '-ecek (który zrobi)', '-miş (zrobiony)'],
    't_harm': ['ev (dom)', 'okul (szkoła)', 'kitap (książka)', 'sokak (ulica)', 'şehir (miasto)', 'otobüs (autobus)', 'deniz (morze)', 'park (park)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'gelmek (przychodzić): czas teraźniejszy', 'os', 'geliyorum; geliyorsun; geliyor; geliyoruz; geliyorsunuz; geliyorlar', 'Temat + -iyor + końcówka osoby. Samogłoska przed -yor dopasowuje się do tematu.'),
    ('conj', 'Wzory koniugacji', 'yapmak (robić): czas teraźniejszy', 'os', 'yapıyorum; yapıyorsun; yapıyor; yapıyoruz; yapıyorsunuz; yapıyorlar', 'Po a, ı: -ıyor.'),
    ('conj', 'Wzory koniugacji', 'okumak (czytać): czas teraźniejszy', 'os', 'okuyorum; okuyorsun; okuyor; okuyoruz; okuyorsunuz; okuyorlar', 'Po o, u: -uyor.'),
    ('conj', 'Wzory koniugacji', 'görmek (widzieć): czas teraźniejszy', 'os', 'görüyorum; görüyorsun; görüyor; görüyoruz; görüyorsunuz; görüyorlar', 'Po ö, ü: -üyor.'),
    ('conj', 'Wyjątki', 'gitmek (iść)', 'os', 'gidiyorum; gidiyorsun; gidiyor; gidiyoruz; gidiyorsunuz; gidiyorlar', 'Przed samogłoską t → d: git- → gid-.'),
    ('conj', 'Wyjątki', 'istemek (chcieć)', 'os', 'istiyorum; istiyorsun; istiyor; istiyoruz; istiyorsunuz; istiyorlar', 'Końcowe e tematu zwęża się: iste- → isti-.'),
    ('conj', 'Wzory koniugacji', 'gelmek: czas przeszły', 'os', 'geldim; geldin; geldi; geldik; geldiniz; geldiler', 'Temat + -di + końcówka osoby.'),
    ('conj', 'Wzory koniugacji', 'öğrenci (student): „jestem”', 'os', 'öğrenciyim; öğrencisin; öğrenci; öğrenciyiz; öğrencisiniz; öğrenciler', '„Być” to końcówka doklejona do słowa.'),
    ('decl', 'Wzory deklinacji', 'ev (dom)', 'przyp', 'ev; evi; eve; evde; evden; evin', 'Po e, i: końcówki z e, i.'),
    ('decl', 'Wzory deklinacji', 'okul (szkoła)', 'przyp', 'okul; okulu; okula; okulda; okuldan; okulun', 'Po a, ı, o, u: końcówki z a, u.'),
    ('decl', 'Wzory deklinacji', 'göz (oko)', 'przyp', 'göz; gözü; göze; gözde; gözden; gözün', 'Po ö, ü: końcówki z e, ü.'),
    ('decl', 'Wzory deklinacji', 'araba (samochód)', 'przyp', 'araba; arabayı; arabaya; arabada; arabadan; arabanın', 'Po samogłosce wstawia się y, a w dopełniaczu n.'),
    ('decl', 'Wyjątki', 'kitap (książka)', 'przyp', 'kitap; kitabı; kitaba; kitapta; kitaptan; kitabın', 'Przed samogłoską p → b; po bezdźwięcznej -ta, -tan.'),
    ('decl', 'Wyjątki', 'su (woda)', 'przyp', 'su; suyu; suya; suda; sudan; suyun', 'Wyjątek: wstawia się y także w dopełniaczu.'),
    ('decl', 'Końcówki dzierżawcze', 'evim (mój dom)', 'pos', 'evim; evin; evi; evimiz; eviniz; evleri', None),
    ('decl', 'Końcówki dzierżawcze', 'arabam (mój samochód)', 'pos', 'arabam; araban; arabası; arabamız; arabanız; arabaları', 'Po samogłosce: -m, -n, -sı.'),
    ('form', 'Imiesłowy', 'gelmek (przychodzić)', 'im', 'gelen; geldik; gelecek; gelmiş', 'Imiesłowy zastępują zdania względne: gelen adam = człowiek, który przychodzi.'),
    ('form', 'Imiesłowy', 'yapmak (robić)', 'im', 'yapan; yaptık; yapacak; yapmış', None),
    ('form', 'Imiesłowy', 'okumak (czytać)', 'im', 'okuyan; okuduk; okuyacak; okumuş', 'Po samogłosce wstawia się y.'),
    ('form', 'Imiesłowy', 'görmek (widzieć)', 'im', 'gören; gördük; görecek; görmüş', None),
    ('conj', 'Czas przyszły', 'gelmek: czas przyszły', 'os', 'geleceğim; geleceksin; gelecek; geleceğiz; geleceksiniz; gelecekler', 'Przed samogłoską k → ğ.'),
    ('conj', 'Czas teraźniejszy ogólny', 'gelmek: geniş zaman', 'os', 'gelirim; gelirsin; gelir; geliriz; gelirsiniz; gelirler', None),
    ('conj', 'Przeczenie', 'gelmek: nie przychodzę', 'os', 'gelmiyorum; gelmiyorsun; gelmiyor; gelmiyoruz; gelmiyorsunuz; gelmiyorlar', 'Przeczenie to -me- w środku słowa.'),
    ('form', 'Typowe trudności', 'Harmonia: „w…” (-de, -da, -te, -ta)', 't_harm', 'evde; okulda; kitapta; sokakta; şehirde; otobüste; denizde; parkta', 'Po e, i, ö, ü: -de; po a, ı, o, u: -da. Po p, ç, t, k, s, ş, h, f: -te, -ta.'),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['ev', 'okul', 'göz', 'kitap', 'gün', 'çocuk', 'şehir', 'araba'],
    't_m1': ['mam samochód', 'nie mam samochodu', 'masz dom', 'nie masz domu', 'on ma książkę', 'on nie ma książki'],
    't_m2': ['Geliyor ___?', 'Okul ___?', 'Güzel ___?', 'Yok ___?', 'Türk ___?', 'Kadın ___?'],
    't_m3': ['kış', 'kiş', 'sıra', 'sira', 'ılık', 'ilik'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Liczba mnoga: -ler czy -lar?', 't_m0', 'evler; okullar; gözler; kitaplar; günler; çocuklar; şehirler; arabalar', 'Po e, i, ö, ü: -ler. Po a, ı, o, u: -lar.'),
    ('form', 'Typowe trudności', 'Mam, nie mam: var i yok', 't_m1', 'arabam var; arabam yok; evin var; evin yok; kitabı var; kitabı yok', '„Mój samochód jest”: końcówka dzierżawcza + var albo yok.'),
    ('form', 'Typowe trudności', 'Pytanie: mi, mı, mu czy mü?', 't_m2', 'mu; mu; mi; mu; mü; mı', 'Partykuła pytająca też podlega harmonii samogłosek.'),
    ('form', 'Typowe trudności', 'ı czy i: co to znaczy?', 't_m3', 'zima; a kysz!; kolej, rząd; (nie ma takiego słowa); letni (o wodzie); szpik, dziurka na guzik', 'ı bez kropki i i z kropką to różne litery, także wielkie: I oraz İ.'),
]

# Szyk zdania
PARADIGM_LABELS.update({
    't_s0': ['Czytam książkę.', 'Ali idzie do szkoły.', 'Dziś piję herbatę.', 'Moja mama gotuje w domu.'],
    't_s1': ['Książka leży na stole.', 'Jestem z przyjacielem.', 'Idę do szkoły.'],
})
PARADIGMS += [
    ('form', 'Szyk zdania', 'Szyk: czasownik na końcu', 't_s0', 'Ben kitap okuyorum.|Ben okuyorum kitap.|Okuyorum ben kitap.|Okuyorum kitap ben.; Ali okula gidiyor.|Ali gidiyor okula.|Gidiyor Ali okula.|Okula gidiyor Ali.; Bugün çay içiyorum.|Bugün içiyorum çay.|İçiyorum bugün çay.|İçiyorum çay bugün.; Annem evde yemek yapıyor.|Annem yapıyor evde yemek.|Yapıyor annem evde yemek.|Evde yemek yapıyor annem.', 'Szyk podmiot, okolicznik, dopełnienie, orzeczenie. Czasownik zawsze na końcu.'),
    ('form', 'Szyk zdania', 'Szyk: przyimek po rzeczowniku', 't_s1', 'Kitap masanın üstünde.|Kitap üstünde masanın.|Masanın kitap üstünde.|Üstünde masanın kitap.; Arkadaşımla birlikteyim.|Birlikte arkadaşımla.|Arkadaşım birlikteyim.|Birlikteyim arkadaşımla.; Okula gidiyorum.|Gidiyorum okula.|Gidiyorum okul.|Okul gidiyorum.', 'Odpowiedniki naszych przyimków stoją po rzeczowniku (postpozycje) albo są końcówką.'),
]

# === PRONOUNS (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('decl', 'Zaimki', 'ben (ja)', 'przyp', 'ben; beni; bana; bende; benden; benim', 'Zaimek ben ma wyjątkowy celownik: bana.'),
    ('decl', 'Zaimki', 'sen (ty)', 'przyp', 'sen; seni; sana; sende; senden; senin', 'Celownik wyjątkowy: sana.'),
    ('decl', 'Zaimki', 'o (on, ona, ono)', 'przyp', 'o; onu; ona; onda; ondan; onun', 'Turecki nie rozróżnia rodzaju.'),
    ('decl', 'Zaimki', 'biz (my)', 'przyp', 'biz; bizi; bize; bizde; bizden; bizim', None),
    ('decl', 'Zaimki', 'siz (wy)', 'przyp', 'siz; sizi; size; sizde; sizden; sizin', None),
    ('decl', 'Zaimki', 'onlar (oni)', 'przyp', 'onlar; onları; onlara; onlarda; onlardan; onların', None),
    ('decl', 'Zaimki', 'bu (ten tu)', 'przyp', 'bu; bunu; buna; bunda; bundan; bunun', None),
    ('decl', 'Zaimki', 'şu (ten)', 'przyp', 'şu; şunu; şuna; şunda; şundan; şunun', None),
    ('decl', 'Zaimki', 'kim (kto)', 'przyp', 'kim; kimi; kime; kimde; kimden; kimin', None),
    ('decl', 'Zaimki', 'ne (co)', 'przyp', 'ne; neyi; neye; nede; neden; neyin', None),
    ('decl', 'Zaimki', 'okul (szkoła): mój, twój…', 'os', 'okulum; okulun; okulu; okulumuz; okulunuz; okulları', 'Końcówka dzierżawcza zależy od harmonii samogłosek: okul → u-typ.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /PRONOUNS ===

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'ben öğretmenim': 'Jestem nauczycielem.', 'senin ablan var': 'Masz starszą siostrę.', 'ben bir kahve istiyorum': 'Chcę kawę.'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'iyi (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'iyi; daha iyi; en iyi', 'daha = bardziej, en = najbardziej.'),
    ('form', 'Stopniowanie', 'büyük (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'büyük; daha büyük; en büyük', None),
    ('form', 'Stopniowanie', 'küçük (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'küçük; daha küçük; en küçük', None),
    ('form', 'Stopniowanie', 'güzel (piękny)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'güzel; daha güzel; en güzel', None),
    ('form', 'Stopniowanie', 'hızlı (szybki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'hızlı; daha hızlı; en hızlı', None),
    ('form', 'Stopniowanie', 'eski (stary)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'eski; daha eski; en eski', None),
    ('form', 'Stopniowanie', 'kötü (zły)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'kötü; daha kötü; en kötü', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 1 (generowane) ===
PARADIGMS += [
    ('conj', 'Czasy', 'yapmak: geniş zaman', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'yaparım; yaparsın; yapar; yaparız; yaparsınız; yaparlar', None),
    ('conj', 'Czasy', 'okumak: geniş zaman', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'okurum; okursun; okur; okuruz; okursunuz; okurlar', None),
    ('conj', 'Czasy', 'görmek: geniş zaman', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'görürüm; görürsün; görür; görürüz; görürsünüz; görürler', None),
    ('conj', 'Czasy', 'gitmek: geniş zaman', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'giderim; gidersin; gider; gideriz; gidersiniz; giderler', None),
    ('conj', 'Czasy', 'almak: geniş zaman', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'alırım; alırsın; alır; alırız; alırsınız; alırlar', None),
    ('conj', 'Czasy', "gelmek: miş'li geçmiş zaman", ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'gelmişim; gelmişsin; gelmiş; gelmişiz; gelmişsiniz; gelmişler', 'Przeszły „-di” mówi o tym, co widziałeś sam; „-miş” o tym, co usłyszałeś lub zauważyłeś.'),
    ('conj', 'Czasy', "yapmak: miş'li geçmiş zaman", ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'yapmışım; yapmışsın; yapmış; yapmışız; yapmışsınız; yapmışlar', None),
    ('conj', 'Czasy', 'gelmek: przeszły z przeczeniem', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'gelmedim; gelmedin; gelmedi; gelmedik; gelmediniz; gelmediler', None),
    ('conj', 'Czasy', 'yapmak: przeszły', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'yaptım; yaptın; yaptı; yaptık; yaptınız; yaptılar', None),
    ('conj', 'Czasy', 'gitmek: przeszły', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'gittim; gittin; gitti; gittik; gittiniz; gittiler', None),
    ('conj', 'Czasy', 'öğrenci: „byłem”', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'öğrenciydim; öğrenciydin; öğrenciydi; öğrenciydik; öğrenciydiniz; öğrenciydiler', None),
    ('conj', 'Tryby', 'gelmek: możliwość (-ebil-)', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'gelebilirim; gelebilirsin; gelebilir; gelebiliriz; gelebilirsiniz; gelebilirler', None),
    ('conj', 'Tryby', 'gelmek: niemożliwość', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'gelemem; gelemezsin; gelemez; gelemeyiz; gelemezsiniz; gelemezler', None),
    ('conj', 'Tryby', 'yapmak: możliwość (-ebil-)', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'yapabilirim; yapabilirsin; yapabilir; yapabiliriz; yapabilirsiniz; yapabilirler', None),
    ('conj', 'Tryby', 'gelmek: powinność (-meli)', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'gelmeliyim; gelmelisin; gelmeli; gelmeliyiz; gelmelisiniz; gelmeliler', None),
    ('conj', 'Tryby', 'yapmak: powinność (-meli)', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'yapmalıyım; yapmalısın; yapmalı; yapmalıyız; yapmalısınız; yapmalılar', None),
    ('conj', 'Tryby', 'gelmek: warunek (-se)', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'gelsem; gelsen; gelse; gelsek; gelseniz; gelseler', None),
    ('conj', 'Tryby', 'yapmak: warunek (-sa)', ['ben', 'sen', 'o', 'biz', 'siz', 'onlar'], 'yapsam; yapsan; yapsa; yapsak; yapsanız; yapsalar', None),
    ('form', 'Tryb rozkazujący', 'rozkaz: gelmek', ['sen', 'o', 'siz'], 'gel; gelsin; gelin', 'Rozkaz dla „sen” to sam temat czasownika.'),
    ('form', 'Tryb rozkazujący', 'rozkaz: gitmek', ['sen', 'o', 'siz'], 'git; gitsin; gidin', None),
    ('form', 'Tryb rozkazujący', 'rozkaz: yapmak', ['sen', 'o', 'siz'], 'yap; yapsın; yapın', None),
    ('form', 'Tryb rozkazujący', 'rozkaz: okumak', ['sen', 'o', 'siz'], 'oku; okusun; okuyun', None),
    ('form', 'Tryb rozkazujący', 'rozkaz: almak', ['sen', 'o', 'siz'], 'al; alsın; alın', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 1 ===

# === SŁOWNICTWO (generowane z langs/vocab, nie edytuj ręcznie) ===
UNITS += [{'id': 'v01a', 'title': 'Ludzie 1', 'icon': 'L', 'track': 'jezyk', 'words': [('erkek', 'mężczyzna', None, None), ('çocuk', 'dziecko', None, None), ('oğlan', 'chłopiec', None, None), ('kız çocuğu', 'dziewczynka', None, None), ('insan', 'człowiek', None, None), ('insanlar', 'ludzie', None, None), ('aile', 'rodzina', None, None), ('anne', 'matka', None, None), ('baba', 'ojciec', None, None), ('oğul', 'syn', None, None), ('kız evlat', 'córka', None, None), ('erkek kardeş', 'brat', None, None), ('kız kardeş', 'siostra', None, None), ('dede', 'dziadek', None, None), ('nine', 'babcia', None, None), ('torun', 'wnuk', None, None)], 'sentences': []}, {'id': 'v01b', 'title': 'Ludzie 2', 'icon': 'L', 'track': 'jezyk', 'words': [('amca', 'wujek', None, None), ('teyze', 'ciocia', None, None), ('kuzen', 'kuzyn', None, None), ('koca', 'mąż', None, None), ('karı', 'żona', None, None), ('arkadaş', 'przyjaciel', None, None), ('komşu', 'sąsiad', None, None), ('misafir', 'gość', None, None), ('patron', 'szef', None, None), ('iş arkadaşı', 'kolega', None, None), ('düşman', 'wróg', None, None), ('kral', 'król', None, None), ('kraliçe', 'królowa', None, None)], 'sentences': []}, {'id': 'v02a', 'title': 'Ciało 1', 'icon': 'C', 'track': 'jezyk', 'words': [('baş', 'głowa', None, None), ('yüz', 'twarz', None, None), ('göz', 'oko', None, None), ('kulak', 'ucho', None, None), ('burun', 'nos', None, None), ('ağız', 'usta', None, None), ('diş', 'ząb', None, None), ('dil', 'język (narząd)', None, None), ('saç', 'włosy', None, None), ('boyun', 'szyja', None, None), ('omuz', 'ramię', None, None), ('el', 'ręka', None, None), ('parmak', 'palec', None, None), ('bacak', 'noga', None, None), ('ayak', 'stopa', None, None), ('diz', 'kolano', None, None)], 'sentences': []}, {'id': 'v02b', 'title': 'Ciało 2', 'icon': 'C', 'track': 'jezyk', 'words': [('sırt', 'plecy', None, None), ('karın', 'brzuch', None, None), ('kalp', 'serce', None, None), ('kan', 'krew', None, None), ('kemik', 'kość', None, None), ('deri', 'skóra', None, None), ('ses', 'głos', None, None), ('vücut', 'ciało', None, None), ('mide', 'żołądek', None, None), ('sakal', 'broda', None, None), ('dudak', 'warga', None, None), ('tırnak', 'paznokieć', None, None), ('göğüs', 'pierś', None, None), ('beyin', 'mózg', None, None)], 'sentences': []}, {'id': 'v03a', 'title': 'Jedzenie 1', 'icon': 'J', 'track': 'jezyk', 'words': [('tereyağı', 'masło', None, None), ('yumurta', 'jajko', None, None), ('et', 'mięso', None, None), ('tavuk', 'kurczak', None, None), ('domuz eti', 'wieprzowina', None, None), ('çorba', 'zupa', None, None), ('salata', 'sałatka', None, None), ('pirinç', 'ryż', None, None), ('makarna', 'makaron', None, None), ('patates', 'ziemniak', None, None), ('havuç', 'marchewka', None, None), ('soğan', 'cebula', None, None), ('sarımsak', 'czosnek', None, None), ('domates', 'pomidor', None, None), ('salatalık', 'ogórek', None, None), ('armut', 'gruszka', None, None)], 'sentences': []}, {'id': 'v03b', 'title': 'Jedzenie 2', 'icon': 'J', 'track': 'jezyk', 'words': [('muz', 'banan', None, None), ('portakal', 'pomarańcza', None, None), ('limon', 'cytryna', None, None), ('çilek', 'truskawka', None, None), ('üzüm', 'winogrono', None, None), ('şeker', 'cukier', None, None), ('tuz', 'sól', None, None), ('biber', 'pieprz', None, None), ('yağ', 'olej', None, None), ('un', 'mąka', None, None), ('bal', 'miód', None, None), ('çikolata', 'czekolada', None, None), ('dondurma', 'lody', None, None), ('pasta', 'ciasto (tort)', None, None), ('kurabiye', 'ciastko', None, None), ('kahvaltı', 'śniadanie', None, None)], 'sentences': []}, {'id': 'v03c', 'title': 'Jedzenie 3', 'icon': 'J', 'track': 'jezyk', 'words': [('öğle yemeği', 'obiad', None, None), ('akşam yemeği', 'kolacja', None, None), ('atıştırmalık', 'przekąska', None, None)], 'sentences': []}, {'id': 'v04a', 'title': 'Napoje i restauracja 1', 'icon': 'N', 'track': 'jezyk', 'words': [('meyve suyu', 'sok', None, None), ('bira', 'piwo', None, None), ('şarap', 'wino', None, None), ('içecek', 'napój', None, None), ('bardak', 'szklanka', None, None), ('fincan', 'filiżanka', None, None), ('tabak', 'talerz', None, None), ('bıçak', 'nóż', None, None), ('çatal', 'widelec', None, None), ('kaşık', 'łyżka', None, None), ('şişe', 'butelka', None, None), ('menü', 'menu', None, None), ('hesap', 'rachunek', None, None), ('bahşiş', 'napiwek', None, None), ('masa (w restauracji)', 'stolik', None, None), ('garson', 'kelner', None, None)], 'sentences': []}, {'id': 'v04b', 'title': 'Napoje i restauracja 2', 'icon': 'N', 'track': 'jezyk', 'words': [('aşçı', 'kucharz', None, None), ('aç', 'głodny', None, None), ('susamış', 'spragniony', None, None)], 'sentences': []}, {'id': 'v05a', 'title': 'Dom 1', 'icon': 'D', 'track': 'jezyk', 'words': [('daire', 'mieszkanie', None, None), ('oda', 'pokój', None, None), ('mutfak', 'kuchnia', None, None), ('banyo', 'łazienka', None, None), ('yatak odası', 'sypialnia', None, None), ('salon', 'salon', None, None), ('bahçe', 'ogród', None, None), ('kapı', 'drzwi', None, None), ('pencere', 'okno', None, None), ('duvar', 'ściana', None, None), ('zemin', 'podłoga', None, None), ('çatı', 'dach', None, None), ('merdiven', 'schody', None, None), ('anahtar', 'klucz', None, None), ('masa', 'stół', None, None), ('sandalye', 'krzesło', None, None)], 'sentences': []}, {'id': 'v05b', 'title': 'Dom 2', 'icon': 'D', 'track': 'jezyk', 'words': [('yatak', 'łóżko', None, None), ('dolap', 'szafa', None, None), ('lamba', 'lampa', None, None), ('halı', 'dywan', None, None), ('ayna', 'lustro', None, None), ('televizyon', 'telewizor', None, None), ('telefon', 'telefon', None, None), ('bilgisayar', 'komputer', None, None), ('yastık', 'poduszka', None, None), ('battaniye', 'koc', None, None), ('havlu', 'ręcznik', None, None), ('sabun', 'mydło', None, None), ('diş fırçası', 'szczoteczka do zębów', None, None), ('buzdolabı', 'lodówka', None, None), ('fırın', 'piec', None, None), ('çamaşır makinesi', 'pralka', None, None)], 'sentences': []}, {'id': 'v05c', 'title': 'Dom 3', 'icon': 'D', 'track': 'jezyk', 'words': [('çöp', 'śmieci', None, None)], 'sentences': []}, {'id': 'v06a', 'title': 'Ubrania 1', 'icon': 'U', 'track': 'jezyk', 'words': [('giysi', 'ubranie', None, None), ('gömlek', 'koszula', None, None), ('pantolon', 'spodnie', None, None), ('elbise', 'sukienka', None, None), ('etek', 'spódnica', None, None), ('ceket', 'kurtka', None, None), ('palto', 'płaszcz', None, None), ('kazak', 'sweter', None, None), ('ayakkabı', 'buty', None, None), ('çorap', 'skarpetki', None, None), ('şapka', 'czapka', None, None), ('fötr', 'kapelusz', None, None), ('eldiven', 'rękawiczki', None, None), ('atkı', 'szalik', None, None), ('çanta', 'torba', None, None), ('sırt çantası', 'plecak', None, None)], 'sentences': []}, {'id': 'v06b', 'title': 'Ubrania 2', 'icon': 'U', 'track': 'jezyk', 'words': [('cüzdan', 'portfel', None, None), ('gözlük', 'okulary', None, None), ('kol saati', 'zegarek', None, None), ('yüzük', 'pierścionek', None, None), ('iç çamaşırı', 'bielizna', None, None), ('pijama', 'piżama', None, None), ('kemer', 'pasek', None, None), ('kravat', 'krawat', None, None), ('takım elbise', 'garnitur', None, None)], 'sentences': []}, {'id': 'v07a', 'title': 'Kolory i kształty 1', 'icon': 'K', 'track': 'jezyk', 'words': [('kırmızı', 'czerwony', None, None), ('mavi', 'niebieski', None, None), ('yeşil', 'zielony', None, None), ('sarı', 'żółty', None, None), ('siyah', 'czarny', None, None), ('beyaz', 'biały', None, None), ('gri', 'szary', None, None), ('kahverengi', 'brązowy', None, None), ('pembe', 'różowy', None, None), ('mor', 'fioletowy', None, None), ('renk', 'kolor', None, None), ('yuvarlak', 'okrągły', None, None), ('kare', 'kwadratowy', None, None), ('düz', 'prosty', None, None), ('eğri', 'krzywy', None, None), ('çizgi', 'linia', None, None)], 'sentences': []}, {'id': 'v07b', 'title': 'Kolory i kształty 2', 'icon': 'K', 'track': 'jezyk', 'words': [('nokta', 'punkt', None, None)], 'sentences': []}, {'id': 'v08a', 'title': 'Liczby i ilości 1', 'icon': 'L', 'track': 'jezyk', 'words': [('sıfır', 'zero', None, None), ('on bir', 'jedenaście', None, None), ('on iki', 'dwanaście', None, None), ('on üç', 'trzynaście', None, None), ('on dört', 'czternaście', None, None), ('on beş', 'piętnaście', None, None), ('on altı', 'szesnaście', None, None), ('on yedi', 'siedemnaście', None, None), ('on sekiz', 'osiemnaście', None, None), ('on dokuz', 'dziewiętnaście', None, None), ('yirmi', 'dwadzieścia', None, None), ('otuz', 'trzydzieści', None, None), ('kırk', 'czterdzieści', None, None), ('elli', 'pięćdziesiąt', None, None), ('altmış', 'sześćdziesiąt', None, None), ('yetmiş', 'siedemdziesiąt', None, None)], 'sentences': []}, {'id': 'v08b', 'title': 'Liczby i ilości 2', 'icon': 'L', 'track': 'jezyk', 'words': [('seksen', 'osiemdziesiąt', None, None), ('doksan', 'dziewięćdziesiąt', None, None), ('bin', 'tysiąc', None, None), ('milyon', 'milion', None, None), ('birinci', 'pierwszy', None, None), ('ikinci', 'drugi', None, None), ('üçüncü', 'trzeci', None, None), ('yarım', 'połowa', None, None), ('çift', 'para', None, None), ('birkaç', 'kilka', None, None), ('az', 'mało', None, None), ('bütün', 'cały', None, None)], 'sentences': []}, {'id': 'v09a', 'title': 'Czas 1', 'icon': 'C', 'track': 'jezyk', 'words': [('saniye', 'sekunda', None, None), ('dakika', 'minuta', None, None), ('saat (godzina)', 'godzina', None, None), ('gün', 'dzień', None, None), ('gece', 'noc', None, None), ('hafta', 'tydzień', None, None), ('ay', 'miesiąc', None, None), ('yıl', 'rok', None, None), ('ilkbahar', 'wiosna', None, None), ('yaz', 'lato', None, None), ('sonbahar', 'jesień', None, None), ('kış', 'zima', None, None), ('pazartesi', 'poniedziałek', None, None), ('salı', 'wtorek', None, None), ('çarşamba', 'środa', None, None), ('perşembe', 'czwartek', None, None)], 'sentences': []}, {'id': 'v09b', 'title': 'Czas 2', 'icon': 'C', 'track': 'jezyk', 'words': [('cuma', 'piątek', None, None), ('cumartesi', 'sobota', None, None), ('pazar', 'niedziela', None, None), ('ocak', 'styczeń', None, None), ('şubat', 'luty', None, None), ('mart', 'marzec', None, None), ('nisan', 'kwiecień', None, None), ('mayıs', 'maj', None, None), ('haziran', 'czerwiec', None, None), ('temmuz', 'lipiec', None, None), ('ağustos', 'sierpień', None, None), ('eylül', 'wrzesień', None, None), ('ekim', 'październik', None, None), ('kasım', 'listopad', None, None), ('aralık', 'grudzień', None, None), ('sabah', 'rano (pora dnia)', None, None)], 'sentences': []}, {'id': 'v09c', 'title': 'Czas 3', 'icon': 'C', 'track': 'jezyk', 'words': [('öğle', 'południe', None, None), ('akşam', 'wieczorem', None, None), ('her zaman', 'zawsze', None, None), ('asla', 'nigdy', None, None), ('bazen', 'czasem', None, None), ('sık sık', 'często', None, None), ('artık', 'już', None, None), ('henüz', 'jeszcze', None, None), ('yakında', 'wkrótce', None, None), ('sonra', 'później', None, None), ('erken', 'wcześnie', None, None), ('geç', 'późno', None, None), ('ne zaman', 'kiedy (pytanie)', None, None), ('tarih', 'data', None, None), ('geçmiş', 'przeszłość', None, None), ('gelecek', 'przyszłość', None, None)], 'sentences': []}, {'id': 'v09d', 'title': 'Czas 4', 'icon': 'C', 'track': 'jezyk', 'words': [('doğum günü', 'urodziny', None, None), ('bayram', 'święto', None, None), ('tatil', 'wakacje', None, None)], 'sentences': []}, {'id': 'v10a', 'title': 'Natura i pogoda 1', 'icon': 'N', 'track': 'jezyk', 'words': [('güneş', 'słońce', None, None), ('ay (ciało niebieskie)', 'księżyc', None, None), ('yıldız', 'gwiazda', None, None), ('gökyüzü', 'niebo', None, None), ('bulut', 'chmura', None, None), ('yağmur', 'deszcz', None, None), ('kar', 'śnieg', None, None), ('rüzgâr', 'wiatr', None, None), ('fırtına', 'burza', None, None), ('sis', 'mgła', None, None), ('buz', 'lód', None, None), ('ateş, ziemia (planeta', 'ogień', None, None), ('toprak', 'grunt)', None, None), ('nehir', 'rzeka', None, None), ('göl', 'jezioro', None, None), ('dağ', 'góra', None, None)], 'sentences': []}, {'id': 'v10b', 'title': 'Natura i pogoda 2', 'icon': 'N', 'track': 'jezyk', 'words': [('orman', 'las', None, None), ('ağaç', 'drzewo', None, None), ('çiçek', 'kwiat', None, None), ('çim', 'trawa', None, None), ('yaprak', 'liść', None, None), ('tarla', 'pole', None, None), ('ada', 'wyspa', None, None), ('plaj', 'plaża', None, None), ('çöl', 'pustynia', None, None), ('kaya', 'skała', None, None), ('taş', 'kamień', None, None), ('hava', 'pogoda', None, None), ('sıcaklık', 'temperatura', None, None), ('soğuk', 'zimny', None, None), ('ılık', 'ciepły', None, None), ('sıcak', 'gorący', None, None)], 'sentences': []}, {'id': 'v11a', 'title': 'Zwierzęta 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('köpek', 'pies', None, None), ('kedi', 'kot', None, None), ('at', 'koń', None, None), ('inek', 'krowa', None, None), ('domuz', 'świnia', None, None), ('koyun', 'owca', None, None), ('keçi', 'koza', None, None), ('tavuk (kura)', 'kura', None, None), ('ördek', 'kaczka', None, None), ('kuş', 'ptak', None, None), ('fare', 'mysz', None, None), ('sıçan', 'szczur', None, None), ('yılan', 'wąż', None, None), ('kurbağa', 'żaba', None, None), ('aslan', 'lew', None, None), ('kaplan', 'tygrys', None, None)], 'sentences': []}, {'id': 'v11b', 'title': 'Zwierzęta 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('fil', 'słoń', None, None), ('ayı', 'niedźwiedź', None, None), ('kurt', 'wilk', None, None), ('tilki', 'lis', None, None), ('tavşan', 'zając', None, None), ('geyik', 'jeleń', None, None), ('maymun', 'małpa', None, None), ('kelebek', 'motyl', None, None), ('arı', 'pszczoła', None, None), ('sinek', 'mucha', None, None), ('örümcek', 'pająk', None, None), ('hayvan', 'zwierzę', None, None), ('böcek', 'owad', None, None)], 'sentences': []}, {'id': 'v12a', 'title': 'Miasto 1', 'icon': 'M', 'track': 'jezyk', 'words': [('köy', 'wieś', None, None), ('yol', 'droga', None, None), ('meydan', 'plac', None, None), ('köprü', 'most', None, None), ('park', 'park', None, None), ('dükkân', 'sklep', None, None), ('pazar (targ)', 'targ', None, None), ('süpermarket', 'supermarket', None, None), ('banka', 'bank', None, None), ('postane', 'poczta', None, None), ('hastane', 'szpital', None, None), ('eczane', 'apteka', None, None), ('üniversite', 'uniwersytet', None, None), ('kütüphane', 'biblioteka', None, None), ('müze', 'muzeum', None, None), ('kilise', 'kościół', None, None)], 'sentences': []}, {'id': 'v12b', 'title': 'Miasto 2', 'icon': 'M', 'track': 'jezyk', 'words': [('restoran', 'restauracja', None, None), ('kafe', 'kawiarnia', None, None), ('havalimanı', 'lotnisko', None, None), ('gar', 'dworzec', None, None), ('durak', 'przystanek', None, None), ('sinema', 'kino', None, None), ('tiyatro', 'teatr', None, None), ('polis', 'policja', None, None), ('ofis', 'biuro', None, None), ('fabrika', 'fabryka', None, None), ('bina', 'budynek', None, None), ('kule', 'wieża', None, None), ('merkez', 'centrum', None, None), ('adres', 'adres', None, None), ('harita', 'mapa', None, None)], 'sentences': []}, {'id': 'v13a', 'title': 'Transport i podróż 1', 'icon': 'T', 'track': 'jezyk', 'words': [('araba', 'samochód', None, None), ('otobüs', 'autobus', None, None), ('tren', 'pociąg', None, None), ('tramvay', 'tramwaj', None, None), ('metro', 'metro', None, None), ('uçak', 'samolot', None, None), ('gemi', 'statek', None, None), ('bisiklet', 'rower', None, None), ('motosiklet', 'motocykl', None, None), ('bilet', 'bilet', None, None), ('yolculuk', 'podróż', None, None), ('gezi', 'wycieczka', None, None), ('pasaport', 'paszport', None, None), ('bavul', 'walizka', None, None), ('benzin', 'benzyna', None, None), ('otopark', 'parking', None, None)], 'sentences': []}, {'id': 'v13b', 'title': 'Transport i podróż 2', 'icon': 'T', 'track': 'jezyk', 'words': [('kavşak', 'skrzyżowanie', None, None), ('trafik ışığı', 'światła', None, None), ('ehliyet', 'prawo jazdy', None, None), ('şoför', 'kierowca', None, None), ('yolcu', 'pasażer', None, None), ('giriş', 'wjazd', None, None), ('çıkış', 'wyjazd', None, None), ('demiryolu', 'kolej', None, None), ('liman', 'port', None, None), ('sınır', 'granica', None, None)], 'sentences': []}, {'id': 'v14a', 'title': 'Praca i szkoła 1', 'icon': 'P', 'track': 'jezyk', 'words': [('iş', 'praca', None, None), ('meslek', 'zawód', None, None), ('doktor', 'lekarz', None, None), ('hemşire', 'pielęgniarka', None, None), ('üniversite öğrencisi', 'student', None, None), ('mühendis', 'inżynier', None, None), ('avukat', 'prawnik', None, None), ('polis memuru', 'policjant', None, None), ('asker', 'żołnierz', None, None), ('çiftçi', 'rolnik', None, None), ('satıcı', 'sprzedawca', None, None), ('kasiyer', 'kasjer', None, None), ('oyuncu', 'aktor', None, None), ('yazar', 'pisarz', None, None), ('ressam', 'malarz', None, None), ('müzisyen', 'muzyk', None, None)], 'sentences': []}, {'id': 'v14b', 'title': 'Praca i szkoła 2', 'icon': 'P', 'track': 'jezyk', 'words': [('sanatçı', 'artysta', None, None), ('şirket', 'firma', None, None), ('para', 'pieniądze', None, None), ('maaş', 'pensja', None, None), ('sözleşme', 'umowa', None, None), ('toplantı', 'spotkanie', None, None), ('ders', 'lekcja', None, None), ('sınav', 'egzamin', None, None), ('not', 'ocena', None, None), ('sınıf', 'klasa', None, None), ('kitap', 'książka', None, None), ('defter', 'zeszyt', None, None), ('tükenmez kalem', 'długopis', None, None), ('kurşun kalem', 'ołówek', None, None), ('kâğıt', 'papier', None, None), ('tahta', 'tablica', None, None)], 'sentences': []}, {'id': 'v14c', 'title': 'Praca i szkoła 3', 'icon': 'P', 'track': 'jezyk', 'words': [('sözlük', 'słownik', None, None), ('soru', 'pytanie', None, None), ('cevap', 'odpowiedź', None, None), ('ödev', 'zadanie', None, None), ('test', 'test', None, None)], 'sentences': []}, {'id': 'v15a', 'title': 'Pieniądze i zakupy 1', 'icon': 'P', 'track': 'jezyk', 'words': [('fiyat', 'cena', None, None), ('kredi kartı', 'karta (płatnicza)', None, None), ('nakit', 'gotówka', None, None), ('bozuk para', 'moneta', None, None), ('banknot', 'banknot', None, None), ('para üstü', 'reszta', None, None), ('indirim', 'zniżka', None, None), ('sepet', 'koszyk', None, None), ('fiş', 'paragon', None, None), ('mal', 'towar', None, None), ('alışveriş', 'zakup', None, None), ('satış', 'sprzedaż', None, None), ('değer', 'wartość', None, None), ('kredi', 'kredyt', None, None), ('borç', 'dług', None, None), ('vergi', 'podatek', None, None)], 'sentences': []}, {'id': 'v15b', 'title': 'Pieniądze i zakupy 2', 'icon': 'P', 'track': 'jezyk', 'words': [('zenginlik', 'bogactwo', None, None), ('fakir', 'biedny', None, None), ('zengin', 'bogaty', None, None)], 'sentences': []}, {'id': 'v16a', 'title': 'Zdrowie 1', 'icon': 'Z', 'track': 'jezyk', 'words': [('sağlık', 'zdrowie', None, None), ('hastalık', 'choroba', None, None), ('ağrı', 'ból', None, None), ('ateş', 'gorączka', None, None), ('öksürük', 'kaszel', None, None), ('nezle', 'katar', None, None), ('ilaç', 'lekarstwo', None, None), ('hap', 'tabletka', None, None), ('ameliyat', 'operacja', None, None), ('yara', 'rana', None, None), ('kaza', 'wypadek', None, None), ('sağlıklı', 'zdrowy', None, None), ('hasta', 'chory', None, None), ('yorgun', 'zmęczony', None, None), ('uykulu', 'śpiący', None, None), ('güçlü', 'silny', None, None)], 'sentences': []}, {'id': 'v16b', 'title': 'Zdrowie 2', 'icon': 'Z', 'track': 'jezyk', 'words': [('zayıf', 'słaby', None, None)], 'sentences': []}, {'id': 'v17a', 'title': 'Uczucia i charakter 1', 'icon': 'U', 'track': 'jezyk', 'words': [('sevinç', 'radość', None, None), ('üzüntü', 'smutek', None, None), ('korku', 'strach', None, None), ('öfke', 'gniew', None, None), ('aşk', 'miłość', None, None), ('nefret', 'nienawiść', None, None), ('umut', 'nadzieja', None, None), ('hayal', 'marzenie', None, None), ('mutluluk', 'szczęście', None, None), ('utanç', 'wstyd', None, None), ('şaşkınlık', 'zdziwienie', None, None), ('merak', 'ciekawość', None, None), ('sabır', 'cierpliwość', None, None), ('cesaret', 'odwaga', None, None), ('samimi', 'szczery', None, None), ('nazik', 'miły', None, None)], 'sentences': []}, {'id': 'v17b', 'title': 'Uczucia i charakter 2', 'icon': 'U', 'track': 'jezyk', 'words': [('kibar', 'grzeczny', None, None), ('aptal', 'głupi', None, None), ('akıllı', 'mądry', None, None), ('tembel', 'leniwy', None, None), ('çalışkan', 'pracowity', None, None), ('ilginç', 'ciekawy', None, None), ('sıkıcı', 'nudny', None, None), ('neşeli', 'wesoły', None, None), ('üzgün', 'smutny', None, None), ('kızgın', 'zły (rozgniewany)', None, None), ('mutlu', 'szczęśliwy', None, None), ('aşık', 'zakochany', None, None), ('yalnız', 'samotny', None, None), ('sakin', 'spokojny', None, None)], 'sentences': []}, {'id': 'v18a', 'title': 'Przymiotniki 1', 'icon': 'P', 'track': 'jezyk', 'words': [('büyük', 'duży', None, None), ('uzun', 'długi', None, None), ('kısa', 'krótki', None, None), ('yüksek', 'wysoki', None, None), ('alçak', 'niski', None, None), ('geniş', 'szeroki', None, None), ('dar', 'wąski', None, None), ('kalın', 'gruby', None, None), ('zayıf (chudy)', 'chudy', None, None), ('ağır', 'ciężki', None, None), ('hafif', 'lekki', None, None), ('hızlı', 'szybki', None, None), ('yavaş', 'wolny', None, None), ('sert', 'twardy', None, None), ('yumuşak', 'miękki', None, None), ('ıslak', 'mokry', None, None)], 'sentences': []}, {'id': 'v18b', 'title': 'Przymiotniki 2', 'icon': 'P', 'track': 'jezyk', 'words': [('kuru', 'suchy', None, None), ('temiz', 'czysty', None, None), ('kirli', 'brudny', None, None), ('dolu', 'pełny', None, None), ('boş', 'pusty', None, None), ('keskin', 'ostry', None, None), ('gürültülü', 'głośny', None, None), ('sessiz', 'cichy', None, None), ('aydınlık', 'jasny', None, None), ('karanlık', 'ciemny', None, None), ('genç', 'młody', None, None), ('yaşlı', 'stary', None, None), ('yeni', 'nowy', None, None), ('kötü', 'zły (niedobry)', None, None), ('çirkin', 'brzydki', None, None), ('kolay', 'łatwy', None, None)], 'sentences': []}, {'id': 'v18c', 'title': 'Przymiotniki 3', 'icon': 'P', 'track': 'jezyk', 'words': [('zor', 'trudny', None, None), ('önemli', 'ważny', None, None), ('mümkün', 'możliwy', None, None), ('gerçek', 'prawdziwy', None, None), ('sahte', 'fałszywy', None, None), ('pahalı', 'drogi', None, None), ('ucuz', 'tani', None, None)], 'sentences': []}, {'id': 'v19a', 'title': 'Czasowniki podstawowe 1', 'icon': 'C', 'track': 'jezyk', 'words': [('olmak', 'być', None, None), ('sahip olmak', 'mieć', None, None), ('yapmak', 'robić', None, None), ('gitmek', 'iść', None, None), ('binmek', 'jechać', None, None), ('gelmek', 'przyjść', None, None), ('çıkmak', 'wyjść', None, None), ('girmek', 'wejść', None, None), ('dönmek', 'wrócić', None, None), ('koşmak', 'biec', None, None), ('ayakta durmak', 'stać', None, None), ('oturmak', 'siedzieć', None, None), ('yatmak', 'leżeć', None, None), ('uyumak', 'spać', None, None), ('kalkmak', 'wstać', None, None), ('yemek', 'jeść', None, None)], 'sentences': []}, {'id': 'v19b', 'title': 'Czasowniki podstawowe 2', 'icon': 'C', 'track': 'jezyk', 'words': [('içmek', 'pić', None, None), ('pişirmek', 'gotować', None, None), ('yıkamak', 'myć', None, None), ('giyinmek', 'ubierać się', None, None), ('konuşmak', 'mówić', None, None), ('söylemek', 'powiedzieć', None, None), ('sormak', 'pytać', None, None), ('cevaplamak', 'odpowiadać', None, None), ('duymak', 'słyszeć', None, None), ('dinlemek', 'słuchać', None, None), ('görmek', 'widzieć', None, None), ('bakmak', 'patrzeć', None, None), ('okumak', 'czytać', None, None), ('yazmak', 'pisać', None, None), ('öğrenmek', 'uczyć się', None, None), ('öğretmek', 'uczyć (kogoś)', None, None)], 'sentences': []}, {'id': 'v19c', 'title': 'Czasowniki podstawowe 3', 'icon': 'C', 'track': 'jezyk', 'words': [('anlamak', 'rozumieć', None, None), ('bilmek', 'wiedzieć', None, None), ('tanımak', 'znać', None, None), ('düşünmek', 'myśleć', None, None), ('hatırlamak', 'pamiętać', None, None), ('unutmak', 'zapominać', None, None), ('istemek', 'chcieć', None, None), ('sevmek', 'lubić', None, None), ('aşık olmak', 'kochać', None, None), ('ihtiyaç duymak', 'potrzebować', None, None), ('bilmek (móc)', 'móc', None, None), ('zorunda olmak', 'musieć', None, None), ('vermek', 'dawać', None, None), ('almak', 'brać', None, None), ('satın almak', 'kupować', None, None), ('satmak', 'sprzedawać', None, None)], 'sentences': []}, {'id': 'v19d', 'title': 'Czasowniki podstawowe 4', 'icon': 'C', 'track': 'jezyk', 'words': [('ödemek', 'płacić', None, None), ('açmak', 'otwierać', None, None), ('kapatmak', 'zamykać', None, None), ('başlamak', 'zaczynać', None, None), ('bitirmek', 'kończyć', None, None), ('çalışmak', 'pracować', None, None), ('oynamak', 'grać', None, None), ('şarkı söylemek', 'śpiewać', None, None), ('dans etmek', 'tańczyć', None, None), ('yüzmek', 'pływać', None, None), ('uçmak', 'latać', None, None), ('koymak', 'kłaść', None, None), ('aramak', 'szukać', None, None), ('bulmak', 'znajdować', None, None), ('beklemek', 'czekać', None, None), ('yardım etmek', 'pomagać', None, None)], 'sentences': []}, {'id': 'v19e', 'title': 'Czasowniki podstawowe 5', 'icon': 'C', 'track': 'jezyk', 'words': [('rica etmek', 'prosić', None, None), ('özür dilemek', 'przepraszać', None, None), ('izin vermek', 'pozwalać', None, None), ('denemek', 'próbować', None, None), ('değiştirmek', 'zmieniać', None, None), ('taşımak', 'nosić', None, None), ('tutmak', 'trzymać', None, None), ('atmak', 'rzucać', None, None), ('yakalamak', 'łapać', None, None), ('dövmek', 'bić', None, None), ('öldürmek', 'zabijać', None, None), ('ölmek', 'umierać', None, None), ('yaşamak', 'żyć', None, None), ('oturmak (mieszkać)', 'mieszkać', None, None), ('buluşmak', 'spotykać', None, None), ('aramak (dzwonić)', 'dzwonić', None, None)], 'sentences': []}, {'id': 'v19f', 'title': 'Czasowniki podstawowe 6', 'icon': 'C', 'track': 'jezyk', 'words': [('göndermek', 'wysyłać', None, None), ('almak (dostawać)', 'dostawać', None, None), ('göstermek', 'pokazywać', None, None), ('davet etmek', 'zapraszać', None, None), ('ziyaret etmek', 'odwiedzać', None, None), ('ağlamak', 'płakać', None, None), ('gülmek', 'śmiać się', None, None), ('gülümsemek', 'uśmiechać się', None, None), ('korkmak', 'bać się', None, None), ('sevinmek', 'cieszyć się', None, None), ('inanmak', 'wierzyć', None, None), ('katılmak', 'zgadzać się', None, None), ('seçmek', 'wybierać', None, None), ('karar vermek', 'decydować', None, None), ('saymak', 'liczyć', None, None), ('tartmak', 'ważyć', None, None)], 'sentences': []}, {'id': 'v20a', 'title': 'Czasowniki dnia codziennego 1', 'icon': 'C', 'track': 'jezyk', 'words': [('yürümek', 'chodzić', None, None), ('sürmek', 'jeździć', None, None), ('binmek (wsiadać)', 'wsiadać', None, None), ('inmek', 'wysiadać', None, None), ('dönmek (skręcać)', 'skręcać', None, None), ('durmak', 'zatrzymywać się', None, None), ('geç kalmak', 'spóźniać się', None, None), ('acele etmek', 'spieszyć się', None, None), ('dinlenmek', 'odpoczywać', None, None), ('eğlenmek', 'bawić się', None, None), ('çizmek', 'rysować', None, None), ('inşa etmek', 'budować', None, None), ('tamir etmek', 'naprawiać', None, None), ('kesmek', 'ciąć', None, None), ('kızartmak', 'smażyć', None, None), ('fırınlamak', 'piec', None, None)], 'sentences': []}, {'id': 'v20b', 'title': 'Czasowniki dnia codziennego 2', 'icon': 'C', 'track': 'jezyk', 'words': [('karıştırmak', 'mieszać', None, None), ('dökmek', 'nalewać', None, None), ('temizlemek', 'sprzątać', None, None), ('çamaşır yıkamak', 'prać', None, None), ('ütülemek', 'prasować', None, None), ('tıraş olmak', 'golić się', None, None), ('taramak', 'czesać', None, None), ('banyo yapmak', 'kąpać się', None, None), ('uyanmak', 'budzić się', None, None), ('uykuya dalmak', 'zasypiać', None, None), ('hayal etmek', 'marzyć', None, None), ('rüya görmek', 'śnić', None, None), ('egzersiz yapmak', 'ćwiczyć', None, None), ('antrenman yapmak', 'trenować', None, None), ('kazanmak', 'wygrywać', None, None), ('kaybetmek', 'przegrywać', None, None)], 'sentences': []}, {'id': 'v20c', 'title': 'Czasowniki dnia codziennego 3', 'icon': 'C', 'track': 'jezyk', 'words': [('kıpırdatmak', 'ruszać', None, None), ('çekmek', 'ciągnąć', None, None), ('itmek', 'pchać', None, None), ('kaldırmak', 'podnosić', None, None), ('düşmek', 'spadać', None, None), ('zıplamak', 'skakać', None, None), ('tırmanmak', 'wspinać się', None, None), ('saklamak', 'ukrywać', None, None), ('çalmak', 'kraść', None, None), ('geri vermek', 'oddawać', None, None), ('ödünç vermek', 'pożyczać', None, None), ('harcamak', 'wydawać', None, None), ('biriktirmek', 'oszczędzać', None, None)], 'sentences': []}, {'id': 'v21a', 'title': 'Słowa funkcyjne 1', 'icon': 'S', 'track': 'jezyk', 'words': [('bu', 'ten', None, None), ('şu', 'tamten', None, None), ('nasıl', 'jak', None, None), ('neden', 'dlaczego', None, None), ('ne', 'co', None, None), ('kim', 'kto', None, None), ('hangi', 'który', None, None), ('nasıl bir', 'jaki', None, None), ('ama', 'ale', None, None), ('veya', 'lub', None, None), ('çünkü', 'bo', None, None), ('eğer', 'jeśli', None, None), ('ki', 'że', None, None), ('bu yüzden', 'więc', None, None), ('de', 'też', None, None), ('sadece', 'tylko', None, None)], 'sentences': []}, {'id': 'v21b', 'title': 'Słowa funkcyjne 2', 'icon': 'S', 'track': 'jezyk', 'words': [('biraz', 'trochę', None, None), ('çok (dużo)', 'dużo', None, None), ('her şey', 'wszystko', None, None), ('hiçbir şey', 'nic', None, None), ('bir şey', 'coś', None, None), ('birisi', 'ktoś', None, None), ('hiç kimse', 'nikt', None, None), ('her', 'każdy', None, None), ('başka', 'inny', None, None), ('aynı', 'ten sam', None, None), ('belki', 'może (być)', None, None), ('kesinlikle', 'na pewno', None, None), ('birlikte', 'razem', None, None), ('kendi', 'sam', None, None), ('-sız', 'bez', None, None), ('ile', 'z (towarzysząc)', None, None)], 'sentences': []}, {'id': 'v21c', 'title': 'Słowa funkcyjne 3', 'icon': 'S', 'track': 'jezyk', 'words': [('içinde', 'w (miejsce)', None, None), ('üstünde', 'na (powierzchni)', None, None), ('-e doğru', 'do (kierunek)', None, None), ('-den beri', 'od', None, None), ('için', 'dla', None, None), ('boyunca', 'przez', None, None), ('-den sonra', 'po (czas)', None, None), ('önce', 'przed', None, None), ('arkasında', 'za (z tyłu)', None, None), ('üzerinde', 'nad', None, None), ('altında', 'pod', None, None), ('yanında', 'obok', None, None), ('arasında', 'między', None, None), ('karşı', 'przeciw', None, None), ('hakkında', 'o (temat)', None, None), ('yanında (u)', 'u (przy)', None, None)], 'sentences': []}, {'id': 'v21d', 'title': 'Słowa funkcyjne 4', 'icon': 'S', 'track': 'jezyk', 'words': [('yaklaşık', 'około', None, None), ('neredeyse', 'prawie', None, None), ('bile', 'nawet', None, None), ('tekrar', 'jeszcze raz', None, None), ('o zaman', 'wtedy', None, None), ('bir yerde', 'gdzieś', None, None), ('hiçbir yerde', 'nigdzie', None, None), ('her yerde', 'wszędzie', None, None)], 'sentences': []}, {'id': 'v22a', 'title': 'Świat i społeczeństwo 1', 'icon': 'Ś', 'track': 'jezyk', 'words': [('hayat', 'życie', None, None), ('ölüm', 'śmierć', None, None), ('dünya', 'świat', None, None), ('ülke', 'kraj', None, None), ('devlet', 'państwo', None, None), ('lisan', 'język (mowa)', None, None), ('kelime', 'słowo', None, None), ('cümle', 'zdanie', None, None), ('isim', 'imię', None, None), ('soyadı', 'nazwisko', None, None), ('yaş', 'wiek', None, None), ('tarih (historia)', 'historia', None, None), ('kültür', 'kultura', None, None), ('din', 'religia', None, None), ('Tanrı', 'Bóg', None, None), ('savaş', 'wojna', None, None)], 'sentences': []}, {'id': 'v22b', 'title': 'Świat i społeczeństwo 2', 'icon': 'Ś', 'track': 'jezyk', 'words': [('barış', 'pokój (brak wojny)', None, None), ('yasa', 'prawo (przepis)', None, None), ('özgürlük', 'wolność', None, None), ('iktidar', 'władza', None, None), ('hükümet', 'rząd', None, None), ('seçim', 'wybory', None, None), ('sorun', 'problem', None, None), ('fikir', 'pomysł', None, None), ('sebep', 'powód', None, None), ('sonuç', 'wynik', None, None), ('yöntem', 'sposób', None, None), ('başlangıç', 'początek', None, None), ('son', 'koniec', None, None), ('bölüm', 'część', None, None), ('yer', 'miejsce', None, None), ('şey', 'rzecz', None, None)], 'sentences': []}, {'id': 'v22c', 'title': 'Świat i społeczeństwo 3', 'icon': 'Ś', 'track': 'jezyk', 'words': [('mesele', 'sprawa', None, None), ('bilgi', 'informacja', None, None), ('mesaj', 'wiadomość', None, None), ('mektup', 'list', None, None), ('gazete', 'gazeta', None, None), ('film', 'film', None, None), ('müzik', 'muzyka', None, None), ('şarkı', 'piosenka', None, None), ('resim', 'obraz', None, None), ('oyun', 'gra', None, None), ('spor', 'sport', None, None), ('maç', 'mecz', None, None), ('takım', 'drużyna', None, None), ('top', 'piłka', None, None), ('eğlence', 'zabawa', None, None), ('parti', 'impreza', None, None)], 'sentences': []}, {'id': 'v22d', 'title': 'Świat i społeczeństwo 4', 'icon': 'Ś', 'track': 'jezyk', 'words': [('hediye', 'prezent', None, None), ('rüya', 'sen', None, None), ('plan', 'plan', None, None), ('seçenek', 'wybór', None, None), ('hata', 'błąd', None, None), ('gerçek (prawda)', 'prawda', None, None), ('yalan', 'kłamstwo', None, None), ('sır', 'tajemnica', None, None), ('kuvvet', 'siła', None, None), ('enerji', 'energia', None, None), ('ışık', 'światło', None, None), ('sesli (dźwięk)', 'dźwięk', None, None), ('sessizlik', 'cisza', None, None), ('hareket', 'ruch', None, None), ('değişim', 'zmiana', None, None), ('fark', 'różnica', None, None)], 'sentences': []}, {'id': 'v22e', 'title': 'Świat i społeczeństwo 5', 'icon': 'Ś', 'track': 'jezyk', 'words': [('örnek', 'przykład', None, None), ('bütünlük', 'całość', None, None)], 'sentences': []}, {'id': 'v23a', 'title': 'Technologia 1', 'icon': 'T', 'track': 'jezyk', 'words': [('internet', 'internet', None, None), ('e-posta', 'e-mail', None, None), ('şifre', 'hasło', None, None), ('web sitesi', 'strona internetowa', None, None), ('program', 'program', None, None), ('uygulama', 'aplikacja', None, None), ('ekran', 'ekran', None, None), ('klavye', 'klawiatura', None, None), ('dosya', 'plik', None, None), ('fotoğraf', 'zdjęcie', None, None), ('kamera', 'kamera', None, None), ('pil', 'bateria', None, None), ('elektrik', 'prąd', None, None), ('kablo', 'kabel', None, None), ('makine', 'maszyna', None, None), ('alet', 'narzędzie', None, None)], 'sentences': []}, {'id': 'v23b', 'title': 'Technologia 2', 'icon': 'T', 'track': 'jezyk', 'words': [('çekiç', 'młotek', None, None), ('yazıcı', 'drukarka', None, None), ('şarj aleti', 'ładowarka', None, None)], 'sentences': []}, {'id': 'v24a', 'title': 'Geografia 1', 'icon': 'G', 'track': 'jezyk', 'words': [('kuzey', 'północ', None, None), ('güney', 'południe (kierunek)', None, None), ('doğu', 'wschód', None, None), ('batı', 'zachód', None, None), ('Polonya', 'Polska', None, None), ('Avrupa', 'Europa', None, None), ('Almanya', 'Niemcy', None, None), ('Fransa', 'Francja', None, None), ('İtalya', 'Włochy', None, None), ('İspanya', 'Hiszpania', None, None), ('Rusya', 'Rosja', None, None), ('İngiltere', 'Anglia', None, None), ('Amerika', 'Ameryka', None, None), ('Çin', 'Chiny', None, None), ('Japonya', 'Japonia', None, None), ('Afrika', 'Afryka', None, None)], 'sentences': []}, {'id': 'v24b', 'title': 'Geografia 2', 'icon': 'G', 'track': 'jezyk', 'words': [('Asya', 'Azja', None, None), ('kıta', 'kontynent', None, None), ('başkent', 'stolica', None, None), ('vatandaş', 'obywatel', None, None)], 'sentences': []}, {'id': 'v25a', 'title': 'Materiały i przedmioty 1', 'icon': 'M', 'track': 'jezyk', 'words': [('parça', 'kawałek', None, None), ('damla', 'kropla', None, None), ('kutu', 'pudełko', None, None), ('çuval', 'worek', None, None), ('iplik', 'nić', None, None), ('tel', 'drut', None, None), ('iğne', 'igła', None, None), ('makas', 'nożyczki', None, None), ('sopa', 'kij', None, None), ('ip', 'lina', None, None), ('zincir', 'łańcuch', None, None), ('vida', 'śruba', None, None), ('çivi', 'gwóźdź', None, None), ('yapıştırıcı', 'klej', None, None), ('boya', 'farba', None, None), ('cam', 'szkło', None, None)], 'sentences': []}, {'id': 'v25b', 'title': 'Materiały i przedmioty 2', 'icon': 'M', 'track': 'jezyk', 'words': [('odun', 'drewno', None, None), ('metal', 'metal', None, None), ('altın', 'złoto', None, None), ('gümüş', 'srebro', None, None), ('demir', 'żelazo', None, None), ('plastik', 'plastik', None, None), ('deri (materiał)', 'skóra (materiał)', None, None), ('pamuk', 'bawełna', None, None), ('yün', 'wełna', None, None), ('kum', 'piasek', None, None), ('çamur', 'błoto', None, None), ('toz', 'kurz', None, None), ('duman', 'dym', None, None), ('buhar', 'para (wodna)', None, None)], 'sentences': []}, {'id': 'v26a', 'title': 'Kierunki i miejsca 1', 'icon': 'K', 'track': 'jezyk', 'words': [('yukarı', 'góra (kierunek)', None, None), ('aşağı', 'dół', None, None), ('ön', 'przód', None, None), ('arka', 'tył', None, None), ('orta', 'środek', None, None), ('yan', 'bok', None, None), ('iç', 'wewnątrz', None, None), ('dış', 'na zewnątrz', None, None), ('uzak', 'daleko', None, None), ('yakın', 'blisko', None, None), ('yüksekte', 'wysoko', None, None), ('alçakta', 'nisko', None, None), ('çabuk', 'szybko', None, None), ('yavaşça', 'wolno', None, None), ('iyi (dobrze)', 'dobrze', None, None), ('kötü (źle)', 'źle', None, None)], 'sentences': []}, {'id': 'v26b', 'title': 'Kierunki i miejsca 2', 'icon': 'K', 'track': 'jezyk', 'words': [('kolayca', 'łatwo', None, None), ('zorla', 'trudno', None, None), ('ayrı', 'osobno', None, None), ('karşısında', 'naprzeciw', None, None), ('çapraz', 'w poprzek', None, None), ('etrafında', 'dokoła', None, None)], 'sentences': []}, {'id': 'v27a', 'title': 'Więcej jedzenia 1', 'icon': 'W', 'track': 'jezyk', 'words': [('lahana', 'kapusta', None, None), ('bezelye', 'groszek', None, None), ('fasulye', 'fasola', None, None), ('mantar', 'grzyb', None, None), ('ceviz', 'orzech', None, None), ('erik', 'śliwka', None, None), ('vişne', 'wiśnia', None, None), ('şeftali', 'brzoskwinia', None, None), ('karpuz', 'arbuz', None, None), ('ahududu', 'malina', None, None), ('sosis', 'kiełbasa', None, None), ('jambon', 'szynka', None, None), ('çörek', 'bułka', None, None), ('sandviç', 'kanapka', None, None), ('krep', 'naleśnik', None, None), ('yoğurt', 'jogurt', None, None)], 'sentences': []}, {'id': 'v27b', 'title': 'Więcej jedzenia 2', 'icon': 'W', 'track': 'jezyk', 'words': [('krema', 'śmietana', None, None), ('sos', 'sos', None, None), ('sirke', 'ocet', None, None), ('maya', 'drożdże', None, None), ('muhallebi', 'kisiel', None, None), ('jöle', 'galaretka', None, None), ('kuru üzüm', 'rodzynek', None, None), ('badem', 'migdał', None, None), ('maydanoz', 'pietruszka', None, None), ('dereotu', 'koperek', None, None), ('dolmalık biber', 'papryka', None, None), ('marul', 'sałata', None, None), ('ıspanak', 'szpinak', None, None), ('pancar', 'burak', None, None)], 'sentences': []}, {'id': 'v28a', 'title': 'Rodzina i zawody 1', 'icon': 'R', 'track': 'jezyk', 'words': [('kayınpeder', 'teść', None, None), ('kayınvalide', 'teściowa', None, None), ('eniște', 'szwagier', None, None), ('erkek yeğen', 'bratanek', None, None), ('kız yeğen', 'siostrzenica', None, None), ('yetim', 'sierota', None, None), ('dul', 'wdowa', None, None), ('nişanlı', 'narzeczony', None, None), ('düğün', 'ślub', None, None), ('boşanma', 'rozwód', None, None), ('doğum', 'urodzenie', None, None), ('cenaze', 'pogrzeb', None, None), ('berber', 'fryzjer', None, None), ('fırıncı', 'piekarz', None, None), ('kasap', 'rzeźnik', None, None), ('garson kadın', 'kelnerka', None, None)], 'sentences': []}, {'id': 'v28b', 'title': 'Rodzina i zawody 2', 'icon': 'R', 'track': 'jezyk', 'words': [('postacı', 'listonosz', None, None), ('itfaiyeci', 'strażak', None, None), ('hâkim', 'sędzia', None, None), ('müdür', 'dyrektor', None, None)], 'sentences': []}]
# === /SŁOWNICTWO ===
