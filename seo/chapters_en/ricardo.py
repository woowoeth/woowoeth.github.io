# -*- coding: utf-8 -*-
"""David Ricardo — English.

English readers who know the name know "comparative advantage" as a line in a
trade-policy argument between countries. This page turns both of his sums on the
reader's own desk: why the person who is better at everything should still hand
work off, and why the newest branch is the one to cost on its own.

Everything here is our own wording. The figures (100, 120, 90 and 80 men; one
fifth and one third) are Ricardo's, from chapter 7 of the Principles (1817) and
its footnote; no sentence of his is put in quotation marks.
"""

PARENT = {
    "name": "David Ricardo",
    "slug": "ricardo",
    "blurb": "Deep read",
    "items": [
        {"k": "better-at-both", "n": "Better at Both, and Still Hand One Over",
         "w": "Keep the job where your lead is widest",
         "ready": True,
         "line": "Portugal made both cloth and wine with fewer men than England, and he showed it should still leave the cloth to England"},
        {"k": "the-last-field", "n": "The Last Field Ploughed",
         "w": "The further you spread, the poorer the ground the next share lands on",
         "ready": True,
         "line": "The best land is farmed first, each new field is worse, and the price of corn follows the worst one"},
    ],
}

CHAPTERS = [
    {
        "k": "better-at-both", "n": "Better at Both, and Still Hand One Over",
        "w": "Keep the job where your lead is widest",
        "src": "On the Principles of Political Economy and Taxation (1817), chapter 7, 'On Foreign Trade', and its footnote",
        "dek": "You are the best person for every job on the list. Ricardo's question is what each one stops you doing.",
        "story":
            "In his 1817 book Ricardo set out a sum. Cloth in England takes "
            "the labour of 100 men for a year, and wine takes 120. In Portugal "
            "the same cloth takes 90 men and the same wine only 80. Portugal "
            "is better at both, so instinct says it should make both. He "
            "showed the opposite: ==Portugal should leave the cloth to England "
            "and make wine.== Between them, the same men end up with more "
            "cloth and more wine.",
        "f": [
            {"n": "Count what you give up, not how far ahead you are",
             "d": "Portugal saves 10 men on cloth and 40 on wine. Every batch of cloth it weaves is wine it did not make. The question is not whether you beat the other person, but what the job in front of you stops you doing.",
             "eg": "You draft proposals faster than your assistant and build spreadsheets faster too. An afternoon on the spreadsheet costs a proposal only you could write."},
            {"n": "The stronger one should still pick one",
             "d": "In a footnote he makes it two men who both make shoes and hats. One is better at both: a fifth better at hats, a third better at shoes. Surely both gain, he asks, if the better man makes only shoes?",
             "eg": "Because you can do every job on the team, you most need to find the one where your lead is widest and give the rest away."},
            {"n": "The work you hand off will be done worse",
             "d": "Handing it over does not mean it is done as well. England needs more men for the cloth, and the sum still comes out ahead, because the men Portugal saved went to dearer work. Slower and rougher is the price of dividing labour.",
             "eg": "Your assistant takes a day on the spreadsheet and you fix two cells in ten minutes. That day, you finished the proposal."},
        ],
        "q": [
            "The question is not who is better but what each gives up.",
            "Better at everything still means doing one thing.",
            "Slower hands on the work you gave away are the price.",
        ],
        "apply":
            "Where you are: you keep taking more on because you do each thing better than anyone near you, and none of it gets finished.\n"
            "Ask first: how far ahead am I on this job, and how far on that one? Keep the job where the lead is widest and hand off the rest in order of what each costs you.\n"
            "Where it goes wrong: using it to push off the work you dislike. He counted what is given up, not what is enjoyed, and the job you find easiest is not always the one to keep.",
    },
    {
        "k": "the-last-field", "n": "The Last Field Ploughed",
        "w": "The further you spread, the poorer the ground the next share lands on",
        "src": "On the Principles of Political Economy and Taxation (1817), chapter 2, 'On Rent'; An Essay on the Influence of a Low Price of Corn on the Profits of Stock (1815)",
        "dek": "The business keeps growing and every new branch earns less than the one before. Ricardo explains why, and what that last branch quietly sets.",
        "story":
            "Ricardo begins his account of rent with a newly settled country. "
            "Good land is plentiful and nobody pays for it. As people multiply "
            "and food runs short, second-rate land is ploughed, and from that "
            "moment the first-rate land earns a rent. Then the third grade is "
            "ploughed, then the fourth. ==The price of corn is set by the "
            "last and worst field.== Nothing changed on the good land. What "
            "changed is the field at the edge.",
        "f": [
            {"n": "The next share lands on worse ground",
             "d": "The best land is farmed first. Each new field, and each extra dose of capital on the same field, returns less than the one before. Nobody got lazy; the good ground was simply used up first.",
             "eg": "Your first shop is on the corner you know best. The fifth is in a mall you have visited three times and still can't read."},
            {"n": "The average hides the last share",
             "d": "The yield across the whole estate still looks fine, but whether this round pays is settled by the last field. He did his sums on the field that barely covers its costs and pays no rent, not on the average.",
             "eg": "Five shops together make a decent profit. Taken alone, the fifth has been living off what the first four put by."},
            {"n": "The gain from good ground goes to whoever holds it",
             "d": "The worse the new land, the higher the rent on the best. That was his case against the Corn Laws that propped up grain prices: dearer corn raised the landlord's rent and squeezed the profits of the farmer who rented from him.",
             "eg": "When the mall gets busy, the rent goes up first, and most of what you sold extra goes back to the landlord at the end of the month."},
        ],
        "q": [
            "Cost the last share on its own.",
            "A healthy average can hide a losing edge.",
            "The good ground goes first; what follows is poorer.",
        ],
        "apply":
            "Where you are: the first few branches make money, you are about to open another, and the average margin still looks fine.\n"
            "Ask first: taken on its own, does the new one earn its own costs? Do not let the earlier ones' results pay for it.\n"
            "Where it goes wrong: reading it as growth always loses. He said the new land is poorer, not that it should never be farmed. While good ground is left, or you can improve the poor ground, the sum has to be done again.",
    },
]
