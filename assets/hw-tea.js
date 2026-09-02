/* 「请喝茶」：页尾分享按钮旁那一枚。点开一张小卡，按环境给不同的付款路径——
   微信内置浏览器：微信收款码，长按识别；手机上其他浏览器：支付宝收款链接直接跳，
   或截图后在支付宝里扫相册；桌面：两枚二维码，拿手机扫。
   收款图和链接由页面注入的 window.HW_TEA 给：{wechat, alipay, alipayLink}。
   没有配置就什么都不做——按钮本身也只在有收款图时才会被构建进页面。 */
(function () {
  var C = window.HW_TEA;
  if (!C || !C.wechat || !C.alipay) return;
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
    '#hwt h3{font-family:"Noto Serif SC","Songti SC","STSong",serif;font-size:20px;font-weight:700;margin:0 0 6px}',
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
    /* 章节页的暗色变量表里没有 --card，首页的里没有 --surface；两处都兜住，再补显式暗色。 */
    ':root[data-theme="dark"] #hwt{background:#1d1913;border-color:#3a342a}',
    '@media(prefers-color-scheme:dark){:root:not([data-theme="light"]) #hwt{background:#1d1913;border-color:#3a342a}}',
    '#hwt[hidden],#hwt-back[hidden]{display:none}'
  ].join('');
  var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);

  var back, card;
  function build() {
    back = document.createElement('div'); back.id = 'hwt-back'; back.hidden = true;
    card = document.createElement('div'); card.id = 'hwt'; card.hidden = true;
    card.setAttribute('role', 'dialog'); card.setAttribute('aria-label', '请我喝杯茶');
    var html = '<button class="x" type="button" aria-label="关闭">×</button>' +
      '<h3>请我喝杯茶</h3><p class="sub">金额随意，帮到了你就好。</p>';
    if (inWeChat) {
      card.className = 'one';
      html += '<div class="qrs"><figure><img src="' + C.wechat + '" alt="微信收款码"></figure></div>' +
        '<p class="how">长按二维码，识别后就能付。</p>';
    } else if (mobile) {
      card.className = 'one';
      html += (C.alipayLink ? '<a class="go" href="' + C.alipayLink + '" rel="noopener">打开支付宝</a>' : '') +
        '<div class="qrs"><figure><img src="' + C.alipay + '" alt="支付宝收款码"></figure></div>' +
        '<p class="how">' + (C.alipayLink ? '或者' : '') + '截图，在支付宝里扫相册。</p>';
    } else {
      html += '<div class="qrs">' +
        '<figure><img src="' + C.wechat + '" alt="微信收款码"><figcaption>微信</figcaption></figure>' +
        '<figure><img src="' + C.alipay + '" alt="支付宝收款码"><figcaption>支付宝</figcaption></figure>' +
        '</div><p class="how">拿手机扫一扫，哪个顺手用哪个。</p>';
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
