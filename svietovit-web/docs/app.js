"use strict";
/* Śviętovit – aplikacja webowa. Silniki kursów działają w Pythonie (Pyodide), tu jest tylko interfejs. */
const $ = (s, el = document) => el.querySelector(s);
function h(tag, attrs, ...kids) {
  const e = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v == null || v === false) continue;
    if (k === "class") e.className = v;
    else if (k === "style") e.style.cssText = v;
    else if (k.startsWith("on")) e.addEventListener(k.slice(2), v);
    else if (k === "dir") e.dir = v;
    else e.setAttribute(k, v === true ? "" : v);
  }
  for (const c of kids.flat()) {
    if (c == null || c === false) continue;
    e.append(c.nodeType ? c : document.createTextNode(String(c)));
  }
  return e;
}
const store = {
  get(k, d) { try { const v = localStorage.getItem(k); return v == null ? d : v; } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* tryb prywatny */ } },
};

/* ---------------- teksty interfejsu ---------------- */
const TX = {
  pl: {
    motto: "szkoła języków dawnych i dalekich", learn_in: "Uczę się po", no_chats: "Ten kurs uczy samych znaków. Zdania i rozmowy ćwiczysz w kursie %s.", larps: "Larpy", larps_d: "Sceny ze stawką: płacisz wpisowe w XP i możesz je stracić.", larp_enter: "Wchodzę", larp_rules: "Wpisowe %d XP. Wygrana: +%d XP. Udało się mimo potknięć: zwrot wpisowego. Porażka: tracisz wpisowe. Zła odpowiedź zabiera punkt cierpliwości, a pytanie z ☠ kończy scenę od razu.", larp_need: "Potrzebujesz %d XP, żeby wejść.", larp_goal: "Cel", larp_deadly: "☠ Jedna szansa: zła odpowiedź kończy scenę.", larp_weak: "Niezręcznie.", larp_win: "Sukces!", larp_partial: "Udało się, ale…", larp_fail: "Porażka", larp_quit_t: "Wyjść ze sceny?", larp_quit_d: "Stracisz wpisowe.", larp_refund: "Wpisowe zwrócone", larp_patience: "Cierpliwość", larp_correct: "Poprawnie: ", tonecolor: "Kolory tonów", script: "Pismo ćwiczeń", size: "Litery", theme: "Motyw", th_navy: "Granat", th_sky: "Jasny", new: "nowy", xp: "XP",
    foot: "Postęp zapisuje się w tej przeglądarce. Dodaj stronę do ekranu głównego, żeby działała jak aplikacja.",
    reports: "Zgłoszone błędy: %d", copy: "SKOPIUJ", clear: "WYCZYŚĆ", copied: "Skopiowano. Wklej zgłoszenia w rozmowie z Claude'em.",
    rep_title: "Zgłoś błąd w ćwiczeniu", rep_hint: "Opis (nie musisz nic pisać)", rep_send: "ZAPISZ", rep_cancel: "ANULUJ",
    rep_saved: "Dziękuję! Zgłoszenie zapisane.", path: "Ścieżka", chats: "Rozmowy", practice: "Powtórka", profile: "Profil",
    goal_day: "Cel dnia", locked: "zamknięty", repeat: "warto powtórzyć", start_here: "▸ zacznij tutaj",
    unlock_after: "Odblokujesz po dziale: ", start_lesson: "Zacznij lekcję", close: "Zamknij", check: "Sprawdź", next: "Dalej",
    got_it: "Rozumiem", skip: "Dalej", praise: ["Świetnie!", "Dobrze!", "Tak jest!", "Brawo!", "Znakomicie!"],
    correct_answer: "Poprawna odpowiedź:", think: "Pomyśl:", how_went: "Jak ci poszło?", not_quite: "Nie całkiem", did_it: "Udało się",
    all_matched: "Wszystko dopasowane!", wait: "Zaczekaj, nie odchodź!", lose: "Stracisz postęp w tej lekcji.", keep: "Uczę się dalej",
    quit: "Zakończ", no_hearts: "Skończyły ci się serca", hearts_hint: "Zrób powtórkę, żeby odzyskać serce, albo poczekaj %d min.",
    refill: "Uzupełnij", practice_heart: "Powtórka za serce", leave: "Wyjdź", lesson_done: "Lekcja ukończona!",
    accuracy: "trafność", combo: "z rzędu", streak_days: "Seria: %d dni!", crown_up: "Nowa korona!", unlocked: "Odblokowano dział",
    chat_unlocked: "Odblokowano rozmowę", back_home: "Wróć", chat_done: "Rozmowa ukończona!", back_chats: "Wróć do rozmów",
    again: "Jeszcze raz", tap_tr: "Dotknij wiadomości, żeby zobaczyć tłumaczenie.", pick_answer: "Wybierz odpowiedź", say: "Powiedz:",
    send: "Wyślij", practice_t: "Powtórka", practice_d: "Mieszane ćwiczenia ze słów, które już znasz. Odzyskujesz serce.",
    sound_t: "Trening dźwięków", sound_t_h: "Trening tonów", sound_d: "Samo słuchanie i rozpoznawanie.",
    stats: "Statystyki", level: "Poziom", xp_total: "XP łącznie", best_streak: "Najdłuższa seria", words: "Poznane słowa", lessons: "Lekcje",
    week: "Ostatnie 7 dni", daily_goal: "Cel dzienny", settings: "Ustawienia", pron: "Pokazuj wymowę", sound: "Dźwięki", voice: "Czytaj na głos",
    shop: "Sklep", freeze: "Zamrożenie serii", refill_hearts: "Uzupełnij serca", gems: "klejnoty", reset: "Zeruj postęp w tym kursie",
    reset_q: "Na pewno? Cały postęp tego kursu zniknie.", yes: "Tak", no: "Nie", language: "Język interfejsu",
    welcome: "Witaj w kursie", welcome_d: "Ile chcesz się uczyć każdego dnia?", flag: "Zgłoś błąd", over: "Powtórka dziś nie dała serca",
    placeholder_type: "wpisz odpowiedź…", clear_pad: "Wyczyść", show_guide: "Pokaż wzór", hide_guide: "Ukryj wzór",
    draw_hint: "Porównaj swoje pociągnięcia z czerwonym wzorem. Bądź uczciwy!", listen: "Posłuchaj", play_pitch: "Odtwórz wysokość",
    hum_hint: "Brzęczenie, które idzie za melodią tonu. Bez słowa, sama melodia.", loading: "Ładuję silnik kursów…",
    insight: "Wgląd", new_word: "Nowe słowo", sound_tag: "Wymowa", read: "czytaj", know_pl: "Znasz z polskiego:", remember: "Zapamiętaj",
    insight_note: "Nie ucz się tego na pamięć. Zauważ to, a potem użyj w kolejnych krokach.", offline_ready: "Gotowe do pracy offline.",
    installed: "Dodaj do ekranu głównego, żeby uruchamiać jak aplikację.", err: "Coś poszło nie tak:", retry: "Spróbuj ponownie",
  },
  en: {
    motto: "a school of ancient and faraway languages", learn_in: "I learn in", no_chats: "This course teaches characters only. Practise sentences and conversations in the %s course.", larps: "Larps", larps_d: "Scenes with stakes: you pay an XP entry fee and can lose it.", larp_enter: "Enter", larp_rules: "Entry fee %d XP. Win: +%d XP. Made it despite slips: fee refunded. Fail: you lose the fee. A wrong reply costs a point of patience, and a ☠ question ends the scene at once.", larp_need: "You need %d XP to enter.", larp_goal: "Goal", larp_deadly: "☠ One chance: a wrong reply ends the scene.", larp_weak: "Awkward.", larp_win: "Success!", larp_partial: "You made it, but…", larp_fail: "Failed", larp_quit_t: "Leave the scene?", larp_quit_d: "You will lose the entry fee.", larp_refund: "Entry fee refunded", larp_patience: "Patience", larp_correct: "Correct: ", tonecolor: "Tone colours", script: "Exercise script", size: "Text size", theme: "Theme", th_navy: "Navy", th_sky: "Light", new: "new", xp: "XP",
    foot: "Progress is saved in this browser. Add the page to your home screen to use it like an app.",
    reports: "Reported mistakes: %d", copy: "COPY", clear: "CLEAR", copied: "Copied. Paste the reports into your chat with Claude.",
    rep_title: "Report a mistake in this exercise", rep_hint: "Description (optional)", rep_send: "SAVE", rep_cancel: "CANCEL",
    rep_saved: "Thank you! Report saved.", path: "Path", chats: "Chats", practice: "Practice", profile: "Profile",
    goal_day: "Daily goal", locked: "locked", repeat: "worth a review", start_here: "▸ start here",
    unlock_after: "Unlocks after: ", start_lesson: "Start lesson", close: "Close", check: "Check", next: "Continue",
    got_it: "Got it", skip: "Continue", praise: ["Great!", "Nice!", "That's it!", "Well done!", "Excellent!"],
    correct_answer: "Correct answer:", think: "Think:", how_went: "How did it go?", not_quite: "Not quite", did_it: "I got it",
    all_matched: "All matched!", wait: "Wait, don't go!", lose: "You'll lose your progress in this lesson.", keep: "Keep learning",
    quit: "Quit", no_hearts: "You're out of hearts", hearts_hint: "Do a practice round to earn a heart, or wait %d min.",
    refill: "Refill", practice_heart: "Practice for a heart", leave: "Leave", lesson_done: "Lesson complete!",
    accuracy: "accuracy", combo: "in a row", streak_days: "Streak: %d days!", crown_up: "New crown!", unlocked: "Unlocked unit",
    chat_unlocked: "Unlocked conversation", back_home: "Back", chat_done: "Conversation complete!", back_chats: "Back to chats",
    again: "Again", tap_tr: "Tap a message to see its translation.", pick_answer: "Choose a reply", say: "Say:",
    send: "Send", practice_t: "Practice", practice_d: "Mixed exercises from words you already know. Earns a heart back.",
    sound_t: "Sound training", sound_t_h: "Tone training", sound_d: "Just listening and recognising.",
    stats: "Stats", level: "Level", xp_total: "Total XP", best_streak: "Best streak", words: "Words learned", lessons: "Lessons",
    week: "Last 7 days", daily_goal: "Daily goal", settings: "Settings", pron: "Show pronunciation", sound: "Sounds", voice: "Read aloud",
    shop: "Shop", freeze: "Streak freeze", refill_hearts: "Refill hearts", gems: "gems", reset: "Reset progress in this course",
    reset_q: "Really? All progress in this course will be erased.", yes: "Yes", no: "No", language: "Interface language",
    welcome: "Welcome to", welcome_d: "How much do you want to study each day?", flag: "Report a mistake", over: "",
    placeholder_type: "type your answer…", clear_pad: "Clear", show_guide: "Show guide", hide_guide: "Hide guide",
    draw_hint: "Compare your strokes with the red model. Be honest!", listen: "Listen", play_pitch: "Play pitch",
    hum_hint: "A hum that follows the tone's pitch. No word, just the melody.", loading: "Loading the course engine…",
    insight: "Insight", new_word: "New word", sound_tag: "Pronunciation", read: "read", know_pl: "You know this from English:", remember: "Remember",
    insight_note: "Don't memorise this. Notice it, then use it in the next steps.", offline_ready: "Ready to work offline.",
    installed: "Add it to your home screen to launch it like an app.", err: "Something went wrong:", retry: "Try again",
  },
};
let THEME = store.get("sv_theme", "navy"); if (THEME !== "sky") THEME = "navy";
function setTheme(k) {
  THEME = k; store.set("sv_theme", k); document.documentElement.dataset.theme = k;
  const mt = document.querySelector('meta[name="theme-color"]'); if (mt) mt.content = k === "sky" ? "#D9E7F8" : "#0A1430";
}
setTheme(THEME);
let FS = parseFloat(store.get("sv_fs", "1")); if (![1, 1.2, 1.4].includes(FS)) FS = 1;
function setFs(v) { FS = v; store.set("sv_fs", String(v)); document.documentElement.style.setProperty("--fs", String(v)); }
setFs(FS);
function eyesEl() {   // siedmioro oczu, każde mruga w swoim losowym rytmie
  const pos = [[35, 20], [65, 20], [20, 50], [50, 50], [80, 50], [35, 80], [65, 80]];
  const el = document.createElement("div"); el.className = "emb-svg";
  el.innerHTML = '<svg class="eyes" viewBox="0 0 100 100" aria-hidden="true">' + pos.map(([x, y]) => {
    const d = (3 + Math.random() * 6).toFixed(2), dl = (-Math.random() * 8).toFixed(2);
    return `<g class="eye" style="animation-duration:${d}s;animation-delay:${dl}s"><ellipse cx="${x}" cy="${y}" rx="12.5" ry="15" fill="none" stroke="currentColor" stroke-width="5"/><circle cx="${x}" cy="${y}" r="3.6" fill="currentColor"/></g>`;
  }).join("") + "</svg>";
  return el;
}
function sizeRow(after) {
  return h("div", { class: "size-row" }, t("size"),
    ...[[1, "A"], [1.2, "A+"], [1.4, "A++"]].map(([v, n]) => h("button", { class: "chip" + (v === FS ? " on" : ""), onclick: () => { setFs(v); (after || showHub)(); } }, n)));
}
let LANG = store.get("sv_lang", (navigator.language || "pl").startsWith("pl") ? "pl" : "en");
const t = (k, ...a) => { let s = (TX[LANG][k] ?? k); if (typeof s === "string") a.forEach(v => s = s.replace("%d", v)); return s; };

