---
id: 20260211234059-memory-note-reference-normalization-for-command-targets-aa86cfeb
title: Memory note reference normalization for command targets
tags:
- memory
- ux
scopes:
- kind: file
  raw: src/agent_loom/memory/vault.py
  path: src/agent_loom/memory/vault.py
- kind: file
  raw: src/agent_loom/memory/core.py
  path: src/agent_loom/memory/core.py
- kind: command
  raw: loom memory edit <note-ref> --append ...
  pattern: loom memory edit <note-ref> --append ...
visibility: shared
status: active
created_at: "2026-02-11T23:40:59Z"
updated_at: "2026-02-11T23:40:59Z"
---

When a memory command targets an existing note, resolve the user input as a note reference instead of requiring literal id only. Accept id, title, alias, and slug-like variants with deterministic ranking, then fail fast on ambiguity. Apply this consistently across edit, append, show, open, around, and link commands that take a note target. Keep create-time id checks exact-only so add id uniqueness remains strict. Related: [[20260211214655-agentic-memory-cli-append-normalization-patterns-241b6c19|20260211214655-agentic-memory-cli-append-normalization-patterns-241b6c19]].
