# -*- coding: utf-8 -*-
"""Daily entry, day 22: Michael Porter.

Picked by fan-out. 'Do I enter a crowded market' and 'Can't settle on a
price' sit at eight on the Chinese side. What hangs under 'crowded' says
avoid the fight altogether (Thiel), be last and copy well (Duan Yongping), or
wait for the rival to stumble (Guo Jia, Sima Yi). Nothing says what to do if
you must stay in a crowded market, or why getting better than your rivals
leaves the margin thin anyway: Porter's 1996 essay answers exactly that.
Under pricing, nothing asks whether the price is stuck in the middle because
the positioning is.

Recent entries were Chinese, foreign, foreign; this is foreign too, but the
last eight still do not run three of one side, and pick_balance stays green.

Three stories, no overlap: the entry is the 1979 five-forces article; the
chapters are the 1996 essay's convergence puzzle and Southwest versus
Continental Lite. Every situation already exists, so there is no SC_BOX.
"""

ENTRIES = [
    {
        "c": "Starting and building",
        "n": "Michael Porter",
        "slug": "porter",
        "e": "United States · 1947–",
        "w": "Competitive strategy", "y": 1980,
        "d": "American scholar, born in 1947, trained as an economist and "
             "long a professor at Harvard Business School, widely regarded "
             "as the founder of the modern study of competitive strategy. "
             "In 1979 he put the five forces in the Harvard Business "
             "Review, in 1980 he published Competitive Strategy, and in "
             "1996 he wrote \"What Is Strategy?\". He kept asking one "
             "question: in the same industry, some firms always earn well "
             "and others never do, so where is the difference? His answer "
             "was not effort or good management but choosing a different "
             "set of things to do.",
        "story":
            "In 1979 Harvard Business School professor Michael Porter "
            "published an article in the Harvard Business Review titled "
            "\"How Competitive Forces Shape Strategy\". Whether an "
            "industry makes money, he said, does not depend on how "
            "fashionable it looks. It depends on five forces: rivalry "
            "among existing competitors, the threat of new entrants, the "
            "threat of substitutes, the bargaining power of buyers and the "
            "bargaining power of suppliers. He had moved the question from "
            "how well a company is run to whether the industry can pay "
            "anyone at all.",
        "f": [
            {"n": "Look at the industry before the firm",
             "d": "The same effort can earn very different returns in "
                  "different industries. The five forces work as a check-up: "
                  "how fierce the rivals are, how easy it is to enter, "
                  "whether substitutes exist, and how much bargaining power "
                  "buyers and suppliers hold.",
             "eg": "The same coffee shop at the foot of an office block and "
                   "in a residential street faces two different sets of "
                   "rivals, customers and landlords."},
            {"n": "Better is not the same as different",
             "d": "In 1996 he pointed out that quality programmes, "
                  "benchmarking and outsourcing are learned and used by "
                  "everyone. Firms converge on the same best practice, "
                  "grow alike, and the profit thins out together. "
                  "Efficiency is the price of entry, not the way to win.",
             "eg": "Five hotpot places on one street all offer a sauce bar "
                   "and a birthday cake; diners pick whoever has a "
                   "discount today."},
            {"n": "A strategy is a set of activities that fit together",
             "d": "His example was Southwest Airlines: short point-to-point "
                  "routes, no meals, no assigned seats, one aircraft type. "
                  "Each thing it left out lets another work, so a rival "
                  "copying a single piece gets nothing like the same "
                  "result.",
             "eg": "A barber who only visits homes, with no shop and no "
                   "loyalty card, spends all the saved time on the road "
                   "and on the haircut."},
            {"n": "What you refuse is what draws your outline",
             "d": "His line: the essence of strategy is choosing what not "
                  "to do. Continental wanted Southwest's low fares and its "
                  "own full service in one airline, and the same planes and "
                  "staff were pulled two ways. Wanting everything leaves "
                  "you standing out in nothing.",
             "eg": "A restaurant that wants a cheap quick lunch and a "
                   "pricey banquet menu tears its kitchen in half."},
        ],
        "apply":
            "Pick a place where you are competing hard with rivals. On a "
            "sheet, write on the left the things you do that rivals do not, "
            "or do not do in the same way. On the right, write what you "
            "added in the last six months only because rivals had it. If "
            "the left stays empty, you are competing on efficiency. If "
            "the right is full, rivals are leading you around. Then write "
            "a \"what I won't do\" list of at least three. His test is one "
            "question: do not ask how to do it better than the others, "
            "ask how to do it differently from them.",
        "q": [
            "Operational effectiveness is not strategy.",
            "The essence of strategy is choosing what not to do.",
            "Competitive strategy is about being different.",
            "Each extra yes makes you harder to remember.",
        ],
        "l": ["Peter Thiel", "Peter Drucker", "Duan Yongping",
              "The Wealth of Nations"],
        "contrast": [
            {"n": "Peter Thiel",
             "why": "Both are about not being ground down by competition. "
                    "Thiel says build something ten times better and aim "
                    "for a monopoly, because competition is for losers. "
                    "Porter says that inside one industry you can choose a "
                    "different set of activities and hold a different "
                    "position. One tells you to leave the fight; the other "
                    "tells you how to live differently inside it."},
            {"n": "Duan Yongping",
             "why": "Both are about whether to learn from others. Duan "
                    "says dare to be last: let others test the road, then "
                    "do it well. Porter says that if everyone studies the "
                    "same best practice they end up alike and the profit "
                    "thins together. One is about turning what you learn "
                    "into your own; the other is about why learning is not "
                    "enough."},
        ],
    },
]

INTROS = {
    "porter":
        "An American professor at Harvard Business School and the founder of "
        "the modern study of competitive strategy. His most useful idea: "
        "when everyone gets better at the same thing, profit thins "
        "anyway, and real strategy is choosing what not to do",
}

SCENES = [
    ("Winning is costing too much", "Facing an opponent", [
        ("My rivals keep getting better and my margin keeps thinning.",
         [("porter", "better-is-not-different")]),
        ("I copied the best in the field. Why am I still not winning?",
         [("porter", "better-is-not-different")]),
        ("My rivals have it, so do I need it too?",
         [("porter", "what-not-to-do")]),
        ("I can't decide whether to price low or high.",
         [("porter", "what-not-to-do")]),
    ]),
]

ASKS = {
    "porter/better-is-not-different":
        "My rivals keep getting better and my margin keeps thinning.",
    "porter/what-not-to-do":
        "My rivals have it, so do I need it too?",
}
