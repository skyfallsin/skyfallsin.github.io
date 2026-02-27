---
layout: post
title: "Jo 1.0"
date: 2026-02-27
published: false
description: "A personal AI assistant that lives on your Mac, knows your context, and gets better every day."
---

Jo is a personal AI assistant. Half of it runs on your Mac: voice, screen reading, photos, files. Anything that touches your personal data. The other half runs on a dedicated machine in the cloud: conversations, memory, tools, scheduled tasks. Nobody else's data touches yours on either side. The two halves sync with minimal data crossing the boundary. Just your question and enough context to answer it.

This is the philosophy behind it.

---

## Your personal data stays on your Mac

Voice, screen, photos, files, reminders, notes. All processed locally. None of it leaves your Mac.

Jo reads your screen by pulling the actual content from Safari, Chrome, Notes, Slack, Messages. Not screenshots. A local model that ships with Jo processes all of this into clips, grouped by what you're working on, without anything leaving your machine.

---

## Voice is a first-class citizen

Transcription runs locally on your Mac. Echo cancellation means you can talk through your laptop speakers without headphones. No AirPods required. You can be cooking, walking around, doing laundry, and just talk.

You can also send voice messages on Telegram or WhatsApp, and have Jo respond in audio.

---

## Your own zero-maintenance machine in the cloud

Most AI products put everyone in the same database. Jo gives each user their own machine. Dedicated storage, dedicated compute. Nobody else's data touches yours.

Your storage shows up as a drive on your Mac. Browse your files, read your memories, see your conversation history. Regular files on a mounted drive.

**Your data is physically separate from everyone else's.** Different machine, different storage, different everything.

**No noisy neighbors.** Someone else's heavy request doesn't slow you down.

---

## One Jo across every channel

Mac, Telegram, WhatsApp. Same Jo, same conversations, same memory. The channels are windows into the same system, not separate bots.

Every message follows the same path to your machine and back.

---

## Fast for simple things, thorough for hard things

The most powerful AI models are also the slowest. "What's on my calendar today?" doesn't need 30 seconds of deep reasoning.

A fast model handles most requests in 1-2 seconds: calendar, search, reminders, weather. When a request needs more depth, it hands off to a reasoning model with the full set of tools.

You pick the models. OpenAI, Anthropic, Grok, Kimi — each with their own routing and reasoning pair, and more coming soon. Jo also ships with a local model that runs entirely on your Mac.

---

## Tools that run on your Mac, triggered from the cloud

When Jo needs to search your photos, the request travels from the cloud to your Mac, runs locally, and sends the results back. Same for reminders, notes, files, browser tabs. Everything that only exists on your machine.

The things that make a personal assistant useful live on your Mac. So the tools run there too.

---

## Real web browsing

Jo can browse the web. Not just fetch pages, but actually navigate, click, scroll, and fill out forms. It runs a fingerprint-resistant browser on a separate machine so sites treat it like a real user.

Works well for searching, reading articles, checking prices, and filling forms. Adversarial sites with heavy bot detection are harder. This is the area with the most room to improve.

---

## Memory

Jo's memory has two sides.

**What we've done together.** Every conversation is stored and searchable. "What did we talk about last week about restaurants" works across all channels. Plain text files track the ongoing relationship: notes and decisions, what happened each day, things to come back to. If you want to see what Jo remembers, open the files. They're right there in plain text.

**The facts about you.** Preferences, locations, routines, contacts. When Jo knows you prefer window seats, live in San Francisco, and have a meeting with Sarah every Tuesday, it doesn't need to be told again.

---

## It notices what you're working on

Most productivity tools ask you to organize. Create folders, apply tags, sort into categories. Jo does it differently.

It watches your browser tabs, notes, and saved content, then groups related activity into clips. All locally, using the model that ships with Jo. Eight tabs about Tokyo neighborhoods, a saved article about cherry blossoms, and a restaurant list becomes "Japan Trip Planning." None of that activity leaves your Mac.

It focuses on *what you're thinking about*, not *what you're clicking on*.

---

## Jo does things when you're not there

Jo runs scheduled tasks. A morning briefing with your calendar, weather, and things you're tracking. Weekly planning on Sunday evening.

You can create your own too. "Alert me if BTC drops below $90K" checks the price and only messages you when the condition is met. No "nothing to report" noise.

Delivery goes wherever you want. This shifts Jo from something you go to into something that comes to you.

---

## What's actually private

**Never leaves your Mac:** Voice, screen content, photos, files. All processed locally.

**Lives on your machine in the cloud:** Conversations, memories, skills. Physically separate from every other user.

**Cloud inference:** Your prompts go to the AI model you choose. Our cloud models run on contracts that prevent training on your data.

---

## Is this just OpenClaw?

Jo is built on the same [pi](https://github.com/mariozechner/pi-coding-agent) roots as [OpenClaw](https://openclaw.com). Plain text memory, self-extensible skills, markdown rules that the AI reads and writes directly. But Jo goes deeper. A nightly reflection loop reviews each day's sessions, finds where things went wrong, and rewrites the behavioral rules so the same mistakes don't repeat. On top of that, custom tools for calendar, email, photos, screen reading, browser automation, voice, and scheduled tasks that turn a general-purpose agent into a personal assistant.

less planning. more doing.
