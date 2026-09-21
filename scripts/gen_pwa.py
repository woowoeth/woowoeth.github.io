#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""三语 PWA：manifest + service worker + 注册。

    python3 scripts/gen_pwa.py

修的三件事（2026-09-21 查出来的）：

1. **描述被写死了。** 原文「75位古今中外顶级人物…7大生存主题」，而现在是
   171 个条目、403 章节。写死的数字一定会过期 —— 这里改成从 hw_chapters 现算。
2. **英文站和繁体站的 manifest 是 404。** 三语页面都写着
   `<link rel="manifest" href="site.webmanifest">`，**相对路径** ——
   /en/index.html 解析成 /en/site.webmanifest，那个文件不存在。
3. **没有 service worker。** 没有它就没有离线，装到主屏也只是个书签。

图标一律用绝对路径（/icon-192.png），否则 /en/ 下又会解析到不存在的地方 ——
和第 2 条同一个病。
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

SW_VERSION = "2026-09-21a"          # 改了 sw.js 就往后挪，否则老用户拿不到新的

LANGS = [
    ("", "zh-CN", "人类世界生存法则", "生存法则",
     "%d 个人物与典籍、%d 篇深读：遇到一件事，看以前的人怎么处理。"),
    ("en/", "en", "OurWord — Human World Rules", "OurWord",
     "%d people and classics, %d deep reads: see how people before you handled it."),
    ("tw/", "zh-Hant", "人類世界生存法則", "生存法則",
     "%d 個人物與典籍、%d 篇深讀：遇到一件事，看以前的人怎麼處理。"),
]

SW = """// OurWord service worker — v%(v)s
// 策略：页面走网络优先（内容每天更新，不能给旧的），静态资源走缓存优先，
// 断网时回退到缓存里那份。**不预缓存整站** —— 1700 多页，预缓存等于替用户下载全站。
const V = '%(v)s';
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

  const isAsset = /\\.(css|js|png|jpg|jpeg|webp|svg|woff2?|ico)$/.test(u.pathname);
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
"""

OFFLINE = """<!doctype html><meta charset="utf-8">
<title>断网了 — 人类世界生存法则</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>html,body{margin:0;height:100%%;display:grid;place-items:center;
background:#f5f2ea;color:#14120e;font:16px/1.7 -apple-system,system-ui,sans-serif}
div{max-width:30em;padding:2em;text-align:center}a{color:#9d2933}</style>
<div>
<p style="font-size:1.3em;font-weight:700">现在连不上网。</p>
<p>你之前打开过的页面还在，回退一步就能看。<br>网络回来之后刷新这一页。</p>
<p><a href="/">回首页</a></p>
</div>
"""

REG = ('<script>if("serviceWorker" in navigator){addEventListener("load",function(){'
       'navigator.serviceWorker.register("/sw.js").catch(function(){})})}</script>')


def counts():
    os.environ.pop("HW_CHAPTERS", None)
    import hw_chapters as C
    return len(C.PARENTS), len(C.CHAPTERS)


def main():
    people, chapters = counts()
    wrote = []
    for prefix, lang, name, short, desc in LANGS:
        d = os.path.join(ROOT, prefix) if prefix else ROOT
        if not os.path.isdir(d):
            continue
        m = {
            "name": name, "short_name": short,
            "description": desc % (people, chapters),
            "lang": lang,
            "start_url": "/" + prefix, "scope": "/" + prefix,
            "display": "standalone",
            "background_color": "#f0f0ec", "theme_color": "#9d2933",
            # 绝对路径：相对路径在 /en/ 下会解析到不存在的地方（本次修的第 2 条）
            "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                      {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
                      {"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
        }
        p = os.path.join(d, "site.webmanifest")
        io.open(p, "w", encoding="utf-8").write(json.dumps(m, ensure_ascii=False, indent=2) + "\n")
        wrote.append(os.path.relpath(p, ROOT))
    io.open(os.path.join(ROOT, "sw.js"), "w", encoding="utf-8").write(SW % {"v": SW_VERSION})
    io.open(os.path.join(ROOT, "offline.html"), "w", encoding="utf-8").write(OFFLINE)
    print("  manifest：%s" % "、".join(wrote))
    print("  sw.js（v%s）+ offline.html" % SW_VERSION)

    # 每一页都要挂：manifest 让它可安装，注册脚本让离线在任何一页都生效。
    # 而且 manifest 必须写**绝对路径** —— 原来三语页面写的都是相对的
    # `href="site.webmanifest"`，/en/ 下解析成 /en/site.webmanifest，404。
    n = fixed = 0
    for dirp, _dn, fn in os.walk(ROOT):
        if os.sep + "." in dirp or os.sep + "skill" in dirp or os.sep + "podcast" in dirp:
            continue
        for f in fn:
            if f != "index.html":
                continue
            fp = os.path.join(dirp, f)
            rel = os.path.relpath(fp, ROOT).replace(os.sep, "/")
            pre = "en/" if rel.startswith("en/") else ("tw/" if rel.startswith("tw/") else "")
            href = "/%ssite.webmanifest" % pre
            t = io.open(fp, encoding="utf-8", errors="ignore").read()
            o = t
            i = t.find('<link rel="manifest"')
            if i >= 0:
                j = t.find(">", i) + 1
                if ('href="%s"' % href) not in t[i:j]:
                    t = t[:i] + '<link rel="manifest" href="%s">' % href + t[j:]
                    fixed += 1
            else:
                k = t.find("</head>")
                if k < 0:
                    continue
                t = t[:k] + '<link rel="manifest" href="%s">' % href + t[k:]
            if "serviceWorker" not in t:
                i = t.find('<link rel="manifest"')
                j = t.find(">", i) + 1
                t = t[:j] + REG + t[j:]
            if t != o:
                io.open(fp, "w", encoding="utf-8").write(t)
                n += 1
    print("  页面：%d 页挂上 manifest + 注册（其中 %d 页原来的 manifest 路径是坏的）" % (n, fixed))
    print("  内容规模：%d 个条目 · %d 篇章节（描述从这里现算，不再写死）" % (people, chapters))
    return 0


if __name__ == "__main__":
    sys.exit(main())
