---
id: 20260211214655-agentic-memory-cli-append-normalization-patterns-241b6c19
title: Agentic memory CLI append normalization patterns
tags:
- memory
- ux
scopes:
- kind: file
  raw: src/agent_loom/memory/cli.py
  path: src/agent_loom/memory/cli.py
- kind: file
  raw: src/agent_loom/memory/hydrate.py
  path: src/agent_loom/memory/hydrate.py
- kind: command
  raw: loom memory append <id> --append ...
  pattern: loom memory append <id> --append ...
visibility: shared
status: active
created_at: "2026-02-11T21:46:55Z"
updated_at: "2026-02-11T21:47:36Z"
---

For agentic UX in [[20260211211958-memory-scope-kinds-ignore-unknown-11557cf3|20260211211958-memory-scope-kinds-ignore-unknown-11557cf3]], normalize hallucinated plural flags such as --tags, --aliases, --scopes, --links, and --relateds. Map append aliases (add-note, append-note) to a dedicated append command. Avoid stdin foot-guns: when stdin is piped for edit/update/append with no explicit body mode, return structured ARG guidance instead of silently ignoring input. Hydration scaffolds are more likely to be maintained when stubs include provenance context and existing empty scaffolds are seeded when referenced.
