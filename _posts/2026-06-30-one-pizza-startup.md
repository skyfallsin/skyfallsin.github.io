---
layout: post
title: The One Pizza Startup
date: 2026-06-30
image: /images/posts/one-pizza-startup.jpg
image_alt: Two founders and small AI robots eating pizza around laptops
description: Zero-to-one teams used to trade O(n²) communication for speed. LLMs flip that math — two disciplined engineers can now get to PMF faster.
---

## The Math of Team Size

Language models asked to assist engineers with writing code predict tokens non-deterministically, and need humans to manage their expense and set guardrails that guarantee quality and consistency. One human running *n* LLM conversations is limited by their ability to manage those *n* conversations in parallel — an **O(n)** _attention_ problem.

Groups of *n* people coding without LLMs behave non-deterministically too, and need human oversight.

Each person in that group has to communicate with *every* other member, so the number of 1:1 channels grows as **n(n−1)/2 → O(n²)**. Large teams slow down dramatically as headcount grows: a team of 10 has 10·9/2 = **45** potential 1:1 channels. In practice, org trees cap this by limiting each person to the handful they directly work with, pulling the effective cost back toward **O(n)** — a far more manageable experience.
 
But we’re talking about founding teams: zero-to-one product development with deeply technical founders. These are usually under 10 people, mostly engineers — so let’s say 6. Even at that size there are 6·5/2 = **15** distinct communication paths.

## When Code Got Cheap

Inside software companies, code generation by humans is usually the biggest cost center. Software companies also don’t grow unless the code changes to meet customer expectations, so also the biggest value center.

Before December ’25, fresh startups were told to hire slowly but most never listened.

Pre-LLM: hire a solid team of engineers, and as a technical founder you free up your time to “run the business” while increasing the probability of creating best-in-class IP, at the expense of reducing your runway. But your team will ship faster.

This IP will then lead to liquidity for all if it’s sufficiently high in value while protecting the downside risks of future financing and team attrition. Worst case scenario, the product doesn’t work, the team lands on its feet with an acqui-hire of specifically the engineering team.

Since Dec ’25, this line of thinking seems to be fraying, as recent frontier models started delivering high code quality at a low cost.

LLMs are a fraction of the cost of human engineers, generate higher quality code, don’t need weekly 1:1s, can usually work in isolation, don’t lose time worrying about the codebase’s overall quality or demanding rewrites to reduce tech debt. They can teach themselves to be better, most models improve every quarter and can follow instructions precisely. 

In the event they spawn more of themselves to work with, the relationships aren’t fraught with human dynamics and are a lot more predictably high quality.

As a software company, LLMs type out code faster than humans manually writing it. Tech, a measure of providence and human oversight combine to make that code actually shippable. The cost of managing a “team” of _n_ LLM agents is the cost of a highly paid engineer’s salary plus disciplined token burn. The best engineers are able to orchestrate LLMs to execute high-quality deltas in hours, not weeks, at the cost of _n_ individual 1:1 conversations with isolated agents.

## The One Pizza Team

Let’s do some rough napkin math now:  

Assuming an engineer is $250k/year and there’s a team of six  
`$250k * 6 = $1.5M/year` and `~$130/hr/person` assuming 48 weeks at 40h/week. 

`$130 * 6 people * 8h = $6,250/day`

That’s 12-14 months of runway for a $2M seed round after $500k in other expenses.

With a LLM-assisted stack with one engineer:  `$250k salary + $250k token burn = $500k/year` and `~$260/hr/person`, and `$2,083/day/person`.

Token burn discipline is mandatory here. Running maxed-out context windows, for example, kills code quality while also making it insanely expensive with the best frontier models. 

Let’s add one more engineer just to solve the “what if the one engineer gets hit by a bus” problem.

2x engineers at this rate is `$4,167/day`, savings of 33% compared to six engineers.

The real benefit though, is going from 15 conversation pairs to just **ONE**, between two people who can hold the entire product in their head. This is a “one medium pizza” team, and it’s pretty freakin’ fast. 

So now the big question - why add more people to a zero-to-one engineering team anymore?  A single disciplined, seasoned engineer can run multiple backends and frontends solo, written in the best language for that problem. Do we need more?

The heavy lifting being done in these team structures: the quality of the engineers in question, their paranoia when designing, building and editing systems over time, and their and the org’s token budgeting and discipline. Can these engineers context-switch aggressively without burning out over time? That’s another huge one.

## Where the Moat Actually Lives

Code as leverage is well understood. But there’s a notion in the funding market right now that small teams produce easily reproducible products with no moat — the old logic being “more code needs more engineers, so it’s hard to pull off fast, and *that difficulty* is the moat.” 

The problem: no number of engineers saves a company that lacks product-market-fit. So that objection sounds less like analysis and more like an excuse to pass. It’s likely more interesting to check whether the team has a tight, compounding learning loop that leads to PMF.

The worst-case downside scenario from before is now markedly different - if there is an acqui-hire, it’ll look more like an extra-rich IC offer at a big shop. But there may also not be an offer at all, since the team size is small.

The best case scenario is you _actually_ solve for product-market-fit faster, instead of saying you do.  You have more at-bats as a founding team.

And once you have product-market-fit, there’s a higher probability of above-average software margin due to the initial discipline of carrying almost no fixed headcount costs. 

High margins plus capital efficiency translate into premium multiples in the public markets.

That single trade at the beginning: going from the _O(n²)_ personal communication problem to the _O(n)_ attention problem compounds from seed-stage runway all the way to IPO. But, it’ll take discipline.
