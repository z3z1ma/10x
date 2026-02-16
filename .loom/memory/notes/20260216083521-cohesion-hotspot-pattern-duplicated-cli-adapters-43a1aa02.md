---
id: 20260216083521-cohesion-hotspot-pattern-duplicated-cli-adapters-43a1aa02
title: "Cohesion hotspot pattern: duplicated CLI adapters"
tags:
- architecture
- cli
visibility: shared
status: active
created_at: "2026-02-16T08:35:21Z"
updated_at: "2026-02-16T08:35:21Z"
---

Observed recurring duplication across Loom CLIs: repeated JSON envelope helpers in team command modules, repeated argv normalization scaffolding across ticket/memory/team, and workspace command modules importing presentation helpers from workspace CLI internals. Prefer shared primitives in [[20260216083521-cli-cohesion-42b76bb6|CLI cohesion]] and explicit presentation modules in [[20260216083521-workspace-boundaries-8c6a6cb1|workspace boundaries]] to keep command handlers thin and composable.

Related: [[[[20260216083521-cli-cohesion-42b76bb6|CLI cohesion]]]] [[[[20260216083521-workspace-boundaries-8c6a6cb1|workspace boundaries]]]] [[[[20260216083521-team-output-contracts-62cd692b|team output contracts]]]]
