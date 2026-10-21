# -*- coding: utf-8 -*-
"""Daily entry: David Ricardo.

Picked by fan-out. 'There's never enough time' (one of the emptiest) holds
Seneca, Newport, Parkinson and Cowan: time stolen by others, by fragments, by
deadlines, by machines. Nothing on the person who is short of time because
they are better than everyone around them at every job, and so keep all of it.
'Everyone says it can't be done cheaper' has nothing on why each new site costs
more than the last.

Why he qualifies: the leading theorist of classical political economy; his
Principles (1817) introduced comparative advantage, still the foundation of
trade theory, and the theory of differential rent.

The entry story is his marriage and his first reading of Smith at Bath; the
chapters are England and Portugal (chapter 7) and rent at the margin
(chapter 2).
"""

ENTRIES = [
    {
        "c": "How the world works",
        "n": "David Ricardo",
        "slug": "ricardo",
        "e": "England · 1772–1823",
        "w": "Dividing the work", "y": 1817,
        "d": "English economist. He joined his father on the London Stock Exchange at fourteen, made a fortune "
             "dealing in stocks and government loans, and in his early forties left the exchange and bought a "
             "country estate. His Principles of Political Economy and Taxation (1817) set out comparative "
             "advantage, which still sits under the theory of trade. This page takes two of his sums: why the "
             "person who is better at everything should still divide the work, and why the newest share always "
             "does worse than the ones before.",
        "story":
            "At twenty-one Ricardo married a Quaker, broke with his Jewish parents over it, and started again "
            "on the exchange on his own. At twenty-seven, staying in Bath while his wife took the waters, he "
            "happened on a copy of Adam Smith's Wealth of Nations and was taken with economics from then on. "
            "Ten years passed before he published anything on it: a piece on why the price of gold had risen.",
        "f": [
            {"n": "What is given up decides it",
             "d": "Portugal made both cloth and wine with fewer men than England, and he showed it should still make "
                  "only wine and leave the cloth, because each batch of cloth cost it more wine. Who is better "
                  "does not decide the division; what each gives up does.",
             "eg": "You are faster than your assistant at proposals and spreadsheets. The afternoon on the spreadsheet costs a proposal only you could write."},
            {"n": "The newest share lands on poorer ground",
             "d": "The best land is farmed first, and each new field returns less than the last. The price of corn is "
                  "set by the worst field in use, and the extra the good fields yield becomes the landlord's rent.",
             "eg": "Your fifth shop is usually on a worse site than your first, and the average across five hides its loss."},
            {"n": "The world in a few numbers",
             "d": "He hardly used real firms in his book, only a few figures: 100 men, 120, 90, 80. Few enough to "
                  "see at a glance, so the conclusion has nowhere to hide. Schumpeter later called this habit of "
                  "running from a few assumptions straight to policy the Ricardian vice.",
             "eg": "Reduce an argument to three numbers on the whiteboard before the meeting, then ask what the three numbers leave out."},
        ],
        "apply": "List the jobs on your plate. For each, write two columns: how far ahead of the people around me I am; and "
                 "what I am not doing while I do it. Keep the one where the second column is dearest, and hand one of the rest over this week.",
        "q": [
            "Not who is better, but what each gives up.",
            "Cost the newest share on its own.",
            "A sum in three numbers still leaves things out.",
        ],
        "l": ["The Wealth of Nations", "Ronald Coase", "John Maynard Keynes", "Thorstein Veblen"],
        "contrast": [
            {"n": "The Wealth of Nations", "why": "Both are about dividing labour. Smith says division makes people more skilled, one step each in the pin factory; Ricardo says that even with no difference in skill, division pays as long as what each gives up differs. One explains where the gain comes from, the other who should take which job."},
            {"n": "Ronald Coase", "why": "Both ask who should do a job. Coase counts the cost of buying it from outside, so some work belongs inside the firm; Ricardo counts what you give up by doing it yourself, so even work you can do should go to someone else. One looks at the cost of the handover, the other at your own alternatives."},
        ],
    },
]

INTROS = {
    "ricardo":
        "English economist who set out comparative advantage - Portugal made "
        "cloth and wine with fewer men than England, and he showed it should "
        "still make only wine; he also showed the price of corn follows the "
        "last and worst field ploughed",
}

SCENES = [
    ("There's never enough time", "Body and energy", [
        ("I'm better at all of it, so I end up doing all of it.",
         [("ricardo", "better-at-both")]),
    ]),
    ("Everyone says it can't be done cheaper", "Getting it done", [
        ("Every new site we open costs more than the last.",
         [("ricardo", "the-last-field")]),
    ]),
]

ASKS = {
    "ricardo/better-at-both": "I'm better at all of it, so I end up doing all of it.",
    "ricardo/the-last-field": "Every new site we open costs more than the last.",
}
