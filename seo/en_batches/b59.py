# -*- coding: utf-8 -*-
"""Daily entry: Søren Kierkegaard.

Picked by fan-out; the last eight are 5 Chinese to 3 foreign, so either side was
open. 'Two things I want' (9 pieces, tied for emptiest) has the cut-one rule, the
circle of competence and 'good enough', but nothing that says what to do when
you know you will regret either choice. 'Too many paths' has nothing on waiting
until you understand first.

Why he qualifies: founder of existentialist philosophy; Either/Or (1843), Fear
and Trembling (1843) and The Concept of Anxiety (1844) set the terms for how
the twentieth century talked about choice.

Quoted phrases are those common to every translation. Three stories, no
overlap: the entry is the broken engagement and the desk; the chapters are the
aphorism and the journal line.
"""

ENTRIES = [
    {
        "c": "Mind and feeling",
        "n": "Søren Kierkegaard",
        "slug": "kierkegaard",
        "e": "Denmark · 1813–1855",
        "w": "Choosing", "y": 1843,
        "d": "A Danish philosopher, born in Copenhagen in 1813 and dead in the "
             "same city in 1855. In 1843 he published Either/Or under a "
             "pseudonym, and that year also Fear and Trembling; in 1844 came "
             "The Concept of Anxiety. He signed different books with different "
             "invented names and let each voice argue its own position, "
             "without telling the reader which was right. What he wanted to "
             "know was not which answer is correct but how a person standing "
             "before two roads actually chooses, and answers for it.",
        "story":
            "In October 1841, aged twenty-eight, Kierkegaard returned the "
            "engagement ring to Regine Olsen, a little over a year after they "
            "had become engaged. He never married. Two years later Either/Or "
            "appeared without his name on it: the editor was a made-up "
            "Victor Eremita, whose preface says he found the papers in a "
            "hidden drawer of an old writing desk.",
        "f": [
            {"n": "The one choosing is you",
             "d": "Either/Or sets two ways of living side by side and does not announce a winner. The reader has to do the choosing, which is the point: no one else can do it in your place.",
             "eg": "A friend lays out both options and says 'I would take the first', and you still have to be the one who signs."},
            {"n": "Anxiety is the dizziness of freedom",
             "d": "In The Concept of Anxiety he says the dizziness comes from looking down into your own possibilities. The more you could do, the more it swims. He does not treat it as a fault; he treats it as what freedom feels like.",
             "eg": "Standing in front of twelve career paths, you feel sick, and the sickness is a sign the choice is real."},
            {"n": "Understood backwards, lived forwards",
             "d": "His journal says life can only be understood looking back, yet has to be lived looking ahead. So the clarity you are waiting for will not arrive before the decision; it arrives after.",
             "eg": "Only on leaving a job do you see which of the early signs mattered."},
            {"n": "Different names, one reader",
             "d": "He published under pseudonyms so that readers could not borrow his authority. If the voice is invented, you cannot say 'the author agrees with me'; you have to argue with the position itself.",
             "eg": "A manager who writes the case against his own plan, and has someone else sign it."},
        ],
        "apply": "Pick one small thing where you do not want to let either side go. Give yourself ten minutes, cross out the column that says 'afraid of regret', and write only which one you are more willing to answer for. Then do it, and do not reopen the other column.",
        "q": [
            "Anxiety is the dizziness of freedom.",
            "Regret cannot rank two choices; do not ask it to.",
            "Looking back makes sense of it; only going forward gets you there.",
        ],
        "l": ["Steve Jobs", "Herbert Simon", "Viktor Frankl"],
        "contrast": [
            {"n": "Steve Jobs", "why": "Both face two good things. Jobs says cut one and accept the loss; Kierkegaard says whichever you cut will hurt, and the hurt is not evidence you cut the wrong one"},
            {"n": "Herbert Simon", "why": "Both are about choices that will not settle. Simon puts a stopping rule on the search, good enough and go; Kierkegaard says the search will not stop because we dread regret, and regret comes from both sides"},
        ],
    },
]

INTROS = {
    "kierkegaard":
        "Danish philosopher, author of Either/Or - he wrote a book that "
        "refuses to give the answer: what to go by when you want both and "
        "dread regretting either, and why waiting until you understand "
        "first never ends",
}

SCENES = [
    ("Too many paths", "Looking back, moving on", [
        ("Whichever I pick, I will regret it.",
         [("kierkegaard", "regret-either-way")]),
        ("I want to understand it first, then choose.",
         [("kierkegaard", "lived-forwards")]),
    ]),
]

ASKS = {
    "kierkegaard/regret-either-way": "Whichever I pick, I will regret it.",
    "kierkegaard/lived-forwards": "I want to understand it first, then choose.",
}
