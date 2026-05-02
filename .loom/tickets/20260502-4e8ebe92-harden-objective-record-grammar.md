---
id: ticket:4e8ebe92
kind: ticket
status: ready
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T08:46:28Z
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
  - ticket:0a1106b6
---

# Summary

Harden shared record grammar for objective coverage, valid/current record kinds,
canonical ID/path families, memory frontmatter expectations, semantic links, and
external reference provenance.

# Context

The council found that the corpus already uses concepts that the shared grammar
does not fully enumerate. The most visible example is `OBJ-*` objective criteria
inside initiatives and tickets. Other gaps include centrally listed `kind:`
values, ID/path forms, memory exceptions, semantic link terms, and external
reference lifecycle guidance.

# Why Now

Downstream skills should not define their own local grammar when the relationship
is shared. This ticket gives later packet, ticket, workspace, memory, and
consolidation slices a stable record-grammar owner to cite.

# Scope

- Update `skills/loom-records/references/claim-coverage.md` to cover `OBJ-*`
  objective criteria if initiatives continue using them.
- Decide and document the qualified objective reference form.
- Update `skills/loom-initiatives/**` so objective criteria are clearly owned by
  initiatives while tickets own in-scope coverage and closure disposition.
- Add a canonical or current-supported `kind:` / ID / path table in
  `loom-records`.
- Clarify memory frontmatter/status expectations without making memory canonical
  project truth.
- Clarify semantic link usage for supersession, promotion, related tickets,
  follow-up tickets, accepted risk, and external references.
- Tighten external reference provenance and lifecycle guidance.
- Add or update native validation/query guidance for the new grammar.

# Non-goals

- Do not normalize packet family semantics beyond the record-ID table; packet
  behavior belongs to `ticket:0cd38381`.
- Do not change ticket acceptance gates beyond references needed to point at the
  new shared grammar; acceptance grammar belongs to `ticket:50ded996`.
- Do not rewrite memory model guidance beyond frontmatter/status and
  owner-boundary references; memory pruning belongs to `ticket:795fa0f4`.

# Acceptance Criteria

- ACC-001: `loom-records` teaches objective coverage grammar for `OBJ-*` or
  explicitly explains why initiative objective IDs remain outside claim coverage.
- ACC-002: `loom-initiatives` aligns with the selected objective coverage grammar.
- ACC-003: `loom-records` contains one easy-to-find table or section for current
  `kind:` values, canonical ID families, and path conventions.
- ACC-004: Memory frontmatter/status expectations are explicit enough that future
  validation does not falsely treat intentional memory support files as broken
  canonical records.
- ACC-005: Semantic links and external references are described as graph aids and
  support surfaces, not truth owners.
- ACC-006: New grammar can be checked with ordinary grep/rg queries documented in
  or near the relevant record guidance.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening` OBJ-002
- `research:skills-corpus-council-review#CLAIM-005`
- `research:skills-corpus-council-review#CLAIM-007`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening` OBJ-002 | implementation evidence pending | mandatory critique pending | open |
| `research:skills-corpus-council-review#CLAIM-005` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | mandatory critique pending | supported_pending_review |
| `research:skills-corpus-council-review#CLAIM-007` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | mandatory critique pending | supported_pending_review |

# Execution Notes

Prefer one shared grammar section over repeated explanations across downstream
skills. If a field is current corpus usage rather than closed vocabulary, say so
instead of overclaiming finality.

# Blockers

Do not start until `ticket:0a1106b6` has landed or been intentionally deferred.

# Next Move / Next Route

Ralph implementation packet for shared record grammar.

# Ralph Readiness

Bounded iteration:

Update shared record and initiative grammar for objective coverage, kind/ID/path,
semantic links, memory exception, and external references.

Write boundary:

- `skills/loom-records/**`
- `skills/loom-initiatives/**`
- targeted references in `skills/loom-memory/**` or `skills/loom-evidence/**` only
  when needed to preserve link truth

Likely verification posture:

Observation-first structural validation.

Expected output contract:

- changed files,
- selected objective-reference form and rationale,
- validation queries and outputs,
- any grammar questions escalated to research/spec/constitution.

# Evidence

Expected:

- `git diff --check`
- coverage-ID grep checks for records and initiatives
- kind/ID/path, external reference, and semantic-link grep checks
- manual comparison against this ticket's acceptance criteria

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale:

This changes shared record grammar and can affect how downstream tickets,
evidence, critique, and initiatives cite objective and claim coverage.

Required critique profiles:

- records-grammar
- protocol-change
- operator-clarity

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None. Critique is mandatory.

# Wiki Disposition

Pending. If the selected objective coverage grammar becomes a durable operator
concept beyond the reference text, consider wiki promotion during final
retrospective.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

- `ticket:0a1106b6`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the shared record-grammar slice.
