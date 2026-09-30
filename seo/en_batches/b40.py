# -*- coding: utf-8 -*-
"""Daily entry, day 20: Edward Deci.

Picked by fan-out. 'Straight A's, then no more grades' was among the
emptiest situations on the Chinese side, at eight. What hangs there says the
scoreboard left you with no direction (Excellent Sheep, Socrates, Jobs);
nothing says that the scoreboard may have eaten the drive itself, which is
what the 1971 puzzle experiment shows. Under 'The team has gone flat' the
pages are about rewards and punishments used well (Han Feizi), scaffolding
(Vygotsky) and process praise (Dweck); nothing turns the question round from
'how do I motivate them' to 'what conditions let them motivate themselves'.

The last two entries were Chinese, so this one comes from the other side.

Three stories, no overlap: the entry is the argument over the 1999
meta-analysis; the chapters are the Soma puzzles and the 1995 book.

All situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Edward Deci",
        "slug": "deci",
        "e": "United States · 1942–",
        "w": "Intrinsic motivation", "y": 1971,
        "d": "American psychologist, born in 1942, who took his doctorate "
             "at Carnegie Mellon in 1970 and spent his career at the "
             "University of Rochester. In 1971 he published an experiment "
             "that behaviourists found hard to accept: pay people for "
             "something they already enjoy, stop paying, and they do less of "
             "it than before. With Richard Ryan he built that finding into "
             "self-determination theory, which says people need three "
             "things, autonomy, competence and relatedness, and move without "
             "being pushed when they have them.",
        "story":
            "Plenty of people refused to believe it. Decades of behaviourism "
            "said that rewarded behaviour increases. In 1994 Judy Cameron and "
            "David Pierce published a review in the Review of Educational "
            "Research concluding that, overall, rewards did not undermine "
            "intrinsic interest. Deci, Richard Koestner and Ryan gathered 128 "
            "experiments and published their own analysis in Psychological "
            "Bulletin in 1999. Spoken praise made people keener. Tangible "
            "rewards promised in advance for doing a task reliably made them "
            "do less of it when nobody was watching. The two sides went on "
            "arguing for years.",
        "f": [
            {"n": "Is the reason inside or outside?",
             "d": "He looked less at how much people did than at why. Done for "
                  "fun or done for pay, the act looks the same. In the first "
                  "the reason sits with you; in the second it sits in someone "
                  "else's hand, and they can take it back.",
             "eg": "Someone who loved writing starts taking work by the word, "
                   "and writes nothing on days without a commission."},
            {"n": "The deal struck in advance does the damage",
             "d": "In the 1999 analysis the worst effect came from tangible "
                  "rewards promised beforehand for doing the task. Surprise "
                  "rewards and spoken praise did not do it. The question is "
                  "not whether to reward, but whether the reward has become a "
                  "trade.",
             "eg": "Make the top ten and you get a new phone. The top ten is "
                   "now the phone's price."},
            {"n": "Three things people need",
             "d": "He and Ryan named the conditions under which people move "
                  "on their own: autonomy, the sense that this is theirs; "
                  "competence, doing it well at a stretch; relatedness, "
                  "someone nearby who cares. Take one away and they need "
                  "pushing.",
             "eg": "A quiet new hire: check whether he lacks the why, the how, "
                   "or anyone who talks to him."},
            {"n": "Autonomy is not independence",
             "d": "He kept correcting one misreading. Autonomy is not having "
                  "the final say or being left alone. You can rely on others "
                  "and follow them and still feel the choice is yours; you "
                  "can go it alone and simply be avoiding someone.",
             "eg": "Taking the pills your doctor prescribed can be compliance "
                   "or a decision you have made your own."},
            {"n": "Outside rules can become your own",
             "d": "Not everything is fun. He and Ryan layered the outside "
                  "reasons too: doing it because someone watches, because you "
                  "would feel guilty, because you see its use. The further "
                  "along, the more it is yours.",
             "eg": "Two students learn vocabulary daily. The one afraid of a "
                   "scolding stops in the holidays; the one who wants to read "
                   "novels keeps going."},
        ],
        "apply":
            "Pick one thing you are pushing someone to do with rewards or "
            "penalties: a child's homework, a weekly report, your own gym "
            "streak. Pause the 'do it and you get this' deal and say three "
            "things instead: why it matters, that you know they may not want "
            "to, and which parts they can decide. Check in a week whether "
            "any of it happens when nobody is watching. If the person you "
            "are pushing is you, put the streak chart away and note only the "
            "times you wanted to do it anyway.",
        "q": [
            "Buy something a person loved doing, and you buy up the love.",
            "A reason held in someone else's hand can be taken back.",
            "Autonomy is not having the final say. It is meaning it.",
            "Don't ask how to motivate him. Ask what room to build.",
        ],
        "l": ["Excellent Sheep", "Carol Dweck", "Han Feizi",
              "Mihaly Csikszentmihalyi"],
        "contrast": [
            {"n": "Han Feizi",
             "why": "Both are about how reward and punishment move people. "
                    "Han Feizi calls them the ruler's two handles: grip them "
                    "and people move. Deci found that paying for something "
                    "people already loved left them doing less once the pay "
                    "stopped. One treats reward as the engine; the other asks "
                    "what the reward replaced."},
            {"n": "Carol Dweck",
             "why": "Both are about praise. Dweck says praise effort, not "
                    "cleverness, because praising cleverness makes people "
                    "afraid to fail. Deci says the same words of praise can "
                    "inform or control. One asks what you praise; the other "
                    "asks who is in charge when you do."},
        ],
    },
]

INTROS = {
    "deci":
        "An American psychologist who showed in 1971 that paying people for "
        "something they already love can leave them doing less of it once "
        "the pay stops - the drive was not added by the reward, it was "
        "swapped out",
}

SCENES = [
    ("Straight A's, then no more grades", "Starting out", [
        ("Nobody praises me, so I can't get going.",
         [("deci", "paid-to-play")]),
    ]),
    ("My kid won't listen", "At home", [
        ("I pay him for good grades. Is that wrong?",
         [("deci", "paid-to-play")]),
    ]),
    ("The team has gone flat", "Leading people", [
        ("How do I get them to want it themselves?",
         [("deci", "conditions-not-carrots")]),
    ]),
]

ASKS = {
    "deci/paid-to-play":
        "Nobody praises me, so I can't get going.",
    "deci/conditions-not-carrots":
        "How do I get them to want it themselves?",
}
