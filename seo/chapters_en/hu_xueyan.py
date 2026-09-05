# -*- coding: utf-8 -*-
"""Hu Xueyan — English.

The name means nothing to an English reader, so the page has to earn its
place with two artefacts rather than a reputation: a wooden board he hung
facing away from his customers, and a corner in raw silk that took the
richest merchant in the Qing empire apart in two years. One shows where a
rule has to live to work; the other shows how a correct view still loses.
"""

PARENT = {
    "name": "Hu Xueyan",
    "slug": "hu-xueyan",
    "blurb": "Deep read",
    "items": [
        {"k": "no-cheating", "n": "The board that faces inward",
         "w": "Put the rule where the cheating is possible", "ready": True,
         "line": "It hangs where only his own staff walk past it"},
        {"k": "the-silk-corner", "n": "The silk corner",
         "w": "What it costs to bet everything once", "ready": True,
         "line": "He bet on the price and lost on the funding"},
    ],
}

CHAPTERS = [
    {
        "k": "no-cheating",
        "n": "The board that faces inward",
        "w": "Put the rule where the cheating is possible",
        "src": "The No Cheating board at Hu Qing Yu Tang, 1878",
        "dek": "Adulterating medicine is easy and almost never detected. What "
               "is worth studying is where he chose to hang the rule about "
               "it.",
        "story":
            "In 1878 he wrote two characters for his pharmacy, Hu Qing Yu "
            "Tang: No Cheating. Underneath ran a note. No trade can afford "
            "the word cheat, and medicine, which holds lives, least of all; "
            "he would not take a fat profit with an inferior drug, and he "
            "asked the managers to hold this as their own. ==The board was "
            "not hung at the front for customers. It faces inward, where only "
            "the staff and the managers pass it every day.== A second board, "
            "One True Price, faced the shop floor.",
        "f": [
            {"n": "Put the rule on the side where cheating is possible",
             "d": "A customer cannot tell good herbs from bad, so no external "
                  "check exists. Hanging the board inward concedes that the "
                  "only available constraint is internal, and that an "
                  "internal constraint needs a physical reminder people walk "
                  "past daily. A rule posted where outsiders read it is "
                  "mostly advertising.",
             "eg": "Promising customers you never use cheap inputs matters "
                   "less than the spec sheet taped above the benches where "
                   "the only people who could substitute actually stand."},
            {"n": "Where nothing can be verified, honesty is an asset choice",
             "d": "In a trade the buyer cannot audit, adulteration pays "
                  "immediately and invisibly. Giving up that informational "
                  "advantage converts a certain current profit into something "
                  "long-dated and unseeable. His bank failed and he was "
                  "ruined; the pharmacy is still trading.",
             "eg": "Holding the standard where the client could never check "
                   "always shows on the books as money wasted. It pays back "
                   "years later, as people not needing to check you."},
            {"n": "Two boards, two audiences",
             "d": "One True Price faces out; No Cheating faces in. He treated "
                  "them as separate jobs. Outward you owe a clear promise; "
                  "inward you owe an enforceable discipline. A promise "
                  "without the discipline eventually breaks, and a discipline "
                  "nobody announces builds no expectation at all.",
             "eg": "Telling customers the price is fixed needs a matching "
                   "internal rule that nobody may discount, ever. Without the "
                   "second, the first lasts about a quarter."},
        ],
        "q": [
            "No trade can afford the word cheat; medicine, which holds lives, "
            "least of all.",
            "I will not take a fat profit with an inferior drug.",
            "One true price, and no second price.",
        ],
        "apply":
            "Where you are: there is a step the customer could never audit, "
            "and the cost pressure is real.\n"
            "Ask first: where is this rule currently posted, and who reads it "
            "there?\n"
            "Where it goes wrong: turning the promise into marketing with no "
            "matching internal rule, or assuming that what cannot be detected "
            "does not exist.",
    },
    {
        "k": "the-silk-corner",
        "n": "The silk corner",
        "w": "What it costs to bet everything once",
        "src": "The raw silk campaign of 1882 to 1883",
        "dek": "The richest merchant in the empire lost everything inside two "
               "years. The interesting question is which step was the "
               "mistake.",
        "story":
            "From 1882 he used his bank and his silk business to hoard raw "
            "silk, meaning to control supply and force the foreign houses to "
            "his price. The first year worked; they had to pay. Then Europe "
            "turned. Silk prices fell, the Italian crop came in large, and "
            "the foreign buyers simply bought elsewhere. ==His money was "
            "locked in silk for a season, while the deposits funding it could "
            "be withdrawn in a day.== With Zuo Zongtang dead he had no "
            "protection at court, a rumour started, and the branches were run "
            "on at once.",
        "f": [
            {"n": "Cornering a good whose supply you do not own",
             "d": "A corner only works if you control the supply and the "
                  "buyer has nowhere else to go. Raw silk failed both tests, "
                  "because China was not the only source and Italy was having "
                  "a good year. Before squeezing anyone, establish whether "
                  "they have a second seller.",
             "eg": "Locking up capacity to lift a price requires knowing "
                   "whether the other side can find a second supplier within "
                   "three months. If they can, you have bought inventory."},
            {"n": "Long bets on short money",
             "d": "Silk needed a year or more to come back. Deposits could "
                  "leave in an afternoon. An asset that outlasts its funding "
                  "looks completely normal in calm weather and fails on the "
                  "first tremor. What finished him was not the wrong view; it "
                  "was the mismatch.",
             "eg": "Funding a three-year build with money that can be "
                   "recalled on notice means any ordinary wobble removes you, "
                   "even when the direction was right all along."},
            {"n": "A borrowed advantage expires with the lender",
             "d": "Cheap funding, government deposits and official "
                  "convenience all rested on one patron. That kind of "
                  "advantage looks like capability while it lasts and reveals "
                  "itself as a lease when it ends. Sorting your moat means "
                  "separating what you grew from what you rent.",
             "eg": "The exclusive channel you hold because of one executive "
                   "expires the day he leaves. Counting it as durable "
                   "advantage is keeping a false set of books."},
        ],
        "q": [
            "A corner needs the supply, not only the money.",
            "Across five thousand years of trade, the first man is Fan Li.",
            "Never wear arrogance; never be without a backbone.",
        ],
        "apply":
            "Where you are: you are convinced something will rise and you "
            "want to concentrate everything into it.\n"
            "Ask first: can the other side buy elsewhere, and what is the "
            "earliest my funding can be taken away?\n"
            "Where it goes wrong: counting a borrowed relationship as your "
            "own moat, or holding a long position on money that is short.",
    },
]
