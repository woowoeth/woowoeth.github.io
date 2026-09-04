#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""窄屏门禁：375px 下不许横向撑开。

    python3 scripts/check_mobile.py

为什么要单独一道闸：撑开这件事**桌面端完全看不见**。这次的原因是
`.layout{grid-template-columns:1fr!important}` —— `1fr` 等价于
`minmax(auto,1fr)`，`auto` 这个下限取的是内容的 min-content；移动端把侧栏
目录改成了一条横向滚动的胶囊带，它的 min-content 就是整条带子的宽度，
于是网格轨道被顶到 2000px 开外，整页跟着横着滚，正文右半边全在屏幕外。

三种语言都要量：这条 CSS 是三种语言共用的，而英文的标题比中文长得多，
同一个 bug 在中文页上表现轻、在英文页上表现重 —— 只量一种语言，
既可能漏掉，也可能误判成「英文的问题」。

判据是 documentElement.scrollWidth <= clientWidth + 1，也就是
「读者不需要横向滚动」。允许 1px 是给亚像素留的余量。
"""
import os
import subprocess
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PORT = 8934
WIDTH, HEIGHT = 375, 812

# 每种语言各挑三类版式：首页、条目页、章节页。撑开是版式问题，
# 不是内容问题 —— 同一类版式抽一页就够，抽满三类才不漏版式。
SAMPLE = [
    ("简体首页", "/"),
    ("简体条目", "/i/su-shi/"),
    ("简体章节", "/i/su-shi/no-wind-no-rain/"),
    ("简体全集", "/all/"),
    ("繁体首页", "/tw/"),
    ("繁体条目", "/tw/i/su-shi/"),
    ("繁体章节", "/tw/i/su-shi/no-wind-no-rain/"),
    ("英文首页", "/en/"),
    ("英文条目", "/en/i/su-shi/"),
    ("英文章节", "/en/i/su-shi/no-wind-no-rain/"),
    ("英文全集", "/en/all/"),
]


def serve():
    import http.server
    import functools
    # 静音要挂在 handler 上，不是 server 上 —— log_message 是 handler 的
    # 方法。挂错地方的话每个请求都往门禁输出里打一行，最后一行访问日志
    # 会盖掉真正的结论。
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    h = functools.partial(Quiet, directory=ROOT)
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("（没装 playwright，跳过窄屏检查）")
        return 0

    srv = serve()
    bad, checked = [], 0
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            pg = b.new_page(viewport={"width": WIDTH, "height": HEIGHT},
                            device_scale_factor=2, is_mobile=True,
                            has_touch=True, locale="en-US")
            for label, path in SAMPLE:
                fp = os.path.join(ROOT, path.strip("/"), "index.html")
                if path == "/":
                    fp = os.path.join(ROOT, "index.html")
                if not os.path.exists(fp):
                    bad.append("%s 这一页不存在：%s（抽样表要跟着改）" % (label, path))
                    continue
                # 语言重定向会把 / 送到 /en/：URL 优先，带上 ?hwxlang 之类
                # 的开关不现实，所以直接把 localStorage 里的偏好设成这一页
                # 自己的语言，让重定向不发生。
                lang = "en" if path.startswith("/en") else (
                    "tw" if path.startswith("/tw") else "sc")
                pg.goto("http://127.0.0.1:%d/" % PORT, wait_until="domcontentloaded")
                pg.evaluate("l => localStorage.setItem('hwx_lang', l)", lang)
                pg.goto("http://127.0.0.1:%d%s" % (PORT, path),
                        wait_until="load")
                pg.wait_for_timeout(500)
                r = pg.evaluate("""() => {
                    const d = document.documentElement;
                    const vw = d.clientWidth;
                    const over = [];
                    document.querySelectorAll('body *').forEach(el => {
                      const b = el.getBoundingClientRect();
                      if (b.width > vw + 1 && el.scrollWidth <= b.width + 1)
                        over.push(el.tagName.toLowerCase()
                          + (el.className ? '.' + String(el.className).trim()
                             .split(/\\s+/)[0] : '')
                          + ' ' + Math.round(b.width) + 'px');
                    });
                    return {sw: d.scrollWidth, vw, over: over.slice(0, 4)};
                }""")
                checked += 1
                if r["sw"] > r["vw"] + 1:
                    bad.append("%s %s 横向撑开：页面 %dpx，屏幕 %dpx%s"
                               % (label, path, r["sw"], r["vw"],
                                  ("　撑开的是 " + "、".join(r["over"]))
                                  if r["over"] else ""))
            b.close()
    finally:
        srv.shutdown()

    print("窄屏 %dpx：量了 %d 页" % (WIDTH, checked))
    if bad:
        print("\n不合格：")
        for x in bad:
            print("  ✗ " + x)
        return 1
    print("✓ 三种语言的首页、条目页、章节页在 375px 下都不需要横向滚动")
    return 0


if __name__ == "__main__":
    sys.exit(main())
