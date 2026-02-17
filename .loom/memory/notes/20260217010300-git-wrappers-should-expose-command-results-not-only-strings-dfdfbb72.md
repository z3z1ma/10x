---
id: 20260217010300-git-wrappers-should-expose-command-results-not-only-strings-dfdfbb72
title: Git wrappers should expose command results, not only strings
visibility: shared
status: active
created_at: "2026-02-17T01:03:00Z"
updated_at: "2026-02-17T01:03:00Z"
---

In [[20260216165029-loom-core-0720b53e|Loom Core]], git lookup helpers should return typed command results with stdout/stderr/returncode context so callers can make explicit decisions without relying on empty-string fallbacks. This improves [[20260217010300-failure-diagnostics-a5de5598|failure diagnostics]] and supports clearer [[20260217005244-error-contracts-8c70bded|error contracts]] across ticket/workspace flows.

Related: [[[[20260217010300-git-wrappers-2589ccf4|git wrappers]]]] [[[[20260217010300-result-objects-70c19ccd|result objects]]]] [[[[20260217010300-observability-d3e1afcf|observability]]]]
