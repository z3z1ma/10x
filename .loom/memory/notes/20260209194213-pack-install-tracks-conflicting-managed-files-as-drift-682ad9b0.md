---
id: 20260209194213-pack-install-tracks-conflicting-managed-files-as-drift-682ad9b0
title: Pack install tracks conflicting managed files as drift
tags:
- drift
- lock
- pack
scopes:
- kind: command
  raw: loom pack install
  pattern: loom pack install
visibility: shared
status: active
created_at: "2026-02-09T19:42:13Z"
updated_at: "2026-02-09T19:42:13Z"
---

Bug fix: managed-file conflicts during `loom pack install` are now persistent.

Previously:
- If a managed file already existed and differed from the builtin pack file, install would report it as `drifted` but would NOT record it in `.loom/pack/lock.json`.
- As a result, `loom pack status` / `loom pack doctor` (and `loom pack status --diff`) could show zero drift right after an install that reported drift.

Now:
- Install records the pack\x27s expected sha256 for those conflicting managed paths in the lock, while still not overwriting the on-disk file unless `--force`.
- This makes drift visible and diffable immediately after install.

Related: [[20260209193523-inspect-pack-drift-diffs-f02eb23a]]
