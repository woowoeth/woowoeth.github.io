# -*- coding: utf-8 -*-
"""三语层：hreflang、语言切换、首访跟随浏览器语言。

简体站、繁体站、英文站共用这一份。抽成独立模块有两个理由：

· force_chapter_ui.py 只走简体树（它盖的是简体挂件，盖到 tw/ 上会把繁体页的
  资源路径和收款码改坏 —— 真发生过，553 个文件）。英文站由 build_en.py 生成，
  也需要同一套语言层，于是两个调用方需要同一份实现。
· 更要紧的是 hreflang 必须在三份拷贝里**逐字相同**。分成两处写，迟早走散，
  而走散的 hreflang 不会报错，只会让搜索引擎认不出这几页是同一篇。

关键一条：三条 hreflang 用的都是**去掉语言前缀的裸路径**。/en/i/su-shi/ 这一页
的 zh-Hans 指的是 /i/su-shi/，不是 /en/i/su-shi/ —— 它描述的是「别的语言版本
在哪」，不是这一页自己在哪（那是 canonical 的活）。
"""
import os
import re

HWL_A = "<!--HWX:LANG-->"
HWL_B = "<!--/HWX:LANG-->"


def _derived(dp):
    return any(x in dp for x in ("/.git", "/tw", "/en", "node_modules", "__pycache__")) \
        or dp.startswith((".git", "./tw", "./en"))


def _en_paths():
    """英文版**真实存在**的那些路径（站内绝对路径，带首尾斜杠）。

    为什么从数据推而不是走一遍 en/：英文站由 build_en.py 生成，而本脚本排在
    它前面。走产物的话，第一次构建时 en/ 还不存在，hreflang 就会整批漏掉；
    走数据则跟构建顺序无关，同一份输入永远算出同一个集合。

    这一版只有 30 个条目上线，全站 159 个条目里剩下的 129 个**没有**英文版。
    给它们发 hreflang="en" 等于把搜索引擎指向 404 —— 比不发更糟。
    """
    import os
    out = {"/"}
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "seo", "chapters_en")
    here = os.path.normpath(here)
    if not os.path.isdir(here):
        return out
    import importlib
    import pkgutil
    import sys as _s
    _s.path.insert(0, os.path.dirname(here))
    for mod in sorted(m.name for m in pkgutil.iter_modules([here])):
        m = importlib.import_module("chapters_en." + mod)
        slug = (getattr(m, "PARENT", {}) or {}).get("slug", "")
        if not slug:
            continue
        out.add("/i/%s/" % slug)
        for ch in getattr(m, "CHAPTERS", []) or []:
            out.add("/i/%s/%s/" % (slug, ch["k"]))
    return out


EN_PATHS = _en_paths()


