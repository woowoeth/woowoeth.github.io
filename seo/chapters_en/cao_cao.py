# -*- coding: utf-8 -*-
"""Cao Cao — English.

The English reader who has met him at all met him through the novel, as the
villain. The historical record is stranger and more useful: a man who put in
writing that he would hire on ability with no examination of character, who
grew his own grain while everyone else seized theirs, and who burned the
evidence of his own officers hedging against him rather than read it.
"""

PARENT = {
    "name": "Cao Cao",
    "slug": "cao-cao",
    "blurb": "Deep read",
    "items": [
        {"k": "talent-only", "n": "Ability only, character not examined",
         "w": "One test, and it is a hard one", "ready": True,
         "line": "When you are short of people, keep the criteria few and hard"},
        {"k": "military-farming", "n": "Grow the grain yourself",
         "w": "Fix your own supply first", "ready": True,
         "line": "While the others seized grain, he was in the fields planting it"},
        {"k": "burning-the-letters", "n": "Burning the letters at Guandu",
         "w": "Some accounts must not be settled", "ready": True,
         "line": "Establish who did it and you lose half the people you need"},
    ],
}

CHAPTERS = [
    {
        "k": "talent-only",
        "n": "Ability only, character not examined",
        "w": "One test, and it is a hard one",
        "src": "The Order Seeking the Worthy, 210",
        "dek": "He announced in public that he would look at ability and not "
               "at conduct. Under what conditions that extreme rule holds.",
        "story":
            "In 210 he issued the Order Seeking the Worthy. He opens with a "
            "counter-example: if only men of blameless conduct could be "
            "employed, how did Duke Huan of Qi ever become hegemon? Guan Zhong "
            "had once shot an arrow at him. Then he takes it all the way — "
            "the realm is not yet settled, this is precisely the hour of "
            "urgent need, so bring me the men of low birth and poor "
            "reputation who can govern and command: ==put forward ability "
            "alone, and I will use it.== In the moral climate of the time "
            "this was scandalous.",
        "f": [
            {"n": "Few criteria, or you never choose quickly",
             "d": "What a long list of requirements actually does is strain "
                  "out everyone with an edge and leave the people who are "
                  "adequate at everything and outstanding at nothing. Cutting "
                  "to one criterion admits that in fast expansion, one person "
                  "who can carry the load beats three with no weaknesses.",
             "eg": "The job posting listed eight requirements and everyone "
                   "hired scored a pass on all eight. The one capability "
                   "actually wanted got squeezed out by the other seven."},
            {"n": "The rule comes with an expiry date",
             "d": "He wrote the precondition into the order himself: the "
                  "realm is not yet settled, this is the hour of urgent need. "
                  "Disorder wants ability; settled times want order. He ran "
                  "this rule during expansion while backing it with severe "
                  "military law — not examining character assumes something "
                  "else governs behaviour.",
             "eg": "Hiring someone brilliant and hard to work with is fine "
                   "early on, provided the boundaries are explicit and "
                   "correction is fast. Loosening the bar with no backstop is "
                   "gambling with the organisation."},
            {"n": "Say it with no room left to retreat",
             "d": "The wording of the order is deliberately extreme. He was "
                  "not after precision; he was breaking the habit of choosing "
                  "men by reputation. A moderate phrasing gets absorbed by "
                  "the existing filter and changes nothing. Overturning a "
                  "deep default takes an oversized signal.",
             "eg": "To end promotion by seniority, saying we also value "
                   "ability does nothing. Promote the most junior person on "
                   "the team and everyone understands by lunchtime."},
        ],
        "q": [
            "If only blameless men could serve, how did Duke Huan rule?",
            "Put forward ability alone, and I will use it.",
            "The realm is not yet settled. This is the urgent hour.",
        ],
        "apply":
            "Where you are: you are hiring or promoting and the list of "
            "criteria runs long.\n"
            "Ask first: which single one of these does this seat genuinely "
            "require? Can the rest stop being filters?\n"
            "Where it goes wrong: loosening the conduct bar without setting "
            "behavioural boundaries; trying to overturn a hardened default "
            "with careful, moderate language.",
    },
    {
        "k": "military-farming",
        "n": "Grow the grain yourself",
        "w": "Fix your own supply first",
        "src": "The Order Establishing Agricultural Colonies, 196; Records of "
               "the Three Kingdoms",
        "dek": "The same collapse, and every warlord was seizing food. What "
               "he did instead was the thing nobody else had patience for.",
        "story":
            "In 196 the central plain was in chaos and the armies fed "
            "themselves by plunder. Yuan Shao's men in Hebei lived on "
            "mulberries; Yuan Shu's troops on the Huai lived on water snails; "
            "when the grain ran out the army dispersed. On Zao Zhi's advice, "
            "Cao Cao settled farmers on garrison land around Xu and took a "
            "million bushels that first year. His stated reason was one "
            "sentence: ==the method of settling a state lies in a strong army "
            "and sufficient food.== He then put agricultural officers in "
            "every province, and the granaries filled.",
        "f": [
            {"n": "Plunder is fast and it does not last",
             "d": "Seizing grain feeds you today; sowing it means waiting a "
                  "season. Every force living off plunder met the same end — "
                  "the grain ran out and the army dispersed. Whether an "
                  "outfit is earning or burning down a stock comes to one "
                  "test: is the supply produced or drawn down?",
             "eg": "Growth on continuous funding and subsidy, and growth on "
                   "gross margin, can look identical for a while. Close the "
                   "funding window and the first one disperses that month."},
            {"n": "Your supply line has to grow on your own ground",
             "d": "The point of the farming colonies was not agriculture. It "
                  "was moving army grain from asking others to producing it. "
                  "Any lifeline that depends on outside supply is a switch in "
                  "someone else's hand. Internalising it is expensive, and it "
                  "is the only solution there is.",
             "eg": "If every customer arrives through one platform's traffic, "
                   "no amount of skill at buying that traffic puts the "
                   "lifeline in your hands. Owned channels are slower, and "
                   "they are the granary."},
            {"n": "Planting while everyone else grabs takes nerve",
             "d": "The first year of a farming colony produces nothing while "
                  "rivals expand on what they seize. The difficulty is not "
                  "technical; it is holding steady through the year in which "
                  "you are visibly behind. Every long-cycle advantage has a "
                  "stretch like that in it.",
             "eg": "While a rival buys share with heavy spending, you work on "
                   "retention. Two quarters of ugly numbers, and whether you "
                   "survive them decides who is standing in year three."},
        ],
        "q": [
            "Settling a state lies in a strong army and sufficient food.",
            "When the grain ran out, the army simply dispersed.",
            "A supply line someone else can switch off is not yours.",
        ],
        "apply":
            "Where you are: to catch up, you are considering the fastest "
            "available way to get resources.\n"
            "Ask first: did this supply line grow on my own ground, or can "
            "someone else close it at will?\n"
            "Where it goes wrong: counting drawdown as growth; letting "
            "short-term numbers turn you around in the year you were supposed "
            "to endure.",
    },
    {
        "k": "burning-the-letters",
        "n": "Burning the letters at Guandu",
        "w": "Some accounts must not be settled",
        "src": "Records of the Three Kingdoms, with Pei Songzhi's citation of "
               "the Spring and Autumn of Wei",
        "dek": "A stack of evidence in hand, enough to name everyone who "
               "hedged against you. Why he burned it in front of everybody.",
        "story":
            "After the victory at Guandu his men found a bundle of letters in "
            "Yuan Shao's camp: secret correspondence from his own officials "
            "at Xu and his own commanders, written before the battle, "
            "arranging somewhere to land if he lost. His staff proposed "
            "checking every name and arresting them all. He did not look. He "
            "ordered the letters burned in the open, and said: ==when Shao "
            "was strong, even I could not be sure of surviving — how much "
            "less everyone else.== The letters went, the matter ended, and "
            "not one man was pursued.",
        "f": [
            {"n": "Establishing the facts costs you half your people",
             "d": "With the evidence in hand, pursuing it is the natural next "
                  "move. But those names are the same people who just won the "
                  "battle. Following it through is unanswerable in logic and "
                  "dismantles your own organisation in fact. Some accounts "
                  "can be settled and must not be.",
             "eg": "Investigate one incident to the bottom and assign blame "
                   "to everyone involved, and nobody reports the second one. "
                   "What you learn is worth far less than the channel you "
                   "close."},
            {"n": "Supply the reason on their behalf",
             "d": "His line was not I am magnanimous. It was that at the time "
                  "even he was unsure he would live. He attributed the "
                  "wavering to the situation rather than to character, which "
                  "let every one of them keep their face. That sentence "
                  "turned a pardon into a shared account.",
             "eg": "Someone wavered during the bad stretch. Saying nobody "
                   "could read it back then works far better than saying I "
                   "forgive you, which is still keeping score."},
            {"n": "It is over only once it is destroyed",
             "d": "The decisive act is not declining to pursue; it is "
                  "destroying the evidence publicly. Keeping it unused means "
                  "everyone knows the list is still with you, and that state "
                  "drains people more than an investigation would. For a "
                  "thing to be over, the proof has to physically stop "
                  "existing.",
             "eg": "You said it was finished, and the records from that time "
                   "are still in your folder. Everyone can feel that file "
                   "sitting there, and trust does not come back."},
        ],
        "q": [
            "When Shao was strong, even I could not be sure.",
            "Some accounts can be settled and must not be.",
            "Kept but unused, the list drains more than the investigation "
            "would.",
        ],
        "apply":
            "Where you are: something is over, and you are holding the "
            "evidence of who did what.\n"
            "Ask first: what does establishing it get me? Do I still need the "
            "people I would lose?\n"
            "Where it goes wrong: treating accountability as a process that "
            "has to be completed; saying it is finished while keeping the "
            "file.",
    },
]
