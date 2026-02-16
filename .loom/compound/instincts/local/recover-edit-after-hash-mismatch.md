---
id: recover-edit-after-hash-mismatch
title: Recover Edit operations after LINE:HASH mismatch
trigger: When Edit reports lines changed since last read or asks for updated LINE:HASH anchors
confidence: 0.8000
status: active
domain: workflow
source: local
created_at: 2026-02-15T21:05:27.994617Z
updated_at: 2026-02-15T23:42:09.148457Z
tags: workflow, editing, concurrency, recovery
notes: Another mismatch-then-retry sequence in this run confirms anchor refresh before retry is a durable recovery pattern.
---

## Action
On Edit hash-mismatch failure, stop mutation flow, re-read the affected region to obtain fresh LINE:HASH anchors, then retry a minimal targeted edit with updated anchors.

## Evidence
- ts=2026-02-15T20:56:59.440111Z source_id=obs-edit-hash-205659 source_hash=edit-failed-lines-changed-since-last-read
- ts=2026-02-15T20:57:02.378747Z source_id=obs-edit-retry-205702 source_hash=edit-success-after-mismatch
- ts=2026-02-15T21:05:04.359273Z source_id=obs-edit-hash-210504 source_hash=edit-failed-1-line-changed-since-last-read
- ts=2026-02-15T21:05:07.869005Z source_id=obs-read-refresh-210507 source_hash=read-refresh-anchors
- ts=2026-02-15T21:05:11.218783Z source_id=obs-edit-retry-210511 source_hash=edit-success-after-anchor-refresh
- ts=2026-02-15T23:41:02.511079Z source_id=obs-edit-hash-234102 source_hash=edit-failed-1-line-changed-since-last-read
- ts=2026-02-15T23:41:04.842819Z source_id=obs-edit-retry-234104 source_hash=edit-success-after-updated-anchors

## Notes
Another mismatch-then-retry sequence in this run confirms anchor refresh before retry is a durable recovery pattern.
