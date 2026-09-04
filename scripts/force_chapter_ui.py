#!/usr/bin/env python3
# Patch generators AND already-built HTML so highlight/sidebar cannot miss.
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SLOGAN_TEXT = "遇到事了，看看以前的人怎么处理"
STYLE = (
    '<style id="hw-force">'
    'mark,mark.hl{background:transparent!important;color:#9d2933!important;'
    'font-weight:700!important;text-decoration:none!important;}'
    '@media (max-width:900px){aside.side{display:none!important}'
    '.layout{grid-template-columns:1fr!important}}'
    '</style>'
)
MARK_OPEN = (
    '<mark class="hl" style="background:transparent;color:#9d2933;font-weight:700;'
    'text-decoration:none">'
)

# 读完之后的收尾块：条目页与章节页共用。
# 文案避开「觉得有用请分享」这种索取式说法——那是替网站要东西。
# 改成把动作说成读者自己的事：他刚获得了一个可用的想法，
# 分享是「把它给到那个正需要的人」，收藏是「下次遇到还找得到」。
OUTRO_CSS = (
    '<style id="hw-outro">'
    '.hw-outro{margin:38px 0 8px;padding:22px 20px;border-radius:16px;'
    'background:var(--surface-2,#f2ece0);text-align:center}'
    '.hw-outro p{font-family:"Noto Serif SC","Songti SC","STSong",serif;'
    'font-size:16px;line-height:1.9;margin:0 0 4px;color:var(--ink)}'
    '.hw-outro small{display:block;font-size:13px;color:var(--muted);'
    'line-height:1.8;margin-bottom:14px}'
    '.hw-outro .acts{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}'
    '.hw-outro .acts button{border:1px solid var(--ink);background:var(--ink);'
    'color:var(--paper,#f7f4ec);border-radius:999px;padding:6px 18px;cursor:pointer;'
    'font-family:"Noto Serif SC","Songti SC",serif;font-size:13px;line-height:1.6}'
    '.hw-outro .acts button:active{transform:scale(.97)}'
    '</style>'
)


# 「请我喝茶」：仓库里有支付宝收款图（assets/pay-alipay.png）才构建按钮和脚本；微信码
# （assets/pay-wechat.png）可选；支付宝收款链接放 assets/pay.json 的 alipayLink（从码里解出来的）。
# 没图就一个字都不出现——半成品不上线。位置只在读完之后的收尾块，跟分享并排。
import os as _os, json as _json
_ASSETS = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "assets")
TEA_ON = _os.path.exists(_os.path.join(_ASSETS, "pay-alipay.png"))          # 支付宝码是底线
TEA_WECHAT = _os.path.exists(_os.path.join(_ASSETS, "pay-wechat.png"))      # 微信码可选，没有就在微信里也给支付宝码
try:
    TEA_ALIPAY_LINK = _json.load(open(_os.path.join(_ASSETS, "pay.json"), encoding="utf-8")).get("alipayLink", "")
except Exception:
    TEA_ALIPAY_LINK = ""


def outro_html(title, url, text):
    return (
        '<div class="hw-outro">'
        '<p>这一篇如果说中了你正在经历的事，</p>'
        '<small>转给可能需要的人，或者存下来，下次好找。</small>'
        '<div class="acts">'
        '<button type="button" data-share '
        'data-share-title="%s" data-share-url="%s" data-share-text="%s">分享给朋友</button>'
        + ('<button type="button" data-tea>请我喝杯茶</button>' if TEA_ON else '')
        + '</div></div>'
    ) % (title, url, text)


OUTRO_JS = ""   # 收藏按钮已移除，不再需要


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
        # 读完之后的收尾块——正文结束处，不是页脚
        if "hw-outro" not in s:
            m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
            _t = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "人类世界生存法则"
            _u = "https://ourword.ai" + "/" + str(path.parent.relative_to(ROOT)) + "/"
            _u = _u.replace("//", "/").replace("https:/", "https://")
            _blk = outro_html(_t + " — 人类世界生存法则", _u, _t)
            for _tail in ('</section>\n</article>', '</div>\n</article>', '</article>'):
                if _tail in s:
                    s = s.replace(_tail, _blk + _tail, 1); break
            else:
                s = s.replace("</main>", _blk + "</main>", 1)
            s = s.replace("</head>", OUTRO_CSS + "</head>", 1)
        if s != orig:
            path.write_text(s, encoding="utf-8")
            n += 1
    print("force_chapter_ui html", n)

if __name__ == "__main__":
    patch_html()


# HWX v3: 最新 tab + 瀑布流混排 + 今日三样 + 历史行 + 暗色双主题
HWX_A, HWX_B = "<!--HWX:FIND-->", "<!--/HWX:FIND-->"

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))  # CI 从仓库根调用本脚本
# 英文站换一份处境表（hwx_scenes_en），其余渲染逻辑一个字不改。
HWX_SCENES = __import__(_os.environ.get("HW_SCENES", "hwx_scenes"),
                        fromlist=["SCENES"]).SCENES
from quote_asks import QUOTE_ASKS

# 悬浮球问答的后端地址。空字符串＝功能关闭（前端不渲染任何东西）。
# 2026-09-01 上线。Worker 名字是控制台随机生成的，不好看但只影响这一行；
# 改名要删了重建，不值当。key 存在 Worker 的 HW_CHAT_KEY secret 里，不进浏览器。
# 跨站调用由 Worker 的 Origin 白名单挡（fail-closed），跟同不同源无关。
HW_CHAT_ENDPOINT = "https://wandering-wind-0168.djjian.workers.dev"

# 处境的短标签：首页「今日一问」右上角那个跳转标签只放得下四个字。
# 112 个处境里 63 个原名超过 4 字，逐个手写——截断会出「一个能约」这种废话。
# 今日一问下面那个框里预填的整句，一个处境一句，全部手写。
#
# 为什么不能拿卡片上那句问句去拼：那句话已经在屏幕上了，框里再出现一次，
# 读者三厘米之内读到同一句，卡片就从「这就是我」塌成一个表单默认值。
#
# 所以每句写成两半：前半说卡片没说的那一半——这件事正在把我怎么样
# （「一整天都在切换，什么都没往前推」「翻了一遍通讯录，一个都发不出去」），
# 后半是一句答得上来的请求。共情在前半，能聊下去在后半。
# 前半必须是代价不是事实：事实卡片已经讲过了，代价才是他没说出口的那句。
SC_BOX = {
# 要做决定
"情绪上头":"我现在整个人是绷着的，怕一开口就把事做死。先怎么办？",
"做不完":"事情堆成一片，我一整天都在切换，什么都没往前推。今天先动哪一件？",
"起了冲突":"我跟他已经杠上了，现在每句话都在加码。我该怎么收？",
"拖着不开始":"这件事我拖了很久，每天都在想它，就是没动。今天怎么起头？",
"不可逆的决定":"这一步走出去就回不了头，我反复算还是不敢按。我该怎么判断？",
"信息不全":"该知道的我都不知道，可期限就在那儿。这种情况我怎么定？",
"方案被否":"被否之后我一直在想是不是我的问题，也不敢再提。我下一步该怎么走？",
"全票通过":"大家都说好，我却越听越不踏实，又说不出哪儿不对。我该怎么验？",
# 有对手
"对手更强":"正面我肯定打不过，可这仗又躲不掉。我还有什么打法？",
"被牵着走":"他每动一下我就得跟着动，我自己的事一件都推不了。怎么把节奏抢回来？",
"进不进红海":"这块地方已经杀成一片，可我看不到别的入口。我该进还是绕开？",
"赢了之后":"最近几把都赢了，我现在下手比以前重，自己都觉得不对。我该怎么办？",
# 钱的事
"投资在亏":"这笔一直在亏，我每天一开盘就心慌，也不肯认。我该怎么办？",
"该不该买":"我心里其实已经想买了，找的理由全在帮自己。我该怎么判断？",
"怕错过":"看着别人一天天赚，我坐不住了。这件事我该怎么想？",
"让钱生钱":"我的钱全靠自己上班换，人一停就断了。我该先动哪一步？",
"接不到活":"活越来越少，我开始不敢花钱了。我先做什么？",
"钱不够":"钱一紧我整个人就窄了，眼里只剩这个月。我该先动哪一笔？",
# 跟人打交道
"这人可信吗":"我得把事交给他，可心里一直有个疙瘩，说不上为什么。我该看什么？",
"上面说的话不能信":"他答应过的一次也没兑现，我现在听什么都自动打折。我该怎么办？",
"要说服人":"道理我都摆完了，他还是不动，我快没耐心了。这话我该怎么说？",
"谈条件":"我们卡住了，谁先松口谁像输。我该怎么开口？",
"被猜忌":"我能感觉到别人在防着我，可我什么都没做。我该怎么处理？",
"两个都想要":"两边我都舍不得，可只能留一个。我该怎么选？",
"信不信直觉":"我心里有个说法，数据却不支持。我该听哪个？",
"定不好价":"我一直不敢开价，怕报高了人就走了。我该怎么定？",
"遇上不讲理":"对面根本不接话，只想赢，我硬顶又怕把自己拖脏。我该怎么办？",
"功劳被抢":"活是我一个人干下来的，报上去却成了别人的成绩。这话我该怎么说？",
"该不该妥协":"退一步事情就能成，可我心里过不去。我该怎么办？",
"总在讨好别人":"我总是先答应下来，回头一个人难受。我该怎么改？",
"推不动别人":"事情卡在别人那儿，我催了几轮还是原地不动。我还能做什么？",
"合伙人闹掰":"我们已经说不到一块了，可这摊事还得一起做。我该怎么谈？",
"觉得没意义":"日子一天天过去，我说不上自己图的是什么。我该先想清楚什么？",
"要不要跳槽":"留着不甘心，走了又怕更差。我该怎么判断？",
"信错了人":"那件事之后，我对谁都先留一手，自己也累。我该怎么办？",
"一个能约的人都没有":"我想找个人说说话，翻了一遍通讯录，最后谁也没点开。我先做什么？",
# 带人
"错反复犯":"同一个问题反复出，我说了很多遍也没用。我该先改哪一处？",
"下不了手":"要处理的偏偏是最早跟着我的那个，我拖了好几个月。我该怎么做？",
"团队没劲":"交代下去都会照办，可没有一个人是主动的，我自己也提不起劲。我该先改哪一处？",
"招人换人":"这个人到底留不留，我拖了很久没定。我该看哪几点？",
"听不到实话":"报上来的全是好消息，出事都是最后才知道。我该怎么办？",
"队伍出不了活":"人都不差，交上来的东西就是不行。我该先动哪一步？",
# 把事做成
"从零开始":"手里什么都还没有，我不知道第一步该重还是该轻。我先做什么？",
"推不动":"我使了很久的劲，几乎没有回响，开始怀疑是不是方向错了。我该先动哪一步？",
"扩不扩张":"机会摆在那儿，可我怕铺出去以后养不住。我该怎么判断？",
"成本降不动":"明面上的都抠完了，再压就要伤到人和货。我下一刀该往哪儿切？",
"顺境里发慌":"越是没出事，我心里越不踏实，又说不上在怕什么。我现在该做什么？",
"做的东西没人看":"做出来没什么人看，我开始怀疑还有没有必要做。我该怎么办？",
# 自己的状态
"在低谷":"这段时间什么都不顺，我把自己关起来了。先做什么能好一点？",
"想太多":"同一件事我能来回想一整夜，越想越糟。我怎么停下来？",
"知道做不到":"道理我全懂，可到了当下我还是老样子。先做什么能好一点？",
"学不进去":"看的时候都懂，用的时候一个也想不起来。我该怎么练？",
"忙到没自己":"从早排到晚，回头一看全是替别人跑的腿。我该砍掉什么？",
"被比下去":"身边人好像都比我稳、比我快，我一直在后面追。我该怎么想这件事？",
"不想卷但怕掉队":"我不想再这么熬下去，可一慢下来就心慌。我该怎么办？",
# 进退取舍
"该不该接":"位置递到我手上了，好处一眼看得见，坏处要出事才知道。我该进还是该退？",
"该不该退":"我心里清楚差不多了，可真到要放手那一下就下不了决心。我该怎么退？",
"要立规矩":"我立的规矩，执行两周就松回去了，现在连我都懒得再提。我该先改哪一处？",
"看不清大势":"我分不清眼下是刚开场还是已经到了尾巴，做什么都心里没数。我该往哪边走？",
# AI 来了
"我这行会不会没了":"我这行现在还养得活我，可我不知道还剩几年。我现在该练什么？",
"追不上新东西":"每次刚熟悉一点，前面又换了一茬，我很累。我现在该练什么？",
"手艺不值钱了":"我练了很多年的东西，现在几秒就做出来了。我现在该练什么？",
"工具替我想了":"习惯了先让它给个答案，我自己那步慢慢不走了。我现在该练什么？",
"出得多了人却空了":"我一天能交出去的东西比过去多好几倍，人反而是麻的。我该怎么办？",
"人人都在喊风口":"身边每个人都在往里冲，我怕自己是最后一个进场的。我该怎么想？",
"要不要现在跳进去":"我想进去，又觉得不是太早就是太晚。我该怎么判断？",
"日子被工具占满":"从早到晚都在回消息，一件完整的事都做不成。我先做什么？",
"不知道该练什么了":"昨天还算本事的东西今天就不值钱了，我不知道往哪儿使劲。我现在该练什么？",
# 家里的事
"跟伴侣吵":"我们绕来绕去还是那一件事，每次都以更难看的话收场。我该怎么说？",
"孩子不听":"他现在听不进我说的，最后总是变成吵架。这话我该怎么说？",
"孩子不说话":"我连他今天过得怎么样都不知道，问了也只有一个字。我该怎么办？",
"被家人的情绪裹着":"家里的情绪一上来我就被卷进去，好几天缓不过来。我该怎么办？",
"父母催得紧":"一说到这事我们就翻脸，可我又不想伤他们。这话我该怎么说？",
"身边人不敢跟我说真话":"他们只跟我报好的，坏消息总是绕过我。我该先改哪一处？",
"家里的活没人算":"这些活加起来比上班还长，可在家里它不算数。这话我该怎么说？",
"照顾老人":"我一边照顾他，一边把自己耗空了。我今天能先做哪一件？",
"被背叛了":"我嘴上说过去了，可每次想起来还是堵。我该怎么办？",
"在一起久了没感觉":"我们像合租的室友，各忙各的，谁也不问谁。我该怎么办？",
# 身体与精力
"睡不好":"一关灯脑子就开始过电影，翻来覆去到三四点。我今天能先做哪一件？",
"精力跟不上":"我撑到下午就空了，全靠咖啡顶着。我今天能先做哪一件？",
"坐不住":"我坐不到十分钟就想去摸手机。我今天能先做哪一件？",
"想改个习惯":"我靠的一直是那股劲，劲一过就回到原样。这回怎么做才不一样？",
"长期紧绷":"我好像忘了不使劲是什么感觉，肩膀一直是硬的。我今天能先做哪一件？",
"想戒又戒不掉":"每次都在同一个时间点上失守，第二天再重来。我该怎么办？",
"干不动了":"不是忙不过来，是心里那股劲没了，做什么都没反应。我今天能先做哪一件？",
"时间不够用":"时间全被别人的事占满了，轮到我自己的就没了。我该先夺回哪一段？",
"病了":"报告拿到手里，我放了三天没敢打开。我今天能先做哪一件？",
# 刚起步
"一路优秀，突然没了标准":"我一直是靠达标活着的，现在没有标可以达了。我该先做什么？",
"第一份工作":"我坐在这儿不知道该干嘛，也不敢老去麻烦人。我该先做什么？",
"要不要接着读书":"继续念书还是先进去做，这一步我怕走反了。我该怎么判断？",
"学的用不上":"课上会做的题，到了真事上一件也接不上。我该先练什么？",
# 人生转弯
"突然没了工作":"一夜之间我没了去处，明天早上不知道该干什么。接下来我先做什么？",
"重要的人走了":"他不在了以后，我一直没接上，日子空了一大块。接下来我先做什么？",
"要重新开始":"前面那些年等于清零，我这个岁数再来一次，心里很虚。接下来我先做什么？",
"扛不动了":"这副担子只有我一个人扛，放又放不下。接下来我先做什么？",
"换个地方重来":"换了地方之后，我一个人都不认识。接下来我先做什么？",
"人到中年":"外面看我样样都齐了，只有我知道里面是空的。接下来我先做什么？",
# 使不上劲
"事情我说了不算":"这件事的决定权不在我手上，我只能在旁边干着急。这种时候我还能做什么？",
"已经改不了了":"事情已经这样了，可我脑子里一遍遍重放。这种时候我还能做什么？",
"努力也没用":"能做的我全做了，局面一点没动。这种时候我还能做什么？",
"一直没成":"这件事我从很早就开始做，到今天还差最后一口气。这种时候我还能做什么？",
"被晾在一边":"我经手的事一件比一件轻，重要的会已经没我了。这种时候我还能做什么？",
# 回头与往前
"主线没成副业成了":"正经做的那件不温不火，随手做的反倒起来了。我该往哪边走？",
"那件事一直搁在心里":"过去很多年了，一想起来我还是难受。我该怎么把它翻过去？",
"不知道要什么":"问我想过什么日子，我答不上来，只知道现在这样不对。我该往哪边走？",
"路太多，选不出来":"摆在面前的都不算错，正因为都不错我一直没动。我该往哪边走？",
"要不要现在转向":"眼下这摊子还转得动，可我心里清楚它不是我要的。我该往哪边走？",
# 说不出口
"看不得别人好":"听到身边人的好消息，我第一反应居然是难受。我该怎么办？",
"我做错了事":"那件事我到现在都没跟人提过，一想起来就烫。这话我要不要说出口？",
"怕被看穿":"我总觉得自己是混进来的，早晚要露馅。我该怎么办？",
"放不下一个人":"都这么多年了，我还是会突然想到他。我该怎么办？",
"开始怕死":"一到夜里这个念头就上来，压都压不住。我该怎么办？",
}

# 手写的那 10 张 QQ 不来自处境层，本来没有处境标签也没有预填句。
# 它们各自对应一个已有处境，挂上去就行——不然这 10 天卡片会缺一块。
QQ_SC = {
"方案被毙了，还要不要提第二次？":"方案被否",
"连赢三把，加仓还是收手？":"赢了之后",
"亏着的仓位，砍还是扛？":"投资在亏",
"对面比我强十倍，怎么打？":"对手更强",
"被当众激怒，第一反应做什么？":"情绪上头",
"团队同一个错犯第三遍了，怪谁？":"错反复犯",
"看不清方向的时候，先做什么？":"看不清大势",
"这个人能不能信？":"这人可信吗",
"从零开始，第一步做重的还是轻的？":"从零开始",
"现在是该退场的时候吗？":"该不该退",
}

