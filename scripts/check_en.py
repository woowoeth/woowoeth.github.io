#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""English site gate.

    python3 scripts/check_en.py

The English site is not a conversion of the Chinese one — every string is
written by hand — so none of the繁体 machinery applies. What can go wrong here
is different, and each rule below covers one way it actually goes wrong:

① Every (slug, k) resolves to a real chapter. A typo here renders a dead link
   that looks completely normal on the page — this is the single most likely
   defect, because the refs are copied by hand from the Chinese layer.
② Every referenced entry is inside the pilot set. A ref to an untranslated
   entry sends an English reader to a Chinese page. Rule ① would pass it.
③ No CJK anywhere in the English strings. A line left untranslated is invisible
   in review — you read past it — but it is glaring to a reader.
④ No duplicate questions, and no duplicate (group, situation). The Chinese
   layer has near-identical phrasings on purpose; if two came across as the
   same English sentence, one of them is dead weight in the list.
⑤ Group and situation names carry no trailing punctuation and stay short
   enough for the chip strip — long ones wrap and break the row.
⑥ Coverage back-check: every pilot entry is reachable from at least one
   question, and every chapter of every pilot entry too. An entry nothing
   points at is a page no reader can find from the front door.
⑦ 「今日一句」的每条映射：值必须是处境层里的**原句**，而且那一句必须真的
   引用了这一章。差一个字就是配错，而配错的第一人称句是假共情 —— 中文那边
   的教训写在 quote_asks.py 开头。每章必须且只能有一条。
⑧ 英文章节的长度闸。中文一个字顶英文一个词还多，照着中文的篇幅写英文，
   dek 会长到吃掉两行、金句会长到没法当金句用。这几个数是排版定的，不是
   风格偏好：dek 12-30 词、story 50-110 词、分则 20-55 词、例 8-40 词、
   金句 ≤14 词。
   靠眼睛盯 79 章必漏，所以让机器数。
⑪ 构建出来的 /en/ 里一个中日韩字符都不许剩。这是整套英文站赖以成立的判据：
   内容已经是英文，剩下的中文按定义就是没翻的界面串 —— 界面层那 90 多条
   就是这么一条条数出来的，不是读生成器猜的。
   两处豁免，都写在下面的 EXEMPT 里，各有理由。
⑩ 条目记录不带 == 强调（条目页不渲染它，会显示成两个字面的等号）。
⑨ 章节数据自身完整：每章七个字段都在，f 至少两条，q 至少两条，
   story 里恰好一处 ==…== 强调（模板拿它做引文块，没有就是一段白文，
   两处则第二处不会被渲染）。
