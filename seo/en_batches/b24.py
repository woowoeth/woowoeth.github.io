# -*- coding: utf-8 -*-
"""每日一条，第 4 天：阿尔伯特·赫希曼。

按扇出选。中文最空的处境之一是「要不要跳槽」（6 篇）——那里挂着博伊德、
张一鸣、纳瓦尔、巴菲特、凯文·凯利，五条都在帮你判断「走对自己好不好」，
没有一条说得出**走和留之外还有第三个选项，而它总是先死**。

英文这边同样空：Should I leave this job 只有 2 篇，They said no to my plan
只有 3 篇。两章分别落在这两个处境上，另加 Only good news reaches me
（3 篇，领导视角的同一件事：肯提意见的人早就走了）。三个都是已有处境，
不新开，所以没有 SC_BOX。

术语全部用他自己的英文：exit / voice / loyalty、the lazy monopolist，
以及 1991 年那本书副标题里的 perversity, futility, jeopardy。
条目金句里那句 "Creativity always comes as a surprise to us" 出自
《Development Projects Observed》(1967) 讲「隐藏之手」的那一节。
其余金句是本站自己的话，不假托成引语——他在 EVL 里给 voice 下的那句定义
我记得住意思、记不准词序，照 HOWTO 那条就没放。

三个 story 互不重叠：条目用 1940 年马赛，第一章用尼日利亚铁路，
第二章用两百年三波扩权。
"""

ENTRIES = [
    {
        "c": "Power and organisation", "n": "Albert O. Hirschman",
        "slug": "hirschman", "e": "United States · 1915-2012",
        "w": "Voice", "y": 1915,
        "d": "A German-born American economist. He left Berlin in 1933, "
             "fought in Spain in 1936, spent 1940 in Marseille forging "
             "papers and finding mountain routes for refugees, went to "
             "Colombia as an economic adviser in 1952, and ended at the "
             "Institute for Advanced Study in Princeton. One thing annoyed "
             "him for a lifetime: reducing a tangled situation to a tidy "
             "law. Exit, Voice, and Loyalty (1970) is the famous one. Faced "
             "with something getting worse, people can do two things — walk "
             "out, or speak up. Economics studies only the first, while the "
             "second is what most people are actually doing, and the "
             "easiest for an institution to lose without noticing. The "
             "Rhetoric of Reaction (1991) does something else: rather than "
             "argue with what objectors say, it counts the shapes their "
             "sentences take, and finds three. He called himself a "
             "possibilist — not predicting what must happen, only insisting "
             "that things have more room in them than a theory allows.",
        "story":
            "Marseille, summer 1940. Hirschman is twenty-five, working out "
            "of hotel rooms on forged papers, mountain routes and "
            "black-market francs. Varian Fry, an American, has arrived in "
            "France with a rescue list; Hirschman is the one who runs the "
            "errands, scouts the passes and changes the money, and Fry "
            "gives him the code name Beamish. Hannah Arendt and Marc "
            "Chagall got out along that line. By the end of the year he "
            "crossed the Pyrenees himself and reached the United States by "
            "way of Spain and Portugal. Thirty years later, when he wrote "
            "down the word exit, he knew what it weighed.",
        "f": [
            {"n": "Dissatisfaction has two ways out",
             "d": "Something is getting worse and you can do one of two "
                  "things. Exit: switch, resign, stop buying. Voice: stay "
                  "and say what is wrong. Economics studies the first, "
                  "politics the second, and you meet both in one week.",
             "eg": "The food got worse. You can find another place, or call "
                   "the owner over. Most people quietly find another place."},
            {"n": "The easier the exit, the fewer the complaints",
             "d": "The two doors compete for the same people, and the first "
                  "to leave are the fussiest. Once they are gone nobody "
                  "left behind complains, and the thing declining has lost "
                  "its one signal that it is declining.",
             "eg": "Your most demanding customers stop renewing and stop "
                   "complaining. On the report it is a few missing names."},
            {"n": "Loyalty buys the time voice needs",
             "d": "Loyalty is not obedience. It raises the cost of leaving "
                  "so you stay while there is still time to change "
                  "something. Where you cannot leave and nobody listens, "
                  "what is left is not loyalty but capture.",
             "eg": "Whoever has been there eight years is least willing to "
                   "go and most likely to speak, if speaking is taken "
                   "seriously."},
            {"n": "A no comes in three shapes",
             "d": "The Rhetoric of Reaction counts them: perversity, your "
                  "remedy will worsen the very thing; futility, nothing "
                  "will shift either way; jeopardy, the cost is something "
                  "we already hold. The first two contradict each other and "
                  "one mouth says both.",
             "eg": "When a plan is refused, name the shape first, then ask "
                   "how much. Two of the three stop there."},
            {"n": "The hiding hand",
             "d": "Watching development projects in 1967 he saw two errors "
                  "cancelling: people underrate the difficulties and "
                  "equally underrate the solutions they will later invent. "
                  "Not seeing how hard it was is what let the thing get "
                  "started at all.",
             "eg": "The job you had no idea would be that hard is the one "
                   "you finished. The one whose costs you knew fully has "
                   "not begun."},
        ],
        "apply":
            "Take something you are weighing up as stay or go and put the "
            "leaving sum aside. Write three lines: the one time you "
            "genuinely raised it, who you raised it with, and what came "
            "back. If any line is blank, the choice in front of you is not "
            "exit against voice, it is exit against putting up with it. "
            "Then add a fourth line — if I said it tomorrow, what is the "
            "worst that happens — and make it concrete. Written out, it is "
            "usually smaller than it was in your head.",
        "q": [
            "The easier a place is to leave, the less anyone says.",
            "The first to go are the ones who would have complained.",
            "The case against a change comes back in only three shapes.",
            "Creativity always comes as a surprise to us.",
        ],
        "l": ["Hannah Arendt", "Andy Grove", "Peter Drucker",
              "Thinking in Systems", "The Old Regime and the Revolution"],
        "contrast": [
            {"n": "Friedrich Hayek",
             "why": "Hayek argues a reform endangers a freedom we already "
                    "hold, which is the third shape Hirschman names; "
                    "Hirschman does not dispute it, he asks for a quantity "
                    "someone can check"},
            {"n": "Andy Grove",
             "why": "Both ask how bad news travels upward: Grove wants the "
                    "people sounding alarms brought into the room, "
                    "Hirschman asks whether they resigned some time ago"},
        ],
    },
]

INTROS = {
    "hirschman": "Economist who named exit and voice; spent 1940 running an "
                 "escape route over the Pyrenees",
}

SCENES = [
    ("Should I leave this job", "Dealing with people", [
        ("I'm unhappy here and leaving is the only move I can picture.",
         [("hirschman", "exit-voice-loyalty")]),
    ]),
    ("Only good news reaches me", "Leading people", [
        ("The people who used to push back have all left.",
         [("hirschman", "exit-voice-loyalty")]),
    ]),
    ("They said no to my plan", "Making a call", [
        ("The no came back. I can't tell what shape it was.",
         [("hirschman", "rhetoric-of-reaction")]),
        ("They told me it would only make things worse.",
         [("hirschman", "rhetoric-of-reaction")]),
    ]),
]

ASKS = {
    "hirschman/exit-voice-loyalty":
        "I'm unhappy here and leaving is the only move I can picture.",
    "hirschman/rhetoric-of-reaction":
        "The no came back. I can't tell what shape it was.",
}
