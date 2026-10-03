# -*- coding: utf-8 -*-
"""Daily entry, day 23: Xiao He.

Picked by fan-out. 'Everyone is piling in' sits at eight on the Chinese side,
and what hangs under it (Soros, Le Bon, Marks, Kindleberger) all explains the
crowd; none says what to do with your hands while the crowd runs. Under 'credit
stolen' the answers are to push forward, to take less, or to stand under a tree
(Feng Yi); nobody speaks for the person whose work is the base the others
stand on and is never counted, or for the one who must rank a back office
against a front line. Xiao He, first chancellor of the Han and ranked first
of all the founders in the year 202 BC, answers both from his own record.

Recent entries were foreign, foreign, foreign, and pick_balance went red, so
the pool was switched to Chinese. His standing: a full biography in Records of
the Grand Historian; one of the 'three heroes' of the Han founding.

Three stories, no overlap: the entry is the night chase after Han Xin; the
chapters are the Xianyang records and the hunter-and-hounds ranking.
Quoted lines are our own renderings of the Chinese. Every situation already
exists, so there is no SC_BOX.
"""

ENTRIES = [
    {
        "c": "Power and organisation",
        "n": "Xiao He",
        "slug": "xiao-he",
        "e": "Western Han · died 193 BC",
        "w": "The back office", "y": -206,
        "d": "Chancellor to the first Han emperor, from Pei, who was a "
             "county clerk under the Qin and joined Liu Bang's rising from "
             "the start. His work was the managing: gathering records, "
             "recommending people, holding the rear, feeding the army. When "
             "Liu Bang became King of Han he was chancellor, and during the "
             "war he held the heartland and kept men and grain flowing to "
             "the front. In 202 BC, ranking the founders, Liu Bang put him "
             "first. He left one method: when others grab what is in front "
             "of them, take what will be needed next; when others count "
             "battles, ask whether the fighting could have happened without "
             "him.",
        "story":
            "Han Xin, who had been given little responsibility in Hanzhong, "
            "slipped away one night. Xiao He heard of it and did not "
            "wait to report; he rode out after him. Someone told Liu Bang "
            "the chancellor had run. Liu Bang felt he had lost both "
            "hands. Two or three days later Xiao He came back, and Liu Bang "
            "swore at him: why did you run? I did not run, said Xiao He, "
            "I went after someone who did. Who? Han Xin. Dozens of "
            "generals have deserted, said Liu Bang, and you chased "
            "none. Generals are easy to find, said Xiao He. A man like Han "
            "Xin is one of a kind. If you only want to be king of "
            "Hanzhong, you do not need him. If you want the realm, nobody "
            "else will do.",
        "f": [
            {"n": "He took the records, not the gold",
             "d": "When the army entered the Qin capital, the generals ran "
                  "for the treasury. Xiao He alone went first to the "
                  "chancellor's office and sealed away the laws and maps. "
                  "Later Liu Bang knew every pass and census figure because "
                  "of that. Others took what was valuable now; he took what "
                  "would be used.",
             "eg": "When a new project starts and everyone fights for titles "
                   "and budget, the person who has tidied the history and "
                   "the rules is steadiest three months on."},
            {"n": "He asked first what made the fighting possible",
             "d": "In 202 BC the generals said they had fought a hundred "
                  "battles and Xiao He none. Liu Bang answered with the "
                  "hunt: the hound runs down the hare, the hunter says where "
                  "it is. He ranked those who made the battles possible "
                  "above those who won them.",
             "eg": "When a project succeeds, thank the coders. Then also "
                   "the one who won the brief, the budget and the rota."},
            {"n": "He treated keeping the right person as his job",
             "d": "When Han Xin left, Xiao He rode after him himself, and "
                  "the reason he gave was no kindness but this: if you want "
                  "the realm, nobody else will do. For him the rear meant "
                  "grain, and also not losing the person the plan needs.",
             "eg": "When your strongest colleague is about to leave, your "
                   "first thought should be to go after them, not to say "
                   "the road is theirs to choose."},
        ],
        "apply":
            "If you are the one doing the supporting work, so that others "
            "can charge ahead, do not just complain that nobody sees it. "
            "Write on a sheet: if my part were gone, which things would "
            "stop this month? Put each as a fact someone can check and "
            "hand it to whoever decides the rewards. If you are the one "
            "ranking, do not rank by the numbers. Ask who made each "
            "success possible. His three acts, taking the records, "
            "chasing Han Xin and holding the heartland, were one judgment: "
            "find the thing without which the whole job fails.",
        "q": [
            "The hound runs down the hare; the hunter points out where.",
            "Generals are easy to find. A man like Han Xin is one of a kind.",
            "He held the rear, soothed the people and kept the army fed.",
        ],
        "l": ["Liu Bang", "Zhang Liang", "Han Xin", "Feng Yi"],
        "contrast": [
            {"n": "Han Xin",
             "why": "Both were among the Han founders. Han Xin's merit lay "
                    "on the battlefield, counted in battles won and cities "
                    "taken. Xiao He's was in what made those battles "
                    "possible, and cannot be counted. Liu Bang ranked the "
                    "second above the first. And Han Xin was the man Xiao "
                    "He had gone after."},
            {"n": "Feng Yi",
             "why": "Both stayed out of the scramble for credit. Feng Yi "
                    "walked away from the table where merit was argued and "
                    "let the soldiers and the emperor keep his account. "
                    "Xiao He had no battle record, and his emperor named "
                    "his merit aloud in front of every general. One was "
                    "credited by silence, the other by being spoken for."},
        ],
    },
]

INTROS = {
    "xiao-he":
        "Chancellor to the first Han emperor and the only one of the "
        "founding 'three heroes' who never fought. When the others raced "
        "for the Qin treasury he took its records, and when the generals "
        "protested his rank, Liu Bang called him the hunter and them the "
        "hounds",
}

SCENES = [
    ("Everyone is piling in", "Money", [
        ("Everyone's grabbing the shiny thing. What should I take first?",
         [("xiao-he", "take-the-records")]),
    ]),
    ("Things are going well and it scares me", "Getting it done", [
        ("A chance has come. What do I grab first?",
         [("xiao-he", "take-the-records")]),
    ]),
    ("Nobody is looking at my work", "Getting it done", [
        ("I do the work behind the scenes and nobody counts it.",
         [("xiao-he", "hunter-and-hounds")]),
    ]),
    ("The team has gone flat", "Leading people", [
        ("The front line says the back office hasn't earned its share. "
         "How do I reward?",
         [("xiao-he", "hunter-and-hounds")]),
    ]),
]

ASKS = {
    "xiao-he/take-the-records":
        "Everyone's grabbing the shiny thing. What should I take first?",
    "xiao-he/hunter-and-hounds":
        "I do the work behind the scenes and nobody counts it.",
}
