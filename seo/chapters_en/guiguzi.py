# -*- coding: utf-8 -*-
"""Guiguzi — English.

Almost no English reader has met this book, and the first thing it looks like
is a manipulation manual: the one classical Chinese text that is a systematic
handbook on moving a single named person, banned and denounced for centuries
on exactly that charge. What the page has to show is the other half — that its
opening move is not a trick but a decision made before you speak, and that the
whole method is built on calibrating yourself before you read anyone else.
"""

PARENT = {
    "name": "Guiguzi",
    "slug": "guiguzi",
    "blurb": "Deep read",
    "items": [
        {"k": "open-and-close", "n": "Open and close",
         "w": "Decide which one this is before you speak", "ready": True,
         "line": "Settle how much of you he will see before you settle the words"},
        {"k": "listen-in-reverse", "n": "Listening in reverse",
         "w": "To make him talk, stop talking", "ready": True,
         "line": "Ask, then add nothing. The silence does the work"},
        {"k": "sound-out", "n": "Sounding out what he wants",
         "w": "Measure at the peaks, not in the middle", "ready": True,
         "line": "Nobody edits themselves at the top of joy or the bottom of fear"},
    ],
}

CHAPTERS = [
    {
        "k": "open-and-close",
        "n": "Open and close",
        "w": "Decide which one this is before you speak",
        "src": "Guiguzi, Opening and Closing",
        "dek": "The most important decision in a conversation gets made before "
               "it starts. This asks which of the two decisions this one is.",
        "story":
            "The first chapter puts two words above everything else: "
            "==opening and closing are the way of heaven and earth.== To open "
            "is to let out; to close is to draw back. The principle underneath "
            "is plain — the mouth is the door of the heart, and when the door "
            "opens what is inside goes out, when it shuts the intent stays in. "
            "So before an exchange you settle one thing: how much of me does "
            "this person see, and how much stays. Neither is better. Only the "
            "wrong one for the occasion is.",
        "f": [
            {"n": "Settle open or closed before you settle words",
             "d": "Most people prepare content — what am I going to say. His "
                  "order puts a layer in front of that. Is this one an opening "
                  "or a closing? Get that wrong and the more elegantly you "
                  "speak the more damage you do.",
             "eg": "An investor asks what the biggest risk is. Opened, you take "
                   "it apart and give your answer to it. Closed, you reply "
                   "briefly without evading."},
            {"n": "You open so that he opens",
             "d": "Opening is not only expression, it is extraction. Show part "
                  "of your own footing and he has a reason to show his. So it "
                  "goes in order: open something small and survivable, watch "
                  "whether he follows, and only then decide how much further "
                  "to go.",
             "eg": "Name one real reservation of your own and the other side "
                   "usually names theirs. Ask what their reservations are, "
                   "cold, and you get politeness."},
            {"n": "Closing is chosen silence, not absence",
             "d": "Closing is an active withdrawal. You may close so that he "
                  "has to come and take it, or close in order to end the "
                  "thing. Without that distinction, closing decays into "
                  "awkwardness, and awkwardness reads as something to prod.",
             "eg": "Naming your price and adding nothing is closing to draw "
                   "him in. Going vague when he presses for detail looks "
                   "similar and means the opposite."},
        ],
        "q": [
            "Opening and closing are the way of heaven and earth.",
            "The mouth is the door of the heart.",
            "To open is to speak; to close is to keep silent.",
        ],
        "apply":
            "Where you are: an important conversation, and you are working on "
            "what to say in it.\n"
            "Ask first: how much do I want him to see this time, and what does "
            "not have to be given at this stage?\n"
            "Where it goes wrong: treating open and closed as a personality "
            "trait rather than a choice; or, when it is time to close, going "
            "vague instead of simply not saying it.",
    },
    {
        "k": "listen-in-reverse",
        "n": "Listening in reverse",
        "w": "To make him talk, stop talking",
        "src": "Guiguzi, Reacting",
        "dek": "How do you get a person who does not want to talk to talk? The "
               "answer is four reversals, and one precondition under them.",
        "story":
            "The Reacting chapter runs a set of paired instructions: to hear "
            "him speak, be silent; to have him open out, draw in; to stand "
            "high, stand low; ==to take, first give.== Behind the pairs is a "
            "harder demand. Knowing begins with yourself, and you know "
            "yourself before you know others — because every judgement you "
            "make about another person has to pass through your own "
            "instrument, and an instrument nobody has calibrated adds error to "
            "everything it measures.",
        "f": [
            {"n": "Silence is the strongest question",
             "d": "People find a silence uncomfortable and move to fill it. So "
                  "ask, and then add nothing: no softening, no restating, no "
                  "second question. It routinely returns more than three "
                  "further questions would have. That is what the first "
                  "reversal means.",
             "eg": "Say the price and stop. He often supplies there may be "
                   "some room on that himself. Whoever hurries on never hears "
                   "the sentence."},
            {"n": "Give first, or there is nothing to take",
             "d": "To take, first give is a sequence rather than a posture. "
                  "Information, concessions and goodwill all obey it: until "
                  "something has been put down, the other side has no reason "
                  "to start an exchange. What you put down should be real and "
                  "bounded.",
             "eg": "Want to know their timeline? Say yours. Most people match "
                   "it, and it is information you cannot get by asking for "
                   "it."},
            {"n": "Calibrate your own instrument first",
             "d": "Know yourself and then you know others is the precondition "
                  "for everything else here. Your reading of a person is mixed "
                  "with your own taste, the mood you are in, and what you "
                  "already think about people like him. Uncalibrated, more "
                  "information only loads a crooked scale.",
             "eg": "If slow talkers always strike you as unreliable, that is "
                   "not skill at reading people, it is a fixed offset. Knowing "
                   "it is there is what lets you subtract it."},
        ],
        "q": [
            "To hear him speak, be silent. To take, first give.",
            "Knowing begins with yourself; know yourself, then you know "
            "others.",
            "Ask, and then add nothing. The silence does the work.",
        ],
        "apply":
            "Where you are: you need the real position out of someone who is "
            "not saying much.\n"
            "Ask first: what am I putting down first, and can I hold my tongue "
            "after the question?\n"
            "Where it goes wrong: replacing the pause with a run of follow-up "
            "questions; or mistaking your own preferences for experience in "
            "reading people.",
    },
    {
        "k": "sound-out",
        "n": "Sounding out what he wants",
        "w": "Measure at the peaks, not in the middle",
        "src": "Guiguzi, Weighing and Sounding",
        "dek": "What a person says day to day and what he actually wants are "
               "rarely the same. This asks when the reading comes out true.",
        "story":
            "The Weighing chapter is almost coldly specific about timing. Go "
            "to him at the height of joy and press on what he wants, and "
            "having wanted it he cannot hide it; ==go to him at the height of "
            "fear and press on what he dreads, and having dreaded it he cannot "
            "hide it.== The Sounding chapter supplies the matching technique: "
            "rub gently along the line of what he wants, test and probe, and "
            "the inside answers. Not an interrogation. A light touch, and then "
            "watching.",
        "f": [
            {"n": "What people say at rest is edited",
             "d": "In a level state a person says what he believes he ought to "
                  "say. To reach the real preference you have to watch when "
                  "there is no attention left over for editing: very pleased, "
                  "very frightened, very tired. Not manipulation. Choosing the "
                  "observation window.",
             "eg": "What someone says offhand about the next step at the "
                   "celebration dinner beats anything in the formal meeting. "
                   "So does what he said the night it broke."},
            {"n": "Touch lightly, then watch the reaction",
             "d": "Sounding means to rub, not to press. Put out a small "
                  "hypothesis that can be denied at no cost, then watch the "
                  "direction and the speed of what comes back. The reaction is "
                  "the answer; the content of the reply matters much less.",
             "eg": "If we moved this two weeks later, would that be hard? "
                   "Whether he starts calculating or first asks why tells you "
                   "two completely different things."},
            {"n": "Use it to understand, not to work someone",
             "d": "The method plainly invites manipulation, and he says "
                  "himself that the sage works in the dark. The larger value "
                  "is in reversing it: knowing when other people are "
                  "unguarded tells you when you are, and big decisions do not "
                  "belong at either peak.",
             "eg": "Long contracts signed the week the funding landed have a "
                   "high rate of regret. The useful response is a cooling-off "
                   "rule you apply to yourself."},
        ],
        "q": [
            "Approach him at the height of joy and his wants show.",
            "Rub gently at what he wants, and the inside answers.",
            "The sage works in the dark; the fool works in the light.",
        ],
        "apply":
            "Where you are: trying to work out what the other side actually "
            "cares about.\n"
            "Ask first: the information I am holding — what state was he in "
            "when he gave it to me?\n"
            "Where it goes wrong: pointing it only outward and never at "
            "yourself; or turning the light touch into an interrogation, which "
            "spends the relationship in one go.",
    },
]
