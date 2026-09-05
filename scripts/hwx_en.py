# -*- coding: utf-8 -*-
"""英文首页要用的几张表。

首页那套 JS 一行都不改 —— 它读的是 HWXD 这个数据块，英文站只是喂它另一份
同样形状的数据。所以这里要备齐中文那边同名的几张表：

  SC_BOX     每个处境的预填句：读者点开处境后，输入框里已经替他写好的那句话。
             它和卡片上的问句相距三厘米，**不能是同一句话的复述** ——
             构建时有硬断言逐条查重。
  SC_SHORT   处境的短名，进 chip 条用。英文多数本来就短，只收长的那几个。
  INTROS     每个条目一句话介绍。卡片上的名字英文读者多半不认识，
             这一句要出现在他第一次碰到这个名字的地方。
  QQ         首页「今日一问」的手写卡片。
  SYNONYMS   搜索同义词：读者打 "burnout"，要能找到马斯拉赫。
"""

# 预填句：读者会打进输入框的那句话。写法是「现在的状态 + 怕什么 + 先怎么办」，
# 和卡片上那句「你是不是……」的问句是两种不同的话。
SC_BOX = {
    # Facing an opponent
    "Winning is costing too much":
        "Every round goes my way and there is less of me afterwards. What am "
        "I spending that nobody counts?",
    # Getting it done
    "I'm managing it and it's getting worse":
        "Every fix I add seems to create the next problem. What should I "
        "stop doing?",
    # Making a call
    "Anger just took over":
        "I'm wound up and afraid that if I speak now I'll wreck it. Where do I start?",
    "It turned into a fight":
        "We're locked in and every sentence is raising the stakes. How do I bring this down?",
    "I keep not starting":
        "I've carried this around for weeks, thought about it daily, and touched none of it. How do I begin today?",
    "A decision I can't undo":
        "Once I move there's no going back, and I've run the numbers and still can't press. How should I judge it?",
    "I don't have enough information":
        "I don't know the things I'd need to know, and the deadline is fixed. How do I decide anyway?",
    "They said no to my plan":
        "Since the no I've been wondering whether it's me, and I haven't raised it again. What's my next move?",
    # Facing an opponent
    "They're setting the pace":
        "Everything I do lately is a response to them. How do I get the initiative back?",
    "After the win":
        "A run of good results, and I cannot tell if this is the moment to push or to stop. How do I decide?",
    # Money
    "Making money work":
        "There's cash sitting there and leaving it alone makes me uneasy. What should I be thinking about?",
    "Not enough money":
        "The numbers don't reach the end of the month and I keep re-adding them. What do I do first?",
    # Dealing with people
    "Can I trust this person":
        "Everything he says sounds right and something in me won't settle. How do I check?",
    "I don't believe what my boss says":
        "I've stopped taking the promises at face value and I still have to work here. How do I handle it?",
    "They've started watching me":
        "Things went well for me and now I can feel the room change. What should I do?",
    "Do I trust my gut":
        "Something in me says one thing and my reasoning says another. Which do I follow?",
    "Someone is being unreasonable":
        "He isn't playing straight and I'm deciding how far to go. What's the right move?",
    "I can't stop pleasing people":
        "I agree to things I don't want and then carry them for weeks. How do I stop?",
    "My partner and I are falling out":
        "The two of us built this and now it's coming apart. How do I handle the split?",
    "None of it means anything":
        "I do the days and nothing in them reaches me. Where do I even start?",
    "Should I leave this job":
        "I go in, I do it, and I've stopped believing in any of it. How do I decide whether to go?",
    "I trusted the wrong person":
        "Someone took advantage of me and since then I keep everybody at a distance. How do I loosen that?",
    "I have no one to call":
        "There's nobody I could ring without a reason, and I've been here a while. Where do I start?",
    # Leading people
    "The same mistakes keep happening":
        "It's gone wrong the same way three times and telling people hasn't changed it. What do I change?",
    "The team has gone flat":
        "Nobody is pushing on anything and I've tried the obvious levers. What now?",
    "Nothing ships":
        "I explain what's needed and what comes back is something else. What am I doing wrong?",
    # Getting it done
    "Starting from nothing":
        "There's no money, no name and no one waiting for it. What's the first thing?",
    "Things are going well and it scares me":
        "Everything is going smoothly and that itself makes me uneasy. What ought I to prepare?",
    "Nobody is looking at my work":
        "I keep making things and they land on nobody. Do I keep going?",
    # How you're doing
    "I'm at the bottom":
        "This is the lowest it's been and the days are long. How do I get through them?",
    "I overthink everything":
        "The same thoughts run all day and none of them end anywhere. How do I stop?",
    "I know better and still don't do it":
        "I can give someone else the right advice on this and never take it myself. What is in the way?",
    "Nothing I study stays":
        "I read and I forget and nothing carries into the work. How should I be learning?",
    "Too busy to have a life":
        "Every hour is spoken for and none of them are mine. How do I get some back?",
    "Someone is ahead of me":
        "Watching people my age do well leaves me flat for the rest of the day. How do I deal with it?",
    "I don't want to race but I'm scared to stop":
        "Living at this pace is wrong for me, and slowing down frightens me more. What are my options?",
    # When to step back
    "Should I step back":
        "It's gone as far as I can take it and leaving feels like losing. How do I think about it?",
    # AI arrived
    "Will my line of work still exist":
        "What I do for a living is changing under me and nobody can say how fast. What should I do now?",
    "I can't keep up with the new thing":
        "The ground shifted and my hours are all going into the old skill. How do I catch up?",
    "My craft stopped being worth anything":
        "The thing I spent years getting good at is worth less every month. What do I do with it?",
    "The tool does my thinking":
        "I hand things over and then can't explain what I handed in. How do I fix this?",
    "More output, emptier":
        "My output has gone up and something in the work has drained away. What is missing?",
    "Do I jump in now":
        "Everyone is moving and I can't tell if it's early or late. How do I decide?",
    "I don't know what to practice anymore":
        "The bar keeps moving and I've stopped knowing what to get good at. Where should I put the hours?",
    # At home
    "We keep fighting":
        "We've had the same argument so many times we could recite it. How do we stop?",
    "My kid won't listen":
        "I've asked the same thing a hundred ways and nothing lands. What should I try?",
    "My kid stopped talking to me":
        "He used to tell me things and now he doesn't. How do I get back in?",
    "The work at home doesn't count":
        "The cooking, the laundry, the appointments — none of it shows up anywhere. How do I raise this?",
    "Caring for a parent":
        "Someone at home needs me every day and I'm running out. What can I actually do?",
    "I was betrayed":
        "Something happened behind my back and I can't unknow it. How do I decide what's next?",
    "Years in, nothing left between us":
        "We've been together a long time and there's nothing in the room. What can be done?",
    # Body and energy
    "I can't sleep":
        "I lie down and my head starts and it's been like this for months. What should I change?",
    "I've run out of energy":
        "I sleep and it doesn't restore anything. Where is this going?",
    "I want to change a habit":
        "I've been at the same thing for months with nothing to show. What am I missing?",
    "I've been tense for a long time":
        "It has been months since I was genuinely off duty in my own head. What do I do?",
    "I keep trying to quit":
        "I stop, and then a few weeks later I'm back. How do I make it stick?",
    "I have nothing left to give":
        "I get through the day and there's nothing in me afterwards. What is this?",
    "There's never enough time":
        "There is always more than the day holds. How do I get on top of it?",
    "I got sick":
        "Something is wrong with my health and it's going to be a long thing. How do I live with it?",
    # Starting out
    "Straight A's, then no more grades":
        "I did everything right and now nobody is telling me what right is. What do I do?",
    "My first job":
        "Two weeks in and most of what lands on my desk is beyond me. How do I get up to speed?",
    "Should I go back to school":
        "I'm considering more study and I can't say what it buys me. How do I decide?",
    "What I studied doesn't apply":
        "None of what I learned survives contact with the actual work. Where do I start?",
    # A turn in the road
    "I lost my job":
        "It ended and I have a few months of money. What do I do first?",
    "Someone I needed is gone":
        "The person I leaned on has died and tomorrow still arrives. How do I get through this?",
    "Starting over":
        "I'm beginning again from nothing at an age where that's unusual. Where do I start?",
    "I can't carry it anymore":
        "What used to hold me up has stopped working. What do I do now?",
    "Moving somewhere new":
        "I've moved and I know almost nobody here. How do I build something?",
    "Middle of my life":
        "On paper it's fine and something in it has gone quiet. What's happening?",
    # Nothing's moving
    "It's already done and I can't undo it":
        "It happened, it's finished, and I go over it every day. How do I put it down?",
    "It still hasn't worked":
        "I have been at this a very long time with nothing to show. Do I keep going?",
    "They've put me on the shelf":
        "The work has drained away and nobody says why. What should I do?",
    # Looking back, moving on
    "The side thing worked, the main thing didn't":
        "My proper job has stalled while the evening project keeps picking up. What do I make of that?",
    "I never put it down":
        "Something from years ago still sits in my chest. How do I get past it?",
    "I don't know what I want":
        "I can describe what I don't want in detail and nothing else. How do I work it out?",
    "Too many paths":
        "Several options and every one of them makes sense. How do I choose?",
    "Do I change direction now":
        "Switching tracks would cost me everything I've built. How do I weigh it?",
    # Things you don't say out loud
    "I can't stand other people's good news":
        "When people near me do well I feel something ugly. What do I do with that?",
    "I'm the one who did wrong":
        "I caused real harm to someone and I have carried it ever since. How do I handle it?",
    "They'll find out I can't do this":
        "I'm in a role I don't feel equal to and I keep waiting to be found out. What helps?",
    "I can't let go of someone":
        "It's been a long time and they're still the first thing I think about. What do I do?",
    "I've started being afraid of dying":
        "I've become aware of how much time is left and it's changed everything. How do I sit with it?",
}

