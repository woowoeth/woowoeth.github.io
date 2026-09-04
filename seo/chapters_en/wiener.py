# -*- coding: utf-8 -*-
"""Norbert Wiener — English."""

PARENT = {
    "name": "Norbert Wiener",
    "slug": "wiener",
    "blurb": "Deep read",
    "items": [
        {"k": "wrote-to-the-union", "n": "He wrote to the union first",
         "w": "Before automation landed", "ready": True,
         "line": "The man who built it warned the people it would displace"},
        {"k": "human-use", "n": "What a machine can do, and what to give it",
         "w": "Two separate questions", "ready": True,
         "line": "Don't use people to do a machine's work"},
        {"k": "feedback-not-command", "n": "Control is a loop, not an order",
         "w": "Seeing the result beats issuing instructions", "ready": True,
         "line": "An action with no feedback is only repetition"},
    ],
}

CHAPTERS = [
    {
        "k": "wrote-to-the-union",
        "n": "He wrote to the union first",
        "w": "Before automation landed",
        "src": "Wiener's 1949 letter to Walter Reuther of the UAW; The Human "
               "Use of Human Beings, 1950",
        "dek": "Is there a move to make before a technology reaches you? What "
               "the man who built it did first.",
        "story":
            "Cybernetics was published in 1948, and Wiener was the person who "
            "put machine control into the world. The next year he did "
            "something nobody was doing: ==he wrote to Walter Reuther, head "
            "of the United Auto Workers==, saying automation would displace "
            "assembly-line workers on a large scale, that he was unwilling "
            "for this to happen with no preparation, and that the union "
            "should get involved early. In 1950 he turned the same worry into "
            "a book.",
        "f": [
            {"n": "The people who see it coming usually aren't hit yet",
             "d": "The year Wiener wrote, automation wasn't deployed and "
                  "nobody had lost a job. Precisely because it hadn't landed, "
                  "there was time to arrange something. Once it lands you "
                  "only get to react; there is no room left to prepare.",
             "eg": "The stretch while you still have work and haven't been "
                   "cut is the only window you get to plan in."},
            {"n": "Find people in the same position before you find answers",
             "d": "He didn't start by writing a survival guide for workers. "
                  "He went to the people who were already organised. One "
                  "person carrying this kind of shock has almost no leverage; "
                  "tens of thousands do. Making contact comes before working "
                  "it out.",
             "eg": "Finding people in your field already dealing with it "
                   "beats sitting alone devising a strategy."},
            {"n": "The people pushing it and the people hit by it aren't two groups",
             "d": "He was both the inventor and the person raising the alarm, "
                  "and in him those didn't conflict. The tool you use every "
                  "day — the better you get with it, the sooner you can see "
                  "which tasks it will take. Those are exactly the ones to "
                  "prepare for.",
             "eg": "The work you're saving yourself with it is work somebody "
                   "else still eats from."},
        ],
        "apply":
            "Where you are: something is spreading through your field, it "
            "hasn't reached your income yet, and you plan to wait and see.\n"
            "Ask first: which task of mine can it already do? Who in my field "
            "have I actually talked to about it?\n"
            "Where it goes wrong: reading it as a call to oppose things "
            "early — he went to the union to move the preparation forward, "
            "not to block automation; and this isn't personal heroism. His "
            "first move was to find people already organised.",
        "q": [
            "Once it lands you only get to react. There is no room to plan.",
            "Finding people in the same position comes before working it out.",
            "The work you save with it is work somebody else eats from.",
        ],
    },
    {
        "k": "human-use",
        "n": "What a machine can do, and what to give it",
        "w": "Two separate questions",
        "src": "The Human Use of Human Beings, 1950",
        "dek": "Which work belongs to a tool and which doesn't. Why Wiener "
               "said capability doesn't settle it.",
        "story":
            "Through The Human Use of Human Beings, Wiener keeps returning to "
            "one point: ==what a machine is capable of and what people are "
            "for are two independent questions==. Whether a machine can do a "
            "task is technical. What is left of the person once you hand it "
            "over is a different question, and the answer isn't "
            "automatically good. What worried him wasn't machines getting "
            "stronger. It was people being arranged to do the machine's kind "
            "of work: repetitive, judgement-free, instruction-following.",
        "f": [
            {"n": "'It can' does not imply 'it should'",
             "d": "Tool capability and division of labour are separate "
                  "layers. Hand over everything it can do and what's left "
                  "is often the scraps it can't do and you learn nothing "
                  "from. What should go is the repetition, not the "
                  "judgement.",
             "eg": "Letting it draft is fine. Letting it decide what the "
                   "piece is arguing hands over the wrong half."},
            {"n": "The fear is people used as machines",
             "d": "Wiener's worry ran the other way round. He wasn't afraid "
                  "machines would be like people; he was afraid people would "
                  "be arranged like machines — executing, not judging, not "
                  "knowing why. Those roles go first, because they were "
                  "already designed in a machine's shape.",
             "eg": "A job that works a ticket queue and never asks why is in "
                   "the first batch automation takes."},
            {"n": "Keep the part where you decide",
             "d": "Once the repetition is handed over, what has to remain is "
                  "the stretch that needs a call made. Otherwise you gave "
                  "away repetition and kept repetition. Judgement doesn't get "
                  "cheaper as the tools improve. It gets dearer.",
             "eg": "The tool gives you three options. Which one and why is "
                   "the step you can't also hand over."},
        ],
        "apply":
            "Where you are: you're shifting work onto a tool and can't say "
            "which part should go and which shouldn't.\n"
            "Ask first: am I handing over the repetition or the judgement? "
            "After it's gone, does anything left on my desk require a "
            "decision?\n"
            "Where it goes wrong: using it as grounds for distrusting tools "
            "and doing everything yourself — he objected to handing over the "
            "judgement, not the repetition; and it isn't a list of things "
            "machines may not touch. He's describing a division of labour.",
        "q": [
            "What a machine can do and what people are for are separate "
            "questions.",
            "He feared people being arranged like machines, not machines "
            "resembling people.",
            "Hand over the repetition. Not the judgement.",
        ],
    },
    {
        "k": "feedback-not-command",
        "n": "Control is a loop, not an order",
        "w": "Seeing the result beats issuing instructions",
        "src": "Cybernetics, 1948",
        "dek": "Why the thing you carefully explained still comes back wrong. "
               "How Wiener defined control instead.",
        "story":
            "Cybernetics defines control not as issuing an instruction but as "
            "using the actual result to correct the next move — the feedback "
            "loop. Wiener's example is reaching for a cup: the eyes keep "
            "reporting the gap between hand and cup, and the hand corrects as "
            "it travels. ==Cut that report and the movement immediately goes "
            "off==, however well it was aimed to begin with. Machines and "
            "living things, he said, obey the same thing here.",
        "f": [
            {"n": "An instruction with no report back isn't control",
             "d": "However clearly you explained it, without a channel "
                  "carrying the actual result back you hold an intention, not "
                  "control. Things come back wrong not because people don't "
                  "listen but because the loop is cut and nobody can tell how "
                  "far off it has drifted.",
             "eg": "Brief it and wait for delivery, never seeing the thing "
                   "in between, and what arrives will not be what you "
                   "pictured."},
            {"n": "The report has to arrive while it can still be changed",
             "d": "Feedback later than the correctable window is worthless. "
                  "The value of a loop isn't whether it exists but how often "
                  "it reports — weekly and daily differ by an order of "
                  "magnitude in how much drift can still be pulled back.",
             "eg": "Finding out at month end that the month went wrong means "
                   "the month is already spent."},
            {"n": "Practising alone runs on the same rule",
             "d": "Stuck on a skill is usually not a shortage of practice. "
                  "It's the absence of any mechanism reporting the result "
                  "back: you finish and don't know whether it was good or "
                  "where it went wrong. More hours won't fix that. A report "
                  "channel will.",
             "eg": "Months of practice and no progress: first check whether "
                   "anything tells you which move was wrong."},
        ],
        "apply":
            "Where you are: what you asked for keeps coming back different, "
            "or you've practised something for months with no progress.\n"
            "Ask first: how often does the actual result come back to me? "
            "Inside that interval, how much is still changeable?\n"
            "Where it goes wrong: reading it as watch more closely — he means "
            "shorten the reporting cycle, not raise the intervention rate. "
            "They aren't the same, and the second usually crushes the loop "
            "itself.",
        "q": [
            "Control isn't issuing an order. It's correcting from the result.",
            "It came back wrong because the loop was cut, not because nobody "
            "listened.",
            "Feedback later than the correctable window is no feedback.",
        ],
    },
]
