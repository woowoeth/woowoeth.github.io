# -*- coding: utf-8 -*-
"""英文条目的**批次包**。每个批次一个文件，互不相干。

为什么要有这一层：把 159 个人补齐是并行的活，而条目记录、处境问句、
今日一句、一句介绍原来分别住在四个共享文件里 —— 几个人同时往同一个文件
中间插东西，一定打架，而且冲突解出来的东西谁都没读过。

改成：**每批只写自己那一个文件**（外加自己那几个 chapters_en/<slug>.py），
共享文件只保留一次性的「把所有批次拼进来」那几行。

一个批次文件长这样（四个名字都可以缺，缺的当空）：

    ENTRIES = [ {...}, ... ]        # 条目记录，形状同 en_entries.ENTRIES
    INTROS  = { "slug": "一句话介绍" }
    SCENES  = [ ("处境名", "分组", [ ("问句", [("slug","章key")]), ... ]) ]
    ASKS    = { "slug/章key": "今日一句（必须与上面某条问句逐字相同）" }
    SC_BOX  = { "处境名": "预填句" }     # 只有**新开**处境才需要
    SC_SHORT= { "处境名": "短名" }       # 只有名字过长的处境才需要

SCENES 里如果处境名和已有的重复，拼装时会**并进那个已有处境**，
不会生出两个同名的 —— 多数新章节应该挂在已有处境下，而不是自己新开一个。
"""
import importlib
import os
import pkgutil

_HERE = os.path.dirname(os.path.abspath(__file__))


BROKEN = {}


def _mods():
    """能导入的批次。导不进来的记在 BROKEN 里，**不中断**。

    为什么要容忍：补齐 159 条是十几个人同时在写，各写各的 bNN.py。
    严格模式下，任何一个人写到一半（文件存了、语法还不全）都会让**其他
    所有人**的自检当场崩掉，而错误信息指向的是别人的文件 —— 谁都不知道
    自己该改什么。

    容忍不等于放过：scripts/check_en.py（真门禁）会因为 BROKEN 非空而
    整体失败。快的那一道往前走，慢的那一道守住底线。
    """
    BROKEN.clear()
    for m in sorted(x.name for x in pkgutil.iter_modules([_HERE])):
        if not m.startswith("b"):
            continue
        try:
            yield importlib.import_module("%s.%s" % (__name__, m))
        except Exception as e:                       # noqa: BLE001
            BROKEN[m] = "%s: %s" % (type(e).__name__, e)


def broken():
    list(_mods())
    return dict(BROKEN)


def collect(name, empty):
    """把所有批次里的 name 合起来。list 相加，dict 相并。"""
    out = type(empty)(empty)
    for m in _mods():
        v = getattr(m, name, None)
        if not v:
            continue
        if isinstance(out, list):
            out += list(v)
        else:
            out.update(v)
    return out


def merge_scenes(base):
    """把批次里的 SCENES 并进 base：同名处境合并问句，新处境追加在末尾。

    不合并的话会出现两个「Too many paths」，chip 条上并排站着两个一样的名字，
    点哪个都只看到一半 —— 而每个批次单独看都是对的。
    """
    idx = {t: i for i, (t, _g, _q) in enumerate(base)}
    out = [(t, g, list(q)) for t, g, q in base]
    for m in _mods():
        for t, g, qs in getattr(m, "SCENES", []) or []:
            if t in idx:
                have = {q for q, _ in out[idx[t]][2]}
                out[idx[t]][2].extend([x for x in qs if x[0] not in have])
            else:
                idx[t] = len(out)
                out.append((t, g, list(qs)))
    return [(t, g, q) for t, g, q in out]


def slugs():
    return [e["slug"] for e in collect("ENTRIES", [])]


def conflicts(base_scenes=(), base_names=(), base_slugs=()):
    """跨批次的冲突 —— **只有把所有批次摆在一起才看得见**的那一类。

    每一批单独看都是对的：slug 不重、名字不重、处境名不重。合起来就未必。
    check_batch.py 是给写手用的，它只看自己那一批，看不见这些；
    所以这一条只能长在这里，由 check_en.py 调。

    查四样：
    ① 同一个 slug 被两批都写了 —— 后导入的那批静默覆盖前一批。
    ② 同一个英文名被两个 slug 用了 —— 交叉引用会指错人。
    ③ 处境名「几乎一样」—— 「Too many paths」和「Too many options」
       会在 chip 条上并排站着，读者以为是两个地方，其实内容被劈成两半。
    ④ 同一个 slug/章key 有两句今日一句 —— 后写的赢，前一批的白写。
    """
    import re
    out = []
    seen_slug, seen_name, seen_ask = {}, {}, {}
    for s in base_slugs:
        seen_slug[s] = "已上线"
    for n in base_names:
        seen_name[n] = "已上线"
    scenes = {t: "已上线" for t in base_scenes}

    def norm(t):
        return re.sub(r"[^a-z]", "", t.lower())

    nscene = {norm(t): t for t in scenes}
    for m in _mods():
        who = m.__name__.rsplit(".", 1)[-1]
        for e in getattr(m, "ENTRIES", []) or []:
            sl, nm = e.get("slug"), e.get("n")
            if sl in seen_slug:
                out.append("slug %s 在 %s 和 %s 里各有一条，后一条会静默覆盖"
                           % (sl, seen_slug[sl], who))
            seen_slug[sl] = who
            if nm in seen_name and seen_name[nm] != who:
                out.append("英文名「%s」被两处用了（%s / %s）—— 交叉引用会指错人"
                           % (nm, seen_name[nm], who))
            seen_name[nm] = who
        for t, _g, _q in getattr(m, "SCENES", []) or []:
            k = norm(t)
            if k in nscene and nscene[k] != t:
                out.append("处境名几乎一样：「%s」和「%s」—— chip 条上会并排"
                           " 站着两个，内容被劈成两半" % (nscene[k], t))
            nscene.setdefault(k, t)
        for key in getattr(m, "ASKS", {}) or {}:
            if key in seen_ask and seen_ask[key] != who:
                out.append("%s 的今日一句在 %s 和 %s 里各写了一句，后一句赢"
                           % (key, seen_ask[key], who))
            seen_ask[key] = who
    return out
