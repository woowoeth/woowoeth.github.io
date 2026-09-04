#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reverse-verify scripts/check_en.py.

A gate that has only ever printed "ok" has proved nothing. For each rule this
injects one defect of exactly the kind that rule exists for, and requires the
gate to exit 1 **and** say the expected thing. A rule with no injection here
is a rule nobody has watched fail.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, "hwx_scenes_en.py")
CHAP = os.path.join(ROOT, "seo", "chapters_en", "curie.py")
QA = os.path.join(HERE, "quote_asks_en.py")
GATE = os.path.join(HERE, "check_en.py")

# (名字, 替换函数, 期望字样[, 改哪个文件])
# 默认改 hwx_scenes_en.py；带第四项的改 check_en.py 自己。
CASES = [
    ("① ref 打错字",
     lambda s: s.replace('("su-shi", "east-slope")', '("su-shi", "east-slop")', 1),
     "does not exist"),
    ("② ref 指向名单外的条目",
     lambda s: s.replace('("su-shi", "east-slope")', '("epictetus", "dichotomy")', 1),
     "not in the pilot set"),
    ("③ 有一行忘了译",
     lambda s: s.replace('"The income stopped. What do I do first?"',
                         '"\\u6536\\u5165\\u65ad\\u4e86\\uff0c\\u6211\\u5148\\u8be5\\u5e72\\u4ec0\\u4e48\\u3002"', 1),
     "still Chinese"),
    ("④ 两句译成了同一句",
     lambda s: s.replace('"I know what to do. I\'m not doing it."',
                         '"I understand it completely and still don\'t move."', 1),
     "duplicate question"),
    ("⑤ 处境名过长",
     lambda s: s.replace('("Starting over", "A turn in the road"',
                         '("Starting over again from nothing at all in the middle of everything", '
                         '"A turn in the road"', 1),
     "situation too long"),
    ("⑤b 处境名带尾标点",
     lambda s: s.replace('("Starting over", "A turn in the road"',
                         '("Starting over?", "A turn in the road"', 1),
     "should not end in punctuation"),
    ("⑥ 某一章没人指得到",
     lambda s: s.replace('("boyd", "ooda")', '("boyd", "to-be-or-to-do")'),
     "nothing points at chapter boyd/ooda"),
    ("⑥b 某个条目整个没人指得到",
     lambda s: s.replace('("montessori", "prepared-environment")', '("montessori", "help-me-do-it-myself")')
                .replace('("montessori", "help-me-do-it-myself"), ("montessori", "help-me-do-it-myself")',
                         '("montessori", "help-me-do-it-myself")'),
     "nothing points at chapter montessori/prepared-environment"),
    ("④b 同一分组下两个同名处境",
     lambda s: s.replace('("Starting over", "A turn in the road"',
                         '("I lost my job", "A turn in the road"', 1),
     "duplicate situation"),
    # PILOT 名单是手抄的，抄错 slug 的事今天就发生过三次（han-fei / gordon /
    # ratey 都不是真名）。这一条守的正是那个错：名单里的 slug 若压根没有章节，
    # 「每一章都要有人指」那条看不见它 —— 它没有章。
    ("⑥c PILOT 名单里抄错了 slug",
     lambda s: s.replace("dweck john-ratey", "dweck john-radey"),
     "nothing points at entry john-radey", "gate"),
    # ⑦ 今日一句：值必须逐字等于处境层原句，且那句真的引用了这一章。
    ("⑦ 今日一句的值差了个标点",
     lambda s: s.replace('"su-shi/no-wind-no-rain": "It hit me and I can\'t cool down."',
                         '"su-shi/no-wind-no-rain": "It hit me and I can\'t cool down"'),
     "punctuation differs", "qa"),
    ("⑦b 值是原句，但指的是别的章",
     lambda s: s.replace('"su-shi/no-wind-no-rain": "It hit me and I can\'t cool down."',
                         '"su-shi/no-wind-no-rain": "The income stopped. What do I do first?"'),
     "is not a question that points at it", "qa"),
    ("⑦c 有一章漏配了今日一句",
     lambda s: s.replace('    "boyd/ooda": "I\'m only ever reacting. I never set the tempo.",\n', ""),
     "no today's line for chapter boyd/ooda", "qa"),
    # ⑧⑨ 章节自身：长度闸和字段完整性。这两条是后加的，一度没有注入 ——
    # 而一道没人看着它失败过的闸，等于没有。
    ("⑧ dek 太短",
     lambda s: s.replace('"dek": "The person who mattered most is suddenly gone and the days "',
                         '"dek": "Too short." + (""', 1)
                .replace('"still have to continue. What she did seven months later.",',
                         '"still have to continue."),', 1),
     "dek is", "chap"),
    ("⑧b 金句超长",
     lambda s: s.replace('"It doesn\'t solve the grief. It gives the day a shape.",',
                         '"It does not solve the grief but it does give the day a shape '
                         'that you can put yourself inside of somehow.",', 1),
     "line to keep is", "chap"),
    ("⑨ story 少了强调段",
     lambda s: s.replace('"his chair to his widow. ==On 5 November she gave her first "',
                         '"his chair to his widow. On 5 November she gave her first "', 1)
                .replace('"lecture==, with the room overflowing', '"lecture, with the room overflowing', 1),
     "exactly one ==...== span", "chap"),
    ("⑨b 分则整个丢了",
     lambda s: s.replace('        "f": [\n            {"n": "Catch hold of one specific thing that must be done",',
                         '        "f_gone": [\n            {"n": "Catch hold of one specific thing that must be done",', 1),
     "needs at least 2", "chap"),
    ("問句没有挂任何章节",
     lambda s: s.replace('("It hit me and I can\'t cool down.",\n     [("su-shi", "no-wind-no-rain")]),',
                         '("It hit me and I can\'t cool down.",\n     []),', 1),
     "question with no chapter"),
]


