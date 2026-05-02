---
id: ticket:wfxfu4zp
kind: ticket
status: ready
change_class: record-hygiene
risk_class: medium
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T15:25:50Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  plan:
    - plan:skills-corpus-perfection-council-followup
external_refs: {}
depends_on:
  - ticket:3twzep5n
  - ticket:4ilnwsnl
  - ticket:lqiw3hvp
  - ticket:yk89awl5
  - ticket:u02z7o9j
  - ticket:9c2delu8
---

# Summary

Run the low-risk corpus hygiene sweep from the council review after all earlier
terminology decisions land.

# Context

Council findings `COUNCIL-FIND-005`, `COUNCIL-FIND-009`, `COUNCIL-FIND-010`,
`COUNCIL-FIND-012`, `COUNCIL-FIND-013`, `COUNCIL-FIND-014`, and
`COUNCIL-FIND-015` identified grep recipe gaps, tree diagram drift,
install-layout assumptions, heading inconsistency, memory status drift,
`external_refs` inconsistency, and ad hoc research link verbs.

# Why Now

These findings are lower risk individually but should be resolved after the
shared terminology tickets to avoid churn and stale examples.

# Scope

- Include `OBJ-*` in validation/repair/status-snapshot claim queries where
  omitted.
- Align `.loom/` tree diagrams/lists or point summaries to the canonical
  workspace tree.
- Replace repo-root `skills/...` copy assumptions with install-safe wording.
- Standardize `# Non-goals` / `# Out Of Scope` template headings if earlier
  ticket changes have not already done so.
- Replace memory `inactive` example status with an allowed support status.
- Normalize `external_refs: {}` template convention or document when templates
  omit it.
- Remove or formalize ad hoc research link verbs.

# Non-goals

- Do not reopen settled vocabulary from earlier tickets unless evidence shows a
  direct inconsistency.
- Do not perform broad prose style rewrites.
- Do not touch internal `examples/` unless product-surface references require it.

# Acceptance Criteria

- ACC-001: Hygiene findings named in scope are resolved or explicitly deferred
  with rationale.
- ACC-002: Evidence records targeted searches for each hygiene item and
  `git diff --check`.
- ACC-003: No new runtime, command-wrapper truth, or canonical owner layer is
  introduced.
- ACC-004: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-perfection-council-followup#OBJ-007`
- `initiative:skills-corpus-perfection-council-followup#OBJ-008`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-perfection-council-followup#OBJ-007` | pending | pending | open |
| `initiative:skills-corpus-perfection-council-followup#OBJ-008` | pending | pending | open |

# Execution Notes

This is the final child ticket before plan/initiative acceptance. It should also
prepare the parent to mark the plan and initiative complete if all prior tickets
are closed.

# Blockers

Depends on every earlier ticket in this plan.

# Next Move / Next Route

Ralph implementation packet after dependencies close.

# Ralph Readiness

Bounded iteration: run targeted low-risk hygiene sweep and prepare final plan
reconciliation.

Write boundary: targeted `skills/**` and README/bootstrap/workspace summary files
as needed for the named hygiene findings, this ticket, one evidence record, one
critique record, and the Ralph packet. Parent may update plan/initiative after
critique.

Likely verification posture: observation-first structural validation.

Expected output contract: changed files, evidence, critique, ticket closure
recommendation, retrospective disposition, and final plan/initiative completion
recommendation.

# Evidence

Expected:

- `git diff --check`
- targeted searches for every hygiene finding in scope
- manual comparison against owning references/templates

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: user requires oracle critique for every ticket; final sweep
touches multiple protocol surfaces.

Required critique profiles:

- records-grammar
- operator-clarity
- routing-safety

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None. Critique is required by user instruction.

# Wiki Disposition

Pending retrospective decision after critique.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

- `ticket:3twzep5n`
- `ticket:4ilnwsnl`
- `ticket:lqiw3hvp`
- `ticket:yk89awl5`
- `ticket:u02z7o9j`
- `ticket:9c2delu8`

# Journal

- 2026-05-02T15:25:50Z: Created from council hygiene findings
  `COUNCIL-FIND-005`, `COUNCIL-FIND-009`, `COUNCIL-FIND-010`,
  `COUNCIL-FIND-012`, `COUNCIL-FIND-013`, `COUNCIL-FIND-014`, and
  `COUNCIL-FIND-015`.
