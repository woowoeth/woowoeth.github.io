#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""站内门禁总入口。

    python3 scripts/gate.py          七道闸（秒级）
    python3 scripts/gate.py --full   再加门禁自检：给每道闸注入它本该抓到的缺陷，看它拦不拦

为什么要有这个文件：七道闸原来散在 HANDOVER.md 的第 249-254 行，靠人照着抄命令。
散着的后果不是漏跑一两道，是**没人知道它们是不是还活着** —— 视频侧刚出过一次：
`series.py` 的「已推锁定」拿 `git show HEAD:...` 当真源，而那个文件根本没进 git，
取到空串就静默跳过，不报错、不打印、不拦，二十几篇的锁空了几个月没人发现。
这个仓里同样的病也有过记录：`check_pullquotes.py` 的文件头自己写着
「脚本末尾根本没有 sys.exit，无论抓到多少都返回 0，等于一直空转」。

所以 --full 那一档不是锦上添花，它是唯一能回答「这些闸还活着吗」的东西。
"""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# (名字, 脚本带参数, 说明)
CHECKS = [
    ("章节形制", "check_chapters.py", "长度/分则/三问/红字用量"),
    ("问题内容", "check_questions.py", "第一人称、不抽象、不查资料语气"),
    ("处境覆盖", "check_coverage.py", "新章节有没有挂上问题"),
    ("站点完整", "check_integrity.py", "链接/图/二维码"),
    ("同页重复", "check_repetition.py", "同一页里重复的可见文本块"),
    ("就地加重", "check_pullquotes.py", "同页重复加重 + 旧式 blockquote 残留"),
    ("金句重叠", "check_quote_overlap.py . 10", "文末金句不得与正文大段重合"),
    ("教训去向", "wikigate.py", "FAILURES.md 里每条教训必须写明变成了哪道闸"),
    ("繁体站", "check_tw.py", "结构一一对应 / 链接一致 / 无漏转 / 歧义字已登记"),
    ("语言站链接", "check_links.py", "每条地址落到真实页面 / 姊妹站指对语言版本 / 语言层无遗漏"),
    ("英文站", "check_en.py", "引用/长度/无中文残留（含渲染后）"),
    ("英文内联脚本", "check_en_js.py", "盲替换有没有把 JS 字符串截断"),
]


def run(cmd, cwd=ROOT):
    r = subprocess.run([sys.executable, os.path.join(HERE, *cmd.split()[:1])]
                       + cmd.split()[1:], cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    full = "--full" in sys.argv
    bad, t0 = [], time.time()
    for name, cmd, note in CHECKS:
        t = time.time()
        rc, out = run(cmd)
        tail = [l for l in out.strip().split("\n") if l.strip()]
        line = tail[-1][:60] if tail else ""
        print("  %s %-10s %5.1fs  %s" % ("✓" if rc == 0 else "✗", name, time.time() - t, line))
        if rc != 0:
            bad.append((name, out))

    if full:
        t = time.time()
        rc, out = run("gate_selftest.py")
        print("  %s %-10s %5.1fs" % ("✓" if rc == 0 else "✗", "门禁自检", time.time() - t))
        if rc != 0:
            bad.append(("门禁自检", out))

    print("\n  共 %.1fs%s" % (time.time() - t0, "" if full else "（提交前跑 --full）"))
    if bad:
        for name, out in bad:
            print("\n—— %s 不合格 ——" % name)
            for l in out.strip().split("\n")[-24:]:
                print("   " + l)
        return 1
    print("✓ 站内门禁通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
