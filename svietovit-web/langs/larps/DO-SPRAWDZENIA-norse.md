# Larpy (norse): do sprawdzenia przez natywnego speakera

Sprawdź naturalność, formę grzecznościową, pisownię i czy wyjaśnienia są prawdziwe. Wszystko napisane z głowy przez AI. Poprawki wpisz w tabelę albo komentarzem.

## W hali gospodarza (karczma)

**Scena:** Jesteś w drodze na Althing. Wieczorem docierasz do hali gospodarza przy szlaku: zmęczony, głodny i spragniony. Przy ogniu czeka gospodarz.  
**Cel:** Zamów miód pitny, chleb i solone ryby, a potem zapłać i zobacz, czy twój pobratymiec już dotarł.  
**Rozmówca:** Húsbóndi  
**Zakończenia:** win: Gospodarz jest pod wrażeniem, że tak dobrze mówisz po nordycku. „Heill ok sæll, gestr!” – dostajesz ucztę na koszt domu i najlepsze miejsce przy ogniu. · partial: Posiłek dotarł na stół, choć kilka razy musiałeś poprawiać. Gospodarz kiwa głową i przynosi ci misę. · fail: Gospodarz ma dość: nie zrozumiał cię kilka razy z rzędu i każe ci spać w stajni.  

### Poziom 1: Miód, chleb i ryba  (typed=0, hint=none, cierpliwość 6)

Nowe słowa: fóstbróður = pobratymca (biernik), bíð = czekam (bíða), sit = siądź (sitja), gef = daj (gefa), mér = mi, þat = to, allt = wszystko, boð = wiadomość

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Wieczór przy szlaku na Althing. Umówiłeś się tu z Þorgeirem, swoim pobratymcem (fóstbróðir), ale jego jeszcze nie ma. Wchodzisz do hali i siadasz, żeby poczekać.  
*Cel:* Zamów miód pitny, wodę, rybę z chlebem i masło, a przy okazji dowiedz się, co z Þorgeirem.  
*Zakończenia:* win: Gospodarz podaje ci wiadomość od Þorgeira: „Spóźnię się. Jutro rano zjemy razem, a potem ruszamy na Althing.” Masz plan na jutro. · partial: Posiłek dotarł, a gospodarz podaje ci wiadomość od Þorgeira, chociaż z trudem zrozumiał, czego chcesz. Þorgeirr przeprasza i zaprasza na jutro. · fail: Gospodarz nie wie, kim jesteś. Wiadomość od Þorgeira trafia do kogoś innego, a ty kładziesz się spać głodny.

| 1 | Heill ok sæll, gestr! Ert þú einn? *(Witaj, szczęśliwy gościu! Czy jesteś sam?)* | **Heill! Já, ek em einn. Ek bíð fóstbróður.** *(Przywitaj się, potwierdź, że jesteś sam, i powiedz, że czekasz na pobratymca.)* | „Jestem” to ek em, „czekam” to ek bíð; fóstbróðir to „pobratymiec”. |
| 2 | Sit hér. Hvat vilt þú drekka? *(Siądź tu. Czego chcesz się napić?)* | **Ek vil mjǫð.** *(Zamów miód pitny.)* | Mjǫðr jest rodzaju męskiego; po „vil” biernik: mjǫð. |
| 3 | Hér er mjǫðr. Vilt þú ok vatn? *(Oto miód. Chcesz też wody?)* | **Já, gef mér vatn.** *(Zgódź się na wodę.)* | „Daj mi” to gef mér. |
| 4 | Hvat vilt þú eta? Hér eru brauð, fiskr ok kjǫt. *(Co chcesz zjeść? Oto chleb, ryba i mięso.)* | **Ek vil fisk ok brauð.** *(Zamów rybę i chleb.)* | Fiskr jest rodzaju męskiego; w bierniku: fisk. Brauð nie zmienia formy. |
| 5 | Vilt þú ok smjǫr? *(Chcesz też masła?)* | **Já, gef mér smjǫr.** *(Zgódź się na masło.)* | Smjǫr to „masło”; „daj mi” to gef mér. |
| 6 | Vilt þú hunang eða skyr? *(Chcesz miodu czy twarogu?)* | **Gef mér hunang.** *(Wybierz miód pszczeli.)* | Hunang to miód pszczeli (mjǫðr to miód pitny); „eða” to „lub”. |
| 7 | Hér er mjǫðr ok brauð. *(Oto miód pitny i chleb.)* | **Þökk!** *(Podziękuj gospodarzowi.)* | Þökk to „dziękuję”. |
| 8 | Vilt þú nǫkkut? *(Chcesz coś jeszcze?)* | **Nei, þökk. Þat er allt.** *(Odmów: to już wszystko.)* | „To wszystko” to þat er allt. |
| 9 | Heill, gestr! Hér er boð frá fóstbróður. *(Witaj, gościu! Oto wiadomość od pobratymca.)* | — |  |

### Poziom 2: Poranek  (typed=0.25, hint=bank, cierpliwość 6)

Nowe słowa: dagverð = śniadanie (biernik od dagverðr), kǫku = placek (biernik od kaka), þik = ciebie (biernik), móður = matkę (biernik), mína = moją (biernik, rodzaj żeński), kem = przyjdę (koma)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Następnego ranka. Þorgeirr czeka już przy ławie, a gospodarz przyjmuje zamówienia. Þorgeirr prosi, żebyś zamówił sam, a przy okazji kupił placek dla twojej matki.  
*Cel:* Zamów śniadanie i kup placek dla swojej matki.  
*Zakończenia:* win: Þorgeirr się śmieje: „Þú mælir sem norrœnn maðr!” Placek dla matki zapakowany, a Þorgeirr obiecuje, że ruszycie razem na Althing. · partial: Śniadanie jest, placek też, ale Þorgeirr musiał pomóc ci kilka razy. Obiecuje, że następnym razem zamówisz sam. · fail: Pomyliłeś zamówienia i Þorgeirr dostał coś zupełnie innego. Zjadł w milczeniu i wyszedł do koni.

| 1 | Góðan dag, gestr! Vilt þú dagverð? *(Dzień dobry, gościu! Czy chcesz śniadanie?)* | **Já, ek vil dagverð.** *(Powiedz, że chcesz zjeść śniadanie.)* | Dagverðr to „śniadanie”; w bierniku dagverð. |
| 2 | Hér eru brauð, egg ok ostr. Hvat vilt þú? *(Oto chleb, jajka i ser. Czego chcesz?)* | **Ek vil tvau egg ok brauð.** *(Zamów dwa jajka i chleb.)* | Egg jest nijakie, więc „dwa” to tvau; liczba mnoga egg wygląda tak samo jak pojedyncza. |
| 3 | Vilt þú mjǫð eða ǫl? *(Chcesz miód pitny czy piwo?)* | **Gef mér ǫl.** *(Wybierz piwo.)* | Ǫl jest nijakie: w bierniku wygląda tak samo. |
| 4 | Vilt þú mjólk? *(Chcesz mleka?)* | **Já, mjólk ok hunang.** *(Zgódź się na mleko z miodem.)* | Ok to „i”; mjólk ok hunang to „mleko i miód”. |
| 5 | Vilt þú ok seyði? *(Chcesz też zupy?)* | **Nei, ek vil ekki seyði.** *(Odmów zupy.)* | „Nie chcę” to ek vil ekki. |
| 6 | Vilt þú kaupa kǫku eða flatbrauð? *(Chcesz kupić placek czy chleb płaski?)* | **Ek vil kaupa kǫku.** *(Wybierz placek: chcesz go kupić.)* | Kaka jest rodzaju żeńskiego; w bierniku kǫku. „Kupić” to kaupa (bezokolicznik na końcu). |
| 7 | Er þat fyrir þik? *(Czy to dla ciebie?)* | **Nei, þat er fyrir móður mína.** *(Zaprzecz: to dla twojej matki.)* | „Dla” to fyrir, a po nim biernik: móðir → móður, mín → mína. |
| 8 | Bíð hér. Ek kem brátt. *(Czekaj tu. Zaraz wrócę.)* | **Þökk, ek bíð hér.** *(Podziękuj i powiedz, że poczekasz.)* | „Czekam” to ek bíð; brátt to „wkrótce”. |
| 9 | Hér er allt, gestr. *(Oto wszystko, gościu.)* | **Þökk, bóndi!** *(Podziękuj gospodarzowi.)* | Bóndi to „gospodarz”; þökk to „dziękuję”. |
| 10 | Heill, gestr! *(Witaj, gościu!)* | — |  |

### Poziom 3: Ława, pytania i cena  (typed=0.5, hint=bank, cierpliwość 5)

Nowe słowa: bekk = ławę (biernik), eldi = ognisku (celownik), hefir = masz (hafa), dýrt = drogie (rodzaj nijaki), nóg = dość

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Po południu. Þorgeirr jest zajęty końmi, więc umówiłeś się z jego siostrą, Þórdís. Gospodarz pyta o miejsce, a ty musisz wybrać jedzenie i dowiedzieć się, ile to kosztuje.  
*Cel:* Znajdź dla was miejsce, zamów posiłek dla obojga i nie przepłać.  
*Zakończenia:* win: Þórdís jest zachwycona: „Nú skil ek, hví Þorgeirr mælir svá vel um þik!” Zaprasza cię wieczorem do domu swej rodziny. · partial: Posiłek się udał, ale Þórdís musiała kilka razy tłumaczyć gospodarzowi, czego chcesz. Wieczorne spotkanie nadal aktualne. · fail: Nie dogadałeś się z gospodarzem, a Þórdís patrzyła na to z niedowierzaniem. Wieczorem słyszysz od niej: „Annat sinn!”

| 1 | Heill ok sæll! Vilt þú sitja á bekk eða hjá eldi? *(Witaj! Chcesz siedzieć na ławie czy przy ognisku?)* | **Ek vil sitja hjá eldi.** *(Powiedz, że chcesz siedzieć przy ognisku.)* | „Przy” to hjá; po nim celownik: eldr → eldi. Bezokolicznik (sitja) stoi po „vil”. |
| 2 | Hvat vilt þú drekka? *(Czego chcesz się napić?)* | **Gef mér mjǫð ok vatn.** *(Zamów miód i wodę.)* | „Daj mi” to gef mér; mjǫð to biernik od mjǫðr. |
| 3 | Hér eru seyði ok saltfiskr. Vilt þú seyði? *(Oto zupa i solona ryba. Chcesz zupy?)* | **Nei, ek vil ekki seyði. Hefir þú kjǫt?** *(Odmów zupy i zapytaj o mięso.)* | „Masz” w pytaniu to hefir þú (czasownik przed podmiotem). |
| 4 | Já. Kjǫt er mjǫk gott. *(Tak. Mięso jest bardzo dobre.)* | **Gott. Ek vil kjǫt.** *(Zdecyduj się na mięso.)* | „Dobrze” to gott. |
| 5 | Vilt þú ok kál eða ber? *(Chcesz też kapusty czy jagód?)* | **Ek vil ber.** *(Wybierz jagody.)* | „Lub” to eða; ber to „jagody”. |
| 6 | Hér er mjǫðr ok kjǫt. *(Oto miód i mięso.)* | **Hvat er verð?** *(Zapytaj o cenę.)* | „Jaka jest cena?” to hvat er verð? (dosłownie „co jest cena”). |
| 7 | Verð er tvau silfr. *(Cena to dwa srebrne.)* | **Þat er eigi dýrt. Ek vil kjǫt.** *(Powiedz, że to niedrogie, i weź mięso.)* | Eigi to „nie”; dýrt (nijaki), bo þat jest nijakie. |
| 8 | Vilt þú kjǫt nú eða síðar? *(Chcesz mięso teraz czy później?)* | **Ek vil kjǫt síðar.** *(Powiedz, że mięso chcesz później.)* | „Później” to síðar. |
| 9 | Vel. Vilt þú ok mjǫð? *(Dobrze. Chcesz też miodu?)* | **Nei, þökk. Þat er nóg.** *(Grzecznie odmów: to wystarczy.)* | „To wystarczy” to þat er nóg. |
| 10 | Vel! Bíð hér, gestr. *(Dobrze! Czekaj tu, gościu.)* | — |  |

### Poziom 4: Rozmowa przy ławie  (typed=0.75, hint=letters, cierpliwość 5)

Nowe słowa: mælir = mówisz (mæla), hvaðan = skąd, lengi = długo, kom = przybyłem (koma), leið = droga, podróż, ost = ser (biernik od ostr), heitt = gorące (rodzaj nijaki)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Wieczorem Þorgeirr zabiera cię do hali, której gospodynią jest jego ciotka. Húsfreyja zna wszystkich, a ciebie wypytuje jak nowego znajomego Þorgeira.  
*Cel:* Odpowiadaj na pytania gospodyni o to, skąd jesteś i dokąd jedziesz. Jeśli jej się spodobasz, Þorgeirr weźmie cię jutro na Althing.  
*Zakończenia:* win: Gospodyni klepie cię po ramieniu: „Hann er nú einn af oss!” Þorgeirr mówi, że jutro razem kupicie konie i ruszycie na Althing. · partial: Gospodyni jest uprzejma, ale nie do końca przekonana. Þorgeirr uspokaja: „Hon þarf tíma.” Jutro i tak idziecie razem po konie. · fail: Gospodyni przestała cię rozumieć w połowie wywiadu i uznała, że jesteś nieszczery. Þorgeirr wychodzi zakłopotany.

| 1 | Heill ok sæll! Hvat vilt þú drekka? *(Witaj! Czego chcesz się napić?)* | **Ek vil ǫl ok vatn, húsfreyja.** *(Zamów piwo i wodę, zwracając się do gospodyni.)* | Ǫl jest nijakie; vatn też. Húsfreyja to „gospodyni”. |
| 2 | Þú mælir vel. Hvaðan ert þú? *(Dobrze mówisz. Skąd jesteś?)* | **Þökk! Ek em frá Noregi.** *(Podziękuj i powiedz, że jesteś z Norwegii.)* | „Z” w znaczeniu pochodzenia to frá; po nim celownik: Noregr → Noregi. |
| 3 | Frá Noregi! Hvé lengi ert þú hér? *(Z Norwegii! Jak długo tu jesteś?)* | **Ek kom í gær.** *(Powiedz, że przybyłeś wczoraj.)* | „Przybyłem” to ek kom (czas przeszły od koma); „wczoraj” to í gær. |
| 4 | Gott! Ert þú á leið á þing? *(Dobrze! Czy jedziesz na zgromadzenie?)* | **Já, ek fer á þing.** *(Potwierdź: jedziesz na Althing.)* | „Jadę” to ek fer; „na zgromadzenie” to á þing (á + biernik przy ruchu). |
| 5 | Seyði er gott. Vilt þú seyði? *(Zupa jest dobra. Chcesz zupy?)* | **Já, ek vil seyði. Er kjǫt í seyði?** *(Zgódź się na zupę i zapytaj, czy jest w niej mięso.)* | „Czy jest w niej mięso?” to er kjǫt í seyði? (pytanie przez szyk: czasownik na początku). |
| 6 | Nei, ekki kjǫt. Vilt þú brauð? *(Nie, bez mięsa. Chcesz chleba?)* | **Já, gef mér brauð ok ost.** *(Zgódź się: chleb i ser.)* | Ostr jest męskie; w bierniku: ost. |
| 7 | Hvé er seyði? *(Jaka jest zupa?)* | **Seyði er gott, en heitt.** *(Pochwal zupę, ale zaznacz, że jest gorąca.)* | „Ale” to en; seyði jest nijakie: gott, heitt. |
| 8 | Vilt þú ok ǫl? *(Chcesz też piwa?)* | **Nei, þökk. Nú vil ek mjǫð.** *(Odmów i powiedz, że teraz chcesz miód pitny.)* | „Teraz” to nú. |
| 9 | Ert þú kaupmaðr? *(Czy jesteś kupcem?)* | **Nei, ek em skáld.** *(Zaprzecz: jesteś poetą.)* | Przy zawodzie nie ma rodzajnika: ek em skáld. |
| 10 | Þú ert góðr gestr! *(Jesteś dobrym gościem!)* | — |  |

