# -*- coding: utf-8 -*-
"""Florence Nightingale — English.

Everyone knows the Lady with the Lamp. This page takes three judgements
behind the legend: what she did first at Scutari, how she made officials
see where soldiers died, and what she did with her fame.

Quoted lines are condensed from Notes on Nursing (1859; checked against Project
Gutenberg #12439) and the preface to the third edition of Notes on
Hospitals (1863).
"""

PARENT = {
    "name": "Florence Nightingale",
    "slug": "nightingale",
    "blurb": "Deep read",
    "items": [
        {"k": "do-no-harm", "n": "First, Do the Sick No Harm",
         "w": "Caring for someone, first remove what is making them worse",
         "ready": True,
         "line": "At the war hospital her first work was laundry, kitchens, air and cleaning, not surgery"},
        {"k": "the-rose-diagram", "n": "Deaths Drawn as a Rose",
         "w": "For people who will not read tables, draw the data as a picture they grasp at a glance",
         "ready": True,
         "line": "With a statistician she showed most soldiers died of preventable disease, then drew it as a wheel"},
        {"k": "miss-smith", "n": "Travelling as Miss Smith",
         "w": "Once famous, do not let the fame do your work; turn it into something that lasts",
         "ready": True,
         "line": "A national heroine, she came home under a false name and spent decades indoors pushing reform"},
    ],
}

