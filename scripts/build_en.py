# 英文页按**杂志**排：Playfair Display 做标题，Source Serif 4 做正文。
# 杂志排法的要点是标题和正文分工，不是一个家族通吃 —— 标题要有编辑性格
# （高对比、字面收紧，压得住版面），正文要的是另一回事（耐读、字宽均匀、
# 一整页不累）。用同一个字体做两件事，标题不够抢，正文不够稳。
#
# 走到这一步试过四套：
#
#   ① 思源宋体（主站原来的样子）—— 那是**下载**下来的 CJK 网络字体，
#      它的西文是为「和汉字并排」设计的：窄、低对比、重心跟着汉字身框走。
#      单独排一整页英文就是「完全不适合阅读」。
#   ② Songti SC（照抄原声站）—— 不下载网络字体，落到系统自带的宋体。
#      比 ① 好，但它同样是 CJK 字体的配套西文：偏细、字宽不匀，
#      小段落还行，一整页长文撑不住。
#   ③ Source Serif 4 通篇 —— Adobe 专门为屏幕阅读做的西文衬线：x 高度大、
#      笔画结实、字宽均匀。正文对了，但标题也用它，版面平，没有杂志感。
#   ④ Playfair Display 标题 + Source Serif 4 正文 —— 现在这一套。
#
# 教训是 ①②③ 共同的：判断一个西文字体，得拿**一整段真实正文**在真实
# 字号下看，不能拿标题看 —— 标题上三套差别很小，正文上差别是决定性的。
#
# 备选（换的话只改下面两个常量，别的都不用动）：
#   Fraunces 标题 + Newsreader 正文 —— 性格更强，「旧字模」的不规则感
#   Newsreader 通篇 —— 本来就是为新闻杂志做的，一个家族最协调
#   Libre Bodoni 标题 + Lora 正文 —— 时装／文化杂志那一路
#
# 界面文字（导航、胶囊、按钮）留系统无衬线：12px 的衬线不够清晰。
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
EN_DISPLAY = '"Playfair Display",Georgia,"Times New Roman",serif' 
EN_READ = '"Source Serif 4",Charter,Georgia,"Times New Roman",serif'
# 界面无衬线：一个 CJK 字体名都不留 —— 它们的西文是配汉字设计的
EN_SANS = ('-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,'
           '"Helvetica Neue",Arial,sans-serif')

EN_FONT_URL = ("https://fonts.googleapis.com/css2?family=Playfair+Display:"
               "wght@600;700;800&family=Source+Serif+4:"
               "opsz,wght@8..60,400;8..60,600;8..60,700&display=swap")

