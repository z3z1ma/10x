---
id: ticket:revtgt7x
kind: ticket
status: closed
change_class: record-hygiene
risk_class: medium
created_at: 2026-05-02T18:58:43Z
updated_at: 2026-05-02T20:35:22Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  packet:
    - packet:ralph-ticket-revtgt7x-20260502T201800Z
    - packet:ralph-ticket-revtgt7x-20260502T202813Z
  evidence:
    - evidence:review-target-shape-validation
  critique:
    - critique:review-target-shape-review
    - critique:review-target-shape-rereview
external_refs: {}
depends_on:
  - ticket:pktlife6
---

# Summary

Canonicalize or explicitly document `review_target` shape across critique records
and critique packets.

# Context

Council finding `CR-007` found `review_target` appears as a scalar in critique
records and a mapping in critique packets.

# Why Now

Shared fields should be grep-friendly and validation-friendly without requiring a
runtime parser.

# Scope

- Decide whether `review_target` is one canonical shape or two explicitly allowed
  variants.
- Update critique templates and frontmatter grammar accordingly.
- Preserve usability for direct artifact critique and packetized critique.

# Out Of Scope

- Do not bulk-normalize every historical critique record unless necessary.
- Do not add schema validation.
- Do not change critique ownership.

# Acceptance Criteria

- ACC-001: `review_target` grammar is explicit in shared frontmatter or critique
  references.
- ACC-002: Critique record and critique packet templates align with that grammar.
- ACC-003: The chosen shape remains easy to grep and human-read.
- ACC-004: Evidence records before/after `review_target` searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-council-precision-pass#OBJ-007`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-council-precision-pass#OBJ-007` | `evidence:review-target-shape-validation` | `critique:review-target-shape-rereview` | supported |
| `ticket:revtgt7x#ACC-001` | `evidence:review-target-shape-validation` | `critique:review-target-shape-rereview` | supported |
| `ticket:revtgt7x#ACC-002` | `evidence:review-target-shape-validation` | `critique:review-target-shape-rereview` | supported |
| `ticket:revtgt7x#ACC-003` | `evidence:review-target-shape-validation` | `critique:review-target-shape-rereview` | supported |
| `ticket:revtgt7x#ACC-004` | `evidence:review-target-shape-validation` | `critique:review-target-shape-rereview` | supported |
| `ticket:revtgt7x#ACC-005` | `critique:review-target-shape-rereview` | oracle re-critique passed with no findings | supported |

# Execution Notes

Ralph iteration `packet:ralph-ticket-revtgt7x-20260502T201800Z` aligned direct
critique record and critique packet `review_target` grammar across critique and
frontmatter guidance.

Mandatory oracle critique found `REVTGT7X-CRIT-001`: the critique-packet grammar
must not retroactively invalidate older consumed critique packets. Repair
iteration `packet:ralph-ticket-revtgt7x-20260502T202813Z` is scoped to add the
legacy compatibility boundary and refresh evidence.

Repair iteration `packet:ralph-ticket-revtgt7x-20260502T202813Z` added a concise
legacy compatibility boundary for older consumed critique packets that only carry
`review_target.kind` plus `review_target.diff`, refreshed targeted evidence, and
left ticket acceptance pending mandatory oracle re-critique.

# Blockers

None - `ticket:pktlife6` is closed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:tmplph8x`.

# Route Readiness

Route: acceptance_review

Acceptance review readiness:
Evidence `evidence:review-target-shape-validation` and oracle re-critique
`critique:review-target-shape-rereview` support closure. Prior finding
`critique:review-target-shape-review#REVTGT7X-CRIT-001` is resolved by the
legacy compatibility repair.

# Evidence

Recorded in `evidence:review-target-shape-validation`:

- before/after `review_target`, `Review Target`, and `review target` searches
- repair compatibility wording and targeted historical critique packet observation
- `git diff --check`

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: user requires oracle critique for every ticket; shared fields
affect record grammar.

Required critique profiles:

- records-grammar
- operator-clarity

Findings:

- `critique:review-target-shape-review#REVTGT7X-CRIT-001` - medium; repair
  applied and resolved by `critique:review-target-shape-rereview`.
- `critique:review-target-shape-rereview` - no findings.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle re-critique passed with no findings.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Direct critique record scalar `review_target` grammar and critique packet
  structured `review_target` grammar were promoted into
  `skills/loom-critique/templates/critique.md`,
  `skills/loom-critique/templates/critique-packet.md`,
  `skills/loom-critique/SKILL.md`,
  `skills/loom-critique/references/critique-lens.md`,
  `skills/loom-records/references/frontmatter.md`, and
  `skills/loom-records/references/packet-frontmatter.md`.
- The compatibility lesson from `REVTGT7X-CRIT-001` was promoted into
  `skills/loom-records/references/packet-frontmatter.md` and reinforced in the
  critique packet template.

Deferred / not-required rationale:

Not deferred. The durable lesson was promoted directly into the owner product
surfaces listed above; no separate wiki page, research record, spec,
constitution decision, or memory entry is needed.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation is now in the
critique/frontmatter owner surfaces.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T20:35:22Z
Basis: Ralph packets `packet:ralph-ticket-revtgt7x-20260502T201800Z` and
`packet:ralph-ticket-revtgt7x-20260502T202813Z`; evidence
`evidence:review-target-shape-validation`; critique
`critique:review-target-shape-review` resolved by oracle re-critique
`critique:review-target-shape-rereview` with no findings.
Residual risks: `records-grammar` remains a ticket-requested lens rather than a
separately listed named profile; oracle re-critique treated this as non-blocking
pre-existing usage.

# Dependencies

- `ticket:pktlife6`

# Journal

- 2026-05-02T18:58:43Z: Created from council finding `CR-007`.
- 2026-05-02T20:18:00Z: Started Ralph iteration
  `packet:ralph-ticket-revtgt7x-20260502T201800Z` from baseline
  `b7c076f5105c2c241ac3b7ec932eb6f8a165c86f`.
- 2026-05-02T20:19:52Z: Ralph iteration completed grammar/template updates and
  moved ticket to `review_required`; evidence recorded in
  `evidence:review-target-shape-validation`. Mandatory oracle critique remains
  pending.
- 2026-05-02T20:27:44Z: Mandatory oracle critique recorded
  `critique:review-target-shape-review` with `changes_required` finding
  `REVTGT7X-CRIT-001`.
- 2026-05-02T20:28:13Z: Compiled repair Ralph iteration
  `packet:ralph-ticket-revtgt7x-20260502T202813Z` to add a legacy compatibility
  boundary and refresh evidence.
- 2026-05-02T20:30:02Z: Repair iteration added the legacy compatibility boundary,
  refreshed evidence, and moved the ticket to `review_required` for mandatory
  oracle re-critique.
- 2026-05-02T20:35:22Z: Oracle re-critique passed with no findings, resolved
  `REVTGT7X-CRIT-001`, recorded retrospective / promotion disposition, and
  closed the ticket.
