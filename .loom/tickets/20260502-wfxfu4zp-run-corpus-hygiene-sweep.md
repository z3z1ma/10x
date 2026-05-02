---
id: ticket:wfxfu4zp
kind: ticket
status: closed
change_class: record-hygiene
risk_class: medium
created_at: 2026-05-02T15:25:50Z
updated_at: 2026-05-02T17:27:34Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-perfection-council-followup
  plan:
    - plan:skills-corpus-perfection-council-followup
  evidence:
    - evidence:corpus-hygiene-sweep-validation
  critique:
    - critique:corpus-hygiene-sweep-review
  packet:
    - packet:ralph-ticket-wfxfu4zp-20260502T171547Z
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

# Out Of Scope

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
| `initiative:skills-corpus-perfection-council-followup#OBJ-007` | `evidence:corpus-hygiene-sweep-validation` | `critique:corpus-hygiene-sweep-review` | supported |
| `initiative:skills-corpus-perfection-council-followup#OBJ-008` | `evidence:corpus-hygiene-sweep-validation` and this ticket acceptance dossier; semantic commit/push remains the next git step before final plan acceptance | `critique:corpus-hygiene-sweep-review` | supported_for_ticket_scope |
| `ticket:wfxfu4zp#ACC-001` | `evidence:corpus-hygiene-sweep-validation` | `critique:corpus-hygiene-sweep-review` | supported |
| `ticket:wfxfu4zp#ACC-002` | `evidence:corpus-hygiene-sweep-validation` | `critique:corpus-hygiene-sweep-review` | supported |
| `ticket:wfxfu4zp#ACC-003` | `evidence:corpus-hygiene-sweep-validation`; diff shows Markdown-only product/record edits inside packet scope | `critique:corpus-hygiene-sweep-review` | supported |
| `ticket:wfxfu4zp#ACC-004` | `critique:corpus-hygiene-sweep-review` | `critique:corpus-hygiene-sweep-review` passed with no findings | supported |

# Execution Notes

This is the final child ticket before plan/initiative acceptance. It should also
prepare the parent to mark the plan and initiative complete if all prior tickets
are closed.

Ralph iteration `packet:ralph-ticket-wfxfu4zp-20260502T171547Z` completed the
targeted hygiene sweep. Product-surface edits covered `OBJ-*` claim-query gaps,
runtime-tree ordering/detail drift, install-safe template-copy wording, scope
heading standardization, memory support status examples, the `external_refs`
template omission convention, and ad hoc research link verbs. No runtime,
command-wrapper truth, or new canonical owner layer was introduced.

# Blockers

None current. Earlier dependencies were required before launch and remain linked
for audit history.

# Next Move / Next Route

Closed. Commit and push this ticket before final plan/initiative acceptance.

# Route Readiness

Route: ticket acceptance review completed.

Review target: final corpus hygiene sweep across scoped product surfaces and
Loom records.

Evidence reviewed: `evidence:corpus-hygiene-sweep-validation`, Ralph packet,
oracle critique, and the git diff.

Acceptance result: close-ready with no oracle findings.

# Evidence

Expected:

- `git diff --check`
- targeted searches for every hygiene finding in scope
- manual comparison against owning references/templates

Recorded:

- `evidence:corpus-hygiene-sweep-validation` records before/after targeted
  searches for each scoped hygiene item and `git diff --check` with exit 0.

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

Recorded in `critique:corpus-hygiene-sweep-review`:

- None - no findings.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle critique passed with no findings.

# Wiki Disposition

Retrospective disposition complete. Durable lessons were promoted directly into
the owner product surfaces: README runtime tree, bootstrap/tooling copy guidance,
ticket skill copy guidance and template heading, record grammar query/frontmatter
references, workspace status snapshot query, research link guidance, and memory
entity template status vocabulary. No separate wiki page, research record, spec,
constitution decision, or memory entry is needed for this ticket.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T17:27:34Z
Basis: Ralph packet `packet:ralph-ticket-wfxfu4zp-20260502T171547Z`; evidence
`evidence:corpus-hygiene-sweep-validation`; oracle critique
`critique:corpus-hygiene-sweep-review` with no findings.
Residual risks: validation and critique were structural/textual; future operator
application is not proven beyond corpus consistency.

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
- 2026-05-02T17:15:47Z: Started Ralph iteration
  `packet:ralph-ticket-wfxfu4zp-20260502T171547Z` for the final hygiene sweep.
- 2026-05-02T17:20:51Z: Ralph child sweep completed product-surface hygiene
  edits and recorded `evidence:corpus-hygiene-sweep-validation`; ticket moved to
  `review_required` because oracle critique is mandatory before closure.
- 2026-05-02T17:27:34Z: Oracle critique passed with no findings. Recorded
  `critique:corpus-hygiene-sweep-review`, retrospective disposition, and
  acceptance; closed ticket.
