# -*- coding: utf-8 -*-
"""Peter Drucker — English.

Both of these lines are already in the reader's vocabulary, which is the
problem: create a customer has become a slogan for being nice to customers,
and doing the right things has become a slogan for prioritising. The original
sentences are sharper than that, and they are in print, so this page quotes
them and then does the part the slogans drop — what each one obliges you to
stop doing on Monday.
"""

PARENT = {
    "name": "Peter Drucker",
    "slug": "drucker",
    "blurb": "Deep read",
    "items": [
        {"k": "create-a-customer", "n": "The purpose is to create a customer",
         "w": "Defining the business from the outside in", "ready": True,
         "line": "Profit is the result, never the purpose"},
        {"k": "right-things-first",
         "n": "Doing efficiently what should not be done",
         "w": "Effectiveness comes before efficiency", "ready": True,
         "line": "The wrong thing done beautifully is the most expensive "
                 "waste"},
    ],
}

CHAPTERS = [
    {
        "k": "create-a-customer",
        "n": "The purpose is to create a customer",
        "w": "Defining the business from the outside in",
        "src": "The Practice of Management, 1954",
        "dek": "Ask why a business exists and most people answer profit. Why "
               "he called that answer not merely wrong but harmful.",
        "story":
            "The sharpest passage in The Practice of Management: ==there is "
            "only one valid definition of business purpose, to create a "
            "customer==. Profit is not the purpose. It is the test of "
            "validity, the risk premium on the future, a result rather than a "
            "cause. Treating it as the purpose turns everyone inward, "
            "deciding from the statements. His questions run the other way, "
            "because what the customer buys is never a product but the "
            "satisfaction of a want. Hence the set every business has to "
            "answer again periodically. What is our business? Who is the "
            "customer? What does he buy?",
        "f": [
            {"n": "Profit is the thermometer, not the heart",
             "d": "Profit measures how efficiently you create value for a "
                  "customer, the way a temperature reports health. Pushing on "
                  "the thermometer makes nobody healthy. Cut research, "
                  "squeeze service, raise the price, and the reading improves "
                  "for a while at the cost of the machine producing it.",
             "eg": "A company that meets its profit target by trimming costs "
                   "four quarters running finds in the fifth that there is "
                   "nothing left to trim, and that half its customers left "
                   "during the year."},
            {"n": "What the customer buys is nearly always wrong first time",
             "d": "The Cadillac customer, he wrote, buys not transportation "
                  "but status. He used it to show where the first instinct "
                  "stops, which is at the product. Push one layer down to "
                  "what does he solve with this, and the boundary, the rivals "
                  "and the openings are all redrawn.",
             "eg": "A cafe thinks it sells coffee until it notices the "
                   "afternoon customer is buying a seat that is neither the "
                   "office nor home. The rival becomes co-working and the "
                   "opening becomes power sockets."},
            {"n": "Create a customer, with the weight on create",
             "d": "Markets are made by businessmen, he said, not by God or "
                  "nature. Until a want has been satisfied the customer often "
                  "does not know he has it. Listening is therefore the floor. "
                  "Identifying what he cannot yet say and turning it into "
                  "effective demand is the whole ambition here.",
             "eg": "No survey ever asked for overnight delivery. Once "
                   "somebody built it, it became the pass mark for the trade. "
                   "Questionnaires collect known wants."},
        ],
        "q": [
            "There is only one valid definition of business purpose: to "
            "create a customer.",
            "Profit is not the explanation of business decisions but the test "
            "of them.",
            "What is our business? Who is the customer? What does he buy?",
        ],
        "apply":
            "Where you are: the whole company is organised around a profit "
            "number.\n"
            "Ask first: who is our customer, what is he actually buying, and "
            "when were those two answers last updated?\n"
            "Where it goes wrong: using profit is only a result to excuse "
            "years of not making any. A thermometer reading that stays wrong "
            "for years means the heart really is in trouble.",
    },
    {
        "k": "right-things-first",
        "n": "Doing efficiently what should not be done",
        "w": "Effectiveness comes before efficiency",
        "src": "His 1963 Harvard Business Review article; The Effective "
               "Executive",
        "dek": "He pulled apart two words that get used interchangeably. Why "
               "a gain in efficiency can conceal an error of direction.",
        "story":
            "In the 1963 article he wrote the warning he is quoted for most: "
            "==there is surely nothing quite so useless as doing with great "
            "efficiency what should not be done at all==. Two words come "
            "apart. Efficiency is doing things right; effectiveness is doing "
            "the right things. One asks how, the other asks whether. With the "
            "direction wrong, efficiency is an amplifier, and speed only "
            "widens the gap. The Effective Executive is one long argument "
            "about choosing: concentrate on the few things that matter, and "
            "abandon, systematically, what yesterday's success left behind.",
        "f": [
            {"n": "Improving efficiency keeps the wrong thing alive",
             "d": "Something that should not be done is easy to cut while it "
                  "is slow and expensive, because everyone can see it. The "
                  "moment somebody optimises it into something fast and "
                  "cheap, it acquires a reason to survive: it runs so well, "
                  "why kill it. The optimisation becomes its armour.",
             "eg": "A weekly report nobody reads gets automated, and after "
                   "that nobody proposes killing it. Its cost has fallen "
                   "below the price of holding one meeting about it."},
            {"n": "Whether comes before how",
             "d": "Most review agendas open on the details of the proposal, "
                  "and should this exist at all gets skipped in silence, "
                  "because it was approved once. The repair is a question in "
                  "front of every routine: if we were starting today, would "
                  "we begin this? A no voids the rest of the agenda.",
             "eg": "He called it systematic abandonment. Walk the list of "
                   "activities once a year asking whether you would enter "
                   "this today. Most organisations never ask, and carry "
                   "yesterday on their backs."},
            {"n": "Busyness is the best disguise an effectiveness problem has",
             "d": "A person doing the wrong thing idly is found out quickly. "
                  "A person doing the wrong thing at high speed reads to "
                  "everybody, himself included, as valuable. So diagnose a "
                  "team by the overlap between what it produces and what the "
                  "customer needs, not by its efficiency numbers.",
             "eg": "A department at full capacity all year, over target every "
                   "quarter, finds at the year end that nothing it delivered "
                   "appears in any customer's reason for buying."},
        ],
        "q": [
            "Nothing is so useless as doing efficiently what should not be "
            "done.",
            "Efficiency is doing things right; effectiveness is doing the "
            "right things.",
            "If we were not in this already, would we go into it now?",
        ],
        "apply":
            "Where you are: you are optimising a process and it is going "
            "well.\n"
            "Ask first: if we were starting from zero today, would we do this "
            "at all? If not, what is this optimisation keeping alive?\n"
            "Where it goes wrong: using the effectiveness point to dismiss "
            "all efficiency work. Once the direction is right, efficiency is "
            "the entire game. And asking the question daily rather than "
            "yearly means nothing ever accumulates.",
    },
]
