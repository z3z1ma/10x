---
id: ticket:evshape9
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T18:58:43Z
updated_at: 2026-05-02T20:54:00Z
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
    - packet:ralph-ticket-evshape9-20260502T204732Z
  evidence:
    - evidence:evidence-quality-guidance-validation
  critique:
    - critique:evidence-quality-guidance-review
external_refs: {}
depends_on:
  - ticket:retrod3p
---

# Summary

Strengthen evidence quality guidance and ticket evidence teaching.

# Context

Council finding `CR-009` found evidence records carry acceptance weight but lack a
dedicated evidence-shape/quality reference covering freshness, scope, limitations,
and support/challenge strength.

# Why Now

Tickets and critique rely on evidence. Evidence should be inspectable without
overclaiming.

# Scope

- Add or expand evidence quality guidance under `loom-evidence`.
- Teach freshness, environment, observed result, limitations, support/challenge,
  invalidation/supersession, and change-class expectations.
- Expand ticket evidence examples or references where acceptance depends on
  evidence sufficiency.

# Out Of Scope

- Do not create an evidence schema runtime.
- Do not make evidence own acceptance or critique verdicts.
- Do not require heavy evidence for trivial local edits.

# Acceptance Criteria

- ACC-001: Evidence skill has dedicated evidence-quality guidance.
- ACC-002: Ticket evidence teaching links evidence sufficiency to acceptance
  without making evidence the owner of closure.
- ACC-003: Guidance distinguishes observed artifacts, inference, limitations,
  freshness, invalidation, and supersession.
- ACC-004: Evidence records before/after evidence-quality searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-council-precision-pass#OBJ-009`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-council-precision-pass#OBJ-009` | `evidence:evidence-quality-guidance-validation` supports structural guidance update | `critique:evidence-quality-guidance-review` | supported |
| `ticket:evshape9#ACC-001` | `evidence:evidence-quality-guidance-validation` supports dedicated evidence-quality guidance | `critique:evidence-quality-guidance-review` | supported |
| `ticket:evshape9#ACC-002` | `evidence:evidence-quality-guidance-validation` supports ticket evidence sufficiency teaching | `critique:evidence-quality-guidance-review` | supported |
| `ticket:evshape9#ACC-003` | `evidence:evidence-quality-guidance-validation` supports observed/inference, limitations, freshness, invalidation, and supersession coverage | `critique:evidence-quality-guidance-review` | supported |
| `ticket:evshape9#ACC-004` | `evidence:evidence-quality-guidance-validation` records before/after searches and `git diff --check` | `critique:evidence-quality-guidance-review` | supported |
| `ticket:evshape9#ACC-005` | `critique:evidence-quality-guidance-review` | oracle critique passed with no findings | supported |

# Execution Notes

Touched surfaces include `skills/loom-evidence/SKILL.md`,
`skills/loom-evidence/references/evidence-quality.md`, the evidence template,
ticket evidence teaching, and acceptance gate references.

Ralph iteration `packet:ralph-ticket-evshape9-20260502T204732Z` is scoped to add
evidence quality guidance and ticket evidence sufficiency teaching.

# Blockers

None - `ticket:retrod3p` is closed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:dwhand10`.

# Route Readiness

Route: acceptance_review

Acceptance review readiness:
Evidence `evidence:evidence-quality-guidance-validation` and oracle critique
`critique:evidence-quality-guidance-review` support closure with no findings.

# Evidence

Observed: `evidence:evidence-quality-guidance-validation` records before/after
searches for evidence freshness, limitations, observed/inference,
support/challenge, invalidation/supersession, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: user requires oracle critique; evidence quality affects
acceptance honesty.

Required critique profiles:

- evidence-sufficiency
- operator-clarity
- routing-safety

Findings:

Recorded in `critique:evidence-quality-guidance-review`:

- None - no findings.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle critique passed with no findings.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Dedicated evidence quality guidance was promoted into
  `skills/loom-evidence/references/evidence-quality.md` and linked from
  `skills/loom-evidence/SKILL.md`.
- Evidence record prompts for freshness, invalidation, supersession, observed
  result, and bounded inference were promoted into
  `skills/loom-evidence/templates/evidence.md`.
- Ticket evidence sufficiency teaching was promoted into
  `skills/loom-tickets/SKILL.md`, `skills/loom-tickets/templates/ticket.md`, and
  `skills/loom-tickets/references/acceptance-gate.md`.

Deferred / not-required rationale:

Not deferred. The durable lesson was promoted directly into the owner product
surfaces listed above; no separate wiki page, research record, spec,
constitution decision, or memory entry is needed.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation now lives in the
evidence and ticket owner surfaces.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T20:54:00Z
Basis: Ralph packet `packet:ralph-ticket-evshape9-20260502T204732Z`; evidence
`evidence:evidence-quality-guidance-validation`; oracle critique
`critique:evidence-quality-guidance-review` with no findings.
Residual risks: validation is structural and prose-based; future operator
adoption is not mechanically enforceable, by design.

# Dependencies

- `ticket:retrod3p`

# Journal

- 2026-05-02T18:58:43Z: Created from council finding `CR-009`.
- 2026-05-02T20:47:32Z: Started Ralph iteration
  `packet:ralph-ticket-evshape9-20260502T204732Z` from baseline
  `4ee1f67f07bf4428829f57460870d24e06f080bf`.
- 2026-05-02T20:49:39Z: Ralph child completed bounded guidance updates,
  created `evidence:evidence-quality-guidance-validation`, and moved ticket to
  `review_required` for mandatory oracle critique.
- 2026-05-02T20:54:00Z: Oracle critique passed with no findings. Recorded
  acceptance and retrospective / promotion disposition; closed ticket.
