# -*- coding: utf-8 -*-
"""Thorstein Veblen — English.

English readers know the phrase "conspicuous consumption" and tend to hear it as
a sneer at the rich. This page does the other thing: it takes three passages
from The Theory of the Leisure Class (1899) and turns them on the reader's own
basket, pay rise and price list. The "Veblen effect" is a later name, and the
third chapter says so.

Quoted lines are from the 1899 text (public domain, on Project Gutenberg),
checked against it; everything else is our own wording.
"""

PARENT = {
    "name": "Thorstein Veblen",
    "slug": "veblen",
    "blurb": "Deep read",
    "items": [
        {"k": "conspicuous-consumption", "n": "Who Is It Bought For",
         "w": "Some things are bought to be seen, not to be used",
         "ready": True,
         "line": "He used the long skirt and the high heel as exhibits: made so that the wearer cannot work"},
        {"k": "ideal-just-out-of-reach", "n": "Always Just Out of Reach",
         "w": "The line for enough moves with your income",
         "ready": True,
         "line": "He drew a ladder in which each rung measures itself against the one above"},
        {"k": "costliness-as-beauty", "n": "When the Price Is the Product",
         "w": "For some goods the price is part of what is sold",
         "ready": True,
         "line": "He imagined two silver spoons, one hand-wrought and one machine-made, and what happens when the buyer learns which is which"},
    ],
}

