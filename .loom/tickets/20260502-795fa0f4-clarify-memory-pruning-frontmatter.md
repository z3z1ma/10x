---
id: ticket:795fa0f4
kind: ticket
status: closed
change_class: protocol-authority
risk_class: medium
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T10:50:58Z
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
    - evidence:memory-pruning-frontmatter-validation
  critique:
    - critique:memory-pruning-frontmatter-review
  packet:
    - packet:ralph-ticket-795fa0f4-20260502T104301Z
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
| `initiative:skills-corpus-protocol-sharpening#OBJ-003` | `evidence:memory-pruning-frontmatter-validation` | `critique:memory-pruning-frontmatter-review` | supported |
| `research:skills-corpus-council-review#CLAIM-007` | `evidence:skills-corpus-council-review`; `evidence:memory-pruning-frontmatter-validation` | `critique:memory-pruning-frontmatter-review` | supported |

# Execution Notes

Start from the current memory support-layer contract. This is a precision pass,
not a conceptual redesign.

# Blockers

None. Dependencies `ticket:4e8ebe92` and `ticket:1a12d9ff` are closed.

# Next Move / Next Route

Closed. Continue with the next sequenced plan ticket, `ticket:53cf2989`.

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

Recorded:

- `evidence:memory-pruning-frontmatter-validation`
- `git diff --check` passed with no output.
- Targeted searches confirmed pruning/promotion/stale handling, memory
  frontmatter/status exceptions, optionality as correctness boundary, owner-layer
  promotion, retrospective/closure housekeeping triggers, and no new runtime.

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

No findings in `critique:memory-pruning-frontmatter-review`.

Disposition status: complete

Deferral / not-required rationale:

Not deferred. Oracle critique is recorded in
`critique:memory-pruning-frontmatter-review`.

# Wiki Disposition

Deferred intentionally. The accepted memory maintenance guidance now lives in the
memory and records owner surfaces. No separate wiki page is needed for this
ticket; the final corpus-wide validation ticket may still choose broader wiki
promotion.

# Acceptance Decision

Accepted by: OpenCode parent agent

Accepted at: 2026-05-02T10:50:58Z

Basis: Ralph packet `packet:ralph-ticket-795fa0f4-20260502T104301Z`, validation
evidence `evidence:memory-pruning-frontmatter-validation`, and final oracle
critique `critique:memory-pruning-frontmatter-review` with no findings.

Residual risks: Guidance is not runtime-enforced; future validators or adapters
must preserve the memory exception if they add validation behavior later.
Historical `.loom/memory` files were intentionally not rewritten or validated.

# Dependencies

- `ticket:4e8ebe92`
- `ticket:1a12d9ff`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the memory pruning and frontmatter expectation slice.
- 2026-05-02T10:43:01Z: Started Ralph iteration
  `packet:ralph-ticket-795fa0f4-20260502T104301Z` for memory pruning and
  frontmatter/status expectations.
- 2026-05-02T10:47:08Z: Moved to review after Ralph implementation and structural
  validation.
- 2026-05-02T10:50:58Z: Accepted and closed after structural evidence, oracle
  critique with no findings, and retrospective disposition.
