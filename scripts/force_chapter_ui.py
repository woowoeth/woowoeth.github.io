#!/usr/bin/env python3
# Patch generators AND already-built HTML so highlight/sidebar cannot miss.
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STYLE = (
    '<style id="hw-force">'
    'mark,mark.hl{background:transparent!important;color:#9d2933!important;'
    'font-weight:700!important;text-decoration:underline!important;'
    'text-decoration-color:#9d2933!important;text-underline-offset:.16em;'
    'text-decoration-thickness:1.5px}'
    '@media (max-width:900px){aside.side{display:none!important}'
    '.layout{grid-template-columns:1fr!important}}'
    '</style>'
)
MARK_OPEN = (
    '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700;'
    'text-decoration:underline;text-decoration-color:#9d2933;text-underline-offset:.16em;'
    'text-decoration-thickness:1.5px">'
)

def patch_html():
    n = 0
    for path in (ROOT / "i").rglob("index.html") if (ROOT / "i").exists() else []:
        s = path.read_text(encoding="utf-8")
        # Legacy CJK-slug stubs are meta-refresh redirects rewritten byte-for-byte
        # by write_legacy_redirects on every build. Touching them here makes the two
        # scripts fight and produces a fresh commit every single run.
        if 'http-equiv="refresh"' in s:
            continue
        orig = s
        if 'id="hw-force"' not in s:
            s = s.replace("</head>", STYLE + "</head>", 1)
        s = re.sub(r"<mark class=\"hl\"(?: style=\"[^\"]*\")?>", MARK_OPEN, s)
        if s != orig:
            path.write_text(s, encoding="utf-8")
            n += 1
    print("force_chapter_ui html", n)

if __name__ == "__main__":
    patch_html()

# ---------------- HWX v2: 首页「按处境找 + 双列人物流」 ----------------
# v2 依用户反馈：人物入口改小红书式双列卡（名 + 身份一句话 + 钩子句，整卡可点），
# 卡上不再放章节标签（章节直达走处境区和搜索）；新增类别筛选；处境结果附钩子；
# 处境标签在手机上单行横滑。数据每次构建自 hw_chapters 再生，场景引用构建期校验。
HWX_A, HWX_B = "<!--HWX:FIND-->", "<!--/HWX:FIND-->"

HWX_SCENES = [
    ("要做不可逆的决定", [("caesar","the-rubicon"),("li-ka-shing","knowing-when-to-stop"),("graham","margin-of-safety"),("han-xin","back-to-the-river"),("xiang-yu","sinking-the-boats"),("schelling","binding-yourself")]),
    ("对手比我强", [("napoleon","decisive-point"),("mao","on-protracted-war"),("sun-tzu","form-like-water"),("musashi","no-favorite-weapon"),("li-bi","strike-the-base"),("boyd","ooda")]),
    ("我对，但被否了", [("su-yu","daring-to-state"),("thiel","the-contrarian-question"),("marks","second-level-thinking"),("franklin","never-say-certainly"),("boyd","to-be-or-to-do")]),
    ("连胜，要不要加码", [("art-of-worldly-wisdom","quit-while-winning"),("bismarck","art-of-the-possible"),("buffett","swimming-naked"),("taleb","turkey-problem"),("napoleon","sublime-to-ridiculous"),("zhang-liang","asking-for-less")]),
    ("亏着，砍还是扛", [("livermore","hope-and-fear-inverted"),("livermore","sitting-tight"),("grove","revolving-door"),("huang","strategic-retreat"),("thinking-fast-and-slow","loss-aversion"),("lynch","stomach-not-brain")]),
    ("情绪上头", [("epictetus","judgments-not-things"),("su-shi","no-wind-no-rain"),("zhang-yiming","ordinary-mind"),("marcus-aurelius","morning-preparation"),("zhang-liang","picking-up-the-shoe")]),
    ("谈判与说服", [("schelling","focal-points"),("influence","reciprocity"),("wealth-of-nations","not-benevolence"),("guiguzi","listen-in-reverse"),("caesar","clementia"),("gandhi","salt-march")]),
    ("团队老出同样的问题", [("thinking-in-systems","structure-drives-behavior"),("han-feizi","not-counting-on-goodness"),("grove","inflection-and-cassandras"),("dalio","believability"),("shang-yang","moving-the-pole"),("zhuge-liang","executing-ma-su")]),
    ("看不清方向", [("marks","taking-the-temperature"),("einstein","formulating-the-problem"),("mao","on-contradiction"),("wang-xing","core-not-boundary"),("tao-te-ching","reversal"),("huang","zero-billion-markets")]),
    ("从零开始一件事", [("paul-graham","dont-scale"),("zhu-yuanzhang","delay-the-title"),("thiel","competition-is-for-losers"),("matsushita","tap-water"),("naval","productize-yourself"),("duan-yongping","dare-to-be-last"),("lee-kuan-yew","does-it-work")]),
    ("投资不亏大钱", [("graham","mr-market"),("buffett","circle-of-competence"),("munger","invert"),("taleb","skin-in-the-game"),("lynch","tenbagger-at-the-mall"),("bai-gui","take-what-others-drop")]),
    ("看人与防骗", [("analects","see-how"),("zeng-guofan","recruit-and-test"),("zizhi-tongjian","talent-and-virtue"),("strategies-of-the-warring-states","three-mirrors"),("la-rochefoucauld","memory-vs-judgment"),("crowd","assert-repeat-contaminate"),("influence","social-proof")]),
    ("在低谷", [("frankl","the-last-freedom"),("dalio","pain-plus-reflection"),("nietzsche","what-does-not-kill"),("su-shi","three-exiles"),("marcus-aurelius","obstacle-is-the-way")]),
    ("忙，但心虚", [("wang-xing","escape-from-thinking"),("jobs","focus-is-saying-no"),("drucker","right-things-first"),("bezos","what-wont-change"),("franklin","one-virtue-a-week")]),
    ("交班与退场", [("fan-li","leave-at-the-top"),("lee-kuan-yew","from-my-sickbed"),("guo-ziyi","open-gates"),("wang-jian","asking-for-fields"),("li-bi","no-office")]),
]

