---
id: ticket:ralphg20
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T08:12:20Z
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
    - critique:ralph-launch-hard-gates-review
external_refs: {}
depends_on:
  - ticket:shipacc1
  - ticket:gitstat26
---

# Summary

Add Ralph launch hard gates for unresolved placeholders and ticket route
authorization.

# Context

Ralph packet templates are strong, but the launch checklist does not explicitly
block unresolved template placeholders or packets whose target ticket does not
authorize `next_route: ralph`.

# Why Now

A well-formed packet should not become an unauthorized or placeholder-filled work
order.

# Scope

- Add launch checks for unresolved placeholders / example IDs / generic `<...>`
  tokens.
- Add launch check that target ticket's next route is `ralph` and readiness fields
  match the packet.

# Out Of Scope

- Do not change child outcome vocabulary.
- Do not add automated validators.

# Acceptance Criteria

- ACC-001: Ralph launch checklist blocks unresolved placeholders or example IDs.
- ACC-002: Ralph launch checklist verifies target ticket `next_route: ralph` and
  readiness match.
- ACC-003: Gates preserve parent-side packet authorization and ticket truth.
- ACC-004: Evidence records targeted launch gate searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-021`
- `ticket:ralphg20#ACC-001`
- `ticket:ralphg20#ACC-002`
- `ticket:ralphg20#ACC-003`
- `ticket:ralphg20#ACC-004`
- `ticket:ralphg20#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-021` | `evidence:ralph-launch-hard-gates-validation` | `critique:ralph-launch-hard-gates-review` | supported |
| `ticket:ralphg20#ACC-001` | `evidence:ralph-launch-hard-gates-validation` | `critique:ralph-launch-hard-gates-review` | supported |
| `ticket:ralphg20#ACC-002` | `evidence:ralph-launch-hard-gates-validation` | `critique:ralph-launch-hard-gates-review` | supported |
| `ticket:ralphg20#ACC-003` | `evidence:ralph-launch-hard-gates-validation` | `critique:ralph-launch-hard-gates-review` | supported |
| `ticket:ralphg20#ACC-004` | `evidence:ralph-launch-hard-gates-validation` | `critique:ralph-launch-hard-gates-review` | supported |
| `ticket:ralphg20#ACC-005` | `evidence:ralph-launch-hard-gates-validation` | `critique:ralph-launch-hard-gates-review` | supported |

# Execution Notes

Likely touched files: `skills/loom-ralph/templates/ralph-packet.md` and possibly
`skills/loom-ralph/references/packet-contract.md`.

# Blockers

None - prerequisites `ticket:shipacc1` and `ticket:gitstat26` are closed and
pushed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:pktorph21`.

Ralph packet `packet:ralph-ticket-ralphg20-20260503T080431Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Ralph readiness:
Bounded iteration: Ralph launch hard gates.
Write boundary: Ralph packet template and directly related launch contract
guidance.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, launch gate observations, and critique
recommendation.

Acceptance review readiness:
Evidence `evidence:ralph-launch-hard-gates-validation` and mandatory critique
`critique:ralph-launch-hard-gates-review` support closure.

# Evidence

Expected: targeted searches for placeholder gate, `next_route: ralph`, readiness
match, launch checklist, and `git diff --check`.

Recorded:

- `evidence:ralph-launch-hard-gates-validation`

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: launch checks authorize fresh child execution.

Required critique profiles:

- packet-safety
- ticket-truth
- operator-clarity

Findings:

`critique:ralph-launch-hard-gates-review`: no findings; mandatory critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Ralph launch hard-gate guidance was promoted into the Ralph packet contract and
  Ralph packet template.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to Ralph launch checklist guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in Ralph
launch checklist guidance and the packet template.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T08:12:20Z
Basis: Ralph packet `packet:ralph-ticket-ralphg20-20260503T080431Z`; evidence
`evidence:ralph-launch-hard-gates-validation`; mandatory critique
`critique:ralph-launch-hard-gates-review` with no findings.
Residual risks: Enforcement remains operator/parent discipline rather than a
runtime validator, consistent with ticket scope.

# Dependencies

- `ticket:shipacc1`
- `ticket:gitstat26`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass audit finding 9.
- 2026-05-03T08:04:31Z: Parent confirmed `ticket:gitstat26` pushed, moved this
  ticket to active, and compiled Ralph iteration 1.
- 2026-05-03T08:07:26Z: Ralph child returned `stop`; parent accepted the scoped
  implementation output with a wording adjustment to avoid self-blocking literal
  placeholder examples, recorded evidence, consumed the packet, and moved to
  mandatory critique.
- 2026-05-03T08:12:20Z: Mandatory critique
  `critique:ralph-launch-hard-gates-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
