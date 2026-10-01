#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 ce/index.html ——「测测你的历史分身」。

    python3 scripts/build_ce.py

内容全在 seo/ce_data.py，这里只管排版和交互；改内容别改这里。
页面是纯前端的：答题、打分、出结果、出分享卡、算两个人的关系，都在浏览器里，
不收任何数据。计数走站上现成的 GA（window.gtag 在才发）。

三个入口参数：
  ?f=<n>  朋友分享来的：他测出第 n 型，你测完显示你们俩在历史上是什么关系
  ?r=<n>  直接看第 n 型的介绍（「32 型全览」里点进来的就是这个）
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


def payload():
    fam = {a + c: v for (a, c), v in D.FAMILIES.items()}
    types = []
    for t in D.TYPES:
        x = dict(t)
        x["slug"] = hw_slugs.slug_for(t["who"])
        x["story"] = {"t": t["story"][0], "u": t["story"][1]}
        types.append(x)
    kin = {k: [{"n": n, "u": "/i/%s/" % hw_slugs.slug_for(n)} for n in v]
           for k, v in D.KIN.items()}
    return {"axes": D.AXES, "dims": D.DIMS, "fam": fam, "types": types, "kin": kin,
            "qs": D.QUESTIONS, "rel": D.RELATIONS,
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
.top{display:flex;align-items:center;justify-content:space-between;font-size:13px;color:var(--muted)}
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
.faces{display:flex;flex-wrap:wrap;gap:6px;margin:26px 0 8px}
.faces span{font-size:13px;border:1px solid var(--line);border-radius:999px;padding:3px 10px;color:var(--muted)}
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
<title>测测你的历史分身 · 32 种历史人格 — 人类世界生存法则</title>
<meta name="description" content="20 道遇事题，2 分钟，测出 2600 年里和你是同一种人的那位：项羽、张良、苏轼、居里、乔布斯……32 种历史人格，每一种都链到他当年的真事。">
<meta name="robots" content="noindex">
<meta property="og:title" content="测测你的历史分身">
<meta property="og:description" content="20 道遇事题，测出 2600 年里和你是同一种人的那位。">
<meta property="og:image" content="https://ourword.ai/og.png">
<link rel="canonical" href="https://ourword.ai/ce/">
<style>__CSS__</style>
</head>
<body>
<div class="wrap">
  <div class="top"><a href="/"><span class="seal">人</span>人类世界生存法则</a><a href="#types" id="toTypes">32 型全览</a></div>

  <section id="start">
    <h1 class="serif">测测你的<br>历史分身</h1>
    <p class="sub">20 道遇事题 · 2 分钟 · 32 种历史人格</p>
    <div class="from" id="fromBox" style="display:none"></div>
    <p class="hook">遇到事的时候，你是先冲，还是先等？<br>是硬刚，还是绕过去？<br>2600 年里，总有一个人和你是同一种人。</p>
    <button class="btn" id="go">开始测试</button>
    <div class="faces" id="faces"></div>
    <p class="muted" style="font-size:13px">每一种结果，都链到那个人当年的真事。</p>
  </section>

  <section id="quiz">
    <div class="prog"><i id="bar"></i></div>
    <div class="pn"><span id="pn">1 / 20</span><span id="pax"></span></div>
    <div class="qq serif" id="qq"></div>
    <div class="opt"><small>A</small><span id="oa"></span></div>
    <div class="dots" id="dots">
      <button data-v="-2" aria-label="非常像 A"></button><button data-v="-1" aria-label="偏 A"></button><button data-v="0" aria-label="都有可能"></button><button data-v="1" aria-label="偏 B"></button><button data-v="2" aria-label="非常像 B"></button>
    </div>
    <div class="dotlab"><span>更像 A</span><span>都有可能</span><span>更像 B</span></div>
    <div class="opt"><small>B</small><span id="ob"></span></div>
    <button class="back" id="prev">← 上一题</button>
  </section>

  <section id="result"></section>
  <section id="types"></section>

  <div class="foot">人物、故事、原话，都来自 <a href="/">ourword.ai</a> 的人物库。<br>测着玩的。真遇到事了，去看他们当年是怎么处理的。</div>
</div>
<div id="shot"><img id="shotImg" alt="分享卡"><p>长按图片保存，或者</p><div class="row"><a id="shotDl" download="我的历史分身.png">下载</a><button id="shotX">关闭</button></div></div>
<div class="toast" id="toast"></div>
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
function trk(n,p){try{if(window.gtag)gtag('event',n,p||{})}catch(e){}}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function fam(t){return D.fam[t.code[0]+t.code[2]]}
function toast(m){var e=$('toast');e.textContent=m;e.classList.add('on');setTimeout(function(){e.classList.remove('on')},1800)}
function show(id){['start','quiz','result','types'].forEach(function(s){$(s).style.display=(s===id)?'block':'none'});window.scrollTo(0,0)}

/* ── 开始页 ── */
(function(){
  var f=$('faces'), pick=[9,23,30,11,4,26,13,15,16,2,22,8];
  f.innerHTML=pick.map(function(i){return '<span>'+esc(T[i].who)+'</span>'}).join('')+'<span>……</span>';
  if(fromIdx>=0){var t=T[fromIdx];
    $('fromBox').style.display='block';
    $('fromBox').innerHTML='你的朋友测出来是 <b>'+esc(t.who)+'</b>（'+esc(t.title)+'）。<br>测完看看，你们俩在历史上是什么关系。';
    trk('ce_from_open',{from:t.who});}
})();
$('go').onclick=function(){cur=0;show('quiz');paintQ();trk('ce_start',{from:fromIdx>=0?T[fromIdx].who:''})};

/* ── 答题 ── */
function paintQ(){
  var q=Q[cur];
  $('bar').style.width=(cur/Q.length*100)+'%';
  $('pn').textContent=(cur+1)+' / '+Q.length;
  $('qq').textContent=q.q; $('oa').textContent=q.a; $('ob').textContent=q.b;
  [].forEach.call($('dots').children,function(b){b.classList.toggle('on',ans[cur]!==undefined&&+b.dataset.v===ans[cur])});
  $('prev').style.visibility=cur?'visible':'hidden';
}
[].forEach.call($('dots').children,function(b){b.onclick=function(){
  ans[cur]=+b.dataset.v; paintQ();
  setTimeout(function(){ if(cur<Q.length-1){cur++;paintQ()} else finish(); },180);
}});
$('prev').onclick=function(){if(cur>0){cur--;paintQ()}};

/*SCORE-BEGIN*/
/* 打分：全部按答题现算。这一段是纯函数（只读 D 和 ans），
   scripts/check_ce.py 会把它原样抠出来放进 node 里，模拟两万个人答题，
   看 32 型是不是都抽得到、分布匀不匀 —— 判据跑的就是页面上这份代码，不是另抄一份。 */
function scoreOf(D,ans){
  var A=D.axes,Q=D.qs,DIMS=D.dims,T=D.types;
  var sum=A.map(function(){return 0}), first=A.map(function(){return 0}), tot=0;
  var raw={},mx={}; DIMS.forEach(function(d){raw[d]=0;mx[d]=0});
  Q.forEach(function(q,i){
    var v=ans[i]||0; sum[q.axis]+=v; tot+=v; if(v&&!first[q.axis])first[q.axis]=v;
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
  var code=pole.slice(0,4).join('')+'-'+pole[4];
  var idx=-1; for(var n=0;n<T.length;n++)if(T[n].code===code){idx=n;break}
  return {pct:pct,pole:pole,dims:dims,code:code,idx:idx};
}
/*SCORE-END*/
function score(){return scoreOf(D,ans)}
function match(s,t){
  var dot=0,na=0,nb=0; s.dims.forEach(function(x,i){dot+=x*t.dims[i];na+=x*x;nb+=t.dims[i]*t.dims[i]});
  var cos=(na&&nb)?dot/Math.sqrt(na*nb):0;
  var lean=0; t.code.replace('-','').split('').forEach(function(ch,i){lean+= (A[i][0]===ch?s.pct[i]:100-s.pct[i])});
  lean/=5;
  return Math.round(100*(0.5*cos+0.5*lean/100));
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
  var d=0; for(var k=0;k<4;k++)if(a.code[k]!==b.code[k])d++;
  var x=D.reld[String(d)]; return {l:x[0],t:x[1]};
}

/* ── 结果页（me 为空 = 只看这一型的介绍）── */
function isDark(){var a=document.documentElement.getAttribute('data-theme');if(a)return a==='dark';
  return window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches}
/* 家族色在深色底上要提亮：布局者的蓝灰在 #171410 上几乎看不见。混 45% 的米白进去。 */
function famCol(f){if(!isDark())return f.color;var h=f.color.slice(1),n=parseInt(h,16),
  r=n>>16,g=n>>8&255,b=n&255,mix=function(c){return Math.round(c+(234-c)*.45)};
  return 'rgb('+mix(r)+','+mix(g)+','+mix(b)+')'}
function renderType(t,me){
  var f=fam(t); document.documentElement.style.setProperty('--fam',famCol(f));
  var h='';
  var m=me?match(me,t):null;
  h+='<div class="hero"><div class="eyebrow">Your Historical Twin · 你的历史分身</div>';
  if(me)h+='<div class="pill">◆ 你的历史分身契合度 <b>'+m+'%</b> ◆</div>';
  else h+='<div class="pill">◆ 32 型之一 · '+esc(f.name)+' ◆</div>';
  h+='<div class="name serif'+(t.who.length>3?' long':'')+'">'+esc(t.who)+'</div><div class="rule"><i></i><b></b><i></i></div>';
  h+='<p class="title serif">'+esc(t.title)+'</p>';
  h+='<div class="chips"><span class="chip solid">'+esc(t.code)+'</span><span class="chip">'+esc(f.name)+' · '+esc(f.tag)+'</span></div>';
  h+='<div class="quote serif">'+esc(t.quote)+'</div><div class="qsrc">—— '+esc(t.quote_src)+'</div></div>';

  if(me){
    var order=DIMS.map(function(d,i){return [d,me.dims[i]]}).sort(function(x,y){return y[1]-x[1]});
    h+='<div class="stats"><div class="stat"><b>'+order[0][1]+'</b><span>'+order[0][0]+'</span><em>最高维度</em></div>'
      +'<div class="stat mid"><b>'+m+'%</b><span>分身契合度</span><em>'+esc(t.who)+'</em></div>'
      +'<div class="stat"><b>'+order[5][1]+'</b><span>'+order[5][0]+'</span><em>待提升</em></div></div>';
    h+='<div class="card sec"><div class="lab">五维倾向 · TRAITS</div>';
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
    h+='</div>';
  }
  h+='<div class="card sec"><div class="lab">你是这样的人 · PORTRAIT</div><div class="desc serif">'+esc(t.desc)+'</div></div>';
  h+='<div class="two sec"><div class="card"><h4>你的超能力</h4><p>'+esc(t.power)+'</p></div><div class="card"><h4>你最容易栽在</h4><p>'+esc(t.pit)+'</p></div></div>';
  h+='<div class="card sec story"><div class="lab">他当年那件事 · THE STORY</div><a href="'+t.story.u+'" data-trk="ce_to_chapter"><div class="st serif">'+esc(t.story.t)+'</div><div class="go">读'+esc(t.who)+'当年是怎么做的 →</div></a></div>';
  var kin=D.kin[t.code.split('-')[0]]||[];
  if(kin.length)h+='<div class="card sec"><div class="lab">同型名人 · ALSO THIS TYPE</div><div class="kin">'+kin.map(function(k){return '<a href="'+k.u+'">'+esc(k.n)+'</a>'}).join('')+'<a href="/i/'+t.slug+'/">'+esc(t.who)+'的全部篇章 →</a></div></div>';

  if(me&&fromIdx>=0){var fr=T[fromIdx],rel=relation(t,fr);
    h+='<div class="rel sec"><div class="eyebrow" style="color:var(--acc)">你和朋友在历史上是</div><div class="pair serif">'+esc(t.who)+' × '+esc(fr.who)+'</div><span class="rl">'+esc(rel.l)+'</span><p>'+esc(rel.t)+'</p></div>';
    trk('ce_pair',{me:t.who,friend:fr.who,rel:rel.l});
  }
  if(me){
    h+='<div class="card sec ask"><div class="lab">问问'+esc(t.who)+' · ASK</div><p class="muted" style="margin:0 0 10px;font-size:14px">说说你最近遇到的一件事，看看'+esc(t.who)+'会怎么处理。</p><textarea id="askIn" placeholder="比如：老板天天改需求，我手上三件事都做不完"></textarea><button class="btn" id="askGo">问'+esc(t.who)+'</button></div>';
    h+='<div class="sec"><button class="btn" id="shareCard">生成我的分享卡</button><button class="btn ghost" id="invite">叫朋友来测，看你们是什么关系</button><button class="btn ghost" id="again">重新测一次</button></div>';
  }else{
    h+='<div class="sec"><button class="btn" id="tryIt">测测你是不是'+esc(t.who)+'</button><a class="btn ghost" href="#types">看全部 32 型</a></div>';
  }
  $('result').innerHTML=h; show('result');
  [].forEach.call(document.querySelectorAll('[data-trk]'),function(a){a.onclick=function(){trk(a.dataset.trk,{who:t.who})}});
  if(me){
    $('again').onclick=function(){ans=new Array(Q.length);cur=0;show('quiz');paintQ()};
    $('askGo').onclick=function(){var v=($('askIn').value||'').trim()||'我最近遇到一件事，不知道怎么办';
      trk('ce_ask',{who:t.who});
      if(typeof window.hwAsk==='function')window.hwAsk(v+'（我测出来是'+t.who+'那一型，想听听'+t.who+'会怎么处理）',{pin:[t.story.u],scene:''});
      else location.href=t.story.u;};
    $('shareCard').onclick=function(){trk('ce_share_card',{who:t.who});card(t,me,m)};
    $('invite').onclick=function(){
      var url=location.origin+location.pathname+'?f='+T.indexOf(t);
      var txt='我测出来是'+t.who+'（'+t.title+'）。你遇事像历史上的谁？测完看看我们俩是什么关系：';
      trk('ce_invite',{who:t.who});
      if(navigator.share){navigator.share({title:'测测你的历史分身',text:txt,url:url}).catch(function(){})}
      else if(navigator.clipboard){navigator.clipboard.writeText(txt+' '+url).then(function(){toast('链接已复制，发给朋友吧')})}
      else prompt('复制这个链接发给朋友：',url);
    };
  }else{ $('tryIt').onclick=function(){fromIdx=-1;ans=new Array(Q.length);cur=0;show('quiz');paintQ()}; }
}
function finish(){
  var s=score(); if(s.idx<0){s.idx=0}
  var t=T[s.idx];
  try{history.replaceState(null,'',location.pathname+(fromIdx>=0?'?f='+fromIdx:''))}catch(e){}
  trk('ce_done',{who:t.who,code:t.code});
  renderType(t,s);
}

/* ── 分享卡：3:4，给小红书用。图上只放名字、原型、金句和三个数 ── */
function card(t,me,m){
  var c=document.createElement('canvas'),W=1080,H=1440; c.width=W;c.height=H;
  var x=c.getContext('2d'), f=fam(t), dark=false;
  var P='#f5f1e8',CARD='#faf7f0',INK='#1f1c17',MUT='#8a8377',LINE='#d8d2c6',SERIF='"Noto Serif SC","Songti SC","STSong",serif',SANS='-apple-system,"PingFang SC","Microsoft YaHei",sans-serif';
  x.fillStyle=P;x.fillRect(0,0,W,H);
  x.strokeStyle=LINE;x.lineWidth=3;x.strokeRect(36,36,W-72,H-72);
  function txt(s,y,font,col,al,ls){x.font=font;x.fillStyle=col;x.textAlign=al||'center';
    if(ls){var w=0,ch=s.split('');ch.forEach(function(k){w+=x.measureText(k).width+ls});var sx=W/2-w/2;x.textAlign='left';ch.forEach(function(k){x.fillText(k,sx,y);sx+=x.measureText(k).width+ls})}
    else x.fillText(s,W/2,y)}
  function wrap(s,y,font,col,maxw,lh){x.font=font;x.fillStyle=col;x.textAlign='center';var line='',lines=[];
    s.split('').forEach(function(ch){if(x.measureText(line+ch).width>maxw){lines.push(line);line=ch}else line+=ch});lines.push(line);
    lines.forEach(function(l,i){x.fillText(l,W/2,y+i*lh)});return y+lines.length*lh}
  txt('YOUR HISTORICAL TWIN',138,'600 26px '+SANS,f.color,'center',10);
  x.strokeStyle=f.color;x.lineWidth=3;var pw=560,ph=78,px=(W-pw)/2,py=180;x.beginPath();x.moveTo(px+ph/2,py);x.arcTo(px+pw,py,px+pw,py+ph,ph/2);x.arcTo(px+pw,py+ph,px,py+ph,ph/2);x.arcTo(px,py+ph,px,py,ph/2);x.arcTo(px,py,px+pw,py,ph/2);x.stroke();
  txt('你的历史分身契合度  '+m+'%',py+51,'500 34px '+SANS,f.color);
  txt(t.who,t.who.length>3?470:500,'700 '+(t.who.length>3?150:190)+'px '+SERIF,INK);
  x.fillStyle=f.color;x.fillRect(W/2-170,548,120,5);x.fillRect(W/2+50,548,120,5);x.beginPath();x.arc(W/2,550,10,0,7);x.fill();
  txt(t.title,640,'600 54px '+SERIF,INK);
  txt(t.code+'  ·  '+f.name,712,'500 34px '+SANS,f.color);
  var y=wrap('“'+t.quote+'”',812,'italic 44px '+SERIF,INK,820,68);
  txt('—— '+t.quote_src,y+6,'28px '+SANS,MUT);
  var order=DIMS.map(function(d,i){return [d,me.dims[i]]}).sort(function(a,b){return b[1]-a[1]});
  var bx=[[100,'最高维度',order[0][0],String(order[0][1])],[400,'分身契合度',t.who,m+'%'],[700,'待提升',order[5][0],String(order[5][1])]];
  bx.forEach(function(b,i){var bw=280,bh=210,by=1010,mid=i===1;x.fillStyle=mid?f.color:CARD;x.strokeStyle=mid?f.color:LINE;x.lineWidth=3;
    x.beginPath();x.moveTo(b[0]+24,by);x.arcTo(b[0]+bw,by,b[0]+bw,by+bh,24);x.arcTo(b[0]+bw,by+bh,b[0],by+bh,24);x.arcTo(b[0],by+bh,b[0],by,24);x.arcTo(b[0],by,b[0]+bw,by,24);x.closePath();x.fill();x.stroke();
    x.textAlign='center';x.fillStyle=mid?'#fff':INK;x.font='700 72px '+SERIF;x.fillText(b[3],b[0]+bw/2,by+100);
    x.font='34px '+SANS;x.fillStyle=mid?'rgba(255,255,255,.9)':MUT;x.fillText(b[2],b[0]+bw/2,by+150);x.font='26px '+SANS;x.fillText(b[1],b[0]+bw/2,by+190)});
  x.fillStyle='#a33b2e';x.fillRect(110,1290,74,74);x.fillStyle='#fff';x.font='700 48px '+SERIF;x.textAlign='center';x.fillText('人',147,1345);
  x.textAlign='left';x.fillStyle=INK;x.font='600 36px '+SANS;x.fillText('测测你的历史分身',212,1322);
  x.fillStyle=MUT;x.font='28px '+SANS;x.fillText('ourword.ai/ce · 32 种历史人格',212,1362);
  var url=c.toDataURL('image/png'); $('shotImg').src=url; $('shotDl').href=url; $('shot').style.display='flex';
}
$('shotX').onclick=function(){$('shot').style.display='none'};

/* ── 32 型全览 ── */
function renderTypes(){
  var order=[['进','谋'],['进','真'],['退','谋'],['退','真']], h='<h1 class="serif" style="font-size:30px;margin:26px 0 4px">32 种历史人格</h1><p class="muted" style="margin:0">四个家族，十六个基础型，每型分「定」和「燃」两种。</p>';
  order.forEach(function(k){var f=D.fam[k[0]+k[1]];
    h+='<div class="fam"><h3 class="serif" style="color:'+f.color+'">'+f.name+'</h3><p class="ft">'+k[0]+' · '+k[1]+' —— '+f.tag+'</p><div class="grid">';
    T.forEach(function(t,i){if(t.code[0]===k[0]&&t.code[2]===k[1])
      h+='<a class="tile" href="?r='+i+'" style="border-color:'+f.color+'33"><b>'+esc(t.who)+'</b><span>'+esc(t.title)+'</span><em style="color:'+f.color+'">'+esc(t.code)+'</em></a>'});
    h+='</div></div>';});
  h+='<div class="sec"><button class="btn" id="tGo">开始测试</button></div>';
  $('types').innerHTML=h; show('types'); $('tGo').onclick=function(){cur=0;show('quiz');paintQ()};
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
