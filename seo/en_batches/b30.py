# -*- coding: utf-8 -*-
"""Daily entry, day 10: Liu Yan.

Picked by fan-out. Making money work was the emptiest situation on the site,
six pieces: Naval on assets and on productising yourself, Fan Li on stocking
the opposite, The Wealth of Nations on the pin factory, Bai Gui's four
qualifications, Inamori's multiplier. Every one of them answers with what to
own or when to buy. None of them says that the return comes from how often
the capital turns over, and that the first thing you buy is the information
that lets it turn. Liu Yan says exactly that, and paid for it: runners on
salary and relay posts within sight of each other, so prices anywhere reached
him within days.

Chapter two goes to I can't find anyone good, which had a single piece. His
answer is not a better way to judge people. Han Feizi already tells you not
to count on goodness and to rely on law and position; Cao Cao tells you to
take the talent and live with the character. Liu Yan names the specific
device - rank, appraisal, a way up - and says that a capped post makes the
immediate take the only real thing for whoever sits in it.

Both English situations already exist, so there is no SC_BOX here.

Quoted matter is from the Xin Tangshu biography. Three things were checked
against the original because the popular retellings get them wrong, and a
draft from memory would have repeated the errors: the runners are shi zu not
ji zu, the posts were stations within sight not couriers within sight, and
the grain line carried four hundred thousand measures a year, not a million.

Three stories, no overlap: the entry is his death and the inventory of his
house, chapter one is the reporting network, chapter two is handing audit and
cash to ranked officials.
"""

ENTRIES = [
    {
        "c": "Money and risk", "n": "Liu Yan",
        "slug": "liu-yan", "e": "Tang · 716-780",
        "w": "Money flowing on the ground", "y": 764,
        "d": "The financial administrator who rebuilt the revenue of the Tang "
             "after the An Lushan rebellion had emptied it. For nearly twenty "
             "years from 763 he held the commissions for transport, salt and "
             "price stabilisation: he rebuilt the grain line to the capital, "
             "recast the salt monopoly, and held the price of grain and salt "
             "steady in a wrecked economy. The verdict his own history gives him "
             "is that the levies never reached the people and the treasury was "
             "still sufficient. What he left is not a trick for getting rich but "
             "two mechanisms: money grows by turning over, and turnover is "
             "bought with information; and money passes safely through a post "
             "only if that post leads somewhere. He was framed and put to death "
             "in 780.",
        "story":
            "In the seventh month of 780 a palace eunuch reached Zhongzhou with "
            "an order and Liu Yan was put to death at sixty-five; the formal "
            "decree followed nineteen days later. Someone proposed confiscating "
            "his estate. The council refused, but the inventory had already been "
            "taken: two cartloads of assorted books, a few measures of rice and "
            "wheat. That was the household of a man who had handled the revenue "
            "of an empire for twenty years. The history also keeps his working "
            "day - at the office by first light, still at it near midnight, "
            "holidays included, doing sums with his riding crop on the way to "
            "court.",
        "f": [
            {"n": "His first outlay bought no goods",
             "d": "At each circuit office he recruited fast runners and set relay "
                  "posts within sight of one another, so that what prices were "
                  "doing anywhere, however distant, reached him within days. Those "
                  "men produced nothing; they only shortened the gap between a "
                  "price moving and him knowing.",
             "eg": "The subscription or the extra pair of hands that looks like "
                   "pure overhead is often what lets the capital move at all."},
            {"n": "When it would not turn, he turned it into something else",
             "d": "Goods from the far southern hills cost more to carry than they "
                  "fetched. Rather than wait for prices to recover he stored them "
                  "in the Huai valley, traded them for copper and firewood, and "
                  "minted a hundred thousand strings of coin a year.",
             "eg": "With stock you cannot shift, the question is not when it will "
                   "recover but what it can become today."},
            {"n": "He sold off the last stretch of road",
             "d": "Salt was not carried to every county. The state bought at the "
                  "works, added its margin and sold on to merchants, who took the "
                  "carriage and the selling. Revenue rose tenfold and nobody "
                  "complained of a new burden.",
             "eg": "Owning the whole chain gets you stuck at the last mile; hand "
                   "that stretch to someone who wants to run it."},
            {"n": "The step closest to the money went to people who could lose",
             "d": "Audit and disbursement were handed to ranked officials who drew "
                  "salaries and could be promoted, while the career clerks were "
                  "left the paperwork. No clerk was dismissed. What changed was "
                  "not the staff list but which step belonged to whom.",
             "eg": "When a post ruins three people in a row, do not reach for a "
                   "fourth; move the step nearest the money instead."},
            {"n": "For the well-connected, a title and no work",
             "d": "When the powerful pressed him to place their people he paid "
                  "them handsomely from the salary budget and never let them near "
                  "the business. The result his history records is that everyone "
                  "else applied themselves, the real posts plainly not going to "
                  "whoever had a word put in.",
             "eg": "For the favour you cannot refuse, give the title in full and "
                   "take the real authority away."},
        ],
        "apply":
            "If your money holds but will not grow, do not start by hunting for "
            "something to buy. Count the days between a price moving and you "
            "hearing of it, then ask whether money can shorten them. His first "
            "outlay bought the reporting network, not goods; without it, moving "
            "faster only loses faster. And if what troubles you is money going "
            "wrong in somebody's hands, do not reach for a fourth person. Look "
            "at whether the post leads anywhere: in a post that leads nowhere, "
            "keeping the rules buys nothing, and you are asking that person to "
            "weigh a reputation they have no use for against what is in front of "
            "them. Move the step closest to the money to someone who has "
            "something to lose.",
        "q": [
            "It was like watching money flow across the ground.",
            "The levies never reached the people, and the treasury sufficed.",
            "A man with rank values his name above the immediate gain.",
            "Only Yan could work it, and no one else.",
        ],
        "l": ["Bai Gui", "Fan Li", "Guan Zhong", "Zhang Juzheng", "Han Feizi"],
        "contrast": [
            {"n": "Bai Gui",
             "why": "Two routes to making money work: Bai Gui buys what others "
                    "discard and earns the spread on a single trade, while Liu "
                    "Yan pays for a reporting network to know days earlier, "
                    "earns the number of turns, and wants the spread closed"},
            {"n": "Han Feizi",
             "why": "Neither counts on people being good: Han Feizi says do not "
                    "rely on their goodness and rely on law and position instead, "
                    "while Liu Yan names the particular device - rank and a way "
                    "up - that makes keeping the rules pay in that seat"},
        ],
    },
]

INTROS = {
    "liu-yan": "Tang administrator who ran the revenue of a wrecked empire for "
               "twenty years, paying for runners so he knew prices first, and "
               "giving the jobs that touched money to people who could be "
               "promoted",
}

SCENES = [
    ("Making money work", "Money", [
        ("My money turns over far too slowly.",
         [("liu-yan", "money-flows-on-the-ground")]),
    ]),
    ("I can't find anyone good", "Leading people", [
        ("I replaced the person and the post is still rotten.",
         [("liu-yan", "rank-outweighs-profit")]),
    ]),
]

ASKS = {
    "liu-yan/money-flows-on-the-ground":
        "My money turns over far too slowly.",
    "liu-yan/rank-outweighs-profit":
        "I replaced the person and the post is still rotten.",
}
