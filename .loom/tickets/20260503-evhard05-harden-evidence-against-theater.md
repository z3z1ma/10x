---
id: ticket:evhard05
kind: ticket
status: ready
change_class: evidence-quality
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T04:09:51Z
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
  - ticket:pktfam04
---

# Summary

Harden evidence guidance against overclaiming, stale source state, and vague
validation records.

# Context

Council identified evidence theater as one of Loom's highest-risk failure modes.

# Why Now

Evidence is the observed reward signal for agentic work. If it overclaims, ticket
closure becomes untrustworthy.

# Scope

- Strengthen evidence template/reference guidance around claim/question,
  expected result, actual result, source state, support/challenge strength,
  limitations, and recheck triggers.
- Keep evidence as observation, not acceptance.

# Out Of Scope

- Do not require exhaustive logs or a test framework for every evidence record.
- Do not make evidence own intended behavior, critique verdicts, or closure.

# Acceptance Criteria

- ACC-001: Evidence guidance asks for expected and actual observed results when
  applicable.
- ACC-002: Evidence guidance ties observations to source state/environment and
  recheck/invalidated-by conditions.
- ACC-003: Evidence guidance distinguishes support, challenge, partial support,
  and untested limits.
- ACC-004: Evidence records targeted evidence-quality searches and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-006`
- `ticket:evhard05#ACC-001`
- `ticket:evhard05#ACC-002`
- `ticket:evhard05#ACC-003`
- `ticket:evhard05#ACC-004`
- `ticket:evhard05#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-006` | pending | pending | open |
| `ticket:evhard05#ACC-001` | pending | pending | open |
| `ticket:evhard05#ACC-002` | pending | pending | open |
| `ticket:evhard05#ACC-003` | pending | pending | open |
| `ticket:evhard05#ACC-004` | pending | pending | open |
| `ticket:evhard05#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched files: `skills/loom-evidence/templates/evidence.md`,
`skills/loom-evidence/SKILL.md`, `skills/loom-evidence/references/evidence-quality.md`,
and claim-coverage examples if needed.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: evidence anti-theater hardening.
Write boundary: evidence skill/template/reference and directly related claim
coverage examples.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, evidence-quality observations, and
critique recommendation.

# Evidence

Expected: targeted searches for expected/actual, source state, support/challenge,
limitations, recheck/invalidated-by, and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: evidence quality gates truthful acceptance.

Required critique profiles:

- evidence-quality
- closure-honesty
- operator-clarity

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Pending after critique.

# Wiki Disposition

Pending retrospective decision after critique.

# Acceptance Decision

Accepted by:
Accepted at:
Basis:
Residual risks:

# Dependencies

- `ticket:pktfam04`

# Journal

- 2026-05-03T04:09:51Z: Created from council evidence anti-theater finding.
