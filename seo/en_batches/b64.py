# -*- coding: utf-8 -*-
"""Daily entry: Isaac Newton.

From DAILY_QUEUE.md row 1. 'Everyone is piling in' holds Soros, Kindleberger,
Keynes and Marks on crowds and on envy of a friend who got rich. Nothing on the
person who already sold at a profit and is pulled back by watching it keep
rising. 'I don't have enough information' has nothing on a rule that works
while its cause is still unknown.

Why he qualifies: founder of classical mechanics and of the calculus of
motion; the Principia (1687) is the founding text of modern physics.

The entry story is Halley's visit to Cambridge in 1684 and the printing of the
Principia; the chapters are the South Sea stock of 1720 and the General
Scholium of 1713.
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Isaac Newton",
        "slug": "newton",
        "e": "England · 1643–1727",
        "w": "Framing no hypotheses", "y": 1687,
        "d": "English physicist and mathematician. His Mathematical Principles of Natural Philosophy (1687) "
             "put the orbits of the heavens and the fall of an apple into one set of laws. In 1696 he left "
             "Cambridge to work at the Royal Mint in London, became its Master in 1699, and from 1703 was "
             "President of the Royal Society. This page takes two things: how to keep what you can calculate "
             "apart from what you can only guess, and how a man who lived by sums sold a stock well and then "
             "bought it back.",
        "story":
            "In August 1684 the astronomer Edmond Halley came to Cambridge and asked what curve a planet "
            "would follow if the sun's pull weakened with the square of the distance. An ellipse, Newton "
            "said, and he had worked it out, but he could not find the paper among the others on his desk. "
            "After Halley left he did the sum again, and in November sent a short tract that grew into the "
            "Principia. It came out in 1687, and Halley paid for the printing.",
        "f": [
            {"n": "Keep the rule apart from the cause",
             "d": "He gave the formula for gravity in full, and when asked how it reaches across empty space he said he did not yet know and would not make something up. What was not drawn from the phenomena he called a hypothesis and kept out of his conclusions.",
             "eg": "You see from the data that sales move with the weather. 'People are in a better mood' is only a guess, and in the report it gets a line to itself."},
            {"n": "Sold well, then bought back in",
             "d": "In spring 1720 he sold his South Sea stock for a profit of a few thousand pounds. In summer he watched the price keep rising, bought a larger stake, and by the autumn crash had lost about twenty thousand pounds in all.",
             "eg": "You cash out, it rises another twenty per cent, and what you remember is the twenty per cent, not the gain already in your hand."},
            {"n": "Admit no extra cause",
             "d": "The Principia opens with rules of reasoning, and the first says to admit no more causes than are true and enough to explain the thing. The extra one is your taste, not evidence.",
             "eg": "Traffic fell and your data shows two changes you made. Check those two before you wonder whether the algorithm changed."},
        ],
        "apply": "This week take one conclusion you are about to give someone and split it into two columns: what I measured or calculated, and what I guessed. "
                 "When you report it, say the two columns separately.",
        "q": [
            "Use the rule now; the cause can wait.",
            "After selling, do not keep the books on the rise.",
            "Explain a thing without adding a cause.",
        ],
        "l": ["Albert Einstein", "Richard Feynman", "Charles P. Kindleberger", "George Soros"],
        "contrast": [
            {"n": "Albert Einstein", "why": "Both faced a cause nobody had. Newton said he would not invent one and left it empty while the calculation stood; Einstein invented one and pushed it until it contradicted itself. One shelves what he cannot prove, the other puts it out to be tested."},
            {"n": "Charles P. Kindleberger", "why": "The same South Sea bubble of 1720. Kindleberger stood outside it and laid three hundred years of crashes into one table; Newton was one cell in that table, inside it and swept along. One counted from outside, the other was pushed from within."},
        ],
    },
]

INTROS = {
    "newton":
        "English physicist and author of the Principia - he calculated "
        "gravity in full and, asked how it crosses empty space, said he did "
        "not yet know and would frame no hypotheses; in 1720 he sold South "
        "Sea stock at a profit, bought back in higher, and lost about "
        "twenty thousand pounds",
}

SCENES = [
    ("Everyone is piling in", "Money", [
        ("I sold early, watched it keep going up, and bought back in.",
         [("newton", "sold-too-early")]),
    ]),
    ("I don't have enough information", "Making a call", [
        ("I can't say why it works. Can I act on the data anyway?",
         [("newton", "no-hypotheses")]),
    ]),
]

ASKS = {
    "newton/sold-too-early": "I sold early, watched it keep going up, and bought back in.",
    "newton/no-hypotheses": "I can't say why it works. Can I act on the data anyway?",
}