def run(tmp):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, os.path.join(tmp, "scripts", "check_en.py")],
                       capture_output=True, text=True, env=env)
    return p.returncode, p.stdout + p.stderr


def main():
    orig = open(SRC, encoding="utf-8").read()
    bad = []

    tmp = tempfile.mkdtemp(prefix="en-selftest-")
    for d in ("scripts", "seo"):
        shutil.copytree(os.path.join(ROOT, d), os.path.join(tmp, d),
                        ignore=shutil.ignore_patterns("__pycache__"))

    # 先证明干净的树是过的 —— 否则下面每一条都会「通过」而毫无意义
    rc, out = run(tmp)
    if rc != 0:
        print("干净的树就没过，后面的注入全都说明不了问题：\n" + out)
        return 1

    origs = {"scenes": orig, "gate": open(GATE, encoding="utf-8").read()}
    origs["qa"] = open(QA, encoding="utf-8").read()
    origs["chap"] = open(CHAP, encoding="utf-8").read()
    paths = {"scenes": os.path.join(tmp, "scripts", "hwx_scenes_en.py"),
             "gate": os.path.join(tmp, "scripts", "check_en.py"),
             "qa": os.path.join(tmp, "scripts", "quote_asks_en.py"),
             "chap": os.path.join(tmp, "seo", "chapters_en", "curie.py")}
    for case in CASES:
        name, mutate, want = case[:3]
        which = case[3] if len(case) > 3 else "scenes"
        s = mutate(origs[which])
        if s == origs[which]:
            bad.append("%s —— 注入没生效（源码里没找到要改的那段）" % name)
            continue
        open(paths[which], "w", encoding="utf-8").write(s)
        # .pyc 会把上一个用例的注入喂给这一次：多数注入只改几个字节，
        # mtime 秒数和文件大小都可能不变，Python 就直接用缓存了。
        for dp, dn, fn in os.walk(tmp):
            if os.path.basename(dp) == "__pycache__":
                shutil.rmtree(dp, ignore_errors=True)
        rc, out = run(tmp)
        open(paths[which], "w", encoding="utf-8").write(origs[which])   # 复原，免得叠加
        if rc == 0:
            bad.append("%s —— 闸门放行了" % name)
        elif want not in out:
            bad.append("%s —— 拦是拦了，但理由不对（没看到 %r）\n      %s"
                       % (name, want, out.strip().splitlines()[-1][:100]))
        else:
            print("  ✓ %s → 拦住，理由对" % name)
    shutil.rmtree(tmp, ignore_errors=True)

    if bad:
        print("\n自检不合格：")
        for b in bad:
            print("  ✗ " + b)
        return 1
    print("\n✓ %d 条注入全部被拦下，且报的理由都对得上" % len(CASES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
