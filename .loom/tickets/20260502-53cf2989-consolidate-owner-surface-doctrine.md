---
id: ticket:53cf2989
kind: ticket
status: ready
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T09:28:53Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  roadmap:
    - roadmap:bootstrap-the-markdown-first-protocol-corpus
  initiative:
    - initiative:skills-corpus-protocol-sharpening
  research:
    - research:skills-corpus-council-review
  evidence:
    - evidence:skills-corpus-council-review
  plan:
    - plan:skills-corpus-protocol-sharpening
  supersedes:
    - ticket:3uv5l5fh
external_refs: {}
depends_on:
  - ticket:4e8ebe92
---

# Summary

Consolidate duplicated atlas, retrospective, spike/sketch, and skill metadata
doctrine under the owner skill that should teach each shape.

# Context

The council found several duplication hotspots. Atlas guidance appears across
codemap and wiki surfaces. Retrospective mechanics are spread between records and
retrospective guidance. Spike/sketch variants appear in research and spike
surfaces. Skill metadata conventions need an explicit owner in skill authoring.

# Why Now

Duplication makes the corpus harder to keep perfect. This slice should reduce
drift by assigning each repeated doctrine area one clear owner surface and
replacing duplicate detail with pointers where appropriate.

# Scope

- Make atlas page shape canonical in the wiki surface, then point codemap guidance
  to that owner shape while preserving codemap's evidence/research/wiki route.
- Move or point retrospective mechanics to `loom-retrospective`, keeping
  `loom-records` focused on shared grammar and validation.
- Let `loom-research` define spike/sketch as research variants at a high level;
  let `loom-spike` own procedural workflow detail.
- Tighten `loom-skill-authoring` metadata guidance for `skill_kind`,
  `compatibility`, activation descriptions, and skill frontmatter expectations.
- Preserve useful domain nuance before deleting or shortening duplicated text.

# Non-goals

- Do not remove doctrine merely because it is repeated; first make sure the owner
  surface contains the needed instruction.
- Do not change atlas, retrospective, spike, or sketch into new canonical layers.
- Do not rewrite all skill metadata by hand unless the owner guidance requires a
  minimal consistency fix.
- Do not update examples broadly; create follow-up work if fixtures become stale.

# Acceptance Criteria

- ACC-001: Atlas shape has one clear owner surface, with codemap pointing to it
  rather than teaching a competing full shape.
- ACC-002: Retrospective workflow mechanics are owned by `loom-retrospective`, with
  `loom-records` retaining only shared grammar or pointer guidance.
- ACC-003: Spike/sketch guidance distinguishes research-owned truth from
  spike-owned workflow procedure without duplicating full instructions.
- ACC-004: `loom-skill-authoring` defines or explicitly leaves open `skill_kind`,
  `compatibility`, and related metadata conventions.
- ACC-005: Targeted searches show no obvious stale duplicate doctrine left in the
  touched surfaces.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening#OBJ-004`
- `research:skills-corpus-council-review#CLAIM-008`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening#OBJ-004` | implementation evidence pending | critique recommended | open |
| `research:skills-corpus-council-review#CLAIM-008` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | critique recommended | supported_pending_review |

# Execution Notes

This is a consolidation pass. It should make owner boundaries clearer without
turning pointers into vague cross-references that force future agents to chase too
many files.

# Blockers

Do not start until `ticket:4e8ebe92` lands or is intentionally deferred, because
metadata and record-owner wording may depend on shared grammar.

# Next Move / Next Route

Ralph implementation packet or local edit for owner-surface consolidation.

# Ralph Readiness

Bounded iteration:

Consolidate duplicated atlas, retrospective, spike/sketch, and metadata doctrine.

Write boundary:

- `skills/loom-wiki/**`
- `skills/loom-codemap/**`
- `skills/loom-retrospective/**`
- `skills/loom-records/**`
- `skills/loom-research/**`
- `skills/loom-spike/**`
- `skills/loom-skill-authoring/**`

Likely verification posture:

Observation-first structural validation.

Expected output contract:

- changed files,
- owner surface chosen for each duplicated doctrine area,
- removed/replaced duplicate wording summary,
- validation output.

# Evidence

Expected:

- `git diff --check`
- targeted grep checks for atlas, retrospective, spike, sketch, `skill_kind`, and
  `compatibility`
- manual comparison against owner-surface acceptance criteria

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:

This changes workflow doctrine placement and could lose nuance if consolidation is
too aggressive.

Required critique profiles:

- operator-clarity
- routing-safety

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None yet.

# Wiki Disposition

Pending. Consolidation itself should usually live in skills, but accepted atlas
or retrospective concepts may already belong in wiki if they are reusable
explanations.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

- `ticket:4e8ebe92`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the owner-surface consolidation slice.