SC_SHORT = {
"拖着不开始":"迟迟不动","不可逆的决定":"不可逆","进不进红海":"进红海","这人可信吗":"这人可信",
"上面说的话不能信":"话不能信","听不到实话":"没有实话","队伍出不了活":"出不了活","成本降不动":"降不动",
"顺境里发慌":"顺境发慌","做的东西没人看":"没人看","知道做不到":"做不到","忙到没自己":"没有自己",
"不想卷但怕掉队":"不想卷","看不清大势":"大势不明","我这行会不会没了":"这行没了","追不上新东西":"追不上",
"手艺不值钱了":"手艺贬值","工具替我想了":"不会想了","出得多了人却空了":"多而空","人人都在喊风口":"都喊风口",
"要不要现在跳进去":"要不要跳","日子被工具占满":"时间被占","不知道该练什么了":"练什么","两个都想要":"都想要",
"信不信直觉":"信不信","遇上不讲理":"不讲理","该不该妥协":"该妥协吗","总在讨好别人":"总在讨好",
"推不动别人":"推不动人","合伙人闹掰":"合伙闹掰","觉得没意义":"没有意义","要不要跳槽":"跳不跳槽",
"一个能约的人都没有":"没人可约","孩子不说话":"孩子不说","被家人的情绪裹着":"家里情绪","父母催得紧":"父母在催",
"身边人不敢跟我说真话":"没有真话","家里的活没人算":"家务不算","在一起久了没感觉":"没感觉了","精力跟不上":"精力不够",
"想改个习惯":"改变习惯","想戒又戒不掉":"戒不掉","时间不够用":"时间不够","一路优秀，突然没了标准":"没了标准",
"第一份工作":"刚上班","要不要接着读书":"要不要读","学的用不上":"学的没用","突然没了工作":"没了工作",
"重要的人走了":"有人走了","要重新开始":"重新开始","换个地方重来":"换个地方","事情我说了不算":"说了不算",
"已经改不了了":"改不了了","努力也没用":"努力没用","主线没成副业成了":"副业成了","被晾在一边":"被晾一边",
"看不得别人好":"见不得好","我做错了事":"我做错了","放不下一个人":"放不下","那件事一直搁在心里":"搁在心里",
"不知道要什么":"要什么","路太多，选不出来":"选不出来","要不要现在转向":"要不要转",
}

HWX_INTROS = {
"kasparov":"1997 年输给深蓝的世界冠军，第二年把电脑请上了自己的赛场",
"wiener":"控制论的提出者，1949 年主动写信给汽车工人工会提醒自动化",
"hot-metal":"1978 年 7 月 1 日那一夜，一门养了几代人的排字手艺结束了",
"sima-qian":"受腐刑之后活下来写完《史记》的人，报任安书里说了为什么",
"shi-tiesheng":"二十一岁瘫痪、后半生透析写作三十年——「职业是生病，业余在写作」",
"i-ching":"六十四卦讲的都是同一件事：什么时候该动，什么时候该等",
"montaigne":"四百年前把自己的怯懦、病和怕死写成书的人",
"tao-yuanming":"当了八十天县令就走，然后穷了一辈子也没回头",
"cs-lewis":"妻子死后几个月的日记，没整理成道理",
"ohno":"在丰田车间里把「问五次为什么」「谁都能停线」做出来的人",
"augustine":"「赐我贞洁，但不是现在」——一千六百年前把拖延写透的人",
"arendt":"在法庭上看见「不思考」是什么样；三十五岁到纽约不会英文，从头开始",
"fukuzawa":"学了几年荷兰语，到横滨一看招牌全是英文，当天决定重学",
"du-fu":"长安十年没成，四十八岁弃官入蜀，最好的诗写在这之后",
"chu-shijian":"七十四岁上山种橙，等了五年第一次结果",
"churchill":"丢了官的十年靠写书养家，六十五岁当上首相",
"curie":"丈夫死后第七个月，她从他讲停的地方接着讲",
"caigentan":"明代三百多条语录，讲人前人后怎么过日子",
"bhagavad-gita":"阵前一个人扔下弓，论了十八章他才动",
"sun-tzu":"最早也最完整的战争方法论，被读了两千五百年",
"adler":"把「这是谁的课题」问成一把刀的心理学家",
"csikszentmihalyi":"给几千人配呼叫器，找出人什么时候最投入",
"sapolsky":"在东非看了三十年狒狒，讲清压力如何伤人",
"bj-fogg":"斯坦福行为设计实验室，把习惯缩到不会失败",
"satir":"家庭治疗开创者，让全家站起来摆成雕塑",
"bowen":"提出自我分化：既在关系里，又是自己",
"thomas-gordon":"罗杰斯的学生，把倾听拆成父母能照做的步骤",
"vygotsky":"三十七岁去世，留下最近发展区这个概念",
"dweck":"成长型思维的提出者，效应比流行说法小得多",
"brene-brown":"把羞耻和内疚拆开的人：一个指着行为，一个指着你",
"pu-songling":"考了四十年没中，顺手写的《聊斋》成了——他不知道",
"perel":"伴侣治疗三十年：什么都好、就是没感觉了，是怎么回事",
"maslach":"倦怠量表的提出者：该修的是工作，不是人",
"jung":"把一生分成上午和下午，两段的题目不一样",
"rat-park":"把笼子换成公园，老鼠就不那么想喝吗啡水了",
"kleinman":"照护研究的权威，照顾患病妻子十年才知道有多难",
"murakami":"关了酒吧去写小说，用跑步的办法写了三十年",
"harvard-study":"跟了八十多年：让人晚年好过的不是钱，是关系",
"cacioppo":"孤独研究者：它是信号不是缺陷，像饿一样",
"konnikova":"骗局研究者：骗子不制造信任，他用你已经有的需要",
"granovetter":"弱连接的发现者：机会从不常见面的那些人那儿来",
"scarcity":"缺钱缺时间抢的是同一份脑子：不是不理性，是带宽被占满",
"kristin-neff":"把自我关怀做成可测量的东西：三个零件，少一个就变味",
"hochschild":"把家务和「装出来的情绪」算成劳动的社会学家",
"kevin-kelly":"不用红也能活：一千个铁杆粉丝，前提是中间不能有人",
"excellent-sheep":"在耶鲁教了十年，写下对精英教育的批评",
"cal-newport":"论证专注为何正在变成稀缺能力",
"feynman":"用一杯冰水戳穿NASA几百页报告的物理学家",
"carl-rogers":"第一个把心理治疗全程录音拿来做研究的人",
"attachment-theory":"从婴儿重聚那一刻看出一生关系模板",
"atomic-habits":"把改变拆到每天百分之一的行为设计",
"popper":"用「能不能被推翻」划开科学与空话",
"ericsson":"证明决定水平的是练法不是时长",
"montessori":"用环境替代管教的儿童教育奠基者",
"john-ratey":"把运动重新定义为大脑的药",

"nonviolent-communication":"把吵架拆成四步的沟通课",
"seneca":"在权力核心里写节制的斯多噶派",
"chris-voss":"谈判先处理情绪的FBI首席专家",
"gottman":"用实验室数据预测婚姻存亡的心理学家",
"crucial-conversations":"研究了两万人怎么把难谈的话谈成",
"mao":"从绝对弱势打到全局翻盘的战略操盘手",
"su-yu":"敢三次电报推翻上级部署的战役指挥员","tao-te-ching":"五千字讲透以柔克刚的元典",
"wang-yangming":"把「知道做不到」判为不知道的心学宗师","zeng-guofan":"资质平平、靠笨功夫成大事的标本",
"fan-li":"三次散尽家财三次重来的商圣","han-xin":"用兵如神却死于收场的名将",
"liu-bang":"承认部下都比自己强的开国皇帝","cao-cao":"乱世里只认结果不认出身的组织者",
"sima-yi":"靠熬和忍拿走天下的终局玩家","zhuge-liang":"把承诺执行到死的丞相",
"guan-zhong":"先解决吃饭再谈道德的第一名相","buffett":"把复利和常识做到极致的股东信作者",
"munger":"用上百个思维模型避蠢的巴菲特搭档","li-ka-shing":"九成时间在想失败的华人首富",
"jobs":"靠砍产品线救活苹果的产品独裁者","zhang-yiming":"把延迟满足做成方法的字节创始人",
"duan-yongping":"「本分」二字管一生的企业家","inamori":"两造世界五百强、再救日航的经营者",
"musk":"把一切拆到物理事实重算的造火箭者","huang":"专挑还不存在的市场下注的英伟达掌舵人",
"thiel":"专问「重要而无人同意」问题的逆向投资人","ren-zhengfei":"在最好年景写《华为的冬天》的创始人",
"sovereign-individual":"1997年预言数字货币与远程工作的奇书","zhang-liang":"功成身退教科书级别的帝王师",
"li-bi":"四朝辅政却坚决不要官位的白衣宰相","han-feizi":"不指望人性善的制度设计师",
"huo-qubing":"不读兵书只看战场的少年名将","li-shimin":"把逆耳之言制度化的皇帝",
"socrates":"承认自己无知的提问之父","marcus-aurelius":"一边打仗一边写自省笔记的皇帝",
"machiavelli":"只写人如何做、不写应如何做的政治解剖者","dalio":"把破产教训写成《原则》的桥水创始人",
"taleb":"专研黑天鹅与反脆弱的风险哲学家","naval":"把财富与运气讲成算法的硅谷天使",
"wang-xing":"只看核心、不设边界的美团创始人","strategies-of-the-warring-states":"纵横家的话术与人心案例库",
"analects":"被用了两千年的做人做事底层代码","sapiens":"用「虚构」一词解释人类协作的畅销书",
"wang-jian":"灭楚之前先自污求田宅的老将","xiang-yu":"赢了所有战役、输掉天下的霸王",
"wu-zetian":"破格用人也快速弃人的女皇","zhu-yuanzhang":"缓称王、熬死群雄的开国者",
"zhang-juzheng":"用考成法逼动整个官僚系统的改革家","su-shi":"被贬到哪就把日子过好到哪的大文豪",
"nietzsche":"专拆现成价值观的锤子哲学家","frankl":"从集中营带出意义疗法的心理学家",
"soros":"靠认错速度盈利的宏观投机者","influence":"拆解六种顺从开关的说服科学",
"innovators-dilemma":"解释好公司为何死于好管理的经典","guo-jia":"算人心比算兵力更准的谋士",
"bruce-lee":"把武术拆到「像水」的截拳道创始人","records-of-the-grand-historian":"功过同录的史家绝唱",
"zizhi-tongjian":"写给管理者的一千三百年案例集","gandhi":"用一撮盐动摇帝国的非暴力者",
"einstein":"在专利局改写物理学的问题重构者","shang-yang":"徙木立信再推变法的立规者",
"caesar":"把宽赦用作武器的内战赢家","mandela":"把审判变成讲台的和解者",
"napoleon":"在局部永远保持多数的用兵大师","musashi":"六十余战不败的孤剑客",
"zhuangzi":"把「无用」讲成活路的逍遥派","guo-ziyi":"功高震主却得善终的中兴名将",
"franklin":"把美德排进日程表的自我管理鼻祖","graham":"发明市场先生与安全边际的价值投资之父",
"livermore":"四起四落写下投机圣经的作手","thinking-fast-and-slow":"把人类判断的漏洞列成清单的心理学",
"crowd":"一百年前写透群体失智的社会心理学","bezos":"永远把公司留在第一天的长期主义者",
"thinking-in-systems":"教人先看结构再怪人的系统论入门","old-regime":"解释革命为何在松绑时爆发的史学经典",
"on-war":"把战争定义为政治延续的军事哲学","schelling":"证明自缚双手反而更强的博弈论者",
"hu-xueyan":"靠信用起家也毁于一注的红顶商人","wealth-of-nations":"用晚餐和扣针讲清市场的经济学开山",
"epictetus":"只管自己能控之事的奴隶哲学家","bai-gui":"人弃我取的商业鼻祖",
"grove":"只有偏执狂才能生存的英特尔舵手","technological-revolutions":"证明泡沫写在剧本里的技术史框架",
"marks":"不预测、只定位的周期观察者","feng-dao":"历五代十帝而善终的争议宰相",
"huineng":"不识字却讲透顿悟的禅宗六祖","simons":"让模型代替人交易的量化之王",
"lynch":"在商场里找十倍股的基金经理","art-of-worldly-wisdom":"三百年前的处世三百则",
"why-nations-fail":"用一墙之隔的双城解释贫富的制度经济学","lee-kuan-yew":"只问管不管用的新加坡设计师",
"boyd":"提出OODA循环、终身上校的空战理论家","guiguzi":"教人先听后说的纵横家祖师",
"la-rochefoucauld":"三百年前把人心写成箴言的公爵","paul-graham":"教创业者先做不能规模化之事的YC创始人",
"matsushita":"立志让电器便宜如自来水的经营之神","finite-and-infinite-games":"分清两种游戏的哲学小书",
"guns-germs-steel":"把文明差距归因于起跑线的地理史观","mencius":"把民心定为权力地基的亚圣",
"xunzi":"主张制度驯化人性的现实派儒家","drucker":"发明「管理学」这门学科的人",
"hayek":"证明知识无法集中的经济学家","bismarck":"铁血开国又急刹车的首相",
}

CAT_COLOR = {
    "谋略与竞争":"#a33b2e",
    "权力与组织":"#7d5a3c",
    "财富与风险":"#8a6d2f",
    "创业与产品":"#c26b3f",
    "识人与相处":"#5f7355",
    "心智与情绪":"#4e6b7a",
    "学习与成长":"#4a7c6f",
    "身心与生活":"#7a6a8a",
    "家庭与关系":"#a35f6e",
    "世界如何运转":"#6b5b73",
}

def _tint(hex_color, alpha):
    """把类别色化成极淡的底色——只用来区分门类，不能抢正文。"""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "rgba(%d,%d,%d,%.3f)" % (r, g, b, alpha)

CAT_TINT = {k: _tint(v, 0.055) for k, v in CAT_COLOR.items()}      # 亮色底
CAT_TINT_D = {k: _tint(v, 0.16) for k, v in CAT_COLOR.items()}     # 暗色底

# 用户搜的是口语（睡不着、拖延、吵架），内容里写的是书面语。索引只存正文，
# 这类查询必然落空。试过按词频自动关联，结果「拖延」命中张居正和《战争论》——
# 词频匹配不出主题。改为显式指定：一个口语词挂到哪几个条目，人工决定。
SYNONYMS = {
    "睡不着":   ["john-ratey", "cal-newport", "seneca"],
    "失眠":     ["john-ratey", "seneca", "marcus-aurelius"],
    "拖延":     ["atomic-habits", "wang-yangming", "cal-newport", "paul-graham"],
    "摆烂":     ["atomic-habits", "frankl", "inamori"],
    "吵架":     ["nonviolent-communication", "gottman", "crucial-conversations", "adler"],
    "冷战":     ["gottman", "nonviolent-communication", "adler"],
    "分手":     ["gottman", "attachment-theory", "adler"],
    "带娃":     ["montessori", "attachment-theory", "adler", "carl-rogers"],
    "孩子不听话": ["montessori", "adler", "attachment-theory"],
    "内耗":     ["epictetus", "marcus-aurelius", "seneca", "john-ratey"],
    "焦虑":     ["epictetus", "seneca", "john-ratey", "marcus-aurelius"],
    "累":       ["john-ratey", "cal-newport", "seneca"],
    "没动力":   ["frankl", "inamori", "atomic-habits", "adler"],
    "社恐":     ["adler", "carl-rogers", "nonviolent-communication"],
    "被裁":     ["frankl", "su-shi", "nietzsche", "dalio"],
    "加班":     ["cal-newport", "drucker", "jobs"],
    "学不会":   ["feynman", "ericsson", "mao"],
    "记不住":   ["feynman", "ericsson"],
    "选择困难": ["munger", "buffett", "jobs"],
}


def _syn(slug):
    """按 slug 反查它被哪些口语词指向。"""
    return "".join(k for k, slugs in SYNONYMS.items() if slug in slugs)


