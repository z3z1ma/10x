---
id: prefer-surgical-edit-operations
title: Prefer surgical edit operations over broad rewrites
trigger: When modifying existing files with Edit/Write and the change is logically small-to-medium
confidence: 0.9000
status: active
domain: workflow
source: local
created_at: 2026-02-13T19:10:38.159235Z
updated_at: 2026-02-15T23:50:38.827061Z
tags: workflow, editing, safety, diff-quality
notes: Even mid-sized single-operation replacements repeatedly trigger warning signals, so surgical edits remain the safer default.
---

## Action
Use narrow, hash-anchored edits at the smallest logical locus; avoid whole-file or large-block replacements unless the intent is true full-file replacement.

## Evidence
- ts=2026-02-15T23:42:38.686011Z source_id=obs-edit-234238 source_hash=edit-warning-282-lines-1-op
- ts=2026-02-15T23:42:50.646639Z source_id=obs-edit-234250 source_hash=edit-warning-66-lines-1-op
- ts=2026-02-15T23:48:53.126364Z source_id=obs-edit-234853 source_hash=edit-warning-65-lines-1-op
- ts=2026-02-15T23:49:43.357551Z source_id=obs-write-234943 source_hash=write-10795-bytes-test-file
- ts=2026-02-15T23:49:54.212706Z source_id=obs-edit-234954 source_hash=edit-warning-376-lines-1-op

## Notes
Even mid-sized single-operation replacements repeatedly trigger warning signals, so surgical edits remain the safer default.
