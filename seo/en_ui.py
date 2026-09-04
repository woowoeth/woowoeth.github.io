# -*- coding: utf-8 -*-
"""Interface strings for the English site.

How this list was built: render the English chapter data through the ordinary
templates, then look at what is still Chinese on the page. Whatever survives is
by definition interface, because the content is already English. That beats
reading the generators and guessing — scripts/check_en.py fails the build on any
CJK left in /en/, so the list cannot silently fall behind.

**Order matters: longest first.** Replacing a short string before the longer one
that contains it leaves a half-converted phrase behind. The Traditional build
shipped exactly that bug once — 支付寶 was replaced before 支付寶收款鏈接, and
readers got "AlipayHK收款鏈接" with the space eaten.

Fixed terms, used everywhere and not to be varied for flavour:
    处境 Situations · 深度阅读 Deep read · 金句 Lines to keep · 分则 The parts
    局面/先问/用反了 → Where you are / Ask first / Where it goes wrong
    本篇结构 In this piece · 对照着读 Read alongside · 延伸 Further
"""
import re

# (中文, English) —— 按长度降序应用，见上面为什么
UI = [
    # 站名与标语
    ("遇到事了，看看以前的人怎么处理", "See how people before you handled it."),
    ("人类世界生存法则", "Human World Rules"),
    ("人类生存法则", "Human World Rules"),
    (">人类世界<span class=", ">Human World <span class="),
    (">生存法则</span></span>", ">Rules</span></span>"),

    # 章节页的两问
    ("### Q：背后是什么故事？", "### Q: What actually happened?"),
    ("### Q：今天怎么用？", "### Q: How do I use it today?"),
    ("背后是什么故事？", "What actually happened?"),
    ("今天怎么用？", "How do I use it today?"),
    ("背后是什么故事", "What actually happened"),
    ("今天怎么用", "How do I use it today"),

    # 小标题
    (">和谁对照着读</h2><div class=", ">Read alongside</h2><div class="),
    (">本篇结构</p><nav class=", ">In this piece</p><nav class="),
    (">延伸</h2><div class=", ">Further</h2><div class="),
    (">金句</h2>", ">Lines to keep</h2>"),
    ("### 分则 · ", "### The parts · "),
    ("### 金句", "### Lines to keep"),
    ("对照着读", "Read alongside"),
    ("本篇结构", "In this piece"),
    ("金句", "Lines to keep"),
    ("分则", "The parts"),
    ("对照", "Compare"),
    ("原话", "In their words"),
    ("后来", "What came after"),
    ("留下", "What stayed"),
    ("延伸", "Further"),
    ("今天", "Today"),

    # 正文里的固定引导词
    ("局面：", "Where you are: "),
    ("先问：", "Ask first: "),
    ("用反了：", "Where it goes wrong: "),
    ("\n例：", "\ne.g. "),
    ("例：", "e.g. "),
    ("例:", "e.g. "),

    # 导航
    (">上一篇</span>", ">Previous</span>"),
    (">下一篇</span>", ">Next</span>"),
    (">回</span>", ">Back to </span>"),
    ("上一篇", "Previous"),
    ("下一篇", "Next"),
    ("本页可直接引用", "Cite this page"),
    ("分享本页", "Share this page"),
    ("首页", "Home"),
    ("分享", "Share"),

    # 页脚与姊妹站
    ("原声播客", "Podcast"),
    # 品味站自己的英文名就是 Taste（?lang=en 下的 <title> 是
    # 「Taste — curated agent skills」），不是把「Skill」照抄过来。
    ("品位 Skill", "Taste"),
    ("全部条目", "Everyone"),
    ("深度阅读", "Deep read"),

    # 时代分期（条目页的年代标签）
    ("先秦与古典时代", "Pre-Qin and classical"),
    ("秦汉至魏晋", "Qin, Han and the Six Dynasties"),
    ("工业时代", "The industrial age"),
    ("中古", "Medieval"),
    ("近世", "Early modern"),
    ("现代", "Modern"),
]

# 长的先换。写在这里而不是靠上面的手工排序，是因为手工排序改两次就会错。
UI = sorted(UI, key=lambda p: -len(p[0]))

# 少数几处靠上下文才认得出来，字面量表配不了。
# 「回」在返回链接里有两种写法：<span class="dir">回</span>名字 已经被上面的
# '>回</span>' 配掉了；另一种是 <a class="pill" href="…">回名字</a>，回和名字
# 之间没有标签。按属性顺序去写死那一串太脆，用正则认「>回 后面紧跟拉丁字母」。
REGEX = [
    (re.compile(r">\u56de(?=[A-Za-z])"), ">Back to "),
]