def _hwx_payload():
    import json, sys as _s, re
    _s.path.insert(0, "seo")
    import hw_chapters as C, hw_slugs, hw_kind, build_seo

    line_by = {}
    for pname, spec in C.PARENTS.items():
        for it in spec.get("items", []):
            line_by[(pname, it["k"])] = it.get("line", "")

    def best_q(ch, maxlen=34):
        qs = [re.sub(r"==", "", q).strip().rstrip("。") for q in ch.get("q", [])]
        fit = [q for q in qs if 8 <= len(q) <= maxlen]
        return max(fit, key=len) if fit else (qs[0] if qs else "")

    def scene_of(ch):
        """apply 里的「局面：…」句——这句话说的正是「什么时候用得上」。"""
        m = re.search(r"局面：(.+?)(?:\n|$)", ch.get("apply", ""))
        return m.group(1).strip().rstrip("。") if m else ""

    def gloss_of(ch):
        """金句解析：一句自然话，说清「什么时候这句话用得上」。

        材料取自章节已有的 apply「局面」句，只补一个「用在……的时候」的壳，
        不另造内容。"""
        sc = scene_of(ch)
        if not sc:
            return {"pt": ch.get("w", ""), "when": "", "gl": ""}
        # 本身就以时间词收尾的不再补壳，否则会出「一段时期的时候」这种叠字。
        tail = "" if sc.endswith(("时", "时候", "时期", "期间", "阶段",
                                  "之后", "以后", "之前", "那阵", "关头",
                                  "时刻", "当口")) else "的时候"
        return {"pt": ch.get("w", ""), "when": sc, "gl": "用在" + sc + tail + "。"}

    E, ch_by = [], {}
    for ch in C.CHAPTERS:
        ch_by.setdefault(ch["parent"], []).append((ch["k"], ch["n"], ch["w"]))
    for e in build_seo.load_array():
        slug = hw_slugs.slug_for(e["n"])
        chs = ch_by.get(e["n"], [])
        hook = next((line_by.get((e["n"], k), "") for k, _, _ in chs if line_by.get((e["n"], k))), "")
        it = HWX_INTROS.get(slug, "")
        if not it:
            it = (e.get("d", "").split("。")[0])[:38]
            print("HWX 警告：%s 缺手写介绍" % slug)
        # 搜索索引：并入该条目所有章节的标题、角度、金句与正文关键词，
        # 使「止损」「复利」这类只在正文出现的词也能搜到。
        body = []
        first_ch = next((c for c in C.CHAPTERS if c["parent"] == e["n"]), None)
        for ch in C.CHAPTERS:
            if ch["parent"] != e["n"]:
                continue
            body.append(ch["n"]); body.append(ch.get("w", ""))
            body.append(re.sub(r"==", "", ch.get("story", "")))
            body.append(re.sub(r"==", "", ch.get("apply", "")))
            for f in ch.get("f", []):
                body.append(f.get("n", "")); body.append(f.get("d", ""))
            for q in ch.get("q", []):
                body.append(re.sub(r"==", "", q))
        E.append({"n": e["n"], "s": slug, "c": e["c"], "w": e["w"], "it": it, "hk": hook,
                  "nc": len(chs), "c0": chs[0][1] if chs else "",
                  "cs": [n for _, n, _ in chs[:3]] if len(chs) >= 3 else [],
                  "sc": scene_of(first_ch) if first_ch else "",
                  "pt": first_ch.get("w", "") if first_ch else "",
                  "ix": (re.sub(r"[\s，。、；：！？「」（）——…]+", "", " ".join(body))[:900]
                         + _syn(slug))})

    # 金句池：每章取 8-34 字里最长一条，带出处深链
    # 「今日一句」原来只有引文加出处，是关于说话那个人的。给它配一句
    # 第一人称的话——不用新写：每一篇在处境层里本来就挂着问句，
    # 取「本篇是首答」的那些，再按与 when/pt 的二元组重合度择优。
    #
    # 关键是**宁可少，不可错**。不设门槛时 100% 都配得上，但抽检 14 条只有
    # 9 条对：哈耶克「知识是分散的」配到了「这个位置我接下来，可能是个坑」。
    # 一句配错的第一人称句正是「艾利克森也卡在这儿」那种假共情——
    # 比没有更糟。重合度 ≥2 时抽检 12/12 全对，覆盖 19%（61/319），
    # 剩下的退回 when（第二人称条件句，仍然是冲着读者说的，只是弱一档）。
    _prim = {}
    for _t, _g, _qs in HWX_SCENES:
        for _qt, _refs in _qs:
            if _refs:
                _prim.setdefault(_refs[0], []).append(_qt)

    def _bg2(t):
        t = re.sub(r"[，。！？、：；「」（）\s—…·]", "", t)
        return {t[i:i + 2] for i in range(len(t) - 1)}

    # 手挑的那份优先。scripts/quote_asks.py 里 235 条是逐条看引文、看 when、
    # 看这一篇挂着哪些问句挑出来的；剩下的仍走自动，门槛照旧 2。
    _all_q, _own = set(), {}
    for _t, _g, _qs in HWX_SCENES:
        for _qt, _refs in _qs:
            _all_q.add(_qt)
            for _r in _refs:
                _own.setdefault(_r, set()).add(_qt)
    for _k, _v in QUOTE_ASKS.items():
        _sl, _kk = _k.split("/", 1)
        assert _v in _all_q, "quote_asks 里的问句在处境层不存在：%s → %s" % (_k, _v)
        assert _v in _own.get((_sl, _kk), set()), (
            "quote_asks 配的问句没有引用这一篇：%s → %s" % (_k, _v))

    def first_person(ch, g):
        key = "%s/%s" % (hw_slugs.slug_for(ch["parent"]), ch["k"])
        if key in QUOTE_ASKS:
            return QUOTE_ASKS[key]
        pool = _prim.get((hw_slugs.slug_for(ch["parent"]), ch["k"]), [])
        if not pool:
            return ""
        ref = _bg2(g["when"] + g["pt"] + ch["n"])
        n, q = max((len(_bg2(x) & ref), x) for x in pool)
        return q if n >= 2 else ""

    QP = []
    for ch in C.CHAPTERS:
        q = best_q(ch)
        if not q: continue
        g = gloss_of(ch)
        QP.append({"q": q, "who": ch["parent"], "cn": ch["n"],
                   "pt": g["pt"], "when": g["when"], "gl": g["gl"],
                   "fq": first_person(ch, g),
                   "u": "/i/%s/%s/" % (hw_slugs.slug_for(ch["parent"]), ch["k"])})

    # 问题卡：10 张第一人称问句
    def ref(slug, k):
        ch = next(c for c in C.CHAPTERS if hw_slugs.slug_for(c["parent"]) == slug and c["k"] == k)
        return {"who": ch["parent"], "cn": ch["n"], "u": "/i/%s/%s/" % (slug, k)}
    QQ = [
        {"t": "方案被毙了，还要不要提第二次？", "r": [ref("su-yu","daring-to-state"), ref("franklin","never-say-certainly")]},
        {"t": "连赢三把，加仓还是收手？",      "r": [ref("art-of-worldly-wisdom","quit-while-winning"), ref("bismarck","art-of-the-possible")]},
        {"t": "亏着的仓位，砍还是扛？",        "r": [ref("livermore","hope-and-fear-inverted"), ref("lynch","stomach-not-brain")]},
        {"t": "对面比我强十倍，怎么打？",       "r": [ref("napoleon","decisive-point"), ref("mao","on-protracted-war")]},
        {"t": "被当众激怒，第一反应做什么？",   "r": [ref("epictetus","judgments-not-things"), ref("zhang-liang","picking-up-the-shoe")]},
        {"t": "团队同一个错犯第三遍了，怪谁？", "r": [ref("thinking-in-systems","structure-drives-behavior"), ref("han-feizi","not-counting-on-goodness")]},
        {"t": "看不清方向的时候，先做什么？",   "r": [ref("marks","taking-the-temperature"), ref("einstein","formulating-the-problem")]},
        {"t": "这个人能不能信？",              "r": [ref("analects","see-how"), ref("zeng-guofan","recruit-and-test")]},
        {"t": "从零开始，第一步做重的还是轻的？","r": [ref("paul-graham","dont-scale"), ref("zhu-yuanzhang","delay-the-title")]},
        {"t": "现在是该退场的时候吗？",         "r": [ref("fan-li","leave-at-the-top"), ref("guo-ziyi","open-gates")]},
    ]

    # 处境
    ch_index = {(hw_slugs.slug_for(c["parent"]), c["k"]): c for c in C.CHAPTERS}
    S = []
    for t, grp, questions in HWX_SCENES:
        qs = []
        for qtext, refs in questions:
            answers = []
            for s_, k_ in refs:
                assert (s_, k_) in ch_index, "HWX 场景引用不存在: %s/%s (%s)" % (s_, k_, t)
                c = ch_index[(s_, k_)]
                answers.append({"who": c["parent"], "cn": c["n"],
                                "u": "/i/%s/%s/" % (s_, k_),
                                # wk=1 表示这是一部作品不是一个人。首页「今日一问」
                                # 原来一律说「X 也卡在同一件事上」，于是出现过
                                # 「智慧书也卡在同一件事上」——书不会卡在任何事上。
                                "wk": 1 if hw_kind.is_work(c["parent"]) else 0,
                                "hint": line_by.get((c["parent"], k_), "") or c.get("w", "")})
            qs.append({"q": qtext, "a": answers})
        S.append({"t": t, "g": grp, "qs": qs})

    # ASK（apply 里的「先问」句）已删。今日一问改用 QQ 之后它就没有任何读者了，
    # 却仍然随首页发给每一个访客：276 条、114KB 原始 / 45KB gzip，占整页 7%。
    # 和 fail/lesson 是同一种病的反面——那个是写了没人渲染，这个是发了没人读。

    # NC: 40 最新章节（按章节 py 文件 git 首次 commit 时间降序）
    import os, subprocess
    ch_times = {}
    for ch in C.CHAPTERS:
        slug = hw_slugs.slug_for(ch["parent"])
        for cand in ["seo/chapters/%s.py" % slug.replace("-","_"),
                     "seo/chapters/%s.py" % slug.replace("-","")]:
            if os.path.exists(cand):
                try:
                    r = subprocess.run(["git","log","--follow","--format=%at","--",cand],
                                       capture_output=True, text=True)
                    ts = [x for x in r.stdout.strip().split("\n") if x]
                    ch_times[(ch["parent"], ch["k"])] = int(ts[-1]) if ts else 0
                except: ch_times[(ch["parent"], ch["k"])] = 0
                break
    cat_by = {e["n"]: e["c"] for e in build_seo.load_array()}
    recent = sorted(ch_times.items(), key=lambda x: -x[1])[:40]
    NC = []
    for (pname, k), _ in recent:
        ch = next(c for c in C.CHAPTERS if c["parent"] == pname and c["k"] == k)
        slug = hw_slugs.slug_for(pname)
        NC.append({"pn": pname, "cn": ch["n"], "w": ch.get("w",""), "q": best_q(ch),
                   "sc": scene_of(ch),
                   "s": slug, "k": k, "u": "/i/%s/%s/" % (slug, k),
                   "c": cat_by.get(pname,"")})

    # 竖排卡在 158px 窄列里只放得下 4 列，长句会把卡片撑到别人两倍高：
    # 另建一个 ≤24 字的短句池给信息流，长句仍归今日一句与分享卡。
    QS = [q for q in QP if len(q["q"]) <= 20]
    # 问题卡原来只用手写的 10 张，插满就没了。处境层的 114 个问题本身就带答案，
    # 合进来池子扩到 124，频率才提得上去。
    # 问题卡与首页一问共用这个池。补齐 hint（章节一句话）与 sc（apply 的局面句），
    # 手写的那 10 张原本只有 who/cn/u，放到首页大块里会缺两行。
    _apply_sc = {}
    for _c in C.CHAPTERS:
        _m = re.search(r"局面：(.+?)(?:\n|$)", _c.get("apply", ""))
        if _m:
            _apply_sc[(hw_slugs.slug_for(_c["parent"]), _c["k"])] = _m.group(1).strip()
    def _enrich(ans):
        out = []
        for a in ans:
            b = dict(a)
            # 两批 QQ（原生的和处境派生的）都过这里，wk 在这儿补最省事。
            b["wk"] = 1 if hw_kind.is_work(a.get("who", "")) else 0
            _key = tuple(a["u"].strip("/").split("/")[1:3])
            if not b.get("hint"):
                _ch = ch_index.get(_key)
                if _ch:
                    b["hint"] = line_by.get((_ch["parent"], _ch["k"]), "") or _ch.get("w", "")
            _sc = _apply_sc.get(_key)
            if _sc:
                b["sc"] = _sc
            out.append(b)
        return out
    # 今日一问带上它属于哪个处境。531 条里 521 条本来就来自处境层，
    # 只是卡片上从不说——于是「今日一问」是一张抽奖券，而不是进入处境层的门。
    # 带上之后可以点进去看同一类的其他问题。
    _sc_by_name = {sc["t"]: sc for sc in S}
    def _scfields(name):
        sc = _sc_by_name[name]
        return {"s": name, "ss": SC_SHORT.get(name, name), "sg": sc["g"],
                "sn": len(sc["qs"]), "bx": SC_BOX[name]}
    QQ_ALL = ([dict({"t": q["t"], "r": _enrich(q["r"])}, **_scfields(QQ_SC[q["t"]])) for q in QQ]
              + [dict({"t": q["q"], "r": _enrich(q["a"])}, **_scfields(sc["t"]))
                 for sc in S for q in sc["qs"]])

    # 屏幕上同一句话不能出现两次：卡片是问句，框里是预填句，两者相距三厘米。
    # 逐条比对每个处境的每个问句和它的预填句，共 8 字以上的连续片段就算重复。
    # 改处境问句或改 SC_BOX 时最容易踩这个，所以放在构建里而不是靠人眼。
    def _grams(t, n=4):
        t = re.sub(r"[，。！？、：；「」…—\s]", "", t)
        return {t[i:i+n] for i in range(len(t) - n + 1)}
    # 四字片段里有一批是中文绕不开的连接语——「为了什么」「不知道该」「该干什么」。
    # 拿它们判重会把 34 处全报成撞车，其中大半根本不是。所以先数一遍语料：
    # 一个片段出现在三个以上处境里就是通用词，只出现在一两个处境里的才是真回声。
    _df = {}
    for sc in S:
        seen = set(_grams(SC_BOX[sc["t"]]))
        for q in sc["qs"]:
            seen |= _grams(q["q"])
        for gm in seen:
            _df[gm] = _df.get(gm, 0) + 1
    _pairs = ([(sc["t"], q["q"]) for sc in S for q in sc["qs"]]
              + [(QQ_SC[q["t"]], q["t"]) for q in QQ])
    _dup = [(a, b, sorted(g for g in _grams(b) & _grams(SC_BOX[a]) if _df.get(g, 0) < 3))
            for a, b in _pairs]
    _dup = [d for d in _dup if d[2]]
    assert not _dup, "预填句在复读卡片问句：%s" % (_dup[:3],)
    assert set(SC_BOX) == {sc["t"] for sc in S}, (
        "SC_BOX 与处境对不上：多 %s 缺 %s" % (set(SC_BOX) - {s_["t"] for s_ in S},
                                             {s_["t"] for s_ in S} - set(SC_BOX)))
    # 卡片上的人名多数读者不认识（159 条里 24 条），介绍句本来就有，
    # 一并送到前端，让「这人是谁」出现在读者第一次碰到名字的地方。
    import hw_slugs as _hs
    WHO = {}
    for _e in build_seo.load_array():
        _i = HWX_INTROS.get(_hs.slug_for(_e["n"]))
        if _i:
            WHO[_e["n"]] = _i
    j = json.dumps({"E": E, "QP": QP, "QS": QS, "QQ": QQ_ALL, "S": S, "WHO": WHO,
                    "CC": CAT_COLOR, "CT": CAT_TINT, "CTD": CAT_TINT_D, "NC": NC}, ensure_ascii=False, separators=(",",":")).replace("</","<\\/")
    return j, len(E), len(NC)


