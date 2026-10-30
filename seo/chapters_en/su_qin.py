# -*- coding: utf-8 -*-
"""Su Qin — English.

English readers who know the name at all know a footnote about the Warring
States and a bit of strategy-book rhetoric. This page takes two moments from
his biography in Sima Qian's Records of the Grand Historian: the year after ten
failed pitches to the King of Qin, and the turn to a different buyer.

The Records and the Mawangdui silk manuscripts (Zhanguo zongheng jia shu) disagree
about when Su Qin lived and what he did. This page follows the Records and does
not pretend the question is settled. No classical line is quoted; everything is
paraphrase.
"""

PARENT = {
    "name": "Su Qin",
    "slug": "su-qin",
    "blurb": "Deep read",
    "items": [
        {"k": "ten-pitches", "n": "Ten Refusals, Then Back to the Books",
         "w": "After a refusal, blame once, then fix one thing",
         "ready": True,
         "line": "Ten pitches failed, nobody at home would speak to him, and that night he opened the books and gave himself a year"},
        {"k": "wrong-buyer", "n": "Qin Won't Buy, Try Yan",
         "w": "After a refusal, ask whether they lack the need",
         "ready": True,
         "line": "The strongest state wanted to swallow others, so he went to the one most afraid of being swallowed"},
    ],
}

CHAPTERS = [
    {
        "k": "ten-pitches", "n": "Ten Refusals, Then Back to the Books",
        "w": "After a refusal, blame once, then fix one thing",
        "src": "Sima Qian, Records of the Grand Historian, 'Biography of Su Qin'; Strategies of the Warring States, Qin 1",
        "dek": "Ten pitches, ten refusals. This asks what to do next: blame the buyer, hide, or go back and fix one thing.",
        "story":
            "According to the Records, Su Qin wrote to the King of Qin ten "
            "times and was never taken up. His sable coat wore through and "
            "his hundred catties of gold ran out, and he went home. His wife "
            "would not leave her loom, his sister-in-law would not cook for "
            "him, and his parents would not speak to him. He sighed that it "
            "was all Qin's fault, and that night he dragged out a chest of "
            "books and, when he grew sleepy, stabbed his thigh with an awl. "
            "==A year later he said he was ready to persuade the rulers of "
            "his day.==",
        "f": [
            {"n": "Blaming once is normal",
             "d": "His first reaction was to blame someone else: his family had turned on him, and Qin was to blame. But that same night he opened the chest. Blame once if you must; after it you need a next step, or all you keep is the grievance.",
             "eg": "Ten applications and no replies. Curse the market for one evening, then look at your portfolio and find the page least like what they asked for."},
            {"n": "Fix the part that faces a person",
             "d": "He read a treatise on strategy, and what he practised was working out what one particular ruler wanted and feared, and how he himself should speak to that. The books were material. The skill was opening his mouth.",
             "eg": "Someone who cannot land work may not lack a certificate. They may lack one sentence that lets the client see what they would solve."},
            {"n": "Give the retreat an end date",
             "d": "He gave himself a year, and went out again at the end of it. A deadline keeps the fixing specific. Without one, going back to the books drifts into hiding.",
             "eg": "Give yourself two months to improve one thing, then take it and knock on a door."},
        ],
        "apply":
            "Where you are: you have tried many times, nothing has landed, and the people around you have started to doubt you.\n"
            "Ask first: what did they turn down, me or the one thing I put in front of them? If I fix one thing, what do I bring next time?\n"
            "Where it goes wrong: reading it as fail, then shut the door and study. He shut it for a year in order to come out again. Studying until you dare not try again is hiding.",
        "q": [
            "Blame once, then go back and fix one thing.",
            "Fix what lets someone grasp you in one line.",
            "A retreat needs an end date. The door opens again.",
        ],
    },
    {
        "k": "wrong-buyer", "n": "Qin Won't Buy, Try Yan",
        "w": "After a refusal, ask whether they lack the need",
        "src": "Sima Qian, Records of the Grand Historian, 'Biography of Su Qin' (the audience with the Marquis of Yan); Strategies of the Warring States, Qin 1",
        "dek": "The King of Qin did not want his plan. This asks whether to change the plan or change who hears it.",
        "story":
            "To the King of Qin, Su Qin had proposed how to swallow the other "
            "states and rule an empire. The king answered that a bird whose "
            "feathers are not full cannot fly high. Qin had just put Shang Yang "
            "to death and had no love for talkers. Su Qin turned to Yan and "
            "waited more than a year for an audience. Then he changed his "
            "pitch: Yan had been spared invasion only because Zhao shielded "
            "it to the south, so it should ally with Zhao. ==The Marquis of Yan "
            "gave him carriages and silks and sent him on to Zhao.==",
        "f": [
            {"n": "The strongest may need you least",
             "d": "Qin was strong and busy swallowing others. It wanted to do it faster and had no time for an alliance. Yan sat between great powers and feared being swallowed, so a plan for staying safe found a ready ear.",
             "eg": "You pitch a management tool to a big company and they say they already have one. You pitch it to a team of a dozen and the owner asks the price on the spot."},
            {"n": "Keep the skill, change where you start",
             "d": "To Qin he spoke of swallowing, to Yan of not being swallowed. He did not change what he could do. He changed the direction of the plan and his first sentence.",
             "eg": "The same quote: lead with delivery time for the client who is in a hurry, and with price for the one on a tight budget."},
            {"n": "The right person is worth a wait",
             "d": "The Marquis of Yan did not see him on the first day. Su Qin waited over a year for a place in the queue, and one meeting settled it. Finding the right person can take time. With the wrong one, a year of waiting is wasted.",
             "eg": "The right client may need a quarter to fit you in. That is cheaper than ten meetings with the wrong one."},
        ],
        "apply":
            "Where you are: you keep making your case and the person across the table does not want it.\n"
            "Ask first: do they refuse because my work is weak, or because they do not lack this and do not fear it? Who has the very problem I can solve?\n"
            "Where it goes wrong: reading it as one refusal means switch targets. In Qin he pitched ten times. Switch when the person truly has no need, not because they said no today.",
        "q": [
            "The biggest player is often the one that needs you least.",
            "Keep the skill; find someone who fears this problem.",
            "Wait a year for the right person, not a day for the wrong one.",
        ],
    },
]
