"""Treść kursu: tajski dla Polaków. Piąte pole słowa to zapis wymowy (litery łacińskie, tony znakami nad samogłoską)."""

PUNCT = {"?"}

TRACKS = {"wymowa": "เสียง · PISMO I TONY", "jezyk": "ภาษา · JĘZYK"}

TONE_NOTE = "Tony: bez znaku = środkowy, ` = niski, ^ = opadający, ´ = wysoki, ˇ = rosnący."

UNITS = [
    {"id": "wymowa", "title": "Pismo i tony", "icon": "ก", "track": "wymowa",
     "letters": [
         ("ก", "[k]: bez dmuchnięcia, jak polskie k; spółgłoska klasy średniej", "กิน (kin: jeść)"),
         ("ข", "[kʰ]: k z dmuchnięciem; klasa wysoka", "ไข่ (khài: jajko)"),
         ("ค", "[kʰ]: k z dmuchnięciem; klasa niska", "คน (khon: człowiek)"),
         ("ง", "[ŋ]: jak „ng” w „ang”; może stać na początku słowa; klasa niska", "งาน (ngaan: praca)"),
         ("จ", "[tɕ]: coś między c a ć, bez dmuchnięcia; klasa średnia", "จาน (jaan: talerz)"),
         ("ด", "[d]: jak polskie d; klasa średnia", "ดี (dii: dobry)"),
         ("ต", "[t]: bez dmuchnięcia, jak polskie t; klasa średnia", "ตา (taa: oko)"),
         ("น", "[n]: jak polskie n; klasa niska", "น้ำ (náam: woda)"),
         ("บ", "[b]: jak polskie b; klasa średnia", "บ้าน (bâan: dom)"),
         ("ป", "[p]: bez dmuchnięcia, jak polskie p; klasa średnia", "ปลา (plaa: ryba)"),
         ("ม", "[m]: jak polskie m; klasa niska", "แม่ (mɛ̂ɛ: matka)"),
         ("ย", "[j]: jak polskie j; klasa niska", "ยา (yaa: lek)"),
         ("ร", "[r]: lekko toczone, często brzmi jak l; klasa niska", "รถ (rót: samochód)"),
         ("ล", "[l]: jak polskie l; klasa niska", "ลูก (lûuk: dziecko)"),
         ("ว", "[w]: jak polskie ł (w); klasa niska", "วัน (wan: dzień)"),
         ("ส", "[s]: jak polskie s; klasa wysoka", "สอง (sɔ̌ɔng: dwa)"),
         ("ห", "[h]: jak polskie h; klasa wysoka; przed niektórymi spółgłoskami podnosi ton", "หก (hòk: sześć)"),
         ("อ", "litera zerowa: słowo zaczyna się od samogłoski; w środku to też [ɔɔ]", "อร่อย (à-rɔ̀i: pyszny)"),
         ("า", "[aa]: długie a, pisane po spółgłosce", "ชา (chaa: herbata)"),
         ("ะ", "[a]: krótkie a na końcu sylaby", "กะ (ka: aby)"),
         ("ี", "[ii]: długie i, znak nad spółgłoską", "ดี (dii: dobry)"),
         ("ู", "[uu]: długie u, znak pod spółgłoską", "ปู (puu: krab)"),
         ("เ-", "[ee]: samogłoska piszemy przed spółgłoską, ale czytamy po niej", "เด็ก (dèk: dziecko)"),
         ("แ-", "[ɛɛ]: szerokie e, pisane przed spółgłoską", "แม่ (mɛ̂ɛ: matka)"),
         ("โ-", "[oo]: długie o, pisane przed spółgłoską", "โต๊ะ (tó: stół)"),
         ("ไ-, ใ-", "[ai]: dwa znaki, ta sama wymowa, pisane przed spółgłoską", "ไป (pai: iść)"),
         ("่", "mai ek: znak tonu nad spółgłoską; zmienia ton zależnie od klasy litery", "ที่ (thîi: miejsce, że)"),
         ("้", "mai tho: znak tonu nad spółgłoską; zwykle ton opadający", "ไม้ (máai: drewno)"),
         ("pięć tonów", "środkowy, niski, opadający, wysoki, rosnący: ten sam zlepek głosek znaczy co innego", "ใกล้ (klâi: blisko), ไกล (klai: daleko)"),
     ]},
    {"id": "slowa", "title": "Pierwsze słowa", "icon": "ส", "track": "jezyk", "requires": "wymowa",
     "words": [
         ("สวัสดี", "cześć; dzień dobry", None, "Jedno słowo na każdą porę dnia.", "sà-wàt-dii"),
         ("ขอบคุณ", "dziękuję", None, None, "khɔ̀ɔp-khun"),
         ("ครับ", "partykuła grzecznościowa (mężczyzna)", None, "Mężczyzna kończy tak zdania grzeczne.", "khráp"),
         ("ค่ะ", "partykuła grzecznościowa (kobieta)", None, "Kobieta kończy tak zdania grzeczne.", "khâ"),
         ("ใช่", "tak; zgadza się", None, None, "châi"),
         ("ไม่", "nie", None, "Stawiasz przed czasownikiem lub przymiotnikiem.", "mâi"),
         ("ขอโทษ", "przepraszam", None, None, "khɔ̌ɔ-thôot"),
         ("ดี", "dobry", None, None, "dii"),
         ("มาก", "bardzo; dużo", None, "Stoi po słowie, które wzmacnia.", "mâak"),
         ("ลาก่อน", "do widzenia", None, None, "laa-kɔ̀ɔn"),
     ],
     "sentences": [
         (["สวัสดี", "ครับ"], "Dzień dobry. (mężczyzna mówi)", {"ค่ะ": "ค่ะ mówi kobieta."}),
         (["สวัสดี", "ค่ะ"], "Dzień dobry. (kobieta mówi)", {"ครับ": "ครับ mówi mężczyzna."}),
         (["ขอบคุณ", "ครับ"], "Dziękuję. (mężczyzna)", {"ค่ะ": "ค่ะ mówi kobieta."}),
         (["ขอบคุณ", "ค่ะ"], "Dziękuję. (kobieta)", {"ครับ": "ครับ mówi mężczyzna."}),
         (["ใช่", "ครับ"], "Tak. (mężczyzna)", {"ไม่": "ไม่ to „nie”."}),
         (["ไม่", "ค่ะ"], "Nie. (kobieta)", {"ใช่": "ใช่ to „tak”."}),
         (["ขอโทษ", "ครับ"], "Przepraszam. (mężczyzna)", {}),
         (["ดี", "มาก", "ค่ะ"], "Bardzo dobrze. (kobieta)", {}),
         (["ลาก่อน", "ครับ"], "Do widzenia. (mężczyzna)", {"สวัสดี": "สวัสดี to powitanie."}),
     ]},
    {"id": "ja", "title": "Ja, ty, on", "icon": "ผ", "track": "jezyk",
     "words": [
         ("ผม", "ja (mężczyzna)", None, None, "phǒm"),
         ("ฉัน", "ja (kobieta)", None, None, "chǎn"),
         ("คุณ", "ty; pan, pani", None, None, "khun"),
         ("เขา", "on; ona", None, "Nie ma rodzaju.", "khǎo"),
         ("เรา", "my", None, None, "rao"),
         ("เป็น", "być (kimś, czymś)", None, None, "pen"),
         ("นักเรียน", "uczeń; student", None, None, "nák-rian"),
         ("ครู", "nauczyciel", None, None, "khruu"),
         ("คนโปแลนด์", "Polak; Polka", None, "คน (człowiek) + โปแลนด์ (Polska).", "khon-poo-lɛɛn"),
         ("มาจาก", "pochodzić z; przyjechać z", None, None, "maa-jàak"),
         ("โปแลนด์", "Polska", None, None, "poo-lɛɛn"),
         ("ไทย", "Tajlandia; tajski", None, None, "thai"),
         ("ไหม", "czy (partykuła pytająca)", None, "Dodajesz na końcu zdania, żeby zrobić pytanie.", "mǎi"),
     ],
     "sentences": [
         (["ผม", "เป็น", "นักเรียน", "ครับ"], "Jestem uczniem. (mężczyzna)", {"ฉัน": "ฉัน mówi kobieta."}),
         (["ฉัน", "เป็น", "นักเรียน", "ค่ะ"], "Jestem uczennicą. (kobieta)", {"ผม": "ผม mówi mężczyzna."}),
         (["คุณ", "เป็น", "ครู", "ไหม"], "Czy jest pan nauczycielem?", {"ไม่": "ไม่ to „nie”. Pytanie robi ไหม."}),
         (["เขา", "เป็น", "คนโปแลนด์"], "On jest Polakiem.", {}),
         (["ผม", "มาจาก", "โปแลนด์", "ครับ"], "Jestem z Polski. (mężczyzna)", {"ไทย": "ไทย to Tajlandia."}),
         (["คุณ", "มาจาก", "ไทย", "ไหม"], "Czy jest pan z Tajlandii?", {"โปแลนด์": "โปแลนด์ to Polska."}),
         (["เรา", "เป็น", "นักเรียน"], "Jesteśmy uczniami.", {}),
         (["ผม", "ไม่", "เป็น", "ครู", "ครับ"], "Nie jestem nauczycielem. (mężczyzna)", {"ใช่": "ใช่ to „tak”."}),
     ]},
    {"id": "ludzie", "title": "Ludzie i rodzina", "icon": "แ", "track": "jezyk",
     "words": [
         ("พ่อ", "tata", None, None, "phɔ̂ɔ"),
         ("แม่", "mama", None, None, "mɛ̂ɛ"),
         ("ลูก", "dziecko", None, None, "lûuk"),
         ("เพื่อน", "przyjaciel; przyjaciółka", None, None, "phʉ̂an"),
         ("พี่ชาย", "starszy brat", None, "Tajski odróżnia starszeństwo: พี่ = starszy.", "phîi-chaai"),
         ("น้องสาว", "młodsza siostra", None, "น้อง = młodszy.", "nɔ́ɔng-sǎao"),
         ("มี", "mieć; być (jest, są)", None, None, "mii"),
         ("ของ", "należący do; z", None, "ของผม = mój.", "khɔ̌ɔng"),
         ("คน", "osoba; licznik dla osób", None, "Liczysz osoby: ลูกสองคน = dwoje dzieci.", "khon"),
     ],
     "sentences": [
         (["ผม", "มี", "พี่ชาย", "ครับ"], "Mam starszego brata. (mężczyzna)", {"น้องสาว": "น้องสาว to młodsza siostra."}),
         (["ฉัน", "มี", "น้องสาว", "ค่ะ"], "Mam młodszą siostrę. (kobieta)", {"พี่ชาย": "พี่ชาย to starszy brat."}),
         (["คุณ", "มี", "ลูก", "ไหม"], "Czy ma pan dziecko?", {}),
         (["แม่", "เป็น", "ครู"], "Mama jest nauczycielką.", {"พ่อ": "พ่อ to tata."}),
         (["พ่อ", "ของ", "ผม", "เป็น", "ครู"], "Mój tata jest nauczycielem.", {"แม่": "แม่ to mama."}),
         (["เขา", "เป็น", "เพื่อน", "ของ", "ฉัน"], "On jest moim przyjacielem.", {}),
     ]},
    {"id": "jedzenie", "title": "Jedzenie i picie", "icon": "ข", "track": "jezyk",
     "words": [
         ("กิน", "jeść", None, None, "kin"),
         ("ดื่ม", "pić", None, None, "dʉ̀ʉm"),
         ("น้ำ", "woda", None, None, "náam"),
         ("กาแฟ", "kawa", "kawa", None, "kaa-fɛɛ"),
         ("ชา", "herbata", None, None, "chaa"),
         ("ข้าว", "ryż; jedzenie", None, "Tajowie mówią „zjeść ryż”, gdy jedzą posiłek.", "khâao"),
         ("นม", "mleko", None, None, "nom"),
         ("ปลา", "ryba", None, None, "plaa"),
         ("ไก่", "kurczak", None, None, "kài"),
         ("อยาก", "chcieć; mieć ochotę", None, "Stoi przed czasownikiem: อยากกิน = chcę jeść.", "yàak"),
         ("ขอ", "prosić o", None, None, "khɔ̌ɔ"),
         ("อร่อย", "smaczny", None, None, "à-rɔ̀i"),
         ("หิว", "głodny", None, None, "hǐu"),
     ],
     "sentences": [
         (["ผม", "อยาก", "กิน", "ข้าว", "ครับ"], "Chcę zjeść ryż. (mężczyzna)", {"ดื่ม": "ดื่ม to „pić”. Jeść: กิน."}),
         (["ฉัน", "ดื่ม", "กาแฟ", "ค่ะ"], "Piję kawę. (kobieta)", {"กิน": "กิน to „jeść”. Pić: ดื่ม."}),
         (["ขอ", "น้ำ", "ครับ"], "Poproszę wodę. (mężczyzna)", {}),
         (["ผม", "กิน", "ปลา"], "Jem rybę.", {"ดื่ม": "ดื่ม to „pić”."}),
         (["คุณ", "อยาก", "ดื่ม", "ชา", "ไหม"], "Chce pan herbaty?", {}),
         (["ข้าว", "อร่อย", "มาก"], "Ryż jest bardzo smaczny.", {}),
         (["ฉัน", "หิว", "ค่ะ"], "Jestem głodna. (kobieta)", {}),
         (["ผม", "ไม่", "กิน", "ไก่", "ครับ"], "Nie jem kurczaka. (mężczyzna)", {}),
         (["ฉัน", "อยาก", "ดื่ม", "นม", "ค่ะ"], "Chcę pić mleko. (kobieta)", {}),
     ]},
    {"id": "liczby", "title": "Liczby i pieniądze", "icon": "๑", "track": "jezyk",
     "words": [
         ("หนึ่ง", "jeden", None, None, "nʉ̀ng"),
         ("สอง", "dwa", None, None, "sɔ̌ɔng"),
         ("สาม", "trzy", None, None, "sǎam"),
         ("สี่", "cztery", None, None, "sìi"),
         ("ห้า", "pięć", None, None, "hâa"),
         ("หก", "sześć", None, None, "hòk"),
         ("เจ็ด", "siedem", None, None, "jèt"),
         ("แปด", "osiem", None, None, "pɛ̀ɛt"),
         ("เก้า", "dziewięć", None, None, "kâao"),
         ("สิบ", "dziesięć", None, None, "sìp"),
         ("เท่าไร", "ile", None, "Pytasz o cenę: กาแฟเท่าไร.", "thâo-rai"),
         ("บาท", "bat (waluta)", None, None, "bàat"),
         ("แพง", "drogi", None, None, "phɛɛng"),
         ("ถูก", "tani", None, None, "thùuk"),
     ],
     "sentences": [
         (["กาแฟ", "เท่าไร", "ครับ"], "Ile kosztuje kawa? (mężczyzna)", {}),
         (["น้ำ", "สิบ", "บาท"], "Woda kosztuje dziesięć batów.", {}),
         (["ข้าว", "ถูก", "มาก"], "Ryż jest bardzo tani.", {"แพง": "แพง to „drogi”."}),
         (["ปลา", "แพง", "มาก"], "Ryba jest bardzo droga.", {"ถูก": "ถูก to „tani”."}),
         (["ผม", "มี", "ลูก", "สอง", "คน", "ครับ"], "Mam dwoje dzieci. (mężczyzna)", {"บาท": "บาท to waluta. Osoby liczysz คน."}),
         (["ฉัน", "มี", "เพื่อน", "สาม", "คน", "ค่ะ"], "Mam troje przyjaciół. (kobieta)", {}),
         (["ชา", "ห้า", "บาท"], "Herbata kosztuje pięć batów.", {}),
     ]},
    {"id": "miejsca", "title": "Miejsca i podróż", "icon": "ท", "track": "jezyk",
     "words": [
         ("บ้าน", "dom", None, None, "bâan"),
         ("โรงเรียน", "szkoła", None, None, "roong-rian"),
         ("ตลาด", "targ", None, None, "ta-làat"),
         ("โรงแรม", "hotel", "hotel", None, "roong-rɛɛm"),
         ("แท็กซี่", "taksówka", "taksówka", None, "thɛ́k-sîi"),
         ("กรุงเทพ", "Bangkok", None, None, "grung-thêep"),
         ("ไป", "iść; jechać", None, None, "pai"),
         ("อยู่", "znajdować się; mieszkać", None, None, "yùu"),
         ("ที่ไหน", "gdzie", None, "ที่ + ไหน; pytasz o miejsce.", "thîi-nǎi"),
         ("ที่นั่น", "tam", None, None, "thîi-nân"),
         ("ที่นี่", "tu", None, None, "thîi-nîi"),
         ("ทาง", "strona; droga", None, None, "thaang"),
         ("ซ้าย", "lewy", None, None, "sáai"),
         ("ขวา", "prawy", None, None, "khwǎa"),
     ],
     "sentences": [
         (["โรงแรม", "อยู่", "ที่ไหน", "ครับ"], "Gdzie jest hotel? (mężczyzna)", {"ที่นี่": "ที่นี่ to „tu”. Pytasz o miejsce: ที่ไหน."}),
         (["โรงแรม", "อยู่", "ที่นั่น"], "Hotel jest tam.", {"ที่นี่": "ที่นี่ to „tu”."}),
         (["ผม", "ไป", "บ้าน"], "Idę do domu.", {"อยู่": "อยู่ to „znajdować się”. Ruch: ไป."}),
         (["ฉัน", "ไป", "ตลาด", "ค่ะ"], "Idę na targ. (kobieta)", {}),
         (["ผม", "ไป", "กรุงเทพ", "ครับ"], "Jadę do Bangkoku. (mężczyzna)", {}),
         (["แท็กซี่", "อยู่", "ทาง", "ขวา"], "Taksówka jest po prawej.", {"ซ้าย": "ซ้าย to „lewy”."}),
         (["โรงเรียน", "อยู่", "ที่นี่"], "Szkoła jest tu.", {"ที่นั่น": "ที่นั่น to „tam”."}),
         (["แม่", "อยู่", "ที่", "บ้าน"], "Mama jest w domu.", {}),
     ]},
]
UNITS[6]["words"] += [("ที่", "w; przy (miejsce)", None, None, "thîi")]

