# -*- coding: utf-8 -*-
"""Daily entry: Gregor Mendel.

Picked the old way (the queue in DAILY_QUEUE.md is finished and the next batch is not yet approved).
'The side thing worked, the main thing didn't' is among the emptiest scenes, and almost every question
in it points to Pu Songling, whose lesson is that the side work succeeded without his knowing. None says
how to run a side project so that it can succeed: choose the material, count, keep it narrow.
'Nobody is looking at my work' has pieces on persisting and finding true fans; none says what to do with
the work itself while nobody looks: write it up completely and put it where it can be found.

Why he qualifies: founder of genetics; 'Experiments in Plant Hybridisation' (1866).
The entry story is the teacher's exam of 1850 and 1856; the chapters are the choice of peas and the rediscovery of 1900.
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Gregor Mendel",
        "slug": "mendel",
        "e": "Austrian Empire · 1822–1884",
        "w": "Heredity", "y": 1866,
        "d": "Augustinian friar at the abbey in Brünn (now Brno) and the founder of genetics. Between 1856 and 1863 "
             "he crossed peas in the monastery garden, and in 1866 published 'Experiments in Plant Hybridisation', "
             "the first account of heredity in counted ratios. The paper was almost ignored until three botanists "
             "found it independently in 1900. He is here for two situations: how to make the thing you do on the "
             "side more than a hobby, and what to do with good work that nobody reads.",
        "story":
            "In 1850 Mendel sat the exam to become a certified schoolteacher and failed its last part, the oral. "
            "His abbot, Cyril Napp, sent him to the University of Vienna, where from 1851 to 1853 he studied physics "
            "and natural science. Back in Brünn he taught as a substitute teacher. In 1856 he took the exam again "
            "and again failed the oral. That same year he planted the first peas for his crosses in the monastery garden.",
        "f": [
            {"n": "One pair at a time",
             "d": "He chose seven pairs of characters that anyone could tell apart: round or wrinkled seed, yellow or green seed leaves, the colour of the seed coat, inflated or constricted pods, green or yellow unripe pods, flowers along the stem or at its end, tall or short stems. He followed one pair at a time.",
             "eg": "To judge whether something is improving, watch one measure at a time, not ten at once."},
            {"n": "What hides comes back",
             "d": "In the first hybrid generation only one character of each pair showed. He called it dominant and the hidden one recessive. When the hybrids set seed, the hidden character returned, in about one in four. Hidden is not gone.",
             "eg": "A pupil who shows no progress this term has not lost everything you taught."},
            {"n": "After he became abbot",
             "d": "In 1868 he was elected abbot of the monastery. With the duties that came with it, his scientific work largely ended. Most of what he did in science was done in the dozen or so years before.",
             "eg": "When the main job finally takes off, keep a fixed slot for the side thing you care about."},
        ],
        "apply": "This week pick one thing you do on the side and care about, and choose a number to record every week: "
                 "pieces written, sessions practised, people who came. Record it for four weeks before deciding whether it is working.",
        "q": [
            "Watch one pair of characters at a time.",
            "Hidden is not gone.",
            "Treat the side project as real work.",
        ],
        "l": ["Charles Darwin", "Pu Songling", "Isaac Newton"],
        "contrast": [
            {"n": "Charles Darwin", "why": "They lived at the same time and both asked how living things pass on what they are. Darwin gathered material for twenty years and wrote a book that covered everything and was argued over at once. Mendel worked on one plant, wrote one paper, and was not cited for thirty-four years. One went as wide as possible, the other as narrow; later genetics needed both."},
        ],
    },
]

INTROS = {
    "mendel":
        "The founder of genetics, a friar who twice failed his teacher's exam. He spent two years choosing his peas "
        "and eight years counting them; his paper went unread for thirty-four years and was found by three people at once in 1900",
}

SCENES = [
    ("The side thing worked, the main thing didn't", "Looking back, moving on", [
        ("I want to take my side project seriously for once.",
         [("mendel", "pick-the-pea")]),
    ]),
    ("Nobody is looking at my work", "Getting it done", [
        ("My work is solid and nobody pays attention.",
         [("mendel", "on-the-record")]),
    ]),
]

ASKS = {
    "mendel/pick-the-pea": "I want to take my side project seriously for once.",
    "mendel/on-the-record": "My work is solid and nobody pays attention.",
}
