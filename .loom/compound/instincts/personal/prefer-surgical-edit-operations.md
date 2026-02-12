---
id: prefer-surgical-edit-operations
title: Prefer surgical edit operations over broad rewrites
trigger: When modifying existing files with Edit/Write and the change is logically small-to-medium
confidence: 0.6800
status: active
domain: workflow
source: personal
created_at: 2026-02-13T19:10:38.159235Z
updated_at: 2026-02-13T19:10:38.159235Z
tags: workflow, editing, safety, diff-quality
notes: Repeated large-span edit warnings in one change stream indicate elevated unintended-reformatting risk; smaller targeted edits reduce drift and make intent auditable.
---

## Action
Use narrow, hash-anchored edits at the smallest logical locus; avoid whole-file or very large block replacements unless the intent is genuinely full-file replacement.

## Evidence
- ts=2026-02-13T18:14:05.898502Z source_id=obs-edit-181405 source_hash=edit-warning-410-lines
- ts=2026-02-13T18:14:19.887469Z source_id=obs-edit-181419 source_hash=edit-warning-283-lines
- ts=2026-02-13T18:14:30.131879Z source_id=obs-edit-181430 source_hash=edit-warning-448-lines

## Notes
Repeated large-span edit warnings in one change stream indicate elevated unintended-reformatting risk; smaller targeted edits reduce drift and make intent auditable.
