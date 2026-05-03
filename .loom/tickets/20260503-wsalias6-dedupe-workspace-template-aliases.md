---
id: ticket:wsalias6
kind: ticket
status: closed
change_class: record-hygiene
risk_class: low
created_at: 2026-05-03T00:56:36Z
updated_at: 2026-05-03T02:22:39Z
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
    - packet:ralph-ticket-wsalias6-20260503T021836Z
  evidence:
    - evidence:workspace-alias-template-validation
  critique:
    - critique:workspace-alias-template-review
external_refs: {}
depends_on: []
---

# Summary

Deduplicate `repo_aliases` in the workspace template so frontmatter is the single
authoritative alias surface.

# Context

Council finding `NC2-006` found the workspace template duplicates `repo_aliases`
in frontmatter and body YAML, which can drift if a fresh agent edits only one.

# Why Now

Workspace metadata supports scope recovery. Duplicated alias truth in a template
undermines the frontmatter/body boundary.

# Scope

- Keep frontmatter `repo_aliases` authoritative.
- Replace or simplify the body YAML duplicate with prose that points to
  frontmatter.
- Preserve workspace support-only truth boundaries.

# Out Of Scope

- Do not change workspace ID shape or scope semantics.
- Do not make workspace metadata canonical project truth.

# Acceptance Criteria

- ACC-001: Workspace template no longer duplicates `repo_aliases` as a second YAML
  body block.
- ACC-002: Workspace template clearly points readers to frontmatter for aliases.
- ACC-003: Workspace notes still say aliases do not own project behavior,
  strategy, or execution truth.
- ACC-004: Evidence records before/after workspace template searches and
  `git diff --check`.
- ACC-005: Oracle critique passes with no unresolved findings.

# Coverage

Covers:

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-008`
- `ticket:wsalias6#ACC-001`
- `ticket:wsalias6#ACC-002`
- `ticket:wsalias6#ACC-003`
- `ticket:wsalias6#ACC-004`
- `ticket:wsalias6#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-008` | `evidence:workspace-alias-template-validation` | `critique:workspace-alias-template-review` | supported |
| `ticket:wsalias6#ACC-001` through `ticket:wsalias6#ACC-005` | `evidence:workspace-alias-template-validation` | `critique:workspace-alias-template-review` | supported |

# Execution Notes

Likely touched surface is `skills/loom-workspace/templates/workspace.md`.

# Blockers

None.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:pktmeta12`.

# Route Readiness

Acceptance review readiness:
Evidence `evidence:workspace-alias-template-validation` and oracle critique
`critique:workspace-alias-template-review` support closure with no findings.

# Evidence

Recorded: `evidence:workspace-alias-template-validation`.

# Critique Disposition

Risk class: low

Critique policy: mandatory

Policy rationale: user instruction requires oracle critique for every ticket;
template duplication can create graph drift.

Required critique profiles:

- template-safety
- owner-boundary

Findings:

`critique:workspace-alias-template-review` - no findings; mandatory oracle
critique passed.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Workspace alias dedupe guidance was promoted directly into the workspace
  template by making frontmatter the authoritative alias surface.

Deferred / not-required rationale:

No separate wiki page, research record, spec, constitution decision, or memory
entry is needed. The durable lesson is the product guidance itself.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in the
workspace template.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T02:22:39Z
Basis: Ralph packet `packet:ralph-ticket-wsalias6-20260503T021836Z`; evidence
`evidence:workspace-alias-template-validation`; oracle critique
`critique:workspace-alias-template-review` with no findings.
Residual risks: validation is structural/manual; there is no automated
protocol-template test suite.

# Dependencies

None.

# Journal

- 2026-05-03T00:56:36Z: Created from council finding `NC2-006`.
- 2026-05-03T02:19:58Z: Ralph iteration
  `packet:ralph-ticket-wsalias6-20260503T021836Z` completed in scope. Evidence
  recorded in `evidence:workspace-alias-template-validation`; next route is
  mandatory oracle critique.
- 2026-05-03T02:22:39Z: Mandatory oracle critique
  `critique:workspace-alias-template-review` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
