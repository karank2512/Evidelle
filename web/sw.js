/* Service worker: precaches the app shell so the check works fully offline after
 * the first visit. The experimental detector (~60 MB) is not precached — its files
 * are fetched from this same site only if the user runs the detector, then cached
 * for reuse. Bump CACHE when any vendored file or asset changes. */
const CACHE = 'evidelle-20261128-1';
const ASSETS = [
  './',
  './index.html',
  './styles.css',
  './app.js',
  './trust-anchors.js',
  './manifest.webmanifest',
  './icon-192.png',
  './icon-512.png',
  './vendor/c2pa-web/inline.js',
  './vendor/c2pa-web/builder-CaTgrAW1.js',
  './vendor/c2pa-web/c2pa_worker.js',
  './vendor/c2pa-utilities/index.js',
  './vendor/c2pa-utilities/context.js',
  './vendor/c2pa-utilities/settings.js',
  './vendor/c2pa-utilities/fetchWithRetry.js',
  './vendor/c2pa-utilities/caseConversion.js',
  './vendor/c2pa-utilities/signingAlg.js',
  './vendor/c2pa-utilities/assetSize.js',
  './vendor/highgain/index.js',
  './vendor/ts-deepmerge/index.js',
];
/* Fetched on demand (same origin) and then kept in the same cache. */
const RUNTIME_ASSETS = [
  './vendor/onnxruntime-web/ort.wasm.min.mjs',
  './vendor/onnxruntime-web/ort-wasm-simd-threaded.mjs',
  './vendor/onnxruntime-web/ort-wasm-simd-threaded.wasm',
  './detector-model.fp16.onnx',
];
const RUNTIME_SET = new Set(RUNTIME_ASSETS.map((u) => new URL(u, self.location.href).pathname));

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys()
    .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') { return; }
  e.respondWith(
    caches.match(e.request, { ignoreSearch: true }).then((hit) => {
      if (hit) { return hit; }
      return fetch(e.request).then((res) => {
        if (res.ok && RUNTIME_SET.has(new URL(e.request.url).pathname)) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(e.request, copy));
        }
        return res;
      });
    })
  );
});
