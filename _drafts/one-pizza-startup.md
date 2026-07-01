---
layout: post
title: The One Pizza Startup
date: 2026-06-30
description: Zero-to-one teams used to trade O(n²) communication for speed. LLMs flip that math. Two disciplined engineers can now get to PMF faster.
---

Roughly around December 2025, seasoned engineers noticed that frontier coding models now generated consistently high-quality code at a low cost. This has changed the dynamics of starting companies, and technical founders seem to be realizing collectively that there’s a new path, one that could increase the chances of success to an IPO while reducing the costs of getting there.

The problem: no number of engineers saves a company that lacks product-market-fit.  Except the engine of PMF is a tight, compounding learning loop, which requires a focused team. They need to maximize their probability of success by using as few at-bats as possible to make a company’s growth durably skyrocket. Otherwise the paths are failure or being annoyingly diluted, not to mention founder opportunity cost.

This post is intended to start the conversation on how LLMs can change this, using back-of-the-napkin math and thinking.

# Pre-LLM startup life
Before LLMs, new startups were told to hire slowly but most never listened. The usual advice as the business scaled was:

> Hire a solid team of engineers, and as a technical founder/CEO you free up your time to “run the business” while increasing the probability of creating best-in-class IP, at the expense of reducing your runway. But your team will ship faster.
> 
> This IP will then lead to liquidity for all if it’s sufficiently high in value while protecting the downside risks of future financing and team attrition. 
> 
> Worst case scenario, the product doesn’t work, the engineering team lands on its feet with an acqui-hire. [^1]

But ever since Opus 4.7 & GPT-5.5, this line of pre-LLM thinking seems to be fraying.

Inside software companies, the act of changing code to meet customer expectations directly drives growth, and is both the biggest cost and value center.

Pre-LLM, any group of _n_ engineers had `(n*(n-1))/2` number of 1:1 communication channels.

A starting founding team of two people had exactly one communication channel, and staggeringly fast execution. 

However, as team size grows, the number of channels grows non-intuitively and quadratically while the number of parallel work streams an engineer can handle remains exactly one.

| Headcount | \# of comms channels | Workstreams per engineer | Total work streams/day |
| --------- | -------------------- | ------------------------ | ---------------------- |
| 2         | 1                    | 1                        | 2                      |
| 4         | 6                    | 1                        | 4                      |
| 6         | 15                   | 1                        | 6                      |
| 10        | 45                   | 1                        | 10                     |

A growing team’s execution velocity usually slowed down, started behaving non-deterministically and needed more human oversight. Since each engineer could only run one work stream, it was crucial to discover what the right changes had to be before anyone touched an editor. So, communications requirements started eating into the time spent modifying code.[^2]

For a team of six, we have six code editors open (one per person) but 15 potential 1:1 communication channels. 

Financially, assuming an engineer is $250k/year, a team of six is $1.5M, which leads to 12-14 months of runway for a $2M seed round after $500k in other expenses. Purely from a financial lens, given the communication requirements, engineering budgets for teams over two people were underutilized expenses.

If you were an especially good founding team, in practice 12-14 months gets you  approximately 8-10 months of at-bat PMF attempts before you have to plan next steps if there’s no PMF. At the same time, the engine of product-market-fit is a continuous learning loop directly tied to code change velocity post-insights.

Going from seed-stage startup to a robust company was and is quite brutal.

How does this change with LLMs in the mix?

LLMs also behave non-deterministically and need human oversight. However, if an engineering team consists instead of a small number of engineers running many LLM code threads, this materially changes the velocity & survival possibilities for an early startup.

The team structure goes from the `O(n²)` communication problem to a much more tractable  `O(n)` _attention_ problem of a small team of engineers attending to _n_ LLM coding work streams in parallel.

| Headcount | \# of comms channels | Agent work streams per engineer | Total work streams/day |
| --------- | -------------------- | ------------------------------- | ---------------------- |
| 2         | 1                    | 5                               | 10                     |
| 4         | 6                    | 5                               | 20                     |
| 6         | 15                   | 5                               | 30                     |
| 10        | 45                   | 5                               | 50                     |

The same team of six now can run 30 work streams running in parallel instead of six, with a theoretical (but usually not practical) upper cap of 5x the output at double the cost. 

Less synchronization is needed since writing throwaway prototypes is now cheap. This speeds up the entire company’s learning loop, which is the primary engine of product-market-fit, and gives founders a true dial for maximizing at-bats vs engineering budget.

It gets very interesting when the team size drops down to 2 engineers with this structure. 

One conversation pair, between two people who can hold the entire product in their heads and use LLM work streams to get more done faster. This is the “one pizza  startup”, and it’s pretty freakin’ fast. Kevin & I have been iterating for a bit now with this pattern, and it’s hard to go back.

_n_ LLMs type out code faster than humans manually writing it. A bit of tech, intuition and disciplined human oversight of quality and token burn makes that code actually shippable. 

AI-native engineers are able to orchestrate LLMs to execute high-quality deltas in hours, not weeks. 

Engineering success within these new structures hinges on heavy lifting: 
- the caliber of the engineers in question, 
- their paranoid attention to system architecture and maintenance, 
- their ability to run context-switching marathons without burnout, and 
- rigorous token budgeting and discipline. 

The upside is simple: the founding team gets double the at-bats in a shorter window of time. It forces urgency, which materially increases your chances of _actually_ achieving product-market-fit, rather than posturing that you have it. 

And once you have product-market-fit, there’s a higher probability of above-average software margin over time due to the initial discipline of carrying almost no fixed headcount costs, as long as it’s kept an eye on. High margins plus capital efficiency translate into premium multiples in the public markets.

That single trade at the beginning: going from the _O(n²)_ personal communication problem to the _O(n)_ attention problem could actually compound from seed-stage runway all the way to IPO. 




[^1]:	Pre-LLM — Since code was more expensive to create but highly leveraged, a notion also seems to have developed among seed-stage financiers that “more code needs more engineers, so it’s hard to pull off fast, and *that difficulty* is also a part of the moat of a new product”. This means optically you were lower risk with a larger team. A team is always interesting to acquirers even if the product fails, increasing the chances of any return at all. 

	Post-LLM — The worst-case downside scenario from before is now markedly different - if there is an acqui-hire, it’ll look more like an extra-rich IC offer at a big shop for phenomenal engineers. But there may also not be an offer at all, since the team size is small.

[^2]:	This is well-understood territory, see [“Mythical Man Month”][1]. 

[1]:	https://www.amazon.com/dp/0201835959?lv=shuf&channelId=500&plpRedirect=mhFallback