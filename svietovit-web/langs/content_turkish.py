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
