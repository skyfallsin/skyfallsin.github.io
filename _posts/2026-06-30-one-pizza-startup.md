---
layout: post
title: The One Pizza Startup
date: 2026-06-30
published: true
description: Zero-to-one teams used to trade O(n²) communication for speed. LLMs flip that math. Two disciplined engineers can now get to PMF faster.
---

Around December 2025, seasoned engineers noticed that frontier coding models now generated consistently high-quality code at a low cost. This has changed the dynamics of starting companies.

Technical founders seem to be realizing collectively that there’s a new path, one that lets a small founding team run more product learning loops each week without adding the comms overhead that usually comes with adding more team members.

The problem: no number of engineers saves a company that lacks product-market fit. Except, the engine of PMF is a tight, compounding learning loop, which requires a focused team and not lots of lines of code written by a large one.

Founding teams need to maximize their probability of growth by getting as many high-quality at-bats as possible before time runs out. Otherwise the paths are failure or being annoyingly diluted, not to mention founder opportunity cost.

This post is intended to start the conversation on how LLMs can change this, using back-of-the-napkin math and thinking.

### Pre-LLM startup life

Before LLMs, new startups were told to hire slowly but most never listened. The usual advice as the business scaled was:

> Hire a solid team of engineers, and as a technical founder/CEO you free up your time to “run the business” while increasing the probability of creating best-in-class IP, at the expense of reducing your runway. But your team will ship faster.
>
> This IP will then lead to liquidity for all if it’s sufficiently high in value while protecting the downside risks of future financing and team attrition.
>
> Worst case scenario, if the product doesn’t work, the engineering team lands on its feet with an acqui-hire. [^1]

Ever since Opus 4.7 & GPT-5.5, this line of pre-LLM thinking seems to be fraying.

Inside software companies, the act of changing code to meet customer expectations directly drives growth, and is both the biggest cost and value center.

Pre-LLM, any group of _n_ engineers had `(n*(n-1))/2` number of 1:1 communication channels.

A starting founding team of two people had exactly one communication channel, and staggeringly fast execution.

However, as team size grows, the number of channels grows non-intuitively and quadratically while the number of concurrent threads an engineer can handle remains exactly one.

| Headcount | \# of comms channels | Active threads per engineer | Active threads |
| --------- | -------------------- | --------------------------- | -------------- |
| 2         | 1                    | 1                           | 2              |
| 4         | 6                    | 1                           | 4              |
| 6         | 15                   | 1                           | 6              |
| 10        | 45                   | 1                           | 10             |

A growing team’s execution velocity usually slowed down, started behaving non-deterministically and needed more human oversight. Since each engineer could only run one thread, it was crucial to discover what the right changes had to be before anyone touched an editor. So, communications requirements started eating into the time spent modifying code.[^2]

For a team of six, we have six code editors open (one per person) but 15 potential 1:1 communication channels.

Financially, assuming an engineer costs $250k/year, a team of six is $1.5M, which leads to 12-14 months of runway for a $2M seed round after $500k in other expenses. Purely from a financial lens, given the communication requirements, engineering budgets for teams over two people were underutilized expenses.

If you were an especially good founding team, in practice 12-14 months gets you  approximately 8-10 months of at-bat PMF attempts before you have to plan next steps if there’s no PMF. At the same time, the engine of product-market fit is a continuous learning loop directly tied to code change velocity post-insights.

Going from seed-stage startup to a robust company was and is quite brutal.

### LLMs break the patterns

Like humans, LLMs also behave non-deterministically and need human oversight. However, if an engineering team consists instead of a small number of engineers running many LLM code threads, this materially changes the velocity & survival possibilities for an early startup.

The team structure goes from the `O(n²)` communication problem to a much more tractable  `O(n)` _attention_ problem of a small team of engineers attending to _n_ concurrent threads in parallel.

| Headcount | \# of comms channels | Active threads per engineer | Total active threads |
| --------- | -------------------- | --------------------------- | -------------------- |
| 2         | 1                    | 5                           | 10                   |
| 4         | 6                    | 5                           | 20                   |
| 6         | 15                   | 5                           | 30                   |
| 10        | 45                   | 5                           | 50                   |

The same team of six now can run 30 concurrent threads instead of six, with a theoretical (but usually not practical) upper cap of 5x the output at double the cost.

The above is a capacity model, not a productivity claim.

Less synchronization is needed since writing throwaway prototypes is now cheap. This speeds up the entire company’s learning loop, which is the primary engine of product-market fit, and gives founders a true dial for maximizing at-bats vs engineering budget.

### One pizza for a long time

A “one pizza startup” is a founding team small enough to have a single conversation pair, between two people who can hold the entire product in their heads and use concurrent LLM threads to get more done faster.

Kevin & I have been iterating for a year or so now with this pattern, and it’s pretty freakin’ fast. It’s hard to go back.

_n_ LLMs type out code faster than humans manually writing it. A bit of tech, intuition and disciplined human oversight of quality and token burn makes that code actually shippable.

LLM-fluent engineers execute high-quality deltas in hours, not weeks. Now the hard work is choosing the right bets, building high-quality architecture and maintaining a taste-led, high-bar culture.

Engineering success within these new structures hinges on heavy lifting:
- the caliber of the engineers in question,
- their paranoid attention to system architecture and maintenance,
- their ability to run context-switching marathons without burnout, and
- rigorous token budgeting and discipline.

The upside is simple: the founding team gets double the at-bats in a shorter window of time. It forces urgency, which materially increases your chances of _actually_ achieving product-market fit, rather than posturing that you have it. [^3]

So… why add more people to a zero-to-one engineering team until you need them?

The best founders may now be able to stay small, fast and high-bandwidth for longer than before. Hiring goes from a structural issue to one that’s a problem to solve when the current team can’t, as it absolutely should. The best seed startups get more chances to iterate their way to PMF. But, it’ll take discipline!

----
_Thank you to Naveen Selvadurai, Walter Chen, Silas Hundt, Hiten Shah and Michael Galpert for draft feedback._


[^1]:	Pre-LLM — Since code was more expensive to create but highly leveraged, a notion also seems to have developed among seed-stage financiers that “more code needs more engineers, so it’s hard to pull off fast, and *that difficulty* is also a part of the moat of a new product”.

	The problem is that implementation difficulty is a weak proxy (and getting weaker) for PMF. So when “small team” becomes a proxy for “easily implementable and not enough moat,” that objection starts to sound less like analysis and more like an excuse to pass.

	This means optically you were lower risk with a larger team. A team is always interesting to acquirers even if the product fails, increasing the chances of any return at all.

	Post-LLM — The worst-case downside scenario from before is now markedly different - if there is an acqui-hire, it’ll look more like an extra-rich IC offer at a big shop for phenomenal engineers. But there may also not be an offer at all, since the team size is small.

[^2]:	This is well-understood territory, see [“Mythical Man Month”][1].

[^3]:	And once you have product-market fit, there’s a higher probability of above-average software margin over time due to the initial discipline of carrying almost no fixed headcount costs, as long as it’s kept an eye on. High margins plus capital efficiency do translate into premium multiples in the public markets.

	That single trade at the beginning: going from the _O(n²)_ personal communication problem to the _O(n)_ attention problem could actually compound from seed-stage runway all the way to IPO.

[1]:	https://www.amazon.com/dp/0201835959?lv=shuf&channelId=500&plpRedirect=mhFallback
