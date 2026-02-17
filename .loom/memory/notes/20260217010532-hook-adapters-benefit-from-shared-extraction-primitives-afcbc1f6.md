---
id: 20260217010532-hook-adapters-benefit-from-shared-extraction-primitives-afcbc1f6
title: Hook adapters benefit from shared extraction primitives
visibility: shared
status: active
created_at: "2026-02-17T01:05:32Z"
updated_at: "2026-02-17T01:05:32Z"
---

In [[20260216165029-loom-compound-947b083c|Loom Compound]], adapter payload normalization should share extractor primitives for session/tool/input/output/outcome fields while preserving adapter-specific event and prompt semantics. This reduces drift between adapters and improves [[20260217010532-consistency-by-construction-5545b5bf|consistency by construction]] for multi-harness observation capture.

Related: [[[[20260217010532-hook-adapters-25c81996|hook adapters]]]] [[[[20260217010532-normalization-pipeline-7c7a18c0|normalization pipeline]]]] [[[[20260217010532-deduplication-34bd18fb|deduplication]]]]
