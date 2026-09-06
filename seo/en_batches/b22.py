# -*- coding: utf-8 -*-
"""每日一条，第 2 天：西蒙娜·薇依。

按扇出选，不按名气。最空的处境仍然是「出得多了人却空了」（English:
More output, emptier）—— 那里挂着伊里奇、德鲁克、庄子、契克森米哈赖，
四条说的都是「你做错了事」，没有一条说得出**人为什么会空**。
薇依补的正是这一句：你空，是因为这些活儿从头到尾没有一处需要你的注意。

另外两章分别挂到「工具替我想了」和「赢了之后」，都不新开处境。

条目 story 用的是 1936 年西班牙那一段（贝尔纳诺斯信），三章的 story
分别是几何题、工厂第一年、《伊利亚特》，四个场景互不重叠。

引语全部是通行英译（Craufurd 译学校学习那篇，McCarthy 译《伊利亚特》一文），
不从中文回译；McCarthy 的原文写作 center 而非 centre，照引不改。
"""

ENTRIES = [
    {
        "c": "Mind and feeling", "n": "Simone Weil", "slug": "weil",
        "e": "France · 1909-1943", "w": "Attention", "y": 1909,
        "d": "A French philosopher who qualified to teach philosophy at "
             "twenty-two and then spent a decade putting herself inside the "
             "situations she wanted to understand: a year as a factory hand, "
             "a spell at the front in Spain, a grape harvest in the south. "
             "She had one subject, attention. Attention is not straining, "
             "she said; it is emptying yourself until the thing can enter — "
             "which is the whole of learning and the rarest thing one person "
             "can give another. She then turned the same measure on how "
             "people get destroyed: work that never needs you to think, and "
             "force that turns a person into a thing, both take the same "
             "faculty away. She died in England in 1943, aged thirty-four.",
        "story":
            "In 1936 she went to the front in the Spanish Civil War and "
            "joined an anarchist column. She was severely short-sighted and "
            "barely a soldier; the story is that she fired once, at an "
            "aircraft. What struck her was not the fighting. Two years "
            "later she wrote to the novelist Georges Bernanos describing "
            "the atmosphere she had found: one in which killing had become "
            "something nobody needed to justify — a captured fifteen-year-"
            "old who would not change sides was shot — and in which nobody "
            "present was a bad man. She left because she stepped into a pan "
            "of boiling oil while cooking and was badly burned. Spain did "
            "not change which side she was on. It changed her test, from "
            "which side is right to what has force made of the people here.",
        "f": [
            {"n": "Attention is emptying, not straining",
             "d": "Told to concentrate, people clench, as if closing a hand "
                  "around something. She says that is muscular effort and "
                  "the opposite of attention, which asks you to admit you do "
                  "not yet understand and stay there so the thing can enter.",
             "eg": "Handed a report you cannot read, the first move is to "
                   "fit a familiar model over it. From then on the report "
                   "cannot say anything of its own."},
            {"n": "The time that produced nothing was not wasted",
             "d": "Effort that fails still grows something, provided the "
                  "attention holds and you do not run. What grows is next "
                  "time's discrimination. Only leaving actually voids the "
                  "hour, which is why she thought the subject studied barely "
                  "mattered.",
             "eg": "You shipped nothing in the two hours you were stuck, and "
                   "you will see faster where the next one is jammed."},
            {"n": "She went and worked in the factories",
             "d": "In 1934 she took leave, hired on under her own name at "
                  "piece rates and lived on the wages. What shook her was "
                  "not exhaustion but finding she had stopped being able to "
                  "think: the machine set the pace, the method came with the "
                  "job, and no thought of hers could get in.",
             "eg": "To learn how bad a process is, run it end to end "
                   "yourself and forbid yourself from asking anyone inside "
                   "for a shortcut."},
            {"n": "What gets removed is judgement, not strength",
             "d": "Judgement unused decays, and past a point people being "
                  "ground down stop protesting and concede the fault is "
                  "their own. So the damage is invisible from outside: the "
                  "room is quiet, and the quiet is the evidence it has "
                  "finished.",
             "eg": "Nobody objecting in the meeting rarely means nobody "
                   "objects. It means they no longer believe objecting "
                   "counts."},
            {"n": "Force turns both sides into things",
             "d": "Reading the Iliad she said its true subject is force. "
                  "The struck side becomes a thing first, but the side "
                  "holding it changes too: the winner takes force for a "
                  "property of himself and can no longer picture the day it "
                  "comes round to him.",
             "eg": "The party with all the leverage signs the contract the "
                   "other side cannot perform, having stopped assuming the "
                   "relationship continues next year."},
        ],
        "apply":
            "Take twenty minutes today on something you cannot yet do, and "
            "forbid yourself from reaching for a ready-made framework "
            "partway through. When the timer stops, ask two things: did I "
            "run? Can I now say exactly which step it is jammed at? If you "
            "can, the twenty minutes were not wasted, whatever you produced. "
            "Then turn the same measure on your work: which step of today "
            "was waiting on your judgement?",
        "q": [
            "What you call concentrating is straining. Attention is "
            "emptying yourself.",
            "The half hour you failed to solve it is where learning "
            "happened.",
            "Attention is the rarest and purest form of generosity.",
            "What empties you is not fatigue. It is work that needs no "
            "thought.",
            "The winner loses not his conscience but his idea of tomorrow.",
        ],
        "l": ["Hannah Arendt", "Ivan Illich", "Cal Newport", "Viktor Frankl",
              "Mihaly Csikszentmihalyi"],
        "contrast": [
            {"n": "Naval Ravikant",
             "why": "Both ask where a person should put themselves: one "
                    "wants leverage that works without you present, the "
                    "other says being present is the one thing you cannot "
                    "outsource"},
            {"n": "Taiichi Ohno",
             "why": "Both stared at the same assembly line: one rebuilt it "
                    "so the worker's thinking is required, the other "
                    "recorded what the line that needs no thinking does to "
                    "a person"},
        ],
    },
]

INTROS = {
    "weil": "A philosopher who took a year off teaching to work the factory floor",
}

SCENES = [
    ("More output, emptier", "AI arrived", [
        ("My day was full and I can't name one thing that stayed with me.",
         [("weil", "attention-is-emptying")]),
    ]),
    ("Nothing I study stays", "How you're doing", [
        ("I stared at the page for an hour and none of it went in.",
         [("weil", "attention-is-emptying")]),
    ]),
    ("The tool does my thinking", "AI arrived", [
        ("The work arrives already decided. I just carry it out.",
         [("weil", "the-factory-year")]),
    ]),
    ("Too busy to have a life", "How you're doing", [
        ("I work at it every day and it stopped feeling like me doing it.",
         [("weil", "the-factory-year")]),
    ]),
    ("After the win", "Facing an opponent", [
        ("I won, and I don't much recognise the person who won.",
         [("weil", "force-makes-things")]),
    ]),
    ("It's my call and they don't get a say", "Leading people", [
        ("I have the power to decide this and I can't bring myself to use it.",
         [("weil", "force-makes-things")]),
    ]),
]

ASKS = {
    "weil/attention-is-emptying":
        "My day was full and I can't name one thing that stayed with me.",
    "weil/the-factory-year":
        "I work at it every day and it stopped feeling like me doing it.",
    "weil/force-makes-things":
        "I won, and I don't much recognise the person who won.",
}
