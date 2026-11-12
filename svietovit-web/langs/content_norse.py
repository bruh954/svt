"""Treść kursu: staronordycki (norrønt mál) dla Polaków.

Pisownia znormalizowana (jak w wydaniach sag). Wymowa odtworzona; zapis polskimi literami:
th = [θ] jak angielskie th w „think”, dh = [ð] jak th w „this”, ö = [ø], ǫ ≈ [ɔ].
"""

PUNCT = {"!", "?", ".", ",", ":"}

TRACKS = {"wymowa": "RUNA · WYMOWA", "jezyk": "MÁL · JĘZYK"}

UNITS = [
    {"id": "wymowa", "title": "Litery i dźwięki", "icon": "Þ", "track": "wymowa",
     "letters": [
         ("þ", "[θ]: jak angielskie th w „think” (runa thorn)", "þing /θiŋɡ/ (wiec)"),
         ("ð", "[ð]: jak angielskie th w „this”", "bróðir /broːðir/ (brat)"),
         ("æ", "[ɛː]: długie e, jak w „ten”, rozciągnięte", "bær /bɛːr/ (gospodarstwo)"),
         ("ø / œ", "[øː]: jak niemieckie ö, długie", "sœkja /søːkja/ (szukać)"),
         ("ǫ", "[ɔ]: jak polskie o, otwarte", "ǫl /øl/ (piwo)"),
         ("á", "[aː]: długie a", "má /maː/ (może)"),
         ("é", "[eː]: długie e", "hér /hɛːr/ (tu)"),
         ("í", "[iː]: długie i", "vín /viːn/ (wino)"),
         ("ó", "[oː]: długie o", "nótt /noːtː/ (noc)"),
         ("ú", "[uː]: długie u", "þú /θuː/ (ty)"),
         ("ý", "[yː]: długie ü", "bý /byː/ (osada)"),
         ("hv", "[xʷ]: jak polskie chł", "hvar /xʷar/ (gdzie)"),
         ("j", "[j]: jak polskie j", "jór /joːr/ (koń)"),
         ("r", "[r]: mocno toczone, jak polskie", "rún /ruːn/ (runa)"),
         ("ll, nn", "wymawiasz je długo, z lekkim d: [dl], [dn]", "fjall /fjalː/ (góra)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "H", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("heill", "witaj (do mężczyzny)", None, "Z germańskiego „zdrowy”; stąd niem. „Heil” i ang. „hale”.", "/hɛilː/"),
         ("far", "idź; jedź", None, "Z „far vel”: „jedź dobrze”.", "/far/"),
         ("vel", "dobrze", None, None, "/vɛl/"),
         ("þökk", "dziękuję; podziękowanie", None, "Ang. „thank” to to samo słowo.", "/θøkː/"),
         ("já", "tak", None, None, "/jaː/"),
         ("nei", "nie", None, None, "/nɛi/"),
         ("góðan", "dobry (biernik: dobry dzień)", None, None, "/ɡoːðan/"),
         ("dag", "dzień", None, "Ang. „day”.", "/daɡ/"),
         ("góða", "dobrą (biernik)", None, None, "/ɡoːða/"),
         ("nótt", "noc", None, "Niem. „Nacht”.", "/noːtː/"),
         ("ok", "i", None, "Ang. „and” stoi jak „ok”.", "/ɔk/"),
         ("gott", "dobrze; dobre", None, None, "/ɡɔtː/"),
     ],
     "sentences": [
         (["heill", "!"], "Witaj!", {"vel": "vel to „dobrze”."}),
         (["far", "vel", "!"], "Bądź zdrów! (żegnając)", {"heill": "heill to „witaj”."}),
         (["góðan", "dag", "!"], "Dobrego dnia!", {"nótt": "nótt to „noc”."}),
         (["góða", "nótt", "!"], "Dobrej nocy!", {"dag": "dag to „dzień”."}),
         (["já", ",", "þökk"], "Tak, dziękuję.", {"nei": "nei to „nie”."}),
         (["nei", ",", "þökk"], "Nie, dziękuję.", {"já": "já to „tak”."}),
         (["gott", "!"], "Dobrze!", {}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "E", "track": "jezyk",
     "words": [
         ("ek", "ja", None, "Ang. „I”, niem. „ich”.", "/ɛk/"),
         ("þú", "ty", None, None, "/θuː/"),
         ("hann", "on", None, None, "/hanː/"),
         ("hon", "ona", None, None, "/hɔn/"),
         ("em", "jestem", None, "Ang. „am”.", "/ɛm/"),
         ("ert", "jesteś", None, "Ang. „art”.", "/ɛrt/"),
         ("er", "jest", None, "Ang. „is”.", "/ɛr/"),
         ("maðr", "mężczyzna; człowiek", None, "Ang. „man”.", "/maðr/"),
         ("kona", "kobieta", None, "Ang. „queen” (ta sama rodzina).", "/kɔna/"),
         ("víkingr", "wiking", None, None, "/viːkiŋɡr/"),
         ("bóndi", "gospodarz", None, None, "/boːndi/"),
         ("frá", "z; od", None, None, "/fraː/"),
         ("Íslandi", "Islandii", None, "Po „frá”: celownik.", "/iːslandi/"),
         ("Noregi", "Norwegii", None, "Po „frá”: celownik.", "/nɔrɛɡi/"),
     ],
     "sentences": [
         (["ek", "em", "víkingr"], "Jestem wikingiem.", {"ert": "ert to „jesteś”. O sobie: em."}),
         (["þú", "ert", "bóndi"], "Jesteś gospodarzem.", {"em": "em to „jestem”. Do „þú”: ert."}),
         (["hann", "er", "maðr"], "On jest mężczyzną.", {"kona": "kona to „kobieta”."}),
         (["hon", "er", "kona"], "Ona jest kobietą.", {"maðr": "maðr to „mężczyzna”."}),
         (["ek", "em", "frá", "Íslandi"], "Jestem z Islandii.", {"Noregi": "Noregi to „Norwegia”."}),
         (["hann", "er", "frá", "Noregi"], "On jest z Norwegii.", {}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "R", "track": "jezyk",
     "words": [
         ("móðir", "matka", None, "Ang. „mother”.", "/moːðir/"),
         ("faðir", "ojciec", None, "Ang. „father”.", "/faðir/"),
         ("bróðir", "brat", None, "Ang. „brother”.", "/broːðir/"),
         ("systir", "siostra", None, "Ang. „sister”.", "/systir/"),
         ("bróður", "brata (biernik)", None, None, "/broːður/"),
         ("systur", "siostrę (biernik)", None, None, "/systur/"),
         ("vinr", "przyjaciel", None, None, "/vinr/"),
         ("minn", "mój (męski)", None, "Postawiony po słowie: „bróðir minn”.", "/minː/"),
         ("mín", "moja (żeński)", None, "„Systir mín”.", "/miːn/"),
         ("á", "mam", None, "Ang. „own”.", "/aː/"),
         ("átt", "masz", None, None, "/aːt/"),
         ("lítill", "mały (męski)", None, "Ang. „little”.", "/liːtilː/"),
         ("lítil", "mała (żeński)", None, None, "/liːtil/"),
         ("góðr", "dobry (męski)", None, None, "/ɡoːðr/"),
         ("góð", "dobra (żeński)", None, None, "/ɡoːð/"),
     ],
     "sentences": [
         (["bróðir", "minn", "er", "lítill"], "Mój brat jest mały.", {"mín": "bróðir jest męski: minn."}),
         (["systir", "mín", "er", "góð"], "Moja siostra jest dobra.", {"minn": "systir jest żeńska: mín.", "góðr": "systir jest żeńska: góð."}),
         (["faðir", "minn", "er", "góðr"], "Mój ojciec jest dobry.", {}),
         (["ek", "á", "bróður"], "Mam brata.", {"átt": "átt to „masz”. O sobie: á."}),
         (["þú", "átt", "systur"], "Masz siostrę.", {"á": "á to „mam”. Do „þú”: átt."}),
         (["vinr", "minn", "er", "maðr"], "Mój przyjaciel jest mężczyzną.", {}),
         (["móðir", "mín", "er", "lítil"], "Moja matka jest mała.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "Ǫ", "track": "jezyk",
     "words": [
         ("vatn", "woda", None, "Ang. „water”.", "/vatn/"),
         ("mjǫðr", "miód pitny", None, None, "/mjøðr/"),
         ("mjǫð", "miód pitny (biernik)", None, None, "/mjøð/"),
         ("ǫl", "piwo", None, "Ang. „ale”.", "/øl/"),
         ("brauð", "chleb", None, "Ang. „bread”.", "/brɔuð/"),
         ("ostr", "ser", None, None, "/ɔstr/"),
         ("mjólk", "mleko", None, "Ang. „milk”.", "/mjoːlk/"),
         ("fiskr", "ryba", None, None, "/fiskr/"),
         ("fisk", "rybę (biernik)", None, None, "/fisk/"),
         ("epli", "jabłko", None, "Ang. „apple”.", "/ɛpli/"),
         ("vil", "chcę", None, "Ang. „will”.", "/vil/"),
         ("vilt", "chcesz", None, None, "/vilt/"),
         ("nú", "teraz", None, "Ang. „now”.", "/nuː/"),
     ],
     "sentences": [
         (["ek", "vil", "ǫl"], "Chcę piwo.", {"vilt": "vilt to „chcesz”. O sobie: vil."}),
         (["þú", "vilt", "mjǫð"], "Chcesz miód.", {"vil": "vil to „chcę”. Do „þú”: vilt."}),
         (["ek", "vil", "brauð"], "Chcę chleb.", {}),
         (["þú", "vilt", "epli"], "Chcesz jabłko.", {}),
         (["fiskr", "er", "góðr"], "Ryba jest dobra.", {}),
         (["nú", "vil", "ek", "vatn"], "Teraz chcę wodę.", {"vilt": "vilt to „chcesz”. O sobie: vil."}),
     ]},
    {"id": "liczby", "title": "Liczby i czas", "icon": "I", "track": "jezyk",
     "words": [
         ("tvau", "dwa (rodzaj nijaki)", None, None, "/tvɔu/"),
         ("þrír", "trzej", None, None, "/θriːr/"),
         ("fjórir", "czterej", None, None, "/fjoːrir/"),
         ("fimm", "pięć", None, None, "/fimː/"),
         ("tíu", "dziesięć", None, None, "/tiːu/"),
         ("bǫrn", "dzieci", None, "Ang. „bairn” (szkockie „dziecko”).", "/børn/"),
         ("menn", "mężczyźni; ludzie", None, "Ang. „men”.", "/mɛnː/"),
         ("eru", "są", None, None, "/ɛru/"),
         ("hér", "tu", None, "Ang. „here”.", "/hɛːr/"),
         ("í", "w; na", None, None, "/iː/"),
         ("morgin", "ranek; jutro", None, None, "/mɔrɡin/"),
         ("gær", "wczoraj", None, None, "/ɡɛːr/"),
     ],
     "sentences": [
         (["ek", "á", "tvau", "bǫrn"], "Mam dwoje dzieci.", {}),
         (["ek", "vil", "fimm", "epli"], "Chcę pięć jabłek.", {"tvau": "tvau to „dwa”. Chcesz pięć: fimm."}),
         (["í", "dag", "vil", "ek", "ǫl"], "Dziś chcę piwo.", {"gær": "gær to „wczoraj”."}),
         (["á", "morgin", "vil", "ek", "fisk"], "Jutro chcę rybę.", {"gær": "gær to „wczoraj”."}),
         (["tíu", "menn", "eru", "hér"], "Dziesięciu mężczyzn jest tu.", {}),
         (["þrír", "menn", "eru", "hér"], "Trzej mężczyźni są tu.", {"fjórir": "fjórir to „czterej”."}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "S", "track": "jezyk",
     "words": [
         ("hús", "dom", None, "Ang. „house”.", "/huːs/"),
         ("borg", "gród", None, "Ang. „borough”.", "/bɔrɡ/"),
         ("vegr", "droga", None, "Ang. „way”.", "/vɛɡr/"),
         ("skip", "statek", None, "Ang. „ship”.", "/skip/"),
         ("haf", "morze", None, None, "/haf/"),
         ("hǫll", "hala", None, "Ang. „hall”.", "/hølː/"),
         ("bær", "gospodarstwo", None, None, "/bɛːr/"),
         ("hvar", "gdzie", None, None, "/xʷar/"),
         ("þar", "tam", None, "Ang. „there”.", "/θar/"),
         ("fer", "idę; jadę", None, None, "/fɛr/"),
         ("heim", "do domu", None, "Ang. „home”.", "/hɛim/"),
         ("til", "do", None, "Ang. „till”.", "/til/"),
         ("Noregs", "Norwegii (do Norwegii)", None, "Po „til”: dopełniacz.", "/nɔrɛɡs/"),
         ("hægri", "prawy; w prawo", None, None, "/hɛːɡri/"),
         ("vinstri", "lewy; w lewo", None, None, "/vinstri/"),
     ],
     "sentences": [
         (["hvar", "er", "skip", "?"], "Gdzie jest statek?", {"hér": "hér to „tu”. Pytasz „gdzie”: hvar."}),
         (["skip", "er", "þar"], "Statek jest tam.", {"hér": "hér to „tu”. Tu „tam”: þar."}),
         (["ek", "fer", "heim"], "Idę do domu.", {}),
         (["ek", "fer", "til", "Noregs"], "Jadę do Norwegii.", {"frá": "frá to „z”. Jedziesz do: til."}),
         (["skip", "er", "til", "hægri"], "Statek jest po prawej.", {"vinstri": "vinstri to „lewa”."}),
         (["hǫll", "er", "þar"], "Hala jest tam.", {}),
     ]},
]

INSIGHTS = {
    "wymowa": [{"title": "Þ i ð: dwa th", "chain": [],
                "text": "Þ (thorn) to twarde th jak w angielskim „think”: þú, þökk. Ð (eth) to miękkie th jak w „this”: bróðir, góðan. Kreska nad samogłoską (á, é, í, ó, ú, ý) oznacza, że jest długa."}],
    "ja": [{"title": "Ek em, þú ert, hann er", "chain": [
                ("Jestem wikingiem.", ["ek", "em", "víkingr"], "Do „ek” pasuje em."),
                ("Jesteś gospodarzem.", ["þú", "ert", "bóndi"], "Do „þú” pasuje ert."),
            ],
            "text": "Staronordycki jest bliski angielskiemu: ek em ≈ I am, þú ert ≈ thou art, hann er ≈ he is. Końcówkę -r w maðr, víkingr usuń po angielsku w głowie: to „man”, „viking”."}],
    "ludzie": [{"title": "Minn, mín: po rzeczowniku", "chain": [],
                "text": "Dzierżawcze stoi po rzeczowniku i zgadza się z jego rodzajem: bróðir minn (m), systir mín (ż). Przymiotniki też: góðr (m), góð (ż)."}],
    "jedzenie": [{"title": "Vil i vilt", "chain": [],
                  "text": "Czasownik „chcieć”: ek vil (chcę), þú vilt (chcesz). W zdaniu oznajmującym czasownik stoi na drugim miejscu: nú vil ek vatn."}],
}

ENDINGS_INSIGHT = {"title": "Rodzaj i forma czasownika",
                   "text": "Ćwiczysz rodzaj (minn/mín, góðr/góð) i formy czasownika (em, ert, er). Tu to robisz."}

ENDINGS = [
    ("ek ", "", "em", " víkingr", ["em", "ert", "er"], "ja jestem", "Do „ek” pasuje em.", "ja"),
    ("þú ", "", "ert", " bóndi", ["em", "ert", "er"], "ty jesteś", "Do „þú” pasuje ert.", "ja"),
    ("hann ", "", "er", " maðr", ["em", "ert", "er"], "on jest", "Do „hann” pasuje er.", "ja"),
    ("bróðir ", "", "minn", " er lítill", ["minn", "mín"], "mój (męski)", "bróðir jest męski: minn.", "ludzie"),
    ("systir ", "", "mín", " er lítil", ["minn", "mín"], "moja (żeński)", "systir jest żeńska: mín.", "ludzie"),
    ("faðir minn er ", "", "góðr", "", ["góðr", "góð"], "dobry (męski)", "faðir jest męski: góðr.", "ludzie"),
    ("móðir mín er ", "", "góð", "", ["góðr", "góð"], "dobra (żeńska)", "móðir jest żeńska: góð.", "ludzie"),
    ("ek ", "", "á", " bróður", ["á", "átt"], "ja mam", "Do „ek” pasuje á.", "ludzie"),
    ("þú ", "", "átt", " systur", ["á", "átt"], "ty masz", "Do „þú” pasuje átt.", "ludzie"),
    ("ek ", "", "vil", " ǫl", ["vil", "vilt"], "ja chcę", "Do „ek” pasuje vil.", "jedzenie"),
    ("þú ", "", "vilt", " mjǫð", ["vil", "vilt"], "ty chcesz", "Do „þú” pasuje vilt.", "jedzenie"),
    ("ek fer ", "", "til", " Noregs", ["til", "frá"], "do", "til to „do”, frá to „z”.", "miejsca"),
    ("ek em ", "", "frá", " Íslandi", ["til", "frá"], "z", "frá to „z”.", "miejsca"),
]

CHAT_EXTRA = {"Sigrún": "Sigrún (imię)", "Eiríkr": "Eiríkr (imię)", "Ragnarr": "Ragnarr (imię)",
              "hvert": "dokąd", "ferr": "idziesz; jedziesz", "gott": "dobrze"}

CHATS = [
    {"id": "holl", "title": "W wielkiej sali", "partner": "Sigrún", "avatar": "S", "requires": "jedzenie",
     "turns": [
         {"bot": ["heill", "!"], "en": "Witaj!",
          "options": [(["heill", "!"], True, None), (["góða", "nótt", "!"], False, "góða nótt to „dobrej nocy”. Tu witasz.")]},
         {"bot": ["ǫl", "?"], "en": "Piwa?",
          "options": [(["já", ",", "ek", "vil", "ǫl"], True, None),
                      (["já", ",", "þú", "vilt", "ǫl"], False, "vilt to „chcesz”. O sobie: vil.")]},
         {"bot": ["ok", "brauð", "?"], "en": "I chleba?",
          "options": [(["nei", ",", "þökk"], True, None),
                      (["far", "vel", "!"], False, "far vel to pożegnanie. Odmów: nei, þökk.")]},
         {"bot": ["gott", "!"], "build": (["þökk", "!"], "Dziękuję!"), "en": "Dobrze!"},
     ]},
    {"id": "kynning", "title": "Poznajemy się", "partner": "Eiríkr", "avatar": "E", "requires": "ludzie",
     "turns": [
         {"bot": ["heill", "!"], "en": "Witaj!",
          "options": [(["heill", "!"], True, None), (["nei", "!"], False, "nei to „nie”. Powitaj: heill.")]},
         {"bot": ["þú", "ert", "frá", "Noregi", "?"], "en": "Jesteś z Norwegii?",
          "options": [(["nei", ",", "ek", "em", "frá", "Íslandi"], True, None),
                      (["nei", ",", "ek", "ert", "frá", "Íslandi"], False, "ert to „jesteś”. O sobie: em.")]},
         {"bot": ["átt", "þú", "bróður", "?"], "en": "Masz brata?",
          "options": [(["já", ",", "ek", "á", "bróður"], True, None),
                      (["já", ",", "ek", "átt", "bróður"], False, "átt to „masz”. O sobie: á.")]},
         {"bot": ["far", "vel", "!"], "build": (["far", "vel", "!"], "Bądź zdrów!"), "en": "Bądź zdrów!"},
     ]},
    {"id": "skip", "title": "Na statku", "partner": "Ragnarr", "avatar": "R", "requires": "miejsca",
     "turns": [
         {"bot": ["góðan", "dag", "!"], "en": "Dobrego dnia!",
          "options": [(["góðan", "dag", "!"], True, None), (["góða", "nótt", "!"], False, "góða nótt to „dobrej nocy”. Jest dzień.")]},
         {"bot": ["hvert", "ferr", "þú", "?"], "en": "Dokąd jedziesz?",
          "options": [(["ek", "fer", "til", "Noregs"], True, None),
                      (["ek", "ferr", "til", "Noregs"], False, "ferr to „idziesz”. O sobie: fer.")]},
         {"bot": ["hvar", "er", "skip", "?"], "en": "Gdzie jest statek?",
          "options": [(["skip", "er", "þar"], True, None), (["hvar", "er", "skip", "?"], False, "To pytanie, nie odpowiedź. Odpowiedz: skip er þar.")]},
         {"bot": ["gott", "!"], "build": (["far", "vel", "!"], "Bądź zdrów!"), "en": "Dobrze!"},
     ]},
]


# ---------------------------------------------------------------------------
# Gramatyka.
# PARADIGMS: ("conj" | "decl" | "form", grupa, tytuł, klucz etykiet, formy rozdzielone „; ”, uwaga lub None)
# conj = koniugacje i czasy, decl = deklinacje, zaimki i liczebniki, form = imiesłowy, formy podstawowe, ćwiczenia celowane.
# Liczba form musi być równa liczbie etykiet. Uczeń przechodzi cały wzór: tabela, po kolei, na wyrywki.
# ---------------------------------------------------------------------------

PARADIGM_LABELS = {
    'os': ['ek', 'þú', 'hann/hon', 'vér', 'þér', 'þeir'],
    'przyp': ['mianownik lp.', 'biernik lp.', 'celownik lp.', 'dopełniacz lp.', 'mianownik lm.', 'biernik lm.', 'celownik lm.', 'dopełniacz lm.'],
    'przyp4': ['mianownik', 'biernik', 'celownik', 'dopełniacz'],
    'im': ['imiesłów teraźniejszy', 'imiesłów przeszły (męski)', 'imiesłów przeszły (żeński)', 'imiesłów przeszły (nijaki)'],
    't_uprz': ['barn (dziecko)', 'land (kraj)', 'fjall (góra)', 'vatn (woda)', 'nafn (imię)'],
}

PARADIGMS = [
    ('conj', 'Wzory koniugacji', 'kalla (wołać): słaby', 'os', 'kalla; kallar; kallar; kǫllum; kallið; kalla', 'Czasownik słaby. Przed -um a → ǫ (u-przegłos).'),
    ('conj', 'Wzory koniugacji', 'fara (jechać): mocny', 'os', 'fer; ferr; ferr; fǫrum; farið; fara', 'Czasownik mocny: w lp. przegłos a → e.'),
    ('conj', 'Czasowniki nieregularne', 'vera (być)', 'os', 'em; ert; er; erum; eruð; eru', None),
    ('conj', 'Czasowniki nieregularne', 'hafa (mieć)', 'os', 'hef; hefr; hefr; hǫfum; hafið; hafa', None),
    ('conj', 'Czasowniki nieregularne', 'vilja (chcieć)', 'os', 'vil; vilt; vill; viljum; vilið; vilja', None),
    ('conj', 'Czasowniki nieregularne', 'eiga (posiadać)', 'os', 'á; átt; á; eigum; eiguð; eigu', None),
    ('conj', 'Czasowniki nieregularne', 'koma (przychodzić)', 'os', 'kem; kemr; kemr; komum; komið; koma', None),
    ('conj', 'Czasowniki nieregularne', 'sjá (widzieć)', 'os', 'sé; sér; sér; sjám; séð; sjá', None),
    ('decl', 'Wzory deklinacji', 'hestr (koń): męski', 'przyp', 'hestr; hest; hesti; hests; hestar; hesta; hestum; hesta', 'Mocny męski: -r w mianowniku, -s w dopełniaczu.'),
    ('decl', 'Wzory deklinacji', 'armr (ramię): męski', 'przyp', 'armr; arm; armi; arms; armar; arma; ǫrmum; arma', 'Przed -um a → ǫ.'),
    ('decl', 'Wzory deklinacji', 'saga (opowieść): żeński słaby', 'przyp', 'saga; sǫgu; sǫgu; sǫgu; sǫgur; sǫgur; sǫgum; sagna', None),
    ('decl', 'Wzory deklinacji', 'skip (statek): nijaki', 'przyp', 'skip; skip; skipi; skips; skip; skip; skipum; skipa', 'Nijakie: mianownik = biernik, także w lm.'),
    ('decl', 'Wyjątki', 'barn (dziecko)', 'przyp', 'barn; barn; barni; barns; bǫrn; bǫrn; bǫrnum; barna', 'W lm. a → ǫ: bǫrn.'),
    ('decl', 'Wyjątki', 'maðr (człowiek)', 'przyp', 'maðr; mann; manni; manns; menn; menn; mǫnnum; manna', None),
    ('decl', 'Wyjątki', 'faðir (ojciec)', 'przyp', 'faðir; fǫður; fǫður; fǫður; feðr; feðr; feðrum; feðra', None),
    ('decl', 'Zaimki', 'ek (ja)', 'przyp4', 'ek; mik; mér; mín', None),
    ('decl', 'Zaimki', 'þú (ty)', 'przyp4', 'þú; þik; þér; þín', None),
    ('form', 'Imiesłowy', 'kalla (wołać)', 'im', 'kallandi; kallaðr; kǫlluð; kallat', None),
    ('form', 'Imiesłowy', 'fara (jechać)', 'im', 'farandi; farinn; farin; farit', 'Czasowniki mocne: imiesłów przeszły na -inn.'),
    ('form', 'Imiesłowy', 'koma (przychodzić)', 'im', 'komandi; kominn; komin; komit', None),
    ('conj', 'Czas przeszły', 'vera: czas przeszły', 'os', 'var; vart; var; várum; váruð; váru', None),
    ('conj', 'Czas przeszły', 'kalla: czas przeszły', 'os', 'kallaða; kallaðir; kallaði; kǫlluðum; kǫlluðuð; kǫlluðu', 'Czasowniki słabe: znak -ð-.'),
    ('conj', 'Czas przeszły', 'fara: czas przeszły', 'os', 'fór; fórt; fór; fórum; fóruð; fóru', 'Czasowniki mocne: zmiana samogłoski tematu.'),
    ('form', 'Typowe trudności', 'U-przegłos: mianownik liczby mnogiej', 't_uprz', 'bǫrn; lǫnd; fjǫll; vǫtn; nǫfn', 'Rzeczowniki nijakie nie mają końcówki w lm.; zmienia się tylko a → ǫ.'),
]

# Więcej ćwiczeń celowanych w typowe trudności
PARADIGM_LABELS.update({
    't_m0': ['hestr', 'armr', 'konungr', 'maðr', 'sonr', 'dagr', 'fiskr', 'vinr'],
    't_m1': ['fara', 'kalla', 'koma', 'taka', 'hafa', 'gefa', 'segja', 'sjá'],
    't_m2': ['vin', 'vín', 'sal', 'sál', 'mal', 'mál'],
})
PARADIGMS += [
    ('form', 'Typowe trudności', 'Biernik: bez końcowego -r', 't_m0', 'hest; arm; konung; mann; son; dag; fisk; vin', '-r jest końcówką mianownika, nie częścią tematu.'),
    ('form', 'Typowe trudności', 'Czas przeszły (3. osoba): mocny czy słaby?', 't_m1', 'fór; kallaði; kom; tók; hafði; gaf; sagði; sá', 'Mocne zmieniają samogłoskę, słabe dodają -ði lub -di.'),
    ('form', 'Typowe trudności', 'Długość: co to znaczy?', 't_m2', 'łąka; wino; salę (biernik); dusza; (nie ma takiego słowa); mowa, sprawa', 'Kreska oznacza długą samogłoskę.'),
]
