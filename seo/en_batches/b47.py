# -*- coding: utf-8 -*-
"""Daily entry, day 27: Thucydides.

Picked by fan-out. 'Someone is being unreasonable' (遇上不讲理, 9), 'I don't
believe what my boss says' (上面说的话不能信, 9) and 'Anger just took over'
(情绪上头, 10) were among the emptiest. Under unreasonable people hang
Epictetus, Gandhi and Machiavelli: stay out of it, refuse to mirror it, or
face it as it is. Nobody is the person who records a power speech in full and
shows what it cost the speaker. Under 'cannot believe what is said above' hang
Han Feizi, Axelrod and Schelling, all on whether the promiser will keep his
word; nobody asks how to test a report when several accounts disagree. Under
anger hang the Stoics, Su Shi and Neff on calming down; nobody says what to do
after the thing is already decided and sent.

His standing: founder of critical history, source of political realism, the
History of the Peloponnesian War read for 2,400 years. The last entries were
Xiao He, King Wuling, the Duke of Zhou (Chinese), so pick_balance asked for a
foreign pick.

Three scenes, no overlap: the entry is the plague, the chapters are Melos,
Mytilene and the method of 1.22. Quoted lines are Richard Crawley's
translation, checked against the Gutenberg text. All three situations already
exist, so no SC_BOX.
"""

ENTRIES = [
    {
        "c": "Strategy and competition",
        "n": "Thucydides",
        "slug": "thucydides",
        "e": "Ancient Greece · c. 460–400 BC",
        "w": "History",
        "y": -431,
        "d": "An Athenian general who lived through the Peloponnesian War "
             "and wrote its history, regarded as the founder of critical "
             "history and a source of political realism. This page takes "
             "only three things from the book: how to read a situation when "
             "the other side counts only strength, how to take back a "
             "decision made in anger, and how to check when accounts do not "
             "agree. He left three methods. Find out what the other side "
             "counts and what you actually hold. Do not settle irreversible "
             "things in the heat. Do not take the first account as fact, "
             "and when they differ, ask why.",
        "story": "In the second year of the war a plague broke out in "
                 "Athens and killed thousands. Thucydides caught it and "
                 "survived. Writing about it later, he did not say where it "
                 "came from or why; he left that to others. He set down "
                 "what it was like: heat in the head, red eyes, then bleeding "
                 "in the throat and tongue, symptom after symptom in order. "
                 "He did it, he said, so that if it ever broke out again, "
                 "people would recognise it.",
        "f": [
            {"n": "He did not treat hope as capital",
             "d": "In the Melian Dialogue the Athenians tell the weaker side that hope comforts those with something to spare, and for the rest it means staking everything on what they cannot see. Count what you hold first.",
             "eg": "When someone says 'we will come and help', ask what exactly they have said."},
            {"n": "He let a decision be reopened the next day",
             "d": "In a rage the Athenians sentenced a city to death, regretted it by morning, and held the assembly again. A second ship caught the first. For anything that cannot be undone, leave a night.",
             "eg": "Before firing someone, finish the process; do not announce it in the group chat."},
            {"n": "He asked why the accounts differed",
             "d": "When eyewitnesses disagreed, he did not hurry to find who was lying. He asked whether it was memory or partiality, which tells you which part to discount.",
             "eg": "Two colleagues tell the same story in opposite ways: ask which side each was on, and how long ago it was."},
        ],
        "apply": "Pick one thing you are stuck on and write three lines: what "
                 "the other side counts and what I actually hold; whether "
                 "this decision can wait one night before it goes out; which "
                 "of my accounts is the first and which is a second, "
                 "independent source. His one judgement runs through all "
                 "three: see the facts clearly first, then decide whether to move.",
        "q": ["right, as the world goes, is only in question between equals in power",
              "I think the two things most opposed to good counsel are haste and passion",
              "I did not even trust my own impressions"],
        "l": ["Machiavelli", "Gandhi", "Sima Qian", "On War"],
        "contrast": [
            {"n": "Machiavelli",
             "why": "Both wrote about how the strong behave. Machiavelli "
                    "teaches a prince how to use force. Thucydides sets down "
                    "the Athenians' line, 'the strong do what they can', as "
                    "they said it, and sets down what came of it. One "
                    "teaches what to do, the other records what happened "
                    "after it was done"},
            {"n": "Sima Qian",
             "why": "Both were historians who wanted the facts straight. "
                    "Sima Qian travelled the country and questioned the "
                    "people involved. Thucydides checked each eyewitness "
                    "against the others, and asked why they differed. One "
                    "relied on going and asking, the other on checking and "
                    "asking why they do not match"},
        ],
    },
]

INTROS = {
    "thucydides": "An Athenian general who wrote the history of the Peloponnesian "
                  "War, and is thought of as the founder of critical history. He "
                  "set down the Athenian line that 'the strong do what they can' "
                  "just as they said it, and the Melians staking all on help that "
                  "never came. In another debate Athens sentenced a city to "
                  "death in a rage, repented by morning, and a second ship "
                  "overtook the first.",
}

SCENES = [
    ("Someone is being unreasonable", "Dealing with people", [
        ("He only counts strength. Is there any use in reasoning with him?",
         [("thucydides", "the-strong-do-what-they-can")]),
    ]),
    ("I don't believe what my boss says", "Dealing with people", [
        ("The accounts don't match. Which one do I believe?",
         [("thucydides", "first-source-that-came-to-hand")]),
    ]),
    ("Anger just took over", "Making a call", [
        ("I decided in anger. Can I take it back?",
         [("thucydides", "the-morrow-brought-repentance")]),
    ]),
]

ASKS = {
    "thucydides/the-strong-do-what-they-can":
        "He only counts strength. Is there any use in reasoning with him?",
    "thucydides/the-morrow-brought-repentance":
        "I decided in anger. Can I take it back?",
    "thucydides/first-source-that-came-to-hand":
        "The accounts don't match. Which one do I believe?",
}
