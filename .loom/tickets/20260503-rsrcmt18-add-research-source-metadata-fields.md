---
id: ticket:rsrcmt18
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T07:28:48Z
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
    - critique:research-template-source-metadata-review
external_refs: {}
depends_on:
  - ticket:shipacc1
---

# Summary

Add copyable source metadata fields to the research template.

# Context

Research source-handling doctrine is stronger than the template's prose-only
`# Sources` section.

# Why Now

Research is a primary place where external documents can accidentally become
shadow truth if provenance, freshness, and trust limits are not explicit.

# Scope

- Add source metadata prompts to `skills/loom-research/templates/research.md`.
- Align fields with source-handling doctrine.

# Out Of Scope

- Do not require full raw source dumps.
- Do not make external sources canonical project truth.

# Acceptance Criteria

- ACC-001: Research template prompts for title/type, URL or path, observed time,
  version/date/commit, freshness risk, recheck trigger, and trust rationale.
- ACC-002: Template preserves research as evidence synthesis, not external source
  authority.
- ACC-003: Source-handling reference remains consistent with template fields.
- ACC-004: Evidence records targeted source metadata searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-019`
- `ticket:rsrcmt18#ACC-001`
- `ticket:rsrcmt18#ACC-002`
- `ticket:rsrcmt18#ACC-003`
- `ticket:rsrcmt18#ACC-004`
- `ticket:rsrcmt18#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-019` | `evidence:research-template-source-metadata-validation` | `critique:research-template-source-metadata-review` | supported |
| `ticket:rsrcmt18#ACC-001` | `evidence:research-template-source-metadata-validation` | `critique:research-template-source-metadata-review` | supported |
| `ticket:rsrcmt18#ACC-002` | `evidence:research-template-source-metadata-validation` | `critique:research-template-source-metadata-review` | supported |
| `ticket:rsrcmt18#ACC-003` | `evidence:research-template-source-metadata-validation` | `critique:research-template-source-metadata-review` | supported |
| `ticket:rsrcmt18#ACC-004` | `evidence:research-template-source-metadata-validation` | `critique:research-template-source-metadata-review` | supported |
| `ticket:rsrcmt18#ACC-005` | `evidence:research-template-source-metadata-validation` | `critique:research-template-source-metadata-review` | supported |

# Execution Notes

Likely touched file: `skills/loom-research/templates/research.md`; source-handling
reference only if alignment wording is needed.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:pktws19`.

Ralph packet `packet:ralph-ticket-rsrcmt18-20260503T072340Z` completed in scope,
evidence was recorded, mandatory critique passed with no findings, and acceptance
is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:research-template-source-metadata-validation` and mandatory
critique `critique:research-template-source-metadata-review` support closure.

# Evidence

Recorded:

- `evidence:research-template-source-metadata-validation`

The evidence records targeted searches for source metadata fields,
freshness/recheck/trust wording, source authority boundary, forbidden additions,
and `git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: research source metadata affects external-source trust.

Required critique profiles:

- trust-boundary
- operator-clarity
- template-safety

Findings:

- `critique:research-template-source-metadata-review` - no findings; mandatory
  critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Research template source metadata prompts were promoted into
  `skills/loom-research/templates/research.md`.
- Field alignment was promoted into
  `skills/loom-research/references/source-handling.md`.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to research template and source-handling guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
research template and source-handling guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T07:28:48Z
Basis: Ralph packet `packet:ralph-ticket-rsrcmt18-20260503T072340Z`; evidence
`evidence:research-template-source-metadata-validation`; mandatory critique
`critique:research-template-source-metadata-review` with no findings.
Residual risks: Future research quality depends on operators filling metadata
honestly when source-dependent claims matter. Template prompts are lightweight and
do not enforce correctness by themselves.

# Dependencies

- `ticket:shipacc1`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass audit finding 7.
- 2026-05-03T07:23:41Z: Started Ralph iteration
  `packet:ralph-ticket-rsrcmt18-20260503T072340Z` from clean `main` at
  `bbe01ec`.
- 2026-05-03T07:25:10Z: Ralph iteration consumed. Product edits landed inside
  packet write scope, `evidence:research-template-source-metadata-validation`
  recorded, and ticket moved to `review_required` for mandatory critique.
- 2026-05-03T07:28:48Z: Mandatory critique
  `critique:research-template-source-metadata-review` passed with no findings.
  Parent recorded retrospective / promotion disposition and accepted closure.