"""
import collections
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

import hw_chapters as H          # _load() runs at import — do not call it again
from hwx_scenes_en import SCENES
from quote_asks_en import QUOTE_ASKS_EN

PILOT = """su-shi wang-yangming zhuangzi pu-songling huineng fan-li li-ka-shing han-feizi
kasparov wiener excellent-sheep maslach cacioppo harvard-study granovetter curie
hochschild rat-park vygotsky thomas-gordon cs-lewis churchill perel jung sapolsky
dweck john-ratey gottman montessori boyd""".split()

def load_en():
    """已经写好的英文章节。

    单独加载而不是靠 HW_CHAPTERS 环境变量切换，是因为这道闸要同时用到两份：
    引用是否成立要拿**中文章节**当全集校验（那是这一版计划里存在的 79 章），
    长度和完整性只能校验**已经写出来的**那些。混用一份的话，写到一半时闸门
    会把还没写的章全报成「引用指向不存在的页」，把真正的错埋掉。
    """
    import importlib
    import pkgutil
    here = os.path.join(ROOT, "seo", "chapters_en")
    if not os.path.isdir(here):
        return []
    sys.path.insert(0, os.path.join(ROOT, "seo"))
    out = []
    for mod in sorted(m.name for m in pkgutil.iter_modules([here])):
        m = importlib.import_module("chapters_en." + mod)
        spec = getattr(m, "PARENT", {}) or {}
        for ch in getattr(m, "CHAPTERS", []) or []:
            ch = dict(ch)
            ch["parent_slug"] = spec.get("slug", "")
            ch["parent"] = spec.get("name", "")
            out.append(ch)
    return out


# /en/ 里允许留中文的地方：
#
# ① data-t="新" / "全" / "境" —— 首页标签页的**数据值**，JS 拿它比对
#    （if(t==='新')）。翻了标签页就废了。
# ② 语言切换里的 简体 / 繁體 —— 语言的名字用它自己的文字写，是有意的。
# ③ 红印上的那个字 —— 卡片的印章、分享图上的「人」。那是这个站的标识
#    （logo 本身就是一枚红「人」印），是图形不是文字。
#
# 扫描口径是「**读者看得见的东西**」，不是「整个文件减去注释」。
# 后者试过，不好使：注释配对会被某个字符串里的 */ 带偏，于是一段注释漏出来；
# 而 JS 正则字面量里的禁则字符表（/[。，、；：？！…]+$/）也会被当成漏译。
# 两样都不是给人看的。所以直接只看三处：
#   · HTML 文本节点（> 和 < 之间）
#   · 会显示出来的属性（title / alt / placeholder / aria-label / content）
#   · JS 里的**带引号字符串** —— 页面上大半的字是 JS 拼出来的，必须查。
#     正则字面量不带引号，注释也不带，天然排除。
EXEMPT = re.compile(r'data-t="[^"]*"|class="seal">[^<]*<|fillText\(\'[一-鿿]\'')
# 语言选择器里那几项：每一项用它自己的语言写，是有意留的中文。
# 标签后来从「简体／繁體」缩成「简／繁」（窄屏页头放不下整个词），
# 短的那两个也得在这张表里，否则 ⑪⑫ 会把它们当漏译报出来。
LANG_NAMES = ("简体", "繁體", "繁体", "简", "繁")
# 首页三个标签页的**内部键**：新 / 全 / 境。只出现在 data-t 和 JS 比较里，
# 从不显示给读者 —— 翻了标签页就废了。
TAB_KEYS = ("新", "全", "境")

# 名字不能叫 CJK —— 文件后面已经有一个 CJK = re.compile(…) 给判据 ③ 用，
# 同名会被后定义的那个覆盖掉。
CJK_CHARS = "一-鿿、。《》「」！，：；？"
TEXT_NODE = re.compile(r">([^<>]{0,300})<")
VISIBLE_ATTR = re.compile(
    r'\b(?:title|alt|placeholder|aria-label|content)="([^"]{0,300})"')
# JS 里的字符串**不用正则去找**。试过，不行：注释里的 don't 会和代码里的
# 引号配对，整段注释被当成字符串报出来，而真正漏译的反而淹掉。
# 靠正则切 JS 字符串需要一个真的分词器。
#
# 页面上大半的字确实是 JS 拼出来的，所以这一层改用**浏览器读渲染后的正文**
# —— 见下面的 rendered_cjk()。那才是读者真正看到的东西，也正是截图里
# 一眼看出「这一问来自「…」」还是中文的那个层面。


def cjk_left(path):
    """静态 HTML 里**读者看得见**的中文片段（文本节点 + 可见属性）。

    JS 拼出来的那一层不在这里查，见 rendered_cjk()。
    """
    raw = open(path, encoding="utf-8", errors="ignore").read()
    # script / style 整块剥掉：它们里面的 > 和 < 会让文本节点的正则
    # 把 JS 代码当成正文报出来。那一层由 rendered_cjk() 用浏览器覆盖，
    # 这里只管静态 HTML。
    raw = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", "", raw, flags=re.S)
    raw = EXEMPT.sub("", raw)
    cand = set()
    for pat in (TEXT_NODE, VISIBLE_ATTR):
        for m in pat.findall(raw):
            cand.add(m)
    hit = re.compile("[" + CJK_CHARS + "]")
    out = set()
    for c in cand:
        c = c.strip()
        if c and hit.search(c) and c not in LANG_NAMES and c not in TAB_KEYS:
            out.add(c[:80])
    return sorted(out)

CJK = re.compile(r"[　-〿一-鿿＀-￯]")
# 例（eg）和分则（d）不是一回事，不能共用一个区间：d 是论证，要说完；
# eg 是一句具体的例子，短才好用。第一版把 20-55 同时套在两者上，
# 结果闸门把一批写得正好的例子判成太短 —— 照它去注水只会写坏。
LEN = {"dek": (12, 30), "story": (50, 110),
       "part": (20, 55), "eg": (8, 40), "quote": (1, 14)}
MAX_SCENE = 46          # 处境名进 chip 条，长了换行把整排挤散
MAX_GROUP = 30


def rendered_cjk(url="http://localhost:8931/en/"):
    """把英文首页真的渲染一遍，读 body 的可见文字里还有没有中文。

    这一层非有不可：首页大半的字是 JS 画的，静态 HTML 干净不等于页面干净。
    实测过一次 —— 静态扫描全绿，截图上「这一问来自「I have no one to call」」
    明晃晃是中文。

    没装 playwright 就跳过（返回 None），本地跑得动、CI 上一定跑。
    """
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        return None
    import subprocess
    import time
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8931"],
                           cwd=ROOT, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
    time.sleep(2.0)
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            pg = b.new_page(locale="en-US")
            pg.goto(url, timeout=30000)
            pg.wait_for_timeout(2500)
            txt = pg.evaluate("() => document.body.innerText")
            b.close()
    finally:
        srv.terminate()
    hit = re.compile("[" + CJK_CHARS + "]")
    # 语言名和红印是有意留的，见文件开头 EXEMPT 那几条的说明。
    keep = set(LANG_NAMES) | set(TAB_KEYS) | {"问", "句", "人"}
    return sorted({ln.strip()[:70] for ln in txt.split("\n")
                   if ln.strip() and hit.search(ln) and ln.strip() not in keep})


# 英文页的字体判据，两条，都落在**渲染之后**：
#
# ⓐ 不许下载 CJK 网络字体。这才是当初「英文页字体完全不适合阅读」的根因：
#    主站下载 Noto Serif SC，于是英文标题落到思源宋体的西文字形 —— 那套西文
#    是为「和汉字并排」设计的（窄、低对比、重心跟着汉字身框走），单独排一
#    整页英文就是「哪里不对但说不出」。原声站不下载任何网络字体，英文标题
#    落到系统自带的 Songti SC，它的拉丁字形是 Times 一路的老式衬线，排英文
#    本来就成立 —— 同一个位置，差别只在有没有下载那个 CJK 字体。
#    所以拦的是**下载**，不是「出现 CJK 字体名」。系统里的宋体和苹方是好
#    西文字体，而且后面跟着 Georgia / 系统无衬线兜底，在非苹果平台上也成立。
#
# ⓑ 解出来的字体栈必须**就是** build_en 打算给的那一套。这一条防的是覆盖
#    丢失：那段 html[lang="en"] 的变量覆盖丢过两次，字体照旧下载、页面照旧
#    拿别的字体排英文，而 ①-⑫ 全绿（它们只看有没有中文**字**，看不见用
#    什么**字体**）。判据对着 build_en 里的 EN_DISPLAY / EN_SANS 比，
#    单一来源 —— 有意改字体的人改那一处，闸门跟着走。

CJK_WEBFONTS = ("Noto+Serif+SC", "Noto+Sans+SC", "Noto+Serif+TC",
                "Noto+Sans+TC", "Source+Han", "Noto+Serif+HK", "Noto+Sans+HK",
                "LXGW", "ZCOOL", "Ma+Shan", "Zhi+Mang", "Liu+Jian")

# 三类版式各抽一页，每页量标题和正文两个层面。抽样表里少一类版式，那一类
# 就没人看着 —— 首页的字体族是写死在内联 <style> 里的，条目页走
# /assets/hw-en.css，两条路完全不同。
# 抽样的选择器必须指到**那一类字体真正管的元素**。踩过：写 "article p"
# 抽正文，而 article 里第一个 p 是 p.kicker —— 界面标签，本来就该是无衬线。
# 闸门于是报「正文不是衬线」，而正文其实是对的：抽样抽偏了，不是产物坏了。
#
# 三类版式各抽一页，每处标明该用哪一类字体。角色必须写在表里，不能靠
# 「叫正文的就是无衬线」这种猜 —— 英文站是杂志排法：标题 display、
# 正文 read（衬线）、界面 sans，三类各有各的值，猜一定会猜错一类。
FONT_SAMPLE = [
    ("英文首页", "/en/", [("站名", ".hd-title", "display"),
                          ("界面", "body", "sans")]),
    ("英文条目", "/en/i/su-shi/",
     [("标题", "h1", "display"), ("正文", ".sec p", "read"),
      ("眉标", ".kicker", "sans")]),
    ("英文章节", "/en/i/su-shi/no-wind-no-rain/",
     [("标题", "h1", "display"), ("正文", ".sec p", "read")]),
    ("英文分类", "/en/t/mind-and-feeling/", [("标题", "h1", "display")]),
    ("英文全集", "/en/all/", [("标题", "h1", "display")]),
]


def _norm(fam):
    """把字体栈normalise成可比的形式：去引号、去空格、小写。

    浏览器会把 '"Songti SC",Georgia' 解析成 '"Songti SC", Georgia' —— 引号和
    空格都不稳定，逐字符比会假报。

    还有一个别名要抹平：Chrome 在 getComputedStyle 里把 BlinkMacSystemFont
    规范化成 "system-ui"。不抹的话这道闸会**一直报红而覆盖其实是好的** ——
    比对着声明去比，就得按浏览器的说法归一化。
    """
    t = fam.replace('"', "").replace("'", "").replace(" ", "").lower()
    return t.replace("blinkmacsystemfont", "system-ui")


def rendered_fonts(port=8932):
    """渲染英文页，量下载了什么字体、解出了什么字体栈。

    没装 playwright 就跳过（返回 None），本地跑得动、CI 上一定跑。
    """
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        return None
    import subprocess
    import time
    sys.path.insert(0, HERE)
    import build_en
    WANT = {"display": build_en.EN_DISPLAY,
            "read": build_en.EN_READ,
            "sans": build_en.EN_SANS}

    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port)],
                           cwd=ROOT, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
    time.sleep(2.0)
    out = []
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            pg = b.new_page(locale="en-US")
            for label, path, spots in FONT_SAMPLE:
                pg.goto("http://localhost:%d%s" % (port, path), timeout=30000)
                pg.wait_for_timeout(1200)
                # ⓐ 页面自己声明要下载哪些字体
                links = pg.evaluate(
                    "() => [...document.querySelectorAll('link[rel=stylesheet]')]"
                    ".map(l => l.href).join(' ')")
                for w in CJK_WEBFONTS:
                    if w in links:
                        out.append("%s 还在下载 CJK 网络字体 %s —— 英文页不该下载它"
                                   % (label, w.replace("+", " ")))
                        break
                # ⓑ 解出来的字体栈
                for what, sel, role in spots:
                    fam = pg.evaluate(
                        "s => { const e = document.querySelector(s);"
                        " return e ? getComputedStyle(e).fontFamily : null }", sel)
                    if fam is None:
                        out.append("%s 的%s（%s）在页面上找不到 —— 抽样表要跟着改"
                                   % (label, what, sel))
                        continue
                    if _norm(fam) != _norm(WANT[role]):
                        out.append("%s 的%s 解出的不是英文站的「%s」那一套：\n"
                                   "      得到 %s\n      应为 %s"
                                   % (label, what, role, fam[:110],
                                      WANT[role][:110]))
            b.close()
    finally:
        srv.terminate()
    return out


# 渲染之后的英文页上，这些是「读者一眼看得出别扭」的东西。
# 必须在浏览器里量：首页那一层是 JS 运行时拼出来的，静态 HTML 里一个
# 都看不到 —— 「253  questions」「and 3  more」就是这么漏了一整轮的。
FLAW_PAGES = ["/en/", "/en/i/su-shi/", "/en/all/"]


def rendered_flaws(port=8933):
    """渲染英文页，读 innerText，找排版上的硬伤。

    ① 连续两个空格 —— 中文里数字和量词之间本来有一个空格（'26'+' 个问题'），
       而界面串规则的替换串自己又带一个前导空格，拼出来就是两个。
       中文页上看不出来，英文页上很显眼。
    ② 标点前有空格 —— 同一类拼接留下的。
    ③ 中文标点混在英文里。
    """
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        return None
    import subprocess
    import time
    srv = subprocess.Popen([sys.executable, "-m", "http.server", str(port)],
                           cwd=ROOT, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
    time.sleep(2.0)
    out = []
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            pg = b.new_page(locale="en-US")
            for path in FLAW_PAGES:
                pg.goto("http://localhost:%d%s" % (port, path), timeout=30000)
                pg.wait_for_timeout(2000)
                txt = pg.evaluate("() => document.body.innerText")
                for line in txt.split("\n"):
                    t = line.strip()
                    if not t:
                        continue
                    for pat, why in ((r"\S  +\S", "连续两个空格"),
                                     (r"\s[,.;:!?]", "标点前有空格"),
                                     (r"[，。、；：？！]", "中文标点")):
                        m = re.search(pat, t)
                        if m:
                            out.append("%s  %s：…%s…"
                                       % (path, why,
                                          t[max(0, m.start() - 35):m.end() + 25]))
                            break
                    if len(out) >= 12:
                        break
            b.close()
    finally:
        srv.terminate()
    return out


def main():
    real = {(c["parent_slug"], c["k"]) for c in H.CHAPTERS}
    bad, seen_q, seen_s = [], {}, {}
    hit_entry, hit_ch = set(), set()

    for scene, group, qs in SCENES:
        # ③ 英文层里不该有中日韩字符
        for label, s in (("group", group), ("situation", scene)):
            if CJK.search(s):
                bad.append("%s still Chinese: %r" % (label, s))
        # ⑤ 名字的形状
        if len(scene) > MAX_SCENE:
            bad.append("situation too long (%d > %d): %r" % (len(scene), MAX_SCENE, scene))
        if len(group) > MAX_GROUP:
            bad.append("group too long (%d > %d): %r" % (len(group), MAX_GROUP, group))
        if scene.rstrip() != scene or scene.endswith((".", "?", "!", ":")):
            bad.append("situation should not end in punctuation: %r" % scene)
        # ④ (分组, 处境) 不能重
        if (group, scene) in seen_s:
            bad.append("duplicate situation: %r in %r" % (scene, group))
        seen_s[(group, scene)] = 1

        for q, refs in qs:
            if CJK.search(q):
                bad.append("question still Chinese: %r" % q)
            if q in seen_q:
                bad.append("duplicate question: %r (%r and %r)" % (q, seen_q[q], scene))
            seen_q[q] = scene
            if not refs:
                bad.append("question with no chapter: %r" % q)
            for slug, k in refs:
                # ② 必须在试水名单里
                if slug not in PILOT:
                    bad.append("%r points at %s, which is not in the pilot set" % (q, slug))
                # ① 必须真的存在
                elif (slug, k) not in real:
                    bad.append("%r points at %s/%s, which does not exist" % (q, slug, k))
                else:
                    hit_entry.add(slug)
                    hit_ch.add((slug, k))

    # ⑥ 反向：每个条目、每一章都得有人指得到
    for slug in PILOT:
        if slug not in hit_entry:
            bad.append("nothing points at entry %s" % slug)
    for slug, k in sorted(real):
        if slug in PILOT and (slug, k) not in hit_ch:
            bad.append("nothing points at chapter %s/%s" % (slug, k))

    # ⑦ 今日一句
    q_of = {}
    for scene, group, qs in SCENES:
        for q, refs in qs:
            for r in refs:
                q_of.setdefault("%s/%s" % r, set()).add(q)
    strip = lambda x: x.strip(" .?!\"'").lower()
    for key, q in sorted(QUOTE_ASKS_EN.items()):
        if key not in q_of:
            bad.append("today's line maps %s, which no question points at" % key)
        elif q not in q_of[key]:
            near = any(strip(x) == strip(q) for x in q_of[key])
            bad.append("today's line for %s is not a question that points at it: %r%s"
                       % (key, q, "  (punctuation differs?)" if near else ""))
    for key in sorted(q_of):
        if key not in QUOTE_ASKS_EN:
            bad.append("no today's line for chapter %s" % key)

    # ⑩ 条目记录不许带 == 强调：章节页渲染它，条目页不渲染（geo_kit 那条路径
    #    没有这一步，中文站的条目记录也从不用它）。带进来就是页面上两个等号。
    from en_entries import ENTRIES as _EN
    for e in _EN:
        flat = repr(e)
        if "==" in flat:
            bad.append("entry %s uses == emphasis, which entry pages don't render"
                       % e["slug"])

    # ⑧⑨ 章节自身
    def words(x):
        return len(x.split())

    written = load_en()
    planned = {(c["parent_slug"], c["k"]) for c in H.CHAPTERS if c["parent_slug"] in PILOT}
    for ch in sorted(written, key=lambda c: (c["parent_slug"], c["k"])):
        if (ch["parent_slug"], ch["k"]) not in planned:
            bad.append("%s/%s is written in English but not in the pilot plan"
                       % (ch["parent_slug"], ch["k"]))
            continue
        where = "%s/%s" % (ch["parent_slug"], ch["k"])
        for field in ("n", "w", "src", "dek", "story", "apply"):
            if not (ch.get(field) or "").strip():
                bad.append("%s is missing %s" % (where, field))
        parts, quotes = ch.get("f") or [], ch.get("q") or []
        if len(parts) < 2:
            bad.append("%s has %d parts, needs at least 2" % (where, len(parts)))
        if len(quotes) < 2:
            bad.append("%s has %d lines to keep, needs at least 2" % (where, len(quotes)))
        n_emph = (ch.get("story") or "").count("==")
        if n_emph != 2:
            bad.append("%s: story needs exactly one ==...== span, found %d marks"
                       % (where, n_emph))
        for field, key in (("dek", "dek"), ("story", "story")):
            lo, hi = LEN[key]
            n = words(ch.get(field) or "")
            if not lo <= n <= hi:
                bad.append("%s: %s is %d words (want %d-%d)" % (where, field, n, lo, hi))
        for i, part in enumerate(parts, 1):
            for key in ("d", "eg"):
                lo, hi = LEN["part" if key == "d" else "eg"]
                n = words(part.get(key) or "")
                if not lo <= n <= hi:
                    bad.append("%s: part %d %s is %d words (want %d-%d)"
                               % (where, i, key, n, lo, hi))
        for q in quotes:
            if words(q) > LEN["quote"][1]:
                bad.append("%s: line to keep is %d words (max %d): %r"
                           % (where, words(q), LEN["quote"][1], q))

    # ⑪ 构建产物里不许剩中文
    en_dir = os.path.join(ROOT, "en")
    if os.path.isdir(en_dir):
        n_page = 0
        for dp, _dn, fn in os.walk(en_dir):
            for f in fn:
                if not f.endswith((".html", ".xml", ".txt", ".json")):
                    continue
                n_page += 1
                left = cjk_left(os.path.join(dp, f))
                if left:
                    rel = os.path.relpath(os.path.join(dp, f), ROOT)
                    bad.append("%s still has Chinese: %s"
                               % (rel, " | ".join(x[:50] for x in left[:2])))
                if len([x for x in bad if "still has Chinese" in x]) >= 5:
                    break
    else:
        bad.append("no en/ built yet — run python3 scripts/build_en.py")

    # ⑬ 英文页上真正用来排字的必须是拉丁字体。
    #    量的是**渲染之后 getComputedStyle 解出来的字体栈**，不是「源码里
    #    有没有那段覆盖」。第一版量的就是后者，而它是个代理：
    #    build_en 早就把 Google Fonts 链接换成了 Newsreader + Source Serif 4，
    #    覆盖规则却从来没进过仓库 —— 字体下载了，页面照旧拿宋体渲染拉丁
    #    字母，①-⑫ 全绿（它们只看有没有中文**字**，看不见用什么**字体**）。
    #    这段覆盖后来又丢了一次，所以判据必须落在结果上。
    #    判据的**内容**后来也改过一次：一开始拦的是「出现 CJK 字体名」，
    #    那是拦错了对象 —— 系统里的宋体和苹方本身是好西文字体，坏的是
    #    **下载**思源宋体那一类为配汉字设计的西文。见上面 ⓐ 的说明。
    r = rendered_fonts()
    if r is None:
        print("（没装 playwright，跳过英文字体检查）")
    else:
        for x in r:
            bad.append("英文页字体不对：%s" % x)

    # ⑭ 渲染之后的英文页上不许有排版硬伤（双空格 / 标点前空格 / 中文标点）
    fl = rendered_flaws()
    if fl is None:
        print("（没装 playwright，跳过渲染后的排版检查）")
    else:
        for x in fl[:6]:
            bad.append("英文页排版：%s" % x)

    # ⑫ 渲染之后的首页正文里也不许有中文
    r = rendered_cjk()
    if r is None:
        print("（没装 playwright，跳过渲染后的中文检查）")
    elif r:
        for x in r[:4]:
            bad.append("英文首页渲染后仍有中文：%s" % x)

    nq = sum(len(q) for _, _, q in SCENES)
    print("English: %d groups · %d situations · %d questions · "
          "%d entries · %d chapters planned · %d today's-lines · "
          "%d/%d chapters written"
          % (len({g for _, g, _ in SCENES}), len(SCENES), nq,
             len(hit_entry), len(hit_ch), len(QUOTE_ASKS_EN),
             len(written), len(planned)))
    if bad:
        print("\nnot ready:")
        for b in bad[:40]:
            print("  x " + b)
        if len(bad) > 40:
            print("  … and %d more" % (len(bad) - 40))
        return 1
    print("ok — every ref resolves, all inside the pilot set, no Chinese left, "
          "no duplicates, every entry and chapter reachable,\n   every chapter has a today's line that points back at it")
    return 0


if __name__ == "__main__":
    sys.exit(main())
