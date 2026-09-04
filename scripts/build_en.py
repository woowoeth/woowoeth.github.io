#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the English site into /en/.

    python3 scripts/build_en.py

Why this is not shaped like build_tw.py: the Traditional site is a *conversion*
of the built Simplified tree, so it can be produced by walking the output. The
English site shares no sentences with it — every string is written by hand — so
there is nothing to convert. What it does share is the templates, and those are
worth sharing: a second copy of the renderer would drift from the first within
a month.

So the English site is the ordinary generators pointed at English data:

    seo/chapters_en/*.py     chapters, same shape as seo/chapters/*.py
    scripts/hwx_scenes_en.py the situation layer, the front door for /en/
    scripts/quote_asks_en.py today's line
    seo/en_ui.py             the interface strings

The one trick worth naming: after the English data is rendered, **anything
still in Chinese on the page is interface, by definition** — the content is
already English. That is how seo/en_ui.py was enumerated, and it is why
scripts/check_en.py can fail the build on a single CJK character left in /en/.
No guessing at how many interface strings there are; the page says.

Three rules carried over from the Traditional build, each of which cost
something to learn there:

① URLs must not go through any text substitution. They are stashed behind
   private-use placeholders first. (Not \\x00 — that one truncates C-string
   backends and fills hrefs with body text.)
② canonical and og:url point at this page; hreflang stays identical across all
   language versions, because it describes where the *others* are.
③ Long strings are replaced before short ones. Replacing 分享 before 分享本页
   leaves "Share本页" behind.
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

OUT = os.path.join(ROOT, "en")
# 站点配置直接借 build_seo 那一份：它本来就带英文的 name/tagline/description
# （中文站用的是同一个对象的 *_zh 字段）。生成出来的地址是 /i/<slug>/，
# 随后由 finish() 统一改指 /en/ —— 和章节页走同一条路。

# URL 长这样，不能进替换
URLISH = re.compile(r"^(https?:|//|/|#|\.\.?/|mailto:|data:)")
ATTR = re.compile(r'\b(href|src|action|srcset|content|data-u|url)\s*=\s*"([^"]*)"')
# 目录白名单里**不能有 en**：ATTR 已经把 href 加过一次 /en 前缀，
# 若 en 在这张表里，JSURL 会认出 "/en/assets/…" 再加一次，变成 /en/en/。
JSURL = re.compile(r"""(fetch\(|import\(|['"])(/(?:assets|i|t|all|api)/[^'"()]*)(['"]|\))""")

# 语言标记：转换碰不到这些，它们是标记不是正文。漏了的后果是搜索引擎和
# 分享卡片把英文页按简体中文归类 —— 页面看着全对，只有翻 head 才看得见。
LOCALE = [
    ('<html lang="zh-Hans"', '<html lang="en"'),
    ('property="og:locale" content="zh_CN"', 'property="og:locale" content="en_US"'),
    ('"inLanguage":["en","zh-Hans"]', '"inLanguage":"en"'),
    ('"inLanguage":"zh-Hans"', '"inLanguage":"en"'),
    ('"inLanguage": "zh-Hans"', '"inLanguage": "en"'),
    ("<language>zh-cn</language>", "<language>en</language>"),
    ("<language>zh-CN</language>", "<language>en</language>"),
    ('"lang": "zh-CN"', '"lang": "en"'),
]

# 思源宋体简体不含合适的西文字形，英文页用 Noto Serif 的拉丁族。
FONT = [("Noto+Serif+SC", "Noto+Serif"), ("Noto Serif SC", "Noto Serif")]

# 赞赏码：英文页用 AlipayHK，和繁体站同一个。大陆个人收款码在境外收不了；
# AlipayHK 港澳读者用得上，**欧美读者用不了**（注册要香港手机号）。
# 已知缺口，等接了卡支付回来改这一处。
ALIPAY_HK_LINK = ("https://render.alipay.com/p/yuyan/180020010001270667/landing/"
                  "income.html?qrcode=https://qr.alipay.hk/281004010499ha1j0b9kg7PhWd30nLZv4Zfa")
PAY = [
    ("/assets/pay-alipay.png", "/assets/pay-alipayhk.png"),
    ("https://qr.alipay.com/fkx10243q5q41avrifvyj24", ALIPAY_HK_LINK),
]


def protect(s):
    keep = []

    def stash(v):
        keep.append(v)
        return "%d" % (len(keep) - 1)

    def attr(m):
        name, val = m.group(1), m.group(2)
        if URLISH.match(val) or "%" in val:
            return '%s="%s"' % (name, stash(val))
        return m.group(0)

    s = ATTR.sub(attr, s)
    s = JSURL.sub(lambda m: m.group(1) + stash(m.group(2)) + m.group(3), s)
    return s, keep


def restore(s, keep):
    return re.sub("(\\d+)", lambda m: keep[int(m.group(1))], s)


from lang_urls import fix_urls, sister, prefix  # noqa: E402

# 英文站不复制资源：CSS、JS、字体、图片一律用主站那一份，所以 assets=False。
# 加了 /en 前缀就指向不存在的 /en/assets/，线上是一页没有样式的裸 HTML，
# 而构建全程不报错。
ASSETS = False


def retarget(s, rel=None):
    """站内地址指到 /en/ 下；hreflang 那几行不动（它说的是别人在哪）。

    姊妹站、资源不加前缀、JSON-LD 三条规则见 scripts/lang_urls.py，
    那三条各自对应一次真实事故。
    """
    def one(m):
        name, val = m.group(1), m.group(2)
        # 跳转桩写的是 content="0;url=https://…"，前面带个秒数，
        # URLISH 认不出它是地址。漏掉的后果：繁体的分类跳转桩
        # tw/t/权力治理/ 把读者弹到**简体**的 /t/power/ 去。
        if name == "content" and re.match(r"^\s*\d+\s*;\s*url=", val, re.I):
            pre, u = re.split(r"(?i)url=", val, 1)
            b = u.replace("https://ourword.ai", "", 1) if u.startswith("https://") else u
            sis = sister(b, "en")
            nb = sis if sis is not None else prefix(b, "en", ASSETS)
            return '%s="%surl=%s"' % (name, pre, u.replace(b, nb, 1))
        bare = val.replace("https://ourword.ai", "", 1) if val.startswith("https://") else val
        sis = sister(bare, "en")
        if sis is not None:
            return '%s="%s"' % (name, val.replace(bare, sis, 1))
        if val.startswith("/"):
            val = prefix(val, "en", ASSETS)
        elif val.startswith("https://ourword.ai/") and "/en/" not in val:
            val = "https://ourword.ai" + prefix(bare, "en", ASSETS)
        return '%s="%s"' % (name, val)

    holes = []
    s = re.sub(r'<link rel="alternate"[^>]*>',
               lambda m: holes.append(m.group(0)) or "\ue002%d\ue003" % (len(holes) - 1), s)
    # 跳转桩的 content="0;url=…" 以数字开头，URLISH 认不出来，
    # 得单独放行进 one() —— 否则上面那段处理它的分支永远不会被调用。
    REFRESH = re.compile(r"^\s*\d+\s*;\s*url=", re.I)
    s = ATTR.sub(lambda m: one(m) if (URLISH.match(m.group(2)) or "%" in m.group(2)
                                      or REFRESH.match(m.group(2)))
                 else m.group(0), s)
    s = JSURL.sub(lambda m: m.group(1) + prefix(m.group(2), "en", ASSETS) + m.group(3), s)
    # 通用的一遍：属性之外的地址（JSON-LD、script、链接文字）也要改。
    # 这里同时把「本页指向自己」那几处改对了，所以不再单独跑 self_url。
    s = fix_urls(s, "en", ASSETS)
    s = re.sub("\ue002(\\d+)\ue003", lambda m: holes[int(m.group(1))], s)
    return s


def finish(s, rel=None):
    """一页渲染好之后统一做的四件事，顺序有意义。"""
    import en_ui
    kept, keep = protect(s)          # ① URL 先藏起来
    kept = en_ui.apply(kept)         # ② 界面串（表内已按长度降序）
    s = restore(kept, keep)
    s = retarget(s, rel)             # ③ 站内地址改指 /en/（含自指地址）
    for a, b in FONT + LOCALE + PAY:  # ④ 字体、语言标记、收款码
        s = s.replace(a, b)
    return s



# 英文条目页：用同一套 geo_kit 生成器，喂英文数据。
# 分块标题在这里就写成英文，不走 en_ui 的替换 —— 它们是内容结构的一部分，
# 而不是界面装饰，写在这里比让替换表去猜更清楚。
EN_ERA = [(-221, "Pre-Qin and classical"), (589, "Qin, Han and the Six Dynasties"),
          (1368, "Medieval"), (1800, "Early modern"), (1945, "The industrial age")]


def _era(y):
    if y is None:
        return ""
    for cut, name in EN_ERA:
        if y < cut:
            return name
    return "Modern"


def _flat(v):
    """列表/字典拍平成一段文本。build_seo 里有同名函数，但它用中文全角冒号
    连接「名字：理由」，英文站不能借用。"""
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    out = []
    for x in (v if isinstance(v, list) else [v]):
        if isinstance(x, dict):
            head = x.get("n") or x.get("name") or ""
            body = x.get("why") or x.get("d") or ""
            out.append((head + " \u2014 " + body).strip(" \u2014") if head or body else "")
        else:
            out.append(str(x))
    return "\n".join(t for t in out if t)


def en_items():
    """把 seo/en_entries.py 变成 geo_kit 的 Item 列表。"""
    import geo_kit as G
    import hw_kind
    from en_entries import ENTRIES

    names = {e["n"] for e in ENTRIES}
    items = []
    for e in ENTRIES:
        # 反向补齐：A 说和 B 对照着读，B 那页也该看得见 A。
        # 中文那边靠 rev_l / rev_c 做，这里同理，否则互引只有单向。
        rel = list(e.get("l") or [])
        for o in ENTRIES:
            if e["n"] in (o.get("l") or []) and o["n"] not in rel and o["n"] != e["n"]:
                rel.append(o["n"])
        ctr = [dict(c) for c in (e.get("contrast") or [])]
        seen_c = {c["n"] for c in ctr}
        for o in ENTRIES:
            for c in (o.get("contrast") or []):
                if c.get("n") == e["n"] and o["n"] not in seen_c and o["n"] != e["n"]:
                    seen_c.add(o["n"])
                    ctr.append({"n": o["n"], "why": c.get("why", "")})
        assert not ({x for x in rel} | seen_c) - names, e["slug"]

        blocks = [("Q: What did this one leave behind?", e["d"]),
                  ("Q: What actually happened?", e["story"])]
        for f in e.get("f") or []:
            body = f.get("d") or ""
            if f.get("eg"):
                body += "\ne.g. " + f["eg"]
            blocks.append(("The parts \u00b7 %s" % f.get("n", ""), body))
        if e.get("apply"):
            blocks.append(("Q: How do I use it today?", e["apply"]))
        if e.get("q"):
            blocks.append(("Lines to keep", _flat(e["q"])))
        if ctr:
            blocks.append(("Q: What should I read alongside?", _flat(ctr)))
        if rel:
            blocks.append(("Further", _flat(rel)))

        one, era = e.get("w") or "", e.get("e") or ""
        summary = "%s%s \u2014 %s. %s" % (
            e["n"], (" (%s)" % era if era else ""), one, G.plain(e.get("d"), 140))
        is_text = hw_kind.is_work(e["n"])
        extra = {"about": one} if one else {}
        if is_text:
            extra["bookFormat"] = "https://schema.org/Hardcover"
        items.append(G.Item(
            slug=e["slug"], title=e["n"], summary=summary, blocks=blocks,
            tags=[t for t in [e.get("c"), _era(e.get("y")), one] if t],
            updated="", schema_type="Book" if is_text else "Person",
            schema_extra=extra))
    items.sort(key=lambda i: i.title)
    return items



HOME_CSS = """
.hero{margin:34px 0 10px}
.hero h1{font-size:clamp(28px,5vw,40px);line-height:1.15;margin:0 0 10px}
.hero .lede{font-size:17px;line-height:1.6;color:var(--muted,#6b6357);max-width:44em;margin:0}
.sec-h{margin:44px 0 6px;font-size:13px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted,#6b6357)}
.sec-s{margin:0 0 16px;color:var(--muted,#6b6357);font-size:15px}
.grp{margin:0 0 22px}
.grp-n{font-size:15px;font-weight:600;margin:0 0 8px}
.chips{display:flex;flex-wrap:wrap;gap:7px}
.chip2{border:1px solid var(--line,#e2ddd0);background:var(--paper,#f5f1e8);
  color:var(--ink,#1c1917);font:inherit;font-size:14px;line-height:1.3;padding:6px 12px;
  border-radius:15px;cursor:pointer}
.chip2:hover{border-color:var(--acc,#9d2933);color:var(--acc,#9d2933)}
.chip2[aria-expanded=true]{background:var(--acc,#9d2933);border-color:var(--acc,#9d2933);
  color:#fff}
.qs{margin:10px 0 0;padding:14px 16px;border:1px solid var(--line,#e2ddd0);
  border-radius:10px;background:var(--surface,#fff)}
.qs[hidden]{display:none}
.q{margin:0 0 12px}
.q:last-child{margin-bottom:0}
.q-t{margin:0 0 4px;font-size:16px;line-height:1.45}
.q-a{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:14px}
.q-a a{color:var(--muted,#6b6357);text-decoration:none;border-bottom:1px solid
  var(--line,#e2ddd0)}
.q-a a:hover{color:var(--acc,#9d2933);border-color:var(--acc,#9d2933)}
"""


def _home_body(items):
    """首页正文：处境层在前，条目在后。

    这一版三十个条目里，英文读者认得的只有荣格、丘吉尔、蒙台梭利几个，
    所以入口不能是名字墙 —— 读者是搜「I got passed over」进来的，
    不是搜「Su Shi」。名字放在处境下面。
    """
    import json
    from hwx_scenes_en import SCENES
    import collections

    groups = collections.OrderedDict()
    for scene, grp, qs in SCENES:
        groups.setdefault(grp, []).append(scene)
    data = {}
    for scene, grp, qs in SCENES:
        data[scene] = [[q, [["/en/i/%s/%s/" % r, r[0]] for r in refs]] for q, refs in qs]

    name_of = {it.slug: it.title for it in items}
    for v in data.values():
        for _q, refs in v:
            for r in refs:
                r[1] = name_of.get(r[1], r[1])

    out = ['<div class="hero"><h1>See how people before you handled it.</h1>'
           '<p class="lede">Thirty people and books, seventy-nine deep reads. '
           'Start from where you are, not from a name you already know \u2014 '
           'most of these are strangers, and that is the point.</p></div>']
    out.append('<p class="sec-h">Situations</p>')
    out.append('<p class="sec-s">Pick the one that fits. Every question opens '
               'onto what somebody already worked out about it.</p>')
    for grp, scenes in groups.items():
        out.append('<div class="grp"><p class="grp-n">%s</p><div class="chips">' % grp)
        for sc in scenes:
            out.append('<button class="chip2" type="button" aria-expanded="false" '
                       'data-s="%s">%s</button>' % (esc(sc), esc(sc)))
        out.append('</div></div>')
    out.append('<div class="qs" id="qs" hidden></div>')

    out.append('<p class="sec-h">Everyone</p>')
    out.append('<p class="sec-s">The thirty in this first batch.</p>')
    out.append('<div class="feed">')
    for it in items:
        out.append('<a href="/en/i/%s/"><span class="k">%s</span><strong>%s</strong>'
                   '<span class="s">%s</span></a>'
                   % (it.slug, esc(it.tags[0] if it.tags else ""), esc(it.title),
                      esc(it.summary[:150])))
    out.append('</div>')

    out.append("<script>var HWQ=%s;(function(){"
               "var box=document.getElementById('qs');"
               "document.querySelectorAll('.chip2').forEach(function(b){"
               "b.onclick=function(){"
               "var open=b.getAttribute('aria-expanded')==='true';"
               "document.querySelectorAll('.chip2').forEach(function(x){"
               "x.setAttribute('aria-expanded','false')});"
               "if(open){box.hidden=true;return}"
               "b.setAttribute('aria-expanded','true');"
               "var qs=HWQ[b.getAttribute('data-s')]||[];"
               "box.innerHTML=qs.map(function(q){return '<div class=\"q\">'"
               "+'<p class=\"q-t\">'+q[0]+'</p><div class=\"q-a\">'"
               "+q[1].map(function(r){return '<a href=\"'+r[0]+'\">'+r[1]+'</a>'}).join('')"
               "+'</div></div>'}).join('');"
               "box.hidden=false;"
               "b.parentNode.parentNode.insertAdjacentElement('afterend',box);"
               "box.scrollIntoView({block:'nearest'})}})})();</script>"
               % json.dumps(data, ensure_ascii=False))
    return "\n".join(out)


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def write_home(items):
    """英文首页：借 /en/all/ 那一页的外壳，换掉正文。

    外壳（head、页眉、页脚、CSS 链接）照搬，是为了和站里其他页一模一样 ——
    自己再写一套 head，迟早和别的页走散。中文首页那 1MB 的机器不搬：
    它的处境层数据由 _hwx_payload() 生成，而那个函数是围着中文写的
    （解析「局面：」、按汉字数挑金句、剥句号），英文化是重写不是参数化。
    """
    import re
    src = os.path.join(OUT, "all", "index.html")
    if not os.path.exists(src):
        return 0
    s = open(src, encoding="utf-8").read()
    i, j = s.index("<div class=\"wrap\">", s.index("</header>")), s.rindex("<footer")
    title = "Human World Rules \u2014 see how people before you handled it"
    desc = ("Thirty people and books on how the world actually works, and "
            "seventy-nine deep reads. Find yours by the situation you are in.")
    head = s[:i]
    head = re.sub(r"<title>[^<]*</title>", "<title>%s</title>" % title, head)
    head = re.sub(r'(<meta name="description" content=")[^"]*"',
                  r"\g<1>%s\"" % desc, head)
    head = re.sub(r'((?:og|twitter):title" content=")[^"]*"', r"\g<1>%s\"" % title, head)
    head = re.sub(r'((?:og|twitter):description" content=")[^"]*"',
                  r"\g<1>%s\"" % desc, head)
    head = head.replace("https://ourword.ai/en/all/", "https://ourword.ai/en/")
    head = head.replace("https://ourword.ai/all/", "https://ourword.ai/")
    head = head.replace("https://ourword.ai/tw/all/", "https://ourword.ai/tw/")
    head = head.replace("</head>", "<style>%s</style></head>" % HOME_CSS)
    body = '<div class="wrap">\n' + _home_body(items) + "\n"
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        head + body + s[j:])
    return 1


def main():
    os.environ["HW_CHAPTERS"] = "chapters_en"
    os.environ["HW_SCENES"] = "hwx_scenes_en"
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)

    cwd = os.getcwd()
    os.chdir(os.path.join(ROOT, "seo"))
    try:
        import geo_kit as G
        import hw_chapters
        from build_seo import SITE, fill_counts
        items = en_items()
        fill_counts(SITE, len(items))
        rep = G.build(SITE, items, root=OUT, item_pages=True, robots=False,
                      sitemap=True, hubs=False,
                      today=__import__("datetime").date.today().isoformat(),
                      extra_urls=[u.replace("https://ourword.ai/",
                                            "https://ourword.ai/en/")
                                  for u in hw_chapters.chapter_urls()])
        n_ch = hw_chapters.write_chapters(root=OUT)
    finally:
        os.chdir(cwd)
    print("English entries: %d pages" % rep.get("pages", 0))
    sys.path.insert(0, HERE)
    print("English home page: %d" % write_home(items))

    # 三个挂件整块从已构建的简体页里原样搬过来，再由 finish() 统一翻标签、
    # 改资源路径。自己再写一份的话，两边的配色和行为迟早对不上。
    #
    # 聊天挂件是一份文件两种语言：assets/hw-chat.js 自己看 location.pathname，
    # /en/ 下就换英文串、换英文检索索引、请求里带 lang:'en'（Worker 据此
    # 换一套英文系统提示词）。所以这里不需要为英文另搬一份资源。
    #
    # 赞赏码换成 AlipayHK，和繁体站同一个：大陆个人码在境外收不了，
    # AlipayHK 至少港澳读者用得上。**欧美读者两个都用不了** —— 这是个已知
    # 缺口，等接了卡支付再回来改这里。
    src = os.path.join(ROOT, "i", "su-shi", "no-wind-no-rain", "index.html")
    blocks = []
    if os.path.exists(src):
        t = open(src, encoding="utf-8").read()
        for a, b in (("<!--HWX:THEME-->", "<!--/HWX:THEME-->"),
                     ("<!--HWX:CHAT-->", "<!--/HWX:CHAT-->"),
                     ("<!--HWX:TEA-->", "<!--/HWX:TEA-->")):
            if a in t and b in t:
                blocks.append((a, t[t.index(a):t.index(b) + len(b)]))
    for dp, _dn, fn in os.walk(OUT):
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            p_ = os.path.join(dp, f)
            x = open(p_, encoding="utf-8").read()
            if "</body>" not in x:
                continue
            add = "".join(blk for mark, blk in blocks if mark not in x)
            if add:
                open(p_, "w", encoding="utf-8").write(
                    x.replace("</body>", add + "</body>", 1))

    # 三语层：和简体、繁体共用 scripts/hwx_lang.py 的同一份实现。
    # 分成两处写的话 hreflang 迟早走散，而走散了不报错，只是搜索引擎
    # 认不出这几页是同一篇。
    import hwx_lang
    hwx_lang.patch_tree("en")

    n_fix = 0
    for dp, _dn, fn in os.walk(OUT):
        for f in fn:
            if not f.endswith((".html", ".xml", ".txt", ".json")):
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding="utf-8").read()
            rel = os.path.relpath(p, OUT).replace(os.sep, "/")
            rel = "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)
            open(p, "w", encoding="utf-8").write(finish(s, rel))
            n_fix += 1

    print("English site: %d chapter pages rendered, %d files localised" % (n_ch, n_fix))
    return 0


if __name__ == "__main__":
    sys.exit(main())
