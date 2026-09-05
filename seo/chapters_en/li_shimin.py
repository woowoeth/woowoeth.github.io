# -*- coding: utf-8 -*-
"""Li Shimin — English.

Tang Taizong reaches the English reader, if at all, as a good emperor, which
is the least interesting thing about him. What the Zhenguan record actually
preserves is closer to an operating manual: an information structure rather
than a virtue, a metaphor used as a check before every call on the people,
and one argument at the start of the reign where he took the slower road
against the more experienced man in the room.
"""

PARENT = {
    "name": "Li Shimin",
    "slug": "li-shimin",
    "blurb": "Deep read",
    "items": [
        {"k": "hearing-all-sides", "n": "Listen to all sides",
         "w": "One source is not listening", "ready": True,
         "line": "How many channels you have decides how good your judgement is"},
        {"k": "boat-and-water", "n": "Water carries the boat",
         "w": "What holds you up can turn you over", "ready": True,
         "line": "The thing carrying you is the thing that can tip you over"},
        {"k": "the-first-debate", "n": "The argument at the start of Zhenguan",
         "w": "He took the slower road", "ready": True,
         "line": "Everyone said there was no time. He waited several years"},
    ],
}

CHAPTERS = [
    {
        "k": "hearing-all-sides",
        "n": "Listen to all sides",
        "w": "One source is not listening",
        "src": "Essentials of Government of the Zhenguan Era, The Way of the "
               "Ruler",
        "dek": "The emperor asked what makes a ruler clear-sighted. The "
               "answer he got describes an information structure, not a "
               "virtue.",
        "story":
            "Taizong asked Wei Zheng what separates a clear-sighted ruler "
            "from a benighted one. ==Listening to all sides makes you clear; "
            "trusting one source leaves you in the dark.== Then the examples: "
            "Yao and Shun opened the four gates, so no one could screen them "
            "off; the Second Emperor of Qin trusted Zhao Gao alone and did "
            "not know the realm had risen until it was over; Yang of Sui "
            "trusted Yu Shiji, and provinces were in revolt while the news "
            "never reached him. The conclusion is practical: when a ruler "
            "hears widely, the great ministers cannot block, and what is "
            "below reaches the top.",
        "f": [
            {"n": "Screening you off requires no lying",
             "d": "Zhao Gao and Yu Shiji need not have lied in every "
                  "sentence; they only had to control which reports went up. "
                  "When all information passes one person, that person "
                  "decides the world you see without inventing anything. The "
                  "root is the number of channels, not anyone's loyalty.",
             "eg": "If one team assembles and presents all the business data, "
                   "it need not falsify a figure. Choosing which metrics "
                   "reach the dashboard has already shaped your judgement."},
            {"n": "The channels have to be strangers to each other",
             "d": "The value of hearing all sides comes from independence "
                  "between the sources. Three accounts drawn from the same "
                  "meeting and the same document are one thing heard three "
                  "times. Real breadth requires people with no shared boss "
                  "and no shared interest.",
             "eg": "Ask three directors the same question and get one answer. "
                   "That may mean the facts are clear, or that they met "
                   "yesterday. Ask a fourth who was not there."},
            {"n": "Measure how fast bad news arrives",
             "d": "Yang of Sui's problem was not an absence of bad news; it "
                  "was that bad news could not get to him. The most direct "
                  "gauge of an organisation's information health is one "
                  "number: from the moment a clear problem occurs to the "
                  "moment you hear, how long, and through how many people?",
             "eg": "A live incident took six hours and four layers to reach "
                   "you. The thing that actually needs fixing is not that "
                   "bug."},
        ],
        "q": [
            "Listening to all sides makes you clear; one source, dark.",
            "Hear widely and the great ministers cannot block what comes up.",
            "Three accounts from one meeting are one thing heard three times.",
        ],
        "apply":
            "Where you are: everything you know about this arrived through a "
            "single reporting line.\n"
            "Ask first: who else knows about this and has no stake in that "
            "line?\n"
            "Where it goes wrong: taking hearing all sides to mean asking "
            "more people from the same circle; counting good news and never "
            "timing how long bad news takes.",
    },
    {
        "k": "boat-and-water",
        "n": "Water carries the boat",
        "w": "What holds you up can turn you over",
        "src": "Essentials of Government of the Zhenguan Era, On Governance; "
               "Instructions to the Crown Prince",
        "dek": "The line has been recited for over a thousand years. Under "
               "Taizong it was a piece of daily working discipline.",
        "story":
            "Taizong told his attendants that the way of a ruler must begin "
            "with keeping the people whole; injuring the people to serve "
            "yourself is like cutting flesh off your thigh to fill your "
            "stomach — the belly fills and the body dies. To the crown prince "
            "he repeated one figure again and again: ==the ruler is the boat, "
            "the common people are the water; water carries the boat and "
            "water can capsize it.== The image comes from Xunzi; in these "
            "years it was used as a check to run before every call on the "
            "people's labour. It was there to be applied, not admired.",
        "f": [
            {"n": "The thing holding you up is the thing that overturns you",
             "d": "What makes the figure sharp is the identity: it is not one "
                  "force supporting you and a different force opposing you. "
                  "The force carrying you is the one that can turn you over. "
                  "So stability does not come from suppressing it; it comes "
                  "from never taking it to the tipping point.",
             "eg": "Your core users are both the revenue and the public "
                   "voice. The same people are the moat when handled well and "
                   "the loudest critics the next morning when not."},
            {"n": "Cutting the thigh happens gradually",
             "d": "The belly fills and the body dies describes a slow "
                  "process: each extraction from below relieves the immediate "
                  "difficulty at once, while the cost is spread across a "
                  "future nobody is looking at. That is why it is almost "
                  "always the best move this period, and exactly why it is "
                  "dangerous.",
             "eg": "Stuff the channel with inventory at each quarter end and "
                   "every quarter looks good. Three years on the channel is "
                   "loss-making and gone, and each single decision was "
                   "reasonable."},
            {"n": "Keep one person whose job is to disagree",
             "d": "Wei Zheng remonstrated on more than two hundred matters "
                  "and repeatedly left the emperor nowhere to go, and stayed. "
                  "With bronze as a mirror you straighten your dress; with a "
                  "man as a mirror you see your gains and losses. In "
                  "practice: institutionalise the objector and do not move "
                  "him for objecting badly.",
             "eg": "Name someone to argue the opposite case at a major "
                   "decision meeting, and make explicit that doing it will "
                   "not affect their review. Without that role, meetings only "
                   "confirm."},
        ],
        "q": [
            "Water carries the boat, and water can capsize it.",
            "The belly fills and the body dies.",
            "With a man as a mirror, you see your losses.",
        ],
        "apply":
            "Where you are: to hit the target in front of you, you need to "
            "take a bit more from one side.\n"
            "Ask first: is that side also the one holding me up? How much "
            "margin is left after this time?\n"
            "Where it goes wrong: reading the people's support as a mood to "
            "be soothed; having nobody near you whose job is to disagree and "
            "who is not punished for it.",
    },
    {
        "k": "the-first-debate",
        "n": "The argument at the start of Zhenguan",
        "w": "He took the slower road",
        "src": "Essentials of Government of the Zhenguan Era, On Governance",
        "dek": "You inherit a wreck. Harsh law, or lenient rule? He picked "
               "the option everyone told him there was no time for.",
        "story":
            "Early in the Zhenguan years the country was exhausted. Taizong "
            "asked what to do. Wei Zheng argued for government by benevolence "
            "and right. Feng Deyi rebutted him forcefully: after the Three "
            "Dynasties human character grew thin, which is why Qin used law "
            "and Han mixed in force — they wanted to transform people and "
            "could not. He called Wei Zheng a bookish man whose advice would "
            "wreck the state. Taizong went with Wei Zheng. Some years later: "
            "==traders camped in the open, there were no more bandits, the "
            "jails stood empty, and doors were left unbarred.== Taizong told "
            "his court: this is what Wei Zheng urged on me.",
        "f": [
            {"n": "The realistic-sounding option is usually the faster one",
             "d": "Feng Deyi's evidence was all historical experience and "
                  "sounded far more solid than Wei Zheng's case. But his real "
                  "advantage was not being right; it was showing results "
                  "sooner. Harsh law works within the year, transformation "
                  "takes several. The side called realistic usually has the "
                  "short cycle.",
             "eg": "Strict targets lift the numbers this month; building "
                   "capability takes a year. The first always argues better "
                   "in the room, because its evidence arrives early."},
            {"n": "To beat a prejudice, take its premise to the end",
             "d": "Wei Zheng's counter was hard: if human character really "
                  "declines one generation after another, by now everyone "
                  "would be a ghoul, and there would be nothing left to "
                  "transform. He did not out-read his opponent in history. He "
                  "showed the premise produces an absurdity.",
             "eg": "Against new hires are not as solid as the old ones, skip "
                   "the counter-examples. Ask instead why, on that logic, the "
                   "company still runs after twenty years."},
            {"n": "Choosing slow means carrying the years in the middle",
             "d": "The result showed up several years later, and through "
                  "those years there was nothing to display while Feng Deyi's "
                  "route could be proposed again at any moment. The "
                  "difficulty of a long-cycle choice is not the moment of "
                  "deciding. It is not turning at each subsequent challenge.",
             "eg": "Commit two years to rebuilding the platform and by month "
                   "three someone asks why you did not just add people. "
                   "Whether you hold through those asks decides it."},
        ],
        "q": [
            "Traders camped in the open, and the jails stood empty.",
            "The side called realistic is often only the faster one.",
            "If character always declined, there would be nothing left to "
            "teach.",
        ],
        "apply":
            "Where you are: two options, one that shows results quickly and "
            "one that is more fundamental but has to be waited for.\n"
            "Ask first: is the reason it is called realistic that it is more "
            "correct, or that it is faster?\n"
            "Where it goes wrong: mistaking a short cycle for realism; "
            "picking the long option and turning at the first challenge.",
    },
]
