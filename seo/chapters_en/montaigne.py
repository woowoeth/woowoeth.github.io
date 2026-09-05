# -*- coding: utf-8 -*-
"""Montaigne — English.

The English reader knows the word essay and often not the man who made it,
or knows him vaguely as a genial sceptic quoted in prefaces. What the page
has to establish is stranger and more useful: he is the first writer to
put his own weaknesses on the table before anyone else could, and he did
it deliberately, as a position rather than a confession.
"""

PARENT = {
    "name": "Montaigne",
    "slug": "montaigne",
    "blurb": "Deep read",
    "items": [
        {"k": "learning-to-die", "n": "To philosophise is to learn to die",
         "w": "After he was thrown from the horse", "ready": True,
         "line": "The dying was lighter than the decades of dreading it"},
        {"k": "what-do-i-know", "n": "What do I know?",
         "w": "Put your own weaknesses on the table first", "ready": True,
         "line": "A card you turn over yourself cannot be played against you"},
        {"k": "the-tower", "n": "At thirty-eight he moved into the tower",
         "w": "He fenced off a piece for himself", "ready": True,
         "line": "Not a retreat. A different desk"},
    ],
}

CHAPTERS = [
    {
        "k": "learning-to-die",
        "n": "To philosophise is to learn to die",
        "w": "After he was thrown from the horse",
        "src": "Essays I.20; II.6, Of practice",
        "dek": "He tells you to think about death daily, which sounds "
               "morbid. Then he reports having very nearly done it.",
        "story":
            "One essay is titled That to philosophise is to learn to die, "
            "and its method runs against instinct: ==do not look away, think "
            "about it daily, until it stops being strange.== This is not "
            "theory. In his thirties a rider knocked him off his horse from "
            "behind; he was unconscious a long time and the people around "
            "him thought he was dead. Coming back, he wrote the whole "
            "passage down. It had been light, like falling asleep, nothing "
            "like the horror he had spent decades imagining.",
        "f": [
            {"n": "Mostly you fear the imagining, not the thing",
             "d": "He came close enough to find the moment itself quiet. "
                  "Decades of dread had been aimed at a version his own head "
                  "had built. The experience cannot be lent to anyone, but "
                  "the sorting can: separate fear of the event from fear of "
                  "your picture of it.",
             "eg": "The dread that arrives at two in the morning is usually "
                   "a film, not the event."},
            {"n": "Avoided it stays terrible, looked at it flattens",
             "d": "His method is to make death ordinary: mention it, think "
                  "of it, keep it as an acquaintance. Only the unfamiliar is "
                  "frightening; once familiar it is merely a fact. Refuse to "
                  "look and the fear stays permanently new, which is exactly "
                  "what keeps it strong.",
             "eg": "Say the thing you fear out loud, write it down, and look "
                   "at it once a day."},
            {"n": "Learning to die is learning to weigh",
             "d": "He says whoever has taught people to die has taught them "
                  "to live. Once the heaviest item has genuinely been "
                  "handled, the arguments and the wounded pride of an "
                  "ordinary week change weight. This is not detachment, it "
                  "is pricing: using the heaviest thing to value the rest.",
             "eg": "Weigh the thing keeping you awake against I am going to "
                   "die anyway, and see what is left of it."},
        ],
        "q": [
            "The thing I fear most is fear.",
            "He who has learned how to die has unlearned how to serve.",
            "Let us deprive death of its strangeness. Let us frequent it.",
        ],
        "apply":
            "Where you are: you lie awake thinking about dying and have "
            "never said so to anyone.\n"
            "Ask first: is it the event I fear, or my version of it? Have I "
            "ever thought it through in daylight, from beginning to end?\n"
            "Where it goes wrong: reading it as think it through and the "
            "fear goes — he was still afraid in old age, only no longer run "
            "by it; and the daily thinking is for familiarity, not for "
            "sinking into it.",
    },
    {
        "k": "what-do-i-know",
        "n": "What do I know?",
        "w": "Put your own weaknesses on the table first",
        "src": "Essays II.12; the medal he had struck in 1576",
        "dek": "He wrote down his cowardice, his bad memory, his dithering. "
               "Not as confession. As a position that cannot be attacked.",
        "story":
            "In 1576 he had a medal struck for himself carrying three words: "
            "==What do I know?== The Essays are that question worked out at "
            "length. He writes that his memory is poor, that he dislikes "
            "pain, that he hesitates and contradicts himself from one page "
            "to the next, and he softens none of it. I do not portray being, "
            "he says, I portray passing. Four hundred years on it is still "
            "read, partly because the author's faults are placed at the "
            "front, where nobody else can pick them up and use them.",
        "f": [
            {"n": "A card you play yourself cannot be played against you",
             "d": "What people afraid of exposure actually fear is somebody "
                  "else naming the weakness first. He inverts it and names "
                  "it himself, more fully than anyone else could be "
                  "bothered to. Once a thing is face up on the table it has "
                  "stopped being in anybody's hand.",
             "eg": "Saying this part is not my area, up front, costs far "
                   "less than being caught out on it later."},
            {"n": "What do I know is a stance, not a modesty formula",
             "d": "He is not performing ignorance. He has made I might be "
                  "wrong his permanent standing position. From there, being "
                  "corrected requires no defence, because no claim to being "
                  "right was ever made. Defending is the expensive part, and "
                  "he simply removed the bill.",
             "eg": "Open with I may have this wrong, and the correction "
                   "costs you nothing to absorb."},
            {"n": "Inconsistency is not a flaw, it is a person",
             "d": "He says he portrays passing, not being. Most people panic "
                  "when someone says that is not what you told me last time. "
                  "He does not, because he announced from the start that he "
                  "changes. Admit that you move and nobody can pin you to a "
                  "fixed position.",
             "eg": "Told you never used to think this, yes, I changed is "
                   "shorter than any explanation you could give."},
        ],
        "q": [
            "What do I know?",
            "I do not portray being. I portray passing.",
            "A card you turn over yourself cannot be played against you.",
        ],
        "apply":
            "Where you are: you are in a seat that feels hollow, and you "
            "expect to be found out.\n"
            "Ask first: of the three faults you most fear being exposed, has "
            "one ever come out of your own mouth? Do you have a ready this "
            "is not my area?\n"
            "Where it goes wrong: reading it as confess everything and drop "
            "all guard — every fault he set down was thought about first; "
            "and what do I know is not a licence to judge nothing, he judges "
            "constantly, just never as final truth.",
    },
    {
        "k": "the-tower",
        "n": "At thirty-eight he moved into the tower",
        "w": "He fenced off a piece for himself",
        "src": "The 1571 inscription on his study wall; Essays III.13, Of "
               "experience",
        "dek": "The famous retirement was not a retirement. What he actually "
               "did is smaller, repeatable, and the reason the book exists.",
        "story":
            "In 1571, aged thirty-eight, he resigned his post as a "
            "magistrate in Bordeaux, went home to the family estate, and "
            "==turned the third floor of a tower into a library==, with an "
            "inscription on the wall saying he was weary of public duties "
            "and meant to give what remained to himself. The Essays were "
            "written in that room over the next twenty years. He also served "
            "two terms as mayor of Bordeaux in the middle of it. When kidney "
            "stones arrived he wrote the pain down there, page by page.",
        "f": [
            {"n": "Not withdrawal, a fenced-off piece",
             "d": "He did not become a hermit; he was mayor twice "
                  "afterwards. What he did was nail down one space and one "
                  "stretch of time as his and leave everything else running. "
                  "Full retreat is flight, no retreat is being eaten. The "
                  "position that holds is between them.",
             "eg": "One hour and one room a day that nobody else can reach, "
                   "everything else unchanged. Far easier than a new life."},
            {"n": "Mark it, and say it out loud to yourself",
             "d": "He had the decision carved into the wall. That is not "
                  "decoration, it is turning a vague intention into a "
                  "visible fact he walked past every morning. A decision "
                  "that has been written down outlives one that was only "
                  "thought about.",
             "eg": "This stretch is mine, put where you will see it, works "
                   "better than the same sentence held in your head."},
            {"n": "The pain got written in that room too",
             "d": "When the stones came he did not stop. The illness became "
                  "material rather than an interruption. Having a place of "
                  "your own means bad things also have somewhere to be put, "
                  "which is precisely the moment most people give the place "
                  "up.",
             "eg": "When your health goes, that reserved hour is the right "
                   "container for it. Do not cancel it first."},
        ],
        "q": [
            "Full retreat is flight. No retreat is being eaten.",
            "A decision written down outlives one that was only thought.",
            "Somewhere of your own is where bad news can be put.",
        ],
        "apply":
            "Where you are: the calendar is full, none of it is yours, and "
            "clearing all of it looks impossible.\n"
            "Ask first: can I fence off one place and one fixed stretch of "
            "time as mine and leave the rest alone? Have I written it down "
            "anywhere?\n"
            "Where it goes wrong: reading it as quit and go and live in the "
            "country — he was mayor twice after moving into the tower; and "
            "the room is not a hiding place, he worked in it for twenty "
            "years.",
    },
]
