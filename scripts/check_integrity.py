#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站完整性闸门。

这个脚本收的都是本次会话里真实发生过、且当时没被任何检查拦住的错误：

  1. 加了条目却没写章节 —— 条目页没有「深度阅读」，也进不了「最新」
  2. 加了条目却没写手写介绍 —— 首页卡片回落到简介首句
  3. 加了章节却没生成分享图 —— 分享出去还是全站通用图
  4. 关联字段指向尚未收录的条目 —— 生成死链
  5. 新类别条目数不足却进了 slug 表 —— 主题页不生成，链接悬空
  6. 条目没有英文 slug —— 生成中文路径 URL
  7. 二维码被换坏 —— 页脚和分享卡的码扫不出来
  8. 写了 fail/lesson 却没有任何渲染器读它 —— 4525 字内容在页面上不存在
  9. 三条金句全与正文重复 —— 被 hw_theme 丢光，整个「金句」段不渲染
 10. 新条目没在 hw_kind 里归类过 —— 默认当成人，书被 schema.org 标成 Person
 11. 典籍没在 hw_omit 里被问过「不取哪一部分」—— 漏了不报，读者替你发现
 12. 标签掉到 hub_min 以下，话题页不再生成，但磁盘上那一页没人删 ——
     它继续 200、继续自指 canonical，只是从此不在任何 sitemap、任何导航里

每一条都曾经是「我以为做完了」。现在改成构建失败。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, "seo")
sys.path.insert(0, "scripts")

import build_seo          # noqa: E402
import hw_chapters as C   # noqa: E402
import hw_kind            # noqa: E402
import hw_omit            # noqa: E402
import hw_slugs           # noqa: E402

problems = []


def bad(kind, detail):
    problems.append("%s: %s" % (kind, detail))


entries = build_seo.load_array()
names = {e["n"] for e in entries}
parents = {c["parent"] for c in C.CHAPTERS}

# 1) 每个条目至少一篇深度阅读
for e in entries:
    if e["n"] not in parents:
        bad("条目无深度阅读", e["n"])

# 1b) 反向：有章节文件却没有对应条目
#     rebase 时若取了远端的 index.html，D 数组会退回旧版而 seo/chapters/ 仍是新的，
#     条目静默丢失。只查「条目→章节」发现不了，必须双向查。
for pname in sorted(parents):
    if pname not in names:
        bad("有章节但条目已丢失", pname)

# 2) 每个条目有手写介绍
try:
    src = open("scripts/force_chapter_ui.py", encoding="utf-8").read()
    seg = src[src.index("HWX_INTROS = {"):]
    seg = seg[:seg.index("\n}") + 2]
    ns = {}
    exec(seg, ns)
    intros = ns["HWX_INTROS"]
except Exception as exc:                      # pragma: no cover
    intros = {}
    bad("读取 HWX_INTROS 失败", exc)
for e in entries:
    slug = hw_slugs.slug_for(e["n"])
    if slug not in intros:
        bad("条目无手写介绍", "%s (%s)" % (e["n"], slug))

# 2.5) 「最新」里必须真的是最新的那一批。
#      NC 按章节文件的 git **首次提交时间**排序，而构建发生在提交之前 ——
#      新写的章节那时还没进 git，git log 返回空，时间戳算成 0，排到最后：
#      **新加的人永远进不了「最新」**。页面照常渲染、链接照常通、别的闸照常绿，
#      只有那一格永远看不到今天加的东西。改成每天一条之后，这条会每天咬一次。
#      判据：最近一次提交里新增的章节文件，它的章必须出现在 NC 里。
import subprocess as _sp
try:
    _new = _sp.run(["git", "diff", "--name-only", "--diff-filter=A", "HEAD~1", "HEAD",
                    "--", "seo/chapters/"], capture_output=True, text=True).stdout.split()
except Exception:
    _new = []
