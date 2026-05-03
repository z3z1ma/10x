---
id: ticket:askpost22
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T08:23:28Z
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
  critique:
    - critique:problem-shaping-ask-user-posture-review
external_refs: {}
depends_on:
  - ticket:shipacc1
---

# Summary

Align problem-shaping ambiguous-choice guidance with the newer `ask_user` posture.

# Context

Problem shaping currently says not to silently choose between ambiguous readings.
That is directionally right but too absolute for low-risk reversible assumptions
inside delegated authority.

# Why Now

The corpus now distinguishes unsafe material ambiguity from low-risk reversible
assumptions that can be recorded and carried forward.

# Scope

- Qualify the ambiguous-choice guardrail.
- Preserve mandatory questioning for material, irreversible, high-risk,
  authority-changing, or owner-record-affecting ambiguity.
- Allow low-risk reversible assumptions inside delegated authority when recorded
  in the owner record.

# Out Of Scope

- Do not weaken `ask_user` for material decisions.
- Do not let chat summaries replace owner records.

# Acceptance Criteria

- ACC-001: Problem-shaping guardrail distinguishes material ambiguity from
  low-risk reversible assumptions.
- ACC-002: Low-risk assumption path requires recording the assumption in the
  owning record.
- ACC-003: `ask_user` remains required when proceeding would invent authority or
  accept material risk.
- ACC-004: Evidence records targeted problem-shaping / ask-user searches and
  `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-023`
- `ticket:askpost22#ACC-001`
- `ticket:askpost22#ACC-002`
- `ticket:askpost22#ACC-003`
- `ticket:askpost22#ACC-004`
- `ticket:askpost22#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-023` | `evidence:problem-shaping-ask-user-posture-validation` | `critique:problem-shaping-ask-user-posture-review` | supported |
| `ticket:askpost22#ACC-001` | `evidence:problem-shaping-ask-user-posture-validation` | `critique:problem-shaping-ask-user-posture-review` | supported |
| `ticket:askpost22#ACC-002` | `evidence:problem-shaping-ask-user-posture-validation` | `critique:problem-shaping-ask-user-posture-review` | supported |
| `ticket:askpost22#ACC-003` | `evidence:problem-shaping-ask-user-posture-validation` | `critique:problem-shaping-ask-user-posture-review` | supported |
| `ticket:askpost22#ACC-004` | `evidence:problem-shaping-ask-user-posture-validation` | `critique:problem-shaping-ask-user-posture-review` | supported |
| `ticket:askpost22#ACC-005` | `evidence:problem-shaping-ask-user-posture-validation` | `critique:problem-shaping-ask-user-posture-review` | supported |

# Execution Notes

Likely touched file: `skills/loom-workspace/references/problem-shaping.md`.

# Blockers

None - prerequisite `ticket:shipacc1` is closed and pushed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:readwsh23`.

Ralph packet `packet:ralph-ticket-askpost22-20260503T081918Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Ralph readiness:
Bounded iteration: problem-shaping ask-user posture alignment.
Write boundary: workspace problem-shaping reference only.
Likely verification posture: observation-first structural validation.
Expected output contract: changed file, ambiguity posture observations, and
critique recommendation.

Acceptance review readiness:
Evidence `evidence:problem-shaping-ask-user-posture-validation` and mandatory
critique `critique:problem-shaping-ask-user-posture-review` support closure.

# Evidence

Expected: targeted searches for ambiguous readings, material/high-risk,
low-risk reversible assumptions, owner record, ask_user, and `git diff --check`.

Recorded:

- `evidence:problem-shaping-ask-user-posture-validation`

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: problem shaping controls when agents ask versus proceed.

Required critique profiles:

- operator-clarity
- authority-boundary
- workflow-boundary

Findings:

`critique:problem-shaping-ask-user-posture-review`: no findings; mandatory
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Problem-shaping ask-user posture was promoted into workspace problem-shaping
  guidance.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to problem-shaping guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in
workspace problem-shaping guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T08:23:28Z
Basis: Ralph packet `packet:ralph-ticket-askpost22-20260503T081918Z`; evidence
`evidence:problem-shaping-ask-user-posture-validation`; mandatory critique
`critique:problem-shaping-ask-user-posture-review` with no findings.
Residual risks: The low-risk/reversible/delegated-authority test still depends on
operator judgment, bounded by the owner-record recording requirement.

# Dependencies

- `ticket:shipacc1`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass audit finding 11.
- 2026-05-03T08:19:18Z: Parent confirmed prerequisites are closed and pushed,
  moved this ticket to active, and compiled Ralph iteration 1.
- 2026-05-03T08:20:52Z: Ralph child returned `stop`; parent accepted the scoped
  implementation output, recorded evidence, consumed the packet, and moved to
  mandatory critique.
- 2026-05-03T08:23:28Z: Mandatory critique
  `critique:problem-shaping-ask-user-posture-review` passed with no findings.
  Parent recorded retrospective / promotion disposition and accepted closure.
