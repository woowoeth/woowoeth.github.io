#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""单个批次的快速自检 —— 不开浏览器、不起服务、不跑构建。

    python3 scripts/check_batch.py b07

为什么要有它：完整的 scripts/check_en.py 要起三个 http 服务、渲染页面，
三十多秒，而且几个人同时跑会抢端口。补齐 159 个人是并行的活，每个人手里
需要一个几秒钟能跑完、只看自己这一批的判据。

它查的是 check_en.py 里**与浏览器无关**的那部分，判据和阈值直接从
check_en.py 读，不另抄一份 —— 抄一份的下场是两边慢慢漂移，本地绿、
门禁红，而且没人知道哪个才算数。
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

import check_en as C  # noqa: E402


def words(x):
    return len((x or "").split())


def hwx_scenes_all():
    """合并之后的全部处境（已有 84 个 + 所有批次）。"""
    import hwx_scenes_en
    return hwx_scenes_en.SCENES


def zh_path(slug):
    """中文原文的文件路径 —— 按 **PARENT.slug** 找，不按文件名猜。

    文件名多数等于 slug（`-` 换 `_`），但有六个不是：hot-metal.py 用连字符、
    strategies_warring_states.py 是简写。假设文件名等于 slug 的下场是
    报「在 seo/chapters/ 下没有中文原文」，而写手为了让校验器闭嘴，
    会去**改中文源文件的名字** —— 有人已经这么干了两次。
    判据落在文件里写的 slug 上，猜不出来的事就别猜。
    """
    d = os.path.join(ROOT, "seo", "chapters")
    guess = os.path.join(d, slug.replace("-", "_") + ".py")
    if os.path.exists(guess):
        return guess
    for f in sorted(os.listdir(d)):
        if not f.endswith(".py") or f.startswith("_"):
            continue
        try:
            m = load(os.path.join(d, f), "zhscan_" + f[:-3])
        except Exception:                                    # noqa: BLE001
            continue
        if (getattr(m, "PARENT", {}) or {}).get("slug") == slug:
            return os.path.join(d, f)
    return None


