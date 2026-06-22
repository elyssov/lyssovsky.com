/* =========================================================================
   lyssovsky.com service worker — stale-while-revalidate cache
   Caches HTML / CSS / JS / WebP / fonts so the site keeps working offline
   and feels instant on repeat visits. The cache name bumps with each change
   so old assets are evicted on activation.
   ========================================================================= */
const CACHE = "lyssovsky-v1-2026-06-22";

const PRECACHE = [
  "/",
  "/index.html",
  "/about.html",
  "/about-aeliss.html",
  "/hire.html",
  "/gallery.html",
  "/journalism.html",
  "/products.html",
  "/research.html",
  "/writing.html",
  "/404.html",
  "/style.css",
  "/app.js",
  "/favicon.ico",
  "/favicon-180.png",
  "/favicon-512.png",
  "/manifest.webmanifest"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(PRECACHE).catch(() => {}))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);

  // Only handle same-origin and the Google Fonts files (woff2)
  const sameOrigin = url.origin === self.location.origin;
  const isFontFile = url.hostname === "fonts.gstatic.com";
  if (!sameOrigin && !isFontFile) return;

  // Stale-while-revalidate
  event.respondWith(
    caches.open(CACHE).then((cache) =>
      cache.match(req).then((cached) => {
        const network = fetch(req)
          .then((res) => {
            if (res && res.status === 200 && (res.type === "basic" || res.type === "cors")) {
              cache.put(req, res.clone()).catch(() => {});
            }
            return res;
          })
          .catch(() => cached);
        return cached || network;
      })
    )
  );
});
