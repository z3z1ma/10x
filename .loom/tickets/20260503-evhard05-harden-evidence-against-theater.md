---
id: ticket:evhard05
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T05:31:12Z
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
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-006` | `evidence:evidence-anti-theater-validation` | `critique:evidence-anti-theater-review` | supported |
| `ticket:evhard05#ACC-001` | `evidence:evidence-anti-theater-validation` | `critique:evidence-anti-theater-review` | supported |
| `ticket:evhard05#ACC-002` | `evidence:evidence-anti-theater-validation` | `critique:evidence-anti-theater-review` | supported |
| `ticket:evhard05#ACC-003` | `evidence:evidence-anti-theater-validation` | `critique:evidence-anti-theater-review` | supported |
| `ticket:evhard05#ACC-004` | `evidence:evidence-anti-theater-validation` | `critique:evidence-anti-theater-review` | supported |
| `ticket:evhard05#ACC-005` | None - critique outcome is the acceptance instrument | `critique:evidence-anti-theater-review` | supported |

# Execution Notes

Likely touched files: `skills/loom-evidence/templates/evidence.md`,
`skills/loom-evidence/SKILL.md`, `skills/loom-evidence/references/evidence-quality.md`,
and claim-coverage examples if needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:reconchk`.

Ralph packet `packet:ralph-ticket-evhard05-20260503T052442Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:evidence-anti-theater-validation` and mandatory critique
`critique:evidence-anti-theater-review` support closure with no findings.

# Evidence

Recorded: `evidence:evidence-anti-theater-validation`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: evidence quality gates truthful acceptance.

Required critique profiles:

- evidence-quality
- closure-honesty
- operator-clarity

Findings:

`critique:evidence-anti-theater-review` - no findings; mandatory critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Evidence expected/actual, freshness, partial-support, untested-limit, and
  anti-acceptance guidance was promoted directly into the evidence skill,
  evidence-quality reference, evidence template, and claim-coverage example.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to evidence guidance and claim-coverage examples.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
evidence skill/reference/template and claim-coverage reference.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T05:31:12Z
Basis: Ralph packet `packet:ralph-ticket-evhard05-20260503T052442Z`; evidence
`evidence:evidence-anti-theater-validation`; mandatory critique
`critique:evidence-anti-theater-review` with no findings.
Residual risks: This is prose/protocol guidance and cannot prove future operators
will apply it correctly. The template intentionally relies on honest operator
completion of `when applicable`, `None - reason`, limitations, and recheck fields.

# Dependencies

- `ticket:pktfam04`

# Journal

- 2026-05-03T04:09:51Z: Created from council evidence anti-theater finding.
- 2026-05-03T05:24:42Z: Started Ralph iteration
  `packet:ralph-ticket-evhard05-20260503T052442Z` from clean `main` at
  `88fcd76`. Normalized ticket `change_class` to valid `protocol-authority`
  before execution.
- 2026-05-03T05:27:17Z: Ralph iteration
  `packet:ralph-ticket-evhard05-20260503T052442Z` completed in scope. Evidence
  recorded in `evidence:evidence-anti-theater-validation`; next route is
  mandatory critique.
- 2026-05-03T05:31:12Z: Mandatory critique
  `critique:evidence-anti-theater-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
