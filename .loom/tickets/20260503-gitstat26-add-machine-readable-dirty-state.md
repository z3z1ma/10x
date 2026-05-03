---
id: ticket:gitstat26
kind: ticket
status: closed
change_class: protocol-authority
risk_class: high
created_at: 2026-05-03T06:20:11Z
updated_at: 2026-05-03T08:02:37Z
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
    - critique:git-dirty-state-fingerprint-review
    - critique:git-dirty-state-fingerprint-rereview
external_refs: {}
depends_on:
  - ticket:shipacc1
  - ticket:netgate25
---

# Summary

Make packet Git dirty state machine-readable.

# Context

Packet source fingerprints currently use broad `clean|dirty|unknown` values,
which hide whether tracked files, untracked files, or both caused dirty state.

# Why Now

Fresh workers and parents need clear launch-freshness signals.

# Scope

- Add or clarify machine-readable dirty categories such as `dirty_tracked`,
  `dirty_untracked`, and `dirty_mixed`.
- Preserve human-readable detail in `git_status_detail`.
- Update packet templates if needed.

# Out Of Scope

- Do not require a Git helper runtime.
- Do not change Git itself as truth owner for file history.

# Acceptance Criteria

- ACC-001: Packet fingerprint guidance names machine-readable dirty categories.
- ACC-002: Guidance preserves `clean` and `unknown` with rationale when needed.
- ACC-003: `git_status_detail` remains available for human context.
- ACC-004: Evidence records targeted dirty-state searches and `git diff --check`.
- ACC-005: Mandatory critique passes with no unresolved findings.

# Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-027`
- `ticket:gitstat26#ACC-001`
- `ticket:gitstat26#ACC-002`
- `ticket:gitstat26#ACC-003`
- `ticket:gitstat26#ACC-004`
- `ticket:gitstat26#ACC-005`

# Claim Matrix

| Claim | Evidence | Critique | Status |
| --- | --- | --- | --- |
| `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-027` | `evidence:git-dirty-state-fingerprint-validation` | `critique:git-dirty-state-fingerprint-rereview` | supported |
| `ticket:gitstat26#ACC-001` | `evidence:git-dirty-state-fingerprint-validation` | `critique:git-dirty-state-fingerprint-rereview` | supported |
| `ticket:gitstat26#ACC-002` | `evidence:git-dirty-state-fingerprint-validation` | `critique:git-dirty-state-fingerprint-rereview` | supported |
| `ticket:gitstat26#ACC-003` | `evidence:git-dirty-state-fingerprint-validation` | `critique:git-dirty-state-fingerprint-rereview` | supported |
| `ticket:gitstat26#ACC-004` | `evidence:git-dirty-state-fingerprint-validation` | `critique:git-dirty-state-fingerprint-rereview` | supported |
| `ticket:gitstat26#ACC-005` | `evidence:git-dirty-state-fingerprint-validation` | `critique:git-dirty-state-fingerprint-rereview` | supported |

# Execution Notes

Likely touched files: `skills/loom-records/references/packet-frontmatter.md`,
Ralph packet contract, and packet templates.

# Blockers

None - prerequisites `ticket:shipacc1` and `ticket:netgate25` are closed and
pushed.

# Next Move / Next Route

Closed. Commit and push this ticket before continuing to `ticket:ralphg20`.

Ralph packet `packet:ralph-ticket-gitstat26-20260503T075047Z` completed in
scope, evidence was recorded, mandatory critique F-001 was resolved, rereview
passed with no findings, and acceptance is complete.

# Route Readiness

Ralph readiness:
Bounded iteration: machine-readable packet Git dirty state.
Write boundary: packet frontmatter guidance, Ralph packet contract, and directly
related packet templates.
Likely verification posture: observation-first structural validation.
Expected output contract: changed files, dirty-state observations, and critique
recommendation.

Acceptance review readiness:
Evidence `evidence:git-dirty-state-fingerprint-validation` and mandatory critique
rereview `critique:git-dirty-state-fingerprint-rereview` support closure.

# Evidence

Expected: targeted searches for `dirty_tracked`, `dirty_untracked`,
`dirty_mixed`, `git_status_detail`, and `git diff --check`.

Recorded:

- `evidence:git-dirty-state-fingerprint-validation`

# Critique Disposition

Risk class: high

Critique policy: mandatory

Policy rationale: Git state is a launch-safety fingerprint.

Required critique profiles:

- packet-safety
- git-provenance
- operator-clarity

Findings:

`critique:git-dirty-state-fingerprint-review#F-001`: stale next route conflicted
with `status: review_required`. Disposition: resolved by updating `# Next Move /
Next Route` from `ralph` to `critique` and naming mandatory critique rereview as
the current step.

`critique:git-dirty-state-fingerprint-rereview`: no findings; mandatory rereview
passed and confirmed F-001 resolved.

Disposition status: completed

Deferral / not-required rationale:

Not deferred.

# Retrospective / Promotion Disposition

Disposition status: completed

Promoted:

- Machine-readable dirty-state fingerprint guidance was promoted into packet
  frontmatter, Ralph packet contract, and packet-family templates.

Deferred / not-required rationale:

No separate wiki, research, spec, constitution, or memory record is needed. The
durable lesson is local to packet source-fingerprint guidance.

# Wiki Disposition

N/A - no separate wiki promotion route. The accepted explanation lives in packet
source-fingerprint guidance and templates.

# Acceptance Decision

Accepted by: OpenCode parent agent
Accepted at: 2026-05-03T08:02:37Z
Basis: Ralph packet `packet:ralph-ticket-gitstat26-20260503T075047Z`; evidence
`evidence:git-dirty-state-fingerprint-validation`; initial mandatory critique
`critique:git-dirty-state-fingerprint-review` with F-001 resolved; mandatory
rereview `critique:git-dirty-state-fingerprint-rereview` with no findings.
Residual risks: Historical consumed packets may still contain legacy
`git_status_summary: dirty`; this is acceptable because they are support
artifacts, not current authoring guidance.

# Dependencies

- `ticket:shipacc1`
- `ticket:netgate25`

# Journal

- 2026-05-03T06:20:11Z: Created from third-pass secondary polish finding.
- 2026-05-03T07:50:47Z: Parent confirmed `ticket:netgate25` pushed, moved this
  ticket to active, and compiled Ralph iteration 1.
- 2026-05-03T07:54:00Z: Ralph child returned `stop`; parent accepted the scoped
  implementation output, recorded evidence, consumed the packet, and moved to
  mandatory critique.
- 2026-05-03T07:58:57Z: Mandatory critique found F-001, a stale ticket next-route
  value. Parent resolved the ticket ledger conflict and queued rereview before
  acceptance.
- 2026-05-03T08:02:37Z: Mandatory rereview
  `critique:git-dirty-state-fingerprint-rereview` passed with no findings. Parent
  recorded retrospective / promotion disposition and accepted closure.
