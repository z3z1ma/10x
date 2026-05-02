---
id: evidence:evidence-quality-guidance-validation
kind: evidence
status: recorded
created_at: 2026-05-02T20:49:39Z
updated_at: 2026-05-02T20:49:39Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:evshape9
  packet:
    - packet:ralph-ticket-evshape9-20260502T204732Z
external_refs: {}
---

# Summary

Observation-first validation for `ticket:evshape9`: before/after searches show
evidence quality terms strengthened across evidence and ticket guidance, and
`git diff --check` reported no whitespace errors.

# Procedure

1. Before editing, ran:
   `rg -n "freshness|fresh enough|limitations|observed|inference|support|challenge|invalidation|supersession|git diff --check" "skills/loom-evidence" "skills/loom-tickets/SKILL.md" "skills/loom-tickets/templates/ticket.md" "skills/loom-tickets/references/acceptance-gate.md"`
2. Updated evidence and ticket guidance within the Ralph packet write scope.
3. After editing, ran the same `rg` command over the same guidance targets.
4. Ran `git diff --check` from repository root.

# Artifacts

## Before Search Observation

The before search found evidence and ticket guidance already used `observed`,
`support`, `challenge`, `fresh enough`, and `limitations` in scattered places,
including:

- `skills/loom-evidence/SKILL.md` described evidence as observed artifacts and
  named support/challenge links.
- `skills/loom-evidence/templates/evidence.md` had procedure, artifacts,
  supports, challenges, environment, validity, limitations, result, and
  interpretation sections.
- `skills/loom-tickets/references/acceptance-gate.md` asked whether evidence is
  `fresh enough` and whether the claim matrix summarizes support and challenge.

The before search did not find dedicated evidence-quality guidance under
`skills/loom-evidence/references/`, and did not find `invalidation`,
`supersession`, or the literal `git diff --check` in the searched guidance
targets.

## After Search Observation

The after search found the strengthened terms in the edited guidance:

- `skills/loom-evidence/references/evidence-quality.md` now teaches observed
  artifacts before inference, freshness / `fresh enough`, limitations, support
  and challenge strength, invalidation, supersession, proportional evidence
  expectations, and the acceptance boundary.
- `skills/loom-evidence/SKILL.md` now points to the evidence-quality reference
  and names freshness, invalidation, supersession, limitations, and observed
  support/challenge expectations.
- `skills/loom-evidence/templates/evidence.md` now prompts for freshness,
  invalidation, supersession, observed result, and bounded inference.
- `skills/loom-tickets/SKILL.md`, `skills/loom-tickets/templates/ticket.md`, and
  `skills/loom-tickets/references/acceptance-gate.md` now teach ticket-owned
  evidence sufficiency without making evidence close the ticket.

## Validation Command Observation

`git diff --check` result: passed with no output.

# Supports Claims

- `initiative:skills-corpus-council-precision-pass#OBJ-009`
- `ticket:evshape9#ACC-001`
- `ticket:evshape9#ACC-002`
- `ticket:evshape9#ACC-003`
- `ticket:evshape9#ACC-004`

# Challenges Claims

None - the observed searches and whitespace check did not challenge the scoped
claims.

# Environment

Commit: `4ee1f67f07bf4428829f57460870d24e06f080bf`
Branch: `main`
Runtime: Markdown/source inspection; no app runtime or automated test suite.
OS: Darwin 24.6.0 arm64
Relevant config: repository root `/Users/alexanderbutler/code_projects/personal/agent-loom`; worktree had uncommitted Loom packet/ticket changes during validation.

# Validity

Valid for: the edited evidence and ticket guidance at the current worktree state.
Fresh enough for: structural validation of `ticket:evshape9#ACC-001` through
`ticket:evshape9#ACC-004` pending critique.
Recheck when: any changed guidance file, this evidence record, the ticket, or
the packet changes before acceptance; critique requests more evidence; or the
acceptance scope changes.
Invalidated by: contradictory critique finding, removed evidence-quality
reference, broken links, failed `git diff --check`, or guidance that makes
evidence own acceptance, critique verdicts, intended behavior, or closure.
Supersedes / superseded by: superseded by any later evidence record that reruns
the same searches and whitespace validation against a newer source state.

# Limitations

This evidence records structural term searches and whitespace validation only. It
does not prove operators will apply the guidance correctly, does not constitute
oracle critique, and does not accept or close `ticket:evshape9`.

# Result

The observations showed that evidence quality guidance now includes the required
freshness, limitation, observed/inference, support/challenge,
invalidation/supersession, and ticket evidence sufficiency terms, and that
`git diff --check` passed.

# Interpretation

The limited inference justified by this evidence is that the Ralph iteration has
structural support for `ticket:evshape9#ACC-001` through `ticket:evshape9#ACC-004`.
This evidence alone does **not** justify ticket closure because mandatory oracle
critique and ticket-owned acceptance remain pending.

# Related Records

- `ticket:evshape9`
- `packet:ralph-ticket-evshape9-20260502T204732Z`
