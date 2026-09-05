# -*- coding: utf-8 -*-
"""The I Ching — English.

Most English readers have met this book as an oracle: something you consult
with coins about a decision you have already half made. These pages leave the
divination alone entirely and read it as what it is line by line, a table of
positions. The same dragon is given six different instructions depending on
where it stands, and the useful question the book keeps asking is not what
will happen but where exactly are you.

Facts follow the line texts of the Qian hexagram, the Commentary on the Words
on the top line, the hexagrams Tai and Pi and their order, and the sentence in
the Great Commentary about the limit.
"""

PARENT = {
    "name": "The I Ching",
    "slug": "i-ching",
    "blurb": "Deep read",
    "items": [
        {"k": "hidden-dragon", "n": "The hidden dragon does not act",
         "w": "Newly in place, do not move yet", "ready": True,
         "line": "The bottom line is not short of power. It is short of time"},
        {"k": "arrogant-dragon", "n": "The overreaching dragon repents",
         "w": "The line above the peak", "ready": True,
         "line": "To know advancing and not retreating"},
        {"k": "peace-and-stagnation", "n": "After Peace comes Standstill",
         "w": "Run it to the limit and it turns", "ready": True,
         "line": "The wall falls back into the moat"},
    ],
}

CHAPTERS = [
    {
        "k": "hidden-dragon",
        "n": "The hidden dragon does not act",
        "w": "Newly in place, do not move yet",
        "src": "Book of Changes, Qian hexagram, bottom line; Commentary on "
               "the Words",
        "dek": "Just arrived, just promoted, just moved. This one asks why "
               "the first line of the first hexagram says do not act.",
        "story":
            "The six lines of Qian read from the bottom up as one dragon "
            "moving from hidden to flying to overreaching. ==The bottom line "
            "has four words: the hidden dragon does not act.== The dragon is "
            "under water. Not for lack of power, since a dragon is a dragon. "
            "The position is still lowest, and force used from there is all "
            "your own, with all of the risk on you. One step up is the dragon "
            "appearing in the field. A step above that, the noble man is busy "
            "all day and wary at night. Capacity and the right moment are two "
            "different times.",
        "f": [
            {"n": "Being able and being due are two different times",
             "d": "The first line and the fifth are both the dragon. What "
                  "differs is not power but position. Rushing to prove "
                  "yourself in a new place spends your own force and carries "
                  "all the risk; from the second or third line the same act "
                  "is far easier.",
             "eg": "New to a team, change nothing in the first month. Not "
                   "because it should not be changed, but because that is "
                   "when changing it costs the most."},
            {"n": "Not acting is accumulating, not waiting",
             "d": "The hidden dragon is not lying down. The third line is "
                  "explicit: busy all day, wary into the evening. The time "
                  "under water goes on reading the ground and gathering what "
                  "you will need. What is waited for is a change of position, "
                  "not a change of mood.",
             "eg": "Before you are in a position to decide anything, find out "
                   "everything worth finding out. That is the work of the "
                   "hidden stretch."},
            {"n": "Every line has its own move, and skipping costs",
             "d": "The six lines give six different pieces of advice because "
                  "the positions differ. Acting from the first line as though "
                  "you stood at the fifth is using force that is not yours to "
                  "use. Knowing which line you are on matters more than "
                  "knowing all six.",
             "eg": "Ask which line am I on before deciding whose advice to "
                   "follow, including your own from the last job."},
        ],
        "q": [
            "The hidden dragon does not act.",
            "Being able and being due are two different times.",
            "Ask which line you are on before choosing how to act.",
        ],
        "apply":
            "Where you are: newly in a position or a new place, wanting to "
            "produce something fast to prove yourself.\n"
            "Ask first: which line am I on here, and if it is the bottom one, "
            "have I gathered what that line is for?\n"
            "Where it goes wrong: reading it as hide and do nothing. The "
            "bottom line withholds action, not effort, and the third line is "
            "busy all day; it is also not a reason to stay under water "
            "forever, because the dragon is meant to rise.",
    },
    {
        "k": "arrogant-dragon",
        "n": "The overreaching dragon repents",
        "w": "The line above the peak",
        "src": "Book of Changes, Qian hexagram, top line; Commentary on the "
               "Words",
        "dek": "What the risk is when everything has gone your way for a long "
               "time, and why the top line is not the best one.",
        "story":
            "Counting up Qian, the fifth line is the dragon flying in the "
            "heavens, which looks like the summit. There is one line above "
            "it. ==The top line reads: the overreaching dragon repents.== The "
            "Commentary on the Words glosses that word: to know advancing and "
            "not retreating, to know preserving and not perishing, to know "
            "gaining and not losing. Three knowings against three "
            "not-knowings. A whole ascent spent learning advance, "
            "preservation and gain, and never once practising the other half. "
            "At the highest point the missing half is what brings you down.",
        "f": [
            {"n": "There is a line above the summit, and it repents",
             "d": "Most people take the fifth line for the end; the hexagram "
                  "is not finished. Keep pushing in the same direction after "
                  "the dragon is flying and you arrive at the top line. The "
                  "problem with a peak is not the height, it is adding after "
                  "you have reached it.",
             "eg": "Most of those who double down straight after their best "
                   "year are on their way to the top line."},
            {"n": "What is missing is not the skill of advancing",
             "d": "To know advancing and not retreating. A run of good "
                  "fortune trains half a person. Advance, preserve and gain "
                  "become fluent; retreat, perish and lose are never "
                  "rehearsed. What the summit calls for is precisely the "
                  "unrehearsed half, which is why people fall.",
             "eg": "Someone who has only ever added is clumsy the first time "
                   "subtraction is the right move."},
            {"n": "Repentance is not ruin, it is a warning",
             "d": "The line says repents, not disaster. The overreaching "
                  "dragon does not necessarily die of the fall, but will "
                  "certainly regret not having stopped at the fifth. It is "
                  "written for someone still in the air: the position one "
                  "step above yours is that one.",
             "eg": "Reading this line while everything is still going well is "
                   "worth more than reading it after the fall."},
        ],
        "q": [
            "The overreaching dragon repents.",
            "To know advancing and not retreating, gaining and not losing.",
            "Above the summit there is one more line, and it repents.",
        ],
        "apply":
            "Where you are: a long run has gone your way and you are standing "
            "higher than you ever have, thinking about adding.\n"
            "Ask first: am I at the fifth line or already at the top one, and "
            "have I ever practised retreat and loss, or only advance and "
            "gain?\n"
            "Where it goes wrong: reading it as quit while ahead. The flying "
            "dragon at the fifth line is good and the hexagram wants the "
            "ascent; this says only that one more line exists above the peak.",
    },
    {
        "k": "peace-and-stagnation",
        "n": "After Peace comes Standstill",
        "w": "Run it to the limit and it turns",
        "src": "Book of Changes, hexagrams Tai and Pi and their order; Great "
               "Commentary",
        "dek": "What to prepare when everything is going well, and what to "
               "hope for when it is jammed. Why the two sit side by side.",
        "story":
            "Among the sixty-four, the eleventh is Tai, free passage, and the "
            "twelfth is Pi, blockage. ==They are placed next to each other==, "
            "and the top line of Tai already reads: the wall falls back into "
            "the moat. The last position of the smooth run is itself the "
            "beginning of the turn. It works the other way too, since the top "
            "of Pi reads standstill first, then joy. The Great Commentary "
            "states the rule. At the limit it changes; changed, it passes "
            "through; passing through, it lasts. Not a fated cycle: every "
            "state carries its own end inside it.",
        "f": [
            {"n": "The turn is written into the top line of Peace",
             "d": "The wall falling back into the moat is not in Pi; it is in "
                  "Tai. The reversal does not begin when the bad days start, "
                  "it begins at the last position of the good ones. The "
                  "moment most worth preparing is the one that looks least "
                  "like it needs preparing.",
             "eg": "The year the business is best is the year to work out how "
                   "it ends. Waiting until it has ended means you are already "
                   "in Pi."},
            {"n": "At the limit it changes, so being jammed is the condition",
             "d": "People try to change things while they still just about "
                  "work, and cannot, because the limit has not been reached. "
                  "Fully jammed, change becomes possible, because the old way "
                  "has run out and nobody is defending it any more.",
             "eg": "Stop forcing the change while it still half works. Push "
                   "at the moment it genuinely seizes and the resistance is "
                   "at its lowest."},
            {"n": "Adjacent means neither one lasts",
             "d": "Tai does not stay Tai and Pi does not stay Pi. The same "
                  "sentence is a warning to whoever is up and a comfort to "
                  "whoever is down. What matters is reading which hexagram "
                  "you are in rather than treating the present as permanent.",
             "eg": "Now is not the normal state. It is one line of one "
                   "hexagram. Ask yourself which."},
        ],
        "q": [
            "The wall falls back into the moat.",
            "At the limit it changes; changed it passes through, and so "
            "lasts.",
            "Now is not the normal state. It is one line of one hexagram.",
        ],
        "apply":
            "Where you are: either everything is going well and you expect it "
            "to continue, or you are jammed and expect never to get out.\n"
            "Ask first: if this is Tai, which line am I on and how far off is "
            "the wall falling back into the moat? If this is Pi, am I "
            "treating the jam as the entry ticket for change or only as bad "
            "luck?\n"
            "Where it goes wrong: reading it as fatalism, that it will turn "
            "anyway so nothing matters. The Great Commentary says at the "
            "limit it changes, and changing is something a person does.",
    },
]