INSIGHTS = {
    "wymowa": [{"title": "Pięć tonów i brak spacji", "chain": [],
                "text": "Tajski ma pięć tonów: środkowy, niski, opadający, wysoki i rosnący. Zmiana tonu zmienia słowo. Piszesz bez spacji między wyrazami; pod słowami zobaczysz zapis wymowy z tonami: ` niski, ^ opadający, ´ wysoki, ˇ rosnący, bez znaku środkowy. Spółgłoski dzielą się na trzy klasy (średnią, wysoką, niską), która wraz ze znakiem tonu ustala ton."}],
    "slowa": [{"title": "ครับ i ค่ะ", "chain": [
                ("Dzień dobry. (mężczyzna mówi)", ["สวัสดี", "ครับ"], "Mężczyzna dodaje ครับ."),
                ("Dzień dobry. (kobieta mówi)", ["สวัสดี", "ค่ะ"], "Kobieta dodaje ค่ะ."),
            ],
            "text": "Grzeczność w tajskim zależy od płci mówiącego, a nie słuchacza: mężczyzna kończy zdania ครับ, kobieta ค่ะ (w pytaniach คะ)."}],
    "ja": [{"title": "Brak odmiany", "chain": [],
            "text": "Tajski nie odmienia czasowników i nie ma rodzaju. „Jestem, jesteś, jest” to zawsze เป็น (tożsamość) lub อยู่ (miejsce). Pytanie robisz, dodając ไหม na końcu zdania."}],
    "liczby": [{"title": "Liczniki", "chain": [],
                "text": "Po liczebniku stawiasz licznik: osoby liczysz z คน (ลูกสองคน = dwoje dzieci). Dla innych rzeczy są inne liczniki, a tu poznajesz najczęstszy."}],
}

