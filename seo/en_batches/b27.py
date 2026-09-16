# -*- coding: utf-8 -*-
"""Daily entry, day 7: Robert K. Merton.

Picked by fan-out. The two thinnest Chinese situations are 被猜忌 and
功劳被抢, six chapters each. What hangs on the first - Guo Ziyi, Wang Jian,
Fan Li, Han Xin - all answer the same way: make yourself smaller, open the
gates, leave at the top. What hangs on the second - Gracian, Xiang Yu, Zhang
Liang, La Rochefoucauld - answers with visibility or with restraint. None of
them can say the structural sentence, which is Merton's: suspicion builds the
evidence that justifies it, and credit is allocated on reputation already
held, so neither is repaired by the suspected or uncredited person trying
harder.

All four English situations already exist, so there is no SC_BOX here.
Quoted lines are his own or the ones he quotes (the Thomas theorem, Matthew
13:12), with spelling left as printed - "behavior" inside the quotation marks
against the site's British spelling outside them.

Three stories, no overlap: the entry is the boy who renamed himself Merlin,
chapter one is the Last National Bank, chapter two is Zuckerman's interviews.
"""

ENTRIES = [
    {
        "c": "How the world works", "n": "Robert K. Merton",
        "slug": "merton", "e": "United States · 1910-2003",
        "w": "Self-confirming", "y": 1910,
        "d": "An American sociologist, born in a poor quarter of Philadelphia in "
             "1910 to immigrant parents, who taught at Columbia from 1941 until "
             "he retired. He never built a grand system. He did one thing: take "
             "a mechanism people could feel but could not name, give it an exact "
             "name, and then show how it runs. Several words now in ordinary use "
             "are his - self-fulfilling prophecy, role model, unintended "
             "consequences, the Matthew effect. They lasted because each one has "
             "a mechanism behind it that can be retold, not just a clever "
             "phrase. In 1994 he received the National Medal of Science, the "
             "first sociologist to do so.",
        "story":
            "He was not born Merton. Meyer Robert Schkolnick arrived in South "
            "Philadelphia in 1910, the son of Eastern European Jewish "
            "immigrants. As a boy he earned money doing magic and took a stage "
            "name: Merlin, after the magician at Arthur's court. A friend told "
            "him it was a cliche, so he changed it to something that sounded "
            "English, Merton, and kept it for the rest of his life. Decades "
            "later the boy who had chosen his own name wrote the paper on how "
            "differently the world remembers the same contribution depending on "
            "whose name is attached.",
        "f": [
            {"n": "His work was naming mechanisms",
             "d": "Self-fulfilling prophecy, role model, unintended consequences, "
                  "the Matthew effect: all his. He picked things everyone could "
                  "sense and nobody could name, because only a named thing can "
                  "be pointed at, argued about and guarded against.",
             "eg": "The thing that keeps happening on your team changes character "
                   "the moment it finally has an exact name."},
            {"n": "A false definition can produce a true result",
             "d": "In 1948 he set out the self-fulfilling prophecy: a wrong "
                  "reading of a situation prompts behaviour that turns the "
                  "situation into what was read. His case is the bank run - the "
                  "rumour says it is failing, depositors withdraw, it fails.",
             "eg": "Enough people call the project doomed, the strong ones "
                   "transfer out, and the project is duly doomed."},
            {"n": "Afterwards the prophet looks vindicated",
             "d": "The cruelty is in the aftermath. Whoever said it points to what "
                  "happened as proof, and the thing happened precisely because "
                  "they said it. His phrase for this state of affairs is a reign "
                  "of error kept alive by a specious validity.",
             "eg": "The person certain she was never up to it is often the person "
                   "who stopped handing her anything."},
            {"n": "Recognition is paid on reputation held",
             "d": "In 1968 he named a second mechanism in Science. Work by "
                  "someone of standing draws extra recognition; identical work by "
                  "an unknown has it withheld. The name comes from Matthew's "
                  "gospel: to every one that hath shall be given.",
             "eg": "The same memo is decisive under one signature and premature "
                   "under another."},
            {"n": "He was caught by his own finding",
             "d": "That paper stands on his student Zuckerman's interviews and "
                  "carries only his name. Twenty years on he published the "
                  "correction: it should have been joint. Nobody had to act badly "
                  "for the effect to work, which is the strongest evidence for it.",
             "eg": "When you last said the team did it, did people remember the "
                   "team or the person saying it?"},
        ],
        "apply":
            "Take one thing you are being misread on, or misreading someone "
            "else on, and do two things. First, write the judgement out as a "
            "full sentence - he is not really trying, they are guarding "
            "themselves against me - then ask which pieces of your evidence "
            "existed before that sentence did. Usually none; the rest accumulated "
            "afterwards. Second, if you are the one being guarded against, stop "
            "working on the explanation. Look for an arrangement where neither "
            "side has to trust the other: shared numbers, shared access, a "
            "written scope. Explaining keeps you inside the loop.",
        "q": [
            "The false judgement comes first and then produces its own evidence.",
            "Whoever said it will cite the outcome as proof they knew.",
            "The extra portion is paid on reputation, not on contribution.",
            "Nobody has to act badly for either mechanism to run.",
        ],
        "l": ["Thinking in Systems", "George Soros", "Mark Granovetter",
              "The Art of Worldly Wisdom", "La Rochefoucauld"],
        "contrast": [
            {"n": "The Art of Worldly Wisdom",
             "why": "Two places to cut into the same problem: Gracian tells you to "
                    "make sure the finished work is seen, Merton says whether it "
                    "is seen depends first on where your name already stands"},
            {"n": "George Soros",
             "why": "Both say belief rewrites fact: Soros watches price and "
                    "fundamentals push each other in markets, Merton watches "
                    "suspicion and reputation confirm themselves in a room"},
        ],
    },
]

INTROS = {
    "merton": "Sociologist who named two machines: suspicion builds its own "
              "evidence, and recognition is paid on reputation already held",
}

SCENES = [
    ("They've started watching me", "Dealing with people", [
        ("Once they suspect me, everything I do reads as proof.",
         [("merton", "self-fulfilling-prophecy")]),
    ]),
    ("The same mistakes keep happening", "Leading people", [
        ("I decided he wouldn't make it, and then he didn't.",
         [("merton", "self-fulfilling-prophecy")]),
    ]),
    ("Nobody is looking at my work", "Getting it done", [
        ("Same work, and the better-known name is the one remembered.",
         [("merton", "matthew-effect")]),
    ]),
    ("Starting from nothing", "Getting it done", [
        ("Nobody calls me because nobody has ever called me.",
         [("merton", "matthew-effect")]),
    ]),
]

ASKS = {
    "merton/self-fulfilling-prophecy":
        "Once they suspect me, everything I do reads as proof.",
    "merton/matthew-effect":
        "Same work, and the better-known name is the one remembered.",
}
