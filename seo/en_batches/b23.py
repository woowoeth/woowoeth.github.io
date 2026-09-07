# -*- coding: utf-8 -*-
"""每日一条，第 3 天：尼尔·波斯曼。

按扇出选。最空的处境是中文站的「日子被工具占满」（5 篇）——那里挂着伊里奇、
卡尔·纽波特、《有限与无限的游戏》，三条都在教你怎么把这笔账算清，
没有一条说得出**为什么算清了也不管用**：省下的时间当场被抬高的标准收走，
因为工具不是被加进你的日子里，它换掉了整个日子。波斯曼补的正是这一句。

英文站没有对应的处境（英文的 AI arrived 只有 7 个），所以两章挂到英文这边
同样空的两个已有处境上：More output, emptier（3 篇）和 Do I jump in now（3 篇），
不新开处境。

引语全部还原英文原句，不从中文回译：1998 年那篇演讲的第一条（trade-off）、
第二条（distributed evenly）、第四条（not additive; it is ecological）、
第五条（mythic），以及《Technopoly》第一章那句 one-sided effect。
第二章原本想引「a Faustian bargain」整句，记不准全句的词序，就只留
确定的那半句，把「Faustian bargain」放进正文按他的说法交代——
HOWTO 那条「想不起是哪一章哪一页就换一句」在这里真的用上了一次。

三个 story 互不重叠：条目用塔姆斯的判词，第一章用印刷机，第二章用机械钟。
"""

ENTRIES = [
    {
        "c": "How the world works", "n": "Neil Postman", "slug": "postman",
        "e": "United States · 1931-2003", "w": "Cost", "y": 1931,
        "d": "An American media critic who taught at New York University; "
             "Amusing Ourselves to Death (1985) and Technopoly (1992) are "
             "the two hard ones. He spent a career against a single idea — "
             "that a technology is a neutral instrument, take it or leave "
             "it, good or bad depending on use. His counter is that every "
             "technology is a bargain: it hands you one thing while taking "
             "another, and the giving and the taking do not land on the "
             "same people. Nor does it simply get added to the world; it "
             "rearranges the world. He is not asking anyone to smash "
             "anything. He is asking for both columns to be filled in "
             "before signing: whose problem does this solve, and who "
             "carries the cost.",
        "story":
            "Technopoly opens with a story Plato recorded. The Egyptian god "
            "Theuth brings writing to King Thamus and calls it a remedy for "
            "memory. Thamus does not thank him. He answers first that an "
            "inventor is fond of his own invention and is therefore not the "
            "right judge of it, and then that writing will make people lean "
            "on marks outside themselves instead of recalling from within: "
            "what you have found is not a remedy for memory but for "
            "reminding. Postman then turns on Thamus too. Thamus is right "
            "about only half of it, seeing what writing takes and not what "
            "it gives; the enthusiast makes the opposite mistake and sees "
            "only the gift. Postman wants both eyes open.",
        "f": [
            {"n": "The Faustian bargain",
             "d": "Technology is never free: it hands you one thing and "
                  "takes another, and no receipt is issued for the thing "
                  "taken. So is it any good has no answer. Ask what it "
                  "gives and what it cancels.",
             "eg": "The spell checker saved you the dictionary and took your "
                   "certainty about the word. You can no longer spell it."},
            {"n": "The winners and the payers are different people",
             "d": "Advantages and costs are never spread evenly. A "
                  "technology is pure gain for one group and pure loss for "
                  "another, and the group deciding to adopt it is usually "
                  "the one gaining.",
             "eg": "Typesetting software saved the publisher a whole "
                   "hot-metal floor, and none of it went to the "
                   "compositors."},
            {"n": "Not additive, ecological",
             "d": "People expect addition: the day carries on, one chore "
                  "gets cheaper. What happens is ecological — Europe after "
                  "the printing press was not the old Europe with a machine "
                  "in it, it was a different Europe.",
             "eg": "The shared document saved you the attachments. What "
                   "changed is that progress is visible at all times, so no "
                   "stretch of work is unwatched."},
            {"n": "Used long enough, it stops looking like technology",
             "d": "His fifth point: once something has been around long "
                  "enough it is taken as the way things are rather than as "
                  "an invention, and nobody asks who installed it or why.",
             "eg": "Nobody asks in the meeting why this is measured in "
                   "hours. The clock stopped looking like an invention."},
            {"n": "Its makers are not the right judges",
             "d": "An inventor is fond of his invention and sees what it "
                  "can do rather than what it removes. The case for and "
                  "against a tool should not rest on the people who know it "
                  "best.",
             "eg": "What a system really costs is described best by whoever "
                   "is blocked by it daily and cannot change it."},
        ],
        "apply":
            "Take one tool you have adopted in the last six months and make "
            "a two-column table. On the left, what it actually gave you, in "
            "hours or in units shipped. On the right, what it cancelled: "
            "one thing you used to do and no longer do, and one feel for "
            "the work you used to have and no longer have. Then ask who is "
            "pure gain here, who is pure loss, which side you are on, and "
            "what you would still be able to do if it disappeared tomorrow.",
        "q": [
            "All technological change is a trade-off.",
            "The advantages and disadvantages of new technologies are never "
            "distributed evenly among the population.",
            "A new medium does not add something; it changes everything.",
            "Media tend to become mythic.",
            "It is a mistake to suppose that any technological innovation "
            "has a one-sided effect.",
        ],
        "l": ["Ivan Illich", "Cal Newport", "Norbert Wiener", "Kevin Kelly",
              "Finite and Infinite Games"],
        "contrast": [
            {"n": "Kevin Kelly",
             "why": "Both watch where a technology is heading over decades: "
                    "one asks what it wants to become, the other asks whose "
                    "place it moved when it sat down"},
            {"n": "Ivan Illich",
             "why": "Both keep a ledger on tools: one counts the hours you "
                    "pay to keep it, the other counts how far it raised the "
                    "line for what counts as enough"},
        ],
    },
]

INTROS = {
    "postman": "Wrote Amusing Ourselves to Death; held that every technology is a bargain you sign",
}

SCENES = [
    ("More output, emptier", "AI arrived", [
        ("I added one tool and the whole day changed shape.",
         [("postman", "ecological-change")]),
        ("It saved my time. I can't say whose it spent.",
         [("postman", "faustian-bargain")]),
    ]),
    ("Do I jump in now", "AI arrived", [
        ("Everyone is adopting this. Do I have to as well?",
         [("postman", "faustian-bargain")]),
        ("If I take this on, what am I giving up?",
         [("postman", "ecological-change")]),
    ]),
]

ASKS = {
    "postman/ecological-change":
        "I added one tool and the whole day changed shape.",
    "postman/faustian-bargain":
        "It saved my time. I can't say whose it spent.",
}