ENDINGS_INSIGHT = {"title": "Partykuły",
                   "text": "Po tajsku nie ma końcówek, za to są partykuły: ครับ i ค่ะ (grzeczność), ไหม (pytanie), ไม่ (przeczenie). Tu je ćwiczysz."}

ENDINGS = [
    ("ผมเป็นนักเรียน", "", "ครับ", "", ["ครับ", "ค่ะ"], "mężczyzna mówi", "Mężczyzna kończy zdanie ครับ.", "slowa"),
    ("ฉันเป็นนักเรียน", "", "ค่ะ", "", ["ครับ", "ค่ะ"], "kobieta mówi", "Kobieta kończy zdanie ค่ะ.", "slowa"),
    ("คุณเป็นครู", "", "ไหม", "", ["ไหม", "ไม่"], "pytanie „czy?”", "ไหม robi pytanie.", "ja"),
    ("ผม", "", "ไม่", "เป็นครู", ["ไหม", "ไม่"], "przeczenie", "ไม่ stoi przed czasownikiem.", "ja"),
    ("คุณอยากกินข้าว", "", "ไหม", "", ["ไหม", "ไม่"], "pytanie „czy?”", "ไหม robi pytanie.", "jedzenie"),
    ("ผมไป", "", "บ้าน", "", ["บ้าน", "ที่บ้าน"], "idę do domu", "Po ไป bez ที่.", "miejsca"),
]

