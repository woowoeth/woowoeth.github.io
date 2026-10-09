#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 ce/index.html ——「测测你的历史分身」。

    python3 scripts/build_ce.py

内容全在 seo/ce_data.py，这里只管排版和交互；改内容别改这里。
页面是纯前端的：答题、打分、出结果、出分享卡、算两个人的关系，都在浏览器里，
不收任何数据。计数走站上现成的 GA（window.gtag 在才发）。

这一页也走全站的构建链（scripts/build_all.py 里「历史分身」那一步），之后的挂件、
语言层、PWA、资源版本号会照样加上；繁体版 tw/ce/ 由 build_tw 自动转出来。

三个入口参数：
  ?f=<n>  朋友分享来的：他测出第 n 型，你测完显示你们俩在历史上是什么关系
  ?r=<n>  直接看第 n 型的介绍（「64 型全览」里点进来的就是这个）
  #types  32 型全览
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "seo"))

import ce_data as D   # noqa: E402
import hw_slugs       # noqa: E402

OUT = os.path.join(ROOT, "ce", "index.html")


def questions():
    """出题顺序：五维交错（每维第 1 道、再每维第 2 道……），不让同一维的四道题挨着 ——
    挨着出，答到第二道就看得出「这几道在问同一件事」。对调的题标 flip（见 ce_data.FLIP）。"""
    by_axis = [[q for q in D.QUESTIONS if q["axis"] == a] for a in range(len(D.AXES))]
    out = []
    for i in range(4):
        for a in range(len(D.AXES)):
            q = dict(by_axis[a][i])
            q["flip"] = 1 if i in D.FLIP[a] else 0
            out.append(q)
    return out


def partner(t, kind):
    """拍档（ally）/ 宿敌（rival）：有史实就用史实（RELATIONS 里排在前面的那条），
    没有就按五维推：拍档只差「独 / 群」一维、温度相反 —— 你扛不动的他找得来人，一个稳住
    一个点火；宿敌四维全反、温度相反。推出来的会标「按五维推算」，不冒充史实。"""
    idx = {x["who"]: i for i, x in enumerate(D.TYPES)}
    for a, b, lab, txt, k in D.RELATIONS:
        if k == kind and t["who"] in (a, b):
            other = b if a == t["who"] else a
            return {"i": idx[other], "l": lab, "t": txt, "real": 1}
    AX = D.AXES
    base, temp = t["code"].split("-")
    other_temp = "燃" if temp == "定" else "定"
    nbase = len(AX) - 1                      # 不算最后那一维（定/燃）
    if kind == "ally":
        # 64 型：拍档在「独/群」「显/藏」上都互补 —— 一个扛、一个聚人，一个台前、一个幕后
        nb = base[:3] + ("群" if base[3] == "独" else "独") + ("藏" if base[4] == "显" else "显")
    else:
        nb = "".join(AX[i][1] if base[i] == AX[i][0] else AX[i][0] for i in range(nbase))
    code = nb + "-" + other_temp
    o = [x for x in D.TYPES if x["code"] == code][0]
    p = "她" if o["who"] in D.FEMALE else "他"
    if kind == "ally":
        a1 = ("你习惯独自扛事，%s擅长聚人成事" % p if base[3] == "独"
              else "你擅长聚人成事，%s习惯独自扛事" % p)
        a2 = ("你站在台前，%s藏在幕后" % p if base[4] == "显" else "你藏在幕后，%s站在台前" % p)
        a3 = ("你心定，%s心里有火" % p if temp == "定" else "你心里有火，%s心定" % p)
        txt = "%s；%s；%s——你缺的那一块，正好是%s的长处。" % (a1, a2, a3, p)
        lab = "最佳拍档"
    else:
        def d(i, pole):
            return AX[i][2] if pole == AX[i][0] else AX[i][3]
        txt = "你%s，%s%s；你%s，%s%s——五个维度全反：要么是最强的对手，要么是最好的搭档。" % (
            d(0, base[0]), p, d(0, nb[0]), d(1, base[1]), p, d(1, nb[1]))
        lab = "宿命对手"
    return {"i": D.TYPES.index(o), "l": lab, "t": txt, "real": 0}


def payload():
    fam = {a + c: v for (a, c), v in D.FAMILIES.items()}
    types = []
    for t in D.TYPES:
        x = dict(t)
        x["slug"] = hw_slugs.slug_for(t["who"])
        x["story"] = {"t": t["story"][0], "u": t["story"][1]}
        x["moments"] = D.MOMENTS[t["who"]]
        x["she"] = 1 if t["who"] in D.FEMALE else 0
        x["ally"] = partner(t, "ally")
        x["rival"] = partner(t, "rival")
        types.append(x)
    kin = {k: [{"n": n, "u": "/i/%s/" % hw_slugs.slug_for(n)} for n in v]
           for k, v in D.KIN.items()}
    return {"axes": D.AXES, "dims": D.DIMS, "dimdesc": D.DIM_DESC, "fam": fam,
            "types": types, "kin": kin, "qs": questions(), "rel": D.RELATIONS,
            "reld": {str(k): v for k, v in D.REL_BY_DIST.items()}}