FONT = [
    ("https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700;900"
     "&display=swap",
     ""),
    ("https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700"
     "&display=swap",
     ""),
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
# 用的就是原声站那一套（逐个字体名对齐，不是"差不多"）。为什么原声的
# 英文好看而主站的不好看，量出来只差一件事：
#
#   原声**不下载任何网络字体**，所以英文标题落到 Songti SC —— macOS 自带，
#   它的拉丁字形是 Times 一路的老式衬线，排英文本来就成立。
#   主站**下载** Noto Serif SC，于是英文标题落到它的拉丁字形 —— 思源宋体的
#   西文是为「和汉字并排」设计的：窄、低对比、重心跟着汉字身框走，
#   单独排一整页英文就是「完全不适合阅读」。
#
# 所以修法不是换一个更好的西文字体族，是**不要在英文页上下载那个 CJK
# 网络字体**，让它落到系统里那个拉丁字形本来就好的宋体上。Newsreader 那
# 一版是走岔了：它确实是个好西文字体，但和原声不是一个样子，而这两个站
# 得看起来是一家的。
#
# 非苹果平台上 Songti SC / PingFang SC 都不存在，落到 Georgia 和系统无衬线
# —— 这也是原声在那些平台上的样子。
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
/* 正文用衬线：这个站的英文页是拿来**读一整页**的，不是扫一眼。
   界面文字（导航、胶囊、按钮）留在 --sans 上。 */
html[lang="en"] article,
html[lang="en"] .dek,
html[lang="en"] .lede,
html[lang="en"] .idx,
html[lang="en"] .sec p,
html[lang="en"] blockquote{font-family:var(--read)}
/* 眉标是界面标签不是正文（「Mind and feeling」那一行），它在 article
   里面，会被上面那条扫到 —— 显式拨回无衬线。 */
html[lang="en"] .kicker,
html[lang="en"] .sec-k,
html[lang="en"] .chip,
html[lang="en"] .ph{font-family:var(--sans)}
html[lang="en"] h1,
html[lang="en"] h2,
html[lang="en"] .one,
html[lang="en"] .hd-title,
html[lang="en"] .point h2{font-family:var(--display)}
html[lang="en"] blockquote{font-family:var(--quote)}

/* ── Playfair 只做大标题 ─────────────────────────────────
   FONT 表是按**字体族**整批替换的，于是原来那个中文宋体用在哪里，
   Playfair 就跟到哪里 —— 11px 的分组标签、12px 的胶囊、16.5px 的卡片
   问句全变成了 Playfair。它是高对比的 Didone 展示体：字干粗细反差大、
   衬线细如发丝，20px 以上很有气势，12px 上就是一团做作的噪点。
   中文那边同一个位置是宋体，宋体在小字号上是**正文字体**，所以中文看着
   正常、英文看着别扭 —— 同一份排版，两种语言的字体分工本来就不一样。

   规矩：≥20px 的标题归 Playfair，正文归 Source Serif 4，界面归无衬线。 */
/* 选择器里必须带上 #hwx：页面自己的规则是 `#hwx .kc .t{…}`，带 id，
   权重 (1,2,0)；不带 id 的 `html[lang="en"] .kc .t` 是 (0,3,1)，
   id 那一位直接压死后面所有位，怎么写都赢不了。 */
html[lang="en"] #hwx .qc .v,
html[lang="en"] #hwx .kc .t,
html[lang="en"] #hwx .qzq,
html[lang="en"] #hwx .scline b{font-family:var(--read)}
/* ── 卡片上的「名字」统一用展示体，并且要大到看得出是它 ──────
   两件事一起修：
   一、人物卡的名字是 Playfair 19px、问题卡的名字是 Source Serif 4 13.5px
      —— 同样是「这张卡讲谁」，两种卡各说各的，扫读时没有节奏。
   二、19px 的 Playfair 认不出来。它是高对比的 Didone，靠字干粗细反差和
      发丝般的衬线立住，而这两样在 19px 上几乎看不见，读出来就是一个普通
      的粗衬线 —— 声明是对的、渲染也是对的（实测宽度和强制 Playfair 完全
      一致），只是尺寸没给到它能说话的地方。
   中文那边 19px 的宋体没有这个问题：宋体在小字号上本来就是正文字体。
   又是同一个形状 —— 尺寸参数是照汉字定的。 */
html[lang="en"] #hwx .pc b{font-family:var(--display);font-size:21px;
  letter-spacing:-.012em;line-height:1.25}
html[lang="en"] #hwx .kc b{font-family:var(--display);font-size:15px;
  letter-spacing:-.008em}

html[lang="en"] #hwx .said,
html[lang="en"] #hwx .scg,
html[lang="en"] #hwx .tabs2 button,
html[lang="en"] #hwx .chip,
html[lang="en"] #hwx .pill,
html[lang="en"] .chip{font-family:var(--sans)}

/* ── 引号用英文的那一对 ─────────────────────────────────
   卡片上的引文是用 ::before/::after 加「」包起来的。中文页对，英文页
   就成了「The winner had already won when the fighting started」——
   一句英文外面套一对中文书名号。这不是细节洁癖：读者一眼看出这一页
   是从别的语言搬过来的，而整站在做的事正是让它读起来像本来就是英文。
   直接写引号字符，不写 \\201C —— EN_CSS 是普通三引号串，
   \\201 会被 Python 当成八进制转义吃掉，生成出来是 content:"C"。 */
html[lang="en"] #hwx .qc .v::before,
html[lang="en"] #hwx .pc .hk::before,
html[lang="en"] #hwx .nc .q::before{content:"“"}
html[lang="en"] #hwx .qc .v::after,
html[lang="en"] #hwx .pc .hk::after,
html[lang="en"] #hwx .nc .q::after{content:"”"}

