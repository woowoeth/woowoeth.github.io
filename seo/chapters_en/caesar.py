# -*- coding: utf-8 -*-
"""Julius Caesar — English.

The English reader already owns the two lines, the die is cast and I came, I
saw, I conquered, and owns them as bravado. Both pages here work against that
reading. The crossing is interesting because of the long pause before it and
the arithmetic inside the pause, and the clemency is interesting because he
wrote down, in a letter that survives, exactly why he was doing it.

Quotations follow Suetonius, Plutarch, and Caesar's own letter as preserved by
Cicero.
"""

PARENT = {
    "name": "Julius Caesar",
    "slug": "caesar",
    "blurb": "Deep read",
    "items": [
        {"k": "the-rubicon", "n": "The die is cast",
         "w": "The step that has no way back", "ready": True,
         "line": "He stopped at the bank and finished the sums before crossing"},
        {"k": "clementia", "n": "Mercy as a weapon",
         "w": "A new way of winning", "ready": True,
         "line": "The more men he pardoned, the harder they were to recruit"},
    ],
}

CHAPTERS = [
    {
        "k": "the-rubicon",
        "n": "The die is cast",
        "w": "The step that has no way back",
        "src": "Suetonius, The Deified Julius 31-32; Plutarch, Life of Caesar",
        "dek": "Taking an army across that small river meant civil war. This "
               "one is about what he was calculating while he stood there.",
        "story":
            "January 49 BC. The senate had ordered Caesar to disband his army "
            "and return to Rome to stand trial. The Rubicon was the legal "
            "boundary between his province and Italy, and to cross it under "
            "arms was treason. Suetonius records that he halted at the bank "
            "and hesitated a long while, telling those with him that they "
            "could still turn back, but that once over the little bridge "
            "everything would have to be settled by arms. Then he said ==the "
            "die is cast== and crossed. The order matters: the long pause and "
            "the arithmetic came before the famous sentence.",
        "f": [
            {"n": "An irreversible decision has earned a deliberate pause",
             "d": "Reversible decisions should be fast, since a mistake can "
                  "be walked back. Irreversible ones should be slow, because "
                  "they delete the option of walking back. The hesitation at "
                  "the bank was not weakness, it was correct pricing. Most "
                  "people do it the other way round.",
             "eg": "Switching a tool can be undone in a fortnight, so do not "
                   "hold three meetings about it. An exclusive contract, a "
                   "public side taken, a relationship burned: those are worth "
                   "a night at the bank."},
            {"n": "Half the war was already won before the crossing",
             "d": "This was not a gambler's throw. Ten years in Gaul had made "
                  "his legions the best in Rome, Pompey's strength was "
                  "scattered in Spain, and the city had no troops to hold it. "
                  "He took Italy almost without blood. The romance of the "
                  "line hides the arithmetic under it.",
             "eg": "Before going all in publicly, confirm your own core "
                   "capability, the gap in theirs, and the position you can "
                   "hold in the first month. The declaration is for outside; "
                   "the sums are for you."},
            {"n": "Once thrown, stop looking back at the bank",
             "d": "After the crossing he was famous for speed, holding all "
                  "Italy within sixty days. The second half of an "
                  "irreversible decision has its own discipline: spend "
                  "nothing more on what if I had not crossed. The hesitation "
                  "budget was used up at the river.",
             "eg": "Deciding to change direction and then reopening whether "
                   "to change direction every week is fighting two wars at "
                   "once. Review it in December; until then, only the next "
                   "step."},
        ],
        "q": [
            "We can still turn back; beyond that bridge, arms decide "
            "everything.",
            "The die is cast.",
            "I would rather be first in a village than second in Rome.",
        ],
        "apply":
            "Where you are: one step in front of you, and past it there is no "
            "way back.\n"
            "Ask first: is this really irreversible, and if it is, have you "
            "given the pause enough time and finished the arithmetic?\n"
            "Where it goes wrong: treating small decisions as Rubicons and "
            "living in permanent high drama; or crossing and leaving half "
            "your attention on the other bank.",
    },
    {
        "k": "clementia",
        "n": "Mercy as a weapon",
        "w": "A new way of winning",
        "src": "Cicero, Letters to Atticus 9.7C, quoting Caesar's own letter",
        "dek": "In the civil war he killed no prisoners and confiscated no "
               "property. He set out his motive plainly in a letter.",
        "story":
            "Early in the civil war Caesar took Corfinium, capturing Pompeian "
            "troops and senators, and then did what nobody in a Roman civil "
            "war had done: released them all and returned their property. The "
            "letter he wrote to his staff survives because Cicero kept it, "
            "and the motive is not hidden. Let us try whether by this means "
            "we can win all men back and make the victory lasting. Sulla won "
            "by cruelty and could not hold it. ==Let mercy and generosity be "
            "our new way of winning.== The effect was immediate: mobilising "
            "against him got much harder.",
        "f": [
            {"n": "Mercy changes what it costs them to mobilise",
             "d": "How hard the other side fights depends on what they expect "
                  "defeat to mean. When defeat means death, everyone fights "
                  "to the end. When defeat means going home, resistance stops "
                  "being worth buying. This was not a moral choice; it "
                  "attacked their recruiting directly.",
             "eg": "Treat the team of the company you just bought well and "
                   "the next negotiation gets easier immediately, because "
                   "every future target is watching how you handled the last "
                   "one."},
            {"n": "He wrote the method down",
             "d": "The phrase new way of winning shows this was policy and "
                  "not temperament. He deliberately set it against Sulla's "
                  "terror and made mercy his brand. One act of clemency is a "
                  "gesture; clemency that becomes a reliable expectation is a "
                  "weapon, because only expectation changes behaviour.",
             "eg": "Letting one departing employee off quietly is forgotten "
                   "by everyone. Writing the rule down and honouring it for "
                   "three years is why almost nobody breaks your non-compete."},
            {"n": "The bill for this method arrives later",
             "d": "Brutus and Cassius, among the men who killed him, were "
                  "Pompeians he had pardoned and promoted. Mercy wins wars, "
                  "but the pardoned often remember the humiliation rather "
                  "than the kindness: they owe a life, and the debt makes the "
                  "creditor hard to look at.",
             "eg": "Keep a beaten rival and give them real responsibility, and "
                   "understand that they come in every day facing the "
                   "evidence that they lost to you. That post needs "
                   "designing, not gratitude."},
        ],
        "q": [
            "Let mercy and generosity be our new way of winning.",
            "Let us see whether this way we can win all men back.",
            "Sulla won by cruelty and could not keep what he won.",
        ],
        "apply":
            "Where you are: you have won, and how the losing side is handled "
            "is in your hands.\n"
            "Ask first: will this handling make the next opponent fight "
            "harder, or make them talk?\n"
            "Where it goes wrong: making mercy a one-off gesture that never "
            "becomes an expectation; assuming the pardoned are now on your "
            "side.",
    },
]
