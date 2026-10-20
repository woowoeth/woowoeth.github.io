# -*- coding: utf-8 -*-
"""Zichan — English.

The English reader may know the Chinese tradition of statecraft mostly as
stratagem: the clever envoy, the bluff. These two pages are about something
plainer. A small state is leaned on by a great one, twice, and each time the
head of the small state wins by quoting a rule the great state already
accepts, and by working out what a yes today would cost every day after it.

Quoted lines are our own renderings of the Chinese in the Zuo Commentary
(Duke Zhao, years 13 and 16), checked against the Chinese text, not lines
taken from a published translation.
"""

PARENT = {
    "name": "Zichan",
    "slug": "zichan",
    "blurb": "Deep read",
    "items": [
        {"k": "noon-to-dusk", "n": "From Noon to Dusk",
         "w": "When they price you like a big player, find the rule they already accept",
         "ready": True,
         "line": "Jin wanted little Zheng to pay tribute at a duke's rate, and he argued from midday until dark"},
        {"k": "the-pair-of-rings", "n": "The Ring He Would Not Give",
         "w": "When they ask for little, remember that the first yes sets the price of every later one",
         "ready": True,
         "line": "A Jin envoy wanted one jade ring, and he refused, then cited an oath both sides had sworn"},
    ],
}

CHAPTERS = [
    {
        "k": "noon-to-dusk",
        "n": "From Noon to Dusk",
        "w": "When they price you like a big player, find the rule they already accept",
        "src": "Zuo Commentary, Duke Zhao, year 13",
        "dek": "They price you like a big player. How did Zichan, head of a small state, get mighty Jin to lower its tribute?",
        "story":
            "In 529 BC Jin gathered the lords at Pingqiu to swear a covenant, and expected little Zheng "
            "to pay tribute at the rate of a marquis. When the oath was sworn, Zichan spoke up. In the Zhou "
            "system, he said, the higher the rank the heavier the tribute, and Zheng's ruler ranked as a baron. "
            "To make him pay like a marquis was to ask for what he could not supply. He asked Jin to change it. "
            "==He argued from noon until dark, and Jin gave way.==",
        "f": [
            {"n": "Start with the rule they already accept",
             "d": "He did not open with \"we cannot afford it\". He opened with the Zhou schedule Jin itself recognised: "
                  "the higher the rank, the heavier the tribute. Zheng's ruler was a baron, asked to pay like a marquis. "
                  "The hardship came last, in one sentence, as a consequence of that rule.",
             "eg": "Handed a big-client price, you first show the price list they quote to firms your size, then your budget."},
            {"n": "Count the other side's interest too",
             "d": "He did not say only that Zheng was losing. A covenant, he said, exists to keep small states alive; "
                  "tribute without a limit leaves them short, gives offence, and ends them. Which of those it would be "
                  "was being settled that day. He spoke for the covenant's own purpose.",
             "eg": "Haggling over payment terms with a large customer, you say the delay will break their own supply line first, not that you are short of cash."},
            {"n": "Judge when they cannot spare the attention, then outlast them",
             "d": "He argued from noon to dusk, and Jin agreed. Afterwards a colleague feared punishment. Zichan answered "
                  "that Jin's government had many doors and no time for reprisals, and that a state which will not contest "
                  "is trampled anyway. He pressed because he had judged Jin could not turn on him that day.",
             "eg": "The other side is racing another deadline and does not want a fight over your order, so one more round counts for more than usual."},
        ],
        "q": [
            "Covenants are sworn to keep small states alive.",
            "Tribute without limit, and ruin is only a matter of time.",
            "A state that will not contest is trampled all the same.",
        ],
        "apply":
            "Where you are: The other side has priced you like a large player, and you are the smaller one.\n"
            "Ask first: What rule do they already accept, and can I put it on the table before my hardships?\n"
            "Where it goes wrong: Treating it as \"never give way\". It worked because the rule was Jin's own and Jin could not spare "
            "the attention that day; without both, sitting until dark is just stubbornness.",
    },
    {
        "k": "the-pair-of-rings",
        "n": "The Ring He Would Not Give",
        "w": "When they ask for little, remember that the first yes sets the price of every later one",
        "src": "Zuo Commentary, Duke Zhao, year 16",
        "dek": "They want only one small thing. Why did Zichan refuse a jade ring to Jin's Han Xuanzi, and how did the envoy end up withdrawing his own request?",
        "story":
            "Han Xuanzi of Jin, visiting Zheng, owned one of a pair of jade rings; the other was in the hands of a Zheng "
            "merchant. He asked the ruler of Zheng for it, and Zichan refused: it was not state property, and his lord knew "
            "nothing of it. Colleagues urged him to give way rather than offend a great state. Zichan answered that "
            "==a great state's demands never end, so how long could Zheng go on meeting them? Yield once and refuse once, and the offence is worse.==",
        "f": [
            {"n": "Not state property, so not his to give",
             "d": "His first reason was authority, not mood: the ring was not the government's to hand over, and his lord "
                  "did not know of it. When what they ask lies outside what you can give, say where the boundary is. "
                  "It lands better than \"I would rather not\".",
             "eg": "A client asks for another client's contact list; you say the list is not yours to share, not that you would rather not."},
            {"n": "The first price is every later price",
             "d": "His colleagues counted the cost of one ring. Zichan counted the cost of the habit: if visitors from a great "
                  "state get whatever they ask for, how long can that last? A yes followed later by a no offends more "
                  "than a no from the start.",
             "eg": "A client gets one free feature from you in the first quarter; by the next, as far as he is concerned, it is in the contract."},
            {"n": "Quote the oath they both swore, and let them withdraw",
             "d": "Han bought the ring from the merchant, who said he must tell the officials. Zichan cited Zheng's old oath "
                  "with its merchants: we will not seize from you, you will not turn on us. Taking the ring, he said, would "
                  "teach Zheng to break it. Han withdrew.",
             "eg": "The other side wants an exception; you point to the clause they signed themselves, not to how you feel."},
        ],
        "q": [
            "A great state asks without limit. How long can a small one keep giving?",
            "You would not take the jade and lose the lords.",
        ],
        "apply":
            "Where you are: Someone is asking for a small thing that is not yours to give.\n"
            "Ask first: If I give this once, what reason will I have to refuse next time, and is there a rule they have already signed up to?\n"
            "Where it goes wrong: Treating it as \"never yield to the big party\". The ring was not the state's to give, and there was a "
            "mutual oath to cite; without both, refusing is just offending.",
    },
]
