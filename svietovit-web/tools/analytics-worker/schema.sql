CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ts INTEGER NOT NULL,      -- czas (ms)
  day TEXT NOT NULL,        -- data zdarzenia YYYY-MM-DD
  name TEXT NOT NULL,       -- np. app_open, lesson_done, larp_end, larp_feedback
  props TEXT,               -- JSON z parametrami (kurs, larp, wynik...)
  lang TEXT,
  cid TEXT,                 -- losowy anonimowy numer przeglądarki (puste przy opinii bez zgody)
  d0 TEXT                   -- data pierwszej wizyty tej przeglądarki
);
CREATE INDEX IF NOT EXISTS idx_events_name_day ON events(name, day);
