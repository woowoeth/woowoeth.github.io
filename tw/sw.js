// OurWord service worker — v2026-09-21a
// 策略：頁面走網絡優先（內容每天更新，不能給舊的），靜態資源走緩存優先，
// 斷網時回退到緩存裡那份。**不預緩存整站** —— 1700 多頁，預緩存等於替用戶下載全站。
const V = '2026-09-21a';
const PAGES = 'ow-pages-' + V;
const ASSETS = 'ow-assets-' + V;
const SHELL = ['/', '/offline.html'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(PAGES).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  // 換版必須清舊緩存，否則用戶會一直吃到上一版 —— service worker 最常見的坑。
  e.waitUntil(caches.keys().then(ks => Promise.all(
    ks.filter(k => k.startsWith('ow-') && !k.endsWith(V)).map(k => caches.delete(k))
  )).then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const r = e.request;
  if (r.method !== 'GET') return;
  const u = new URL(r.url);
  if (u.origin !== location.origin) return;          // 第三方不碰
  if (u.pathname.startsWith('/skill/') || u.pathname.startsWith('/podcast/')) return;

  const isAsset = /\.(css|js|png|jpg|jpeg|webp|svg|woff2?|ico)$/.test(u.pathname);
  if (isAsset) {                                      // 靜態資源：緩存優先（帶版本號，改了就換名）
    e.respondWith(caches.match(r).then(hit => hit || fetch(r).then(res => {
      const copy = res.clone();
      caches.open(ASSETS).then(c => c.put(r, copy));
      return res;
    }).catch(() => hit)));
    return;
  }
  e.respondWith(fetch(r).then(res => {                // 頁面：網絡優先
    const copy = res.clone();
    caches.open(PAGES).then(c => c.put(r, copy));
    return res;
  }).catch(() => caches.match(r).then(hit => hit || caches.match('/offline.html'))));
});
