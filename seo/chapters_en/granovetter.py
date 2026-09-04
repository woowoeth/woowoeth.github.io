# -*- coding: utf-8 -*-
"""Mark Granovetter — English."""

PARENT = {
    "name": "Mark Granovetter",
    "slug": "granovetter",
    "blurb": "Deep read",
    "items": [
        {"k": "weak-ties", "n": "The strength of weak ties",
         "w": "Opportunity arrives from people you rarely see", "ready": True,
         "line": "56% saw the person who helped them only occasionally"},
        {"k": "no-strong-tie-is-a-bridge", "n": "No strong tie is a bridge",
         "w": "The people closest to you know what you know", "ready": True,
         "line": "It sounds like a phrase. It's a structural result"},
    ],
}

CHAPTERS = [
    {
        "k": "weak-ties",
        "n": "The strength of weak ties",
        "w": "Opportunity arrives from people you rarely see",
        "src": "Granovetter, The Strength of Weak Ties, AJS, 1973",
        "dek": "Who to ask when you're looking for work. Your instinct gives "
               "the wrong answer; here's what the data gave.",
        "story":
            "In 1973 Granovetter surveyed 282 people about how they found "
            "their jobs. Among those who got there through a personal "
            "contact, ==56% said they saw that person only occasionally, and "
            "28% said rarely== — the people who mattered were the ones they "
            "barely knew. That runs against instinct: your closest friends "
            "want to help you most. But the reason isn't willingness, it's "
            "information. Your circles overlap almost completely with your "
            "closest friends'; someone you rarely see is standing in a "
            "different network.",
        "f": [
            {"n": "What matters isn't willingness, it's whether the news is new",
             "d": "Close friends are more willing to help and hold almost the "
                  "same information you do — same people, same news. A weak "
                  "tie is not more generous. He is standing somewhere else, "
                  "holding the part you can't reach from where you are.",
             "eg": "You already knew about the opening in the team chat. The "
                   "genuinely new thing comes from the person you see once a "
                   "year."},
            {"n": "So maintain breadth, not depth",
             "d": "This changes where the effort goes: rather than pouring "
                  "all of it into a few people, keep more weak ties in the "
                  "'still knows who you are' state. The cost is tiny — an "
                  "occasional message, a hello with no request attached — and "
                  "that's enough to keep the line usable.",
             "eg": "Contacting old colleagues only once you want to move is "
                   "usually too late. That line has to be kept while you "
                   "don't need it."},
            {"n": "When you move, weak ties are what breaks first",
             "d": "Change city or leave an industry and what disappears isn't "
                  "the close friends — those survive — it's the wide band of "
                  "people you saw occasionally. That's exactly the layer that "
                  "supplies new opportunities, so the drought after a move "
                  "isn't imagined. It's structural.",
             "eg": "Six months in a new city and nothing comes to you. You "
                   "didn't get worse. That layer hasn't been built yet."},
        ],
        "apply":
            "Where you are: you're looking for something — a job, a partner, "
            "customers — and circling the same few people.\n"
            "Ask first: of everyone I've contacted in six months, how many do "
            "I see only a few times a year? If almost none, one whole source "
            "of opportunity is switched off.\n"
            "Where it goes wrong: reading it as collect contacts — a weak tie "
            "only works if the person still knows who you are and what you "
            "do; and don't neglect close friends for this. That's a different "
            "loss.",
        "q": [
            "Of people who found work through a contact, 56% saw them only "
            "occasionally.",
            "Your closest friends want to help most. The useful news sits "
            "further out.",
            "When you move, the layer that breaks first is the one that "
            "brought opportunities.",
        ],
    },
    {
        "k": "no-strong-tie-is-a-bridge",
        "n": "No strong tie is a bridge",
        "w": "The people closest to you know what you know",
        "src": "Granovetter 1973, on bridges",
        "dek": "It sounds like a turn of phrase. It's a structural result, "
               "and here is what it rests on.",
        "story":
            "Granovetter states it flatly: ==no strong tie is a bridge==. The "
            "reason isn't sentiment, it's geometry. If you're close to A and "
            "close to B, then A and B probably know each other — close people "
            "introduce each other, and the circle closes. Once it's closed, "
            "the three of you know largely the same things, and none of you "
            "is a route to anywhere outside. Only rarely-used ties can be "
            "bridges, because only they have non-overlapping networks at each "
            "end.",
        "f": [
            {"n": "Closure is what strong ties inevitably produce",
             "d": "This isn't a question of social strategy, it's geometry: "
                  "closeness means frequent contact, and frequent contact "
                  "makes your friends meet each other. Closure itself is "
                  "good — it's where support and trust come from — but it "
                  "also means information circulates rather than arrives.",
             "eg": "A tight team is superbly informed internally and the "
                   "slowest in the building to notice what's changing "
                   "outside."},
            {"n": "To test whether a tie is a bridge, look at the overlap",
             "d": "The test is simple: if this person knows most of the "
                  "people you know, he isn't a bridge; if you share very few "
                  "mutual contacts, he probably is. A bridge's value has "
                  "nothing to do with how close you are and everything to do "
                  "with the overlap at each end.",
             "eg": "The person you share two mutual friends with is likelier "
                   "to bring you something new than the one you share thirty "
                   "with."},
            {"n": "A group's health shows in how many bridges it has",
             "d": "Applied to a team: an organisation made entirely of strong "
                  "ties is warm inside and slowest to react to anything "
                  "outside. What needs protecting is the few people who don't "
                  "quite fit in and spend time elsewhere. They are the "
                  "bridges, and bridges are what cohesion squeezes out first.",
             "eg": "The one who's always off with another department is "
                   "usually the door news comes through."},
        ],
        "apply":
            "Where you are: you want yourself or your team to hear sooner "
            "what's happening outside.\n"
            "Ask first: how many lines do I have into circles that don't "
            "overlap with mine? Name them. If you can't name one, build a "
            "bridge before deepening what you already have.\n"
            "Where it goes wrong: using this to dismiss close ties — they "
            "supply support and trust, a different job entirely; or setting "
            "out to 'network outward', which makes the tie a task, and those "
            "don't hold.",
        "q": [
            "No strong tie is a bridge.",
            "Close to A and close to B? A and B probably know each other.",
            "Bridges are what a group squeezes out first when it wants "
            "cohesion.",
        ],
    },
]
