# -*- coding: utf-8 -*-
"""Strategies of the Warring States — English.

Not a work of philosophy and not a chronicle: a collection of persuasions,
recorded close to the ground, in which the argument that worked is preserved
along with what the speaker actually wanted. The English reader expects
another book of ancient wisdom. What this is, is field notes on how people are
moved, and the two chapters here are the two halves of that: what to buy that
cannot be booked, and how to read a compliment.
"""

PARENT = {
    "name": "Strategies of the Warring States",
    "slug": "strategies-of-the-warring-states",
    "blurb": "Deep read",
    "items": [
        {"k": "burning-the-debts", "n": "Burning the bonds",
         "w": "Buying what the ledger cannot hold", "ready": True,
         "line": "He burned the debt contracts and called it a purchase"},
        {"k": "three-mirrors", "n": "Zou Ji at the mirror",
         "w": "Three people praise you, three motives", "ready": True,
         "line": "The better it sounds, the harder you should ask what they want"},
    ],
}

CHAPTERS = [
    {
        "k": "burning-the-debts",
        "n": "Burning the bonds",
        "w": "Buying what the ledger cannot hold",
        "src": "Strategies of the Warring States, Qi IV",
        "dek": "The man sent to collect the debts burned the contracts "
               "instead. This is about how that apparently pure loss was "
               "finally settled.",
        "story":
            "Lord Mengchang sent Feng Xuan to Xue to collect debts, and asked "
            "before he left what he should buy with the proceeds. Whatever "
            "the house is short of, he was told. At Xue, Feng Xuan called the "
            "people together, checked the bonds against them, then announced "
            "a pardon in his lord's name and burned every contract. The "
            "people cheered. Asked what he had bought, he said "
            "righteousness, since the house lacked nothing else. Lord "
            "Mengchang was displeased. A year later, out of office and back "
            "at Xue, he was met a hundred li out by the whole population. "
            "==Today, he said, I see what you bought for me.==",
        "f": [
            {"n": "Some assets are not on the books",
             "d": "A debt is a measurable asset and goodwill is not. What "
                  "Feng Xuan performed was a conversion: a receivable most of "
                  "which was never coming back, exchanged for something "
                  "carried at zero and useful in exactly one kind of moment. "
                  "Whether the trade was right depends on whether you counted "
                  "that moment.",
             "eg": "Over-compensating your earliest users is pure loss in the "
                   "accounts. When a public crisis lands they are the people "
                   "speaking for you, and no budget line buys that."},
            {"n": "You do not choose when it pays out",
             "d": "He was displeased on the spot and understood a year later. "
                  "Spending of this kind shares a shape: the cost is now and "
                  "certain, the return is later and uncertain, and the "
                  "trigger is usually bad news about you. Which is exactly "
                  "why it is the first line cut.",
             "eg": "A customer team looks most redundant while growth is easy "
                   "and proves itself the quarter renewals slip. The cuts "
                   "happen in the first phase."},
            {"n": "Feng Xuan did not ask permission",
             "d": "He acted and reported afterwards, which from another angle "
                  "is exceeding his authority. He could do it because the "
                  "brief he was given was extremely wide: buy whatever the "
                  "house is short of. Wide authority and unforeseen action "
                  "are one thing, not two.",
             "eg": "Say use your judgement and you have accepted a choice you "
                   "would not have made. Taking back control of the detail "
                   "takes that possibility back with it."},
        ],
        "q": [
            "I bought you righteousness. Your house lacked nothing else.",
            "Today I see what you bought for me.",
            "The cost is now and certain. The payout waits for bad news.",
        ],
        "apply":
            "Where you are: a spend that shows no return anywhere in the "
            "accounts.\n"
            "Ask first: what is it actually buying, under what conditions "
            "does it pay out, and are those conditions likely?\n"
            "Where it goes wrong: writing off everything unmeasurable as "
            "waste; and handing out wide authority while still expecting "
            "every step to match what you would have done.",
    },
    {
        "k": "three-mirrors",
        "n": "Zou Ji at the mirror",
        "w": "Three people praise you, three motives",
        "src": "Strategies of the Warring States, Qi I",
        "dek": "Wife, concubine and guest all said he was the handsomer man. "
               "This is about the three different things he heard in one "
               "answer.",
        "story":
            "Zou Ji asked his wife whether he or Xu Gong of the northern city "
            "was the better looking. Far handsomer, she said. His concubine "
            "said Xu Gong was not his equal. The next day a guest said the "
            "same. Then Xu Gong came in person, and Zou Ji judged himself the "
            "lesser man. Lying awake he worked it out: my wife praises me "
            "because she favours me, my concubine because she fears me, my "
            "guest because he wants something. He told the king of Qi, then "
            "applied it to a kingdom of people who favour, fear or want. "
            "==Seen this way, your majesty is very thoroughly screened.==",
        "f": [
            {"n": "One compliment, three different sources",
             "d": "Partiality, fear, want: three motives producing wording "
                  "that is word for word identical, so the sentence itself "
                  "cannot tell them apart. The only way to sort them is the "
                  "structure of the relationship. What someone stands to gain "
                  "from you decides what he says to you.",
             "eg": "Your report says the plan is good, your supplier says the "
                   "plan is good, your investor says the plan is good. Three "
                   "reliabilities, one identical sentence."},
            {"n": "The higher you sit, the fuller the set",
             "d": "Zou Ji's inference is the hard part. He had three people "
                  "and the king had a kingdom. Every step up adds another "
                  "cohort with a reason to praise you and removes people "
                  "willing to say the hard thing. The screening grows with "
                  "the position, with nobody deceiving anybody.",
             "eg": "The more senior you get, the more positive the feedback, "
                   "and the change has nothing to do with your standard. "
                   "Reading it as progress is the usual mistake."},
            {"n": "He calibrated against Xu Gong",
             "d": "He worked it out because Xu Gong actually turned up and "
                  "gave him a reference point uncontaminated by any "
                  "relationship. Without that external ruler, three people "
                  "agreeing is the whole body of evidence. Breaking the "
                  "screen is not a matter of reminding yourself to be humble. "
                  "It is going and finding the comparison.",
             "eg": "Do not ask the team whether the product is good. Look at "
                   "a rival's real numbers, and at what users say when you "
                   "are not in the room."},
        ],
        "q": [
            "My wife favours me, my concubine fears me, my guest wants "
            "something.",
            "Seen this way, the king is very thoroughly screened.",
            "Three people agreeing is not evidence. It is a relationship map.",
        ],
        "apply":
            "Where you are: your plan has come back with unanimous "
            "approval.\n"
            "Ask first: for each person who praised it, what do they stand to "
            "gain or lose from me?\n"
            "Where it goes wrong: treating unanimity as proof of quality; and "
            "never going to find one reference point that owes you nothing.",
    },
]