/* ---------------- statystyki i reklamy (domyślnie wyłączone, patrz config.js) ---------------- */
const CFG = window.SV_CONFIG || {};
function initAnalytics() {
  const a = CFG.analytics; if (!a || !a.domain) return;
  window.plausible = window.plausible || function () { (window.plausible.q = window.plausible.q || []).push(arguments); };
  const sc = document.createElement("script"); sc.defer = true; sc.dataset.domain = a.domain; sc.src = a.src; document.head.append(sc);
}
function track(name, props) { try { if (window.plausible) window.plausible(name, { props: props || {} }); } catch (e) { /* statystyki są opcjonalne */ } }
let adsLoaded = false;
function adSlot(slot) {
  const a = CFG.ads; if (!a || !a.enabled || !slot) return null;
  if (!adsLoaded) { adsLoaded = true; window.adsbygoogle = window.adsbygoogle || []; window.adsbygoogle.requestNonPersonalizedAds = 1;
    const sc = document.createElement("script"); sc.async = true; sc.crossOrigin = "anonymous"; sc.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + a.client; document.head.append(sc); }
  const ins = h("ins", { class: "adsbygoogle", style: "display:block;min-height:90px", "data-ad-client": a.client, "data-ad-slot": slot, "data-ad-format": "auto", "data-full-width-responsive": "true" });
  setTimeout(() => { try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) { /* brak reklamy */ } }, 50);
  return h("div", { class: "adbox" }, h("small", {}, "Reklama"), ins);
}

/* ---------------- Python ---------------- */
let B = null, PY = null, META = [], BYID = {};
const loadedCourses = new Set();
async function ensureCourse(cid) {
  if (loadedCourses.has(cid)) return;
  PY.unpackArchive(await (await fetch("py/" + cid + ".zip")).arrayBuffer(), "zip", { extractDir: "/home/pyodide" });
  loadedCourses.add(cid);
}
const SAVE_PREFIX = "sv:";
function bootMsg(msg, pct) { const m = $("#boot-msg"), f = $("#boot-fill"); if (m) m.textContent = msg; if (f && pct != null) f.style.width = pct + "%"; }
async function initPython() {
  bootMsg(t("loading"), 5);
  const py = await loadPyodide({ indexURL: "pyodide/" }); window.__py = py;
  bootMsg(t("loading"), 55);
  PY = py;
  py.unpackArchive(await (await fetch("py/core.zip")).arrayBuffer(), "zip", { extractDir: "/home/pyodide" });
  const code = await (await fetch("py/bridge.py")).text();
  py.FS.writeFile("/home/pyodide/bridge.py", code);
  py.runPython("import sys; sys.path.insert(0, '/home/pyodide')");
  B = py.pyimport("bridge");
  const tz = new Date().getTimezoneOffset() * 60; // sekundy do dodania do UTC, by dostać czas lokalny
  B.set_env(tz, (cid, js) => store.set(SAVE_PREFIX + cid, js));
  bootMsg(t("loading"), 100);
}
const J = s => JSON.parse(s);

/* ---------------- dźwięk ---------------- */
let actx = null, SOUND_ON = true;
function ac() { if (!actx) { try { actx = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return null; } } if (actx.state === "suspended") actx.resume(); return actx; }
function beep(freqs, dur = 0.12, type = "sine", vol = 0.12, force = false) {
  if (!SOUND_ON && !force) return;
  const c = ac(); if (!c) return;
  let at = c.currentTime;
  for (const f of freqs) {
    const o = c.createOscillator(), g = c.createGain();
    o.type = type; o.frequency.value = f; g.gain.setValueAtTime(vol, at); g.gain.exponentialRampToValueAtTime(0.001, at + dur);
    o.connect(g).connect(c.destination); o.start(at); o.stop(at + dur + 0.02); at += dur * 0.9;
  }
}
const sfx = {
  tap: () => beep([520], 0.05, "triangle", 0.08), correct: () => beep([660, 880], 0.12, "triangle"),
  wrong: () => beep([220, 160], 0.18, "sawtooth", 0.08), streak: () => beep([523, 659, 784, 1047], 0.1, "triangle"),
  done: () => beep([523, 659, 784, 1047, 1319], 0.13, "triangle"),
};
const CONTOURS = {};
function playTone(tone) {
  const c = ac(); if (!c) return;
  if (!Object.keys(CONTOURS).length) Object.assign(CONTOURS, J(B.tone_contours()));
  const pts = CONTOURS[tone], N = 90, dur = 0.75, curve = new Float32Array(N);
  const level = x => { for (let i = 0; i < pts.length - 1; i++) { const [x0, y0] = pts[i], [x1, y1] = pts[i + 1]; if (x >= x0 && x <= x1) { let f = (x - x0) / (x1 - x0); f = f * f * (3 - 2 * f); return y0 + (y1 - y0) * f; } } return pts[pts.length - 1][1]; };
  for (let i = 0; i < N; i++) curve[i] = 110 * Math.pow(2, (level(i / (N - 1)) - 1) / 4);
  const o = c.createOscillator(), g = c.createGain(), now = c.currentTime;
  o.type = "triangle"; o.frequency.setValueCurveAtTime(curve, now, dur);
  g.gain.setValueAtTime(0.0001, now); g.gain.linearRampToValueAtTime(0.25, now + 0.05); g.gain.setValueAtTime(0.25, now + dur - 0.08); g.gain.linearRampToValueAtTime(0.0001, now + dur);
  o.connect(g).connect(c.destination); o.start(now); o.stop(now + dur + 0.02);
}
const voiceOn = () => store.get("sv_voice", "1") === "1";
function speak(text, auto) {
  const m = BYID[cur.cid]; if (!m || !m.tts || !text) return;
  text = String(text).replace(/\u0301/g, "");   // znak akcentu (rosyjski) nie jest do czytania
  if (window.AndroidTTS) { if (auto === true && !voiceOn()) return; try { AndroidTTS.speak(String(text), m.tts, 0.85); } catch (e) { /* brak głosu */ } return; }
  if (!window.speechSynthesis) return;
  if (auto === true && !voiceOn()) return;
  try { speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(text); u.lang = m.tts; u.rate = 0.85; speechSynthesis.speak(u); } catch (e) { /* brak głosu */ }
}
const canSpeak = () => !!((window.speechSynthesis || window.AndroidTTS) && BYID[cur.cid] && BYID[cur.cid].tts);

