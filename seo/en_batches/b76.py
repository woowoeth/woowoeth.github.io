# -*- coding: utf-8 -*-
"""Daily entry: Extraordinary Popular Delusions.

From DAILY_QUEUE.md row 13. 'Everyone is piling in' holds entries on contagion in crowds, credit as fuel,
reflexivity and bubbles as a phase of technological revolutions. None of them says that the buyers stop
wanting the thing itself, or that nobody tells you when a mania is over. Both chapters hang there.

Why it qualifies: Charles Mackay's book has been in print since 1841 and is still the standard
first reading on financial manias. Only the money chapters are used; its anecdotes are treated as
Mackay's telling, not as history (see hw_omit).

The entry story is the sailor who ate a tulip bulb; the chapters are the change in buyers at the top of
the tulip trade, and the 1720 company that would not say what it did. Newton's South Sea trade has its
own page and is not repeated.
"""

ENTRIES = [
    {
        "c": "Money and risk",
        "n": "Extraordinary Popular Delusions",
        "slug": "popular-delusions",
        "e": "Britain · 1841",
        "w": "Manias", "y": 1841,
        "d": "Charles Mackay's Extraordinary Popular Delusions and the Madness of Crowds, first published in 1841 and in "
             "print ever since. Its opening chapters are on money: John Law's Mississippi Scheme, the South Sea Bubble and "
             "the Dutch tulip mania. Many of its anecdotes are second-hand and it is no careful history, but it leaves a way "
             "of watching crowds. It is here because no entry yet says that buyers stop wanting the thing itself, or that "
             "nobody tells you when it is over.",
        "story":
            "A wealthy Dutch merchant, proud of his rare tulips, rewarded a sailor who brought news of a cargo with a red "
            "herring for breakfast. The sailor, fond of onions, saw what looked like one on the counter, pocketed it and "
            "ate it with his herring on the quay. It was a Semper Augustus bulb worth three thousand florins. The household "
            "found him sitting on a coil of ropes, finishing the last of it. Mackay, who took the story from an older "
            "travel book, says that breakfast could have fed a whole ship's crew for a year.",
        "f": [
            {"n": "One bulb, one list",
             "d": "Mackay copies out what was handed over for a single Viceroy bulb: two lasts of wheat, four of rye, four fat oxen, eight fat swine, twelve fat sheep, wine, beer, butter, a thousand pounds of cheese, a bed, a suit of clothes and a silver cup. Total: 2,500 florins.",
             "eg": "Turn a price into things you can see and use. It often sobers you up at once."},
            {"n": "From nobles to chimney-sweeps",
             "d": "At the height of it nobles, citizens, farmers, mechanics, seamen, footmen, maid-servants, even chimney-sweeps and old clothes-women dabbled in tulips. People turned their property into cash to buy flowers, and houses and land went at ruinously low prices.",
             "eg": "When people who never touch this kind of thing start telling you about it, most of the buyers are already in."},
            {"n": "No rescue and no court",
             "d": "After the crash, tulip-holders sent deputies to Amsterdam to ask the government for a remedy. It refused at first to interfere. In the end contracts made before November 1636 were declared void, later buyers were released on paying ten per cent, and the courts would not hear gambling debts.",
             "eg": "Money staked on a mania is rarely bailed out when it goes wrong."},
        ],
        "apply": "Next time you are about to follow everyone into something that is soaring, write one line first: am I "
                 "buying it to use, or only to sell to the next person? If it is the second, write down who that person is.",
        "q": [
            "To an outsider it was an onion.",
            "That breakfast could have fed a ship's crew for a year.",
            "Mad together, sane one at a time.",
        ],
        "l": ["The Crowd", "Charles P. Kindleberger", "Isaac Newton"],
        "contrast": [
            {"n": "Technological Revolutions", "why": "Perez sees bubbles as part of a technology's installation, with the wasted money laying the railways and fibre that later pay off. Mackay's tulips left nothing behind when they crashed. One asks whether a mania will leave something; the other asks whether you will be the last one holding it."},
        ],
    },
]

INTROS = {
    "popular-delusions":
        "Charles Mackay's 1841 history of manias, from a tulip bulb traded for 2,500 florins of grain and livestock to "
        "a London company that never said what it did - crowds, he says, go mad together and recover one at a time",
}

SCENES = [
    ("Everyone is piling in", "Money", [
        ("If nobody takes it off my hands, what's it worth?",
         [("popular-delusions", "bought-to-sell")]),
        ("Everyone's buying. Do I even need to ask what it is?",
         [("popular-delusions", "one-by-one")]),
    ]),
]

ASKS = {
    "popular-delusions/bought-to-sell": "If nobody takes it off my hands, what's it worth?",
    "popular-delusions/one-by-one": "Everyone's buying. Do I even need to ask what it is?",
}
