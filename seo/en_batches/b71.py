# -*- coding: utf-8 -*-
"""Daily entry: Xu Guangqi.

From DAILY_QUEUE.md row 8. 'I can't keep up with the new thing' holds entries on betting on the
old skill, attention, staying fluid and learning from people below you. None of them says where to
begin when a whole new field arrives in mid-career: start with the book everything else rests on.
The second chapter hangs on 'The tool does my thinking': ask for the needle, not the embroidery.

Why he qualifies: biography in the History of Ming; Minister of Rites and Grand Secretary; with
Matteo Ricci he translated the first six books of Euclid's Elements (1607), the founding text of
geometry in Chinese, and he compiled the Complete Treatise on Agriculture.

The entry story is the 1608 sweet potato planting; the chapters are both from the Elements translation.
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Xu Guangqi",
        "slug": "xu-guangqi",
        "e": "Ming · 1562–1633",
        "w": "Start from the bottom", "y": 1607,
        "d": "Ming-dynasty scholar from Shanghai who passed the highest civil-service examination in 1604 "
             "and rose to Minister of Rites and Grand Secretary; his biography is in the History of Ming. "
             "In his forties he translated the first six books of Euclid's Elements with the Jesuit Matteo "
             "Ricci, printed in 1607, and late in life he led a reform of the calendar and compiled a great "
             "treatise on agriculture. He is here for 'I can't keep up with the new thing', which covers "
             "practice, attention and learning from people below you, but not where to begin when a whole "
             "new field arrives in mid-career.",
        "story":
            "In 1608 floods across the lower Yangtze wiped out the wheat and rice. Xu was at home in Shanghai, "
            "mourning his father and looking for a crop that could tide people over. He heard that sweet "
            "potatoes did well in Fujian, and a visitor from Putian brought him planting stock three times. "
            "They grew as well as they did in the south, so he wrote a short treatise on how to plant them, "
            "for others to copy.",
        "f": [
            {"n": "The final exam at forty-two",
             "d": "He came first in the provincial examination at thirty-five and passed the final one only at forty-two. Two years later he began translating the Elements with Ricci, starting a whole new subject at an age when most men stop.",
             "eg": "Someone who moves into programming at forty need not feel they started late."},
            {"n": "What he learned went into the ground",
             "d": "He took European surveying and hydraulics straight into flood control and farming. The sweet potato went into a book only after he had grown it. His test for anything new was whether he could make it work with his own hands.",
             "eg": "Learn a new tool, then use it to finish one real piece of work on your own desk."},
            {"n": "Learn one thing, write one thing",
             "d": "The Elements, a book on surveying, a book on Western water methods, the treatise on agriculture: almost everything he learned he turned into writing. Once it was written down, he was no longer the only one who knew it.",
             "eg": "Learn a new method, write one page about it for a colleague, and find out whether you understand it."},
        ],
        "apply": "This week pick one new thing you feel you cannot keep up with. Find the most basic course or book underneath it, "
                 "and get the definitions in its first chapter clear before you look at any of the applications.",
        "q": [
            "Exams passed at forty-two, geometry begun at forty-four.",
            "Learn something new, then make it work with your own hands.",
            "Write down what you learned, and you are not the only one who knows it.",
        ],
        "l": ["Xu Xiake", "Fukuzawa Yukichi", "Richard Feynman"],
        "contrast": [
            {"n": "Fukuzawa Yukichi", "why": "Fukuzawa spent years on Dutch, saw that the signs in Yokohama were all in English, and switched at once: learn first what you can use now. Xu chose the book least usable on its own, the Elements: learn first what lies at the bottom. One warns against investing in a tool that is going out of date; the other says that under the new things there is a layer that does not."},
        ],
    },
]

INTROS = {
    "xu-guangqi":
        "Ming-dynasty minister who, in his forties, translated Euclid with Matteo Ricci - offered astronomy, "
        "calendars and firearms, he started with the driest book at the bottom, and said he wanted the needle, "
        "not the finished embroidery",
}

SCENES = [
    ("I can't keep up with the new thing", "AI arrived", [
        ("I'm past forty and don't know where to start with all this.",
         [("xu-guangqi", "start-from-the-root")]),
    ]),
    ("The tool does my thinking", "AI arrived", [
        ("Its answers are right, and I have no idea how it got them.",
         [("xu-guangqi", "golden-needle")]),
    ]),
]

ASKS = {
    "xu-guangqi/start-from-the-root": "I'm past forty and don't know where to start with all this.",
    "xu-guangqi/golden-needle": "Its answers are right, and I have no idea how it got them.",
}
