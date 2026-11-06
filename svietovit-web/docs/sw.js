const CACHE = "sviet-0285aebcfa";
const FILES = ["./", "app.js", "courses.json", "fonts.css", "fonts/Sviet-Bold.ttf", "fonts/Sviet-Regular.ttf", "fonts/abba-b.ttf", "fonts/abba-r.ttf", "fonts/abba-x.ttf", "fonts/ave-b.ttf", "fonts/ave-r.ttf", "fonts/glagol-b.ttf", "fonts/glagol-r.ttf", "fonts/glagol-x.ttf", "fonts/han-b.ttf", "fonts/han-r.ttf", "fonts/hangeul-b.ttf", "fonts/hangeul-r.ttf", "fonts/hanzi_hero-b.ttf", "fonts/hanzi_hero-r.ttf", "fonts/kana-b.ttf", "fonts/kana-r.ttf", "fonts/kaszeby-b.ttf", "fonts/kaszeby-r.ttf", "fonts/logos-b.ttf", "fonts/logos-r.ttf", "fonts/nihon-b.ttf", "fonts/nihon-r.ttf", "icon-192.png", "icon-512.png", "index.html", "manifest.webmanifest", "py/bridge.py", "py/courses.zip", "pyodide/pyodide-lock.json", "pyodide/pyodide.asm.js", "pyodide/pyodide.asm.wasm", "pyodide/pyodide.js", "pyodide/python_stdlib.zip", "style.css"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(caches.match(e.request, { ignoreSearch: true }).then(r => r || fetch(e.request)));
});