def hwx_block():
    j, ne, nnc = _hwx_payload()
    css = r"""
:root{color-scheme:light dark;--paper:#f5f1e8;--ink:#1f1c17;--acc:#a33b2e;--muted:#8a8377;--line:#d8d2c6;--paper2:#eee8da;--card:#faf7f0;--kbg:#1f1c17;--kfg:#f5f1e8;--kmut:#cfc7b8}
@media(prefers-color-scheme:dark){:root{--paper:#171410;--ink:#eae3d4;--acc:#c65f4f;--muted:#9a917f;--line:#3a342a;--paper2:#201c15;--card:#1d1913;--kbg:#eae3d4;--kfg:#171410;--kmut:#5a5344}}
:root[data-theme="light"]{--paper:#f5f1e8;--ink:#1f1c17;--acc:#a33b2e;--muted:#8a8377;--line:#d8d2c6;--paper2:#eee8da;--card:#faf7f0;--kbg:#1f1c17;--kfg:#f5f1e8;--kmut:#cfc7b8}
:root[data-theme="dark"]{--paper:#171410;--ink:#eae3d4;--acc:#c65f4f;--muted:#9a917f;--line:#3a342a;--paper2:#201c15;--card:#1d1913;--kbg:#eae3d4;--kfg:#171410;--kmut:#5a5344}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--white:#1d1913;--line-strong:rgba(234,227,212,.22);--ink-30:rgba(234,227,212,.42);--ink-50:rgba(234,227,212,.6)}}
:root[data-theme="dark"]{--white:#1d1913;--line-strong:rgba(234,227,212,.22);--ink-30:rgba(234,227,212,.42);--ink-50:rgba(234,227,212,.6)}
body{background:var(--paper);color:var(--ink)}
.share-btn{background:var(--white)!important;color:var(--ink)!important;border-color:var(--line-strong)!important}
:root[data-theme="dark"] .dot,:root[data-theme="dark"] .hd-en,:root[data-theme="dark"] .kicker,:root[data-theme="dark"] .sec-k{color:#e0705f!important}
:root[data-theme="dark"] body{background:#171410!important;color:#eae3d4!important}
:root[data-theme="dark"] .hd-title,:root[data-theme="dark"] h1,:root[data-theme="dark"] h2,:root[data-theme="dark"] h3{color:#eae3d4!important}
:root[data-theme="dark"] #hwx .tq .dt{color:#e0705f!important}
:root[data-theme="dark"] #hwx .tq .src,:root[data-theme="dark"] #hwx .tq .src a,:root[data-theme="dark"] #hwx .tbox .hint{color:#d9d1c0!important;opacity:1}
:root[data-theme="dark"] #hwx .qc .who,:root[data-theme="dark"] #hwx .pc .it,:root[data-theme="dark"] #hwx .pc .tag,:root[data-theme="dark"] #hwx .pc .ls,:root[data-theme="dark"] #hwx .nc .w,:root[data-theme="dark"] #hwx .nc .pn{color:#a79e8b!important}
:root[data-theme="dark"] #hwx .cf,:root[data-theme="dark"] #hwx .qc .who i,:root[data-theme="dark"] #hwx .nc .pn i,:root[data-theme="dark"] #hwx .seal{color:#ef8b78!important}
:root[data-theme="dark"] #hwx .nb{background:#b8452f!important;color:#fff!important}
:root[data-theme="dark"] #hwx .kc .qm{color:#8a3a2e!important}
#hwx .kc .qm{color:#c4644f}
#hwx-theme{position:fixed;top:14px;right:14px;z-index:9999;width:36px;height:36px;border:1px solid var(--line);background:var(--paper);color:var(--ink);border-radius:50%;font-size:15px;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 6px rgba(0,0,0,.10);padding:0}
#hwx-theme:hover{border-color:var(--acc);color:var(--acc)}
#hwx .today{display:grid;grid-template-columns:1.5fr 1fr;gap:14px;margin:18px 0 6px}
@media(max-width:700px){#hwx .today{grid-template-columns:1fr}}
/* 日夜切换是 fixed 在右上角的 36px 圆钮；窄屏上它正压在第一张卡的表头右端
   （处境标签那颗胶囊）上。表头右边让出它的宽度。 */
@media(max-width:480px){#hwx .askhero .ahead{padding-right:38px}}
#hwx .tq{border:1px solid var(--line);border-radius:16px;padding:20px 22px;background:transparent;display:flex;flex-direction:column}
#hwx .tq .dt{font-size:12.5px;letter-spacing:.24em;color:var(--acc);font-weight:700;margin-bottom:6px}
#hwx .tq .q{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:clamp(20px,3.6vw,26px);font-weight:700;line-height:1.85;margin-bottom:14px}
#hwx .tq .src{font-size:13.5px;color:var(--muted)}
#hwx .tq .src a{color:var(--acc);text-decoration:none}
#hwx .tq .tgl{font-size:14.5px;line-height:1.75;color:var(--ink);opacity:.72;margin:0 0 10px}
#hwx .tq .acts{display:flex;gap:8px;margin-top:14px}
#hwx .tq .acts button{border:1.5px solid var(--ink);background:transparent;color:var(--ink);border-radius:999px;padding:7px 16px;font-family:inherit;font-size:14px;cursor:pointer}
#hwx .tq .acts .bs{background:var(--ink);color:var(--paper)}
#hwx .askhero{border:1px solid var(--line);border-radius:16px;background:var(--card);padding:20px 18px 16px;margin-bottom:12px}
#hwx .askhero .ahead{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin-bottom:12px}
#hwx .askhero .lb{font-size:11.5px;letter-spacing:.28em;color:var(--acc);font-weight:700}
#hwx .askhero #hwx-asc-tag{margin:-6px 0 14px}
/* 搜不到时的那块。语气跟站上一致：先说没找到什么，再给一条出路。 */
#hwx #hwx-none{border:1px dashed var(--line);border-radius:14px;padding:20px 18px;margin:14px 0 8px;text-align:center}
#hwx #hwx-none b{display:block;font-family:"Noto Serif SC","Songti SC",serif;font-size:17px;line-height:1.7;color:var(--ink)}
#hwx #hwx-none i{display:block;font-style:normal;font-size:13.5px;line-height:1.8;color:var(--muted);margin:6px 0 14px}
#hwx #hwx-none button{border:1px solid var(--ink);background:var(--ink);color:var(--paper);border-radius:999px;padding:7px 18px;font-family:inherit;font-size:13.5px;cursor:pointer}
#hwx .askhero #hwx-asc-tag button{border:0;background:transparent;color:var(--muted);padding:0;font-family:inherit;font-size:12.5px;line-height:1.7;cursor:pointer;text-align:left}
#hwx .askhero #hwx-asc-tag button:hover{color:var(--acc)}
#hwx .amine{border-top:1px dashed var(--line);margin-top:14px;padding-top:12px}
/* 按钮放进框里的右下角。手机上预填句会折成三行，框一长高，贴在框外面的
   圆球就成了另一样东西；放进去之后它跟着框底走，单行时正好居中（6+30+6=42）。 */
#hwx .amine .arow{display:flex;align-items:flex-end;gap:4px;border:1px solid var(--line);border-radius:14px;background:var(--paper);padding:0 6px 0 0}
#hwx .amine .arow:focus-within{border-color:var(--acc)}
#hwx .amine textarea{flex:1;min-width:0;display:block;resize:none;font-family:inherit;font-size:15px;line-height:1.6;color:var(--ink);background:transparent;border:none;border-radius:14px;padding:9px 13px;outline:none;max-height:96px}
#hwx .amine button{flex:0 0 auto;height:30px;margin:6px 0;border:none;border-radius:9px;background:var(--ink);color:var(--paper);font-family:inherit;font-size:14px;line-height:30px;padding:0 14px;cursor:pointer}
#hwx .amine button:disabled{opacity:.4;cursor:default}

#hwx .askhero .said{font-family:"Noto Serif SC","Songti SC",serif;font-size:13.5px;color:var(--acc);line-height:1.7;margin:11px 0 0}
#hwx .askhero .q{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:21px;font-weight:700;line-height:1.75;margin:0 0 14px}
#hwx .askhero .sc{font-size:13.5px;color:var(--muted);line-height:1.8;margin:0;padding-left:12px;border-left:2px solid var(--line)}
#hwx .askhero .go a{display:block;text-decoration:none;color:inherit;border-top:1px dashed var(--line);padding-top:11px;margin-top:12px}
#hwx .askhero .go a.lead b{font-size:17px;color:var(--ink)}
#hwx .askhero .go a.lead i{font-size:14px;line-height:1.75;color:var(--ink);opacity:.85}
#hwx .askhero .go a.sub b{font-size:14px}
#hwx .askhero .go a.sub i{font-size:12.5px}
#hwx .askhero .go b{font-family:"Noto Serif SC","Songti SC",serif;font-size:15.5px;display:block}
#hwx .askhero .go i{font-style:normal;font-size:12.5px;color:var(--muted);display:block;margin-top:3px}
/* 今日一问主篇下的「这人是谁」：一天一张、位置最靠前，多一行凭据划算。
   处境卡不加——28 张连着刷，每张多一行会让扫读变慢，而卡片的主角是那句问题。 */
#hwx .askhero .go a u{display:block;text-decoration:none;font-size:12.5px;line-height:1.6;color:var(--muted);margin-top:2px}
#hwx .askhero .go a em{display:block;font-style:normal;font-size:14px;line-height:1.7;color:var(--acc);margin-top:5px}
#hwx .kc .r a u{display:block;text-decoration:none;font-size:11.5px;line-height:1.55;color:var(--muted);opacity:.85;margin-top:2px}
#hwx .kc .r a em{display:block;font-style:normal;color:var(--acc);margin-top:3px}
#hwx .today .tq{padding:15px 16px}
#hwx .today .tq .q{font-size:17px!important;line-height:1.8!important;margin-bottom:8px!important}
#hwx .today .tq .tgl{display:block;font-size:13.5px;line-height:1.7;margin:6px 0 12px}
/* 第一人称那句是读者自己的话，给它一道竖线，跟上面的引文分开——
   没有标签，靠这道线说明它不是引文的续文。 */
#hwx .today .tq .tgl.mine{padding-left:11px;border-left:2px solid var(--line);color:var(--ink);opacity:.9}
#hwx .today .tq .acts button{padding:5px 12px;font-size:12.5px;border-width:1px}
#hwx .today .tq .acts .bs{background:var(--ink);color:var(--paper);border-color:var(--ink)}
#hwx .tbox-s{padding:12px 14px}
#hwx .tbox-s b{font-size:15px}
#hwx .tbox-s .hint2{display:none}
#hwx .today-foot{margin-top:22px}
#hwx .tcol{display:flex;flex-direction:column;gap:14px}
#hwx .tbox{border:1px solid var(--line);border-radius:16px;padding:14px 16px;flex:1}
#hwx .tbox .lb{font-size:11.5px;letter-spacing:.28em;color:var(--acc);font-weight:700;margin-bottom:6px}
#hwx .tbox a{color:inherit;text-decoration:none;display:block}
#hwx .tbox b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:16.5px}
#hwx .tbox .hint{display:block;font-size:14.5px;color:var(--ink);opacity:.72;margin-top:4px;line-height:1.65}
#hwx .tbox .hint2{display:block;font-size:14px;color:var(--acc);opacity:.92;margin-top:6px;line-height:1.6}
#hwx .hh{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:21px;font-weight:700;margin:24px 0 10px;letter-spacing:.03em;display:flex;justify-content:space-between;align-items:baseline}
#hwx .hh .ct{font-size:12px;color:var(--muted);font-weight:500}
#hwx .sc{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0}
#hwx .scmore{order:9999;flex:0 0 auto;border:1px dashed var(--line);background:transparent;color:var(--acc);border-radius:999px;padding:7px 14px;font-family:inherit;font-size:14.5px;cursor:pointer;white-space:nowrap;line-height:1.6}
#hwx .scmore:hover{border-color:var(--acc)}
/* 组名独占一行。试过与标签同行以省高度，结果组名混在标签流里像半个标签，
   比原来更乱——高度靠「每组只露 2 个」和紧凑的行距来收，不靠挤掉标题。 */
#hwx .scg{flex:0 0 100%;font-family:"Noto Serif SC","Songti SC",serif;font-size:11.5px;color:var(--muted);letter-spacing:.1em;margin:9px 0 -2px;padding:0;line-height:1.4}
#hwx .scg:first-child{margin-top:0}
#hwx .sc{row-gap:7px}
#hwx .sc{flex-wrap:wrap!important;overflow-x:visible!important}
#hwx .sc button{flex:0 0 auto;border:1px solid var(--line);background:transparent;color:inherit;border-radius:999px;padding:7px 14px;font-family:inherit;font-size:14.5px;cursor:pointer;white-space:nowrap}
#hwx .sc button.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
#hwx .res{display:none;border-left:3px solid var(--acc);padding:4px 0 4px 13px;margin:8px 0 6px}
#hwx .res.on{display:block}
#hwx .res .qz{margin:0 0 14px}
#hwx .res .qz:last-child{margin-bottom:2px}
#hwx .res .qzq{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:16px;font-weight:700;line-height:1.6;margin-bottom:4px}
#hwx .res .qzq::before{content:"？";color:var(--acc);font-weight:900;margin-right:5px}
#hwx .res a{display:block;padding:4px 0 4px 16px;text-decoration:none;color:inherit}
#hwx .res a b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:15px;font-weight:600}
#hwx .res a span{display:block;font-size:13.5px;color:var(--muted);line-height:1.6}
#hwx .res a:hover b{border-bottom:1px solid}
#hwx .hist{display:none;align-items:center;gap:8px;margin:0 0 14px;font-size:13px}
header.hd{margin-bottom:12px!important}
#hwx .hist .hl{color:var(--acc);font-weight:700;letter-spacing:.1em;flex:0 0 auto}
#hwx .hist .hchips{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;flex:1}
#hwx .hist .hchips::-webkit-scrollbar{display:none}
#hwx .hist .hchips a{flex:0 0 auto;border:1px solid var(--line);border-radius:999px;padding:4px 11px;color:var(--muted);text-decoration:none;white-space:nowrap}
#hwx .hist .hchips a:hover{color:var(--ink)}
#hwx .hist button{border:none;background:transparent;color:var(--muted);font-family:inherit;font-size:11px;cursor:pointer;flex:0 0 auto}
#hwx .qbar{margin:22px 0 0}
#hwx .qbar input{width:100%;border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:999px;padding:12px 20px;font-family:inherit;font-size:16px;outline:none;transition:border-color .15s}\n#hwx .qbar input:focus{border-color:var(--muted)}
#hwx .qbar input::placeholder{color:var(--muted)}
/* 一行入口：两行结构（标题+计数 / 提示语），替代原先 1049px 的标签目录。
   试过 flex 单行，三段挤在一起且箭头折行——中文没有词间空格，靠 gap 撑不开。 */
#hwx .scline{display:block;width:100%;background:transparent;border:none;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:15px 2px;margin:16px 0 0;cursor:pointer;color:inherit;text-align:left;font-family:inherit}
#hwx .scline b{font-family:"Noto Serif SC","Songti SC",serif;font-size:19px;font-weight:700;margin-right:10px}
#hwx .scline span{font-size:12.5px;color:var(--muted)}
#hwx .scline i{display:block;font-style:normal;margin-top:6px;font-size:13px;color:var(--acc)}
#hwx .tabs2{flex-shrink:0}
#hwx .tabs2{display:flex;gap:0;border-bottom:2px solid var(--line);margin:14px 0 0}
#hwx .tabs2 button{border:none;background:transparent;padding:9px 20px;font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:17px;font-weight:600;color:var(--muted);cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-2px}
#hwx .tabs2 button.on{color:var(--ink);border-bottom-color:var(--acc)}
#hwx .cats{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;margin:10px 0 0}
#hwx .cats::-webkit-scrollbar{display:none}
#hwx .cats button{flex:0 0 auto;border:none;background:transparent;color:var(--muted);font-family:inherit;font-size:14px;cursor:pointer;padding:5px 11px;border-radius:999px}
#hwx .cats button.on{background:var(--line);color:var(--ink)}
/* 处境选择条：两行横滑。76 个处境竖着平铺是 1049px，那正是被废掉的旧目录；
   横滑两行占 78px，一屏能扫到十几个，滑动就能看完全部。
   不放组名——组名与标签同行会混成半个标签（见 DESIGN.md §7），
   改用「按组排序」让相邻的处境自然聚在一起。 */
#hwx .scmore-note{grid-column:1/-1;padding:14px 4px 4px;font-size:13.5px;color:var(--muted);line-height:1.7}
#hwx .scpick{display:grid;grid-auto-flow:column;grid-template-rows:auto auto;grid-auto-columns:max-content;gap:7px 6px;overflow-x:auto;overscroll-behavior-x:contain;scrollbar-width:none;margin:12px 0 0;padding-bottom:2px}
#hwx .scpick::-webkit-scrollbar{display:none}
#hwx .scpick button{border:1px solid var(--line);background:transparent;color:inherit;border-radius:999px;padding:7px 14px;font-family:inherit;font-size:14.5px;line-height:1.3;cursor:pointer;white-space:nowrap}
#hwx .scpick button.on{background:var(--ink);color:var(--paper);border-color:var(--ink)}
#hwx .scpick button.sub{border-style:dashed;font-size:14px}
#hwx .scpick button.sub.on{border-style:solid}
#hwx .scpick .scsep{display:block;width:1px;align-self:stretch;background:var(--line);margin:0 4px;grid-row:1/3}
#hwx .feed{columns:150px;column-gap:12px;margin-top:14px}
#hwx .feed>*{break-inside:avoid;width:100%;margin:0 0 12px}
#hwx .nc-feed{columns:150px;column-gap:12px;margin-top:14px}
#hwx .nc-feed>*{break-inside:avoid;width:100%;margin:0 0 12px}
#hwx .pc{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:14px;padding:17px 17px 15px;text-decoration:none;color:inherit;background:var(--tint,var(--card))}
:root[data-theme="dark"] #hwx .pc,:root[data-theme="dark"] #hwx .nc{background:var(--tintd,var(--card))}
/* flex-wrap:wrap 是为了不让右边的小字（条目的 w）把标题挤折行。
   卡片内容宽只有 124px，人名 + 小字超过约 116px 标题就断词——
   而这跟小字多长关系不大：马可·奥勒留(91px)+「克制」(22px) 照样折，
   毛泽东(57px)+「集中优势」(50px) 反而不折。限制小字字数解决不了。
   允许换行之后，放不下的小字自己掉到第二行，标题永远完整。
   实测 60 张卡：折行 9 → 0，卡片中位高 258px 不变。 */
#hwx .pc .r1{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px}
#hwx .pc b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:19px;line-height:1.45}
#hwx .pc .tag{font-size:12.5px;color:var(--muted);white-space:nowrap;max-width:52%;overflow:hidden;text-overflow:ellipsis;font-style:normal}
#hwx .pc .it{font-size:14px;color:var(--muted);margin:6px 0 9px;line-height:1.65}
#hwx .pc .hk{font-size:15.5px;line-height:1.85;flex:1}
#hwx .pc .hk::before{content:"「"}#hwx .pc .hk::after{content:"」"}
#hwx .pc .ls{font-size:12.5px;color:var(--muted);margin-top:10px;border-top:1px dashed var(--line);padding-top:9px;line-height:1.65}
#hwx .pc .cf{font-size:12.5px;color:var(--acc);margin-top:10px}
#hwx .nc{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:14px;padding:17px 17px 15px;text-decoration:none;color:inherit;background:var(--tint,var(--card))}
#hwx .nc .pn{font-size:13px;color:var(--muted);margin-bottom:5px}
#hwx .nc .pn i{font-style:normal;color:var(--acc)}
#hwx .nc .nb{font-size:11px;background:var(--acc);color:#fff;border-radius:4px;padding:1px 5px;margin-left:5px;vertical-align:1px}
#hwx .nc b{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:19px;line-height:1.45}
#hwx .nc .w{font-size:13px;color:var(--muted);margin:4px 0 10px}
#hwx .nc .q{font-size:15.5px;line-height:1.85}
#hwx .nc .q::before{content:"「"}#hwx .nc .q::after{content:"」"}
#hwx .qc{border-radius:14px;background:var(--paper2);border:1px solid var(--line);padding:17px 15px 14px;display:flex;flex-direction:column;text-decoration:none;color:inherit;position:relative}
#hwx .qc .v{writing-mode:vertical-rl;text-orientation:mixed;height:186px;width:fit-content;max-width:100%;font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong","SimSun",serif;font-size:17px;font-weight:700;line-height:1.85;letter-spacing:.04em;margin:5px auto 12px;overflow:hidden;display:block}
#hwx .qc .v::before{content:"「"}#hwx .qc .v::after{content:"」"}
#hwx .qc .who{font-size:12.5px;color:var(--muted);margin-top:2px}
#hwx .qc .gl{font-size:13px;line-height:1.65;color:var(--ink);opacity:.72;margin:0 0 8px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
#hwx .qc .who i{font-style:normal;color:var(--acc)}
#hwx .qc .seal{position:absolute;top:13px;right:13px;width:22px;height:22px;border:1.5px solid var(--acc);border-radius:4px;color:var(--acc);font-size:11px;display:flex;align-items:center;justify-content:center}
#hwx .kc{border-radius:14px;background:rgba(163,59,46,.07);border:1px solid rgba(163,59,46,.22);color:var(--ink);padding:16px 16px 14px;display:flex;flex-direction:column}
:root[data-theme="dark"] #hwx .kc{background:rgba(224,112,95,.13);border-color:rgba(224,112,95,.3)}
#hwx .kc{position:relative;cursor:pointer}
#hwx .kc:hover{border-color:rgba(163,59,46,.42)}
:root[data-theme="dark"] #hwx .kc:hover{border-color:rgba(224,112,95,.5)}
#hwx .kc .seal{position:absolute;top:13px;right:13px;width:22px;height:22px;border:1.5px solid var(--acc);border-radius:4px;color:var(--acc);font-size:11px;display:flex;align-items:center;justify-content:center;font-family:"Noto Serif SC","Songti SC",serif}
#hwx .kc .said{font-size:12px;line-height:1.6;font-family:"Noto Serif SC","Songti SC",serif;margin-bottom:8px;color:var(--acc);padding-right:28px}
#hwx .kc .qm{display:none;font-size:25px;color:var(--acc);font-weight:900;line-height:1}
#hwx .kc .t{font-family:"Noto Serif SC","Source Han Serif SC","Songti SC","STSong",serif;font-size:16.5px;font-weight:700;line-height:1.65;margin:9px 0 12px;flex:1;color:var(--ink)}
#hwx .kc .r a{display:block;font-size:13.5px;color:var(--muted);text-decoration:none;padding:4px 0}
#hwx .kc .r a b{color:var(--ink);font-weight:600}
.dq{display:none!important}
.tabs,#tl-wrap{display:none!important}
.family a{color:inherit;text-decoration:none}
@media(min-width:900px){#hwx .feed,#hwx .nc-feed{columns:230px}}
.hid{display:none!important}
""".strip()

    js = r"""
(function(){
var D=HWXD;
/* 日夜模式：默认跟随系统，点击在 跟随/日间/夜间 之间循环并记住 */
(function(){
  var R=document.documentElement, KEY='hwx_theme';
  function sysDark(){return !!(window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches)}
  function get(){try{return localStorage.getItem(KEY)||''}catch(e){return ''}}
  function set(v){try{localStorage.setItem(KEY,v)}catch(e){}}
  function eff(){var m=get();return m||(sysDark()?'dark':'light')}
  function paint(){
    var m=eff();
    R.setAttribute('data-theme',m);
    var b=document.getElementById('hwx-theme');
    if(b){b.textContent=(m==='dark'?'\u2600':'\u263e');
          b.setAttribute('title',m==='dark'?'切换到日间':'切换到夜间');}
  }
  paint();
  setTimeout(function(){
    var b=document.getElementById('hwx-theme');
    if(!b)return;
    b.onclick=function(){set(eff()==='dark'?'light':'dark');paint()};
    paint();
  },0);
  if(window.matchMedia){var mq=window.matchMedia('(prefers-color-scheme:dark)');
    if(mq.addEventListener)mq.addEventListener('change',paint);else if(mq.addListener)mq.addListener(paint);}
})();
function esc(s){return(s||'').replace(/&/g,'&amp;').replace(/"/g,'&quot;')}
var _n=new Date(),WD='日一二三四五六';
var day=Math.floor((_n.getTime()-_n.getTimezoneOffset()*60000)/864e5);
/* ── 今日三样 ── */
var qIdx=day%D.QP.length, q1=D.QP[qIdx];
function paintQuote(first){
  q1=D.QP[qIdx];
  /* 页面上不显示日期——它对读者没有用，只是让卡片更花。
     分享卡里仍然带日期，那里日期是有意义的（记录哪天存的）。 */
  document.getElementById('hwx-dt').textContent='今日一句';
  document.getElementById('hwx-tq').textContent='「'+q1.q+'」';
  document.getElementById('hwx-tqs').innerHTML='—— '+q1.who+' · <a href="'+q1.u+'" data-h="'+esc(q1.who+' · '+q1.cn)+'">'+q1.cn+' →</a>';
  /* 「什么时候想起这句」——和「今日一篇」的「什么时候翻开它」是同一个手法。
     这一句 319 条引文本来每条都有（QP 的 when 字段），只是首页一直
     display:none 藏着，只在分享卡上用。于是首页那块成了名言展示柜：
     它是关于说话那个人的，不是关于读者的。露出来它才冲着读者。
     用 when 不用 gl：gl 是「用在……的时候。」，公文腔；when 就是那半句人话。 */
  /* 有配得准的第一人称问句就用它——「有人这么问过：我一见那种人就来气。」
     读者不必先把自己的处境翻译成条件句，一眼就认出来。
     配不准就退回 when（第二人称条件句，弱一档但不会错）。 */
  /* 第一人称那句不加任何标签。原来写「有人这么问过：」，两处不对：
     一是这些句子多半是陈述句（「我一提，就变成我在抱怨。」），「问过」对不上；
     二是凡以「有人」开头的标签都在把这句话推远——而这块要的正是读者
     把它读成自己的话。今日一问也是零框架，就是这个道理。
     位置留在引文和出处之间，靠一道竖线把它和引文分开。
     配不准的仍退回 gl，那本来就是现成的一句「用在……的时候。」。 */
  var gl=document.getElementById('hwx-tgl');
  if(gl){
    var w=q1.fq?esc(q1.fq):esc(q1.gl||'');
    gl.className=q1.fq?'tgl mine':'tgl';
    gl.textContent=w; gl.style.display=w?'':'none';
  }
}
paintQuote(true);
document.getElementById('hwx-next').onclick=function(){
  qIdx=Math.floor(Math.random()*D.QP.length); paintQuote(false);
};
var p1=D.E[(day*7)%D.E.length];
var tpEl=document.getElementById('hwx-tp');
tpEl.href='/i/'+p1.s+'/';tpEl.setAttribute('data-h',p1.n);
tpEl.innerHTML='<b>'+p1.n+' — '+p1.w+'</b><span class="hint">'+p1.it+'</span>'
  +(p1.sc?'<span class="hint2">什么时候翻开它：'+p1.sc+'</span>':'');
/* 一问不再冲着读者提问，而是「有人也卡在这里」——读者只需认出，不必回答。
   取 QQ 而非 ASK：前者是处境式的人话（「方案被毙了，还要不要提第二次？」），
   后者是 apply 里的自省句（「我真正想缓解的是谁的不安？」），接不上「某某也卡在这里」。 */
var a1=D.QQ[(day*13)%D.QQ.length];
var a1r=(a1.r&&a1.r[0])?a1.r[0]:{};
var a1w=a1r.who||'';
/* 「X 也卡在同一件事上」对人成立，对书不成立——出现过「智慧书也卡在同一件事上」。
   wk=1 表示这条的首答主是一部作品，换一句说得通的话。 */
document.getElementById('hwx-aq').textContent=a1.t;
/* 这里原来还有两块，都拆了：
   「局面」是用第二人称把读者刚认出的事再抽象讲一遍，稀释共鸣；
   「X 也卡在这儿」对一半人是假的——库里很多是研究者不是亲历者，
   艾利克森研究刻意练习，他没有「练了没长进」。
   用不真的话制造共情，是这个站最不该干的事。
   留下的只有：他自己那句话，和一个真做过这件事的人。 */
/* 今日一问下面放一个已经填好的输入框。
   一个正难受的人最难的是把事说清楚——空框把最难的一步放在最前面。
   填成 value 而不是 placeholder：一点就有字，改几个词就成了自己的话。
   原样发出去也能答，只是那是卡片的处境不是他的，所以话术引导改写。 */
/* 处境标签原来是右上角一枚四字胶囊（「没人看 →」），摆在「今日一问」旁边，
   读者看不出它跟这张卡什么关系。改到问句底下，用整名并带上「还有几个」——
   它是这一问的出处，也是「这不是我那件事」时的去处，说清楚了才有人点。 */
var a1sEl=document.getElementById('hwx-asc-tag');
if(a1sEl){
  if(a1.s){
    var _sc=(D.S||[]).filter(function(x){return x.t===a1.s;})[0];
    var _more=_sc?Math.max(0,(_sc.qs||[]).length-1):0;
    a1sEl.innerHTML='<button type="button" id="hwx-a1go">这一问来自「'+esc(a1.s)+'」'
      +(_more?('，那儿还有 '+_more+' 个'):'')+' →</button>';
    document.getElementById('hwx-a1go').onclick=function(){
      SCGRP=a1.sg||''; SCSEL=a1.s;
      switchTab('境'); scBuild(); scRender(); scReveal();
      trk('daily_to_situation',{situation:a1.s});
      var el=document.getElementById('hwx-tabs2');
      if(el&&el.scrollIntoView)try{el.scrollIntoView({block:'start',behavior:'smooth'})}catch(e){}
    };
  }else{a1sEl.style.display='none';}
}
var ain=document.getElementById('hwx-ain');
if(ain){
  /* 框里直接放一句能发出去的话，不让读者自己写——认出「这就是我」之后，
     他想知道的就是「那我该干什么」。
     但不能是卡片那句的复读：同一句话在三厘米之内出现两次，卡片就从
     「这就是我」塌成一个表单默认值。所以取 SC_BOX 里一处境一句手写的，
     前半说这件事正在把人怎么样，后半是一句答得上来的请求。
     想改的人照样能改，但不改也能直接点。 */
  ain.value=a1.bx||'';
  var fit=function(){ain.style.height='auto';ain.style.height=Math.min(ain.scrollHeight,96)+'px';};
  ain.addEventListener('input',fit); setTimeout(fit,0);
  /* 额度那行文案去掉了，但按钮该禁用还是要禁用——不然点了才知道用完，更糟。
     hw-chat.js 是 defer 加载的，写死延时去读必然踩空，轮询到出现为止。 */
  var goBtn=document.getElementById('hwx-ago2');
  var paintLeft=function(){
    if(typeof window.hwLeft!=='function')return false;
    if(goBtn)goBtn.disabled=(window.hwLeft()<=0);
    return true;
  };
  (function poll(i){ if(paintLeft()||i>20)return; setTimeout(function(){poll(i+1)},100); })(0);
  var fire=function(){
    var t=ain.value.trim(); if(!t){ain.focus();return;}
    /* edited 比的是预填句 bx，不是卡片问句——框里放的一直是 bx，
       跟 a1.t 比的话每一次都会被记成「改过了」。 */
    trk('daily_ask',{edited:(t!==(a1.bx||''))?1:0,situation:a1.s||''});
    /* 把卡片上那两篇和处境名一起带过去。这一问的答案首页已经知道，
       不该让聊天窗再用二元组检索猜一遍——猜出来的经常是别的篇。 */
    if(typeof window.hwAsk==='function'){
      window.hwAsk(t,{pin:(a1.r||[]).slice(0,2).map(function(r){return r.u;}),scene:a1.s||''});
      setTimeout(paintLeft,1400);
    }
  };
  document.getElementById('hwx-ago2').onclick=fire;
  ain.addEventListener('keydown',function(e){
    if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();fire();}
  });
}
/* 第一条放大当主角：一个人、一件他真干过的事，比两个并列的链接有力。 */
var WHO=(D.WHO||{});
/* 只放一个例子。两个并列的人名等于让读者先做一道选择题，而这张卡的作用是
   「有人真干过这件事」——一个就够，硬凑第二个只是把第一个的分量摊薄。 */
document.getElementById('hwx-ago').innerHTML=(a1.r||[]).slice(0,1).map(function(r,i){
  /* 主篇下面补一句「这人是谁」：卡片是读者第一次碰到这个名字的地方。 */
  /* 顺序：人 → 这人是谁 → 这一篇说什么 → 去这一篇。链接放最后，前面三行是决定要不要点的依据。 */
  var w=WHO[r.who]?'<u>'+esc(WHO[r.who])+'</u>':'';
  return '<a class="'+(i?'sub':'lead')+'" href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'">'
    +'<b>'+r.who+'</b>'+w+(r.hint?'<i>'+r.hint+'</i>':'')+'<em>'+r.cn+' →</em></a>';}).join('');
/* ── 分享卡 ── */
function drawCard(cb){
  var cv=document.createElement('canvas');cv.width=1080;cv.height=1440;var c=cv.getContext('2d');
  var loaded=0,need=3;function chk(){if(++loaded>=need)render();}
  document.fonts.load('900 128px "Noto Serif SC"').then(chk).catch(chk);
  document.fonts.load('700 58px "Noto Serif SC"').then(chk).catch(chk);
  document.fonts.load('500 34px "Noto Serif SC"').then(chk).catch(chk);
  function render(){
    c.fillStyle='#f5f1e8';c.fillRect(0,0,1080,1440);
    c.strokeStyle='#d8d2c6';c.lineWidth=2;c.strokeRect(46,46,988,1348);
    c.fillStyle='#a33b2e';c.font='900 128px "Noto Serif SC"';c.fillText(String(_n.getDate()),96,232);
    c.fillStyle='#8a8377';c.font='500 34px "Noto Serif SC"';c.fillText((_n.getMonth()+1)+'月 · 星期'+WD[_n.getDay()],100,296);
    c.fillStyle='#9d2933';
    (function(x,y,w){var r=w*0.22;c.beginPath();
      c.moveTo(x+r,y);c.lineTo(x+w-r,y);c.quadraticCurveTo(x+w,y,x+w,y+r);
      c.lineTo(x+w,y+w-r);c.quadraticCurveTo(x+w,y+w,x+w-r,y+w);
      c.lineTo(x+r,y+w);c.quadraticCurveTo(x,y+w,x,y+w-r);
      c.lineTo(x,y+r);c.quadraticCurveTo(x,y,x+r,y);c.closePath();c.fill();})(880,110,104);
    c.fillStyle='#fff';c.font='700 62px "Noto Serif SC"';
    c.textAlign='center';c.fillText('人',932,182);c.textAlign='left';
    c.fillStyle='#1f1c17';c.font='700 58px "Noto Serif SC"';
    var q='「'+q1.q+'」',lines=[],cur='',PUNC='，。、；：！？…」）';
    for(var i=0;i<q.length;i++){var tt=cur+q[i];if(c.measureText(tt).width>880&&PUNC.indexOf(q[i])<0){lines.push(cur);cur=q[i]}else cur=tt}
    if(cur)lines.push(cur);
    var y=560+(5-Math.min(lines.length,5))*46;
    lines.slice(0,6).forEach(function(l){c.fillText(l,100,y);y+=98});
    /* 解析：一句话，画在署名之上；行数按实际内容，不预留空档 */
    var ay=y+46;
    if(q1.gl){
      c.fillStyle='#5f5850';c.font='500 31px "Noto Serif SC"';
      var wl=[],cu='';
      for(var j=0;j<q1.gl.length;j++){var tw=cu+q1.gl[j];
        if(c.measureText(tw).width>860&&PUNC.indexOf(q1.gl[j])<0){wl.push(cu);cu=q1.gl[j]}else cu=tw}
      if(cu)wl.push(cu);
      wl=wl.slice(0,3);
      wl.forEach(function(l){c.fillText(l,100,ay);ay+=46});
    }
    ay+=54;   /* 与上一段空出一行 */
    c.fillStyle='#8a8377';c.font='500 34px "Noto Serif SC"';
    c.textAlign='right';c.fillText('—— '+q1.who+' · '+q1.cn,980,ay);c.textAlign='left';
    c.strokeStyle='#d8d2c6';c.lineWidth=2;c.beginPath();c.moveTo(100,1230);c.lineTo(980,1230);c.stroke();
    c.fillStyle='#1f1c17';c.font='700 34px "Noto Serif SC"';c.fillText('人类世界生存法则',100,1318);
    c.fillStyle='#a33b2e';c.font='500 30px "Noto Serif SC"';c.fillText('OurWord.ai',100,1366);
    var qr=new Image();
    qr.onload=function(){c.drawImage(qr,858,1244,122,122);cv.toBlob(cb,'image/png')};
    qr.onerror=function(){cv.toBlob(cb,'image/png')};
    qr.src='/wechat-qr.png?v=54fb0fdf';
  }
}
document.getElementById('hwx-save').onclick=function(){drawCard(function(b){var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='ourword-'+(_n.getMonth()+1)+'-'+_n.getDate()+'.png';a.click()})};
document.getElementById('hwx-share').onclick=function(){drawCard(function(b){var f=new File([b],'ourword.png',{type:'image/png'});if(navigator.canShare&&navigator.canShare({files:[f]}))navigator.share({files:[f],title:'人类世界生存法则'});else{var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='ourword.png';a.click()}})};
/* ── 处境标签 ── */
var scEl=document.getElementById('hwx-sc'),resEl=document.getElementById('hwx-res');
var scMore=document.getElementById('hwx-scmore');
/* 按组渲染：原来 76 个处境平铺，折叠逻辑按「两行」算，默认只露得出 4 个——
   加多少处境用户都看不见。分组之后每组露前 3 个，默认可见约 30 个。 */
var _seen={};
D.S.forEach(function(s){
  if(s.g && !_seen[s.g]){
    _seen[s.g]=1;
    var h=document.createElement('span');
    h.className='scg';h.textContent=s.g;
    scEl.appendChild(h);
  }
  var b=document.createElement('button');b.type='button';b.textContent=s.t;
  b.dataset.g=s.g||'';
  b._open=function(){
    scEl.querySelectorAll('button').forEach(function(x){x.classList.remove('on')});
    b.classList.add('on');
    resEl.innerHTML=s.qs.map(function(q){
      return '<div class="qz"><div class="qzq">'+q.q+'</div>'
        +q.a.map(function(r){return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+' · '+r.cn+'</b><span>'+(r.hint||'')+'</span></a>'}).join('')
        +'</div>';
    }).join('');
    resEl.classList.add('on');
  };
  b.onclick=function(){
    if(b.classList.contains('on')){          /* 再点已展开的，折叠 */
      b.classList.remove('on');
      resEl.classList.remove('on');resEl.innerHTML='';return;
    }
    b._open();
    resEl.scrollIntoView({behavior:'smooth',block:'nearest'});
  };scEl.appendChild(b);
});

/* 默认只露两行，其余收起 */
(function(){
  var open=false;
  function tags(){return Array.prototype.filter.call(
    scEl.querySelectorAll('button'),function(b){return b!==scMore})}
  function showAll(){tags().forEach(function(b){b.style.display=''})}
  var PER_GROUP=2;   /* 每组默认露几个——14 组 × 3 个占了 1268px，近两屏 */
  function heads(){return Array.prototype.slice.call(scEl.querySelectorAll('.scg'))}
  function fold(){
    if(open){
      showAll();heads().forEach(function(h){h.style.display=''});
      scMore.textContent='收起';return;
    }
    showAll();
    scMore.textContent='展开全部 '+D.S.length+' 个';
    /* 每组只留前 PER_GROUP 个；组标题始终显示，让用户知道底下还有 */
    var count={};
    tags().forEach(function(b){
      var g=b.dataset.g||'';
      count[g]=(count[g]||0)+1;
      if(count[g]>PER_GROUP)b.style.display='none';
    });
    heads().forEach(function(h){h.style.display=''});
  }
  scMore.onclick=function(){open=!open;fold()};
  fold();
  window.addEventListener('resize',function(){if(!open)fold()});
  /* 默认展开第一个处境。用 open() 而不是 click()：
     click 会走「已选中则折叠」这条分支，导致用户点第二个标签时
     第一下只是取消展开，要点两下才切换。 */
  var first=tags()[0]; if(first && first._open) first._open();
})();
/* ── 历史行 ── */
var _mem=[];
function hload(){try{return JSON.parse(localStorage.getItem('hwx_hist')||'[]')}catch(e){return _mem}}
function hsave(a){_mem=a;try{localStorage.setItem('hwx_hist',JSON.stringify(a))}catch(e){}}
function hrender(){
  var a=hload(),el=document.getElementById('hwx-hist');
  if(!a.length){el.style.display='none';return}
  el.style.display='flex';
  document.getElementById('hwx-hchips').innerHTML=a.slice(0,20).map(function(x){return '<a href="'+x.u+'">'+x.t+'</a>'}).join('');
}
document.addEventListener('click',function(ev){
  var a=ev.target.closest&&ev.target.closest('a[data-h]');if(!a)return;
  var rec=hload().filter(function(x){return x.u!==a.getAttribute('href')});
  rec.unshift({u:a.getAttribute('href'),t:a.getAttribute('data-h')});
  hsave(rec.slice(0,50));hrender();
});
document.getElementById('hwx-hclr').onclick=function(){hsave([]);hrender()};
hrender();
/* ── 类别筛选 ── */
var CAT='全部';
var cw=document.getElementById('hwx-cats');
var cats=['全部'];D.E.forEach(function(e){if(cats.indexOf(e.c)<0)cats.push(e.c)});
cats.forEach(function(c){
  var b=document.createElement('button');b.textContent=c;if(c===CAT)b.classList.add('on');
  b.onclick=function(){CAT=c;cw.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x.textContent===c)});applyFeed()};
  cw.appendChild(b);
});
/* ── CTA 差异化 ── */
function cta(e){
  var T=['拆开看他的 '+e.nc+' 套打法 →','先读「'+(e.c0||'')+'」→','他的答案分 '+e.nc+' 篇讲透 →','进去偷师 →',
         '从「'+(e.c0||'')+'」进 →',e.nc+' 篇，句句能落地 →','看他怎么处理最难的那件事 →','带走 '+e.nc+' 条硬原则 →',
         '深读 '+e.nc+' 篇，够用很久 →','「'+(e.c0||'')+'」值得先看 →','他的方法都在里面 →','读透这 '+e.nc+' 篇再走 →',
         '看完你会换个打法 →',e.nc+' 篇深读备好了 →','从最狠的一篇读起 →','他的路数，'+e.nc+' 篇拆完 →'];
  var h=0;for(var i=0;i<e.s.length;i++)h=(h*31+e.s.charCodeAt(i))>>>0;
  var t=T[h%T.length];
  return(t.indexOf('「」')>=0)?'他的方法都在里面 →':t;
}
/* ── 全部 feed（混排） ── */
/* 金句取用器：按日期确定性洗牌后顺序发牌。
   原来用 (i*步长)%池大小 取句，步长 53 撞上池大小 53 时恒取第一条——
   两个 feed 里十张金句卡全是同一句。改成发牌就不再依赖两个数互质。 */
var _qbag=[], _qi2=0;
(function(){
  var a=D.QS.slice(), seed=day;
  for(var i=a.length-1;i>0;i--){
    seed=(seed*9301+49297)%233280;
    var j=Math.floor(seed/233280*(i+1));
    var t=a[i];a[i]=a[j];a[j]=t;
  }
  _qbag=a;
})();
function pickQ(){ var g=_qbag[_qi2 % _qbag.length]; _qi2++; return g; }
/* 金句卡：竖排金句 + 出处 + 一行解析（角度 · 什么时候用），解析取自章节自身字段 */
function qcard(g,cls){
  var gl = g.gl ? ('<span class="gl">'+g.gl+'</span>') : '';
  return '<a class="qc '+cls+'" href="'+g.u+'" data-h="'+esc(g.who+' · '+g.cn)+'" data-t="'+esc((g.q+g.who+g.cn+(g.gl||'')).toLowerCase())+'">'
    +'<span class="seal">句</span><span class="v">'+g.q+'</span>'
    + gl + '<span class="who"><i>'+g.who+'</i> · '+g.cn+'</span></a>';
}
/* 章节标题与角度并入搜索索引：搜「止损」应命中利弗莫尔等 */
var byNC={};D.NC.forEach(function(n){(byNC[n.pn]=byNC[n.pn]||[]).push(n.cn+' '+n.w+' '+n.q)});
D.S.forEach(function(sc){sc.qs.forEach(function(q){q.a.forEach(function(r){(byNC[r.who]=byNC[r.who]||[]).push(q.q+' '+r.cn+' '+(r.hint||''))})})});
D.QP.forEach(function(q){(byNC[q.who]=byNC[q.who]||[]).push(q.cn+' '+q.q)});
var fullCells=[];
var qi=0,ki=0;
D.E.forEach(function(e,i){
  var chTxt=(byNC[e.n]||[]).join(' ');
  var dt=esc((e.n+' '+e.w+' '+e.c+' '+e.it+' '+e.hk+' '+chTxt+' '+(e.ix||'')).toLowerCase());
  fullCells.push('<a class="pc" href="/i/'+e.s+'/" data-h="'+esc(e.n)+'" data-c="'+e.c+'" data-t="'+dt+'" style="--tint:'+(D.CT[e.c]||'transparent')+';--tintd:'+(D.CTD[e.c]||'transparent')+'"><span class="r1"><b>'+e.n+'</b><i class="tag">'+e.w+'</i></span><span class="it">'+e.it+'</span><span class="hk">'+(e.hk||e.w)+'</span>'+(e.cs.length?'<span class="ls">'+e.cs.join(' / ')+'</span>':'')+'<span class="cf">'+cta(e)+'</span></a>');
  if(i%3===2){var g=pickQ();
    fullCells.push(qcard(g,'xtra'));}
  if(i%5===3){var k=D.QQ[ki++%D.QQ.length];
    fullCells.push('<div class="kc xtra" data-t="'+esc((k.t+(k.s||'')+(k.ss||'')).toLowerCase())+'"><span class="seal">问</span>'+(k.r&&k.r[0]?'<span class="said">'+esc(k.r[0].who)+'问过</span>':'')+'<span class="t">'+k.t+'</span><span class="r">'+k.r.slice(0,1).map(function(r){var w=(D.WHO||{})[r.who];return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b>'+(w?'<u>'+esc(w)+'</u>':'')+'<em>'+r.cn+' →</em></a>'}).join('')+'</span></div>');}
});
/* ── 最新 feed ── */
/* 最新 tab 混排：每 4 张深度阅读插 1 张人物/书卡、1 张金句卡，每 9 槽插 1 张问题卡 */
var ncCells=[], _seen={}, _pi=0, _qi=0, _ki=0;
var byName={}; D.E.forEach(function(e){byName[e.n]=e});
D.NC.forEach(function(e,i){
  ncCells.push('<a class="nc" href="'+e.u+'" data-h="'+esc(e.pn+' · '+e.cn)+'" style="--tint:'+(D.CT[e.c]||'transparent')+';--tintd:'+(D.CTD[e.c]||'transparent')+'"><span class="pn"><i>'+e.pn+'</i><span class="nb">新</span></span><b>'+e.cn+'</b><span class="w">'+e.w+'</span>'+(e.q?'<span class="q">'+e.q+'</span>':'')+'</a>');
  if(i%4===3){
    var pe=null;
    for(var t=0;t<D.NC.length&&!pe;t++){
      var cand=byName[D.NC[(_pi+t)%D.NC.length].pn];
      if(cand&&!_seen[cand.s]){pe=cand;_pi=(_pi+t+1)%D.NC.length}
    }
    if(pe){_seen[pe.s]=1;
      ncCells.push('<a class="pc" href="/i/'+pe.s+'/" data-h="'+esc(pe.n)+'" style="--sp:'+(D.CC[pe.c]||'#999')+'"><span class="r1"><b>'+pe.n+'</b><i class="tag">'+pe.w+'</i></span><span class="it">'+pe.it+'</span><span class="hk">'+(pe.hk||pe.w)+'</span><span class="cf">'+cta(pe)+'</span></a>');}
    var g=pickQ();
    ncCells.push(qcard(g,''));
  }
  if(i%5===4){var k=D.QQ[_ki++%D.QQ.length];
    ncCells.push('<div class="kc"><span class="seal">问</span>'+(k.r&&k.r[0]?'<span class="said">'+esc(k.r[0].who)+'问过</span>':'')+'<span class="t">'+k.t+'</span><span class="r">'+k.r.slice(0,1).map(function(r){var w=(D.WHO||{})[r.who];return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b>'+(w?'<u>'+esc(w)+'</u>':'')+'<em>'+r.cn+' →</em></a>'}).join('')+'</span></div>');}
});
/* ── 处境 tab：每个问题一张卡，标注所属处境 ──
   原来「按处境找」是 1049px 的标签目录，三步才到答案，
   而这些问题 100% 已经在信息流里以卡片出现过。改成卡片流：
   同一批内容、同一套视觉，扫读即认出，不必先学会我们的分类。 */
var scCells=[],scOwner=[],scText=[];
D.S.forEach(function(sc){
  sc.qs.forEach(function(q){
    scOwner.push(sc.t);
    scText.push((q.q+sc.t).toLowerCase());
    scCells.push('<div class="kc" data-t="'+esc((q.q+sc.t).toLowerCase())+'">'
      +'<span class="seal">问</span>'
      +'<span class="said">'+esc(sc.t)+'</span>'
      +'<span class="t">'+q.q+'</span>'
      +'<span class="r">'+q.a.slice(0,1).map(function(r){
          /* 一张卡只举一个例子，并把「这人是谁」补上：两个并列的人名会让读者先做选择题，
             而这张卡要说的是「有人真干过这件事」。省下的那一条，正好换成凭据。 */
          var w=(D.WHO||{})[r.who];
          return '<a href="'+r.u+'" data-h="'+esc(r.who+' · '+r.cn)+'"><b>'+r.who+'</b>'+(w?'<u>'+esc(w)+'</u>':'')+'<em>'+r.cn+' →</em></a>'
        }).join('')+'</span></div>');
  });
});
/* ── 埋点：只发聚合信息，不发用户输入的原文以外的任何东西 ── */
function trk(name, params){
  try{ if(window.gtag) gtag('event', name, params||{}); }catch(e){}
}
/* ── 标签页切换 ── */
/* 默认落在「处境」。原来是「最新」——那是一份按章节文件首次提交时间排的
   更新日志，对第一次来的人毫无意义：他看到的是连着四张蒲松龄，
   因为蒲松龄是最近加的。68 张卡里 40 张挂着「新」标记，而对第一次来的人
   所有东西都是新的。「最新」只对回访者有用，不该当门面。 */
var TAB='境';
var feed=document.getElementById('hwx-feed'), ncfeed=document.getElementById('hwx-ncfeed');
var scfeed=document.getElementById('hwx-scfeed');
var scpick=document.getElementById('hwx-scpick');
/* 选中的处境；空串＝全部。选择保留，切走再切回来还在原来那一格 */
var SCSEL='';
/* 把选中的标签滑进视野：选择会跨 tab 保留，切回来时条子若停在开头，
   卡片是筛过的而标签看着像没选，人会以为坏了。 */
function scReveal(){
  var on=scpick.querySelector('button.on');
  if(!on)return;
  /* 只把 chip 条横向滚到位，**绝不滚页面**。
     原来用 scrollIntoView({block:'nearest'})——看着已经防住了纵向，
     可 chip 条在首屏之下时，'nearest' 仍会把整页往下拉一截去露出它（实测 48px）。
     读者每次落地都发现页面不在顶上，切换语言时尤其明显。 */
  try{scpick.scrollLeft = on.offsetLeft - (scpick.clientWidth - on.offsetWidth)/2}catch(e){}
}
/* 没选任何组时只渲染前 SC_CAP 张。默认落到「处境」之后，
   「全部」会把 521 张卡一次铺完，首页从 11050px 涨到 64761px——
   77 屏，比原来那个 13 屏的信息流糟得多。
   选了组或选了具体处境就不截断：那时候总数本来就只有几个到几十个。 */
var SC_CAP=28;
function scRender(){
  var inGrp={};
  if(SCGRP){D.S.forEach(function(sc){if(sc.g===SCGRP)inGrp[sc.t]=1;});}
  var cells=[],n=0;
  for(var i=0;i<scCells.length;i++){
    var own=scOwner[i];
    var ok = SCSEL ? (own===SCSEL) : (SCGRP ? !!inGrp[own] : true);
    if(ok){n++; if(!SCSEL&&!SCGRP&&cells.length>=SC_CAP)continue; cells.push(scCells[i]);}
  }
  if(!SCSEL&&!SCGRP&&n>cells.length){
    cells.push('<div class="scmore-note">还有 '+(n-cells.length)
      +' 个问题。上面挑一个跟你有关的分组，或者直接搜。</div>');
  }
  scfeed.innerHTML=cells.join('');
  ct.textContent=n+' 个问题';   /* 处境名由选中的标签表达，不再重复一遍 */
}
/* 分两级：先 16 个组，点开才出这一组的处境。
   原来是把 112 个处境拍平成一条横向滚动的双行条——要找到「一直没成」
   得横向划过五十多列，而分组信息（S 里的 g 字段）一直都在，只是没用。
   16 个组一屏放得下，112 个放不下，这是全部的理由。 */
var SCGRP='';
function scGroups(){
  var seen={},out=[];
  D.S.forEach(function(sc){ if(sc.g&&!seen[sc.g]){seen[sc.g]=1;out.push(sc.g);} });
  return out;
}
function scBuild(){
  var h=['<button type="button" data-g=""'+((!SCGRP&&!SCSEL)?' class="on"':'')+'>全部</button>'];
  scGroups().forEach(function(g){
    h.push('<button type="button" data-g="'+esc(g)+'"'+(g===SCGRP?' class="on"':'')+'>'+esc(g)+'</button>');
  });
  if(SCGRP){
    h.push('<span class="scsep" aria-hidden="true"></span>');
    D.S.forEach(function(sc){
      if(sc.g!==SCGRP)return;
      h.push('<button type="button" class="sub'+(sc.t===SCSEL?' on':'')+'" data-s="'+esc(sc.t)+'">'+esc(sc.t)+'</button>');
    });
  }
  scpick.innerHTML=h.join('');
  scpick.querySelectorAll('button').forEach(function(b){
    b.onclick=function(){
      if(b.hasAttribute('data-g')){
        var g=b.getAttribute('data-g');
        SCGRP=(g===SCGRP)?'':g;
        SCSEL='';                                   /* 换组＝回到该组全部 */
        trk('situation_group',{group:SCGRP||'all'});
      }else{
        var v=b.getAttribute('data-s');
        SCSEL=(v===SCSEL)?'':v;                     /* 再点一次＝取消 */
        trk('situation_pick',{situation:SCSEL||'all'});
      }
      scBuild(); scRender();
    };
  });
}
var ct=document.getElementById('hwx-ct');
var catsRow=document.getElementById('hwx-cats');
function switchTab(t){
  TAB=t;
  document.querySelectorAll('#hwx-tabs2 button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-t')===t)});
  if(t==='新'){
    feed.style.display='none';scfeed.style.display='none';ncfeed.style.display='';catsRow.style.display='none';
    scpick.style.display='none';
    ncfeed.innerHTML=ncCells.join('');ct.textContent=D.NC.length+' 篇最新';
  }else if(t==='境'){
    ncfeed.style.display='none';feed.style.display='none';catsRow.style.display='none';
    scfeed.style.display='';scpick.style.display='';
    if(!scpick.firstChild)scBuild();
    scRender();scReveal();
  }else{
    ncfeed.style.display='none';scfeed.style.display='none';feed.style.display='';catsRow.style.display='';
    scpick.style.display='none';
    feed.innerHTML=fullCells.join('');applyFeed();
  }
}
document.querySelectorAll('#hwx-tabs2 button').forEach(function(b){
  b.onclick=function(){var t=b.getAttribute('data-t');
    trk('tab_switch',{tab:t==='新'?'latest':(t==='全'?'all':'situations')});
    switchTab(t)};
});
/* 搜索原来两个毛病叠在一起。
   一是逐字子串（data-t.indexOf(v)），差一个字就 0 条：搜「我很难受」出 0，
   可站里的问句是「这件事为什么让我这么难受？」。
   二是范围只覆盖「全部」里的条目和金句卡——112 个处境、521 个问题
   压根没进索引，所以搜「突然没了工作」（处境名逐字）也是 0，
   而那个处境下面挂着 8 个问题。
   读者进这个站的方式恰恰是用自己的话说处境，最该管用的那类输入全废了。

   改成和悬浮球同一套：二元组 + IDF 加权。稀有的词才是查询的意思所在——
   「的人」在几百张卡里都有，「裁员」只在一两张里有，两者不能同权。
   而且真的按分数排序，不再让 DOM 顺序决定谁在前面。
   处境问题在有查询时一并搜、一并排。 */
function _bg(t){var g={},i;for(i=0;i<t.length-1;i++)g[t.slice(i,i+2)]=1;return g}
var _IDF=null;
function _idf(){
  if(_IDF)return _IDF;
  var df={},docs=[],i;
  feed.querySelectorAll('.pc,.xtra').forEach(function(c){docs.push(c.getAttribute('data-t')||'')});
  for(i=0;i<scText.length;i++)docs.push(scText[i]);
  docs.forEach(function(d){var g=_bg(d);for(var k in g)df[k]=(df[k]||0)+1});
  _IDF={df:df,n:docs.length,dflt:Math.log(docs.length+1)};
  return _IDF;
}
function _score(hay,vg){
  var d=_idf(),s=0;
  for(var k in vg){
    if(hay.indexOf(k)<0)continue;
    var c=d.df[k];
    s+= c?Math.log((d.n+1)/(1+c)):d.dflt;
  }
  return s;
}
function applyFeed(){
  if(!feed||!ct)return;
  var v=(document.getElementById('q')||{value:''}).value.trim().toLowerCase();
  var vg=_bg(v),vn=0,_k;for(_k in vg)vn++;
  var full=vn?_score(v,vg):0;          /* 整条查询自己的权重之和，当阈值的基准 */
  /* 两条判据取「或」。按占比会漏掉一类：搜「我很难受」，站里的问句是
     「这件事为什么让我这么难受？」——只对上「难受」一组，占比不够，
     可「难受」本身在全站只出现在很少几张卡里，它就是这句查询的意思所在。
     所以再加一条绝对权重：命中一个足够稀有的词，就够了。 */
  var need=full*0.32;
  /* 只对短查询放宽。长查询本来就有足够多的组，占比是可靠的；
     再叠一条绝对权重，「一个能约的人都没有」会从 30 条涨到 151 条——
     排序还是对的，但后面全是噪音。 */
  var rare=(vn<=4)?2.6:Infinity;
  var qres=document.getElementById('hwx-qres');
  if(!qres){qres=document.createElement('div');qres.id='hwx-qres';qres.className='scfeed';feed.parentNode.insertBefore(qres,feed);}
  if(!v){
    qres.innerHTML='';qres.style.display='none';
    var _n0=document.getElementById('hwx-none'); if(_n0)_n0.style.display='none';
    var vis0=0;
    feed.querySelectorAll('.pc').forEach(function(c){
      var ok=(CAT==='全部'||c.getAttribute('data-c')===CAT);
      c.classList.toggle('hid',!ok);if(ok)vis0++;});
    feed.querySelectorAll('.xtra').forEach(function(c){
      var ok=(CAT==='全部');c.classList.toggle('hid',!ok);if(ok)vis0++;});
    ct.textContent=vis0+' 条知识';
    return;
  }
  /* 条目卡和金句卡：打分、隐藏低分的、按分数重排 */
  var keep=[];
  feed.querySelectorAll('.pc,.xtra').forEach(function(c){
    var isPc=c.classList.contains('pc');
    var inCat=isPc?(CAT==='全部'||c.getAttribute('data-c')===CAT):(CAT==='全部');
    var hay=c.getAttribute('data-t')||'';
    var sc=(hay.indexOf(v)>=0)?full+1:_score(hay,vg);
    var ok=inCat&&sc>0&&(sc>=need||sc>=rare);
    c.classList.toggle('hid',!ok);
    if(ok)keep.push([sc,c]);
  });
  keep.sort(function(a,b){return b[0]-a[0]});
  keep.forEach(function(p){feed.appendChild(p[1])});
  /* 处境里的问题：只在有查询时出现，排在条目前面——
     用自己的话搜处境的人，要的是「有人问过这件事」，不是一张人物名片。 */
  var hits=[];
  for(var i=0;i<scText.length;i++){
    var t=scText[i];
    var sc2=(t.indexOf(v)>=0)?full+1:_score(t,vg);
    if(sc2>0&&(sc2>=need||sc2>=rare))hits.push([sc2,i]);
  }
  hits.sort(function(a,b){return b[0]-a[0]});
  hits=hits.slice(0,12);
  qres.innerHTML=hits.map(function(p){return scCells[p[1]]}).join('');
  qres.style.display=hits.length?'':'none';
  ct.textContent=(keep.length+hits.length)+' 条知识';
  /* 一条都没有的时候得说话。原来是整片空白——读者分不清是搜不到还是页面坏了。
     另外两个站都有这句（「没有匹配的，换个词试试」「没有匹配的深读」），只有这儿没有。
     出路指向处境：用自己的话搜不到，多半是词不对，而处境是按人话写的。 */
  var none=document.getElementById('hwx-none');
  if(!none){none=document.createElement('div');none.id='hwx-none';none.style.display='none';feed.parentNode.insertBefore(none,feed);}
  if(keep.length+hits.length===0){
    none.innerHTML='<b>没找到「'+esc(v)+'」</b>'
      +'<i>换个说法试试——或者到下面的处境里挑你自己那一件。</i>'
      +'<button type="button" id="hwx-none-go">去挑处境 →</button>';
    none.style.display='';
    var g=document.getElementById('hwx-none-go');
    if(g)g.onclick=function(){
      var qi=document.getElementById('q'); if(qi)qi.value='';
      SCSEL=''; SCGRP=''; switchTab('境'); applyFeed(); scBuild(); scRender(); scReveal();
      var el=document.getElementById('hwx-tabs2');
      if(el&&el.scrollIntoView)try{el.scrollIntoView({block:'start',behavior:'smooth'})}catch(e){}
    };
  }else{none.style.display='none';}
}
/* 搜索框接管 */
var qin=document.getElementById('q');
if(qin){qin.oninput=null;
  /* 搜索落空记录：这是三个埋点里最值钱的一个——用户搜了什么、我们没有，
     直接告诉我们该补什么内容，比坐着推理准得多。
     只在停止输入 1.2 秒后发一次，避免把「睡」「睡不」「睡不着」都记下来。 */
  var _mt=null, _lastMiss='';
  qin.addEventListener('input',function(){
    if(qin.value.trim()&&TAB!=='全'){switchTab('全');}   /* 搜索一律在「全部」里进行 */
    else{applyFeed();}
    clearTimeout(_mt);
    _mt=setTimeout(function(){
      var v=qin.value.trim();
      if(v.length<2||v===_lastMiss)return;
      var n=parseInt((document.getElementById('hwx-ct').textContent||'0'),10)||0;
      _lastMiss=v;
      if(n===0) trk('search_miss',{term:v.slice(0,40)});
      else trk('search_hit',{term:v.slice(0,40), results:n});
    },1200);
  });}
/* 初始化 */
/* 一行入口：点它切到「处境」tab，不再就地展开 1049px 的标签目录 */
(function(){
  var line=document.getElementById('hwx-scline');
  if(!line)return;
  var n=0; D.S.forEach(function(x){n+=x.qs.length});
  var c=document.getElementById('hwx-sccount');
  if(c)c.textContent=D.S.length+' 种处境 · '+n+' 个问题';
  line.onclick=function(){
    trk('situation_entry_click',{});
    switchTab('境');
    document.getElementById('hwx-tabs2').scrollIntoView({behavior:'smooth',block:'start'});
  };
})();
/* 问题卡整块可点。条目卡（.nc）和人物卡（.pc）本来就是一整个 <a>，只有问题卡
   是 div 套一个链接——读者点在卡片别处没反应，等于每张卡有一小片能点、一大片不能。
   委托到 feed 上：点在真链接上走原生跳转，点在卡片别处就跳这张卡唯一那个去处。 */
['hwx-ncfeed','hwx-feed','hwx-scfeed'].forEach(function(id){
  var el=document.getElementById(id); if(!el)return;
  el.addEventListener('click',function(e){
    if(e.target.closest('a'))return;
    var card=e.target.closest('.kc'); if(!card)return;
    var a=card.querySelector('a[href^="/i/"]'); if(!a)return;
    if(e.metaKey||e.ctrlKey||e.shiftKey||e.button)return;
    a.click();
  });
});
/* 卡片点击：用委托，三个 feed 一处覆盖。只记卡片类型和去向，不记内容。 */
['hwx-ncfeed','hwx-feed','hwx-scfeed'].forEach(function(id){
  var el=document.getElementById(id); if(!el)return;
  el.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="/i/"]'); if(!a)return;
    var card=e.target.closest('.pc,.nc,.qc,.kc');
    var kind=card?(card.classList.contains('kc')?'question':
              card.classList.contains('qc')?'quote':
              card.classList.contains('nc')?'chapter':'person'):'other';
    trk('card_click',{card_type:kind, feed:id.replace('hwx-',''), dest:a.getAttribute('href')});
  },true);
});
/* 处境层展开区的答案点击 */
(function(){
  var r=document.getElementById('hwx-res'); if(!r)return;
  r.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="/i/"]'); if(!a)return;
    trk('card_click',{card_type:'situation_answer', feed:'res', dest:a.getAttribute('href')});
  },true);
})();
/* 今日一问的答案点击 */
(function(){
  var g=document.getElementById('hwx-ago'); if(!g)return;
  g.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="/i/"]'); if(!a)return;
    trk('card_click',{card_type:'daily_question', feed:'hero', dest:a.getAttribute('href')});
  },true);
})();
switchTab('境');
})();
""".strip()

    html = (
        HWX_A + "\n"
        "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;600;700;900&display=swap\">\n"
        "<style>" + css + "</style>\n"
        "<section id=\"hwx\">\n"
        "<button id=\"hwx-theme\" type=\"button\" aria-label=\"切换日夜模式\"></button>\n"
        "<div class=\"hist\" id=\"hwx-hist\"><span class=\"hl\">最近看过</span>"
        "<span class=\"hchips\" id=\"hwx-hchips\"></span><button id=\"hwx-hclr\">清空</button></div>"
        "<div class=\"askhero\" id=\"hwx-askhero\">"
        "<div class=\"ahead\"><span class=\"lb\">今日一问</span></div>"
        "<div class=\"q\" id=\"hwx-aq\"></div>""<div id=\"hwx-asc-tag\"></div>""<div class=\"go\" id=\"hwx-ago\"></div>"
        "<div class=\"amine\" id=\"hwx-amine\">"
        "<div class=\"arow\"><textarea id=\"hwx-ain\" rows=\"1\"></textarea>"
        "<button type=\"button\" id=\"hwx-ago2\">问</button></div></div>""</div>"
        "<button class=\"scline\" id=\"hwx-scline\" type=\"button\">"
        "<b>你遇到的是别的事？</b><span id=\"hwx-sccount\"></span>"
        "<i>挑你自己那一件 →</i></button>"
        # 「今日一句」「今日一篇」紧跟在「不是这件事？」下面。
        # 先接住「这条不是我的事」的那个人——给他别的入口，
        # 再顺手给两块随便看看的东西；然后才是搜索和处境列表。
        # 放到整页最底下是过了：那两块有换一换 / 保存卡片 / 分享，
        # 埋到四千像素以下等于废掉。
        "<div class=\"today today-foot\">"
        "<div class=\"tq\"><div class=\"dt\" id=\"hwx-dt\"></div><div class=\"q\" id=\"hwx-tq\"></div>"
        "<div class=\"tgl\" id=\"hwx-tgl\"></div><div class=\"src\" id=\"hwx-tqs\"></div>"
        "<div class=\"acts\"><button id=\"hwx-next\">换一换</button>"
        "<button class=\"bs\" id=\"hwx-save\">保存卡片</button>"
        "<button id=\"hwx-share\">分享</button></div></div>"
        "<div class=\"tcol\">"
        "<div class=\"tbox tbox-s\"><div class=\"lb\">今日一篇</div><a id=\"hwx-tp\"></a></div>"
        "</div></div>"
        "<div class=\"sc\" id=\"hwx-sc\" style=\"display:none\">"
        "<button class=\"scmore\" id=\"hwx-scmore\" type=\"button\"></button></div>"
        "<div class=\"res\" id=\"hwx-res\" style=\"display:none\"></div>"
                "<div class=\"qbar\"><input id=\"q\" placeholder=\"搜你遇到的事：被裁了、睡不着、孩子不听…\" aria-label=\"搜索\"></div>"
        "<div style=\"display:flex;align-items:baseline;justify-content:space-between;margin-top:14px\">"
        "<div class=\"tabs2\" id=\"hwx-tabs2\">"
        "<button data-t=\"新\">最新</button><button data-t=\"全\">全部</button>"
        "<button data-t=\"境\" class=\"on\">处境</button></div>"
        "<span class=\"ct\" id=\"hwx-ct\" style=\"font-size:12px;color:var(--muted);white-space:nowrap;flex:0 0 auto\"></span></div>"
        "<div class=\"cats\" id=\"hwx-cats\" style=\"display:none\"></div>"
        "<div class=\"scpick\" id=\"hwx-scpick\" style=\"display:none\" role=\"group\" aria-label=\"按处境筛选\"></div>"
        "<div class=\"nc-feed\" id=\"hwx-ncfeed\"></div>"
        "<div class=\"feed\" id=\"hwx-feed\" style=\"display:none\"></div><div class=\"nc-feed\" id=\"hwx-scfeed\" style=\"display:none\"></div>"
        # 悬浮球问答不在这里注入——它要出现在每一页，由 patch_chat_widget() 统一挂。
        "<script>var HWXD=" + j + ";</script>"
        "<script>" + js + "</script>"
        "\n</section>\n" + HWX_B
    )
    return html


