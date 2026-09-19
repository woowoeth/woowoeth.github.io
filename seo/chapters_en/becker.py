# -*- coding: utf-8 -*-
"""Gary Becker — English.

The English reader arrives knowing the phrase "human capital" and probably
disliking it, or else treating it as a management cliche about training
budgets. Both readings skip what the 1964 book actually does, which is put
a number on things people argue about with adjectives. Two numbers carry
these pages: foregone earnings were seventy-four per cent of the private
cost of college in 1939 and tuition only seventeen, and reenlistment in the
American military ran inversely to how much civilian-usable skill the
services had taught. Both are from the book, not from later retellings.

Sources are the NBER text: chapter IV for the 1939 cost split and the
rate-of-return estimates, chapter III for illiquidity and for the number of
periods, chapter II for general and specific training, the machinist and
interning doctor, the astronauts and fighter pilots, the recruiting problem,
the quit and layoff implications, and the Marshall footnote.
"""

PARENT = {
    "name": "Gary Becker",
    "slug": "becker",
    "blurb": "Deep read",
    "items": [
        {"k": "you-are-the-capital", "n": "The principal you never counted",
         "w": "You are the asset, and its price is not the tuition",
         "ready": True,
         "line": "On the 1939 college bill, tuition was seventeen per cent"},
        {"k": "general-and-specific",
         "n": "What they pay to teach you is what you cannot take",
         "w": "The line falls on the day you leave", "ready": True,
         "line": "The more civilian skill the military taught, the fewer "
                 "men re-enlisted"},
    ],
}

