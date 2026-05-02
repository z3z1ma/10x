---
id: ticket:233cfdeb
kind: ticket
status: ready
change_class: protocol-authority
risk_class: medium
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
  - ticket:4e8ebe92
  - ticket:1a12d9ff
---

# Summary

Add operator guidance that prevents generic scratchpads, external systems, and
concurrent file edits from becoming shadow truth or unsafe workflow shortcuts.

# Context

The council found underdeveloped failure-mode areas: scratchpad avoidance,
external-reference lifecycle, and concurrent agent edit safety. These are all
file-first ergonomics problems that should be solved through owner-layer routing,
not a new runtime.

# Why Now

As Loom work spreads across smaller Ralph iterations, agents need precise rules
for where temporary-seeming information belongs, how external systems relate to
Loom truth, and how to avoid clobbering another actor's changes.

# Scope

- Add an explicit anti-pattern warning against generic `scratch.md`, `notes.md`,
  or junk-drawer files.
- Route scratchpad-like material to the correct owner: evidence, research,
  tickets, wiki, or memory.
- Expand external-reference lifecycle guidance for issue trackers, PRs, URLs,
  dashboards, generated context files, and harness artifacts as support surfaces.
- Add file-first concurrency guidance: re-read before writing, fail closed on
  conflicts, preserve unrelated changes, and reconcile stale records by owner
  layer rather than recency.
- Place guidance in the smallest owner surfaces that future agents will read.

# Non-goals

- Do not create a scratchpad record kind.
- Do not require lockfiles, a coordination service, or a generated index.
- Do not make external issue trackers or PRs canonical Loom truth.
- Do not duplicate full resume guidance from `ticket:1a12d9ff`.

# Acceptance Criteria

- ACC-001: The corpus directly warns against generic scratchpad or junk-drawer
  files and gives owner-layer alternatives.
- ACC-002: External reference guidance explains mirror/package/request roles
  without granting truth ownership.
- ACC-003: Concurrent edit guidance tells agents when to re-read, fail closed, and
  preserve unrelated changes.
- ACC-004: Stale or contradictory records are routed to owner-layer reconciliation
  instead of latest-file-wins behavior.
- ACC-005: The guidance stays Markdown-native and does not require locks,
  daemons, or helpers.

# Coverage

Covers:

- `initiative:skills-corpus-protocol-sharpening` OBJ-003
- `research:skills-corpus-council-review#CLAIM-007`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-protocol-sharpening` OBJ-003 | implementation evidence pending | critique recommended | open |
| `research:skills-corpus-council-review#CLAIM-007` | `evidence:skills-corpus-council-review` supports need; implementation evidence pending | critique recommended | supported_pending_review |

# Execution Notes

Teach high-signal guardrails, not every possible bad filename or external system.
Keep examples concrete and owner-routed.

# Blockers

Do not start until shared semantic/external reference grammar and resume guidance
have landed or been intentionally deferred.

# Next Move / Next Route

Ralph implementation packet or local edit for scratchpad, external reference, and
concurrency guidance.

# Ralph Readiness

Bounded iteration:

Add scratchpad anti-pattern, external reference lifecycle, and concurrent edit
safety guidance to owner surfaces.

Write boundary:

- `skills/loom-records/**`
- `skills/loom-workspace/**`
- `skills/loom-git/**`
- `skills/loom-evidence/**`
- `skills/loom-research/**`
- `skills/loom-tickets/**`
- `skills/loom-memory/**`

Likely verification posture:

Observation-first structural validation.

Expected output contract:

- changed files,
- owner routing examples,
- validation queries and outputs,
- any deferred external-reference nuance.

# Evidence

Expected:

- `git diff --check`
- targeted grep checks for scratchpad, external references, re-read, concurrency,
  stale records, and latest-file wording
- manual check that guidance does not create a new ledger

# Critique Disposition

Risk class: medium

Critique policy: recommended

Policy rationale:

This changes operator guardrails and truth-boundary interpretation but should not
change core acceptance or packet contracts.

Required critique profiles:

- operator-clarity
- routing-safety

Findings:

None - no critique yet.

Disposition status: pending

Deferral / not-required rationale:

None yet.

# Wiki Disposition

Pending. If scratchpad routing becomes a common operator problem, promote a short
workflow explanation during retrospective.

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
  the scratchpad, external reference, and concurrency guidance slice.
