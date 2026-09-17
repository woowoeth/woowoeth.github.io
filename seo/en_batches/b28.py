# -*- coding: utf-8 -*-
"""Daily entry, day 8: Robert Axelrod.

Picked by fan-out. The thinnest Chinese situations are 被背叛了 and
上面说的话不能信, six chapters each. What hangs on being betrayed is Gottman
on repair, Konnikova on how trust is really built, Epictetus on judgement,
Han Xin and Li Ka-shing on when to stop - all of them about what to feel or
when to quit. What hangs on not believing your boss is Han Feizi, Hu Xueyan,
Schelling, the Analects: how to test a promise before you act on it. Nobody
there gives a rule for what to do on the next move after someone crosses you,
and nobody says the condition that decides whether a promise holds at all.
Axelrod's tournaments give both: never defect first, answer once and return
immediately, and expect none of it to work where there is no next round.

All four English situations already exist, so there is no SC_BOX here. The
famous sentence about winning by eliciting good behaviour is his, but it runs
to twenty-six words and the pull quotes cap at fourteen, so it appears as an
argument rather than inside quotation marks - no quoted line here is trimmed
or reworded.

Three stories, no overlap: the entry is the arms-race question he started
from, chapter one is the 1980 tournament, chapter two is the trench truce.
"""

ENTRIES = [
    {
        "c": "How the world works", "n": "Robert Axelrod",
        "slug": "axelrod", "e": "United States · born 1943",
        "w": "Reciprocity", "y": 1943,
        "d": "An American political scientist, born in 1943, who spent his "
             "career at the University of Michigan chasing one question: how "
             "can two sides who distrust each other, with no referee above "
             "them, ever cooperate. In 1980 he did something nobody had tried. "
             "Instead of proving which strategy was best, he invited game "
             "theorists everywhere to submit their best one as a computer "
             "program and ran a round robin, letting the scores decide. The "
             "winner was the shortest entry, TIT FOR TAT: cooperate first, then "
             "copy the other side's last move. In 1981, with the evolutionary "
             "biologist W. D. Hamilton, he carried the same logic into biology; "
             "in 1984 it became The Evolution of Cooperation.",
        "story":
            "What he was actually trying to solve was nuclear war. Born in "
            "1943, a mathematics degree from Chicago and a doctorate in "
            "political science from Yale, he kept returning to the question of "
            "his era: two states aimed at each other, trusting nothing, unable "
            "to fire, and somehow not fighting. Others worked on the "
            "negotiating table, on deterrence, on morality. He took a stranger "
            "route. He compressed the whole thing into a game with two moves, "
            "cooperate or defect, played over and over, and then refused to "
            "solve it himself. He posted the problem and asked the world to "
            "send programs.",
        "f": [
            {"n": "He ran a tournament instead of proving a theorem",
             "d": "The usual answer to which strategy is best is a model and a "
                  "proof. He published the rules, asked researchers to submit "
                  "their best rule as code, played every pair and let the totals "
                  "rank them. The answer was played out, not thought up.",
             "eg": "Rather than arguing in the meeting over which plan is better, "
                   "run both for a month and read the numbers."},
            {"n": "The shortest entry won",
             "d": "TIT FOR TAT is four lines: cooperate on the first move, then "
                  "copy the other side's last one. The second tournament drew "
                  "sixty-two programs whose authors all knew it had won and knew "
                  "its weaknesses. None of them beat it.",
             "eg": "The rule everyone can read, and everyone can predict, usually "
                   "outlasts the one with something hidden in it."},
            {"n": "The dividing line was moving first",
             "d": "No program near the top ever defected first. They let every "
                  "chance to take advantage go past and still scored highest. The "
                  "ones that took those chances collected early and spent the "
                  "rest of the tournament against opponents they had made.",
             "eg": "The two points squeezed out of this contract are usually drawn "
                   "in advance from the next one."},
            {"n": "Cooperation needs no friendship, only a next time",
             "d": "He pushes the claim to its floor. In the trenches of the "
                  "Western Front the two sides had never met, were ordered to "
                  "shoot each other and had no authority between them, and a "
                  "tacit truce grew anyway, because the same men faced each other "
                  "daily.",
             "eg": "Two firms in the same building settle a dispute far more "
                   "easily than two on different continents."},
        ],
        "apply":
            "To get something honoured, stop auditing the other person's "
            "character and count the rounds instead. Turn a single payment into "
            "monthly ones, split delivery into three stages, put the two of you "
            "somewhere you both have to keep showing up - once tomorrow holds "
            "the same two people, their arithmetic changes on its own. Then fix "
            "your own rule of response: never move first; if you are genuinely "
            "crossed, answer once, and only once; the moment they cooperate "
            "again, cooperate on your very next move, with no arrears and no "
            "ledger. Half of that rule on its own is either an invitation or a "
            "permanent feud.",
        "q": [
            "None of the leading programs was ever the first to defect.",
            "Hit back once, then come straight back. No ledger.",
            "It never outscored a single opponent and still finished first.",
            "A promise holds because of tomorrow's meeting, not his character.",
        ],
        "l": ["Thomas Schelling", "Han Feizi", "Maria Konnikova",
              "Robert K. Merton", "John Gottman"],
        "contrast": [
            {"n": "Han Feizi",
             "why": "Neither trusts human nature: Han Feizi holds reward and "
                    "punishment himself so that nobody dares defect, Axelrod "
                    "lengthens the relationship until nobody needs to - one runs "
                    "on power, the other on repetition"},
            {"n": "Thomas Schelling",
             "why": "Both answer why should I believe you: Schelling has you burn "
                    "your own way out so the promise is credible right now, "
                    "Axelrod says credibility depends on how many rounds are "
                    "still to come"},
        ],
    },
]

INTROS = {
    "axelrod": "Political scientist who ran two computer tournaments; the winner "
               "was four lines long - never defect first, answer once, return "
               "immediately",
}

SCENES = [
    ("I was betrayed", "At home", [
        ("He took a piece out of me. Do I hit back?",
         [("axelrod", "tit-for-tat")]),
    ]),
    ("Can I trust this person", "Dealing with people", [
        ("Do I go first and trust him once?",
         [("axelrod", "tit-for-tat")]),
    ]),
    ("I don't believe what my boss says", "Dealing with people", [
        ("He agreed this time. Will it hold next time?",
         [("axelrod", "shadow-of-the-future")]),
    ]),
    ("My partner and I are falling out", "Dealing with people", [
        ("After all this, can we still work together?",
         [("axelrod", "shadow-of-the-future")]),
    ]),
]

ASKS = {
    "axelrod/tit-for-tat":
        "He took a piece out of me. Do I hit back?",
    "axelrod/shadow-of-the-future":
        "He agreed this time. Will it hold next time?",
}
