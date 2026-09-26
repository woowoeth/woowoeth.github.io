# -*- coding: utf-8 -*-
"""Daily entry, day 17: Herbert Simon.

Picked by fan-out. 'Too many paths' and 'I can't keep up with the new thing'
were among the emptiest situations. What hangs under 'Too many paths' is
Boyd (to be or to do), Jobs (focus is saying no), Bismarck and Excellent
Sheep: cut, or ask what you really want. None of them says when to stop
comparing - set the line first, take the first option that clears it, and
move the line with how hard the search turns out to be. Under 'I can't keep
up' hang Bruce Lee (one kick practised ten thousand times) and
Csikszentmihalyi (the flow channel), which are about how to practise, not
about why more reading leaves you poorer. Simon's 1971 sentence on the
poverty of attention, with the design test that follows it, fills that.

Three stories, no overlap: the entry is the 1935 Milwaukee recreation
budget, the chapters are the house seller of 1955 and the late-1960s talk
of more information for decision makers.

Both situations already exist, so there is no SC_BOX here.
"""

ENTRIES = [
    {
        "c": "Learning and growth",
        "n": "Herbert Simon",
        "slug": "herbert-simon",
        "e": "United States · 1916-2001",
        "w": "Bounded rationality", "y": 1947,
        "d": "American social scientist, born in Milwaukee in 1916, with a "
             "doctorate in political science from Chicago. From 1949 he "
             "taught at the Carnegie Institute of Technology, later Carnegie "
             "Mellon, for over fifty years. Administrative Behavior (1947) "
             "became a classic of management; he shared the 1975 Turing "
             "Award with Allen Newell and won the 1978 Nobel prize in "
             "economics. All of it answers one question: how do people "
             "actually decide? His answer retired the all-knowing rational "
             "man. People try to reason, but lack the information and the "
             "computing power, so they do not pick the best option. They take "
             "the first one that is good enough.",
        "story":
            "In 1935, still an undergraduate at Chicago, he went home to "
            "Milwaukee to study how the city's public recreation programme "
            "divided its budget. The money had to be split between keeping "
            "up the playgrounds and paying the leaders who ran activities "
            "for children. The textbook said to split it until the last "
            "dollar did equal good on either side. Nobody he met thought that "
            "way. The people who looked after the grounds wanted more for "
            "the grounds; the people who ran activities wanted more leaders. "
            "Neither side was confused. Each saw the problem from inside its "
            "own patch. He later traced his whole subject back to that study.",
        "f": [
            {"n": "He replaced the rational man",
             "d": "Economics assumed a chooser who knows every option, can "
                  "work out every consequence, and picks the best. Simon's "
                  "people have incomplete information, limited computing "
                  "power and limited time, so their reasoning works inside "
                  "those bounds. He called it bounded rationality: reasoning "
                  "has a cost.",
             "eg": "A plan that three hours of meetings cannot settle is rarely "
                   "stuck because somebody is being unreasonable."},
            {"n": "Good enough, then stop",
             "d": "Since the best cannot be computed, people do something "
                  "else. They set an acceptable line, look at options one at "
                  "a time, take the first that clears it, and raise or lower "
                  "the line as the search proves easy or hard. He called it "
                  "satisficing.",
             "eg": "Choosing a builder, the first one whose price and "
                   "references both clear the line spares you meeting a "
                   "sixth."},
            {"n": "Where you stand is what you see",
             "d": "Milwaukee left him a second idea. A person deciding "
                  "inside an organisation takes the angle of the unit he "
                  "belongs to. Administrative Behavior gives this "
                  "identification its own treatment: it spares people from "
                  "weighing everything afresh, and hides whatever lies "
                  "outside their patch.",
             "eg": "When sales and engineering fight over the budget, neither "
                   "side is usually playing games."},
            {"n": "A wealth of information, a poverty of attention",
             "d": "In 1971 he wrote the lines quoted ever since: information "
                  "consumes the attention of its recipients, so a wealth of "
                  "information creates a poverty of attention. The question "
                  "for any new system is not how much it tells you, but how "
                  "much it keeps away.",
             "eg": "Someone getting hundreds of group messages a day gains "
                   "more by muting them than by learning to skim."},
            {"n": "He tested thinking on a computer",
             "d": "In 1955 and 1956 he, Newell and Cliff Shaw wrote a program "
                  "called the Logic Theorist and set it to prove theorems "
                  "from Principia Mathematica. It did not try every path, "
                  "only the few that looked promising. People think the same "
                  "way, he held: by selective search, not by exhausting the "
                  "options.",
             "eg": "An experienced engineer chasing a fault checks the two "
                   "likeliest places first, not line one onwards."},
        ],
        "apply":
            "If you are stuck between two or three decent options, don't go "
            "looking for a fourth today. Write down the three things you "
            "cannot do without, check each option against them, and take the "
            "first that clears all three. If none does, the line is too "
            "high: move it and check again. Keep a second job for your "
            "reading: go back over what you read this week, count the items "
            "that actually changed a decision, and drop half of the sources "
            "that supplied the rest. He used one test for both: your "
            "computing power and your attention are finite, so don't spend "
            "them on the chance that something better is still coming.",
        "q": [
            "You are not looking for the best. You want the first good enough.",
            "Reasoning costs computing power, and nobody has much.",
            "More information makes attention the thing that runs short.",
            "Where you stand is what you see.",
        ],
        "l": ["Thinking, Fast and Slow", "Charlie Munger", "Steve Jobs",
              "Cal Newport", "John Boyd"],
        "contrast": [
            {"n": "Steve Jobs",
             "why": "Both answer what to do when you want two things. Jobs "
                    "says to say no to a hundred good ideas and cut down to "
                    "the best one. Simon says the best one was never going "
                    "to be found: set a line and stop at the first option "
                    "that clears it. One cuts; the other stops."},
            {"n": "Cal Newport",
             "why": "Both say attention is being chopped up. Newport is "
                    "talking about you, and how to protect a stretch of time "
                    "nobody interrupts. Simon is talking about design: a new "
                    "tool or a new department must keep out more than it "
                    "lets in, or it is one more source you have to read."},
        ],
    },
]

INTROS = {
    "herbert-simon":
        "Winner of a Turing Award and a Nobel prize in economics, who "
        "spent his life asking how people actually decide - "
        "nobody picks the best, he found, they take the first good enough, "
        "and a flood of information leaves attention short",
}

SCENES = [
    ("Too many paths", "Looking back, moving on", [
        ("I keep thinking something better is still coming.",
         [("herbert-simon", "good-enough")]),
    ]),
    ("I can't keep up with the new thing", "AI arrived", [
        ("Something new appears every day and I'm scared of missing it.",
         [("herbert-simon", "poverty-of-attention")]),
    ]),
]

ASKS = {
    "herbert-simon/good-enough":
        "I keep thinking something better is still coming.",
    "herbert-simon/poverty-of-attention":
        "Something new appears every day and I'm scared of missing it.",
}