/* ── 卡片分栏要按英文的字宽来 ───────────────────────────
   栏宽写死 150px 是照汉字算的：131px 的正文宽度放得下 8 个汉字，一句
   12 字的问句两行就完了。同样 131px 放得下三个英文单词 —— 「It hit me
   and I can't cool down.」要断成三行，每行三个词，读起来是碎的。
   英文把栏宽放到 260px：390px 的屏上就是一栏，宽屏上仍然是两栏。 */
/* 用 columns 简写，不用 column-width：页面写的是 `columns:150px`，
   简写会把 column-count 一并设回 auto，只覆盖 column-width 的话
   两条各写各的，最后仍然是它说了算。 */
html[lang="en"] #hwx .feed,
html[lang="en"] #hwx .nc-feed{columns:260px}
/* 字距是给汉字调的：汉字是方块，拉开一点更透气；拉丁字母的字距字体里
   已经调好了，再加 .04em 就散。标题类归零偏紧一点，小标签留一点点。 */
html[lang="en"] h1,
html[lang="en"] .one,
html[lang="en"] .hd-title,
html[lang="en"] .point h2{letter-spacing:-.02em}
html[lang="en"] .kicker,
html[lang="en"] .sec-k{letter-spacing:.008em}
""" % {"disp": EN_DISPLAY, "read": EN_READ, "sans": EN_SANS}
# 版本号跟内容走，不写死。写死的话改了 CSS 而 URL 不变，浏览器照旧用
# 缓存里的旧文件 —— 我自己就被它骗了一轮：改完样式反复重建，页面纹丝不动，
# 以为是选择器权重不够，其实根本没加载新文件。读者那边同样会中招。
EN_CSS_HREF = "/assets/hw-en.css?v=" + __import__("hashlib").md5(
    EN_CSS.encode("utf-8")).hexdigest()[:8]


def write_en_css():
    """写出英文样式表。放在 /assets/ 下和其他样式表同级。"""
    p = os.path.join(ROOT, "assets", "hw-en.css")
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    if old != EN_CSS:
        open(p, "w", encoding="utf-8").write(EN_CSS)
    return len(EN_CSS)


def drop_wechat(s):
    """英文页去掉公众号引导块。

    那一块是「没找到想看的？在公众号里告诉我」+ 一张二维码 + 一句「用微信
    扫码关注」。英文读者用不了微信公众号 —— 给他们一个扫不了的码，等于在
    页脚放一块自己不能用的东西；二维码正中间还嵌着「人」字印，那是英文页脚
    上唯一剩下的中文。

    只在英文页去掉，中文和繁体照旧。
    """
    a = s.find('<div class="wx">')
    if a < 0:
        return s
    b = s.find("</div>", s.find('class="wx-hint"', a))
    if b < 0:
        return s
    return s[:a] + s[b + len("</div>"):]


def link_en_assets(s):
    """给每个英文页挂上西文字体和英文样式表。

    字体链接必须**主动挂上**，不能靠 FONT 表替换。踩过：表里写的是
    「把中文字体的 Google Fonts 地址换成英文的」，可条目页和章节页本来
    就没有那条地址（中文站那两类页用的是系统宋体）—— 换无可换，于是
    **一个英文页都没有加载 webfont**，Playfair 和 Source Serif 4 全部落到
    Georgia 兜底。首页因为原来有那条地址，看着是对的，内页不对。
    这也是为什么同样声明了 Playfair，主站看起来和原声不一样。

    英文样式表排在所有其他样式表后面 —— 同等权重的规则要靠源码顺序赢。
    """
    if "</head>" not in s:
        return s
    add = ""
    # 判据要看**这条字体样式表在不在**，不能看 preconnect 在不在：
    # 条目页和章节页本来就带着 fonts.gstatic.com 的 preconnect（给中文站
    # 用的），拿它当判据的话这些页全被跳过 —— 只有首页挂上了。
    if "Playfair+Display" not in s:
        add += ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                '<link rel="stylesheet" href="%s">' % EN_FONT_URL)
    if EN_CSS_HREF not in s:
        add += '<link rel="stylesheet" href="%s">' % EN_CSS_HREF
    if not add:
        return s
    i = s.rindex("</head>")
    return s[:i] + add + s[i:]


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
    return link_en_assets(drop_wechat(s))



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


def _first_sentences(d, lo=90, hi=170):
    """取 d 开头的**若干个完整句子**，不硬切。

    原来是 G.plain(d, 140) —— 按字数硬切，切在哪个字母上纯看运气。这个
    summary 有三个出口，三个都露过切口：条目页导语、分享文案、还有给爬虫
    和无脚本读者看的条目索引（「He married at fifty-eight; hi」，切在词
    中间）。它同时还是 meta description，也就是搜索结果里那一段。

    中文那边同样是硬切，但汉字没有词界，切在哪儿都还算「一句没说完」；
    英文切在词中间就是明显的坏。

    lo/hi 是「至少这么长、最多到这里」：先凑够 lo，再在 hi 之前的最后一个
    句号处收。一句都凑不满就整句给出去，不留半截词。
    """
    import geo_kit as G          # G 是在 en_items() 里才 import 的
    t = G.plain(d)
    if len(t) <= hi:
        return t
    cut = t[:hi]
    ends = [m.end() for m in re.finditer(r"[.!?](?=\s|$)", cut) if m.end() >= lo]
    if ends:
        return cut[:ends[-1]].strip()
    # hi 之前没有句号：退到词界，并且明确打省略号
    sp = cut.rfind(" ")
    return (cut[:sp] if sp > lo else cut).rstrip(" ,;:—-") + "\u2026"


def _dedupe_paragraphs(path):
    """合掉紧挨着的重复段落。

    llms.txt 的开头是「英文自述 + 中文自述」两段。中文那段翻成英文之后，
    和上一段**一字不差** —— 英文站的 llms.txt 开头把同一段话说了两遍，
    而这正是喂给模型的第一屏。中文站不会有这个问题（两段本来就不同语言），
    所以这是「翻译之后才出现」的重复，翻译规则那一层看不见。

    只合**相邻**的：隔开的重复段落可能是有意的（比如引用），不该动。
    """
    if not os.path.exists(path):
        return 0
    parts = open(path, encoding="utf-8").read().split("\n\n")
    out, n = [], 0
    for x in parts:
        if out and x.strip() and x.strip() == out[-1].strip():
            n += 1
            continue
        out.append(x)
    if n:
        open(path, "w", encoding="utf-8").write("\n\n".join(out))
    return n


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
            e["n"], (" (%s)" % era if era else ""), one, _first_sentences(e.get("d")))
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
                  "const DQ_FONT='\"Playfair Display\",Georgia,serif';", "DQ_FONT")

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
        # 把章节折进 llms.txt / llms-full.txt / feed.xml。
        # 漏掉这一句的代价：英文的 GEO 层只有 30 个条目，**80 个章节一个
        # 都没有** —— 而章节才是真正讲道理的那一层。对一个读 llms-full.txt
        # 的模型来说，英文站看起来只有 30 页内容（中文站 377 章全在里面）。
        # 页面建出来了、sitemap 也有，所以任何「页面在不在」的检查都发现
        # 不了；只有去数 llms-full 里的章节地址才看得见。
        hw_chapters.write_indexes(root=OUT)
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
            # 已经有日夜按钮的页面不要再贴一个。英文首页自己的 #hwx 块里
            # 就带着一个（简体首页在 force_chapter_ui 里是按路径特判跳过
            # 的），再贴一份的结果是**两个 id="hwx-theme"**：
            # getElementById 只认第一个，第二个既没人给它换图标、也没人
            # 给它去框，于是页头右上角挂着一个什么都没有的浅色圆圈 ——
            # 用户看到的就是它。按「页面上有没有」判，不按路径判。
            add = "".join(blk for mark, blk in blocks
                          if mark not in x
                          and not (mark == "<!--HWX:THEME-->"
                                   and 'id="hwx-theme"' in x))
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

    # 去重必须在**本地化之后**：llms.txt 开头是「英文自述 + 中文自述」两段，
    # 翻译之前它们一中一英、不重复；翻完才变成一字不差的两段。放在翻译前跑
    # 等于什么都没做 —— 我第一版就放错了位置，跑完还是两段。
    _dedupe_paragraphs(os.path.join(OUT, "llms.txt"))

    print("English site: %d chapter pages rendered, %d files localised" % (n_ch, n_fix))
    return 0


if __name__ == "__main__":
    sys.exit(main())
