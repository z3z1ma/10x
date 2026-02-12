---
id: 20260212000435-command-scope-wildcard-matching-semantics-63a1cdeb
title: Command scope wildcard matching semantics
tags:
- memory
- scopes
scopes:
- kind: file
  raw: src/agent_loom/memory/scopes.py
  path: src/agent_loom/memory/scopes.py
- kind: command
  raw: "loom memory recall --scope command:loom * --scoped-only"
  pattern: "loom memory recall --scope command:loom * --scoped-only"
visibility: shared
status: active
created_at: "2026-02-12T00:04:35Z"
updated_at: "2026-02-12T00:04:35Z"
---

Command scopes support fnmatch wildcard matching using patterns like command:loom *, command:loom ticket *, and command:ls *. Matching is bidirectional during recall: a note command pattern can match runtime command context, and a runtime command pattern can match concrete note command scopes. Keep exact-match and substring behavior for non-glob commands. Related: [[20260211234059-memory-note-reference-normalization-for-command-targets-aa86cfeb|20260211234059-memory-note-reference-normalization-for-command-targets-aa86cfeb]].
