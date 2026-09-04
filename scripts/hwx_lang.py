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
    """这个目录是不是「派生出来的语言站」—— 是的话本脚本一个字都不该碰。

    tw/ 由 build_tw.py 从简体产物整树转出，en/ 由 build_en.py 用英文数据生成。
    本脚本往页面里盖的是**简体**挂件（切换日夜模式、/assets/… 的资源路径、
    大陆支付宝收款码）。盖到 tw/ 上的后果实测过：553 页的「切換」变回「切换」、
    资源指回简体站、繁体读者的 AlipayHK 码被换成大陆码 —— 页面照样渲染，
    构建照样通过，只有逐字比对才看得出来。

    **必须按路径段比，不能按子串比。** 第一版写的是 "/tw" in dp，于是
    i/han-feizi/two-handles/ 被当成繁体目录跳过了 —— "/two-handles" 里就含
    "/tw"。这样误伤了 5 页（two-nogales、two-kinds、two-handles、
    two-ways-of-seeing、enlarging-huaihai），它们整层语言层、夜间模式、
    聊天挂件全都没有，而且没有任何报错。
    """
    segs = [x for x in dp.replace("\\", "/").split("/") if x not in ("", ".")]
    return bool(set(segs) & {".git", "tw", "en", "node_modules", "__pycache__"})


