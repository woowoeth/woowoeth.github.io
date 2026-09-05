# -*- coding: utf-8 -*-
"""Benjamin Graham — English.

Most English readers meet Graham second-hand, through Buffett, and meet Mr.
Market as a poster about staying calm. Both chapters here go after the fine
print instead: the parable is a claim about who holds the initiative, and the
margin of safety is priced off how little you trust your own arithmetic.
Not Paul Graham, who has his own pages on this site.
"""

PARENT = {
    "name": "Benjamin Graham",
    "slug": "graham",
    "blurb": "Deep read",
    "items": [
        {"k": "mr-market", "n": "Mr. Market",
         "w": "A quote is a service, not a verdict", "ready": True,
         "line": "He does not mind being ignored, and he comes back tomorrow"},
        {"k": "margin-of-safety", "n": "The margin of safety",
         "w": "The room you leave for being wrong", "ready": True,
         "line": "Three words, and what they buy is surviving your own error"},
    ],
}

CHAPTERS = [
    {
        "k": "mr-market",
        "n": "Mr. Market",
        "w": "A quote is a service, not a verdict",
        "src": "The Intelligent Investor, chapter 8",
        "dek": "He turns the entire market into one manic-depressive business "
               "partner. What that story actually unlocks is smaller and "
               "stranger than it looks.",
        "story":
            "Chapter eight asks you to imagine a partner in a private "
            "business. His name is Mr. Market and he turns up every single "
            "day with a price, ready to buy your share or sell you his. His "
            "moods are extreme: elated, he names an absurd figure; depressed, "
            "he sells everything cheap. ==The part that matters comes next. "
            "He does not mind being ignored, and he is back tomorrow with a "
            "new quotation.== Which makes him useful in proportion to how "
            "unstable he is, provided you use his prices rather than catch "
            "his mood.",
        "f": [
            {"n": "A quote is an option, not a grade",
             "d": "Most people read the tape as a live score on their own "
                  "judgement, so a fall means they were wrong. The parable "
                  "separates the two. A price is one man's mood today, and "
                  "you have three responses: buy from him, sell to him, or "
                  "ignore him. The third is where the initiative lives.",
             "eg": "Down twenty per cent, ask what changed: the business, or "
                   "the quotation? If the business is intact, that was a "
                   "mood, and moods come back tomorrow."},
            {"n": "Volatility is the service you are not charged for",
             "d": "An emotional partner is not the risk; he is the only "
                  "source of your return. Without his depressions nothing is "
                  "ever cheap, and without his manias nothing is ever dear. "
                  "Complaining about swings is complaining that your one "
                  "supplier keeps turning up for work.",
             "eg": "In the same fund, the holder who treats a drawdown as a "
                   "disaster sells at the low to the holder who treats it as "
                   "a delivery window."},
            {"n": "Do not let him do your valuation",
             "d": "The discipline sits in the fine print. Using his prices "
                  "requires a valuation of your own, or you cannot tell a "
                  "bargain from a trap and contrarianism decays into reflex. "
                  "Whether he is servant or master depends on whether you "
                  "brought your own ruler.",
             "eg": "It has fallen this far, it must be oversold is not a "
                   "valuation. It is measuring today's quotation against "
                   "yesterday's quotation."},
        ],
        "q": [
            "One of your partners, named Mr. Market, is very obliging indeed.",
            "He is back again tomorrow with a new quotation.",
            "Price fluctuations have only one significant meaning for the "
            "true investor.",
        ],
        "apply":
            "Where you are: the price is swinging hard and your pulse is "
            "following the chart.\n"
            "Ask first: what is my own valuation, and against it, is today's "
            "quote an opportunity, a trap, or noise?\n"
            "Where it goes wrong: turning ignore him into never looking, so a "
            "real deterioration goes unnoticed; or going contrary with no "
            "valuation of your own, which is only reflex.",
    },
    {
        "k": "margin-of-safety",
        "n": "The margin of safety",
        "w": "The room you leave for being wrong",
        "src": "The Intelligent Investor, chapter 20",
        "dek": "He said the whole secret of sound investment fits in three "
               "words. The question is what those three words are actually "
               "buying.",
        "story":
            "The last chapter of the book is the answer, and its title is the "
            "phrase. ==Distill the secret of sound investment into three "
            "words, he writes, and the motto is margin of safety.== Pay fifty "
            "cents for a dollar of value, and the gap is not an expected "
            "profit. It is room for bad luck and for your own arithmetic "
            "being wrong. His definition of investing is colder still: "
            "thorough analysis, safety of principal, an adequate return, and "
            "anything short of that is speculation. Note the order.",
        "f": [
            {"n": "What you are buying is surviving your own error",
             "d": "The margin does not make a correct judgement pay more. It "
                  "makes a wrong one affordable. Its price is set by "
                  "self-doubt: the valuation could be thirty per cent out, "
                  "the industry could turn, something unmodelled could "
                  "arrive. Size the discount to how much you distrust your "
                  "own estimate.",
             "eg": "Schedule buffer is not for slow workers. It is for the "
                   "requirement being misunderstood. A plan that has never "
                   "slipped has usually spent its margin early."},
            {"n": "A good asset with no margin is still dangerous",
             "d": "Graham is explicit that the counter-example is not a bad "
                  "company. It is a good company bought at the wrong price. "
                  "Quality and safety are two independent variables, and the "
                  "largest losses tend to start with the sentence that "
                  "something this good does not need a discount.",
             "eg": "The outstanding candidate names an outsized number; the "
                   "celebrated project asks for unconditional commitment. "
                   "Both are good, and both trades assume no mistakes."},
            {"n": "The margin comes from the price, not from your confidence",
             "d": "Conviction cannot serve as a buffer. The more certain a "
                  "judgement feels, the easier it is to conclude the discount "
                  "is unnecessary, which is exactly when it should be widest. "
                  "So the rule has to be mechanical: below this discount, no "
                  "action, however sure you are.",
             "eg": "Write down a position cap and a required discount and let "
                   "them stand. They exist for the handful of occasions when "
                   "you are most convinced."},
        ],
        "q": [
            "Distill the secret of sound investment into three words: margin "
            "of safety.",
            "An investment operation promises safety of principal and an "
            "adequate return.",
            "The margin of safety renders an accurate estimate of the future "
            "unnecessary.",
        ],
        "apply":
            "Where you are: an opportunity you feel certain about, and the "
            "cushion looks like money left on the table.\n"
            "Ask first: if my estimate is thirty per cent out, does this "
            "price still protect the principal?\n"
            "Where it goes wrong: using the margin as a reason to haggle "
            "forever and never own anything fairly priced, or trading the "
            "discount away for a feeling of certainty.",
    },
]