# 短名：进 chip 条用。英文多数本来就短，只收超过 30 个字符的那几个。
SC_SHORT = {
    "I don't want to race but I'm scared to stop": "Don't want to race",
    "The side thing worked, the main thing didn't": "The side thing won",
    "Things are going well and it scares me": "Going well, and scared",
    "I don't know what to practice anymore": "What do I practise",
    "My craft stopped being worth anything": "My craft lost value",
    "Will my line of work still exist": "Will this job exist",
    "I know better and still don't do it": "Know it, don't do it",
    "It's already done and I can't undo it": "Already done",
    "I can't stand other people's good news": "Other people's good news",
    "They'll find out I can't do this": "They'll find out",
    "I've started being afraid of dying": "Afraid of dying",
    "Straight A's, then no more grades": "No more grades",
    "I don't have enough information": "Not enough information",
    "Years in, nothing left between us": "Nothing left between us",
    "The same mistakes keep happening": "Same mistakes again",
    "I've been tense for a long time": "Tense for a long time",
    "The work at home doesn't count": "Work at home",
    "I don't believe what my boss says": "Can't believe my boss",
    "My partner and I are falling out": "Partner falling out",
    "I have nothing left to give": "Nothing left to give",
    "What I studied doesn't apply": "What I studied",
    "Someone is being unreasonable": "Being unreasonable",
    "I can't stop pleasing people": "Can't stop pleasing",
    "I can't keep up with the new thing": "Can't keep up",
    "They've put me on the shelf": "On the shelf",
    "Should I go back to school": "Back to school",
    "My kid stopped talking to me": "Kid stopped talking",
    "I trusted the wrong person": "Trusted wrong person",
    "There's never enough time": "Never enough time",
    "Someone I needed is gone": "Someone is gone",
    "I can't carry it anymore": "Can't carry it",
    "I can't let go of someone": "Can't let go",
    "I'm the one who did wrong": "I did wrong",
    "None of it means anything": "Means nothing",
    "Nobody is looking at my work": "Nobody's looking",
    "The tool does my thinking": "Tool thinks for me",
    "Moving somewhere new": "Somewhere new",
}

