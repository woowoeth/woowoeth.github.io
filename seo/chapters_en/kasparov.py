# -*- coding: utf-8 -*-
"""Garry Kasparov — English."""

PARENT = {
    "name": "Garry Kasparov",
    "slug": "kasparov",
    "blurb": "Deep read",
    "items": [
        {"k": "advanced-chess", "n": "After losing to it, he changed the rules",
         "w": "Let people bring machines to the board", "ready": True,
         "line": "Stop competing on who calculates faster"},
        {"k": "process-beats-both",
         "n": "The winner wasn't the best human or the best machine",
         "w": "It was the pair with the best process", "ready": True,
         "line": "Two amateurs beat the grandmasters"},
        {"k": "excuses-cost-years",
         "n": "He spent years arguing the match didn't count",
         "w": "Conceding is cheaper than appealing", "ready": True,
         "line": "IBM dismantled Deep Blue. He had no opponent left"},
    ],
}

CHAPTERS = [
    {
        "k": "advanced-chess",
        "n": "After losing to it, he changed the rules",
        "w": "Let people bring machines to the board",
        "src": "The six-game rematch, New York, May 1997; the first Advanced "
               "Chess event, León, 1998",
        "dek": "When a machine wins at your craft, what's left of it. Why "
               "Kasparov invited the computer onto his own board.",
        "story":
            "He beat Deep Blue in Philadelphia in 1996. In the New York "
            "rematch of May 1997 it beat him 3.5–2.5, the first time a world "
            "champion lost a formal match to a machine. A year later he "
            "staged an event in León under new rules: ==each side brought a "
            "computer to the board== and could consult it at any time. He "
            "called it Advanced Chess. The reasoning was plain — calculation "
            "was already lost, so stop competing on who calculates faster.",
        "f": [
            {"n": "First identify what's no longer worth competing on",
             "d": "The day machines won on depth of calculation, the 'who "
                  "sees furthest' track closed. Training on a closed track "
                  "has no exit however hard you train. The first step isn't "
                  "redoubling effort; it's striking the lost item off your "
                  "own list of what you're worth.",
             "eg": "Speed of looking things up, of arithmetic, of making a "
                   "sentence read properly — none of these are things to "
                   "compete on now."},
            {"n": "Change the rules, not the effort",
             "d": "He didn't train harder and he didn't switch fields. He "
                  "changed what the contest permits. When a tool matches an "
                  "ability, the valuable position moves to how the tool gets "
                  "used — and somebody has to define that position before it "
                  "exists.",
             "eg": "Not 'I'll write faster than it' but 'I decide what this "
                   "piece is and which parts are whose'."},
            {"n": "Inviting the tool in holds better than keeping it out",
             "d": "A contest that bans tools survives only on enforcement, "
                  "and collapses the moment enforcement slips. A contest that "
                  "permits them is measuring something else — something that "
                  "doesn't expire as tools improve, because it improves "
                  "alongside them.",
             "eg": "You can ban calculators in an exam. You can't hold that "
                   "line at work, and the sneaks end up ahead."},
        ],
        "apply":
            "Where you are: a core skill in your field has been matched by a "
            "tool, and you're still training on the old track.\n"
            "Ask first: which item in my field is now clearly lost to the "
            "tool? Strike it out — what's left that it can't replace?\n"
            "Where it goes wrong: hearing 'if you can't win, don't train' — "
            "he didn't stop playing chess, he stopped competing on "
            "calculation; and changing the rules isn't open to everyone. "
            "First you have to know the old game well enough to see them.",
        "q": [
            "Calculation was already lost, so stop competing on calculation.",
            "The first step isn't more effort. It's striking out what's lost.",
            "A contest that bans tools survives only while enforcement holds.",
        ],
    },
    {
        "k": "process-beats-both",
        "n": "The winner wasn't the best human or the best machine",
        "w": "It was the pair with the best process",
        "src": "The 2005 PAL/CSS freestyle tournament; Kasparov, Deep "
               "Thinking, 2017",
        "dek": "What human plus tool is actually good at. Why two amateurs "
               "won a tournament where everyone could use a computer.",
        "story":
            "A freestyle online tournament in 2005 admitted grandmasters and "
            "supercomputers, with humans and machines free to team up. "
            "==The winners were two American amateurs==, Steven Cramton and "
            "Zackary Stephen, running three ordinary PCs. Their method was to "
            "ask all three and apply their own judgement only where the three "
            "disagreed. Kasparov later compressed it: a weak human plus a "
            "machine plus a good process beats a strong human plus a machine "
            "plus a poor one.",
        "f": [
            {"n": "The value moves from answering well to asking well",
             "d": "Where all three machines return the same answer, adding a "
                  "person adds nothing. The human value concentrates entirely "
                  "in the few moves where they disagree — finding the "
                  "disagreement and judging which side to believe. That is a "
                  "different job from playing chess.",
             "eg": "Two tools give different conclusions and you can say why "
                   "you trust one. That's your work."},
            {"n": "Process makes up for ability; ability can't make up for process",
             "d": "The amateurs won on a stable checking routine. The "
                  "grandmasters lost by treating the machine as a reference "
                  "and calling it themselves at the end. The first doesn't "
                  "depend on how you feel that day; the second does. That is "
                  "how weaker players beat stronger ones.",
             "eg": "Same tool: one person asks three times and cross-checks, "
                   "the other asks once and ships it."},
            {"n": "Don't keep only one tool",
             "d": "With one machine there is no disagreement to look at — you "
                  "either believe all of it or none of it. Three aren't "
                  "valuable because the compute adds up. They're valuable "
                  "because the places they disagree mark exactly where the "
                  "problem is genuinely hard.",
             "eg": "Ask two different tools the same question. Where the "
                   "answers fight is where you should be thinking."},
        ],
        "apply":
            "Where you are: you already use the tools, and what you get out "
            "looks like what everyone else gets out of the same ones.\n"
            "Ask first: do I have a fixed way of checking? Do I ever put the "
            "same question to a second tool?\n"
            "Where it goes wrong: hearing it as 'just open more tools' — they "
            "won on the checking routine, not the count; and don't skip the "
            "fundamentals because amateurs won. Recognising a real "
            "disagreement takes knowing the subject.",
        "q": [
            "Where all three agree, adding a person adds nothing.",
            "The human value sits in the few moves where they disagree.",
            "Process makes up for ability. Ability can't make up for process.",
        ],
    },
    {
        "k": "excuses-cost-years",
        "n": "He spent years arguing the match didn't count",
        "w": "Conceding is cheaper than appealing",
        "src": "His 1997 post-match statement and rematch demand; Deep "
               "Thinking, 2017",
        "dek": "What the first year after being replaced usually looks like. "
               "What he did, and what he said twenty years later.",
        "story":
            "After the loss he told the press that IBM had used human "
            "intervention mid-match, and demanded a rematch. IBM refused, and "
            "dismantled Deep Blue — leaving him without even an opponent to "
            "play again. He told that version for years. By the time he wrote "
            "Deep Thinking in 2017 he had withdrawn it himself: ==Deep Blue "
            "won, and that is all==. The 1997 explanations were what he "
            "couldn't accept at the time.",
        "f": [
            {"n": "Appealing and moving on can't run in parallel",
             "d": "The effort to prove that match didn't count and the effort "
                  "to work out what to train next come out of the same person "
                  "in the same stretch of time. The first buys no new skill "
                  "even when it wins.",
             "eg": "Six months proving the tool was used wrong is six months "
                   "not spent learning to use it right."},
            {"n": "The other side isn't waiting for your post-mortem",
             "d": "IBM dismantled the machine, which shows the pattern: "
                  "whatever replaced you doesn't need your agreement and "
                  "won't hold a rematch open for you. Hoping to end this by "
                  "getting the other side to concede is usually a wait with "
                  "no end.",
             "eg": "A role is cut and it's cut. Nobody comes back to debate "
                   "whether cutting it was right."},
            {"n": "Conceding isn't surrendering",
             "d": "The same year he accepted the loss he was staging a "
                  "tournament under new rules. Accepting a result and giving "
                  "up the craft are two different things — accepting it first "
                  "is what freed his hands to change the track. Nobody "
                  "swallowing their pride changes anything.",
             "eg": "'The machine is faster at this than me' and 'my field is "
                   "done with me' are not the same sentence."},
        ],
        "apply":
            "Where you are: a tool or a new method has beaten you, and most "
            "of your energy is going into explaining that it's unfair or that "
            "it isn't actually good.\n"
            "Ask first: how many times this month have I said it's unfair? In "
            "the same month, what new thing did I practise?\n"
            "Where it goes wrong: hearing it as 'no feelings allowed' — it "
            "took him twenty years. The point is not to let the appeal become "
            "the only thing you're doing, not to demand you accept it today.",
        "q": [
            "Whatever replaced you does not need your agreement.",
            "Proving it didn't count and deciding what to train next cost the "
            "same hours.",
            "Accepting the result and giving up the craft are different "
            "things.",
        ],
    },
]
