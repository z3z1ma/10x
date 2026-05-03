---
id: critique:problem-shaping-ask-user-posture-review
kind: critique
status: final
created_at: 2026-05-03T08:23:28Z
updated_at: 2026-05-03T08:23:28Z
scope:
  kind: repository
  repositories:
    - repo:root
review_target: "ticket:askpost22 diff 1b2aa2e..working-tree"
links:
  ticket:
    - ticket:askpost22
  evidence:
    - evidence:problem-shaping-ask-user-posture-validation
  packet:
    - packet:ralph-ticket-askpost22-20260503T081918Z
external_refs: {}
---

# Summary

Mandatory oracle critique for `ticket:askpost22` after aligning problem-shaping
ambiguous-choice guidance with the `ask_user` posture.

# Review Target

Current working-tree diff from baseline
`1b2aa2e5ca58cb3a5ce5dbaa7fb8486d63220950`, covering workspace problem-shaping
guidance, ticket reconciliation, Ralph packet consumption, and evidence.

Required critique profiles: `operator-clarity`, `authority-boundary`, and
`workflow-boundary`.

# Verdict

`pass` - no findings.

# Findings

None - no findings.

# Profile Results

- `operator-clarity`: pass. The guardrail distinguishes material ambiguity from
  low-risk reversible assumptions.
- `authority-boundary`: pass. `ask_user` remains required when proceeding would
  invent authority, accept material risk, change owner-record truth, or make
  irreversible/high-risk decisions.
- `workflow-boundary`: pass. Chat and transcript summaries are explicitly
  prevented from replacing owner-record truth.

# Evidence Reviewed

- Working-tree diff from `1b2aa2e5ca58cb3a5ce5dbaa7fb8486d63220950`.
- `git diff --check`: passed with no output.
- `ticket:askpost22`.
- `packet:ralph-ticket-askpost22-20260503T081918Z`.
- `evidence:problem-shaping-ask-user-posture-validation`.
- `skills/loom-workspace/references/problem-shaping.md`.
- `skills/loom-records/references/route-vocabulary.md`.
- Targeted searches for `ask_user`, low-risk/reversible/delegated authority,
  material risk/invent authority, and chat/transcript owner boundaries.

# Acceptance Coverage

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-023`: supported.
- `ticket:askpost22#ACC-001`: supported. Material ambiguity and low-risk
  reversible assumptions are distinguished.
- `ticket:askpost22#ACC-002`: supported. Low-risk assumption path requires
  recording in the owning record before continuing.
- `ticket:askpost22#ACC-003`: supported. `ask_user` remains required for invented
  authority, material risk, owner-record truth changes, and irreversible/high-risk
  decisions.
- `ticket:askpost22#ACC-004`: supported. Evidence records targeted searches and
  `git diff --check`.
- `ticket:askpost22#ACC-005`: supported. Mandatory critique has no unresolved
  findings.

# Residual Risks

- The low-risk/reversible/delegated-authority test still depends on operator
  judgment, bounded by the owner-record recording requirement.

# Required Follow-up

None for this ticket.

# Acceptance Recommendation

`acceptance-ready`
