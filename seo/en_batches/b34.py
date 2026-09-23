# -*- coding: utf-8 -*-
"""Daily entry, day 14: Ruth Schwartz Cowan.

Picked by fan-out. On the Chinese side 'The work at home doesn't count' was
one of the emptiest situations, and every question in it pointed at
Hochschild, Satir, Thomas Gordon or nonviolent communication: all of them
about the division between two people. None of them answers the question the
reader in a house full of appliances actually asks, which is why the
appliances did not help. Cowan's answer is historical and has two halves:
the machines mostly replaced helpers - the men's share, the maid, the
laundress, the delivery man - and what they did save in effort was eaten by
rising standards. The second half also fills a hole in 'More output,
emptier', where Postman, Illich and Weil explain how tools reshape a day but
nobody shows the arithmetic of a saving that never arrived.

Figures and the two quoted sentences are from her own essay 'Less Work for
Mother?', American Heritage 38:6 (1987), checked against the printed text,
not written from memory. The GE advertisement is given as she paraphrases
it, not in quotation marks.

Three stories, no overlap: the entry is her own afternoon of five
interruptions while writing that essay, the first chapter is the 1918
vacuum-cleaner advertisement and the servant census, the second is the
laundry basket.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Family and relationships",
        "n": "Ruth Schwartz Cowan",
        "slug": "cowan",
        "e": "United States · 1941-",
        "w": "Household technology", "y": 1983,
        "d": "American historian of technology, born in Brooklyn in 1941, "
             "who taught at SUNY Stony Brook from 1967 to 2002 and is now "
             "professor emerita at the University of Pennsylvania. Her 1983 "
             "book More Work for Mother won the Dexter Prize of the Society "
             "for the History of Technology the following year. It asks a "
             "question everyone assumes is settled: the house fills with "
             "machines, so why has the housework not shrunk? Her answer has "
             "two halves. The machines mostly replaced helpers - the men's "
             "and children's share, the maid, the laundress, the delivery "
             "man - and what was left fell to the wife alone. And whatever "
             "effort they did save was absorbed by rising standards. By the "
             "time studies she gathered, a full-time American housewife "
             "worked fifty to sixty hours a week at home from the early "
             "twentieth century to the 1980s.",
        "story":
            "In 1987 she wrote an essay for American Heritage called 'Less "
            "Work for Mother?'. Partway through she recorded what happened "
            "while she was writing it. She was interrupted five times: to "
            "take a child to field hockey practice, then to bring her back, "
            "to pick up groceries at the supermarket, to retrieve her husband "
            "stranded at the train station, and for a trip to a doctor's "
            "office. Each time, she wrote, she was doing housework, and each "
            "time she had to use her car. We do not think of cars as "
            "household appliances. She argued that is exactly what they are.",
        "f": [
            {"n": "Ask whose effort it saved",
             "d": "Every labour-saving thing that enters a house deserves one "
                  "question: before it came, who did this? Her answer kept "
                  "repeating. The share removed was the husband's, the "
                  "children's, the maid's, the delivery man's. The share "
                  "left over did not shrink; it became one person's.",
             "eg": "The robot vacuum arrives, and the family that used to "
                   "clean together on Saturdays goes back to their rooms."},
            {"n": "Saved effort, eaten by standards",
             "d": "The washing machine made laundry lighter, so laundry was "
                  "done more often: whole shirts instead of detachable "
                  "collars, both sheets changed, clean underwear daily. By "
                  "the 1980s a housewife washed about ten times her mother's "
                  "load by weight, in no less time.",
             "eg": "A slide takes five minutes instead of an hour, so every "
                   "review now needs fifty of them."},
            {"n": "The car is an appliance",
             "d": "The iceman, the milkman, the grocer, the seamstress and "
                  "the doctor used to come to the door. Once she drove, "
                  "businesses and doctors found it paid not to, and her work "
                  "gained a new line: chauffeur. The road became a full "
                  "working day a week.",
             "eg": "'Click and collect' and 'self-service online': the "
                   "journey you no longer pay for is the one you now make."},
        ],
        "apply":
            "If every machine is in your house and you are still the busiest "
            "person in it, do one thing today. List each labour-saving "
            "machine you own, and next to it write who did that job before "
            "it arrived. Some lines will name other people: a relative who "
            "used to help, a shop that used to deliver, someone who used to "
            "do the washing-up without being asked. Those lines are what the "
            "machines really replaced. Then add a second note to each line: "
            "who set today's standard for this job, and how much higher is "
            "it than ten years ago? With that list on the table the "
            "conversation is no longer 'could you help me more', but how "
            "many people this work was meant for, and whether the standard "
            "needs to be this high.",
        "q": [
            "Drudgery had disappeared, but the laundry hadn't.",
            "The machine did not remove the work. It removed the helpers.",
            "Effort saved is not time saved.",
            "The delivery man is gone; the delivering is not.",
        ],
        "l": ["Arlie Hochschild", "Ivan Illich", "Neil Postman",
              "C. Northcote Parkinson"],
        "contrast": [
            {"n": "Arlie Hochschild",
             "why": "Both keep the books on the unseen work at home: "
                    "Hochschild counts who works the extra shift between two "
                    "partners, while Cowan goes one step back and shows the "
                    "ledger was already wrong between people and machines, "
                    "when the helpers, the delivery man and the men's share "
                    "left the house as the appliances came in"},
            {"n": "Ivan Illich",
             "why": "Both say a labour-saving tool can end up occupying the "
                    "person it served: Illich argues it from thresholds and "
                    "the effective speed of the car, while Cowan follows the "
                    "same car as it moves the shop's and the doctor's "
                    "delivery work onto the housewife, and names who was "
                    "occupied and for how many hours"},
        ],
    },
]

INTROS = {
    "cowan":
        "A historian of technology who asked why a house full of "
        "labour-saving machines still takes fifty to sixty hours a week - "
        "the machines mostly replaced helpers, and the effort they saved was "
        "eaten by rising standards",
}

SCENES = [
    ("The work at home doesn't count", "At home", [
        ("Every machine is in the house and the work is still all mine.",
         [("cowan", "the-helpers-left")]),
    ]),
    ("There's never enough time", "Body and energy", [
        ("Nothing gets delivered any more. I drive to all of it.",
         [("cowan", "the-helpers-left")]),
        ("The house is full of appliances and I am never done.",
         [("cowan", "effort-saved-time-not")]),
    ]),
    ("More output, emptier", "AI arrived", [
        ("The tools got faster and I have no less to do.",
         [("cowan", "effort-saved-time-not")]),
    ]),
]

ASKS = {
    "cowan/the-helpers-left":
        "Every machine is in the house and the work is still all mine.",
    "cowan/effort-saved-time-not":
        "The tools got faster and I have no less to do.",
}