def _en_paths():
    """英文版**真实存在**的那些路径（站内绝对路径，带首尾斜杠）。

    读的是构建出来的 en/ 树，不是源数据。第一版从 seo/chapters_en/ 推，
    理由是「跟构建顺序无关」，但它推出来的是**计划**不是事实：那份数据里
    有 30 个条目，而 build_en 目前只产出章节页，条目页和首页都还没有。
    于是 hreflang 宣称 /en/ 存在，首访跟随把英文语系的读者 location.replace
    到 /en/ —— 一个 404。headless 浏览器就是这么被弹走，站点完整那道闸报
    「#hwx-tabs2 是 undefined」，看起来毫不相干。

    代价是 build_en.py 必须排在本脚本前面跑。换来的是这件事永远和事实一致：
    英文站多一页，hreflang 就多一条；没建的页一条都不会被宣称。

    这一版全站 159 个条目只上线一部分，给没有英文版的页发 hreflang="en"
    等于把搜索引擎指向 404 —— 比不发更糟。
    """
    import os
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "en")
    root = os.path.normpath(root)
    out = set()
    if not os.path.isdir(root):
        return out
    for dp, _dn, fn in os.walk(root):
        if "index.html" not in fn:
            continue
        rel = os.path.relpath(dp, root).replace(os.sep, "/")
        out.add("/" if rel == "." else "/" + rel + "/")
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
                  # **URL 里已经写了语言，就以 URL 为准。**
                  #
                  # 第一版不是这样，而是无条件跟随浏览器语言。后果实测过：
                  # 打开 /tw/i/su-shi/… 会被改写成 /i/su-shi/…，打开 /en/… 也一样
                  # —— 只要浏览器的语言列表里有 zh。也就是说**任何非默认语言的
                  # 链接都分享不出去**：台湾读者转给朋友的繁体链接、发给英文读者
                  # 的英文链接，落地全变简体。三个站都是这个毛病。
                  #
                  # 现在只在读者落在**默认语言**（无前缀）时才跟随浏览器。
                  # 落在 /tw/ 或 /en/ 是一个明确的选择，不该被猜测覆盖。
                  "if(cur!=='sc'){"
                  # 没有记过偏好的，把这次当成他的选择记下来；已经记过的不动 ——
                  # 一条别人分享的链接不该永久改掉你的语言。
                  "if(!saved){try{localStorage.setItem(K,cur)}catch(e){}}"
                  "}else{"
                  "var L=(navigator.languages||[navigator.language||'']).join(',');"
                  "var guess=/zh-(hant|tw|hk|mo)/i.test(L)?'tw':(/zh/i.test(L)?'sc':(HAS_EN?'en':'sc'));"
                  "var want=saved||guess;"
                  "if(want==='en'&&!HAS_EN){want='sc'}"
                  "if(want!=='sc'&&to[want]){location.replace(to[want]);return}"
                  "}"
                  # 按钮**进头部**，不浮在页面上。找得到头部就放进去，找不到
                  # （比如 404 没有 header）才退回悬浮。悬浮的坏处不只是难看：
                  # 它会一直压在聊天窗上面。
                  "document.addEventListener('DOMContentLoaded',function(){"
                  # 宿主不能选一个**当前正被隐藏**的容器。踩过：条目页和
                  # 章节页的 .mast-links 在 700px 以下是 display:none
                  # （页头导航在手机上收起），工具条被塞进去之后整个
                  # 尺寸为 0 —— 三种语言的条目页在手机上都没有语言切换、
                  # 也没有夜间模式开关，而桌面端一切正常。
                  # 顺序不变（桌面还是优先 .mast-links），只是跳过隐藏的。
                  "var host=null,cand=['.mast-links','.mast-top','header.hd'];"
                  "for(var ci=0;ci<cand.length;ci++){var hc=document.querySelector(cand[ci]);"
                  "if(hc&&getComputedStyle(hc).display!=='none'){host=hc;break}}"
                  "var box=document.createElement('div');box.id='hwx-tools';"
                  # 三种语言并排三个按钮，头部会被挤满（390 宽下标题、额度、
                  # 关闭三样本来就紧）。改成一个下拉：当前语言显示在上面，
                  # 点开是全部三种。
                  #
                  # 用原生 <select> 不自己画菜单：键盘操作、焦点管理、移动端的
                  # 原生选择器都是白得的，自己画一套还得把这些补回来。
                  # 代价是各平台外观略有差异，用 appearance:none 加自己的箭头
                  # 已经压掉大部分。
                  # 标签只用一个字／两个字母。原来是「简体／繁體／English」，
                  # 「English」一个词就占 87px，把 375px 的页头挤到站名
                  # 得换行才不被压住。原生 <select> 收起和展开显示的是
                  # 同一份文字，所以短标签是列表里也短 —— 语言选择器的
                  # 惯例本来就是「每一项用它自己的语言写」，简／繁／EN
                  # 三个都认得出，只读英文的人也认得出 EN 那一项。
                  "var NAME={sc:'简',tw:'繁',en:'EN'};"
                  "var sel=document.createElement('select');sel.id='hwx-lang';"
                  "sel.setAttribute('aria-label','Language');"
                  "['sc','tw','en'].forEach(function(k){"
                  "if(k==='en'&&!HAS_EN)return;"
                  "var o=document.createElement('option');o.value=k;o.textContent=NAME[k];"
                  "if(k===cur)o.selected=true;sel.appendChild(o)});"
                  "sel.onchange=function(){var k=sel.value;if(k===cur)return;"
                  "try{localStorage.setItem(K,k)}catch(e){};location.href=to[k]};"
                  "var wrap=document.createElement('span');wrap.className='hwx-lang-wrap';"
                  "wrap.appendChild(sel);box.appendChild(wrap);"
                  "if(host){host.appendChild(box);"
                  # 主题按钮原本 position:fixed 单独浮着，一并收进来并排放
                  "var t=document.getElementById('hwx-theme');if(t)box.appendChild(t);"
                  # .mast-top 本身是一行 flex（站名在里面），把工具条当
                  # 这一行的最后一个 flex 项推到右边就行 —— 不用绝对定位，
                  # 也就**结构上不可能**压住站名。header.hd 是 relative，
                  # 那里继续用绝对定位（桌面端那一版的位置没变）。
                  "if(host.classList.contains('mast-top'))"
                  "box.classList.add('in-row');"
                  "else if(host.classList.contains('hd'))"
                  "box.classList.add('float-in-head');}"
                  "else{document.body.appendChild(box);box.classList.add('loose')}"
                  "})"
                  "}catch(e){}})();</script>"
                  "<style>#hwx-tools{display:flex;gap:8px;align-items:center}"
                  # 头部本身 position:relative，所以贴它右上角＝跟着页面滚，
                  # 不盖正文、也不盖聊天窗
                  "#hwx-tools.float-in-head{position:absolute;top:18px;right:0}"
                  "#hwx-tools.loose{position:fixed;top:14px;right:14px;z-index:9999}"
                  "#hwx-tools .hwx-lang-wrap{position:relative;display:inline-flex}"
                  # 自己画箭头：appearance:none 之后原生箭头没了，不补一个
                  # 读者看不出这是可点开的。
                  "#hwx-tools .hwx-lang-wrap::after{content:'';position:absolute;"
                  "right:11px;top:50%;width:5px;height:5px;margin-top:-3px;"
                  "border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;"
                  "transform:rotate(45deg);opacity:.55;pointer-events:none}"
                  "#hwx-lang{height:32px;padding:0 26px 0 13px;border:1px solid var(--line,#e2ddd0);"
                  "background:var(--paper,#f5f1e8);color:var(--ink,#1c1917);font:inherit;"
                  "font-size:13px;letter-spacing:.02em;line-height:30px;cursor:pointer;"
                  "border-radius:16px;-webkit-appearance:none;-moz-appearance:none;appearance:none}"
                  # 不用红：胭脂红是这个站的印章色，只该出现在「重点」上。
                  # 而 select 选完之后焦点还在它身上，红环就一直挂着不走，
                  # 看上去像是这里出了错。hover/focus 都改成墨色深一档。
                  "#hwx-lang:hover{border-color:var(--rule-2,#d0c9b8)}"
                  "#hwx-lang:focus-visible{outline:2px solid var(--ink,#1c1917);outline-offset:2px}"
                  "#hwx-lang:focus:not(:focus-visible){outline:none}"
                  # 展开的菜单项由系统画，深色模式下要显式给底色，
                  # 否则 Chrome 会用白底黑字，和页面反差刺眼。
                  ":root[data-theme=\"dark\"] #hwx-lang option{background:#1d1913;color:#eae3d4}"
                  # 收进头部之后不该再自己定位，否则会飞回右上角
                  "#hwx-tools #hwx-theme{position:static;width:32px;height:32px;margin:0;"
                  "box-shadow:none}"
                  "#hwx-tools.in-row{margin-left:auto;align-self:flex-start;flex:0 0 auto}"
                  # 绝对定位的工具条不占位，站名一长就从它底下穿过去：
                  # 中文站名 375px 下压 28px，英文「Human World Rules」压
                  # 64px（「Rules」半个词看不见）。
                  #
                  # 限的必须是**宽度**，不是内边距：站名是 flex 项、宽度按内容
                  # 算，加 padding-right 只是把盒子撑大，右边缘一点没退，
                  # 重叠反而从 64px 变成 87px（整个下拉框）。
                  #
                  # 而且百分比在这里也不行：max-width:calc(100% - 190px) 的
                  # 100% 是按父元素宽度算的，父元素又是 shrink-to-fit ——
                  # 宽度取决于这个子元素，循环，最后算出 27px，站名断成
                  # 「Human / World / Rules」三行。所以用视口单位：
                  # 两侧各 24px 内边距 + 40px 图标 + 12px 间距 + 工具条约 114px
                  # ≈ 220px，再留 12px 别让站名贴着下拉框。375px 下给站名 143px，「Human World」
                  # 一行、「Rules」一行；414px 以上一行就放得下。
                  "@media(max-width:760px){#hwx-tools.float-in-head{top:10px}"
                  "#hwx-lang{padding:0 22px 0 10px;font-size:12.5px}"
                  ".hd .hd-title,.hd .wordmark{max-width:calc(100vw - 232px)}}</style>"
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
