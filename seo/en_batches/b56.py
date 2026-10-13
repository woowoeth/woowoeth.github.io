# -*- coding: utf-8 -*-
"""Daily entry: Thorstein Veblen.

Picked by fan-out, on the foreign side (the last three were all Chinese).
'Should I buy this' (10 pieces) is full of the question of whether it is worth
it and whether I understand it; nothing asks whether I am buying it for the
use or for who will see it. 'Someone is ahead of me' has comparison with a
person but nothing on why the line for enough keeps moving with income.
'I don't know what to charge' has price as value and as cost but not price as
signal.

Why he qualifies: founder of institutional economics; the phrase
'conspicuous consumption' is in every economics textbook.

Quoted lines are from The Theory of the Leisure Class (1899), public domain.
Three stories, no overlap: the entry is the seven years on the farm; the
chapters are the skirt and the heel, the ladder and the two spoons.
"""

ENTRIES = [
    {
        "c": "How the world works",
        "n": "Thorstein Veblen",
        "slug": "veblen",
        "e": "USA · 1857–1929",
        "w": "Display", "y": 1857,
        "d": "An American economist born in 1857 on a Norwegian immigrant "
             "farm in Wisconsin, where Norwegian was spoken at home. He took "
             "a PhD in philosophy at Yale in 1884 and later taught at "
             "Chicago, Stanford, Missouri and the New School. He founded "
             "institutional economics, rejecting the lone calculating "
             "individual of the textbooks: wants, he argued, are learned "
             "from habit, institutions and the people around us. "
             "The Theory of the Leisure Class (1899) gave us conspicuous "
             "consumption, conspicuous leisure and pecuniary emulation.",
        "story":
            "In 1884 Veblen had a Yale doctorate in philosophy and no job. "
            "He went back to his parents' farm in Minnesota and stayed for "
            "seven years, mostly reading, with no post and no income. A boy "
            "who grew up speaking Norwegian watched from outside the circle "
            "that cared most about appearances. The first book he wrote "
            "afterwards was about how that circle uses money and idleness "
            "to prove itself to the neighbours.",
        "f": [
            {"n": "People are not calculating machines",
             "d": "He mocked the isolated, cool figure of the textbooks who only weighs gains and losses. To him, what people want and how they spend is learned, bit by bit, from habit and from the people around them; economics should study how habits harden into institutions and change.",
             "eg": "The same income feels like enough in one circle and not nearly enough in another."},
            {"n": "Three terms, one mechanism",
             "d": "Conspicuous consumption, conspicuous leisure and pecuniary emulation are one thing seen three ways: esteem goes to what can be seen, so money has to be shown, idleness has to be shown, and when the neighbour shows, you follow.",
             "eg": "The neighbour's new car and suddenly yours looks old, though it was fine yesterday."},
            {"n": "Making money is not making things",
             "d": "In The Theory of Business Enterprise (1904) he separated business, which looks at prices and profit, from industry, which looks at whether things get made. The two often agree and often do not: to hold a price up, some firms would rather produce less.",
             "eg": "To keep the price from falling, half the stock sits in the warehouse."},
        ],
        "apply": "Take your three largest recent purchases and write one line after each: bought to use, or bought to be seen. Do not edit the answers. Just look at the proportion.",
        "q": [
            "Esteem is given to what can be seen.",
            "The neighbour shows and you follow.",
            "Making money and making things are different jobs.",
        ],
        "l": ["The Wealth of Nations", "John Maynard Keynes", "Robert K. Merton", "Albert O. Hirschman"],
        "contrast": [
            {"n": "The Wealth of Nations", "why": "Both are about buying and selling. Smith has people trading from self-interest, with price as a signal; Veblen adds a kind of trade where the buyer uses the goods to say something about himself, and the price goes home with the goods"},
            {"n": "Robert K. Merton", "why": "Both ask who people measure themselves against. Merton gives the reference group; Veblen notices that most people use the rung just above them, so the yardstick moves up as they do"},
        ],
    },
]

INTROS = {
    "veblen":
        "Founder of institutional economics who coined 'conspicuous "
        "consumption' - his point was that much of what we buy is bought to "
        "be seen, and that where this holds, the price itself can be part of "
        "what is sold",
}

SCENES = [
    ("Should I buy this", "Money", [
        ("Am I buying it for the use, or for who will see it?",
         [("veblen", "conspicuous-consumption")]),
    ]),
    ("Someone is ahead of me", "How you're doing", [
        ("I earn more than before and it still isn't enough.",
         [("veblen", "ideal-just-out-of-reach")]),
    ]),
    ("I don't know what to charge", "Dealing with people", [
        ("I cut my price and fewer people asked.",
         [("veblen", "costliness-as-beauty")]),
    ]),
]

ASKS = {
    "veblen/conspicuous-consumption": "Am I buying it for the use, or for who will see it?",
    "veblen/ideal-just-out-of-reach": "I earn more than before and it still isn't enough.",
    "veblen/costliness-as-beauty": "I cut my price and fewer people asked.",
}

SC_BOX = {
    "Should I buy this":
        "I have half decided already and every reason I find is on my side. "
        "How do I tell what I really want?",
    "I don't know what to charge":
        "I keep quoting low in case they walk. Where do I start working "
        "out a number?",
}

SC_SHORT = {
    "I don't know what to charge": "What to charge",
}
