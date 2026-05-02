---
id: ticket:1a12d9ff
kind: ticket
status: ready
change_class: protocol-authority
risk_class: high
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
  - ticket:0a1106b6
---

# Summary

Make cold-start, post-compaction, and pre-compaction recovery a first-class
workspace-entry route that continues from Loom owner records rather than chat
memory.

# Context

The council identified a product-promise gap: README emphasizes disposable
sessions and repo-local recovery, but the skills corpus does not teach cold-start
resume as directly as the premise deserves. Resume behavior appears mostly through
`loom-drive`, when it should also be available to normal workspace entry.

# Why Now

Fresh-context recovery is one of Loom's deepest value claims. Workspace entry
should teach agents exactly how to recover active work from `.loom/` and fail
closed when owner records conflict.

# Scope

- Add workspace-entry guidance for cold-start and post-compaction resume.
- Teach a fresh agent to load bootstrap doctrine, read `constitution:main`, inspect
  active tickets, follow upstream links, inspect evidence/critique, and continue
  from owner records.
- Add an active-ticket discovery query where appropriate.
- Add pre-compaction checkpoint guidance that updates the correct owner record
  before a session ends or compacts.
- Decide where to summarize resume guidance beyond workspace without duplicating
  the full workflow everywhere.
- Ensure resume guidance routes support-only continuity to memory but keeps live
  execution truth in tickets.

# Non-goals

- Do not create a new resume record kind, checkpoint ledger, or generated context
  file requirement.
- Do not make memory required for correctness.
- Do not update ticket acceptance grammar except where resume guidance points at
  the ticket ledger.
- Do not change `loom-drive` beyond pointers or overlap reduction needed for
  workspace resume consistency.

# Acceptance Criteria

- ACC-001: `loom-workspace` teaches a concrete cold-start and post-compaction
  recovery path.
- ACC-002: The route reads bootstrap doctrine and `constitution:main` before
  relying on downstream records.
- ACC-003: The route discovers active tickets and follows the upstream owner chain
  before continuing work.
- ACC-004: The route explicitly rejects chat transcript memory as canonical truth.
- ACC-005: Pre-compaction guidance updates tickets, evidence, critique, wiki, or
  memory according to owner boundaries instead of creating a checkpoint ledger.
- ACC-006: Any overlap with `loom-drive` is clarified so drive remains an
  objective coordinator, not the only resume route.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening#OBJ-003`
- `research:skills-corpus-council-review#CLAIM-004`
- `research:skills-corpus-council-review#CLAIM-007`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening#OBJ-003` | implementation evidence pending | mandatory critique pending | open |
| `research:skills-corpus-council-review#CLAIM-004` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | mandatory critique pending | supported_pending_review |
| `research:skills-corpus-council-review#CLAIM-007` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | mandatory critique pending | supported_pending_review |

# Execution Notes

Keep the guidance operational and short enough to be used in a cold session. Avoid
making a decision tree that competes with layer ownership.

# Blockers

Do not start until `ticket:0a1106b6` lands or is intentionally deferred, because
public framing may affect where resume is summarized.

# Next Move / Next Route

Ralph implementation packet for workspace resume and compaction guidance.

# Ralph Readiness

Bounded iteration:

Add first-class cold-start, post-compaction, and pre-compaction guidance through
workspace entry and narrow supporting pointers.

Write boundary:

- `skills/loom-workspace/**`
- `skills/loom-bootstrap/**`
- `skills/loom-drive/**`
- `skills/loom-tickets/**`
- `skills/loom-memory/**`
- public docs only if needed for a short pointer

Likely verification posture:

Observation-first structural validation.

Expected output contract:

- changed files,
- exact recovery route added,
- duplicate or conflicting resume wording removed or deferred,
- validation output.

# Evidence

Expected:

- `git diff --check`
- targeted grep checks for cold-start, post-compaction, resume, active tickets,
  `constitution:main`, chat memory, and transcript wording
- manual route walkthrough from a hypothetical cold session

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale:

This changes core operator recovery behavior and could accidentally create a
second ledger if poorly framed.

Required critique profiles:

- protocol-change
- operator-clarity
- routing-safety

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None. Critique is mandatory.

# Wiki Disposition

Pending. Cold-start recovery may deserve a wiki page if the accepted route needs
to be reused outside the skill text.

# Acceptance Decision

Accepted by:

Accepted at:

Basis:

Residual risks:

# Dependencies

- `ticket:0a1106b6`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the workspace resume and compaction guidance slice.
