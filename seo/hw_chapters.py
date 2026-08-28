# -*- coding: utf-8 -*-
"""Child essays hanging off a person/book map page. Not part of D[]."""
import os
from geo_kit import esc, SITE, head_block, ga_block, sibling_links, org_ld
import hw_theme

PARENTS = {
    "毛泽东": {
        "slug": "mao",
        "cat": "战略·博弈",
        "blurb": "先读这几篇，其余按需",
        "items": [
            {
                "k": "on-contradiction",
                "n": "矛盾论",
                "w": "一次只打一个结",
                "line": "一团乱麻里，先找那根一抽全松的线",
                "ready": True,
            },
            {"k": "on-practice", "n": "实践论", "w": "从事里认识", "line": "道理不从书里完成", "ready": False},
            {"k": "on-protracted-war", "n": "论持久战", "w": "时间换力量", "line": "弱的一方怎么把战争拖成自己能打的形状", "ready": False},
        ],
    }
}

CHAPTERS = [
    {
        "parent": "毛泽东",
        "parent_slug": "mao",
        "k": "on-contradiction",
        "n": "矛盾论",
        "w": "一次只打一个结",
        "src": "《矛盾论》（1937）",
        "dek": "事情同时在响，每件都像急事。这一篇要回答的不是怎么努力，是先打哪一个结：解了它，别的结自己会松。",
        "story": "1937 年在延安，毛把当时的乱局写成一张判断图：一个阶段里同时存在许多矛盾，只有一种起规定作用。抓住它，其余问题跟着改形状；抓错了，力气平摊给十件急事，看起来什么都在做，其实一件都没打穿。后来他打仗、整党、建国，重复的都是这一问：这一阶段的主要矛盾是什么。",
        "f": [
            {
                "n": "先找总开关",
                "d": "主要矛盾不是最急的事，也不是最难的事。是那件解了它，其他问题跟着改形状的事。没找到之前，动手越多，结打得越死。",
                "eg": "滴滴早期用户少、司机少、产品弱、对手凶，同时在响。总开关是司机够不够。钱全压在补贴司机上，循环才转起来。减肥先管嘴，转行先交出一个作品，都是同一条。",
            },
            {
                "n": "找到了还得敢砍",
                "d": "「伤其十指不如断其一指」。力量平摊等于没有力量。找到重点只是一半，敢为它放掉其他，才算抓住。",
                "eg": "找到重点的人很多。清单仍在变长、主项目仍交不出来的人，多半是还没敢砍。",
            },
            {
                "n": "阶段一变，结就变",
                "d": "主要矛盾不是固定的。用上一个阶段的打法，打这一个阶段的仗，必输。",
                "eg": "2021 年双减之后，新东方的主要矛盾从「怎么把教培做好」变成「这群人和这家公司怎么活」。还在旧打法里换马甲的同行越陷越深；承认昨天的仗打完了的那一方，才进了直播间。",
            },
        ],
        "apply": "局面：几件事同时在响，每件都像不能放。\n先问：只解哪一件，其余大半会自己松？\n用反了：清单还在变长，那件能带动其余的事仍交不出来；季度过了，打法还是上一个阶段的打法。",
        "q": [
            "在复杂的事物的发展过程中，有许多的矛盾存在，其中必有一种是主要的矛盾，由于它的存在和发展规定或影响着其他矛盾的存在和发展。",
            "捉住了这个主要矛盾，一切问题就迎刃而解了。",
            "伤其十指，不如断其一指。",
        ],
        "next_n": "实践论",
        "next_note": "下一篇将写《实践论》",
    }
]


def catalog_html(title):
    spec = PARENTS.get(title)
    if not spec:
        return ""
    rows = []
    for it in spec["items"]:
        if it.get("ready"):
            href = "/i/%s/%s/" % (spec["slug"], it["k"])
            rows.append(
                '<a class="map-row" href="%s">'
                '<span class="map-n">%s</span>'
                '<span class="map-w">%s</span>'
                '<span class="map-line">%s</span></a>'
                % (esc(href), esc(it["n"]), esc(it["w"]), esc(it["line"]))
            )
        else:
            rows.append(
                '<div class="map-row pending">'
                '<span class="map-n">%s</span>'
                '<span class="map-w">%s</span>'
                '<span class="map-line">%s</span></div>'
                % (esc(it["n"]), esc(it["w"]), esc(it.get("line") or "待写"))
            )
    return (
        '<section class="map-cat" id="map">'
        '<h2 class="sec-k">%s</h2>'
        '<div class="map-list">%s</div></section>'
        % (esc(spec["blurb"]), "".join(rows))
    )


def inject_catalog(blocks_html, title):
    chunk = catalog_html(title)
    if not chunk:
        return blocks_html
    for mark in ('<section id="contrast"', '<section id="ext"'):
        if mark in blocks_html:
            return blocks_html.replace(mark, chunk + mark, 1)
    return blocks_html + chunk