def patch_home_discover():
    import re
    p = "index.html"
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"\n*" + re.escape(HWX_A) + r".*?" + re.escape(HWX_B) + r"\n*", "", s, flags=re.S)
    # 时间轴已隐藏，遗留的 renderTL 仍在找已删除的计数节点并抛错——让它安全空转
    # 时间轴已隐藏；老 renderTL/rTabs 仍在启动时访问被移除的节点并抛错。
    # stub 会被后面的函数声明覆盖，所以直接把函数体改成空转。
    s = s.replace('function renderTL(){\n  rTabs();',
                  'function renderTL(){\n  return;', 1)
    # 655KB 的汇文明朝体只被旧金句卡（.dq，早已隐藏）用到，首页却无条件加载它——
    # 实测拖慢首屏 4.6 秒，而首次绘制其实只要 0.6 秒。改成运行时按需注入：
    # 只有真的要画旧金句卡时才插入 @font-face，平时一个字节都不下载。
    s = s.replace(
        '@font-face{font-family:"Huiwen-mincho";src:url("hw-mincho-subset.woff2") format("woff2");font-display:swap}',
        '')
    if "__hwFont=function" not in s:   # 幂等：重复构建不叠加
        s = s.replace('<body', '<script>window.__hwFont=function(){'
                      'if(window.__hwFontDone)return;window.__hwFontDone=1;'
                      'var st=document.createElement("style");'
                      'st.textContent=\'@font-face{font-family:"Huiwen-mincho";'
                      'src:url("/hw-mincho-subset.woff2") format("woff2");font-display:swap}\';'
                      'document.head.appendChild(st)};</script><body', 1)
    # 旧金句卡真要用时先注入
    if "if(window.__hwFont)window.__hwFont();" not in s:   # 幂等
        s = s.replace("function dqFont(){",
                      "function dqFont(){\n  if(window.__hwFont)window.__hwFont();", 1)
    # .dq 区块早已隐藏，但它的初始化仍在启动时调用 dqFont() 预取 655KB 字体。
    # 首屏因此从 0.6 秒拖到 4.6 秒。去掉这次预取，字体只在真要画卡时才下载。
    s = s.replace("dqRender();dqFont().then(", "dqRender();Promise.resolve().then(", 1)
    # 二维码换新后文件名不变，浏览器会用旧缓存——按内容哈希击穿
    s = re.sub(r'(wechat-qr\.png)(\?v=[0-9a-f]+)?', r'\1?v=54fb0fdf', s)
    # 文案兜底：每轮构建强制生效，防止 rebase / 其他脚本回写旧值
    s = s.replace("95 位人物与典籍", "100 位人物与典籍")
    # 条目数写死过三次（95 → 100 → 现在），每次加条目都漏改。改成按实际数量回写：
    # 详情页的 slogan 早就是自动的，首页却一直是手填的。
    import sys as _s2
    _s2.path.insert(0, "seo")
    import build_seo as _bs
    _n = len(_bs.load_array())
    s = re.sub(r"<title>人类世界生存法则[^<]*</title>",
               "<title>人类世界生存法则 — %d 位人物与典籍的生存智慧</title>" % _n, s)
    # 标语从「装了什么」改成「能拿来干嘛」——前者让人把它归类成一个收藏，
    # 后者才让人知道现在就能用。
    s = re.sub(r"[\d]+ [个位]人物与典籍的生存智慧，跨越 2600 年", "%s" % SLOGAN_TEXT, s)
    s = re.sub(r"[\d]+ [个位]人物与典籍的生存智慧", "%s" % SLOGAN_TEXT, s)
    s = re.sub(r"(\d+) 位人物与典籍(?=[，、])",
               "%d 位人物与典籍" % _n, s)
    s = s.replace("人类文明的坐标，照亮千年的灯塔",
                  SLOGAN_TEXT)
    # logo 旁的标语已经写了「115 个人物与典籍的生存智慧，跨越 2600 年」，
    # 下面那排 stats 是同一句话拆成三块再说一遍——删掉，并收紧页头下方留白。

    # 页头所在的 .wrap 有 80px 下内距（原本给 stats 和旧内容留的），删掉 stats 后
    # 这块空白就孤零零挂在 logo 下面。只收含页头的那一个 wrap。
    s = s.replace('  .wrap{padding:0 24px 80px}', '  .wrap{padding:0 24px 8px}')
    s = s.replace('.hd-stats{display:flex;gap:20px;flex-wrap:wrap;align-items:center}',
                  '.hd-stats{display:none}')
    # stats 撤掉后页头留下一块空白（它原来撑着高度），把页头的上下留白一并收回
    s = s.replace('#hwx .hist{display:none;align-items:center;gap:8px;margin:2px 0 4px;font-size:13px}',
                  '#hwx .hist{display:none;align-items:center;gap:8px;margin:2px 0 4px;font-size:13px}\n'
                  'header.hd{padding:20px 0 4px!important;margin:0 0 6px!important}\n'
                  'header.hd .brand-lockup,header.hd .brand{margin-bottom:0!important}\n'
                  '#hwx{margin-top:0}')
    # 页头样式改了，升版本号击穿浏览器缓存
    s = s.replace("hw-home-lockup.css?v=2", "hw-home-lockup.css?v=3")
    # stats 节点删了，但仍有代码往 #st / #cat-count 写数——加空值保护
    s = s.replace("document.getElementById('st').textContent=D.length",
                  "(document.getElementById('st')||{}).textContent=D.length")
    s = s.replace("document.getElementById('cat-count').textContent=CATS.length-2",
                  "(document.getElementById('cat-count')||{}).textContent=CATS.length-2")
    # 页头精简：删掉「古今中外 · 东西并观」与页头分享按钮，位置让给「最近看过」
    s = re.sub(r'<span[^>]*>\s*古今中外[^<]*</span>', '', s)
    s = re.sub(r'<button class="share-btn"[^>]*>.*?</button>', '', s, flags=re.S, count=1)
    s = s.replace("古今中外 · 东西并观", "")
    # 去掉 hw-share.js 重复加载
    s = re.sub(r'(?:<script src="/assets/hw-share\.js" defer></script>\s*)+',
               '<script src="/assets/hw-share.js" defer></script>\n', s)
    # noscript h1 降 h2
    s = re.sub(r"(<noscript>)(.*?)(</noscript>)",
               lambda m: m.group(1) + m.group(2).replace("<h1","<h2").replace("</h1>","</h2>") + m.group(3),
               s, flags=re.S)
    # 搜索框原本在页面上方的 toolbar 里，改为置于 最新/全部 标签之上：
    # 移除原位置的 toolbar（保留 input 供 HWX 复用，DOM 由 HWX 块内重建）
    s = re.sub(r'<div class="toolbar">.*?</div>\s*', '', s, flags=re.S, count=1)
    anchor = '<div class="tabs" id="tabs"'
    assert anchor in s, "HWX 锚点丢失"
    s = s.replace(anchor, "\n" + hwx_block() + "\n" + anchor, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("HWX v3 注入完成")



# ---------------- 章节页 og:image 指向各自的分享图 ----------------
# scripts/gen_og.py 一次性生成 i/<slug>/<k>/og.png（静态资产，不进 CI 链）。
# 这里在每次构建后把「存在 og.png 的章节页」的 og:image / og:image:alt /
# twitter:image 改写为该页专属图；没有图的页面保持全站图，优雅降级。
def patch_chapter_og():
    import os, re
    n = 0
    for slug in os.listdir("i"):
        d1 = os.path.join("i", slug)
        if not os.path.isdir(d1):
            continue
        for k in os.listdir(d1):
            d2 = os.path.join(d1, k)
            page = os.path.join(d2, "index.html")
            png = os.path.join(d2, "og.png")
            if not (os.path.isdir(d2) and os.path.exists(page) and os.path.exists(png)):
                continue
            s = open(page, encoding="utf-8").read()
            url = "https://ourword.ai/i/%s/%s/og.png" % (slug, k)
            m = re.search(r"<title>([^<|]+)", s)
            alt = (m.group(1).strip() if m else "深度阅读")
            s2 = re.sub(r'(<meta property="og:image" content=")[^"]*(")', r"\g<1>%s\g<2>" % url, s)
            s2 = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(")', r"\g<1>%s\g<2>" % alt.replace("\\", ""), s2)
            s2 = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', r"\g<1>%s\g<2>" % url, s2)
            if s2 != s:
                open(page, "w", encoding="utf-8").write(s2)
                n += 1
    print("chapter og:image rewired:", n)




def patch_entry_og():
    """人物页的分享图：有 i/<slug>/og.png 就指过去，没有仍回落到全站图。
    人物页的 head 由 geo_kit 生成（不能改），所以和章节页一样在这里事后改写。"""
    import os, re
    n = 0
    for slug in os.listdir("i"):
        page = os.path.join("i", slug, "index.html")
        png = os.path.join("i", slug, "og.png")
        if not (os.path.exists(page) and os.path.exists(png)):
            continue
        s = open(page, encoding="utf-8").read()
        url = "https://ourword.ai/i/%s/og.png" % slug
        m = re.search(r"<title>([^<|—]+)", s)
        alt = (m.group(1).strip() if m else "人物").replace("\\", "")
        s2 = re.sub(r'(<meta property="og:image" content=")[^"]*(")', lambda mm: mm.group(1) + url + mm.group(2), s)
        s2 = re.sub(r'(<meta property="og:image:alt" content=")[^"]*(")', lambda mm: mm.group(1) + alt + mm.group(2), s2)
        s2 = re.sub(r'(<meta name="twitter:image" content=")[^"]*(")', lambda mm: mm.group(1) + url + mm.group(2), s2)
        if s2 != s:
            open(page, "w", encoding="utf-8").write(s2)
            n += 1
    print("entry og:image rewired:", n)





def patch_chapter_scene():
    """章节页末尾加一块「同一件事，还有人这么问」。

    从搜索或 AI 引流进来的人，落地就是一篇章节页。他被说中了，然后呢——
    页尾只有「上一篇 / 下一篇」，那是按书目顺序排的，是这本书的目录，
    不是他的处境。112 个处境、521 个问题就在数据里，章节页一个字都没提。

    放在「这一篇如果说中了你正在经历的事」之前：先给同类，再谈转发。
    """
    import os, re, html as _h
    by_ch = {}
    for t, g, qs in HWX_SCENES:
        for qtext, refs in qs:
            for sl, kk in refs:
                by_ch.setdefault((sl, kk), set()).add(t)
    n = 0
    for (sl, kk), scenes in by_ch.items():
        page = os.path.join("i", sl, kk, "index.html")
        if not os.path.exists(page):
            continue
        s = open(page, encoding="utf-8").read()
        if 'class="hw-same"' in s or '<div class="hw-outro">' not in s:
            continue
        sc = sorted(scenes)[0]
        qs = next(q for t, g, q in HWX_SCENES if t == sc)[1] if False else None
        for t, g, q in HWX_SCENES:
            if t == sc:
                qs = q
                break
        rows = []
        for qtext, refs in qs:
            if not refs:
                continue
            # 原来把「答案里含本篇」的问题整条剔掉，结果同处境里最贴的几个
            # 全被滤走，还出现过一页一条都不剩。改成只换链接：优先指向别的篇，
            # 全都是这一篇时就还指它——问题本身不一样，值得列出来。
            alt = [r for r in refs if r != (sl, kk)] or list(refs)
            rows.append((qtext, "/i/%s/%s/" % alt[0]))
            if len(rows) >= 4:
                break
        if not rows:
            continue
        blk = ('<section class="hw-same"><p class="ph">同一件事，还有人这么问</p>'
               + "".join('<a href="%s">%s</a>' % (u, _h.escape(q)) for q, u in rows)
               + '<a class="more" href="/#hwx-tabs2">%s · 全部 %d 个问题 →</a></section>'
                 % (_h.escape(sc), len(qs)))
        s = s.replace('<div class="hw-outro">', blk + '<div class="hw-outro">', 1)
        open(page, "w", encoding="utf-8").write(s)
        n += 1
    print("chapter same-scene block:", n)




# ---------------- 条目页：手写介绍替换模板句 ----------------
# 原 dek 是 "格雷厄姆（美·1894-1976年）——安全边际·市场先生。"，与上一行 .one 重复、
# 信息量为零。改用 HWX_INTROS 的手写介绍；无手写介绍的条目保留原句。
def patch_entry_intro():
    import os, re, sys
    sys.path.insert(0, "seo")
    import hw_slugs, build_seo
    n = 0
    for e in build_seo.load_array():
        slug = hw_slugs.slug_for(e["n"])
        intro = HWX_INTROS.get(slug)
        page = os.path.join("i", slug, "index.html")
        if not (intro and os.path.exists(page)):
            continue
        s = open(page, encoding="utf-8").read()
        s2 = re.sub(r'<p class="dek">[^<]*</p>',
                    '<p class="dek">%s</p>' % intro, s, count=1)
        if s2 != s:
            open(page, "w", encoding="utf-8").write(s2)
            n += 1
    print("entry intro rewritten:", n)


# ---------------- 全站：日夜切换按钮 ----------------
# 首页的按钮在 HWX 块里；其余页面（条目页/章节页/主题页）在这里统一注入。
HWX_T_A, HWX_T_B = "<!--HWX:THEME-->", "<!--/HWX:THEME-->"

def theme_widget():
    css = (
        # 站点主变量 + hw-entry/hw-chapter 的整套变量（不补全这些，正文会用亮色墨值印在暗底）
        ':root[data-theme="dark"]{--paper:#171410;--ink:#eae3d4;--acc:#c65f4f;'
        '--line:#3a342a;--white:#1d1913;--line-strong:rgba(234,227,212,.22);'
        '--ink-30:rgba(234,227,212,.42);--ink-50:rgba(234,227,212,.6);--paper2:#201c15;'
        '--bg:#171410;--bg-tint:#201c15;--surface:#1d1913;--surface-2:#232019;'
        '--ink-2:#d9d1c0;--muted:#a79e8b;--faint:#8b8371;'
        '--rule:#3a342a;--rule-2:#443d31;--seal:#e0705f;--seal-soft:#3a221f;'
        '--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -18px rgba(0,0,0,.6)}'
        ':root[data-theme="dark"] body{background:var(--bg);color:var(--ink)}'
        ':root[data-theme="dark"] .panel,:root[data-theme="dark"] article{background:transparent}'
        # 正文与次级文本走变量，覆盖硬编码墨色（原来 #3f3a34 在暗底对比度仅 1.63）
        ':root[data-theme="dark"] p,:root[data-theme="dark"] li,:root[data-theme="dark"] .dek,'
        ':root[data-theme="dark"] .one,:root[data-theme="dark"] .f-d,:root[data-theme="dark"] .eg,'
        ':root[data-theme="dark"] blockquote{color:var(--ink-2)}'
        ':root[data-theme="dark"] .src,:root[data-theme="dark"] .why,:root[data-theme="dark"] .meta,'
        ':root[data-theme="dark"] .sub,:root[data-theme="dark"] .crumb{color:var(--muted)}'
        # 朱红提亮：#9d2933 在暗底只有 2.45
        ':root[data-theme="dark"] .kicker,:root[data-theme="dark"] .sec-k,:root[data-theme="dark"] .dot,'
        ':root[data-theme="dark"] mark.hl,:root[data-theme="dark"] .seal,'
        ':root[data-theme="dark"] .chip.on{color:#e0705f}'
        ':root[data-theme="dark"] mark.hl{text-decoration:none}'
        # 浅底区块：背景跟随暗色，否则白底白字（实测对比度 1.26）
        ':root[data-theme="dark"] .card,:root[data-theme="dark"] .map,:root[data-theme="dark"] .rel,'
        ':root[data-theme="dark"] .box,:root[data-theme="dark"] .quote-card,:root[data-theme="dark"] .panel,'
        ':root[data-theme="dark"] .chip,:root[data-theme="dark"] .side .panel'
        '{background:var(--surface);border-color:var(--rule)}'
        ':root[data-theme="dark"] .map-n,:root[data-theme="dark"] .n,'
        ':root[data-theme="dark"] a{color:var(--ink)}'
        ':root[data-theme="dark"] .toc a,:root[data-theme="dark"] .sib a{color:var(--ink-2)}'
        ':root[data-theme="dark"] .share-btn{background:var(--surface);color:var(--ink);border-color:var(--line-strong)}'
        ':root[data-theme="dark"] .sep,:root[data-theme="dark"] .crumb .sep{color:var(--faint)}'
        ':root[data-theme="dark"] mark.hl,:root[data-theme="dark"] article mark.hl{color:#e0705f!important;background:transparent}'
        ':root[data-theme="dark"] .map,:root[data-theme="dark"] .map *,'
        ':root[data-theme="dark"] .rel,:root[data-theme="dark"] .rel *{background-color:transparent}'
        ':root[data-theme="dark"] .map,:root[data-theme="dark"] .rel{background:var(--surface)!important}'
        ':root[data-theme="dark"] .map-cat,:root[data-theme="dark"] .map-list,'
        ':root[data-theme="dark"] .map-row{background:var(--surface)!important;border-color:var(--rule)!important}'
        ':root[data-theme="dark"] .map-n{color:var(--ink)!important}'
        ':root[data-theme="dark"] .map-w,:root[data-theme="dark"] .map-line{color:var(--muted)!important}'
        ':root[data-theme="dark"] .map .why,:root[data-theme="dark"] .rel .why{color:var(--muted)!important}'
        '#hwx-theme{position:fixed;top:14px;right:14px;z-index:9999;width:36px;height:36px;'
        'border:1px solid var(--rule,#d8d2c6);background:var(--paper,#f5f1e8);color:var(--ink,#1f1c17);'
        'border-radius:50%;font-size:15px;line-height:1;cursor:pointer;display:flex;align-items:center;'
        'justify-content:center;box-shadow:0 1px 6px rgba(0,0,0,.10);padding:0}'
        '#hwx-theme:hover{border-color:#9d2933;color:#9d2933}'
    )
    js = (
        "(function(){var R=document.documentElement,K='hwx_theme';"
        "function sd(){return !!(window.matchMedia&&window.matchMedia('(prefers-color-scheme:dark)').matches)}"
        "function g(){try{return localStorage.getItem(K)||''}catch(e){return ''}}"
        "function st(v){try{localStorage.setItem(K,v)}catch(e){}}"
        "function eff(){return g()||(sd()?'dark':'light')}"
        "function paint(){var m=eff();R.setAttribute('data-theme',m);"
        "var b=document.getElementById('hwx-theme');"
        "if(b){b.textContent=(m==='dark'?'\\u2600':'\\u263e');"
        "b.setAttribute('title',m==='dark'?'切换到日间':'切换到夜间')}}"
        "paint();document.addEventListener('DOMContentLoaded',function(){"
        "var b=document.getElementById('hwx-theme');if(!b)return;"
        "b.onclick=function(){st(eff()==='dark'?'light':'dark');paint()};paint()});})();"
    )
    return (HWX_T_A + '<style>' + css + '</style>'
            '<button id="hwx-theme" type="button" aria-label="切换日夜模式"></button>'
            '<script>' + js + '</script>' + HWX_T_B)



def _derived(dp):
    """这个目录是不是「派生出来的语言站」——是的话本脚本一个字都不该碰。

    tw/ 由 build_tw.py 从简体产物整树转出，en/ 由 build_en.py 用英文数据生成。
    本脚本往页面里盖的是**简体**挂件（切换日夜模式、/assets/… 的资源路径、
    大陆支付宝收款码）。盖到 tw/ 上的后果实测过：553 页的「切換」变回「切换」、
    资源指回简体站、繁体读者的 AlipayHK 码被换成大陆码 —— 而页面照样渲染，
    构建照样通过，只有逐字比对才看得出来。

    正常构建链里 build_tw.py 排在本脚本之后并且整树重建，所以看不出问题；
    单独跑本脚本就会留下这份污染。五个 walk 里原先只有一个记得躲开 tw/。
    """
    # **必须按路径段比，不能按子串比。** 第一版写的是 "/tw" in dp，于是
    # i/han-feizi/two-handles/ 被当成繁体目录跳过 —— "/two-handles" 里就含
    # "/tw"。这样误伤了 5 页（two-nogales、two-kinds、two-handles、
    # two-ways-of-seeing、enlarging-huaihai），它们整层语言层、夜间模式、
    # 聊天挂件全都没有，而且没有任何报错。
    segs = [x for x in dp.replace("\\", "/").split("/") if x not in ("", ".")]
    return bool(set(segs) & {".git", "tw", "en", "node_modules", "__pycache__"})
def patch_theme_widget():
    import os, re
    n = 0
    for dp, dn, fn in os.walk("."):
        if _derived(dp) or dp.startswith("./assets"):
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            path = os.path.join(dp, f)
            s = open(path, encoding="utf-8").read()
            if 'http-equiv="refresh"' in s:      # 跳转桩跳过
                continue
            if path == "./index.html":           # 首页按钮在 HWX 块里
                continue
            s2 = re.sub(re.escape(HWX_T_A) + r".*?" + re.escape(HWX_T_B), "", s, flags=re.S)
            if "</body>" not in s2:
                continue
            s2 = s2.replace("</body>", theme_widget() + "</body>", 1)
            if s2 != s:
                open(path, "w", encoding="utf-8").write(s2)
                n += 1
    print("theme widget on pages:", n)


def patch_chapter_intro():
    """章节页的人名底下加一句「这人是谁」。

    章节页是搜索和 AI 引流的落地页——读者是带着自己的处境进来的，
    多数不认识页头那个名字。全站 159 条里有 24 条是普通读者没听过的，
    而且集中在家庭与关系、身心与生活这两组（那两组本来就该由专门研究
    这件事的人来答，不该让熟名字去答他没研究过的事）。

    介绍句本来就有（HWX_INTROS，159 条全覆盖），此前只出现在人物页和
    「全部」信息流卡上，恰好不在读者第一次碰到这个名字的地方。
    """
    import os, re, html as _h
    n = 0
    for slug in sorted(os.listdir("i")):
        intro = HWX_INTROS.get(slug)
        d1 = os.path.join("i", slug)
        if not (intro and os.path.isdir(d1)):
            continue
        for k in sorted(os.listdir(d1)):
            page = os.path.join(d1, k, "index.html")
            if not os.path.exists(page):
                continue
            s = open(page, encoding="utf-8").read()
            if 'class="who"' in s:
                continue
            # 有几条介绍句本身就是从这一篇的标题来的（鲍恩那句含「既在关系里，又是自己」），
            # 放上去就成了同一屏读两遍。撞了就跳过——那种页面本来也不缺凭据。
            body = re.sub(r"<[^>]+>", "", s)
            if any(intro[i:i + 8] in body for i in range(max(1, len(intro) - 7))):
                continue
            s2, cnt = re.subn(r'(<p class="kicker">[^<]*</p>)',
                              lambda m: m.group(1) + '<p class="who">%s</p>' % _h.escape(intro),
                              s, count=1)
            if cnt and s2 != s:
                open(page, "w", encoding="utf-8").write(s2)
                n += 1
    print("chapter who-line:", n)


def patch_icons():
    """给每一页补 favicon 声明。

    首页声明了 /favicon.svg，535 个人物页/章节页一条都没有——浏览器只能回退去要
    根目录的 /favicon.ico，而那个文件是个黑底白十字，跟站上的红「人」毫无关系。
    读者收藏一篇文章，书签栏里出现的就是那个十字。
    （ico 本身也换成了从 icon-512.png 渲的 16/32/48 三档。）

    条目页的 head 由 geo_kit 生成、章节页由 hw_chapters 手拼，两处都没有 icon，
    所以和 og 一样在这里事后补，一处覆盖全站。
    """
    import os, re
    ICONS = ('<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
             '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">\n'
             '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">\n')
    n = 0
    for dp, dn, fn in os.walk("."):
        if _derived(dp):
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            path = os.path.join(dp, f)
            s = open(path, encoding="utf-8").read()
            if 'rel="icon"' in s or 'http-equiv="refresh"' in s:
                continue
            m = re.search(r'<meta name="viewport"[^>]*>\n?', s)
            if not m:
                m = re.search(r'<meta charset="[^"]*">\n?', s)
            if not m:
                continue
            s2 = s[:m.end()] + ICONS + s[m.end():]
            open(path, "w", encoding="utf-8").write(s2)
            n += 1
    print("favicon 声明补上:", n)







HWQ_A, HWQ_B = "<!--HWX:CHAT-->", "<!--/HWX:CHAT-->"


def chat_widget():
    """悬浮球问答的注入块。HW_CHAT_ENDPOINT 为空时返回空串——
    前端脚本本来也会 return，但连 <script> 都不发更干净，也省一次请求。"""
    if not HW_CHAT_ENDPOINT:
        return ""
    return (HWQ_A
            + '<script>window.HW_CHAT_ENDPOINT="' + HW_CHAT_ENDPOINT + '";</script>'
            + '<script src="/assets/hw-chat.js?v=24" defer></script>'
            + HWQ_B)


def patch_chat_widget():
    """悬浮球要全局出现，所以走和 patch_theme_widget 一样的全站扫描。

    首页也走这里（不像主题按钮那样特例挂在 HWX 块里）——同一个东西两处注入，
    迟早有一处忘了改。先剥掉旧块再插新块，所以是幂等的；
    把 HW_CHAT_ENDPOINT 改回 "" 再跑一次，全站就干净了。
    """
    import os, re
    n = 0
    block = chat_widget()
    for dp, dn, fn in os.walk("."):
        if _derived(dp) or dp.startswith("./assets"):
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            path = os.path.join(dp, f)
            s = open(path, encoding="utf-8").read()
            if 'http-equiv="refresh"' in s:      # 跳转桩跳过
                continue
            s2 = re.sub(re.escape(HWQ_A) + r".*?" + re.escape(HWQ_B), "", s, flags=re.S)
            if "</body>" not in s2:
                continue
            if block:
                s2 = s2.replace("</body>", block + "</body>", 1)
            if s2 != s:
                open(path, "w", encoding="utf-8").write(s2)
                n += 1
    print("chat widget on pages:", n)




HWT_A, HWT_B = "<!--HWX:TEA-->", "<!--/HWX:TEA-->"


def tea_widget():
    """「请喝茶」弹层脚本。没有收款图时返回空串，全站连 <script> 都不发。"""
    if not TEA_ON:
        return ""
    import json
    cfg = json.dumps({"wechat": "/assets/pay-wechat.png?v=1" if TEA_WECHAT else "", "alipay": "/assets/pay-alipay.png?v=1",
                      "alipayLink": TEA_ALIPAY_LINK}, ensure_ascii=False)
    return (HWT_A + "<script>window.HW_TEA=" + cfg + ";</script>"
            + '<script src="/assets/hw-tea.js?v=1" defer></script>' + HWT_B)


def patch_tea_widget():
    """和 patch_chat_widget 同一套：先剥旧块再插新块，幂等；TEA_ON 为假时全站剥干净。"""
    import os, re
    n = 0
    block = tea_widget()
    for dp, dn, fn in os.walk("."):
        if _derived(dp) or dp.startswith("./assets"):
            continue
        for f in fn:
            if f not in ("index.html", "404.html"):
                continue
            path = os.path.join(dp, f)
            s = open(path, encoding="utf-8").read()
            if 'http-equiv="refresh"' in s:
                continue
            s2 = re.sub(re.escape(HWT_A) + r".*?" + re.escape(HWT_B), "", s, flags=re.S)
            if "</body>" not in s2:
                continue
            if block:
                s2 = s2.replace("</body>", block + "</body>", 1)
            if s2 != s:
                open(path, "w", encoding="utf-8").write(s2)
                n += 1
    print("tea widget on pages:", n)





# ---------------- 繁体版：hreflang + 语言切换 + 首访跟随 ----------------
HWL_A, HWL_B = "<!--HWX:LANG-->", "<!--/HWX:LANG-->"


def patch_lang():
    import hwx_lang
    hwx_lang.patch_tree(".")


if __name__ == "__main__":
    patch_home_discover()
    patch_chapter_og()
    patch_entry_og()
    patch_chapter_scene()
    patch_entry_intro()
    patch_chapter_intro()
    patch_icons()
    patch_theme_widget()
    patch_chat_widget()
    patch_tea_widget()
    patch_lang()
