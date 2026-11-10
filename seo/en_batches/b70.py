# -*- coding: utf-8 -*-
"""Daily entry: Leo Tolstoy.

From DAILY_QUEUE.md row 7. 'More output, emptier' holds entries on efficiency, tools and doing the
right things first. None of them describes a person who has already achieved what he wanted and
finds the emptiness arriving exactly then, or where he looked to get out of it.

Why he qualifies: author of War and Peace and Anna Karenina, by common consent at the summit of
world literature; A Confession is one of the classic first-person accounts of a midlife crisis of meaning.

The entry story is his last journey in 1910; the chapters are both from A Confession.
"""

ENTRIES = [
    {
        "c": "Mind and feeling",
        "n": "Leo Tolstoy",
        "slug": "tolstoy",
        "e": "Russia · 1828–1910",
        "w": "And what then", "y": 1879,
        "d": "Russian novelist who wrote War and Peace between 1863 and 1869 and Anna Karenina between 1873 "
             "and 1877. This page does not judge the novels, and leaves aside the religious and social teaching "
             "of his old age. It takes one stretch of A Confession: nearly fifty and holding everything, he was "
             "stopped by the question 'and what then?', and slowly worked his way out. He is here for the "
             "'more output, emptier' group, which covers efficiency, tools and doing the right things first, "
             "but not where the emptiness comes from once you have achieved what you set out to do.",
        "story":
            "In late autumn 1910, at eighty-two, Tolstoy slipped away before dawn from the estate where he "
            "had lived most of his life and boarded a train. A few days later he fell ill on the way and was "
            "carried into the stationmaster's house at Astapovo, where he died ten days after leaving home. "
            "The question he had written down in A Confession more than thirty years before had never let him go.",
        "f": [
            {"n": "After the two great books",
             "d": "War and Peace took about six years and Anna Karenina more than four. With both finished he had nothing left to prove as a writer, and that is exactly when the crisis came.",
             "eg": "The hardest stretch sometimes comes right after the biggest thing you have ever finished."},
            {"n": "Thinking of a rope at the best of times",
             "d": "He writes that he was not yet fifty, with a loving wife, good children, a thriving estate and a famous name. Yet he hid a cord from himself and stopped taking a gun out shooting, in case he used them.",
             "eg": "The person who seems to lack nothing is the one who finds it hardest to say they feel empty."},
            {"n": "He wrote those years down",
             "d": "In A Confession he set out how he got stuck, whom he looked at and which ways out he tried, without sparing himself. A vague misery only takes a shape you can see once it is written.",
             "eg": "Write your recent low in three lines: when it started, what makes it worst, what you are avoiding."},
        ],
        "apply": "This week, take something you recently finished and write down what you actually want now that it is done. "
                 "If you cannot write it, hold off before starting the next thing.",
        "q": [
            "Only once you have done it all does the hardest question arrive.",
            "The man who hid the rope seemed to have everything.",
            "Answer 'what for' before you take on the next thing.",
        ],
        "l": ["Søren Kierkegaard", "Henry David Thoreau", "Viktor Frankl"],
        "contrast": [
            {"n": "Viktor Frankl", "why": "Frankl had everything taken from him in the camps and still held on to a reason to live. Tolstoy had everything and could not find one. One shows that meaning does not depend on circumstances; the other, that circumstances cannot supply it."},
        ],
    },
]

INTROS = {
    "tolstoy":
        "Russian author of War and Peace and Anna Karenina - nearly fifty, with family, estate and fame, "
        "he was stopped by the question 'and what then?', hid a cord from himself, "
        "and wrote the way out in A Confession",
}

SCENES = [
    ("More output, emptier", "AI arrived", [
        ("The more I get done, the less I know what it's for.",
         [("tolstoy", "what-then")]),
    ]),
    ("None of it means anything", "Dealing with people", [
        ("Everyone tells me not to think so much, and I can't stop.",
         [("tolstoy", "look-elsewhere")]),
    ]),
]

ASKS = {
    "tolstoy/what-then": "The more I get done, the less I know what it's for.",
    "tolstoy/look-elsewhere": "Everyone tells me not to think so much, and I can't stop.",
}
