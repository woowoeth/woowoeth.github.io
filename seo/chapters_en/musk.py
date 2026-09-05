# -*- coding: utf-8 -*-
"""Elon Musk — English.

First principles is now said so often in English that it has stopped
meaning anything; it mostly signals that the speaker intends to disagree.
So the page does not argue for the method. It gives the definition he
actually used and the arithmetic he did with it, and then the second
chapter gives the crude little ratio that turned the method into something
a purchasing department can run every week — which is the part that makes
it a practice rather than an attitude.
"""

PARENT = {
    "name": "Elon Musk",
    "slug": "musk",
    "blurb": "Deep read",
    "items": [
        {"k": "first-principles", "n": "Boil it down to what is physically true",
         "w": "Analogy quotes the going rate; physics gives the floor", "ready": True,
         "line": "Batteries cost 600 a kilowatt-hour. The metals cost 80"},
        {"k": "idiot-index", "n": "Part price over material price",
         "w": "A number that tells you where to start", "ready": True,
         "line": "Aluminium worth hundreds, bought for tens of thousands"},
    ],
}

CHAPTERS = [
    {
        "k": "first-principles",
        "n": "Boil it down to what is physically true",
        "w": "Analogy quotes the going rate; physics gives the floor",
        "src": "TED interview, 2013",
        "dek": "The phrase is everywhere now. What is worth having is his own "
               "definition, and the arithmetic he did on a battery.",
        "story":
            "In the 2013 TED interview he set it out plainly: reason from "
            "first principles rather than by analogy. Analogy is everyone "
            "does it this way, so we will too. First principles is "
            "boiling a thing down to its most fundamental truths and "
            "reasoning up. His example was batteries. Everyone said a "
            "pack costs six hundred dollars a kilowatt-hour and always "
            "will. ==From first principles: what is a battery made of?== "
            "Cobalt, nickel, aluminium, carbon, polymers, a steel can. "
            "Buy those on the metal exchange and it comes to eighty. The "
            "other five hundred is the price of how they are currently "
            "assembled — and assembly can be reinvented.",
        "f": [
            {"n": "Analogy gives you the market rate, physics gives the floor",
             "d": "It has always cost this and the industry standard both "
                  "quote the price of other people's methods, not the "
                  "cost of the thing. Separate the two: where is the "
                  "floor set by materials and physical law, and who "
                  "collects the gap between that floor and today's price?",
             "eg": "Margins in this kind of service are just thin — take it "
                   "apart: what does delivery actually cost, and how many "
                   "hands take a cut in between? The gap is the opportunity "
                   "list."},
            {"n": "Keep going until you hit something that cannot be reduced",
             "d": "Most attempts stop halfway and treat a supplier quote or "
                  "an industry convention as bedrock. Those are still "
                  "somebody's decisions. The test is whether you can still "
                  "ask why. If you can, you are not at the bottom. The bottom "
                  "feels like a physical law or a published market price.",
             "eg": "Servers are expensive is not bedrock. The market price of "
                   "silicon, electricity and bandwidth is. Stopping at the "
                   "invoice is haggling; going to the floor is rebuilding."},
            {"n": "It is expensive, so spend it where the leverage is",
             "d": "He has said himself that analogy is usually the cheaper "
                  "move, and he is right: reasoning up the whole chain costs "
                  "an enormous amount of attention. The correct use is "
                  "selective — the one or two assumptions that decide whether "
                  "the thing lives. Doing it everywhere means reinventing "
                  "the wheel everywhere.",
             "eg": "Apply it to the cost structure that decides the business "
                   "and buy stationery by analogy. Teams that cannot tell the "
                   "difference exhaust on wheels the attention the rocket "
                   "needed."},
        ],
        "q": [
            "We reason from first principles rather than by analogy.",
            "Boil things down to the most fundamental truths and reason up "
            "from there.",
            "Those materials, bought on the metal exchange, come to about "
            "eighty a kilowatt-hour.",
        ],
        "apply":
            "Where you are: everyone is telling you that some cost or method "
            "simply is what it is.\n"
            "Ask first: what irreducible facts is it made of, and who is "
            "collecting the difference between their sum and today's price?\n"
            "Where it goes wrong: using the phrase as a way of dismissing all "
            "experience, or spending it on things too small to be worth "
            "rebuilding.",
    },
    {
        "k": "idiot-index",
        "n": "Part price over material price",
        "w": "A number that tells you where to start",
        "src": "Isaacson's biography, on the SpaceX costing method",
        "dek": "He gives every component a humiliating score. What it does is "
               "turn a way of thinking into something you can run on a "
               "spreadsheet.",
        "story":
            "Isaacson records a hard metric inside SpaceX: ==the idiot "
            "index — the finished price of a part divided by the cost of "
            "its raw material.== An aluminium part holding a few hundred "
            "dollars of metal, bought for tens of thousands, scores in "
            "the dozens. A score that absurd says what you are paying for "
            "is process and inertia, not physics. The rule follows: a "
            "high index is either explained or made in house. Many Falcon "
            "parts ended up built on site, at a fraction of the industry "
            "price. What makes the index good is that it turns a "
            "judgement call into a list you can sort.",
        "f": [
            {"n": "The index turns judgement into a scanner",
             "d": "First principles depends on someone deciding to think. The "
                  "index makes the candidates queue up on their own: run the "
                  "ratio across every purchased line, sort descending, and "
                  "the rebuild priority list writes itself. The best form a "
                  "method can take is decaying from an insight into a "
                  "division anyone can do.",
             "eg": "Divide each outsourced fee by what doing it in house "
                   "would cost in people and tools. The few at the top of "
                   "that list are the ones to bring back."},
            {"n": "A high score is a toll booth left by history",
             "d": "A part selling at fifty times its metal usually has no "
                  "villain behind it: years of safety margin, layers of "
                  "certification, small batches, a sole supplier. Every "
                  "layer had a reason once; stacked up they are a row of "
                  "toll booths. You do not negotiate those away, you "
                  "route around them.",
             "eg": "Half of an incumbent supplier's quote is paying for a "
                   "process set twenty years ago. What will not come down "
                   "under pressure often goes to zero on a different route."},
            {"n": "Where the score is low, leave it alone",
             "d": "The tool carries its own limit. A part scoring near one is "
                  "already priced against physics; making it yourself will "
                  "not be cheaper, only slower. So it guards against more "
                  "than overpaying — it guards against the compulsion to "
                  "build everything. Vertical integration belongs where the "
                  "index is high, not everywhere.",
             "eg": "Bringing a part scoring thirty in house saves money. "
                   "Bringing one scoring one point two in house trades "
                   "somebody else's scale for your own tuition."},
        ],
        "q": [
            "The idiot index: a part's finished cost over its material "
            "cost.",
            "A ratio that high means you are paying for process and inertia, "
            "not physics.",
            "High index: either explain it, or make it ourselves.",
        ],
        "apply":
            "Where you are: costs will not come down and you cannot see where "
            "to cut.\n"
            "Ask first: divide every line by its underlying material or "
            "compute cost. Who scores highest?\n"
            "Where it goes wrong: bringing everything in house on sight of a "
            "high score without doing your own scale and yield arithmetic, "
            "or using the index as a stick to squeeze suppliers.",
    },
]
