# -*- coding: utf-8 -*-
"""Daily entry: Henry Ford.

From DAILY_QUEUE.md row 11. 'I don't know what to charge' holds entries on pricing high, pricing as
abundance, and knowing what a thing should cost. None of them says the price can be set first and the
costs made to follow. The second chapter is hung on 'Everyone says it can't be done cheaper': the
five-dollar day, which Ford described as a cost-cutting move.

Why he qualifies: founder of the Ford Motor Company, whose Model T and moving assembly line (1913) made
mass production the model for manufacturing.

The entry story is the 1909 decision to build only the Model T; the chapters are the price table and
the five-dollar day. Only his production, pricing and wages are used here, not his politics.
"""

ENTRIES = [
    {
        "c": "Starting and building",
        "n": "Henry Ford",
        "slug": "henry-ford",
        "e": "United States · 1863–1947",
        "w": "Price", "y": 1913,
        "d": "Founder of the Ford Motor Company. He launched the Model T in 1908 and from 1913 ran a moving "
             "assembly line at Highland Park, turning the car from a rich man's luxury into something ordinary "
             "families could buy and making mass production the template for manufacturing. His method was to "
             "set the price where far more people could pay, then force production to meet it. He is here for "
             "'I don't know what to charge', where nothing yet says the price can come first and the costs follow.",
        "story":
            "One morning in 1909, without warning anyone, Ford announced that from then on the company would build "
            "a single model, the Model T, on one chassis for every car. He added that a customer could have any colour "
            "he liked so long as it was black. Nobody agreed with him, he later wrote. The salesmen could not see what "
            "one model would do for production, and they were sure a lower price would hurt sales by driving away the "
            "buyers who wanted quality.",
        "f": [
            {"n": "One model pays off in the factory",
             "d": "The salesmen wanted to cater to every customer's taste. He was thinking about the shop floor: with one chassis, every machine, part and movement could be arranged for a single car and made as cheap as possible.",
             "eg": "Before cutting a product line down to one, work out what that one would save in production."},
            {"n": "He bought every new car and took it apart",
             "d": "If anyone had something better, he wrote, he wanted to know. So the company bought one of every new car on the market, drove it for a while, road-tested it, then took it apart to see how and of what it was made.",
             "eg": "When a rival launches, buy one and strip it to the last screw. It teaches more than ten reviews."},
            {"n": "The biggest success is the hardest to drop",
             "d": "The Model T ran until 1927, more than fifteen million cars, with the price cut again and again while the car changed little. When it finally ended, the plants stopped for months to retool, and that year Chevrolet outsold Ford.",
             "eg": "With a product that has sold for ten years, the question to ask is whether customers still want the same thing."},
        ],
        "apply": "This week take your main product and write down two numbers: what customers will pay for it, and the "
                 "price your current costs produce. However wide the gap, list the parts of the process you would have to change.",
        "q": [
            "He set the price, then made the factory reach it.",
            "One model pays off on the shop floor.",
            "The biggest success is the hardest to drop.",
        ],
        "l": ["Taiichi Ohno", "Konosuke Matsushita", "Elon Musk"],
        "contrast": [
            {"n": "Thorstein Veblen", "why": "Veblen saw people want a thing more because it is expensive, so the price itself is the reason to buy. Ford bet on the other end: make the car cheap enough for ordinary families and so many will buy that the costs come down. One explains why the rich buy dear; the other how to let everyone else buy at all."},
        ],
    },
]

INTROS = {
    "henry-ford":
        "Founder of Ford Motor - he cut the Model T from $950 to $360 in eight seasons, said the price cut always "
        "came first and the costs had to follow, and called the five-dollar day a way of saving money",
}

SCENES = [
    ("I don't know what to charge", "Dealing with people", [
        ("Once I add up my costs, my price is too high to sell.",
         [("henry-ford", "price-first")]),
    ]),
    ("Everyone says it can't be done cheaper", "Getting it done", [
        ("People keep leaving. How do I bring costs down?",
         [("henry-ford", "five-dollar-day")]),
    ]),
]

ASKS = {
    "henry-ford/price-first": "Once I add up my costs, my price is too high to sell.",
    "henry-ford/five-dollar-day": "People keep leaving. How do I bring costs down?",
}