### Poziom 5: Pełna wizyta i zapłata  (typed=1, hint=none, cierpliwość 4)

Nowe słowa: saltfisk = solona ryba (biernik), gjarna = chętnie, þinn = twój (rodzaj męski), gistingu = gościnę (biernik)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Ostatni poranek w hali. Z samego rana siadasz, żeby zjeść pożegnalny posiłek i zapłacić. Za godzinę Þorgeirr ma czekać przy stajni, a ty kupisz konia na Althing.  
*Cel:* Zamów pełne śniadanie z solonymi rybami, usiądź przy oknie, zapłać i pożegnaj się. Nie możesz się spóźnić.  
*Zakończenia:* win: Gospodyni życzy ci szczęśliwej drogi i wręcza paczkę placków „na drogę”. Biegniesz do stajni, a tam czeka Þorgeirr. · partial: Zapłaciłeś, ale straciłeś sporo czasu na poprawki. Biegniesz do stajni w ostatniej chwili. · fail: Zapłata zrobiła się kłopotliwa, gospodarz nie rozumiał, ile masz zapłacić. Þorgeirr odjechał bez ciebie.

| 1 | Góðan dag! Hvat vilt þú drekka? *(Dzień dobry! Czego chcesz się napić?)* | **Góðan dag! Ek vil mjǫð, en eigi ǫl.** *(Przywitaj się i zamów miód pitny, ale nie piwo.)* | „Ale” to en; „nie” to eigi. |
| 2 | Vel. Hér eru brauð, egg, saltfiskr ok kjǫt. *(Dobrze. Oto chleb, jajka, solona ryba i mięso.)* | **Ek vil brauð ok saltfisk.** *(Zamów chleb i solone ryby.)* | Saltfiskr jest męskie; w bierniku saltfisk. |
| 3 | Vilt þú ok vatn? *(Chcesz też wody?)* | **Já, gjarna. Hvat er ok gott?** *(Zgódź się chętnie i zapytaj, co jeszcze jest dobre.)* | „Chętnie” to gjarna; „co jeszcze jest dobre?” to hvat er ok gott? |
| 4 | Seyði er gott í dag. *(Zupa jest dziś dobra.)* | **Þá vil ek seyði.** *(Zdecyduj się na zupę.)* | Þá to „w takim razie”; czasownik stoi na drugim miejscu: þá vil ek. |
| 5 | Vilt þú sitja hér eða þar? *(Chcesz siedzieć tu czy tam?)* | **Ek vil sitja hjá vindauga.** *(Powiedz, że chcesz siedzieć przy oknie.)* | „Przy” to hjá; „okno” to vindauga. |
| 6 | Hér er dagverðr þinn. *(Oto twoje śniadanie.)* | **Þökk, húsfreyja!** *(Podziękuj gospodyni.)* | Þökk to „dziękuję”. |
| 7 | Er seyði gott? *(Czy zupa jest dobra?)* | **Já, seyði er mjǫk gott.** *(Potwierdź: zupa jest bardzo dobra.)* | Seyði jest nijakie: gott. |
| 8 | Vilt þú nǫkkut ok? *(Chcesz coś jeszcze?)* | **Nei, þökk. Ek vil gjalda.** *(Odmów i powiedz, że chcesz zapłacić.)* | „Płacić” to gjalda (bezokolicznik na końcu). |
| 9 | Verð er fimm silfr. *(Cena to pięć srebrnych.)* | **Hér eru tíu silfr. Þökk fyrir gistingu!** *(Zapłać z nawiązką i podziękuj za gościnę.)* | „Dziękuję za” to þökk fyrir + biernik: gisting → gistingu. |
| 10 | Far vel, gestr! *(Bądź zdrów, gościu!)* | **Far vel! Heill, húsfreyja!** *(Pożegnaj się.)* | Far vel to „bądź zdrów” przy rozstaniu. |
| 11 | Heill ok sæll! *(Bądź zdrów i szczęśliwy!)* | — |  |

## Koń na Althing (stajnia)

**Scena:** Rano po zapłaceniu rachunku idziesz do stajni gospodarza. Þorgeirr czeka na ciebie przy szlaku, a droga na Althing jest długa.  
**Cel:** Kup konia, siodło i uzdę i dojedź na Althing.  
**Rozmówca:** Bóndi  
**Zakończenia:** win: Siedzisz na koniu, a Þorgeirr jedzie obok z szerokim uśmiechem. Althing czeka na was za górą. · partial: Dotarłeś na Althing, ale kilka razy ktoś musiał ci pomagać. Þorgeirr mówi: „Na następny raz poćwicz jeszcze pytania.” · fail: Þorgeirr odjechał bez ciebie, a ty zostajesz z koniem na rozstajach. Althing zaczyna się bez ciebie.  

### Poziom 1: Koń  (typed=0, hint=none, cierpliwość 5)

Nowe słowa: hest = konia (biernik), hans = jego (dopełniacz od hann), átta = osiem

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Mgliste przedpołudnie. Gospodarz prowadzi cię do stajni. Kilka koni stoi w boksach, a Þorgeirr czeka przy bramie.  
*Cel:* Wybierz konia, dowiedz się, ile kosztuje, i zapłać.  
*Zakończenia:* win: Gospodarz wręcza ci uzdę konia: „Góða ferð!” Þorgeirr już siedzi na swoim koniu. · partial: Kupiłeś konia, ale gospodarz kilka razy musiał powtarzać cenę. Þorgeirr niecierpliwie czeka przy bramie. · fail: Gospodarz nie zrozumiał, który koń ci się podoba. Þorgeirr wzdycha i jedzie sam.

| 1 | Heill, gestr! Hvat vilt þú? *(Witaj, gościu! Czego chcesz?)* | **Heill! Ek vil kaupa hest.** *(Przywitaj się i powiedz, że chcesz kupić konia.)* | Hestr jest męski; w bierniku hest. „Kupić” to kaupa (bezokolicznik na końcu). |
| 2 | Hér eru hestr ok merr. Hvat vilt þú? *(Oto koń i klacz. Czego chcesz?)* | **Ek vil hest. Er hann góðr?** *(Powiedz, że chcesz konia, i zapytaj, czy jest dobry.)* | Hestr jest męski, więc „on” to hann. |
| 3 | Já, hann er ungr ok sterkr. *(Tak, jest młody i silny.)* | **Er hann skjótr?** *(Zapytaj, czy jest szybki.)* | Hestr jest męski: hann, skjótr. |
| 4 | Já, hann er skjótr. Hann er brúnn. *(Tak, jest szybki. Jest gniady.)* | **Gott. Hvat er verð hans?** *(Zapytaj o cenę konia.)* | „Jego cena” to verð hans (dosłownie „cena jego”). |
| 5 | Verð hans er tíu silfr. *(Jego cena to dziesięć srebrnych.)* | **Þat er mikit. Ek á fimm silfr.** *(Powiedz, że to dużo, i że masz pięć srebrnych.)* | Ek á to „mam”; þat to „to”. |
| 6 | Þá er verð átta silfr. *(W takim razie cena to osiem srebrnych.)* | **Já, þat er gott verð. Hér eru átta silfr.** *(Zgódź się i zapłać osiem srebrnych.)* | „Oto” przy liczbie mnogiej to hér eru. |
| 7 | Þökk! Hér er hestr þinn. *(Dzięki! Oto twój koń.)* | **Þökk! Hann er góðr hestr.** *(Podziękuj i pochwal konia.)* | Þökk to „dziękuję”. |
| 8 | Far vel, gestr! Góða ferð! *(Bądź zdrów, gościu! Szczęśliwej drogi!)* | — |  |

### Poziom 2: Siodło i uzda  (typed=0.25, hint=bank, cierpliwość 5)

Nowe słowa: sǫðul = siodło (biernik), sex = sześć, hvert = dokąd, langt = daleko; długie (rodzaj nijaki)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Koń jest twój, ale nie ma jeszcze siodła ani uzdy. Stajenny stoi z naręczem rzemieni, a Þorgeirr przygląda się z siodła.  
*Cel:* Kup siodło, uzdę i strzemiona, zapłać i zaopatrz się na drogę.  
*Zakończenia:* win: Stajenny zapina popręg: „Hestr þinn er búinn!” Þorgeirr kiwa głową i prowadzi cię na szlak. · partial: Wszystko kupiłeś, ale stajenny kilka razy powtarzał pytania. Þorgeirr niecierpliwie czeka. · fail: Stajenny nie zrozumiał, czego chcesz, i dał ci stare, zniszczone siodło. Koń rzuca cię na pierwszym zakręcie.

| 1 | Heill! Hestr þinn er góðr. Hvat vilt þú? *(Witaj! Twój koń jest dobry. Czego chcesz?)* | **Gef mér sǫðul ok beizl.** *(Poproś o siodło i uzdę.)* | Sǫðull to męskie, w bierniku sǫðul; beizl nie zmienia formy. „Daj mi” to gef mér. |
| 2 | Hér eru sǫðull ok beizl. Vilt þú ok stigreip? *(Oto siodło i uzda. Chcesz też strzemiona?)* | **Já, ek vil ok stigreip.** *(Zgódź się na strzemiona.)* | Stigreip to „strzemię”; ok to „też”. |
| 3 | Já, hér er stigreip. *(Tak, oto strzemiona.)* | **Hvat er verð?** *(Zapytaj o cenę.)* | „Jaka jest cena?” to hvat er verð? |
| 4 | Verð er sex silfr. *(Cena to sześć srebrnych.)* | **Hér eru sex silfr.** *(Zapłać sześć srebrnych.)* | „Oto” przy liczbie mnogiej to hér eru. |
| 5 | Hvert fer þú? *(Dokąd jedziesz?)* | **Ek fer á þing.** *(Powiedz, że jedziesz na Althing.)* | „Jadę” to ek fer; „na zgromadzenie” to á þing. |
| 6 | Þing er langt. Fer þú einn? *(Zgromadzenie jest daleko. Czy jedziesz sam?)* | **Nei, ek fer með fóstbróður.** *(Zaprzecz: jedziesz z pobratymcem.)* | „Z” to með; „pobratymca” to fóstbróður. |
| 7 | Veðr er eigi gott í dag. Er hestr þinn sterkr? *(Pogoda dziś nie jest dobra. Czy twój koń jest silny?)* | **Já, hann er sterkr.** *(Potwierdź: koń jest silny.)* | Hestr jest męski: hann, sterkr. |
| 8 | Vilt þú brauð ok vatn á ferð? *(Chcesz chleb i wodę na drogę?)* | **Já, gef mér brauð ok vatn.** *(Zgódź się: chleb i woda na drogę.)* | „Daj mi” to gef mér. |
| 9 | Þökk fyrir, gestr! Far vel! *(Dzięki, gościu! Bądź zdrów!)* | — |  |

### Poziom 3: Droga na Althing  (typed=0.5, hint=bank, cierpliwość 4)

Nowe słowa: skógi = lesie (celownik), hafi = morzu (celownik), fjalli = górze (celownik)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Jedziecie z Þorgeirem szlakiem. Na rozstajach spotykasz wędrowca, który zna drogę. Þorgeirr pojechał z przodu, a niebo nad górą jest ciemne.  
*Cel:* Zapytaj o drogę, uważaj na burzę i dojedź na Althing.  
*Zakończenia:* win: Wędrowiec macha ręką: „Far heill!” Za lasem widzisz równinę Althingu, a Þorgeirr wita cię przy bramie. · partial: Dotarłeś na Althing, ale wędrowiec kilka razy musiał powtarzać wskazówki. Þorgeirr czeka już przy namiocie. · fail: Wędrowiec nie mógł cię zrozumieć, a burza złapała cię w górach. Althing zaczyna się bez ciebie.

| 1 | Heill, gestr! Hvert fer þú? *(Witaj, gościu! Dokąd jedziesz?)* | **Heill! Ek fer á þing.** *(Przywitaj się i powiedz, że jedziesz na Althing.)* | „Dokąd” to hvert. |
| 2 | Hér er mjǫðr. Vilt þú drekka? *(Oto miód. Chcesz się napić?)* | **Já, þökk!** *(Zgódź się i podziękuj.)* | Já to „tak”; þökk to „dziękuję”. |
| 3 | Stormr er á fjalli. Far hjá skógi, ekki yfir fjall. *(Burza jest w górach. Jedź obok lasu, nie przez górę.)* | **Þökk! Ek fer hjá skógi.** (dobra); złe: Þökk! Ek fer yfir fjall.; Þökk! Ek fer hjá hafi. · ŚMIERTELNE | Hjá skógi to „obok lasu”: właściwa droga.; Yfir fjall to „przez górę”, a właśnie tam jest burza.; Hjá hafi to „obok morza”: to inna strona, tam nie ma drogi na Althing. |
| 4 | Þú ert vitr maðr! Hestr þinn er skjótr. *(Jesteś mądrym człowiekiem! Twój koń jest szybki.)* | **Þökk! Hvar er þing?** *(Podziękuj i zapytaj, gdzie jest Althing.)* | „Gdzie” to hvar. |
| 5 | Þing er nær. Far vestr, ok þú ert þar brátt. *(Althing jest blisko. Jedź na zachód, a wkrótce tam będziesz.)* | **Þökk! Far vel!** *(Podziękuj i pożegnaj się.)* | Far vel to „bądź zdrów”. |
| 6 | Far heill, gestr! *(Jedź w zdrowiu, gościu!)* | — |  |

## Babcia przed halą (amma)

**Scena:** Niedziela przed hallą. Na ławie siedzi starsza pani, która uwielbia rozmawiać i ma całe popołudnie.  
**Cel:** Posiedź z babcią Gerðr i porozmawiaj z nią. Nikt cię stąd nie wyrzuci.  
**Rozmówca:** Amma Gerðr  
**Zakończenia:** win: Amma Gerðr promienieje: „Hví góðr maðr!” Zaprasza cię na niedzielny miód i kawałek placka. · partial: Rozmowa się toczyła, choć kilka razy musiałeś prosić o powtórzenie. Amma Gerðr uśmiecha się cierpliwie i zaprasza cię znowu. · fail: Amma Gerðr się nie zniechęca, bo ma nieskończoną cierpliwość. Jeśli kiedyś zobaczysz ten komunikat, napisz do nas.  

