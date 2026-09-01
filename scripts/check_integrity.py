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
LEGACY_NO_QUOTES = {
    "BJ·福格",
    "优秀的绵羊",
    "克里斯·沃斯",
    "关键对话",
    "卡尔·波普尔",
    "卡尔·纽波特",
    "原子习惯",
    "塞涅卡",
    "契克森米哈赖",
    "孙子兵法",
    "孟子",
    "托马斯·戈登",
    "拉罗什富科",
    "王翦",
    "王阳明",
    "白圭",
    "约翰·戈特曼",
    "约翰·瑞迪",
    "维果茨基",
    "艾利克森",
    "萨波尔斯基",
    "费曼",
    "霍去病",
    "非暴力沟通",
    "马基雅维利",
    "鲍恩",
}
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
            pg = b.new_page(viewport={"width": 390, "height": 1200})
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
