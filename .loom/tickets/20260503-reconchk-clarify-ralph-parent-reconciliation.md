---
id: ticket:reconchk
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T05:39:42Z
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
  - ticket:evhard05
---

# Summary

Make Ralph parent reconciliation and stale compiled packet recovery explicit.

# Context

Council identified parent reconciliation as the fragile point where child output
can fail to become ticket/evidence/critique truth.

# Why Now

Ralph is central to bounded fresh-worker execution. The parent checklist should be
copyable and recovery queries should find stale packets.

# Scope

- Add or sharpen parent reconciliation checklist in Ralph guidance.
- Add stale `compiled` packet recovery/search guidance in Ralph or records query
  references.
- Keep packets as support artifacts, not truth owners.

# Out Of Scope

- Do not create a reconciliation record kind.
- Do not add automated merge scripts or hidden runtimes.

# Acceptance Criteria

- ACC-001: Ralph guidance gives a concrete parent reconciliation checklist after
  child output.
- ACC-002: Guidance includes stale `compiled` packet discovery and disposition.
- ACC-003: The text preserves ticket-owned execution/acceptance and packet support
  boundaries.
- ACC-004: Evidence records targeted reconciliation/stale packet searches and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-007`
- `ticket:reconchk#ACC-001`
- `ticket:reconchk#ACC-002`
- `ticket:reconchk#ACC-003`
- `ticket:reconchk#ACC-004`
- `ticket:reconchk#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-007` | `evidence:ralph-parent-reconciliation-validation` | `critique:ralph-parent-reconciliation-review` | supported |
| `ticket:reconchk#ACC-001` | `evidence:ralph-parent-reconciliation-validation` | `critique:ralph-parent-reconciliation-review` | supported |
| `ticket:reconchk#ACC-002` | `evidence:ralph-parent-reconciliation-validation` | `critique:ralph-parent-reconciliation-review` | supported |
| `ticket:reconchk#ACC-003` | `evidence:ralph-parent-reconciliation-validation` | `critique:ralph-parent-reconciliation-review` | supported |
| `ticket:reconchk#ACC-004` | `evidence:ralph-parent-reconciliation-validation` | `critique:ralph-parent-reconciliation-review` | supported |
| `ticket:reconchk#ACC-005` | None - critique outcome is the acceptance instrument | `critique:ralph-parent-reconciliation-review` | supported |

# Execution Notes

Likely touched files: `skills/loom-ralph/references/work-driver.md`,
`skills/loom-ralph/references/packet-contract.md`, and query/status references if
needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:localed7`.

Ralph packet `packet:ralph-ticket-reconchk-20260503T053234Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:ralph-parent-reconciliation-validation` and mandatory critique
`critique:ralph-parent-reconciliation-review` support closure with no findings.

# Evidence

Recorded: `evidence:ralph-parent-reconciliation-validation`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: parent reconciliation controls whether child work becomes
truthful Loom state.

Required critique profiles:

- workflow-boundary
- packet-safety
- operator-clarity

Findings:

`critique:ralph-parent-reconciliation-review` - no findings; mandatory critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Parent reconciliation checklist guidance was promoted directly into
  `skills/loom-ralph/references/work-driver.md`.
- Stale compiled packet recovery guidance was promoted directly into Ralph packet,
  query/linking, and status lifecycle references.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to Ralph and shared records references.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in Ralph
and shared records references.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T05:39:42Z
Basis: Ralph packet `packet:ralph-ticket-reconchk-20260503T053234Z`; evidence
`evidence:ralph-parent-reconciliation-validation`; mandatory critique
`critique:ralph-parent-reconciliation-review` with no findings.
Residual risks: Review is structural and manual. Guidance cannot prove future
operators will reconcile correctly; it makes the required path explicit.

# Dependencies

- `ticket:evhard05`

# Journal

- 2026-05-03T04:09:51Z: Created from council parent reconciliation finding.
- 2026-05-03T05:32:34Z: Started Ralph iteration
  `packet:ralph-ticket-reconchk-20260503T053234Z` from clean `main` at
  `c4a476e`. Normalized ticket `change_class` to valid `protocol-authority`
  before execution.
- 2026-05-03T05:35:38Z: Ralph iteration
  `packet:ralph-ticket-reconchk-20260503T053234Z` completed in scope. Evidence
  recorded in `evidence:ralph-parent-reconciliation-validation`; next route is
  mandatory critique.
- 2026-05-03T05:39:42Z: Mandatory critique
  `critique:ralph-parent-reconciliation-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
