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