CHAT_EXTRA = {"แพร": "Phrae (imię)", "สมชาย": "Somchai (imię)", "คนขับรถ": "kierowca"}

CHATS = [
    {"id": "kafe", "title": "W kawiarni", "partner": "แพร", "avatar": "แ", "requires": "jedzenie",
     "turns": [
         {"bot": ["สวัสดี", "ค่ะ"], "en": "Dzień dobry.",
          "options": [(["สวัสดี", "ครับ"], True, None), (["ขอบคุณ", "ครับ"], False, "ขอบคุณ to „dziękuję”. Powitaj: สวัสดี.")]},
         {"bot": ["คุณ", "อยาก", "ดื่ม", "กาแฟ", "ไหม"], "en": "Chce pan kawy?",
          "options": [(["ผม", "อยาก", "ดื่ม", "กาแฟ", "ครับ"], True, None),
                      (["สวัสดี", "ครับ"], False, "To powitanie, a pytają o kawę.")]},
         {"bot": ["คุณ", "อยาก", "กิน", "ข้าว", "ไหม"], "en": "Chce pan ryżu?",
          "options": [(["ไม่", "ขอบคุณ", "ครับ"], True, None),
                      (["ขอโทษ", "ครับ"], False, "ขอโทษ to „przepraszam”, nie odmowa.")]},
         {"bot": ["ดี", "มาก"], "build": (["ขอบคุณ", "ครับ"], "Dziękuję!"), "en": "Bardzo dobrze."},
     ]},
    {"id": "tuukjak", "title": "Poznajemy się", "partner": "สมชาย", "avatar": "ส", "requires": "ludzie",
     "turns": [
         {"bot": ["สวัสดี", "ครับ"], "en": "Dzień dobry.",
          "options": [(["สวัสดี", "ครับ"], True, None), (["ขอโทษ", "ครับ"], False, "ขอโทษ to „przepraszam”. Powitaj: สวัสดี.")]},
         {"bot": ["คุณ", "มาจาก", "ไทย", "ไหม"], "en": "Jest pan z Tajlandii?",
          "options": [(["ไม่", "ผม", "มาจาก", "โปแลนด์", "ครับ"], True, None),
                      (["ใช่", "ผม", "มาจาก", "โปแลนด์", "ครับ"], False, "ใช่ to „tak”, a odpowiedź przeczy pytaniu.")]},
         {"bot": ["คุณ", "มี", "ลูก", "ไหม"], "en": "Ma pan dzieci?",
          "options": [(["ผม", "มี", "ลูก", "สอง", "คน", "ครับ"], True, None),
                      (["ผม", "มี", "ลูก", "สอง", "บาท", "ครับ"], False, "บาท to waluta. Osoby liczysz คน.")]},
         {"bot": ["ลาก่อน", "ครับ"], "build": (["ลาก่อน", "ครับ"], "Do widzenia!"), "en": "Do widzenia!"},
     ]},
    {"id": "taxi", "title": "W taksówce", "partner": "คนขับรถ", "avatar": "ค", "requires": "miejsca",
     "turns": [
         {"bot": ["สวัสดี", "ครับ"], "en": "Dzień dobry.",
          "options": [(["สวัสดี", "ครับ"], True, None), (["ลาก่อน", "ครับ"], False, "ลาก่อน to „do widzenia”. Powitaj: สวัสดี.")]},
         {"bot": ["คุณ", "ไป", "ที่ไหน", "ครับ"], "en": "Dokąd pan jedzie?",
          "options": [(["ผม", "ไป", "โรงแรม", "ครับ"], True, None),
                      (["ผม", "อยู่", "โรงแรม", "ครับ"], False, "อยู่ to „być w miejscu”. „Jadę”: ไป.")]},
         {"bot": ["โรงแรม", "อยู่", "ทาง", "ขวา"], "en": "Hotel jest po prawej.",
          "options": [(["ขอบคุณ", "ครับ"], True, None), (["ขอโทษ", "ครับ"], False, "Dziękujesz: ขอบคุณ.")]},
         {"bot": ["ดี", "มาก"], "build": (["ขอบคุณ", "ครับ"], "Dziękuję!"), "en": "Bardzo dobrze."},
     ]},
]

