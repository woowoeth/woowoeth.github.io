# -*- coding: utf-8 -*-
"""Emperor Wu of Han — English.

English readers know him, if at all, as the emperor who sent armies against the Xiongnu. This page
skips the campaigns and takes the thing he is rarely credited for: late in life, when asked to push
further west, he stopped, and said why. Two chapters: the edict of 89 BCE that refused the Luntai
garrison, and what he did with the effort once he had pulled it back.
"""

PARENT = {
    "name": "Emperor Wu of Han",
    "slug": "han-wudi",
    "blurb": "Deep read",
    "items": [
        {"k": "luntai-edict", "n": "The Edict of Luntai",
         "w": "The hardest part of stopping is turning over the old accounts first",
         "ready": True,
         "line": "Asked to garrison a place even farther west, he refused, and first counted the dead from the last campaign"},
        {"k": "after-the-retreat", "n": "Where the Effort Goes Next",
         "w": "Stopping is not resting: the effort you pull back needs somewhere to go",
         "ready": True,
         "line": "After the edict he made his chancellor Marquis Who Enriches the People and put Zhao Guo in charge of a new way of farming"},
    ],
}

CHAPTERS = [
    {
        "k": "luntai-edict", "n": "The Edict of Luntai",
        "w": "The hardest part of stopping is turning over the old accounts first",
        "src": "Ban Gu, Book of Han, 'Account of the Western Regions II'",
        "dek": "Someone urged him one step further, and he opened the old accounts instead. This asks what to say when it is time to stop.",
        "story":
            "In 89 BCE Sang Hongyang and others asked the emperor to plant military farms east of "
            "Luntai in the Western Regions and station troops there, pushing the frontier one more "
            "step west. Wu refused, and issued an edict. It began with the old bills: the extra levy "
            "already laid on the people, and the last march on Cheshi, where the army ran short of grain "
            "and dozens died on the road. ==Since taking the throne, he said, much of what he had done "
            "had been reckless, had made the empire miserable, and could not be undone.==",
        "f": [
            {"n": "Open last time's books, not next time's forecast",
             "d": "Sang Hongyang had a case: good pasture, land for grain, soldiers who could feed themselves. Wu did not argue the sums. He asked what the last expedition had actually cost, in hunger, deaths and extra tax. He looked at what had happened, not at what was projected.",
             "eg": "Before a third branch opens, look at what the second one really spent and how long it lost money, not at the founder's forecast."},
            {"n": "The word 'stop' should come from whoever signed the cheque",
             "d": "The hardest line in the edict is the emperor calling his own conduct reckless. The larger the earlier investment, the less anyone dares say stop, because stopping implies the past was wrong. It carries weight only from the person who ordered it.",
             "eg": "Three years into a project nobody dares cut it. The lead says in a meeting, 'I judged this wrong', and only then do others tell the truth."},
            {"n": "Stop the new push, keep the existing line",
             "d": "In the same edict he says the priorities now are to curb harshness, end unauthorised levies, encourage farming and mend the horse administration, and to keep up the defences, nothing more. What he pulled back was the next reach, not the garrisons already in place.",
             "eg": "Cancel the market you have not entered yet. Do not cut one person from serving the customers you already have."},
        ],
        "q": [
            "Count what the last push cost, then talk about the next.",
            "Whoever ordered it is best placed to call it off.",
            "Stop the new reach. Keep what is already held.",
        ],
        "apply":
            "Where you are: You have put a lot behind one direction, someone now asks for another round, and you suspect it is wrong but cannot say stop.\n"
            "Ask first: What did the last round actually cost and return? Am I looking at forecasts or at what happened?\n"
            "Where it goes wrong: Reading it as 'never expand'. He did not dismantle the frontier or say every earlier campaign was a mistake. He stopped the next step and kept what he held. Say stop and hold separately, or one will take the other down with it.",
    },
    {
        "k": "after-the-retreat", "n": "Where the Effort Goes Next",
        "w": "Stopping is not resting: the effort you pull back needs somewhere to go",
        "src": "Ban Gu, Book of Han, 'Treatise on Food and Money I'",
        "dek": "He stopped the war and then found the army, the labour and the grain somewhere else to go. This asks what to do after you pull back.",
        "story":
            "After the edict, Wu made his chancellor Tian Qianqiu Marquis Who Enriches the People, "
            "and the one line that mattered in the decree was that ==the business of the moment is to "
            "put effort into farming==. He appointed Zhao Guo as chief of grain procurement and set "
            "him to spread alternating-field farming: three furrows to a mu, crops planted in the furrows, "
            "ridge and furrow swapped the next year, so the land took turns resting. The people and "
            "grain that had been headed for the frontier had a new destination.",
        "f": [
            {"n": "Give the effort you pull back a named destination",
             "d": "Saying 'no more war' leaves soldiers, labourers and officials with energy and nowhere to put it, which easily turns into the next flurry. He wrote farming into the decree, named a man to run it and gave him a method.",
             "eg": "When you close a product line, say in the same message where its people are going and who they report to."},
            {"n": "A change of direction needs a concrete method",
             "d": "The record of alternating-field farming is specific: three furrows to a mu, ridge and furrow swapped each year. According to the Treatise, land worked this way regularly out-yielded the old kind, the best by double. A slogan is not a method.",
             "eg": "'Focus on existing customers' is not enough. Write down who calls which customer, and how often."},
            {"n": "A turn takes time, so do not read it too soon",
             "d": "When the decree went out nothing was growing yet. The road paid off only after some years, and meanwhile the frontier had no new victories to report. Pulling back means accepting a stretch with no visible score.",
             "eg": "Stop chasing new users to work on retention and the numbers look worse for two months. Agree beforehand which figures you will watch."},
        ],
        "q": [
            "On the day you stop, say where the people go.",
            "A turn needs someone in charge and a method, not a slogan.",
            "The first stretch after stopping looks bad on paper.",
        ],
        "apply":
            "Where you are: You have just decided to close one operation, and the people and resources it freed are idle. You worry that with nothing to do they will drift.\n"
            "Ask first: Which concrete job does this effort go to? Who runs it? What counts as moving forward in the first three months?\n"
            "Where it goes wrong: Treating it as 'stop, then do something else'. His turn had a person, a method and one clear sentence in the decree. Without those three, the effort you pulled back only becomes the next round of upheaval.",
    },
]
