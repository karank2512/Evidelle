/* Service worker: precaches the whole app shell so the check works fully offline
 * after the first visit. Bump CACHE when any vendored file or asset changes. */
const CACHE = 'evidelle-20261127-1';
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
    caches.match(e.request, { ignoreSearch: true }).then((hit) => hit || fetch(e.request))
  );
});
