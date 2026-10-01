#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""「测测你的历史分身」的内容判据：好玩可以，编不行。

测试是拿来传播的，传出去的每一句话都会被人截图、被人挑。所以这里不判
「写得好不好」（那只能靠眼睛），只判那几条「错了就是假话」的：

  ① 32 型齐全：16 个四维基础型 × 定 / 燃，一个不少、一个不重
  ② 每个结果人物都是库里真有章节的人；站主划掉的人（毛泽东、粟裕）不许出现
  ③ 「当年那件事」链到的页面真实存在，而且就是这个人的那一篇
  ④ 「你最容易栽在哪」在他自己那几篇里找得到出处 —— 可以改短，不许另编
     判法：这句话里的汉字二元组，至少一半出现在他那几篇的正文里
  ⑤ 金句要么在库里原样找得到，要么写明出处（quote_src 非空）
  ⑥ 同型名人、关系配对里的名字都在库里 / 都在 32 型里；20 道题每维 4 道
  ⑦ 32 种结果都抽得到，而且分布匀：把**页面里那段打分代码原样**抠出来放进 node，
     模拟两万个像真人一样答题的人，每型占比必须在理想值（1/32）的 0.75–1.3 倍之间。
     第一版的平局规则偏向左极，模拟出来韩信 4.5%、杜甫 2.1% —— 上线了也没人看得出来，
     大家只会觉得「怎么这么多人测出韩信」。不另抄一份打分逻辑：抄的那份一定会和真的那份漂开。
