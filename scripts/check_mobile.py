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

判据三条：
① 不横向撑开 —— documentElement.scrollWidth <= clientWidth + 1，也就是
   「读者不需要横向滚动」。允许 1px 是给亚像素留的余量。
② 语言切换和夜间模式在手机上必须真的**在**、真的能点。踩过：条目页和
   章节页的 .mast-links 在 700px 以下是 display:none（页头导航在手机上
   收起），而工具条被塞进了它里面 —— 尺寸 0×0，三种语言的条目页在手机上
   都没有语言切换、也没有夜间模式开关，而桌面端一切正常，所有闸门全绿。
③ 页头不许自己压自己 —— 工具条是绝对定位的、不占位，站名一长就从它底下
   穿过去。中文站名短，勉强不撞；英文「Human World Rules」在 375px 下被
   下拉框压掉「Rules」半个词。判的是两个矩形有没有交集。
⑤ 文字必须放得进它的框 —— 英文界面串普遍比中文长（同一句话「搜你遇到的
   事：被裁了、睡不着、孩子不听…」20 字，英文 62 个字符），塞进按中文宽度
   定好的控件里就被裁。裁掉的往往正是那句话唯一有用的部分（举例、数字）。
   判的是 scrollWidth 超出 clientWidth，以及占位文字量出来比输入框还宽。
⑥ 切页签要把信息流带回标签行 —— 读者已经往下翻了两屏，一换页签内容整个
   换掉、位置却留在原地，落在新一批卡片的中间，前面那些永远不会被看到。
   这一条只在**行为**上看得见，静态检查全绿。
