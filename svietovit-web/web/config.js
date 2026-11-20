/* Ustawienia wdrożenia. Domyślnie wszystko wyłączone. */
window.SV_CONFIG = {
  // Anonimowe statystyki, tylko za zgodą użytkownika.
  // endpoint: adres własnego zbieracza zdarzeń (patrz tools/analytics-worker/README.md). Puste = wyłączone.
  // domain: opcjonalnie Plausible (płatny), np. "swietovit.pl". Puste = wyłączone.
  analytics: { endpoint: "", domain: "", src: "https://plausible.io/js/script.tagged-events.js" },
  // Reklamy Google AdSense. Włącz dopiero po akceptacji konta i wdrożeniu okna zgody (CMP).
  ads: { enabled: false, client: "ca-pub-0000000000000000", slotHome: "", slotResult: "" },
};
