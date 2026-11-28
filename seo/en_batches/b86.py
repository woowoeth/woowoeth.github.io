# -*- coding: utf-8 -*-
"""Daily entry: Franz Kafka.

Picked the old way (the queue in DAILY_QUEUE.md is finished and the next batch is not yet approved).
'Parents pushing' (Chinese side) is among the emptiest scenes; what hangs there is technique: separate the tasks,
label the feeling, find the need, stay differentiated, get out of the triangle. None says that the account between
a parent and a child may have no debtor, or asks you to write your parent's rebuttal before you speak.

Why he qualifies: one of the defining writers of the twentieth century (The Metamorphosis, The Trial, The Castle).
The entry story is the night on the pavlatche; the chapters are the opening and the closing of the Letter to His Father.
"""

ENTRIES = [
    {
        "c": "Family and relationships",
        "n": "Franz Kafka",
        "slug": "kafka",
        "e": "Prague, Austria-Hungary · 1883–1924",
        "w": "Fathers", "y": 1919,
        "d": "A German-language writer from Prague and the author of The Metamorphosis, The Trial and The Castle. "
             "He worked by day at a workers' accident insurance institute and wrote at night, published little, "
             "and died of tuberculosis at forty. In November 1919, aged thirty-six, he wrote his father a letter that ran "
             "to forty-five typed pages; according to his friend Max Brod it was given to his mother to pass on, and she never did. "
             "He is here for that letter: a son trying to settle accounts with an overwhelming father.",
        "story":
            "Kafka remembered one night as a small child when he kept whimpering for water, not from thirst, he admits, "
            "but partly to annoy and partly to amuse himself. After several stern threats failed, his father lifted him out "
            "of bed, carried him out onto the pavlatche, the open gallery outside the flat, shut the door and left him "
            "standing there alone in his nightshirt. He does not say it was wrong, he writes. He was obedient afterwards, "
            "but it did him inner harm.",
        "f": [
            {"n": "Rules for me alone",
             "d": "He saw his father mostly at meals. Food was not to be criticised, yet his father called it swill. Bones were not to be cracked, vinegar not slurped, but his father did both, and cut his nails at the table. The trouble was not the rules but who broke them.",
             "eg": "Telling a child to put the phone away at dinner while you answer messages teaches the second lesson, not the first."},
            {"n": "Kindness can crush",
             "d": "They often undressed in the same bathing hut, the boy thin and weak, the father big and broad. Meaning well, his father kept demonstrating swimming strokes the boy could not copy, and the boy felt only shame. His father was the measure of all things.",
             "eg": "If the fifth demonstration still has not landed, stop. Let someone else teach it, or try tomorrow."},
            {"n": "Put it on the bedside table",
             "d": "When he brought his father a new book, his father, usually at cards, would say only to put it on the bedside table. It hurt his vanity, yet it also sounded like being set free. All his writing, he later saw, was about his father: a long, deliberate farewell.",
             "eg": "If you are working to show your parents something, ask whether you would still do it if they never looked."},
        ],
        "apply": "This week write down one rule at home that binds you but not the person who made it. Do not take it to them. "
                 "Beside it, note whether you would keep it yourself if it were yours, and drop any such rule from the ones you set for your own children or team.",
        "q": [
            "A rule its maker breaks is only pressure.",
            "He meant well, and what I learned was shame.",
            "Everything I wrote was a farewell to you.",
        ],
        "l": ["Leo Tolstoy", "Murray Bowen", "Alfred Adler"],
        "contrast": [
            {"n": "Alfred Adler", "why": "Contemporaries, both born in Austria-Hungary, both wrote about how parents shape a child. Adler said the past does not decide you, the purpose you give it does, and that a parent's task should be separated from your own. Kafka set down thirty years of incidents for his father, admitted they had shaped him, and still refused to make them a charge. One tells you to cut the cord; the other lays the whole account on the table first."},
        ],
    },
]

INTROS = {
    "kafka":
        "The author of The Metamorphosis, an insurance clerk in Prague by day. At thirty-six he wrote his father "
        "forty-five pages about how he had been crushed, and still said: you are entirely blameless, and so am I",
}

SCENES = [
    ("I can't be myself around family", "At home", [
        ("My father and I: whose fault is it really?",
         [("kafka", "both-blameless")]),
        ("I've planned what to say, but only my side of it.",
         [("kafka", "his-objection")]),
    ]),
    ("We keep fighting", "At home", [
        ("After every fight I only remember my half.",
         [("kafka", "his-objection")]),
    ]),
]

ASKS = {
    "kafka/both-blameless": "My father and I: whose fault is it really?",
    "kafka/his-objection": "I've planned what to say, but only my side of it.",
}
