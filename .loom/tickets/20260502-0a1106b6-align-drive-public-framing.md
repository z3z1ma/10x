---
id: ticket:0a1106b6
kind: ticket
status: ready
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T08:46:28Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  roadmap:
    - roadmap:bootstrap-the-markdown-first-protocol-corpus
  initiative:
    - initiative:skills-corpus-protocol-sharpening
  research:
    - research:skills-corpus-council-review
  evidence:
    - evidence:skills-corpus-council-review
  plan:
    - plan:skills-corpus-protocol-sharpening
  supersedes:
    - ticket:3uv5l5fh
external_refs: {}
depends_on: []
---

# Summary

Align public and bootstrap-facing skill maps with the actual shipped Loom skill
surface, especially `loom-drive`, and correct README framing that can make Loom's
outer loop look like a single linear sequence.

# Context

The council found low-risk but important drift: `loom-drive` exists as a shipped
workflow skill but is missing from README skill-map surfaces, and README's outer
loop diagram can be read as a linear sequence from research through memory rather
than a backbone plus conditional routes.

This ticket handles only the first alignment slice. It should make public framing
and bootstrap-adjacent routing agree with the corpus without changing shared
record grammar, packet semantics, or ticket acceptance rules.

# Why Now

This is the safest first Ralph-sized slice because downstream grammar and
workflow tickets should inherit a public map that names the correct shipped skill
surface and does not mis-teach the basic Loom route.

# Scope

- Add `loom-drive` anywhere the product enumerates shipped workflow skills and it
  is currently missing.
- Inspect and update `README.md`, `PROTOCOL.md`, and `ARCHITECTURE.md` only where
  they enumerate Loom skills or summarize the workflow map.
- Inspect `skills/loom-bootstrap/**` for routing summaries that should mention
  `loom-drive` as a workflow coordinator.
- Reconcile README outer-loop wording so it distinguishes the backbone,
  conditional research/spec strengthening, follow-through routes, packet support,
  and memory support.
- Preserve README's product clarity without letting README outrank bootstrap
  doctrine.

# Non-goals

- Do not edit shared claim coverage, packet, or ticket grammar in this slice.
- Do not restructure `loom-drive` itself beyond small route-summary alignment if
  needed.
- Do not add new concepts or workflow layers.
- Do not update examples unless a direct public-surface statement points at them
  incorrectly.

# Acceptance Criteria

- ACC-001: `loom-drive` appears in README and any touched public skill maps that
  enumerate shipped workflow skills.
- ACC-002: `loom-drive` is described as an objective/workflow coordinator that
  routes through owner layers and does not own project truth.
- ACC-003: README no longer presents the outer loop as one linear
  research-to-memory conveyor that conflicts with bootstrap doctrine.
- ACC-004: Any touched top-level docs distinguish canonical owner layers from
  support surfaces such as packets and memory.
- ACC-005: Bootstrap-adjacent routing references, if edited, remain consistent
  with mandatory bootstrap authority and local-work nuance.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening` OBJ-001
- `research:skills-corpus-council-review#CLAIM-002`
- `research:skills-corpus-council-review#CLAIM-003`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening` OBJ-001 | implementation evidence pending | critique recommended | open |
| `research:skills-corpus-council-review#CLAIM-002` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | critique recommended | supported_pending_review |
| `research:skills-corpus-council-review#CLAIM-003` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | critique recommended | supported_pending_review |

# Execution Notes

This is the first implementation ticket under
`plan:skills-corpus-protocol-sharpening`. Keep the diff narrow and avoid using
this slice to fix every wording issue discovered nearby.

# Blockers

None.

# Next Move / Next Route

Ralph implementation packet or local edit. Ralph is preferred if a fresh worker
is available because the write boundary is clear and this ticket seeds later
dependent work.

# Ralph Readiness

Bounded iteration:

Align `loom-drive` visibility and README/public outer-loop framing.

Write boundary:

- `README.md`
- `PROTOCOL.md`
- `ARCHITECTURE.md`
- `skills/loom-bootstrap/**`
- direct skill-map references only if discovered during the slice

Likely verification posture:

Observation-first structural validation.

Expected output contract:

- changed files,
- exact `rg` queries used to verify `loom-drive` visibility and outer-loop wording,
- any public-surface drift intentionally deferred to later tickets.

# Evidence

Expected:

- `git diff --check`
- targeted `rg` checks for `loom-drive`, outer-loop wording, packets, and memory
- diff review showing no shared grammar or packet contract changes landed here

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:

This changes public protocol framing but should not alter record grammar or
acceptance semantics. The final integration ticket still requires mandatory
critique.

Required critique profiles:

- operator-clarity
- protocol-change if bootstrap doctrine changes materially

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None yet.

# Wiki Disposition

Likely deferred. This ticket should improve product-facing instructions directly;
wiki promotion is only needed if the framing decision needs a reusable project
explanation beyond the skill/docs text.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

No hard upstream tickets.

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the first Ralph-sized public-alignment slice.
