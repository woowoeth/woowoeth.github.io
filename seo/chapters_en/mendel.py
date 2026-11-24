# -*- coding: utf-8 -*-
"""Gregor Mendel — English.

English readers know the peas and the 3:1 from school, usually as a fact rather than a way of working.
This page takes two things from the man: how he made a spare-time project into a rigorous one, and how a
paper nobody read for thirty-four years was still there to be found. It leaves later disputes in genetics alone.
Quoted words are from William Bateson's translation in Mendel's Principles of Heredity: A Defence (1902),
Project Gutenberg no. 69362, which also holds Bateson's 1900 lecture on the rediscovery.
The popular line 'My time will come' rests on a later recollection and is not used.
"""

PARENT = {
    "name": "Gregor Mendel",
    "slug": "mendel",
    "blurb": "Deep read",
    "items": [
        {"k": "pick-the-pea", "n": "Choose the pea first",
         "w": "A side project succeeds when you run it like a real one", "ready": True,
         "line": "Before a single cross, he grew thirty-four kinds of pea for two years just to choose his material"},
        {"k": "on-the-record", "n": "Print it and leave it",
         "w": "When nobody reads your work, make sure it can be found", "ready": True,
         "line": "A paper nobody cited for thirty-four years was found by three people at once in 1900"},
    ],
}

CHAPTERS = [
    {
        "k": "pick-the-pea", "n": "Choose the pea first",
        "w": "A side project succeeds when you run it like a real one",
        "src": "Gregor Mendel, 'Experiments in Plant Hybridisation' (1866), in William Bateson's translation (1902)",
        "dek": "There is a thing you do on the side that you care about. How do you make it more than a hobby?",
        "story":
            "Mendel twice failed the oral part of the exam to become a certified schoolteacher, and taught as a "
            "substitute. His peas grew in the monastery garden. Before making a single cross he obtained thirty-four "
            "varieties from several seedsmen and grew them for two years, only to see which kept their characters "
            "true. In a pea the pollen reaches the stigma before the flower opens, so stray pollen rarely gets in. "
            "==With the right material, the counting could be trusted.==",
        "f": [
            {"n": "Decide what the material must do",
             "d": "His paper opens the method by saying that \"the value and utility of any experiment are determined by the fitness of the material to the purpose for which it is used\". Then the conditions: constant, clearly different characters; hybrids that can be protected from foreign pollen; offspring that stay fertile.",
             "eg": "Before starting a podcast on the side, try three formats for two weeks and keep the one you can measure the same way every time."},
            {"n": "Count, don't look",
             "d": "He noted that among all the hybrid experiments before him, none had been carried far enough to count the forms of the offspring and their ratios. He counted: 253 hybrids gave 7,324 seeds, 5,474 round and 1,850 wrinkled, a ratio of 2.96 to 1.",
             "eg": "To know whether the side project is going anywhere, write down the same number every week for three months."},
            {"n": "Keep it small, finish it",
             "d": "He said the work was practically confined to a small plant group and took eight years to conclude in all essentials. \"It requires indeed some courage to undertake a labour of such far-reaching extent\", he wrote, yet it seemed the only right way.",
             "eg": "Pick one narrow question and carry it through to a complete result before widening it."},
        ],
        "q": [
            "An experiment is worth what its material is fit for.",
            "Many had crossed plants. Nobody had counted to the end.",
            "One kind of pea, eight years.",
        ],
        "apply":
            "Where you are: The day job is going nowhere, and the thing you do on the side matters to you, but you have always treated it as play.\n"
            "Ask first: Can the results of this thing be counted? Am I recording numbers, or impressions?\n"
            "Where it goes wrong: Reading it as 'take your side project seriously and it will succeed'. Mendel did the work properly and nobody recognised it in his lifetime. Rigour buys a result that others can check later, not a guarantee.",
    },
    {
        "k": "on-the-record", "n": "Print it and leave it",
        "w": "When nobody reads your work, make sure it can be found",
        "src": "Gregor Mendel, 'Experiments in Plant Hybridisation' (1866); William Bateson, Mendel's Principles of Heredity: A Defence (1902)",
        "dek": "The work is solid and nobody pays attention. What should you do with it while nobody is looking?",
        "story":
            "In February and March 1865 Mendel read his pea experiments to the Natural History Society of Brünn, and "
            "the next year the paper appeared in the society's proceedings. For more than thirty years almost nobody "
            "cited it. He died in 1884. In 1900 Hugo de Vries, Carl Correns and Erich von Tschermak, working separately, "
            "reached the same ratios, and ==each of them pointed back to that paper==. William Bateson, reading it, "
            "called the account \"excellent and complete\".",
        "f": [
            {"n": "Write it so others can check it",
             "d": "He recorded how many plants were used, how many seeds they bore, of which kinds and in what ratio, down to extreme cases such as one plant with 14 round and 15 angular seeds. Thirty-four years later others laid their own counts beside his, and they matched.",
             "eg": "For the piece nobody read, add how you did it and what the numbers were, so someone could repeat it."},
            {"n": "A lecture lasts one evening; print lasts",
             "d": "Reading the paper aloud reached one room of listeners. Printing it put it on paper and onto shelves. The three men of 1900 could find it because of the printed copy, not because anyone remembered those two evenings.",
             "eg": "Put finished work somewhere public, dated and searchable, not only on your own laptop."},
            {"n": "Neglect is often bad timing",
             "d": "Bateson offered a reason for the silence: around 1865 new methods of research had opened up, and the most original investigators preferred them to the tedious observations of hybridisers. He still admitted that the total neglect of such a discovery was not easy to account for.",
             "eg": "When everyone is chasing another field, an empty audience is not proof that you did the work badly."},
        ],
        "q": [
            "Unread does not mean badly done.",
            "A complete record still matched thirty-four years later.",
            "Put it where it can be found.",
        ],
        "apply":
            "Where you are: You made something you believe is solid, you put it out, and nobody paid attention. You are starting to think it was wasted.\n"
            "Ask first: Is it written up completely? If someone wanted to check it one day, could they? Is it somewhere it can be found?\n"
            "Where it goes wrong: Reading it as 'good work is always discovered, so just wait'. Mendel did not live to see it. It was found because of the complete record and the printed copy, and both of those he made himself.",
    },
]
