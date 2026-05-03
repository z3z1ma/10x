---
id: ticket:bootdoc17
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T07:22:10Z
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
    - critique:bootstrap-heredoc-copy-safety-review
external_refs: {}
depends_on:
  - ticket:shipacc1
---

# Summary

Make the bootstrap here-doc file creation example copy-safe.

# Context

Bootstrap tooling warns placeholders must be replaced, but its research here-doc
example still writes to a literal `.loom/research/<slug>.md` path if copied.

# Why Now

Bootstrap examples are high-leverage copy surfaces for fresh agents.

# Scope

- Replace the literal placeholder path with a safer variable pattern.
- Keep a local placeholder scan near the example.
- Preserve Markdown-native shell guidance without adding helpers.

# Out Of Scope

- Do not add a command wrapper or runtime validator.
- Do not expand bootstrap into a full template catalog.

# Acceptance Criteria

- ACC-001: Bootstrap here-doc example no longer writes to literal `<slug>` path.
- ACC-002: Example includes or points to a local placeholder scan for the saved
  file.
- ACC-003: Bootstrap remains concise and Markdown-native.
- ACC-004: Evidence records targeted copy-safety searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-018`
- `ticket:bootdoc17#ACC-001`
- `ticket:bootdoc17#ACC-002`
- `ticket:bootdoc17#ACC-003`
- `ticket:bootdoc17#ACC-004`
- `ticket:bootdoc17#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-018` | `evidence:bootstrap-heredoc-copy-safety-validation` | `critique:bootstrap-heredoc-copy-safety-review` | supported |
| `ticket:bootdoc17#ACC-001` | `evidence:bootstrap-heredoc-copy-safety-validation` | `critique:bootstrap-heredoc-copy-safety-review` | supported |
| `ticket:bootdoc17#ACC-002` | `evidence:bootstrap-heredoc-copy-safety-validation` | `critique:bootstrap-heredoc-copy-safety-review` | supported |
| `ticket:bootdoc17#ACC-003` | `evidence:bootstrap-heredoc-copy-safety-validation` | `critique:bootstrap-heredoc-copy-safety-review` | supported |
| `ticket:bootdoc17#ACC-004` | `evidence:bootstrap-heredoc-copy-safety-validation` | `critique:bootstrap-heredoc-copy-safety-review` | supported |
| `ticket:bootdoc17#ACC-005` | `evidence:bootstrap-heredoc-copy-safety-validation` | `critique:bootstrap-heredoc-copy-safety-review` | supported |

# Execution Notes

Likely touched file: `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:rsrcmt18`.

Ralph packet `packet:ralph-ticket-bootdoc17-20260503T071649Z` completed in
scope, evidence was recorded, mandatory critique passed with no findings, and
acceptance is complete.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:bootstrap-heredoc-copy-safety-validation` and mandatory
critique `critique:bootstrap-heredoc-copy-safety-review` support closure.

# Evidence

Recorded:

- `evidence:bootstrap-heredoc-copy-safety-validation`

The evidence records targeted searches for literal `<slug>` output paths, the
path variable, local placeholder scan, forbidden additions, template changes, and
`git diff --check`.

# Critique Disposition

Risk class: medium

Critique policy: mandatory

Policy rationale: bootstrap examples are copied by cold agents.

Required critique profiles:

- template-safety
- operator-clarity
- workflow-boundary

Findings:

- `critique:bootstrap-heredoc-copy-safety-review` - no findings; mandatory
  critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Copy-safe bootstrap here-doc guidance was promoted into
  `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to bootstrap filesystem/tooling guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in
bootstrap filesystem/tooling guidance.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T07:22:10Z
Basis: Ralph packet `packet:ralph-ticket-bootdoc17-20260503T071649Z`; evidence
`evidence:bootstrap-heredoc-copy-safety-validation`; mandatory critique
`critique:bootstrap-heredoc-copy-safety-review` with no findings.
Residual risks: The placeholder scan is heuristic and post-write; the here-doc is
intentionally unquoted to interpolate `${slug}`; slug validation is sentinel-only.
These are acceptable for the scoped copy-safety guidance change.

# Dependencies

- `ticket:shipacc1`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass audit finding 6.
- 2026-05-03T07:16:49Z: Started Ralph iteration
  `packet:ralph-ticket-bootdoc17-20260503T071649Z` from clean `main` at
  `f93b432`.
- 2026-05-03T07:18:35Z: Ralph iteration consumed. Product edit landed inside
  packet write scope, `evidence:bootstrap-heredoc-copy-safety-validation`
  recorded, and ticket moved to `review_required` for mandatory critique.
- 2026-05-03T07:22:10Z: Mandatory critique
  `critique:bootstrap-heredoc-copy-safety-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
