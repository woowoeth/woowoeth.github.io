# -*- coding: utf-8 -*-
"""Extraordinary Popular Delusions — English.

English readers usually know the book by its title and by the tulip, and often know too that historians
have since cut the tulip story down to size. This page does not lean on it as history. It reads two
passages for how crowds think: the moment the buyers stopped wanting the thing they bought, and the line
in the preface about going mad in herds and recovering one by one. Quotations follow the 1852 London
edition (Project Gutenberg #24518) word for word.
"""

PARENT = {
    "name": "Extraordinary Popular Delusions",
    "slug": "popular-delusions",
    "blurb": "Deep read",
    "items": [
        {"k": "bought-to-sell", "n": "Bought to sell, not to plant",
         "w": "Who is buying, and what for", "ready": True,
         "line": "Rich people stopped buying tulips for their gardens and bought them to sell on, and the price never recovered"},
        {"k": "one-by-one", "n": "One by one",
         "w": "Nobody announces the end", "ready": True,
         "line": "A company that would not say what it did took a thousand deposits in five hours, and its founder left that night"},
    ],
}

CHAPTERS = [
    {
        "k": "bought-to-sell", "n": "Bought to sell, not to plant",
        "w": "Who is buying, and what for",
        "src": "Charles Mackay, Extraordinary Popular Delusions and the Madness of Crowds, 'The Tulipomania', from 'the more prudent began to see' to the defaults and the cancelled contracts",
        "dek": "The buyers no longer wanted the flowers. When everyone is scrambling for something, what is its price actually resting on?",
        "story":
            "Mackay describes a Holland where nobles, farmers, sailors, maid-servants and even chimney-sweeps dabbled "
            "in tulips, and small towns closed their deals in taverns, over tables set with vases of flowers in full "
            "bloom. Then, he writes, the more prudent began to see that it could not last. ==Rich people no longer "
            "bought tulips for their gardens, only to sell them on at double the price.== Somebody was bound to lose "
            "badly in the end. As that thought spread, prices fell and never rose again.",
        "f": [
            {"n": "The change was in the buyers",
             "d": "The turn Mackay records is not in the price but in who was buying. Early buyers wanted tulips for their gardens; later ones wanted only to sell to someone else. Once nobody wants the thing itself, the next buyer is all that holds the price up.",
             "eg": "A flat nobody plans to live in, stock nobody plans to use: count the people lined up to take it off you."},
            {"n": "A contract price counts on delivery day",
             "d": "Mackay records one deal. A agreed to buy ten Semper Augustus bulbs from B at four thousand florins each, six weeks later. B had the flowers ready on the day, but the price had fallen to three or four hundred, and A would neither pay the difference nor take the tulips.",
             "eg": "A paper gain is yours only on the day someone actually hands over the money."},
            {"n": "Everyone assumed it would last",
             "d": "Everyone, Mackay says, imagined the passion for tulips would last for ever, and that the rich of every country would send to Holland and pay whatever was asked. Everyone knew someone would lose in the end. Nobody counted themselves in.",
             "eg": "Ask yourself: if I turn out to be the last buyer, would I still buy?"},
        ],
        "q": [
            "When the buyer doesn't want it, the price hangs on the next one.",
            "Someone loses in the end; nobody counts themselves in.",
            "A contract price counts on delivery day.",
        ],
        "apply":
            "Where you are: everyone around you is buying the same thing, the price has multiplied in months, and you hold a little and wonder whether to add.\n"
            "Ask first: how many of the buyers mean to keep it and use it? If nobody took it off my hands, what would it be worth?\n"
            "Where it goes wrong: reading it as 'anything that rises fast is a bubble, so stay out'. The tulips were real flowers and the gardeners were real. What changed was the buyer, from someone who wanted a flower to someone who wanted the next buyer.",
    },
    {
        "k": "one-by-one", "n": "One by one",
        "w": "Nobody announces the end",
        "src": "Charles Mackay, Extraordinary Popular Delusions and the Madness of Crowds, Preface; and 'The South-Sea Bubble', the company for 'an undertaking of great advantage'",
        "dek": "There is no signal to wake up. When everyone is pushing in, what lets you be the one who stops and asks?",
        "story":
            "In 1720, the year of the South Sea Bubble, new companies were floated in London almost daily. The most "
            "absurd, Mackay says, was 'A company for carrying on an undertaking of great advantage, but nobody to know "
            "what it is'. The prospectus asked a deposit of two pounds a share and promised a hundred a year. At nine "
            "the next morning its founder opened an office in Cornhill and crowds besieged his door. ==By three o'clock "
            "a thousand shares were paid for.== He left for the Continent that evening and was never heard of again.",
        "f": [
            {"n": "The queue was all they knew",
             "d": "The company would not say what it did. All anyone in the queue could see was that plenty of people were ahead of them. Mackay's preface has the line for it: 'Men, it has been well said, think in herds; it will be seen that they go mad in herds'.",
             "eg": "If you can't say how a venture makes money, only who else has invested, you are looking at the queue, not the venture."},
            {"n": "Nobody wakes up together",
             "d": "The sentence goes on: 'while they only recover their senses slowly, and one by one.' Going mad has leaders and noise. Coming round has no signal, and nobody announces that it is over. By the time everyone wakes together, it has usually crashed.",
             "eg": "Don't wait for someone in the group chat to say it's time to get out. By then the exit is crowded."},
            {"n": "Ask what it is",
             "d": "The company put the answer in its name: nobody to know what it is. Anyone in that queue who asked what the business was would have got no answer, and for five hours nobody asked. Asking first, in a crowd, feels like spoiling things. That is why people wake one at a time.",
             "eg": "Before you pay in, write three sentences on what it is and how it earns. If you can't, don't pay yet."},
        ],
        "q": [
            "The queue told them only that others were queuing.",
            "Madness has a crowd behind it. Sanity comes back alone.",
            "Ask what it is before you ask who else is in.",
        ],
        "apply":
            "Where you are: suddenly everyone is talking about something and buying it. You can't quite say what it is, only that people you know are in.\n"
            "Ask first: leaving aside that other people bought it, can I say in three sentences what it is and how it makes money?\n"
            "Where it goes wrong: reading it as 'the crowd is always wrong, so do the opposite'. Mackay doesn't say crowds are always wrong; he says don't expect the crowd to come round for you. Doing the opposite is still steering by the crowd. The work is asking the question yourself.",
    },
]
