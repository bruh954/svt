// Prosty zbieracz zdarzeń dla Śviętovita: Cloudflare Worker + baza D1 (darmowy plan wystarcza na start).
// Przyjmuje POST z JSON-em { n, p, lang, v, ts, id?, d0? } i zapisuje do tabeli events.
export default {
  async fetch(req, env) {
    const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type" };
    if (req.method === "OPTIONS") return new Response(null, { headers: cors });
    if (req.method !== "POST") return new Response("ok", { headers: cors });
    let b; try { b = JSON.parse(await req.text()); } catch (e) { return new Response("bad", { status: 400, headers: cors }); }
    if (!b || typeof b.n !== "string" || b.n.length > 40) return new Response("bad", { status: 400, headers: cors });
    const p = JSON.stringify(b.p || {}).slice(0, 500);
    await env.DB.prepare("INSERT INTO events (ts, day, name, props, lang, cid, d0) VALUES (?, ?, ?, ?, ?, ?, ?)")
      .bind(Date.now(), new Date().toISOString().slice(0, 10), b.n, p, String(b.lang || "").slice(0, 5), b.id ? String(b.id).slice(0, 64) : null, b.d0 ? String(b.d0).slice(0, 10) : null).run();
    return new Response("ok", { headers: cors });
  },
};
