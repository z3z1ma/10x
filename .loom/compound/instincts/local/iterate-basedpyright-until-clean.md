---
id: iterate-basedpyright-until-clean
title: Iterate on type errors until basedpyright is clean
trigger: After semantic edits in typed Python modules when `uv run basedpyright` reports errors
confidence: 0.6800
status: active
domain: testing
source: local
created_at: 2026-02-16T00:22:16.771339Z
updated_at: 2026-02-16T00:22:16.771339Z
tags: testing, type-checking, basedpyright, debugging, iteration
notes: This run shows a clear fail-fix-recheck loop for type safety rather than deferring unresolved type issues.
---

## Action
When basedpyright fails, inspect reported locations, apply targeted edits, and re-run `uv run basedpyright` in a tight loop until it reports zero errors before moving to downstream gates.

## Evidence
- ts=2026-02-16T00:20:19.100036Z source_id=obs-pyright-fail-002019 source_hash=uv-run-basedpyright-fail
- ts=2026-02-16T00:21:01.362943Z source_id=obs-pyright-fail-002101 source_hash=uv-run-basedpyright-fail
- ts=2026-02-16T00:21:18.252116Z source_id=obs-pyright-fail-002118 source_hash=uv-run-basedpyright-fail
- ts=2026-02-16T00:21:40.719491Z source_id=obs-pyright-fail-002140 source_hash=uv-run-basedpyright-fail
- ts=2026-02-16T00:22:07.544781Z source_id=obs-pyright-pass-002207 source_hash=uv-run-basedpyright-zero-errors

## Notes
This run shows a clear fail-fix-recheck loop for type safety rather than deferring unresolved type issues.
