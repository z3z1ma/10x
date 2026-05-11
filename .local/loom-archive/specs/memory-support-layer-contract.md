---
id: spec:memory-support-layer-contract
kind: spec
status: active
created_at: 2026-04-30T08:22:13Z
updated_at: 2026-04-30T08:31:09Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:sharpen-memory-support-layer
  ticket:
    - ticket:329erym3
  evidence:
    - evidence:memory-support-layer-validation
  critique:
    - critique:memory-support-layer-review
external_refs: {}
---

# Summary

This spec defines Loom memory as an optional support layer for recall and
retrieval cues, not a canonical project-truth owner.

# Problem

The rest of Loom's layers are concrete enough that an agent can usually route a
fact quickly. Memory is currently described mostly by negatives: optional,
support-only, and not canonical truth. That protects the owner model, but it does
not teach when memory is valuable or how to use it without creating shadow state.

# Desired Behavior

The product should teach memory as a lightweight continuity surface. Memory is
useful when a small support fact helps the next operator orient faster but would
overstate, clutter, or distort the canonical layers if promoted too early.

Optionality means Loom must remain correct when memory is absent, stale, or
pruned. It does not mean memory is useless. Good memory reduces rediscovery cost
without changing what the project is, what it intends, what is happening now, or
what has been proven.

# Constraints

- Memory must remain durable but non-canonical.
- Memory must not own live execution state, acceptance, evidence, critique,
  intended behavior, sequencing, strategy, explanation, or policy.
- Memory must be safe to delete after useful facts are promoted or become stale.
- Memory must remain Markdown-native and script-free.
- Memory must not require a database, indexer, embedding service, daemon, or
  harness-specific runtime.

# Requirements

- REQ-001: Memory guidance must define optionality as a correctness boundary:
  memory is allowed to help, but canonical Loom records must remain sufficient
  for truth and resumption.
- REQ-002: Memory guidance must name positive use cases: retrieval cues, hot
  context, operator or user preferences, recurring entities, support
  observations, and support-only reminders.
- REQ-003: Memory guidance must distinguish memory from tickets, wiki, research,
  evidence, specs, plans, initiatives, constitution, and packets.
- REQ-004: Memory guidance must provide promotion triggers for facts that become
  canonical project truth or repeated reusable explanation.
- REQ-005: Memory guidance must provide pruning and retrieval discipline so the
  layer stays small, linked, and safe to ignore when not relevant.

# Scenarios

- A user preference such as "prefer concise handoff summaries" belongs in memory
  unless it becomes a project constraint that the constitution should own.
- A note that `ticket:abc12345` is the current blocker does not belong in memory;
  the ticket owns blockers and live state.
- A recurring label for an external service can live in entities memory when it
  helps retrieval, while any accepted architecture explanation belongs in wiki.
- A dated observation that may help a future operator can start in observations
  memory, but if it supports acceptance or critique it must become evidence.
- A support reminder can live in memory action items only while it is not scoped
  Loom work; once scoped, it needs a ticket.

# Acceptance

- ACC-001: `skills/loom-memory/SKILL.md` explains memory's positive job, its
  optionality boundary, and the deletion/promote test.
- ACC-002: `skills/loom-memory/references/memory-model.md` includes concrete
  fit tests, examples, and a layer-difference guide.
- ACC-003: `skills/loom-memory/references/retrieval.md` explains progressive
  loading and forbids answering owner-truth questions from memory alone.
- ACC-004: `skills/loom-memory/references/housekeeping.md` explains pruning,
  promotion, stale handling, and action-item boundaries.
- ACC-005: Templates and summary surfaces that define memory shapes or layer
  roles use language compatible with this spec and do not reduce memory to vague
  optional scratch space.
- ACC-006: The implementation preserves the no-runtime, no-new-canonical-layer,
  and no-second-ledger constraints.

# Open Questions

- Whether a later golden example should show memory item promotion into wiki,
  evidence, or tickets after this first product-surface sharpening lands.