# 条目介绍：一句话说清「这是谁、为什么在这里」。卡片上的名字英文读者多半
# 不认识，这一句要出现在他第一次碰到名字的地方。
INTROS = {
    "su-shi": "Song poet, exiled three times, and freer each time it happened",
    "wang-yangming": "A philosopher who was also his generation's best general",
    "zhuangzi": "Turned down the government of a state to stay in the mud",
    "pu-songling": "Sat the exam for forty years, never passed, wrote the classic on the side",
    "huineng": "An illiterate woodcutter who became the sixth patriarch of Chan",
    "fan-li": "Left on the day it was won, then made and gave away three fortunes",
    "li-ka-shing": "Spends ninety per cent of his time thinking about failure",
    "han-feizi": "Wrote the definitive analysis of court intrigue, then died of one",
    "kasparov": "Lost to Deep Blue in 1997, and a year later invited the computer in",
    "wiener": "Founded cybernetics, then wrote to the union it would displace",
    "excellent-sheep": "Ten years teaching at Yale, on students who can clear any hurdle",
    "maslach": "Made burnout measurable, and says it's the job, not the person",
    "cacioppo": "Brought blood pressure and immune markers to the study of loneliness",
    "harvard-study": "Eighty years of tracking. Relationships, not wealth, predict the end",
    "granovetter": "Showed that jobs arrive through the people you barely see",
    "curie": "Took over her husband's course seven months after he was killed",
    "hochschild": "Named emotional labour, then named the second shift",
    "rat-park": "Changed the cage instead of the rat, and the addiction changed",
    "vygotsky": "Died at 37; left the idea that learning happens just above you",
    "thomas-gordon": "Turned Rogers into something ordinary parents could learn",
    "cs-lewis": "Wrote four notebooks after his wife died, published under a false name",
    "churchill": "Ten years with no office, writing and laying brick, then 1940",
    "perel": "Thirty years of couples work, on the difference between broken and empty",
    "jung": "Freud's heir and his most famous defector, on the second half of life",
    "sapolsky": "Thirty years with wild baboons, on why only people get stress illness",
    "dweck": "Fixed and growth mindset — and the correction she keeps having to make",
    "john-ratey": "Harvard psychiatrist who redefined exercise as a drug for the brain",
    "gottman": "Fifteen minutes of one argument, and he can tell you how it ends",
    "montessori": "One of Italy's first women doctors; changed the room, not the child",
    "boyd": "Never made general, and rewrote how the West thinks about conflict",
}

