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
# 整条 Google Fonts 链接换掉，不是逐个字体名替换：英文要的是另外两个族
# （Newsreader 做标题、Source Serif 4 做正文），字重也不一样。
# 具体的变量覆盖在 assets/hw-entry.css 末尾的 html[lang="en"] 块里。
EN_DISPLAY = '"Newsreader",Georgia,"Times New Roman",serif'
EN_SANS = ('-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,'
           '"Helvetica Neue",Arial,sans-serif')
EN_READ = '"Source Serif 4",Georgia,"Times New Roman",serif'

FONT = [
    ("https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700;900"
     "&display=swap",
     "https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;"
     "6..72,600;6..72,700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600"
     "&display=swap"),
    ("https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700"
     "&display=swap",
     "https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;"
     "6..72,600;6..72,700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600"
     "&display=swap"),
    # 首页不引 hw-entry.css，字体族是直接写死在内联 <style> 里的，所以
    # html[lang="en"] 那套变量覆盖够不到它 —— 必须在这里逐个换掉字体栈。
    # 长的排在前面：短的会先吃掉长栈的一截，剩下半截换不干净。
    ('"Songti SC","Noto Serif CJK SC","Source Han Serif SC",Georgia,serif',
     EN_DISPLAY),
    ('"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif',
     EN_DISPLAY),
    ('"Noto Serif SC","Songti SC","STSong",serif', EN_DISPLAY),
    ('"Noto Serif SC","Songti SC",serif', EN_DISPLAY),
    ('-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC",'
     '"Noto Sans SC","Hiragino Sans GB",sans-serif', EN_SANS),
    ('"PingFang SC","HarmonyOS Sans SC","Hiragino Sans GB","Microsoft YaHei",'
     '-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif', EN_SANS),
    # 兜底：漏网的字体名换成拉丁族，别把 CJK 字体名留在英文页上
    ("Noto+Serif+SC", "Source+Serif+4"),
    ("Noto Serif SC", "Source Serif 4"),
]

# 赞赏码：英文页用 AlipayHK，和繁体站同一个。大陆个人收款码在境外收不了；
# AlipayHK 港澳读者用得上，**欧美读者用不了**（注册要香港手机号）。
# 已知缺口，等接了卡支付回来改这一处。
ALIPAY_HK_LINK = ("https://render.alipay.com/p/yuyan/180020010001270667/landing/"
                  "income.html?qrcode=https://qr.alipay.hk/281004010499ha1j0b9kg7PhWd30nLZv4Zfa")
PAY = [
    ("/assets/pay-alipay.png", "/assets/pay-alipayhk.png"),
    ("https://qr.alipay.com/fkx10243q5q41avrifvyj24", ALIPAY_HK_LINK),
]


# ── 英文排版 ────────────────────────────────────────────────
# 这段 CSS 由构建**生成**成 assets/hw-en.css，不是手写在 hw-entry.css
# 末尾的。写在那里试过两次，两次都丢：hw-entry.css 是中文站的样式表，
# 谁碰一下、哪次回滚一下，尾巴上这块就没了，而且没有任何闸看得见 ——
# 字体链接照旧下载 Newsreader，页面照旧拿宋体渲染拉丁字母。
#
# 为什么英文非得单独一套：中文字体（PingFang SC / 宋体 / 思源宋体）里的
# 西文字形是**配汉字设计的** —— 字宽被压成半角以对齐字身框，重心偏高，
# 斜体多半是机器倾斜。一行中英混排看不出来，整页英文长文就是「哪里不对
# 但说不出」。
#
# 分工：Newsreader 做标题（带 optical sizing，大字号收得住），
# Source Serif 4 做正文（为屏幕阅读设计，x 高度够），
# 界面文字（导航、胶囊、按钮）留给系统无衬线 —— 12px 的衬线不够清晰。
EN_CSS = """/* 由 scripts/build_en.py 生成，别手改 —— 改这里的话下次构建就没了。 */
html[lang="en"]{
  --display:%(disp)s;
  --quote:%(disp)s;
  --read:%(read)s;
  --sans:%(sans)s;
  /* 站名那几条带 !important（要压住首页内联样式），所以只能从值这一层
     覆盖 —— 见 assets/hw-home-lockup.css 里同一处的注释。 */
  --brand-serif:%(disp)s;
  --brand-track:0;
}
html[lang="en"] body{font-family:var(--sans)}
html[lang="en"] article,
html[lang="en"] .dek,
html[lang="en"] .lede,
html[lang="en"] .idx{font-family:var(--read)}
html[lang="en"] h1,
html[lang="en"] h2,
html[lang="en"] .one,
html[lang="en"] .hd-title,
html[lang="en"] .point h2{font-family:var(--display)}
html[lang="en"] blockquote{font-family:var(--quote)}
/* 字距是给汉字调的：汉字是方块，拉开一点更透气；拉丁字母的字距字体里
   已经调好了，再加 .04em 就散。标题类归零偏紧一点，小标签留一点点。 */
html[lang="en"] h1,
html[lang="en"] .one,
html[lang="en"] .hd-title,
html[lang="en"] .point h2{letter-spacing:-.011em}
html[lang="en"] .kicker,
html[lang="en"] .sec-k{letter-spacing:.008em}
""" % {"disp": EN_DISPLAY, "read": EN_READ, "sans": EN_SANS}
EN_CSS_HREF = "/assets/hw-en.css?v=1"


