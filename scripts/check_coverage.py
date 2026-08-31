#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""处境层覆盖闸门——防止「写了但用户找不到」。

四层数据的依赖关系：

    条目 D[]            index.html 里的 const D=[...]，全站唯一真源
      └─ 章节           seo/chapters/<slug>.py，PARENT + CHAPTERS
           └─ 处境      scripts/hwx_scenes.py，场景名 → 问题 → 答案(slug, k)
                └─ 问题 首页「今日一问」与信息流问题卡共用同一个池

    条目 → 章节：由 check_integrity.py 双向强制，每个条目必须有章节
    章节 → 处境：由本脚本强制，新写的章节必须挂进至少一个问题

为什么需要这一条：加内容时很容易只写条目和章节就收工，而处境层是用户
实际进入内容的入口。曾经出现过 9 个家庭与关系的条目全部写完、处境层却
一个都挂不上的情况——内容存在，没有任何路径能走到它。

三条规则：

  ① 每个条目至少要有一篇章节被问题引用（不能整个条目对用户不可达）
  ② 每个领域的覆盖率不得低于阈值——某一领域集体失联时报警
  ③ 全站章节覆盖率不得低于 MIN_TOTAL

覆盖率不要求 100%：有些章节是同一条目下的补充视角，挂不挂看内容，
但一个条目一篇都不挂，就是漏了。
"""
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, "seo")
sys.path.insert(0, "scripts")

import build_seo          # noqa: E402
import hw_chapters as C   # noqa: E402
import hw_slugs           # noqa: E402
from hwx_scenes import SCENES  # noqa: E402

MIN_TOTAL = 0.70          # 全站章节被问题引用的下限
MIN_PER_DOMAIN = 0.40     # 单个领域的下限

entries = build_seo.load_array()
cat_of = {e["n"]: e["c"] for e in entries}
name_by_slug = {hw_slugs.slug_for(e["n"]): e["n"] for e in entries}

used = set()
for _, _g, group in SCENES:
    for _, refs in group:
        for r in refs:
            used.add(tuple(r))

all_ch = {(hw_slugs.slug_for(c["parent"]), c["k"]) for c in C.CHAPTERS}
problems = []

# ① 每个条目至少一篇章节可达
by_entry = defaultdict(list)
for c in C.CHAPTERS:
    by_entry[c["parent"]].append((hw_slugs.slug_for(c["parent"]), c["k"]))
unreachable = sorted(n for n, ks in by_entry.items() if not any(k in used for k in ks))
for n in unreachable:
    problems.append("条目进不了处境层: %s（写了 %d 篇章节，一篇都没挂到问题上）"
                    % (n, len(by_entry[n])))

# ② 领域覆盖率
dom_all, dom_used = Counter(), Counter()
for c in C.CHAPTERS:
    d = cat_of.get(c["parent"], "?")
    dom_all[d] += 1
    if (hw_slugs.slug_for(c["parent"]), c["k"]) in used:
        dom_used[d] += 1
for d, total in dom_all.items():
    rate = dom_used[d] / total if total else 0
    if rate < MIN_PER_DOMAIN:
        problems.append("领域覆盖不足: %s 只有 %d/%d (%.0f%%) 的章节能被问到，下限 %.0f%%"
                        % (d, dom_used[d], total, 100 * rate, 100 * MIN_PER_DOMAIN))

# ③ 全站覆盖率
rate = len(used & all_ch) / len(all_ch) if all_ch else 0
if rate < MIN_TOTAL:
    problems.append("全站覆盖不足: %d/%d (%.0f%%)，下限 %.0f%%"
                    % (len(used & all_ch), len(all_ch), 100 * rate, 100 * MIN_TOTAL))

print("条目 %d → 章节 %d → 处境 %d → 问题 %d → 答案 %d"
      % (len(entries), len(C.CHAPTERS), len(SCENES),
         sum(len(g) for _, _x, g in SCENES),
         sum(len(r) for _, _x, g in SCENES for _, r in g)))
print("章节可达率 %d/%d (%.0f%%)" % (len(used & all_ch), len(all_ch), 100 * rate))

if problems:
    print("覆盖问题 %d 处：" % len(problems))
    for p in problems:
        print("  - " + p)
    print()
    print("补内容时，处境层要一起补：在 scripts/hwx_scenes.py 里给新章节")
    print("挂上问题，或新增处境。问题本身的写法见 scripts/check_questions.py。")
    sys.exit(1)
print("处境层覆盖检查通过 ✅")