CHAPTERS = [
    {
        "k": "conspicuous-consumption", "n": "Who Is It Bought For",
        "w": "Some things are bought to be seen, not to be used",
        "src": "The Theory of the Leisure Class (1899), chapters 2, 4 and 7",
        "dek": "You have talked yourself into the purchase with three reasons, all about function. Veblen's question is who will see it.",
        "story":
            "In The Theory of the Leisure Class Veblen takes women's fashion "
            "as an exhibit. The long skirt, the corset and the high heel "
            "share one feature: the woman wearing them cannot work in them. "
            "That is exactly what makes them worth having, because each says "
            "something on the wearer's behalf, that she has no need to work. "
            "==The inconvenience is the message.== The same is true of much "
            "else that is costly and gets in the way.",
        "f": [
            {"n": "Wealth has to be shown",
             "d": "In chapter 2 he writes that wealth must be put in evidence, \"for esteem is awarded only on evidence.\" Among neighbours who never see your accounts, what they can judge you by is what you put out where they can see it.",
             "eg": "You move into a new block of flats. Nobody knows your savings; everybody sees the car parked outside."},
            {"n": "Waste is the point",
             "d": "A useful thing invites the suspicion that it was bought to be used. To show you can afford more than use requires, you spend where use ends: needless ornament, labour nobody needs. He called it conspicuous waste, and the waste is itself the message.",
             "eg": "A watch rated to three hundred metres, worn by someone whose deepest swim is the bath."},
            {"n": "Leisure is displayed too",
             "d": "The same reasoning applies to time. Being visibly unproductive, which he named conspicuous leisure, says the person does not have to trade hours for a living.",
             "eg": "The photo of a Wednesday afternoon in a café shows the afternoon off, not the coffee."},
        ],
        "q": [
            "Money must be seen before it earns respect.",
            "The less use it has, the better it proves you can pay.",
            "Would I still buy this if nobody could see it?",
        ],
        "apply":
            "Where you are: something costly sits in the basket and you have found three reasons for it, all about function.\n"
            "Ask first: if no one would ever see that I own it, or what it cost, would I still buy it? Whatever changes is the part you are paying for in other people's eyes.\n"
            "Where it goes wrong: concluding that every expensive thing is vanity. He is measuring the status part of a purchase; the feel of the thing, its durability and the pleasure it gives you are not in his ledger.",
    },
    {
        "k": "ideal-just-out-of-reach", "n": "Always Just Out of Reach",
        "w": "The line for enough moves with your income",
        "src": "The Theory of the Leisure Class (1899), chapters 2 and 5",
        "dek": "You earn more than you used to and the gap is exactly the same. Where does the line for enough come from?",
        "story":
            "Veblen names no family in his book; what he draws is a ladder. "
            "The people on each rung admire and imitate those on the rung "
            "just above, and seldom compare themselves with anyone below. "
            "What the rung above lives like becomes what decency means one "
            "rung down. When the lower rung catches up, the line has already "
            "moved. ==The line always sits a little above where you have "
            "just stood.== Nobody announced it, yet everyone feels it is there.",
        "f": [
            {"n": "The standard is not the average",
             "d": "He wrote that the standard we spend towards is not what has already been achieved but \"an ideal of consumption that lies just beyond our reach.\" Whatever we reach stops being the ideal.",
             "eg": "On fifty thousand a year you eye the life of someone on eighty, not the national average."},
            {"n": "The neighbour stings, the billionaire does not",
             "d": "He observed that each class envies and imitates the class next above it, and rarely measures itself against those far ahead. The very rich do not make you feel poor; the colleague with the new flat does.",
             "eg": "A colleague buys a flat and you notice you have not; a billionaire buys an island and nobody minds."},
            {"n": "A richer country does not fill it",
             "d": "His conclusion is harsher: however wealth is shared out, a general rise in a community's wealth cannot satisfy this need, because it is a contest for rank, not a quantity. A raise for everyone lifts everyone one rung.",
             "eg": "Everyone in the firm gets a grade's raise and nobody feels better off than last year."},
        ],
        "q": [
            "The gap you feel is often someone else's lifestyle.",
            "Everyone rises together and the ranking stays put.",
            "Watching the neighbour costs more than watching the account.",
        ],
        "apply":
            "Where you are: your pay went up and the month-end is as tight as ever, and you suspect you are bad with money.\n"
            "Ask first: whose life is it that I mean by enough? If you can name the person, the line is borrowed, not yours.\n"
            "Where it goes wrong: hearing it as be content and stop striving. He describes how comparison is structured; he does not tell you not to earn more.",
    },
    {
        "k": "costliness-as-beauty", "n": "When the Price Is the Product",
        "w": "For some goods the price is part of what is sold",
        "src": "The Theory of the Leisure Class (1899), chapter 6; Leibenstein, Quarterly Journal of Economics (1950)",
        "dek": "You cut your price and fewer people asked. When does the price itself become part of the thing being bought?",
        "story":
            "Veblen asks us to imagine two silver spoons, one beaten out by "
            "hand, the other pressed by a machine, a close copy. People "
            "pick up the hand-wrought one and find it handsome. Tell them "
            "it came from a machine and the same spoon loses some of its "
            "charm. ==Part of what they liked was that it was not cheap.==",
        "f": [
            {"n": "Costliness passes for beauty",
             "d": "He wrote that much of the pleasure we take in costly things we call beautiful is \"a gratification of our sense of costliness masquerading under the name of beauty.\" The buyer sees the price and reports it as taste.",
             "eg": "In experiments, the same wine described as dearer is rated as tasting better."},
            {"n": "Others gave it a name later",
             "d": "In 1950 the economist Harvey Leibenstein called one version the Veblen effect: some goods are wanted more, not less, as they get dearer. Veblen himself never drew that demand curve; he was writing about display.",
             "eg": "Some luxury brands raise their prices and the queue gets longer."},
            {"n": "First find out what is being bought",
             "d": "If a customer buys for use, a price is a price, and cutting it just makes the thing cheaper. Only when the buyer uses the object to say something about himself does the price go home with the goods. Which kind are your customers?",
             "eg": "A plumber's quote gets haggled over; a handbag's price tag is half of what the buyer is carrying."},
        ],
        "q": [
            "A price cut saves money and may lose the signal.",
            "Part of what they love is that it is not cheap.",
            "Is this bought to use, or to show?",
        ],
        "apply":
            "Where you are: your work is good, you have kept the price low, and fewer people ask.\n"
            "Ask first: do the people who buy this buy its use, or what it lets them show? For the first, a cut is a cut; for the second, the price is part of the goods.\n"
            "Where it goes wrong: raising the price on everything. It holds only for things bought to be seen; for things bought to be used, high is just high.",
    },
]