if _new:
    _home = open("index.html", encoding="utf-8", errors="ignore").read()
    _i = _home.find('"NC":[')
    # HWXD（含 NC）自 2026-09-06 起外置到 assets/home-hwxd.js（首页瘦身），
    # 首页里只剩一个 <script src>。这条判据第一版只看 index.html，
    # 于是在数据外置之后对每一条新章节都报「没进最新」—— 自己的两处改动撞车了。
    if _i < 0 and os.path.exists("assets/home-hwxd.js"):
        _home = open("assets/home-hwxd.js", encoding="utf-8", errors="ignore").read()
        _i = _home.find('"NC":[')
    _nc = _home[_i:_i + 6000] if _i > 0 else ""
    for _f in _new:
        _slug = os.path.basename(_f)[:-3].replace("_", "-")
        if _slug and ('"s":"%s"' % _slug) not in _nc:
            bad("新章节没进「最新」",
                "%s —— 构建跑在提交之前时 git log 是空的，时间戳算成 0" % _slug)

# 2.6) 「今日一篇」必须指向**最新那一条**，不能退回轮播。
#      站里每天真加一个人，而这张写着「今日」的卡原来是
#      `D.E[(day*7)%D.E.length]` —— 一个纯轮播，和今天加了谁毫无关系。
#      它是新内容唯一的正门；退回轮播不报错、不溢出，只是每天新写的东西
#      在首屏上没有任何位置。
_home_js = open("index.html", encoding="utf-8", errors="ignore").read()
if "var p1=D.E[D.E.length-1];" not in _home_js:
    bad("今日一篇不是最新那条", "首页又变回轮播了（找不到 D.E[D.E.length-1]）")
# 「今日一句」开局也要落在最新那个人身上（点「换一换」之后才进轮播）。
# 退回 day%D.QP.length 不报错、不溢出，只是每天新写的东西在首屏又没了位置。
if "if(D.QP[i].who===newest) return i;" not in _home_js:
    bad("今日一句开局不是最新那条", "首页又变回纯轮播了")

# 3) 每篇章节有专属分享图
for ch in C.CHAPTERS:
    png = os.path.join("i", hw_slugs.slug_for(ch["parent"]), ch["k"], "og.png")
    if not os.path.exists(png):
        bad("章节无分享图", png)

# 4) 关联字段只能指向已收录的条目（前向引用会生成死链）
home = open("index.html", encoding="utf-8").read()
for ref in set(re.findall(r'\{n:"([^"]+)",why:', home)):
    if ref not in names:
        bad("contrast 指向未收录条目", ref)
for block in re.findall(r'l:\[([^\]]*)\]', home):
    for ref in re.findall(r'"([^"]+)"', block):
        if ref not in names:
            bad("l 指向未收录条目", ref)

# 5) 类别要么条目数达标、要么不进 slug 表（否则主题页不生成，链接悬空）
HUB_MIN = 3
counts = {}
for e in entries:
    counts[e["c"]] = counts.get(e["c"], 0) + 1
tag_slugs = getattr(hw_slugs, "TAG_SLUGS", {})
for cat, n in counts.items():
    if cat in tag_slugs and n < HUB_MIN:
        bad("类别进了 slug 表但条目不足",
            "%s 只有 %d 个，需要 %d" % (cat, n, HUB_MIN))

# 6) 条目必须有英文 slug
for e in entries:
    slug = hw_slugs.slug_for(e["n"])
    if re.search(r"[\u4e00-\u9fff]", slug or ""):
        bad("条目无英文 slug", "%s → %s" % (e["n"], slug))

# 6b) 条目名里不能有空格
#     「延伸」区按词切分渲染，含空格的名字会被拆成两个链接
#     （BJ 福格 → /i/bj/ 和 /i/福格/，两个都是死链）。用 · 代替空格。
for e in entries:
    if " " in e["n"] or "\u3000" in e["n"]:
        bad("条目名含空格", "%s —— 会被「延伸」区拆成两个死链，用 · 代替" % e["n"])

