# -*- coding: utf-8 -*-
"""Andy Grove — English.

Only the Paranoid Survive is on the reader's shelf or at least in his
vocabulary, usually reduced to a mood: be worried, all the time. Grove's
paranoia has an object and a procedure. One chapter is the sentence he said
to Gordon Moore in 1985 and what it does to sunk cost; the other is the
machinery he built so that the people who feel the change first can reach the
people who can act on it. Both quotations here are his own words.
"""

PARENT = {
    "name": "Andy Grove",
    "slug": "grove",
    "blurb": "Deep read",
    "items": [
        {"k": "revolving-door", "n": "The revolving door test",
         "w": "Become your own successor", "ready": True,
         "line": "What would a new chief executive do? Then why not do it "
                 "ourselves"},
        {"k": "inflection-and-cassandras",
         "n": "Inflection points and the people who warn you",
         "w": "The channel bad news travels down", "ready": True,
         "line": "When the tenfold change lands, the front line knows first"},
    ],
}

CHAPTERS = [
    {
        "k": "revolving-door",
        "n": "The revolving door test",
        "w": "Become your own successor",
        "src": "Only the Paranoid Survive",
        "dek": "Intel was built on memory chips and nearly died of them. What "
               "was said in one office in 1985.",
        "story":
            "By 1985 Japanese makers had driven memory prices through the "
            "floor, Intel had lost money for several quarters, and the "
            "argument over whether to hold the business had run for a year. "
            "Grove asked Moore: if we got kicked out and the board brought in "
            "a new chief executive, what do you think he would do? Moore "
            "answered without hesitating: ==he would get us out of "
            "memories.== Grove looked at him and said, why shouldn't you and "
            "I walk out the door, come back, and do it ourselves? Intel "
            "amputated and went all in on microprocessors.",
        "f": [
            {"n": "A successor's view is the same machine with the feelings "
                  "removed",
             "d": "A new chief executive sees exactly the data you see. One "
                  "thing differs: no sunk cost, no credit from the old days, "
                  "no this is what we were founded on. The test borrows his "
                  "eyes, and the answer usually turns out to have been there "
                  "already, held under by feeling.",
             "eg": "Stuck on cutting a line you raised yourself, ask what a "
                   "parachuted successor does in his first week. If he cuts "
                   "it, the only open question is who swings the axe."},
            {"n": "Walk out and walk back in. Both steps count",
             "d": "The precision of the image is that it has two halves. "
                  "Walking out sheds the old identity; walking back in "
                  "executes under the new one. The first alone is avoidance, "
                  "seeing clearly and not moving. The second alone is "
                  "butchery, cutting without having changed your mind.",
             "eg": "Announcing a new direction while still measuring everyone "
                   "on the old business is walking back in with your head "
                   "left outside. The change happened in the memo."},
            {"n": "Doing it yourself is how you keep the people who do it",
             "d": "The half of his sentence that gets dropped is by "
                  "ourselves. Wait for a board to bring somebody in to do the "
                  "identical thing and the company bleeds two more years "
                  "first. Do it yourself and the pain is the same, but the "
                  "memory is we turned, not we were rescued.",
             "eg": "The same cut announced by the founder who takes the blame "
                   "leaves a different organisation than one made by an "
                   "incoming team. The first team will turn with you again."},
        ],
        "q": [
            "If we got kicked out, what would a new chief executive do?",
            "Why shouldn't you and I walk out the door and do it ourselves?",
            "The first thing to overcome is your own emotional attachment.",
        ],
        "apply":
            "Where you are: a business you have feelings about is bleeding "
            "steadily and you cannot bring yourself to act.\n"
            "Ask first: what would my successor do with it in his first "
            "month? Does that answer contain any information I do not have — "
            "and if it does not, the only thing stopping me is feeling.\n"
            "Where it goes wrong: using the test as a switch for turning off "
            "responsibility, cutting and then disowning the cut. Or playing "
            "successor with everything, until the patience some things need "
            "gets cut too.",
    },
    {
        "k": "inflection-and-cassandras",
        "n": "Inflection points and the people who warn you",
        "w": "The channel bad news travels down",
        "src": "Only the Paranoid Survive",
        "dek": "When the tenfold change arrives the top floor is almost "
               "always last to hear. His prescription for that structural "
               "lag.",
        "story":
            "Grove calls a change that rewrites the foundations of an "
            "industry a ==strategic inflection point==: one factor moves by a "
            "factor of ten and the old map is void. Its cruellest property is "
            "that it comes with no alarm bell, and by the time the data is "
            "clear the best window has shut. His remedy is a kind of person, "
            "the helpful Cassandras: the middle managers and front-line staff "
            "who feel it first. He asks management not to be cleverer but to "
            "let bad news travel faster than good, and to stay close to the "
            "frightened messenger.",
        "f": [
            {"n": "The turn is late in the data and on time in the feel",
             "d": "Early in a tenfold change the statements still look "
                  "healthy, because existing customers carry you a year or "
                  "two on inertia. The first signals are qualitative: the "
                  "questions customers ask, where the hiring market moves, "
                  "how deals are now lost. By the time those reach a report "
                  "they are an obituary.",
             "eg": "Revenue is still climbing, and new customers start "
                   "putting you on the same comparison sheet as a rival you "
                   "look down on. That is page one."},
            {"n": "How the Cassandras are treated decides whether the alarm "
                  "exists",
             "d": "Somebody always felt it earlier. The question is what "
                  "happened to them when they said so. If the last person to "
                  "bring bad news was quietly frozen out, the warning system "
                  "shut down that day. Not nobody saw it: everybody who saw "
                  "it learned to be silent.",
             "eg": "In a review, ask who noticed first, whether they spoke, "
                   "and what happened to them afterwards. The third answer "
                   "decides whether anyone speaks next time."},
            {"n": "Put money behind the unease at the edge, not just an ear",
             "d": "Hearing the Cassandra is only step one. His practice was "
                  "to fund the unease: real budget for hedging experiments, "
                  "so a judgement at the edge gets a chance to grow into "
                  "data. Open-mindedness that funds nothing ends where "
                  "deafness ends, because the turn will not wait.",
             "eg": "When the front line keeps saying a new category is taking "
                   "customers, stop arguing about whether it is true. Give a "
                   "small team a budget and three months. You are buying "
                   "information, not a business."},
        ],
        "q": [
            "A strategic inflection point rarely comes with an alarm bell.",
            "Let bad news travel faster than good news.",
            "Snow melts first at the periphery.",
        ],
        "apply":
            "Where you are: a signal from the edge is making you uneasy, and "
            "the numbers are still calm.\n"
            "Ask first: who stands closest to this signal? What happened to "
            "them the last time they brought bad news? Could a small sum let "
            "the signal turn itself into evidence?\n"
            "Where it goes wrong: turning paranoia into a general alarm where "
            "every noise mobilises everybody. Or protecting the messengers "
            "beautifully and then never acting on what they said.",
    },
]
