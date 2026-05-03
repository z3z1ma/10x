---
id: ticket:wikiret14
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T06:54:13Z
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
  - ticket:drvcont13
---

# Summary

Split the drive route-priority row that currently groups `wiki` and
`retrospective`.

# Context

Wiki capture and retrospective compounding are adjacent follow-through routes,
but they do not own the same workflow truth.

# Why Now

Drive priority should not blur accepted explanation capture with a broader
promotion pass across owner layers.

# Scope

- Split the route-priority row into separate `wiki` and `retrospective` cases.
- Keep both routes available and correctly ordered.

# Out Of Scope

- Do not change wiki or retrospective record kinds.
- Do not create a new retrospective directory or ledger.

# Acceptance Criteria

- ACC-001: Drive priority has a distinct `wiki` row for accepted reusable
  explanation or architecture concept capture.
- ACC-002: Drive priority has a distinct `retrospective` row for compounding /
  promotion across owner layers.
- ACC-003: Reconciliation guidance still routes wiki and retrospective results to
  their correct owner layers.
- ACC-004: Evidence records targeted wiki/retrospective priority searches and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-015`
- `ticket:wikiret14#ACC-001`
- `ticket:wikiret14#ACC-002`
- `ticket:wikiret14#ACC-003`
- `ticket:wikiret14#ACC-004`
- `ticket:wikiret14#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-015` | `evidence:wiki-retrospective-priority-validation` | `critique:wiki-retrospective-priority-review` | supported |
| `ticket:wikiret14#ACC-001` | `evidence:wiki-retrospective-priority-validation` | `critique:wiki-retrospective-priority-review` | supported |
| `ticket:wikiret14#ACC-002` | `evidence:wiki-retrospective-priority-validation` | `critique:wiki-retrospective-priority-review` | supported |
| `ticket:wikiret14#ACC-003` | `evidence:wiki-retrospective-priority-validation` | `critique:wiki-retrospective-priority-review` | supported |
| `ticket:wikiret14#ACC-004` | `evidence:wiki-retrospective-priority-validation` | `critique:wiki-retrospective-priority-review` | supported |
| `ticket:wikiret14#ACC-005` | `evidence:wiki-retrospective-priority-validation` | `critique:wiki-retrospective-priority-review` | supported |

# Execution Notes

Likely touched file: `skills/loom-drive/references/tranche-decision-protocol.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:wroute15`.

Ralph packet `packet:ralph-ticket-wikiret14-20260503T064951Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:wiki-retrospective-priority-validation` and mandatory critique
`critique:wiki-retrospective-priority-review` support closure with no findings.

# Evidence

Recorded:

- `evidence:wiki-retrospective-priority-validation`

The evidence records targeted searches for `wiki`, `retrospective`, route
priority, reconciliation guidance, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: drive priority controls follow-through routing.

Required critique profiles:

- workflow-boundary
- owner-boundary
- operator-clarity

Findings:

`critique:wiki-retrospective-priority-review` - no findings; mandatory critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Separate drive `wiki` and `retrospective` route-priority rows were promoted into
  `skills/loom-drive/references/tranche-decision-protocol.md`.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to drive tranche decision guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in drive
tranche decision guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T06:54:13Z
Basis: Ralph packet `packet:ralph-ticket-wikiret14-20260503T064951Z`; evidence
`evidence:wiki-retrospective-priority-validation`; mandatory critique
`critique:wiki-retrospective-priority-review` with no findings.
Residual risks: Documentation-only enforcement depends on future operators
choosing between wiki capture and retrospective promotion correctly.

# Dependencies

- `ticket:shipacc1`
- `ticket:drvcont13`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass audit finding 3.
- 2026-05-03T06:49:51Z: Started Ralph iteration
  `packet:ralph-ticket-wikiret14-20260503T064951Z` from clean `main` at
  `922e342`.
- 2026-05-03T06:51:39Z: Ralph iteration consumed. Product edit landed inside
  packet write scope, `evidence:wiki-retrospective-priority-validation` recorded,
  and ticket moved to `review_required` for mandatory critique.
- 2026-05-03T06:54:13Z: Mandatory critique
  `critique:wiki-retrospective-priority-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
