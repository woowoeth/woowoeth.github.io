# -*- coding: utf-8 -*-
"""Aristotle — English.

English readers know Aristotle as the logic-and-categories man, or the
"golden mean". This page uses a less-quoted part of the Nicomachean Ethics:
Books VIII and IX on friendship, taken as a tool for someone who has just been
let down. Chapter one is the three kinds of friendship (VIII.3-4, VIII.13);
chapter two is whether to end a friendship once a friend has changed (IX.3).

No sentence here is put in quotation marks as his; the wording is ours, and
translations differ. We draw on his way of taking a friendship apart, not on
his views about slaves or women.
"""

PARENT = {
    "name": "Aristotle",
    "slug": "aristotle",
    "blurb": "Deep read",
    "items": [
        {"k": "three-kinds", "n": "Not the Same Kind of Friend",
         "w": "A bond falls apart when the thing holding it up is gone",
         "ready": True,
         "line": "He splits friendship into three kinds, and only one is for the person himself; in the other two the bond goes when the support goes"},
        {"k": "when-a-friend-turns", "n": "When a Friend Has Changed",
         "w": "First decide whether he put on a show or you misjudged him, then decide whether to end it",
         "ready": True,
         "line": "He says being fooled by a faked friend gives you more right to complain than being fooled by counterfeit coin, because more was taken"},
    ],
}

CHAPTERS = [
    {
        "k": "three-kinds", "n": "Not the Same Kind of Friend",
        "w": "A bond falls apart when the thing holding it up is gone",
        "src": "Nicomachean Ethics, Book VIII chs. 3-4 (1156a-b) and ch. 13 (1162b); paraphrase, not quotation",
        "dek": "First work out which kind of friend he was. Aristotle asks whether the bond came apart because he changed, or because it was never what you thought.",
        "story":
            "In Book VIII of the Nicomachean Ethics, Aristotle sorts friendship "
            "into three kinds: people who befriend you because you are useful, "
            "because you are pleasant company, or because they admire who you "
            "are. In the first two, he says, they do not love the person himself "
            "but what the person brings, so when the benefit goes or the "
            "pleasure fades, the bond goes with it. ==Only the third is for the "
            "person's own sake, and so only the third holds up over time.== He "
            "adds that complaints and score-keeping turn up almost entirely in "
            "the first kind.",
        "f": [
            {"n": "Three bonds, three supports",
             "d": "A useful bond rests on the benefit, a pleasant one on the enjoyment, and only the third rests on the person. When the support goes, the bond falls. Sometimes someone wronged you; sometimes the thing holding it up has simply left.",
             "eg": "Two people grow close over one project; when it folds, the lunches stop too."},
            {"n": "Most complaints come from the useful kind",
             "d": "He notes that grievances and reproaches arise mostly in friendships of utility, which is no surprise: each side feels it gives more and gets less. In that kind of bond, the sense of being short-changed is practically built in.",
             "eg": "A year into running a shop together, each partner is sure they are the one doing more."},
            {"n": "Name the kind before you name the wrong",
             "d": "If you thought it was the third kind and he only ever meant the first, that gap is where the sting comes from. Whether he lied to you is a separate question. Whether you took a transaction for a friendship comes first.",
             "eg": "His warmth always showed up when you held something he needed. You were probably in the first kind all along."},
        ],
        "q": [
            "When the support goes, the bond goes.",
            "Complaints cluster in bonds built on use.",
            "Name the kind before you name the wrong.",
        ],
        "apply":
            "Where you are: You feel betrayed, but looking back he was warmest when he needed something from you.\n"
            "Ask first: What was holding this bond up? What was it on his side, and what on mine? Write both down and set them side by side.\n"
            "Where it goes wrong: Using it to say he was only using you, so you had it coming. He does not say that. He says sort it first, so that what you expect and how you guard yourself stop being out of step. Being used is still being used, whatever you call it.",
    },
    {
        "k": "when-a-friend-turns", "n": "When a Friend Has Changed",
        "w": "First decide whether he put on a show or you misjudged him, then decide whether to end it",
        "src": "Nicomachean Ethics, Book IX ch. 3 (1165b-1166a); paraphrase, not quotation",
        "dek": "He has changed, so what now? Aristotle asks when a friendship should end, and on what grounds.",
        "story":
            "In Book IX Aristotle asks a very practical question: if a friend "
            "turns bad, must you stay his friend? He first separates two ways "
            "of being deceived. If you assumed he liked you for your character "
            "when he was after something else, the mistake is yours. But if he "
            "put on a show to fool you, you have every right to complain, more "
            "right than against someone who passes counterfeit coin, because "
            "what was taken from you is worth more. ==First decide whether you "
            "misjudged him or he deceived you; only then decide whether to end "
            "it.==",
        "f": [
            {"n": "Two ways of being fooled",
             "d": "If you misread him, the fault lies in treating something he never said as a promise. If he put on a front, the fault is his. Knowing which tells you whom to be angry with, and what to change next time.",
             "eg": "You assumed he admired you; he never said so, he just liked talking about the project."},
            {"n": "Rescue before rupture",
             "d": "His order is: first ask whether the person can be brought back. If he has merely drifted and can be recovered, help him mend his character before anything else, which he thinks closer to friendship than helping with money. Only when he is past saving do you end it.",
             "eg": "A colleague starts padding numbers: say it to his face once; if he carries on, deal with him differently."},
            {"n": "Keep a record of the old bond",
             "d": "When you do part, he says to allow something for the sake of the past friendship, unless the other person has become wicked to an extreme. That is not softness; it admits that something real once existed between you.",
             "eg": "Former partners who still nod in the street and do not run each other down."},
        ],
        "q": [
            "Did he fool me, or did I misjudge him?",
            "Help the one who can be saved before you cut him off.",
            "Parting does not make the old years unreal.",
        ],
        "apply":
            "Where you are: A friend has left you cold and you are wondering whether to delete him from your life.\n"
            "Ask first: Did he put on a show to fool me, or did I misread him? Can he still be brought back, or is he past saving? Write down both answers.\n"
            "Where it goes wrong: Using it to say he fooled you but you once were friends, so you must forgive. He speaks of leaving some room, not of letting him off; where someone faked it to deceive you, he thinks your complaint is fair.",
    },
]