/* ---------------- UI pomocnicze ---------------- */
function put(parent, ...kids) { parent.append(...kids.flat().filter(k => k != null && k !== false)); }
const app = () => $("#app");
const cur = { cid: null, home: null, tab: "path", L: null };
function show(node, cls = "") { const a = app(); $("#modal-root").replaceChildren(); a.replaceChildren(h("div", { class: "screen " + cls }, node)); return a.firstChild; }
function toast(msg, ms = 1800) { const el = $("#toast"); el.className = "toast show"; el.textContent = msg; clearTimeout(toast._t); toast._t = setTimeout(() => el.className = "toast", ms); }
function sheet(content, { mid = false } = {}) {
  const bg = h("div", { class: "sheet-bg" + (mid ? " mid" : ""), onclick: e => { if (e.target === bg) close(); } });
  const sh = h("div", { class: "sheet course" + (mid ? " mid" : ""), style: themeStyle() }, content);
  bg.append(sh); $("#modal-root").append(bg);
  const close = () => bg.remove();
  return close;
}
function themeStyle() { const m = BYID[cur.cid]; return m ? `--cfont:${cfont(m)}` : ""; }
function cfont(m) { return `"F-${m.id}","F-${m.id}-x","Sviet",Georgia,serif`; }
function confirmBox(title, text, yes, no, onYes, onNo) {
  const close = sheet([h("h3", {}, title), h("p", {}, text),
    h("button", { class: "btn green", onclick: () => { close(); onNo && onNo(); } }, no),
    h("button", { class: "btn ghost", onclick: () => { close(); onYes && onYes(); } }, yes)], { mid: true });
}
function persistReports() { return J(store.get("sv_reports", "[]")); }
function reportDialog(data) {
  const ta = h("textarea", { class: "input", placeholder: t("rep_hint") });
  const close = sheet([h("h3", {}, t("rep_title")), ta,
    h("div", { class: "row" }, h("button", { class: "btn ghost", onclick: () => close() }, t("rep_cancel")),
      h("button", { class: "btn", onclick: () => {
        const r = persistReports(); const d = Object.assign({}, data, { kurs: cur.cid, jezyk: LANG, czas: new Date().toISOString() });
        if (ta.value.trim()) d.opis = ta.value.trim(); r.push(d); store.set("sv_reports", JSON.stringify(r)); close(); toast(t("rep_saved"));
      } }, t("rep_send")))], { mid: true });
}
const rtl = () => (cur.cid === "abba");

/* ---------------- ekran główny (arka) ---------------- */
function showHub() {
  cur.cid = null; document.body.classList.remove("rtl-course"); SOUND_ON = true;
  const cards = META.map(m => {
    const pr = J(B.course_progress(m.id, store.get(SAVE_PREFIX + m.id, "")));
    const info = pr.xp ? `${pr.xp} ${t("xp")} · ${"●".repeat(Math.min(pr.crowns, 5))}${pr.crowns > 5 ? "+" + (pr.crowns - 5) : ""}` : t("new");
    return h("button", { class: "cc", onclick: () => enterCourse(m.id) },
      h("div", { class: "gl", style: `background:${m.paper};color:${m.accent};font-family:"F-${m.id}-x","F-${m.id}",serif` }, m.glyph),
      h("div", {}, h("div", { class: "nm", style: `font-family:"F-${m.id}-x","F-${m.id}",serif`, dir: "auto" }, m.native),
        h("div", { class: "sb" }, m.sub[LANG]), h("div", { class: "pr" }, info)));
  });
  const reps = persistReports();
  show(h("div", { class: "scroll hubscroll" },
    h("div", { class: "hub-head" }, eyesEl(), h("h1", {}, "Śviętovit"), h("p", {}, t("motto"))),
    h("div", { class: "theme-row" }, t("theme"),
      ...[["navy", t("th_navy")], ["sky", t("th_sky")]].map(([k, n]) => h("button", { class: "chip" + (k === THEME ? " on" : ""), onclick: () => { setTheme(k); showHub(); } }, n))),
    sizeRow(),
    h("div", { class: "langs" }, t("learn_in"),
      ...["pl", "en"].map(l => h("button", { class: "chip" + (l === LANG ? " on" : ""), onclick: () => { LANG = l; store.set("sv_lang", l); showHub(); } }, l.toUpperCase()))),
    ...cards, adSlot(CFG.ads && CFG.ads.slotHome), h("div", { class: "hub-foot" }, t("foot")),
    reps.length ? h("div", { class: "rep-box" }, t("reports").replace("%d", reps.length),
      h("div", {}, h("button", { onclick: async () => { const txt = "Śviętovit: zgłoszone błędy (" + reps.length + ")\n" + reps.map((r, i) => "#" + (i + 1) + " " + JSON.stringify(r)).join("\n"); try { await navigator.clipboard.writeText(txt); toast(t("copied")); } catch (e) { prompt("", txt); } } }, t("copy")),
        h("button", { onclick: () => { store.set("sv_reports", "[]"); showHub(); } }, t("clear")))) : null));
}