# 6b) 写了 fail/lesson 就必须真的渲染出来
#     真实事故：23 个条目写了「败局时刻」+ 教训，合计 4525 字，
#     而全站没有任何渲染器读这两个字段——大概是 2026-08-17 改版
#     （首页卡片从浮层改成跳 /i/<slug>/）之后的遗留。
#     内容存在、闸门全绿、页面上一个字都没有，躺了两周没人发现。
#     这一条把「写了」和「看得见」绑死。
for e in entries:
    if not (e.get("fail") or e.get("lesson")):
        continue
    _sl = hw_slugs.slug_for(e["n"])
    _f = "i/%s/index.html" % _sl
    if not os.path.exists(_f):
        bad("败局未渲染", "%s 有 fail/lesson 但条目页不存在（%s）" % (e["n"], _f))
        continue
    _h = open(_f, encoding="utf-8").read()
    if e.get("fail"):
        _probe = re.sub(r"<[^>]+>", "", e["fail"])[:18]
        if _probe and _probe not in _h:
            bad("败局未渲染", "%s 的 fail 不在 %s 里" % (e["n"], _f))
    for _l in (e.get("lesson") or [])[:1]:
        _probe = re.sub(r"<[^>]+>", "", _l)[:16]
        if _probe and _probe not in _h:
            bad("败局未渲染", "%s 的 lesson 不在 %s 里" % (e["n"], _f))

# 6c) 写了金句，就必须真的渲染出「金句」段
#     hw_theme 会丢掉与正文重复的金句——它的注释写着「100 个条目里有 55 个
#     把分则开头那句又在文末列一遍」。全部被丢光时，整个「金句」段不渲染：
#     页面上一个字都没有，而所有既有检查都通过。
#     2026-09-01 普查：128 个条目里 27 个中招，21%。存量太多，一次改不完，
#     所以做成棘轮——存量挂在下面这张表里，新增条目再犯直接失败。
#     **这张表只许变短。** 改好一个就从表里删一个；往里加名字等于把问题藏起来。
#
#     同日走完，27 → 0。其中 22 个的根因不是「写重了」，是 hw_theme 原来把
#     「与本条目章节的金句重复」也当成硬过滤——可章节金句并不出现在条目页上，
#     读者在这一页没见过它，孙子兵法的「知己知彼」这类名句本来就该两边都有。
#     那条规则已降为优先级（同页去重照旧从严）。剩下 4 个是真与本页正文重复，
#     给它们各补了两条正文里没有的原句。
#     表清空了但检查留着：新增条目再犯照样失败。
LEGACY_NO_QUOTES = set()   # 2026-09-01 清空：27 → 0，棘轮走完了
_no_q = []
for e in entries:
    if not e.get("q"):
        continue
    _f = "i/%s/index.html" % hw_slugs.slug_for(e["n"])
    if not os.path.exists(_f):
        continue
    if '<h2 class="sec-k">金句</h2>' not in open(_f, encoding="utf-8").read():
        _no_q.append(e["n"])
for _n in _no_q:
    if _n not in LEGACY_NO_QUOTES:
        bad("金句段未渲染",
            "%s 写了 %d 条金句，但页面上没有「金句」段——多半三条全与正文重复，"
            "被 hw_theme 丢光了。换成正文里没有出现过的句子。"
            % (_n, len([x for x in entries if x["n"] == _n][0].get("q") or [])))
_fixed = LEGACY_NO_QUOTES - set(_no_q)
if _fixed:
    bad("请从 LEGACY_NO_QUOTES 里删掉已修好的条目", "、".join(sorted(_fixed)))
print("金句段：%d/%d 个条目正常渲染；历史遗留 %d 个待修"
      % (len(entries) - len(_no_q), len(entries), len(_no_q)))

