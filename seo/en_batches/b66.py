# -*- coding: utf-8 -*-
"""Daily entry: Leonardo da Vinci.

From DAILY_QUEUE.md row 3. 'I can't land work' holds Kevin Kelly, Paul Graham,
Graham, Merton and Su Qin on audiences, margins, being noticed and what to fix
after refusals. Nothing on what to put first in the pitch itself, or on how to
lower the buyer's fear of choosing wrong.

Why he qualifies: the defining figure of the Renaissance, painter, engineer and
anatomist, and an author of one of the largest surviving notebook corpora.

The entry story is the fate of the Sforza horse; the chapters are the letter's
list and its ending.
"""

ENTRIES = [
    {
        "c": "Reading people",
        "n": "Leonardo da Vinci",
        "slug": "leonardo",
        "e": "Italy · 1452–1519",
        "w": "Their list first", "y": 1482,
        "d": "Painter, engineer and student of anatomy of the Italian Renaissance, painter of the Last Supper and the "
             "Mona Lisa, and the author of thousands of surviving notebook pages. Around 1482 he drafted a letter "
             "asking Ludovico Sforza, the effective ruler of Milan, for work; the draft is in the Codex Atlanticus. "
             "This page takes two things from that letter: what he put first, and how it ends. It does not claim "
             "to know that the letter went out in this form.",
        "story":
            "Leonardo spent years on a bronze horse for Milan. In 1493 a clay model, about twenty-four feet high, "
            "stood on show for a royal wedding. The next year, with the French threatening, the bronze set aside "
            "for casting was sent to be made into cannon. In 1499 the French took Milan, and soldiers are said to "
            "have used the model for target practice. The horse he had offered in the letter was never cast.",
        "f": [
            {"n": "Write their list before yours",
             "d": "Nine of the ten claims in his letter are about war, and painting sits in the last sentence. He led with what the ruler was short of, and left what he loved most to be discovered later.",
             "eg": "In a cover letter, open with the problem the company has right now, not with your career history."},
            {"n": "Offer a small trial they can judge",
             "d": "He closed by offering to demonstrate any claim that seemed doubtful, in the duke's own park. The buyer's fear is hiring wrong, and a demonstration puts the checking in the buyer's hands.",
             "eg": "Offer to show a first page in the meeting, rather than asking them to take your word."},
            {"n": "What you promise has to get made",
             "d": "The horse was promised in the letter and never cast. War and the cost of bronze played their part, but the lesson stands: a promise on paper is a thing you will have to produce.",
             "eg": "Before you promise delivery in two weeks, check who actually has the time."},
        ],
        "apply": "Write a three-line note to one person you would like to work with: one trouble they have now, "
                 "one thing you can do about it, and one small piece you would gladly show them in person.",
        "q": [
            "Write what they lack before what you have.",
            "Offer a small trial and let them check it.",
            "A promise on paper is something you have to produce.",
        ],
        "l": ["Su Qin", "Guiguzi", "Kevin Kelly"],
        "contrast": [
            {"n": "Su Qin", "why": "Su Qin changed the buyer after a refusal. Leonardo changed the list before he ever spoke, putting what the buyer wanted ahead of what he loved. One adjusted after being turned down, the other in advance."},
        ],
    },
]

INTROS = {
    "leonardo":
        "Renaissance painter and engineer - his job letter to the ruler "
        "of Milan listed nine kinds of war machine and left painting to the "
        "last sentence",
}

SCENES = [
    ("Nobody is looking at my work", "Getting it done", [
        ("I can do almost anything, so why has nobody replied?",
         [("leonardo", "their-list-first")]),
        ("They're afraid of hiring wrong. What do I offer to put them at ease?",
         [("leonardo", "show-it-in-the-park")]),
    ]),
]

ASKS = {
    "leonardo/their-list-first": "I can do almost anything, so why has nobody replied?",
    "leonardo/show-it-in-the-park": "They're afraid of hiring wrong. What do I offer to put them at ease?",
}