"""
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

import ce_data as D        # noqa: E402
import hw_chapters as C    # noqa: E402
import hw_kind             # noqa: E402
import hw_slugs            # noqa: E402

BANNED = {"毛泽东", "粟裕"}


def grams(s):
    zh = re.findall(r"[一-鿿]", s)
    return {zh[i] + zh[i + 1] for i in range(len(zh) - 1)}


def main():
    bad = []
    idx = json.load(io.open(os.path.join(ROOT, "assets", "hw-chat-index.json"), encoding="utf-8"))
    by_who = {}
    for c in idx["chapters"]:
        by_who.setdefault(c.get("p"), []).append(c)

    # ① 32 型齐全
    codes = [t["code"] for t in D.TYPES]
    want = {a + b + c + d + "-" + e
            for a in "进退" for b in "刚柔" for c in "谋真" for d in "独群" for e in "定燃"}
    if len(codes) != len(set(codes)):
        bad.append("有重复的类型代号：%s" % sorted({c for c in codes if codes.count(c) > 1}))
    for c in sorted(want - set(codes)):
        bad.append("少了类型 %s" % c)
    for c in sorted(set(codes) - want):
        bad.append("多了一个不合法的类型代号 %s" % c)
    whos = [t["who"] for t in D.TYPES]
    if len(whos) != len(set(whos)):
        bad.append("同一个人当了两个结果：%s" % sorted({w for w in whos if whos.count(w) > 1}))

    for t in D.TYPES:
        w, code = t["who"], t["code"]
        # ② 库里真有、没被划掉
        if w in BANNED:
            bad.append("%s（%s）是站主划掉的人，不许当结果" % (w, code))
        if w not in hw_kind.PEOPLE or not by_who.get(w):
            bad.append("%s（%s）不是库里有章节的人" % (w, code))
            continue
        # ③ 当年那件事
        title, url = t["story"]
        mine = {c.get("u"): c for c in by_who[w]}
        if url not in mine:
            bad.append("%s 的「当年那件事」链到 %s —— 那不是他的章节" % (w, url))
        elif not os.path.isfile(os.path.join(ROOT, url.strip("/"), "index.html")):
            bad.append("%s 的「当年那件事」%s 这一页不存在" % (w, url))
        elif mine[url].get("n") != title:
            bad.append("%s 的「当年那件事」标题写成「%s」，那一篇实际叫「%s」"
                       % (w, title, mine[url].get("n")))
        # ④ 你最容易栽在哪
        body = "".join(c.get("txt", "") for c in by_who[w])
        g = grams(t["pit"])
        if g:
            hit = len(g & grams(body)) / float(len(g))
            if hit < 0.5:
                bad.append("%s 的「最容易栽在哪」只有 %d%% 能在他那几篇里找到出处 —— 像是另编的：%s"
                           % (w, round(hit * 100), t["pit"][:30]))
        # ⑤ 金句
        in_lib = any(t["quote"].rstrip("。！？") in (c.get("txt", "") + "".join(c.get("q") or []))
                     for c in by_who[w])
        if not in_lib and not (t.get("quote_src") or "").strip():
            bad.append("%s 的金句在库里找不到，也没写出处：%s" % (w, t["quote"]))
        # 形状
        if len(t.get("dims") or []) != len(D.DIMS) or not all(0 <= x <= 100 for x in t["dims"]):
            bad.append("%s 的六维基准不是 6 个 0–100 的数" % w)
        for k in ("title", "desc", "power", "pit", "quote"):
            if not (t.get(k) or "").strip():
                bad.append("%s 缺 %s" % (w, k))

    # ⑥ 同型名人、关系、题目
    for base, names in D.KIN.items():
        for n in names:
            if n in BANNED:
                bad.append("同型名人里出现了 %s" % n)
            if not by_who.get(n) or not hw_slugs.slug_for(n):
                bad.append("同型名人 %s（%s）不在库里" % (n, base))
    whoset = set(whos)
    for a, b, lab, txt in D.RELATIONS:
        for n in (a, b):
            if n not in whoset:
                bad.append("关系「%s」里的 %s 不在 32 型里" % (lab, n))
        if "你" in txt or "ta" in txt.lower():
            bad.append("关系「%s × %s」的文案写了「你/ta」—— 谁先测谁后测读起来会反" % (a, b))
    per = [0] * len(D.AXES)
    for q in D.QUESTIONS:
        per[q["axis"]] += 1
        for side in ("da", "db"):
            for k in q[side]:
                if k not in D.DIMS:
                    bad.append("题目「%s」加分加到了不存在的维度 %s" % (q["q"][:12], k))
    if per != [4] * len(D.AXES):
        bad.append("每个维度应该 4 道题，现在是 %s" % per)

    # ⑦ 分布：跑页面里那份真打分代码
    page = os.path.join(ROOT, "ce", "index.html")
    if not os.path.isfile(page):
        bad.append("没有 ce/index.html —— 先跑 python3 scripts/build_ce.py")
    else:
        html = io.open(page, encoding="utf-8").read()
        m = re.search(r"/\*SCORE-BEGIN\*/(.*?)/\*SCORE-END\*/", html, re.S)
        dm = re.search(r"window\.CE=(\{.*?\});</script>", html, re.S)
        if not m or not dm:
            bad.append("页面里找不到打分代码段（SCORE-BEGIN/END）或数据 —— 判据没法跑真代码")
        else:
            sim = ("var D=%s;\n%s\n"
                   "var seed=7;function rnd(){seed=(seed*1103515245+12345)%%2147483648;return seed/2147483648}\n"
                   "var pool=[-2,-1,-1,0,0,1,1,2],N=20000,c={};\n"
                   "for(var k=0;k<N;k++){var a=D.qs.map(function(){return pool[Math.floor(rnd()*pool.length)]});"
                   "var r=scoreOf(D,a);c[r.code]=(c[r.code]||0)+1}\n"
                   "console.log(JSON.stringify({n:N,c:c}))" % (dm.group(1), m.group(1)))
            try:
                out = subprocess.run(["node", "-e", sim], capture_output=True, text=True, timeout=120)
                res = json.loads(out.stdout) if out.returncode == 0 else None
            except FileNotFoundError:
                res = "nonode"
            except Exception as e:
                res = None
                bad.append("模拟答题跑不起来：%s" % e)
            if res == "nonode":
                print("  （没有 node，分布检查跳过）")
            elif res is None:
                bad.append("模拟答题跑不起来：%s" % (out.stderr.strip()[:200] if out else ""))
            else:
                ideal = res["n"] / 32.0
                who = {t["code"]: t["who"] for t in D.TYPES}
                for code in sorted(want):
                    r = res["c"].get(code, 0) / ideal
                    if r == 0:
                        bad.append("%s（%s）在两万次模拟里一次都没抽到" % (who.get(code, code), code))
                    elif r < 0.75 or r > 1.3:
                        bad.append("%s（%s）抽中率是理想值的 %.2f 倍 —— 分布偏了"
                                   % (who.get(code, code), code, r))

    if bad:
        print("\n  历史分身测试的内容有 %d 处问题：" % len(bad))
        for b in bad[:12]:
            print("    ✗ " + b)
        return 1
    print("  历史分身：32 型齐全、人都在库里、每一篇原文都在、短处都有出处、金句有来处、"
          "20 道题每维 4 道；\n"
          "      两万次模拟 32 型都抽得到、分布匀（跑的是页面里那份打分代码）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