def load(path, name):
    """按**文件路径**加载。

    中文章节在 seo/chapters/<x>.py，英文在 seo/chapters_en/<x>.py ——
    模块名一模一样。两个目录都进 sys.path 的话，import 拿到的是先进路径的
    那一个，而两边字段名也一样，于是校验器会拿中文去校验中文，全绿。
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location("_b_" + name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(name):
    mod = importlib.import_module("en_batches.%s" % name)
    entries = getattr(mod, "ENTRIES", [])
    scenes = getattr(mod, "SCENES", [])
    asks = getattr(mod, "ASKS", {})
    intros = getattr(mod, "INTROS", {})
    bad = []

    # 可以被 l / contrast 引用的全集 = 已经上线的 + 名字契约里定好的。
    # 契约里的人可能还没写完（并行的其它批次在写），但名字是定死的，
    # 所以现在就可以引用 —— 这正是那张表存在的理由。
    import en_entries
    from en_names import NAMES
    known = {e["n"] for e in en_entries.ENTRIES} | {v[0] for v in NAMES.values()}

    # 每个处境都要有预填句。判据直接落在 SC_BOX 上，不去比「这个处境是不是
    # 新的」—— 批次里的处境在导入时已经被并进 hwx_scenes_en.SCENES 了，
    # 拿它当「已有」来判，新处境永远显示成已有，这条分支是死的。
    import hwx_en
    sc_box = dict(hwx_en.SC_BOX)
    sc_box.update(getattr(mod, "SC_BOX", {}))

    q_of = {}
    for t, g, qs in scenes:
        if t not in sc_box:
            bad.append("新处境「%s」没有 SC_BOX 预填句" % t)
        if len(t) > C.MAX_SCENE:
            bad.append("处境名太长（%d > %d）：%s" % (len(t), C.MAX_SCENE, t))
        for q, refs in qs:
            for slug, k in refs:
                q_of.setdefault("%s/%s" % (slug, k), []).append(q)

    for e in entries:
        w = "条目 %s" % e.get("slug", "?")
        for f in ("c", "n", "slug", "e", "w", "y", "d", "story", "f", "apply", "q"):
            if not e.get(f):
                bad.append("%s 缺 %s" % (w, f))
        if "==" in repr(e):
            bad.append("%s 用了 ==强调==，条目页不渲染它，会露出两个等号" % w)
        for n in list(e.get("l", [])) + [x["n"] for x in e.get("contrast", [])]:
            if n not in known:
                bad.append("%s 引用了「%s」，英文站没有这个人的页" % (w, n))
        want = NAMES.get(e.get("slug"))
        if want is None:
            bad.append("%s 不在 seo/en_names.py 的名单里 —— slug 写错了？" % w)
        else:
            if e.get("n") != want[0]:
                bad.append("%s 的名字是 %r，契约里是 %r（名字是接口，"
                           "别的批次会照契约引用你）" % (w, e.get("n"), want[0]))
            if e.get("c") != want[1]:
                bad.append("%s 的分类是 %r，契约里是 %r" % (w, e.get("c"), want[1]))
        if e["slug"] not in intros:
            bad.append("%s 没有一句话介绍（INTROS）" % w)

    for e in entries:
        py = e["slug"].replace("-", "_")
        p_en = os.path.join(ROOT, "seo", "chapters_en", py + ".py")
        p_zh = zh_path(e["slug"])
        if not os.path.exists(p_en):
            bad.append("%s 没有 seo/chapters_en/%s.py" % (e["slug"], py))
            continue
        m_en = load(p_en, py + "_en")
        keys_en = [c["k"] for c in m_en.CHAPTERS]
        # 章节 key 必须和中文那边一样：门禁拿中文当「这一版的计划」，
        # key 对不上的英文章会被报成「写了但不在计划里」。
        if p_zh:
            keys_zh = [c["k"] for c in load(p_zh, py + "_zh").CHAPTERS]
            extra = [k for k in keys_en if k not in keys_zh]
            missing = [k for k in keys_zh if k not in keys_en]
            if extra:
                bad.append("%s 的章 key 中文那边没有：%s（中文是 %s）"
                           % (e["slug"], extra, keys_zh))
            if missing:
                bad.append("%s 还缺这些章：%s" % (e["slug"], missing))
        else:
            bad.append("%s 在 seo/chapters/ 下没有中文原文，确认人选对不对"
                       % e["slug"])
        for c in m_en.CHAPTERS:
            where = "%s/%s" % (e["slug"], c["k"])
            for f in ("n", "w", "src", "dek", "story", "apply"):
                if not (c.get(f) or "").strip():
                    bad.append("%s 缺 %s" % (where, f))
            if (c.get("story") or "").count("==") != 2:
                bad.append("%s 的 story 需要正好一处 ==强调==" % where)
            if len(c.get("f") or []) < 2:
                bad.append("%s 只有 %d 段，至少 2 段" % (where, len(c.get("f") or [])))
            if len(c.get("q") or []) < 2:
                bad.append("%s 只有 %d 句金句，至少 2 句" % (where, len(c.get("q") or [])))
            for f, key in (("dek", "dek"), ("story", "story")):
                lo, hi = C.LEN[key]
                n = words(c.get(f))
                if not lo <= n <= hi:
                    bad.append("%s：%s 是 %d 词（要 %d-%d）" % (where, f, n, lo, hi))
            for i, part in enumerate(c.get("f") or [], 1):
                for key in ("d", "eg"):
                    lo, hi = C.LEN["part" if key == "d" else "eg"]
                    n = words(part.get(key))
                    if not lo <= n <= hi:
                        bad.append("%s：第 %d 段 %s 是 %d 词（要 %d-%d）"
                                   % (where, i, key, n, lo, hi))
            for q in c.get("q") or []:
                if words(q) > C.LEN["quote"][1]:
                    bad.append("%s：金句 %d 词（最多 %d）：%s"
                               % (where, words(q), C.LEN["quote"][1], q))
            if where not in q_of:
                bad.append("%s 没有指向它的处境问句" % where)
            elif where not in asks:
                bad.append("%s 没有今日一句（ASKS）" % where)
            elif asks[where] not in q_of[where]:
                bad.append("%s 的今日一句和处境问句对不上（必须逐字相同）：%r"
                           % (where, asks[where]))
        # PARENT 的 items 要覆盖所有章
        items = {i["k"] for i in getattr(m_en, "PARENT", {}).get("items", [])}
        for k in keys_en:
            if k not in items:
                bad.append("%s：PARENT.items 里没有 %s" % (e["slug"], k))

    from en_batches import broken as _broken
    others = {k: v for k, v in _broken().items() if k != name}
    if others:
        print("（别的批次现在导不进来，不是你的问题，先不用管：%s）"
              % "、".join(sorted(others)))
    # 预填句不许复读卡片上的问句 —— 这是 hwx_en.py 里的一条**硬断言**，
    # 撞上了整站构建直接抛异常。而它必须在**合并之后**的全集上算：
    # 你的预填句可能和别人批次里的问句撞，也可能和已有 84 个处境里的撞。
    # 判据照抄 hwx_en 的口径：四个词的片段，出现在三个以上处境的算英语
    # 绕不开的连接语、不算回声。
    try:
        import hwx_en as _H

        def _g4(t, n=4):
            w = (t or "").split()
            return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}

        all_sc = {t: [] for t in sc_box}
        for t, _g, qs in hwx_scenes_all():
            all_sc.setdefault(t, []).extend(q for q, _r in qs)
        df = {}
        for t, qs in all_sc.items():
            seen = _g4(sc_box.get(t, ""))
            for q in qs:
                seen |= _g4(q)
            for gm in seen:
                df[gm] = df.get(gm, 0) + 1
        mine = {t for t, _g, _q in scenes}
        for t, qs in all_sc.items():
            if t not in mine and t not in getattr(mod, "SC_BOX", {}):
                continue
            for q in qs:
                hit = sorted(g for g in _g4(q) & _g4(sc_box.get(t, ""))
                             if df.get(g, 0) < 3)
                if hit:
                    bad.append("处境「%s」的预填句在复读问句 %r —— 重的片段：%s"
                               "（构建时是硬断言，会直接抛异常）" % (t, q, hit))
    except Exception as _e:                                  # noqa: BLE001
        print("（预填句复读检查跑不起来：%s）" % _e)

    print("批次 %s：%d 个条目 · %d 个处境 · %d 句今日一句"
          % (name, len(entries), len(scenes), len(asks)))
    if bad:
        print("\n不合格：")
        for b in bad[:60]:
            print("  ✗ " + b)
        if len(bad) > 60:
            print("  … 还有 %d 条" % (len(bad) - 60))
        return 1
    print("✓ 这一批自检通过（完整门禁还要跑 scripts/check_en.py）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "b01"))
