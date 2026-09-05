# -*- coding: utf-8 -*-
"""Jensen Huang — English.

He speaks English in public and the lines here are his own, which matters,
because the popular version of this story is that he got lucky with a bet on
graphics chips. The two chapters are the parts luck cannot explain: a decade
of funding a market whose size was zero, and a decision to walk out of the
fastest-growing category he was in. The second is the one nobody copies.
"""

PARENT = {
    "name": "Jensen Huang",
    "slug": "huang",
    "blurb": "Deep read",
    "items": [
        {"k": "zero-billion-markets", "n": "Zero-billion-dollar markets",
         "w": "Entering before the market exists", "ready": True,
         "line": "No competitors, because there are no customers yet"},
        {"k": "strategic-retreat", "n": "Retreating with dignity",
         "w": "The second story in the Taipei address", "ready": True,
         "line": "Retreat is hardest for the people who never fail"},
    ],
}

CHAPTERS = [
    {
        "k": "zero-billion-markets",
        "n": "Zero-billion-dollar markets",
        "w": "Entering before the market exists",
        "src": "Public talks and interviews over the years",
        "dek": "He has his own name for how the company chooses. How to stay "
               "alive inside a market that does not exist yet.",
        "story":
            "He describes the choice in one phrase: ==we go after "
            "zero-billion-dollar markets==. Not billion-dollar markets. "
            "Markets whose present size is zero, where nobody is competing "
            "because nobody is yet buying. CUDA is the case. From 2006 the "
            "graphics chip was rebuilt for scientific computing and handed "
            "free to researchers everywhere, and the spending looked terrible "
            "on the statements for close to a decade, until deep learning "
            "arrived and everyone discovered the AI world was standing on his "
            "foundations. His explanation: if the market already exists, you "
            "are playing a game somebody else wrote the rules for.",
        "f": [
            {"n": "A zero market buys the seat where the rules get written",
             "d": "Enter a mature market and the product, the channels and "
                  "the standards belong to somebody else; you are scoring on "
                  "their board. Enter at zero and the toolchain, the "
                  "developer habits and the interfaces are yours to write. "
                  "What you buy is not a head start. It is the referee's "
                  "chair.",
             "eg": "Early in a category the valuable move is not selling "
                   "units. It is making your interface the default, so later "
                   "arrivals build on your ground however good they are."},
            {"n": "Getting through it takes two lines of blood supply",
             "d": "A zero market pays nothing for ten years, so what keeps "
                  "the company alive? Two tracks. Gaming cards as the mature "
                  "business feeding cash, CUDA as the zero track burning it. "
                  "Without the first the second is suicide; without the "
                  "second the first is merely a good business.",
             "eg": "Feed one dark line off the cash cow and exempt it from "
                   "revenue targets for five years. Most companies fail this "
                   "on the quarterly question, not on the money."},
            {"n": "Which zero to pick is read off physics, not off research",
             "d": "A zero market has no users to survey, because the demand "
                  "is not there to ask about. His basis was harder: the "
                  "growth curve of demand for computation, the physical "
                  "advantage of running things in parallel. The only "
                  "dependable map here is where the technology curve points.",
             "eg": "Surveys cannot ask about the unseen. Watch where the "
                   "underlying cost curve is falling and what crossing a "
                   "threshold would unlock. That crossing is the market's "
                   "birthday."},
        ],
        "q": [
            "We go after zero-billion-dollar markets.",
            "There are no competitors there, because there are no customers "
            "yet.",
            "If the market already exists, you are playing somebody else's "
            "game.",
        ],
        "apply":
            "Where you are: a direction with no market today, and every "
            "projection tells you to drop it.\n"
            "Ask first: if it does come true, who writes the rules? Do I have "
            "a line of supply that lasts until then? Am I betting on an "
            "opinion or on a physical curve?\n"
            "Where it goes wrong: treating everything nobody is doing as a "
            "zero-billion gold mine. Most markets that are zero stay zero "
            "permanently.",
    },
    {
        "k": "strategic-retreat",
        "n": "Retreating with dignity",
        "w": "The second story in the Taipei address",
        "src": "Commencement address at National Taiwan University, 2023",
        "dek": "One of the three stories he told the graduates is about "
               "giving up. Why he says retreat is hardest for the ablest.",
        "story":
            "At the 2023 Taipei commencement he told the story of leaving "
            "mobile chips. Nvidia had entered mobile processors early, then "
            "saw giants ringing the category and the margin being squeezed "
            "out, and knew that dropping it meant dropping the biggest growth "
            "story it had. They dropped it, and moved the chips toward "
            "robotics and AI. Then he named the psychology out loud: "
            "==retreat does not come easily to brilliant, successful people "
            "like you==; but strategic retreat, sacrifice, deciding what to "
            "give up, is core to success. Hence the second half of the famous "
            "line: run, don't walk.",
        "f": [
            {"n": "The abler you are, the dearer admitting defeat costs",
             "d": "A clever person's record holds no failures, and that is "
                  "precisely the burden. Retreat is not a business adjustment "
                  "for him, it is a threat to identity: the story I never "
                  "give up is what stops him doing the right thing. Watch for "
                  "star teams defending ground that should be given up.",
             "eg": "The failing project hardest to kill is the one handed to "
                   "the best team. Not because it deserves rescuing, but "
                   "because nobody wants a loss on that record."},
            {"n": "Retreat on the structure, not on this quarter's fighting",
             "d": "Mobile chips were still growing when they left. What they "
                  "read was not the quarter but the structure: giants "
                  "subsidising the modem, a visible ceiling on margin, their "
                  "own comparative advantage sitting elsewhere. Retreat timed "
                  "off the fighting always comes too late to bring the troops "
                  "out whole.",
             "eg": "It is still growing, so let us look again is reading the "
                   "fighting. Growing does not change who upstream takes the "
                   "margin is reading the structure."},
            {"n": "A retreat has to become a redeployment the same day",
             "d": "The period that took them out of mobile put the engineers "
                  "onto the robotics platform. The value of a retreat is not "
                  "the loss it stops but the freed strength having somewhere "
                  "to go immediately. Withdrawal without redeployment is "
                  "bleeding; withdrawal into a new formation is manoeuvre.",
             "eg": "The announcement that cuts a line has to name the new "
                   "position and who goes there. Retreat first and think "
                   "later cuts the team's belief in the next attack too."},
        ],
        "q": [
            "Retreat does not come easily to brilliant, successful people.",
            "Strategic retreat, sacrifice, deciding what to give up, is core "
            "to success.",
            "Run, don't walk.",
        ],
        "apply":
            "Where you are: a business that is still growing, has no "
            "structural way out, and is the team's pride.\n"
            "Ask first: is what stops us a structural judgement, or the story "
            "that we never give up? For the people and money coming out, have "
            "we named where they go?\n"
            "Where it goes wrong: reading strategic retreat as a pass to "
            "withdraw whenever things get hard. Or retreating without "
            "redeploying, so the freed resources sit in the account going "
            "mouldy.",
    },
]
