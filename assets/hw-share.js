/* Human World share — same contract as 原声 /podcast/assets/site.js
   [data-share] + data-share-title/url/text
   WeChat: copy + toast. Elsewhere: navigator.share, fallback copy. */
(function () {
  'use strict';

  var toastEl, toastTimer;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.setAttribute('role', 'status');
      toastEl.style.cssText =
        'position:fixed;left:50%;bottom:34px;transform:translate(-50%,14px);z-index:120;' +
        'background:#1c1917;color:#f7f4ec;font-size:13px;padding:10px 18px;border-radius:999px;' +
        'opacity:0;pointer-events:none;transition:opacity .2s,transform .2s;max-width:86vw;text-align:center';
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    toastEl.style.opacity = '1';
    toastEl.style.transform = 'translate(-50%,0)';
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toastEl.style.opacity = '0';
      toastEl.style.transform = 'translate(-50%,14px)';
    }, 2600);
  }

  function copy(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (res, rej) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
      document.body.appendChild(ta);
      ta.select();
      ta.setSelectionRange(0, ta.value.length);
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) {}
      ta.remove();
      ok ? res() : rej(new Error('execCommand failed'));
    });
  }

  function inWeChat() { return /MicroMessenger/i.test(navigator.userAgent); }

  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-share]');
    if (!b) return;
    e.preventDefault();
    var text = b.getAttribute('data-share-text') || '';
    var url = b.getAttribute('data-share-url') || location.href;
    var title = b.getAttribute('data-share-title') || document.title;
    var wx = inWeChat();
    if (!wx && navigator.share) {
      // text 传**不带链接**的那一份。带链接的话，它和 url 字段是同一个
      // 地址，一次分享出现两个 URL —— 微信会当成两个条目，文本正常发出，
      // URL 另存成一个临时文件跟着发过去（原声那边实测到过）。
      var desc = b.getAttribute('data-share-desc') || text;
      navigator.share({ title: title, text: desc, url: url })
        .catch(function (err) {
          if (err && err.name === 'AbortError') return;
          fallback(text);
        });
      return;
    }
    fallback(text);

    function fallback(t) {
      copy(t).then(function () {
        toast(wx ? '已复制，长按粘贴发给朋友；发朋友圈点右上角 ···'
                 : '已复制，粘到微信、朋友圈或任何地方');
      }).catch(function () {
        toast('复制没成功，长按选中链接：' + url);
      });
    }
  });
})();