CSS = r"""
:root{--paper:#f5f1e8;--paper2:#eee8da;--card:#faf7f0;--ink:#1f1c17;--muted:#8a8377;--line:#d8d2c6;--acc:#a33b2e;--fam:#a33b2e}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#171410;--paper2:#201c15;--card:#1d1913;--ink:#eae3d4;--muted:#9a917f;--line:#3a342a;--acc:#c65f4f;color-scheme:dark}}
:root[data-theme=dark]{--paper:#171410;--paper2:#201c15;--card:#1d1913;--ink:#eae3d4;--muted:#9a917f;--line:#3a342a;--acc:#c65f4f;color-scheme:dark}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink)}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
.serif{font-family:"Noto Serif SC","Songti SC","STSong","SimSun",serif}
.wrap{max-width:520px;margin:0 auto;padding:22px 20px 64px}
a{color:inherit}
/* 顶栏带 mast-top：站上的语言 / 夜间工具条（scripts/hwx_lang.py）认这一行，排成它的最后一项。
   不带的话工具条退成浮在右上角，正好压住「32 型全览」（2026-10-08 跑完整条构建后实测）。
   它自带 margin-left:auto，会和「32 型全览」平分空白，这里压掉，间距交给 gap。 */
.top{display:flex;align-items:center;gap:12px;font-size:13px;color:var(--muted)}
.top #toTypes{margin-left:auto}
.top #hwx-tools.in-row{margin-left:0;align-self:center}
.top a{text-decoration:none}
.seal{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:5px;background:var(--acc);color:#fff;font-family:"Noto Serif SC","Songti SC",serif;font-size:16px;margin-right:8px}
.eyebrow{font-size:11px;letter-spacing:.32em;color:var(--fam);text-transform:uppercase;text-align:center;font-weight:600}
.btn{display:block;width:100%;border:1px solid var(--ink);background:var(--ink);color:var(--paper);border-radius:999px;padding:14px 18px;font-size:16px;font-family:inherit;cursor:pointer;text-align:center;text-decoration:none}
.btn.ghost{background:transparent;color:var(--ink)}
.btn+.btn{margin-top:10px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 18px}
.card+.card{margin-top:14px}
.sec{margin-top:18px}
.lab{font-size:12px;letter-spacing:.18em;color:var(--fam);font-weight:600;margin-bottom:12px;display:flex;align-items:center;gap:10px}
.lab:after{content:"";flex:1;height:1px;background:var(--line)}
.muted{color:var(--muted)}
/* 开始页 */
#start h1{font-size:34px;line-height:1.35;margin:34px 0 6px;letter-spacing:.02em}
#start .sub{font-size:15px;color:var(--muted);margin:0 0 22px}
#start .hook{font-size:17px;margin:0 0 26px}
.from{border:1px dashed var(--acc);border-radius:14px;padding:14px 16px;margin:0 0 20px;font-size:15px}
.from b{color:var(--acc)}
.peek{margin:0 0 26px}
.peek .pl{font-size:13.5px;color:var(--muted);margin:0 0 4px}
.peek ul{list-style:none;margin:0;padding:0}
.peek li{padding:12px 0;border-bottom:1px solid var(--line);font-size:16px;line-height:1.65;cursor:pointer}
.peek li em{display:none;font-style:normal;font-size:13px;color:var(--acc);margin-top:3px}
.peek li.on em{display:block}
.peek .re{border:0;background:transparent;color:var(--muted);font:inherit;font-size:13px;padding:10px 0 0;cursor:pointer}
.pairhook{font-size:14px;line-height:1.7;margin:20px 0 6px}
.guess{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0 4px}
.guess button{border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:12px;padding:11px 8px;font:inherit;font-size:16px;cursor:pointer}
.guess button.ok{border-color:var(--acc);color:var(--acc);font-weight:600}
.guess button.no{opacity:.45;text-decoration:line-through}
.guess button:disabled{cursor:default}
.gres{font-size:15px;line-height:1.7;margin:10px 0 0}
.echo{min-height:21px;font-size:13px;color:var(--muted);margin:2px 0 0}
.echo b{color:var(--acc);font-weight:600}
.echo i{font-style:normal;font-size:11.5px;opacity:.75;margin-left:6px}
.rarenote{font-size:12px;color:var(--muted);margin:8px 2px 0;line-height:1.6}
.moments .hit{display:inline-block;margin-left:8px;border:0;background:transparent;padding:0;font:inherit;font-size:12.5px;color:var(--muted);cursor:pointer;white-space:nowrap}
.moments li.on .hit{color:var(--fam);font-weight:600}
.moments + .hint{font-size:12.5px;color:var(--muted);margin:10px 0 0}
.tile.mine{border-width:2px}.tile .me{float:right;font-size:11px;color:#fff;background:var(--acc);border-radius:4px;padding:0 6px;line-height:18px}
/* 答题 */
#quiz{display:none}
.prog{height:4px;background:var(--line);border-radius:4px;overflow:hidden;margin:18px 0 6px}
.prog i{display:block;height:100%;background:var(--acc);width:0;transition:width .25s}
.pn{font-size:12px;color:var(--muted);display:flex;justify-content:space-between}
.qq{font-size:21px;line-height:1.6;margin:26px 0 22px;min-height:68px}
.opt{border:1px solid var(--line);border-radius:14px;padding:14px 16px;font-size:16px;background:var(--card)}
.opt small{display:block;font-size:11px;letter-spacing:.2em;color:var(--muted);margin-bottom:2px}
.dots{display:flex;justify-content:space-between;align-items:center;margin:16px 4px}
.dots button{border:2px solid var(--line);background:transparent;border-radius:50%;cursor:pointer;padding:0;transition:transform .12s,background .12s,border-color .12s}
.dots button:nth-child(1),.dots button:nth-child(5){width:46px;height:46px}
.dots button:nth-child(2),.dots button:nth-child(4){width:36px;height:36px}
.dots button:nth-child(3){width:26px;height:26px}
.dots button:nth-child(1),.dots button:nth-child(2){border-color:#3d5a6c}
.dots button:nth-child(4),.dots button:nth-child(5){border-color:var(--acc)}
.dots button.on:nth-child(1),.dots button.on:nth-child(2){background:#3d5a6c}
.dots button.on:nth-child(4),.dots button.on:nth-child(5){background:var(--acc)}
.dots button.on:nth-child(3){background:var(--muted);border-color:var(--muted)}
.dots button:active{transform:scale(.92)}
.dotlab{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin:-6px 0 14px}
.back{border:0;background:transparent;color:var(--muted);font-size:14px;margin-top:20px;cursor:pointer;padding:6px 0}
/* 结果 */
#result{display:none}
.hero{text-align:center;padding:26px 6px 6px}
.pill{display:inline-flex;align-items:center;gap:10px;border:1px solid var(--fam);border-radius:999px;padding:8px 18px;margin:16px 0 8px;font-size:14px;letter-spacing:.08em;color:var(--fam)}
.pill b{font-size:17px}
.name{font-size:62px;line-height:1.15;margin:14px 0 4px;letter-spacing:.06em}
.name.long{font-size:46px}
.rule{display:flex;align-items:center;justify-content:center;gap:12px;margin:2px 0 10px}
.rule i{width:54px;height:2px;background:var(--fam);opacity:.75}
.rule b{width:8px;height:8px;border-radius:50%;background:var(--fam)}
.title{font-size:22px;letter-spacing:.12em;margin:0}
.chips{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin:14px 0 4px}
.chip{font-size:13px;border-radius:999px;padding:4px 12px;border:1px solid var(--fam);color:var(--fam)}
.chip.solid{background:var(--fam);color:#fff;border-color:var(--fam)}
.quote{font-size:18px;font-style:italic;line-height:1.75;margin:22px 4px 4px;position:relative;padding:0 22px}
.quote:before,.quote:after{position:absolute;font-size:34px;color:var(--fam);opacity:.45;font-style:normal;line-height:1}
.quote:before{content:"“";left:0;top:-4px}.quote:after{content:"”";right:0;bottom:-14px}
.qsrc{font-size:12px;color:var(--muted);text-align:center;margin:6px 0 0}
.stats{display:grid;grid-template-columns:1fr 1.15fr 1fr;gap:10px;margin:24px 0 4px;align-items:center}
.stat{border:1px solid var(--line);background:var(--card);border-radius:14px;padding:14px 6px;text-align:center}
.stat b{display:block;font-size:26px;line-height:1.2;font-family:"Noto Serif SC","Songti SC",serif}
.stat span{display:block;font-size:13px;color:var(--muted);margin-top:2px}
.stat em{display:block;font-size:11px;font-style:normal;color:var(--muted);letter-spacing:.1em;margin-top:4px}
.stat.mid{background:var(--fam);border-color:var(--fam);color:#fff;padding:20px 6px}
.stat.mid b{font-size:32px}.stat.mid span,.stat.mid em{color:rgba(255,255,255,.88)}
.axis{margin:12px 0}
.axis .row{display:flex;justify-content:space-between;font-size:14px;margin-bottom:5px}
.axis .row b{color:var(--fam)}
.bar{height:10px;border-radius:10px;background:var(--paper2);position:relative;overflow:hidden;border:1px solid var(--line)}
.bar i{position:absolute;top:0;bottom:0;background:var(--fam);opacity:.85}
.radar{display:block;margin:0 auto;max-width:340px;width:100%}
.legend{display:flex;justify-content:center;gap:20px;font-size:13px;color:var(--muted);margin-top:6px}
.legend i{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.dim{display:flex;align-items:center;gap:12px;padding:9px 0}
.dim .rk{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;background:var(--paper2);color:var(--muted);flex:0 0 auto}
.dim.top .rk{background:var(--fam);color:#fff}
.dim .dn{width:44px;font-size:15px;flex:0 0 auto}
.dim .db{flex:1;height:8px;border-radius:8px;background:var(--paper2);overflow:hidden}
.dim .db i{display:block;height:100%;background:var(--fam);opacity:.55;border-radius:8px}
.dim.top .db i{opacity:.95}
.dim .dv{width:34px;text-align:right;font-size:17px;font-family:"Noto Serif SC","Songti SC",serif;flex:0 0 auto}
.dim.top .dv{color:var(--fam)}
.desc{font-size:17px;line-height:1.95}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.two .card+.card{margin-top:0}
.two h4{margin:0 0 6px;font-size:13px;color:var(--muted);font-weight:500;letter-spacing:.1em}
.two p{margin:0;font-size:15px;line-height:1.7}
.story a{display:block;text-decoration:none}
.story .st{font-size:19px;margin:2px 0 4px}
.story .go{color:var(--acc);font-size:14px}
.kin{display:flex;flex-wrap:wrap;gap:8px}
.kin a{font-size:14px;text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:5px 12px;background:var(--card)}
.rel{border:1px solid var(--acc);background:var(--card);border-radius:14px;padding:18px;text-align:center}
.rel .pair{font-size:26px;margin:4px 0}
.rel .rl{display:inline-block;background:var(--acc);color:#fff;border-radius:999px;padding:2px 12px;font-size:13px;margin:4px 0 10px}
.rel p{margin:0;font-size:15px}
.ask textarea{width:100%;border:1px solid var(--line);border-radius:12px;background:var(--paper);color:var(--ink);font:inherit;font-size:16px;padding:10px 12px;resize:none;min-height:70px}
.ask .btn{margin-top:10px}
.foot{margin-top:28px;text-align:center;font-size:12px;color:var(--muted);line-height:1.9}
.notice{border:1px dashed var(--fam);border-radius:14px;padding:12px 14px;font-size:14px;line-height:1.7;margin-top:18px}
.notice button{border:0;background:transparent;color:var(--fam);font:inherit;font-size:14px;padding:0;margin-left:4px;cursor:pointer;text-decoration:underline}
.moments{list-style:none;margin:0;padding:0}
.moments li{position:relative;padding:11px 0 11px 18px;border-top:1px solid var(--line);font-size:16px;line-height:1.7}
.moments li:first-child{border-top:0;padding-top:0}
.moments li:before{content:"";position:absolute;left:2px;top:22px;width:6px;height:6px;border-radius:50%;background:var(--fam)}
.moments li:first-child:before{top:11px}
.ar{display:block;text-decoration:none;padding:14px 0 0;margin-top:14px;border-top:1px solid var(--line)}
.ar:first-of-type{border-top:0;margin-top:0;padding-top:0}
.arh{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.arl{font-size:12px;color:var(--muted);letter-spacing:.12em}
.arn{font-size:21px}
.art{font-size:12px;color:var(--fam);border:1px solid var(--fam);border-radius:999px;padding:0 8px;line-height:20px}
.ar p{margin:6px 0 0;font-size:14px;line-height:1.75}
.ar+.btn{margin-top:16px}
.dimdesc{display:grid;grid-template-columns:1fr 1fr;gap:4px 14px;margin-top:10px;padding-top:12px;border-top:1px solid var(--line);font-size:12px;color:var(--muted);line-height:1.6}
.dimdesc b{color:var(--ink);font-weight:500;margin-right:4px}
/* 揭晓 */
#reveal{display:none;text-align:center;padding:110px 0 90px}
.rv-tip{font-size:14px;color:var(--muted);letter-spacing:.12em;margin:0}
.rv-name{font-size:54px;line-height:1.3;margin:26px 0 10px;min-height:72px;transition:transform .35s,color .35s}
.rv-name.land{color:var(--acc);transform:scale(1.14)}
.rv-sub{font-size:13px;color:var(--muted);min-height:20px;margin:0}
@media (prefers-reduced-motion:reduce){.rv-name,.prog i,.dots button{transition:none}}
/* 全览 */
#types{display:none}
.fam{margin-top:22px}
.fam h3{font-size:18px;margin:0 0 2px}
.fam .ft{font-size:13px;color:var(--muted);margin:0 0 10px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.tile{border:1px solid var(--line);border-radius:14px;background:var(--card);padding:12px 12px 10px;text-decoration:none;display:block}
.tile b{display:block;font-size:20px;font-family:"Noto Serif SC","Songti SC",serif}
.tile span{display:block;font-size:13px;line-height:1.5;margin-top:2px}
.tile em{display:block;font-style:normal;font-size:11px;letter-spacing:.12em;margin-top:6px}
/* 分享卡浮层 */
#shot{position:fixed;inset:0;background:rgba(0,0,0,.72);display:none;align-items:center;justify-content:center;flex-direction:column;z-index:60;padding:18px}
#shot img{max-width:100%;max-height:78vh;border-radius:10px}
#shot p{color:#fff;font-size:14px;margin:12px 0 8px}
#shot .row{display:flex;gap:10px}
#shot .row a,#shot .row button{color:#fff;border:1px solid rgba(255,255,255,.6);background:transparent;border-radius:999px;padding:8px 16px;font-size:14px;text-decoration:none;cursor:pointer;font-family:inherit}
.toast{position:fixed;left:50%;bottom:36px;transform:translateX(-50%);background:var(--ink);color:var(--paper);padding:10px 18px;border-radius:999px;font-size:14px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:70}
.toast.on{opacity:1}
"""

