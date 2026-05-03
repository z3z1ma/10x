---
id: ticket:evfresh8
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T00:56:36Z
updated_at: 2026-05-03T02:50:42Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  plan:
    - plan:skills-corpus-residual-protocol-sharpening-pass
  research:
    - research:skills-corpus-residual-audit-synthesis
  packet:
    - packet:ralph-ticket-evfresh8-20260503T024435Z
  evidence:
    - evidence:evidence-freshness-validation
  critique:
    - critique:evidence-freshness-review
external_refs: {}
depends_on: []
---

# Summary

Strengthen evidence freshness metadata and negative-evidence examples.

# Context

Older audit action 7 found that evidence freshness doctrine exists but the
template could make source state, command/procedure, exit code/verdict, raw
artifacts, and challenging evidence more visible.

# Why Now

Evidence supports acceptance, critique, and wiki/research claims. If freshness and
challenge paths are under-specified, agents can overclaim green evidence or miss
observations that falsify a claim.

# Scope

- Add observation metadata or equivalent fields to the evidence template.
- Make freshness fields harder to skip.
- Add a negative/challenging evidence example in claim coverage or evidence
  guidance.
- Preserve evidence as observed artifact truth, not acceptance or critique truth.

# Out Of Scope

- Do not require every evidence record to store full raw logs inline.
- Do not make evidence own intended behavior, critique verdicts, or ticket closure.

# Acceptance Criteria

- ACC-001: Evidence template asks for observed-at/source-state/procedure/verdict
  or equivalent metadata.
- ACC-002: Evidence template makes freshness, invalidation, and recheck triggers
  explicit.
- ACC-003: Claim coverage or evidence guidance includes a concrete challenge
  example for negative evidence.
- ACC-004: Evidence records before/after evidence freshness/challenge searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-010`
- `ticket:evfresh8#ACC-001`
- `ticket:evfresh8#ACC-002`
- `ticket:evfresh8#ACC-003`
- `ticket:evfresh8#ACC-004`
- `ticket:evfresh8#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-010` | `evidence:evidence-freshness-validation` | `critique:evidence-freshness-review` | supported |
| `ticket:evfresh8#ACC-001` through `ticket:evfresh8#ACC-005` | `evidence:evidence-freshness-validation` | `critique:evidence-freshness-review` | supported |

# Execution Notes

Likely touched surfaces include `skills/loom-evidence/templates/evidence.md`,
`skills/loom-evidence/SKILL.md`, and
`skills/loom-records/references/claim-coverage.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:srcmeta13`.

Ralph packet `packet:ralph-ticket-evfresh8-20260503T024435Z` was consumed in
scope, evidence was recorded, oracle critique passed with no findings, and
acceptance is complete.

# Route Readiness

Acceptance review readiness:

Evidence `evidence:evidence-freshness-validation` and oracle critique
`critique:evidence-freshness-review` support closure with no findings.

# Evidence

Recorded: `evidence:evidence-freshness-validation`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: evidence freshness and negative evidence directly affect
acceptance honesty.

Required critique profiles:

- evidence-quality
- closure-honesty
- operator-clarity

Findings:

`critique:evidence-freshness-review` - no findings; mandatory oracle critique
passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Evidence freshness metadata prompts were promoted directly into the evidence
  template and evidence skill procedure.
- The concrete challenging-evidence example was promoted into evidence-quality
  guidance.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the product guidance itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
touched evidence template and references.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T02:50:42Z
Basis: Ralph packet `packet:ralph-ticket-evfresh8-20260503T024435Z`; evidence
`evidence:evidence-freshness-validation`; oracle critique
`critique:evidence-freshness-review` with no findings.
Residual risks: validation is structural/manual; no validator enforces evidence
fields. Correct use still depends on operators replacing placeholders honestly
when creating evidence records.

# Dependencies

None.

# Journal

- 2026-05-03T00:56:36Z: Created from older audit action 7.
- 2026-05-03T02:44:36Z: Marked active and compiled Ralph packet
  `packet:ralph-ticket-evfresh8-20260503T024435Z` for evidence freshness
  metadata and challenging-evidence examples.
- 2026-05-03T02:47:50Z: Ralph iteration
  `packet:ralph-ticket-evfresh8-20260503T024435Z` completed in scope. Evidence
  recorded in `evidence:evidence-freshness-validation`; next route is mandatory
  oracle critique.
- 2026-05-03T02:50:42Z: Mandatory oracle critique
  `critique:evidence-freshness-review` passed with no findings. Parent recorded
  retrospective / promotion disposition and accepted closure.
