---
id: ticket:drvgram3
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T22:03:13Z
updated_at: 2026-05-02T22:39:44Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-template-grammar-safety-pass
  plan:
    - plan:skills-corpus-template-grammar-safety-pass
  packet:
    - packet:ralph-ticket-drvgram3-20260502T223317Z
  evidence:
    - evidence:drive-handoff-grammar-validation
  critique:
    - critique:drive-handoff-grammar-review
external_refs: {}
depends_on:
  - ticket:pktsupp1
---

# Summary

Document or simplify drive outer-loop handoff metadata so fresh agents do not
guess field semantics.

# Context

Council finding `NC-003` found `source_snapshot`, `drive_checkpoint`, and
`gate_status` in the drive handoff template without reference-level grammar.

# Why Now

Drive handoffs are support artifacts. Their metadata should be legible without
creating hidden schema requirements or packet confusion.

# Scope

- Audit drive outer-loop handoff template and drive continuity/checkpoint
  references.
- Either document the handoff fields or simplify the template to existing shared
  support/source grammar.
- Keep drive handoff metadata support-local, not canonical truth.

# Out Of Scope

- Do not make drive handoffs packets.
- Do not add a schema, runtime, or command wrapper.

# Acceptance Criteria

- ACC-001: Drive handoff metadata fields are documented or removed.
- ACC-002: Field semantics do not conflict with Ralph packet grammar.
- ACC-003: Handoff metadata remains support-local and non-canonical.
- ACC-004: Evidence records handoff metadata searches and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-template-grammar-safety-pass#OBJ-003`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-template-grammar-safety-pass#OBJ-003` | `evidence:drive-handoff-grammar-validation` | `critique:drive-handoff-grammar-review` | supported |
| `ticket:drvgram3#ACC-001` | `evidence:drive-handoff-grammar-validation` | `critique:drive-handoff-grammar-review` | supported |
| `ticket:drvgram3#ACC-002` | `evidence:drive-handoff-grammar-validation` | `critique:drive-handoff-grammar-review` | supported |
| `ticket:drvgram3#ACC-003` | `evidence:drive-handoff-grammar-validation` | `critique:drive-handoff-grammar-review` | supported |
| `ticket:drvgram3#ACC-004` | `evidence:drive-handoff-grammar-validation` | `critique:drive-handoff-grammar-review` | supported |
| `ticket:drvgram3#ACC-005` | `critique:drive-handoff-grammar-review` | oracle critique passed with no findings | supported |

# Execution Notes

Likely touched surfaces include `skills/loom-drive/templates/outer-loop-handoff.md`,
`skills/loom-drive/references/continuity-contract.md`, and
`skills/loom-drive/references/checkpoint-resume-protocol.md`.

# Blockers

None currently. Dependency `ticket:pktsupp1` was closed before this Ralph packet
was compiled.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:pktprov4`.

# Route Readiness

Route: acceptance_review

Acceptance review readiness:
Evidence `evidence:drive-handoff-grammar-validation` and oracle critique
`critique:drive-handoff-grammar-review` support closure with no findings.

# Evidence

Recorded: `evidence:drive-handoff-grammar-validation` with before/after searches
for `source_snapshot`, `drive_checkpoint`, `gate_status`,
`handoff_write_scope`, `outer-loop handoff`, and `packet_kind`, plus
`git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: undocumented support grammar creates recovery ambiguity.

Required critique profiles:

- records-grammar
- owner-boundary
- operator-clarity

Findings:

`critique:drive-handoff-grammar-review` - no findings; mandatory oracle critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Saved drive handoff metadata semantics were promoted directly into
  `skills/loom-drive/templates/outer-loop-handoff.md` and
  `skills/loom-drive/references/continuity-contract.md`.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the drive skill product wording itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
touched drive guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T22:39:44Z
Basis: Ralph packet `packet:ralph-ticket-drvgram3-20260502T223317Z`; evidence
`evidence:drive-handoff-grammar-validation`; oracle critique
`critique:drive-handoff-grammar-review` with no findings.
Residual risks: validation is structural/prose-based; no automated grammar
validator exists or is expected for this Markdown protocol corpus.

# Dependencies

- `ticket:pktsupp1`

# Journal

- 2026-05-02T22:03:13Z: Created from council finding `NC-003`.
- 2026-05-02T22:33:17Z: Compiled Ralph packet
  `packet:ralph-ticket-drvgram3-20260502T223317Z` and moved ticket to `active`.
- 2026-05-02T22:35:01Z: Ralph iteration documented support-local handoff field
  semantics in the drive template/reference, recorded
  `evidence:drive-handoff-grammar-validation`, and moved the ticket to
  `review_required` for mandatory oracle critique.
- 2026-05-02T22:36:53Z: Parent reconciled Ralph output, normalized claim matrix
  statuses to canonical claim-coverage vocabulary, clarified the nested
  `drive_checkpoint.gate_status` reference wording, and marked the Ralph packet
  consumed.
- 2026-05-02T22:39:44Z: Mandatory oracle critique
  `critique:drive-handoff-grammar-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
