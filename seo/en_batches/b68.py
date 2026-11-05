# -*- coding: utf-8 -*-
"""Daily entry: Henry David Thoreau.

From DAILY_QUEUE.md row 5. 'I don't want to race but I'm scared to stop' holds Zhuangzi,
Confucius, Frankl, Wang Xing, Xunzi, Naval, Bai Juyi and Buffett: how to let go, how to slow
down, what the grind is for. Nobody there makes you work out what 'enough' is in numbers.

Why he qualifies: author of Walden, a book that has stayed in print for more than
a century and a half and a founding text of American nature writing.

The entry story is the borrowed axe; the chapters are the ledger and the train fare.
Everything here paraphrases Walden except one sentence quoted in full.
"""

ENTRIES = [
    {
        "c": "Mind and feeling",
        "n": "Henry David Thoreau",
        "slug": "thoreau",
        "e": "United States · 1817–1862",
        "w": "Counting enough", "y": 1845,
        "d": "American writer, author of Walden. In 1845 he built a small cabin by Walden Pond outside "
             "Concord, lived in it for two years and two months, and then wrote the book. Its most solid "
             "part is the first chapter, 'Economy', where he itemises the house and the food, clothes "
             "and fuel and works out that about six weeks of paid work a year would cover it. This page "
             "takes only his method of counting, not his criticism of society, and passes no verdict on "
             "his way of life.",
        "story":
            "In the spring of 1845 Thoreau borrowed an axe from his friend Bronson Alcott and went down to "
            "the pond to cut white pines for the frame of his cabin. When he was done he took the axe "
            "back. He wrote that he returned it sharper than he had received it.",
        "f": [
            {"n": "Turn enough into a number",
             "d": "He cut necessities down to four, food, shelter, clothing and fuel, and recorded what he actually spent on each. Wanting to spend less is a feeling; a ledger gives you something to compare.",
             "eg": "Sort the last three months into food, housing, getting about and utilities."},
            {"n": "Count the days you pay with",
             "d": "He worked out that a year needed only a few weeks of labour. He then used the same method on a ninety-cent train fare: a price is the part of your life you give up for it.",
             "eg": "Before a big purchase, convert it into extra working days."},
            {"n": "Borrow the method, not the number",
             "d": "He lived on a friend's land, close to town, and often ate at friends' tables. His figures had conditions of their own. What travels is the habit of counting.",
             "eg": "Do not say 'Thoreau needed twenty-eight dollars'. Say 'what did my year cost?'"},
        ],
        "apply": "This week, sort the last three months of spending into food, housing, getting about and utilities, "
                 "and write one total for each. Then ask which part is there only so as not to be outdone.",
        "q": [
            "To do less, first write the costs down.",
            "A price is the days you will pay with.",
            "Borrow the habit of counting, not the figures.",
        ],
        "l": ["Zhuangzi", "Montaigne", "Warren Buffett"],
        "contrast": [
            {"n": "Montaigne", "why": "Montaigne retired to his tower on income from the family estate and used the time to read and think. Thoreau went to the pond on a number he had worked out himself. One could afford to step back; the other first checked whether he could."},
        ],
    },
]

INTROS = {
    "thoreau":
        "American author of Walden - in his cabin by the pond he logged "
        "a year's costs and found about six weeks of paid work covered them; "
        "he also priced a ninety-cent train ticket in days",
}

SCENES = [
    ("I don't want to race but I'm scared to stop", "How you're doing", [
        ("I want to do less, but how much is enough?",
         [("thoreau", "count-enough")]),
    ]),
    ("Too busy to have a life", "How you're doing", [
        ("Is what I'm trading my time for worth it?",
         [("thoreau", "ride-or-walk")]),
    ]),
]

ASKS = {
    "thoreau/count-enough": "I want to do less, but how much is enough?",
    "thoreau/ride-or-walk": "Is what I'm trading my time for worth it?",
}
