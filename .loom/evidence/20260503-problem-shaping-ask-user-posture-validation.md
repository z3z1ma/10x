---
id: evidence:problem-shaping-ask-user-posture-validation
kind: evidence
status: recorded
created_at: 2026-05-03T08:20:52Z
updated_at: 2026-05-03T08:23:28Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:askpost22
  packet:
    - packet:ralph-ticket-askpost22-20260503T081918Z
  critique:
    - critique:problem-shaping-ask-user-posture-review
external_refs: {}
---

# Summary

Validation observations for `ticket:askpost22`, checking that problem-shaping
guardrails distinguish material ambiguity from low-risk reversible assumptions
inside delegated authority.

# Procedure

- Inspected the scoped product diff for `ticket:askpost22`.
- Searched problem-shaping guidance for ambiguous readings, `ask_user`, material
  risk, authority, low-risk reversible assumptions, delegated authority, owning
  record requirements, and chat/transcript summary boundaries.
- Parent-side validation used `git add -N` for newly created scoped records before
  `git diff --check` so new records were included in the whitespace check. This
  happened during parent reconciliation/validation, not during child execution;
  the child did not mutate Git metadata.
- Ran `git diff --check`.

# Artifacts

Scoped changed tracked files:

- `.loom/tickets/20260503-askpost22-align-problem-shaping-ask-user-posture.md`
- `skills/loom-workspace/references/problem-shaping.md`

Scoped new Loom record files:

- `.loom/packets/ralph/20260503T081918Z-ticket-askpost22-iter-01.md`
- `.loom/evidence/20260503-problem-shaping-ask-user-posture-validation.md`
- `.loom/critique/problem-shaping-ask-user-posture-review.md`

Targeted observations:

- `skills/loom-workspace/references/problem-shaping.md:64-66` now says not to
  silently choose between materially ambiguous readings and routes to `ask_user`
  when proceeding would invent authority, accept material risk, change
  owner-record truth, or make irreversible/high-risk decisions.
- `skills/loom-workspace/references/problem-shaping.md:67-69` allows low-risk,
  reversible assumptions inside delegated authority only after recording the
  assumption in the owning record before continuing.
- `skills/loom-workspace/references/problem-shaping.md:71-73` says chat or
  transcript summaries cannot replace spec, plan, ticket, or other owner-record
  ownership when the decision or assumption needs to persist.
- Search for `ambiguous|ask_user|low-risk|reversible|delegated authority|owning record|owner-record|material risk|invent authority|chat|transcript` returned the expected problem-shaping guidance hits.
- `git diff --check` result: passed with no output.

# Supports Claims

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-023`
- `ticket:askpost22#ACC-001`
- `ticket:askpost22#ACC-002`
- `ticket:askpost22#ACC-003`
- `ticket:askpost22#ACC-004`

# Challenges Claims

None - the observations did not weaken the scoped claims.

# Environment

Commit: `1b2aa2e5ca58cb3a5ce5dbaa7fb8486d63220950` plus uncommitted scoped
`ticket:askpost22` changes.
Branch: `main`
Runtime: Markdown/static repository; no app runtime.
OS: macOS/Darwin
Relevant config: no chat summary owner surface, runtime, hidden helper, command
wrapper, or new owner layer observed in the scoped diff.

# Validity

Valid for: the scoped `ticket:askpost22` diff at 2026-05-03T08:23:28Z.
Recheck when: any scoped file changes before closure or before the commit is
created.

# Limitations

This evidence is structural and textual. It validates authored problem-shaping
guidance; actual posture still depends on operators recording assumptions in the
right owner record before continuing.

# Result

Problem-shaping guardrails now preserve `ask_user` for material ambiguity while
allowing low-risk reversible assumptions inside delegated authority only when they
are recorded in the owning record. The scoped diff passes `git diff --check`.

# Interpretation

The evidence supports the ask-user posture alignment claims. It does not close the
ticket; mandatory critique and the ticket-owned acceptance decision remain
separate gates.

# Related Records

- `ticket:askpost22`
- `packet:ralph-ticket-askpost22-20260503T081918Z`
