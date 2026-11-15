# -*- coding: utf-8 -*-
"""Henry Ford — English.

English readers know Ford as the assembly line and the black Model T, and often as a figure whose
politics they would rather not discuss. This page takes only the two business arguments he made in his
own book: the price is set first and the costs are forced to follow, and the five-dollar day was a way
of cutting costs. Every figure and the two quotations come from My Life and Work (1922, written with
Samuel Crowther), Project Gutenberg text. His political views and publications are left out.
"""

PARENT = {
    "name": "Henry Ford",
    "slug": "henry-ford",
    "blurb": "Deep read",
    "items": [
        {"k": "price-first", "n": "Set the price, then reach it",
         "w": "The price comes down first and the costs are made to follow",
         "ready": True,
         "line": "In eight seasons the Model T went from $950 to $360 and output from 18,000 cars to 785,000 - he said the price cut always came first"},
        {"k": "five-dollar-day", "n": "The five-dollar day",
         "w": "He doubled many workers' pay to save money",
         "ready": True,
         "line": "To keep 14,000 people the plant had been hiring 53,000 a year - after the raise it hired 6,508 the next year"},
    ],
}

CHAPTERS = [
    {
        "k": "price-first",
        "n": "Set the price, then reach it",
        "w": "The price comes down first and the costs are made to follow",
        "src": "Henry Ford with Samuel Crowther, My Life and Work (1922), chapters IV, V and X",
        "dek": "He cut the price first. When the price your costs produce will not sell, do you change the price or the way you work?",
        "story":
            "In his 1922 memoir Ford printed a table. The Model T touring car sold for $950 in the 1909-10 season, "
            "when the company built 18,664 cars. The price fell almost every year after that. In 1916-17 it was $360, "
            "and the company built 785,432. The order was deliberate, he wrote. ==First cut the price to where more "
            "people will buy, then work out how to make the car at that price==. The costs were not the starting point.",
        "f": [
            {"n": "Cost-plus was not enough for him",
             "d": "The usual method is to work out the cost and then set the price. He called that scientific only in a narrow sense: what use is knowing the cost if it says you cannot make the thing at a price people will pay?",
             "eg": "Find out what customers will pay for the job first, then ask what your process must become to get there."},
            {"n": "The line the price forced",
             "d": "From 1913 the Highland Park plant moved parts and chassis along a line past the workers. Assembling a chassis in one place had averaged 12 hours 28 minutes. It fell to 5 hours 50, and in early 1914 to 1 hour 33.",
             "eg": "Set a price you cannot reach today, and the team finally takes apart the step nobody has touched."},
            {"n": "The price cut comes before growth",
             "d": "He put his policy in three parts: reduce the price, extend the operations, improve the article, and he pointed out that the price came first. He treated no cost as fixed, so every step had to justify itself again.",
             "eg": "Before quoting thirty per cent under a rival, list the three steps you will have to remove."},
        ],
        "q": [
            "The new price forces the costs down.",
            "We have never considered any costs as fixed.",
            "Set the price first, then go and reach it.",
        ],
        "apply":
            "Where you are: you price at cost plus a margin, customers say it is too expensive, and you feel you cannot go lower.\n"
            "Ask first: if the price were set where most buyers would pay, which steps would I have to change to reach it?\n"
            "Where it goes wrong: reading it as 'cut the price and grab volume'. He worked out where a lower price would sell more and how far volume would push costs down, and he rebuilt the whole process to get there. Without a new process and without the volume, a price cut just gives the margin away.",
    },
    {
        "k": "five-dollar-day",
        "n": "The five-dollar day",
        "w": "He doubled many workers' pay to save money",
        "src": "Henry Ford with Samuel Crowther, My Life and Work (1922), chapter VIII",
        "dek": "He raised pay to cut costs. When wages are already your biggest bill, should you add to them?",
        "story":
            "In January 1914 Ford announced a profit-sharing plan: qualifying workers would earn at least five dollars "
            "a day, and the working day fell from nine hours to eight. About half the men saw their pay doubled. Until then, "
            "keeping a workforce of 14,000 had meant hiring about 53,000 people a year. In 1915 the company hired 6,508, "
            "most of them because the business was growing. ==He later counted the five-dollar day among the best "
            "cost-cutting moves the company ever made==.",
        "f": [
            {"n": "Turnover is not on the payroll",
             "d": "When people leave, hiring, training and beginners' mistakes cost money that never appears as wages but still comes out of profit. He reckoned that at the old rate of turnover his later workforce would need nearly 200,000 hires a year.",
             "eg": "If one role turns over three times a year, add up three rounds of hiring and training before comparing it with a raise."},
            {"n": "The people who stay get better",
             "d": "Even on simple work, he said, a man with a year's experience does more than he did in his first days, and a worker free of worries at home grows steadily more efficient. High wages lowered costs through those who stayed.",
             "eg": "Keeping someone with three years in the job is often cheaper than hiring two new people."},
            {"n": "The money came with a day's work",
             "d": "He argued that there must be a fixed day's work before a real wage can be paid, and that simply putting more money in the pay envelopes would likely have broken the work standards. The raise came with conditions and a set output.",
             "eg": "Before giving a raise, write down what the role must deliver in a day."},
        ],
        "q": [
            "Five dollars a day was a way to save money.",
            "People who keep leaving are the dearest cost.",
            "First a fixed day's work, then a real wage.",
        ],
        "apply":
            "Where you are: you are cutting costs, wages are the biggest line, and people keep leaving after a few months so someone is always learning.\n"
            "Ask first: what does each departure really cost me, and would a raise earn that back?\n"
            "Where it goes wrong: reading it as 'pay more and people stay and costs fall'. His raise came after the day's work was defined and the process let one person produce far more. Without both, a raise is only a cost. He also warned that pay raised too fast is easily taken as easy money.",
    },
]