# 「今日一问」的手写卡片。引用只能落在这一批 30 个条目里。
QQ = [
    ("They said no. Do I raise it a second time?",
     [("boyd", "to-be-or-to-do"), ("churchill", "no-one-listened")], "They said no to my plan"),
    ("It's gone well three times running. Press or bank it?",
     [("li-ka-shing", "knowing-when-to-stop"), ("fan-li", "leave-at-the-top")], "After the win"),
    ("The machine is faster than me now. What's left?",
     [("kasparov", "advanced-chess"), ("wiener", "human-use")], "My craft stopped being worth anything"),
    ("Publicly contradicted. What do I do in the first ten seconds?",
     [("su-shi", "no-wind-no-rain"), ("wang-yangming", "bandits-in-the-heart")], "Anger just took over"),
    ("Same mistake, third time. Whose fault is it?",
     [("han-feizi", "not-counting-on-goodness"), ("wiener", "feedback-not-command")], "The same mistakes keep happening"),
    ("Can I trust this person?",
     [("han-feizi", "form-and-name"), ("fan-li", "leave-at-the-top")], "Can I trust this person"),
    ("Starting from zero. Heavy first move or light?",
     [("li-ka-shing", "ninety-percent-failure"), ("su-shi", "east-slope")], "Starting from nothing"),
    ("Is now the time to walk away?",
     [("fan-li", "leave-at-the-top"), ("li-ka-shing", "knowing-when-to-stop")], "Should I step back"),
    ("Nobody has called in months. What do I do with the time?",
     [("churchill", "wilderness-years"), ("pu-songling", "collecting-at-the-roadside")], "They've put me on the shelf"),
    ("Everything I was supposed to want, and it's empty.",
     [("jung", "afternoon-of-life"), ("zhuangzi", "use-of-uselessness")], "Middle of my life"),
]

