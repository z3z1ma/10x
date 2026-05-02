---
id: ticket:rtvocab1
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T18:58:43Z
updated_at: 2026-05-02T19:15:17Z
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
    - packet:ralph-ticket-rtvocab1-20260502T190248Z
  evidence:
    - evidence:route-vocabulary-validation
  critique:
    - critique:route-vocabulary-review
external_refs: {}
depends_on: []
---

# Summary

Create one canonical, grep-friendly route vocabulary and align drive, ticket,
workspace, and template route wording to it.

# Context

Council finding `CR-001` found route tokens drifting across drive/checkpoint,
ticket readiness, workspace status, and examples: `ask_user`, `ask-user`, `ask
user`, `Ralph`, `acceptance`, `acceptance_review`, `continue`, and related prose.

# Why Now

Route vocabulary is foundational. Later tickets should inherit one safe route
grammar instead of normalizing around drift.

# Scope

- Define a canonical route vocabulary in an owner-appropriate shared reference.
- Update downstream route examples in `loom-drive`, `loom-tickets`,
  `loom-workspace`, and affected templates.
- Preserve route readability without turning every normal sentence into an enum.
- Keep workflow routes separate from command or adapter invocation names.

# Out Of Scope

- Do not add a runtime validator or command router.
- Do not change ticket state-machine statuses unless required by route grammar.
- Do not rename existing record kinds or workflow skills.

# Acceptance Criteria

- ACC-001: A single shared route-vocabulary reference or section owns the route
  tokens used for next-route/checkpoint/resume guidance.
- ACC-002: Drive, ticket, and workspace route examples align with the shared
  vocabulary.
- ACC-003: Route vocabulary stays distinct from ticket lifecycle statuses,
  command names, and adapter invocation surfaces.
- ACC-004: Evidence records before/after token searches and `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-council-precision-pass#OBJ-001`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-council-precision-pass#OBJ-001` | `evidence:route-vocabulary-validation` | `critique:route-vocabulary-review` with finding resolved and re-check passed | supported |
| `ticket:rtvocab1#ACC-001` | `evidence:route-vocabulary-validation` | `critique:route-vocabulary-review` | supported |
| `ticket:rtvocab1#ACC-002` | `evidence:route-vocabulary-validation` | `critique:route-vocabulary-review` | supported |
| `ticket:rtvocab1#ACC-003` | `evidence:route-vocabulary-validation` | `critique:route-vocabulary-review` | supported |
| `ticket:rtvocab1#ACC-004` | `evidence:route-vocabulary-validation` | `critique:route-vocabulary-review` | supported |
| `ticket:rtvocab1#ACC-005` | `critique:route-vocabulary-review` | `critique:route-vocabulary-review#RTVOCAB1-FIND-001` resolved and oracle re-check passed with no findings | supported |

# Execution Notes

Likely touched surfaces include `skills/loom-records`, `skills/loom-drive`,
`skills/loom-tickets`, `skills/loom-workspace`, and route-bearing templates.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:supp0x2a`.

# Route Readiness

Route: acceptance_review

Ralph readiness: N/A - implementation iteration completed.

Direct critique readiness:
N/A - mandatory oracle critique and re-check passed.

Acceptance review readiness:
Evidence and critique disposition: `evidence:route-vocabulary-validation` and
`critique:route-vocabulary-review` support acceptance with no remaining findings.
Residual risks: future route-bearing edits outside this scope should cite or
extend `skills/loom-records/references/route-vocabulary.md`.

# Evidence

Recorded: `evidence:route-vocabulary-validation` with targeted before/after
route-token searches, manual comparison of shared route grammar against
downstream examples, and `git diff --check`.

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: route vocabulary affects checkpoint recovery and workflow
routing safety.

Required critique profiles:

- protocol-change
- operator-clarity
- routing-safety

Findings:

Recorded in `critique:route-vocabulary-review`:

- `critique:route-vocabulary-review#RTVOCAB1-FIND-001` - resolved by packet
  lifecycle reconciliation.

Disposition status: completed

Deferral / not-required rationale:

Not deferred. Oracle critique and re-check passed with no remaining findings.

# Wiki Disposition

Retrospective / promotion disposition complete. Durable route-vocabulary learning
was promoted directly into `skills/loom-records/references/route-vocabulary.md`
and linked from downstream drive, ticket, and workspace owner surfaces. No
separate wiki page, research record, spec, constitution decision, or memory entry
is needed for this ticket.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-02T19:15:17Z
Basis: Ralph packet `packet:ralph-ticket-rtvocab1-20260502T190248Z`; evidence
`evidence:route-vocabulary-validation`; oracle critique
`critique:route-vocabulary-review` with `RTVOCAB1-FIND-001` resolved and final
re-check passing with no findings.
Residual risks: route-bearing edits outside this ticket's scoped surfaces should
cite or extend the shared route vocabulary rather than inventing local tokens.

# Dependencies

None.

# Journal

- 2026-05-02T18:58:43Z: Created from council finding `CR-001`.
- 2026-05-02T19:02:48Z: Started Ralph iteration
  `packet:ralph-ticket-rtvocab1-20260502T190248Z` from baseline
  `86b74e39009eb4eeec4722bec9799f4bbc12705b`.
- 2026-05-02T19:05:00Z: Ralph child normalized route vocabulary, recorded
  `evidence:route-vocabulary-validation`, and moved ticket to `review_required`
  for mandatory oracle critique. Do not close until `ticket:rtvocab1#ACC-005`
  is satisfied and critique findings are dispositioned.
- 2026-05-02T19:13:21Z: Oracle critique found packet lifecycle reconciliation
  issue `RTVOCAB1-FIND-001`. Parent marked packet
  `packet:ralph-ticket-rtvocab1-20260502T190248Z` consumed and recorded critique;
  final oracle re-check remains next.
- 2026-05-02T19:15:17Z: Oracle re-check passed with no findings. Recorded
  acceptance and retrospective disposition; closed ticket.
