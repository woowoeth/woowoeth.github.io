# -*- coding: utf-8 -*-
"""Wu Zetian — English.

In English she is almost always the only empress, and the page about her is
almost always about how she got there. These two chapters are about what she
did once she had it: a hiring machine with the exit built in, and a habit of
reading the most hostile text in front of her for its content before its
side. Both are borrowed from historians who disliked her and said so.
"""

PARENT = {
    "name": "Wu Zetian",
    "slug": "wu-zetian",
    "blurb": "Deep read",
    "items": [
        {"k": "promote-and-drop", "n": "Promote out of turn, drop just as fast",
         "w": "Fast in, and fast out", "ready": True,
         "line": "Daring to promote wildly rests on daring to remove "
                 "immediately"},
        {"k": "the-manifesto", "n": "How did the chancellor lose this man",
         "w": "Recruiting from the pamphlet attacking you", "ready": True,
         "line": "Judge the writing first, then deal with whose side it is on"},
    ],
}

CHAPTERS = [
    {
        "k": "promote-and-drop",
        "n": "Promote out of turn, drop just as fast",
        "w": "Fast in, and fast out",
        "src": "The Comprehensive Mirror, Tang chronicles",
        "dek": "Many of the people she raised were later demoted or killed. "
               "This is about why a method that looks chaotic actually worked.",
        "story":
            "Sima Guang, who did not approve of her, wrote the most precise "
            "account of how she appointed people. She was not sparing with "
            "rank, using it to draw in able men everywhere as her own support; "
            "even an absurd man, if what he said fitted, was promoted out of "
            "turn. Those who could not do the job were dismissed soon after, "
            "or executed. ==Holding the two handles of punishment and reward, "
            "she governed from herself, saw clearly and decided well, so the "
            "able men of the age competed to be used by her.==",
        "f": [
            {"n": "Bold intake requires cheap removal",
             "d": "The risk in promoting out of turn is picking wrong. She "
                  "moved that risk onto the exit: fast in, fast out. Most "
                  "organisations dare not promote boldly, and the real reason "
                  "is not poor judgement of people; it is that removing "
                  "someone is expensive, so the gate has to be conservative.",
             "eg": "If probation is a formality and confirmation is automatic, "
                   "interviews can only get harder. Lower the cost of changing "
                   "your mind and hiring gets braver by itself."},
            {"n": "A wide gate is a way of enlarging the sample",
             "d": "Even an absurd man, if what he said fitted. She did not ask "
                  "for a person to be reliable overall, only to have been "
                  "right about one thing. That turns selection from judging a "
                  "person into collecting samples and filtering, with real "
                  "work replacing prior assessment.",
             "eg": "Instead of three months hunting a flawless candidate, give "
                   "three people one real job each and look at the results in "
                   "a month. Sample size beats accuracy of judgement."},
            {"n": "Both handles have to stay in one hand",
             "d": "Holding the two handles is the pivot the whole thing turns "
                  "on. Promotion and dismissal were hers alone, with no layer "
                  "in between to cushion or to plead. Once those two are "
                  "dispersed, fast in and fast out degrades into in only.",
             "eg": "Promotion needs five meetings and dismissal needs eight. "
                   "The outcome is fixed: people can enter and cannot leave, "
                   "and the organisation only swells."},
        ],
        "q": [
            "She was not sparing with rank, and used it to draw in talent.",
            "Those who could not do the job were dismissed soon after.",
            "Daring to promote out of turn rests on daring to remove.",
        ],
        "apply":
            "Where you are: you want to promote someone with an incomplete "
            "record and one outstanding side, and you are hesitating.\n"
            "Ask first: if this is wrong in three months, can I move them out, "
            "and what does that cost?\n"
            "Where it goes wrong: doing the bold intake without the exit, so "
            "the team runs away from you; handing both handles to committees, "
            "then wondering why nobody ever leaves.",
    },
    {
        "k": "the-manifesto",
        "n": "How did the chancellor lose this man",
        "w": "Recruiting from the pamphlet attacking you",
        "src": "New Book of Tang, Biographies of Men of Letters",
        "dek": "A document tearing you to pieces is put in front of you. This "
               "is about what she said at the cruellest line in it.",
        "story":
            "Xu Jingye rose against her, and Luo Binwang wrote the "
            "proclamation: an attack running from her private life to her "
            "usurpation, in the most vicious terms available. She laughed her "
            "way through it. Then she came to the earth on the late emperor's "
            "grave is not yet dry, and where have you put the orphan entrusted "
            "to you — and stopped laughing, and asked who wrote this. Luo "
            "Binwang, they said. ==How did the chancellor come to lose this "
            "man?== It was a document abusing her, and what she took from it "
            "was the writer.",
        "f": [
            {"n": "Handle the content and the stance separately",
             "d": "A passage carries two things at once: what it says, and "
                  "which side the speaker is on. Almost everyone rejects both "
                  "the moment they feel the hostility. She assessed the "
                  "quality first and dealt with the position second. That "
                  "order decides how much you can learn from an opponent.",
             "eg": "A competitor's public teardown of your product usually "
                   "contains its real weaknesses. Refusing to read it because "
                   "of the source throws away the most honest review you get."},
            {"n": "The line that hurts most is the most accurate",
             "d": "Where she stopped was the one sentence in the whole piece "
                  "she could not answer. An attacker looking to hurt you goes "
                  "hunting for the truest thing available, so hostile text "
                  "often carries more information per line than friendly "
                  "feedback, which is padded with politeness.",
             "eg": "The furious one-star review is usually far more specific "
                   "than the five-star one. How uncomfortable something is to "
                   "read often tracks how much it tells you."},
            {"n": "She sent the blame back to her own system",
             "d": "Her response was not that the man was vile but that the "
                  "chancellor had failed. The problem was assigned to her own "
                  "machinery for finding talent. Few people manage this step: "
                  "facing an able person who has gone to the other side, the "
                  "first move is to audit yourself.",
             "eg": "When a key person leaves for a competitor, asking why our "
                   "own assessment never spotted them is more useful than "
                   "discussing their ingratitude."},
        ],
        "q": [
            "The grave earth is not yet dry; where is the orphan entrusted?",
            "How did the chancellor come to lose this man?",
            "The line you cannot answer is the one worth keeping.",
        ],
        "apply":
            "Where you are: someone is attacking you or your work, in public "
            "and hard.\n"
            "Ask first: setting the stance aside, which sentence in it is "
            "hardest to refute?\n"
            "Where it goes wrong: rejecting the whole thing because of who "
            "wrote it; treating talent going to a rival as their failing and "
            "never auditing your own machinery.",
    },
]