### Poziom 1: Na ławie  (typed=0, hint=none, cierpliwość 3)

Nowe słowa: fǫgr = piękny, mælt = powiedziane (mæla), heitir = nazywa się (heita), heiti = nazywam się (heita), Gerðr = Gerðr (imię), Pétr = Pétr (imię), Býr = mieszka (búa), Póllandi = Polska (celownik)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Dwór, ławka, słońce. Starsza pani karmi okruchami kury i zaczyna rozmowę. Nie musisz się spieszyć: Amma Gerðr poczeka.  
*Cel:* Przywitaj się, powiedz, jak się nazywasz i skąd jesteś.  
*Zakończenia:* win: Amma Gerðr klepie ławę obok siebie: „Sit hjá mér, Pétr!” Zostajesz na dłużej. · partial: Rozmowa się udała, mimo kilku pomyłek. Amma Gerðr zachowuje cierpliwość i robi ci miejsce na ławie. · fail: Amma Gerðr nigdy się nie zniechęca.

| 1 | Heill, ungr maðr! Er eigi veðr gott í dag? *(Witaj, młody człowieku! Czyż pogoda nie jest dziś dobra?)* | **Já, veðr er gott.** *(Zgódź się, że pogoda jest dobra.)* · warianty: Já, sól er fǫgr. | „Pogoda” to veðr; „dobra” (nijaki) to gott. |
| 2 | Vel mælt! Hvé heitir þú? Ek heiti Gerðr. *(Dobrze powiedziane! Jak się nazywasz? Ja nazywam się Gerðr.)* | **Ek heiti Pétr.** *(Powiedz, jak się nazywasz.)* · warianty: Ek em Pétr. | „Nazywam się” to ek heiti. |
| 3 | Pétr! Þat er gott nafn. Býr þú hér? *(Piotr! To dobre imię. Mieszkasz tutaj?)* | **Nei, ek bý eigi hér. Ek em frá Póllandi.** *(Zaprzecz i powiedz, że jesteś z Polski.)* · warianty: Nei, ek bý ekki hér. Ek em frá Póllandi. | „Nie” przy czasowniku to eigi; „z” to frá + celownik. |
| 4 | Frá Póllandi! Þat er langt. Vilt þú sitja? *(Z Polski! To daleko. Chcesz usiąść?)* | **Já, gjarna. Þökk!** *(Zgódź się i podziękuj.)* | „Chętnie” to gjarna. |
| 5 | Heill ok sæll! Hér er rúm. *(Zdrów i szczęśliwy! Tu jest miejsce.)* | — |  |

### Poziom 2: Wnuk i kaczki  (typed=0.25, hint=bank, cierpliwość 3)

Nowe słowa: Ari = Ari (imię), vetra = zim, lat (dopełniacz mn.), gefr = daje (gefa), ǫndum = kaczkom (celownik mn.), bakaða = upieczoną (biernik), hana = ją, sjálf = sama, Kakan = placek (z rodzajnikiem), tigir = dziesiątki; „sjau tigir” = siedemdziesiąt

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Mały Ari biega po trawniku i karmi kaczki, a Amma Gerðr pokazuje ci swe bransolety. Z torby wyjmuje placek własnej roboty.  
*Cel:* Porozmawiaj o wnuku Arim, powiedz, czy masz dzieci, i spróbuj placka.  
*Zakończenia:* win: Amma Gerðr wręcza ci drugi kawałek: „Et, et, þú ert of mjór!” Ari macha do ciebie z daleka. · partial: Zjadłeś placek, choć kilka razy brakowało ci słów. Amma Gerðr dolewa miodu z dzbana. · fail: Amma Gerðr nie traci cierpliwości.

| 1 | Þat er sonarsonr minn, Ari. Hann er sex vetra gamall. *(To mój wnuk Ari. Ma sześć zim.)* | **Hann er mjǫk góðr sveinn.** *(Pochwal wnuka: powiedz, że to bardzo dobry chłopiec.)* · warianty: Ari er mjǫk góðr sveinn. | „Chłopiec” to sveinn; „on jest” to hann er. |
| 2 | Þökk! Ari gefr ǫndum brauð. Átt þú bǫrn? *(Dziękuję! Ari daje kaczkom chleb. Masz dzieci?)* | **Nei, ek á eigi bǫrn.** *(Powiedz, że nie masz dzieci.)* · warianty: Nei, ek á ekki bǫrn. | „Nie mam” to ek á eigi; bǫrn to „dzieci”. |
| 3 | Átt þú eigi bǫrn? Svá. Vilt þú kǫku? Ek bakaða hana sjálf. *(Nie masz dzieci? Tak. Chcesz placek? Sama go upiekłam.)* | **Já, gjarna. Kakan er mjǫk góð!** *(Przyjmij placek i pochwal go.)* · warianty: Já, þökk. Kakan er mjǫk góð! | Kaka jest rodzaju żeńskiego: kakan er góð. |
| 4 | Vel! Hvé gamall ert þú? *(Dobrze! Ile masz lat?)* | **Ek em þrír tigir vetra gamall.** *(Powiedz, że masz trzydzieści zim.)* | „Mam … zim” to ek em … vetra gamall. |
| 5 | Svá ungr! *(Taki młody!)* | — |  |

### Poziom 3: Zaproszenie  (typed=0.5, hint=bank, cierpliwość 3)

Nowe słowa: hvern = każdego, który (biernik r. m.), fagrt = piękne (r. nijaki), satt = prawdziwe, prawda (r. nijaki), sunnudag = niedzielę, Hvenær = kiedy, Hjálpar = pomaga (hjálpa), sekkinn = worek (z rodzajnikiem), sekk = worek, sunnudags = niedzieli (dopełniacz)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Słońce chyli się ku zachodowi. Amma Gerðr pakuje dzban i prosi cię o pomoc. Zanim wstaniecie z ławy, chce cię jeszcze zaprosić.  
*Cel:* Przyjmij zaproszenie na niedzielny miód i pomóż babci z workiem.  
*Zakończenia:* win: Amma Gerðr pokazuje ci drogę do swego domu: „Hafðu hungr með þér!” Idziesz do domu w świetnym nastroju. · partial: Wszystko się wyjaśniło, choć trzeba było kilka razy powtarzać. Amma Gerðr mówi: „Far vel til sunnudags, sveinn minn!” · fail: Amma Gerðr nie traci cierpliwości.

| 1 | Sér þú, ek em hér hvern dag. Hér er svá fagrt. *(Wiesz, jestem tu codziennie. Jest tu tak pięknie.)* | **Já, hér er mjǫk fagrt.** *(Zgódź się, że jest tu pięknie.)* · warianty: Já, hér er mjǫk gott. | „Pięknie” (nijaki) to fagrt. |
| 2 | Eigi satt? Á sunnudag brugga ek mjǫð. Vilt þú koma? *(Prawda? W niedzielę warzę miód. Chcesz przyjść?)* | **Já, gjarna. Hvenær?** *(Zgódź się i zapytaj, kiedy.)* | „Kiedy?” to hvenær. |
| 3 | Þegar sól er hátt. Sekkr minn er þungr. Hjálpar þú mér? *(Gdy słońce jest wysoko. Mój worek jest ciężki. Pomożesz mi?)* | **Já, víst. Ek ber sekkinn.** *(Zgódź się i zaproponuj, że poniesiesz worek.)* · warianty: Já, ek ber sekk þinn. | „Niosę” to ek ber, a „worek” to sekkr (z rodzajnikiem sekkinn). |
| 4 | Hvé góðr maðr! Þú ert góðr. *(Jaki dobry człowiek! Jesteś dobry.)* | **Þökk! Far vel til sunnudags!** *(Podziękuj i pożegnaj się do niedzieli.)* | „Do niedzieli” to til sunnudags. |
| 5 | Far vel til sunnudags! Heill! *(Do niedzieli! Bądź zdrów!)* | — |  |

## Szpieg (njosn)

**Scena:** Jesteś agentem pod przykrywką. W Heiðabýr masz odebrać tajny list z hali jarla i przekazać go dalej. Jedno złe słowo i jesteś zdemaskowany.  
**Cel:** Zachowaj przykrywkę kupca Brandra, zdobądź list i uciekaj z kufrem.  
**Rozmówca:** Sendimaðr  
**Zakończenia:** win: Kufer jest w twoich rękach, a statek odpływa z portu. Ktoś w centrali szepcze: „Vel gǫrt, Haukr.” Przykrywka nie pękła ani razu. · partial: Misja się udała, ale po drodze kilka razy omal się nie zdradziłeś. Centrala odnotowuje: „Hann hafði hamingju.” · fail: Zdradziłeś się jednym słowem. Przykrywka pękła, a ty znikasz w ciemności bez listu i bez kufra.  

### Poziom 1: Hasło w porcie  (typed=0, hint=none, cierpliwość 2)

Nowe słowa: Kalt = zimno, kalt = zimno, kemr = przychodzi (koma), Þegi = milcz (þegja), Brandr = Brandr (imię), Haukr = Haukr (imię), njósnarmaðr = szpieg, Fylgir = towarzyszy (fylgja), þér = tobie, fylgir = towarzyszy (fylgja), hefi = mam (hafa), erendi = sprawa, zadanie, þitt = twoje (r. nijaki), ferr = idzie, płynie (fara), jarls = jarla (dopełniacz), skil = rozumiem (skilja), veizlu = ucztę (biernik), Svanr = Svanr (imię), orðit = słowo (z rodzajnikiem), Orðit = słowo (z rodzajnikiem), Kennir = poznajesz (kenna), mik = mnie (biernik), kenni = poznaję (kenna)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Heiðabýr, wieczór, nabrzeże. Jesteś szpiegiem „Haukr”, ale dla wszystkich jesteś Brandrem, kupcem futer z Hǫfn. Na nabrzeżu czeka człowiek w kapturze. Hasło: „Vetr kemr snemma.” Odzew: „Ok sumar kemr síð.”  
*Cel:* Podaj hasło, nie zdradź swojej przykrywki i przyjmij zadanie. Jedna zła odpowiedź i jesteś zdemaskowany.  
*Zakończenia:* win: Człowiek w kapturze znika w tłumie, a ty zostajesz z wiadomością w kieszeni. Przykrywka nietknięta, a jutro czeka cię hala jarla. · partial: Dostałeś zadanie, ale kontakt zmarszczył brwi przy kilku twoich odpowiedziach. Lepiej uważaj jutro. · fail: Człowiek w kapturze spojrzał na ciebie zimno, odwrócił się i odszedł. Zadanie dostanie ktoś inny.

| 1 | Heill, gestr. Kalt er í dag, er eigi svá? *(Witaj, gościu. Zimno dziś, prawda?)* | **Já, kalt er. Vetr kemr snemma.** *(Zgódź się, że jest zimno, i powiedz hasło: zima przychodzi wcześnie.)* · warianty: Já, mjǫk kalt. Vetr kemr snemma. | Hasło brzmi: „Vetr kemr snemma.” |
| 2 | Ok sumar kemr síð. Þegi! Hér hlýða menn. Hvé heitir þú? *(A lato przychodzi późno. Cicho! Tu ludzie słuchają. Jak się nazywasz?)* | **Ek heiti Brandr. Ek em kaupmaðr.** (dobra); złe: Ek heiti Haukr. Ek em njósnarmaðr.; Ek heiti Brandr. Ek em njósnarmaðr. · ŚMIERTELNE | Haukr to twoje imię agenta, a ludzie słuchają.; Brandr się zgadza, ale „njósnarmaðr” zdradza przykrywkę. |
| 3 | Gott. Fylgir þér nǫkkurr? *(Dobrze. Czy ktoś cię śledzi?)* | **Nei, engi fylgir mér.** (dobra); złe: Já, nǫkkurr fylgir mér.; Nei, ek hefi eigi tíð. · ŚMIERTELNE | Mówisz, że nikt cię nie śledzi.; Kontakt pyta o śledzenie, nie o czas. |
| 4 | Vel. Hér er erendi þitt. Á morgin ferr þú í hǫll jarls. Þar er veizla. *(Dobrze. Oto twoje zadanie. Jutro idziesz do hali jarla. Jest tam uczta.)* | **Ek skil. Á morgin fer ek í hǫll jarls.** *(Powiedz, że zrozumiałeś: jutro idziesz do hali jarla.)* | „Rozumiem” to ek skil; „do hali” to í hǫll. |
| 5 | Gott. Orð til veizlu er Svanr. Hvat er orðit? *(Dobrze. Hasło na ucztę to „Łabędź”. Jakie jest hasło?)* | **Orðit er Svanr.** *(Powtórz hasło na ucztę.)* | Orð to „słowo, hasło”; Svanr to „łabędź”. |
| 6 | Vel. Þegi! Vǫrðr kemr. Kennir þú mik? *(Dobrze. Cicho! Idzie strażnik. Znasz mnie?)* | **Nei, ek kenni þik eigi.** *(Zaprzecz, że znasz tego człowieka.)* · warianty: Nei, ek kenni þik eigi! · ŚMIERTELNE | Nie możesz zdradzić, że znasz kontakt. |
| 7 | Góða nótt, Brandr. *(Dobranoc, Brandrze.)* | — |  |

### Poziom 2: Uczta w hali jarla  (typed=0.2, hint=bank, cierpliwość 2)

Nowe słowa: velkominn = witaj (r. m.), vápn = broń, bréf = list, vinnr = pracuje (vinna), vinn = pracuję (vinna), kaupmann = kupca (biernik), Hǫfn = Hǫfn (miasto-port), konung = króla (biernik), Bergþóru = Bergþóra (biernik), sel = daję (selja), feldi = płaszczu (celownik), þín = twój (r. żeński), Fróðligt = ciekawie, náðhús = wygódka, Herbergi = izba, lokat = zamknięte (r. nijaki), herbergi = izba, Skemmtu = baw się (skemmta)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Następny wieczór. W hali jarla trwa uczta, a przy wejściu stoi Bergþóra, zarządczyni. Ona i goście zadają pytania o twoją „firmę”. Twoja przykrywka: Brandr, futra, Hǫfn. Hasło wejściowe: Svanr. Komnata jarla jest po prawej, wychodek po lewej.  
*Cel:* Wejdź na ucztę, nie zdradź się pytaniom o firmę i znajdź pretekst, żeby dotrzeć do komnaty.  
*Zakończenia:* win: Bergþóra macha ci na pożegnanie, a w komnacie leży list, o który ci chodziło. Nikt niczego nie podejrzewa. · partial: Weszłeś i dotarłeś do komnaty, ale Bergþóra patrzyła na ciebie dłużej, niż trzeba. · fail: Bergþóra przestaje się uśmiechać i daje znak straży. Za chwilę wyprowadzą cię z hali.

