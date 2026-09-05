# -*- coding: utf-8 -*-
"""Guo Jia — English.

An English reader meeting this name for the first time will place him in the
Three Kingdoms as one more clever adviser, the genre where every good idea
arrives as a trick. These pages do the opposite: what Guo Jia actually did was
turn feelings into counts, preparation into subtraction, and pursuit into
patience, and each of the three is a procedure you can run without any of his
century's colour.

Quotations follow the Records of the Three Kingdoms and Pei Songzhi's citation
of the Fuzi.
"""

PARENT = {
    "name": "Guo Jia",
    "slug": "guo-jia",
    "blurb": "Deep read",
    "items": [
        {"k": "ten-victories", "n": "Ten defeats, ten victories",
         "w": "Morale broken into checkable items", "ready": True,
         "line": "A pep talk cannot be checked. Ten items can"},
        {"k": "leave-the-baggage", "n": "Leave the baggage, march light",
         "w": "Speed is what is left after subtraction", "ready": True,
         "line": "Carry everything you own and you never arrive"},
        {"k": "waiting-out-liaodong", "n": "The last plan: Liaodong",
         "w": "Do not press, and they turn on each other", "ready": True,
         "line": "Press them and they unite. Ease off and they quarrel"},
    ],
}

CHAPTERS = [
    {
        "k": "ten-victories",
        "n": "Ten defeats, ten victories",
        "w": "Morale broken into checkable items",
        "src": "Records of the Three Kingdoms, Book of Wei, Biography of Guo "
               "Jia, with Pei Songzhi citing the Fuzi",
        "dek": "Facing an opponent stronger on every axis, how do you make a "
               "team believe? He said nothing encouraging at all.",
        "story":
            "Before Guandu, Yuan Shao had more men and more grain, and Cao "
            "Cao's side was broadly pessimistic. Guo Jia did not give a "
            "speech. He made a list. ==Shao has ten defeats, you have ten "
            "victories==, and then set them out one at a time. Shao is thick "
            "with ceremony, you follow what is natural. Shao is outwardly "
            "generous and inwardly suspicious, employing men while doubting "
            "them; you use a man without doubt and fit him to the work. Shao "
            "plans much and decides little. Ten items later, the judgement "
            "was no longer a feeling.",
        "f": [
            {"n": "Break the whole judgement into items checkable one by one",
             "d": "We can take them is a single impression nobody can argue "
                  "with. Supporters and objectors each produce examples and "
                  "neither moves. Split it into ten and each item can be "
                  "granted or refuted on its own; anyone who disagrees has to "
                  "say which one fails.",
             "eg": "We are stronger than them produces nothing. Cost "
                   "structure, delivery time, decision speed and channel "
                   "depth, compared line by line, produce something you can "
                   "act on in an afternoon."},
            {"n": "Name where they are strong, or nobody believes the rest",
             "d": "The ten items do not dodge Yuan Shao's advantages: more "
                  "troops, more territory, greater standing, all true. "
                  "Because none of that is avoided, the differences that "
                  "remain carry weight. A comparison listing only your own "
                  "strengths reads as a pep talk.",
             "eg": "If the competitive review finds nothing good about the "
                   "rival, the team discounts the whole thing. Write the "
                   "three ways they genuinely beat you first."},
            {"n": "Each difference has to land on something you can do",
             "d": "Not one of the ten is we want it more. Judgement means "
                  "using a man without doubting him; strategy means acting "
                  "once the plan is set. Each names an organisational "
                  "behaviour that can be kept or wrecked. One vague item "
                  "spoils the whole table.",
             "eg": "We have more passion is a blank cell. Three approval "
                   "layers against seven is something you can hold on to and "
                   "can also lose."},
        ],
        "q": [
            "Shao has ten defeats and you have ten victories.",
            "He employs men and doubts them; you use a man without doubt.",
            "Encouragement is not a comparison. Ten items you can check is.",
        ],
        "apply":
            "Where you are: up against an opponent obviously stronger, and "
            "the team has stopped believing.\n"
            "Ask first: can our advantage be split into ten items that each "
            "stand or fall on their own?\n"
            "Where it goes wrong: encouragement standing in for the count; a "
            "comparison that lists only your strengths and skips where they "
            "are genuinely better.",
    },
    {
        "k": "leave-the-baggage",
        "n": "Leave the baggage, march light",
        "w": "Speed is what is left after subtraction",
        "src": "Records of the Three Kingdoms, Book of Wei, Biography of Guo "
               "Jia",
        "dek": "Everyone said a thousand-mile raid was too risky. He said the "
               "risk was not the distance but what you were carrying.",
        "story":
            "In 207 Cao Cao wanted to march north against the Wuhuan, and his "
            "generals objected: with the army beyond the frontier, Liu Biao "
            "might send Liu Bei against the capital. Guo Jia judged that Liu "
            "Biao would only talk and would never trust Liu Bei with troops, "
            "and pressed for the campaign. At Yi county he raised something "
            "more urgent still. ==Speed is the essence of war; a "
            "thousand-mile raid with heavy baggage cannot seize the "
            "advantage.== Leave it behind and march light day and night. Cao "
            "Cao did, went out by Lulong Pass, and broke the Wuhuan at White "
            "Wolf Mountain.",
        "f": [
            {"n": "Speed is not running faster, it is carrying less",
             "d": "The pace of a long march is set by its slowest part, and "
                  "the slowest part is always the baggage. The only way to be "
                  "quick is to decide what not to bring. That is subtraction, "
                  "and preparation is almost always addition.",
             "eg": "Three months went into analytics, an admin console, "
                   "permissions and every screen size, for a test meant to be "
                   "quick. Which of those would still have answered the "
                   "question?"},
            {"n": "Accept the price of travelling light before you go",
             "d": "Leaving the baggage means no supply and no line of retreat "
                  "if it goes badly. Marching light is not free; it trades "
                  "margin for error against speed. So the decision rests on "
                  "one prior judgement: does this have to be fast, or can it "
                  "be slow?",
             "eg": "Dropping monitoring and the rollback plan to hit a date "
                   "is allowed, as long as you know what you sold. Whoever "
                   "thinks light costs nothing panics the first time."},
            {"n": "Answer the fear everybody already has",
             "d": "He did not skirt the worry about the capital; he ruled on "
                  "it first, and only then proposed the raid. Meeting the "
                  "largest objection head on is what makes the rest of a plan "
                  "movable at all.",
             "eg": "Pitching something aggressive, put the thing the team is "
                   "most afraid of on the first page: why it will not happen, "
                   "and what you do if it does."},
        ],
        "q": [
            "Speed is the essence of war.",
            "Leave the baggage, march light, and come at them unlooked for.",
            "Liu Biao is a talker, and knows he cannot control Liu Bei.",
        ],
        "apply":
            "Where you are: something has to be fast and you are still "
            "finishing the preparation.\n"
            "Ask first: which of these could be skipped and still give you "
            "the answer, and do you accept the cost of skipping them?\n"
            "Where it goes wrong: treating light as free; walking around the "
            "risk the team is most worried about instead of ruling on it.",
    },
    {
        "k": "waiting-out-liaodong",
        "n": "The last plan: Liaodong",
        "w": "Do not press, and they turn on each other",
        "src": "Records of the Three Kingdoms, Book of Wei, Biography of Guo "
               "Jia and Annals of Emperor Wu",
        "dek": "The remnants fled onto somebody else's ground. Do you chase? "
               "The plan he left behind runs against the instinct.",
        "story":
            "Beaten, Yuan Shang and Yuan Xi fled to Gongsun Kang in Liaodong. "
            "The generals urged pursuit and the taking of Liaodong in one "
            "stroke. Cao Cao said there was no need: Kang would send him "
            "their heads. He withdrew. Shortly afterwards Kang killed both "
            "brothers and sent the heads on. Asked why, Cao Cao said, ==he "
            "has always feared Shang; press him and they combine, ease off "
            "and they plot against each other==. The judgement had been left "
            "to him by Guo Jia before he died.",
        "f": [
            {"n": "Outside pressure welds enemies together",
             "d": "Two parties watching each other will drop the watching the "
                  "moment a larger threat appears outside. So when a crack "
                  "already runs through the other side, the last thing to "
                  "hand them is a common enemy.",
             "eg": "Two rivals were poaching each other's staff. You started "
                   "a price war and within a month they were supplying each "
                   "other."},
            {"n": "Withdrawing puts the conflict back where it was",
             "d": "Leading the army home was not giving up. It handed the "
                  "principal conflict back to the other side's interior. The "
                  "move looks like doing nothing and is in fact very "
                  "specific: removing the reason they have to stay united.",
             "eg": "Two departments deadlocked, and the more you intervened "
                   "the more they aligned their story against you. Step out "
                   "and the original clash of interests reappears."},
            {"n": "The judgement rests on the relationship, not on strength",
             "d": "He has always feared Shang. The whole basis of the plan is "
                  "an old wariness that existed long before you arrived. "
                  "Without that ledger between them, withdrawing is simply "
                  "letting a tiger back into the hills.",
             "eg": "Counting on competitors to fight each other assumes an "
                   "unsettled account already exists. Where none does, "
                   "stepping back just lets them both grow."},
        ],
        "q": [
            "Press him and they combine; ease off and they plot against each "
            "other.",
            "Do not pursue. Kang will behead them and send them to you.",
            "A common enemy is the cheapest gift you can give two rivals.",
        ],
        "apply":
            "Where you are: the opponent has broken up and you are weighing "
            "whether to finish the pursuit.\n"
            "Ask first: is there already a conflict inside them, and does my "
            "pressure make it larger or smaller?\n"
            "Where it goes wrong: reading withdrawal as surrender; counting "
            "on infighting where no crack exists.",
    },
]