/* ---------------- kurs ---------------- */
async function enterCourse(cid) {
  if (!loadedCourses.has(cid)) { const m = BYID[cid]; show(h("div", { class: "boot", style: "color:" + m.accent }, h("div", { class: "boot-glyph", dir: "auto" }, m.glyph), h("div", {}, m.native))); try { await ensureCourse(cid); } catch (e) { toast(t("err") + " " + e); return showHub(); } }
  track("course_open", { course: cid });
  cur.cid = cid; cur.tab = "path";
  B.open_course(cid, LANG, store.get(SAVE_PREFIX + cid, ""));
  document.body.classList.toggle("rtl-course", rtl());
  refreshHome();
  SOUND_ON = cur.home.settings.sound !== false;
  if (!cur.home.onboarded) return showWelcome();
  renderHome();
}
function refreshHome() { cur.home = J(B.home()); }
function topbar() {
  const H = cur.home, m = BYID[cur.cid];
  return h("div", { class: "top" },
    h("button", { class: "back", onclick: showHub, "aria-label": "back" }, "‹"),
    h("div", { class: "ttl", dir: "auto" }, m.native),
    h("span", { class: "stat s-streak" }, "☀ " + H.streak), h("span", { class: "stat s-gem" }, "◆ " + H.gems), h("span", { class: "stat s-heart" }, "♥ " + H.hearts));
}
function navbar() {
  const items = [["path", "◉", t("path")], ["chats", "✉", t("chats")], ["practice", "↻", t("practice")], ["profile", "☺", t("profile")]];
  return h("div", { class: "nav" }, items.map(([k, ic, lb]) => h("button", { class: cur.tab === k ? "on" : "", onclick: () => { cur.tab = k; renderHome(); } }, h("b", {}, ic), lb)));
}
function renderHome() {
  refreshHome();
  const H = cur.home, m = BYID[cur.cid];
  const body = { path: pathTab, chats: chatsTab, practice: practiceTab, profile: profileTab }[cur.tab]();
  const goal = h("div", { class: "goal" }, `${t("goal_day")}  ${Math.min(H.xp_today, H.goal)}/${H.goal} XP`, h("div", { class: "bar" }, h("i", { style: `width:${Math.min(100, 100 * H.xp_today / H.goal)}%` })));
  const scr = show([topbar(), goal, h("div", { class: "scroll", id: "tabbody" }, body), navbar()], "course");
  scr.style.cssText = themeStyle();
}
function pathTab() {
  const H = cur.home, out = [];
  H.units.forEach((u, i) => {
    if (i === 0 || u.track !== H.units[i - 1].track) {
      out.push(h("div", { class: "track" }, "· " + (H.tracks[u.track] || "") + " ·", !u.unlocked ? h("small", {}, t("unlock_after") + u.reason) : null));
    }
    const marks = "●".repeat(u.crowns) + "○".repeat(H.max_crowns - u.crowns);
    out.push(h("button", { class: "unit" + (u.unlocked ? "" : " locked"), onclick: () => u.unlocked && unitSheet(u) },
      h("div", { class: "node" }, u.icon || (u.i + 1)),
      h("div", {}, h("div", { class: "nm", dir: "auto" }, u.title), h("div", { class: "cr" }, u.unlocked ? marks : t("locked")),
        u.cracked ? h("div", { class: "hint warn" }, t("repeat")) : (u.i === H.current ? h("div", { class: "hint" }, t("start_here")) : null))));
  });
  return out;
}
function unitSheet(u) {
  const close = sheet([h("h3", { dir: "auto" }, u.title), h("p", {}, "●".repeat(u.crowns) + "○".repeat(cur.home.max_crowns - u.crowns)),
    h("button", { class: "btn", onclick: () => { close(); startSession("lesson", u.i); } }, t("start_lesson")),
    h("button", { class: "btn ghost", onclick: () => close() }, t("close"))]);
}
function practiceTab() {
  const H = cur.home;
  const out = [h("div", { class: "card" }, h("h4", {}, t("practice_t")), h("p", {}, t("practice_d")), h("button", { class: "btn green", onclick: () => startSession("practice") }, t("practice_t")))];
  if (H.has_sounds) out.push(h("div", { class: "card" }, h("h4", {}, H.hanzi ? t("sound_t_h") : t("sound_t")), h("p", {}, t("sound_d")), h("button", { class: "btn blue", onclick: () => startSession("sound") }, H.hanzi ? t("sound_t_h") : t("sound_t"))));
  return out;
}
function profileTab() {
  const H = cur.home;
  const mx = Math.max(1, ...H.week.map(w => w[1]));
  const tog = (key, label) => h("div", { class: "sw", onclick: () => { B.set_setting(key, !H.settings[key]); if (key === "sound") SOUND_ON = !H.settings[key]; renderHome(); } }, label, h("div", { class: "tg" + (H.settings[key] !== false ? " on" : "") }));
  return [
    h("div", { class: "card" }, sizeRow(renderHome)),
    cur.cid === "serbian" ? h("div", { class: "card" }, h("div", { class: "size-row" }, t("script"),
      ...[[false, "Latinica"], [true, "Ћирилица"]].map(([v, n]) => h("button", { class: "chip" + (!!H.settings.cyr === v ? " on" : ""), onclick: () => {
        B.set_setting("cyr", v); B.open_course(cur.cid, LANG, store.get(SAVE_PREFIX + cur.cid, "")); renderHome(); } }, n)))) : null,
    h("div", { class: "card" }, h("h4", {}, t("stats")),
      [[t("level"), `${H.level}  (${H.level_xp}/${H.level_need})`], [t("xp_total"), H.xp_total], [t("best_streak"), H.longest], [t("words"), `${H.words_learned}/${H.words_total}`], [t("lessons"), H.lessons_completed]]
        .map(([a, b]) => h("div", { class: "kv" }, h("span", {}, a), h("b", {}, b)))),
    h("div", { class: "card" }, h("h4", {}, t("week")), h("div", { class: "week" }, H.week.map(([d, v]) => h("div", {}, h("i", { style: `height:${Math.round(70 * v / mx)}px` }), d)))),
    h("div", { class: "card" }, h("h4", {}, t("daily_goal")), h("div", { class: "grid2" }, H.goals.map(([n, v]) => h("button", { class: "btn" + (v === H.goal ? "" : " ghost"), onclick: () => { B.set_goal(v); renderHome(); } }, `${v} XP`)))),
    h("div", { class: "card" }, h("h4", {}, t("settings")), tog("pron", t("pron")), tog("sound", t("sound")),
      TONE_COURSES.includes(cur.cid) ? tog("tonecolor", t("tonecolor")) : null,
      TONE_COURSES.includes(cur.cid) && H.settings.tonecolor !== false ? h("div", { class: "tone-legend" }, ...[[1, "ā"], [2, "á"], [3, "ǎ"], [4, "à"], [5, "a"]].map(([n, s]) => h("span", { class: "tn t" + n }, (n < 5 ? n + " " : "· ") + s))) : null,
      h("div", { class: "sw", onclick: () => { store.set("sv_voice", voiceOn() ? "0" : "1"); renderHome(); } }, t("voice"), h("div", { class: "tg" + (voiceOn() ? " on" : "") }))),
    h("div", { class: "card" }, h("h4", {}, t("shop")),
      h("button", { class: "btn blue", disabled: H.gems < H.freeze_cost || H.freezes >= H.max_freezes, onclick: () => { if (B.buy("freeze")) { toast("✓"); renderHome(); } } }, `${t("freeze")} (${H.freezes}/${H.max_freezes}) ◆ ${H.freeze_cost}`),
      h("div", { style: "height:8px" }),
      h("button", { class: "btn blue", disabled: H.gems < H.refill_cost || H.hearts >= H.heart_max, onclick: () => { if (B.buy("refill")) { toast("✓"); renderHome(); } } }, `${t("refill_hearts")} ◆ ${H.refill_cost}`)),
    h("button", { class: "btn ghost", onclick: () => confirmBox(t("reset"), t("reset_q"), t("yes"), t("no"), () => { B.reset_progress(); enterCourse(cur.cid); }) }, t("reset")),
  ];
}

/* ---------------- powitanie ---------------- */
function showWelcome() {
  const H = cur.home, m = BYID[cur.cid];
  const scr = show(h("div", { class: "scroll res" },
    h("div", { class: "big", style: `color:${m.accent}`, dir: "auto" }, m.glyph),
    h("h2", {}, t("welcome") + " " + m.native), h("p", {}, t("welcome_d")),
    ...H.goals.map(([n, v]) => h("button", { class: "btn", onclick: () => { B.onboard(v); renderHome(); } }, `${n} · ${v} XP`))), "course");
  scr.style.cssText = themeStyle();
}

/* ---------------- rozmowy ---------------- */
function chatsTab() {
  const H = cur.home;
  const cols = ["#B3261E", "#2A6FB0", "#4F8A3A", "#8C3B9E", "#D26A12", "#1F7A78"];
  const larps = (H.larps || []).length ? [h("div", { class: "track", style: "margin-top:22px" }, "· " + t("larps") + " ·", h("small", {}, t("larps_d"))),
    ...H.larps.map(l => h("button", { class: "chat-item larp-item" + (l.unlocked ? "" : " locked"), onclick: () => l.unlocked && larpSheet(l) },
      h("div", { class: "av", style: "background:#7A2E5E" }, l.avatar),
      h("div", {}, h("div", { class: "t" }, l.title), h("div", { class: "s" }, l.partner + " · −" + l.fee + " XP")),
      h("div", { class: "stars" }, l.best === 2 ? "★" : l.best === 1 ? "◐" : l.best === 0 ? "✕" : "")))] : [];
  if (!H.chats.length && !larps.length) return [h("div", { class: "card" }, h("p", { style: "margin:0" }, t("no_chats").replace("%s", { han: "中文", kana: "日本語" }[cur.cid] || "")))];
  return [...H.chats.map((c, i) => h("button", { class: "chat-item" + (c.unlocked ? "" : " locked"), onclick: () => c.unlocked && openChat(c.id, i) },
    h("div", { class: "av", style: `background:${cols[i % cols.length]}` }, c.avatar),
    h("div", {}, h("div", { class: "t" }, c.partner), h("div", { class: "s" }, c.title)),
    h("div", { class: "stars" }, "★".repeat(c.stars) + "☆".repeat(3 - c.stars)))), ...larps];
}
function openChat(cid, idx) {
  const chat = J(B.chat_get(cid)), color = ["#B3261E", "#2A6FB0", "#4F8A3A", "#8C3B9E", "#D26A12", "#1F7A78"][idx % 6];
  let turn = 0, mistakes = 0, attempts = 0, excluded = new Set();
  const log = h("div", { class: "log" }), reply = h("div", { class: "reply" });
  const scr = show([h("div", { class: "top" }, h("button", { class: "back", onclick: renderHome }, "‹"), h("div", { class: "av", style: `background:${color};width:38px;height:38px;font-size:calc(19px*var(--k))` }, chat.avatar), h("div", { class: "ttl" }, chat.partner)), log, reply], "course");
  scr.style.cssText = themeStyle();
  const toBottom = () => setTimeout(() => log.scrollTo({ top: log.scrollHeight, behavior: "smooth" }), 30);
  const bubble = (text, sub, en, mine, wrong) => {
    const b = h("div", { class: "msg" + (mine ? " me" : "") + (wrong ? " wrong" : ""), dir: "auto", onclick: () => b.classList.toggle("open") }, text, sub ? h("small", {}, sub) : null, en ? h("div", { class: "en" }, en) : null);
    log.append(b); toBottom(); return b;
  };
  const note = (txt) => { log.append(h("div", { class: "note" }, txt)); toBottom(); };
  note(t("tap_tr"));
  const botTurn = () => {
    if (turn >= chat.turns.length) return finish();
    const tr = chat.turns[turn]; reply.replaceChildren();
    const typing = h("div", { class: "msg" }, "…"); log.append(typing); toBottom();
    setTimeout(() => { typing.remove(); bubble(tr.bot_text, tr.bot_sub, tr.en); if (tr.note) note(tr.note); attempts = 0; showReply(tr); speak(tr.bot_text, true); }, 500 + 60 * tr.bot.length);
  };
  const showReply = (tr) => {
    reply.replaceChildren();
    if (tr.options) {
      reply.append(h("div", { class: "sub", style: "text-align:left" }, t("pick_answer")));
      const opts = tr.options.filter(o => !excluded.has(o.text)).sort(() => Math.random() - 0.5);
      opts.forEach(o => reply.append(h("button", { class: "opt", dir: "auto", onclick: () => {
        speak(o.text, true); bubble(o.text, o.sub, null, true, !o.ok); reply.replaceChildren();
        if (o.ok) { sfx.correct(); excluded = new Set(); turn++; setTimeout(botTurn, 450); }
        else { sfx.wrong(); mistakes++; confused(o.why); excluded.add(o.text); setTimeout(() => showReply(tr), 900); }
      } }, o.text, h("small", {}, o.sub))));
    } else {
      const bd = tr.build, picked = [];
      const ans = h("div", { class: "tiles answer", style: "background:var(--white);border-radius:12px;padding:8px;min-height:60px" }), bank = h("div", { class: "tiles" });
      const send = h("button", { class: "btn", disabled: true }, t("send"));
      const render = () => {
        ans.replaceChildren(...picked.map(p => tile(p, () => { picked.splice(picked.indexOf(p), 1); render(); })));
        bank.replaceChildren(...bd.bank.filter(b => !picked.includes(b)).map(b => tile(b, () => { picked.push(b); render(); })));
        send.disabled = !picked.length;
      };
      send.onclick = () => {
        const given = picked.map(p => p.v), r = J(B.chat_check(cid, turn, given));
        bubble(r.text || given.join(" "), r.sub, null, true, !r.ok); reply.replaceChildren();
        if (r.ok) { sfx.correct(); turn++; setTimeout(botTurn, 450); }
        else { sfx.wrong(); mistakes++; attempts++; let w = r.why || ""; if (attempts >= 2) w += "\n" + bd.text; confused(w); setTimeout(() => showReply(tr), 900); }
      };
      reply.append(h("div", {}, h("b", {}, t("say") + " "), `„${bd.prompt}”`), ans, bank, send); render();
    }
  };
  const confused = (why) => { bubble("?"); if (why) note(t("think") + " " + why); };
  const finish = () => {
    const ev = J(B.chat_finish(cid, mistakes)); sfx.done(); track("chat_done", { course: cur.cid }); reply.replaceChildren();
    log.append(h("div", { class: "card", style: "text-align:center;background:var(--yelll)" }, h("b", {}, t("chat_done")), h("div", { style: "font-size:calc(30px*var(--k));color:#83611F" }, "★".repeat(ev.stars) + "☆".repeat(3 - ev.stars)),
      `+${ev.xp} XP · ◆ +${ev.gems}` + (ev.had_full ? "" : " · ♥ +1"), ev.streak_extended ? h("div", { style: "color:#9E2B25;font-weight:700" }, "☀ " + t("streak_days", ev.streak)) : null)); toBottom();
    reply.append(h("button", { class: "btn", onclick: () => { cur.tab = "chats"; renderHome(); } }, t("back_chats")), h("button", { class: "btn ghost", onclick: () => openChat(cid, idx) }, t("again")));
  };
  botTurn();
}
function tile(tk, onclick) { return h("button", { class: "tile", dir: "auto", onclick: () => { sfx.tap(); onclick(); } }, tk.v, tk.sub && cur.home.settings.pron !== false ? h("small", {}, tk.sub) : null); }

