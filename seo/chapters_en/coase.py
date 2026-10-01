# -*- coding: utf-8 -*-
"""Ronald Coase - English.

English readers meet Coase as "the Coase theorem", a phrase he never used and
did not much like. These two pages go back to the questions he actually asked:
why a firm exists at all, and who is harming whom when two uses of one place
collide. Sources: "The Nature of the Firm", Economica, 1937; "The Problem of
Social Cost", Journal of Law and Economics, 1960 (which discusses Sturges v
Bridgman, 1879). Quoted lines are his own wording from those two papers.
"""

PARENT = {
    "name": "Ronald Coase",
    "slug": "coase",
    "blurb": "Deep read",
    "items": [
        {"k": "price-has-a-cost", "n": "Buying is not free",
         "w": "A firm ends where doing it yourself costs the same as buying it",
         "ready": True,
         "line": "Finding, haggling, checking delivery: every step costs "
                 "something"},
        {"k": "harm-goes-both-ways", "n": "Who is really harming whom?",
         "w": "He gets in your way and you get in his; weigh which loss is "
              "heavier",
         "ready": True,
         "line": "The confectioner pounded for twenty years, until a doctor "
                 "built a room"},
    ],
}

CHAPTERS = [
    {
        "k": "price-has-a-cost",
        "n": "Buying is not free",
        "w": "A firm ends where doing it yourself costs the same as buying it",
        "src": "\"The Nature of the Firm\", Economica, 1937",
        "dek": "Do I build this myself or hand it to someone outside? This "
               "page is about the line that is easiest to leave out of that "
               "sum.",
        "story":
            "In 1937 Ronald Coase, then twenty-six, published a paper in "
            "Economica that asked what economists thought needed no asking. "
            "The textbooks said prices coordinate everything. Yet walk into "
            "a factory and nobody haggles: people do what the manager says. "
            "If prices work so well, ==why is there a firm at all==? His "
            "answer was plain. Buying through the market costs something "
            "too: finding who sells, asking prices, settling terms, writing "
            "the contract, checking delivery.",
        "f": [
            {"n": "The quote has more in it than the price",
             "d": "He put it plainly: it is profitable to set up a firm "
                  "because \"there is a cost of using the price mechanism.\" "
                  "The price on the quote is only the part that shows. "
                  "Finding the seller, agreeing terms and chasing delivery "
                  "all take time, and none of it is in the price.",
             "eg": "A photographer quotes five hundred pounds. Comparing "
                   "three, briefing, two rounds of edits and chasing the "
                   "files are not in it."},
            {"n": "A firm turns many deals into one instruction",
             "d": "Rather than negotiate every time, you hire someone and "
                  "buy, through one employment contract, the right to tell "
                  "them what to do for a while. A firm exists because "
                  "directing people inside is cheaper than bargaining "
                  "outside, task by task.",
             "eg": "A standing photographer needs only \"Friday, you're "
                   "on.\" The re-briefing and re-pricing disappear."},
            {"n": "The edge sits where the two costs meet",
             "d": "Inside has costs too: the larger the operation, the "
                  "harder it is for whoever runs it to know what each part "
                  "needs, and the more gets misallocated. So the firm grows, "
                  "he said, until the cost of organising one more "
                  "transaction inside it equals the cost of doing it on the "
                  "open market.",
             "eg": "A support team goes from three people to thirty. Rotas, "
                   "training and management get dearer every month, until "
                   "buying the service looks cheaper."},
            {"n": "The line moves",
             "d": "He pointed out that the telephone and the telegraph cut "
                  "the cost of managing at a distance, and so change how "
                  "big firms get. There is no standing answer to in-house "
                  "or outside. There are two costs, and what each is today.",
             "eg": "With remote tools you can hire a remote employee or buy "
                   "a remote service, and both are cheaper than a decade "
                   "ago."},
        ],
        "q": [
            "Buying through the market is not free.",
            "A firm grows until managing one more thing costs more than "
            "buying it.",
            "The costliest line is the one the quote leaves out.",
        ],
        "apply":
            "Where you are: Deciding whether to build a function yourself, "
            "hire for it, or buy it in.\n"
            "Ask first: Outside, how much effort will I spend finding, "
            "haggling and checking delivery? Inside, what does each extra "
            "head cost in meetings, coordination and waiting for sign-off? "
            "Write both columns.\n"
            "Where it goes wrong: Comparing only the quote with the salary. "
            "The inside costs are on no payslip and the outside costs are "
            "on no quote, so you are comparing two numbers neither of which "
            "has been written down.",
    },
    {
        "k": "harm-goes-both-ways",
        "n": "Who is really harming whom?",
        "w": "He gets in your way and you get in his; weigh which loss is "
             "heavier",
        "src": "\"The Problem of Social Cost\", Journal of Law and "
               "Economics, 1960",
        "dek": "His way of working gets in my way; should I make him stop? "
               "This page is about the half of that question people leave "
               "out.",
        "story":
            "In 1879 an English court heard a case. A confectioner had "
            "pounded ingredients with a mortar and pestle for more than "
            "twenty years and no one had complained. Then the doctor next "
            "door built a consulting room against the confectioner's wall, "
            "and the thumping drowned out his stethoscope. The court ordered "
            "the confectioner to stop. Eighty years on, Coase looked at the "
            "case and saw that ==without the doctor's new room the mortar "
            "harms no one==. The trouble comes from two uses side by side.",
        "f": [
            {"n": "The harm is made by two parties",
             "d": "People assume A harmed B, so A is what needs managing. "
                  "But to spare B you have to harm A. Without the doctor the "
                  "mortar is harmless, and without the mortar the room is "
                  "quiet. The trouble is two uses of the same place.",
             "eg": "A late-night food stall keeps the flat upstairs awake. "
                   "Close the stall, and the owner loses their living."},
            {"n": "Weigh the heavier loss",
             "d": "The real question, he said, is whether A should be "
                  "allowed to harm B or B to harm A. His test is to avoid "
                  "the more serious harm. That means putting both losses on "
                  "one table instead of first deciding who is the culprit.",
             "eg": "Stopping the confectioner costs a twenty-year trade. Not "
                   "building the room costs one room. Which is heavier has "
                   "to be worked out."},
            {"n": "Talking only settles it when talking is cheap",
             "d": "In a world where bargaining costs nothing, he argued, "
                  "the two sides would settle on an arrangement that suits "
                  "both, and who holds the right only decides who pays "
                  "whom. He added at once that in the real world bargaining "
                  "costs money, which is why who holds the right at the "
                  "start matters.",
             "eg": "Two households can settle a shared lane themselves. A "
                   "hundred on one street cannot, and need a rule first."},
        ],
        "q": [
            "We are dealing with a problem of a reciprocal nature.",
            "The problem is to avoid the more serious harm.",
            "Without the new room, the mortar harms no one.",
        ],
        "apply":
            "Where you are: Someone's way of doing things is getting in "
            "your way and you want them to stop, or you have been told to "
            "stop.\n"
            "Ask first: If he stops, what does it cost him? If I carry on, "
            "what does it cost me? Is there an arrangement that leaves both "
            "better off: another time, another place, a payment?\n"
            "Where it goes wrong: Reading this as \"money settles "
            "everything\". He said himself that bargaining is not free, and "
            "some harms cannot be priced. The chapter asks you to lay out "
            "both sides' accounts, not to name a price.",
    },
]