def _chapter_page(ch):
    parent = ch["parent"]
    parent_url = "%s/i/%s/" % (SITE, ch["parent_slug"])
    page_url = "%s/i/%s/%s/" % (SITE, ch["parent_slug"], ch["k"])
    title = "%s — %s — 人类世界生存法则" % (ch["n"], parent)
    points = []
    toc = [("s1", "这一篇在解决什么局面"), ("s2", "背后是什么故事")]
    for i, f in enumerate(ch["f"], 1):
        aid = "p%d" % i
        toc.append((aid, f["n"]))
        points.append(
            '<section class="point" id="%s"><h2>%s</h2><p>%s</p>%s</section>'
            % (
                aid, esc(f["n"]), esc(f["d"]),
                ('<p class="eg">%s</p>' % esc(f["eg"])) if f.get("eg") else "",
            )
        )
    toc += [("s7", "今天怎么用"), ("quotes", "原话")]
    quotes = "".join("<blockquote><p>%s</p></blockquote>" % esc(q) for q in ch["q"])
    apply_paras = "".join("<p>%s</p>" % esc(p) for p in ch["apply"].split("\n") if p.strip())
    toc_html = "".join(
        '<a href="#%s"><span class="i">%02d</span>%s</a>' % (esc(a), i, esc(n))
        for i, (a, n) in enumerate(toc, 1)
    )
    share = hw_theme._share_btn(title, page_url, "%s\n\n%s\n\n%s" % (ch["n"], ch["dek"], page_url))
    next_html = ""
    if ch.get("next_n"):
        next_html = (
            '<span class="sib-pending"><span class="dir">下一篇</span>%s</span>'
            % esc(ch.get("next_note") or ch["next_n"])
        )
    body = """
<header class="mast wrap">
  <div class="mast-top">
    %s
    <div class="mast-links">
      <a class="pill" href="%s">回%s</a>
      <a class="pill" href="%s/">首页</a>
    </div>
  </div>
</header>
<div class="wrap">
  <nav class="crumb">
    <a href="%s/">首页</a><span class="sep">/</span>
    <a href="%s">%s</a><span class="sep">/</span>%s
  </nav>
  <div class="layout">
    <article>
      <p class="kicker">%s · 骨干</p>
      <h1>%s</h1>
      <p class="one">%s</p>
      <p class="src">%s</p>
      <p class="dek">%s</p>
      <div class="meta-row"><span class="chip">%s</span><span class="chip">%s</span>%s</div>
      <aside class="pull">%s</aside>
      <section class="sec" id="s1"><h2 class="sec-k">这一篇在解决什么局面</h2>
      <p>%s</p></section>
      <section class="sec" id="s2"><h2 class="sec-k">背后是什么故事？</h2>
      <p>%s</p></section>
      %s
      <section class="sec apply" id="s7"><h2 class="sec-k">今天怎么用？</h2>%s</section>
      <section class="quotes" id="quotes"><h2 class="sec-k">原话</h2>%s</section>
    </article>
    <aside class="side"><div class="panel"><p class="ph">本篇结构</p><nav class="toc">%s</nav></div></aside>
  </div>
  <nav class="sib">
    <a href="%s"><span class="dir">回</span>%s</a>
    %s
  </nav>
  <footer class="site-foot">
    <p>本页可直接引用 <code>%s</code></p>
    <p>%s</p>
  </footer>
</div>
""" % (
        hw_theme.brand_html(SITE + "/", "毛泽东 · 骨干"),
        esc(parent_url), esc(parent), esc(SITE),
        esc(SITE), esc(parent_url), esc(parent), esc(ch["n"]),
        esc(parent), esc(ch["n"]), esc(ch["w"]), esc(ch["src"]), esc(ch["dek"]),
        esc(parent), esc(ch["w"]), share, esc(ch["dek"]),
        esc(ch["dek"]), esc(ch["story"]), "\n".join(points), apply_paras, quotes,
        toc_html, esc(parent_url), esc(parent), next_html,
        esc(page_url), sibling_links(None, True),
    )
    head = head_block(
        type("S", (), {"url": lambda self, p="": SITE + "/" + p, "base": SITE + "/",
                       "name": "Human World", "name_zh": "人类世界生存法则",
                       "zh": lambda self: True})(),
        page_url, title, ch["dek"], zh=True, ld=[org_ld()],
    ) if False else (
        '<meta name="description" content="%s">'
        '<link rel="canonical" href="%s">'
        '<meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s">'
        '<meta property="og:url" content="%s">'
        '<script type="application/ld+json">%s</script>'
        % (
            esc(ch["dek"]), esc(page_url), esc(title), esc(ch["dek"]), esc(page_url),
            esc('{"@context":"https://schema.org","@type":"Article","headline":"%s","url":"%s"}' % (ch["n"], page_url)).replace("&quot;", '"')
            if False else
            '{"@context":"https://schema.org","@type":"Article","headline":"%s","url":"%s"}' % (ch["n"], page_url),
        )
    )
    # fix ld json not escaped as html text incorrectly — write raw script
    head = (
        '<meta name="description" content="%s">\n'
        '<link rel="canonical" href="%s">\n'
        '<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n'
        '<meta property="og:url" content="%s">\n'
        '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"%s","url":"%s"}</script>\n'
        % (esc(ch["dek"]), page_url, esc(title), esc(ch["dek"]), page_url, ch["n"], page_url)
    )
    return hw_theme._shell("zh-Hans", title, head, body)


def write_chapters(root="."):
    n = 0
    for ch in CHAPTERS:
        path = os.path.join(root, "i", ch["parent_slug"], ch["k"], "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        html = _chapter_page(ch)
        open(path, "w", encoding="utf-8").write(html)
        n += 1
    return n
