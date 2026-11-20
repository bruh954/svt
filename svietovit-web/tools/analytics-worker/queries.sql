-- Najczęstsze pytania do bazy (uruchamiasz je w panelu Cloudflare: D1 > twoja baza > Console).

-- 1. Nowi użytkownicy dziennie
SELECT d0 AS dzien, COUNT(DISTINCT cid) AS nowi FROM events WHERE cid IS NOT NULL GROUP BY d0 ORDER BY d0 DESC;

-- 2. Powrót po 7 dniach: ilu z osób, które przyszły pierwszego dnia, wróciło dokładnie po 7 dniach (lub później w oknie 7-9 dni)
SELECT a.d0 AS kohorta,
       COUNT(DISTINCT a.cid) AS osoby,
       COUNT(DISTINCT CASE WHEN julianday(b.day) - julianday(a.d0) BETWEEN 7 AND 9 THEN a.cid END) AS wrocilo_d7,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN julianday(b.day) - julianday(a.d0) BETWEEN 7 AND 9 THEN a.cid END) / COUNT(DISTINCT a.cid), 1) AS procent
FROM (SELECT DISTINCT cid, d0 FROM events WHERE cid IS NOT NULL AND d0 IS NOT NULL) a
JOIN events b ON b.cid = a.cid
GROUP BY a.d0 ORDER BY a.d0 DESC;

-- 3. Ile osób zaczęło larp i ile skończyło, z wynikiem
SELECT json_extract(props, '$.larp') AS larp, COUNT(*) AS starty FROM events WHERE name = 'larp_start' GROUP BY larp;
SELECT json_extract(props, '$.larp') AS larp, json_extract(props, '$.outcome') AS wynik, COUNT(*) AS ile FROM events WHERE name = 'larp_end' GROUP BY larp, wynik;

-- 4. Opinie o trudności i tempie larpów
SELECT json_extract(props, '$.larp') AS larp, json_extract(props, '$.difficulty') AS trudnosc, json_extract(props, '$.pace') AS tempo, COUNT(*) AS ile
FROM events WHERE name = 'larp_feedback' GROUP BY larp, trudnosc, tempo ORDER BY larp, ile DESC;

-- 5. Rzucone lekcje (porzucone w trakcie) i ukończone
SELECT name, COUNT(*) FROM events WHERE name IN ('lesson_start', 'lesson_done', 'lesson_abandon') GROUP BY name;
