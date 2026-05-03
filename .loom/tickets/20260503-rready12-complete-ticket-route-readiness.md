---
id: ticket:rready12
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T06:43:29Z
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
    - research:skills-corpus-third-pass-follow-up-validation
external_refs: {}
depends_on:
  - ticket:shipacc1
---

# Summary

Make ticket route readiness cover every legal route a ready ticket may name.

# Context

The ticket readiness reference lists the legal route vocabulary but only gives
route-readiness details for a subset. Missing branches make routes like
`research`, `spec`, `plan`, `ticket`, `workspace_status`, `records_repair`,
`continue`, and `stop` too easy to name without enough safety facts.

# Why Now

Ready tickets should be resumable without chat history regardless of the chosen
next route.

# Scope

- Add explicit readiness guidance for the missing legal routes.
- Keep guidance concise and route-neutral.
- Update the ticket template route-readiness prompt if needed.

# Out Of Scope

- Do not add route tokens.
- Do not make every route Ralph-shaped.

# Acceptance Criteria

- ACC-001: Readiness guidance covers every legal route token listed in the
  reference.
- ACC-002: New route branches name the minimal safety facts required for each
  route.
- ACC-003: `continue` and `stop` readiness distinguish route tokens from Ralph
  child outcomes.
- ACC-004: Evidence records targeted route readiness searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-013`
- `ticket:rready12#ACC-001`
- `ticket:rready12#ACC-002`
- `ticket:rready12#ACC-003`
- `ticket:rready12#ACC-004`
- `ticket:rready12#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-013` | `evidence:route-readiness-coverage-validation` | `critique:route-readiness-coverage-rereview` | supported |
| `ticket:rready12#ACC-001` | `evidence:route-readiness-coverage-validation` | `critique:route-readiness-coverage-rereview` | supported |
| `ticket:rready12#ACC-002` | `evidence:route-readiness-coverage-validation` | `critique:route-readiness-coverage-rereview` | supported |
| `ticket:rready12#ACC-003` | `evidence:route-readiness-coverage-validation` | `critique:route-readiness-coverage-rereview` | supported |
| `ticket:rready12#ACC-004` | `evidence:route-readiness-coverage-validation` | `critique:route-readiness-coverage-rereview` | supported |
| `ticket:rready12#ACC-005` | `evidence:route-readiness-coverage-validation` | `critique:route-readiness-coverage-review#FIND-001` resolved; `critique:route-readiness-coverage-review#FIND-002` resolved; `critique:route-readiness-coverage-rereview` | supported |

# Execution Notes

Likely touched files: `skills/loom-tickets/references/readiness.md` and possibly
`skills/loom-tickets/templates/ticket.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:drvcont13`.

Ralph packet `packet:ralph-ticket-rready12-20260503T063515Z` completed in scope,
evidence was recorded, initial critique findings were resolved, mandatory
re-critique passed with no findings, and acceptance is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:route-readiness-coverage-validation`, resolved initial
findings `critique:route-readiness-coverage-review#FIND-001` and
`critique:route-readiness-coverage-review#FIND-002`, and mandatory re-critique
`critique:route-readiness-coverage-rereview` support closure.

# Evidence

Recorded:

- `evidence:route-readiness-coverage-validation`

The evidence records targeted searches for all legal routes, newly added
route-readiness branches, `continue` / `stop` wording, and `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: route readiness controls whether tickets can safely launch
downstream routes.

Required critique profiles:

- route-coverage
- operator-clarity
- workflow-boundary

Findings:

- `critique:route-readiness-coverage-review#FIND-001` - resolved by replacing
  noncanonical `evidence_recorded` claim matrix states with canonical
  `supported_pending_review` / `challenged` values.
- `critique:route-readiness-coverage-review#FIND-002` - resolved by replacing
  stale Ralph readiness with critique readiness for the current next route.
- `critique:route-readiness-coverage-rereview` - no findings; mandatory
  re-critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Route-complete ticket readiness was promoted into
  `skills/loom-tickets/references/readiness.md` and
  `skills/loom-tickets/templates/ticket.md`.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to ticket readiness guidance and the ticket template.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in ticket
readiness guidance and the ticket template.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T06:43:29Z
Basis: Ralph packet `packet:ralph-ticket-rready12-20260503T063515Z`; evidence
`evidence:route-readiness-coverage-validation`; initial critique
`critique:route-readiness-coverage-review` with findings resolved; mandatory
re-critique `critique:route-readiness-coverage-rereview` with no findings.
Residual risks: Documentation-only enforcement depends on future operators
filling route-readiness prompts correctly. Evidence is structural/textual,
appropriate for a Markdown protocol guidance change.

# Dependencies

- `ticket:shipacc1`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass audit finding 1.
- 2026-05-03T06:35:16Z: Started Ralph iteration
  `packet:ralph-ticket-rready12-20260503T063515Z` from clean `main` at
  `78a5f60`.
- 2026-05-03T06:38:05Z: Ralph iteration consumed. Product edits landed inside
  packet write scope, `evidence:route-readiness-coverage-validation` recorded,
  and ticket moved to `review_required` for mandatory critique.
- 2026-05-03T06:41:38Z: Initial mandatory critique
  `critique:route-readiness-coverage-review` returned `changes_required` for two
  ticket-ledger issues. Parent resolved both in the ticket and kept the ticket in
  `review_required` for re-review.
- 2026-05-03T06:43:29Z: Mandatory re-critique
  `critique:route-readiness-coverage-rereview` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
