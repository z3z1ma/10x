---
id: 20260216153101-team-start-decomposition-pattern-d123011f
title: Team start decomposition pattern
tags:
- architecture
- team
visibility: shared
status: active
created_at: "2026-02-16T15:31:01Z"
updated_at: "2026-02-16T15:31:01Z"
---

For [[20260216153101-team-orchestration-818eb728|team orchestration]], the maintainable extraction pattern is: keep start() as orchestration glue and move lock-scoped run-state mutation, run creation defaults, ticket/agent bootstrap, and manager session bootstrapping into focused helpers with explicit inputs/outputs. This preserves behavior while making high-risk lifecycle code easier to test and evolve incrementally.

Related: [[[[20260216153101-team-orchestration-818eb728|team orchestration]]]] [[[[20260216083521-cli-cohesion-42b76bb6|CLI cohesion]]]]