CHAPTERS = [
    {
        "k": "you-are-the-capital",
        "n": "The principal you never counted",
        "w": "You are the asset, and its price is not the tuition",
        "src": "Human Capital, 1964 — chapter IV on the 1939 college cohort, "
               "chapter III on the incentive to invest",
        "dek": "You keep looking for somewhere to put the money. The largest "
               "principal you hold has never been priced.",
        "story":
            "In 1939 an urban white American man going to college paid about "
            "$112 a year in tuition and fees, and under $175 once books and "
            "extra living costs were added. Becker went after the other "
            "figure: what he would have earned between eighteen and "
            "twenty-two and a half, had he not been in a lecture hall. Put "
            "the two together and foregone earnings came to seventy-four per "
            "cent of the whole, tuition and fees to seventeen. ==Which is "
            "why, he wrote, free colleges are not really very free after "
            "all.==",
        "f": [
            {"n": "The objection was to the phrase, not the finding",
             "d": "Until 1964 capital meant plant, machinery and land. "
                  "Counting a person's schooling as capital struck readers as "
                  "treating people like machines or like slaves. He returned "
                  "to the reception in a later introduction, by then mainly to "
                  "note how completely the objection had faded.",
             "eg": "Most people can list the projects they ran and not one of "
                   "them can say what those projects made them worth."},
            {"n": "The tuition line is the small line",
             "d": "He split the cost in two: money handed over, and money not "
                  "earned because you were studying instead. On the 1939 "
                  "accounts the second was almost three-quarters of the total. "
                  "Abolishing tuition removes the smallest item on the bill.",
             "eg": "A weekend course costs you the fee plus the two days of "
                   "work that did not happen."},
            {"n": "This asset cannot be sold or pledged",
             "d": "He is blunt about the defect. Human capital is extremely "
                  "illiquid: it cannot be sold, and it makes poor collateral "
                  "on a loan. You cannot slice off part of your future "
                  "earnings and sell it, so there is one way to pay - earn "
                  "less for a while.",
             "eg": "What stops most career changes is not the fee, it is the "
                   "six months of income nobody replaces."},
            {"n": "Twenty-five and fifty differ in years, not in rate",
             "d": "He separates the two deliberately. The rate of return on "
                  "the same outlay may be identical at every age; what differs "
                  "is how many years you get to collect it. Younger people "
                  "invest more not because they learn better or carry less, "
                  "but because they collect longer.",
             "eg": "Before deciding whether to learn something at forty, count "
                   "the years you will use it, then look at the fee."},
            {"n": "A footnote from a children's book",
             "d": "Making the point about remaining years, he adds a note from "
                  "an animal book he read to his children: training a working "
                  "elephant takes about ten years and nearly five thousand "
                  "dollars, but the animal usually lives past sixty, so the "
                  "outlay is not thought excessive.",
             "eg": "A skill good for twenty more years and one obsolete in "
                   "three are not the same purchase at the same price."},
        ],
        "apply":
            "Where you are: you have some money set aside and are deciding "
            "where to put it, while privately feeling you have not got much "
            "better at anything lately.\n"
            "Ask first: over the last twelve months, how much did I put into "
            "myself - not the fees, but the earnings I gave up to learn it, "
            "written down as a number and set beside what I invested.\n"
            "Where it goes wrong: reading it as stop investing, take a course. "
            "He is computing a rate of return, not recommending an attitude. "
            "A course is worth it if what it adds to future earnings beats "
            "what you gave up, multiplied by the years you will still use it.",
        "q": [
            "Tuition was seventeen per cent. The four years were the rest.",
            "This asset cannot be sold, and makes poor collateral.",
            "The young invest more because they collect for longer.",
        ],
    },
    {
        "k": "general-and-specific",
        "n": "What they pay to teach you is what you cannot take",
        "w": "The line falls on the day you leave",
        "src": "Human Capital, 1964 — chapter II, on-the-job training: "
               "general and specific",
        "dek": "Is what I am good at worth anything elsewhere. There is a "
               "computable answer, and it is in who paid.",
        "story":
            "In the 1960s the American military had a recruiting problem: "
            "first enlistments were easy, re-enlistments were not. Becker "
            "used it as his example. Much of what the services teach is "
            "usable in civilian life - machinists, navigators, pilots - and "
            "the figures ran backwards: the more civilian-type skill a man "
            "had been given, the less likely he was to sign on again. ==The "
            "services are the conspicuous exception, which is exactly why "
            "they show the rule so clearly.==",
        "f": [
            {"n": "He cuts training in two",
             "d": "General training is useful in many firms besides the one "
                  "providing it: a machinist trained in the army is worth the "
                  "same to steel and aircraft firms, a doctor interning at one "
                  "hospital to any other. Specific training raises "
                  "productivity only here - his examples are astronauts, "
                  "fighter pilots, missile men.",
             "eg": "Writing code is the first kind. Knowing which internal "
                   "service in this company must never be touched is the "
                   "second."},
            {"n": "Nobody pays for the half you can carry",
             "d": "In a competitive labour market general training lifts what "
                  "other firms will pay you by the same amount, so the firm "
                  "providing it captures none of the return and will not fund "
                  "it. You fund it, through wages below what you were already "
                  "worth while training.",
             "eg": "We invest in your growth often means the salary is held "
                   "down, and the gap is the tuition."},
            {"n": "Part of your current price holds only here",
             "d": "Specific training the firm will fund, but it fears you "
                  "leaving, so it pays above your outside offer and shares the "
                  "return. Cost and return are split, and what holds you is "
                  "arithmetic. In a footnote he quotes Marshall on the head "
                  "clerk worth several times his salary here and half of it "
                  "anywhere else.",
             "eg": "Before weighing an offer, split your pay: the part the "
                   "market pays, and the part only this employer pays."},
            {"n": "Teach it broadly and they leave sooner",
             "d": "The military numbers run the wrong way round: more "
                  "civilian-usable skill, fewer re-enlistments. It pays for "
                  "general training and then cannot match outside wages, so it "
                  "loses at both ends. First terms fill easily; second terms "
                  "do not, because by then the outside price has risen.",
             "eg": "A firm funding portable certifications either has another "
                   "hold on people or is training the competition."},
            {"n": "They are not the first out in a downturn",
             "d": "It follows that quit rates and layoff rates both fall as "
                  "specific training rises. When demand drops, the untrained "
                  "and the generally trained go first, because their product "
                  "merely equalled their wage; the specifically trained "
                  "started above it and are still above it.",
             "eg": "Whoever survived the last round may not be the ablest, "
                   "only the hardest to replace."},
        ],
        "apply":
            "Where you are: you are weighing whether to go, and the sentence "
            "in your head is whether you would still be worth this "
            "somewhere else.\n"
            "Ask first: of my current pay, how much does the market pay and "
            "how much does only this employer pay - and of what they have "
            "spent on training me these two years, how much can I carry out "
            "of the door.\n"
            "Where it goes wrong: reading it as none of their training is "
            "worth having, so leave. He never says specific training is "
            "worthless; it is the source of the premium you draw here. He "
            "says it does not travel, so it belongs among your reasons to "
            "stay, not in your market price.",
        "q": [
            "What they rush to pay for is what you cannot take.",
            "Teach it broadly and people leave sooner.",
            "What holds you is not loyalty but the unmatchable part.",
        ],
    },
]
