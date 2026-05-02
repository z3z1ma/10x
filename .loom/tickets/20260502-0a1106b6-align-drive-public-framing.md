---
id: ticket:0a1106b6
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T09:13:27Z
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
    - evidence:public-drive-framing-validation
  critique:
    - critique:public-drive-framing-review
  packet:
    - packet:ralph-ticket-0a1106b6-20260502T090349Z
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
| `initiative:skills-corpus-protocol-sharpening` OBJ-001 | `evidence:public-drive-framing-validation` | `critique:public-drive-framing-review` | supported |
| `research:skills-corpus-council-review#CLAIM-002` | `evidence:skills-corpus-council-review`; `evidence:public-drive-framing-validation` | `critique:public-drive-framing-review` | supported |
| `research:skills-corpus-council-review#CLAIM-003` | `evidence:skills-corpus-council-review`; `evidence:public-drive-framing-validation` | `critique:public-drive-framing-review` | supported |

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

Recorded:

- `evidence:public-drive-framing-validation`
- `git diff --check` passed with no output.
- Targeted searches confirmed `loom-drive` visibility in README and bootstrap
  routing.
- Targeted search confirmed the old linear README outer-loop conveyor no longer
  appears.
- Targeted searches confirmed README distinguishes canonical owner layers from
  packet and memory support surfaces.

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

None remaining. Oracle first reported one README packet-row wording nit; the fixer
resolved it and the final oracle pass returned `pass` with no findings.

Disposition status: complete

Deferral / not-required rationale:

Not deferred. Critique is recorded in `critique:public-drive-framing-review`.

# Wiki Disposition

Deferred intentionally. Retrospective found no separate wiki or research promotion
needed because the accepted explanation was placed directly in the product-facing
README and bootstrap reference. The final integration ticket will still perform a
broader cross-surface review.

# Acceptance Decision

Accepted by: OpenCode parent agent

Accepted at: 2026-05-02T09:13:27Z

Basis: Ralph packet `packet:ralph-ticket-0a1106b6-20260502T090349Z`, validation
evidence `evidence:public-drive-framing-validation`, and final oracle critique
`critique:public-drive-framing-review` with no findings.

Residual risks: Review was scoped to this ticket. Cross-surface final validation
and critique remain owned by `ticket:cdf664af`.

# Dependencies

No hard upstream tickets.

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the first Ralph-sized public-alignment slice.
- 2026-05-02T09:03:49Z: Started Ralph iteration
  `packet:ralph-ticket-0a1106b6-20260502T090349Z` for README/public workflow map
  alignment.
- 2026-05-02T09:13:27Z: Accepted and closed after Ralph implementation, structural
  validation, oracle critique, one resolved nit, and retrospective disposition. No
  ticket-scoped follow-up remains.
