# -*- coding: utf-8 -*-
"""Edward Deci — English.

The English reader may already know "intrinsic motivation" as a phrase from
a management book, usually meaning "people like doing things they like".
The first page is there to show the experiment that gave the phrase teeth:
a dollar a puzzle, eight free minutes, and a group that played less once the
money stopped. The second page takes his reframing of the motivation
question, which is usually heard as "be nice to people" and is in fact three
concrete moves.

Sources: "Effects of Externally Mediated Rewards on Intrinsic Motivation",
Journal of Personality and Social Psychology, 1971; Deci and Ryan,
Intrinsic Motivation and Self-Determination in Human Behavior, 1985; the
nursery-school certificate study is Lepper, Greene and Nisbett, 1973, and is
named as theirs. Why We Do What We Do (with Richard Flaste), 1995; Deci,
Eghrari, Patrick and Leone, Journal of Personality, 1994; Ryan and Deci,
American Psychologist, 2000. The "better question" line is paraphrased, not
quoted, because we could not pin the exact wording to a page.
"""

PARENT = {
    "name": "Edward Deci",
    "slug": "deci",
    "blurb": "Deep read",
    "items": [
        {"k": "paid-to-play", "n": "Pay him, and he stops playing",
         "w": "Pay for something a person loved doing, and the love is what "
              "you end up buying",
         "ready": True,
         "line": "A dollar a puzzle, and once the dollars stopped, they left "
                 "the puzzles alone"},
        {"k": "conditions-not-carrots",
         "n": "Stop asking how to motivate him",
         "w": "What you can change is not the person but the place he works in",
         "ready": True,
         "line": "A reason, a choice and someone who cares, and people move "
                 "without a push"},
    ],
}

CHAPTERS = [
    {
        "k": "paid-to-play",
        "n": "Pay him, and he stops playing",
        "w": "Pay for something a person loved doing, and the love is what "
             "you end up buying",
        "src": "\"Effects of Externally Mediated Rewards on Intrinsic "
               "Motivation\", Journal of Personality and Social Psychology, "
               "1971; Deci and Ryan, Intrinsic Motivation and "
               "Self-Determination in Human Behavior, 1985",
        "dek": "Nobody praises me, nobody pays me, and I can't make myself "
               "start. When did the drive get swapped out?",
        "story":
            "In 1971 Deci published an experiment. College students came in "
            "three times, in two groups, to work on a block puzzle called "
            "Soma. In the second session one group was paid a dollar for "
            "each puzzle solved; the other got nothing. Every session he "
            "found a reason to leave the room for eight minutes, with "
            "magazines on the table, and those minutes were what he measured. "
            "In the third session he told the paid group there was no more "
            "money. ==In the eight free minutes they now spent less time on "
            "the puzzles than they had at the start.== The unpaid group "
            "barely changed.",
        "f": [
            {"n": "The reason moved outside",
             "d": "Deci borrowed Richard deCharms's idea of where people feel "
                  "the cause of their actions sits. Doing something you enjoy, "
                  "the reason is inside you. Paid by the piece, you start to "
                  "feel you do it for the money. Stop the money and the inside "
                  "reason does not come back.",
             "eg": "A child who loved drawing enters a few ranked contests and "
                   "stops drawing at home."},
            {"n": "The harm is in the deal struck in advance",
             "d": "In 1973 Mark Lepper and colleagues at Stanford tried it in "
                  "a nursery school. Children promised a certificate for "
                  "drawing drew less in free play a week or two later. "
                  "Children handed the same certificate as a surprise did not.",
             "eg": "Finish your homework and you get half an hour of games. "
                   "Homework has become the price of the games."},
            {"n": "Some praise informs, some praise controls",
             "d": "In his own studies, spoken praise did not cut the time "
                  "people chose to spend on the task; it raised it. Deci and "
                  "Ryan later said a reward has two faces: one tells you how "
                  "you did, one steers what you do. Whichever feels heavier "
                  "decides which way it pushes.",
             "eg": "'Your argument is really clear here' tells. 'Do it my way "
                   "and you did well' steers."},
        ],
        "q": [
            "What you do for the prize stops when the prize does.",
            "The prize is not the harm. The deal made in advance is.",
            "Is that praise telling you something, or steering you?",
        ],
        "apply":
            "Where you are: all your life there were grades, certificates "
            "and bonuses, and now nobody hands them out and you don't feel "
            "like doing anything.\n"
            "Ask first: is there any part of this I would do with nobody "
            "watching and nobody paying, and when did I last do it that "
            "way?\n"
            "Where it goes wrong: reading it as 'all rewards are bad'. The "
            "damage came from pay agreed in advance, per piece. Keep the "
            "salary and the feedback; just don't let them become your only "
            "reason.",
    },
    {
        "k": "conditions-not-carrots",
        "n": "Stop asking how to motivate him",
        "w": "What you can change is not the person but the place he works in",
        "src": "Deci and Flaste, Why We Do What We Do, 1995; Deci, Eghrari, "
               "Patrick and Leone, Journal of Personality, 1994; Ryan and "
               "Deci, American Psychologist, 2000",
        "dek": "They do what they are told and nobody takes the lead. If you "
               "want people to want it themselves, what can you actually "
               "change?",
        "story":
            "In 1995 Deci wrote a book for general readers with the "
            "journalist Richard Flaste. Parents ask how to make children "
            "study, managers how to make staff try harder, teachers how to "
            "make pupils care. It is one question: how do I motivate him? "
            "Deci's point was that the question already treats the other "
            "person as something to be pushed, and whatever is pushed halts "
            "once the pushing does. ==The better question is what conditions "
            "you can set up in which people will motivate themselves.== With "
            "Richard Ryan he named three.",
        "f": [
            {"n": "Autonomy is not being left alone",
             "d": "The first is autonomy. Deci kept insisting it is neither "
                  "independence nor permissiveness; it is the sense that what "
                  "you are doing is something you endorse. His studies used "
                  "three moves: give the reason, acknowledge the reluctance, "
                  "offer a choice wherever there is one.",
             "eg": "The report is due Friday. Say why Friday, then let him "
                   "decide which part to write first."},
            {"n": "Competence: a reachable stretch, feedback about the work",
             "d": "The second is competence. People take on what they feel "
                  "able to do well and still find a little hard. Feedback "
                  "should say what worked and what fell short; feedback used "
                  "to rank people pushes them back to working for the score.",
             "eg": "Give a new hire a first task they can finish with effort, "
                   "neither the hardest nor the dullest."},
            {"n": "Relatedness: first the person, then the rule",
             "d": "The third is relatedness. Plenty of tasks are dull: "
                  "tidying, revising, filling in forms. Deci and Ryan called "
                  "the slow business of making them your own internalisation, "
                  "and it mostly happens beside someone who clearly cares "
                  "about you.",
             "eg": "A child tidies his room less because the argument landed "
                   "than because someone tidied it with him a few times."},
        ],
        "q": [
            "A pushed person stops when the hand lets go.",
            "A reason and a choice go further than a bonus.",
            "We take on a rule once we have taken on the person.",
        ],
        "apply":
            "Where you are: the people you lead do what they are told and "
            "nothing more; you have raised the bonus and tightened the "
            "reviews, and nothing changed.\n"
            "Ask first: have I told him why this matters, and have I left "
            "him the part he could decide for himself?\n"
            "Where it goes wrong: reading it as 'let him choose everything'. "
            "Deadlines and quality bars stay. What changes is how you say it "
            "and what you leave open: the reason first, the reluctance "
            "acknowledged, then a choice inside the line.",
    },
]