/* ---------------- lekcja ---------------- */
function startSession(kind, unit) {
  track("lesson_start", { course: cur.cid, kind });
  B.start(kind, unit == null ? -1 : unit);
  const L = cur.L = { kind, phase: "answer", ready: false, getPayload: null, lastOk: null, ex: null };
  const bar = h("i", { style: "width:0" }), combo = h("div", { class: "combo" }), hearts = h("span", { class: "stat s-heart" });
  L.bar = bar; L.combo = combo; L.hearts = hearts;
  L.body = h("div", { class: "lbody" }); L.foot = h("div", { class: "lfoot" });
  L.main = h("button", { class: "btn", onclick: pressMain }, t("check"));
  const scr = show([h("div", { class: "lhead" },
    h("button", { class: "x", onclick: () => confirmBox(t("wait"), t("lose"), t("quit"), t("keep"), () => { track("lesson_abandon", { course: cur.cid, kind: L.kind }); B.abandon(); renderHome(); }) }, "✕"),
    h("div", { class: "bar" }, bar), hearts,
    h("button", { class: "x", style: "font-size:calc(20px*var(--k))", title: t("flag"), onclick: () => reportDialog({ cwiczenie: L.ex }) }, "⚑")), combo, L.body, L.foot], "course");
  scr.style.cssText = themeStyle();
  showCurrent();
}
function updateHeader(c) {
  const L = cur.L; L.bar.style.width = (100 * c.progress) + "%";
  L.combo.textContent = c.combo >= 3 ? "☀ " + c.combo + " " + t("combo") : "";
  L.hearts.textContent = c.use_hearts ? "♥ " + c.hearts : "";
}
function showCurrent() {
  const L = cur.L, c = J(B.current());
  if (c.finished) return finishSession();
  L.ex = c.ex; L.phase = "answer"; L.ready = false; L.getPayload = null; updateHeader(c);
  L.body.replaceChildren(); L.foot.className = "lfoot"; L.foot.replaceChildren(L.main);
  const graded = !["intro", "insight"].includes(c.ex.type);
  L.main.className = "btn"; L.main.textContent = graded ? t("check") : (c.ex.type === "insight" ? t("got_it") : t("skip"));
  setReady(!graded);
  if (c.ex.title && !["intro", "insight"].includes(c.ex.type)) put(L.body, h("div", { class: "ptitle" }, c.ex.title));
  const fn = RENDER[c.ex.type] || RENDER.unknown;
  fn(c.ex, L);
  L.body.scrollTop = 0;
}
function setReady(v) { cur.L.ready = v; cur.L.main.disabled = !v; }
const hookEl = (txt) => txt ? h("div", { class: "hook", dir: "auto" }, h("b", {}, t("remember")), txt) : null;
const speakBtn = (txt) => canSpeak() ? h("button", { class: "btn ghost", style: "width:auto;margin:0 auto;padding:8px 18px", onclick: () => speak(txt) }, "🔊 " + t("listen")) : null;

