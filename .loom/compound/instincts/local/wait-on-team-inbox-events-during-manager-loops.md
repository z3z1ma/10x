---
id: wait-on-team-inbox-events-during-manager-loops
title: Wait on team inbox events during manager loops
trigger: When managing active team runs and expecting asynchronous worker responses
confidence: 0.7700
status: active
domain: workflow
source: local
created_at: 2026-02-15T23:49:19.074072Z
updated_at: 2026-02-16T00:07:15.797505Z
tags: workflow, team, wait, orchestration, efficiency
notes: This reduces busy polling while still keeping manager response latency low after worker updates arrive.
---

## Action
Use `loom team wait <team>` to block for inbox activity, then immediately inspect `loom team inbox <team>` to process and acknowledge resulting messages.

## Evidence
- ts=2026-02-15T23:42:58.315960Z source_id=obs-team-wait-234258 source_hash=loom-team-wait-awake
- ts=2026-02-15T23:48:36.538550Z source_id=obs-team-wait-234836 source_hash=loom-team-wait-awake
- ts=2026-02-15T23:55:45.180603Z source_id=obs-team-wait-235545 source_hash=loom-team-wait-awake-manager
- ts=2026-02-16T00:01:04.383373Z source_id=obs-team-wait-000104 source_hash=loom-team-wait-awake-manager-round2
- ts=2026-02-16T00:05:51.927466Z source_id=obs-team-wait-000551 source_hash=loom-team-wait-awake-integrator

## Notes
This reduces busy polling while still keeping manager response latency low after worker updates arrive.
