# -*- coding: utf-8 -*-
"""Zhang Juzheng — English.

Both of these are administrative reforms with unglamorous names, and both are
the kind of thing an English reader will recognise instantly from their own
organisation: decisions that leave the room and are never heard of again, and
a process with so many stages that nobody can say where the money went. The
page keeps the Ming detail and lets the mechanism do the work.
"""

PARENT = {
    "name": "Zhang Juzheng",
    "slug": "zhang-juzheng",
    "blurb": "Deep read",
    "items": [
        {"k": "kaocheng", "n": "The evaluation ledgers",
         "w": "Hang every item on a name and a date", "ready": True,
         "line": "Sending the order down is not doing it; striking it off is"},
        {"k": "single-whip", "n": "The single whip",
         "w": "Merge the accounts into one payment", "ready": True,
         "line": "The more hands it passes through, the more is eaten"},
    ],
}

CHAPTERS = [
    {
        "k": "kaocheng",
        "n": "The evaluation ledgers",
        "w": "Hang every item on a name and a date",
        "src": "Memorial on auditing documents and assessing each matter, 1573",
        "dek": "Orders go down and nobody carries them out. This is about the "
               "ledger he used to fix a failure every dynasty had.",
        "story":
            "In 1573 he described the situation plainly: the memorials were "
            "endless and no office held to anything. Once an order left, "
            "nobody tracked it, and there was no record of whether it had been "
            "done. His fix was crude. Everything due was entered in a "
            "register, in three copies, with a deadline, and struck off item "
            "by item when it fell due. ==If the governors delay, the "
            "ministries report it; if the ministries conceal, the six offices "
            "report it; if the six offices miss it, we report it.== Within a "
            "few years an order issued in the morning was obeyed by evening "
            "ten thousand li away.",
        "f": [
            {"n": "Issued is not finished; struck off is",
             "d": "Most organisations break in the same place: there is a "
                  "record that the order went out and no record that it came "
                  "back. Without the act of striking off, work evaporates "
                  "between layers naturally, and nobody has to answer for the "
                  "evaporation.",
             "eg": "The minutes list thirty actions and not one carries an "
                   "owner and a date. Two weeks later, fewer than five have a "
                   "status anyone can state."},
            {"n": "The point of three copies is the third one",
             "d": "One copy stayed with the office, one went to the "
                  "supervising bureau, one to the cabinet. The same item sits "
                  "in three places that do not report to each other, so any "
                  "attempt to soften it shows up in the other two. A single "
                  "ledger never cures delay.",
             "eg": "If the task lives only on the delivery team's own board, "
                   "they define progress. The same list held by the requester "
                   "and by management is what makes the wording match."},
            {"n": "The audit has to reach the top layer",
             "d": "The decisive clause is that if the supervising offices miss "
                  "it, the cabinet reports them. Nearly every assessment "
                  "system stops at the supervisors, which makes the "
                  "supervisors the one link nobody checks, and the whole chain "
                  "slackens from there.",
             "eg": "Who checks the checkers? Without that clause the quality "
                   "team's own late reports are never pursued, and everyone "
                   "can see it."},
        ],
        "q": [
            "The memorials are endless and no office holds to anything.",
            "If the six offices miss it, we report it ourselves.",
            "An order issued in the morning was obeyed by evening.",
        ],
        "apply":
            "Where you are: plenty is decided and little lands, and you want "
            "more execution.\n"
            "Ask first: is there a list with an owner and a deadline on every "
            "item, struck off one by one when due, and how many people hold "
            "that list?\n"
            "Where it goes wrong: substituting meetings and emphasis for "
            "records; leaving the top layer of the assessment system "
            "unexamined.",
    },
    {
        "k": "single-whip",
        "n": "The single whip",
        "w": "Merge the accounts into one payment",
        "src": "History of Ming, Treatise on Food and Money",
        "dek": "Why does the same sum shrink the more hands it passes through? "
               "This is about merging dozens of levies into one.",
        "story":
            "Mid-Ming taxes and labour service were absurdly tangled: land "
            "tax, head service, tribute goods, labour levies, silver levies, "
            "dozens of headings, each with its own collection date, its own "
            "collector, its own conversion rate. Every stage was an "
            "opportunity to take a little more, and what the people paid and "
            "what the treasury received were far apart. ==The single whip "
            "totalled a county's taxes and services together, measured by land "
            "and counted by head, and all of it was paid in to the "
            "government.== The state now hired labour for the year instead of "
            "levying it. Dozens of payments became one, in silver, on one "
            "date.",
        "f": [
            {"n": "Every stage is a chance to lose something",
             "d": "Complexity is itself a cost. More headings and more hands "
                  "mean more room for interpretation, and every scrap of "
                  "interpretive room eventually gets used. Simplification is "
                  "not valuable because it saves effort; it is valuable "
                  "because it removes the positions where things are done "
                  "quietly.",
             "eg": "Twenty expense categories with boundaries a person has to "
                   "judge. Merge them into three and the disputes and the grey "
                   "areas both vanish, without anyone becoming more honest."},
            {"n": "One unit of measurement",
             "d": "Converting to silver is the step people skip past, and it "
                  "is the pivot of the whole reform. Goods, labour and time "
                  "are not commensurable, so they cannot be reconciled. Once "
                  "everything is in one unit, over-collection and "
                  "under-collection are visible at a glance.",
             "eg": "Each department reports on its own basis — leads, "
                   "sign-ups, paid accounts. Until there is one basis, no "
                   "total means anything."},
            {"n": "Simplifying offends whoever lives on the complexity",
             "d": "Complexity did not arise by itself; it is useful to "
                  "somebody. The single whip cut into exactly the clerks and "
                  "gentry who profited from the stages, which is why he was "
                  "condemned after his death — and why the law survived, "
                  "because it worked. Predict who will resist, and why.",
             "eg": "Cut one useless approval and the loudest objection comes "
                   "from whoever runs that approval. This is foreseeable. Have "
                   "somewhere for them to go before you start."},
        ],
        "q": [
            "Total a county's taxes and services, measure by land, count by "
            "head.",
            "A year's labour service, hired by the government instead.",
            "Complexity is useful to somebody. That is why it grew.",
        ],
        "apply":
            "Where you are: a process is full of headings and every stage says "
            "it is necessary.\n"
            "Ask first: converted into one unit, how many payments are "
            "actually left?\n"
            "Where it goes wrong: merging without unifying the measure, so the "
            "books still do not reconcile; not predicting who lives on the "
            "complexity.",
    },
]
