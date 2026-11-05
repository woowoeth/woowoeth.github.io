# -*- coding: utf-8 -*-
"""Henry David Thoreau — English.

English readers arrive with a postcard: the man who went to the woods to live simply and
got a book out of it. This page takes the dullest part of Walden, the first chapter,
'Economy', and asks what a person who wants out of the race should do first. Answer:
count. Two chapters: his household ledger, and the arithmetic of a ninety-cent train fare.
"""

PARENT = {
    "name": "Henry David Thoreau",
    "slug": "thoreau",
    "blurb": "Deep read",
    "items": [
        {"k": "count-enough", "n": "Count What Is Enough",
         "w": "Before you try to do less, put your year's costs into a ledger",
         "ready": True,
         "line": "At the pond he logged the house and every meal and fire, and found about six weeks of paid work a year covered it"},
        {"k": "ride-or-walk", "n": "The Ninety-Cent Ticket",
         "w": "The price of a thing is the days of your life you hand over for it",
         "ready": True,
         "line": "A train fare of ninety cents was nearly a day's pay, so he said he would set out on foot and arrive before dark"},
    ],
}

CHAPTERS = [
    {
        "k": "count-enough", "n": "Count What Is Enough",
        "w": "Before you try to do less, put your year's costs into a ledger",
        "src": "Thoreau, Walden, 'Economy'",
        "dek": "He counted first. This asks what to work out before you step back from the race.",
        "story":
            "On 4 July 1845 Thoreau moved into the cabin he had built by Walden Pond. Then he did "
            "what most people who say they want a simpler life never do: he wrote down every "
            "cost. He itemised the boards, nails and bricks of the house, which came to a little "
            "over twenty-eight dollars, and then the food, clothes and fuel. He concluded that "
            "==about six weeks of paid work a year would cover all his expenses==. The rest of the "
            "year he used to read, walk and write.",
        "f": [
            {"n": "Four needs, each written down",
             "d": "He cut necessities down to four, food, shelter, clothing and fuel, and recorded what he actually spent on each. Most people who say they want to spend less are describing a feeling. He ended up holding a number.",
             "eg": "Sort the last three months into food, housing, getting about and utilities, and see which one is the big one."},
            {"n": "The number tells you how long you must work",
             "d": "What had to be bought with labour turned out to be a few weeks of the year. The rest was not idleness. It was the very thing the rest of us work flat out to buy: time of our own.",
             "eg": "Divide your fixed monthly costs by your daily pay and see how many days of work cover them."},
            {"n": "His number is not yours",
             "d": "He lived on land belonging to his friend Emerson, a mile or so outside Concord, and often walked into town to dine with friends. His ledger had conditions. What travels is his habit of keeping it, not his figures.",
             "eg": "Do not say 'Thoreau needed twenty-eight dollars'. Say 'what did my own year actually cost?'"},
        ],
        "q": [
            "To do less, first write the year's costs down.",
            "Whether it is enough is a number, not a feeling.",
            "Borrow his habit of counting, not his figures.",
        ],
        "apply":
            "Where you are: you want to step back from the grind, but fear that once you slow down you will fall behind.\n"
            "Ask first: what does my year really cost, and which parts are things I need versus things I buy so as not to be outdone?\n"
            "Where it goes wrong: reading it as 'the less the better'. He counted to find where enough sits, not to see who could spend least. Once you know it is enough, stop there.",
    },
    {
        "k": "ride-or-walk", "n": "The Ninety-Cent Ticket",
        "w": "The price of a thing is the days of your life you hand over for it",
        "src": "Thoreau, Walden, 'Economy'",
        "dek": "He never said not to ride. This asks how to tell whether a thing is worth it.",
        "story":
            "Thoreau set himself a small sum. Fitchburg is thirty miles from Concord, and the train "
            "fare was ninety cents, nearly a day's pay. He would start now on foot and arrive "
            "before night. You, he said, must first work a day to earn the fare, and "
            "==will get there tomorrow, or tonight if you are lucky==. His rule: \"The cost of a thing is the "
            "amount of what I will call life which is required to be exchanged for it, immediately or "
            "in the long run.\"",
        "f": [
            {"n": "The price is days, not dollars",
             "d": "In his arithmetic a price is not the number on the label. It is the part of your life you give up to get the thing, paid now or paid later. Ninety cents, for him, was a day.",
             "eg": "Before buying a twenty-thousand-dollar machine, work out how many extra days of work it takes to earn it back."},
            {"n": "Both roads on one ruler",
             "d": "He was not telling anyone to walk. He measured walking and riding on the same ruler: the walker spends the day on the road, the rider spends it earning the fare. Each costs a day. The question is which day you would rather have lived.",
             "eg": "Set the hour you save by ordering in against the hour you worked to pay for it."},
            {"n": "Seeing the trade is not refusing every trade",
             "d": "He wanted you to know you were trading, not to decline everything. Some things are worth those days and some are not. You have to weigh them one by one, and he did not do the weighing for you.",
             "eg": "List the three biggest costs this month, note the working days each took, and keep only the ones worth it."},
        ],
        "q": [
            "The price is not on the tag but in the days.",
            "Ask what life it costs before asking whether to buy.",
            "Seeing the trade is not the same as refusing it.",
        ],
        "apply":
            "Where you are: you keep working more and buying more, and the pile grows while you feel emptier.\n"
            "Ask first: how many days of my life does this cost, and am I willing to pay them?\n"
            "Where it goes wrong: reading it as 'buy nothing'. He wanted you to see the exchange, not to decide for you what is worth it. He ate, too.",
    },
]