const SPEAK_OPT = new Set(["form", "hanzi", "listen"]);
const AUTO_PROMPT = new Set(["meaning", "reading", "sentence", "cognate"]);
const RENDER = {
  intro(ex, L) {
    const pron = cur.home.settings.pron !== false;
    put(L.body, h("div", { class: "tag" }, ex.letter ? t("sound_tag") : t("new_word")),
      h("div", { class: "card", style: "text-align:center" },
        h("div", { class: ex.letter ? "big" : "mid2", dir: "auto" }, ex.form),
        !ex.letter && pron && ex.tr ? h("div", { class: "sub", style: "font-style:italic" }, t("read") + ": " + ex.tr) : null,
        h("div", { style: "font-size:calc(19px*var(--k));margin-top:6px", dir: "auto" }, ex.meaning)),
      speakBtn(ex.audio || ex.form),
      ex.cog ? h("div", { class: "cog" }, h("b", {}, t("know_pl") + " "), ex.cog) : null, hookEl(ex.hook));
    setTimeout(() => speak(ex.audio || ex.form, true), 200);
  },
  insight(ex, L) {
    put(L.body, h("div", { class: "insight" }, h("div", { class: "tag" }, t("insight")), h("h2", {}, ex.title), ex.text), h("div", { class: "sub", style: "font-size:calc(13px*var(--k))" }, t("insight_note")));
  },
  choice(ex, L) {
    const m = ex.mode, state = { v: null };
    if (m === "listen") put(L.body, h("div", { style: "text-align:center" }, h("button", { class: "btn blue", style: "width:auto;display:inline-block;padding:14px 28px", onclick: () => speak(ex.audio) }, "🔊 " + t("listen"))));
    else if (m === "sentence") put(L.body, h("div", { class: "sentence", dir: "auto", onclick: () => speak(ex.audio || ex.sentence) }, ex.sentence), h("div", { class: "sub", style: "text-align:left;font-style:italic" }, ex.sentence_sub));
    else if (m === "form" || m === "hanzi") put(L.body, h("div", { class: "bubble", style: "text-align:center" }, `„${ex.prompt}”`));
    else if (m === "cloze") put(L.body, h("div", { class: "mid2", style: "font-size:calc(36px*var(--k))", dir: "auto" }, ex.prompt), ex.prompt_sub ? h("div", { class: "sub g" }, ex.prompt_sub) : null);
    else {
      const big = ex.word_view && ex.word_view.letter;
      put(L.body, h("div", { class: big ? "big" : "mid2", dir: "auto", onclick: () => speak(ex.audio || ex.prompt) }, ex.prompt),
        ex.prompt_sub ? h("div", { class: "sub", style: "font-style:italic" }, ex.prompt_sub) : null,
        m === "meaning" && ex.word_view && !ex.word_view.letter && !ex.prompt_sub && cur.home.settings.pron !== false && ex.word_view.tr ? h("div", { class: "sub", style: "font-style:italic" }, ex.word_view.tr) : null);
    }
    const oldStyle = ["form", "cloze", "hanzi", "listen"].includes(m);
    const long = !oldStyle && ex.options.some(o => String(o).length > 12);
    const grid = h("div", { class: "opts" + (long ? " one" : "") });
    const btns = ex.options.map((o, k) => {
      const b = h("button", { class: "opt" + (oldStyle ? " big2" : ""), dir: "auto", onclick: () => {
        if (L.phase !== "answer") return; sfx.tap(); if (SPEAK_OPT.has(m) || (m === "reading" && ["kaszeby", "ave"].includes(cur.cid))) speak(o, true);
        btns.forEach(x => x.classList.remove("sel")); b.classList.add("sel"); state.v = o; setReady(true);
      } }, m === "cloze" ? "-" + o : o, ex.option_subs ? h("small", {}, ex.option_subs[k]) : null);
      b._v = o; return b;
    });
    grid.append(...btns); put(L.body, grid);
    L.getPayload = () => ({ value: state.v });
    L.afterCheck = (r) => btns.forEach(b => { b.disabled = true; if (b._v === r.answer) b.classList.add("ok"); else if (b._v === state.v) { b.classList.remove("sel"); b.classList.add("no"); } });
    if (ex.autoplay || m === "listen") setTimeout(() => speak(ex.audio, true), 250);
    else if (AUTO_PROMPT.has(m)) setTimeout(() => speak(ex.audio || (m === "sentence" ? ex.sentence : ex.prompt), true), 250);
  },
  tone(ex, L) {
    const state = { v: null };
    if (ex.hum) { put(L.body, h("div", { style: "text-align:center" }, h("button", { class: "btn blue", style: "width:auto;display:inline-block;padding:14px 28px", onclick: () => playTone(ex.hum) }, "▶ " + t("play_pitch"))), h("div", { class: "sub", style: "font-size:calc(14px*var(--k))" }, t("hum_hint"))); setTimeout(() => playTone(ex.hum), 350); }
    else { put(L.body, h("div", { class: "big", style: "font-size:calc(72px*var(--k))", onclick: () => speak(ex.prompt) }, ex.prompt), h("div", { class: "sub", style: "font-size:calc(24px*var(--k))" }, ex.prompt_sub), speakBtn(ex.prompt), ex.meaning ? h("div", { class: "sub", style: "font-size:calc(14px*var(--k))" }, "(" + ex.meaning + ")") : null); setTimeout(() => speak(ex.prompt, true), 250); }
    const btns = [1, 2, 3, 4].map(n => { const b = h("button", { class: "opt tone-btn", onclick: () => { if (L.phase !== "answer") return; playTone(n); btns.forEach(x => x.classList.remove("sel")); b.classList.add("sel"); state.v = n; setReady(true); } }, contourSvg([n], 56), h("b", {}, String(n))); b._v = n; return b; });
    put(L.body, h("div", { class: "opts" }, btns));
    L.getPayload = () => ({ value: state.v });
    L.afterCheck = () => btns.forEach(b => { b.disabled = true; if (b._v === Number(ex.answerTone ?? L.answerTone)) b.classList.add("ok"); else if (b._v === state.v) { b.classList.remove("sel"); b.classList.add("no"); } });
  },
  tone_pair(ex, L) {
    const state = { v: null };
    put(L.body, h("div", { class: "big", style: "font-size:calc(64px*var(--k))", onclick: () => speak(ex.prompt) }, ex.prompt), h("div", { class: "sub", style: "font-size:calc(22px*var(--k))" }, ex.prompt_sub), speakBtn(ex.prompt), ex.meaning ? h("div", { class: "sub", style: "font-size:calc(14px*var(--k))" }, "(" + ex.meaning + ")") : null);
    setTimeout(() => speak(ex.prompt, true), 250);
    const btns = ex.options.map(p => { const b = h("button", { class: "opt tone-btn", onclick: () => { if (L.phase !== "answer") return; sfx.tap(); btns.forEach(x => x.classList.remove("sel")); b.classList.add("sel"); state.v = p; setReady(true); } }, contourSvg(p, 56), h("b", {}, p.join(" + "))); b._v = p; return b; });
    put(L.body, h("div", { class: "opts" }, btns));
    L.getPayload = () => ({ value: state.v });
    L.afterCheck = (r) => btns.forEach(b => { b.disabled = true; if (JSON.stringify(b._v) === JSON.stringify(r.answer_pair)) b.classList.add("ok"); else if (b._v === state.v) { b.classList.remove("sel"); b.classList.add("no"); } });
  },
  match(ex, L) {
    const left = ex.pairs.map(p => p[0]).sort(() => Math.random() - 0.5), right = ex.pairs.map(p => p[1]).sort(() => Math.random() - 0.5);
    const ans = Object.fromEntries(ex.pairs), sel = { l: null, r: null }; let matched = 0, mistakes = 0;
    const mk = (v, side) => { const b = h("button", { class: "opt", dir: "auto", style: side === "l" ? "font-size:calc(24px*var(--k))" : "font-size:calc(15px*var(--k))", onclick: () => pick(b) }, v); b._v = v; b._s = side; return b; };
    const lb = left.map(v => mk(v, "l")), rb = right.map(v => mk(v, "r"));
    const grid = h("div", { class: "match" }); lb.forEach((b, i) => grid.append(b, rb[i])); put(L.body, grid);
    const pick = (b) => {
      if (b._done || L.phase !== "answer") return; sfx.tap();
      if (sel[b._s]) sel[b._s].classList.remove("sel"); sel[b._s] = b; b.classList.add("sel");
      if (sel.l && sel.r) {
        const l = sel.l, r = sel.r; sel.l = sel.r = null;
        if (ans[l._v] === r._v) { [l, r].forEach(x => { x._done = true; x.classList.remove("sel"); x.classList.add("ok"); setTimeout(() => { x.classList.remove("ok"); x.classList.add("done"); }, 350); }); matched++;
          if (matched === ex.pairs.length) setTimeout(() => autoComplete(mistakes === 0), 500); }
        else { mistakes++; sfx.wrong(); [l, r].forEach(x => { x.classList.remove("sel"); x.classList.add("no"); setTimeout(() => x.classList.remove("no"), 500); }); }
      }
    };
    L.main.textContent = t("next");
  },
  build(ex, L) {
    put(L.body, h("div", { class: "bubble", dir: "auto" }, `„${ex.prompt}”`), ex.think ? h("div", { class: "think" }, h("b", {}, t("think") + " "), ex.think) : null);
    const picked = [], ans = h("div", { class: "tiles answer" }), bank = h("div", { class: "tiles" });
    const render = () => {
      ans.replaceChildren(...picked.map(p => tile(p, () => { if (L.phase !== "answer") return; picked.splice(picked.indexOf(p), 1); render(); })));
      bank.replaceChildren(...ex.bank.map(b => picked.includes(b) ? h("div", { class: "tile ghost" }, b.v) : tile(b, () => { if (L.phase !== "answer") return; picked.push(b); render(); })));
      setReady(picked.length > 0);
    };
    put(L.body, ans, bank); render();
    L.getPayload = () => ({ tokens: picked.map(p => p.v) });
    L.afterCheck = (r) => { if (r.ok) { const sep = ["hanzi_hero", "han", "kana", "nihon"].includes(cur.cid) ? "" : " "; speak(ex.audio || picked.map(p => p.v).join(sep), true); } };
  },
  type(ex, L) {
    put(L.body, h("div", { class: "mid2", style: "font-size:calc(34px*var(--k))", dir: "auto", onclick: () => speak(ex.prompt) }, `„${ex.prompt}”`), ex.prompt_sub ? h("div", { class: "sub g" }, ex.prompt_sub) : null);
    const inp = h("input", { class: "input", placeholder: t("placeholder_type"), autocomplete: "off", autocapitalize: "off", spellcheck: "false", dir: "auto", oninput: () => setReady(inp.value.trim().length > 0), onkeydown: e => { if (e.key === "Enter") pressMain(); } });
    put(L.body, inp); setTimeout(() => inp.focus(), 300);
    L.getPayload = () => ({ text: inp.value });
    L.afterCheck = () => { inp.readOnly = true; };
  },
  draw(ex, L) {
    put(L.body, h("div", {}, h("b", {}, ex.prompt), ex.prompt_sub ? " · " + ex.prompt_sub : "", ex.hook ? h("div", { class: "hook", style: "margin-top:8px" }, ex.hook) : null));
    const cv = h("canvas", { class: "pad", width: 680, height: 680 }), ctx = cv.getContext("2d"), strokes = []; let guide = false, reveal = false, drawing = null;
    const fam = getComputedStyle(document.querySelector(".screen")).getPropertyValue("--cfont") || "serif";
    const paint = () => {
      ctx.clearRect(0, 0, 680, 680); ctx.strokeStyle = "#e6e0d3"; ctx.lineWidth = 2; ctx.setLineDash([10, 10]);
      ctx.beginPath(); ctx.moveTo(340, 0); ctx.lineTo(340, 680); ctx.moveTo(0, 340); ctx.lineTo(680, 340); ctx.stroke(); ctx.setLineDash([]);
      if (guide || reveal) { ctx.font = `560px ${fam}`; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = reveal ? "rgba(200,40,40,.45)" : "rgba(0,0,0,.12)"; ctx.fillText(ex.glyph, 340, 360); }
      ctx.strokeStyle = "#222"; ctx.lineWidth = 16; ctx.lineCap = ctx.lineJoin = "round";
      strokes.forEach(s => { ctx.beginPath(); s.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)); if (s.length === 1) ctx.lineTo(s[0][0] + .1, s[0][1]); ctx.stroke(); });
    };
    const pos = e => { const r = cv.getBoundingClientRect(); return [(e.clientX - r.left) * 680 / r.width, (e.clientY - r.top) * 680 / r.height]; };
    cv.addEventListener("pointerdown", e => { if (L.phase !== "answer") return; cv.setPointerCapture(e.pointerId); drawing = [pos(e)]; strokes.push(drawing); setReady(true); paint(); });
    cv.addEventListener("pointermove", e => { if (drawing) { drawing.push(pos(e)); paint(); } });
    ["pointerup", "pointercancel"].forEach(ev => cv.addEventListener(ev, () => drawing = null));
    const gb = h("button", { class: "btn ghost", onclick: () => { guide = !guide; gb.textContent = guide ? t("hide_guide") : t("show_guide"); paint(); } }, t("show_guide"));
    put(L.body, h("div", { class: "pad-wrap" }, cv), h("div", { class: "row" }, h("button", { class: "btn ghost", onclick: () => { if (L.phase === "answer") { strokes.length = 0; setReady(false); paint(); } } }, t("clear_pad")), gb));
    L.getPayload = () => ({}); L.afterCheck = () => { guide = false; reveal = true; paint(); }; paint();
    if (document.fonts) document.fonts.ready.then(paint);
  },
  unknown(ex, L) { put(L.body, h("div", {}, JSON.stringify(ex))); setReady(true); },
};
function contourSvg(tones, hgt) {
  const NS = "http://www.w3.org/2000/svg", svg = document.createElementNS(NS, "svg"); svg.setAttribute("viewBox", "0 0 100 56");
  const col = { 1: "#c0392b", 2: "#d68910", 3: "#2a8c4a", 4: "#2a6fb0" };
  if (!Object.keys(CONTOURS).length) Object.assign(CONTOURS, J(B.tone_contours()));
  tones.forEach((tn, k) => {
    const pts = CONTOURS[tn], w = tones.length > 1 ? 40 : 70, x0 = tones.length > 1 ? 6 + k * 50 : 15;
    const lvl = x => { for (let i = 0; i < pts.length - 1; i++) { const [a, ya] = pts[i], [b, yb] = pts[i + 1]; if (x >= a && x <= b) { let f = (x - a) / (b - a); f = f * f * (3 - 2 * f); return ya + (yb - ya) * f; } } return pts[pts.length - 1][1]; };
    let d = ""; for (let i = 0; i <= 20; i++) { const x = i / 20; d += (i ? "L" : "M") + (x0 + w * x).toFixed(1) + " " + (50 - (lvl(x) - 1) * 10.5).toFixed(1); }
    const p = document.createElementNS(NS, "path"); p.setAttribute("d", d); p.setAttribute("fill", "none"); p.setAttribute("stroke", col[tn]); p.setAttribute("stroke-width", "5"); p.setAttribute("stroke-linecap", "round"); svg.append(p);
  });
  return svg;
}

