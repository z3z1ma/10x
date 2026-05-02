---
id: ticket:795fa0f4
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
  - ticket:1a12d9ff
---

# Summary

Clarify memory pruning, promotion, optionality, and frontmatter/status
expectations so memory remains useful support recall without becoming project
truth.

# Context

The council found that memory's boundary is strong but still under-specified in
two areas: pruning cadence and frontmatter/status exceptions. Recent memory work
sharpened the support-recall model, so this ticket should be a small alignment
pass rather than another broad memory rewrite.

# Why Now

Resume, compaction, scratchpad routing, and record validation all touch memory.
If memory's structure and pruning rules remain implicit, future agents may either
over-validate support files as canonical records or let stale memory become shadow
truth.

# Scope

- Clarify when memory can be pruned, promoted, linked, or left stale.
- Tie memory pruning or promotion to ticket closure or retrospective when that is
  the clearest route.
- Clarify whether memory records require common frontmatter or may remain lighter
  support recall files.
- Ensure memory optionality is framed as a correctness boundary: absent or stale
  memory cannot make canonical project truth false.
- Align `loom-memory` with any memory exception wording added by
  `ticket:4e8ebe92`.

# Non-goals

- Do not make memory canonical project truth.
- Do not add memory indexing, embeddings, databases, scripts, or required runtime
  behavior.
- Do not rewrite every historical `.loom/memory` file.
- Do not duplicate the full cold-start resume route.

# Acceptance Criteria

- ACC-001: `loom-memory` explains pruning, promotion, linking, and stale-memory
  handling in practical terms.
- ACC-002: Memory frontmatter/status expectations are consistent with
  `loom-records` guidance.
- ACC-003: Memory optionality remains a correctness boundary, not a claim that
  memory is useless.
- ACC-004: Memory does not become a second live task ledger, evidence store, wiki,
  research log, or ticket substitute.
- ACC-005: Any pruning or promotion cadence is tied to existing owner workflows
  such as ticket closure or retrospective.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening#OBJ-003`
- `research:skills-corpus-council-review#CLAIM-007`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening#OBJ-003` | implementation evidence pending | critique recommended | open |
| `research:skills-corpus-council-review#CLAIM-007` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | critique recommended | supported_pending_review |

# Execution Notes

Start from the current memory support-layer contract. This is a precision pass,
not a conceptual redesign.

# Blockers

Do not start until `ticket:4e8ebe92` and `ticket:1a12d9ff` have landed or been
intentionally deferred.

# Next Move / Next Route

Ralph implementation packet or local edit for memory boundary precision.

# Ralph Readiness

Bounded iteration:

Clarify memory pruning, promotion, optionality, and frontmatter/status
expectations.

Write boundary:

- `skills/loom-memory/**`
- targeted `skills/loom-records/**` pointers only if needed for consistency
- targeted `skills/loom-retrospective/**` pointers only if pruning/promotion is
  tied to retrospective

Likely verification posture:

Observation-first structural validation.

Expected output contract:

- changed files,
- explicit memory structure/pruning rule,
- validation output,
- no-runtime/no-shadow-truth check.

# Evidence

Expected:

- `git diff --check`
- targeted grep checks for prune, promotion, frontmatter, status, optionality,
  stale memory, second-ledger, and canonical-truth wording
- manual check against the existing memory support-layer records

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:

This changes support-layer operator guidance but should preserve the already
accepted memory boundary.

Required critique profiles:

- operator-clarity
- protocol-change if memory frontmatter expectations change materially

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None yet.

# Wiki Disposition

Likely deferred unless implementation surfaces a reusable memory maintenance
pattern not captured by the skill references.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

- `ticket:4e8ebe92`
- `ticket:1a12d9ff`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the memory pruning and frontmatter expectation slice.
