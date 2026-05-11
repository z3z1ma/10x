---
id: ticket:drives10
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T06:14:19Z
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
  - ticket:queryrc9
---

# Summary

Tighten `loom-drive` and saved support artifact boundaries so drive cannot become
a shadow ledger.

# Context

Council found drive valuable but the highest-risk workflow for duplicating ticket
truth or creating support-ledger drift.

# Why Now

Drive coordinates broad delegated objectives. It must clearly decline one-ticket
work and keep support artifacts reconciled into owner records.

# Scope

- Add prominent `Do not use drive for` guidance for small/ticket-ready work.
- Tighten saved support artifact rules: owner workflow, reconciliation target,
  prune/supersession condition, and no truth ownership.
- Preserve current drive capability for multi-phase objectives.

# Out Of Scope

- Do not add `.loom/drive/`, scheduler, daemon, DB, or drive state file.
- Do not make saved handoffs packets or canonical truth owners.

# Acceptance Criteria

- ACC-001: Drive guidance clearly says when not to use drive.
- ACC-002: Saved support artifact guidance names owner, reconciliation target, and
  prune/supersession condition.
- ACC-003: Guidance preserves ticket-owned live state and support noncanonicality.
- ACC-004: Evidence records targeted drive/support searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-010`
- `ticket:drives10#ACC-001`
- `ticket:drives10#ACC-002`
- `ticket:drives10#ACC-003`
- `ticket:drives10#ACC-004`
- `ticket:drives10#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-010` | `evidence:drive-support-boundary-validation` | `critique:drive-support-boundary-review` | supported |
| `ticket:drives10#ACC-001` | `evidence:drive-support-boundary-validation` | `critique:drive-support-boundary-review` | supported |
| `ticket:drives10#ACC-002` | `evidence:drive-support-boundary-validation` | `critique:drive-support-boundary-review` | supported |
| `ticket:drives10#ACC-003` | `evidence:drive-support-boundary-validation` | `critique:drive-support-boundary-review` | supported |
| `ticket:drives10#ACC-004` | `evidence:drive-support-boundary-validation` | `critique:drive-support-boundary-review` | supported |
| `ticket:drives10#ACC-005` | None - critique outcome is the acceptance instrument | `critique:drive-support-boundary-review` | supported |

# Execution Notes

Likely touched files: `skills/loom-drive/SKILL.md`, drive support/handoff
references/templates, and records support-artifact guidance if needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:shipacc1`.

Ralph packet `packet:ralph-ticket-drives10-20260503T060716Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:drive-support-boundary-validation` and mandatory critique
`critique:drive-support-boundary-review` support closure with no findings.

# Evidence

Recorded: `evidence:drive-support-boundary-validation`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: drive can otherwise become a second ledger.

Required critique profiles:

- workflow-boundary
- owner-boundary
- operator-clarity

Findings:

`critique:drive-support-boundary-review` - no findings; mandatory critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Direct-route / do-not-use-drive boundaries were promoted into
  `skills/loom-drive/SKILL.md`.
- Saved handoff owner, reconciliation, and prune/supersession guidance was
  promoted into drive support references/templates and shared support artifact
  grammar.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to drive and support artifact guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in drive
and support artifact references/templates.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T06:14:19Z
Basis: Ralph packet `packet:ralph-ticket-drives10-20260503T060716Z`; evidence
`evidence:drive-support-boundary-validation`; mandatory critique
`critique:drive-support-boundary-review` with no findings.
Residual risks: Documentation-only enforcement depends on future operators
following routing guidance. Pruning saved support artifacts remains
judgment-based, not automated by design.

# Dependencies

- `ticket:queryrc9`

# Journal

- 2026-05-03T04:09:51Z: Created from council drive/support boundary finding.
- 2026-05-03T06:07:16Z: Started Ralph iteration
  `packet:ralph-ticket-drives10-20260503T060716Z` from clean `main` at
  `4dd406a`. Normalized ticket `change_class` to valid `protocol-authority`
  before execution.
- 2026-05-03T06:11:15Z: Ralph iteration
  `packet:ralph-ticket-drives10-20260503T060716Z` completed in scope. Evidence
  recorded in `evidence:drive-support-boundary-validation`; next route is
  mandatory critique.
- 2026-05-03T06:14:19Z: Mandatory critique
  `critique:drive-support-boundary-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
