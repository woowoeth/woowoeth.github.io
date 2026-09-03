#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""教训有没有编译成闸。

学 WikiSkill（arXiv:2608.27454）那三层：**原始经验 / 沉淀的知识 / 可执行的技能**。
这个仓前两层一直有（会话记录、HANDOVER.md），第三层也有（七道闸），
缺的是**中间那道编译** —— 教训写完就躺在文档里，等下次碰巧读到。

论文的消融实验里，去掉知识固化那一层，平均分从 63.7% 掉到 48.7%。
那 15 个点就是「记了但没编译」的代价。

所以这道闸只干一件事：**逼 FAILURES.md 里每条教训显式说明去向。**

判据：
  ① 每个 `##` 段落必须有一行 `**闸：**`
  ② 点名的脚本必须存在，且真的挂在 gate.py 的 CHECKS 上（不是写着好看）
  ③ 点名的闸必须在 gate_selftest.py 里有反向注入
     —— 例外一：`gate_selftest.py` 自己。它不可能出现在自己的用例表里
        （谁来验自检），所以对它改成要求 `preflight()` 自验存在。
     —— 例外二：`tests/` 下的测试不走 gate.py，改成要求文件存在且能跑。
     豁免要写进判据，不能靠改文档绕过去。
  ④ 写「无」的必须给理由（`无 —— <理由>`），不能空着糊过去

**这道闸不逼你造闸，只逼你把账认了。** 写「无」不丢人 —— 这张表里就有两条是「无」，
一条的结论是「类别判断该用眼睛」，另一条是「值不值得写只能人定」。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "FAILURES.md")

if not os.path.exists(DOC):
    print("✗ 找不到 FAILURES.md —— 教训台账是这道闸的输入")
    sys.exit(1)

RUNNER = open(os.path.join(HERE, "gate.py"), encoding="utf-8").read()
SELF = open(os.path.join(HERE, "gate_selftest.py"), encoding="utf-8").read()
txt = open(DOC, encoding="utf-8").read()

# 文件头那段说明也用 ## 分段会被算成教训，所以从第一个 `---` 之后才开始数
body = txt.split("\n---\n", 1)[-1]
parts = re.split(r"^## ", body, flags=re.M)[1:]

bad, gated, judged = [], [], []

for p in parts:
    title = p.split("\n", 1)[0].strip()
    m = re.search(r"^\*\*闸：\*\*\s*(.+)$", p, re.M)
    if not m:
        bad.append((title, "没写去向（缺 `**闸：**` 那一行）"))
        continue
    v = m.group(1).strip()

    if v.startswith("无"):
        if not re.search(r"无\s*——\s*\S", v):
            bad.append((title, "写了「无」但没给理由"))
        else:
            judged.append(title)
        continue

    scripts = re.findall(r"`([\w./-]+\.py)`", v)
    if not scripts:
        bad.append((title, "看不出点名了哪个脚本：%s" % v[:40]))
        continue

    for s in scripts:
        path = os.path.join(ROOT, s)
        name = os.path.basename(s)
        if not os.path.exists(path):
            bad.append((title, "点名的 %s 不存在" % s))
        elif s.startswith("tests/"):
            # 例外二：tests/ 下的不走 gate.py，只要求存在（上面已查）
            gated.append((title, s))
        elif name == "gate_selftest.py":
            # 例外一：自检没法进自己的用例表，改为要求 preflight 自验
            if "def preflight(" not in SELF or "recover_pending(quiet=True)" not in SELF:
                bad.append((title, "gate_selftest.py 自己没了 preflight 自验"
                                   "（它没法进自己的用例表，只能靠这个）"))
            else:
                gated.append((title, s))
        elif '"%s"' % name not in RUNNER:
            bad.append((title, "%s 没挂在 gate.py 的 CHECKS 上（写着好看）" % s))
        elif name not in SELF:
            bad.append((title, "%s 在 gate_selftest.py 里没有反向注入"
                               "（只验好稿能过等于没验）" % s))
        else:
            gated.append((title, s))

print("教训 %d 条 · 编译成闸 %d 条 · 明确人判 %d 条"
      % (len(parts), len({t for t, _ in gated}), len(judged)))
if judged:
    print("\n明确人判（写了「无」并给了理由）：")
    for t in judged:
        print("  ·", t)
if bad:
    print("\n不合格：")
    for t, why in bad:
        print("  ✗ %s —— %s" % (t, why))
    sys.exit(1)
print("✓ 每条教训的去向都写明了")