HTML = r"""<!DOCTYPE html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>测测你的历史分身 · 64 种历史人格 — 人类世界生存法则</title>
<meta name="description" content="24 道遇事题，3 分钟，测出 2600 年里和你是同一种人的那位：项羽、张良、苏轼、徐霞客、居里、乔布斯……64 种历史人格，每一种都链到他当年的真事。">
<meta property="og:title" content="测测你的历史分身">
<meta property="og:description" content="24 道遇事题，测出 2600 年里和你是同一种人的那位。64 种历史人格。">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ourword.ai/ce/">
<meta property="og:image" content="https://ourword.ai/ce/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://ourword.ai/ce/og.png">
<link rel="canonical" href="https://ourword.ai/ce/">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700&display=swap">
<style>__CSS__</style>
</head>
<body>
<div class="wrap">
  <div class="top mast-top"><a href="/"><span class="seal">人</span>人类世界生存法则</a><a href="#types" id="toTypes">64 型全览</a></div>

  <section id="start">
    <h1 class="serif">测测你的<br>历史分身</h1>
    <p class="sub">24 道遇事题 · 3 分钟 · 64 种历史人格</p>
    <div class="from" id="fromBox" style="display:none"></div>
    <p class="hook">遇到事的时候，你是先冲，还是先等？<br>是硬刚，还是绕过去？<br>2600 年里，总有一个人和你是同一种人。</p>
    <div class="peek"><p class="pl">下面这几句，有没有一句说的就是你？点一下，看是谁。</p><ul id="peekList"></ul><button class="re" id="peekRe" type="button">换三句</button></div>
    <button class="btn" id="go">开始测试</button>
    <p class="pairhook">测完叫朋友也来测，看你们俩在历史上是什么关系：君臣、宿敌，还是隔代知己。</p>
    <p class="muted" style="font-size:13px">每一种结果，都链到那个人当年的真事。</p>
  </section>

  <section id="quiz">
    <div class="prog"><i id="bar"></i></div>
    <div class="pn"><span id="pn">1 / 20</span><span id="pax"></span></div>
    <p class="echo" id="echo"></p>
    <div class="qq serif" id="qq"></div>
    <div class="opt"><small>A</small><span id="oa"></span></div>
    <div class="dots" id="dots">
      <button data-v="-2" aria-label="非常像 A"></button><button data-v="-1" aria-label="偏 A"></button><button data-v="0" aria-label="都有可能"></button><button data-v="1" aria-label="偏 B"></button><button data-v="2" aria-label="非常像 B"></button>
    </div>
    <div class="dotlab"><span>更像 A</span><span>都有可能</span><span>更像 B</span></div>
    <div class="opt"><small>B</small><span id="ob"></span></div>
    <button class="back" id="prev">← 上一题</button>
  </section>

  <section id="reveal" aria-live="polite">
    <p class="rv-tip">正在 2600 年里，找和你同一种人……</p>
    <div class="rv-name serif" id="rvName"></div>
    <p class="rv-sub" id="rvSub"></p>
  </section>

  <section id="result"></section>
  <section id="types"></section>

  <div class="foot">人物、故事、原话，都来自 <a href="/">ourword.ai</a> 的人物库。<br>测着玩的。真遇到事了，去看他们当年是怎么处理的。</div>
</div>
<div id="shot"><img id="shotImg" alt="分享卡"><p>长按图片保存，或者</p><div class="row"><a id="shotDl" download="我的历史分身.png">下载</a><button id="shotX">关闭</button></div></div>
<div class="toast" id="toast"></div>
<script src="/assets/vendor/qrcode-generator-1.4.4.js" defer></script>
<script>window.CE=__DATA__;</script>
<script>__JS__</script>
<script src="/assets/hw-chat.js" defer></script>
</body>
</html>
"""

