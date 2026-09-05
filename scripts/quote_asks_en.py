# -*- coding: utf-8 -*-
"""English "today's line": chapter → the first-person question it answers.

Same job as quote_asks.py, and the same rule: the value must be a verbatim
question from hwx_scenes_en.SCENES, and that question must actually reference
this chapter. Both are checked by scripts/check_en.py — a typo fails the gate.

Picked one at a time by what the chapter argues, not by which sentence sounds
closest. The Chinese file learned that the expensive way: automatic matching
covered 100% of chapters and was wrong about a third of the time, and a
mis-picked first-person line is fake empathy — worse than none. Every chapter
here had two or three candidates; the one kept is the question this chapter's
line is an answer to.
"""

QUOTE_ASKS_EN = {
    # 要做决定 / 有对手
    "boyd/ooda": "I'm only ever reacting. I never set the tempo.",
    "boyd/to-be-or-to-do": "Am I doing the work, or proving something?",

    # 一个能约的人都没有
    "cacioppo/loneliness-is-a-signal": "Three years here and I have no one to call.",
    "cacioppo/hypervigilance": "I keep feeling like people are avoiding me.",
    "cacioppo/not-more-socializing": "I go to the things. I come home just as alone.",
    "harvard-study/someone-to-count-on":
        "If something happened at 2am I don't know who I'd call.",
    "harvard-study/social-fitness":
        "My friends all have families now and we've run out of things to say.",
    "harvard-study/relationships-predict-health":
        "I gave these years to the work and the friendships went quiet.",
    "granovetter/weak-ties": "I want to meet people and I don't know where to start.",
    "granovetter/no-strong-tie-is-a-bridge":
        "My circle is small and I never hear anything new.",

    # 被晾着 / 说了没人听
    "churchill/wilderness-years": "Nobody asks my opinion anymore.",
    "churchill/no-one-listened": "I said it and not one person took it seriously.",
    "churchill/sixty-five": "Is any of what I built still worth something?",

    # 失去
    "cs-lewis/grief-feels-like-fear": "This doesn't feel like sadness. It feels like fear.",
    "cs-lewis/house-of-cards": "The story I told myself stopped holding my weight.",
    "cs-lewis/not-replacing-her":
        "I'm afraid of forgetting her and afraid what I keep isn't her.",
    "curie/the-lecture": "She's gone. What am I supposed to do tomorrow?",
    "curie/journal-of-grief": "There are things I only ever wanted to tell him.",
    "curie/the-little-curies": "What I'm good at, nobody needs right now.",

    # 学与练
    "dweck/praise-the-process": "How do I push them without breaking them?",
    "dweck/effect-size": "I know exactly what to do. I can't make myself do it.",
    "vygotsky/zpd": "I practice constantly and I'm not getting better.",
    "vygotsky/scaffolding": "Without the tool I can't get the first sentence down.",
    "excellent-sheep/hurdles": "I'm good at all of it and I don't know what I want.",
    "excellent-sheep/no-scoreboard":
        "I lived on scores my whole life and now nobody scores me.",

    # 进退
    "fan-li/stock-the-opposite": "Everything's fine. What should I be getting ready for?",
    "fan-li/leave-at-the-top": "I did too well and now it makes me nervous.",
    "li-ka-shing/ninety-percent-failure": "If this is wrong, is there a way back?",
    "li-ka-shing/knowing-when-to-stop": "I won, and now I don't know when to stop.",

    # 亲密关系
    "gottman/four-horsemen": "We've had this same fight a hundred times.",
    "gottman/repair-attempts": "Once it starts, neither of us can stop it.",
    "perel/security-and-desire": "We've been together years and I feel nothing.",
    "perel/not-a-problem-to-solve":
        "We don't fight and we aren't close. I don't know what this is.",
    "perel/quality-not-frequency":
        "We're together every day and further apart every month.",

    # 规则与人
    "han-feizi/not-counting-on-goodness": "New people, same mistakes.",
    "han-feizi/two-handles":
        "I've tried rewards and I've tried consequences. Neither moved anything.",
    "han-feizi/form-and-name": "He talks well. I've never seen him deliver.",

    # 家里的活
    "hochschild/second-shift": "I'm on my feet all day and I'm told I don't work.",
    "hochschild/emotional-labor": "I finished nothing today and I'm too tired to speak.",
    "thomas-gordon/i-message": "We are not having the same conversation.",
    "thomas-gordon/problem-ownership": "Something's wrong and he isn't telling me.",
    "montessori/prepared-environment":
        "I've said it a hundred times and it still doesn't happen.",
    "montessori/help-me-do-it-myself": "How much am I supposed to step in?",

    # 减法
    "huineng/originally-not-a-thing": "How do I stop running it again?",
    "huineng/in-the-world": "Do I have to leave this life to find the real one?",

    # 身体
    "john-ratey/exercise-for-the-brain": "By the afternoon I'm finished.",
    "john-ratey/move-before-you-think": "The second I lie down my head starts up.",
    "sapolsky/stress-mismatch": "I've been holding this long past what I can hold.",
    "sapolsky/predictability": "The pressure isn't even that bad and I'm never off.",
    "rat-park/rat-park": "I know it's bad for me and I can't stop.",
    "rat-park/vietnam-veterans": "Is my willpower just weak?",
    "rat-park/change-the-cage": "I've quit a dozen times and broken every one.",
    "maslach/three-signs": "It isn't tiredness. There's nothing in there.",
    "maslach/fix-the-job": "I took the vacation. The same job was waiting.",
    "maslach/six-mismatches": "The work is light and I need permission for all of it.",

    # 中年与身份
    "jung/afternoon-of-life": "I have everything I was supposed to want and I'm emptier.",
    "jung/the-shadow": "Some people set me off and I can't say why.",
    "jung/the-persona": "I've been playing a part for years.",

    # AI
    "kasparov/advanced-chess": "The one thing I was best at, it now does better.",
    "kasparov/process-beats-both":
        "I shipped what it gave me without working through it myself.",
    "kasparov/excuses-cost-years": "I keep finding proof that it isn't actually good.",
    "wiener/wrote-to-the-union": "It hasn't reached me yet. What do I do first?",
    "wiener/human-use": "I gave away everything I could and what's left is scraps.",
    "wiener/feedback-not-command": "I explained it and what came back was not it.",

    # 一直没成
    "pu-songling/forty-years-of-failing":
        "I've been at this for years and it has never worked.",
    "pu-songling/the-side-thing":
        "What I pushed on went nowhere. What I did casually took off.",
    "pu-songling/collecting-at-the-roadside":
        "I only have scraps of time and I can't afford to quit.",

    # 苏轼
    "su-shi/no-wind-no-rain": "It hit me and I can't cool down.",
    "su-shi/three-exiles": "I lost. Is there anything here worth keeping?",
    "su-shi/no-bad-people": "He meant it. Do I still let it go?",
    "su-shi/east-slope": "The income stopped. What do I do first?",
    "su-shi/silt-into-a-causeway":
        "I built this for one thing and now it's just sitting there.",

    # 孙子兵法 / 道德经 / 巴菲特 / 芒格
    "sun-tzu/win-before-fighting":
        "It starts on Monday and I'm bracing myself. Is that the problem?",
    "tao-te-ching/reversal":
        "It's going well and I can't shake the feeling it won't last.",
    "buffett/circle-of-competence":
        "Everyone I know is in this. I don't actually understand it.",
    "munger/invert":
        "I keep listing reasons this will work. Should I do the other list?",
    "sun-tzu/know-both":
        "I think I know them well enough. Do I know my own side?",
    "sun-tzu/win-without-fighting":
        "I keep winning these and I'm more tired every time.",
    "sun-tzu/orthodox-and-surprise":
        "My clever move didn't land. Was the idea wrong?",
    "sun-tzu/form-like-water":
        "They set the agenda every week and I just respond.",
    "tao-te-ching/wu-wei":
        "The more rules I add, the more people route around them.",
    "tao-te-ching/water":
        "Everyone is chasing the same thing. Where is nobody standing?",
    "tao-te-ching/usefulness-of-emptiness":
        "Every hour is booked and one delay wrecks the week.",
    "buffett/swimming-naked":
        "The numbers look great. Is that skill or is it leverage?",
    "munger/latticework":
        "I've diagnosed this three times and it's always the same cause.",
    "su-shi/no-more-writing": "The more I explain, the worse it gets.",

    # 王阳明
    "wang-yangming/unity-of-knowing-and-doing":
        "I understand it completely and still don't move.",
    "wang-yangming/polish-on-things": "It all makes sense until I have to do it.",
    "wang-yangming/innate-knowing": "Can I trust what my gut is telling me this time?",
    "wang-yangming/bandits-in-the-heart": "The fight I'm afraid of is inside me.",

    # 庄子
    "zhuangzi/use-of-uselessness": "The more useful the task, the sooner it got taken.",
    "zhuangzi/ox-carving": "The same task costs me more than it costs everyone else.",
    "zhuangzi/equalizing-things": "He's a step ahead of me on everything.",
}
