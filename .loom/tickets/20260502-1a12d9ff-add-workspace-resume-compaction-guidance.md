---
id: ticket:1a12d9ff
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-02T08:46:28Z
updated_at: 2026-05-02T10:27:05Z
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
    - evidence:workspace-resume-compaction-validation
  critique:
    - critique:workspace-resume-compaction-review
  packet:
    - packet:ralph-ticket-1a12d9ff-20260502T101425Z
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
| `initiative:skills-corpus-protocol-sharpening#OBJ-003` | `evidence:workspace-resume-compaction-validation` | `critique:workspace-resume-compaction-review` | supported |
| `research:skills-corpus-council-review#CLAIM-004` | `evidence:skills-corpus-council-review`; `evidence:workspace-resume-compaction-validation` | `critique:workspace-resume-compaction-review` | supported |
| `research:skills-corpus-council-review#CLAIM-007` | `evidence:skills-corpus-council-review`; `evidence:workspace-resume-compaction-validation` | `critique:workspace-resume-compaction-review` | supported |

# Execution Notes

Keep the guidance operational and short enough to be used in a cold session. Avoid
making a decision tree that competes with layer ownership.

# Blockers

None. Dependency `ticket:0a1106b6` is closed.

# Next Move / Next Route

Closed. Continue with the next sequenced plan ticket, `ticket:233cfdeb`.

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

Recorded:

- `evidence:workspace-resume-compaction-validation`
- `git diff --check` passed with no output.
- Targeted searches confirmed cold-start, post-compaction, and pre-compaction
  guidance; bootstrap and `constitution:main` ordering; active-ticket discovery;
  chat/transcript/generated-context shadow-truth rejection; pre-compaction owner
  updates; and `loom-drive` as high-level coordinator rather than the only resume
  route.

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

All findings resolved in `critique:workspace-resume-compaction-review`.

Disposition status: complete

Deferral / not-required rationale:

Not deferred. Mandatory critique is recorded in
`critique:workspace-resume-compaction-review`.

# Wiki Disposition

Deferred intentionally. The accepted recovery route now lives in the
`loom-workspace` product surface. No separate wiki page is needed for this ticket;
the final corpus-wide validation ticket may still choose broader wiki promotion.

# Acceptance Decision

Accepted by: OpenCode parent agent

Accepted at: 2026-05-02T10:27:05Z

Basis: Ralph packet `packet:ralph-ticket-1a12d9ff-20260502T101425Z`, validation
evidence `evidence:workspace-resume-compaction-validation`, and final oracle
critique `critique:workspace-resume-compaction-review` with all findings resolved.

Residual risks: Validation is structural/manual rather than a real cold-session
trial. The `loom-workspace` frontmatter description still summarizes "read
constitution first" while the body route correctly requires bootstrap doctrine
before `constitution:main`; final corpus-wide validation may choose to polish that
summary.

# Dependencies

- `ticket:0a1106b6`

# Journal

- 2026-05-02T08:46:28Z: Split from cancelled broad ticket `ticket:3uv5l5fh` as
  the workspace resume and compaction guidance slice.
- 2026-05-02T10:14:25Z: Started Ralph iteration
  `packet:ralph-ticket-1a12d9ff-20260502T101425Z` for workspace resume and
  compaction guidance.
- 2026-05-02T10:22:55Z: Moved to review after Ralph implementation and structural
  validation. Initial oracle critique found parent-side record reconciliation and
  stale evidence issues; product guidance had no blocking text findings.
- 2026-05-02T10:27:05Z: Accepted and closed after record reconciliation, refreshed
  structural evidence, final oracle critique pass, and retrospective disposition.
