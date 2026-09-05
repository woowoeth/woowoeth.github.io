# -*- coding: utf-8 -*-
"""Taiichi Ohno — English.

The English reader has met this material already, as lean, kanban, just in
time, a set of techniques a consultancy sells. What that packaging drops is
the single idea underneath all three chapters: every one of his inventions
exists to make a problem visible at the second and the place it occurs. The
cord, the five whys and the water level are not efficiency tools. They are
instruments for refusing to let anything be covered up.
"""

PARENT = {
    "name": "Taiichi Ohno",
    "slug": "ohno",
    "blurb": "Deep read",
    "items": [
        {"k": "five-whys", "n": "Ask why five times",
         "w": "Replacing the fuse, or fitting the strainer", "ready": True,
         "line": "The first cause is almost never the cause"},
        {"k": "pull-the-cord", "n": "Anyone may pull the cord",
         "w": "The problem surfaces where it happens", "ready": True,
         "line": "Do not let it pile up until the month-end count"},
        {"k": "inventory-hides-problems",
         "n": "Inventory is there to hide problems",
         "w": "Lower the water and the rocks appear", "ready": True,
         "line": "Comfortable margins are not good news"},
    ],
}

CHAPTERS = [
    {
        "k": "five-whys",
        "n": "Ask why five times",
        "w": "Replacing the fuse, or fitting the strainer",
        "src": "Taiichi Ohno, Toyota Production System, 1978",
        "dek": "The same fault keeps coming back and the review was written. "
               "What his five whys found on one stopped machine.",
        "story":
            "There is an example in the book. A machine stopped. ==Why did it "
            "stop? An overload blew the fuse.== Why the overload? The bearing "
            "was not sufficiently lubricated. Why not? The lubrication pump "
            "was not pumping enough. Why not? The pump shaft was worn and "
            "rattling. Why was it worn? No strainer had been fitted, so metal "
            "scrap got in. Only the fifth answer reaches the thing to repair: "
            "fit a strainer. Ask once and you replace the fuse, and it blows "
            "again next week. He called this the basic discipline of the "
            "Toyota floor.",
        "f": [
            {"n": "The first cause is almost never the cause",
             "d": "A blown fuse is a fact, not a cause. It is the first link "
                  "in the chain to show itself, and most reviews stop there "
                  "because it is the easiest to see and the cheapest to "
                  "change. Change it, and next time it is the same link "
                  "again.",
             "eg": "He was careless this time is a fuse. Keep going: why was "
                   "he careless, and what made being careful impossible in "
                   "that spot?"},
            {"n": "Five is not a ritual. It is the length of the chain",
             "d": "Fuse to strainer is exactly five steps, and each step is "
                  "the answer to the why before it. Skip a level and you stop "
                  "halfway, repairing something that will fail again. The "
                  "number is not mystical. It is roughly how long these "
                  "chains run.",
             "eg": "In a review, take every because and ask why that, in "
                   "turn, until nobody in the room can answer."},
            {"n": "The bottom layer is usually small and cheap",
             "d": "A strainer costs less than a pump, less than a bearing, "
                  "far less than the stoppage. Chasing a fault to its root "
                  "usually ends at the smallest available action, and that is "
                  "the reason to keep asking: not to be thorough, but to "
                  "reach the cheap point.",
             "eg": "A genuine root cause maps to a tiny change. If your fix "
                   "is large, you have probably not reached the bottom yet."},
        ],
        "q": [
            "Repeat why five times and the real cause shows itself.",
            "The first cause is only the first link to appear.",
            "A genuine root cause usually maps to a very small change.",
        ],
        "apply":
            "Where you are: one kind of problem keeps recurring, you deal "
            "with it every time, you write the review, and it recurs.\n"
            "Ask first: last time, did I change the fuse or fit the strainer? "
            "Counting down from the incident, how many layers did I actually "
            "reach? Was the change at that layer small?\n"
            "Where it goes wrong: reading it as dig deep into everything. "
            "Five whys is for problems that repeat, and a one-off does not "
            "need it. And never let why turn into whose fault — he was "
            "tracing a chain, not a person.",
    },
    {
        "k": "pull-the-cord",
        "n": "Anyone may pull the cord",
        "w": "The problem surfaces where it happens",
        "src": "Taiichi Ohno, Toyota Production System; Sakichi Toyoda's "
               "self-stopping loom",
        "dek": "What you hand out comes back wrong every time. Why Toyota let "
               "any worker on the line halt the entire line.",
        "story":
            "Toyota began as a loom maker. Sakichi Toyoda's loom had one "
            "design feature: when a thread broke the machine stopped itself, "
            "instead of weaving out a whole bolt of ruined cloth. Ohno moved "
            "the idea onto the car line. A cord hangs above every station, "
            "and ==anyone who sees a problem can pull it and stop the whole "
            "line==. Management feared the lost output. He held. The result "
            "is that a fault surfaces in the second it occurs and is handled "
            "there, rather than accumulating into a pile of scrap found at "
            "the month-end count.",
        "f": [
            {"n": "The earlier a defect stops, the cheaper it is",
             "d": "An error caught at the first station costs a minute. The "
                  "same error found at the last one costs the whole unit. "
                  "Work that comes back to you wrong every time is telling "
                  "you there was no point along the way where anyone could "
                  "halt it.",
             "eg": "If there is no checkpoint between handing the work out "
                   "and getting it back, what comes back will be wrong."},
            {"n": "Give the power to stop to the people furthest down",
             "d": "Whoever sees the problem first is on the line, not in the "
                  "office. If only a manager may stop, the problem has to "
                  "travel upward and wait for permission, and by then it has "
                  "flowed past. Give the stop to whoever can see, and it "
                  "stops where it started.",
             "eg": "Letting the person doing the work say wait, this is not "
                   "right is worth ten times any inspection you run "
                   "afterwards."},
            {"n": "Fear of stopping the line manufactures defects",
             "d": "The instinct of management is to keep running, because "
                  "output matters. But what keeps running is defective "
                  "output, and more of it is worse. His ordering is the "
                  "reverse of the instinct: stopping is what produces, and "
                  "refusing to stop is what really cuts production.",
             "eg": "Get it out now and fix it later mostly produces rework, "
                   "and rework costs far more than the pause would have."},
        ],
        "q": [
            "A thread breaks, the loom stops, and nothing ruined is woven.",
            "Give the power to stop to whoever can see the problem.",
            "Stopping is what produces. Refusing to stop is what cuts output.",
        ],
        "apply":
            "Where you are: what you hand out comes back looking nothing like "
            "what you asked for, and you send it back every time.\n"
            "Ask first: between handing this out and receiving it, how many "
            "points are there where somebody could call a halt? When the "
            "person doing the work sees something wrong, may they stop, and "
            "do they dare?\n"
            "Where it goes wrong: reading it as everything must be escalated. "
            "The cord is pulled on an abnormality, not on the normal flow. "
            "And it is not a licence to watch people harder — the power moves "
            "down, not up.",
    },
    {
        "k": "inventory-hides-problems",
        "n": "Inventory is there to hide problems",
        "w": "Lower the water and the rocks appear",
        "src": "Taiichi Ohno, Toyota Production System, 1978",
        "dek": "Everything obvious has been cut and the cost will not move. "
               "Why he treated stock as a cover rather than a cushion.",
        "story":
            "He had a picture for it. Inventory is water and problems are "
            "rocks on the riverbed. With the water high the boat runs "
            "smoothly, because every rock is submerged: an unreliable "
            "machine, a supplier who misses dates, a handover nobody has "
            "sorted out, all of it carried by the stock. ==Lower the water "
            "and the rocks come up one at a time==; hit one, repair it, and "
            "the channel is genuinely open. Toyota cut stock not to save "
            "warehouse rent but to leave problems nowhere to hide.",
        "f": [
            {"n": "Wherever there is slack, something is being covered",
             "d": "An extra week in the schedule, extra material, an extra "
                  "pair of hands: every piece of slack is underwriting some "
                  "problem. A problem that is underwritten never gets "
                  "repaired, so the slack turns into a permanent cost. Hunt "
                  "the slack first. There is a rock beneath it.",
             "eg": "Whichever stage always keeps a margin has, underneath "
                   "that margin, a problem nobody has fixed."},
            {"n": "You lower the water to hit rocks, not to save water",
             "d": "His purpose in cutting stock was never the storage bill. "
                  "It was forcing problems into the open. Lower the water and "
                  "leave the exposed rocks unrepaired and the boat is holed, "
                  "which is why the imitators failed: they copied the cutting "
                  "and skipped the repairing.",
             "eg": "After you cut a margin, something will go wrong. That is "
                   "the rock surfacing. Repair it instead of putting the "
                   "margin back."},
            {"n": "A little at a time, one rock per pass",
             "d": "He did not drain the river. Lower the level slightly, one "
                  "rock appears, repair it, lower it again. Take it all out "
                  "at once and ten rocks arrive together and none of them get "
                  "fixed. Cost comes down in layers, never in a single cut.",
             "eg": "Cut a margin a little, wait until this layer of problems "
                   "has been repaired, and only then cut the next slice."},
        ],
        "q": [
            "Inventory is water, problems are rocks, and high water runs "
            "smooth.",
            "Every margin is underwriting a problem, and underwritten "
            "problems go unrepaired.",
            "Cut the margin and something breaks. That is the rock you "
            "wanted.",
        ],
        "apply":
            "Where you are: every obvious cost has been cut, and cutting "
            "further would damage the people or the goods, so you cannot see "
            "where to go next.\n"
            "Ask first: which stages always keep a margin? If I removed the "
            "margin at one of them, what problem would surface? Am I prepared "
            "to repair that one?\n"
            "Where it goes wrong: reading it as all margin is waste. What he "
            "cut was stock being used to hide problems, not genuine safety "
            "margin. And never cut it all at once — that is holing the boat, "
            "not clearing the channel.",
    },
]
