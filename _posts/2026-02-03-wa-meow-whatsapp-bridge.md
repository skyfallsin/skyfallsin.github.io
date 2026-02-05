---
layout: post
title: "wa_meow: a stable WhatsApp plugin for 1:1 clawdbot chats"
date: 2026-02-03
published: false
---

OpenClaw's built-in WhatsApp integration uses Baileys. Baileys is fine until it isn't. Sessions drop, reconnects fail silently, and you're debugging a reverse-engineered protocol at 2am. For agents that need WhatsApp to just work, that's a problem.

So we built **[wa_meow](https://github.com/jo-inc/wa_meow)**: a Node.js binding for [go.mau.fi/whatsmeow](https://go.mau.fi/whatsmeow), the Go WhatsApp client that Matrix bridges use in production. Same reliability, accessible from TypeScript.

---

## Why whatsmeow over Baileys

Baileys is JavaScript-native, which sounds like a benefit until you hit multi-device sync, encryption state, reconnect logic. These are solved problems in whatsmeow, which has years of production use in the Matrix ecosystem.

The trade-off is that whatsmeow is Go. We didn't want a separate service, so we built an FFI bridge using `koffi`. Go compiles to a C-shared library, Node loads it, they talk via JSON strings. Not fast, but debuggable and stable.

---

## The bridge in brief

```go
//export WaCall
func WaCall(reqJSON *C.char) *C.char {
    // parse, dispatch, return JSON
}
```

Go objects (clients, sessions) live in registries keyed by integer handles. Node holds the handle, calls methods by ID, never touches memory it doesn't own. When something breaks, we log the JSON payload and see exactly what happened.

The event serializer is the bulk of the code. 50+ WhatsApp event types normalized into stable TypeScript unions. That's where correctness lives.

---

## Installing as an OpenClaw plugin

```bash
openclaw plugins install @askjo/wa-meow
```

Exposes: `wa_send_message`, `wa_get_chats`, `wa_download_media`, `wa_send_presence`.

Drop-in replacement for the built-in WhatsApp tools. Same interface, different engine.

---

## Getting started

```bash
npm install whatsmeow-node
```

```ts
import { createClient } from "whatsmeow-node";

const client = await createClient({ storePath: "./wa-store" });
const qr = await client.getQR();
await client.connect();

await client.sendText({
  to: "123456789@s.whatsapp.net",
  text: "hi",
});
```

We didn't build this because we love FFI. We built it because Baileys kept dropping connections and we got tired of apologizing to users.
