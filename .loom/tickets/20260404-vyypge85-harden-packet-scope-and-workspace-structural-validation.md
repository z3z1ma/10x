---
id: ticket:vyypge85
kind: ticket
status: proposed
created_at: 2026-04-04T23:57:49Z
updated_at: 2026-04-17T23:58:42Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:prove-core-loom-workflow
  plan:
    - plan:bootstrap-core-workflow-backlog
  spec:
    - spec:minimum-proven-core-workflow-surface
  ticket:
    - ticket:1ypcbj0m
depends_on:
  - ticket:1ypcbj0m
---

# Summary

Tighten structural validation guidance, packet/scope diagnostics, and query
recipes around packet shape, scope, and canonical link integrity based on the
concrete failures or ambiguities exposed by the proved workflow path.

# Context

This repository has no conventional test suite. Structural validation,
diagnostics, and record integrity checks are the main guardrails.

The rewrite removed shipped helper scripts from the core bundle, so the next
validation work should sharpen visible rules, references, templates, and query
recipes where `ticket:1ypcbj0m` reveals real gaps instead of rebuilding a hidden
helper layer.

# Why Now

Validation guidance is most useful after one real workflow slice has been
exercised. Without that proof, hardening work would risk teaching the wrong
checks or overfitting to imagined failures.

# Scope

- review packet, scope, and workspace guidance against the exercised proof flow
- sharpen visible validation checklists and query recipes for existing doctrine
  requirements only
- improve diagnostics wording where current failures are hard to interpret
- update the smallest set of rules, skill references, templates, or wrapper
  prompts needed to keep operator expectations truthful

# Non-goals

- do not invent hidden ontology or acceptance scoring
- do not widen scope-resolution heuristics past fail-closed behavior
- do not fold unrelated cleanup into this ticket
- do not reintroduce bundled validation scripts as part of the core package
- do not turn validation into a monolithic test runner

# Acceptance Criteria

- packet and scope guidance catches missing doctrine-required data more clearly
- workspace diagnostics and/or query recipes make ambiguous ownership failures
  easier to interpret
- canonical record and link checks remain clean for the backlog chain and any
  proof-flow artifacts
- any stricter checks that affect operator expectations are reflected in the
  visible rules, references, templates, or wrappers that own those expectations

# Execution Notes

1. Review the proof-flow evidence from `ticket:1ypcbj0m` and note structural
   failure modes or ambiguities.
2. Map each candidate hardening change back to existing doctrine.
3. Implement the smallest guidance and messaging changes that close those gaps.
4. Re-run the smallest honest structural/manual validation for the touched
   surfaces.
5. Reconcile the ticket truthfully.

# Evidence

No validation hardening evidence exists yet.

Expected evidence for this ticket includes:

- diffs to the rules, skill references, templates, or optional wrappers that
  now describe the exercised failures more clearly
- targeted `rg` or manual checks showing that links, packet requirements, and
  scope guidance remain coherent after the changes
- a truthful ticket journal describing which concrete failure modes this ticket
  actually hardened

# Critique Disposition

Critique is recommended if the hardening materially changes operator judgment,
required packet fields, or the expected validation posture.

# Wiki Disposition

Wiki follow-through is not expected unless this ticket produces a reusable
workflow explanation that belongs in the canonical wiki rather than only in the
rules or skill references.

# Dependencies

- `ticket:1ypcbj0m` should provide the main evidence for what to harden
- `ticket:zomng8h3` may reveal additional operator-facing ambiguity if wrapper
  prompts remain in scope
- the relevant rules and skill references that already own packet, scope, and
  validation doctrine

# Journal

- 2026-04-04: created `ticket:vyypge85` as the proposed hardening slice for
  packet, scope, and workspace validation after the first real workflow proof
  run.
- 2026-04-17: reconciled the ticket to the rewrite-era model where validation
  hardening happens in visible guidance and query recipes rather than in a core
  helper-script layer.
