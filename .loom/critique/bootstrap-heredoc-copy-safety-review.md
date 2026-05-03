---
id: critique:bootstrap-heredoc-copy-safety-review
kind: critique
status: final
created_at: 2026-05-03T07:22:10Z
updated_at: 2026-05-03T07:22:10Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:bootdoc17 diff f93b432..working-tree"
links:
  ticket:
    - ticket:bootdoc17
  evidence:
    - evidence:bootstrap-heredoc-copy-safety-validation
  packet:
    - packet:ralph-ticket-bootdoc17-20260503T071649Z
external_refs: {}
---

# Summary

Mandatory oracle critique for `ticket:bootdoc17` after making the bootstrap
here-doc example copy-safe.

# Review Target

Current working-tree diff from baseline
`f93b432e6c9152ec7ac6db73ca381768ce83a8a2`, covering bootstrap filesystem
guidance, ticket reconciliation, Ralph packet consumption, and evidence.

Required critique profiles: `template-safety`, `operator-clarity`, and
`workflow-boundary`.

# Verdict

`pass` - no findings.

# Findings

None - no findings.

# Profile Results

- `template-safety`: pass. The example no longer writes to a literal
  `.loom/research/<slug>.md` path and scans the saved file for remaining
  placeholders.
- `operator-clarity`: pass. The sentinel slug, refusal branch, path variable, and
  local scan make the copy-before-replace failure mode visible without adding
  heavy process.
- `workflow-boundary`: pass. The change remains Markdown-native shell guidance
  and adds no command wrapper, runtime validator, schema engine, generated index,
  helper dependency, template rewrite, or broader template catalog.

# Evidence Reviewed

- Scoped working-tree diff for `ticket:bootdoc17` from
  `f93b432e6c9152ec7ac6db73ca381768ce83a8a2`.
- `skills/loom-bootstrap/references/06-filesystem-and-tooling.md:69-100`
- `ticket:bootdoc17`
- `packet:ralph-ticket-bootdoc17-20260503T071649Z`
- `evidence:bootstrap-heredoc-copy-safety-validation`
- Search for literal `.loom/research/<slug>.md` in the product reference: no
  matches.
- Search for forbidden additions in the edited bootstrap reference: no matches
  for command wrapper, runtime validator, schema engine, generated index, helper
  dependency, or template catalog.
- `git diff --check` on scoped files: passed with no output.
- `git diff --name-only f93b432... -- "skills/**/templates/**"`: no output.

# Acceptance Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-018`: supported.
- `ticket:bootdoc17#ACC-001`: supported. The here-doc no longer writes to a
  literal `<slug>` path.
- `ticket:bootdoc17#ACC-002`: supported. The example includes a local placeholder
  scan for the saved file.
- `ticket:bootdoc17#ACC-003`: supported. Bootstrap guidance remains concise and
  Markdown-native.
- `ticket:bootdoc17#ACC-004`: supported. Evidence records targeted searches,
  template-change check, and `git diff --check`.
- `ticket:bootdoc17#ACC-005`: supported after parent records this critique and
  closes the ticket-owned critique disposition.

# Residual Risks

- The placeholder scan is heuristic and runs after the file is written; operator
  review remains required before treating the saved record as truth.
- The here-doc is intentionally unquoted to interpolate `${slug}`. The current
  static body is safe enough, but operators should not pre-fill the here-doc body
  with `$()`, backticks, or variable-like text unless they intend shell expansion.
- Slug validation is sentinel-only; malformed but non-sentinel slugs can still
  produce odd filenames or IDs. This is acceptable for the narrower copy-safety
  scope.

# Required Follow-up

None for this ticket.

# Acceptance Recommendation

`no-critique-blockers`