④ 站名必须一行 —— ③ 只保证不重叠，而「不重叠」可以靠把站名压窄来达成，
   那样站名就断成两行。它是一个名字，断成两行不是排版，是把名字拆了。
   两条一起才逼出正确的解：工具条自己占一行，站名拿回整行宽度。
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
                    const rect = (e) => {
                      if (!e) return null;
                      const q = e.getBoundingClientRect();
                      return {x: q.x, y: q.y, w: q.width, h: q.height,
                              right: q.right, bottom: q.bottom};
                    };
                    return {sw: d.scrollWidth, vw, over: over.slice(0, 4),
                            lang: rect(document.getElementById('hwx-lang')),
                            theme: rect(document.getElementById('hwx-theme')),
                            title: rect(document.querySelector('.hd-title, .wordmark')),
                            clipped: (() => {
                              const out = [];
                              document.querySelectorAll('body *').forEach(el => {
                                const cs = getComputedStyle(el);
                                if (cs.display === 'none' || cs.visibility === 'hidden') return;
                                const q = el.getBoundingClientRect();
                                if (q.width < 30 || q.height < 8) return;
                                const name = el.tagName.toLowerCase()
                                  + (el.id ? '#' + el.id : '')
                                  + (el.className ? '.' + String(el.className).trim().split(/\\s+/)[0] : '');
                                if (el.scrollWidth > el.clientWidth + 2
                                    && cs.overflowX !== 'auto' && cs.overflowX !== 'scroll')
                                  out.push(name + ' 的内容被裁：'
                                    + (el.textContent || '').trim().slice(0, 40));
                                const ph = el.placeholder;
                                if (ph) {
                                  const probe = document.createElement('span');
                                  probe.style.cssText = 'position:absolute;left:-9999px;'
                                    + 'white-space:nowrap;font:' + cs.font;
                                  probe.textContent = ph;
                                  document.body.appendChild(probe);
                                  const need = probe.getBoundingClientRect().width;
                                  probe.remove();
                                  // clientWidth **含内边距**，直接拿它当
                                  // 可用宽度会算宽 —— 得减掉左右 padding，
                                  // 那才是文字真正能占的地方。
                                  const pad = parseFloat(cs.paddingLeft)
                                            + parseFloat(cs.paddingRight);
                                  const room = el.clientWidth - pad;
                                  if (need > room)
                                    out.push(name + ' 的占位文字放不下（要 '
                                      + Math.round(need) + 'px，框内只有 '
                                      + Math.round(room) + 'px）：' + ph.slice(0, 40));
                                }
                              });
                              return out.slice(0, 4);
                            })(),
                            titleLine: (() => {
                              const e = document.querySelector('.hd-title, .wordmark');
                              return e ? parseFloat(getComputedStyle(e).lineHeight) || 0 : 0;
                            })(),
                            // 读完之后那一块：读者能不能说一句自己的。
                            // 输入框是 hw-chat.js 运行时生成的，静态查不到，
                            // 只能在浏览器里问它在不在、接没接上。
                            yours: (() => {
                              const s = document.querySelector('.hw-same');
                              if (!s) return null;
                              const ta = s.querySelector('.arow textarea');
                              const go = s.querySelector('.arow .go');
                              const toc = document.querySelector('.toc');
                              return {toc: !!(toc && toc.offsetParent),
                                      ta: !!ta, go: !!go,
                                      ph: ta ? ta.placeholder : '',
                                      tail: [...s.children].slice(-2)
                                            .map(e => e.className).join(','),
                                      ask: typeof window.hwAsk};
                            })()};
                }""")
                checked += 1
                if r["sw"] > r["vw"] + 1:
                    bad.append("%s %s 横向撑开：页面 %dpx，屏幕 %dpx%s"
                               % (label, path, r["sw"], r["vw"],
                                  ("　撑开的是 " + "、".join(r["over"]))
                                  if r["over"] else ""))

                # ② 语言切换和夜间模式必须在、必须有尺寸、必须在屏幕里
                for what, box in (("语言切换", r["lang"]), ("夜间模式", r["theme"])):
                    if box is None:
                        bad.append("%s %s 上没有%s" % (label, path, what))
                    elif box["w"] < 20 or box["h"] < 20:
                        bad.append("%s %s 的%s尺寸是 %dx%d —— 大概是被塞进了一个"
                                   "手机上 display:none 的容器里"
                                   % (label, path, what, box["w"], box["h"]))
                    elif box["x"] < -1 or box["right"] > r["vw"] + 1:
                        bad.append("%s %s 的%s跑到屏幕外：x=%d right=%d（屏幕 %d）"
                                   % (label, path, what, box["x"],
                                      box["right"], r["vw"]))

                # ③ 页头不许自己压自己
                ta, la = r["title"], r["lang"]
                if ta and la and la["w"] > 0:
                    ox = min(ta["right"], la["right"]) - max(ta["x"], la["x"])
                    oy = min(ta["bottom"], la["bottom"]) - max(ta["y"], la["y"])
                    if ox > 1 and oy > 1:
                        bad.append("%s %s 语言切换压住站名 %dx%dpx"
                                   % (label, path, ox, oy))
                # ⑥ 信息流的滚动行为：切页签要回到标签行，返回要停在原位。
                #    这两条只在**行为**上看得见，静态检查一点异常都发现不了 ——
                #    页面正常渲染、链接都通、样式也对，只是每次换个页签就落在
                #    新一批卡片的中间，前面那些永远不会被看到。
                if path in ("/", "/tw/", "/en/"):
                    beh = pg.evaluate("""() => {
                      const tabs = document.querySelectorAll('#hwx-tabs2 button');
                      if (tabs.length < 2) return null;
                      const bar = document.getElementById('hwx-tabs2');
                      window.scrollTo(0, 2000);
                      const before = window.scrollY;
                      const off = [...tabs].find(b => !b.classList.contains('on'));
                      if (!off) return null;
                      off.click();
                      const after = window.scrollY;
                      const barTop = bar.getBoundingClientRect().top + window.scrollY;
                      return {before, after, barTop,
                              saves: typeof sessionStorage !== 'undefined'};
                    }""")
                    if beh and beh["before"] > beh["barTop"] + 40 \
                            and beh["after"] >= beh["before"] - 40:
                        bad.append("%s %s 切页签没有把信息流带回标签行"
                                   "（切前 %d，切后 %d，标签行在 %d）"
                                   % (label, path, beh["before"],
                                      beh["after"], beh["barTop"]))

                # ⑤ 文字放不进框：被裁的内容读者永远看不到，而页面上
                #    一点异常都看不出来 —— 它只是「短了一截」。
                for x in (r.get("clipped") or [])[:3]:
                    bad.append("%s %s %s" % (label, path, x))

                # ④ 站名必须一行。它是一个**名字**，断成两行不是排版，是把
                #    名字拆了。③ 只保证不重叠，而「不重叠」可以靠把站名压窄
                #    来达成 —— 那正是之前那一版：「Human World」/「Rules」。
                if ta:
                    lh = r.get("titleLine") or 0
                    if lh and ta["h"] > lh * 1.6:
                        bad.append("%s %s 站名断成了 %d 行"
                                   % (label, path, round(ta["h"] / lh)))

                # ⑦ 章节页读完之后，读者要能说一句自己的。
                #    这一块是站里做共情的地方，顺序是：四条别人的问句 →
                #    你呢 → 转发。原来是「你不是一个人 → 转给别人」，读者
                #    从头到尾没有一次开口的机会 —— 在他最可能想「这说的就是
                #    我」的那一秒，站点的下一句是「转发出去」。
                #    输入框由 hw-chat.js 运行时生成，静态扫不到，只能在浏览器
                #    里验：在不在、接没接上 hwAsk、顺序对不对。
                # 章节页 = `i` 后面还有两段（人 / 篇）。拿斜杠数量判会
                # 把 /tw/i/su-shi/ 这种**条目页**也算进来 —— 条目页本来
                # 就没有这一块，报出来的是假警报。
                _seg = [x for x in path.split("/") if x]
                _is_ch = "i" in _seg and len(_seg) - _seg.index("i") == 3
                if _is_ch:
                    y = r.get("yours")
                    if not y:
                        bad.append("%s %s 没有「还有人这么问」那一块"
                                   % (label, path))
                    else:
                        if not (y["ta"] and y["go"]):
                            bad.append("%s %s 读完之后没有让读者说一句的输入框"
                                       % (label, path))
                        elif not (y["ph"] or "").strip():
                            bad.append("%s %s 输入框没有占位文字（空框子等于让"
                                       "读者先想「我该说什么」，那一步就是流失点）"
                                       % (label, path))
                        if y.get("ask") != "function":
                            bad.append("%s %s 上 window.hwAsk 不在，输入框问不出去"
                                       % (label, path))
                    # 窄屏上不该出现那排 01/02 章内导航：它是侧栏里的目录，
                    #    中文站靠 force_chapter_ui 注的
                    #    `@media(max-width:900px){aside.side{display:none}}`
                    #    收起来 —— 而那个函数只走 i/，英文站一页都没拿到，
                    #    于是英文手机上面包屑底下多出一排横滚胶囊。
                    #    判据放在「渲染出来看不看得见」，不是「样式在不在」。
                    if y and y.get("toc"):
                        bad.append("%s %s 窄屏上露出了章内目录（那排 01/02）——"
                                   "侧栏没被收起来" % (label, path))
                    if not (y.get("tail") or "").startswith("arow"):
                            bad.append("%s %s 那一块顺序不对（末两个是 %s）——"
                                       "导航夹在问句和输入框中间，会把"
                                       "「他们问 → 你呢」这条线打断"
                                       % (label, path, y.get("tail")))
            b.close()
    finally:
        srv.shutdown()

    print("窄屏 %dpx：量了 %d 页" % (WIDTH, checked))
    if bad:
        print("\n不合格：")
        for x in bad:
            print("  ✗ " + x)
        return 1
    print("✓ 三种语言在 375px 下都不横向滚动、语言切换和夜间模式都在且可点、"
          "页头不自己压自己、站名一行、文字都放得进框、切页签回到标签行")
    return 0


if __name__ == "__main__":
    sys.exit(main())