def patch_tree(root="."):
    """给每一页补语言层：hreflang、切换按钮、首访按浏览器语言跳一次。

    为什么这一步放在正常构建里，而不是放进 build_tw.py：
    **简体页和繁体页都需要它**。繁体站是 build_tw.py 拿构建好的简体树转出来的，
    所以只要这里注入一次，转换的时候会跟着复制过去，两边天然对称，不会漏。

    三样东西：

    ① hreflang 用**静态 link 标签**，不靠 JS —— 爬虫不执行脚本，
       只有静态标签才能让搜索引擎知道这两个 URL 是同一篇的两种语言。
       这三行在两份拷贝里内容完全一样（各自指向对方），所以 build_tw.py
       重写绝对地址时必须跳过它们，只改 canonical 和 og:url。

    ② 切换按钮的文字**由 JS 按当前路径决定**，不写死：
       简体页上显示「繁體」，繁体页上显示「简体」（这四个字会被 build_tw
       一并转成「簡體」，正好是繁体页该有的写法）。

    ③ 首访跳转：读 navigator.languages，zh-Hant/TW/HK/MO 去 /tw/。
       跳过一次之后不再自动跳 —— 用户点了切换按钮就把选择记进 localStorage，
       记住的优先级高于浏览器语言，否则一个在台湾用简体的读者每次都被弹走。
       整段在 <head> 里同步执行，在首屏渲染之前完成，不会看到闪一下。
    """
    n = 0
    for dp, dn, fn in os.walk(root):
        if root == "." and _derived(dp):
            continue
        if "__pycache__" in dp or "/.git" in dp:
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            path = os.path.join(dp, f)
            s = open(path, encoding="utf-8").read()
            if 'http-equiv="refresh"' in s:     # 跳转桩不管
                continue
            if HWL_A in s:                       # 幂等：重跑不叠加
                s = re.sub(re.escape(HWL_A) + r".*?" + re.escape(HWL_B), "", s, flags=re.S)
            rel = os.path.relpath(path, ".").replace(os.sep, "/")
            rel = "/" + rel[:-len("index.html")] if rel.endswith("index.html") else "/" + rel
            if rel == "/404.html":
                rel = "/404.html"
            # 裸路径 —— 去掉 /tw 或 /en 前缀。hreflang 描述的是「别的语言版本
            # 在哪」，三份拷贝里这几行必须一模一样，所以不能带自己的前缀。
            bare = re.sub(r"^/(tw|en)(?=/|$)", "", rel) or "/"
            base = "https://ourword.ai"
            has_en = bare in EN_PATHS
            block = (
                HWL_A
                + '<link rel="alternate" hreflang="zh-Hans" href="%s%s">' % (base, bare)
                + '<link rel="alternate" hreflang="zh-Hant" href="%s/tw%s">' % (base, bare)
                + ('<link rel="alternate" hreflang="en" href="%s/en%s">' % (base, bare)
                   if has_en else "")
                + '<link rel="alternate" hreflang="x-default" href="%s%s">' % (base, bare)
                + "<script>(function(){try{"
                  "var K='hwx_lang',p=location.pathname,HAS_EN=" + ("1" if has_en else "0") + ";"
                  "var tw=/^\\/tw(\\/|$)/.test(p),en=/^\\/en(\\/|$)/.test(p);"
                  "var cur=en?'en':(tw?'tw':'sc');"
                  "var bare=p.replace(/^\\/(tw|en)/,'')||'/';"
                  "var to={sc:bare,tw:'/tw'+bare,en:'/en'+bare};"
                  "var saved=null;try{saved=localStorage.getItem(K)}catch(e){}"
                  # 首访跟随浏览器：繁体语系去 /tw/，英文语系去 /en/（这一页有
                  # 英文版才去）。跟过一次就写进 localStorage，之后以读者
                  # 自己点过的为准 —— 否则一个在台湾用简体的读者每次都被弹走。
                  "var L=(navigator.languages||[navigator.language||'']).join(',');"
                  "var guess=/zh-(hant|tw|hk|mo)/i.test(L)?'tw':(/zh/i.test(L)?'sc':(HAS_EN?'en':'sc'));"
                  "var want=saved||guess;"
                  "if(want!=='en'&&!HAS_EN&&cur==='en'){want='sc'}"
                  "if(want!==cur&&to[want]){location.replace(to[want]);return}"
                  # 按钮**进头部**，不浮在页面上。找得到头部就放进去，找不到
                  # （比如 404 没有 header）才退回悬浮。悬浮的坏处不只是难看：
                  # 它会一直压在聊天窗上面。
                  "document.addEventListener('DOMContentLoaded',function(){"
                  "var host=document.querySelector('.mast-links')||document.querySelector('.mast-top')"
                  "||document.querySelector('header.hd');"
                  "var box=document.createElement('div');box.id='hwx-tools';"
                  # 三种语言时不做循环按钮：一个「下一种语言」的按钮读者猜不到
                  # 点下去会去哪。改成把**你不在的那两种**并排列出来，看一眼就知道。
                  # 这一页没有英文版时自然只剩一个，和原来一模一样。
                  "var NAME={sc:'简体',tw:'繁體',en:'EN'};"
                  "var order=['sc','tw','en'];"
                  "order.forEach(function(k){"
                  "if(k===cur)return;if(k==='en'&&!HAS_EN)return;"
                  "var b=document.createElement('button');b.id='hwx-lang-'+k;b.type='button';"
                  "b.className='pill hwx-lang';b.textContent=NAME[k];"
                  "b.setAttribute('aria-label','Switch to '+NAME[k]);"
                  "b.onclick=function(){try{localStorage.setItem(K,k)}catch(e){};location.href=to[k]};"
                  "box.appendChild(b)});"
                  "if(host){host.appendChild(box);"
                  # 主题按钮原本 position:fixed 单独浮着，一并收进来并排放
                  "var t=document.getElementById('hwx-theme');if(t)box.appendChild(t);"
                  "if(host.classList.contains('hd')||host.classList.contains('mast-top'))"
                  "box.classList.add('float-in-head');}"
                  "else{document.body.appendChild(box);box.classList.add('loose')}"
                  "})"
                  "}catch(e){}})();</script>"
                  "<style>#hwx-tools{display:flex;gap:8px;align-items:center}"
                  # 头部本身 position:relative，所以贴它右上角＝跟着页面滚，
                  # 不盖正文、也不盖聊天窗
                  "#hwx-tools.float-in-head{position:absolute;top:18px;right:0}"
                  "#hwx-tools.loose{position:fixed;top:14px;right:14px;z-index:9999}"
                  "#hwx-tools .hwx-lang{height:32px;padding:0 13px;border:1px solid var(--line,#e2ddd0);"
                  "background:var(--paper,#f5f1e8);color:var(--ink,#1c1917);font:inherit;"
                  "font-size:13px;letter-spacing:.02em;line-height:30px;cursor:pointer;"
                  "border-radius:16px}"
                  "#hwx-tools .hwx-lang:hover{border-color:var(--acc,#9d2933);color:var(--acc,#9d2933)}"
                  # 收进头部之后不该再自己定位，否则会飞回右上角
                  "#hwx-tools #hwx-theme{position:static;width:32px;height:32px;margin:0;"
                  "box-shadow:none}"
                  "@media(max-width:700px){#hwx-tools.float-in-head{top:10px}}</style>"
                + HWL_B
            )
            m = re.search(r'<meta name="viewport"[^>]*>\n?', s) or re.search(r"<head[^>]*>\n?", s)
            if not m:
                continue
            s = s[:m.end()] + block + s[m.end():]
            open(path, "w", encoding="utf-8").write(s)
            n += 1
    print("语言层（hreflang + 切换 + 首访跟随）注入 %d 页 [%s]" % (n, root))
    return n