| 1 | Heill ok velkominn í hǫll jarls! Hvat er orðit? *(Witaj w hali jarla! Jakie jest hasło?)* | **Orðit er Svanr.** *(Podaj hasło wejściowe.)* | Orð to hasło, a Svanr to „łabędź”. |
| 2 | Þökk. Ek verð at spyrja. Hefir þú vápn? *(Dziękuję. Muszę zapytać. Masz broń?)* | **Nei, ek hefi ekki vápn.** (dobra); złe: Já, ek hefi vápn.; Nei, ek hefi ekki bréf. · ŚMIERTELNE | Na ucztę nie wchodzi się z bronią.; Pytanie dotyczy broni (vápn), nie listu (bréf). |
| 3 | Gott. Fyrir hvern vinnr þú? *(Dobrze. Dla kogo pracujesz?)* | **Ek vinn fyrir kaupmann í Hǫfn.** (dobra); złe: Ek vinn fyrir konung.; Ek vinn fyrir Bergþóru. · ŚMIERTELNE | Konungr to twoja centrala, tajna.; Bergþóra to zarządczyni hali. |
| 4 | Hvat selr þú? *(Co sprzedajesz?)* | **Ek sel feldi.** *(Powiedz, co sprzedajesz (przykrywka).)* · warianty: Ek sel feldi! · ŚMIERTELNE | Twoja przykrywka to handel futrami. |
| 5 | Hvar er verzlan þín? *(Gdzie jest twój kramik?)* | **Verzlan mín er í Hǫfn.** (dobra); złe: Ek sel feldi.; Verzlan mín heitir Brandr. · ŚMIERTELNE | „Hvar” to „gdzie”, a nie „co sprzedaje”.; „Hvar” pyta o miejsce, nie o nazwę. |
| 6 | Fróðligt! Vilt þú eta? *(Ciekawe! Chcesz coś zjeść?)* | **Nei, þökk. Hvar er náðhús?** *(Odmów i zapytaj o wychodek (to pretekst).)* | Hvar = gdzie, więc „Hvar er náðhús?”. |
| 7 | Náðhús er til vinstri. Herbergi jarls til hægri er lokat. *(Wychodek jest po lewej. Komnata jarla po prawej jest zamknięta.)* | **Þökk, ek fer til vinstri.** (dobra); złe: Þökk, ek fer til hægri.; Þökk, herbergi jarls er fagrt. · ŚMIERTELNE | Komnata po prawej jest zamknięta, a ty idziesz do wychodka po lewej.; Nie wolno ci mówić, że chcesz iść do komnaty. |
| 8 | Skemmtu þér vel, Brandr! *(Baw się dobrze, Brandrze!)* | — |  |

### Poziom 3: Przesłuchanie  (typed=0.35, hint=bank, cierpliwość 1)

Nowe słowa: Stǫð = stój, gerir = robi (gera), náðhúss = wygódki (dopełniacz), Vart = stało się (verða), náðhúsi = wygódka (celownik), Hm = hm, kalla = wołam, nazywam, alla = wszystkich, gesti = gościa (biernik), Bergþóra = Bergþóra (imię), hǫllinni = hala (celownik, z rodzajnikiem), nǫkkurn = jakiegoś (biernik r. m.), engan = żadnego (biernik r. m.)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Masz list w sakwie, ale na dziedzińcu zatrzymuje cię podejrzliwy strażnik Kolr. Zaraz zapyta o wszystko. Pamiętaj: Brandr, kupiec, Hǫfn. Tutaj każda zła odpowiedź kończy misję.  
*Cel:* Przekonaj strażnika, że jesteś zwykłym gościem, i wyjdź z listem.  
*Zakończenia:* win: Kolr przepuszcza cię z kwaśną miną. Wychodzisz z hali, a list w sakwie jest ciężki jak ołów. · partial: Kolr w końcu cię puszcza, ale zapisuje twoje imię na kiju do liczenia. · fail: Kolr chwyta cię za ramię: „Kom með mér!” Misja skończona, zanim naprawdę się zaczęła.

| 1 | Stǫð! Hverr ert þú? Hvat gerir þú hér? *(Stój! Kim jesteś? Co tu robisz?)* | **Ek em gestr. Ek leita náðhúss.** *(Powiedz, że jesteś gościem i szukasz wychodka.)* · warianty: Ek em gestr hér. Ek leita náðhúss. | „Leita” znaczy „szukać”. |
| 2 | Náðhús er þar. Vart þú í herbergi jarls? *(Wychodek jest tam. Czy byłeś w komnacie jarla?)* | **Nei, ek var eigi í herbergi jarls.** (dobra); złe: Já, ek var þar.; Nei, ek var eigi í náðhúsi. · ŚMIERTELNE | Przyznanie się to koniec przykrywki.; Pytanie dotyczy komnaty jarla, nie wychodka. |
| 3 | Hm, gott. Hvat hefir þú í sekk? *(Hm, dobrze. Co masz w worku?)* | **Í sekk hefi ek silfr ok brauð.** (dobra); złe: Í sekk hefi ek bréf.; Ek hefi sekk. · ŚMIERTELNE | List w worku zdradziłby cię od razu.; Strażnik pyta, co jest w worku, a nie czy masz worek. |
| 4 | Silfr ok brauð. Hvé heitir þú, ok hvar býr þú? *(Srebro i chleb. Jak się nazywasz i gdzie mieszkasz?)* | **Ek heiti Brandr ok bý í Hǫfn.** *(Podaj imię z przykrywki i miasto, w którym mieszkasz (Hǫfn).)* · warianty: Ek heiti Brandr ok bý í Hǫfn! · ŚMIERTELNE | Brandr i Hǫfn to twoja przykrywka. |
| 5 | Brandr, Hǫfn. Þú ert njósnarmaðr, er eigi svá? *(Brandr, Hǫfn. Jesteś szpiegiem, prawda?)* | **Nei, ek em eigi njósnarmaðr. Ek em kaupmaðr.** (dobra); złe: Já, en þat er leyndarmál.; Já, ek vinn fyrir konung. · ŚMIERTELNE | Nawet żartem nie przyznawaj się do tajemnicy.; Przyznanie się do centrali to koniec. |
| 6 | Ek kalla á Bergþóru. Hon kennir alla gesti. Kennir hon þik? *(Zawołam Bergþórę. Zna wszystkich gości. Czy zna ciebie?)* | **Já, Bergþóra kennir mik. Ek em gestr.** *(Powiedz, że Bergþóra cię zna.)* · warianty: Já, Bergþóra kennir mik. | „Kennir mik” znaczy „zna mnie”. |
| 7 | Gott. Njósnarmaðr er í hǫllinni. Sá þú nǫkkurn? *(Dobrze. W hali jest szpieg. Widziałeś kogoś?)* | **Nei, ek sá engan.** *(Zaprzecz, że kogokolwiek widziałeś.)* · warianty: Nei, ek sá engan! · ŚMIERTELNE | Engan = nikogo. Ty sam jesteś tym szpiegiem. |
| 8 | Vel. Far heim, Brandr. *(Dobrze. Idź do domu, Brandrze.)* | — |  |

### Poziom 4: Kufer i ucieczka  (typed=0.5, hint=letters, cierpliwość 1)

Nowe słowa: Hrafn = Hrafn (imię), bréfit = list (z rodzajnikiem), Bréfit = list (z rodzajnikiem), mínum = mojemu (celownik), Tak = weź (taka), tek = biorę (taka), kistuna = kufer (biernik, z rodzajnikiem), Gát = uwaga, eltir = goni (elta), oss = nas, gerum = robimy (gera), vér = my, hlaupum = biegniemy (hlaupa), brott = precz, bíðum = czekamy (bíða), drekkum = pijemy (drekka), mælum = mówimy (mæla), við = przy, z; my dwaj, manninn = człowieka (biernik, z rodzajnikiem), af = z, od, Fǫrum = idźmy, płyńmy (fara), bæjar = miasta (dopełniacz), hafnar = portu (dopełniacz), fǫrum = idziemy, płyniemy (fara), siglir = żegluje (sigla), gǫrt = zrobione (r. nijaki), lokit = zamknięte, koniec

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Następny ranek, port. Ulfr z centrali czeka z kufrem pełnym srebra. Wymienisz go na list. Nowe hasło: „Hrafn”. Ale ktoś cię śledzi: w tłumie jest zdrajca (svikari), który chce dostać list dla siebie.  
*Cel:* Wymień list na kufer, nie daj się zdemaskować zdrajcy i wsiądź na statek.  
*Zakończenia:* win: Statek odpływa, a ty stoisz na pokładzie z kufrem. Ulfr macha z nabrzeża: „Góða ferð, Haukr!” · partial: Udało się uciec, ale zdrajca zdążył zobaczyć twoją twarz. Misja zaliczona, lecz twoja przykrywka jest spalona. · fail: Zdrajca był szybszy. Kufer i list zniknęły, a ty zostajesz na nabrzeżu z pustymi rękami.

| 1 | Góðan dag. Hvat er orðit? *(Dzień dobry. Jakie jest hasło?)* | **Orðit er Hrafn.** *(Podaj hasło z dzisiejszej misji.)* · warianty: Orðit er Hrafn! · ŚMIERTELNE | Orð to hasło, a dziś brzmi „Hrafn”. |
| 2 | Gott. Hvar er bréfit? *(Dobrze. Gdzie jest list?)* | **Bréfit er í sekk mínum.** (dobra); złe: Bréfit er hjá Bergþóru.; Bréfit er leyndarmál. · ŚMIERTELNE | List masz przy sobie, w worku.; Kontakt pyta, gdzie jest list, nie o tajemnicę. |
| 3 | Gott. Hér er kista. Silfr er í. Tak hana. *(Dobrze. Oto kufer. Srebro jest w środku. Weź go.)* | **Þökk. Ek tek kistuna.** *(Podziękuj i weź kufer.)* · warianty: Þökk. Ek tek kistuna. | Kista jest żeńska; w bierniku kistuna. |
| 4 | Gát! Maðr þar er svikari. Hann eltir oss. Hvat gerum vér? *(Uwaga! Ten człowiek tam jest zdrajcą. Idzie za nami. Co robimy?)* | **Vér hlaupum skjótt á brott.** (dobra); złe: Vér bíðum hér ok drekkum mjǫð.; Vér mælum við manninn. · ŚMIERTELNE | Zdrajca idzie za wami, trzeba uciekać.; Nie rozmawia się ze zdrajcą. |
| 5 | Já, skjótt! Svikari kemr af vinstri. Fǫrum vér vinstri til bæjar eða hægri til hafnar? *(Tak, szybko! Zdrajca idzie z lewej. Idziemy w lewo do wsi czy w prawo do portu?)* | **Vér fǫrum hægri til hafnar.** (dobra); złe: Vér fǫrum vinstri til bæjar.; Vér fǫrum heim. · ŚMIERTELNE | Zdrajca nadchodzi z lewej, więc idziecie w prawo, do portu.; Pytanie jest o port albo wieś, a nie o dom. |
| 6 | Stǫð! Gef mér kistuna! Ek hefi sverð! *(Stój! Daj mi kufer! Mam miecz!)* | **Nei, ek gef þér eigi kistuna.** *(Odmów oddania kufra.)* · warianty: Nei, ek gef þér eigi kistuna! · ŚMIERTELNE | „Dawać” to gefa, a eigi stoi po czasowniku. |
| 7 | Skjótt! Skip siglir brátt. Hefir þú enn kistuna? *(Szybko! Statek zaraz odpływa. Czy masz jeszcze kufer?)* | **Já, ek hefi enn kistuna.** *(Potwierdź, że masz jeszcze kufer.)* · warianty: Já, ek hefi hana enn. | Enn znaczy „jeszcze”. |
| 8 | Vel gǫrt, Haukr! Erendi er lokit. Far vel! *(Dobra robota, Haukr! Misja zakończona. Bądź zdrów!)* | — |  |

## Podróż w czasie (tima)

**Scena:** Obudziłeś się w czasach wikingów pod wałem miasta Heiðabýr. Nikt nie może się dowiedzieć, że jesteś z przyszłości, bo za dziwne rzeczy i dziwne słowa grozi ci wygnanie albo gorzej.  
**Cel:** Nie daj się wykryć jako przybysz z przyszłości: unikaj wszystkiego, co nie pasuje do epoki wikingów, i dotrwaj do końca dnia.  
**Rozmówca:** Vǫrðr  
**Zakończenia:** win: Jarl kiwa głową: „Sannr ferðamaðr!” Nikt nie podejrzewa, skąd naprawdę jesteś. Wieczorem znajdujesz drogę powrotną, a w kieszeni zostaje ci tylko srebrna moneta na pamiątkę. · partial: Udało ci się przetrwać dzień, ale kilka razy ludzie patrzyli na ciebie podejrzliwie. Jarl każe cię obserwować, więc wymykasz się z miasta o świcie. · fail: Ktoś zauważył, że nie jesteś stąd. Straż woła: „Galdramaðr! Seiðmaðr!” i musisz uciekać. Podróż w czasie skończyła się wcześniej, niż chciałeś.  

### Poziom 1: Brama miasta  (typed=0, hint=none, cierpliwość 5)

Nowe słowa: Þetta = to (r. nijaki), Heiðabýjar = Heiðabýr (dopełniacz), ferðamaðr = podróżnik, Ǫrn = Ǫrn (imię; orzeł), Kevin = Kevin (imię współczesne), Chantal = Chantal (imię współczesne), framtíð = przyszłość, Ameríku = Ameryka (celownik), Fótgangandi = pieszo, hesti = koniu (celownik), ríð = jadę konno (ríða), bíl = samochód, flugvél = samolot, Sýn = pokaż (sýna), síma = telefon (biernik), kreditkort = karta kredytowa, mátt = możesz (mega), inn = do środka, húsbónda = gospodarza (dopełniacz), Rétt = zaraz, prosto; słusznie, hǫllin = hala (z rodzajnikiem), kominn = przybyły

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Czasy wikingów. Stoisz przed wielką drewnianą bramą miasta Heiðabýr. Strażnik Ǫrn zatrzymuje każdego podróżnego i zadaje pytania. Masz na sobie zwykłe ubranie, ale w kieszeniach zostały ci rzeczy z przyszłości.  
*Cel:* Odpowiedz na pytania strażnika tak, żeby nie wzbudzić podejrzeń: przedstaw się, powiedz skąd jesteś i jak podróżujesz. Zwróć uwagę na rzeczy, których w czasach wikingów jeszcze nie było.  
*Zakończenia:* win: Ǫrn otwiera bramę: „Velkominn til Heiðabýjar!” Nic nie wzbudziło jego podejrzeń, a ty wchodzisz do miasta. · partial: Ǫrn w końcu cię wpuszcza, ale przygląda ci się dłużej, niż byś chciał. Wchodzisz do miasta z uczuciem, że ktoś cię obserwuje. · fail: Ǫrn podnosi włócznię: „Þú ert eigi ferðamaðr!” Brama zamyka się z trzaskiem, a ty uciekasz w las.

