---
id: ticket:localed7
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T05:47:58Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-context-integrity-hardening-review
external_refs: {}
depends_on:
  - ticket:reconchk
---

# Summary

Define the cheap `local_edit` route so Loom can remain lightweight without
becoming a bypass around ticket truth.

# Context

Council found README's minimum durable state principle strong, but the skills
corpus needs a clearer operational local-edit path.

# Why Now

Agents need to know when small edits do not need Ralph while still preserving
truth in tickets when a ticket owns the work.

# Scope

- Add a local-edit reference or targeted guidance in workspace/ticket/records
  routing.
- Define when local edit is honest, what ticket update is required, when evidence
  is needed, and when to escalate to Ralph/spec/research/critique.

# Out Of Scope

- Do not create a `loom-local-edit` skill or a bypass mode.
- Do not remove Ralph for implementation-sized work.

# Acceptance Criteria

- ACC-001: Corpus defines when `local_edit` is appropriate.
- ACC-002: Corpus states local edit does not bypass ticket-owned live state when a
  ticket owns the work.
- ACC-003: Corpus names escalation triggers for behavior/protocol/risky changes.
- ACC-004: Evidence records targeted `local_edit` searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-008`
- `ticket:localed7#ACC-001`
- `ticket:localed7#ACC-002`
- `ticket:localed7#ACC-003`
- `ticket:localed7#ACC-004`
- `ticket:localed7#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-008` | `evidence:local-edit-route-validation` | `critique:local-edit-route-review` | supported |
| `ticket:localed7#ACC-001` | `evidence:local-edit-route-validation` | `critique:local-edit-route-review` | supported |
| `ticket:localed7#ACC-002` | `evidence:local-edit-route-validation` | `critique:local-edit-route-review` | supported |
| `ticket:localed7#ACC-003` | `evidence:local-edit-route-validation` | `critique:local-edit-route-review` | supported |
| `ticket:localed7#ACC-004` | `evidence:local-edit-route-validation` | `critique:local-edit-route-review` | supported |
| `ticket:localed7#ACC-005` | None - critique outcome is the acceptance instrument | `critique:local-edit-route-review` | supported |

# Execution Notes

Likely touched files: `skills/loom-workspace/references/routing.md`,
`skills/loom-tickets/references/readiness.md`, and route vocabulary if needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:queryrc9`.

Ralph packet `packet:ralph-ticket-localed7-20260503T054106Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:local-edit-route-validation` and mandatory critique
`critique:local-edit-route-review` support closure with no findings.

# Evidence

Recorded: `evidence:local-edit-route-validation`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: local edit guidance protects minimum durable state without
weakening recovery.

Required critique profiles:

- workflow-boundary
- operator-clarity
- ticket-truth

Findings:

`critique:local-edit-route-review` - no findings; mandatory critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- `local_edit` boundary, ticket-truth, evidence, and escalation guidance was
  promoted directly into workspace routing, ticket readiness, and route vocabulary
  references.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to route and readiness references.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in route
and readiness references.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T05:47:58Z
Basis: Ralph packet `packet:ralph-ticket-localed7-20260503T054106Z`; evidence
`evidence:local-edit-route-validation`; mandatory critique
`critique:local-edit-route-review` with no findings.
Residual risks: Structural/manual review only; no automated test suite exists for
this Markdown corpus. The ticket template's local-edit readiness stub remains
brief, but canonical readiness/reference guidance carries the full rule set.

# Dependencies

- `ticket:reconchk`

# Journal

- 2026-05-03T04:09:51Z: Created from council local-edit ergonomics finding.
- 2026-05-03T05:41:06Z: Started Ralph iteration
  `packet:ralph-ticket-localed7-20260503T054106Z` from clean `main` at
  `b4f2058`. Normalized ticket `change_class` to valid `protocol-authority`
  before execution.
- 2026-05-03T05:43:08Z: Ralph iteration
  `packet:ralph-ticket-localed7-20260503T054106Z` completed in scope. Evidence
  recorded in `evidence:local-edit-route-validation`; next route is mandatory
  critique.
- 2026-05-03T05:47:58Z: Mandatory critique
  `critique:local-edit-route-review` passed with no findings. Parent recorded
  retrospective / promotion disposition and accepted closure.
