// OurWord service worker — v2026-09-21a
// 策略：页面走网络优先（内容每天更新，不能给旧的），静态资源走缓存优先，
// 断网时回退到缓存里那份。**不预缓存整站** —— 1700 多页，预缓存等于替用户下载全站。
const V = '2026-09-21a';
const PAGES = 'ow-pages-' + V;
const ASSETS = 'ow-assets-' + V;
const SHELL = ['/', '/offline.html'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(PAGES).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  // 换版必须清旧缓存，否则用户会一直吃到上一版 —— service worker 最常见的坑。
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
  if (isAsset) {                                      // 静态资源：缓存优先（带版本号，改了就换名）
    e.respondWith(caches.match(r).then(hit => hit || fetch(r).then(res => {
      const copy = res.clone();
      caches.open(ASSETS).then(c => c.put(r, copy));
      return res;
    }).catch(() => hit)));
    return;
  }
  e.respondWith(fetch(r).then(res => {                // 页面：网络优先
    const copy = res.clone();
    caches.open(PAGES).then(c => c.put(r, copy));
    return res;
  }).catch(() => caches.match(r).then(hit => hit || caches.match('/offline.html'))));
});
