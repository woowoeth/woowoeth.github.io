# -*- coding: utf-8 -*-
"""Daily entry, day 18: Feng Yi.

Picked by fan-out. 'Someone took the credit', 'They've started watching me'
and 'They said no to my plan' were among the emptiest situations on the
Chinese side. On credit, what hangs there says either make your work seen
(Gracian) or ask for less (Zhang Liang). Feng Yi is a third answer: stay out
of the argument, and file a report that gives the sequence of events and
nothing about yourself, so the people who worked with you and the person
above you have something to hold up. On suspicion, Wang Jian made himself
look small; Feng Yi answered in writing, in the open, and Liu Xiu, as the
boss, sent him the accusation itself. On a rejected plan, nothing said what
to do once the other plan has failed: help first, gather the stragglers,
keep the argument for the review.

All quoted lines are our own renderings of the Chinese in the History of the
Later Han, checked against the Wikisource text.

Four stories, no overlap: the entry is the bean porridge on the flight from
Wang Lang; the chapters are the tree, the King of Xianyang memorial and the
defeat at Huixi.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Reading people",
        "n": "Feng Yi",
        "slug": "feng-yi",
        "e": "Eastern Han · died 34 CE",
        "w": "Not boasting", "y": 27,
        "d": "A founding general of the Eastern Han, from Fucheng in "
             "Yingchuan, who read the Zuo Commentary and Sun Tzu. He first "
             "held a town for Wang Mang, then joined Liu Xiu as his "
             "secretary and followed him through the northern campaigns. Sent "
             "west in 26 CE, he broke the Red Eyebrows the next year, "
             "pacified the region around the old capital and rose to General "
             "Who Conquers the West. He died in camp in 34. What he left is a "
             "way of standing with a boss and with colleagues: out of the "
             "credit argument, plain in his reports, open under suspicion.",
        "story":
            "When Wang Lang rose in the north, Liu Xiu fled south-east from "
            "Ji, riding day and night and sleeping in sheds. At Wulou "
            "pavilion it was bitterly cold and everyone was starving, and "
            "Feng Yi brought him a bowl of bean porridge. Next morning Liu "
            "Xiu told his generals that the porridge had cured both hunger "
            "and cold. Years later, when Feng Yi came to court, the emperor "
            "loaded him with gifts, and the edict said: the bean porridge at "
            "Wulou and the barley rice by the Hutuo river, a kindness long "
            "unrepaid.",
        "f": [
            {"n": "When they argue merit, stand under the tree",
             "d": "Whenever the army camped, the generals sat down to argue "
                  "over merit and Feng Yi went to stand under a tree. When "
                  "the troops were reassigned, the soldiers all asked for "
                  "the big-tree general. He was absent from the argument; "
                  "the men who had fought with him kept the record.",
             "eg": "A colleague claims the project in the meeting. Let it go "
                   "there, and watch who asks to work with you next."},
            {"n": "Report what happened, not what you deserve",
             "d": "After his victory at Xunyi he wrote only the course of the "
                  "battle and did not presume to boast. When other generals "
                  "wanted a share, Liu Xiu wrote to them himself on Feng "
                  "Yi's behalf. A plain report gave his defender something "
                  "to hold up.",
             "eg": "Write what broke, on which day, and who decided what. "
                   "That is harder to take from you than 'I led the team'."},
            {"n": "Under suspicion, answer in the open",
             "d": "Accused of ruling the west like a king, he was shown the "
                  "memorial and replied formally, with no back-channel "
                  "lobbying. He had already asked to come home, saying he "
                  "felt uneasy holding so much for so long.",
             "eg": "Someone told your boss you act alone. Write one email "
                   "explaining how those decisions were made."},
            {"n": "Overruled and beaten, still clean up",
             "d": "Two commanders ignored his plan and were routed. He went "
                  "to their rescue, walked back to camp after the defeat, "
                  "gathered the stragglers and won the next battle with an "
                  "ambush. The emperor wrote: lost at sunrise, recovered at "
                  "sunset.",
             "eg": "The release you argued against failed. Help fix it now; "
                   "keep your objection for the review."},
        ],
        "apply":
            "If you're somewhere everyone scrambles for credit, don't start "
            "shouting for your share, and don't go silent either. Write down "
            "what you did as a sequence of events: which day, what problem, "
            "who decided, what happened. Hand it in without adjectives, then "
            "notice who wants to work with you when the next job is shared "
            "out. If someone is making a case against you behind your back, "
            "don't send friends to find out what was said; put your answer "
            "where everyone can see it. And if a plan you argued against has "
            "failed, help clean up first and keep your reasoning for the "
            "review.",
        "q": [
            "The generals sat down to argue merit. Feng Yi stood under a tree.",
            "Lost at sunrise, recovered at sunset.",
            "What is there to suspect? Why the fear?",
            "Let the state not forget the troubles north of the river.",
        ],
        "l": ["Zhang Liang", "Wang Jian", "Guo Ziyi", "Han Xin"],
        "contrast": [
            {"n": "Zhang Liang",
             "why": "Both stepped back from reward. Zhang Liang turned down "
                    "thirty thousand households and asked for one small "
                    "county, stepping back from the ruler's gift. Feng Yi "
                    "kept his rewards and simply stayed out of the argument "
                    "about merit, filing plain reports and letting the "
                    "soldiers and the emperor keep the account."},
            {"n": "Wang Jian",
             "why": "Both commanded huge armies far from court and knew they "
                    "would be suspected. Wang Jian sent back again and again "
                    "asking for land and houses, playing a man who wanted "
                    "only property. Feng Yi didn't act a part. He wrote that "
                    "he felt uneasy and asked to come home, and when accused "
                    "he answered formally: one made himself look small, the "
                    "other put everything on the table."},
        ],
    },
]

INTROS = {
    "feng-yi":
        "A founding general of the Eastern Han who walked off to stand under "
        "a tree while the others argued over merit - he never fought for "
        "credit and kept it anyway, and met suspicion and defeat the same way",
}

SCENES = [
    ("Nobody is looking at my work", "Getting it done", [
        ("Everyone's scrambling for credit and I don't want to join in.",
         [("feng-yi", "big-tree")]),
    ]),
    ("They've started watching me", "Dealing with people", [
        ("Someone has been complaining about me upstairs. How do I answer?",
         [("feng-yi", "why-the-fear")]),
    ]),
    ("Can I trust this person", "Dealing with people", [
        ("I've heard a complaint about him. Do I tell him?",
         [("feng-yi", "why-the-fear")]),
    ]),
    ("They said no to my plan", "Making a call", [
        ("They overruled me and it went wrong. Do I still help?",
         [("feng-yi", "lost-at-dawn")]),
    ]),
]

ASKS = {
    "feng-yi/big-tree":
        "Everyone's scrambling for credit and I don't want to join in.",
    "feng-yi/why-the-fear":
        "Someone has been complaining about me upstairs. How do I answer?",
    "feng-yi/lost-at-dawn":
        "They overruled me and it went wrong. Do I still help?",
}
