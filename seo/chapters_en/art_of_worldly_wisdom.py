# -*- coding: utf-8 -*-
"""The Art of Worldly Wisdom — English.

The English reader most likely knows this book through Schopenhauer's praise
or through a quotation calendar, which turns three hundred hard maxims into
decoration. The job of the page is to take two of them back out of the
calendar and show the mechanism underneath: a court chaplain with no power of
his own, working out how a clever man survives among people who have it.
"""

PARENT = {
    "name": "The Art of Worldly Wisdom",
    "slug": "art-of-worldly-wisdom",
    "blurb": "Deep read",
    "items": [
        {"k": "quit-while-winning", "n": "Leave while you are winning",
         "w": "A long run of luck is the warning", "ready": True,
         "line": "The best players rise from the table while they are still ahead"},
        {"k": "do-and-be-seen", "n": "Do, and be seen doing",
         "w": "Half the work is being known to have done it", "ready": True,
         "line": "What is not seen is as if it did not exist"},
    ],
}

CHAPTERS = [
    {
        "k": "quit-while-winning",
        "n": "Leave while you are winning",
        "w": "A long run of luck is the warning",
        "src": "The Art of Worldly Wisdom, maxim 38",
        "dek": "Everyone reads it as timidity. Read as written it is a "
               "gambler's arithmetic: a long winning run is the thing to "
               "distrust.",
        "story":
            "Gracián was a Jesuit in seventeenth-century Spain who spent his "
            "life watching men manoeuvre at court and inside his own order, "
            "and compressed what he saw into three hundred maxims. Number "
            "thirty-eight is about the card table. The reasoning is a "
            "gambler's: a run of luck that goes on too long is itself the "
            "warning, ==a long-continued spell of good luck is always "
            "suspicious==, and the best players rise while they are still "
            "ahead. Fortune, he adds, soon tires of carrying anyone long on "
            "her back.",
        "f": [
            {"n": "A winning run raises your exposure, not your odds",
             "d": "Each success quietly adds to two piles: the stake on the "
                  "table and your confidence in your own reading. The longer "
                  "the run, the higher both stand, and the more a single "
                  "reversal takes away. A streak is not evidence of a "
                  "pattern. It is a measure of what is now at risk.",
             "eg": "After four quarters of beating the forecast, the useful "
                   "move is to cut a position or lower a target, precisely "
                   "because nothing has gone wrong yet."},
            {"n": "Retreat well while retreating is still your choice",
             "d": "He rates a fine retreat as highly as a gallant attack, and "
                  "the rating is entirely about timing. Leaving while the "
                  "table is hot is orderly and your chips come with you. "
                  "Leaving after the mood turns is not a retreat, it is being "
                  "cleared out.",
             "eg": "A business sold at its peak has buyers queueing and sets "
                   "its own terms. The same business sold after the turn goes "
                   "at a third of the price."},
            {"n": "You are cashing in this hand, not quitting the game",
             "d": "Stopping while ahead is not caution. It closes the hand, "
                  "banks the winnings, and opens the next one on a fresh "
                  "judgement. What it cuts is the automatic renewal that lets "
                  "the last hand's luck stake the next one.",
             "eg": "A hit product whose team and budget roll straight into "
                   "the sequel is letting the previous round's luck pick the "
                   "next round's bet."},
        ],
        "q": [
            "Leave your luck while winning. All the best players do so.",
            "A long-continued spell of good luck is always suspicious.",
            "A fine retreat is as good as a gallant attack.",
        ],
        "apply":
            "Where you are: everything is going your way and you are thinking "
            "about adding to it.\n"
            "Ask first: how large is the exposure now, and how much of it "
            "would a reversal tomorrow take back?\n"
            "Where it goes wrong: reading it as never bet at all, or holding "
            "out for the exact top and therefore never leaving.",
    },
    {
        "k": "do-and-be-seen",
        "n": "Do, and be seen doing",
        "w": "Half the work is being known to have done it",
        "src": "The Art of Worldly Wisdom, maxim 130",
        "dek": "The maxim is uncomfortable coming from a priest. What it "
               "argues is not vanity but arithmetic about whose ledger your "
               "work sits on.",
        "story":
            "Maxim one hundred and thirty is its own title: ==do, and be seen "
            "doing==. Gracián is blunt about the reason. Things do not pass "
            "for what they are but for what they seem; to be of use and to "
            "know how to show it is to be twice as useful; what is not seen "
            "is as if it did not exist. From a Jesuit this grates, but he had "
            "watched able men outranked by visible ones. Elsewhere he is just "
            "as firm that reputation without substance does not survive. He "
            "is describing a ratio, not a substitute.",
        "f": [
            {"n": "On someone else's ledger, unseen work was never done",
             "d": "Your own ledger records what happened. Everyone else's "
                  "records only what they saw. Promotions, partnerships and "
                  "trust are drawn against those other ledgers. Quiet work is "
                  "not unrewarded through unfairness. It is held in an "
                  "account nobody else can query.",
             "eg": "The engineer who took uptime from ninety per cent to four "
                   "nines lost the review to the one who handled a single "
                   "visible outage."},
            {"n": "Showing is a craft, and it is not shouting",
             "d": "Being seen is not self-praise. The craft is in the "
                  "carrier: a write-up colleagues pass on, a tool whose users "
                  "say your name, an accurate crediting of your team when you "
                  "report upward. The strongest version has somebody else "
                  "doing the saying.",
             "eg": "A note on what went wrong that circulates all year beats "
                   "a line in a status report claiming a hard problem was "
                   "solved."},
            {"n": "Two ways the ratio kills you",
             "d": "All substance and no visibility buries the work and "
                  "eventually sours the person doing it. All visibility and "
                  "no substance clears to zero the first time anyone checks, "
                  "and someone always checks. The healthy ratio keeps the "
                  "claim half a step behind the fact.",
             "eg": "A firm that describes itself as slightly less capable "
                   "than it is beats expectations on every delivery. The "
                   "reverse pays down debt on every one."},
        ],
        "q": [
            "Do, and be seen doing.",
            "Things do not pass for what they are but for what they seem.",
            "What is not seen is as if it did not exist.",
        ],
        "apply":
            "Where you are: you have done real work and find promoting it "
            "distasteful.\n"
            "Ask first: whose ledger does this exist on right now? Apart from "
            "you, who could look it up?\n"
            "Where it goes wrong: letting showing become boasting, which "
            "spends credit you have not earned; or building the reputation "
            "first and waiting to be checked.",
    },
]
