---
layout: post
title: "Jo, In Commits: 38 Months of Building an Always-On Agent"
date: 2026-02-03
published: false
---

We've been building jo long enough that the git history stopped being "progress" and turned into evidence.

Not the clean, launch-tweet kind. The real kind: half-finished experiments that almost worked, integrations that were 90% auth edge cases, the same feature rebuilt three times because the first two were lies, and a few moments where the loop suddenly felt alive.

I'm Pradeep. I've been building jo with [Kevin Li](https://x.com/liveink) since 2023. We're writing this the way we'd tell it to other developers: specific, honest about the schleps, and structured around the turning points that actually mattered.

---

# Act 1: The Telegram era (learning what doesn't work)

## Aug 2023: 59 users in a chat thread

GPT-4 was five months old. Claude 2 had just dropped. The industry was drunk on "ChatGPT for X" pitches.

jo at that point was not a desktop app. It wasn't a "planner/executor system." It was an invite-only Telegram bot with 59 users, built fast on GPT-4 + Python + Fly.io + LanceDB.

Telegram was the fastest way to get the one thing we couldn't fake: usage pressure.

But it came with a weird tax we didn't fully understand yet. Telegram has a sketchy reputation (crypto-adjacent energy), people treat anything in a chat thread like free ChatGPT, the canvas is tiny and hostile to real work, and voice would be a fight.

We didn't know it then, but we were already walking toward the next iteration.

## Dec 2023: jo ordered a pizza (and: integrations hell)

By Dec 2023 we had "full" Google integration: Gmail, Calendar, Contacts, Docs. Morning briefings. Image generation. Voice call prototypes. Thousands of alpha users.

Also: jo ordered a pizza. It arrived. That mattered more than it should have.

The lesson wasn't "wow, AI can order pizza." The lesson was: the work is the glue. Every "simple" integration is actually auth + permissions + rate limits + latency + retries + UX + angry edge cases. And when it breaks, it breaks in front of the user, not in a unit test.

## Jan 2024: "thank you, Ms. AI"

We were testing outbound voice calls. jo called Xfinity customer support to handle a billing issue. Navigated the phone tree, waited on hold, talked to a human rep, resolved the issue.

At the end of the call, the rep said: "Thank you, Ms. AI."

She knew. And she didn't care. The task got done.

That moment stuck with us. Not because it was a technical milestone (it was janky and half-broken). But because it showed what the endgame looks like: the agent handles the call, the human gets their time back, and nobody needs to pretend the AI is a person.

## Feb 2024: retention still elusive

YC W24 was when we got more serious and more humbled at the same time.

Google OAuth got approved (huge unlock). We tested outbound phone calls and telephone-tree navigation. A new onboarding doubled conversion. Retention… still elusive.

That last part hurt more than we admitted at the time. We were building fast, shipping features, watching usage metrics, and the line just wouldn't bend. Users would try jo, be impressed for a day, then drift back to ChatGPT or just stop messaging entirely.

We had a big hint though: voice-in, text-out felt like the beginning of a moat. This was seven months before OpenAI would ship GPT-4o voice mode.

Not because voice is trendy. Because voice changes the loop. It makes the agent feel less like a document editor and more like a co-worker: you speak → it responds immediately → it does the annoying part.

We didn't fully understand this yet. We just felt it.

---

# Act 2: The iteration and the schlep

## Mar 2024: the crucial move

In Mar 2024 we moved from Telegram to a native macOS app.

The unromantic reasons we wish we'd admitted earlier: Telegram reputation was bleeding into the product, users treated it as free ChatGPT, chat is a limiting UI for doing things, voice integration was blocked/awkward, and we needed the agent to "see what we see."

We picked SwiftUI partly because we're Apple people and partly because it keeps an option value: macOS now, iPhone/iPad/Vision later.

We started TestFlight alpha and built the actual loop we wanted.

## Apr 2024: watching Humane and Rabbit die in public

By Apr 2024 the macOS app was in private alpha. We shipped the global hotkey (Shift+Cmd+J), context capture from highlighted text, and calendar integration.

That same month, Humane's AI Pin and Rabbit R1 shipped to brutal reviews. "Barely reviewable." Fire hazard warnings. Returns outpacing sales. Two well-funded bets on AI hardware were dying in public while we quietly built software.

We watched obsessively. Not to gloat, but because they were stress-testing UX assumptions we'd been debating internally. Their lesson: novel hardware doesn't save you if the interaction loop is broken.

It was clarifying. And a little terrifying. These were teams with real resources and real talent, and the market was rejecting them in realtime. It forced us to ask: what are we actually building that's different? The answer kept coming back to the same thing: the loop. Voice in, action out, no ceremony.

## May–Jul 2024: the 80% tax

This was the part where building looked like 20% features and 80% "why did this permission prompt appear this time?"

Browser workflows that chained together. Our eval suite finally working. Audio fixes. Display support. None of it glamorous. All of it necessary.

We wrote in our notes: "The differentiator isn't the demo. It's whether you can survive the boring parts."

---

# Act 3: Voice changes everything

## Sep 2024: jo speaks back

Sep 2024 was a real milestone: jo could speak back. OpenAI had just shipped GPT-4o voice mode. The industry was finally taking voice seriously.

"Hey jo" didn't steal focus. The product felt less like software and more like presence. Not magical. Just… present.

## Oct–Dec 2024: local models become non-negotiable

Oct 2024 we wrote the vision down plainly: "Working with jo should feel like having a close friend sitting next to you with a copy of your laptop."

In Nov 2024 we shipped proactive behavior: a contextual overlay popping up while you work. And we integrated our first local model for summarization.

This is where local models stopped being ideology and became a consumer product requirement: privacy isn't a settings page. It's whether the user trusts us enough to leave it running.

## Mar–Apr 2025: the magic moment

Mar 2025 we did 50+ user onboardings and got the clearest product signal we've ever gotten: dictation is the magic moment. Browser prefill is the second magic moment ("find me flights from sfo to jfk").

In Apr 2025 we shipped the loop we'd been chasing: hold `fn`, speak, and text appears with perfect punctuation.

No dictation mode. No ceremony. Just talk like a human and keep moving.

By now, 22% of the YC W25 batch was building voice agents. Voice AI had gone from niche to thesis.

That voice-in, text-out insight from YC became a conviction: typing is slow, writing is emotionally loaded, speaking is fast and low-friction, and the agent can translate speech into clean, shippable text.

---

# Act 4: The system comes alive

## May–Jun 2025: the browser fork in the road

May 2025 we added TODO lists where jo actually works on items for you. Deep Apple Notes integration. A memory stack where jo decides what to save long-term.

Then Jun 2025 forced a hard decision about browser automation.

Two paths: remote browser (slow, auth is painful, UX is brittle) or local Safari WebView (keychain, TouchID, feels like your actual computer because it is).

We chose local Safari. Not because remote browser automation isn't cool. Because if you want a daily driver, the browser has to feel native and trustworthy.

## Jul–Oct 2025: parallelism and 1.0 RC

Jul 2025 we shipped agentic behavior. Multiple agents working together.

Oct 2025 we launched 1.0 RC. jo no longer single-threaded. Planner/executor system for autonomous work with self-verification.

This was the point where jo started to feel less like "a chat app with tools" and more like "a system that can actually run a playbook."

## Nov 2025: the painful realization about chat UIs

Nov 2025 we wrote down something we'd been circling for months: starting with a chat-based UI remains a massive mistake for consumer AI. Consumers are anxious writers.

It's not that people can't type. It's that asking someone to stare at a blank input and "tell the AI what you want" is like asking them to draft an email to a stranger, every time, forever.

So we shifted toward suggesting things to tap and guiding the loop, not waiting for perfect prompts.

We started importing Messages, WhatsApp, Telegram, browser history. Not to be creepy. To reduce friction and make jo useful without asking the user to become a prompt engineer.

## Dec 2025 – Jan 2026: hybrid local + remote stack

By Dec 2025 we had local model for privacy, cloud models for capability. Themes auto-generated every minute from browser + chat. Facts extracted from Gmail. What we called (accurately, we think): "first ever hybrid local + remote LLM stack."

Browser history + chat scraped in realtime, stored locally. Semantic + wildcard search across all history.

The product started to look like: an always-on context engine + a fast voice loop + a browser agent that can actually log in + a model router that doesn't break trust.

---

# Feb 2026: OpenClaw shows up

Feb 2026 OpenClaw emerged as serious competition.

We took it as validation, not panic. But we'd be lying if we said we didn't spend a weekend doing a full teardown.

What OpenClaw got right: always available on messaging, self-improving behavior, scheduled tasks, personality that's actually fun to talk to. They understood that "agentic" isn't enough. The thing has to feel like someone you'd want to keep around.

What we think they got wrong: remote-first architecture means auth is always painful, response times have a floor they can't break through, and privacy is a promise rather than a constraint. Their browser automation is impressive in demos but brittle in daily use. And they haven't solved the "anxious writer" problem. You still have to know what to ask for.

We didn't change our roadmap. But we did move faster on the things we already knew mattered: local-first privacy, native browser integration, and the voice loop.

---

# The schleps (the part we now think is the work)

If you're building always-on agents, the differentiator isn't your demo. It's whether you can survive the boring parts:

- always-on endpoint that doesn't flake
- browser automation that works with real auth, real keychains, real 2FA
- secure code execution (actual sandboxing, not "please behave")
- good models and a product that can switch models without whiplash
- a UX loop that doesn't require users to be confident writers

We didn't solve these once. We just kept paying the tax until it started to compound in our favor.

---

# Where we think this goes

We think the natural endpoint of "agent as coworker" is obvious and uncomfortable: at some point, the agent needs real handles. Credit cards, email inboxes, phone numbers.

Not tomorrow. Not casually. But if jo is going to take actual work off your plate, it can't just draft text. It has to complete workflows end-to-end.

And end-to-end workflows live in places with real permissions and real consequences.

---

# What we'd tell ourselves at month 1

1. Ship in the environment users already live in (messaging), but don't confuse distribution with product.
2. Build the "sees what you see" loop early (desktop context is not a nice-to-have).
3. Treat the schleps as the work, not bugs you'll clean up later.
4. Voice isn't a feature. It's a speed advantage and a UX therapy session for anxious writers.
5. Privacy isn't a promise. It's architecture.

---

# Stats (because we are who we are)

- 38 months
- 6,468 commits
  - 3,732 in `jo` (Swift / macOS)
  - 2,736 in `jo_bot` (Python)

<canvas id="commitChart" width="800" height="300" data-chart="
new Chart(document.getElementById('commitChart'), {
  type: 'line',
  data: {
    labels: ['2023 Q1','2023 Q2','2023 Q3','2023 Q4','2024 Q1','2024 Q2','2024 Q3','2024 Q4','2025 Q1','2025 Q2','2025 Q3','2025 Q4','2026'],
    datasets: [{
      label: 'jo (Swift)',
      data: [0,0,0,0,161,237,226,520,333,408,582,869,336],
      borderColor: '#b58900',
      backgroundColor: 'rgba(181,137,0,0.1)',
      tension: 0.3,
      fill: true
    },{
      label: 'jo_bot (Python)',
      data: [48,368,192,169,134,70,119,71,27,217,696,159,286],
      borderColor: '#268bd2',
      backgroundColor: 'rgba(38,139,210,0.1)',
      tension: 0.3,
      fill: true
    }]
  },
  options: {
    scales: {
      y: { beginAtZero: true, grid: { color: '#073642' } },
      x: { grid: { color: '#073642' } }
    },
    plugins: { legend: { labels: { color: '#93a1a1' } } }
  }
});
"></canvas>

Anyway. Back to the commits.