| 1 | Stǫð! Þetta er hlið Heiðabýjar. Hverr ert þú? *(Stój! To brama Heiðabýr. Kim jesteś?)* | **Ek em ferðamaðr.** *(Powiedz, że jesteś podróżnikiem.)* | „Jestem podróżnikiem”: ek em ferðamaðr. |
| 2 | Hvé heitir þú? *(Jak się nazywasz?)* | **Ek heiti Ǫrn.** (dobra); złe: Ek heiti Kevin.; Ek heiti Chantal. · ŚMIERTELNE | w czasach wikingów nikt tak nie nazywał dzieci.;Chantal to nowoczesne, francuskie imię. W tamtych czasach były Ǫrn, Ulfr czy Hrafn. |
| 3 | Hvaðan kemr þú? *(Skąd przychodzisz?)* | **Ek kem frá Póllandi.** (dobra); złe: Ek kem ór framtíð.; Ek kem frá Ameríku. · ŚMIERTELNE | Ameryki jeszcze nikt tak nie nazywa;Vínland to co innego. |
| 4 | Hvé ferr þú? Fótgangandi eða á hesti? *(Jak podróżujesz? Pieszo czy konno?)* | **Ek ríð á hesti.** (dobra); złe: Ek fer í bíl.; Ek fer í flugvél. · ŚMIERTELNE | Samolotów też jeszcze nie ma;ludzie nie latają. |
| 5 | Sýn mér sekk þinn. Hvat hefir þú þar? *(Pokaż mi swój worek. Co tam masz?)* | **Ek hefi einungis brauð ok ǫl.** (dobra); złe: Ek hefi síma.; Ek hefi kreditkort. · ŚMIERTELNE | Telefon w czasach wikingów? Strażnik wziąłby go za magiczne urządzenie.; Karta kredytowa z plastiku wyglądałaby jak magia. Pieniądze to wtedy srebro. |
| 6 | Gott, þú mátt koma inn. Ert þú svangr? *(Dobrze, możesz wejść. Jesteś głodny?)* | **Já, ek em svangr. Hvar er hǫll húsbónda?** *(Powiedz, że jesteś głodny, i zapytaj, gdzie jest hala gospodarza.)* | „Gdzie” to hvar, a „gospodarz” to húsbóndi. |
| 7 | Rétt til vinstri er hǫllin. Vel kominn til Heiðabýjar! *(Zaraz po lewej jest hala. Witaj w Heiðabýr!)* | — |  |

### Poziom 2: Hala gospodarza  (typed=0.15, hint=bank, cierpliwość 5)

Nowe słowa: kaffi = kawa, kóla = cola, farit = przebył (fara), daga = dni (dopełniacz mn.), markað = targ (biernik), tǫkum = bierzemy (taka), vagni = wóz (celownik), reiðhjóli = rower (celownik), kerti = świeca, internet = internet, rafmagn = prąd elektryczny, dǫgum = dniach (celownik mn.), Haralds = Haralda (dopełniacz), konungs = króla (dopełniacz)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Wchodzisz do hali. Gospodarz Konráðr jest ciekawski i pyta o wszystko: co chcesz zjeść, jak podróżujesz i czego potrzebujesz na noc. W hali nie ma elektryczności ani nowoczesnych napojów.  
*Cel:* Zamów jedzenie i picie, które mogli podać w czasach wikingów, ustal nocleg i nie wspomnij o niczym z przyszłości.  
*Zakończenia:* win: Konráðr klepie cię po plecach: „Þú ert góðr gestr!” Dostajesz miejsce przy ogniu i pełną misę. Nikt nie podejrzewa, że jesteś z przyszłości. · partial: Konráðr przygląda ci się podejrzliwie, ale podaje jedzenie. Śpisz źle, bo wciąż myślisz o tym, co powiedziałeś. · fail: Konráðr woła głośno: „Hvat er internet?!” Goście odwracają się w twoją stronę, a ty ledwo uciekasz tylnym wyjściem.

| 1 | Velkominn í hǫll mína! Hvat vilt þú eta? Hér eru brauð ok seyði. *(Witaj w mojej hali! Co chcesz zjeść? Mamy chleb i zupę.)* | **Ek vil brauð ok seyði.** *(Zamów chleb i zupę.)* | „Chleb i zupa”: brauð ok seyði, bez rodzajnika. |
| 2 | Ok hvat vilt þú drekka? Hér eru mjǫðr, ǫl ok vatn. *(A co chcesz pić? Mamy miód pitny, piwo i wodę.)* | **Ek vil mjǫð.** (dobra); złe: Ek vil kaffi.; Ek vil kóla. · ŚMIERTELNE | Kawa dotarła na Północ dopiero wieki później.; Coca-Cola powstała w XIX wieku. |
| 3 | Mjǫð, gott. Þú hefir farit langt. Hvé lengi ert þú á leið? *(Miód, dobrze. Daleko przebyłeś. Jak długo jesteś w drodze?)* | **Ek em á leið tíu daga.** *(Powiedz, że jesteś w drodze dziesięć dni.)* | „Dziesięć dni”: tíu daga. |
| 4 | Tíu daga! Á morgin fer ek á markað. Fer þú með? Vér tǫkum vagn. *(Dziesięć dni! Jutro jadę na targ. Pojedziesz ze mną? Weźmiemy wóz.)* | **Já, gjarna. Vér fǫrum með vagni.** (dobra); złe: Já, vér tǫkum bíl.; Nei, ek fer á reiðhjóli. · ŚMIERTELNE | Samochodu nie ma. Konráðr nie zna takiego słowa.; Rower wynaleziono dopiero w XIX wieku. |
| 5 | Gott. Herbergi hefir rúm. Vilt þú nǫkkut ok? *(Dobrze. W izbie jest łóżko. Chcesz jeszcze coś?)* | **Já, ek vil kerti.** (dobra); złe: Hefir þú internet?; Ek vil rafmagn. · ŚMIERTELNE | Internetu nie ma. Konráðr nie wie, co to jest.; Prądu elektrycznego wynaleziono setki lat później. |
| 6 | Kerti, gott. Hér er mjǫðr annarr: góðr mjǫðr á dǫgum Haralds konungs! Skál! *(Świeca, proszę. A tu jeszcze miód: dobry miód za dni króla Haralda! Na zdrowie!)* | **Skál!** *(Wznieś toast.)* | „Na zdrowie” to skál. |
| 7 | Góða nótt! Á morgin fǫrum vér á markað. *(Dobranoc! Jutro jedziemy na targ.)* | — |  |

### Poziom 3: Targ  (typed=0.3, hint=bank, cierpliwość 4)

Nowe słowa: kostar = kosztuje (kosta), þrjú = trzy (r. nijaki), silfri = srebrem (celownik), evrum = euro (celownik mn.), korti = karta (celownik), undarligt = dziwne (r. nijaki), austri = wschód (celownik), stuttermabolr = t-shirt, gallabuxur = dżinsy, strigaskór = adidasy, buty sportowe, vill = chce (vilja)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Następnego ranka na targu jest tłoczno. Kupcowa Bera sprzedaje chleb i ser. Przy płaceniu liczy się tylko srebro, a ludzie przyglądają się twoim ubraniom.  
*Cel:* Kup chleb i ser, zapłać tak, jak płaci się w czasach wikingów, i wyjaśnij, skąd masz dziwne ubranie.  
*Zakończenia:* win: Bera wsuwa ci do koszyka jabłko: „Fyrir góðan ferðamann!” Targ nic nie podejrzewa, a w oddali widać już halę jarla. · partial: Bera w końcu sprzedała ci chleb i ser, ale kilka osób szepcze za twoimi plecami. Zbliża się hala jarla. · fail: Bera krzyczy: „Hvat er þetta klæði? Hvat er evra?” Tłum się zbiega, a ty uciekasz między straganami.

| 1 | Heill! Hvat vilt þú kaupa? Brauð, ost eða epli? *(Witaj! Co chcesz kupić? Chleb, ser czy jabłka?)* | **Ek vil kaupa brauð ok ost.** *(Poproś o chleb i ser.)* | Ostr jest męski, więc w bierniku ost. |
| 2 | Brauð kostar tvau silfr ok ostr kostar þrjú silfr. *(Chleb kosztuje dwa srebrne, a ser trzy srebrne.)* | **Hvat kostar þat saman?** *(Zapytaj, ile to kosztuje razem.)* | „Razem” to saman. |
| 3 | Þat er fimm silfr. Hvé vilt þú gjalda? *(To pięć srebrnych. Jak chcesz zapłacić?)* | **Ek gjalda með silfri.** (dobra); złe: Ek gjalda með evrum.; Ek gjalda með korti. · ŚMIERTELNE | Euro wprowadzono dopiero w 2002 roku.; Karty płatnicze to wynalazek XX wieku. W czasach wikingów płaci się srebrem. |
| 4 | Gott, silfr. Klæði þitt er undarligt. Hvat er þat? *(Dobrze, srebro. Twoje ubranie jest dziwne. Co to?)* | **Þat er siðr frá austri.** (dobra); złe: Þat er stuttermabolr.; Þat eru gallabuxur ok strigaskór. · ŚMIERTELNE | T-shirty pojawiły się w XX wieku.; Dżinsy i adidasy to rzeczy z dwudziestego wieku. Bera zawołałaby straż. |
| 5 | Frá austri, svá. Jarl vill sjá þik. Fer þú með mér? *(Ze Wschodu, tak. Jarl chce cię zobaczyć. Pójdziesz ze mną?)* | **Já, ek fer með þér.** *(Zgódź się i idź z nią.)* | „Idę z tobą” to ek fer með þér. |
| 6 | Kom þá! Hǫllin er þar. *(No to chodź! Hala jest tam.)* | — |  |

### Poziom 4: Jarl  (typed=0.5, hint=letters, cierpliwość 4)

Nowe słowa: hendi = ręka (celownik), þinni = twojej (celownik r. ż.), armbandsúr = zegarek na rękę, rafhlǫðu = bateria (celownik), stafrænt = cyfrowy (r. nijaki), úr = zegarek, klukkan = zegar, godzina, sýnir = pokazuje (sýna), miðjan = środkowy (biernik r. m.), Klukkan = zegar, godzina, hálf = pół, lít = patrzę (líta), símann = telefon (z rodzajnikiem), ræðr = rządzi (ráða), landi = kraj (celownik), Haraldr = Haraldr (imię), Forseti = prezydent, veit = wiem (vita), hafir = miał (hafa, tryb łączący), galdrakistu = magiczna skrzynia (biernik), enga = żadną (biernik r. ż.), sími = telefon, sein = późno, hliðs = bramy (dopełniacz), tímavélar = wehikuł czasu (dopełniacz), bílsins = samochód (dopełniacz, z rodzajnikiem)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* W hali czeka jarl Sigurðr. Słyszał dziwne plotki o obcym przybyszu. Zauważył coś błyszczącego na twoim nadgarstku i zadaje pytania, a tobie została tylko jedna droga: wrócić do bramy, gdzie wszystko się zaczęło.  
*Cel:* Odpowiedz na pytania jarla tak, żeby nie zdradzić zegarka, telefonu ani przyszłości, i wróć bezpiecznie do bramy.  
*Zakończenia:* win: Jarl macha ręką: „Gott, far þá!” Wracasz do bramy, w powietrzu coś migocze i budzisz się we własnym czasie. Na dłoni masz srebrne monety. · partial: Jarl pozwala ci odejść, ale pod nosem mruczy o czarownikach. Dopiero za bramą migotanie powietrza zabiera cię do domu. · fail: Jarl woła strażników: „Galdrakista! Hann kemr ór framtíð!” Nie zdążysz dojść do bramy.

| 1 | Heill! Ek em jarl hér. Hverr ert þú? *(Witaj! Jestem tu jarlem. Kim jesteś?)* | **Ek em Ǫrn, ferðamaðr frá Póllandi.** *(Przedstaw się: Ǫrn, podróżnik z Polski.)* | „Z Polski” to frá Póllandi. |
| 2 | Hvat er þat á hendi þinni? *(Co to jest na twojej ręce?)* | **Þat er einungis hringr.** (dobra); złe: Þat er armbandsúr með rafhlǫðu.; Þat er stafrænt úr. · ŚMIERTELNE | Zegarek z baterią to wynalazek nowoczesny.; Cyfrowy zegarek wyglądałby jak czary. |
| 3 | Einungis hringr? Hvat er klukkan? Þú hefir víst úr. *(Tylko pierścień? Która godzina? Masz przecież zegarek.)* | **Ek hefi ekki úr. Sól sýnir miðjan dag.** (dobra); złe: Klukkan er hálf þrjú.; Ek lít á símann minn. · ŚMIERTELNE | Taka dokładna godzina to nowoczesny sposób liczenia czasu.; Telefon to rzecz z przyszłości. |
| 4 | Miðjan dag, gott. Hverr ræðr landi nú? *(Południe, dobrze. Kto teraz rządzi krajem?)* | **Haraldr konungr ræðr landi.** (dobra); złe: Forseti ræðr landi.; Ek veit þat eigi. · ŚMIERTELNE | Prezydent to nowoczesny urząd.; Nie wiedzieć, kto rządzi? Jarl uznałby, że ukrywasz coś. |
| 5 | Gott. Menn segja at þú hafir galdrakistu. Er þat satt? *(Dobrze. Mówią, że masz magiczną skrzynię. Czy to prawda?)* | **Nei, ek hefi enga galdrakistu.** (dobra); złe: Já, þat er sími.; Já, ek kem ór framtíð. · ŚMIERTELNE | Przyznanie się do telefonu zakończy rozmowę.; Przyznanie się do podróży w czasie to najgorsza odpowiedź. |
| 6 | Gott. Nú er sein. Hvert ferr þú nú? *(Dobrze. Jest już późno. Dokąd teraz idziesz?)* | **Ek fer aptr til hliðs.** (dobra); złe: Ek fer til tímavélar.; Ek fer til bílsins. · ŚMIERTELNE | Wehikuł czasu to najgorsza odpowiedź.; Samochodu w czasach wikingów nie ma. |
| 7 | Gott, far þá. Góða ferð! *(Dobrze, to idź. Szczęśliwej podróży!)* | — |  |

## Polityk (stjornmal)

**Scena:** Jesteś skorumpowanym politykiem. Dawno temu kupiec Úlfr dał ci mieszek srebra, a „sprawa Gauksmál” (sprawa Kukułki) wraca na każdym szczeblu twojej kariery. Wyborcy ci wierzą… i przestają… i zapominają.  
**Cel:** Przekonaj wyborców, że nadajesz się na stanowisko. Nigdy się nie przyznaj i nie sprzeczaj sam sobie.  
**Rozmówca:** Kjósandi  
**Zakończenia:** win: Wygrywasz wybór na króla! Nikt już nie pamięta mieszka od Úlfra. Przed halą tłum woła twoje imię, a ty obiecujesz „uczciwe rządy”. Úlfr macha z ostatniego rzędu. · partial: Wygrywasz o włos. Skaldowie wciąż układają wersy o sprawie, ale ty już składasz pierwsze przysięgi. Kłamstwo trzyma się na słowo honoru. · fail: Wiarygodność spadła do zera. Wyborcy wyciągają starą sprawę, a z tłumu ktoś woła: „Pungrinn!” Twoja kariera kończy się w pieśni skalda.  

### Poziom 1: Hreppstjóri  (typed=0, hint=none, cierpliwość 4)

