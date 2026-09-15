---
layout: post
title: "agenthook: give your coding agent an inbox"
date: 2026-09-14 23:30:00 -0700
published: true
description: "agenthook is a webhook inbox for coding agents: GitHub Actions, services, and other agents can send an update into the session that needs it."
image: /images/posts/agenthook.png
image_alt: "A friendly blue hawk holding a sealed envelope"
image_class: post-hero-logo
thumb: /images/logos/agenthook.jpg
---

It's annoying when you're working inside a coding agent, doing something with an external service that takes more time than a single turn. For example, a github deploy. Unless the agent is monitoring (which blocks the execution), we might not know.

I kept wanting a simple way to fix that.

[agenthook](https://github.com/skyfallsin/agenthook) gives a coding agent a
small inbox.

Tell your agent to listen on a topic. Then a GitHub Action, a service, or another agent
can post an update to that topic. The agent gets the ping in its own session.

I usually run this on a ngrok on my local machine, but it can be run remotely too if you're running cloud agents.

It works with Pi, Claude Code, and Codex today.

Here's how it works. When your agent needs to wait on some other entity:
  - Your agent creates a 'topic' with agenthook.
  - Something else (agents, external services) posts to agenthook's server endpoint at http://127.0.0.1:$PORT for that topic
  - Your agent gets a notification inside its session that there's been an update.
  - Agent does something with that new update.

This is a starting point, not a whole agent-control platform. It is enough to
build some cool new things: nested subagent trees, small swarms, deploy
listeners, or whatever else needs to tell an agent that something happened.

Also, yes, there is an existing [Apache-licensed AgentHook](https://github.com/agentic-thinking/agenthook). I know, and this is what I'm going with.

Here’s [agenthook](https://github.com/skyfallsin/agenthook).
