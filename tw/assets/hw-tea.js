/* 「請喝茶」：頁尾分享按鈕旁那一枚。點開一張小卡，按環境給不同的付款路徑——
   微信內置瀏覽器：微信收款碼，長按識別；手機上其他瀏覽器：支付寶收款鏈接直接跳，
   或截圖後在支付寶裡掃相冊；桌面：兩枚二維碼，拿手機掃。
   收款圖和鏈接由頁面注入的 window.HW_TEA 給：{wechat, alipay, alipayLink}。
   沒有配置就什麼都不做——按鈕本身也只在有收款圖時才會被構建進頁面。 */
(function () {
  var C = window.HW_TEA;
  if (!C || !C.alipay) return;
  var ua = navigator.userAgent || '';
  var inWeChat = /MicroMessenger/i.test(ua);
  var mobile = /Android|iPhone|iPad|iPod|Mobile/i.test(ua) ||
    (window.matchMedia && matchMedia('(pointer:coarse)').matches);

  var CSS = [
    '#hwt-back{position:fixed;inset:0;z-index:9990;background:rgba(20,16,10,.45)}',
    '#hwt{position:fixed;left:50%;top:50%;transform:translate(-50%,-50%);z-index:9991;',
    'width:min(92vw,392px);box-sizing:border-box;padding:24px 22px 20px;border-radius:18px;',
    'background:var(--surface,var(--card,#faf7f0));color:var(--ink,#1f1c17);border:1px solid var(--line,#d8d2c6);',
    'box-shadow:0 18px 60px -20px rgba(0,0,0,.45);text-align:center}',
    '#hwt h3{font-family:"Noto Serif TC","Songti SC","STSong",serif;font-size:20px;font-weight:700;margin:0 0 6px}',
    '#hwt .sub{font-size:13.5px;color:var(--muted,#8a8377);line-height:1.7;margin:0 0 16px}',
    '#hwt .qrs{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}',
    '#hwt figure{margin:0;display:flex;flex-direction:column;align-items:center;gap:6px}',
    '#hwt img{width:152px;height:152px;border-radius:12px;background:#fff;padding:6px;box-sizing:border-box;display:block}',
    '#hwt.one img{width:200px;height:200px}',
    '#hwt figcaption{font-size:12.5px;color:var(--muted,#8a8377)}',
    '#hwt .how{font-size:13.5px;line-height:1.7;margin:14px 0 0;color:var(--ink,#1f1c17)}',
    '#hwt a.go{display:inline-block;margin:6px 0 2px;padding:9px 22px;border-radius:999px;',
    'background:var(--ink,#1f1c17);color:var(--paper,#f5f1e8);text-decoration:none;font-size:14px}',
    '#hwt .x{position:absolute;right:10px;top:8px;border:0;background:none;font-size:22px;',
    'line-height:1;color:var(--muted,#8a8377);cursor:pointer;padding:6px}',
    /* 章節頁的暗色變量表裡沒有 --card，首頁的裡沒有 --surface；兩處都兜住，再補顯式暗色。 */
    ':root[data-theme="dark"] #hwt{background:#1d1913;border-color:#3a342a}',
    '@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) #hwt{background:#1d1913;border-color:#3a342a}}',
    '#hwt[hidden],#hwt-back[hidden]{display:none}'
  ].join('');
  var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);

  var back, card;
  function build() {
    back = document.createElement('div'); back.id = 'hwt-back'; back.hidden = true;
    card = document.createElement('div'); card.id = 'hwt'; card.hidden = true;
    card.setAttribute('role', 'dialog'); card.setAttribute('aria-label', '請我喝杯茶');
    var html = '<button class="x" type="button" aria-label="關閉">×</button>' +
      '<h3>請我喝杯茶</h3><p class="sub">金額隨意，幫到了你就好。</p>';
    if (inWeChat && C.wechat) {
      card.className = 'one';
      html += '<div class="qrs"><figure><img src="' + C.wechat + '" alt="微信收款碼"></figure></div>' +
        '<p class="how">長按二維碼，識別後就能付。</p>';
    } else if (inWeChat) {
      /* 微信裡打不開支付寶鏈接：長按存圖，去支付寶掃相冊。 */
      card.className = 'one';
      html += '<div class="qrs"><figure><img src="' + C.alipay + '" alt="支付寶收款碼"></figure></div>' +
        '<p class="how">長按保存圖片，打開支付寶掃相冊。</p>';
    } else if (mobile) {
      card.className = 'one';
      html += (C.alipayLink ? '<a class="go" href="' + C.alipayLink + '" rel="noopener">打開支付寶</a>' : '') +
        '<div class="qrs"><figure><img src="' + C.alipay + '" alt="支付寶收款碼"></figure></div>' +
        '<p class="how">' + (C.alipayLink ? '或者' : '') + '截圖，在支付寶裡掃相冊。</p>';
    } else {
      var two = !!C.wechat;
      if (!two) card.className = 'one';
      html += '<div class="qrs">' +
        (two ? '<figure><img src="' + C.wechat + '" alt="微信收款碼"><figcaption>微信</figcaption></figure>' : '') +
        '<figure><img src="' + C.alipay + '" alt="支付寶收款碼">' + (two ? '<figcaption>支付寶</figcaption>' : '') + '</figure>' +
        '</div><p class="how">' + (two ? '拿手機掃一掃，哪個順手用哪個。' : '打開支付寶，掃一掃。') + '</p>';
    }
    card.innerHTML = html;
    document.body.appendChild(back); document.body.appendChild(card);
    back.onclick = close; card.querySelector('.x').onclick = close;
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !card.hidden) close(); });
  }
  function open() { if (!card) build(); back.hidden = false; card.hidden = false; }
  function close() { back.hidden = true; card.hidden = true; }

  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-tea]');
    if (!b) return;
    e.preventDefault(); open();
  });
})();