CHAPTERS = [
    {
        "k": "do-no-harm", "n": "First, Do the Sick No Harm",
        "w": "Caring for someone, first remove what is making them worse",
        "src": "Florence Nightingale, Notes on Nursing (1859); Notes on Hospitals (3rd ed., 1863)",
        "dek": "Someone at home is ill and you want to do something. Where do you start? What did Florence Nightingale do first at Scutari?",
        "story":
            "In the autumn of 1854, with Britain at war in the Crimea, "
            "Florence Nightingale took thirty-eight nurses to the British "
            "army hospital at Scutari in Turkey. Beds lined the corridors, "
            "the drains were blocked, the linen went unwashed, and far more "
            "soldiers died of dysentery and cholera than of wounds. Years "
            "later she wrote that it might seem strange to make it the very "
            "first requirement of a hospital ==that it should do the sick "
            "no harm.==",
        "f": [
            {"n": "Remove what makes them worse",
             "d": "At Scutari her first work was not surgery but laundry, cooking, airing and scrubbing. Dirty linen, bad food and foul air were each making patients worse; take them away first, and medicine has a chance.",
             "eg": "An elderly parent comes home from hospital. Before buying tonics, check whether the bedroom is airy and quiet at night."},
            {"n": "Quiet and certainty are treatment too",
             "d": "In Notes on Nursing she listed apprehension, waiting and fear of surprise among the things that harm the sick more than exertion does. Nursing is not only handing out medicine; keep a patient's mind from hanging in suspense.",
             "eg": "A relative is waiting for test results. Tell them when they arrive and who will collect them; it helps more than 'don't worry'."},
            {"n": "It comes to everyone",
             "d": "She wrote that almost every woman will at some time have charge of someone's health; in other words, every woman is a nurse. Care is not a skill for hospitals only. Families should know about air, quiet and observation.",
             "eg": "Your child has a fever. Note the times, temperatures and what they ate; it is the list the doctor needs."},
        ],
        "q": [
            "A hospital's very first requirement: that it should do the sick no harm.",
            "Unnecessary noise is the most cruel absence of care.",
        ],
        "apply":
            "Where you are: someone at home is ill, or you are caring for "
            "someone in a bad way, and you want to do something.\n"
            "Ask first: what around them is making them worse: dirt, noise, "
            "cold, waiting? Which can I remove first? Am I helping them, or "
            "calming myself?\n"
            "Where it goes wrong: taking 'do no harm' as 'do nothing'. At "
            "Scutari she worked from dawn to night, on exactly the dirty "
            "jobs nobody wanted.",
    },
    {
        "k": "the-rose-diagram", "n": "Deaths Drawn as a Rose",
        "w": "For people who will not read tables, draw the data as a picture they grasp at a glance",
        "src": "Florence Nightingale, Notes on Nursing (1859); her army mortality statistics with William Farr (1857-1858)",
        "dek": "You have solid data, and the people you must persuade will not read tables. How did Nightingale make officials see where soldiers died?",
        "story":
            "Back from the Crimea, Nightingale worked through the army's "
            "death figures with the statistician William Farr. Most "
            "soldiers in the war hospitals had died of preventable disease. "
            "To persuade officials and MPs who would not read tables, she "
            "drew each month's deaths as wedges in a wheel: ==the blue of "
            "disease dwarfed the red of wounds==. It became known as her "
            "rose diagram. In 1858 she became the first woman member of "
            "the Statistical Society.",
        "f": [
            {"n": "Count first, then speak",
             "d": "She did not accuse from impressions of the wards. With Farr she counted the death registers entry by entry: how many from wounds, how many from disease, which months worst. Once the numbers stood, the argument carried weight.",
             "eg": "You think your team works too much overtime. Pull three months of timesheets and count before you raise it."},
            {"n": "Draw it for people who will not read tables",
             "d": "She knew officials would never read a book of tables, so she drew twelve months as a wheel of wedges, each sized by deaths. The disease wedge was so large that anyone could see at a glance where the money had to go.",
             "eg": "Reporting to your boss, do not send a thirty-column sheet; draw one chart that says one thing."},
            {"n": "The chart is for change, not decoration",
             "d": "The diagrams went with reports to a royal commission and to MPs, and pushed reforms in barracks and military hospitals: ventilation, drainage, an army medical school. She wanted fewer deaths in the next war, not a pretty picture.",
             "eg": "After the churn analysis, do not stop at the report; pick the biggest slice and change one thing next week."},
        ],
        "q": [
            "The most important lesson: teach nurses what to observe, and how.",
            "Nursing ought to signify the proper use of fresh air, light, warmth, cleanliness, quiet.",
        ],
        "apply":
            "Where you are: you have solid data, and the people you must "
            "persuade have no patience for it, or do not want to look.\n"
            "Ask first: have I counted it properly myself? Can it be drawn "
            "as one picture understood at a glance? After seeing it, what "
            "one thing do I want them to do?\n"
            "Where it goes wrong: distorting the picture to make it striking. "
            "The rose diagram was powerful because every wedge matched the "
            "real deaths.",
    },
    {
        "k": "miss-smith", "n": "Travelling as Miss Smith",
        "w": "Once famous, do not let the fame do your work; turn it into something that lasts",
        "src": "Florence Nightingale's life, 1856-1860; Notes on Nursing (1859)",
        "dek": "Something made you famous and everyone is praising you. What did Nightingale do with her fame when she came home?",
        "story":
            "The Crimean War made Nightingale a national heroine, the Lady "
            "with the Lamp. Coming home in the summer of 1856, she "
            "travelled as 'Miss Smith', avoided every welcome, and walked "
            "home from the station. For decades after she was often ill and "
            "rarely went out, yet through letters, reports and commissions "
            "she pushed army health reform; ==the Nightingale Fund raised by "
            "the public== opened a nursing school at St Thomas' Hospital, "
            "London, in 1860.",
        "f": [
            {"n": "Skip the welcome, go back to the work",
             "d": "The whole country waited to greet her, and she came home under another name. Receptions, parades and speeches would have made her an image; what she wanted was for the unsolved problems of the war hospitals to be dealt with.",
             "eg": "The launch earned company-wide praise. Go to the party, and the next day put the leftover bugs on the plan."},
            {"n": "Push from outside the room",
             "d": "Back home she was often ill and seldom went out, and spent most of her life writing letters and reports and summoning people to talk. She did not rely on appearing in person, but on getting data and proposals into the hands of those who decide.",
             "eg": "Too unwell to go in often? Write each week's priorities on one page and send it to whoever decides."},
            {"n": "Turn fame into an institution",
             "d": "She did not keep the Nightingale Fund the public gave her. She used it to open a nursing school at St Thomas' Hospital to train nurses properly. People age and fall ill; a school keeps teaching, year after year.",
             "eg": "You are known in your field. Rather than touring with talks, train three people who can stand on their own."},
        ],
        "q": [
            "I use the word nursing for want of a better.",
            "Every woman is a nurse.",
        ],
        "apply":
            "Where you are: something made you famous, everyone praises you, "
            "and invitations keep coming.\n"
            "Ask first: what lasting thing can this fame buy: a rule, a "
            "school, a few people who can carry on? Which occasions only "
            "turn me into an image?\n"
            "Where it goes wrong: treating avoiding fame as a virtue in "
            "itself. She stayed out of sight, and spent the trust behind "
            "her name on reform.",
    },
]
