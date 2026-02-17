---
id: 20260217015632-memory-cli-hotspot-migration-guardrail-72689d4a
title: Memory CLI hotspot migration guardrail
tags:
- architecture
- guardrail
visibility: shared
status: active
created_at: "2026-02-17T01:56:32Z"
updated_at: "2026-02-17T01:56:32Z"
---

Refactoring pattern for large CLI modules: keep  as a stable shim while moving full implementation to , then move guardrail hotspot tracking to the new implementation file so complexity cannot hide behind shims. This preserves import stability while enabling phased decomposition. Related concepts: [[20260217015632-memory-cli-52a58d8c|memory-cli]], [[20260217010919-architecture-guardrails-ffed09fb|architecture-guardrails]], [[20260217015632-shim-boundaries-7b53ab6a|shim-boundaries]], [[20260216233522-behavior-stable-refactor-ff3ee4c3|behavior-stable-refactor]].