JS = r"""
(function(){
var D=window.CE, A=D.axes, DIMS=D.dims, T=D.types, Q=D.qs;
var $=function(id){return document.getElementById(id)};
var ans=new Array(Q.length), cur=0;
var qs=new URLSearchParams(location.search);
var fromIdx=qs.has('f')?parseInt(qs.get('f'),10):-1; if(!(fromIdx>=0&&fromIdx<T.length))fromIdx=-1;
var RM=!!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
function trk(n,p){try{if(window.gtag)gtag('event',n,p||{})}catch(e){}}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function fam(t){return D.fam[t.code[0]+t.code[2]]}
function he(t){return t.she?'她':'他'}
function typeHref(i){return '?r='+i}
function toast(m){var e=$('toast');e.textContent=m;e.classList.add('on');setTimeout(function(){e.classList.remove('on')},1800)}
function show(id){['start','quiz','reveal','result','types'].forEach(function(s){$(s).style.display=(s===id)?'block':'none'});window.scrollTo(0,0)}
function isDark(){var a=document.documentElement.getAttribute('data-theme');if(a)return a==='dark';
  return window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches}
/* 家族色在深色底上要提亮：布局者的蓝灰在 #171410 上几乎看不见。混 45% 的米白进去。 */
function famCol(f){if(!isDark())return f.color;var h=f.color.slice(1),n=parseInt(h,16),
  r=n>>16,g=n>>8&255,b=n&255,mix=function(c){return Math.round(c+(234-c)*.45)};
  return 'rgb('+mix(r)+','+mix(g)+','+mix(b)+')'}
function rgba(c,a){if(c.charAt(0)==='#'){var n=parseInt(c.slice(1),16);return 'rgba('+(n>>16)+','+(n>>8&255)+','+(n&255)+','+a+')'}
  return c.replace('rgb(','rgba(').replace(')',','+a+')')}
/* 测完的答案存在本机（只存 20 个数）：点进别的人物再回来、或者打开朋友的链接，不用重测。 */
var KEY='ce_ans_v2';
function save(){saved=ans.slice();try{localStorage.setItem(KEY,JSON.stringify(ans));localStorage.removeItem(KEY+'_wip')}catch(e){}}
/* 答到一半离开（切去回个消息）回来能接着答，不用从头再来 */
function saveWip(){try{localStorage.setItem(KEY+'_wip',JSON.stringify({a:ans,c:cur}))}catch(e){}}
function loadWip(){try{var w=JSON.parse(localStorage.getItem(KEY+'_wip')||'null');
  if(w&&w.a&&w.a.length===Q.length&&w.c>0&&w.c<Q.length)return w}catch(e){}return null}
function load(){try{var a=JSON.parse(localStorage.getItem(KEY)||'null');
  if(a&&a.length===Q.length&&a.every(function(v){return v===-2||v===-1||v===0||v===1||v===2}))return a}catch(e){}return null}
var saved=load();

/* ── 开始页 ── */
(function(){
  /* 先让人对号入座：随手抽三型（三个不同家族）的「你一定干过」各一句，不报名字；
     点一下才露出是谁。被说中的那一下，比任何介绍都更让人想测。 */
  function peek(){var seen={},out=[],n=0;
    while(out.length<3&&n++<300){var i=Math.floor(Math.random()*T.length),k=T[i].code[0]+T[i].code[2];if(seen[k])continue;seen[k]=1;out.push(i)}
    $('peekList').innerHTML=out.map(function(i){var t=T[i],ms=t.moments;
      return '<li data-i="'+i+'">'+esc(ms[Math.floor(Math.random()*ms.length)])+'<em>—— 这是'+esc(t.who)+'那一型。你是不是，测完才知道。</em></li>'}).join('');
    [].forEach.call($('peekList').children,function(li){li.onclick=function(){li.classList.toggle('on');
      if(li.classList.contains('on'))trk('ce_peek',{who:T[+li.dataset.i].who})}})}
  peek(); $('peekRe').onclick=function(){peek();trk('ce_peek_more')};
  if(fromIdx>=0){var t=T[fromIdx];
    $('fromBox').style.display='block';
    trk('ce_from_open',{from:t.who});
    if(qs.has('c')){   // 扫的是分享卡上的码：卡上已经写着答案，不用猜
      document.title='朋友测出来是'+t.who+'，你呢？测测你的历史分身';
      $('fromBox').innerHTML='你的朋友测出来是 <b>'+esc(t.who)+'</b>（'+esc(t.title)+'）。<br>测完看看，你们俩在历史上是什么关系。';
    }else{
      /* 邀请链接进来的：先猜朋友是谁。四个选项：答案 + 另外三个家族各抽一位（按朋友那一型定，刷新不变） */
      document.title='猜猜你朋友是历史上的谁 · 测测你的历史分身';
      var fk=function(x){return x.code[0]+x.code[2]},opts=[t],seed=fromIdx*7+3;
      Object.keys(D.fam).forEach(function(k){if(k===fk(t))return;var c=T.filter(function(x){return fk(x)===k});opts.push(c[(seed+=11)%c.length])});
      opts.sort(function(a,b){return (T.indexOf(a)*13+fromIdx)%17-(T.indexOf(b)*13+fromIdx)%17});
      $('fromBox').innerHTML='你朋友刚测完。先猜猜：<b>你朋友是历史上的谁？</b><div class="guess">'
        +opts.map(function(o){return '<button type="button" data-i="'+T.indexOf(o)+'">'+esc(o.who)+'</button>'}).join('')+'</div><p class="gres" id="gres"></p>';
      [].forEach.call(document.querySelectorAll('.guess button'),function(b){b.onclick=function(){
        var pick=T[+b.dataset.i],ok=pick===t;
        [].forEach.call(document.querySelectorAll('.guess button'),function(x){x.disabled=true;if(+x.dataset.i===fromIdx)x.classList.add('ok')});
        if(!ok)b.classList.add('no');
        $('gres').innerHTML=(ok?'猜中了，你果然懂你朋友。':'不是'+esc(pick.who)+'——原来在你眼里，你朋友是'+esc(pick.who)+'那一型。')
          +'<br>你朋友是 <b>'+esc(t.who)+'</b>（'+esc(t.title)+'）。那你呢？测完看看，你们俩在历史上是什么关系。';
        trk('ce_guess',{from:t.who,pick:pick.who,ok:ok?1:0});}});
    }}
  if(saved){var s0=scoreOf(D,saved);if(s0.idx>=0){var t0=T[s0.idx],b=document.createElement('button');
    b.className='btn ghost';b.id='seeMine';
    b.textContent=fromIdx>=0?'你上次测出来是'+t0.who+'，直接看你们俩的关系':'上次测出来是'+t0.who+'，看我的结果';
    $('go').insertAdjacentElement('afterend',b);
    b.onclick=function(){ans=saved.slice();trk('ce_reopen',{who:t0.who});renderType(t0,scoreOf(D,ans))};}}
})();
$('go').onclick=function(){ans=new Array(Q.length);cur=0;show('quiz');paintQ();trk('ce_start',{from:fromIdx>=0?T[fromIdx].who:''})};
(function(){var w=loadWip();if(!w)return;var b=document.createElement('button');b.className='btn ghost';b.id='resume';
  b.textContent='接着上次答（第 '+(w.c+1)+' / '+Q.length+' 题）';$('go').insertAdjacentElement('afterend',b);
  b.onclick=function(){ans=w.a.map(function(v){return v===null?undefined:v});cur=w.c;show('quiz');paintQ();trk('ce_resume',{at:w.c})};})();

/* ── 答题 ── */
function paintQ(){
  var q=Q[cur];
  $('bar').style.width=(cur/Q.length*100)+'%';
  $('pn').textContent=(cur+1)+' / '+Q.length;
  if(!cur)$('echo').textContent='';
  var n=left(); $('pax').textContent=n>=T.length?(cur>=Q.length/2?'过半了':''):n<=1?'只剩 1 种人了':'人选还剩 '+n+' 种';
  /* 对调的题：右极那一项放在 A 位。打分时在 scoreOf 里翻回来。 */
  $('qq').textContent=q.q; $('oa').textContent=q.flip?q.b:q.a; $('ob').textContent=q.flip?q.a:q.b;
  [].forEach.call($('dots').children,function(b){b.classList.toggle('on',ans[cur]!==undefined&&+b.dataset.v===ans[cur])});
  $('prev').style.visibility=cur?'visible':'hidden';
}
/* 人选还剩几种：一维里剩下的题全反着答也翻不过来了，这一维才算定下，只留那一极的型。
   这样数字只降不升（第一版按「眼下偏哪边」算，交替作答会 32→1→32 来回跳）。 */
function left(){var s=A.map(function(){return 0}),rest=A.map(function(){return 0});
  Q.forEach(function(q,i){var v=ans[i];if(v!==undefined&&i<cur)s[q.axis]+=v*(q.flip?-1:1);else rest[q.axis]++});
  return T.filter(function(t){var c=t.code.replace('-','');
    return s.every(function(x,a){return Math.abs(x)<=2*rest[a]||c[a]===(x<0?A[a][0]:A[a][1])})}).length}
/* 刚答的那题，哪两位跟你选的是同一边（按他们各自的类型推，不是史书记载） */
function echo(i){var q=Q[i],v=(ans[i]||0)*(q.flip?-1:1),el=$('echo');
  if(!v){el.textContent='';return}
  var pole=v<0?A[q.axis][0]:A[q.axis][1],c=T.filter(function(t){return t.code.replace('-','')[q.axis]===pole}),
    a=c[Math.floor(Math.random()*c.length)],b;do{b=c[Math.floor(Math.random()*c.length)]}while(b===a);
  el.innerHTML='上一题跟你选得一样的：<b>'+esc(a.who)+'</b>、<b>'+esc(b.who)+'</b><i>按类型推算</i>'}
[].forEach.call($('dots').children,function(b){b.onclick=function(){
  ans[cur]=+b.dataset.v; echo(cur); paintQ();
  setTimeout(function(){ if(cur<Q.length-1){cur++;paintQ();saveWip();if(cur===Q.length/2)teaser()} else finish(); },180);
}});
/* 答到一半先透露一点：分身属于哪个家族（按已答的题现算）—— 让人想把剩下一半答完 */
function teaser(){var s=scoreOf(D,ans),f=D.fam[s.pole[0]+s.pole[2]];
  if(!f)return;var e=$('toast');e.textContent='过半了：你的历史分身来自「'+f.name+'」家族';e.classList.add('on');
  setTimeout(function(){e.classList.remove('on')},2600);trk('ce_teaser',{fam:f.name})}
$('prev').onclick=function(){if(cur>0){cur--;$('echo').textContent='';paintQ()}};

/*SCORE-BEGIN*/
/* 打分：全部按答题现算。这一段是纯函数（只读 D 和 ans），
   scripts/check_ce.py 会把它原样抠出来放进 node 里，模拟两万个人答题，
   看 32 型是不是都抽得到、分布匀不匀 —— 判据跑的就是页面上这份代码，不是另抄一份。
   ans 记的是点了哪个圈（负 = 更像 A）；对调过的题（flip）A 位放的是右极，所以先翻回来。 */
function scoreOf(D,ans){
  var A=D.axes,Q=D.qs,DIMS=D.dims,T=D.types;
  var sum=A.map(function(){return 0}), first=A.map(function(){return 0}), tot=0;
  var raw={},mx={}; DIMS.forEach(function(d){raw[d]=0;mx[d]=0});
  Q.forEach(function(q,i){
    var v=(ans[i]||0)*(q.flip?-1:1); sum[q.axis]+=v; tot+=v; if(v&&!first[q.axis])first[q.axis]=v;
    DIMS.forEach(function(d){
      var a=q.da[d]||0,b=q.db[d]||0; mx[d]+=Math.max(a,b);
      raw[d]+= v<0 ? a*(-v/2) : v>0 ? b*(v/2) : (a+b)*0.25;
    });
  });
  var pct=sum.map(function(s){return Math.round(50-s/8*50)});      // 左极占比
  /* 平局：看这一维里第一道没选中间的题。第一版是「最用力那一题，没有就取左极」——
     真人爱选中间，平局多，左极于是白捡：模拟出来韩信 4.5%、杜甫 2.1%，差一倍。 */
  var pole=pct.map(function(p,i){
    if(p!==50)return p>50?A[i][0]:A[i][1];
    var k=first[i]||tot; return k>0?A[i][1]:A[i][0];
  });
  /* 显示刻度 10–98：照样按答题现算，只是不让它出 0 和满分 ——
     第一版极端答法测出「胆识 0」「识人 100」，0 像程序坏了，100 像假的。 */
  var dims=DIMS.map(function(d){return mx[d]?Math.round(10+88*raw[d]/mx[d]):10});
  var nb=A.length-1, code=pole.slice(0,nb).join('')+'-'+pole[nb];
  var idx=-1; for(var n=0;n<T.length;n++)if(T[n].code===code){idx=n;break}
  return {pct:pct,pole:pole,dims:dims,code:code,idx:idx};
}
/*SCORE-END*/
function score(){return scoreOf(D,ans)}
function match(s,t){
  var dot=0,na=0,nb=0; s.dims.forEach(function(x,i){dot+=x*t.dims[i];na+=x*x;nb+=t.dims[i]*t.dims[i]});
  var cos=(na&&nb)?dot/Math.sqrt(na*nb):0;
  var lean=0; t.code.replace('-','').split('').forEach(function(ch,i){lean+= (A[i][0]===ch?s.pct[i]:100-s.pct[i])});
  lean/=A.length;
  return Math.round(100*(0.5*cos+0.5*lean/100));
}
/* 稀有度：和你同一型、而且六维里「倾向鲜明」的维数也和你一样的人，在一批模拟答卷里占多少。
   模拟的人不是乱点：每人先有一套自己的倾向（每维一个偏向），再带着噪声答 24 题 —— 像真人那样前后大体一致。
   只按「同一型」算，人人都是 1/64，没有高低；再按「倾向鲜明的维数」分三档（0–1 / 2–3 / 4–6）。
   第一版按 0–6 维分七格：每题都点「非常」的人在模拟里一份都撞不上，人人「万里挑一」，站主一看就说太假。
   分三档后：没人撞空，多数人 0.4%–0.9%，答得最极端的约 0.1%，最高不过 1/64。
   固定种子，同一份答卷每次算出同一个数。 */
var SIM=null,SIMN=12000;
function vivid(s){var v=s.pct.filter(function(p){return Math.abs(p-50)>=30}).length;return v<=1?0:v<=3?1:2}
function sims(){if(SIM)return SIM;var sd=20261009,out=[];
  function r(){sd=(sd*1103515245+12345)%2147483648;return sd/2147483648}
  for(var k=0;k<SIMN;k++){var lean=A.map(function(){return (r()*2-1)*1.6});
    var a=Q.map(function(q){var v=Math.round(lean[q.axis]+(r()+r()+r()-1.5)*1.15);v=Math.max(-2,Math.min(2,v));return v*(q.flip?-1:1)});
    var s=scoreOf(D,a);if(s.idx>=0)out.push([s.idx,vivid(s)])}
  return SIM=out}
function rarity(me,t){var S=sims(),i=T.indexOf(t),v=vivid(me),k=0;
  S.forEach(function(x){if(x[0]===i&&x[1]===v)k++});
  /* 一份模拟答卷都没撞上：不写「每 12000 人 1 个」（那只是模拟的份数，看着像凑的），写万里挑一 */
  if(!k)return {p:0,txt:'<0.01%',ev:'万里挑一'};
  var p=k/S.length,pct=p*100;
  return {p:p,txt:(pct>=1?pct.toFixed(1):pct.toFixed(2))+'%',ev:'每 '+Math.max(2,Math.round(1/p))+' 人 1 个'}}
/* 答得不像真答的时候，明说结果可能不准 —— 而不是装作很准。 */
function notice(){
  var zero=0,cnt={},mx=0;
  ans.forEach(function(v){v=v||0;if(!v)zero++;cnt[v]=(cnt[v]||0)+1;if(cnt[v]>mx)mx=cnt[v]});
  if(zero>=Q.length/2)return '你有 '+zero+' 道题选了「都有可能」，结果可能没那么准。凭第一反应再测一次，会更像你。';
  if(mx>=Q.length-2)return '你几乎每道题都点在同一个位置。A 和 B 是会换边的，认真读一遍题再测，结果会更准。';
  return '';
}

/* ── 雷达 ── */
function radar(me,base,who){
  var W=340,H=320,cx=170,cy=165,R=112,n=DIMS.length,col=getComputedStyle(document.documentElement).getPropertyValue('--fam')||'#a33b2e';
  function pt(i,v){var a=-Math.PI/2+i*2*Math.PI/n;return [cx+Math.cos(a)*R*v/100, cy+Math.sin(a)*R*v/100]}
  var g='';
  [20,40,60,80,100].forEach(function(r){g+='<polygon points="'+DIMS.map(function(_,i){return pt(i,r).join(',')}).join(' ')+'" fill="none" stroke="var(--line)" stroke-width="1"/>'});
  DIMS.forEach(function(_,i){var p=pt(i,100);g+='<line x1="'+cx+'" y1="'+cy+'" x2="'+p[0]+'" y2="'+p[1]+'" stroke="var(--line)"/>'});
  if(base)g+='<polygon points="'+base.map(function(v,i){return pt(i,v).join(',')}).join(' ')+'" fill="none" stroke="#c9a27e" stroke-width="2" stroke-dasharray="6 5"/>';
  if(me){g+='<polygon points="'+me.map(function(v,i){return pt(i,v).join(',')}).join(' ')+'" fill="'+col+'" fill-opacity=".16" stroke="'+col+'" stroke-width="2.5"/>';
    me.forEach(function(v,i){var p=pt(i,v);g+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="4" fill="'+col+'"/>'});}
  DIMS.forEach(function(d,i){var p=pt(i,128);g+='<text x="'+p[0]+'" y="'+(p[1]+5)+'" text-anchor="middle" font-size="14" fill="var(--ink)">'+d+'</text>'});
  return '<svg class="radar" viewBox="0 0 '+W+' '+H+'">'+g+'</svg>'
    +'<div class="legend">'+(me?'<span><i style="background:'+col+'"></i>你的特征</span>':'')+'<span><i style="background:#c9a27e"></i>'+esc(who)+'基准</span></div>';
}

/* ── 关系 ── */
function relation(a,b){
  if(a.who===b.who)return {l:'灵魂双胞胎',t:'你们测出了同一个人——不用解释，对方就懂。'};
  for(var i=0;i<D.rel.length;i++){var r=D.rel[i];
    if((r[0]===a.who&&r[1]===b.who)||(r[0]===b.who&&r[1]===a.who))return {l:r[2],t:r[3],real:1};}
  var d=0,diff=[]; for(var k=0;k<A.length-1;k++)if(a.code[k]!==b.code[k]){d++;diff.push(k)}
  var x=D.reld[String(d)];
  /* 推算出来的关系，说清在哪几维相反，比一句通用的话好认 */
  function dsc(t,k){return t.code[k]===A[k][0]?A[k][2]:A[k][3]}
  var sp=diff.slice(0,2).map(function(k){return a.who+dsc(a,k)+'，'+b.who+dsc(b,k)}).join('；');
  return {l:x[0],t:(sp?sp+'。':'')+x[1]};
}
function arRow(lab,x){var o=T[x.i];
  return '<a class="ar" href="'+typeHref(x.i)+'" data-trk="ce_to_partner"><div class="arh"><span class="arl">'+lab+'</span><span class="arn serif">'+esc(o.who)+'</span><span class="art">'+(x.real?esc(x.l)+' · 史上真事':'按六维推算')+'</span></div><p>'+esc(x.t)+'</p></a>'}
function invite(t){
  var url=location.origin+location.pathname+'?f='+T.indexOf(t);
  var txt='我测了「我是历史上的谁」。你先猜猜我是谁？猜完你也测测，看我们俩是什么关系：';
  trk('ce_invite',{who:t.who});
  if(navigator.share){navigator.share({title:'测测你的历史分身',text:txt,url:url}).catch(function(){})}
  else if(navigator.clipboard){navigator.clipboard.writeText(txt+' '+url).then(function(){toast('链接已复制，发给朋友吧')})}
  else prompt('复制这个链接发给朋友：',url);
}
function countUp(){
  if(RM)return;
  var els=[].slice.call(document.querySelectorAll('[data-count]')); if(!els.length)return;
  var t0=0;
  function step(ts){if(!t0)t0=ts;var k=Math.min(1,(ts-t0)/800),e=1-Math.pow(1-k,3);
    els.forEach(function(el){el.textContent=Math.round(+el.dataset.count*e)+(el.dataset.suf||'')});
    if(k<1)requestAnimationFrame(step)}
  requestAnimationFrame(step);
  /* 兜底：后台标签页、部分 App 内置浏览器会停掉动画帧，数字会卡在半路（实测截到过 14%）。
     一秒后无论如何写上最终值；动画帧之后恢复，会从 0 再数一遍到同一个数。 */
  setTimeout(function(){els.forEach(function(el){el.textContent=el.dataset.count+(el.dataset.suf||'')})},1000);
}

/* ── 结果页（me 为空 = 只看这一型的介绍）── */
var hitK=-1;   // 「说中了」点中的那一句；分享卡印这一句，没点就印第一句
function renderType(t,me){
  hitK=-1;
  var f=fam(t); document.documentElement.style.setProperty('--fam',famCol(f));
  var h='', m=me?match(me,t):null, P=he(t), fr=(me&&fromIdx>=0)?T[fromIdx]:null;
  h+='<div class="hero"><div class="eyebrow">Your Historical Twin · 你的历史分身</div>';
  if(me)h+='<div class="pill">◆ 你的历史分身契合度 <b data-count="'+m+'" data-suf="%">'+m+'%</b> ◆</div>';
  else h+='<div class="pill">◆ 64 型之一 · '+esc(f.name)+' ◆</div>';
  h+='<div class="name serif'+(t.who.length>3?' long':'')+'">'+esc(t.who)+'</div><div class="rule"><i></i><b></b><i></i></div>';
  h+='<p class="title serif">'+esc(t.title)+'</p>';
  h+='<div class="chips"><span class="chip solid">'+esc(t.code)+'</span><span class="chip">'+esc(f.name)+' · '+esc(f.tag)+'</span></div>';
  h+='<div class="quote serif">'+esc(t.quote)+'</div><div class="qsrc">—— '+esc(t.quote_src)+'</div></div>';

  if(me){
    var nt=notice(); if(nt)h+='<div class="notice">'+esc(nt)+'<button id="redo">再测一次</button></div>';
    /* 朋友带来的人，最想看的就是这一块，放在最上面 */
    if(fr){var rel=relation(t,fr);
      h+='<div class="rel sec"><div class="eyebrow" style="color:var(--acc)">你和朋友在历史上是</div><div class="pair serif">'+esc(t.who)+' × '+esc(fr.who)+'</div><span class="rl">'+esc(rel.l)+'</span><p>'+esc(rel.t)+'</p></div>';
      trk('ce_pair',{me:t.who,friend:fr.who,rel:rel.l});}
    var order=DIMS.map(function(d,i){return [d,me.dims[i]]}).sort(function(x,y){return y[1]-x[1]});
    h+='<div class="stats"><div class="stat"><b>'+order[0][1]+'</b><span>'+order[0][0]+'</span><em>最高维度</em></div>'
      +'<div class="stat mid"><b data-count="'+m+'" data-suf="%">'+m+'%</b><span>分身契合度</span><em>'+esc(t.who)+'</em></div>'
      +'<div class="stat"><b id="rareV">…</b><span>稀有度</span><em id="rareE">正在算</em></div></div>'
      +'<p class="rarenote">稀有度：按 '+SIMN+' 份模拟答卷算——和你同一型、倾向的鲜明程度也和你差不多的人，占多少。</p>';
  }
  h+='<div class="card sec"><div class="lab">'+(me?'你一定干过这些事':'这一型的人，一定干过这些事')+' · MOMENTS</div><ul class="moments">'
    +t.moments.map(function(x,i){return '<li>'+esc(x)+(me?'<button class="hit" type="button" data-k="'+i+'">说中了</button>':'')+'</li>'}).join('')+'</ul>'
    +(me?'<p class="hint">哪句说中了你，点一下；分享卡上印的就是那一句。</p>':'')+'</div>';
  h+='<div class="card sec"><div class="lab">你是这样的人 · PORTRAIT</div><div class="desc serif">'+esc(t.desc)+'</div></div>';
  h+='<div class="two sec"><div class="card"><h4>你的超能力</h4><p>'+esc(t.power)+'</p></div><div class="card"><h4>你最容易栽在</h4><p>'+esc(t.pit)+'</p></div></div>';
  h+='<div class="card sec story"><div class="lab">'+P+'当年那件事 · THE STORY</div><a href="'+t.story.u+'" data-trk="ce_to_chapter"><div class="st serif">'+esc(t.story.t)+'</div><div class="go">读'+esc(t.who)+'当年是怎么做的 →</div></a></div>';
  h+='<div class="card sec"><div class="lab">拍档与宿敌 · ALLIES &amp; RIVALS</div>'+arRow('最佳拍档',t.ally)+arRow('宿命对手',t.rival)
    +(me?'<button class="btn ghost" id="invite2">叫朋友来测，看谁是你的'+esc(T[t.ally.i].who)+'</button>':'')+'</div>';
  if(me){
    h+='<div class="card sec"><div class="lab">你的遇事倾向 · TRAITS</div>';
    A.forEach(function(ax,i){var L=me.pct[i],mine=me.pole[i];
      h+='<div class="axis"><div class="row"><span>'+(mine===ax[0]?'<b>'+ax[0]+' · '+ax[2]+' '+L+'%</b>':ax[0]+' · '+ax[2]+' '+L+'%')+'</span><span>'+(mine===ax[1]?'<b>'+(100-L)+'% '+ax[3]+' · '+ax[1]+'</b>':(100-L)+'% '+ax[3]+' · '+ax[1])+'</span></div>'
        +'<div class="bar"><i style="'+(mine===ax[0]?'left:0;width:'+L+'%':'right:0;width:'+(100-L)+'%')+'"></i></div></div>';
    });
    h+='</div>';
  }
  h+='<div class="card sec"><div class="lab">六维特征图谱 · RADAR PROFILE</div>'+radar(me?me.dims:null,t.dims,t.who)+'</div>';
  if(me){
    h+='<div class="card sec"><div class="lab">维度得分 · DIMENSION SCORES</div>';
    var rk={}; order.forEach(function(x,i){rk[x[0]]=i+1});
    DIMS.forEach(function(d,i){var r=rk[d];
      h+='<div class="dim'+(r<=2?' top':'')+'"><span class="rk">'+r+'</span><span class="dn">'+d+'</span><span class="db"><i style="width:'+me.dims[i]+'%"></i></span><span class="dv">'+me.dims[i]+'</span></div>';});
    h+='<div class="dimdesc">'+DIMS.map(function(d){return '<span><b>'+d+'</b>'+esc(D.dimdesc[d])+'</span>'}).join('')+'</div></div>';
  }
  var kin=D.kin[t.code.split('-')[0]]||[];
  if(kin.length)h+='<div class="card sec"><div class="lab">同型名人 · ALSO THIS TYPE</div><div class="kin">'+kin.map(function(k){return '<a href="'+k.u+'">'+esc(k.n)+'</a>'}).join('')+'<a href="/i/'+t.slug+'/">'+esc(t.who)+'的全部篇章 →</a></div></div>';

  if(me){
    h+='<div class="card sec ask"><div class="lab">问问'+esc(t.who)+' · ASK</div><p class="muted" style="margin:0 0 10px;font-size:14px">说说你最近遇到的一件事，看看'+esc(t.who)+'会怎么处理。</p><textarea id="askIn" placeholder="比如：老板天天改需求，我手上三件事都做不完"></textarea><button class="btn" id="askGo">问'+esc(t.who)+'</button></div>';
    h+='<div class="sec">'+(fr?'<button class="btn" id="pairCard">生成我们俩的关系卡</button><button class="btn ghost" id="shareCard">生成我的分享卡</button>':'<button class="btn" id="shareCard">生成我的分享卡</button>')
      +'<button class="btn ghost" id="invite">叫朋友来测，看你们是什么关系</button><button class="btn ghost" id="again">重新测一次</button></div>';
  }else{
    var mine=saved?scoreOf(D,saved):null;
    h+='<div class="sec"><button class="btn" id="tryIt">测测你是不是'+esc(t.who)+'</button>'
      +(mine&&mine.idx>=0?'<button class="btn ghost" id="backMine">回到我的结果（'+esc(T[mine.idx].who)+'）</button>':'')
      +'<a class="btn ghost" href="#types">看全部 64 型</a></div>';
  }
  $('result').innerHTML=h; show('result');
  if(me)document.title='我是'+t.who+' · '+t.title+'——测测你的历史分身';
  [].forEach.call(document.querySelectorAll('[data-trk]'),function(a){a.onclick=function(){trk(a.dataset.trk,{who:t.who})}});
  var retake=function(){ans=new Array(Q.length);cur=0;show('quiz');paintQ()};
  if(me){
    $('again').onclick=retake; if($('redo'))$('redo').onclick=retake;
    $('askGo').onclick=function(){var v=($('askIn').value||'').trim()||'我最近遇到一件事，不知道怎么办';
      trk('ce_ask',{who:t.who});
      if(typeof window.hwAsk==='function')window.hwAsk(v+'（我测出来是'+t.who+'那一型，想听听'+t.who+'会怎么处理）',{pin:[t.story.u],scene:''});
      else location.href=t.story.u;};
    $('shareCard').onclick=function(){trk('ce_share_card',{who:t.who});withFonts(t.who+t.title+t.quote+t.quote_src,function(){card(t,me,m)})};
    if(fr)$('pairCard').onclick=function(){var rel=relation(t,fr);trk('ce_pair_card',{me:t.who,friend:fr.who});withFonts(t.who+t.title+fr.who+fr.title+rel.t,function(){pairCard(t,fr,rel)})};
    $('invite').onclick=function(){invite(t)}; $('invite2').onclick=function(){invite(t)};
    [].forEach.call(document.querySelectorAll('.moments .hit'),function(b){b.onclick=function(){
      var li=b.parentNode,on=!li.classList.contains('on'),k=+b.dataset.k;
      [].forEach.call(document.querySelectorAll('.moments li'),function(x){x.classList.remove('on');x.querySelector('.hit').textContent='说中了'});
      if(on){li.classList.add('on');b.textContent='✓ 说中了';hitK=k;trk('ce_moment_hit',{who:t.who,k:k})}else hitK=-1}});
    countUp();
    /* 稀有度要跑一万多份模拟答卷（手机上可能要一两秒），先把页面画出来再算 */
    setTimeout(function(){var rr=rarity(me,t);if(!$('rareV'))return;
      $('rareV').textContent=rr.txt;if(rr.txt.length>5)$('rareV').style.fontSize='21px';$('rareE').textContent=rr.ev;
      trk('ce_rarity',{who:t.who,p:Math.round(rr.p*10000)})},60);
  }else{
    $('tryIt').onclick=function(){fromIdx=-1;retake()};
    if($('backMine'))$('backMine').onclick=function(){ans=saved.slice();
      try{history.replaceState(null,'',location.pathname)}catch(e){}
      renderType(T[scoreOf(D,ans).idx],scoreOf(D,ans))};
  }
}

/* ── 揭晓：名字翻过去，停在你那一位。系统要求少动画时直接出结果。 ── */
function finish(){
  var s=score(); if(s.idx<0){s.idx=0}
  var t=T[s.idx];
  save();
  try{history.replaceState(null,'',location.pathname+(fromIdx>=0?'?f='+fromIdx:''))}catch(e){}
  trk('ce_done',{who:t.who,code:t.code});
  if(RM){renderType(t,s);return}
  show('reveal');
  var el=$('rvName'), sub=$('rvSub'), n=0, N=14;
  el.className='rv-name serif'; sub.textContent='';
  (function tick(){
    if(n<N){var o=T[(s.idx+5+n*11)%T.length]; if(o===t)o=T[(s.idx+1)%T.length];
      el.textContent=o.who; n++; setTimeout(tick,40+n*n*0.9)}
    else{el.textContent=t.who; el.className='rv-name serif land'; sub.textContent=t.title;
      setTimeout(function(){renderType(t,s)},900)}
  })();
}

/* ── 分享卡：3:4，给小红书用。图上只放名字、原型、金句和三个数 ── */
var SERIF='"Noto Serif SC","Songti SC","STSong",serif',SANS='-apple-system,"PingFang SC","Microsoft YaHei",sans-serif';
var P0='#f5f1e8',CARD='#faf7f0',INK='#1f1c17',MUT='#8a8377',LINE='#d8d2c6',ACC='#a33b2e';
/* 画卡前先把宋体里要用到的字取回来：网页字体按字分片下载，卡上的字页面上不一定出现过，
   没取到就会退成黑体（手机上没有自带宋体，实测关系卡整张变黑体）。最多等 2.5 秒，取不到照画。 */
function withFonts(s,fn){var ok=0,go=function(){if(!ok){ok=1;fn()}};
  if(!(document.fonts&&document.fonts.load))return go();
  Promise.all(['700 140px','600 54px','500 34px','40px','italic 42px'].map(function(f){return document.fonts.load(f+' "Noto Serif SC"',s)})).then(go,go);
  setTimeout(go,2500)}
function canvasKit(){
  var c=document.createElement('canvas'),W=1080,H=1440; c.width=W;c.height=H;
  var x=c.getContext('2d');
  x.fillStyle=P0;x.fillRect(0,0,W,H);
  x.strokeStyle=LINE;x.lineWidth=3;x.strokeRect(36,36,W-72,H-72);
  function txt(s,y,font,col,ls){x.font=font;x.fillStyle=col;x.textAlign='center';
    if(ls){var w=0,ch=s.split('');ch.forEach(function(k){w+=x.measureText(k).width+ls});var sx=W/2-w/2;x.textAlign='left';ch.forEach(function(k){x.fillText(k,sx,y);sx+=x.measureText(k).width+ls})}
    else x.fillText(s,W/2,y)}
  /* 折行守避头尾：逗号句号这类不许落在行首（宁可上一行略超），引号括号的前半不许留在行尾。
     第一版按宽度硬折，关系卡上折出了一行以「，」开头的字。 */
  var NOHEAD='，。、；：？！」』）》〉”’…—·',NOTAIL='「『（《〈“‘';
  function wrap(s,y,font,col,maxw,lh){x.font=font;x.fillStyle=col;x.textAlign='center';var line='',lines=[];
    s.split('').forEach(function(ch){
      if(line&&x.measureText(line+ch).width>maxw&&NOHEAD.indexOf(ch)<0){
        var carry='';while(line.length>1&&NOTAIL.indexOf(line.slice(-1))>=0){carry=line.slice(-1)+carry;line=line.slice(0,-1)}
        lines.push(line);line=carry+ch}
      else line+=ch});
    lines.push(line);
    lines.forEach(function(l,i){x.fillText(l,W/2,y+i*lh)});return y+lines.length*lh}
  function rrect(x0,y0,w,h,r){x.beginPath();x.moveTo(x0+r,y0);x.arcTo(x0+w,y0,x0+w,y0+h,r);x.arcTo(x0+w,y0+h,x0,y0+h,r);x.arcTo(x0,y0+h,x0,y0,r);x.arcTo(x0,y0,x0+w,y0,r);x.closePath()}
  /* 右下角二维码：微信里长按图片就能识别。码里是「朋友邀请」链接（?f=这一型），
     扫码的人测完直接看到两人的关系。白底 + 两格静区，模块取整像素，缩略图里也认得出。
     库没加载到（离线、被拦）就不画码，卡照出。 */
  function qr(url){if(typeof qrcode!=='function')return;
    try{var q=qrcode(0,'M');q.addData(url);q.make();var n=q.getModuleCount(),m=4,box=(n+4)*m,x0=W-110-box,y0=1390-box;
      x.fillStyle='#fff';x.fillRect(x0,y0,box,box);x.fillStyle='#1f1c17';
      for(var r=0;r<n;r++)for(var c=0;c<n;c++)if(q.isDark(r,c))x.fillRect(x0+(c+2)*m,y0+(r+2)*m,m,m)}catch(e){}}
  function foot(line1,line2){
    x.fillStyle=ACC;x.fillRect(110,1290,74,74);x.fillStyle='#fff';x.font='700 48px '+SERIF;x.textAlign='center';x.fillText('人',147,1345);
    x.textAlign='left';x.fillStyle=INK;x.font='600 36px '+SANS;x.fillText(line1,212,1322);
    x.fillStyle=MUT;x.font='28px '+SANS;x.fillText(line2,212,1362)}
  function done(){var url=c.toDataURL('image/png'); $('shotImg').src=url; $('shotDl').href=url; $('shot').style.display='flex'}
  return {x:x,W:W,txt:txt,wrap:wrap,rrect:rrect,foot:foot,qr:qr,done:done};
}
function inviteUrl(t){return 'https://ourword.ai'+(location.pathname.indexOf('/tw/')===0?'/tw/ce/':'/ce/')+'?f='+T.indexOf(t)+'&c=1'}
function card(t,me,m){
  var k=canvasKit(),x=k.x,W=k.W,f=fam(t);
  k.txt('YOUR HISTORICAL TWIN',128,'600 26px '+SANS,f.color,10);
  x.strokeStyle=f.color;x.lineWidth=3;var pw=560,ph=78,px=(W-pw)/2,py=166;k.rrect(px,py,pw,ph,ph/2);x.stroke();
  k.txt('你的历史分身契合度  '+m+'%',py+51,'500 34px '+SANS,f.color);
  k.txt(t.who,t.who.length>3?450:478,'700 '+(t.who.length>3?150:190)+'px '+SERIF,INK);
  x.fillStyle=f.color;x.fillRect(W/2-170,526,120,5);x.fillRect(W/2+50,526,120,5);x.beginPath();x.arc(W/2,528,10,0,7);x.fill();
  k.txt(t.title,614,'600 54px '+SERIF,INK);
  k.txt(t.code+'  ·  '+f.name,680,'500 34px '+SANS,f.color);
  var y=k.wrap('“'+t.quote+'”',772,'italic 42px '+SERIF,INK,820,62);
  k.txt('—— '+t.quote_src,y+6,'26px '+SANS,MUT);
  /* 最容易让人说「太准了」的那一句：读者点了「说中了」就印那句，没点就印第一句 */
  var mo=t.moments&&t.moments[hitK>=0?hitK:0];
  /* 尽量排成一行：一行放不下就把字缩到 26px；还放不下才折行（折行时下面的数字框会被顶到，所以先缩字） */
  if(mo&&y<950){var ml='你一定干过：'+mo,fs=30;x.font=fs+'px '+SANS;
    while(fs>26&&x.measureText(ml).width>860){fs--;x.font=fs+'px '+SANS}
    k.wrap(ml,y+72,fs+'px '+SANS,f.color,860,42)}
  var order=DIMS.map(function(d,i){return [d,me.dims[i]]}).sort(function(a,b){return b[1]-a[1]}),rr=rarity(me,t);
  var bx=[[100,'最高维度',order[0][0],String(order[0][1])],[400,'分身契合度',t.who,m+'%'],[700,rr.ev,'稀有度',rr.txt]];
  bx.forEach(function(b,i){var bw=280,bh=194,by=1028,mid=i===1;x.fillStyle=mid?f.color:CARD;x.strokeStyle=mid?f.color:LINE;x.lineWidth=3;
    k.rrect(b[0],by,bw,bh,24);x.fill();x.stroke();
    x.textAlign='center';x.fillStyle=mid?'#fff':INK;/* 字长（如「<0.01%」）按框宽缩字，别撑出框 */
    var fz=72;x.font='700 '+fz+'px '+SERIF;while(fz>40&&x.measureText(b[3]).width>bw-36){fz-=4;x.font='700 '+fz+'px '+SERIF}
    x.fillText(b[3],b[0]+bw/2,by+88);
    x.font='34px '+SANS;x.fillStyle=mid?'rgba(255,255,255,.9)':MUT;x.fillText(b[2],b[0]+bw/2,by+138);x.font='26px '+SANS;x.fillText(b[1],b[0]+bw/2,by+174)});
  k.foot('测测你的历史分身','长按识别二维码，看你是谁'); k.qr(inviteUrl(t));
  k.done();
}
/* 关系卡：两个人上下排（名字最长五个字，左右排放不下），中间一枚关系章 */
function pairCard(a,b,rel){
  var k=canvasKit(),x=k.x,W=k.W,fa=fam(a),fb=fam(b);
  k.txt('WE, IN HISTORY',138,'600 26px '+SANS,ACC,10);
  k.txt('我们俩在历史上是',200,'500 34px '+SANS,MUT);
  function person(t,y,f){var big=t.who.length>3;
    k.txt(t.who,y,'700 '+(big?118:140)+'px '+SERIF,INK); k.txt(t.title,y+84,'500 34px '+SERIF,f.color)}
  /* 间距放宽：名字和称号之间、两个人之间、标签和正文之间都留足；
     底下那句「你和你的朋友，又是谁和谁」跟页脚说的是一件事，删了，正文和页脚之间空出来 */
  person(a,390,fa);
  k.txt('×',580,'300 60px '+SANS,ACC);
  person(b,740,fb);
  x.font='600 38px '+SANS; var lw=x.measureText(rel.l).width+96, lx=(W-lw)/2;
  x.fillStyle=ACC;k.rrect(lx,900,lw,72,36);x.fill();
  k.txt(rel.l,950,'600 38px '+SANS,'#fff');
  var lg=rel.t.length>63; k.wrap(rel.t,1066,(lg?'34px ':'38px ')+SERIF,INK,800,lg?58:66);
  k.foot('测测你和朋友在历史上是什么关系','长按识别二维码，看我们俩'); k.qr(inviteUrl(a));
  k.done();
}
$('shotX').onclick=function(){$('shot').style.display='none'};

/* ── 32 型全览 ── */
function renderTypes(){
  var order=[['进','谋'],['进','真'],['退','谋'],['退','真']], h='<h1 class="serif" style="font-size:30px;margin:26px 0 4px">64 种历史人格</h1><p class="muted" style="margin:0">四个家族，三十二个基础型，每型再分「定」和「燃」两种。</p>';
  order.forEach(function(k){var f=D.fam[k[0]+k[1]];
    h+='<div class="fam"><h3 class="serif" style="color:'+f.color+'">'+f.name+'</h3><p class="ft">'+k[0]+' · '+k[1]+' —— '+f.tag+'</p><div class="grid">';
    T.forEach(function(t,i){if(t.code[0]===k[0]&&t.code[2]===k[1])
      var mine=saved&&scoreOf(D,saved).idx===i;
      h+='<a class="tile'+(mine?' mine':'')+'" href="'+typeHref(i)+'" style="border-color:'+(mine?f.color:f.color+'33')+'"><b>'+esc(t.who)+(mine?'<span class="me">你</span>':'')+'</b><span>'+esc(t.title)+'</span><em style="color:'+f.color+'">'+esc(t.code)+'</em></a>'});
    h+='</div></div>';});
  h+='<div class="sec"><button class="btn" id="tGo">开始测试</button></div>';
  $('types').innerHTML=h; show('types'); $('tGo').onclick=function(){ans=new Array(Q.length);cur=0;show('quiz');paintQ()};
}

/* ── 路由 ── */
function route(){
  if(location.hash==='#types'){renderTypes();return}
  if(qs.has('r')){var r=parseInt(qs.get('r'),10);if(r>=0&&r<T.length){renderType(T[r],null);return}}
  show('start');
}
window.addEventListener('hashchange',route); route();
})();
"""


def main():
    data = json.dumps(payload(), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = HTML.replace("__CSS__", CSS).replace("__JS__", JS).replace("__DATA__", data)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write(html)
    print("写好了 %s（%d KB）" % (os.path.relpath(OUT, ROOT), len(html.encode("utf-8")) // 1024))


if __name__ == "__main__":
    main()
