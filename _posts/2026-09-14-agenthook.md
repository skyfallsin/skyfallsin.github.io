---
layout: post
title: "agenthook: give your coding agent an inbox"
date: 2026-09-14
published: true
description: "agenthook is a webhook inbox for coding agents: GitHub Actions, services, and other agents can send an update into the session that needs it."
thumb: /images/logos/agenthook.jpg
---

A deploy finishes. GitHub knows. Your terminal knows. The coding agent that
made the change does not.

I kept wanting a simple way to fix that.

[agenthook](https://github.com/skyfallsin/agenthook) gives a coding agent a
small inbox.

Tell it to listen on a topic. Then a GitHub Action, a service, or another agent
can post an update to that topic. The agent gets the ping in its own session.

It works with Pi, Claude Code, and Codex today. A deploy can say it passed. A
worker can say it is done. You do not have to keep one terminal waiting around
for another one.

Agenthook starts with those updates arriving as untrusted text, not fake user
instructions. The agent still has to decide what to do with them.

This is a starting point, not a whole agent-control platform. It is enough to
build some cool new things: nested subagent trees, small swarms, deploy
listeners, or whatever else needs to tell an agent that something happened.

Also, yes, there is an [Apache-licensed AgentHook](https://github.com/agentic-thinking/agenthook). I know, and this is what I'm going with.

Here’s [agenthook](https://github.com/skyfallsin/agenthook).
