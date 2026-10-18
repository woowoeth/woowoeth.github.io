# -*- coding: utf-8 -*-
"""Daily entry: Aristotle.

Picked by fan-out. The last eight are four Chinese and four foreign, so either
side was open. 'I was betrayed' (9 pieces, the emptiest) hangs Gottman on how
to repair, Konnikova on how not to manufacture trust, Han Xin and Li Ka-shing
on when to stop, Axelrod on tit for tat, Jin Wengong on the one who comes
back. Nothing on the question before all of those: what kind of friend was he,
and did he fake it or did I misjudge him.

Why he qualifies: one of the founders of Western philosophy and of most of the
sciences; the Nicomachean Ethics is the founding text of virtue ethics, and its
Books VIII and IX are the classic treatment of friendship.

Three stories, no overlap: the entry is the twenty years at the Academy and
his remark about a friend's theory; the chapters are the three kinds and the
two ways of being deceived. No sentence is quoted as his.
"""

ENTRIES = [
    {
        "c": "Reading people",
        "n": "Aristotle",
        "slug": "aristotle",
        "e": "Ancient Greece · 384–322 BC",
        "w": "Friendship", "y": -335,
        "d": "An ancient Greek philosopher, born in 384 BC in Stagira, in the "
             "kingdom of Macedon, and dead in 322 BC at Chalcis on Euboea. He "
             "entered Plato's Academy at seventeen and stayed about twenty "
             "years, later tutored Alexander, and in 335 BC founded the Lyceum "
             "in Athens. Two books of his Nicomachean Ethics are given to "
             "friendship. He does not first ask whether a friendship is noble; "
             "he asks what a given bond actually rests on, and what to do when "
             "it will not bear the weight.",
        "story":
            "When Plato died in 347 BC, Aristotle was thirty-seven and had "
            "spent about twenty years at the Academy. It passed to Plato's "
            "nephew Speusippus, and Aristotle left Athens. Later, criticising "
            "his teacher's theory of Forms in the Nicomachean Ethics, he "
            "admits the task is awkward, because the people who introduced "
            "Forms were friends of his. He writes it anyway, and says it is "
            "the truth that comes first.",
        "f": [
            {"n": "Ask what holds it up",
             "d": "He sorts friendship into three kinds: useful, pleasant, and for the person himself. The first two rest on benefit and enjoyment, so when those go the bond goes. Only the third rests on the person.",
             "eg": "Two people at the same dinner, one there for business, the other because they get on."},
            {"n": "Where the complaints come from",
             "d": "Grievances and reproaches, he says, arise mostly in friendships of utility, where each side feels it gives more and gets less. The sense of being short-changed is close to built in.",
             "eg": "At year end, each partner is sure they put in more."},
            {"n": "A friend who has changed: can he be saved?",
             "d": "Book IX asks whether to break with a friend who turns bad. His order is to ask first whether he can be brought back; if he can, help him mend his character, and end it only when he is past saving. Even then, leave some room for the old friendship.",
             "eg": "A colleague pads the numbers: say it once to his face, and if he does not stop, deal with him differently."},
            {"n": "Two ways of being deceived",
             "d": "If you took someone to like you for yourself when he wanted something else, you misjudged him. If he put on a show to deceive you, you may complain, and he says with more right than against a counterfeiter, since more was taken.",
             "eg": "\"He never said he admired me\" and \"he called me his closest friend, then sold what I told him\" are not the same case."},
        ],
        "apply": "Take one friend who has left you cold. Write two lines: what was this bond resting on, and did I misjudge him or did he put on a show? Only after that decide whether to get in touch; do not decide in the heat of it.",
        "q": [
            "When the support goes, the bond goes.",
            "Did he fool me, or did I misjudge him?",
            "Parting does not make the old years unreal.",
        ],
        "l": ["John Gottman", "Maria Konnikova", "The Analects"],
        "contrast": [
            {"n": "John Gottman", "why": "Both look at a relationship that has turned. Gottman teaches how to repair it so the two can stay; Aristotle first asks whether it can be saved at all, and if not, to own that and part"},
            {"n": "Robert Axelrod", "why": "Both ask what to do after being burned. Axelrod looks at how you respond to the other side in a repeated game, behaviour; Aristotle first asks what kind of bond this was, what held it up"},
        ],
    },
]

INTROS = {
    "aristotle":
        "Ancient Greek philosopher, author of the Nicomachean Ethics - he "
        "spent two books taking friendship apart: after a betrayal, first "
        "ask whether you were the same kind of friend; when a friend "
        "changes, when to help and only then when to part",
}

SCENES = [
    ("I was betrayed", "At home", [
        ("I treated him as a friend; he treated me as useful.",
         [("aristotle", "three-kinds")]),
        ("He's changed. Do I still count him a friend?",
         [("aristotle", "when-a-friend-turns")]),
    ]),
]

ASKS = {
    "aristotle/three-kinds": "I treated him as a friend; he treated me as useful.",
    "aristotle/when-a-friend-turns": "He's changed. Do I still count him a friend?",
}
