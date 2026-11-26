# -*- coding: utf-8 -*-
"""Daily entry: Blaise Pascal.

Picked the old way (the queue in DAILY_QUEUE.md is finished and the next batch is not yet approved).
'I can't sit still' (Chinese side) is among the emptiest scenes, and every piece there is a technique:
attention residue, flow, habit anchors, scheduling deep work. None asks what the restlessness is running from.
'I don't know what I want' has pieces on knowing what you don't want and on happiness as a by-product;
none says that what you wanted may have been the chase, not the thing.
English had no 'I can't sit still' situation, so this batch opens it.

Why he qualifies: co-founder of probability theory (with Fermat, 1654), Pascal's law, the Pensées (1670).
The entry story is the calculating machine; the chapters are the two halves of fragment 139.
"""

ENTRIES = [
    {
        "c": "Mind and feeling",
        "n": "Blaise Pascal",
        "slug": "pascal",
        "e": "France · 1623–1662",
        "w": "Diversion", "y": 1670,
        "d": "French mathematician, physicist and writer. At nineteen he built a calculating machine; the law of "
             "pressure in fluids carries his name; his letters with Fermat in 1654 on how to divide the stakes of an "
             "unfinished game began probability theory. He died at thirty-nine, and friends published his notes as the "
             "Pensées in 1670. He is here for what those notes say about why people cannot stop, not for the religious "
             "conclusion he drew from it.",
        "story":
            "In 1640 Pascal's father was posted to Rouen to oversee taxes and spent his days checking columns of figures. "
            "His son, not yet twenty, set out to spare him the drudgery, and in 1642 began building a machine that could "
            "add and subtract. In 1645 he presented one to the Chancellor, Séguier, with a letter. Years later he wrote "
            "that the machine produces effects nearer to thought than anything animals do, but has no will.",
        "f": [
            {"n": "A thinking reed",
             "d": "\"Man is but a reed, the most feeble thing in nature; but he is a thinking reed.\" A vapour or a drop of water can kill him, yet if the universe crushed him he would still be nobler, because he knows he dies and the universe knows nothing.",
             "eg": "When nothing seems to be in your control, you can still think the next thing through clearly. That part is yours."},
            {"n": "We never live in the present",
             "d": "Examine your thoughts, he said, and you will find them all taken up with the past and the future; we think of the present only to arrange the future. \"So we never live, but we hope to live.\"",
             "eg": "You finish dinner and cannot say what you ate, because the whole meal was spent on tomorrow's meeting."},
            {"n": "Two kinds of mind",
             "d": "He distinguished the mathematical mind, whose principles are far from ordinary use but plain once you turn to them, from the intuitive mind, whose principles are in front of everyone but so fine and numerous that some always escape notice.",
             "eg": "The person who can run the numbers often misreads the room, and the reverse. A team needs both."},
        ],
        "apply": "Today find fifteen minutes with no screen and sit alone. Each time you want to get up, note what had just come into your head. "
                 "Afterwards look at the list, pick the thing that came up most, and give it one concrete step this week.",
        "q": [
            "Feeble as a reed, and still able to think.",
            "Always preparing to be happy, never happy.",
            "Keep the mathematical mind and the intuitive one.",
        ],
        "l": ["Montaigne", "Isaac Newton", "Søren Kierkegaard"],
        "contrast": [
            {"n": "Montaigne", "why": "Both were French and both wrote about a person alone in a room; Pascal read Montaigne closely and argued with him throughout the Pensées. Montaigne withdrew to his tower at thirty-eight and wrote there for twenty years, treating a room of one's own as a good. Pascal said people are exactly the creatures who cannot stay in that room. One teaches how to stay; the other asks first why we can't."},
        ],
    },
]

INTROS = {
    "pascal":
        "The Pascal of probability theory and Pascal's law, who built a calculating machine at nineteen. "
        "In the Pensées he traced human unhappiness to one thing: we cannot stay quietly in our own room",
}

SCENES = [
    ("I can't sit still", "Body and energy", [
        ("The moment it goes quiet, I can't stand being in my own skin.",
         [("pascal", "a-quiet-room")]),
    ]),
    ("I don't know what I want", "Looking back, moving on", [
        ("The minute I get it, I stop wanting it.",
         [("pascal", "the-chase-not-the-hare")]),
    ]),
]

ASKS = {
    "pascal/a-quiet-room": "The moment it goes quiet, I can't stand being in my own skin.",
    "pascal/the-chase-not-the-hare": "The minute I get it, I stop wanting it.",
}

SC_BOX = {
    "I can't sit still":
        "Ten minutes at the desk and I'm up again, looking for something, anything. "
        "Where do I start?",
}
