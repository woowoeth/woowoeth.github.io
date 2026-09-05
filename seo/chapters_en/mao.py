# -*- coding: utf-8 -*-
"""Mao Zedong — English.

The English reader arrives at this name with a century of political argument
already attached to it, and none of that argument is what these pages are for.
What is read here is a body of method written between 1936 and 1949: how to
find the one contradiction that governs a situation, where knowledge actually
comes from, how a weaker side changes the shape of a fight, and how a group
moves on a single judgement. The later political history is deliberately
outside the frame.
"""

PARENT = {
    "name": "Mao Zedong",
    "slug": "mao",
    "blurb": "Deep read",
    "items": [
        {"k": "on-contradiction", "n": "On Contradiction",
         "w": "Untie one knot at a time", "ready": True,
         "line": "In a tangle, find the thread that loosens the rest"},
        {"k": "on-practice", "n": "On Practice",
         "w": "Knowing arrives through doing", "ready": True,
         "line": "An idea is not finished inside a book"},
        {"k": "on-protracted-war", "n": "On Protracted War",
         "w": "Trading time for strength", "ready": True,
         "line": "The weaker side changes the shape of the war first"},
        {"k": "strategy-of-the-revolution", "n": "Problems of Strategy",
         "w": "Fight the war your weapons allow", "ready": True,
         "line": "Someone else's manual cannot be carried across"},
        {"k": "methods-of-work", "n": "Methods of Work",
         "w": "Put it on the table", "ready": True,
         "line": "One person deciding is not a group moving"},
    ],
}

