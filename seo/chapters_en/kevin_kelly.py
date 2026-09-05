# -*- coding: utf-8 -*-
"""Kevin Kelly — English.

The essay is one page long, free, and most English readers think they already
have it: a thousand fans, a hundred dollars, done. What gets dropped is the
second condition Kelly attached in the same essay, without which the sum does
not close at all. These pages restore his own sentences rather than a
translation of them, and give the condition equal weight.
"""

PARENT = {
    "name": "Kevin Kelly",
    "slug": "kevin-kelly",
    "blurb": "Deep read",
    "items": [
        {"k": "thousand-true-fans", "n": "A thousand true fans",
         "w": "Not famous, but deep enough", "ready": True,
         "line": "A thousand people at a hundred dollars each is a living"},
        {"k": "direct-relationship", "n": "Nobody in the middle",
         "w": "The money has to reach you directly", "ready": True,
         "line": "Put a platform in between and the arithmetic stops working"},
    ],
}

CHAPTERS = [
    {
        "k": "thousand-true-fans",
        "n": "A thousand true fans",
        "w": "Not famous, but deep enough",
        "src": "1,000 True Fans, 2008, kk.org/thetechnium",
        "dek": "Creators assume fame has to come first. This asks whether "
               "that assumption is necessary at all, and what replaces it.",
        "story":
            "In 2008 Kelly worked out an arithmetic problem for independent "
            "creators: ==a creator needs to acquire only 1,000 True Fans to "
            "make a living==. One thousand customers at a hundred dollars is "
            "a hundred thousand, which is enough for one person. His "
            "definition of a true fan is hard: someone who will buy anything "
            "you produce, who will drive 200 miles to see you sing, who buys "
            "the hardback and the paperback and the audio version of the same "
            "book. The value of the sum is not the number. It is that fame "
            "has been taken off the list of requirements.",
        "f": [
            {"n": "A thousand can be counted one at a time; a million cannot",
             "d": "This is the solid part of the sum. A thousand people, "
                  "three a day, takes a year, and that is a schedule you can "
                  "execute. A million is not something effort assembles, it "
                  "is a lottery ticket. The two ask for completely different "
                  "working days.",
             "eg": "Did one more person who will actually come back arrive "
                   "today? You can ask that every evening. Did I go viral "
                   "today? You cannot."},
            {"n": "A hundred dollars a year is a question about what you make",
             "d": "Run the number backwards and it turns into a design brief: "
                  "what do you have to produce in a year that someone who "
                  "genuinely likes you will spend a hundred dollars on? It "
                  "pushes you off make more content and onto make one thing "
                  "worth buying, which is different work.",
             "eg": "A year of free updates is worth less than one thing they "
                   "will pay for: a course, a printed book, an evening in a "
                   "room with you."},
            {"n": "Kelly says this can become a second full-time job",
             "d": "He never sold it as the easy road. Maintaining a thousand "
                  "direct relationships, answering mail, shipping orders, "
                  "running events, is slow and absorbing work, and done "
                  "properly it is another full-time job. Reading it as a "
                  "shortcut around fame is a misreading.",
             "eg": "The worst stretch is a few hundred fans: not yet a "
                   "living, and already two hours of replies every day."},
        ],
        "q": [
            "A creator needs to acquire only 1,000 True Fans to make a "
            "living.",
            "A True Fan is defined as a fan that will buy anything you "
            "produce.",
            "They will drive 200 miles to see you sing.",
        ],
        "apply":
            "Where you are: you make things, and you are waiting for one of "
            "them to break out.\n"
            "Ask first: how many people would actually pay me today, and how "
            "many of them can I name? Can I make one hundred-dollar thing "
            "this year?\n"
            "Where it goes wrong: treating a thousand as a follower count to "
            "farm, so the fans exist and nothing is for sale; or believing "
            "this road is lighter than fame, when Kelly says it may be a "
            "second job.",
    },
    {
        "k": "direct-relationship",
        "n": "Nobody in the middle",
        "w": "The money has to reach you directly",
        "src": "The second condition in 1,000 True Fans, rechecked against "
               "the platform era",
        "dek": "The sum carries a second condition almost everyone skips. "
               "This is what happens to the arithmetic once you skip it.",
        "story":
            "Kelly set two conditions and most people remember only the "
            "first. The second is this: ==you must have a direct "
            "relationship with your fans; they must pay you directly==. Put "
            "a platform in the middle and everything changes. It takes a cut, "
            "it holds the list, it decides who gets to see you. His 2008 "
            "reference points were blogs and MySpace. The present is tighter: "
            "a service like Spotify will hand you chart positions and never "
            "hand you an address. This is not a footnote to the essay. It is "
            "the switch that decides whether the sum works.",
        "f": [
            {"n": "Whoever holds the list holds your living",
             "d": "There is one test. If this platform throttles or bans you "
                  "tomorrow, can you still reach those thousand people? If "
                  "you cannot, you never had a thousand fans. You were "
                  "renting somebody else's traffic and calling it an "
                  "audience.",
             "eg": "A mailing list, a group chat, your own site: anything you "
                   "could walk out with counts. A follower number does not."},
            {"n": "The cut takes more than money, it takes the feedback",
             "d": "With a platform in between you cannot see who bought, why "
                  "they bought, or when they stopped. What you lose is not "
                  "only the percentage, it is the information that would let "
                  "you improve. The expensive part of a direct relationship "
                  "is the feedback, not the cash.",
             "eg": "One reply explaining why somebody unsubscribed is worth "
                   "more than a retention curve on a dashboard."},
            {"n": "Fix the exit before you chase the growth",
             "d": "Order matters here. Settle how do I take these people with "
                  "me before you spend a year growing on somebody else's "
                  "surface. Done the other way round, the day your follower "
                  "count looks best tends to be the day your leverage is "
                  "lowest.",
             "eg": "Put one route to reach you directly into every piece you "
                   "publish. It only gets more expensive the longer you "
                   "wait."},
        ],
        "q": [
            "You must have a direct relationship with your fans; they must "
            "pay you directly.",
            "The platform gives you chart positions. It never gives you an "
            "address.",
            "Fans you cannot reach without permission were never really "
            "yours.",
        ],
        "apply":
            "Where you are: you have readers or customers on a platform, and "
            "the platform holds every contact detail.\n"
            "Ask first: if I were throttled tomorrow, how many of them could "
            "I still reach by myself?\n"
            "Where it goes wrong: making the experience awkward in order to "
            "own the list, herding people off the platform; or assuming the "
            "list lets you drop the platform, when one is the door and the "
            "other is the insurance.",
    },
]
