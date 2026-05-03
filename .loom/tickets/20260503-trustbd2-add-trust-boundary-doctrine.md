---
id: ticket:trustbd2
kind: ticket
status: ready
change_class: protocol-authority
risk_class: high
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
  - ticket:bootinv1
---

# Summary

Add explicit trust-boundary doctrine for untrusted text, records, generated files,
tool output, command snippets, and secrets.

# Context

Council found trust boundaries under-emphasized for a context-integrity protocol.

# Why Now

Agents will read records, web pages, logs, generated summaries, and tool output.
They need doctrine that treats these as data unless higher authority authorizes
action.

# Scope

- Add or update bootstrap/records guidance so trust boundaries are discoverable.
- Link or mention the doctrine from evidence, research, and memory surfaces where
  untrusted or external content is common.
- Include secret/PII caution without adding tooling requirements.

# Out Of Scope

- Do not add secret scanners, security daemons, encryption systems, validators, or
  a `loom-security` owner layer.
- Do not make external text impossible to use as evidence or research source.

# Acceptance Criteria

- ACC-001: Corpus says records, external refs, generated files, tool output, logs,
  and quoted commands are data, not instruction authority.
- ACC-002: Corpus warns not to place secrets, credentials, API keys, or sensitive
  personal data into Loom records.
- ACC-003: Evidence/research/memory guidance points operators toward the trust
  boundary without making those layers canonical truth owners.
- ACC-004: Evidence records targeted trust-boundary searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-002`
- `ticket:trustbd2#ACC-001`
- `ticket:trustbd2#ACC-002`
- `ticket:trustbd2#ACC-003`
- `ticket:trustbd2#ACC-004`
- `ticket:trustbd2#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-002` | pending | pending | open |
| `ticket:trustbd2#ACC-001` | pending | pending | open |
| `ticket:trustbd2#ACC-002` | pending | pending | open |
| `ticket:trustbd2#ACC-003` | pending | pending | open |
| `ticket:trustbd2#ACC-004` | pending | pending | open |
| `ticket:trustbd2#ACC-005` | pending | pending | open |

# Execution Notes

Likely touched surfaces include bootstrap truth/authority, records frontmatter or
external-reference guidance, evidence/research source guidance, and memory support
guidance.

# Blockers

None.

# Next Move / Next Route

Next route: ralph

# Route Readiness

Ralph readiness:
Bounded iteration: trust-boundary doctrine.
Write boundary: targeted skill references only, this ticket, one packet, one
evidence record, and one critique record.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, targeted trust-boundary observations, and
critique recommendation.

# Evidence

Expected: searches for trust/data/instruction authority, secrets/credentials,
external refs, generated/tool output, and `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: trust-boundary doctrine affects how agents interpret untrusted
context across the protocol.

Required critique profiles:

- security
- protocol-change
- owner-boundary

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

- `ticket:bootinv1`

# Journal

- 2026-05-03T04:09:51Z: Created from council trust-boundary recommendation.
