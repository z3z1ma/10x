---
id: ticket:netgate25
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T07:47:49Z
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
    - critique:network-unknown-launch-gate-review
external_refs: {}
depends_on:
  - ticket:shipacc1
  - ticket:pktws19
---

# Summary

Make `network: unknown` a launch blocker unless justified.

# Context

Packet execution context allows `network: unknown`, but launch safety should fail
closed when network posture is unknown and unjustified.

# Why Now

Network access affects safety, reproducibility, and trust boundaries for fresh
workers.

# Scope

- Clarify packet execution context guidance for `network: unknown`.
- Update packet templates if needed so unknown requires a rationale and blocks
  launch when unsafe.

# Out Of Scope

- Do not forbid all network use.
- Do not add a runtime policy engine.

# Acceptance Criteria

- ACC-001: Packet guidance says `network: unknown` is a launch blocker unless a
  rationale makes it safe.
- ACC-002: Templates prompt for explicit network posture or rationale.
- ACC-003: Guidance preserves allowed/forbidden network choices.
- ACC-004: Evidence records targeted network posture searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-026`
- `ticket:netgate25#ACC-001`
- `ticket:netgate25#ACC-002`
- `ticket:netgate25#ACC-003`
- `ticket:netgate25#ACC-004`
- `ticket:netgate25#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-026` | `evidence:network-unknown-launch-gate-validation` | `critique:network-unknown-launch-gate-review` | supported |
| `ticket:netgate25#ACC-001` | `evidence:network-unknown-launch-gate-validation` | `critique:network-unknown-launch-gate-review` | supported |
| `ticket:netgate25#ACC-002` | `evidence:network-unknown-launch-gate-validation` | `critique:network-unknown-launch-gate-review` | supported |
| `ticket:netgate25#ACC-003` | `evidence:network-unknown-launch-gate-validation` | `critique:network-unknown-launch-gate-review` | supported |
| `ticket:netgate25#ACC-004` | `evidence:network-unknown-launch-gate-validation` | `critique:network-unknown-launch-gate-review` | supported |
| `ticket:netgate25#ACC-005` | `evidence:network-unknown-launch-gate-validation` | `critique:network-unknown-launch-gate-review` | supported |

# Execution Notes

Likely touched files: `skills/loom-records/references/packet-frontmatter.md` and
packet templates that carry `network` posture.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:gitstat26`.

Ralph packet `packet:ralph-ticket-netgate25-20260503T074327Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:network-unknown-launch-gate-validation` and mandatory critique
`critique:network-unknown-launch-gate-review` support closure.

# Evidence

Recorded:

- `evidence:network-unknown-launch-gate-validation`

The evidence records targeted searches for `network: unknown`, launch blocker,
rationale, allowed/forbidden choices, forbidden additions, and `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: network posture is a fresh-worker safety boundary.

Required critique profiles:

- packet-safety
- trust-boundary
- operator-clarity

Findings:

- `critique:network-unknown-launch-gate-review` - no findings; mandatory critique
  passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Network unknown launch-gate guidance was promoted into packet frontmatter,
  Ralph packet contract, and packet-family templates.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to packet execution-context guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in packet
execution-context guidance and templates.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T07:47:49Z
Basis: Ralph packet `packet:ralph-ticket-netgate25-20260503T074327Z`; evidence
`evidence:network-unknown-launch-gate-validation`; mandatory critique
`critique:network-unknown-launch-gate-review` with no findings.
Residual risks: Enforcement remains operator/parent discipline; no runtime
validator enforces this, consistent with ticket scope.

# Dependencies

- `ticket:shipacc1`
- `ticket:pktws19`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass secondary polish finding.
- 2026-05-03T07:43:28Z: Started Ralph iteration
  `packet:ralph-ticket-netgate25-20260503T074327Z` from clean `main` at
  `949cd79`.
- 2026-05-03T07:45:40Z: Ralph iteration consumed. Product edits landed inside
  packet write scope, `evidence:network-unknown-launch-gate-validation` recorded,
  and ticket moved to `review_required` for mandatory critique.
- 2026-05-03T07:47:49Z: Mandatory critique
  `critique:network-unknown-launch-gate-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
