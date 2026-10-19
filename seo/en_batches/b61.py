# -*- coding: utf-8 -*-
"""Daily entry: Fan Zhongyan.

Picked by fan-out. 'They said no to my plan' (10 pieces, one of the emptiest)
hangs Su Yu on bringing it back a third time, Li Shimin on hearing all sides,
Zhang Liang on how to put it to a superior, Boyd and Thiel on whether to hold
out. Nothing on the other half of the sentence: after the no, you still have to
sit at the same table as the man who said it, and when what you are doing looks
wrong to those above you before the results are in.

Why he qualifies: one of the leading statesmen of the Northern Song, with a full
biography in the History of Song; he led the Qingli reforms of 1043.

The entry story is his childhood and why he took his own name back; the chapters
are the Lü Yijian quarrel and the Hangzhou famine. No sentence is quoted as his.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Fan Zhongyan",
        "slug": "fan-zhongyan",
        "e": "Northern Song · 989–1052",
        "w": "Arguing the case", "y": 1043,
        "d": "A Northern Song statesman with a full biography in the History of Song. "
             "Born in 989 in Suzhou, he lost his father at two, was taken by his mother "
             "into a new family, and studied hard until he passed the jinshi examination. "
             "At court he spoke out: a chart of promotions that accused the chief minister of "
             "favouritism got him sent away to Raozhou. Later he defended the north-west and, "
             "in 1043, set out ten proposals for reform; within about two years he asked to be "
             "relieved. This page is about how he argued within one court: what he said while "
             "arguing, how he worked with the man who had overruled him, and how he answered when "
             "his methods were challenged.",
        "story":
            "Fan Zhongyan lost his father at two. His mother remarried into the Zhu family of Changshan, "
            "and the boy took their name and was called Zhu Yue. When he grew up and learned who his family "
            "had been, he wept, took leave of his mother and went to Yingtianfu to study. By day and night "
            "he hardly stopped; in winter, worn out, he splashed his face with cold water, and when there was "
            "no food he made do with thin porridge. Only after he passed the examination and brought his mother "
            "to live with him did he take back the name Fan.",
        "f": [
            {"n": "Argue the case, not the man",
             "d": "In the chart of officials he sorted names into those promoted in order and those not, those moved for the public good and those for private reasons. When Lü Yijian came back into office and the emperor asked him to forget it, he said he had argued state business and held no grudge.",
             "eg": "In a review you say the cost basis on page three does not add up, not that he always does this."},
            {"n": "Charged with frivolity, lay out the method",
             "d": "In the famine of 1050 he let Hangzhou race boats and had the temples build. An inspector charged him with neglecting relief; he answered item by item, saying it put money into the hands of people who live on wages. That year only Hangzhou saw no one forced to leave.",
             "eg": "Asked what a spend was for, you paste the model in."},
            {"n": "Ten proposals at once draw their opponents together",
             "d": "In 1043 he set out ten proposals, from judging officials on results to lightening labour service, and most were issued. The History of Song says the changes came without gradualness and were too wide in scope; slander spread, talk of faction reached the emperor, and he asked to be relieved.",
             "eg": "A reform that touches six departments in one quarter gives every department a reason to wait for it to fail."},
        ],
        "apply": "Pick one proposal that was turned down in a meeting this month. Write down what you said when you argued, and mark which lines were about the decision and which were really about him. Cross out the second kind, and see what you would still say next time you sit at the same table.",
        "q": [
            "Argue the list. Whoever wants to answer has to answer it first.",
            "Looking wrong is not being wrong, but you have to prove it.",
            "Changes made all at once gather their opponents all at once.",
        ],
        "l": ["Wei Zheng", "Su Yu", "Zhang Juzheng", "Yan Ying"],
        "contrast": [
            {"n": "Wei Zheng", "why": "Both said no to power to its face. Wei Zheng was telling an emperor, and was kept on as a remonstrator; Fan Zhongyan was taking on a chief minister, was sent away, and had to share a court with him afterwards. One is about getting those above you to listen, the other about the day after."},
            {"n": "Su Yu", "why": "Both had a plan turned down. Su Yu telegraphed his superiors a third time to bring it back; Fan Zhongyan was transferred for arguing, and years later sat in the same court as the man who had overruled him. One is about whether to bring it again, the other about how to live with the answer."},
        ],
    },
]

INTROS = {
    "fan-zhongyan":
        "Northern Song statesman - sent away for charging the chief minister "
        "with favouritism, he later told the emperor his quarrel had been "
        "about the state, not the man; and when charged with frivolity in a "
        "famine, he wrote out what every item was for",
}

SCENES = [
    ("They said no to my plan", "Making a call", [
        ("He turned down my proposal, and I still have to work with him.",
         [("fan-zhongyan", "the-quarrel-was-about-the-state")]),
        ("My boss says my method is wrong, and I have no results yet.",
         [("fan-zhongyan", "the-famine-ledger")]),
    ]),
]

ASKS = {
    "fan-zhongyan/the-quarrel-was-about-the-state": "He turned down my proposal, and I still have to work with him.",
    "fan-zhongyan/the-famine-ledger": "My boss says my method is wrong, and I have no results yet.",
}
