# -*- coding: utf-8 -*-
"""Isaac Newton — English.

English readers arrive with the apple and the laws of motion. This page is about
two other things he did: the way he kept what he could calculate apart from what
he could only guess, and the year he sold South Sea stock at a profit, bought
back in higher, and lost a fortune.

The sums (a few thousand pounds gained in spring, about twenty thousand lost in
all) are the usual figures from Andrew Odlyzko's study of Newton's accounts and
are given as round numbers. The only words of his in quotation marks are the
Motte translation of "Hypotheses non fingo" from the General Scholium (1713).
"""

PARENT = {
    "name": "Isaac Newton",
    "slug": "newton",
    "blurb": "Deep read",
    "items": [
        {"k": "sold-too-early", "n": "Sold Too Early, Bought Back In",
         "w": "What hurts most after a good sale is having sold early",
         "ready": True,
         "line": "In spring he sold at a profit, in summer he watched others keep gaining and bought back a larger stake"},
        {"k": "no-hypotheses", "n": "Can't Say Why, Use It Anyway",
         "w": "Keep what you can calculate apart from what you can guess",
         "ready": True,
         "line": "He gave the formula for gravity, and when asked how it reaches across empty space he said he did not yet know"},
    ],
}

CHAPTERS = [
    {
        "k": "sold-too-early", "n": "Sold Too Early, Bought Back In",
        "w": "What hurts most after a good sale is having sold early",
        "src": "The South Sea Bubble, 1720; Andrew Odlyzko's study of Newton's investments",
        "dek": "I sold and it kept rising. Newton shows why a well-timed sale is what most often sends people back in.",
        "story":
            "In the spring of 1720 Newton sold his South Sea Company stock "
            "and made a few thousand pounds. The price did not stop. All "
            "summer it climbed, and people around him grew rich. He could not "
            "sit still, bought back in, and this time put in more. In the "
            "autumn it collapsed, and ==he lost about twenty thousand pounds "
            "in all==. He was Master of the Mint and had spent his life "
            "doing sums.",
        "f": [
            {"n": "The first sale was right",
             "d": "He got out in spring at a good price, and at the time that was no mistake. The mistake came after: he treated everything the stock rose from then on as money he had left lying on the table.",
             "eg": "You sell the fund at a high, it climbs another twenty per cent, and what you remember is the twenty per cent, not the gain already in your hand."},
            {"n": "Regret pulls the leaver back in",
             "d": "After you sell, every day shows you what you might have made. It hurts more than a loss, because the loss never happened and has nowhere to go, so it goes into buying back.",
             "eg": "You cash out, a friend says over dinner that he has doubled up, and the first thing you do at home is open the account."},
            {"n": "The second stake is often the biggest",
             "d": "Someone who has won once has a success to lean on and thinks the earlier call proved sound, so the second bet is heavier. He mistook one good judgment for a gift for judging.",
             "eg": "The person who got it right once is the one most likely to borrow to buy more. He is not wiser then, only more sure."},
        ],
        "q": [
            "After selling, do not keep the books on the rise.",
            "Going back in needs a new reason, not regret.",
            "After one win, the next stake should be smaller.",
        ],
        "apply":
            "Where you are: you sold, you made money, it has gone up since, and you want back in.\n"
            "Ask first: am I going back because I have seen something new, or because I cannot bear others earning more than me? Which of the reasons I wrote down the day I sold has changed?\n"
            "Where it goes wrong: reading it as never look back after selling. His fault was a bigger bet with no new reason, only regret. With new evidence and a limit set beforehand, going back is not a mistake.",
    },
    {
        "k": "no-hypotheses", "n": "Can't Say Why, Use It Anyway",
        "w": "Keep what you can calculate apart from what you can guess",
        "src": "Principia, second edition (1713), General Scholium",
        "dek": "I only know how it moves. Newton shows what to do when the rule works and the cause is still missing.",
        "story":
            "Newton's law of gravity could give the orbit of the Moon, the "
            "tides and the return of comets, and his critics kept pressing: "
            "how can two bodies far apart pull on each other? No rope, no "
            "collision, nothing in between to carry it. In 1713 he added a "
            "General Scholium to the second edition of the Principia and "
            "answered. He had not yet found the cause of gravity's properties "
            "in the phenomena, ==and he would 'frame no hypotheses'==.",
        "f": [
            {"n": "The rule, and the cause behind it",
             "d": "He kept two things apart. How strong gravity is and how it falls off with distance could be calculated and measured. Why it behaves so was a separate matter. He gave the first in full and left the second empty.",
             "eg": "A doctor sees from the data that a drug works but does not know how. Using it and explaining it are two different questions."},
            {"n": "Whatever was not drawn from the phenomena was a hypothesis",
             "d": "He used the word narrowly. If it was not deduced from observation, he called it a hypothesis, however plausible, and kept it out of his conclusions. You may think it. You may not file it in the same report as the figures.",
             "eg": "You can show sales move with the weather. 'People are in a better mood' is your guess, and in the report it gets a line to itself."},
            {"n": "Do not add a cause you do not need",
             "d": "At the start of the Principia he set out rules of reasoning, and the first is to admit no more causes than are true and enough to explain the thing. The extra one is your taste, not evidence.",
             "eg": "Traffic fell and the data shows two changes you made. Check those two before you start wondering whether the algorithm changed."},
        ],
        "q": [
            "Use the rule now; the cause can wait.",
            "What you calculated and what you guessed need separate columns.",
            "'I do not know yet' is an honest sentence.",
        ],
        "apply":
            "Where you are: you have seen a rule that is useful, people are pressing you for why, and you are tempted to make something up to fill the gap.\n"
            "Ask first: did I calculate this or guess it? Can I write the two in separate columns?\n"
            "Where it goes wrong: reading it as do not act until you know. He kept using the law of gravity without knowing its cause; he simply wrote down that this column was still empty.",
    },
]
