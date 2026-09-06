# -*- coding: utf-8 -*-
"""Simone Weil — English.

English readers meet her either as a saint or as a curiosity who starved
herself, and both framings bury the part that is usable. She wrote in French;
every quoted line here is a standard English translation (Craufurd for the
school-studies essay, McCarthy for the Iliad essay), never back-rendered
from the Chinese page. The job of these three chapters is to show one method
applied three times: what attention is, what a job that never asks for it
does to a person, and what force does to the person holding it.
"""

PARENT = {
    "name": "Simone Weil",
    "slug": "weil",
    "blurb": "Deep read",
    "items": [
        {"k": "attention-is-emptying", "n": "Attention is emptying, not straining",
         "w": "What you call concentrating is the opposite of it", "ready": True,
         "line": "The half hour you failed to solve it is where the learning happened"},
        {"k": "the-factory-year", "n": "The year she worked the factory floor",
         "w": "To know what a job does to people, do the job", "ready": True,
         "line": "What shook her was not the exhaustion but that she stopped being able to think"},
        {"k": "force-makes-things", "n": "Force turns both sides into things",
         "w": "The side holding it is being altered too", "ready": True,
         "line": "The winner loses not his conscience but his idea of tomorrow"},
    ],
}

CHAPTERS = [
    {
        "k": "attention-is-emptying",
        "n": "Attention is emptying, not straining",
        "w": "What you call concentrating is the opposite of it",
        "src": "Reflections on the Right Use of School Studies with a View to the Love of God (1942)",
        "dek": "Everyone treats attention as a muscle to be gripped harder. "
               "What is worth reading is why she says gripping is the wrong move.",
        "story":
            "We have concentration backwards, she argued. Told to pay "
            "attention, a person frowns, clenches, holds their breath, as "
            "though closing a hand around something. That is muscular "
            "effort, and it is the opposite of attention. ==Real attention "
            "is emptying yourself so the thing can enter.== Her example is "
            "a pupil failing at a geometry problem. Most people write off "
            "the half hour that produced no answer. She says that half "
            "hour is where the learning actually happened — not because "
            "anything was solved, but because someone stayed open in front "
            "of a thing they did not understand and did not run.",
        "f": [
            {"n": "Straining grips, attention waits",
             "d": "Gripping requires a shape to grip with, so the strained "
                  "mind pushes the object into a frame it already owns. "
                  "Attention asks you to admit you do not yet understand "
                  "and to stay there. One produces I knew this already. "
                  "Only the other produces anything new.",
             "eg": "Handed a report you cannot read, the first move is "
                   "usually to fit a familiar model over it. From that "
                   "moment the report can no longer say anything of its own."},
            {"n": "The time that produced nothing was not wasted",
             "d": "This is her least intuitive claim: effort that fails, "
                  "provided the attention holds, is still growing "
                  "something, even if the problem is never solved. What "
                  "grows is next time's discrimination. Only running away "
                  "actually voids the hour.",
             "eg": "You shipped nothing in the two hours you were stuck, "
                   "but you will see faster where the next problem of that "
                   "kind is jammed."},
            {"n": "Attention is a thing you can give someone",
             "d": "She called it the rarest and purest form of generosity. "
                  "Almost nobody can ask what are you going through and "
                  "then wait. Most listeners are already converting the "
                  "situation into a case they have seen before, halfway "
                  "through the second sentence.",
             "eg": "A colleague finishes describing the trouble and you "
                   "produce a fix. The fix may be right; what you just did "
                   "was swap their situation for your problem."},
        ],
        "q": [
            "What you call concentrating is straining. Attention is "
            "emptying yourself.",
            "The half hour you failed to solve it is where learning "
            "happened.",
            "Attention is the rarest and purest form of generosity.",
        ],
        "apply":
            "Where you are: your day was full and productive and you cannot "
            "name one thing that stayed with you.\n"
            "Ask first: was there any stretch today I spent inside not "
            "understanding, without running? When did I last hear someone "
            "out without converting it into a case I know?\n"
            "Where it goes wrong: reading emptying as relaxing. She "
            "describes an exhausting state — the exhaustion is in staying "
            "open, not in clenching.",
    },
    {
        "k": "the-factory-year",
        "n": "The year she worked the factory floor",
        "w": "To know what a job does to people, do the job",
        "src": "Factory Journal, in La Condition ouvriere (1951); letters of 1934-1935",
        "dek": "There is no shortage of surveys of industrial work. What is "
               "worth reading is why she thought no survey could reach the "
               "number she wanted.",
        "story":
            "In December 1934 a twenty-five-year-old philosophy teacher "
            "took a year's leave, and under her own name hired on as an "
            "unskilled hand at the Alsthom electrical works in Paris, then "
            "at Carnaud and Renault. Piece rates, and she lived on the "
            "wages. What shook her was not the exhaustion. ==It was "
            "finding that she had stopped being able to think.== The "
            "machine set the pace and the method came with the job, so "
            "across a whole day no thought of hers could get in. Months "
            "later she wrote that she no longer felt she had any claim on "
            "anything.",
        "f": [
            {"n": "She did not want to understand it, she wanted to undergo it",
             "d": "A survey gets hours, wages, injury rates. It cannot get "
                  "what a person becomes after a year inside, because that "
                  "figure is only generated in whoever is carrying it. She "
                  "gave up the salary and the status so that she had no "
                  "exit, and that is how she got it.",
             "eg": "To learn how bad a process is, do not read the "
                   "complaint log. Run it end to end yourself, and forbid "
                   "yourself from asking anyone inside for a shortcut."},
            {"n": "What is removed is judgement, not strength",
             "d": "What hollows people out is not the physical cost. It is "
                  "that the structure of the work has no slot that needs "
                  "them to think: the pace belongs to the machine, the "
                  "method to the foreman, the verdict to the piece count. "
                  "Judgement unused decays.",
             "eg": "If your view never changes what happens next, the job "
                   "is not only taking your hours. It is quietly taking "
                   "your judgement."},
            {"n": "The mark of humiliation is no longer feeling entitled",
             "d": "Her sharpest finding: past a point, people who are being "
                  "ground down do not protest. They first concede that the "
                  "fault is their own. So the damage is nearly invisible "
                  "from outside — the room is quiet, and the quiet is the "
                  "evidence that it has finished.",
             "eg": "Nobody objecting in the meeting rarely means nobody "
                   "objects. It means they no longer believe objecting "
                   "counts."},
        ],
        "q": [
            "What empties you is not fatigue. It is work that needs no "
            "thought.",
            "Past a point, the ground down first concede the fault is "
            "theirs.",
            "To know what a job does to people, go and do it.",
        ],
        "apply":
            "Where you are: you work at it every day and it feels less and "
            "less like you doing it.\n"
            "Ask first: which step in this job is waiting on my judgement? "
            "When did something I said last change how the next thing was "
            "done?\n"
            "Where it goes wrong: reading it as manual work harms and "
            "desk work does not. Her test is whether the work needs you to "
            "think, not whether it tires you. A desk job that needs no "
            "thought scores identically.",
    },
    {
        "k": "force-makes-things",
        "n": "Force turns both sides into things",
        "w": "The side holding it is being altered too",
        "src": "The Iliad, or the Poem of Force (1939)",
        "dek": "Reading a war usually means picking a side. What is worth "
               "reading is why she says the poem's real subject is neither "
               "of them.",
        "story":
            "She reread the Iliad and said its true hero is not Achilles "
            "and not Hector but force — the thing that turns a person into "
            "a thing. The struck side goes first: corpse, captive, prize "
            "to be traded. ==Her real finding is that the side holding it "
            "changes too.== The winner takes the force in his hands for a "
            "property of himself, and can no longer picture the day it "
            "comes round to him. Hector, killing, does not know tomorrow "
            "is his. Achilles, dragging a body round the walls, does not "
            "know how near his own death is.",
        "f": [
            {"n": "Force acts at both ends",
             "d": "Common sense sees damage only where the pressure lands. "
                  "Her claim is harder: whoever holds force is being "
                  "remade by it, because force persuades its holder that it "
                  "is part of him rather than something briefly in his "
                  "hands.",
             "eg": "Give someone a veto and they soon feel their opinions "
                   "were always the better ones. Their judgement has not "
                   "improved; they have stopped receiving contradiction."},
            {"n": "The winner's blind spot is tomorrow",
             "d": "Every man in Homer who kills in a frenzy is dead a few "
                  "hundred lines later. Force takes not a man's conscience "
                  "but his sense of time — it swaps I am stronger now for "
                  "it will always be like this, and he makes decisions that "
                  "hold only in a world that never turns.",
             "eg": "The party with all the leverage signs the contract the "
                   "other side cannot perform, because it has stopped "
                   "assuming the relationship continues next year."},
            {"n": "The antidote is still being able to imagine the other as a person",
             "d": "The most famous scene in the poem is Priam entering "
                  "Achilles' tent at night to ask for his son's body, and "
                  "the two of them weeping together. She says that is the "
                  "moment force pauses — not because anyone turned kind, "
                  "but because someone saw a person again.",
             "eg": "Facing an opponent who has already lost, there is one "
                   "check on your own condition: can I still say what he is "
                   "afraid of right now? If not, force is working on me."},
        ],
        "q": [
            "Force is what turns a person into a thing, at both ends.",
            "The winner loses not his conscience but his idea of tomorrow.",
            "Priam and Achilles wept together, and force stopped for a "
            "moment.",
        ],
        "apply":
            "Where you are: you now hold power over someone, or someone "
            "holds it over you.\n"
            "Ask first: if the positions reverse next year, does today's "
            "decision still stand? Can I still say what the other side is "
            "afraid of?\n"
            "Where it goes wrong: reading it as therefore never use force. "
            "She is not against using it; she offers a self-check — whether "
            "you can still imagine the other side as a person. The moment "
            "you cannot, you are the one being altered.",
    },
]
