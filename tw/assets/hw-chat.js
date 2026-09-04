/* 懸浮球問答 · 人類世界生存法則
 *
 * 視覺按 DESIGN.md：正文 17px/1.78 對齊章節頁的 17px/1.75（聊天也是閱讀面，
 * 沒道理比正文小）、硃紅是全站唯一強調色、無陰影、層次靠底色與 1px 細線、
 * 標題宋體正文黑體、觸控目標 ≥32px、深色模式三套變量都要顧到。
 *
 * 檢索不走 llms-full.txt（1.4MB）。索引裡有 308 篇章節和 428 條處境問題；
 * 那些問題本來就是第一人稱口語，跟用戶描述處境的說法同源，是最好的匹配信號。
 * 索引 249KB(gzip)，所以點開才加載，不進首屏。
 *
 * 後端：window.HW_CHAT_ENDPOINT。key 永遠不進瀏覽器——
 * 本地 demo 走 scripts/chat_dev_proxy.py，線上要走 Cloudflare Worker。
 */
(function () {
  'use strict';
  if (window.__hwChat) return;
  window.__hwChat = 1;

  // 端點由構建時注入。為空說明 Worker 還沒部署——什麼都不渲染，
  // 寧可沒有這個功能，也不要讓人點開一個連不上的窗口。
  var ENDPOINT = window.HW_CHAT_ENDPOINT || '';
  if (!ENDPOINT) return;
  var DAILY_LIMIT = 5;
  /* 鍵名換過一次。舊版限流按 IP 算，被別人佔滿時前端會把本地計數
     直接寫成「已用 5 次」——於是一個一次都沒問過的人，當天再也點不動，
     而且清不掉，因為按鈕在發請求之前就被這份本地計數禁用了。
     限流改成按瀏覽器算之後，那批寫壞的值必須作廢，換個鍵最乾淨。 */
  var LS_KEY = 'hw-chat-quota2';

  /* ---------- 語言 ----------
     一份文件兩種語言，不是兩份文件：這個掛件是 /assets/ 下的靜態資源，
     三個語言站共用同一個 URL。複製一份出來給英文站，兩份遲早走散。
     判據用路徑：/en/… 是英文站，其餘（含 /tw/）走中文那套。
     繁體頁上的這些字由 build_tw.py 的轉換順帶處理，所以這裡只分中英。 */
  var LANG = /^\/en(\/|$)/.test(location.pathname) ? 'en' : 'zh';
  var T = LANG === 'en' ? {
    ask: 'Stuck? Ask.',
    head: "What's going on?",
    ph: 'Tell me\u2026',
    phDone: "That's today's five. Come back tomorrow.",
    phPass: "You've had a good run today. Tomorrow.",
    open: 'Anything \u2014 work, home, money, your body, or the things you '
        + "don't say out loud. The more specific, the likelier we find "
        + 'someone it actually matches.',
    send: 'Send',
    close: 'Close',
    thinking: 'Looking it up\u2026',
    source: 'Read it',
    left: function (n) { return n + ' left today'; },
    free: 'Unlimited today',
    none: "Nothing here matches that yet. Try saying it another way, or search.",
    neterr: "Couldn't reach it. Try again in a moment.",
    over: "That's today's five. Come back tomorrow.",
    teaHead: "That's today's five.",
    teaBody: 'Buy me a tea and today is unlimited. Any amount.',
    teaGo: 'Open AlipayHK',
    teaAlt: 'AlipayHK payment code',
    teaHowWx: 'Press and hold to save the image, then scan it from your album.',
    teaHowMob: 'Or screenshot it and scan from your album in AlipayHK.',
    teaHowPc: 'Open AlipayHK and scan.',
    teaYes: 'Done \u2014 keep going',
    teaNo: 'Tomorrow',
    teaThanks: 'Thank you. Unlimited today.',
    teaLater: 'Tomorrow then.',
    ball: 'Ask',
    srv: "That's today's allowance. Come back tomorrow."
  } : {
    ask: '\u9047\u5230\u4e8b\u4e86\uff1f\u95ee\u4e00\u95ee',
    head: '\u4f60\u9047\u5230\u4ec0\u4e48\u4e8b\u4e86\uff1f',
    ph: '\u8bf4\u8bf4\u770b\u2026\u2026',
    phDone: '\u4eca\u5929\u7684 5 \u6b21\u7528\u5b8c\u4e86',
    phPass: '\u4eca\u5929\u804a\u5f97\u591f\u591a\u4e86\uff0c\u660e\u5929\u518d\u6765',
    open: '\u5de5\u4f5c\u3001\u5bb6\u91cc\u3001\u94b1\u3001\u8eab\u4f53\uff0c\u6216\u8005\u8bf4\u4e0d\u51fa\u53e3\u7684\u90a3\u4e9b\uff0c\u90fd\u53ef\u4ee5\u8bf4\u3002\u8bf4\u5f97\u8d8a\u5177\u4f53\uff0c\u8d8a\u5bb9\u6613\u627e\u5230\u771f\u7684\u5bf9\u5f97\u4e0a\u7684\u4eba\u3002',
    send: '\u53d1\u9001',
    close: '\u5173\u95ed',
    thinking: '\u5728\u7ffb\u4e66\u2026\u2026',
    source: '\u539f\u6587',
    left: function (n) { return '\u4eca\u5929\u8fd8\u80fd\u95ee ' + n + ' \u6b21'; },
    free: '\u4eca\u5929\u968f\u4fbf\u804a',
    none: '\u8fd9\u4ef6\u4e8b\u7ad9\u91cc\u8fd8\u6ca1\u6709\u5bf9\u5f97\u4e0a\u7684\u5185\u5bb9\u3002\u6362\u4e2a\u8bf4\u6cd5\u8bd5\u8bd5\uff0c\u6216\u8005\u76f4\u63a5\u641c\u4e00\u4e0b\u3002',
    neterr: '\u6ca1\u8fde\u4e0a\uff0c\u7b49\u4e00\u4e0b\u518d\u8bd5\u4e00\u6b21\u3002',
    over: '\u4eca\u5929\u7684 5 \u6b21\u7528\u5b8c\u4e86\uff0c\u660e\u5929\u518d\u6765\u3002',
    teaHead: '\u4eca\u5929\u7684 5 \u6b21\u7528\u5b8c\u4e86\u3002',
    teaBody: '\u8bf7\u6211\u559d\u676f\u8336\uff0c\u4eca\u5929\u65e0\u9650\u7545\u804a\u3002\u91d1\u989d\u968f\u610f\u3002',
    teaGo: '\u6253\u5f00\u652f\u4ed8\u5b9d',
    teaAlt: '\u652f\u4ed8\u5b9d\u6536\u6b3e\u7801',
    teaHowWx: '\u957f\u6309\u4fdd\u5b58\u56fe\u7247\uff0c\u6253\u5f00\u652f\u4ed8\u5b9d\u626b\u76f8\u518c\u3002',
    teaHowMob: '\u6216\u8005\u622a\u56fe\uff0c\u5728\u652f\u4ed8\u5b9d\u91cc\u626b\u76f8\u518c\u3002',
    teaHowPc: '\u6253\u5f00\u652f\u4ed8\u5b9d\uff0c\u626b\u4e00\u626b\u3002',
    teaYes: '\u6211\u8bf7\u4e86\uff0c\u63a5\u7740\u804a',
    teaNo: '\u660e\u5929\u518d\u6765',
    teaThanks: '\u8c22\u8c22\u3002\u4eca\u5929\u968f\u4fbf\u804a\u3002',
    teaLater: '\u90a3\u5c31\u660e\u5929\u3002',
    ball: '\u95ee',
    srv: '\u4eca\u5929\u7684\u6b21\u6570\u7528\u5b8c\u4e86\uff0c\u660e\u5929\u518d\u6765\u3002'
  };

  var PASS_KEY = 'hw-chat-pass';   /* 「請我喝杯茶」當天暢聊：值是當天日期 */
  var PASS_CEIL = 60;
  /* 聊天記錄存 localStorage。
     一開始用的是 sessionStorage——理由是這裡存的是人描述自己的處境，
     不該在設備上留到下次打開瀏覽器。但那是我的判斷不是用戶的需求：
     關掉標籤頁再回來記錄就沒了，被反映了兩次。改成 localStorage，
     關瀏覽器也在。只留最近 20 輪，且每輪只存問題、答案和引用鏈接，
     不存餵給模型的正文。 */
  /* 聊天記錄：本地留著，關瀏覽器再打開也在。
     原來卡 20 條上限——那是按條數砍，砍掉的可能是上週最要緊的那次。
     改成按時間：只丟 7 天前的，7 天內不管多少條都留。
     另有一個條數上限只為兜住 localStorage 的容量，不是產品規則。 */
  var HIST_KEY = 'hw-chat-log';
  var HIST_DAYS = 7;
  var HIST_HARD_MAX = 200;      /* 純粹防 localStorage 撐爆，正常人到不了 */

  function fresh(a) {
    var cut = Date.now() - HIST_DAYS * 864e5;
    return a.filter(function (x) { return !x.ts || x.ts >= cut; });
  }
  function loadHist() {
    try {
      var a = JSON.parse(localStorage.getItem(HIST_KEY) || '[]');
      if (!a.length) return [];
      var f = fresh(a);
      if (f.length !== a.length) saveHist(f);      /* 順手把過期的落盤清掉 */
      return f;
    } catch (e) { return []; }
  }
  function saveHist(h) {
    var keep = fresh(h).slice(-HIST_HARD_MAX);
    try { localStorage.setItem(HIST_KEY, JSON.stringify(keep)); }
    catch (e) {
      /* 滿了就丟最舊的一半再試一次，別讓一次寫失敗把整段記錄卡死 */
      try { localStorage.setItem(HIST_KEY, JSON.stringify(keep.slice(-Math.ceil(keep.length / 2)))); }
      catch (e2) {}
    }
  }

  /* 這個瀏覽器的身份。服務端按它算額度，不再按 IP——
     中國的移動網絡是 CGNAT，一個出口 IP 後面掛著成千上萬部手機，
     按 IP 算等於一個陌生人問完，整個基站下的人當天都被擋住。
     清緩存就能換一個新的，擋不住有心人；但有心人不是這道閘要擋的對象。 */
  var CID_KEY = 'hw-chat-cid';
  function cid() {
    try {
      var v = localStorage.getItem(CID_KEY);
      if (!v) {
        v = (Date.now().toString(36) + Math.random().toString(36).slice(2, 12)).replace(/[^a-z0-9]/g, '');
        localStorage.setItem(CID_KEY, v);
      }
      return v;
    } catch (e) { return ''; }
  }

  /* ---------- 每日額度（前端只是提示，真正的限流必須在服務端） ---------- */
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
  function pass() { try { return localStorage.getItem(PASS_KEY) === today(); } catch (e) { return false; } }
  function grantPass() { try { localStorage.setItem(PASS_KEY, today()); } catch (e) {} }
  function left() { return Math.max(0, (pass() ? PASS_CEIL : DAILY_LIMIT) - quota().n); }

  /* ---------- 樣式 ---------- */
  var CSS = [
    '#hwq-ball{position:fixed;right:18px;bottom:18px;z-index:9998;width:52px;height:52px;',
    'border-radius:50%;background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8);border:none;cursor:pointer;',
    'font-family:"Noto Serif TC","Songti SC","STSong",serif;font-size:21px;font-weight:700;',
    'line-height:52px;padding:0;transition:transform .15s ease}',
    '#hwq-ball:hover{transform:scale(1.06)}',
    '#hwq-ball[hidden]{display:none}',

    /* 全屏，而不是右下角的小彈窗——彈窗在手機上又窄又擠。
       但背景鋪滿、正文列限寬 680px 居中：桌面上讓文字橫貫 1280px，
       一行五六十字，比彈窗更難讀（章節頁桌面也是 32 字一行）。 */
    '#hwq-panel{position:fixed;inset:0;z-index:9999;display:flex;flex-direction:column;',
    'background:var(--paper,#f5f1e8)}',
    '#hwq-panel[hidden]{display:none}',
    /* 背板。真機讀數（scrollY 3186、panel t0 而屏幕頂端仍有頁面內容）說明
       fixed 座標系的 0 不在屏幕頂端——屏幕頂端是負座標。所以 top:0 的背板
       夠不著上面那一半，之前一直沒擋住。改成從 -150vh 起、總高 400vh，
       上下都留足餘量。它只是一塊純色，不花什麼錢。 */
    '#hwq-back{position:fixed;left:0;top:-150vh;width:100%;height:400vh;z-index:9997;',
    'background:var(--paper,#f5f1e8)}',
    '#hwq-back[hidden]{display:none}',
    '#hwq-dbg{position:fixed;left:0;top:0;z-index:10000;background:rgba(0,0,0,.82);color:#0f0;',
    'font:11px/1.45 ui-monospace,Menlo,monospace;padding:6px 8px;white-space:pre;pointer-events:none}',
    '.hwq-col{width:100%;max-width:680px;margin:0 auto;padding:0 20px;box-sizing:border-box}',

    '#hwq-head{flex:0 0 auto;border-bottom:1px solid var(--line,#d8d2c6)}',
    '#hwq-head .hwq-col{display:flex;align-items:baseline;gap:8px;padding-top:16px;padding-bottom:13px}',
    '#hwq-head b{font-family:"Noto Serif TC","Songti SC",serif;font-size:21px;font-weight:700;color:var(--ink,#1f1c17)}',
    '#hwq-head span{font-size:13px;color:var(--muted,#8a8377);margin-left:auto}',
    '#hwq-close{border:none;background:transparent;color:var(--muted,#8a8377);font-size:26px;',
    'line-height:1;cursor:pointer;padding:0 4px;margin-left:8px;min-width:32px;min-height:32px}',

    '#hwq-log{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch}',
    /* 底部留白比頂部厚得多：答案和輸入框之間原來只有 18px，
       最後一行字幾乎貼著輸入框。而且答案讀完之後要能再往上推一截，
       沒有這塊餘量就推不動。 */
    '#hwq-log .hwq-col{display:flex;flex-direction:column;gap:14px;padding-top:18px;padding-bottom:40px}',
    '.hwq-m{max-width:88%;font-size:17px;line-height:1.78;border-radius:12px;padding:10px 12px;white-space:pre-wrap}',
    '.hwq-me{align-self:flex-end;background:var(--paper2,#eee8da);color:var(--ink,#1f1c17)}',
    '.hwq-ai{align-self:flex-start;background:var(--card,#faf7f0);border:1px solid var(--line,#d8d2c6);color:var(--ink,#1f1c17)}',
    '.hwq-hint{align-self:center;font-size:13.5px;color:var(--muted,#8a8377);line-height:1.7;text-align:center}',
    /* 引用行內跟在句子後面，不攢到最後——讀者在讀到那句時就能點過去。
       只寫章節名不寫人名：人名在落地頁第一眼就有，行內每處多六個字太吵。 */
    '.hwq-h{font-weight:700}',
    /* 必須帶 #hwq-panel 前綴。站上有條 :root[data-theme="dark"] … a 的規則
       （優先級 0,2,1）會把鏈接壓成正文色——實測 .hwq-cite(0,1,0) 輸，
       連 a.hwq-cite(0,1,1) 也輸，#hwq-panel .hwq-cite(1,1,0) 才贏。
       用提高優先級而不是 !important：DESIGN.md 裡記著這個站已經被
       !important 坑過一次，不該再加一條。
       懸浮球從只在首頁擴到全站 467 頁之後才暴露——首頁沒有那條規則。 */
    '#hwq-panel .hwq-cite{color:var(--acc,#a33b2e);text-decoration:none;font-size:13.5px;',
    'white-space:nowrap;margin-left:4px;vertical-align:baseline}',
    '#hwq-panel .hwq-cite:hover{opacity:.7}',

    /* 等待時那句話自己會動。靜止的「在翻書……」和卡死的界面長得一模一樣，
       十一秒裡讀者沒有任何依據判斷是哪一種。 */
    '.hwq-wait{background:linear-gradient(90deg,var(--muted,#8a8377) 0%,var(--muted,#8a8377) 42%,',
    'var(--ink,#1f1c17) 50%,var(--muted,#8a8377) 58%,var(--muted,#8a8377) 100%);',
    'background-size:220% 100%;-webkit-background-clip:text;background-clip:text;',
    '-webkit-text-fill-color:transparent;color:transparent;animation:hwq-sheen 1.9s linear infinite}',
    '@keyframes hwq-sheen{from{background-position:120% 0}to{background-position:-120% 0}}',
    '@media(prefers-reduced-motion:reduce){.hwq-wait{animation:none;-webkit-text-fill-color:var(--muted,#8a8377);',
    'color:var(--muted,#8a8377)}#hwq-send.busy svg{animation:none}}',

    '#hwq-foot{flex:0 0 auto;border-top:1px solid var(--line,#d8d2c6);padding-bottom:env(safe-area-inset-bottom)}',
    '#hwq-foot .hwq-col{display:flex;gap:10px;align-items:flex-end;padding-top:12px;padding-bottom:12px}',
    '#hwq-in{flex:1;resize:none;border:1px solid var(--line,#d8d2c6);border-radius:999px;background:transparent;',
    'color:var(--ink,#1f1c17);font-family:inherit;font-size:17px;line-height:1.55;padding:10px 16px;max-height:88px;outline:none}',
    '#hwq-in:focus{border-color:var(--muted,#8a8377)}',
    /* 尺寸和長相都照舊。只加一件事：等回答的時候按鈕轉圈。
       原來這 11 秒裡按鈕毫無反應，唯一的反饋是那句「在翻書」，
       而它可能已經滾上去了。min-width 釘住，換成轉圈時按鈕不跳。 */
    '#hwq-send{flex:0 0 auto;border:none;border-radius:999px;background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8);',
    'font-family:inherit;font-size:15.5px;padding:11px 18px;cursor:pointer;min-height:36px;min-width:67px;',
    'line-height:21px}',
    '#hwq-send:disabled{opacity:.45;cursor:default}',
    /* 轉圈的圖標走內聯，不改按鈕的盒模型——按鈕的高度還是由文字行高撐出來的
       那一個值。改成 flex 居中會讓轉圈時比寫著「發送」時矮 5px，一發一收地跳。 */
    '#hwq-send svg{width:16px;height:16px;vertical-align:middle;animation:hwq-spin .8s linear infinite}',
    '@keyframes hwq-spin{to{transform:rotate(360deg)}}',

    /* 開場白。原先沒有，是想錯了：標題「你遇到什麼事了？」只說了怎麼問，
       沒說能問什麼——新來的人分不清這是站內搜索、客服，還是通用聊天。 */
    '#hwq-intro{align-self:stretch;padding-top:4px}',
    '#hwq-intro p{margin:0;font-size:15px;line-height:1.8;color:var(--muted,#8a8377);text-align:left}',

    '.hwq-tea b{display:block;font-size:16px;margin-bottom:4px}',
    '.hwq-tea p{margin:0 0 10px;font-size:15px;line-height:1.7}',
    '.hwq-tea .hwq-how{font-size:13px;color:var(--muted,#8a8377);margin:8px 0 0}',
    '.hwq-tea .hwq-qr{display:block;width:180px;height:180px;border-radius:12px;background:#fff;padding:6px;box-sizing:border-box;margin:6px 0}',
    '.hwq-tea a.hwq-go{display:inline-block;margin:0 0 8px;padding:8px 18px;border-radius:999px;background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8);text-decoration:none;font-size:14px}',
    '.hwq-tea-acts{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}',
    '.hwq-tea-acts button{border:1px solid var(--ink,#1f1c17);border-radius:999px;padding:7px 16px;font-size:13.5px;cursor:pointer;font-family:inherit}',
    '.hwq-tea-acts .hwq-yes{background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8)}',
    '.hwq-tea-acts .hwq-no{background:transparent;color:var(--ink,#1f1c17)}',
    ':root[data-theme="dark"] .hwq-ai{background:#1d1913}',
    ':root[data-theme="dark"] .hwq-me{background:#201c15}',
    /* 小人頭像：每條回答左邊一枚。頭像是身份不是內容，只在「有人在跟你說話」的地方出現，
       不上懸浮球；也不進面板標題——390 寬下標題、額度、關閉三樣已經滿了。深色底用帶米白描邊的那版。 */
    '.hwq-ai{position:relative;margin-left:36px;max-width:calc(88% - 36px)}',
    '.hwq-ai::before{content:"";position:absolute;left:-36px;top:1px;width:28px;height:28px;border-radius:50%;background:url(/assets/hw-avatar.png) center/cover no-repeat}',
    ':root[data-theme="dark"] .hwq-ai::before{background-image:url(/assets/hw-avatar-dark.png)}',
    '@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) .hwq-ai::before{background-image:url(/assets/hw-avatar-dark.png)}}',
    /* 手機上球縮一號、再貼邊一點。52px 貼在 right:14 時會佔到 x=324-376，
       而章節頁正文列的右邊界是 366——它永久壓住每一屏最後一行的最後兩個字。
       縮到 42、貼到 right:6 之後壓住的寬度從 42px 降到 24px（約一個字）。
       想徹底不壓只能把正文列變窄，那是可見的版式改動，沒自己動。 */
    '@media(max-width:480px){.hwq-col{padding:0 16px}',
    '#hwq-ball{right:6px;bottom:12px;width:42px;height:42px;font-size:18px;line-height:42px}}'
  ].join('');

  var st = document.createElement('style');
  st.id = 'hwq-style'; st.textContent = CSS;
  document.head.appendChild(st);

  /* ---------- DOM ---------- */
  var ball = document.createElement('button');
  ball.id = 'hwq-ball'; ball.type = 'button';
  ball.textContent = T.ball;
  ball.setAttribute('aria-label', T.ask);

  var panel = document.createElement('div');
  panel.id = 'hwq-panel'; panel.hidden = true;
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', T.ask);
  /* 等待時轉的那個圈。內聯 SVG，不引圖標庫（CSP 也不允許）。 */
  var SPIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
    + 'stroke-linecap="round" aria-hidden="true">'
    + '<path d="M21 12a9 9 0 1 1-6.2-8.55"/></svg>';

  panel.innerHTML =
    '<div id="hwq-head"><div class="hwq-col"><b>' + T.head + '</b>' +
    '<span id="hwq-left"></span><button id="hwq-close" type="button" aria-label="' + T.close + '">×</button></div></div>' +
    '<div id="hwq-log"><div class="hwq-col" id="hwq-logc"></div></div>' +
    '<div id="hwq-foot"><div class="hwq-col">' +
    '<textarea id="hwq-in" rows="1" placeholder="' + T.ph + '"></textarea>' +
    '<button id="hwq-send" type="button">' + T.send + '</button></div></div>';

  var back = document.createElement('div');
  back.id = 'hwq-back'; back.hidden = true;

  back.setAttribute('aria-hidden', 'true');

  /* 首頁不掛球：那一頁有「今日一問」自己的輸入框，右下角再放一個「問」
     等於同一件事給兩個入口。首頁走 hwAsk 直接開面板，不經過球。 */
  var HOME = !!document.getElementById('hwx-askhero');
  if (!HOME) document.body.appendChild(ball);
  document.body.appendChild(back);
  document.body.appendChild(panel);

  var log = panel.querySelector('#hwq-logc');       /* 消息進限寬的列裡 */
  var scroller = panel.querySelector('#hwq-log');  /* 滾動的是外層 */
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
    p.textContent = T.open;
    box.appendChild(p);
    log.appendChild(box);
  }
  function dropIntro() {
    var i = log.querySelector('#hwq-intro');
    if (i) i.parentNode.removeChild(i);
  }

  /* 撞到第六次時的那張卡：不是「明天再來」，是「請我喝杯茶，今天無限暢聊」。
     信任制：付完點「我請了」當天解鎖，沒有驗證——白點的人一天最多讓站多花一塊多。
     付款路徑沿用頁尾那套：微信里長按存圖去 AlipayHK掃；手機瀏覽器直接跳AlipayHK；桌面掃碼。 */
  function teaPass(el) {
    var C = window.HW_TEA || {};
    if (!C.alipay) {
      if (el) el.textContent = T.over; else hint(T.over);
      return;
    }
    var d = el || say('ai', '');
    d.classList.remove('hwq-wait'); d.classList.add('hwq-tea');
    var ua = navigator.userAgent || '';
    var wx = /MicroMessenger/i.test(ua);
    var mob = /Android|iPhone|iPad|iPod|Mobile/i.test(ua);
    var how = wx ? T.teaHowWx : (mob ? T.teaHowMob : T.teaHowPc);
    d.innerHTML = '<b>' + T.teaHead + '</b>' +
      '<p>' + T.teaBody + '</p>' +
      ((!wx && mob && C.alipayLink) ? '<a class="hwq-go" href="' + C.alipayLink + '" rel="noopener">' + T.teaGo + '</a>' : '') +
      '<img class="hwq-qr" src="' + C.alipay + '" alt="' + T.teaAlt + '">' +
      '<p class="hwq-how">' + how + '</p>' +
      '<div class="hwq-tea-acts"><button type="button" class="hwq-yes">' + T.teaYes + '</button>' +
      '<button type="button" class="hwq-no">' + T.teaNo + '</button></div>';
    d.querySelector('.hwq-yes').onclick = function () {
      grantPass(); d.parentNode.removeChild(d);
      hint(T.teaThanks); refreshLeft();
      if (!COARSE) input.focus();
    };
    d.querySelector('.hwq-no').onclick = function () { d.parentNode.removeChild(d); hint(T.teaLater); };
    scroller.scrollTop = scroller.scrollHeight;
  }

  /* 只留渲染引用要用的三個字段：正文 txt 一篇 700 字，八篇存進去太浪費。 */
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
    leftEl.textContent = pass() ? T.free : T.left(n);
    /* 滿額時佔位符別說「明天再來」——卡片正在說「今天接著聊」，兩句不能打架 */
    input.placeholder = n > 0 ? T.ph : (pass() ? T.phPass : T.phDone);
    paintSend();
  }
  function paintSend() {
    if (busy) { send.innerHTML = SPIN; send.disabled = true; return; }
    send.textContent = T.send;
    send.disabled = left() <= 0;
  }

  /* 把模型寫的 [0] 換成行內出處鏈接。
     全程只用 createTextNode 與 createElement——模型輸出一律當不可信文本，
     絕不 innerHTML 拼進去。 */
  /* 答完把這條的頂端推到可視區頂上。
     原來一律滾到最底——答案比一屏長的時候，讀者看到的是它的尾巴，
     得自己往回翻才能從頭讀。答案短的時候瀏覽器會把 scrollTop 夾回去，
     行為跟原來一樣。

     anchor 記住「現在該讓誰露在頂上」。鍵盤彈起時那個延時 300ms 的
     滾到底本來是為了別讓新消息被鍵盤蓋住，但它會在 reveal 之後
     再把答案頂回去——實測 reveal 在 +200ms 生效，+500ms 就被沖掉了。
     有 anchor 的時候按 anchor 走。 */
  var anchor = null;
  function toBottom() { scroller.scrollTop = scroller.scrollHeight; }
  function reveal(el) {
    anchor = el || null;
    if (!anchor) return toBottom();
    var a = anchor.getBoundingClientRect(), b = scroller.getBoundingClientRect();
    scroller.scrollTop += (a.top - b.top) - 12;
  }
  function keepInView() { if (anchor) reveal(anchor); else toBottom(); }

  function renderAnswer(el, text, hits) {
    el.textContent = '';
    /* 中文之間的空格去掉。模型愛寫「**先問自己。** 別想怎麼……」——
       句號後面多一個半角空格，中文排版裡那是個洞。
       只在「前後都是中文（或中文標點）」時去：AI 來了、練 30 分鐘、
       OODA loop 這類中英/中數之間的空格是對的，不能碰。
       兩邊的 ** 要看穿：線上那個洞正好在 ** 後面，只認中文字符會漏掉它。 */
    var CJK = '\u3000-\u303f\u4e00-\u9fff\uff01-\uff65';
    text = String(text).replace(
      new RegExp('([' + CJK + ']\\*{0,2})[ \\t]+(?=\\*{0,2}[' + CJK + '])', 'g'), '$1');
    // 引用一律收攏到每段末尾、去重。
    // prompt 裡也這麼要求，但這是確定性的事，不該指望模型每次都聽話：
    // 它常把標記塞在段落中間的句子後面，讀起來像話被打斷。
    var firstBody = true;
    text = text.split('\n').map(function (line) {
      // 第一段是複述處境、說清卡在哪——那是判斷不是引述，不掛出處。
      // prompt 裡也寫了，這裡兜底。
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
    /* 編號按整篇算，不按段算。原來只在「同一段掛了兩條」時才編號，
       可模型多半是一段掛一條——於是兩段各出一個光禿禿的「原文」，
       讀者照樣分不清是兩個鏈接還是同一篇被引了兩次。
       整篇只有一條時不編號，多寫一個「1」是白噪音。
       同一篇在多處出現給同一個號，編號認的是篇不是位置。
       越界的編號（模型偶爾會寫 [9] 而只給了 8 篇）不佔號：它渲染不出鏈接，
       佔了號就會出現「只有一個原文2、沒有原文1」。 */
    var num = {}, seq = 0;
    text.replace(/\[(\d+)\]/g, function (_, d) {
      if (!(d in num) && hits[parseInt(d, 10)]) num[d] = ++seq;
      return '';
    });
    if (seq < 2) num = {};
    // 一遍掃過 **小標題** 和 [編號] 兩種記號。
    // 只認這兩種，其餘一律當普通文字；全程 createTextNode / createElement，
    // 模型輸出永遠不進 innerHTML。
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
          /* 不寫章節名——句句都掛個標題太吵，點進去就知道是哪篇。
             hover 的 title 裡有「誰·哪篇」，要認的時候認得出。 */
          a.textContent = num[m[2]] ? T.source + ' ' + num[m[2]] : T.source;
          a.title = c.p + ' · ' + c.n;
          el.appendChild(a);
        }
      }
      last = re.lastIndex;
    }
    if (last < text.length) el.appendChild(document.createTextNode(text.slice(last)));
  }

  /* ---------- 檢索：中文按二元組算重合 ---------- */
  var INDEX = null, loading = null;
  function loadIndex() {
    if (INDEX) return Promise.resolve(INDEX);
    if (loading) return loading;
    loading = fetch(LANG === 'en' ? '/tw/assets/hw-chat-index-en.json'
                              : '/tw/assets/hw-chat-index.json')
      .then(function (r) { return r.json(); })
      .then(function (j) { INDEX = j; return j; });
    return loading;
  }
  /* 英文必須按**詞**切，不能沿用中文的字符二元組。
     grams() 原本先把空格全刪掉再取兩字窗口 —— 對中文正好（中文沒有詞邊界），
     對英文等於按字母亂撞："I got passed over" 變成 ig/go/ot/tp… ，
     和任何一句英文都有一堆重合，IDF 也救不回來。
     英文取「單詞 + 相鄰詞對」：單詞給召回，詞對認短語。
     輕量歸一化只做三件最常見的（複數、-ing、-ed），再多就開始誤傷。 */
  function stem(w) {
    if (w.length > 4) {
      if (/ies$/.test(w)) return w.slice(0, -3) + 'y';
      if (/(ing|ed)$/.test(w)) return w.replace(/(ing|ed)$/, '');
      if (/s$/.test(w) && !/ss$/.test(w)) return w.slice(0, -1);
    }
    return w;
  }
  function grams(s) {
    s = String(s || '').toLowerCase();
    var g = {}, i;
    if (LANG === 'en') {
      var w = s.replace(/[^a-z0-9\s'-]/g, ' ').split(/\s+/);
      w = w.filter(Boolean).map(stem);
      for (i = 0; i < w.length; i++) {
        g[w[i]] = 1;
        if (i) g[w[i - 1] + ' ' + w[i]] = 1;
      }
      return g;
    }
    s = s.replace(/[\s，。、；：！？「」（）,.!?;:'"]/g, '');
    for (i = 0; i < s.length - 1; i++) g[s.slice(i, i + 2)] = 1;
    if (s.length === 1) g[s] = 1;
    return g;
  }
  /* 二元組按稀有度加權，不再一視同仁。
     原來每個二元組算一分，於是「我做了對不起人的事，一直沒說」會被
     「一直、做了、我做、直沒」勾到蒲松齡《考了四十年》上，而真正帶信息的
     「對不」（全庫只出現 1 次）和它同權。稀有的詞才是查詢的意思所在。 */
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
  function overlap(a, b) {           /* 加權重合度 */
    var s = 0;
    for (var k in a) if (b[k]) s += wgt(k);
    return s;
  }
  var lastScene = '';          /* 最近一次檢索命中最強的處境名 */
  function retrieve(q, k) {
    buildIdf();
    var qa = grams(q), score = {}, sceneBest = 0;
    lastScene = '';
    /* 取最大而不是累加：同一個處境下問句越多，累加就越容易把它頂上來——
       那是「這個處境寫得全」，不是「這一條更對得上」。只認最貼的那一條。 */
    function bump(i, s) { if (s > (score[i] || 0)) score[i] = s; }
    INDEX.alias.forEach(function (row, j) {
      var s = overlap(qa, IDF.ag[j]) * 3 + overlap(qa, IDF.sg[j]) * 2;
      if (s > 0) {
        row[2].forEach(function (i) { bump(i, s); });
        /* 處境名一直在索引裡（alias 行是 [問句, 處境名, [章節]]），
           只是檢索時被丟掉了。帶出來，答案就能點名「你這件事是【錢不夠】」——
           把「我這事很特別」變成「這是一類事，有人處理過」。 */
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

  /* ---------- 提問 ---------- */
  var busy = false;
  /* 這一次會話說過的話，還有上一輪用過的那幾篇。
     缺了這兩樣，答案結尾的追問就是個陷阱：讀者回三五個字，
     那三五個字既沒有上下文、二元組也檢索不出對的篇目——
     實測「卡在總是忘記」被答成了帶團隊出不了活。 */
  var turns = [];
  var lastHits = [];
  /* 首頁那一問是唯一一次「我們已經知道答案」的提問：卡片上那兩篇出處就是
     今日一問的答案，處境名也是數據裡寫死的。檢索是給自由輸入用的，用在這裡
     等於把已知的答案扔了再猜一遍。
     而且這裡的猜特別不準——預填句是按「不復讀卡片」寫的，刻意換了一套詞，
     恰好繞開了二元組索引：實測首位命中從 99% 掉到 7%，七成的日子連正確
     章節都召不回來。所以首頁來的這一問帶著答案走，檢索只負責補後面幾篇。 */
  var pinned = null;
  function ask() {
    var q = input.value.trim();
    if (!q || busy) return;
    if (left() <= 0) { if (pass()) hint(T.phPass); else teaPass(null); return; }
    busy = true; paintSend();
    input.value = ''; input.style.height = 'auto';
    dropIntro();
    anchor = null;            /* 自己剛說完話，先跟著最新走 */
    say('me', q);
    var thinking = say('ai', T.thinking);
    thinking.classList.add('hwq-wait');

    loadIndex().then(function () {
      // 召回 8 篇而不是 6：二元組匹配偏字面，語義差一層。
      // 多給兩篇讓模型自己挑（它看得到正文），比調權重劃算——
      // 每次多約 1500 字，答案只引用它 USED 裡點名的那幾篇。
      var hits = retrieve(q, 8);
      /* 續問時把上一輪用過的篇目排到最前，檢索只負責補後面。
         短句檢索本來就不準：「卡在總是忘記」六個字，
         二元組能匹配上什麼全看運氣。模型看得到對話，讓它自己挑。 */
      if (turns.length && lastHits.length) {
        var keep = {};
        var head2 = lastHits.slice(0, 3).filter(function (c) {
          if (keep[c.u]) return false; keep[c.u] = 1; return true;
        });
        hits = head2.concat(hits.filter(function (c) { return !keep[c.u]; })).slice(0, 8);
      }
      if (pinned) {
        var seen = {}, head = [];
        pinned.pin.forEach(function (u) {
          for (var i = 0; i < INDEX.chapters.length; i++) {
            if (INDEX.chapters[i].u === u && !seen[u]) { seen[u] = 1; head.push(INDEX.chapters[i]); }
          }
        });
        hits = head.concat(hits.filter(function (c) { return !seen[c.u]; })).slice(0, 8);
        if (pinned.scene) lastScene = pinned.scene;
        pinned = null;           /* 只作用於這一條，後面的追問照常檢索 */
      }
      if (!hits.length) {
        thinking.classList.remove('hwq-wait');
        thinking.textContent = T.none;
        busy = false; refreshLeft(); return;
      }
      return fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          q: q, ctx: hits, cid: cid(), pass: pass() ? 1 : 0, lang: LANG,
          /* 處境名只在第一輪送。第二輪再送，模型就會把
             「你這件事是『想改個習慣』」再點一遍，成了復讀。 */
          scene: turns.length ? '' : lastScene,
          history: turns.slice(-3),
        })
      }).then(function (r) {
        // 先無條件取 body：429 的正文裡有服務端寫好的那句話，比「HTTP 429」有用。
        return r.json().catch(function () { return null; })
          .then(function (j) { return { ok: r.ok, status: r.status, body: j }; });
      }).then(function (res) {
        if (res.ok && res.body && res.body.answer) {
          thinking.classList.remove('hwq-wait');
          renderAnswer(thinking, res.body.answer, hits);
          reveal(thinking);
          turns.push({ q: q, a: res.body.answer });
          if (turns.length > 6) turns = turns.slice(-6);
          lastHits = hits;
          var h = loadHist();
          h.push({ q: q, a: res.body.answer, hits: slimHits(hits), ts: Date.now() });
          saveHist(h);
          useOne(); refreshLeft();
          return;
        }
        if (res.status === 429) {
          thinking.classList.remove('hwq-wait');
          if (res.body && res.body.scope === 'you' && !pass() && window.HW_TEA && window.HW_TEA.alipay) {
            teaPass(thinking);          /* 第六次：不是「明天再來」，是「請我喝杯茶，今天接著聊」 */
          } else {
            thinking.textContent = (res.body && res.body.error) || T.srv;
          }
          /* 只有服務端說「是你自己用完了」時才把本地計數校準到滿。
             scope:'net' 是這個出口 IP 上有人問得多——把它記成讀者自己
             用完了，會讓一個一次都沒問過的人當天再也點不動，
             而且提示還告訴他「你的 5 次用完了」。這正是 CGNAT 下的常態。 */
          if (!res.body || res.body.scope !== 'net') {
            try { localStorage.setItem(LS_KEY, JSON.stringify({ d: today(), n: DAILY_LIMIT })); } catch (e) {}
          }
          refreshLeft();
          return;
        }
        throw new Error('HTTP ' + res.status);
      }).catch(function (e) {
        // 真實用戶不該看到 chat_dev_proxy.py 這種字樣；細節留給控制台。
        if (window.console) console.error('[hw-chat]', e);
        thinking.classList.remove('hwq-wait');
        thinking.textContent = T.neterr;
      }).then(function () { busy = false; paintSend(); });
    });
  }

  /* iOS 上 position:fixed;inset:0 貼的是布局視口，而鍵盤彈起來不改變布局視口——
     於是面板底邊留在鍵盤後面，Safari 又把輸入框頂上來，中間那條就露出了頁面本體。
     visualViewport 是唯一拿得到「鍵盤之上那塊可見區域」的接口，實時貼上去。
     沒有這個接口的瀏覽器退回 CSS 的 inset:0，跟改之前一樣。 */
  /* iOS 上鍵盤不改變布局視口，於是 position:fixed 的面板底邊留在鍵盤後面。
     interactive-widget=resizes-content 讓布局視口自己縮，inset:0 就天然貼合，
     不用我去算幾何——算幾何這條路已經錯了兩版。
     只在面板開著時改，關掉就還原：它會影響頁面上任何輸入框獲得焦點時的行為，
     不該為了一個懸浮球改掉整站的默認。 */
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

  /* 只有帶 ?hwqdebug=1 才出現。真機上的 iOS 幾何我在這兒復現不出來，
     與其再猜一版，不如讓一張截圖把數字全給出來。 */
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
    if (key === lastFit) { paintDbg(); return; }   /* 沒變就不寫樣式，免得每次輪詢都觸發重排 */
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
  /* 鍵盤彈出時 iOS 會發 visualViewport.resize，但只掛這一個事件源不夠穩
     （實測在模擬環境裡就沒發）。再掛 window 的兩個，並在 focus/blur 之後補兩刀——
     鍵盤有約 300ms 動畫，動畫結束前量到的高度是中間值。 */
  function scheduleFit() { fitPanel(); setTimeout(fitPanel, 120); setTimeout(fitPanel, 380); }
  if (vv) {
    vv.addEventListener('resize', fitPanel);
    vv.addEventListener('scroll', fitPanel);
  }
  window.addEventListener('resize', scheduleFit);
  window.addEventListener('orientationchange', scheduleFit);

  /* 事件之外再加一層輪詢，只在面板開著的時候跑。
     理由不是理論上不夠，是這條路根本驗不了：模擬環境改視口時一個事件都不發，
     而這正是要修的那個 bug。輪詢不依賴任何事件派發，量到變化才寫樣式，
     沒變化時幾乎不花錢。關掉面板就停。 */
  var fitTimer = null;
  function startFit() { fitPanel(); if (!fitTimer) fitTimer = setInterval(fitPanel, 150); }
  function stopFit() { if (fitTimer) { clearInterval(fitTimer); fitTimer = null; } }

  /* 手機上不自動聚焦：一開面板就彈鍵盤，正好把要給人看的開場白蓋掉。
     桌面沒這個問題，光標直接就位反而省一次點擊。 */
  var COARSE = !!(window.matchMedia && window.matchMedia('(pointer:coarse)').matches);

  /* 真機讀數把病根指出來了：scrollY 1968、vv.pageTop 1968，
     而 panel.getBoundingClientRect().top 是 0——布局視口和視覺視口錯開了近 2000px，
     於是 position:fixed 的原點根本不在屏幕左上角，頁面正文從面板上方和下方都會露。
     前三版都在修鍵盤那一頭，其實是滾動位置沒鎖住。

     documentElement.style.overflow='hidden' 在 iOS 上攔不住這件事——它不改 scrollY。
     標準解法是把 body 自己 fixed 住並上移 scrollY，讓滾動真的歸零，
     兩個視口就重合了。關掉時再滾回原處，用戶看不出發生過什麼。 */
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
    window.scrollTo(0, savedY);   /* 回到原來看的地方 */
  }

  var prevOverflow = '';
  function openPanel() {
    widenViewport();
    lockScroll();                 /* 必須在顯示面板之前：先歸零，fixed 的原點才對 */
    ball.hidden = true; back.hidden = false; panel.hidden = false;
    prevOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = 'hidden';
    startFit();
    restoreHist();               /* 先恢復舊記錄，有記錄時開場白就不出現 */
    showIntro();
    refreshLeft();
    if (!COARSE) setTimeout(function () { input.focus(); }, 50);
  }
  ball.onclick = openPanel;
  function close() {
    input.blur();                 /* 不 blur 的話 iOS 鍵盤會賴著不走 */
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
    setTimeout(keepInView, 300);
  });
  input.addEventListener('blur', scheduleFit);
  input.addEventListener('input', function () {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 88) + 'px';
  });
  refreshLeft();

  /* 給首頁用的一個口子：帶著一句話把面板打開並直接問。
     首頁「今日一問」下面那個輸入框已經讓人改過詞了，所以這裡不再讓他
     在面板裡重打一遍——他編輯的地方只有一個。 */
  window.hwAsk = function (text, opts) {
    var t = String(text || '').trim();
    if (!t) return;
    if (panel.hidden) openPanel();
    /* opts.pin 是卡片上那兩篇的鏈接，opts.scene 是它屬於哪個處境。
       兩個都是首頁已經知道的事實，傳進來就不必再猜。 */
    pinned = (opts && opts.pin && opts.pin.length) ? { pin: opts.pin, scene: opts.scene || '' } : null;
    input.value = t.slice(0, 500);
    ask();
  };
  window.hwLeft = left;          /* 首頁要知道今天還剩幾次 */
})();
