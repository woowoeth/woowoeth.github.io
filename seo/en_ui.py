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
