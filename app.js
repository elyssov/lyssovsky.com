/* =========================================================
   Eugene Lyssovsky — shared site behaviour
   EN/RU switching (no reload) + privacy-friendly counter.

   Each page declares its own translation table and title
   before this script loads:

     <script>
       window.RU    = { "key": "Русский текст", ... };
       window.TITLE = { en: "...", ru: "..." };
     </script>
     <script src="app.js"></script>

   English lives in the HTML; the original innerHTML of every
   [data-i18n] node is captured on load, so EN restore is lossless.
   The chosen language is stored in localStorage and therefore
   persists as the visitor moves between pages.
   ========================================================= */
(function () {
  var RU = window.RU || {};
  var TITLE = window.TITLE || null;

  var nodes = document.querySelectorAll('[data-i18n]');
  // Capture the original English markup once, so EN restore is lossless.
  nodes.forEach(function (el) { el.setAttribute('data-en', el.innerHTML); });

  var counterValue = null;

  function formatCount(lang) {
    var el = document.querySelector('[data-count]');
    if (!el || counterValue === null) return;
    el.textContent = counterValue.toLocaleString(lang === 'ru' ? 'ru-RU' : 'en-US');
  }

  function applyLang(lang) {
    if (lang !== 'ru') lang = 'en';
    nodes.forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      if (lang === 'ru' && RU[key] != null) {
        el.innerHTML = RU[key];
      } else {
        el.innerHTML = el.getAttribute('data-en');
      }
    });
    document.documentElement.lang = lang;
    if (TITLE && TITLE[lang]) document.title = TITLE[lang];
    document.querySelectorAll('.lang__btn').forEach(function (b) {
      var on = b.getAttribute('data-lang') === lang;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    formatCount(lang);
    try { localStorage.setItem('lang', lang); } catch (e) {}
  }

  var saved = 'en';
  try { saved = localStorage.getItem('lang') || 'en'; } catch (e) {}
  applyLang(saved);

  document.querySelectorAll('.lang__btn').forEach(function (b) {
    b.addEventListener('click', function () { applyLang(b.getAttribute('data-lang')); });
  });

  // Privacy-friendly visit counter — no cookies, no registration (abacus.jasoncameron.dev).
  // Shared across every page of the site. Fails silently if unreachable.
  (function () {
    var num = document.querySelector('[data-count]');
    if (!num) return;
    var wrap = num.closest('.footer__counter');
    fetch('https://abacus.jasoncameron.dev/hit/lyssovsky-com/site-views')
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (d && typeof d.value === 'number') {
          counterValue = d.value;
          formatCount(document.documentElement.lang);
          if (wrap) wrap.classList.add('is-visible');
        }
      })
      .catch(function () { /* leave the counter hidden on failure */ });
  })();
})();