/* ---------------- przebieg lekcji ---------------- */
function feedback(kind, title, text) {
  const L = cur.L; L.foot.className = "lfoot " + kind;
  L.foot.replaceChildren(...[h("div", { class: "fb-t" }, title), text ? h("div", { class: "fb-x", dir: "auto" }, text) : null, L.main].filter(Boolean));
}
function autoComplete(perfect) {
  const L = cur.L; if (L.phase !== "answer") return; sfx.correct(); L.phase = "feedback"; L.lastOk = true;
  feedback("good", perfect ? t("praise")[Math.floor(Math.random() * 5)] : t("all_matched"), ""); L.main.className = "btn green"; L.main.disabled = false; L.main.textContent = t("next");
}
function pressMain() {
  const L = cur.L; if (!L || L.main.disabled) return;
  if (L.phase === "feedback") return advance(L.lastOk);
  if (L.phase !== "answer") return;
  const type = L.ex.type;
  if (type === "intro" || type === "insight") return advance(null);
  const r = J(B.check(JSON.stringify(L.getPayload ? L.getPayload() : {})));
  if (L.afterCheck) { if (type === "tone") L.answerTone = r.answer_tone; L.afterCheck(r); }
  if (r.ok === "self") {
    L.phase = "self"; L.foot.className = "lfoot self";
    L.foot.replaceChildren(h("div", { class: "fb-t" }, t("how_went")), h("div", { class: "fb-x" }, t("draw_hint")),
      h("div", { class: "row" }, h("button", { class: "btn red", onclick: () => { sfx.wrong(); advance(false); } }, t("not_quite")), h("button", { class: "btn green", onclick: () => { sfx.correct(); advance(true); } }, t("did_it"))));
    return;
  }
  L.phase = "feedback"; L.lastOk = !!r.ok;
  if (r.ok) { sfx.correct(); feedback("good", t("praise")[Math.floor(Math.random() * 5)], r.solution && type === "type" && r.solution.startsWith("Pełny") ? r.solution : ""); L.main.className = "btn green"; }
  else { sfx.wrong(); feedback("bad", t("correct_answer"), (r.solution || "") + (r.why ? "\n\n" + t("think") + " " + r.why : "")); L.main.className = "btn red"; }
  L.main.textContent = t("next"); L.main.disabled = false;
}
function advance(ok) {
  const a = J(B.advance(ok === null ? "null" : ok ? "1" : ""));
  const L = cur.L; updateHeader(a);
  if (a.milestone) { sfx.streak(); toast("☀ " + a.milestone + " " + t("combo") + "!"); }
  if (a.out_of_hearts) return outOfHearts();
  if (a.finished) return finishSession();
  showCurrent();
}
function outOfHearts() {
  refreshHome(); const H = cur.home;
  const close = sheet([h("div", { style: "font-size:calc(44px*var(--k));text-align:center;color:var(--red)" }, "♥ 0"), h("h3", { style: "text-align:center" }, t("no_hearts")),
    h("p", { style: "text-align:center" }, t("hearts_hint", Math.floor(H.next_heart / 60) + 1)),
    h("button", { class: "btn blue", disabled: H.gems < H.refill_cost, onclick: () => { if (B.buy("refill")) { close(); showCurrent(); } } }, `${t("refill")} ◆ ${H.refill_cost}`),
    h("button", { class: "btn green", onclick: () => { close(); B.abandon(); startSession("practice"); } }, t("practice_heart")),
    h("button", { class: "btn ghost", onclick: () => { close(); B.abandon(); renderHome(); } }, t("leave"))], { mid: true });
}
function finishSession() {
  const ev = J(B.finish()); sfx.done(); track("lesson_done", { course: cur.cid, kind: ev.kind }); refreshHome(); const H = cur.home;
  const names = (ev.unlocked || []).map(i => H.units[i] && H.units[i].title);
  const scr = show(h("div", { class: "scroll res" },
    h("div", { class: "coin" }, ev.crown_up ? "♛" : "✓"), h("h2", {}, ev.crown_up ? t("crown_up") : t("lesson_done")),
    h("div", { class: "rg" }, h("div", {}, h("b", {}, "+" + ev.xp), h("span", {}, "XP")), h("div", {}, h("b", {}, Math.round(100 * ev.accuracy) + "%"), h("span", {}, t("accuracy"))), h("div", {}, h("b", {}, "◆ +" + ev.gems), h("span", {}, t("gems")))),
    ev.perfect ? h("div", {}, "★ perfect") : null, ev.max_combo >= 3 ? h("div", {}, "☀ " + ev.max_combo + " " + t("combo")) : null,
    ev.streak_extended ? h("div", { style: "color:#9E2B25;font-weight:700" }, "☀ " + t("streak_days", ev.streak)) : null,
    ev.heart_back ? h("div", { style: "color:var(--red)" }, "♥ +1") : null,
    ...names.map(n => h("div", { class: "card" }, "🔓 " + t("unlocked") + ": ", h("b", {}, n))),
    ...(ev.chats || []).map(n => h("div", { class: "card" }, "✉ " + t("chat_unlocked") + ": ", h("b", {}, n))),
    adSlot(CFG.ads && CFG.ads.slotResult),
    h("button", { class: "btn", onclick: () => { cur.tab = "path"; renderHome(); } }, t("back_home"))), "course");
  scr.style.cssText = themeStyle();
}

/* ---------------- start ---------------- */
async function main() {
  try {
    META = await (await fetch("courses.json")).json(); META.forEach(m => BYID[m.id] = m);
    initAnalytics();
    await initPython();
    if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
    showHub();
    window.__ready = true;
  } catch (e) {
    console.error(e);
    app().replaceChildren(h("div", { class: "boot" }, h("div", {}, t("err")), h("pre", { style: "white-space:pre-wrap;font-size:calc(12px*var(--k));padding:0 16px" }, String(e && e.stack || e)), h("button", { class: "chip on", onclick: () => location.reload() }, t("retry"))));
  }
}
window.addEventListener("load", main);

/* skróty klawiszowe (komputer): Enter = Sprawdź/Dalej, 1–9 = odpowiedź */
document.addEventListener("keydown", (e) => {
  if (!cur.L || e.ctrlKey || e.metaKey || e.altKey) return;
  const tg = e.target && e.target.tagName;
  if (tg === "INPUT" || tg === "TEXTAREA") { if (e.key === "Enter" && tg === "INPUT" && !e.shiftKey) { const b = document.querySelector(".lfoot .btn"); if (b && !b.disabled) b.click(); } return; }
  if (e.key === "Enter" && tg !== "BUTTON") { const b = document.querySelector(".lfoot .btn"); if (b && !b.disabled) { e.preventDefault(); b.click(); } }
  else if (/^[1-9]$/.test(e.key) && cur.L.phase === "answer") { const o = document.querySelectorAll(".lbody .opts .opt, .lbody .opt"); const el = o[parseInt(e.key, 10) - 1]; if (el && !el.disabled) el.click(); }
});

/* przycisk „wstecz” w aplikacji na Androida: zwraca true, gdy obsłużony */
window.__back = () => {
  const sh = document.querySelector(".sheet-bg"); if (sh) { sh.remove(); return true; }
  const x = document.querySelector(".lhead .x"); if (x) { x.click(); return true; }
  const bk = document.querySelector(".top .back"); if (bk) { bk.click(); return true; }
  return false;
};

