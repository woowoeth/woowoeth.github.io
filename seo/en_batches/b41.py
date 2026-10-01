# -*- coding: utf-8 -*-
"""Daily entry, day 21: Ronald Coase.

Picked by fan-out. 'Do we expand' and 'Costs won't come down' sit at eight
and ten on the Chinese side. What hangs under 'expand' says what to do and
not do (Wang Xing), what will not change (Bezos), how to feed a bigger
operation (Cao Cao); nothing says where the boundary of a firm falls, that
is, when to build the thing yourself and when to buy it in. Coase's 1937
paper answers exactly that. Under 'It turned into a fight' nothing asks who is
harming whom in the first place.

Recent entries were Chinese, Chinese, foreign; this one is foreign, and
pick_balance stays green.

Three stories, no overlap: the entry is the 1960 Chicago dinner; the chapters
are the 1937 question and the 1879 confectioner. Every situation already
exists, so there is no SC_BOX.
"""

ENTRIES = [
    {
        "c": "How the world works",
        "n": "Ronald Coase",
        "slug": "coase",
        "e": "Britain · 1910–2013",
        "w": "Transaction costs", "y": 1937,
        "d": "British economist, born in London in 1910, who moved to the "
             "United States, taught at the University of Chicago until he "
             "retired in 1982, won the Nobel Prize in Economics in 1991 and "
             "died in 2013 aged 102. Most of his fame rests on two papers, "
             "one from 1937 when he was twenty-six and one from 1960. Each "
             "asked something other economists thought needed no asking: if "
             "prices coordinate everything, why is there a firm? when one "
             "person's activity gets in another's way, is he really the one "
             "to restrain? The answer to both was the same: buying and "
             "selling through the market is not free.",
        "story":
            "By Coase's own later account, in 1960 he sat in Aaron "
            "Director's house in Chicago with a roomful of economists "
            "pressing him on the paper he had just written about social "
            "cost. By the standard teaching of the day, if a person's "
            "activity harms others, you restrain him or tax him; it was "
            "close to common sense. Coase took the objections one at a "
            "time. By the end of the evening, he recalled, nobody in the "
            "room was still arguing.",
        "f": [
            {"n": "Dealing is not free",
             "d": "The price is only the part of the cost that shows. "
                  "Finding the seller, asking prices, agreeing terms, "
                  "writing the contract and checking delivery all cost "
                  "something. He called it the cost of using the price "
                  "mechanism; it was later named transaction cost.",
             "eg": "A photographer quoted at five hundred pounds: three "
                   "days comparing, two rounds of briefing, and chasing the "
                   "files at the end."},
            {"n": "A firm stops where the two costs meet",
             "d": "He explained why firms exist: directing people inside is "
                  "cheaper than bargaining outside. A firm grows until "
                  "organising one more thing inside costs as much as doing "
                  "it on the open market.",
             "eg": "A support team grows from three to thirty; rotas and "
                   "training get dearer until outsourcing becomes the "
                   "cheaper line."},
            {"n": "The harm is made by two parties",
             "d": "In 1960 he argued that to spare B you must harm A. The "
                  "confectioner's mortar harmed no one until the doctor "
                  "built his room. What has to be weighed is which loss is "
                  "the heavier.",
             "eg": "A food stall keeps the neighbours awake; closing it "
                   "takes the owner's living."},
            {"n": "Bargaining must be affordable first",
             "d": "In a world where bargaining is free, the two sides "
                  "settle on their own. In the real world finding each "
                  "other, haggling and enforcing the deal all cost money, "
                  "which is why who holds the right at the start matters.",
             "eg": "Two households can settle a shared lane. A hundred on "
                   "one street cannot, and need a rule first."},
        ],
        "apply":
            "Pick something you are weighing: build it yourself or buy it "
            "in. On a sheet, write on the left what the outside route costs "
            "you in finding, haggling and checking, and on the right what "
            "each extra person adds in meetings, coordination and waiting "
            "for approval. Do not stop at the quote and the salary; both "
            "are already written down. If you are stuck in a dispute where "
            "two things get in each other's way, make two columns as well: "
            "what it costs him if he stops, what it costs me if I carry on, "
            "and whether there is an arrangement that leaves both better "
            "off.",
        "q": [
            "Buying through the market is not free.",
            "A firm grows until managing one more thing costs more than "
            "buying it.",
            "We are dealing with a problem of a reciprocal nature.",
            "The problem is to avoid the more serious harm.",
        ],
        "l": ["The Wealth of Nations", "Friedrich Hayek",
              "C. Northcote Parkinson", "Wang Xing"],
        "contrast": [
            {"n": "Friedrich Hayek",
             "why": "Both are about prices. Hayek says the price system "
                    "carries knowledge scattered across millions of heads, "
                    "and nothing coordinates better. Coase asks why, if "
                    "prices are that good, people inside a firm do what the "
                    "manager says instead. One is about what prices can "
                    "do; the other is about what using them costs."},
            {"n": "C. Northcote Parkinson",
             "why": "Both are about organisations getting bigger. Parkinson "
                    "says a bureaucracy grows whatever the work, filled "
                    "with people making work for each other. Coase says a "
                    "firm should stop growing where managing one more thing "
                    "inside costs more than buying it outside. One asks why "
                    "organisations will not stop; the other asks where they "
                    "should."},
        ],
    },
]

INTROS = {
    "coase":
        "A British economist and 1991 Nobel laureate who asked two "
        "questions other economists thought needed no asking: if prices "
        "coordinate everything, why is there a firm, and when one person "
        "gets in another's way, is he really the one to restrain? Both "
        "answers come to the same thing: buying and selling is not free",
}

SCENES = [
    ("Everyone says it can't be done cheaper", "Getting it done", [
        ("Do I build this team myself or outsource it?",
         [("coase", "price-has-a-cost")]),
        ("Outsourcing looks cheaper. How do I work that out?",
         [("coase", "price-has-a-cost")]),
    ]),
    ("It turned into a fight", "Making a call", [
        ("He's in my way. Do I make him stop?",
         [("coase", "harm-goes-both-ways")]),
    ]),
]

ASKS = {
    "coase/price-has-a-cost":
        "Do I build this team myself or outsource it?",
    "coase/harm-goes-both-ways":
        "He's in my way. Do I make him stop?",
}