def _hwx_payload():
    import json, sys as _s
    _s.path.insert(0, "seo")
    import hw_chapters as C, hw_slugs, build_seo
    ch_by, line_by = {}, {}
    for ch in C.CHAPTERS:
        ch_by.setdefault(ch["parent"], []).append((ch["k"], ch["n"], ch["w"]))
    for pname, spec in C.PARENTS.items():
        for it in spec.get("items", []):
            line_by[(pname, it["k"])] = it.get("line", "")
    E = []
    for e in build_seo.load_array():
        slug = hw_slugs.slug_for(e["n"])
        chs = ch_by.get(e["n"], [])
        hook = ""
        for k, _n, _w in chs:
            hook = line_by.get((e["n"], k), "")
            if hook: break
        E.append({"n": e["n"], "s": slug, "c": e["c"], "w": e["w"], "hk": hook,
                  "h": [[k, n, w, line_by.get((e["n"], k), "")] for k, n, w in chs]})
    valid = {(x["s"], k) for x in E for k, _, _, _ in x["h"]}
    for t, refs in HWX_SCENES:
        for s_, k_ in refs:
            assert (s_, k_) in valid, "HWX 场景引用不存在: %s/%s (%s)" % (s_, k_, t)
    S = [{"t": t, "r": [list(r) for r in refs]} for t, refs in HWX_SCENES]
    j = json.dumps({"E": E, "S": S}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return j, len(E), sum(len(x["h"]) for x in E)

def hwx_block():
    j, ne, nc = _hwx_payload()
    css = """
#hwx{margin:24px 0 8px}
#hwx .hwx-h{font-size:15px;letter-spacing:.12em;color:var(--muted,#8a8377);margin:0 0 10px;font-weight:600}
#hwx .hwx-sc{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:8px}
#hwx .hwx-sc button{border:1px solid var(--line,#d8d2c6);background:transparent;color:inherit;border-radius:999px;padding:6px 13px;font-size:13.5px;cursor:pointer;line-height:1.6;white-space:nowrap}
#hwx .hwx-sc button.on{background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8);border-color:var(--ink,#1f1c17)}
@media(max-width:640px){#hwx .hwx-sc{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding-bottom:2px}#hwx .hwx-sc::-webkit-scrollbar{display:none}}
#hwx .hwx-res{display:none;border-left:3px solid var(--acc,#a33b2e);padding:6px 0 6px 14px;margin:10px 0 16px}
#hwx .hwx-res.on{display:block}
#hwx .hwx-res a{display:block;padding:6px 0;text-decoration:none;color:inherit}
#hwx .hwx-res a b{font-weight:600;font-size:14.5px}
#hwx .hwx-res a .hk{display:block;color:var(--muted,#8a8377);font-size:13px;line-height:1.6;margin-top:1px}
#hwx .hwx-res a:hover b{border-bottom:1px solid currentColor}
#hwx .hwx-bar{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin:20px 0 8px;flex-wrap:wrap}
#hwx .hwx-cat{display:flex;flex-wrap:wrap;gap:6px}
#hwx .hwx-cat button{border:none;background:transparent;color:var(--muted,#8a8377);font-size:12.5px;cursor:pointer;padding:3px 8px;border-radius:999px;line-height:1.5}
#hwx .hwx-cat button.on{background:var(--line,#d8d2c6);color:var(--ink,#1f1c17)}
@media(max-width:640px){#hwx .hwx-cat{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;max-width:100%}#hwx .hwx-cat::-webkit-scrollbar{display:none}#hwx .hwx-cat button{white-space:nowrap}}
#hwx .hwx-feed{display:grid;grid-template-columns:repeat(auto-fill,minmax(158px,1fr));gap:10px}
#hwx .hwx-card{display:flex;flex-direction:column;border:1px solid var(--line,#d8d2c6);border-radius:14px;padding:13px 14px 11px;text-decoration:none;color:inherit;background:transparent;transition:border-color .15s}
#hwx .hwx-card:hover{border-color:var(--acc,#a33b2e)}
#hwx .hwx-card b{font-size:15.5px;line-height:1.4}
#hwx .hwx-card .cw{font-size:12px;color:var(--muted,#8a8377);margin:3px 0 8px;line-height:1.5}
#hwx .hwx-card .hk{font-size:13px;line-height:1.7;flex:1}
#hwx .hwx-card .hk::before{content:"「"}#hwx .hwx-card .hk::after{content:"」"}
#hwx .hwx-card .cf{font-size:11.5px;color:var(--acc,#a33b2e);margin-top:9px}
#hwx .hwx-more{margin-top:12px;font-size:13px;color:var(--muted,#8a8377)}
#hwx .hwx-hide{display:none!important}
""".strip()
    js = """
(function(){
var D=HWXD, q=document.getElementById('q');
var scWrap=document.getElementById('hwx-sc'), res=document.getElementById('hwx-res');
var feed=document.getElementById('hwx-feed'), catWrap=document.getElementById('hwx-cat');
var byS={}; D.E.forEach(function(e){byS[e.s]=e});
D.S.forEach(function(s){
  var b=document.createElement('button'); b.type='button'; b.textContent=s.t;
  b.onclick=function(){
    var on=b.classList.contains('on');
    scWrap.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});
    if(on){res.classList.remove('on');res.innerHTML='';return}
    b.classList.add('on');
    res.innerHTML=s.r.map(function(r){
      var e=byS[r[0]], ch=e.h.filter(function(h){return h[0]===r[1]})[0];
      var hint=ch[3]||ch[2];
      return '<a href="/i/'+r[0]+'/'+r[1]+'/"><b>'+e.n+' · '+ch[1]+'</b><span class="hk">'+hint+'</span></a>';
    }).join('');
    res.classList.add('on');
  };
  scWrap.appendChild(b);
});
var CAT='全部', cats=['全部'];
D.E.forEach(function(e){if(cats.indexOf(e.c)<0)cats.push(e.c)});
cats.forEach(function(c){
  var b=document.createElement('button'); b.type='button'; b.textContent=c;
  if(c===CAT)b.classList.add('on');
  b.onclick=function(){CAT=c;catWrap.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x.textContent===c)});apply()};
  catWrap.appendChild(b);
});
feed.innerHTML=D.E.map(function(e){
  var t=(e.n+' '+e.w+' '+e.c+' '+e.hk+' '+e.h.map(function(h){return h[1]+' '+h[2]+' '+h[3]}).join(' ')).toLowerCase().replace(/"/g,'');
  return '<a class="hwx-card" href="/i/'+e.s+'/" data-c="'+e.c+'" data-t="'+t+'"><b>'+e.n+'</b><span class="cw">'+e.w+'</span><span class="hk">'+(e.hk||e.w)+'</span><span class="cf">'+e.h.length+' 篇深度阅读 →</span></a>';
}).join('');
function apply(){
  var v=q?q.value.trim().toLowerCase():'';
  feed.querySelectorAll('.hwx-card').forEach(function(c){
    var ok=(CAT==='全部'||c.getAttribute('data-c')===CAT)&&(!v||c.getAttribute('data-t').indexOf(v)>=0);
    c.classList.toggle('hwx-hide',!ok);
  });
}
if(q){q.setAttribute('placeholder','搜索：人物、书、一句话、章节、处境…');q.addEventListener('input',apply);}
})();
""".strip()
    return (HWX_A + "\n<section id=\"hwx\" aria-label=\"按处境找\">"
            "<div class=\"hwx-h\">按处境找 ——「我现在遇到的是……」</div>"
            "<div class=\"hwx-sc\" id=\"hwx-sc\"></div><div class=\"hwx-res\" id=\"hwx-res\"></div>"
            "<div class=\"hwx-bar\"><div class=\"hwx-h\" style=\"margin:0\">全部 " + str(ne) + " 个入口</div>"
            "<div class=\"hwx-cat\" id=\"hwx-cat\"></div></div>"
            "<div class=\"hwx-feed\" id=\"hwx-feed\"></div>"
            "<div class=\"hwx-more\">共 " + str(nc) + " 篇深度阅读。按时间浏览请见下方年表。</div>"
            "<style>" + css + "</style>"
            "<script>var HWXD=" + j + ";</script><script>" + js + "</script>"
            "</section>\n" + HWX_B)

def patch_home_discover():
    import re
    p = "index.html"
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"\n*" + re.escape(HWX_A) + r".*?" + re.escape(HWX_B) + r"\n*", "", s, flags=re.S)
    anchor = '<div class="tabs" id="tabs"'
    assert anchor in s, "HWX 锚点丢失：首页结构变了"
    s = s.replace(anchor, "\n" + hwx_block() + "\n" + anchor, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("HWX v2 首页发现层已注入")

patch_home_discover()
