---
id: ticket:trustbd2
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T04:09:51Z
updated_at: 2026-05-03T04:53:44Z
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
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-002` | `evidence:trust-boundary-doctrine-validation` | `critique:trust-boundary-doctrine-review` | supported |
| `ticket:trustbd2#ACC-001` | `evidence:trust-boundary-doctrine-validation` | `critique:trust-boundary-doctrine-review` | supported |
| `ticket:trustbd2#ACC-002` | `evidence:trust-boundary-doctrine-validation` | `critique:trust-boundary-doctrine-review` | supported |
| `ticket:trustbd2#ACC-003` | `evidence:trust-boundary-doctrine-validation` | `critique:trust-boundary-doctrine-review` | supported |
| `ticket:trustbd2#ACC-004` | `evidence:trust-boundary-doctrine-validation` | `critique:trust-boundary-doctrine-review` | supported |
| `ticket:trustbd2#ACC-005` | None - critique outcome is the acceptance instrument | `critique:trust-boundary-doctrine-review` | supported |

# Execution Notes

Likely touched surfaces include bootstrap truth/authority, records frontmatter or
external-reference guidance, evidence/research source guidance, and memory support
guidance.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:vocabx08`.

Ralph packets were consumed in scope, evidence was recorded and refreshed,
mandatory critique passed with all findings resolved, and acceptance is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:trust-boundary-doctrine-validation` and mandatory critique
`critique:trust-boundary-doctrine-review` support closure with no unresolved
findings.

# Evidence

Recorded: `evidence:trust-boundary-doctrine-validation`.

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

`critique:trust-boundary-doctrine-review` - no findings; mandatory critique
passed. Preliminary findings were repaired before final critique:

- `TRUSTBD2-ORC-001`: stale bootstrap preload/list surfaces. Repaired by
  `packet:ralph-ticket-trustbd2-20260503T042817Z` and refreshed evidence.
- `TRUSTBD2-ORC-002`: evidence was too summary-level. Repaired by refreshing
  `evidence:trust-boundary-doctrine-validation` with exact commands and outputs.
- `TRUSTBD2-ORC-003`: dropped `external_refs` code span. Repaired by
  `packet:ralph-ticket-trustbd2-20260503T042817Z`.
- `TRUSTBD2-ORC-004`: Claude hook preload omits `08-trust-boundaries.md`.
  Repaired by `packet:ralph-ticket-trustbd2-20260503T043735Z` and refreshed
  evidence.
- `TRUSTBD2-ORC-005`: `decision:0005` `updated_at` stale. Repaired by
  `packet:ralph-ticket-trustbd2-20260503T043735Z`.
- `TRUSTBD2-ORC-006`: internal adapter fixture docs still said "seven" current
  bootstrap references. Repaired by
  `packet:ralph-ticket-trustbd2-20260503T044557Z` and refreshed evidence.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Trust-boundary doctrine was promoted directly into mandatory bootstrap reference
  `skills/loom-bootstrap/references/08-trust-boundaries.md`.
- Related evidence, research, memory, and records-frontmatter surfaces now point
  to the bootstrap trust boundary while preserving their owner/support roles.
- Gemini and Claude bootstrap preload surfaces, install docs, constitutional
  decision metadata, and internal adapter fixtures were reconciled to the new
  ordered reference set.

Deferred / not-required rationale:

No separate wiki, research, spec, or memory record is needed. The durable lesson
is operational doctrine and lives in the bootstrap reference plus adjacent skill
surfaces.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
bootstrap reference.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T04:53:44Z
Basis: Ralph packets `packet:ralph-ticket-trustbd2-20260503T042019Z`,
`packet:ralph-ticket-trustbd2-20260503T042817Z`,
`packet:ralph-ticket-trustbd2-20260503T043735Z`, and
`packet:ralph-ticket-trustbd2-20260503T044557Z`; evidence
`evidence:trust-boundary-doctrine-validation`; mandatory critique
`critique:trust-boundary-doctrine-review` with no unresolved findings.
Residual risks: No automated secret scanning is introduced; this is intentional
doctrine-only behavior. Claude hook ordering remains best effort because
`SessionStart` hooks are concurrent, with source markers preserving attribution.

# Dependencies

- `ticket:bootinv1`

# Journal

- 2026-05-03T04:09:51Z: Created from council trust-boundary recommendation.
- 2026-05-03T04:20:19Z: Started Ralph iteration
  `packet:ralph-ticket-trustbd2-20260503T042019Z` from clean `main` at
  `fc29933`.
- 2026-05-03T04:22:51Z: Ralph iteration
  `packet:ralph-ticket-trustbd2-20260503T042019Z` completed in scope. Evidence
  recorded in `evidence:trust-boundary-doctrine-validation`; next route is
  mandatory critique.
- 2026-05-03T04:28:17Z: Initial mandatory critique found stale bootstrap preload
  surfaces, summary-level evidence detail, and one dropped `external_refs` code
  span. Parent compiled repair packet
  `packet:ralph-ticket-trustbd2-20260503T042817Z`.
- 2026-05-03T04:32:22Z: Ralph repair packet
  `packet:ralph-ticket-trustbd2-20260503T042817Z` consumed. Parent repaired one
  residual stale decision consequence bullet, refreshed evidence with exact query
  output, and routed back to mandatory critique.
- 2026-05-03T04:37:35Z: Mandatory critique returned `changes_requested` with
  `TRUSTBD2-ORC-004` and `TRUSTBD2-ORC-005`. Parent compiled Ralph repair packet
  `packet:ralph-ticket-trustbd2-20260503T043735Z`.
- 2026-05-03T04:40:39Z: Ralph repair packet
  `packet:ralph-ticket-trustbd2-20260503T043735Z` consumed. Evidence refreshed
  with Claude hook preload output, decision metadata, JSON parse check, and full
  diff whitespace check; routed back to mandatory critique.
- 2026-05-03T04:45:57Z: Mandatory critique returned `changes_requested` with
  `TRUSTBD2-ORC-006`. Parent compiled Ralph repair packet
  `packet:ralph-ticket-trustbd2-20260503T044557Z`.
- 2026-05-03T04:48:33Z: Ralph repair packet
  `packet:ralph-ticket-trustbd2-20260503T044557Z` consumed. Evidence refreshed
  with product/example stale-count wording search and routed back to mandatory
  critique.
- 2026-05-03T04:53:44Z: Mandatory critique
  `critique:trust-boundary-doctrine-review` passed with no unresolved findings.
  Parent recorded retrospective / promotion disposition and accepted closure.
