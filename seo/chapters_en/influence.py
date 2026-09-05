# -*- coding: utf-8 -*-
"""Influence — English.

The English reader has almost certainly absorbed the six principles second
hand, as a list to be recited, and that is exactly the form in which they are
useless. Both chapters put a principle back on its evidence and then spend
most of their length on the defence, because the book is far better read as
a manual for noticing what is being done to you than as a sales course.
"""

PARENT = {
    "name": "Influence",
    "slug": "influence",
    "blurb": "Deep read",
    "items": [
        {"k": "reciprocity", "n": "Reciprocity",
         "w": "The sense of owing is the lever", "ready": True,
         "line": "The small thing given first moves a return out of all proportion"},
        {"k": "social-proof", "n": "Social proof",
         "w": "When unsure, we watch each other", "ready": True,
         "line": "The less certain you are, the more the crowd decides for you"},
    ],
}

CHAPTERS = [
    {
        "k": "reciprocity",
        "n": "Reciprocity",
        "w": "The sense of owing is the lever",
        "src": "Influence, chapter 2",
        "dek": "Of the six principles he puts this one first. Why the side "
               "that gives first is the side holding the initiative.",
        "story":
            "Cialdini states the rule plainly: we should try to repay, in "
            "kind, what another person has provided us. How deep does it go? "
            "In 1985 Ethiopia, in the middle of poverty, civil war and "
            "famine, sent five thousand dollars to earthquake victims in "
            "Mexico, because Mexico had sent aid when Ethiopia was invaded in "
            "1935. ==The debt had held for fifty years.== The other face of "
            "the rule is that it can be switched on. A flower, a can of Coke, "
            "a free sample, and the return regularly outruns the gift.",
        "f": [
            {"n": "Being in debt does not require your consent",
             "d": "The strongest feature of reciprocity is that the favour "
                  "can arrive uninvited and the obligation still forms. You "
                  "did not ask for the small gift, and having taken it you "
                  "find refusing the request hard. The initiative sits with "
                  "whoever gives first.",
             "eg": "A supplier insists on doing a free first draft. By the "
                   "time you assess the others, the fact that they did it for "
                   "nothing is already voting."},
            {"n": "The return is usually out of proportion",
             "d": "The rule asks for repayment and says nothing about "
                  "matching value, and people overpay to be rid of the "
                  "feeling quickly. In Regan's experiment an unasked-for Coke "
                  "produced raffle ticket purchases worth several times its "
                  "price. The small favour is the cheapest lever here.",
             "eg": "Solving a colleague's ten-minute problem buys more "
                   "long-term cooperation than one large formal favour. Small "
                   "enough to be awkward to ignore, light enough to settle."},
            {"n": "The defence is to reclassify, not to refuse",
             "d": "Cialdini's counter is not to turn gifts down, which costs "
                  "too much socially. It is to relabel: if the favour is a "
                  "sales device then it is not a favour, and the rule stops "
                  "applying. Favours are owed to favours, and tactics are "
                  "owed nothing.",
             "eg": "Take the sample, sit through the free seminar, then ask "
                   "one question at decision time. With the gift removed, "
                   "does this proposal still pass?"},
        ],
        "q": [
            "We should try to repay, in kind, what another person has "
            "provided us.",
            "There is no duty more indispensable than that of returning a "
            "kindness.",
            "An uninvited favour still creates the debt.",
        ],
        "apply":
            "Where you are: you have taken something small from someone and "
            "are about to weigh their proposal.\n"
            "Ask first: if that favour had never happened, what would you "
            "score this proposal?\n"
            "Where it goes wrong: using reciprocity as bare purchase, which "
            "spends itself in one go; or keeping every kindness at the door "
            "so as never to owe anyone anything.",
    },
    {
        "k": "social-proof",
        "n": "Social proof",
        "w": "When unsure, we watch each other",
        "src": "Influence, chapter 4",
        "dek": "Everyone hates canned laughter and everyone laughs more with "
               "it. This is about the conditions that make the principle "
               "strongest.",
        "story":
            "Cialdini's definition: we determine what is correct by finding "
            "out what other people think is correct. Networks keep the laugh "
            "track although audiences say they dislike it, because experiment "
            "after experiment shows it works. But the principle is not "
            "constant, and he names two amplifiers. The first is "
            "==uncertainty== — when we are unsure of ourselves and the "
            "situation is ambiguous, we are readiest to accept the actions of "
            "others as correct. The second is similarity: people read mainly "
            "from people like themselves.",
        "f": [
            {"n": "In an unclear situation, people read each other",
             "d": "When the facts are plain, people look at facts. When they "
                  "are not, people look at each other. The danger is that "
                  "everyone is doing it at once, so a group with no "
                  "information quotes itself into an apparent consensus. "
                  "Newer and murkier makes the loop stronger.",
             "eg": "Industry consensus on a new technology forms in weeks. "
                   "Chase it down and every view traces back to the same two "
                   "articles and to each other."},
            {"n": "Similarity picks the reference group",
             "d": "People do not follow everyone, they follow people like "
                  "themselves. So a case study persuades in proportion to how "
                  "closely its subject resembles the listener, not to how "
                  "impressive it is. A giant's success story is weaker than a "
                  "peer's.",
             "eg": "To move an internal change, use an ordinary team down the "
                   "corridor rather than a famous company. One invites they "
                   "did it, so can we."},
            {"n": "In a crowd, responsibility is divided by the crowd",
             "d": "The bystander effect runs on two layers: everyone reads "
                  "everyone else's stillness as evidence that nothing is "
                  "wrong, and everyone assumes somebody else will act. "
                  "Cialdini's advice to a person in trouble is therefore very "
                  "specific. Single one person out of the crowd.",
             "eg": "You, sir, in the blue jacket, call an ambulance. The "
                   "group email nobody answers gets a reply the day it names "
                   "a person."},
        ],
        "q": [
            "We determine what is correct by finding out what other people "
            "think is correct.",
            "When uncertainty reigns, we accept the actions of others as "
            "correct.",
            "You, sir, in the blue jacket, I need help. Call an ambulance.",
        ],
        "apply":
            "Where you are: you cannot make the call, and you notice you are "
            "checking what everyone else does.\n"
            "Ask first: did these people reach their views independently, or "
            "are they also reading each other?\n"
            "Where it goes wrong: seeing through the principle and then "
            "opposing every consensus on principle; or, when you need "
            "somebody to act, still addressing the room instead of a name.",
    },
]
