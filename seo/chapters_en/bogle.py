# -*- coding: utf-8 -*-
"""John C. Bogle — English.

English readers usually know Bogle as 'the index fund guy' and file him under 'boring but right'.
This page takes the two arguments underneath the product: costs are the one number you control,
and if you cannot pick the needle you can own the haystack. The only quotation is his own line from
The Little Book of Common Sense Investing (2007).
"""

PARENT = {
    "name": "John C. Bogle",
    "slug": "bogle",
    "blurb": "Deep read",
    "items": [
        {"k": "humble-arithmetic", "n": "Cut the cost first",
         "w": "You cannot set the return, but you can set what you pay",
         "ready": True,
         "line": "His first index fund raised a fraction of its target and rivals mocked it for settling for average - average was the bet"},
        {"k": "buy-the-haystack", "n": "Own the haystack",
         "w": "If you cannot tell which one will rise, stop trying to choose",
         "ready": True,
         "line": "His college thesis already said funds could not claim to beat the market averages - decades later he turned that into a fund"},
    ],
}

CHAPTERS = [
    {
        "k": "humble-arithmetic",
        "n": "Cut the cost first",
        "w": "You cannot set the return, but you can set what you pay",
        "src": "Bogle, 'The Relentless Rules of Humble Arithmetic' (Financial Analysts Journal, 2005); Common Sense on Mutual Funds (1999); Stay the Course (2018)",
        "dek": "He bet on the average. Before you hand your money over, which number should you look at first?",
        "story":
            "In August 1976 Bogle's first index fund went on sale. The underwriters had hoped to raise $150 million and came back with $11.3 million. "
            "Rivals called it Bogle's Folly: who pays someone to manage money and settles for average? "
            "==Average was exactly what he was betting on==. His sum was simple. All investors together own the whole market, so before "
            "costs they earn the market's return between them. After costs they must, on average, earn less, by exactly what they paid.",
        "f": [
            {"n": "Returns are a guess, costs are a fact",
             "d": "Nobody can tell you what the market will do next year. The management fee, the trading costs and the sales charges are certain, and they come round every year. Cost, he argued, is the one variable an investor really controls.",
             "eg": "Which of two funds did better over three years tells you little. The gap in their fees is written into the contract."},
            {"n": "A small fee, compounded for decades",
             "d": "Fees are not paid once. They come out of your capital every year, and whatever they take stops earning for you. The longer you hold, the bigger the bite.",
             "eg": "Thirty years at 7% a year against thirty years at 6% leaves the second pot nearly a quarter smaller."},
            {"n": "Losing as a group is arithmetic, not luck",
             "d": "Active managers taken together are the market. They win and lose against each other and break even before costs. After costs, as a group, they must trail it. That needs no forecast, only subtraction.",
             "eg": "Players at a card table win from one another, but the house's cut is lost by the table as a whole."},
        ],
        "q": [
            "Before costs everyone is average; after costs you lose what you paid.",
            "The market decides what it gives. You decide what you pay.",
            "Every dollar you do not pay keeps working for you.",
        ],
        "apply":
            "Where you are: You choose funds by last year's league table and have never looked at the fees.\n"
            "Ask first: How much does this cost me each year, and what exactly would I give up by going cheaper?\n"
            "Where it goes wrong: Reading it as 'the cheapest is always best' or 'index funds cannot lose'. An index gives you the market minus a small fee. If the market halves, so does your fund. The saving is certain; the return never is.",
    },
    {
        "k": "buy-the-haystack",
        "n": "Own the haystack",
        "w": "If you cannot tell which one will rise, stop trying to choose",
        "src": "Bogle, The Little Book of Common Sense Investing (2007); Princeton senior thesis, 'The Economic Role of the Investment Company' (1951); Stay the Course (2018)",
        "dek": "He stopped hunting for the needle. Can someone who cannot pick winners still invest?",
        "story":
            "In the winter of 1949 a Princeton student named John Bogle was leafing through Fortune in the university library and found a long piece "
            "on the mutual-fund business in Boston. He made it the subject of his senior thesis. In the thesis, handed in in 1951, he already argued "
            "that the funds could not claim to do better than the market averages. ==A quarter of a century later he built a fund on that one sentence==, "
            "and spent the rest of his life telling people to stop hunting for the winner.",
        "f": [
            {"n": "The professionals cannot find the needle either",
             "d": "For decades at Vanguard he kept showing the figures: over long periods most actively managed funds fall behind the market they measure themselves against, and this decade's winners are mostly different names by the next.",
             "eg": "Buy last year's top fund this year and you often catch it on the way back down."},
            {"n": "Own the stack and you need not bet on a straw",
             "d": "Own the whole market and any one company's disaster is only a small slice. What remains is the return of all the companies together. You need not understand every business, only that you own all of them.",
             "eg": "Not sure which electric-car maker survives? Do not bet on one. Own the industry."},
            {"n": "Then leave it alone",
             "d": "The title of the memoir he published near the end of his life is a single instruction: stay the course. Every trade costs something, and people tend to sell at the bottom and buy at the top. Once you own the haystack, the best thing to do is touch it less.",
             "eg": "Set up a monthly investment and stop opening the app every day to check."},
        ],
        "q": [
            "Don't look for the needle in the haystack. Just buy the haystack!",
            "If you cannot tell which one, do not bet on one.",
            "Owning everything is the method. Holding on is the skill.",
        ],
        "apply":
            "Where you are: You know your money should be invested, but you cannot tell what will rise, so you keep putting it off.\n"
            "Ask first: Do I need to pick the winner, or do I only need my share of the whole market?\n"
            "Where it goes wrong: Reading it as 'buy the index and you need not understand anything'. You still need to know how big a fall you can sit through. Sell in a panic when the market halves, and the haystack will not save you.",
    },
]