PARADIGM_LABELS = {
    'l15': ['1', '2', '3', '4', '5'],
    'l610': ['6', '7', '8', '9', '10'],
    'plec': ['mężczyzna', 'kobieta'],
}

PARADIGMS = [
    ('form', 'Liczebniki', 'Liczebniki 1 do 5', 'l15', 'หนึ่ง; สอง; สาม; สี่; ห้า', None),
    ('form', 'Liczebniki', 'Liczebniki 6 do 10', 'l610', 'หก; เจ็ด; แปด; เก้า; สิบ', None),
    ('form', 'Grzeczność', 'Partykuła na końcu zdania', 'plec', 'ครับ; ค่ะ', 'Zależy od płci mówiącego, nie słuchacza.'),
    ('form', 'Grzeczność', 'Ja', 'plec', 'ผม; ฉัน', 'Mężczyzna: ผม, kobieta: ฉัน.'),
]

LARPS = []

# Pełne tłumaczenia zdań z ćwiczeń „Uzupełnij końcówkę” (gdy nie ma ich wśród zdań kursu)
ENDINGS_PL = {'ผมไม่เป็นครู': 'Nie jestem nauczycielem.', 'คุณอยากกินข้าวไหม': 'Chcesz zjeść ryż?'}

# === STOPNIOWANIE (generowane, nie edytuj ręcznie) ===
PARADIGMS += [
    ('form', 'Stopniowanie', 'ดี (dobry)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'ดี; ดีกว่า; ดีที่สุด', 'Wyższy: słowo + กว่า, najwyższy: słowo + ที่สุด.'),
    ('form', 'Stopniowanie', 'ใหญ่ (duży)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'ใหญ่; ใหญ่กว่า; ใหญ่ที่สุด', None),
    ('form', 'Stopniowanie', 'เล็ก (mały)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'เล็ก; เล็กกว่า; เล็กที่สุด', None),
    ('form', 'Stopniowanie', 'แพง (drogi)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'แพง; แพงกว่า; แพงที่สุด', None),
    ('form', 'Stopniowanie', 'ถูก (tani)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'ถูก; ถูกกว่า; ถูกที่สุด', None),
    ('form', 'Stopniowanie', 'สูง (wysoki)', ['stopień równy', 'stopień wyższy', 'stopień najwyższy'], 'สูง; สูงกว่า; สูงที่สุด', None),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /STOPNIOWANIE ===

# === GRAMATYKA 2 (generowane) ===
PARADIGMS += [
    ('form', 'Czasy i przeczenie', 'กิน (jeść)', ['zwykle', 'już zrobione (แล้ว)', 'przyszłość (จะ)', 'właśnie trwa (กำลัง)', 'przeczenie (ไม่)'], 'กิน; กินแล้ว; จะกิน; กำลังกิน; ไม่กิน', 'Tajski nie odmienia czasowników: znaczenie dodają słówka przed i po czasowniku.'),
    ('form', 'Czasy i przeczenie', 'ไป (iść)', ['zwykle', 'już zrobione (แล้ว)', 'przyszłość (จะ)', 'właśnie trwa (กำลัง)', 'przeczenie (ไม่)'], 'ไป; ไปแล้ว; จะไป; กำลังไป; ไม่ไป', None),
    ('form', 'Czasy i przeczenie', 'ดู (patrzeć)', ['zwykle', 'już zrobione (แล้ว)', 'przyszłość (จะ)', 'właśnie trwa (กำลัง)', 'przeczenie (ไม่)'], 'ดู; ดูแล้ว; จะดู; กำลังดู; ไม่ดู', None),
    ('form', 'Czasy i przeczenie', 'ทำ (robić)', ['zwykle', 'już zrobione (แล้ว)', 'przyszłość (จะ)', 'właśnie trwa (กำลัง)', 'przeczenie (ไม่)'], 'ทำ; ทำแล้ว; จะทำ; กำลังทำ; ไม่ทำ', None),
    ('form', 'Czasy i przeczenie', 'เรียน (uczyć się)', ['zwykle', 'już zrobione (แล้ว)', 'przyszłość (จะ)', 'właśnie trwa (กำลัง)', 'przeczenie (ไม่)'], 'เรียน; เรียนแล้ว; จะเรียน; กำลังเรียน; ไม่เรียน', None),
    ('form', 'Pytania', 'กิน: pytanie', ['czy zrobisz? (ไหม)', 'czy tak? (หรือเปล่า)', 'czy już? (หรือยัง)'], 'กินไหม; กินหรือเปล่า; กินแล้วหรือยัง', 'Pytania tak/nie tworzy się partykułą na końcu zdania.'),
    ('form', 'Pytania', 'ไป: pytanie', ['czy zrobisz? (ไหม)', 'czy tak? (หรือเปล่า)', 'czy już? (หรือยัง)'], 'ไปไหม; ไปหรือเปล่า; ไปแล้วหรือยัง', None),
    ('form', 'Zaimki', 'zaimki dzierżawcze: ของ', ['mój', 'twój', 'jego, jej', 'nasz'], 'ของฉัน; ของคุณ; ของเขา; ของเรา', 'Zaimek posiadacza stoi po rzeczowniku: บ้านของฉัน.'),
]
_o = []
for _p in PARADIGMS:
    if _p[1] not in _o:
        _o.append(_p[1])
PARADIGMS.sort(key=lambda p: _o.index(p[1]))
# === /GRAMATYKA 2 ===
