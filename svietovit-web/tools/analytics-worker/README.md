# Statystyki Śviętovita (anonimowe, za zgodą)

Aplikacja wysyła zdarzenia (otwarcie, ukończona lekcja, start i wynik larpa, opinia o trudności i tempie) pod adres z `web/config.js` → `analytics.endpoint`. Dopóki adres jest pusty, nic nie jest wysyłane.

Co leci: nazwa zdarzenia, kurs, larp, poziom, wynik, język interfejsu, losowy numer przeglądarki i data pierwszej wizyty (oba tylko po zgodzie). Nie ma imienia, e-maila ani treści odpowiedzi. Opinia o larpie (trudność, tempo) idzie bez numeru nawet bez zgody, bo użytkownik wybiera ją sam.

## Uruchomienie (około 15 minut, darmowy plan Cloudflare)

1. Załóż konto na cloudflare.com.
2. W panelu: **Storage & Databases → D1 → Create database** (nazwa np. `sviet-stats`). W zakładce **Console** wklej zawartość `schema.sql` i uruchom.
3. **Workers & Pages → Create → Worker**, nazwa np. `sviet-stats`, wklej zawartość `worker.js`, zapisz i wdróż.
4. W ustawieniach workera: **Bindings → Add → D1 database**, nazwa zmiennej **DB**, wybierz bazę z kroku 2. Wdróż ponownie.
5. Skopiuj adres workera (`https://sviet-stats.<twoje-konto>.workers.dev`) i wpisz go w `web/config.js`: `analytics: { endpoint: "https://…", … }`. Zbuduj i wdróż aplikację.
6. Sprawdź: otwórz aplikację, zgódź się na statystyki i w konsoli D1 uruchom `SELECT * FROM events ORDER BY id DESC LIMIT 5;`.

Gotowe zapytania (powrót po 7 dniach, ukończenie larpów, opinie) są w `queries.sql`.

## Uwaga prawna
Zapisywanie losowego numeru w przeglądarce wymaga zgody, dlatego aplikacja pyta o nią przy pierwszym uruchomieniu i pozwala ją cofnąć na ekranie głównym. Jeśli zbierasz dane od ludzi z UE, dopisz krótką informację o prywatności na stronie (co zbierasz, po co i jak się wycofać). To nie jest porada prawna.