# 搜索同义词：读者打的词和条目名对不上时的桥。
SYNONYMS = {
    "burnout": ["maslach", "hochschild", "sapolsky"],
    "exhausted": ["maslach", "sapolsky", "john-ratey"],
    "lonely": ["cacioppo", "harvard-study", "granovetter"],
    "loneliness": ["cacioppo", "harvard-study"],
    "insomnia": ["john-ratey", "sapolsky"],
    "sleep": ["john-ratey", "sapolsky"],
    "anxiety": ["john-ratey", "sapolsky", "wang-yangming"],
    "stress": ["sapolsky", "maslach", "john-ratey"],
    "addiction": ["rat-park", "montessori"],
    "quit": ["rat-park", "fan-li", "li-ka-shing"],
    "grief": ["cs-lewis", "curie"],
    "bereavement": ["cs-lewis", "curie"],
    "divorce": ["gottman", "perel"],
    "marriage": ["gottman", "perel", "harvard-study"],
    "argument": ["gottman", "thomas-gordon"],
    "parenting": ["montessori", "thomas-gordon", "vygotsky"],
    "kids": ["montessori", "thomas-gordon"],
    "teenager": ["thomas-gordon", "montessori"],
    "procrastination": ["wang-yangming", "boyd"],
    "motivation": ["wang-yangming", "dweck", "excellent-sheep"],
    "ai": ["kasparov", "wiener", "excellent-sheep"],
    "automation": ["wiener", "kasparov"],
    "redundancy": ["su-shi", "churchill", "jung"],
    "laid off": ["su-shi", "churchill", "granovetter"],
    "unemployed": ["su-shi", "granovetter", "churchill"],
    "networking": ["granovetter", "harvard-study"],
    "career change": ["fan-li", "boyd", "excellent-sheep"],
    "midlife": ["jung", "churchill"],
    "failure": ["pu-songling", "kasparov", "dweck"],
    "rejection": ["churchill", "boyd", "pu-songling"],
    "promotion": ["boyd", "fan-li", "han-feizi"],
    "management": ["han-feizi", "wiener", "boyd"],
    "team": ["han-feizi", "wiener", "vygotsky"],
    "money": ["fan-li", "li-ka-shing", "hochschild"],
    "investing": ["fan-li", "li-ka-shing"],
    "housework": ["hochschild"],
    "caregiving": ["hochschild", "sapolsky"],
    "learning": ["vygotsky", "dweck", "wang-yangming"],
    "studying": ["vygotsky", "wang-yangming", "excellent-sheep"],
    "purpose": ["zhuangzi", "excellent-sheep", "jung"],
    "meaning": ["zhuangzi", "jung", "huineng"],
    "meditation": ["huineng", "wang-yangming"],
    "overthinking": ["wang-yangming", "huineng", "john-ratey"],
    "jealousy": ["jung", "zhuangzi"],
    "imposter": ["wang-yangming", "excellent-sheep"],
    "moving abroad": ["granovetter", "harvard-study"],
    "immigration": ["granovetter", "harvard-study"],
}


# 分类配色照搬中文那一组，英文名对上中文名 —— 两版的分类是一一对应的，
# 颜色跟着走，读者在两边看到的同一类是同一个色。
CAT_COLOR = {
    "Strategy and competition": "#a33b2e",
    "Power and organisation": "#7d5a3c",
    "Money and risk": "#8a6d2f",
    "Mind and feeling": "#4e6b7a",
    "Learning and growth": "#4a7c6f",
    "Body and daily life": "#7a6a8a",
    "Family and relationships": "#a35f6e",
    "How the world works": "#6b5b73",
}