Nowe słowa: verða = zostać, stać się, hreppstjóri = wójt, heiðarligr = uczciwy, Vegrinn = droga (z rodzajnikiem), brotinn = zepsuty, geri = robię (gera); „gera við” = naprawić, Úlfr = Úlfr (imię; wilk), gaf = dał (gefa), pung = mieszek (biernik), sét = widziany, widział (sjá), Úlf = Úlfr (biernik), varla = ledwo, síðan = temu, odtąd, hǫfum = mamy (hafa), gleymt = zapomniane (gleyma), þessu = temu (celownik), Þakka = dziękuję (þakka), þakklátr = wdzięczny, margar = wiele (r. ż.), skuldir = długi, sveitinni = gmina, okolica (celownik, z rodzajnikiem), meira = więcej, Munt = czy będziesz (munu), yðr = wam, was, kjósum = wybieramy (kjósa)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Zebranie wsi w wielkiej izbie w Smáá. Chcesz zostać wójtem (hreppstjóri). Þórdís zadaje pytania, a cała wieś słucha. Wszyscy pamiętają, że kupiec Úlfr naprawił drogę, i że ktoś widział mieszek…  
*Cel:* Przekonaj wieś, że jesteś uczciwy, i zaprzecz plotkom o mieszku.  
*Zakończenia:* win: Wieś klaszcze. Zostajesz wójtem Smáá. Úlfr, w pierwszym rzędzie, puszcza do ciebie oko. · partial: Wygrywasz jednym głosem. Þórdís patrzy na ciebie podejrzliwie, ale podnosi rękę. · fail: Wieś ma dość. Þórdís mówi: „Vér kjósum annan.” Kończysz karierę, zanim się zaczęła.

| 1 | Góðan dag! Vilt þú verða hreppstjóri? *(Dzień dobry! Chce Pan zostać wójtem?)* | **Já, ek vil verða hreppstjóri.** *(Powiedz, że chcesz zostać wójtem.)* | „Zostać” to verða, a po „vil” stoi bez „at”: ek vil verða. |
| 2 | Ert þú heiðarligr? *(Czy jest Pan uczciwy?)* | **Já, ek em ávallt heiðarligr.** *(Zapewnij, że jesteś zawsze uczciwy.)* | „Zawsze” to ávallt; po „em” przymiotnik zgadza się z podmiotem. |
| 3 | Vegrinn er brotinn. Hvat gerir þú? *(Droga jest zepsuta. Co Pan zrobi?)* | **Ek geri við veginn.** *(Obiecaj, że naprawisz drogę.)* | „Naprawić” to gera við, a „drogę” w bierniku to veginn. |
| 4 | Úlfr kaupmaðr gaf þér pung! Þat hefir einn sét! *(Kupiec Úlfr dał Panu mieszek! Ktoś to widział!)* | **Þat er lygi! Ek kenni Úlf varla.** *(Zaprzecz: to kłamstwo, ledwo znasz Úlfra.)* · warianty: Þat er lygi! Ek kenni Úlf varla. | „Znam” to ek kenni, a „ledwo” to varla. |
| 5 | Þat er langt síðan. Vér hǫfum gleymt þessu. *(To było dawno. Zapomnieliśmy o tym.)* | **Þakka þér, ek em þér þakklátr.** *(Podziękuj wyborcom za wyrozumiałość.)* | „Wdzięczny” to þakklátr; þér to „wam”, celownik. |
| 6 | Vér hǫfum margar skuldir í sveitinni. Hvat gerir þú? *(Mamy w gminie wiele długów. Co Pan zrobi?)* | **Ek spara silfr ok em heiðarligr.** (dobra); złe: Ek tek meira silfr.; Ek veit eigi. | Polityk, który mówi „zabiorę więcej srebra”, nie brzmi wiarygodnie.;„Nie wiem” nie przekona wyborców. |
| 7 | Munt þú vera heiðarligr við oss? *(Czy będzie Pan wobec nas uczciwy?)* | **Já, ek em ávallt heiðarligr við yðr.** *(Obiecaj uczciwość wobec wyborców.)* | „Wobec was” to við yðr. |
| 8 | Þá kjósum vér þik! Velkominn, hreppstjóri! *(Wybieramy więc Pana! Witamy, wójcie!)* | — |  |

### Poziom 2: Goði á þingi  (typed=0.2, hint=bank, cierpliwość 4)

Nowe słowa: skáldkona = skaldka, kunningi = znajomy, nýtt = nowy (r. nijaki), silfrit = srebro (z rodzajnikiem), keypta = kupiłem (kaupa), heiðarliga = uczciwie, skipit = okręt (z rodzajnikiem), tekit = wziął (taka), mútu = łapówka (biernik), Ragnhildr = Ragnhildr (imię), rúnakefli = kij z runami, pungr = mieszek, þessa = tych (biernik r. m.), Keflit = kij (z rodzajnikiem), gamalt = stary (r. nijaki), Kjósendr = wyborcy, mikilvægt = ważny (r. nijaki), segir = mówi (segja), tókt = wziąłeś (taka), Vitnit = świadek (z rodzajnikiem), lýgr = kłamie (ljúga), vitnit = świadek (z rodzajnikiem), saklauss = niewinny, yrki = układam wiersz (yrkja), sem = co, który, sagðir = powiedziałeś (segja)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Zgromadzenie w Þingvǫllr. Kandydujesz na goda (goði). Skaldka Ragnhildr pyta o kupców i o to, skąd masz nowy okręt.  
*Cel:* Zaprzecz, że brałeś srebro, i nie daj się złapać na kłamstwie.  
*Zakończenia:* win: Ragnhildr zamyka tabliczkę: „Gott, ek hefi engar spurningar.” Zostajesz godem. Úlfr gratuluje przez posłańca. · partial: Zostajesz godem, ale Ragnhildr mówi: „Ek fylgi þessu.” Będzie dalej drążyć. · fail: Wywiad trafia do pieśni pod tytułem „Goðinn ok pungrinn”. Nikt na ciebie nie głosuje.

| 1 | Góðan dag, ek em skáldkona. Vilt þú verða goði? *(Dzień dobry, jestem skaldką. Chce Pan zostać godem?)* | **Já, ek vil verða goði.** *(Potwierdź, że chcesz zostać godem.)* | „Goði” to gode; po „verða” bez rodzajnika. |
| 2 | Þú kennir Úlf kaupmann. Er hann vinr þinn? *(Zna Pan kupca Úlfra. Czy to pański przyjaciel?)* | **Nei, hann er einungis kunningi.** *(Zaprzecz: to tylko znajomy.)* | „Tylko” to einungis; „kunningi” to znajomy. |
| 3 | Þú hefir nýtt skip. Hvaðan hefir þú silfrit? *(Ma Pan nowy okręt. Skąd ma Pan srebro?)* | **Ek keypta þat heiðarliga.** *(Powiedz, że kupiłeś go uczciwie.)* · warianty: Ek keypta skipit heiðarliga. | „Kupiłem” to ek keypta; „uczciwie” to heiðarliga. |
| 4 | Hefir þú tekit við mútu? *(Czy brał Pan łapówki?)* | **Nei, ek hefi aldri tekit við mútu.** *(Zaprzecz, że kiedykolwiek brałeś łapówki.)* · warianty: Ek hefi aldri tekit við mútu. | „Wziąć łapówkę” to taka við mútu: hefi tekit; „nigdy” to aldri. |
| 5 | Ragnhildr sýnir rúnakefli. Þar eru þú, Úlfr ok pungr. *(Ragnhildr pokazuje rune-kij. Są na nim Pan, Úlfr i mieszek.)* | **Ek kenni eigi þessa menn.** *(Powiedz, że nie znasz tych ludzi.)* | „Ci ludzie” to þessir menn; w bierniku þessa menn. |
| 6 | Keflit er gamalt. Kjósendr gleyma því brátt. *(Kij jest stary. Wyborcy szybko o tym zapomną.)* | **Keflit er eigi mikilvægt.** *(Zlekceważ kij: nie jest ważny.)* | „Ważny” to mikilvægr; „nie” to eigi. |
| 7 | Vitni segir, at þú tókt silfr. *(Świadek mówi, że wziął Pan srebro.)* | **Þat er eigi satt. Vitnit lýgr.** (dobra); złe: Já, vitnit hefir rétt.; Ek em vitni. | Przyznajesz się, więc przegrywasz.;Vitni to świadek, a ty nim nie jesteś. |
| 8 | Þakka þér fyrir. Hefir þú nǫkkut ok at segja? *(Dziękuję. Czy chce Pan coś jeszcze dodać?)* | **Já, ek em saklauss.** *(Powiedz na koniec, że jesteś niewinny.)* | „Saklauss” to niewinny. |
| 9 | Ek yrki þat, sem þú sagðir. Far vel! *(Ułożę wiersz z tego, co Pan powiedział. Żegnaj!)* | — |  |

### Poziom 3: Hersir  (typed=0.4, hint=bank, cierpliwość 4)

Nowe słowa: lǫgmaðr = prawnik, Hallsteinn = Hallsteinn (imię), lǫgmann = prawnika (biernik), Úlfs = Úlfra (dopełniacz), vann = wygrał (vinna), samning = umowa, kontrakt (biernik), brúna = most (biernik, z rodzajnikiem), hafði = miał (hafa), bezta = najlepszy (biernik), spurningar = pytania, vitna = świadków (dopełniacz), grunr = podejrzenie, vitum = wiemy (vita), báðir = obaj, ákæra = oskarżenie, sekr = winny, gerða = zrobiłem (gera), Segðu = powiedz (segja), eitt = jeden (r. nijaki), sinn = raz, eiði = przysięga (celownik), Úlfi = Úlfr (celownik), tók = wziął (taka), hersir = hersir (władca okręgu), engar = żadne (r. ż.)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* W hali hersira w Hǫfn. Prawnik Hallsteinn bada kontrakt na nowy most (brú). Statek Úlfra wygrał dziwnie łatwo, a w sprawie wraca „Gauksmál”.  
*Cel:* Wyjdź z przesłuchania jako hersir, nie przyznając się do niczego.  
*Zakończenia:* win: Hallsteinn zamyka księgę: „Engi vitni. Málit er lokit.” Zostajesz hersirem, a most otwiera się z pompą. · partial: Księga zostaje otwarta, ale prawnik nie ma dowodów. Zostajesz hersirem z cieniem podejrzeń. · fail: Hallsteinn kładzie na stole pung i kefli. „Ek tek þik!” mówi. Kończysz w kajdanach.

| 1 | Ek em lǫgmaðr Hallsteinn. Þetta er spurning. *(Jestem prawnikiem Hallsteinnem. To jest przesłuchanie.)* | **Ek vil sjá lǫgmann minn.** *(Poproś o swojego obrońcę.)* | „Mój” przy rodzaju męskim w bierniku to minn: lǫgmann minn. |
| 2 | Skip Úlfs vann samning um brúna. Hví? *(Okręt Úlfra wygrał kontrakt na most. Dlaczego?)* | **Þat hafði bezta boð.** *(Wyjaśnij, że miał najlepszą ofertę.)* | „Miał” to hafði; „najlepsza oferta” to bezta boð. |
| 3 | Vér hǫfum margar spurningar. Vilt þú bera vitni? *(Mamy wiele pytań. Czy chce Pan zeznawać?)* | **Ek vil eigi bera vitni.** *(Odmów składania zeznań.)* | „Zeznawać” to bera vitni; „nie chcę” to ek vil eigi. |
| 4 | Án vitna er engi grunr. Þat vitum vér báðir. *(Bez świadków nie ma podejrzenia. Wiemy to obaj.)* | **Þú hefir engi vitni.** *(Powiedz prawnikowi, że nie ma świadków.)* | „Żadne świadki” to engi vitni. |
| 5 | Kannski kemr ákæra. Hvat segir þú? *(Być może będzie oskarżenie. Co Pan na to?)* | **Ek em saklauss.** (dobra); złe: Ek em sekr.; Ek gerða þat. | „Sekr” to winny, a to przyznanie.;„Ek gerða þat” to przyznanie się. |
| 6 | Úlfr segir, at hann gaf þér pung. *(Úlfr mówi, że dał Panu mieszek.)* | **Þat er lygi! Ek hefi aldri tekit pung.** *(Zaprzecz: to kłamstwo, nigdy nie wziąłeś mieszka.)* · warianty: Þat er lygi! Ek hefi aldri tekit pung. | „Nigdy nie wziąłem” to ek hefi aldri tekit; pung w bierniku to pung. |
| 7 | Segðu þá enn eitt sinn undir eiði. Tókt þú silfr af Úlfi? *(A więc powiedz to jeszcze raz pod przysięgą. Wziął Pan srebro od Úlfra?)* | **Nei, ek tók ekki silfr af Úlfi.** *(Zaprzeczaj pod przysięgą: nie wziąłeś od niego srebra.)* · ŚMIERTELNE | „Od Úlfra” to af Úlfi (celownik); „nie wziąłem” to ek tók ekki. Jedna wpadka i koniec. |
| 8 | Gott. Þú ert hersir. Ek hefi engar spurningar. *(Dobrze. Jest Pan hersirem. Nie mam więcej pytań.)* | — |  |

### Poziom 4: Lǫgréttumaðr  (typed=0.6, hint=letters, cierpliwość 4)

Nowe słowa: Lǫgréttu = Lǫgrétta (zgromadzenie ustawodawcze, biernik), segi = mówię (segja), friðhelgi = nietykalność, lǫgréttumaðr = członek Lǫgrétty, láta = pozwolić, oddać, Vitnisburðr = zeznanie, mótsǫgn = sprzeczność, gǫgnin = dowody (z rodzajnikiem), skýrir = wyjaśnia (skýra), ekkert = nic, leyna = ukryć, hugsa = myślą (hugsa), lengr = dłużej, fortíð = przeszłość, skrifaða = napisałem (skrifa), skrifaði = napisał (skrifa), fekkt = dostałeś (fá), fekk = dostałem (fá), þinginu = ting (celownik, z rodzajnikiem), sjáumst = zobaczymy się (sjá)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Alþingi, Lǫgrétta. Jesteś członkiem Lǫgrétty, a Lǫgsǫgumaðr Valgerðr wzywa cię jako świadka w sprawie „Gauksmál”. Prawnicy mają dla ciebie nowe słowa: vitni, eiðr, friðhelgi.  
*Cel:* Odpowiadaj pod przysięgą tak, by nikt nie dowiódł, że kłamiesz.  
*Zakończenia:* win: Valgerðr: „Vitnisburðr er lokit.” Wychodzisz z hali z uniesioną głową. Zgromadzenie nic nie ma. · partial: Lǫgrétta kończy bez wniosków, ale jeden członek zapisał na tabliczce: „Rannsaka síðar!” · fail: Lǫgrétta każe ci wyjaśnić sprzeczność. Zaplątałeś się, a skaldowie śpiewają o „lygimaðr”.