def write_en_css():
    """写出英文样式表。放在 /assets/ 下和其他样式表同级。"""
    p = os.path.join(ROOT, "assets", "hw-en.css")
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    if old != EN_CSS:
        open(p, "w", encoding="utf-8").write(EN_CSS)
    return len(EN_CSS)


def link_en_css(s):
    """把英文样式表挂到 </head> 前 —— 必须排在所有其他样式表后面，
    否则同等权重的规则会被后面的盖回去。首页的字体族是写死在内联
    <style> 里的，那一层靠 FONT 表逐个换栈，不靠这个文件。"""
    if EN_CSS_HREF in s or "</head>" not in s:
        return s
    tag = '<link rel="stylesheet" href="%s">' % EN_CSS_HREF
    i = s.rindex("</head>")
    return s[:i] + tag + s[i:]


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
    """一页渲染好之后统一做的五件事，顺序有意义。"""
    import en_ui
    kept, keep = protect(s)          # ① URL 先藏起来
    kept = en_ui.apply(kept)         # ② 界面串（表内已按长度降序）
    s = restore(kept, keep)
    s = retarget(s, rel)             # ③ 站内地址改指 /en/（含自指地址）
    for a, b in FONT + LOCALE + PAY:  # ④ 字体、语言标记、收款码
        s = s.replace(a, b)
    # ⑤ 英文样式表挂在最后：retarget 之后再挂，它才不会被改写成
    #    /en/assets/（那个路径下没有文件，挂上去等于没挂）。
    return link_en_css(s)



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
            t = (head + " \u2014 " + body).strip(" \u2014") if head or body else ""
            # 「名字 — 理由」这类条目必须自己收尾。它们会被拍进 FAQ 的
            # JSON-LD，而那一层把换行折成空格 —— 不收尾的话
            # 「…refuses to be defined by losing it C.S. Lewis — …」
            # 两条连成一句读不通的话。中文那边靠「。」天然分开，
            # 英文靠的是这一个句点。（纯名字的清单不加，加了像清单里
            # 每个人名后面都点一下。）
            if t and not t.endswith((".", "!", "?", "\u2026", ":")):
                t += "."
            out.append(t)
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




