---
id: ticket:wroute15
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T07:01:20Z
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

Normalize workspace routing rows to separate route tokens from owner or
coordinator skill names.

# Context

Workspace routing currently mixes route-token language with skill-name-only rows,
which can blur saved route values and skill invocation labels.

# Why Now

Fresh agents rely on workspace routing early. It should model route-token grammar
consistently.

# Scope

- Normalize routing rows to include route token and owner/coordinator where
  applicable.
- Keep support-only skills such as memory out of project-truth route tokens.

# Out Of Scope

- Do not add route tokens.
- Do not demote actual workflow coordinator routes.

# Acceptance Criteria

- ACC-001: Workspace routing rows consistently distinguish route token from
  owner/coordinator skill.
- ACC-002: Support-only memory guidance is not presented as a project-truth route.
- ACC-003: Route vocabulary remains the canonical saved-field token source.
- ACC-004: Evidence records targeted workspace routing searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-016`
- `ticket:wroute15#ACC-001`
- `ticket:wroute15#ACC-002`
- `ticket:wroute15#ACC-003`
- `ticket:wroute15#ACC-004`
- `ticket:wroute15#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-016` | `evidence:workspace-routing-row-normalization-validation` | `critique:workspace-routing-row-normalization-review` | supported |
| `ticket:wroute15#ACC-001` | `evidence:workspace-routing-row-normalization-validation` | `critique:workspace-routing-row-normalization-review` | supported |
| `ticket:wroute15#ACC-002` | `evidence:workspace-routing-row-normalization-validation` | `critique:workspace-routing-row-normalization-review` | supported |
| `ticket:wroute15#ACC-003` | `evidence:workspace-routing-row-normalization-validation` | `critique:workspace-routing-row-normalization-review` | supported |
| `ticket:wroute15#ACC-004` | `evidence:workspace-routing-row-normalization-validation` | `critique:workspace-routing-row-normalization-review` | supported |
| `ticket:wroute15#ACC-005` | `evidence:workspace-routing-row-normalization-validation` | `critique:workspace-routing-row-normalization-review` | supported |

# Execution Notes

Likely touched file: `skills/loom-workspace/references/routing.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:phvalid16`.

Ralph packet `packet:ralph-ticket-wroute15-20260503T065527Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:workspace-routing-row-normalization-validation` and mandatory
critique `critique:workspace-routing-row-normalization-review` support closure
with no findings.

# Evidence

Recorded:

- `evidence:workspace-routing-row-normalization-validation`

The evidence records targeted searches for route token, owner/coordinator,
support skill, memory, route vocabulary, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: workspace routing is an early cold-start decision surface.

Required critique profiles:

- route-vocabulary
- workflow-boundary
- operator-clarity

Findings:

`critique:workspace-routing-row-normalization-review` - no findings; mandatory
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Workspace route-token versus owner/coordinator wording was promoted into
  `skills/loom-workspace/references/routing.md`.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to workspace routing guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in
workspace routing guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T07:01:20Z
Basis: Ralph packet `packet:ralph-ticket-wroute15-20260503T065527Z`; evidence
`evidence:workspace-routing-row-normalization-validation`; mandatory critique
`critique:workspace-routing-row-normalization-review` with no findings.
Residual risks: Documentation-only enforcement depends on future operators
choosing the correct route token from the mapping guidance.

# Dependencies

- `ticket:shipacc1`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass audit finding 4.
- 2026-05-03T06:55:27Z: Started Ralph iteration
  `packet:ralph-ticket-wroute15-20260503T065527Z` from clean `main` at
  `4cef2af`.
- 2026-05-03T06:57:36Z: Ralph iteration consumed. Product edit landed inside
  packet write scope, `evidence:workspace-routing-row-normalization-validation`
  recorded, and ticket moved to `review_required` for mandatory critique.
- 2026-05-03T07:01:20Z: Mandatory critique
  `critique:workspace-routing-row-normalization-review` passed with no findings.
  Parent recorded retrospective / promotion disposition and accepted closure.