| 1 | Velkominn í Lǫgréttu. Þú ert undir eiði. *(Witamy w Lǫgréttcie. Zeznaje Pan pod przysięgą.)* | **Já, ek veit þat. Ek segi satt.** *(Potwierdź i zapewnij, że mówisz prawdę.)* | „Mówić prawdę” to segja satt. „Pod przysięgą” to undir eiði. |
| 2 | Þú hefir friðhelgi sem lǫgréttumaðr. Vilt þú láta hana af hendi? *(Jako członek Lǫgrétty ma Pan nietykalność. Czy chce Pan jej się zrzec?)* | **Nei, ek vil halda friðhelgi minni.** *(Odmów zrzeczenia się nietykalności.)* | „Zachować” to halda; „moja nietykalność” w celowniku to friðhelgi minni. |
| 3 | Vitnisburðr þinn er í mótsǫgn við gǫgnin. Hvé skýrir þú þat? *(Pańskie zeznanie jest sprzeczne z dowodami. Jak Pan to wyjaśni?)* | **Ek hefi ekkert at leyna.** *(Powiedz, że nie masz nic do ukrycia.)* | „Nic do ukrycia” to ekkert at leyna. |
| 4 | Þat er langt síðan. Kjósendr hugsa eigi lengr um þat. *(To było dawno. Wyborcy już o tym nie myślą.)* | **Þat er fortíð.** *(Machnij ręką: to przeszłość.)* | „Przeszłość” to fortíð. |
| 5 | Hér er bréf frá Úlfi. Kennir þú þat? *(Oto list od Úlfra. Zna go Pan?)* | **Ek kenni eigi bréfit.** (dobra); złe: Já, ek skrifaða bréfit.; Lǫgmaðr minn skrifaði bréfit. | Przyznajesz się, że to ty napisałeś list: to błąd.;Zwalanie na prawnika nie jest wiarygodne. |
| 6 | Vitni segir, at þú fekkt pung með silfri. *(Świadek mówi, że dostał Pan mieszek ze srebrem.)* | **Vitnit lýgr. Ek fekk ekkert silfr.** *(Nazwij świadka kłamcą i zaprzecz, że dostałeś srebro.)* | „Dostałem” to ek fekk; „żadne srebro” to ekkert silfr. |
| 7 | Á þinginu sagðir þú, at þú kennir Úlf varla. Er þat enn satt? *(Na tingu powiedział Pan: „Ledwo znam Úlfra.” Czy to nadal prawda?)* | **Já, ek kenni hann varla.** (dobra); złe: Nei, hann er vinr minn.; Nei, ek hefi aldri sét hann. · ŚMIERTELNE | Przyznajesz, że to twój przyjaciel: sprzeczność i koniec.;Wcześniej mówiłeś „varla”, a nie „nigdy go nie widziałem”. |
| 8 | Þakka þér. Þú mátt fara. Vér sjáumst brátt aptr. *(Dziękuję. Może Pan odejść. Wkrótce znów się zobaczymy.)* | — |  |

### Poziom 5: Jarl  (typed=0.8, hint=bank, cierpliwość 4)

Nowe słowa: kvǫld = wieczór, erum = jesteśmy (vera), Óvinir = wrogowie, skandall = skandal, sé = jest (vera, tryb łączący), Gauksmál = Gauksmál (sprawa Kukułki), áróðr = propaganda, rúnum = runy (celownik mn.), stendr = stoi (standa), innsigli = pieczęć, minnumk = pamiętam (minnask), þess = tego (dopełniacz), fǫlsun = fałszerstwo, Fylgi = poparcie, vex = rośnie (vaxa), traust = zaufanie, yðart = wasze (r. nijaki), ráðgjafi = doradca, unnit = pracował (vinna), honum = nim (celownik), oft = często, punginum = mieszek (celownik, z rodzajnikiem), hers = wojska (dopełniacz), míns = mojego (dopełniacz)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Uczta w hali króla, a Þorvaldr, skald i gospodarz uczty, pyta cię publicznie. Jesteś jarlem i siedzisz naprzeciw niego. Nagle skald odczytuje stare runy z „Gauksmál”.  
*Cel:* Wyjdź z uczty nadal jako jarl: nie daj się zapędzić w pułapkę przy wszystkich.  
*Zakończenia:* win: Þorvaldr kończy wiersz: „Þakka þér, jarl.” Poparcie rośnie. Úlfr przysyła róg miodu: „Vel gert!” · partial: Uczta kończy się remisem. Wrogowie żądają, byś odstąpił od władzy, ale król cię broni. · fail: Na oczach wszystkich uciekasz od odpowiedzi, a goście wszystko widzą. Rano skaldowie śpiewają o twoim upadku.

| 1 | Gott kvǫld! Vér erum í hǫll konungs. Ert þú búinn, jarl? *(Dobry wieczór! Jesteśmy w hali króla. Jest Pan gotów, jarlu?)* | **Já, ek em búinn. Gjarna.** *(Potwierdź, że jesteś gotów.)* | „Gotów” to búinn. |
| 2 | Óvinir segja, at skandall sé um Gauksmál. *(Wrogowie mówią: wokół Gauksmál jest skandal.)* | **Þat er engi skandall. Þat er áróðr.** *(Zbagatelizuj: to nie skandal, tylko propaganda.)* | „Propaganda” to áróðr; „żaden skandal” to engi skandall. |
| 3 | Á rúnum stendr nafn þitt. Þat er innsigli þitt. *(Na runach jest Pańskie imię. To Pański pieczęć.)* | **Ek minnumk þess ekki.** *(Powiedz, że tego nie pamiętasz.)* | „Pamiętać” to minnask; „nie pamiętam tego” to ek minnumk þess ekki. |
| 4 | Þetta er innsigli þitt. Hvé skýrir þú þat? *(To jest Pański pieczęć. Jak Pan to wyjaśni?)* | **Þat er fǫlsun.** *(Zaprzecz: to fałszerstwo.)* | „Fałszerstwo” to fǫlsun. |
| 5 | Fylgi þitt vex. Kjósendr trúa þér. *(Poparcie rośnie. Wyborcy Panu wierzą.)* | **Ek þakka yðr traust yðart.** *(Podziękuj wyborcom za zaufanie.)* | „Zaufanie” to traust; „dziękuję wam” to ek þakka yðr. |
| 6 | Úlfr segir, at hann var ráðgjafi þinn. Er þat satt? *(Úlfr mówi, że był Pańskim doradcą. Czy to prawda?)* | **Nei, ek hefi aldri unnit með honum.** (dobra); złe: Já, hann gaf mér oft silfr.; Ek vil eigi bera vitni. | Przyznajesz się do srebra: błąd.;Odmowa zeznań przy wszystkich wygląda na przyznanie się, a skald to wykorzysta. |
| 7 | Vilt þú segja af þér? Þá er allt lokit. *(Czy chce Pan zrezygnować? Wtedy wszystko skończone.)* | **Nei, ek segi eigi af mér. Ek em saklauss.** *(Odmów rezygnacji i powiedz, że jesteś niewinny.)* | „Zrezygnować” to segja af sér; „nie zrezygnuję” to ek segi eigi af mér. |
| 8 | Hér er rúnakefli: þú ok Úlfr. Þar er ok pungr. Hvat er í punginum? *(Oto kij z runami: Pan i Úlfr. Jest też mieszek. Co jest w mieszku?)* | **Keflit er gamalt. Ek hefi aldri tekit pung.** (dobra); złe: Þat er silfr til hers míns.; Þat var einungis gjǫf. · ŚMIERTELNE | Przyznanie się do srebra: koniec.;„Gjǫf” to też przyznanie, bo wcześniej mówiłeś, że nie brałeś mieszka. |
| 9 | Þakka þér fyrir, jarl. *(Dziękuję, jarlu.)* | — |  |

### Poziom 6: Konungr  (typed=1, hint=none, cierpliwość 4)

Nowe słowa: Velkomin = witaj (r. ż.), Gunnhildr = Gunnhildr (imię), konungsefni = kandydat na króla, ger = zrób (gera), hinni = tej (celownik r. ż.), heiðarligu = uczciwa (celownik r. ż. przymiotnik słaby), Seg = mów (segja), ásǫk = zarzut, hafna = odrzucam (hafna), þeirri = tej (celownik r. ż.), kosningabarátta = kampania wyborcza, Barátta = walka, kampania, óhrein = brudna, gǫgn = dowody, ætlan = plan, landit = kraj (z rodzajnikiem), skapa = tworzę (skapa), ný = nowe, Hamingju = szczęście (biernik), óska = życzę (óska)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Wielki spór na tingu przed wyborem króla. Kandydujesz na króla (konungr). Naprzeciw stoi Jarl Gunnhildr z rodu „Hin heiðarliga ætt” i jej księga ze „Gauksmál”. Cały kraj słucha.  
*Cel:* Wygraj spór, zachowaj spokój i nie przyznaj się do niczego do samego końca.  
*Zakończenia:* win: Przegrywa nawet wróżba: pięćdziesiąt dwóch na stu woła twoje imię. Zostajesz królem, a mieszek Úlfra leży na dnie skrzyni. · partial: Spór kończy się remisem. Wybór wygrywasz o włos i obiecujesz „więcej jawności”. · fail: Gunnhildr kładzie na stole księgę. Kraj widzi sprzeczność w twoich słowach, a skald wyśpiewuje: „Konungsefni lýgr.”

| 1 | Velkomin á þing! Gunnhildr jarl, konungsefni, ger svá vel. *(Witamy na tingu! Jarlu Gunnhildr, kandydacie, proszę.)* | **Gott kvǫld. Ek vil verða konungr.** *(Przywitaj się i powiedz, że chcesz zostać królem.)* | „Zostać królem” to verða konungr. |
| 2 | Ek em af ætt hinni heiðarligu. Seg satt, konungsefni! *(Jestem z rodu Uczciwych. Mów prawdę, kandydacie!)* | **Ek segi ávallt satt.** *(Zapewnij, że zawsze mówisz prawdę.)* | „Ávallt” to „zawsze”, stoi po czasowniku. |
| 3 | Þú hefir tekit við mútu. Þat er ásǫk mín. *(Brał Pan łapówki. To mój zarzut.)* | **Ek hafna þeirri ásǫk.** *(Odrzuć ten zarzut.)* | „Odrzucić” to hafna; „ten zarzut” w celowniku to þeirri ásǫk. |
| 4 | Þetta er einungis kosningabarátta. Þat er langt síðan. *(To tylko kampania wyborcza. To było dawno.)* | **Barátta þín er óhrein.** *(Zarzuć rywalce brudną kampanię.)* | „Brudna” to óhrein. |
| 5 | Hefir þú gǫgn, Gunnhildr? Ek sé engi gǫgn! *(Ma Pani dowody, Gunnhildr? Ja nie widzę żadnych dowodów!)* | **Ek sé engi gǫgn.** *(Powtórz, że nie widzisz żadnych dowodów.)* | „Dowody” to gǫgn; „żadnych” to engi. |
| 6 | Ok hvat er ætlan þín fyrir landit? *(A jaki jest Pański plan dla kraju?)* | **Ek skapa ný verk.** *(Obiecaj nowe miejsca pracy.)* | „Nowe prace” to ný verk; „stworzę” to ek skapa. |
| 7 | Vinr þinn Úlfr segir, at hann gaf þér mikit silfr! *(Pański przyjaciel Úlfr mówi, że dał Panu dużo srebra!)* | **Þat er lygi! Hann er eigi vinr minn.** *(Zaprzecz: to kłamstwo, on nie jest twoim przyjacielem.)* | „Nie mój przyjaciel” to eigi vinr minn. |
| 8 | Á þinginu sagðir þú, at hann er einungis kunningi. Ok nú? *(Na tingu powiedział Pan: to tylko znajomy. A teraz?)* | **Hann er einungis kunningi.** (dobra); złe: Hann er vinr minn.; Ek hefi aldri sét hann. | Zaprzeczasz sam sobie.;Wcześniej przyznałeś, że go znasz („kunningi”), więc „nigdy go nie widziałem” to sprzeczność. |
| 9 | Gunnhildr sýnir pung. Tókt þú hann? Já eða nei? *(Gunnhildr pokazuje mieszek. Wziął go Pan? Tak czy nie?)* | **Nei, ek tók hann aldri.** (dobra); złe: Já, ek tók hann.; Ek vil eigi bera vitni. · ŚMIERTELNE | Przyznanie się: koniec.;Milczenie przy wszystkich wygląda jak przyznanie się. |
| 10 | Ok konungr ert þú! Hamingju óska ek þér! *(A królem zostaje… Pan! Serdeczne gratulacje!)* | — |  |

## Przystań (hofn)

**Scena:** Heiðabýr, wczesny ranek. Płyniesz do Niðaróss na wesele najlepszego przyjaciela, a okręt nie poczeka. Masz kufer, srebro i mało czasu.  
**Cel:** Przejdź całą drogę: zapłata za przeprawę, kontrola na nabrzeżu, sztorm i zmiana kei, rejs i odbiór kufra w Niðaróss.  
**Rozmówca:** Hafnarvǫrðr  
**Zakończenia:** win: Docierasz do Niðaróss z kufrem, srebrem i pół dnia zapasu. Przyjaciel czeka na nabrzeżu z rogiem miodu: „Þú komt! Brúðlaup skal hefjast!” · partial: Dotarłeś do Niðaróss, ale po drodze sporo się nagadałeś i trochę pobiegałeś. Kufer jest, wesele też, ty trochę zdyszany, ale na czas. · fail: Pomyliłeś coś w najgorszym momencie i okręt odpłynął bez ciebie. Wesele oglądasz tylko w myślach, a przyjaciel obiecuje ci długą ucztę „na pocieszenie”.  

### Poziom 1: Opłata za przeprawę  (typed=0, hint=none, cierpliwość 6)

Nowe słowa: skips = okręt (dopełniacz), „Norðanvinds” = „Norðanvindr” (nazwa okrętu, dopełniacz), Niðaróss = Niðaróss (miasto, dopełniacz), brúðlaups = wesele (dopełniacz), kistu = kufer (biernik), þung = ciężka, kistunni = kufer (celownik, z rodzajnikiem), miðju = środek (celownik), skipi = okręt (celownik), merki = znak, dagmál = dagmál (pora dnia, ok. 9 rano), nǫkkura = jakieś (biernik), réttum = właściwym (celownik), tíma = czas (celownik), Leggstu = połóż się, cumuj (leggja), bryggju = keja (biernik), beint = prosto, bezpośrednio, áfram = naprzód

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Przystań w Heiðabýr, tuż po wschodzie słońca. Podchodzisz do stanowiska szypra okrętu „Norðanvindr”. Szyper patrzy na ciebie życzliwie i czeka na opłatę.  
*Cel:* Opłać przeprawę do Niðaróss: powiedz, dokąd płyniesz, zapłać srebrem, zostaw kufer i wybierz miejsce na okręcie.  
*Zakończenia:* win: Szyper podaje ci znak przeprawy: „Góða ferð!” Kufer jedzie na pokład, a ty idziesz na nabrzeże, gdzie czeka kontrola. · partial: Opłata udała się, ale szyper kilka razy musiał się domyślać, o co ci chodzi. Znak w ręku, czas ucieka. · fail: Szyper nie rozumie, czego chcesz, i woła następnego w kolejce. Musisz zacząć od nowa na końcu kolejki.

