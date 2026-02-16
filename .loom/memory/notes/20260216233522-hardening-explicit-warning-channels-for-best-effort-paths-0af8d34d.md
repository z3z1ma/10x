---
id: 20260216233522-hardening-explicit-warning-channels-for-best-effort-paths-0af8d34d
title: "Hardening: explicit warning channels for best-effort paths"
tags:
- architecture
- reliability
visibility: shared
status: active
created_at: "2026-02-16T23:35:22Z"
updated_at: "2026-02-16T23:35:22Z"
---

When refactoring lifecycle code, convert silent best-effort exceptions into structured warnings instead of swallowing failures. This was effective in sidecar/process-control and workspace cleanup paths: preserve primary behavior while surfacing recoverable issues to operators. Use additive outputs like warnings arrays and structured events (e.g., sidecar.warning) so callers can keep compatibility while gaining observability. Relevant concepts: [[20260216233522-best-effort-semantics-cc9ea17f|best-effort semantics]], [[20260216233522-typed-error-boundaries-a7ae55f1|typed error boundaries]], [[20260216233522-operational-observability-c5bca2be|operational observability]], [[20260216233522-behavior-stable-refactor-ff3ee4c3|behavior-stable refactor]].
