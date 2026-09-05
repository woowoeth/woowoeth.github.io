# -*- coding: utf-8 -*-
"""Chris Voss — English.

The English reader has probably met this book as a set of negotiation tricks
with names, and possibly tried the mirror once at work. The page has to put
the tricks back on top of the claim they come from: that nobody processes
terms while their own state is still unacknowledged, which makes the first
move a description of the other person rather than a number.
"""

PARENT = {
    "name": "Chris Voss",
    "slug": "chris-voss",
    "blurb": "Deep read",
    "items": [
        {"k": "labeling", "n": "Say their feeling out loud",
         "w": "Name it before you negotiate it", "ready": True,
         "line": "Named accurately, a person finds it hard to keep you as the enemy"},
        {"k": "thats-right", "n": "You want that's right, not yes",
         "w": "Two kinds of agreement, nothing alike", "ready": True,
         "line": "Fine, fine, fine is somebody leaving. That's right is somebody starting"},
    ],
}

CHAPTERS = [
    {
        "k": "labeling",
        "n": "Say their feeling out loud",
        "w": "Name it before you negotiate it",
        "src": "Never Split the Difference, on labelling",
        "dek": "The other side has gone quiet and will not take a call. What "
               "Voss says to say first, and why it is not a concession.",
        "story":
            "Voss spent hours outside a door in a Harlem apartment building "
            "where armed fugitives were holed up. They would not pick up the "
            "phone and they were asking for nothing. He made no offer. In a "
            "deliberately slow, low voice he said through the door: ==It "
            "looks like you don't want to come out. It seems like you worry "
            "that if you open the door, we'll come in with guns blazing.== A "
            "long silence, then a voice. He calls the move labelling: not "
            "judging the feeling, only naming it accurately.",
        "f": [
            {"n": "A label is an observation, not a verdict",
             "d": "It seems like the price is a problem, and I think you are "
                  "just balking at the cost, look similar and land nothing "
                  "alike. The first can be denied, which means it can be "
                  "corrected. The second files a finding, and the person on "
                  "the other end can only defend.",
             "eg": "When a client goes silent, it sounds like something here "
                   "is worrying you gives them a specific opening. How do you "
                   "feel about it gives them none."},
            {"n": "Feelings first, terms second",
             "d": "The working assumption is that nobody takes in terms while "
                  "their state is still unacknowledged. So the opening move "
                  "is not a number, it is making the other person feel you "
                  "know what is in their head. Skip it and every later "
                  "concession buys nothing.",
             "eg": "Talking terms to someone who is still angry is talking to "
                   "a shut door. Name where they are and the door can open."},
            {"n": "A wrong label still works",
             "d": "Most people avoid labelling because they might guess wrong. "
                  "Voss argues the reverse: a wrong label gets corrected, and "
                  "the correction is the information you came for. The value "
                  "is not in guessing right, it is in ending the silence.",
             "eg": "Say it sounds like the timeline worries you and you may "
                   "hear that the timeline is fine and the acceptance "
                   "criteria are not. Now you have the real problem."},
        ],
        "q": [
            "It looks like you don't want to come out.",
            "Labeling is a way of validating someone's emotion by "
            "acknowledging it.",
            "Get it wrong and they correct you. That is information too.",
        ],
        "apply":
            "Where you are: someone has gone quiet, is dodging you, or is "
            "plainly upset and not saying so.\n"
            "Ask first: what is the loudest sentence in their head right now, "
            "and can you say it back starting with it seems like?\n"
            "Where it goes wrong: repeating labels as a formula until it "
            "becomes performed empathy, or naming the feeling and rushing "
            "straight into terms before it has settled.",
    },
    {
        "k": "thats-right",
        "n": "You want that's right, not yes",
        "w": "Two kinds of agreement, nothing alike",
        "src": "Never Split the Difference, on that's right",
        "dek": "They nodded and nothing moved afterwards. This is about "
               "telling which of the two agreements you actually walked out "
               "with.",
        "story":
            "Voss calls yes the cheapest word in the language: people say it "
            "to be polite, to be left alone, to end a conversation. What he "
            "wants is two other words. ==That's right== means the other side "
            "believes you have understood them completely, and the route "
            "there is to summarise their position back until they say it. He "
            "pairs this with a counter-intuitive move, going after no. Ask "
            "whether they have given up on the project and they start "
            "explaining why they have not, because refusing feels safe.",
        "f": [
            {"n": "Cheap agreement gets reversed at execution",
             "d": "Nodding in the room and doing nothing afterwards means the "
                  "yes was social lubricant. The test is simple: did they "
                  "restate the plan in their own words? An agreement nobody "
                  "can restate is not an agreement, it is the end of an "
                  "uncomfortable meeting.",
             "eg": "When someone says fine, fine, no problem, ask what the "
                   "first step looks like. No answer means they were closing "
                   "the conversation."},
            {"n": "Summarise until they say it back",
             "d": "The method is to lay out their position, their worries and "
                  "what they want, in full, until they confirm it. Those two "
                  "words mark the moment they feel understood, and people "
                  "only weigh your proposal after that. Everything argued "
                  "before it is wasted.",
             "eg": "Before offering someone a change of role, list their "
                   "concerns one at a time. Wait for that's right, then talk "
                   "about the arrangement."},
            {"n": "No is safer than yes",
             "d": "Chasing a yes puts the other side on guard, because every "
                  "yes moves them nearer a commitment. Letting them say no "
                  "relaxes them, and relaxed people tell the truth. So build "
                  "the question in a form that can be refused.",
             "eg": "Swap can you agree to this for is this completely off the "
                   "table. To deny it, they begin telling you which parts are "
                   "not."},
        ],
        "q": [
            "That's right is better than yes.",
            "Negotiation is not an act of battle; it's a process of "
            "discovery.",
            "No is the start of the negotiation, not the end of it.",
        ],
        "apply":
            "Where you are: they have agreed, and you cannot tell whether "
            "that was agreement or an exit.\n"
            "Ask first: have they put it back in their own words, and did you "
            "actually hear that's right?\n"
            "Where it goes wrong: summarising on and on to manufacture the "
            "phrase, which turns into a script; or using the no question as a "
            "goad rather than an opening.",
    },
]
