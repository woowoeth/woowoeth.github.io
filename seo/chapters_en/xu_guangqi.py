# -*- coding: utf-8 -*-
"""Xu Guangqi — English.

English readers who know the name at all know him as Matteo Ricci's collaborator. This page takes
the one thing he did as a learner: in his forties, faced with a whole new body of knowledge, he
started with the driest book at the bottom of it, and he insisted on the method rather than the
results. Both chapters come from the translation of Euclid's Elements, Books I-VI (1606-1607).
Xu's own words are classical Chinese, so they are paraphrased here, not quoted.
"""

PARENT = {
    "name": "Xu Guangqi",
    "slug": "xu-guangqi",
    "blurb": "Deep read",
    "items": [
        {"k": "start-from-the-root", "n": "The Book at the Bottom",
         "w": "When the new things keep changing, find the layer underneath that does not",
         "ready": True,
         "line": "Offered astronomy, calendars and firearms, he started with a dry book of points and lines"},
        {"k": "golden-needle", "n": "Hand Over the Needle",
         "w": "What you want is not the finished embroidery but the needle that made it",
         "ready": True,
         "line": "He turned an old saying round: never mind the embroidered ducks, hand over the golden needle"},
    ],
}

CHAPTERS = [
    {
        "k": "start-from-the-root", "n": "The Book at the Bottom",
        "w": "When the new things keep changing, find the layer underneath that does not",
        "src": "Matteo Ricci, preface to the Chinese Elements; Xu Guangqi, preface and 'Miscellaneous Remarks'; History of Ming, biography of Xu Guangqi",
        "dek": "He picked the driest book on offer. This asks where to start when new things arrive faster than you can learn them.",
        "story":
            "In 1606 Xu Guangqi was forty-four, two years past the top civil-service examination and "
            "serving at the Hanlin Academy in Beijing. From the Italian Jesuit Matteo Ricci he could have "
            "learned astronomy, calendar-making or firearms, all of them useful at once. He chose a book "
            "of points, lines and proofs: Euclid's Elements. ==He picked the driest book, the one at the "
            "bottom of all the others.== Ricci explained it aloud, Xu wrote it out in Chinese, and they "
            "went through three drafts.",
        "f": [
            {"n": "The surface changes, the bottom stays",
             "d": "In his preface Xu called the book the root of all measurement: calendars, surveying, waterworks and machines all draw on it. The applications change every generation. The definitions and proofs underneath had barely moved in nearly two thousand years.",
             "eg": "Frameworks turn over every year. The data structures and network protocols underneath have stayed much the same for decades."},
            {"n": "At forty-four, from the first definition",
             "d": "As a senior scholar he could simply have memorised ready-made calendar rules. He started from 'A point is that which has no part' and followed each proof in turn. Whoever masters this book, he wrote, can master anything.",
             "eg": "Moving into data work, skip the ten tool tutorials and learn the first chapter of statistics properly."},
            {"n": "Learn the bottom and the rest holds",
             "d": "In 1629, at sixty-seven, he was put in charge of reforming the calendar, and his writing on water control and farming leans on the same ground. What he learned in his forties served him for the rest of his life.",
             "eg": "Someone with solid foundations picks up a new tool in a week."},
        ],
        "q": [
            "The surface changes every year. The book at the bottom does not.",
            "Forty-four, and starting from the first definition.",
            "Learn the bottom layer and new things have somewhere to land.",
        ],
        "apply":
            "Where you are: New things keep arriving, you chase each one, and each feels out of date as soon as you have learned it.\n"
            "Ask first: Under all these new things, is there a layer they all rely on that has not changed in years?\n"
            "Where it goes wrong: Reading it as 'stick to the basics and ignore the new'. Xu learned geometry to use it on calendars, rivers and surveying. The bottom layer is there to catch the new things, not to hide from them.",
    },
    {
        "k": "golden-needle", "n": "Hand Over the Needle",
        "w": "What you want is not the finished embroidery but the needle that made it",
        "src": "Xu Guangqi, 'Miscellaneous Remarks on the Elements'; Matteo Ricci, preface to the Chinese Elements",
        "dek": "He wanted the needle, not the embroidery. This asks what to hold on to when answers come too easily.",
        "story":
            "In the spring of 1607 the first six books of the Elements were finished. An old Chinese saying "
            "went: show people the embroidered mandarin ducks, but never hand over the golden needle. In his "
            "notes on the book Xu turned it round: ==hand over the needle for others to use, and never mind "
            "the finished ducks==. This book, he added, does more than give you a needle. It teaches you to "
            "mine the ore, smelt the iron and draw the wire to make one.",
        "f": [
            {"n": "Results are the ducks, reasoning is the needle",
             "d": "The European calendar methods gave accurate results. That was the finished embroidery. Xu wanted the reasoning that let him work them out again himself. A borrowed result fails when conditions change; with the needle you can stitch a new pattern.",
             "eg": "A formula copied from somewhere breaks in a new setting. One you have derived, you can adapt."},
            {"n": "What can be derived need not be guessed",
             "d": "He wrote that this book left nothing to doubt, guess, test or correct. Each step follows from the one before, so you can check it yourself, without trusting anyone and without relying on luck.",
             "eg": "Sign off on a tool's conclusion only once you can trace it back step by step."},
            {"n": "Hold the needle yourself",
             "d": "Ricci explained aloud and Xu wrote every sentence, which meant understanding each one well enough to put it into Chinese. They went through three drafts. Following someone else's explanation is not the same as being able to write it.",
             "eg": "Close the tool and redo its derivation from scratch. Wherever you get stuck is what you still have to learn."},
        ],
        "q": [
            "Don't settle for the embroidered ducks. Ask for the needle.",
            "What you can derive, you don't have to take on trust.",
            "Write it out yourself, and the needle is in your hand.",
        ],
        "apply":
            "Where you are: The tool's answers are quick and right, and you are less and less able to say how they were reached.\n"
            "Ask first: If one condition changed, could I work this answer out again myself?\n"
            "Where it goes wrong: Reading it as 'invent everything from scratch'. Xu did not invent geometry. He took someone else's proofs and wrote them into words he could explain. The point is being able to redo it, not refusing to use it.",
    },
]