def apply(s):
    for a, b in UI:
        s = s.replace(a, b)
    for r, b in REGEX:
        s = r.sub(b, s)
    return s


# 夜间模式挂件的几处标签（挂件整块是从简体产物里原样搬过来的）
UI += [
    ("切换日夜模式", "Toggle dark mode"),
    ("切换到日间", "Switch to light"),
    ("切换到夜间", "Switch to dark"),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 条目页和 all 页上线之后又数出来的一批。做法同上：渲染 → 看还剩什么中文。
UI += [
    # keywords 整串换掉，不逐词换 —— 中英混排的关键词对英文读者没有意义
    ("生存智慧, 战略思维, 孙子兵法, 人性, 财富 投资 原则, 权力 治理, 创业 方法论, 经典 解读, "
     "life principles, strategy, human nature, classic texts",
     "life principles, strategy, power, human nature, money and risk, "
     "classic texts, how the world works"),
    ("Human World Rules 的全部 30 个条目，一页列完。",
     "All 30 entries on Human World Rules, on a single page."),
    ("这个地址不存在。下面是可以去的地方。",
     "This page doesn't exist. Here's where you can go."),
    (">目录<", ">Contents<"),
    (">全部<", ">All<"),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 站点自述整段替换：**不能靠逐词替换拼出来**。
# 第一版没有这条，于是词级规则（留下 / 分则 / 今天怎么用）在中文句子内部乱开枪，
# llms.txt 里出现了「真正What stayed的那一个想法、拆开的The parts」这种半截洋泾浜。
# 页面渲染正常、构建通过 —— 靠「/en/ 里不许剩中日韩字符」那道闸才发现。
def _site_pairs():
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from build_seo import SITE
    out = []
    for zh, en in ((SITE.description_zh, SITE.description),
                   (SITE.tagline_zh, SITE.tagline),
                   (SITE.name_zh, SITE.name)):
        if zh and en:
            out.append((zh, en))
            # %(n)d 已被填成具体数字的版本也要认
            for n in (30, 159):
                out.append((zh % {"n": n} if "%(n)d" in zh else zh,
                            en % {"n": n} if "%(n)d" in en else en))
    return out


UI += _site_pairs()
UI = sorted(UI, key=lambda p: -len(p[0]))

# 少数带变量的句式只能用正则。「N 个条目」里的 N 是构建时算出来的。
REGEX += [
    (re.compile(r"([^\s\"<>]+(?: [^\s\"<>]+)*) 的全部 (\d+) 个条目，一页列完。"),
     r"All \2 entries on \1, on a single page."),
]


# llms.txt 里的兄弟站清单是双语标签 [English / 中文]，英文站只留英文那半。
# 「Skill Store」换成 Taste：那是品味站在 ?lang=en 下的自称。
UI += [("Skill Store / Skill 商店", "Taste")]
UI = sorted(UI, key=lambda p: -len(p[0]))
REGEX += [
    (re.compile(r"\[([^\]]*?) / [^\]]*[一-鿿][^\]]*\]"), r"[\1]"),
]


# 首页那一层。同样是渲染出来数的：把中文首页克隆过来换掉数据之后，
# 页面上还剩 36 个中文串，全在这里。
#
# 三个 data-t 的值（"新" "全" "境"）**不在这张表里，也不能加进来**：
# 它们是 JS 拿来比对的数据（if(t==='新')），不是显示文字。翻了标签页就废了。
# 所以下面配的是 >最新</button> 这种带标记的形状，不是裸的词。
UI += [
    ("微信扫一扫关注；手机上长按图片 → 存储图像，再用「扫一扫」从相册识别",
     "Scan with WeChat to follow. On a phone, press and hold the image to save "
     "it, then scan it from your album."),
    ("没找到想看的？在公众号里告诉我", "Can't find what you're after? Tell me on WeChat"),
    ("搜你遇到的事：被裁了、睡不着、孩子不听…",
     "Search what you're in: laid off, can't sleep, kid won't listen…"),
    ("OurWord AI 微信公众号二维码", "OurWord AI on WeChat, QR code"),
    ('content="生存法则"', 'content="Human World Rules"'),
    ("你遇到的是别的事？", "Something else on your mind?"),
    ("挑你自己那一件", "Find yours"),
    ("每日金句", "Line of the day"),
    ("今日一问", "Today's question"),
    ("今日一篇", "Today's read"),
    ("跳至主内容", "Skip to content"),
    ("最近看过", "Recently viewed"),
    ("位人物与典籍", " people and books"),
    ("按处境筛选", "Filter by situation"),
    (">最新</button>", ">Latest</button>"),
    (">全部</button>", ">All</button>"),
    (">处境</button>", ">Situations</button>"),
    ('<div class="stat">跨越 ', '<div class="stat">across '),
    ("</b> 年</div>", "</b> years</div>"),
    ("</b> 大主题</div>", "</b> themes</div>"),
    ("保存卡片", "Save card"),
    ("保存图片", "Save image"),
    ("主题分类", "Themes"),
    ("人物详情", "Entry detail"),
    ("上一句", "Previous line"),
    ("下一句", "Next line"),
    ("换一换", "Show another"),
    ('aria-label="搜索"', 'aria-label="Search"'),
    ("出自 ", "from "),
    ("清空", "Clear"),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 又是词级规则在长词内部开枪：每日金句卡片 → 「Line of the day卡片」，
# 复制金句 → 「复制Lines to keep」。整词配整词，长的自然排在前面先跑。
UI += [
    ("每日金句卡片", "Line of the day card"),
    ("复制金句", "Copy the line"),
    ('<span class="dot">生存法则</span>', '<span class="dot">Rules</span>'),
    ('id="hwx-ago2">问</button>', 'id="hwx-ago2">Ask</button>'),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 首页 JS 在运行时拼出来的那一层。第一版闸门把 <script> 整块跳过，
# 于是这些全成了盲区 —— 静态 HTML 干净，页面上一眼还是中文。
# 现在闸门查字面量了，这些是它数出来的。
UI += [
    ("个问题。上面挑一个跟你有关的分组，或者直接搜。",
     " questions. Pick a group above that fits you, or just search."),
    ("换个说法试试——或者到下面的处境里Find yours。",
     "Try saying it another way — or find yours in the situations below."),
    ("长按图片 → 存储图像（保存到相册）",
     "Press and hold the image → Save image"),
    ("复制失败，请长按选择文字", "Copy failed. Press and hold to select the text."),
    ("看他怎么处理最难的那件事 →", "See how he handled the hardest one →"),
    ("从最狠的一篇读起 →", "Start with the sharpest one →"),
    ("他的方法都在里面 →", "His whole method is in there →"),
    ("篇，句句能落地 →", " pieces, every one usable →"),
    ("篇，够用很久 →", " pieces, enough for a long time →"),
    ("条硬原则 →", " hard rules →"),
    ("值得先看 →", " is the one to read first →"),
    ("什么时候翻开它：", "When to open it: "),
    ("已Copy the line到剪贴板", "Copied to the clipboard"),
    ("缺解析的Lines to keep：", "lines with no note: "),
    ("核心Lines to keep", "Lines to keep"),
    ("用 AI 触摸这个世界", "Reaching the world through AI"),
    ("这一问来自「", "This one comes from “"),
    ("那儿还有 ", "; there are "),
    ("按收录顺序 · 最新在前", "In order added, newest first"),
    ("关联知识库", "Related entries"),
    ("失败教训", "What it cost"),
    ("败局时刻", "Where it broke"),
    ("经典一幕", "The scene"),
    ("核心框架", "The framework"),
    ("展开全部", "Show all"),
    ("图片已保存", "Image saved"),
    ("去挑处境 →", "Pick a situation →"),
    ("进去偷师 →", "Go and learn from it →"),
    # 撇号不能进这一条：它落在一个**单引号 JS 字符串**里，一个 ' 就把字符串截断，
    # 整个 script 块语法错误，首页直接空白。scripts/check_en_js.py 守这一类。
    ("看完你会换个打法 →", "It will change how you play it →"),
    ("篇深读备好了 →", " deep reads ready →"),
    ("拆开看他的", "Take apart his "),
    ("套打法 →", " approaches →"),
    ("篇拆完 →", " taken apart →"),
    ("篇讲透 →", " explained in full →"),
    ("篇再走 →", " more before you go →"),
    ("读透这 ", "Read all "),
    ("没找到「", "Nothing found for “"),
    ("关键词：", "Keyword: "),
    ("今日一句", "Line of the day"),
    ("日一二三四五六", "SMTWTFS"),
    ("月 · 星期", " · "),
    ("条知识", " entries"),
    ("种处境 · ", " situations · "),
    ("先读「", "Start with “"),
    ("他的答案分", "His answer comes in "),
    ("他的路数，", "His way of doing it, "),
    ("从「", "From “"),
    ("共 ${list.length} 位", "${list.length} in all"),
    ("阅读", "Read"),
    ("深读", "Deep read"),
    ("带走", "Take away"),
    ("应用", "Apply"),
    ("收起", "Collapse"),
    ("关闭", "Close"),
    ("还有", "and "),
    ("问过", "asked"),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 收尾的几条。两处是我自己犯的老毛病：拿**替换之后**的形态做键
# （「已Copy the line到剪贴板」），而原文是「已复制金句到剪贴板」，永远配不上。
UI += [
    ("换个说法试试——或者到下面的处境里挑你自己那一件。",
     "Try saying it another way — or pick your own from the situations below."),
    ("已复制金句到剪贴板", "Copied to the clipboard"),
    ("缺解析的金句：", "lines with no note: "),
    ("，那儿还有 ", ", and "),
    ("核心金句", "Lines to keep"),
    ("个问题", " questions"),
    ("篇最新", " newest"),
    ("」进 →", "” →"),
    ("个'):''", " more'):''"),
    ("}位</span>", "} in all</span>"),
    (">全部</span>", ">All</span>"),
    ("'全部'", "'All'"),
    ("'最新'", "'Latest'"),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 最后几处。三点要注意：
#
# ① CATS 里的 "最新"/"全部" 既是显示文字**又是比较键**（TAB==="全部"）。
#    两处必须一起换，只换一处标签页就废了。所以这里配的是带引号的形态，
#    双引号单引号都要。
# ② data-t 的 '新'/'全'/'境' 是纯内部键，从不显示 —— 一个字都不能动。
# ③ 汇文明朝体的字体预载探针写死了一个汉字（'删'）。英文页的引文字体是
#    Newsreader，这个探针不但没用，还会白拉一个 670KB 的中文字体。
UI += [
    ('document.fonts.load(\'140px "Huiwen-mincho"\',\'删\')',
     'document.fonts.load(\'140px "Newsreader"\',\'A\')'),
    ('document.fonts.load(\'65px "Huiwen-mincho"\',\'删\')',
     'document.fonts.load(\'65px "Newsreader"\',\'A\')'),
    # 逐个点名比较点太脆 —— 漏一处标签页就废了。到这一步页面上剩下的
    # "最新"/"全部" 只可能是标签页键，对带引号的整体下一条规则更稳。
    ('"最新"', '"Latest"'),
    ('"全部"', '"All"'),
    ('<span class="nb">新</span>', '<span class="nb">New</span>'),
    ("+' 个';", "+'';"),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 中文标点。闸门原来只查汉字（U+4E00 起），碰不到这几个 —— 于是页面上
# 出现了「“I have no one to call」」这种半中半英的引号，闸门全绿。
# 这几个符号在英文页没有任何正当用途，整篇换掉。
# **不能做通配替换。** 第一版直接把 「」、《》、、 全站换掉，结果替换跑进了
# JS 正则的字符类 —— /[。，、；：？！…\.]+$/ 被改成 /[。，, ；：？！…\.]+$/，
# 一个用来剥句尾标点的正则就此失效。en_ui 是盲替换，它不知道自己落在
# 文本里还是代码里；标点这种到处都是的字符，只能逐个显示位置去打。
UI += [
    # 相对路径在 /en/ 下会解析成 /en/wechat-qr.png —— 那个文件在站根，
    # 于是 404。资源不跟着语言走（见 build_en 的 ASSETS=False），
    # 但前提是路径得是绝对的。retarget 只处理以 / 开头的地址，碰不到相对路径。
    ('src="wechat-qr.png', 'src="/wechat-qr.png'),
    ("'「'+q1.q+'」'", "'“'+q1.q+'”'"),          # 今日一句外面的引号
    ("」'\n      +(_more", "”'\n      +(_more"),   # 「这一问来自「X」」的收尾
    ("」值得先看", "” is the one to read first"),
]
UI = sorted(UI, key=lambda p: -len(p[0]))


# 中文破折号只在三处**显示**（今日一句的署名、分享卡的署名、朗读文本），
# 其余是 split("——") 这种逻辑用法，动了会出错。所以逐处配，不整篇换 ——
# 上一版整篇换的时候，它跑进了 JS 正则的字符类里。
UI += [
    ("'—— '+q1.who", "'— '+q1.who"),
    ("fillText('—— '+q1.who", "fillText('— '+q1.who"),
    ('+s.d.t+"——"+s.src', '+s.d.t+" — "+s.src'),
]
UI = sorted(UI, key=lambda p: -len(p[0]))
