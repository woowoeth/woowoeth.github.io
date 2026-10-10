# -*- coding: utf-8 -*-
"""Mozi, added for the Strategy and competition shelf (2026-10-10).

His standing: founder of the Mohist school, the main rival of the Confucians
in the Warring States period; his book was the other great school of the age.
This page leaves the doctrine of impartial care aside and takes three working
methods from stories in the Mozi (Gongshu, Gengzhu, Fei Ming I): how he made
a king call off a war without winning the argument, how he answered a pupil
who asked why he was scolded hardest, and the three tests he set for any claim.

What it fills: "Do I jump in now" (AI arrived) had no tool for checking a
claim you cannot test yourself; "Someone is ahead of me" had nothing on being
singled out for blame.

All quoted lines are our own renderings, checked against the Chinese text on
Wikisource.
"""

ENTRIES = [
    {
        "c": "Strategy and competition",
        "n": "Mozi",
        "slug": "mozi",
        "e": "Spring and Autumn to Warring States · Lu · c.470–391 BC",
        "w": "Against war",
        "y": -450,
        "d": "Philosopher at the turn of the Spring and Autumn and Warring "
             "States periods, founder of the Mohist school, from the state "
             "of Lu. He taught impartial care and opposed offensive war, and "
             "his disciples read books and also knew how to defend a city. "
             "Several stories in the Mozi are about one thing: how to get "
             "someone who does not want to listen to hear you. This page "
             "takes three of his methods: when he agrees with you and still "
             "will not stop, let him work out that he cannot win; when you "
             "are scolded hardest, ask what the scolder has handed you; and "
             "before believing a new claim, put it through three tests.",
        "story": "On the way home from Chu, Mozi passed through Song in the "
                 "rain and tried to shelter under the gate of a village "
                 "lane. The gatekeeper would not let him in. No one in Song "
                 "knew the city had just been saved by him. The book "
                 "closes the story with a line: whoever works in the "
                 "unseen, no one knows his credit; whoever fights in the "
                 "open, everyone sees.",
        "f": [
            {"n": "Let him do the sum",
             "d": "The king of Chu said the argument was well put and still meant to attack. Mozi laid down his belt as a wall and had the engineer try nine attacks. After the ninth the king agreed to stop.",
             "eg": "Your boss nods and keeps the schedule. Put the rival's shipped features on the table and ask which ones we can beat."},
            {"n": "Hard on you because the load is heavy",
             "d": "A pupil he scolded asked if he was worse than the others. Mozi asked back: climbing a mountain, would you drive the horse or the sheep? The horse can bear it, so the horse is the one he drove.",
             "eg": "The person whose draft is cut hardest is often the one the editor wants on stage."},
            {"n": "Three tests for a new claim",
             "d": "When some said fate fixed everything and effort was pointless, he did not first argue right and wrong. He set three tests: where it comes from, what eyewitnesses say, what it does for people.",
             "eg": "A tool everyone praises: find the precedent, then someone who has used it three months, then try it small for two weeks."},
        ],
        "apply": "Pick something you are arguing, being scolded for, or "
                 "being pushed to believe, and write one line each: what I "
                 "could lay in front of him so he does the sum himself; who "
                 "gave the heaviest work to whom; and the origin, the "
                 "eyewitnesses and the use of the claim. All three of his "
                 "methods do the same thing: give the other person "
                 "something he can check himself.",
        "q": [
            "A claim needs three tests.",
            "And I thought you could bear it too.",
            "Whoever works in the unseen, no one knows his credit.",
        ],
        "l": ["Sun Tzu", "Mencius", "Han Feizi", "Xunzi"],
        "contrast": [
            {"n": "Sun Tzu", "why": "Sun Tzu teaches how to win: work out the odds first, then move. Mozi teaches how to make the other side afraid to start: put the odds in front of him and ask him to work them out"},
            {"n": "Mencius", "why": "Mencius condemned the Mohists for impartial care, saying it left a man with no father. Both lived by persuading rulers: Mencius first showed the ruler righteousness, Mozi first showed him the bill"},
        ],
    },
]

INTROS = {
    "mozi": "Founder of the Mohist school, the main rival of the "
            "Confucians. To stop Chu attacking a small neighbour he walked "
            "ten days and nights to its capital, laid down his belt as a "
            "city wall and had the engineer attack it. He also set three "
            "tests that any claim had to pass.",
}

SCENES = [
    ("I'm up against something much bigger", "Facing an opponent", [
        ("He agrees I'm right and still won't stop.",
         [("mozi", "belt-and-sticks")]),
    ]),
    ("Someone is ahead of me", "How you're doing", [
        ("He only ever scolds me, never the others. Does he think less of me?",
         [("mozi", "the-good-horse")]),
    ]),
    ("Do I jump in now", "AI arrived", [
        ("Everyone says it works and I can't test it. What do I check?",
         [("mozi", "three-tests")]),
    ]),
]

ASKS = {
    "mozi/belt-and-sticks": "He agrees I'm right and still won't stop.",
    "mozi/the-good-horse": "He only ever scolds me, never the others. Does he think less of me?",
    "mozi/three-tests": "Everyone says it works and I can't test it. What do I check?",
}