def _sub_once(s, pat, rep, what):
    import re
    new, n = re.subn(pat, lambda _m: rep, s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("英文首页：没找到要替换的 %s —— 中文首页的结构变了，"
                         "build_en.write_home 要跟着改" % what)
    return new


EN_ERAS = """const ERAS=[
{label:"800 BC \\u2013 200 BC",min:-800,max:-200},
{label:"200 BC \\u2013 AD 400",min:-200,max:400},
{label:"400 \\u2013 1400",min:400,max:1400},
{label:"1400 \\u2013 1800",min:1400,max:1800},
{label:"1800 \\u2013 1950",min:1800,max:1950},
{label:"1950 \\u2013 now",min:1950,max:2100},
];"""


def write_home(items):
    """英文首页 = **克隆中文首页，换掉三个数据块**。

    第一版是自己另做了一个简版首页，理由是中文首页那 1MB 机器的处境数据
    由 _hwx_payload() 生成，而那个函数是围着中文写的。那是把「难做」说成
    「不该做」—— 结果英文读者少了搜索、分类筛选、年代筛选、每日金句、
    今日一问、最近看过，整整一层界面。

    正确的做法是同一套机器换数据：首页那套 JS 一行都不改，只把它读的数据块
    换成英文的。

      const D=[…]     30 个条目（字段与中文站同名，JS 才认得）
      var HWXD={…}    处境层负载，由 scripts/hwx_en.py 生成，形状与中文一致
      const ERAS=[…]  年代分档的标签
      const CATS      它是从 D 推出来的，只有两个字面量，走 en_ui

    剩下的界面文字由 finish() 里的 en_ui 处理 —— 和其他页同一条路。
    替换找不到就直接失败，不静默跳过：中文首页改了结构而这里没跟上，
    结果会是一个数据对不上的英文首页，比构建失败难发现得多。
    """
    import json
    sys.path.insert(0, HERE)
    from en_entries import ENTRIES
    import hwx_en

    src = os.path.join(ROOT, "index.html")
    if not os.path.exists(src):
        return 0
    s = open(src, encoding="utf-8").read()

    D = [{k: e[k] for k in ("c", "n", "e", "w", "y", "d", "story", "f", "q",
                            "apply", "l", "contrast") if k in e} for e in ENTRIES]
    s = _sub_once(s, r"const D=\[.*?\n\];",
                  "const D=" + json.dumps(D, ensure_ascii=False) + ";", "const D")
    s = _sub_once(s, r"var HWXD=\{.*?\};",
                  "var HWXD=" + hwx_en.payload() + ";", "HWXD")
    s = _sub_once(s, r"const ERAS=\[.*?\n\];", EN_ERAS, "ERAS")

    # 名字 → slug。中文站那份按中文名做键，英文页一个也对不上，
    # 而它是「延伸/对照着读」里的名字变成链接的唯一途径。
    slugs = {e["n"]: e["slug"] for e in ENTRIES}
    s = _sub_once(s, r"(?:var|const|let) HW_SLUGS\s*=\s*\{.*?\};",
                  "const HW_SLUGS=" + json.dumps(slugs, ensure_ascii=False) + ";",
                  "HW_SLUGS")

    # 金句解析：中文那份 17000 字按中文金句做键，英文金句一条也命中不了，
    # 留着只是白发 21KB。置空 —— 前端取不到就把解析区隐藏（DQX[t]||""），
    # 卡片本身照常显示引文、出处、分类和链接。
    # 要补的话得逐条写 90 句，是另一件事，不在这次范围里。
    s = _sub_once(s, r"const DQX=\{.*?\};", "const DQX={};", "DQX")

    # 每日金句的黑名单，中文那份列的是中文引文（「悔不用蒯通之计」之类），
    # 对英文没有意义。
    s = _sub_once(s, r"(?:var|const|let) DQ_DROP\s*=\s*\[.*?\];",
                  "const DQ_DROP=[];", "DQ_DROP")

    # 每日金句分享卡是 canvas 画的，字体在 DQ_FONT 里写死成汇文明朝体。
    # 不换的话英文金句会被宋体渲染 —— 西文字形是配汉字设计的，单独排一句
    # 英文重心和字宽都不对，而这张卡是要被读者存下来转发的。
    s = _sub_once(s, r"const DQ_FONT='[^']*';",
                  "const DQ_FONT='\"Newsreader\",Georgia,serif';", "DQ_FONT")

    # 哪些条目是「作品」不是「人」—— 前端据此说「it says」还是「he says」。
    # 中文那份列的是中文书名。这一批 30 个里，三个不是人。
    works = ["Excellent Sheep", "Rat Park", "Harvard Study of Adult Development"]
    s = _sub_once(s, r"const DQ_WORKS=new Set\(\[.*?\]\);",
                  "const DQ_WORKS=new Set(" + json.dumps(works, ensure_ascii=False) + ");",
                  "DQ_WORKS")

    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(s)
    return 1


def main():
    os.environ["HW_CHAPTERS"] = "chapters_en"
    os.environ["HW_SCENES"] = "hwx_scenes_en"
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    write_en_css()

    sys.path.insert(0, HERE)
    cwd = os.getcwd()
    os.chdir(os.path.join(ROOT, "seo"))
    try:
        import geo_kit as G
        import hw_chapters
        from build_seo import SITE, fill_counts
        items = en_items()
        fill_counts(SITE, len(items))
        # 首页要先克隆出来：G.build() 会往 index.html 里补 GEO:HEAD / GEO:BODY
        # 两块（给爬虫看的条目索引和站点自述）。文件还不存在时它什么也补不了，
        # 结果是英文首页里留着 159 条中文条目的索引 —— 那不是「界面没翻」，
        # 是整块数据都是别的站的。
        os.makedirs(OUT, exist_ok=True)
        n_home = write_home(items)
        # hubs=True：分类页（/en/t/<tag>/）必须建。关掉它不只是少了 41 个
        # 落地页 —— item_page() 是按「这个标签有没有 hub」决定分类胶囊是
        # <a> 还是死的 <span> 的，所以关掉之后英文条目页上「Mind and
        # feeling / Medieval」三颗胶囊全是不能点的字，读者从条目页没有任何
        # 横向浏览的出口，而中文版有。geo_kit 里 hub 页的英文文案本来就写好了。
        rep = G.build(SITE, items, root=OUT, item_pages=True, robots=False,
                      sitemap=True, hubs=True,
                      today=__import__("datetime").date.today().isoformat(),
                      extra_urls=[u.replace("https://ourword.ai/",
                                            "https://ourword.ai/en/")
                                  for u in hw_chapters.chapter_urls()])
        n_ch = hw_chapters.write_chapters(root=OUT)
    finally:
        os.chdir(cwd)
    print("English entries: %d pages · home %d" % (rep.get("pages", 0), n_home))

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