/* ---------------- chiński: znaki w kolorze tonu ---------------- */
const TONE_COURSES = ["hanzi_hero", "han"];
const toneState = { cid: null, map: null, max: 1 };
const HAN_RE = /[\u3400-\u9fff]/;
function toneOn() { return TONE_COURSES.includes(cur.cid) && cur.home && cur.home.settings && cur.home.settings.tonecolor !== false; }
function toneMap() {
  if (toneState.cid !== cur.cid) {
    try { toneState.map = J(B.tone_map()); } catch (e) { toneState.map = {}; }
    toneState.cid = cur.cid; toneState.max = Math.max(1, ...Object.keys(toneState.map).map(k => k.length));
  }
  return toneState.map;
}
function colorText(node) {
  const txt = node.nodeValue; if (!txt || !HAN_RE.test(txt)) return;
  const par = node.parentNode; if (!par || (par.classList && (par.classList.contains("tcw") || par.classList.contains("tn"))) || /^(TEXTAREA|INPUT|SCRIPT|STYLE)$/.test(par.nodeName)) return;
  const map = toneMap(), wrap = document.createElement("span"); wrap.className = "tcw";
  let i = 0, plain = "";
  const flush = () => { if (plain) { wrap.append(plain); plain = ""; } };
  while (i < txt.length) {
    let hit = null;
    if (HAN_RE.test(txt[i])) for (let n = Math.min(toneState.max, txt.length - i); n >= 1; n--) { const w = txt.substr(i, n); if (map[w]) { hit = w; break; } }
    if (!hit) { plain += txt[i++]; continue; }
    flush();
    map[hit].forEach((tone, k) => { const s = document.createElement("span"); s.className = "tn t" + tone; s.textContent = hit[k]; wrap.append(s); });
    i += hit.length;
  }
  flush(); par.replaceChild(wrap, node);
}
function colorTree(root) {
  if (root.nodeType === 3) return colorText(root);
  if (root.nodeType !== 1 || root.classList.contains("tcw")) return;
  const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), list = []; let n;
  while ((n = w.nextNode())) list.push(n);
  list.forEach(colorText);
}
new MutationObserver((muts) => {
  if (!toneOn()) return;
  for (const m of muts) m.addedNodes.forEach(colorTree);
}).observe(document.getElementById("app"), { childList: true, subtree: true });

/* ---------------- larpy: sceny ze stawką ---------------- */
function larpSheet(l) {
  const close = sheet([h("h3", {}, l.title), h("p", {}, l.scene), h("p", {}, h("b", {}, t("larp_goal") + ": "), l.goal),
    h("p", { style: "font-size:calc(13.5px*var(--k))" }, t("larp_rules").replace("%d", l.fee).replace("%d", l.fee * 3)),
    l.can_pay ? h("button", { class: "btn", onclick: () => { close(); openLarp(l.id); } }, t("larp_enter") + " (−" + l.fee + " XP)")
      : h("p", { style: "color:var(--bad2);font-weight:700" }, t("larp_need").replace("%d", l.fee)),
    h("button", { class: "btn ghost", onclick: () => close() }, t("close"))]);
}
function openLarp(lid) {
  const S = J(B.larp_start(lid)); if (!S.ok) { toast(t("larp_need").replace("%d", "")); return; }
  track("larp_start", { course: cur.cid, larp: lid });
  let node = S.node, patience = S.patience, over = false; const excluded = new Set();
  const log = h("div", { class: "log" }), reply = h("div", { class: "reply" }), pips = h("span", { class: "stat s-heart", title: t("larp_patience") });
  const drawPips = () => { pips.textContent = "◆".repeat(Math.max(0, patience)) + "◇".repeat(Math.max(0, S.max_patience - patience)); };
  const leave = () => { if (over) { cur.tab = "chats"; return renderHome(); } confirmBox(t("larp_quit_t"), t("larp_quit_d"), t("quit"), t("keep"), () => { B.larp_abandon(); cur.tab = "chats"; renderHome(); }); };
  const scr = show([h("div", { class: "top" }, h("button", { class: "back", onclick: leave }, "‹"),
    h("div", { class: "av", style: "background:#7A2E5E;width:38px;height:38px;font-size:calc(19px*var(--k))" }, S.avatar),
    h("div", { class: "ttl", dir: "auto" }, S.partner), pips),
    h("div", { class: "goal", style: "font-weight:400" }, h("b", {}, t("larp_goal") + ": "), S.goal), log, reply], "course");
  scr.style.cssText = themeStyle(); drawPips();
  const toBottom = () => setTimeout(() => log.scrollTo({ top: log.scrollHeight, behavior: "smooth" }), 30);
  const bubble = (text, sub, pl, mine, wrong) => {
    const b = h("div", { class: "msg" + (mine ? " me" : "") + (wrong ? " wrong" : ""), dir: "auto", onclick: () => b.classList.toggle("open") }, text, sub ? h("small", {}, sub) : null, pl ? h("div", { class: "en" }, pl) : null);
    log.append(b); toBottom(); return b;
  };
  const note = (txt, cls) => { log.append(h("div", { class: "note" + (cls ? " " + cls : "") }, txt)); toBottom(); };
  note(S.scene); note(t("tap_tr"));
  const botSay = () => {
    reply.replaceChildren(); excluded.clear();
    const typing = h("div", { class: "msg" }, "…"); log.append(typing); toBottom();
    setTimeout(() => { typing.remove(); bubble(node.bot_text, node.bot_sub, node.pl); speak(node.bot_text, true); if (node.note) note(node.note); if (node.deadly) note(t("larp_deadly"), "deadly"); showReply(); }, 600);
  };
  const finish = (ev) => {
    over = true; reply.replaceChildren(); (ev.outcome === "fail" ? sfx.wrong : sfx.done)(); track("larp_end", { course: cur.cid, larp: lid, outcome: ev.outcome });
    const xp = ev.outcome === "win" ? `+${ev.gain} XP (${t("larp_enter") === "Enter" ? "net" : "zysk"} +${ev.net}) · ◆ +${ev.gems}` : ev.outcome === "partial" ? t("larp_refund") : `−${ev.fee} XP`;
    log.append(h("div", { class: "card larp-end " + ev.outcome, style: "text-align:center" }, h("b", { style: "font-size:calc(20px*var(--k))" }, t("larp_" + ev.outcome)), h("div", { style: "margin:6px 0" }, ev.text), h("div", { style: "font-weight:700" }, xp),
      ev.streak_extended ? h("div", { style: "color:var(--bad2);font-weight:700" }, "☀ " + t("streak_days", ev.streak)) : null)); toBottom();
    refreshHome(); const me = (cur.home.larps || []).find(x => x.id === lid);
    reply.append(h("button", { class: "btn", onclick: () => { cur.tab = "chats"; renderHome(); } }, t("back_chats")),
      me && me.can_pay ? h("button", { class: "btn ghost", onclick: () => openLarp(lid) }, t("again") + " (−" + me.fee + " XP)") : null);
  };
  const handle = (r) => {
    patience = r.patience; drawPips();
    bubble(r.text || "…", r.sub, null, true, r.verdict === "bad");
    reply.replaceChildren();
    if (r.verdict === "bad") { sfx.wrong(); if (r.why) note(t("think") + " " + r.why); if (r.answer && !r.end) note(t("larp_correct") + r.answer); }
    else if (r.verdict === "weak") { sfx.tap(); note(t("larp_weak") + (r.why ? " " + r.why : "")); }
    else sfx.correct();
    if (r.end) return setTimeout(() => { if (r.node && r.node.end) { bubble(r.node.bot_text, r.node.bot_sub, r.node.pl); speak(r.node.bot_text, true); } finish(r.end); }, 700);
    if (r.node) { node = r.node; return setTimeout(botSay, 500); }
    setTimeout(showReply, 900);
  };
  const showReply = () => {
    reply.replaceChildren();
    if (node.options) {
      reply.append(h("div", { class: "sub", style: "text-align:left" }, t("pick_answer")));
      node.options.filter(o => !excluded.has(o.i)).sort(() => Math.random() - 0.5).forEach(o => reply.append(h("button", { class: "opt", dir: "auto", onclick: () => {
        speak(o.text, true); excluded.add(o.i); handle(J(B.larp_answer(JSON.stringify({ option: o.i })))); } }, o.text, o.sub ? h("small", {}, o.sub) : null)));
    } else {
      const bd = node.build, picked = [];
      const ans = h("div", { class: "tiles answer", style: "background:var(--white);border-radius:12px;padding:8px;min-height:60px" }), bank = h("div", { class: "tiles" });
      const send = h("button", { class: "btn", disabled: true }, t("send"));
      const render = () => {
        ans.replaceChildren(...picked.map(p => tile(p, () => { picked.splice(picked.indexOf(p), 1); render(); })));
        bank.replaceChildren(...bd.bank.filter(b => !picked.includes(b)).map(b => tile(b, () => { picked.push(b); render(); })));
        send.disabled = !picked.length;
      };
      send.onclick = () => handle(J(B.larp_answer(JSON.stringify({ tokens: picked.map(p => p.v) }))));
      reply.append(h("div", {}, h("b", {}, t("say") + " "), `„${bd.prompt}”`), ans, bank, send); render();
    }
  };
  botSay();
}