def payload():
    """生成英文首页的 HWXD 数据块。

    输出**形状**必须和 force_chapter_ui._hwx_payload() 一模一样 ——
    首页那套 JS 是共用的，它读 E / QP / QS / QQ / S / WHO / CC / CT / CTD / NC
    这十个字段。这里只换数据，不改契约。

    中文那份的几处写法在英文上不成立，逐条换掉：
      · apply 里的引导句是 "Where you are: " 不是「局面：」
      · 金句挑选按**词**数不按字数（中文 8-34 字 ≈ 英文 3-14 词）
      · 配第一人称问句用的重合度按词算，不按字符二元组
      · 查重用词四元组
    """
    import json
    import os
    import re
    import sys

    HERE = os.path.dirname(os.path.abspath(__file__))
    ROOT = os.path.dirname(HERE)
    sys.path.insert(0, HERE)
    sys.path.insert(0, os.path.join(ROOT, "seo"))

    from en_entries import ENTRIES
    from hwx_scenes_en import SCENES
    from quote_asks_en import QUOTE_ASKS_EN
    import importlib
    import pkgutil

    # ── 章节 ────────────────────────────────────────────────
    here = os.path.join(ROOT, "seo", "chapters_en")
    CH, line_by, parent_of = [], {}, {}
    for mod in sorted(m.name for m in pkgutil.iter_modules([here])):
        m = importlib.import_module("chapters_en." + mod)
        spec = getattr(m, "PARENT", {}) or {}
        for it in spec.get("items", []):
            line_by[(spec["name"], it["k"])] = it.get("line", "")
        for ch in getattr(m, "CHAPTERS", []) or []:
            c = dict(ch)
            c["parent"] = spec["name"]
            c["slug"] = spec["slug"]
            CH.append(c)
            parent_of[spec["name"]] = spec["slug"]

    strip = lambda t: re.sub(r"==", "", str(t or "")).strip()
    words = lambda t: [w for w in re.sub(r"[^a-z0-9'\s-]", " ", t.lower()).split() if w]

    def best_q(ch):
        qs = [strip(q).rstrip(".") for q in ch.get("q", [])]
        fit = [q for q in qs if 3 <= len(q.split()) <= 14]
        return max(fit, key=len) if fit else (qs[0] if qs else "")

    def scene_of(ch):
        m = re.search(r"Where you are:\s*(.+?)(?:\n|$)", ch.get("apply", ""))
        return m.group(1).strip().rstrip(".") if m else ""

    def gloss_of(ch):
        sc = scene_of(ch)
        if not sc:
            return {"pt": ch.get("w", ""), "when": "", "gl": ""}
        return {"pt": ch.get("w", ""), "when": sc, "gl": "Use it when " + sc[0].lower() + sc[1:] + "."}

    # ── E：条目 ─────────────────────────────────────────────
    ch_by = {}
    for c in CH:
        ch_by.setdefault(c["parent"], []).append((c["k"], c["n"], c.get("w", "")))
    E = []
    for e in ENTRIES:
        chs = ch_by.get(e["n"], [])
        hook = next((line_by.get((e["n"], k), "") for k, _, _ in chs
                     if line_by.get((e["n"], k))), "")
        first_ch = next((c for c in CH if c["parent"] == e["n"]), None)
        body = []
        for c in CH:
            if c["parent"] != e["n"]:
                continue
            body += [c["n"], c.get("w", ""), strip(c.get("story")), strip(c.get("apply"))]
            for f in c.get("f", []):
                body += [f.get("n", ""), f.get("d", "")]
            body += [strip(q) for q in c.get("q", [])]
        syn = " ".join(k for k, v in SYNONYMS.items() if e["slug"] in v)
        E.append({"n": e["n"], "s": e["slug"], "c": e["c"], "w": e["w"],
                  "it": INTROS.get(e["slug"], ""), "hk": hook,
                  "nc": len(chs), "c0": chs[0][1] if chs else "",
                  "cs": [n for _, n, _ in chs[:3]] if len(chs) >= 3 else [],
                  "sc": scene_of(first_ch) if first_ch else "",
                  "pt": first_ch.get("w", "") if first_ch else "",
                  "ix": (" ".join(body)[:1400] + " " + syn).strip()})

    # ── S：处境 ─────────────────────────────────────────────
    ch_index = {(c["slug"], c["k"]): c for c in CH}
    S = []
    for t, grp, questions in SCENES:
        qs = []
        for qtext, refs in questions:
            ans = []
            for s_, k_ in refs:
                assert (s_, k_) in ch_index, "处境引用不存在：%s/%s (%s)" % (s_, k_, t)
                c = ch_index[(s_, k_)]
                ans.append({"who": c["parent"], "cn": c["n"], "u": "/i/%s/%s/" % (s_, k_),
                            "wk": 0,
                            "hint": line_by.get((c["parent"], k_), "") or c.get("w", "")})
            qs.append({"q": qtext, "a": ans})
        S.append({"t": t, "g": grp, "qs": qs})

    # ── QP / QS：金句池 ──────────────────────────────────────
    prim = {}
    for _t, _g, _qs in SCENES:
        for _qt, _refs in _qs:
            if _refs:
                prim.setdefault(_refs[0], []).append(_qt)

    def first_person(ch, g):
        key = "%s/%s" % (ch["slug"], ch["k"])
        if key in QUOTE_ASKS_EN:
            return QUOTE_ASKS_EN[key]
        pool = prim.get((ch["slug"], ch["k"]), [])
        if not pool:
            return ""
        ref = set(words(g["when"] + " " + g["pt"] + " " + ch["n"]))
        n, q = max((len(set(words(x)) & ref), x) for x in pool)
        return q if n >= 2 else ""

    QP = []
    for ch in CH:
        q = best_q(ch)
        if not q:
            continue
        g = gloss_of(ch)
        QP.append({"q": q, "who": ch["parent"], "cn": ch["n"], "pt": g["pt"],
                   "when": g["when"], "gl": g["gl"], "fq": first_person(ch, g),
                   "u": "/i/%s/%s/" % (ch["slug"], ch["k"])})
    QS = [q for q in QP if len(q["q"].split()) <= 10]

    # ── QQ：问题卡（手写 + 处境派生）──────────────────────────
    sc_by_name = {sc["t"]: sc for sc in S}

    def scfields(name):
        sc = sc_by_name[name]
        return {"s": name, "ss": SC_SHORT.get(name, name), "sg": sc["g"],
                "sn": len(sc["qs"]), "bx": SC_BOX[name]}

    apply_sc = {(c["slug"], c["k"]): scene_of(c) for c in CH if scene_of(c)}

    def enrich(ans):
        out = []
        for a in ans:
            b = dict(a)
            b["wk"] = 0
            key = tuple(a["u"].strip("/").split("/")[1:3])
            if not b.get("hint"):
                c = ch_index.get(key)
                if c:
                    b["hint"] = line_by.get((c["parent"], c["k"]), "") or c.get("w", "")
            if apply_sc.get(key):
                b["sc"] = apply_sc[key]
            out.append(b)
        return out

    def ref(slug, k):
        c = ch_index[(slug, k)]
        return {"who": c["parent"], "cn": c["n"], "u": "/i/%s/%s/" % (slug, k)}

    QQ_ALL = ([dict({"t": t, "r": enrich([ref(*r) for r in rs])}, **scfields(sc))
               for t, rs, sc in QQ]
              + [dict({"t": q["q"], "r": enrich(q["a"])}, **scfields(sc["t"]))
                 for sc in S for q in sc["qs"]])

    # 预填句不许复读卡片上的问句 —— 两者在屏幕上相距三厘米。
    # 中文那边按四字片段查，英文按**四个词**查；只在一两个处境里出现过的
    # 才算真回声，出现在三个以上处境的是英语绕不开的连接语。
    def grams4(t, n=4):
        w = words(t)
        return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}

    df = {}
    for sc in S:
        seen = grams4(SC_BOX[sc["t"]])
        for q in sc["qs"]:
            seen |= grams4(q["q"])
        for gm in seen:
            df[gm] = df.get(gm, 0) + 1
    pairs = ([(sc["t"], q["q"]) for sc in S for q in sc["qs"]]
             + [(sc, t) for t, _rs, sc in QQ])
    dup = [(a, b, sorted(g for g in grams4(b) & grams4(SC_BOX[a]) if df.get(g, 0) < 3))
           for a, b in pairs]
    dup = [d for d in dup if d[2]]
    assert not dup, "预填句在复读卡片问句：%s" % (dup[:3],)
    assert set(SC_BOX) == {sc["t"] for sc in S}, "SC_BOX 与处境对不上"

    # ── NC：最新章节 ────────────────────────────────────────
    NC = []
    cat_by = {e["n"]: e["c"] for e in ENTRIES}
    for ch in list(reversed(CH))[:40]:
        NC.append({"pn": ch["parent"], "cn": ch["n"], "w": ch.get("w", ""),
                   "q": best_q(ch), "sc": scene_of(ch), "s": ch["slug"], "k": ch["k"],
                   "u": "/i/%s/%s/" % (ch["slug"], ch["k"]),
                   "c": cat_by.get(ch["parent"], "")})

    WHO = {e["n"]: INTROS[e["slug"]] for e in ENTRIES if e["slug"] in INTROS}

    def tint(hexs, a):
        r, g, b = int(hexs[1:3], 16), int(hexs[3:5], 16), int(hexs[5:7], 16)
        return "rgba(%d,%d,%d,%.3f)" % (r, g, b, a)

    return json.dumps(
        {"E": E, "QP": QP, "QS": QS, "QQ": QQ_ALL, "S": S, "WHO": WHO,
         "CC": CAT_COLOR,
         "CT": {k: tint(v, 0.055) for k, v in CAT_COLOR.items()},
         "CTD": {k: tint(v, 0.16) for k, v in CAT_COLOR.items()},
         "NC": NC},
        ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
