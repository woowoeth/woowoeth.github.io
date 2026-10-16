# -*- coding: utf-8 -*-
"""Daily entry: Simone de Beauvoir.

Picked by fan-out, foreign side (the last two were Chinese). 'The work at home
doesn't count' (9 pieces, the emptiest at home) is full of who does what and
how it is split; nothing says why the work disappears: it leaves no trace.
'I can't stop pleasing people' has the stances and the boundaries but nothing
that asks whether the habit was taught.

Why she qualifies: author of The Second Sex (1949), the founding text of
modern feminist philosophy; passed the philosophy agrégation at twenty-one.

Quoted lines are from H. M. Parshley's 1953 translation of The Second Sex.
Three stories, no overlap: the entry is the exam and the ban; the chapters are
the washing up and the girl with a doll.
"""

ENTRIES = [
    {
        "c": "Family and relationships",
        "n": "Simone de Beauvoir",
        "slug": "beauvoir",
        "e": "France · 1908–1986",
        "w": "Not born", "y": 1908,
        "d": "A French philosopher and writer, born in Paris in 1908. She "
             "passed the philosophy agrégation in 1929 and taught in schools "
             "in Marseille, Rouen and Paris. In 1949 she published The Second "
             "Sex, asking from philosophy, history, biology and daily life "
             "why woman is treated as the Other and man as the human being. "
             "Her method was to take the smallest things, a stack of plates, "
             "a doll, a marriage, and ask who decided this. She won the Prix "
             "Goncourt in 1954 for The Mandarins and died in 1986.",
        "story":
            "In 1929, aged twenty-one, Beauvoir sat the French agrégation in "
            "philosophy and came second, behind Sartre; she was the youngest "
            "person ever to pass it. Twenty years later she published The "
            "Second Sex. French newspapers attacked it, and in 1956 the "
            "Vatican put it on the Index of forbidden books. It has been "
            "read ever since, in dozens of languages.",
        "f": [
            {"n": "Three small exhibits",
             "d": "She does not start from a conclusion. She starts with the smallest things and asks who decided them and for whom: a stack of plates, a doll, a marriage.",
             "eg": "A parent says 'girls should be quiet'. Take it apart and ask who is asking what of whom."},
            {"n": "The Other",
             "d": "Her central claim is that man is taken as the standard, as the human being, and woman is defined as his Other. That does not mean she is lesser; it means whoever defines first stands in the middle.",
             "eg": "We say 'woman driver' and 'woman leader'; the same words for a man need no qualifier."},
            {"n": "Situation, not nature",
             "d": "Her word is situation, not nature: what a person is like depends on where she has been put, and when the place changes, the person changes with it.",
             "eg": "The same person is called 'caring' at home and 'too soft' at the office."},
        ],
        "apply": "Pick one small thing you have always put down to 'that is just how I am' and write down when and by whom you were taught it. If you cannot, just notice whether it is a habit with a traceable origin.",
        "q": [
            "One is not born, but rather becomes, a woman.",
            "What looks most natural has often been taught longest.",
            "Ask who decided it before asking whether it is right.",
        ],
        "l": ["Arlie Hochschild", "Donald Winnicott", "Simone Weil"],
        "contrast": [
            {"n": "Arlie Hochschild", "why": "Both look at the work at home. Hochschild counts hours and who does them; Beauvoir asks why this kind of work leaves nothing behind, which is a claim about its nature, not its split"},
            {"n": "Donald Winnicott", "why": "Both study a compliant self. Winnicott looks for its origin in the earliest relationships; Beauvoir looks for it in how society teaches a girl, again and again, to please"},
        ],
    },
]

INTROS = {
    "beauvoir":
        "French philosopher, author of The Second Sex - she placed second in "
        "the philosophy agrégation at twenty-one and asked, with a stack of "
        "plates and a doll, why work that ends where it began goes unseen "
        "and how much of what we call nature was taught",
}

SCENES = [
    ("The work at home doesn't count", "At home", [
        ("I finish everything and the next day I am back at the start.",
         [("beauvoir", "the-torture-of-sisyphus")]),
    ]),
    ("I can't stop pleasing people", "Dealing with people", [
        ("I read faces so well. Was I born like this?",
         [("beauvoir", "one-is-not-born")]),
    ]),
]

ASKS = {
    "beauvoir/the-torture-of-sisyphus": "I finish everything and the next day I am back at the start.",
    "beauvoir/one-is-not-born": "I read faces so well. Was I born like this?",
}
