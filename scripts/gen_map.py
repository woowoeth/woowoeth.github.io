#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 MAP.md —— 内容结构地图。

存在的理由：这个库有四层（条目 → 章节 → 处境 → 问题 → 答案），
层与层之间是多对多的，光看目录看不出「哪一篇被几个处境指着」「哪个处境挂在哪些人身上」。
手写一份会立刻过期，所以从数据现算。

用法：python3 scripts/gen_map.py   （写入仓库根的 MAP.md）
"""
import os
import sys
import re
import json
import collections
import importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "seo"))
from hwx_scenes import SCENES  # noqa: E402

ch, by_parent = {}, collections.OrderedDict()
cdir = os.path.join(ROOT, "seo", "chapters")
for f in sorted(os.listdir(cdir)):
    if not f.endswith(".py") or f.startswith("__"):
        continue
    sp = importlib.util.spec_from_file_location("x", os.path.join(cdir, f))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    p, s = m.PARENT["name"], m.PARENT["slug"]
    by_parent[p] = (s, m.CHAPTERS)
    for c in m.CHAPTERS:
        ch[(s, c["k"])] = (p, c["n"])

h = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
D = h[h.index("const D=["):]
cat = {mm.group(2): mm.group(1) for mm in re.finditer(r'\{c:"(.*?)",n:"(.*?)"', D)}

used = collections.Counter()
scene_of = collections.defaultdict(set)
for n, g, QS in SCENES:
    for q, ans in QS:
        for a in ans:
            used[tuple(a)] += 1
            scene_of[tuple(a)].add(n)

groups = collections.OrderedDict()
for n, g, QS in SCENES:
    groups.setdefault(g, []).append((n, QS))

nq = sum(len(q) for _, _, q in SCENES)
na = sum(len(a) for _, _, QS in SCENES for _, a in QS)
out = []
w = out.append

w("# 内容地图")
w("")
w("由 `scripts/gen_map.py` 从数据现算，不要手改。")
w("")
w("## 一、规模")
w("")
w("| 层 | 数量 | 真源 |")
w("|---|---:|---|")
w("| 条目 | %d | `index.html` 的 `D[]` |" % len(by_parent))
w("| 章节 | %d | `seo/chapters/*.py` |" % len(ch))
w("| 处境 | %d | `scripts/hwx_scenes.py` |" % len(SCENES))
w("| 问题 | %d | 同上 |" % nq)
w("| 答案 | %d | 同上，指向具体章节 |" % na)
w("")
w("章节可达率 **%d / %d**——每一篇都至少有一个处境走得到。" % (sum(1 for k in ch if used[k]), len(ch)))
w("")

w("## 二、条目按分类")
w("")
cc = collections.Counter(cat.get(p, "?") for p in by_parent)
w("| 分类 | 条目 | 章节 |")
w("|---|---:|---:|")
for k, v in cc.most_common():
    nch = sum(len(by_parent[p][1]) for p in by_parent if cat.get(p) == k)
    w("| %s | %d | %d |" % (k, v, nch))
w("")
docat = collections.defaultdict(list)
for p in by_parent:
    docat[cat.get(p, "?")].append(p)
for k, _v in cc.most_common():
    w("**%s**　%s" % (k, "、".join(docat[k])))
    w("")

w("## 三、处境层")
w("")
w("| 组 | 处境 | 问题 |")
w("|---|---:|---:|")
for g, items in groups.items():
    w("| %s | %d | %d |" % (g, len(items), sum(len(q) for _, q in items)))
w("")
for g, items in groups.items():
    w("### %s" % g)
    w("")
    w("| 处境 | 问 | 主要挂在谁身上 |")
    w("|---|---:|---|")
    for n, QS in items:
        who = collections.Counter()
        for q, ans in QS:
            for a in ans:
                who[ch[tuple(a)][0]] += 1
        w("| %s | %d | %s |" % (n, len(QS), "、".join(x for x, _ in who.most_common(4))))
    w("")

w("## 四、被指向最多的章节")
w("")
w("万金油被引得多，往往说明别处还没有更对路的。要深挖，从这里入手比从缺口入手准。")
w("")
w("| 次 | 章节 | 出现在哪些处境 |")
w("|---:|---|---|")
for k, c in used.most_common(15):
    p, n = ch[k]
    ss = sorted(scene_of[k])
    w("| %d | %s · %s | %s |" % (c, p, n, "、".join(ss[:5]) + ("…" if len(ss) > 5 else "")))
w("")

w("## 五、只被指向一次的章节")
w("")
once = [(ch[k][0], ch[k][1]) for k in ch if used[k] == 1]
w("共 **%d** 篇。不是问题——有些原理本来就只罩一个局面；" % len(once))
w("但如果某一篇明明能罩更多，这里就是它被埋着的证据。")
w("")
for p, n in sorted(once):
    w("- %s · %s" % (p, n))
w("")

open(os.path.join(ROOT, "MAP.md"), "w", encoding="utf-8").write("\n".join(out))
print("MAP.md：%d 行 / %d 字节" % (len(out), len("\n".join(out).encode("utf-8"))))
