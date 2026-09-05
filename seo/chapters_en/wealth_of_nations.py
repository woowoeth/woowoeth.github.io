# -*- coding: utf-8 -*-
"""The Wealth of Nations — English.

English readers mostly carry two things out of this book: the invisible hand,
and a general impression that Smith was in favour of selfishness. The hand
appears in the whole book exactly once, in an argument about where merchants
choose to invest, and Smith spends the surrounding pages attacking merchants.
So this page puts the famous sentences back where they were written, with the
conditions Smith attached and the bill he sent himself in Book V.
"""

PARENT = {
    "name": "The Wealth of Nations",
    "slug": "wealth-of-nations",
    "blurb": "Deep read",
    "items": [
        {"k": "not-benevolence", "n": "Not from benevolence",
         "w": "Aim at their interest", "ready": True,
         "line": "Ask for what you need by naming what they get"},
        {"k": "pin-factory", "n": "The pin factory",
         "w": "What division of labour costs", "ready": True,
         "line": "Ten people made forty-eight thousand pins; one alone might make none"},
    ],
}

CHAPTERS = [
    {
        "k": "not-benevolence",
        "n": "Not from benevolence",
        "w": "Aim at their interest",
        "src": "The Wealth of Nations, Book I, chapter 2; Book IV, chapter 2",
        "dek": "The most quoted sentence in economics is about dinner. Read "
               "closely, what it hands you is a protocol for asking.",
        "story":
            "Book I, chapter 2: ==it is not from the benevolence of the "
            "butcher, the brewer, or the baker, that we expect our dinner, "
            "but from their regard to their own interest==. Smith then says "
            "the operative part out loud. We address ourselves not to their "
            "humanity but to their self-love, and never talk to them of our "
            "own necessities but of their advantages. It reads as a verdict "
            "on human selfishness and it is closer to a protocol. If you want "
            "a stranger to act for you dependably, his interest is the only "
            "reliable interface. Goodwill exists; its supply is unsteady and "
            "it does not scale.",
        "f": [
            {"n": "Goodwill is scarce; do not build infrastructure on it",
             "d": "Between friends a favour runs on affection. Cooperation at "
                  "scale cannot: goodwill tires, plays favourites, and moves "
                  "with mood. Smith's observation is that a system built on "
                  "the other side's interest is maintained by every "
                  "participant, while one built on goodwill has to be topped "
                  "up by you.",
             "eg": "Trading on being liked gets a colleague to help you three "
                   "times. Attaching the work to his own targets or his own "
                   "numbers gets it for three years."},
            {"n": "Word order: say what they get first",
             "d": "Never talk of our own necessities but of their advantages "
                  "is a sentence structure you can copy without alteration. "
                  "Most requests open by describing the asker's difficulty, "
                  "which is an application for charity. Open with what the "
                  "other side receives and the same request becomes an offer "
                  "of trade.",
             "eg": "We urgently need your team to schedule this, against once "
                   "this endpoint ships, three of your open tickets close "
                   "themselves. Same request. The second one gets answered "
                   "today."},
            {"n": "The invisible hand appears once, with conditions attached",
             "d": "The phrase occurs once in the entire book, in a passage "
                  "about why merchants invest at home. Self-interest serves "
                  "the public conditionally: Smith's butcher stands in a "
                  "market with competition, law and customers who return. "
                  "Under monopoly or fraud or a one-shot deal, the same "
                  "self-interest points elsewhere.",
             "eg": "Sellers on a marketplace serve you well while reviews "
                   "bite and prices are easy to compare. Switch those two off "
                   "and the same sellers wear a different face."},
        ],
        "q": [
            "It is not from the benevolence of the butcher, the brewer, or "
            "the baker.",
            "We address ourselves not to their humanity but to their "
            "self-love.",
            "Led by an invisible hand to promote an end no part of his "
            "intention.",
        ],
        "apply":
            "Where you are: you need steady cooperation from someone under no "
            "obligation to give it.\n"
            "Ask first: what does this person get when it is done, and can "
            "that sentence go first?\n"
            "Where it goes wrong: turning the interest interface into naked "
            "purchase; or invoking the hand inside a monopoly or a one-shot "
            "deal, where it was never claimed to work.",
    },
    {
        "k": "pin-factory",
        "n": "The pin factory",
        "w": "What division of labour costs",
        "src": "The Wealth of Nations, Book I, chapters 1 to 3; Book V, "
               "chapter 1",
        "dek": "The book opens in a small workshop. This is how the "
               "forty-eight thousand were counted, and what the same author "
               "says they cost.",
        "story":
            "The book's first sentence is not about gold. The greatest "
            "improvement in the productive powers of labour came from the "
            "division of labour, and the evidence is a pin factory. A workman "
            "not trained to the business could scarce, with his utmost "
            "industry, make one pin in a day. Split pin-making into eighteen "
            "operations and ==ten persons could make among them upwards of "
            "forty-eight thousand pins in a day==. Three causes: dexterity, "
            "time no longer lost changing tasks, and machinery invented by "
            "people who do one motion all day. Chapter three adds the "
            "ceiling: the division of labour is limited by the extent of the "
            "market.",
        "f": [
            {"n": "The gain comes from three separate places",
             "d": "Dexterity is bought with repetition, switching cost is "
                  "saved, and machinery is what occurs to somebody who has "
                  "performed the same motion ten thousand times. The third is "
                  "the one that gets forgotten: until the work is cut fine "
                  "enough, there is nothing for automation to take hold of.",
             "eg": "Support as one undivided job can never be automated. Cut "
                   "into triage, lookup and templated reply, the first two "
                   "are on a machine by the second month."},
            {"n": "Market size decides how fine you can cut",
             "d": "The least quoted and most useful chapter says the division "
                  "of labour is limited by the extent of the market: only "
                  "enough volume can keep a full-time specialist fed. "
                  "Widening the market you can reach is therefore not merely "
                  "selling more. It unlocks finer division, and with it lower "
                  "cost.",
             "eg": "One city's volume supports a general repairer. National "
                   "volume supports someone who fixes only one fault. Scale "
                   "comes before specialisation, not after it."},
            {"n": "Smith wrote the bill for it himself",
             "d": "Book V carries the warning: a man whose life is spent "
                  "performing a few simple operations becomes as stupid and "
                  "ignorant as it is possible for a human creature to become. "
                  "The efficiency and the damage are in one book by one "
                  "author. Quoting only chapter one is half the accounting.",
             "eg": "Slice the roles thin enough and the productivity report "
                   "looks superb. Two years on, nobody in those roles has an "
                   "overview or a transferable skill."},
        ],
        "q": [
            "The greatest improvement in the productive powers of labour was "
            "the division of labour.",
            "Ten persons could make among them upwards of forty-eight "
            "thousand pins.",
            "The division of labour is limited by the extent of the market.",
        ],
        "apply":
            "Where you are: you want more output by cutting the work into "
            "steps.\n"
            "Ask first: does current volume feed every specialist the split "
            "creates, and who pays the human side of the bill?\n"
            "Where it goes wrong: splitting before the volume is there, so "
            "every station sits half idle; or counting only the efficiency "
            "and leaving the people on the narrow jobs with no way out.",
    },
]