| 1 | Góðan dag! Velkominn til skips „Norðanvinds”. Hvert ferr þú? *(Dzień dobry! Witamy na okręcie „Norðanvindr”. Dokąd Pan płynie?)* | **Góðan dag! Ek fer til Niðaróss.** *(Przywitaj się i powiedz, że płyniesz do Niðaróss.)* | „Płynę” to ek fer, a „do” miasta to til. |
| 2 | Hví fer þú til Niðaróss? *(Po co Pan płynie do Niðaróss?)* | **Ek fer til brúðlaups.** *(Powiedz, że płyniesz na wesele.)* | „Na wesele” to til brúðlaups. |
| 3 | Gott! Vilt þú hafa kistu með þér? *(Dobrze! Czy chce Pan wziąć kufer ze sobą?)* | **Já, ek vil hafa kistu með mér.** *(Powiedz, że chcesz wziąć kufer.)* | „Chcę mieć” to ek vil hafa. |
| 4 | Kista þín er þung. Hvat hefir þú í kistunni? *(Pana kufer jest ciężki. Co Pan ma w kufrze?)* | **Ek hefi klæði ok gjǫf.** *(Powiedz, że masz ubrania i dar.)* | „Mam” to ek hefi, a „ubrania” to klæði. |
| 5 | Gott. Vilt þú sitja við borð eða á miðju skipi? *(Dobrze. Chce Pan siedzieć przy burcie czy pośrodku okrętu?)* | **Við borð, gjarna.** *(Powiedz, że wolisz przy burcie.)* | „Przy burcie” to við borð. |
| 6 | Hér er merki þitt. Skipit fer um dagmál. Hefir þú nǫkkura spurning? *(Oto Pana znak. Okręt odpływa o dagmál. Czy ma Pan pytanie?)* | **Já, er skipit á réttum tíma?** *(Zapytaj, czy okręt jest na czas.)* | Pytanie zaczyna się od czasownika: er skipit á réttum tíma? |
| 7 | Já, skipit er á réttum tíma. Leggstu við bryggju þrjú. Far beint áfram. *(Tak, okręt jest na czas. Cumujemy przy keji trzeciej. Idź prosto.)* | **Þakka þér! Far vel!** *(Podziękuj i pożegnaj się.)* | „Żegnaj” to far vel. |
| 8 | Góða ferð! *(Szczęśliwej podróży!)* | — |  |

### Poziom 2: Kontrola na nabrzeżu  (typed=0.25, hint=bank, cierpliwość 5)

Nowe słowa: tollr = cło, poborca cła, Legg = połóż (leggja), þína = twoją (biernik r. ż.), auðvitað = oczywiście, drykk = napój (biernik), dæmis = przykład (dopełniacz), einnig = także, kyrtil = kaftan (biernik), borðit = stół (z rodzajnikiem), mitt = moje (r. nijaki), hvárki = ani, øxi = topór (biernik), né = ani, hliðit = brama (z rodzajnikiem), vasa = kieszeń (celownik), þínum = twoim (celownik), lykil = klucz (biernik), hníf = nóż (biernik), lítinn = mały (biernik r. m.), lagi = porządek (celownik); „í lagi” = w porządku

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Masz znak przeprawy, a przed tobą długa kolejka do kontroli. Poborca cła podchodzi do twojego kufra i patrzy uważnie na twój pas.  
*Cel:* Przejdź kontrolę na nabrzeżu: pokaż kufer, zdejmij pas i odpowiedz na pytania poborcy.  
*Zakończenia:* win: Poborca kiwa głową: „Allt er í lagi. Far fram.” Zakładasz pas i biegniesz na keję z pełnym spokojem. · partial: Kontrola przebiegła w końcu bez problemów, ale poborca kilka razy zmarszczył brwi. Zakładasz pas w biegu. · fail: Poborca uznaje twoje odpowiedzi za podejrzane. Zostajesz zatrzymany na dodatkową kontrolę, a okręt odpływa bez ciebie.

| 1 | Góðan dag! Hér er tollr. Legg kistu þína hér á borð. *(Dzień dobry! To jest cło. Połóż kufer tutaj na stole.)* | **Já, auðvitað.** *(Zgódź się i powiedz, że oczywiście.)* | „Oczywiście” to auðvitað. |
| 2 | Hefir þú sverð í kistunni? Opna kistuna, ger svá vel. *(Czy ma Pan miecz w kufrze? Proszę otworzyć kufer.)* | **Já, hér er kista mín.** *(Potwierdź i pokaż kufer.)* | „Mój” przy rodzaju żeńskim to mín: kista mín. |
| 3 | Hefir þú drykk á þér? Til dæmis mjǫð eða ǫl? *(Czy ma Pan przy sobie napój? Na przykład miód albo piwo?)* | **Nei, ek hefi engan drykk á mér.** *(Zaprzecz: nie masz napoju.)* | „Nie mam żadnego” to ek hefi engan. |
| 4 | Legg einnig belti þitt ok kyrtil á borðit. *(Połóż też pas i kaftan na stole.)* | **Já, hér eru belti mitt ok kyrtill minn.** *(Podaj pas i kaftan.)* | Liczba mnoga od „oto” to hér eru. |
| 5 | Er í kistu þinni øx eða sverð? *(Czy w Pana kufrze jest topór albo miecz?)* | **Nei, ek hefi hvárki øxi né sverð.** (dobra); złe: Já, ek hefi øxi.; Ek veit eigi, kannski. · ŚMIERTELNE | Przyznanie się do topora to natychmiastowe zatrzymanie.; Niepewna odpowiedź przy takim pytaniu wzbudza podejrzenia: zatrzymanie. |
| 6 | Far nú um hliðit. Hefir þú enn nǫkkut í vasa þínum? *(Przejdź teraz przez bramkę. Czy ma Pan jeszcze coś w kieszeni?)* | **Já, ek hefi lykil ok hníf lítinn.** *(Powiedz, że masz klucz i mały nóż.)* | „Klucz” to lykill, a „nóż” to hnífr. |
| 7 | Allt er í lagi. Far fram. Góða ferð! *(Wszystko w porządku. Idź dalej. Szczęśliwej podróży!)* | — |  |

### Poziom 3: Przy keji  (typed=0.5, hint=bank, cierpliwość 4)

Nowe słowa: Afsakaðu = przepraszam, farþegi = pasażer, fjórar = cztery (r. ż.), stundir = godziny, Ferðin = rejs (z rodzajnikiem), hefst = zaczyna się (hefjast), nón = nón (pora dnia, ok. 15), ferðin = rejs (z rodzajnikiem), Þarf = musi (þurfa), Niðarósi = Niðaróss (celownik), Gætið = uważajcie (gæta), lokuð = zamknięta (r. ż.), skilit = zrozumiał (skilja), geng = idę (ganga), opit = otwarty (r. nijaki)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Siedzisz przy keji trzeciej i patrzysz na niebo. Nagle rogi wołają, a z wież strażniczych słychać krzyk, że nadciąga sztorm.  
*Cel:* Dowiedz się, co z rejsem, zrozum wezwanie o zmianie keji i wejdź na pokład.  
*Zakończenia:* win: Biegniesz do nowej keji i wskakujesz na pokład jako jeden z ostatnich. Hafnarmaðr zwija trap: „Þat var naumt!” · partial: Znalazłeś w końcu właściwą keję, choć po drodze kilka razy musiałeś dopytywać. Wchodzisz na pokład mokry. · fail: Zrozumiałeś wezwanie na opak i czekasz przy złej keji. Kiedy się orientujesz, okręt już odbił od brzegu.

| 1 | Afsakaðu! Ert þú farþegi á skipi til Niðaróss? *(Przepraszam! Czy jest Pan pasażerem okrętu do Niðaróss?)* | **Já, skip mitt er seint, eða hvat?** *(Potwierdź i zapytaj, czy twój okręt jest spóźniony.)* | „Spóźniony” to seinn; „eða hvat?” na końcu znaczy „prawda?”. |
| 2 | Já, skipit er fjórar stundir seint. Ferðin hefst um nón. *(Tak, okręt jest spóźniony o cztery godziny. Rejs zacznie się o nón.)* | **Hvenær hefst ferðin? Ek skal til brúðlaups.** *(Zapytaj, kiedy rejs, i dodaj, że płyniesz na wesele.)* | Pytanie o czas zaczyna się od hvenær: hvenær hefst ferðin? |
| 3 | Brúðlaup, hvé gott! Ferðin hefst um nón. Þarf þú at skipta um skip í Niðarósi? *(Wesele, jak miło! Rejs zaczyna się o nón. Czy musi Pan zmienić okręt w Niðaróss?)* | **Nei, ek fer beint til Niðaróss.** *(Odpowiedz, że nie, płyniesz bezpośrednio.)* | „Bezpośrednio” to beint. |
| 4 | Gott, beint. Gætið! Stormr kemr. Skipit fer nú frá bryggju fimm. Bryggja þrjú er lokuð. Hefir þú skilit þat? Hvert ferr þú? *(Dobrze, bezpośrednio. Uwaga! Nadciąga sztorm. Okręt odpływa teraz od keji piątej. Keja trzecia jest zamknięta. Czy Pan zrozumiał? Dokąd Pan idzie?)* | **Ek fer til bryggju fimm.** (dobra); złe: Ek verð við bryggju þrjú.; Ek fer heim. · ŚMIERTELNE | Keja trzecia jest zamknięta, więc czekanie tam kończy się spóźnieniem.; Dom to nie keja okrętu. |
| 5 | Þá skjótt! Sýn mér merki þitt. Þú mátt nú ganga á skip. *(W takim razie szybko! Pokaż mi znak. Możesz już wejść na okręt.)* | **Hér er merki mitt. Ek geng nú á skip.** *(Podaj znak i powiedz, że wchodzisz na okręt.)* | „Wchodzę” to ek geng á skip. |
| 6 | Góða ferð! Skipit er opit. *(Szczęśliwej podróży! Okręt jest otwarty.)* | — |  |

### Poziom 4: Rejs i przybycie  (typed=0.75, hint=letters, cierpliwość 4)

Nowe słowa: Haldit = trzymajcie (halda), reipit = lina (z rodzajnikiem), siglum = żeglujemy (sigla), bráðum = zaraz, held = trzymam (halda), komum = przybywamy (koma), tveimr = dwóch (celownik), eftir = po, potem, gestahús = gospoda, fyrst = najpierw, Fyrst = najpierw, tollsins = cło (dopełniacz, z rodzajnikiem), gestahúss = gospoda (dopełniacz), kistunnar = kufer (dopełniacz, z rodzajnikiem), fjǫgur = cztery (r. nijaki), tolla = oclić, cło, spyrr = pyta (spyrja), mikil = wielka (r. ż.), skemmtun = zabawa, brúðlaupinu = wesele (celownik, z rodzajnikiem)

| # | Rozmówca | Uczeń (poprawnie) | Wyjaśnienie |
|---|---|---|---|

*Scena:* Wchodzisz na pokład „Norðanvinds”. Sternik wita pasażerów przy trapie, a za chwilę okręt wypłynie do Niðaróss. Po przybyciu będziesz musiał jeszcze znaleźć poborcę cła i swój kufer.  
*Cel:* Zajmij miejsce, poproś o picie, a po przybyciu dowiedz się, gdzie jest kontrola, gdzie leży kufer i czy masz coś do oclenia.  
*Zakończenia:* win: Kufer stoi na nabrzeżu jako pierwszy, a poborca życzy ci „Velkominn til Nóregs!” Przyjaciel czeka z rogiem miodu. · partial: Wszystko udało ci się znaleźć, ale po drodze trzy razy zapytałeś o drogę. Kufer dotarł, a ty zdążysz na wesele. · fail: Poszedłeś w złą stronę i straciłeś czas na nabrzeżu. Kufer stoi samotnie, a przyjaciel wysyła posłańców co chwilę.

| 1 | Góðan dag ok velkominn á skip! Sýn mér merki þitt. *(Dzień dobry i witamy na okręcie! Pokaż mi znak.)* | **Góðan dag! Hér er merki mitt.** *(Przywitaj się i pokaż znak.)* | „Oto” przy liczbie pojedynczej to hér er. |
| 2 | Rúm þitt er fjórtán. Þat er við borð. Legg kistu þína undir bekk. *(Pana miejsce to czternaste. To przy burcie. Połóż kufer pod ławą.)* | **Þakka þér, ek legg kistu undir bekk.** *(Podziękuj i powiedz, że kładziesz kufer pod ławę.)* | „Kładę” to ek legg, a „pod ławę” to undir bekk. |
| 3 | Haldit í reipit. Vér siglum bráðum. *(Trzymaj się liny. Zaraz wypływamy.)* | **Já, ek held í reipit.** *(Powiedz, że trzymasz linę.)* | „Trzymam” to ek held. |
| 4 | Vilt þú drykk? *(Czy chce Pan napój?)* | **Já, ǫl, ger svá vel.** *(Poproś o piwo.)* | „Piwo” to ǫl, rodzaju nijakiego. |
| 5 | Hér er ǫl þitt. Hvat vilt þú vita meira? *(Oto Pana piwo. Czy chce Pan jeszcze o coś zapytać?)* | **Hvenær komum vér til Niðaróss?** *(Zapytaj, kiedy przypłyniecie do Niðaróss.)* | „Kiedy” to hvenær, a „przypływamy” to komum vér. |
| 6 | Vér komum á tveimr dǫgum. Velkominn til Niðaróss! Ferðin var góð. *(Przypływamy za dwa dni. Witamy w Niðaróss! Rejs był dobry.)* | **Þakka þér! Hvar er tollr, ger svá vel?** *(Podziękuj i zapytaj, gdzie jest cło.)* | Pytanie o miejsce zaczyna się od hvar: hvar er tollr? |
| 7 | Tollr er til vinstri. Þar eftir kemr kista þín ok svá gestahús. Hvert ferr þú fyrst? *(Cło jest po lewej. Potem Pana kufer, a potem gospoda. Dokąd Pan idzie najpierw?)* | **Fyrst fer ek til tollsins.** (dobra); złe: Fyrst fer ek til gestahúss.; Fyrst fer ek til kistunnar. · ŚMIERTELNE | Do gospody idziesz na końcu, po odbiorze kufra.; Kufer odbierasz dopiero po kontroli. |
| 8 | Rétt! Ok þá til kistunnar. Kista þín stendr við bryggju fjǫgur. *(Dokładnie! A potem do kufra. Pana kufer stoi przy keji czwartej.)* | **Þakka þér! Ek tek kistuna af bryggju.** *(Podziękuj i powiedz, że zabierasz kufer z keji.)* | „Zabieram” to ek tek, a „z keji” to af bryggju. |
| 9 | Hefir þú nǫkkut at tolla? Þat spyrr tollr. *(Czy ma Pan coś do oclenia? O to zapyta poborca.)* | **Nei, ek hefi ekkert at tolla.** *(Powiedz, że nie masz nic do oclenia.)* | „Nic” to ekkert: ekkert at tolla. |
| 10 | Þá er allt gott. Velkominn til Nóregs ok mikil skemmtun í brúðlaupinu! *(Wtedy wszystko w porządku. Witamy w Norwegii i dobrej zabawy na weselu!)* | — |  |