# 7) 信息流里同类卡片不得重复
#    真实事故：金句取用写成 (i*53) % 池大小，而池子正好 53 条，
#    于是两个 feed 里所有金句卡都是同一句。用浏览器跑一遍实际渲染来验。
def check_feed_dupes():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("（跳过信息流查重：无 playwright）")
        return
    import subprocess, time
    srv = subprocess.Popen(["python3", "-m", "http.server", "8971"], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2.5)
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            # locale 必须给中文：首页的首访跟随会把 navigator.languages 里
            # 完全没有 zh 的浏览器送去 /en/，而 headless Chromium 默认是 en-US。
            # 不指定的话这道闸测的是英文站，然后报「#hwx-tabs2 是 undefined」
            # —— 一个和真实问题毫无关系的错。
            pg = b.new_page(viewport={"width": 390, "height": 1200},
                            locale="zh-CN")
            pg.goto("http://localhost:8971/", timeout=30000)
            pg.wait_for_timeout(1800)
            for tab, sel in (("最新", "#hwx-ncfeed"), ("全部", "#hwx-feed")):
                if tab == "全部":
                    pg.evaluate("()=>document.querySelectorAll('#hwx-tabs2 button')[1].click()")
                    pg.wait_for_timeout(800)
                got = pg.evaluate("""(s)=>{var o={};
                  ['.qc','.pc','.nc','.kc'].forEach(function(k){
                    o[k]=Array.from(document.querySelectorAll(s+' '+k))
                          .map(function(e){return (e.innerText||'').slice(0,40)})});
                  return o}""", sel)
                for kind, texts in got.items():
                    if len(texts) > 1 and len(set(texts)) < len(texts):
                        from collections import Counter
                        worst = Counter(texts).most_common(1)[0]
                        bad("信息流卡片重复",
                            "%s tab 的 %s：%d 张里只有 %d 种，最多的一张出现 %d 次"
                            % (tab, kind, len(texts), len(set(texts)), worst[1]))
            b.close()
    finally:
        srv.terminate()


check_feed_dupes()

# 7b) 首页显示的条目数必须与实际一致
#     写死过三次（95 → 100 → 115），每次加条目都漏改，而详情页的 slogan 是自动的，
#     于是两边对不上。
import re as _re
_n = len(entries)
# 标语已从计数式改为「遇到事了，看看以前的人怎么处理」，
# 页面上不再有需要跟数据同步的数字；改为检查各类页面标语一致。
_slogan = "遇到事了，看看以前的人怎么处理"
for _f in ("index.html", "all/index.html"):
    if os.path.exists(_f) and _slogan not in open(_f, encoding="utf-8").read():
        bad("标语缺失或不一致", _f)

# 7c) 首页 div 必须配平
#     用正则删过一个带嵌套的块，替换串多补了一个 </div>，父容器被提前关闭，
#     其后所有内容逃出 .wrap，整页左右边距消失——而所有既有检查都通过了。
_open, _close = home.count("<div"), home.count("</div>")
if _open != _close:
    bad("首页 div 不配平", "开 %d 闭 %d，差 %+d" % (_open, _close, _close - _open))

# 10) 每个条目都要在 hw_kind 里被判过一次：是人，还是作品
#     判的是「有没有做过这个判断」，不是「判得对不对」——对不对只能靠眼睛。
#     原来是「WORKS + 默认是人」，默认值替人做了决定又不吭声：《易经》
#     《菜根谭》《薄伽梵歌》《最后一版》四条被 schema.org 标成 Person，
#     从收进来那天起，二十道闸一条都没响（hw_kind.py 文件头记了这件事）。
_miss, _both = hw_kind.unclassified(sorted(names))
for n in _miss:
    bad("条目没有归类", "%s —— 去 seo/hw_kind.py 落进 WORKS 或 PEOPLE" % n)
for n in _both:
    bad("条目归类自相矛盾", "%s 同时在 WORKS 和 PEOPLE 里" % n)

