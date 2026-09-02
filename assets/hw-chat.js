/* 悬浮球问答 · 人类世界生存法则
 *
 * 视觉按 DESIGN.md：正文 17px/1.78 对齐章节页的 17px/1.75（聊天也是阅读面，
 * 没道理比正文小）、朱红是全站唯一强调色、无阴影、层次靠底色与 1px 细线、
 * 标题宋体正文黑体、触控目标 ≥32px、深色模式三套变量都要顾到。
 *
 * 检索不走 llms-full.txt（1.4MB）。索引里有 308 篇章节和 428 条处境问题；
 * 那些问题本来就是第一人称口语，跟用户描述处境的说法同源，是最好的匹配信号。
 * 索引 249KB(gzip)，所以点开才加载，不进首屏。
 *
 * 后端：window.HW_CHAT_ENDPOINT。key 永远不进浏览器——
 * 本地 demo 走 scripts/chat_dev_proxy.py，线上要走 Cloudflare Worker。
 */
(function () {
  'use strict';
  if (window.__hwChat) return;
  window.__hwChat = 1;

  // 端点由构建时注入。为空说明 Worker 还没部署——什么都不渲染，
  // 宁可没有这个功能，也不要让人点开一个连不上的窗口。
  var ENDPOINT = window.HW_CHAT_ENDPOINT || '';
  if (!ENDPOINT) return;
  var DAILY_LIMIT = 5;
  var LS_KEY = 'hw-chat-quota';
  /* 聊天记录存 localStorage。
     一开始用的是 sessionStorage——理由是这里存的是人描述自己的处境，
     不该在设备上留到下次打开浏览器。但那是我的判断不是用户的需求：
     关掉标签页再回来记录就没了，被反映了两次。改成 localStorage，
     关浏览器也在。只留最近 20 轮，且每轮只存问题、答案和引用链接，
     不存喂给模型的正文。 */
  /* 聊天记录：本地留着，关浏览器再打开也在。
     原来卡 20 条上限——那是按条数砍，砍掉的可能是上周最要紧的那次。
     改成按时间：只丢 7 天前的，7 天内不管多少条都留。
     另有一个条数上限只为兜住 localStorage 的容量，不是产品规则。 */
  var HIST_KEY = 'hw-chat-log';
  var HIST_DAYS = 7;
  var HIST_HARD_MAX = 200;      /* 纯粹防 localStorage 撑爆，正常人到不了 */

  function fresh(a) {
    var cut = Date.now() - HIST_DAYS * 864e5;
    return a.filter(function (x) { return !x.ts || x.ts >= cut; });
  }
  function loadHist() {
    try {
      var a = JSON.parse(localStorage.getItem(HIST_KEY) || '[]');
      if (!a.length) return [];
      var f = fresh(a);
      if (f.length !== a.length) saveHist(f);      /* 顺手把过期的落盘清掉 */
      return f;
    } catch (e) { return []; }
  }
  function saveHist(h) {
    var keep = fresh(h).slice(-HIST_HARD_MAX);
    try { localStorage.setItem(HIST_KEY, JSON.stringify(keep)); }
    catch (e) {
      /* 满了就丢最旧的一半再试一次，别让一次写失败把整段记录卡死 */
      try { localStorage.setItem(HIST_KEY, JSON.stringify(keep.slice(-Math.ceil(keep.length / 2)))); }
      catch (e2) {}
    }
  }

  /* ---------- 每日额度（前端只是提示，真正的限流必须在服务端） ---------- */
  function today() { var d = new Date(); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
  function quota() {
    try {
      var raw = JSON.parse(localStorage.getItem(LS_KEY) || '{}');
      if (raw.d !== today()) return { d: today(), n: 0 };
      return { d: raw.d, n: raw.n || 0 };
    } catch (e) { return { d: today(), n: 0 }; }
  }
  function useOne() {
    var q = quota(); q.n += 1;
    try { localStorage.setItem(LS_KEY, JSON.stringify(q)); } catch (e) {}
    return q.n;
  }
  function left() { return Math.max(0, DAILY_LIMIT - quota().n); }

  /* ---------- 样式 ---------- */
  var CSS = [
    '#hwq-ball{position:fixed;right:18px;bottom:18px;z-index:9998;width:52px;height:52px;',
    'border-radius:50%;background:var(--acc,#a33b2e);color:#fff;border:none;cursor:pointer;',
    'font-family:"Noto Serif SC","Songti SC","STSong",serif;font-size:21px;font-weight:700;',
    'line-height:52px;padding:0;transition:transform .15s ease}',
    '#hwq-ball:hover{transform:scale(1.06)}',
    '#hwq-ball[hidden]{display:none}',

    /* 全屏，而不是右下角的小弹窗——弹窗在手机上又窄又挤。
       但背景铺满、正文列限宽 680px 居中：桌面上让文字横贯 1280px，
       一行五六十字，比弹窗更难读（章节页桌面也是 32 字一行）。 */
    '#hwq-panel{position:fixed;inset:0;z-index:9999;display:flex;flex-direction:column;',
    'background:var(--paper,#f5f1e8)}',
    '#hwq-panel[hidden]{display:none}',
    /* 背板。真机读数（scrollY 3186、panel t0 而屏幕顶端仍有页面内容）说明
       fixed 坐标系的 0 不在屏幕顶端——屏幕顶端是负坐标。所以 top:0 的背板
       够不着上面那一半，之前一直没挡住。改成从 -150vh 起、总高 400vh，
       上下都留足余量。它只是一块纯色，不花什么钱。 */
    '#hwq-back{position:fixed;left:0;top:-150vh;width:100%;height:400vh;z-index:9997;',
    'background:var(--paper,#f5f1e8)}',
    '#hwq-back[hidden]{display:none}',
    '#hwq-dbg{position:fixed;left:0;top:0;z-index:10000;background:rgba(0,0,0,.82);color:#0f0;',
    'font:11px/1.45 ui-monospace,Menlo,monospace;padding:6px 8px;white-space:pre;pointer-events:none}',
    '.hwq-col{width:100%;max-width:680px;margin:0 auto;padding:0 20px;box-sizing:border-box}',

    '#hwq-head{flex:0 0 auto;border-bottom:1px solid var(--line,#d8d2c6)}',
    '#hwq-head .hwq-col{display:flex;align-items:baseline;gap:8px;padding-top:16px;padding-bottom:13px}',
    '#hwq-head b{font-family:"Noto Serif SC","Songti SC",serif;font-size:21px;font-weight:700;color:var(--ink,#1f1c17)}',
    '#hwq-head span{font-size:13px;color:var(--muted,#8a8377);margin-left:auto}',
    '#hwq-close{border:none;background:transparent;color:var(--muted,#8a8377);font-size:26px;',
    'line-height:1;cursor:pointer;padding:0 4px;margin-left:8px;min-width:32px;min-height:32px}',

    '#hwq-log{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch}',
    '#hwq-log .hwq-col{display:flex;flex-direction:column;gap:14px;padding-top:18px;padding-bottom:18px}',
    '.hwq-m{max-width:88%;font-size:17px;line-height:1.78;border-radius:12px;padding:10px 12px;white-space:pre-wrap}',
    '.hwq-me{align-self:flex-end;background:var(--paper2,#eee8da);color:var(--ink,#1f1c17)}',
    '.hwq-ai{align-self:flex-start;background:var(--card,#faf7f0);border:1px solid var(--line,#d8d2c6);color:var(--ink,#1f1c17)}',
    '.hwq-hint{align-self:center;font-size:13.5px;color:var(--muted,#8a8377);line-height:1.7;text-align:center}',
    /* 引用行内跟在句子后面，不攒到最后——读者在读到那句时就能点过去。
       只写章节名不写人名：人名在落地页第一眼就有，行内每处多六个字太吵。 */
    '.hwq-h{font-weight:700}',
    /* 必须带 #hwq-panel 前缀。站上有条 :root[data-theme="dark"] … a 的规则
       （优先级 0,2,1）会把链接压成正文色——实测 .hwq-cite(0,1,0) 输，
       连 a.hwq-cite(0,1,1) 也输，#hwq-panel .hwq-cite(1,1,0) 才赢。
       用提高优先级而不是 !important：DESIGN.md 里记着这个站已经被
       !important 坑过一次，不该再加一条。
       悬浮球从只在首页扩到全站 467 页之后才暴露——首页没有那条规则。 */
    '#hwq-panel .hwq-cite{color:var(--acc,#a33b2e);text-decoration:none;font-size:13.5px;',
    'white-space:nowrap;margin-left:4px;vertical-align:baseline}',
    '#hwq-panel .hwq-cite:hover{opacity:.7}',

    '#hwq-foot{flex:0 0 auto;border-top:1px solid var(--line,#d8d2c6);padding-bottom:env(safe-area-inset-bottom)}',
    '#hwq-foot .hwq-col{display:flex;gap:10px;align-items:flex-end;padding-top:12px;padding-bottom:12px}',
    '#hwq-in{flex:1;resize:none;border:1px solid var(--line,#d8d2c6);border-radius:999px;background:transparent;',
    'color:var(--ink,#1f1c17);font-family:inherit;font-size:17px;line-height:1.55;padding:10px 16px;max-height:88px;outline:none}',
    '#hwq-in:focus{border-color:var(--muted,#8a8377)}',
    '#hwq-send{flex:0 0 auto;border:none;border-radius:999px;background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8);',
    'font-family:inherit;font-size:15.5px;padding:11px 18px;cursor:pointer;min-height:36px}',
    '#hwq-send:disabled{opacity:.45;cursor:default}',

    /* 开场白。原先没有，是想错了：标题「你遇到什么事了？」只说了怎么问，
       没说能问什么——新来的人分不清这是站内搜索、客服，还是通用聊天。 */
    '#hwq-intro{align-self:stretch;padding-top:4px}',
    '#hwq-intro p{margin:0;font-size:15px;line-height:1.8;color:var(--muted,#8a8377);text-align:left}',

    ':root[data-theme="dark"] .hwq-ai{background:#1d1913}',
    ':root[data-theme="dark"] .hwq-me{background:#201c15}',
    '@media(max-width:480px){.hwq-col{padding:0 16px}#hwq-ball{right:14px;bottom:14px}}'
  ].join('');

  var st = document.createElement('style');
  st.id = 'hwq-style'; st.textContent = CSS;
  document.head.appendChild(st);

  /* ---------- DOM ---------- */
  var ball = document.createElement('button');
  ball.id = 'hwq-ball'; ball.type = 'button';
  ball.textContent = '问';
  ball.setAttribute('aria-label', '遇到事了？问一问');

  var panel = document.createElement('div');
  panel.id = 'hwq-panel'; panel.hidden = true;
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', '问一问');
  panel.innerHTML =
    '<div id="hwq-head"><div class="hwq-col"><b>你遇到什么事了？</b>' +
    '<span id="hwq-left"></span><button id="hwq-close" type="button" aria-label="关闭">×</button></div></div>' +
    '<div id="hwq-log"><div class="hwq-col" id="hwq-logc"></div></div>' +
    '<div id="hwq-foot"><div class="hwq-col">' +
    '<textarea id="hwq-in" rows="1" placeholder="说说看……"></textarea>' +
    '<button id="hwq-send" type="button">发送</button></div></div>';

  var back = document.createElement('div');
  back.id = 'hwq-back'; back.hidden = true;
  back.setAttribute('aria-hidden', 'true');

  document.body.appendChild(ball);
  document.body.appendChild(back);
  document.body.appendChild(panel);

  var log = panel.querySelector('#hwq-logc');       /* 消息进限宽的列里 */
  var scroller = panel.querySelector('#hwq-log');  /* 滚动的是外层 */
  var input = panel.querySelector('#hwq-in');
  var send = panel.querySelector('#hwq-send');
  var leftEl = panel.querySelector('#hwq-left');

  function say(kind, text) {
    var d = document.createElement('div');
    d.className = 'hwq-m hwq-' + kind;
    d.textContent = text;
    log.appendChild(d);
    scroller.scrollTop = scroller.scrollHeight;
    return d;
  }
  function hint(text) {
    var d = document.createElement('div');
    d.className = 'hwq-hint'; d.textContent = text;
    log.appendChild(d); scroller.scrollTop = scroller.scrollHeight;
  }
  function showIntro() {
    if (log.children.length) return;
    var box = document.createElement('div');
    box.id = 'hwq-intro';
    var p = document.createElement('p');
    p.textContent = '工作、家里、钱、身体，或者说不出口的那些，都可以说。说得越具体，越容易找到真的对得上的人。';
    box.appendChild(p);
    log.appendChild(box);
  }
  function dropIntro() {
    var i = log.querySelector('#hwq-intro');
    if (i) i.parentNode.removeChild(i);
  }

  /* 只留渲染引用要用的三个字段：正文 txt 一篇 700 字，八篇存进去太浪费。 */
  function slimHits(hits) {
    return hits.map(function (c) { return { u: c.u, p: c.p, n: c.n }; });
  }
  var restored = false;
  function restoreHist() {
    if (restored) return;
    restored = true;
    loadHist().forEach(function (t) {
      say('me', t.q);
      var d = document.createElement('div');
      d.className = 'hwq-m hwq-ai';
      log.appendChild(d);
      renderAnswer(d, t.a, t.hits || []);
    });
    scroller.scrollTop = scroller.scrollHeight;
  }

  function refreshLeft() {
    var n = left();
    leftEl.textContent = '今天还能问 ' + n + ' 次';
    send.disabled = n <= 0;
    input.placeholder = n > 0 ? '说说看……' : '今天的 5 次用完了，明天再来';
  }

  /* 把模型写的 [0] 换成行内出处链接。
     全程只用 createTextNode 与 createElement——模型输出一律当不可信文本，
     绝不 innerHTML 拼进去。 */
  function renderAnswer(el, text, hits) {
    el.textContent = '';
    /* 中文之间的空格去掉。模型爱写「先看最近一次。 你最近一次……」——
       句号后面多一个半角空格，中文排版里那是个洞。
       只在「前后都是中文（或中文标点）」时去：AI 来了、练 30 分钟、
       OODA loop 这类中英/中数之间的空格是对的，不能碰。 */
    var CJK = '\u3000-\u303f\u4e00-\u9fff\uff01-\uff65';
    text = String(text).replace(new RegExp('([' + CJK + '])[ \t]+(?=[' + CJK + '])', 'g'), '$1');
    // 引用一律收拢到每段末尾、去重。
    // prompt 里也这么要求，但这是确定性的事，不该指望模型每次都听话：
    // 它常把标记塞在段落中间的句子后面，读起来像话被打断。
    var firstBody = true;
    text = text.split('\n').map(function (line) {
      // 第一段是复述处境、说清卡在哪——那是判断不是引述，不挂出处。
      // prompt 里也写了，这里兜底。
      if (line.trim() && firstBody) {
        firstBody = false;
        return line.replace(/\s*\[\d+\]\s*/g, '').replace(/\s+$/, '');
      }
      var ids = [], seen = {};
      line.replace(/\[(\d+)\]/g, function (_, d) {
        if (!seen[d]) { seen[d] = 1; ids.push(d); }
        return '';
      });
      if (!ids.length) return line;
      var body = line.replace(/\s*\[\d+\]\s*/g, '').replace(/\s+$/, '');
      return body + ids.map(function (d) { return '[' + d + ']'; }).join('');
    }).join('\n');
    /* 编号按整篇算，不按段算。原来只在「同一段挂了两条」时才编号，
       可模型多半是一段挂一条——于是两段各出一个光秃秃的「原文」，
       读者照样分不清是两个链接还是同一篇被引了两次。
       整篇只有一条时不编号，多写一个「1」是白噪音。
       同一篇在多处出现给同一个号，编号认的是篇不是位置。
       越界的编号（模型偶尔会写 [9] 而只给了 8 篇）不占号：它渲染不出链接，
       占了号就会出现「只有一个原文2、没有原文1」。 */
    var num = {}, seq = 0;
    text.replace(/\[(\d+)\]/g, function (_, d) {
      if (!(d in num) && hits[parseInt(d, 10)]) num[d] = ++seq;
      return '';
    });
    if (seq < 2) num = {};
    // 一遍扫过 **小标题** 和 [编号] 两种记号。
    // 只认这两种，其余一律当普通文字；全程 createTextNode / createElement，
    // 模型输出永远不进 innerHTML。
    var re = /\*\*(.+?)\*\*|\[(\d+)\]/g, last = 0, m;
    while ((m = re.exec(text)) !== null) {
      if (m.index > last) el.appendChild(document.createTextNode(text.slice(last, m.index)));
      if (m[1] !== undefined) {
        var bEl = document.createElement('b');
        bEl.className = 'hwq-h';
        bEl.textContent = m[1];
        el.appendChild(bEl);
      } else {
        var c = hits[parseInt(m[2], 10)];
        if (c) {
          var a = document.createElement('a');
          a.className = 'hwq-cite';
          a.href = c.u;
          /* 不写章节名——句句都挂个标题太吵，点进去就知道是哪篇。
             hover 的 title 里有「谁·哪篇」，要认的时候认得出。 */
          a.textContent = num[m[2]] ? '原文' + num[m[2]] : '原文';
          a.title = c.p + ' · ' + c.n;
          el.appendChild(a);
        }
      }
      last = re.lastIndex;
    }
    if (last < text.length) el.appendChild(document.createTextNode(text.slice(last)));
  }

  /* ---------- 检索：中文按二元组算重合 ---------- */
  var INDEX = null, loading = null;
  function loadIndex() {
    if (INDEX) return Promise.resolve(INDEX);
    if (loading) return loading;
    loading = fetch('/assets/hw-chat-index.json')
      .then(function (r) { return r.json(); })
      .then(function (j) { INDEX = j; return j; });
    return loading;
  }
  function grams(s) {
    s = String(s || '').toLowerCase().replace(/[\s，。、；：！？「」（）,.!?;:'"]/g, '');
    var g = {};
    for (var i = 0; i < s.length - 1; i++) g[s.slice(i, i + 2)] = 1;
    if (s.length === 1) g[s] = 1;
    return g;
  }
  /* 二元组按稀有度加权，不再一视同仁。
     原来每个二元组算一分，于是「我做了对不起人的事，一直没说」会被
     「一直、做了、我做、直没」勾到蒲松龄《考了四十年》上，而真正带信息的
     「对不」（全库只出现 1 次）和它同权。稀有的词才是查询的意思所在。 */
  var IDF = null;
  function buildIdf() {
    if (IDF) return;
    var dfc = {}, ag = [], sg = [], n = INDEX.alias.length;
    INDEX.alias.forEach(function (row) {
      var g = grams(row[0]);
      ag.push(g); sg.push(grams(row[1]));
      for (var k in g) dfc[k] = (dfc[k] || 0) + 1;
    });
    var cg = INDEX.chapters.map(function (c) {
      return [grams(c.n + c.w), grams(c.dek)];
    });
    IDF = { df: dfc, n: n, dflt: Math.log(n + 1), ag: ag, sg: sg, cg: cg };
  }
  function wgt(g) {
    var c = IDF.df[g];
    return c ? Math.log((IDF.n + 1) / (1 + c)) : IDF.dflt;
  }
  function overlap(a, b) {           /* 加权重合度 */
    var s = 0;
    for (var k in a) if (b[k]) s += wgt(k);
    return s;
  }
  var lastScene = '';          /* 最近一次检索命中最强的处境名 */
  function retrieve(q, k) {
    buildIdf();
    var qa = grams(q), score = {}, sceneBest = 0;
    lastScene = '';
    /* 取最大而不是累加：同一个处境下问句越多，累加就越容易把它顶上来——
       那是「这个处境写得全」，不是「这一条更对得上」。只认最贴的那一条。 */
    function bump(i, s) { if (s > (score[i] || 0)) score[i] = s; }
    INDEX.alias.forEach(function (row, j) {
      var s = overlap(qa, IDF.ag[j]) * 3 + overlap(qa, IDF.sg[j]) * 2;
      if (s > 0) {
        row[2].forEach(function (i) { bump(i, s); });
        /* 处境名一直在索引里（alias 行是 [问句, 处境名, [章节]]），
           只是检索时被丢掉了。带出来，答案就能点名「你这件事是【钱不够】」——
           把「我这事很特别」变成「这是一类事，有人处理过」。 */
        if (s > sceneBest) { sceneBest = s; lastScene = row[1]; }
      }
    });
    INDEX.chapters.forEach(function (c, i) {
      var s = overlap(qa, IDF.cg[i][0]) * 2 + overlap(qa, IDF.cg[i][1]);
      if (s > 0) bump(i, s);
    });
    return Object.keys(score)
      .sort(function (a, b) { return score[b] - score[a]; })
      .slice(0, k || 6)
      .map(function (i) { return INDEX.chapters[i]; });
  }

  /* ---------- 提问 ---------- */
  var busy = false;
  /* 首页那一问是唯一一次「我们已经知道答案」的提问：卡片上那两篇出处就是
     今日一问的答案，处境名也是数据里写死的。检索是给自由输入用的，用在这里
     等于把已知的答案扔了再猜一遍。
     而且这里的猜特别不准——预填句是按「不复读卡片」写的，刻意换了一套词，
     恰好绕开了二元组索引：实测首位命中从 99% 掉到 7%，七成的日子连正确
     章节都召不回来。所以首页来的这一问带着答案走，检索只负责补后面几篇。 */
  var pinned = null;
  function ask() {
    var q = input.value.trim();
    if (!q || busy) return;
    if (left() <= 0) { hint('今天的 5 次用完了，明天再来。'); return; }
    busy = true; send.disabled = true;
    input.value = ''; input.style.height = 'auto';
    dropIntro();
    say('me', q);
    var thinking = say('ai', '在翻书……');

    loadIndex().then(function () {
      // 召回 8 篇而不是 6：二元组匹配偏字面，语义差一层。
      // 多给两篇让模型自己挑（它看得到正文），比调权重划算——
      // 每次多约 1500 字，答案只引用它 USED 里点名的那几篇。
      var hits = retrieve(q, 8);
      if (pinned) {
        var seen = {}, head = [];
        pinned.pin.forEach(function (u) {
          for (var i = 0; i < INDEX.chapters.length; i++) {
            if (INDEX.chapters[i].u === u && !seen[u]) { seen[u] = 1; head.push(INDEX.chapters[i]); }
          }
        });
        hits = head.concat(hits.filter(function (c) { return !seen[c.u]; })).slice(0, 8);
        if (pinned.scene) lastScene = pinned.scene;
        pinned = null;           /* 只作用于这一条，后面的追问照常检索 */
      }
      if (!hits.length) {
        thinking.textContent = '这件事站里还没有对得上的内容。换个说法试试，或者直接搜一下。';
        busy = false; refreshLeft(); return;
      }
      return fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ q: q, ctx: hits, scene: lastScene })
      }).then(function (r) {
        // 先无条件取 body：429 的正文里有服务端写好的那句话，比「HTTP 429」有用。
        return r.json().catch(function () { return null; })
          .then(function (j) { return { ok: r.ok, status: r.status, body: j }; });
      }).then(function (res) {
        if (res.ok && res.body && res.body.answer) {
          renderAnswer(thinking, res.body.answer, hits);
          var h = loadHist();
          h.push({ q: q, a: res.body.answer, hits: slimHits(hits), ts: Date.now() });
          saveHist(h);
          useOne(); refreshLeft();
          return;
        }
        if (res.status === 429) {
          // 服务端说没额度了就以它为准——前端这份计数只是提示，
          // 换设备、清缓存都会让它和服务端对不上，这里校准回去。
          thinking.textContent = (res.body && res.body.error) || '今天的次数用完了，明天再来。';
          try { localStorage.setItem(LS_KEY, JSON.stringify({ d: today(), n: DAILY_LIMIT })); } catch (e) {}
          refreshLeft();
          return;
        }
        throw new Error('HTTP ' + res.status);
      }).catch(function (e) {
        // 真实用户不该看到 chat_dev_proxy.py 这种字样；细节留给控制台。
        if (window.console) console.error('[hw-chat]', e);
        thinking.textContent = '没连上，等一下再试一次。';
      }).then(function () { busy = false; });
    });
  }

  /* iOS 上 position:fixed;inset:0 贴的是布局视口，而键盘弹起来不改变布局视口——
     于是面板底边留在键盘后面，Safari 又把输入框顶上来，中间那条就露出了页面本体。
     visualViewport 是唯一拿得到「键盘之上那块可见区域」的接口，实时贴上去。
     没有这个接口的浏览器退回 CSS 的 inset:0，跟改之前一样。 */
  /* iOS 上键盘不改变布局视口，于是 position:fixed 的面板底边留在键盘后面。
     interactive-widget=resizes-content 让布局视口自己缩，inset:0 就天然贴合，
     不用我去算几何——算几何这条路已经错了两版。
     只在面板开着时改，关掉就还原：它会影响页面上任何输入框获得焦点时的行为，
     不该为了一个悬浮球改掉整站的默认。 */
  var META = document.querySelector('meta[name="viewport"]');
  var METAORIG = META ? META.getAttribute('content') : null;
  function widenViewport() {
    if (META && METAORIG && METAORIG.indexOf('interactive-widget') < 0) {
      META.setAttribute('content', METAORIG + ',interactive-widget=resizes-content');
    }
  }
  function restoreViewport() {
    if (META && METAORIG != null) META.setAttribute('content', METAORIG);
  }

  /* 只有带 ?hwqdebug=1 才出现。真机上的 iOS 几何我在这儿复现不出来，
     与其再猜一版，不如让一张截图把数字全给出来。 */
  var DEBUG = /[?&]hwqdebug=1/.test(location.search), dbg = null;
  function paintDbg() {
    if (!DEBUG) return;
    if (!dbg) { dbg = document.createElement('div'); dbg.id = 'hwq-dbg'; document.body.appendChild(dbg); }
    var pr = panel.getBoundingClientRect(), br = back.getBoundingClientRect();
    dbg.textContent =
      'inner ' + innerWidth + '\u00d7' + innerHeight +
      '  client ' + document.documentElement.clientHeight +
      '\nvv ' + (vv ? Math.round(vv.width) + '\u00d7' + Math.round(vv.height) +
        ' oT' + Math.round(vv.offsetTop) + ' pT' + Math.round(vv.pageTop) : 'none') +
      '  scrollY ' + Math.round(scrollY) +
      '\npanel t' + Math.round(pr.top) + ' h' + Math.round(pr.height) + ' b' + Math.round(pr.bottom) +
      '\nback  t' + Math.round(br.top) + ' h' + Math.round(br.height) + ' b' + Math.round(br.bottom) +
      '\nlock ' + (locked ? 'on savedY' + savedY : 'off') +
      ' bodyTop' + (document.body.style.top || '-') +
      '\nmeta ' + (META ? (META.getAttribute('content') || '').slice(-34) : 'none');
  }

  var vv = window.visualViewport, lastFit = '';
  function fitPanel() {
    if (!vv || panel.hidden) return;
    var key = vv.offsetTop + '|' + vv.offsetLeft + '|' + vv.width + '|' + vv.height;
    if (key === lastFit) { paintDbg(); return; }   /* 没变就不写样式，免得每次轮询都触发重排 */
    lastFit = key;
    var st2 = panel.style;
    st2.top = vv.offsetTop + 'px';
    st2.left = vv.offsetLeft + 'px';
    st2.width = vv.width + 'px';
    st2.height = vv.height + 'px';
    st2.right = 'auto'; st2.bottom = 'auto';
    paintDbg();
  }
  function unfitPanel() {
    lastFit = '';
    var st2 = panel.style;
    st2.top = st2.left = st2.width = st2.height = st2.right = st2.bottom = '';
  }
  /* 键盘弹出时 iOS 会发 visualViewport.resize，但只挂这一个事件源不够稳
     （实测在模拟环境里就没发）。再挂 window 的两个，并在 focus/blur 之后补两刀——
     键盘有约 300ms 动画，动画结束前量到的高度是中间值。 */
  function scheduleFit() { fitPanel(); setTimeout(fitPanel, 120); setTimeout(fitPanel, 380); }
  if (vv) {
    vv.addEventListener('resize', fitPanel);
    vv.addEventListener('scroll', fitPanel);
  }
  window.addEventListener('resize', scheduleFit);
  window.addEventListener('orientationchange', scheduleFit);

  /* 事件之外再加一层轮询，只在面板开着的时候跑。
     理由不是理论上不够，是这条路根本验不了：模拟环境改视口时一个事件都不发，
     而这正是要修的那个 bug。轮询不依赖任何事件派发，量到变化才写样式，
     没变化时几乎不花钱。关掉面板就停。 */
  var fitTimer = null;
  function startFit() { fitPanel(); if (!fitTimer) fitTimer = setInterval(fitPanel, 150); }
  function stopFit() { if (fitTimer) { clearInterval(fitTimer); fitTimer = null; } }

  /* 手机上不自动聚焦：一开面板就弹键盘，正好把要给人看的开场白盖掉。
     桌面没这个问题，光标直接就位反而省一次点击。 */
  var COARSE = !!(window.matchMedia && window.matchMedia('(pointer:coarse)').matches);

  /* 真机读数把病根指出来了：scrollY 1968、vv.pageTop 1968，
     而 panel.getBoundingClientRect().top 是 0——布局视口和视觉视口错开了近 2000px，
     于是 position:fixed 的原点根本不在屏幕左上角，页面正文从面板上方和下方都会露。
     前三版都在修键盘那一头，其实是滚动位置没锁住。

     documentElement.style.overflow='hidden' 在 iOS 上拦不住这件事——它不改 scrollY。
     标准解法是把 body 自己 fixed 住并上移 scrollY，让滚动真的归零，
     两个视口就重合了。关掉时再滚回原处，用户看不出发生过什么。 */
  var savedY = 0, locked = false;
  function lockScroll() {
    if (locked) return;
    savedY = window.pageYOffset || document.documentElement.scrollTop || 0;
    var b = document.body.style;
    b.position = 'fixed';
    b.top = (-savedY) + 'px';
    b.left = '0';
    b.right = '0';
    b.width = '100%';
    b.overflow = 'hidden';
    locked = true;
  }
  function unlockScroll() {
    if (!locked) return;
    var b = document.body.style;
    b.position = ''; b.top = ''; b.left = ''; b.right = ''; b.width = ''; b.overflow = '';
    locked = false;
    window.scrollTo(0, savedY);   /* 回到原来看的地方 */
  }

  var prevOverflow = '';
  ball.onclick = function () {
    widenViewport();
    lockScroll();                 /* 必须在显示面板之前：先归零，fixed 的原点才对 */
    ball.hidden = true; back.hidden = false; panel.hidden = false;
    prevOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = 'hidden';
    startFit();
    restoreHist();               /* 先恢复旧记录，有记录时开场白就不出现 */
    showIntro();
    refreshLeft();
    if (!COARSE) setTimeout(function () { input.focus(); }, 50);
  };
  function close() {
    input.blur();                 /* 不 blur 的话 iOS 键盘会赖着不走 */
    panel.hidden = true; back.hidden = true; ball.hidden = false;
    restoreViewport();
    if (dbg) { dbg.parentNode.removeChild(dbg); dbg = null; }
    stopFit(); unfitPanel();
    document.documentElement.style.overflow = prevOverflow;
    unlockScroll();
  }
  panel.querySelector('#hwq-close').onclick = close;
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !panel.hidden) close();
  });
  send.onclick = ask;
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); ask(); }
  });
  input.addEventListener('focus', function () {
    scheduleFit();
    setTimeout(function () { scroller.scrollTop = scroller.scrollHeight; }, 300);
  });
  input.addEventListener('blur', scheduleFit);
  input.addEventListener('input', function () {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 88) + 'px';
  });
  refreshLeft();

  /* 给首页用的一个口子：带着一句话把面板打开并直接问。
     首页「今日一问」下面那个输入框已经让人改过词了，所以这里不再让他
     在面板里重打一遍——他编辑的地方只有一个。 */
  window.hwAsk = function (text, opts) {
    var t = String(text || '').trim();
    if (!t) return;
    if (panel.hidden) ball.click();
    /* opts.pin 是卡片上那两篇的链接，opts.scene 是它属于哪个处境。
       两个都是首页已经知道的事实，传进来就不必再猜。 */
    pinned = (opts && opts.pin && opts.pin.length) ? { pin: opts.pin, scene: opts.scene || '' } : null;
    input.value = t.slice(0, 500);
    ask();
  };
  window.hwLeft = left;          /* 首页要知道今天还剩几次 */
})();