CHAPTERS = [
    {
        "k": "on-contradiction",
        "n": "On Contradiction",
        "w": "Untie one knot at a time",
        "src": "On Contradiction (1937)",
        "dek": "Everything is urgent and all of it is yours. The question is "
               "not effort but which knot to pull first.",
        "story":
            "Written at Yan'an in 1937, the essay turns a tangle into a "
            "diagram. At any stage many contradictions exist at once, but "
            "==only one of them is principal, and its existence and "
            "development determine the rest==. Find it and the other "
            "problems change shape on their own. Miss it and effort gets "
            "spread evenly across ten urgent things, which looks like "
            "working on everything and lands on nothing. Every later "
            "application repeats the same opening question: what is the "
            "principal contradiction of this stage?",
        "f": [
            {"n": "The principal one is not the loudest one",
             "d": "The principal contradiction is not the most urgent item "
                  "and not the hardest. It is the one whose solution changes "
                  "the shape of the others. Until you have found it, more "
                  "action ties the knot tighter.",
             "eg": "Weak product, few users, no channel and a loud competitor "
                   "all shout at once. Supply was the switch, and everything "
                   "else moved once it did."},
            {"n": "Finding it is half; cutting the rest is the other half",
             "d": "Better to sever one finger than to wound ten. Naming the "
                  "priority is the easy half. The other half is genuinely "
                  "putting the rest down, which means not doing them this "
                  "stage, not doing them later. Spreading effort is usually "
                  "reluctance, not blindness.",
             "eg": "Plenty of people can name their priority. The ones whose "
                   "list keeps growing and whose main thing still does not "
                   "ship have not cut anything."},
            {"n": "When the stage turns, the knot moves",
             "d": "The principal contradiction is not fixed. Solve this one "
                  "and the next stage surfaces a different one. The common "
                  "death is holding on to yesterday's priority until the "
                  "situation has changed the question and you are still "
                  "answering the old one.",
             "eg": "The team that won the first market kept optimising "
                   "acquisition for two more years, while the actual question "
                   "had quietly become whether anyone stayed."},
        ],
        "q": [
            "Among the many contradictions, one is principal and determines "
            "the rest.",
            "Grasp the principal contradiction and every problem is readily "
            "solved.",
            "Better to sever one finger than to wound all ten.",
        ],
        "apply":
            "Where you are: several things are all sounding at once and none "
            "of them feels droppable.\n"
            "Ask first: which single one, solved, would loosen most of the "
            "others?\n"
            "Where it goes wrong: the list keeps growing and the one thing "
            "that would move the rest still does not ship; the quarter turned "
            "and the method did not.",
    },
    {
        "k": "on-practice",
        "n": "On Practice",
        "w": "Knowing arrives through doing",
        "src": "On Practice (1937)",
        "dek": "You understood the idea and nothing changed. This one asks "
               "where knowledge comes from, and answers: from carrying "
               "something out.",
        "story":
            "Written at Yan'an the same year as On Contradiction. Two "
            "failures were common in the ranks: one man memorised manuals and "
            "treated conclusions drawn on somebody else's battlefield as his "
            "own knowledge; another charged on instinct alone. The essay "
            "refuses both. Real knowledge comes out of doing, then has to be "
            "checked against what happened, then done again. ==If you want to "
            "know the taste of a pear, you must change the pear by eating it "
            "yourself.== Memorising without that loop is what he called book "
            "worship.",
        "f": [
            {"n": "Knowledge comes out of doing",
             "d": "Following an argument is not the same as being able to run "
                  "it. A judgement that has never been struck back at by "
                  "events is a sentence nobody has paid for yet. What "
                  "survives hardens after you have taken something out into "
                  "the world.",
             "eg": "Many people can describe the product well. Few have "
                   "closed the first paying customer. The first group is "
                   "still outside the knowledge; the second is inside it."},
            {"n": "Doing once is not the loop",
             "d": "One pass is not enough. Do without looking back and all "
                  "you keep is fatigue. Look without going again and all you "
                  "keep is an impression. Knowledge is a circle: act, review, "
                  "act again, and the review has to be able to change the "
                  "next act.",
             "eg": "A team running the same playbook for three quarters with "
                   "flat numbers, adding hours rather than reading them, has "
                   "stopped at the doing."},
            {"n": "A book hands you the result, not the circuit",
             "d": "What somebody wrote down is the product of a loop they "
                  "finished. You get the conclusion; the trials, corrections "
                  "and second attempts are not on the page. So reading can "
                  "shorten your route and cannot walk it for you.",
             "eg": "Twenty books of method and still no plan anyone can "
                   "execute is normal. That is twenty circuits other people "
                   "walked, and none of them yours."},
        ],
        "q": [
            "If you want to know the taste of a pear, eat it.",
            "Practice is the criterion of truth.",
            "What is merely perceived cannot at once be understood.",
        ],
        "apply":
            "Where you are: a shelf of method and not one live situation of "
            "your own.\n"
            "Ask first: which already-finished thing has this sentence been "
            "through?\n"
            "Where it goes wrong: you can explain more and more and deliver "
            "less and less; somebody else's review gets filed as your own "
            "experience.",
    },
    {
        "k": "on-protracted-war",
        "n": "On Protracted War",
        "w": "Trading time for strength",
        "src": "On Protracted War (1938)",
        "dek": "The weaker side that fights at the stronger side's tempo "
               "loses. This one is about changing the shape of the war "
               "itself.",
        "story":
            "After Xuzhou and Nanjing in 1938, two errors were loud: that "
            "China was finished, and that victory would be quick. The lecture "
            "puts fought and unfought battles on one diagram, strategic "
            "defensive, strategic stalemate, strategic counter-offensive. "
            "==It is not a forecast of dates; it is a rule about what may not "
            "be done.== Do not trade your main force for the news value of "
            "one city. Do not seek a decisive battle before the fist has "
            "formed.",
        "f": [
            {"n": "Survive first, then talk about winning",
             "d": "The weaker side's first objective is not to destroy the "
                  "other but to remain impossible to destroy. While the main "
                  "force exists, time exists. Gamble it away and time goes to "
                  "zero the same afternoon.",
             "eg": "Nine months of cash left: cutting three lines to keep one "
                   "alive beats starving four at once. A win reported for "
                   "every position held is helping the other side get its "
                   "decisive battle."},
            {"n": "Stalemate is not a pause, it is a change of rules",
             "d": "The middle stretch looks most like no progress. It is the "
                  "war moving off the quick decision the stronger side is "
                  "good at and onto the attrition you can survive. Whoever "
                  "cannot bear the stalemate will reach for a decisive battle "
                  "early.",
             "eg": "While the rival burned funding on discounts and city "
                   "launches, the side that refused the speed contest and "
                   "ground on retention let them hold points they could not "
                   "hold."},
            {"n": "The counter-offensive waits for the fist",
             "d": "Going over to the attack is not a change of mood. It is "
                  "scattered strength gathered into something that can be "
                  "moved as one. Attacking before that is a donation; staying "
                  "in stalemate after it wastes time on a stage that has "
                  "already ended.",
             "eg": "Going to full war before word of mouth has joined into a "
                   "network is graduating early. The slogan changed; the "
                   "supply lines did not."},
        ],
        "q": [
            "Both the defeatists and those who promise a quick win are wrong.",
            "Weapons matter in war, but the decisive factor is people.",
            "Is this fight buying time, or spending it?",
        ],
        "apply":
            "Where you are: you are the weaker side and they want it settled "
            "this week.\n"
            "Ask first: is this engagement buying time or spending it?\n"
            "Where it goes wrong: trading the main force for visible small "
            "wins to prove you are not stalling; a calendar full of battles "
            "and no week that grew the fist.",
    },
    {
        "k": "strategy-of-the-revolution",
        "n": "Problems of Strategy",
        "w": "Fight the war your weapons allow",
        "src": "Problems of Strategy in China's Revolutionary War (1936)",
        "dek": "Someone else's victory does not transfer. This one asks what "
               "a method has to look like given your ground, your people and "
               "your weapons.",
        "story":
            "In 1936 the Red Army was still in the northwest, and two "
            "imported methods were in fashion: Soviet field manuals, and the "
            "memory of the Northern Expedition. He put both down and asked a "
            "prior question. What is the character of war on this particular "
            "ground? Against a stronger and larger opponent, the method "
            "cannot be the stronger side's method. The essay turns opposition "
            "to book worship into a battlefield rule and writes ==concentrate "
            "a superior force and destroy the enemy one by one== as an "
            "operating order.",
        "f": [
            {"n": "Against book worship",
             "d": "Opposing book worship is not opposing study. It is "
                  "refusing to skip the look at your own ground. How the "
                  "Soviets fought and how the Northern Expedition fought are "
                  "other people's answers; imported as doctrine, the first "
                  "engagement is lost on terrain.",
             "eg": "A forty-person company running the org chart of a "
                   "forty-thousand-person one, or a workshop copying a "
                   "software release cadence: both are doctrine without "
                   "ground."},
            {"n": "Concentrate a superior force",
             "d": "Concentrate and destroy them one at a time: three against "
                  "one, finish, then move to the next. Spread out, it looks "
                  "as though fighting is happening everywhere and nothing is "
                  "punched through. On Contradiction says what to put down; "
                  "this says how to place what is left.",
             "eg": "Five features shipped the same quarter and not one of "
                   "them gives a customer a reason to stay. Punch one "
                   "through first, then start the second."},
            {"n": "Your battlefield is not theirs",
             "d": "Where you are weaker and smaller, the method built for "
                  "parity does not apply. Fighting with the weapons you have "
                  "is not consolation; it is nailing the method to your "
                  "actual strength instead of to the strength you are reading "
                  "about.",
             "eg": "A six-person team borrowing a public company's campaign "
                   "calendar runs out of money and people by week three. Ask "
                   "what these six can punch through, then pick that."},
        ],
        "q": [
            "No investigation, no right to speak.",
            "Concentrate a superior force and destroy the enemy one by one.",
            "Someone else's victory arrives without the ground it was won on.",
        ],
        "apply":
            "Where you are: you are holding a method that won for somebody "
            "else, on ground unlike yours.\n"
            "Ask first: how many of the conditions that method depends on do "
            "we actually have?\n"
            "Where it goes wrong: still running their org chart and their "
            "campaign calendar; five lines open and not one of them punched "
            "through.",
    },
    {
        "k": "methods-of-work",
        "n": "Methods of Work",
        "w": "Put it on the table",
        "src": "Methods of Work of Party Committees (1949)",
        "dek": "The call was right and everyone still went their own way. "
               "This one is about getting a group to actually move on one "
               "judgement.",
        "story":
            "March 1949. The organisation was about to change from fighting "
            "to administering, and what he wrote down was twelve rules of "
            "craft rather than a line of argument: how to run a meeting, how "
            "to question the people below you, how to push ten things along "
            "at once without noise, how to turn I think into I have counted. "
            "==The earlier essays settle the judgement; this one starts after "
            "it.== One person seeing clearly and a group moving accordingly "
            "are two different problems.",
        "f": [
            {"n": "Put the problem on the table",
             "d": "A disagreement that is not aired does not go away; it "
                  "moves into the corridor afterwards and ferments. Tabling "
                  "it is not about arguing. It lets whoever objects finish "
                  "the reason out loud, because a reason left unfinished "
                  "comes back in some other form.",
             "eg": "Unanimous in the room, full of reservations in private "
                   "messages afterwards. That agreement is the expensive "
                   "kind: everyone executes their own unspoken version of "
                   "it."},
            {"n": "Learn to play the piano",
             "d": "All ten fingers move, but they do not come down together. "
                  "Push only one thing and the rest rot; press ten evenly and "
                  "what comes out is noise. The craft is in sequence: which "
                  "is the melody this stretch, what accompanies it, who takes "
                  "over next.",
             "eg": "One word shouted all quarter while the other lines are "
                   "left to rot, or twelve goals every one of them marked "
                   "highest priority. Neither is playing."},
            {"n": "Have the numbers in your head",
             "d": "Any quality shows up as a definite quantity. Feedback is "
                  "good is an impression, not a situation. Retention is "
                  "thirty-eight per cent this month against forty-one last "
                  "month is a situation. Without quantity, the discussion is "
                  "won by whoever is loudest.",
             "eg": "Ask a manager what the biggest problem is and most can "
                   "answer. Ask how many times a week it happens and half the "
                   "answers disappear."},
        ],
        "q": [
            "Put problems on the table; a meeting that hides them settles "
            "nothing.",
            "Ten fingers all move, but pressed down together they make no "
            "tune.",
            "Any quality shows up as a quantity; without quantity there is "
            "none.",
        ],
        "apply":
            "Where you are: the direction is settled and the group is still "
            "each running its own reading of it.\n"
            "Ask first: has the disagreement been finished out loud, in front "
            "of everyone?\n"
            "Where it goes wrong: nobody objects in the room and reservations "
            "are everywhere afterwards; twelve goals all marked top priority; "
            "two hours of discussion without a single number on the table.",
    },
]
