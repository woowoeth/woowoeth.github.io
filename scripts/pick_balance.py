#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题闸：最近加的这几条，是不是一直在同一个文化圈里打转。

    python3 scripts/pick_balance.py        # 日更选人**之前**跑

为什么要有它（2026-09-17 加）：

  日更选人的判据只有两条——「哪个处境最空」和「他补的是哪一句」。这两条都对，
  但它们**合起来有一个谁也没打算要的副作用**：最空的处境常年是
  【AI 来了】【自己的状态】【世界如何运转】那几组，而那是西方社会科学的主场。
  于是选人一路往那边滑。日更前八天——伊里奇、薇依、波斯曼、赫希曼、
  金德尔伯格、帕金森、默顿、阿克塞尔罗德——**八条全是外国人，没有一天有人察觉**。
  全站底盘其实是平的（88 中 / 79 外），偏的是这条选人规则。

  这正是「量了代理指标当结果」的形状：每一天单独看都是对的（最空 + 补得准），
  连起来看就偏了。**单条的判据拦不住连起来才显形的偏差**，所以要有一条
  只看序列、不看单条的判据。

为什么不挂进 gate.py：gate 管的是**产物**对不对，它在每次构建时跑。选题偏不偏
是**选之前**的事，挂上去只会在一堆无关的提交上红，然后被人习惯性忽略——
那就等于没有。它的位置是日更第一步，红了就换一个文化圈再选。

表怎么维护：只标它要打印的那些条目，缺了会点名叫你补，不用一次标全站 167 条。
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOOK = 8          # 往回看几条
STREAK = 3        # 连续几条同一侧就算偏

# 来源。判据是「这条内容长在哪个文化里」，不是作者护照——
# 《薄伽梵歌》《枪炮病菌与钢铁》都归「外」，日本、印度、阿拉伯也归「外」：
# 这张表分的是「中文读者自己的传统」和「别人的传统」，两侧都该有人。
CN = {
    "lin-xiangru", "lushi-chunqiu", "yanshi-jiaxun",
    "analects", "bai-gui", "caigentan", "cao-cao",
    "chu-shijian", "du-fu", "fan-li", "feng-dao", "guan-zhong", "guiguzi",
    "guo-jia", "guo-ziyi", "han-feizi", "han-xin", "hu-xueyan", "huineng",
    "huo-qubing", "i-ching", "li-bi", "li-ka-shing", "li-shimin", "liu-bang",
    "mao", "mencius", "pu-songling", "records-of-the-grand-historian",
    "ren-zhengfei", "shang-yang", "shi-tiesheng", "sima-qian", "sima-yi",
    "strategies-of-the-warring-states", "su-shi", "su-yu", "sun-tzu",
    "tao-te-ching", "tao-yuanming", "wang-jian", "wang-xing", "wang-yangming",
    "wu-zetian", "xiang-yu", "xunzi", "zeng-guofan", "zhang-juzheng",
    "zhang-liang", "zhang-yiming", "zhu-yuanzhang", "zhuangzi", "zhuge-liang",
    "zizhi-tongjian", "bai-juyi", "liu-yan", "lee-kuan-yew",
    "duan-yongping", "huang",
}
FO = {
    "bhagavad-gita", "churchill", "curie", "illich", "weil", "postman",
    "hirschman", "kindleberger", "parkinson", "merton", "axelrod",
    "becker", "cowan",
}


def recent(n):
    """按**加入顺序**取最近 n 个条目的 slug（git 里第一次出现的那一笔）。"""
    out = subprocess.run(
        ["git", "-C", ROOT, "log", "--reverse", "--pretty=format:",
         "--diff-filter=A", "--name-only", "--", "seo/chapters/"],
        capture_output=True, text=True, check=True).stdout
    files = [l for l in out.splitlines() if l.startswith("seo/chapters/")]
    return [os.path.basename(f)[:-3].replace("_", "-") for f in files][-n:]


def name_of(slug):
    s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    for c, n, e in re.findall(r'\{c:"([^"]+)",n:"([^"]+)",e:"([^"]+)"', s):
        import hw_slugs
        if hw_slugs.SLUGS.get(n) == slug:
            return n, e
    return slug, ""


def main():
    sys.path.insert(0, os.path.join(ROOT, "seo"))
    rows, unknown = [], []
    for slug in recent(LOOK):
        side = "中" if slug in CN else ("外" if slug in FO else None)
        if side is None:
            unknown.append(slug)
        rows.append((slug, side))

    for slug, side in rows:
        n, e = name_of(slug)
        print("  %-4s %-14s %s" % (side or "??", n, e))

    if unknown:
        print("\n✗ 这几条没标来源：%s" % "、".join(unknown))
        print("  去 scripts/pick_balance.py 的 CN / FO 表里加一行再跑。")
        return 1

    tail = [s for _, s in rows]
    run = 1
    for a, b in zip(tail, tail[1:]):
        run = run + 1 if a == b else 1
    if run >= STREAK:
        print("\n✗ 已经连续 %d 条「%s」。今天换一边选。" % (run, tail[-1]))
        print("  判据仍然是「哪个处境最空 + 他补的是哪一句」，只是候选池先换一侧；")
        print("  换不出补得准的人，就说清楚为什么，别硬凑一个来解这条红。")
        return 1
    print("\n✓ 最近 %d 条没有连着 %d 条同一侧" % (len(rows), STREAK))
    return 0


if __name__ == "__main__":
    sys.exit(main())
