# -*- coding: utf-8 -*-
"""Daily entry: Charles Darwin.

The queue (DAILY_QUEUE.md) was finished yesterday, so this one was picked the old way: every scene now
holds at least ten pieces, and among the emptiest are 'credit taken' and 'out of energy'. The credit
pieces are about being overlooked or pushed aside; none covers the case where someone else independently
arrives first. The energy pieces all assume the energy can be got back; none starts from a limit that
will not lift.

Why he qualifies: founder of evolutionary biology; On the Origin of Species (1859).

The entry story is the Beagle offer (Autobiography); the chapters are the Wallace letters of June 1858
and Francis Darwin's account of the daily routine. Quoted words are checked against the Darwin
Correspondence Project transcriptions and The Life and Letters of Charles Darwin (1887), vol. 1.
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Charles Darwin",
        "slug": "darwin",
        "e": "England · 1809–1882",
        "w": "Slow work", "y": 1859,
        "d": "English naturalist and founder of evolutionary biology. At twenty-two he sailed on the Beagle for nearly "
             "five years; in 1837 he opened his first notebook on species; in 1859 he published On the Origin of "
             "Species and gave biology natural selection. He gathered facts for more than twenty years before the book, "
             "much of that time ill. He is here for two things anyone may meet: being beaten to your own idea, and "
             "working with a body that will not cooperate.",
        "story":
            "In the summer of 1831 Darwin, twenty-two, had a letter: the captain of the Beagle would give up part of "
            "his own cabin to a young man willing to sail unpaid as naturalist. He was eager at once. His father "
            "strongly objected, and added: \"If you can find any man of common sense who advises you to go I will "
            "give my consent.\" Darwin wrote that evening and refused. Next morning, out shooting at his uncle Josiah "
            "Wedgwood's, he was sent for. The uncle thought he should go and drove him home to say so. His father "
            "held the uncle one of the most sensible men in the world, and consented at once.",
        "f": [
            {"n": "Write down the fact against you, at once",
             "d": "For many years he kept what he called a golden rule: whenever a fact, observation or thought turned up that went against his results, he made a note of it without fail and at once. He had found such things slip from memory far more easily than welcome ones.",
             "eg": "Keep one page in the plan for what counts against it, and fill it in the same day."},
            {"n": "A theory in hand, and nothing written",
             "d": "Once he had natural selection he was so anxious to avoid prejudice that he decided not to write even the briefest sketch for some time. In June 1842 he allowed himself 35 pages in pencil. In the summer of 1844 he enlarged it to 230 and had it fairly copied.",
             "eg": "When an explanation feels beautiful, go looking for what it cannot explain."},
            {"n": "His own verdict on himself",
             "d": "In old age he took stock. No great quickness of apprehension or wit, unlike Huxley; little power to follow a long abstract argument, so no mathematics. He put his success down to love of science, patience in reflecting, industry in collecting facts and a fair share of common sense.",
             "eg": "If you are not the quickest in the room, be the one who thinks about it longest."},
        ],
        "apply": "This week keep one page beside the thing you are pushing, headed 'against it'. Note each item the "
                 "moment you meet it. If the page is empty by Friday, you probably did not write, not that there was nothing.",
        "q": [
            "The fact against you is the first one you forget.",
            "Not the quickest? Think about it longest.",
            "Find one person of common sense who says go.",
        ],
        "l": ["Isaac Newton", "Richard Feynman", "Karl Popper"],
        "contrast": [
            {"n": "Isaac Newton", "why": "Both faced the question of who thought of it first. Newton fought Leibniz over the calculus for years, and the Royal Society report that found for him came from a committee appointed while he was its president. Darwin handed his old draft to two friends, published jointly with Wallace, and Wallace later called his own book on evolution Darwinism."},
        ],
    },
]

INTROS = {
    "darwin":
        "The founder of evolutionary biology. A stranger posted him the theory he had kept unpublished for twenty "
        "years, and he argued the case against himself before letting friends decide; ill for nearly forty years, "
        "he wrote the Origin on about four working hours a day",
}

SCENES = [
    ("Nobody is looking at my work", "Getting it done", [
        ("I worked on it for years and someone else got there first.",
         [("darwin", "forestalled")]),
    ]),
    ("I've run out of energy", "Body and energy", [
        ("My health won't improve. Can I still get real work done?",
         [("darwin", "a-good-days-work")]),
    ]),
]

ASKS = {
    "darwin/forestalled": "I worked on it for years and someone else got there first.",
    "darwin/a-good-days-work": "My health won't improve. Can I still get real work done?",
}
