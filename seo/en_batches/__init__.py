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


def _mods():
    for m in sorted(x.name for x in pkgutil.iter_modules([_HERE])):
        if m.startswith("b"):
            yield importlib.import_module("%s.%s" % (__name__, m))


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
