---
id: recover-edit-after-hash-mismatch
title: Recover Edit operations after LINE:HASH mismatch
trigger: When Edit reports lines changed since last read or asks for updated LINE:HASH anchors
confidence: 0.8300
status: active
domain: workflow
source: local
created_at: 2026-02-15T21:05:27.994617Z
updated_at: 2026-02-16T00:22:16.771339Z
tags: workflow, editing, concurrency, recovery
notes: The same recovery loop happened twice in this run with identical sequencing and successful retries.
---

## Action
On Edit hash-mismatch failure, stop mutation flow, re-read the affected region to obtain fresh LINE:HASH anchors, then retry a minimal targeted edit with updated anchors.

## Evidence
- ts=2026-02-16T00:17:36.055560Z source_id=obs-edit-hash-001736 source_hash=edit-failed-1-line-changed-since-last-read
- ts=2026-02-16T00:17:38.507900Z source_id=obs-read-refresh-001738 source_hash=read-refresh-anchors
- ts=2026-02-16T00:17:43.277216Z source_id=obs-edit-retry-001743 source_hash=edit-success-after-anchor-refresh
- ts=2026-02-16T00:19:46.287262Z source_id=obs-edit-hash-001946 source_hash=edit-failed-1-line-changed-since-last-read
- ts=2026-02-16T00:19:48.383729Z source_id=obs-read-refresh-001948 source_hash=read-refresh-anchors
- ts=2026-02-16T00:19:50.318795Z source_id=obs-edit-retry-001950 source_hash=edit-success-after-anchor-refresh

## Notes
The same recovery loop happened twice in this run with identical sequencing and successful retries.
