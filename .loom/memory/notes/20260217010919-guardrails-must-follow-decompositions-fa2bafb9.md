---
id: 20260217010919-guardrails-must-follow-decompositions-fa2bafb9
title: Guardrails must follow decompositions
visibility: shared
status: active
created_at: "2026-02-17T01:09:19Z"
updated_at: "2026-02-17T01:09:19Z"
---

When splitting hotspot modules in Loom, update architectural guardrail tests in the same change so complexity and line caps follow the new implementation location. This preserves [[20260217010919-guardrail-integrity-b4148167|guardrail integrity]] and prevents accidental [[20260217010919-hotspot-migration-33a9486a|hotspot migration]].

Related: [[[[20260217010919-architecture-guardrails-ffed09fb|architecture guardrails]]]] [[[[20260217010919-workspace-parser-7f6e305d|workspace parser]]]] [[[[20260217010919-refactor-hygiene-8ee3d510|refactor hygiene]]]]
