# -*- coding: utf-8 -*-
"""每日一条，第 1 天：伊万·伊里奇。

改成一天一个之后的第一条。选法不按名气，按**扇出** —— 数出每个处境底下
挂着几篇，最空的两个是「出得多了人却空了」和「日子被工具占满」（各 4 篇）。
那里现在挂的是德鲁克、庄子、契克森米哈赖、纽波特，都好，但没有一条说到
「工具越过某个门槛之后会开始吞掉它要服务的目的」—— 而这正是伊里奇。

条目故事避开了两章用过的场景（分水岭/医源病、汽车那笔账），
用的是他晚年拒绝自己那个瘤的手术：写下「医疗在制造疾病」的人，
面对方案是「成功率可观，代价是可能失去说话和听力」时，自己怎么算这笔账。
"""

ENTRIES = [
    {
        "c": "How the world works", "n": "Ivan Illich", "slug": "illich",
        "e": "Austria–Mexico · 1926–2002", "w": "A ceiling", "y": 1926,
        "d": "A priest who spent the 1970s taking apart four systems "
             "everybody treated as progress: schooling, transport, medicine, "
             "and the idea of a tool itself. One claim runs through all four "
             "— every tool crosses two watersheds, and past the second it "
             "starts producing what it was built to remove. Medicine makes "
             "patients, school makes a feeling of ignorance, transport makes "
             "distance. He is not against technology. He wants an upper "
             "bound on it.",
        "story":
            "The man who wrote that medical treatment produces illness grew "
            "a tumour on his face in later life. The proposed treatment was "
            "surgery and radiation, with respectable odds, at the risk of "
            "his speech and his hearing — and speaking, and listening to "
            "people speak, was the entire form of his work. He declined. He "
            "lived nearly two decades with the growth, teaching, in pain, "
            "managing the worst days with opium he prepared himself, and "
            "died in Bremen in 2002. He never wrote it up as a manifesto; "
            "asked, he said it was his own arithmetic. He never denied the "
            "treatment worked. He questioned whether the word worked had "
            "counted everything it costs.",
        "f": [
            {"n": "The two watersheds",
             "d": "Before the first, a tool solves a real problem. Between "
                  "the two it is steadily useful. Past the second it begins "
                  "producing the opposite. So does it work is unanswerable — "
                  "it does. The question is when what you pay to keep it "
                  "overtook what it gives you.",
             "eg": "The group chat saved ten emails in week one. At two "
                   "hundred people it takes an hour a day and anything real "
                   "still arrives privately."},
            {"n": "The signal is the reverse, not the slowdown",
             "d": "Efficiency usually keeps climbing after the crossing, "
                  "which is exactly why it is hard to notice. The reliable "
                  "signal is production of the opposite: care that generates "
                  "illness, communication tools that generate the fear of "
                  "being unreachable.",
             "eg": "The reporting got beautiful and people started splitting "
                   "tasks to make the board look right. What the tool wants "
                   "is replacing the work."},
            {"n": "A convivial tool lets you leave",
             "d": "His test for whether a tool is yours is whether you can "
                  "decline it. The higher the exit cost, the less it is your "
                  "tool and the more you are its. That is a property of the "
                  "arrangement, not of the features.",
             "eg": "A system you can export everything from and one you "
                   "renegotiate with after lock-in can look identical on a "
                   "comparison table."},
            {"n": "One ledger, not two",
             "d": "Tools advertise time saved and never report time spent — "
                  "learning, maintaining, working to pay, and getting back "
                  "into the work afterwards. Those land on different days, "
                  "so nobody adds them. Added, the answer often flips.",
             "eg": "Convert the monthly fee into your own hours and add the "
                   "weekly upkeep. A surprising number stop making sense."},
            {"n": "Professions monopolise the definition of the problem",
             "d": "His harder claim: past a point, a profession captures the "
                  "right to say what counts as a problem. Doctors define "
                  "illness, schools define having learned — and ordinary "
                  "people lose the ability to name their own situation.",
             "eg": "Once a field only speaks in terms insiders share, an "
                   "outsider's question is automatically unprofessional. "
                   "Those are often the real questions."},
        ],
        "apply":
            "Take the tool you lean on hardest and work out two numbers: the "
            "hours a week it costs to keep (learning, upkeep, recovering "
            "from its interruptions, and working to pay for it), and what it "
            "actually finished for you. Then ask the third question: what "
            "would leaving cost? Those three answers are worth more than any "
            "position on technology.",
        "q": [
            "Past the second watershed a tool produces what it was meant to "
            "remove.",
            "Illness produced by the treatment itself I call iatrogenesis.",
            "A convivial tool is one you can master, repair, and do without.",
        ],
        "l": ["Zhuangzi", "Peter Drucker", "Cal Newport", "Thinking in Systems",
              "Finite and Infinite Games"],
        "contrast": [
            {"n": "Kevin Kelly",
             "why": "Both read where technology is heading: one asks what it "
                    "will grow into, the other asks where it starts eating "
                    "people"},
            {"n": "Peter Drucker",
             "why": "Both ask what comes after efficiency — do the right "
                    "things, or put a ceiling on the tool"},
        ],
    },
]

INTROS = {
    "illich": "A priest who wrote that medicine makes patients, then declined his own surgery",
}

SCENES = [
    ("More output, emptier", "AI arrived", [
        ("It genuinely saved effort at first. Now I can't say who it is "
         "helping.",
         [("illich", "two-watersheds")]),
    ]),
    ("There's never enough time", "Body and energy", [
        ("I installed a stack of things that save time and my days are "
         "fuller.",
         [("illich", "effective-speed")]),
    ]),
]

ASKS = {
    "illich/two-watersheds":
        "It genuinely saved effort at first. Now I can't say who it is "
        "helping.",
    "illich/effective-speed":
        "I installed a stack of things that save time and my days are "
        "fuller.",
}