# 11) 每一部典籍都要被问过「哪一部分我们不取」。写 None 是合法答案，
#     这条判的是「问过没有」，不是「有没有免责声明」。
#     键钉死在 WORKS 上：少一条是新收的书没问，多一条是从 WORKS 挪走了
#     却忘了在这边删 —— 后一种更隐蔽，所以两个方向都报。
_omit_miss, _omit_extra = hw_omit.mismatch(hw_kind.WORKS)
for n in _omit_miss:
    bad("典籍没问过不取哪部分", "%s —— 去 seo/hw_omit.py 写一句，或写 None" % n)
for n in _omit_extra:
    bad("hw_omit 里多了一条", "%s 不在 hw_kind.WORKS 里，该删" % n)

# 12) /t/ 下不许有孤儿话题页。
#     话题页是按标签出的：某个标签的条目掉到 hub_min 以下、或掉出前 40，
#     构建就不再出它 —— 但**已经写在磁盘上的那一页不会被删**，它继续 200，
#     继续自指 canonical，只是从此不在任何 sitemap、不在任何导航里。
#     /t/classics/ 和 /t/human-nature/（中文站和繁体站各一份，约 20KB）
#     就是这么留下的：没有任何条目还挂着「典籍·洞见」「处世·人性」这两个标签，
#     而两个跳转桩还在往里指。查链接的闸抓不到 —— 没有人链接它，正是问题本身。
#     判据：/t/ 下每个目录，要么它的 slug 在本语言的 sitemap 里（当前话题页），
#     要么它是一个跳转桩、且目的地在 sitemap 里。
def _topic_orphans():
    out = []
    for base, smap, pref in (("t", "sitemap.xml", "/t/"),
                             ("en/t", "en/sitemap.xml", "/en/t/"),
                             ("tw/t", "tw/sitemap.xml", "/tw/t/")):
        if not os.path.isdir(base) or not os.path.isfile(smap):
            continue
        sm = open(smap, encoding="utf-8").read()
        # 只认 <loc>：sitemap 里还有 xhtml:link 语言标注，它们会把别的语言的
        # 地址也带进来，拿那个当「在不在 sitemap 里」会把孤儿放过去。
        live = set(re.findall(r"<loc>" + re.escape("https://ourword.ai" + pref)
                              + r"([^/\"<]+)/</loc>", sm))
        if not live:
            continue
        for d in sorted(os.listdir(base)):
            f = os.path.join(base, d, "index.html")
            if not os.path.isfile(f):
                continue
            if d in live:
                continue
            t = open(f, encoding="utf-8").read()
            m = re.search(r'http-equiv="refresh"[^>]*url=([^"\']+)', t)
            if not m:
                out.append((os.path.join(base, d), "整页留在磁盘上，却不在 sitemap 里"))
                continue
            dest = m.group(1).rstrip("/").rsplit("/", 1)[-1]
            if dest not in live:
                out.append((os.path.join(base, d), "跳转桩指向已经不存在的 /%s/" % dest))
    return out


for _p, _why in _topic_orphans():
    bad("话题页成了孤儿", "%s —— %s" % (_p, _why))

# 8) 二维码必须仍可解码
try:
    from PIL import Image
    from pyzbar.pyzbar import decode
    got = [x.data.decode() for x in decode(Image.open("wechat-qr.png"))]
    if not got:
        bad("二维码扫不出", "wechat-qr.png")
    elif "weixin.qq.com" not in got[0]:
        bad("二维码指向异常", got[0])
except ImportError:
    print("（跳过二维码检查：缺 pyzbar/PIL）")
except Exception as exc:
    bad("二维码读取失败", exc)

print("条目 %d / 章节 %d / 覆盖 %d 个条目" % (len(entries), len(C.CHAPTERS), len(parents)))
if problems:
    print("完整性问题 %d 处：" % len(problems))
    for p in problems[:40]:
        print("  - " + p)
    sys.exit(1)
print("完整性检查全部通过 ✅")
