---
id: 20260209193523-inspect-pack-drift-diffs-f02eb23a
title: Inspect pack drift diffs
tags:
- cli
- pack
scopes:
- kind: command
  raw: loom pack status --diff
  pattern: loom pack status --diff
visibility: shared
status: active
created_at: "2026-02-09T19:35:23Z"
updated_at: "2026-02-09T19:35:23Z"
---

Use `loom pack status --diff` to print unified diffs for drifted managed files.

Behavior:
- Default `loom pack status` prints a drift/missing summary and, if drift exists, a hint to rerun with --diff.
- With --diff, it prints per-file diffs as `diff (drifted): <pack-id>/<relpath>` followed by a unified diff.
- Diffs are truncated to 400 lines per file.
- For machine consumption, `loom pack status --json --diff` includes a `diffs` array (each item includes pack_id, relpath, ok, diff).

Note: diffs compare current builtin pack sources to the repo file on disk (useful to preview what an update/force would overwrite).
