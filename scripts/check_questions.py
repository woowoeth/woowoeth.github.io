#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""问题卡的内容运营标准。

这些问题是首页一问和信息流问题卡共用的池子，是整个站最靠前的一层——
问题本身不戳中人，卡片设计得再好也没用。所以它有独立于工程校验的一套标准。

标准来自一句定位：「遇到事了，看看以前的人怎么处理」。
问题必须是**当事人此刻会对自己说的那句话**，不是一个可以拿去查资料的题目。

四条否决项：

  ① 不能是查资料的语气
     ✗ 怎么让自己迈出第一步？        —— 这是想学个方法
     ✓ 我知道该做，可就是动不了。     —— 这是正卡着

  ② 不能是抽象名词堆的分析题
     ✗ 什么样的资产才是真正的资产？
     ✓ 钱放着不动，心里发慌。

  ③ 必须带人称或情境词，读起来像一个人在说话而不是一道题
     ✗ 砍掉哪些才是对的？
     ✓ 事情越堆越多，我已经不知道先干哪个了。

  ④ 长度 8-18 字。短于 8 撑不起情境，长于 18 一眼读不完。

用法：python3 scripts/check_questions.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from hwx_scenes import SCENES  # noqa: E402

LOOKUP_START = re.compile(r"^(怎么|如何|该怎么|怎样)")
ABSTRACT = ("价值", "本质", "机制", "逻辑", "维度", "要素", "原则", "方法论")
PERSON = ("我", "自己", "你")
SITUATION = ("了", "还", "就", "可", "但", "却", "又", "总")


def check(q):
    """返回这条问题违反的标准列表，空列表表示合格。"""
    bad = []
    if LOOKUP_START.match(q):
        bad.append("查资料语气")
    if any(w in q for w in ABSTRACT):
        bad.append("抽象词")
    if not (any(w in q for w in PERSON) or any(w in q for w in SITUATION)):
        bad.append("无人称无情境")
    n = len(q)
    if n < 8:
        bad.append("过短(%d)" % n)
    elif n > 18:
        bad.append("过长(%d)" % n)
    return bad


def main():
    rows = [(scene, q) for scene, _g, group in SCENES for q, _ in group]
    flagged = [(s, q, b) for s, q in rows for b in [check(q)] if b]
    print("问题 %d 条，处境 %d 个" % (len(rows), len(SCENES)))
    if flagged:
        pct = 100.0 * len(flagged) / len(rows)
        print("不合格 %d 条（%.0f%%）：" % (len(flagged), pct))
        for s, q, b in flagged[:40]:
            print("  [%s] %s  ← %s" % (s, q, "/".join(b)))
        if len(flagged) > 40:
            print("  …… 另有 %d 条" % (len(flagged) - 40))
        sys.exit(1)
    print("全部符合内容标准 ✅")


if __name__ == "__main__":
    main()
