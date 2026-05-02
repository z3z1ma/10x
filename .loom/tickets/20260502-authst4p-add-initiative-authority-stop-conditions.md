---
id: ticket:authst4p
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T18:58:43Z
updated_at: 2026-05-02T19:51:50Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  packet:
    - packet:ralph-ticket-authst4p-20260502T194511Z
  evidence:
    - evidence:initiative-authority-stop-conditions-validation
  critique:
    - critique:initiative-authority-stop-conditions-review
external_refs: {}
depends_on:
  - ticket:rtvocab1
---

# Summary

Add initiative guidance for delegated autonomy, authority limits, and objective
level stop conditions.

# Context

Council finding `CR-004` found `loom-drive` says initiatives own delegated
autonomy and objective-level stop conditions, but initiative template/reference do
not cue those fields.

# Why Now

Autonomous drive sessions should not rely on transcript memory for authority
boundaries.

# Scope

- Add optional delegated authority and stop-condition prompts to initiative
  template/reference.
- Align drive continuity contract with the initiative template language.
- Keep the section optional for non-drive initiatives.

# Out Of Scope

- Do not require all initiatives to use autonomous drive.
- Do not grant autonomy outside recorded user delegation.
- Do not create a new authority record type.

# Acceptance Criteria

- ACC-001: Initiative template cues delegated authority/autonomy limits and
  objective-level stop conditions.
- ACC-002: Initiative reference explains when the fields are required or optional.
- ACC-003: Drive continuity guidance points to the same owner fields.
- ACC-004: Evidence records before/after authority/stop-condition searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-council-precision-pass#OBJ-004`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-council-precision-pass#OBJ-004` | `evidence:initiative-authority-stop-conditions-validation` | `critique:initiative-authority-stop-conditions-review` | supported |
| `ticket:authst4p#ACC-001` | `evidence:initiative-authority-stop-conditions-validation` | `critique:initiative-authority-stop-conditions-review` | supported |
| `ticket:authst4p#ACC-002` | `evidence:initiative-authority-stop-conditions-validation` | `critique:initiative-authority-stop-conditions-review` | supported |
| `ticket:authst4p#ACC-003` | `evidence:initiative-authority-stop-conditions-validation` | `critique:initiative-authority-stop-conditions-review` | supported |
| `ticket:authst4p#ACC-004` | `evidence:initiative-authority-stop-conditions-validation` | `critique:initiative-authority-stop-conditions-review` | supported |
| `ticket:authst4p#ACC-005` | `critique:initiative-authority-stop-conditions-review` | `critique:initiative-authority-stop-conditions-review` passed with no findings | supported |

# Execution Notes

Likely touched surfaces include `skills/loom-initiatives/templates/initiative.md`,
`skills/loom-initiatives/references/initiative-shape.md`, and `skills/loom-drive/references/continuity-contract.md`.

# Blockers

None - `ticket:rtvocab1` is closed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:pktgram5`.

# Route Readiness

Route: acceptance_review

Acceptance review readiness:
Evidence and critique disposition: `evidence:initiative-authority-stop-conditions-validation`
and `critique:initiative-authority-stop-conditions-review` support acceptance
with no findings.
Residual risks: default initiative templates now include optional drive fields
that ordinary non-drive initiatives may leave unused; the template/reference
explicitly state optionality.

# Evidence

Recorded:

- `evidence:initiative-authority-stop-conditions-validation` - before/after
  delegated-authority/autonomy, human-decision trigger, budget/time, and
  objective-level stop-condition observations plus `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: this governs autonomous objective boundaries.

Required critique profiles:

- protocol-change
- operator-clarity
- routing-safety

Findings:

Recorded in `critique:initiative-authority-stop-conditions-review`:

- None - no findings.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Mandatory oracle critique passed with no findings.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Delegated authority/autonomy and objective-level stop-condition guidance was
  promoted into `skills/loom-initiatives/templates/initiative.md`,
  `skills/loom-initiatives/references/initiative-shape.md`, `skills/loom-drive/SKILL.md`,
  `skills/loom-drive/references/continuity-contract.md`,
  `skills/loom-drive/references/drive-loop.md`, and
  `skills/loom-drive/references/checkpoint-resume-protocol.md`.

Deferred / not-required rationale:

Not deferred. The durable lesson was promoted directly into the owner product
surfaces listed above; no separate wiki page, research record, spec,
constitution decision, or memory entry is needed.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation is now in the
initiative and drive owner surfaces.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T19:51:50Z
Basis: Ralph packet `packet:ralph-ticket-authst4p-20260502T194511Z`; evidence
`evidence:initiative-authority-stop-conditions-validation`; oracle critique
`critique:initiative-authority-stop-conditions-review` with no findings.
Residual risks: default initiative templates now include optional drive fields
that ordinary non-drive initiatives may leave unused; the template/reference
explicitly state optionality.

# Dependencies

- `ticket:rtvocab1`

# Journal

- 2026-05-02T18:58:43Z: Created from council finding `CR-004`.
- 2026-05-02T19:45:43Z: Started Ralph iteration
  `packet:ralph-ticket-authst4p-20260502T194511Z` from baseline
  `d98a2ef2a26a8519675235fc4c6624a8ab921a93`.
- 2026-05-02T19:46:59Z: Ralph iteration landed scoped initiative/drive guidance
  edits and recorded `evidence:initiative-authority-stop-conditions-validation`.
  Ticket moved to `review_required`; mandatory critique remains pending.
- 2026-05-02T19:51:50Z: Oracle critique passed with no findings. Recorded
  acceptance and retrospective / promotion disposition; closed ticket.
