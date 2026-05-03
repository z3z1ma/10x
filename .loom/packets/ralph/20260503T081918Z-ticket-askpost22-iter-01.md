---
id: packet:ralph-ticket-askpost22-20260503T081918Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:askpost22
mode: execution
change_class: protocol-authority
risk_class: medium
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-03T08:19:18Z
updated_at: 2026-05-03T08:20:52Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - None - child returns output only; parent reconciles ticket, evidence, critique, and packet status.
  paths:
    - skills/loom-workspace/references/problem-shaping.md
parent_merge_scope:
  records:
    - ticket:askpost22
  paths:
    - .loom/tickets/20260503-askpost22-align-problem-shaping-ask-user-posture.md
    - .loom/evidence/20260503-problem-shaping-ask-user-posture-validation.md
    - .loom/critique/problem-shaping-ask-user-posture-review.md
    - .loom/packets/ralph/20260503T081918Z-ticket-askpost22-iter-01.md
source_fingerprint:
  git_commit: 1b2aa2e5ca58cb3a5ce5dbaa7fb8486d63220950
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: 1b2aa2e5ca58cb3a5ce5dbaa7fb8486d63220950
  git_status_summary: dirty_mixed
  git_status_detail: parent-owned ticket and packet records are modified/untracked for launch; child write-scope file is clean relative to 1b2aa2e
  compiled_from:
    - ticket:askpost22
    - ticket:pktorph21
    - plan:skills-corpus-context-integrity-hardening-pass
    - initiative:skills-corpus-context-integrity-hardening-pass
    - research:skills-corpus-third-pass-follow-up-validation
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
  network: forbidden
context_budget:
  posture: tight
  max_source_files: 5
  max_excerpt_lines_per_file: 180
  avoid_full_file_reads: true
sources:
  initiative:
    - initiative:skills-corpus-context-integrity-hardening-pass
  research:
    - research:skills-corpus-third-pass-follow-up-validation
  plan:
    - plan:skills-corpus-context-integrity-hardening-pass
  ticket:
    - ticket:askpost22
  files:
    - skills/loom-workspace/references/problem-shaping.md
    - skills/loom-records/references/route-vocabulary.md
links: {}
---

# Mission

Align problem-shaping ambiguous-choice guidance with the `ask_user` posture for
low-risk reversible assumptions.

# Bound Context

`ticket:askpost22` covers `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-023`.
Problem shaping currently says not to silently choose between ambiguous readings.
That remains correct for material, irreversible, high-risk, authority-changing,
or owner-record-affecting ambiguity. It should not force a clarifying question for
every low-risk reversible assumption inside delegated authority when the
assumption can be recorded in the owning record and safely carried forward.

# Source Snapshot

- `skills/loom-workspace/references/problem-shaping.md` guardrails currently say
  `Do not silently choose between ambiguous readings.`
- Route vocabulary's `ask_user` guidance says to ask when an operator decision
  cannot be inferred, but low-risk reversible assumptions inside delegated
  authority can be recorded and work can continue.

# Change Class

Declared as `protocol-authority` with medium risk. The edit changes ask-versus-
proceed operator posture and must preserve material ambiguity gates while staying
Markdown-native.

# Verification Targets

- `initiative:skills-corpus-context-integrity-hardening-pass#OBJ-023`
- `ticket:askpost22#ACC-001`
- `ticket:askpost22#ACC-002`
- `ticket:askpost22#ACC-003`
- `ticket:askpost22#ACC-004`

# Task For This Iteration

Make the smallest coherent problem-shaping edit:

1. Qualify the ambiguous-choice guardrail so material ambiguity still routes to
   `ask_user`.
2. Preserve mandatory questioning when proceeding would invent authority, accept
   material risk, change owner-record truth, or make an irreversible/high-risk
   decision.
3. Allow low-risk reversible assumptions inside delegated authority only when the
   assumption is recorded in the owning record before continuing.
4. Do not weaken `ask_user` for material decisions.
5. Do not let chat summaries replace owner records.

# Verification Posture

Observation-first. Before and after editing, report targeted observations for:

- ambiguous readings / material ambiguity guidance;
- low-risk reversible assumption path;
- owner-record recording requirement;
- `ask_user` still required for authority or material-risk decisions;
- no chat-summary-as-owner-record loophole.

Run `git diff --check` after editing.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- the edit would weaken `ask_user` for material, irreversible, high-risk,
  authority-changing, or owner-record-affecting decisions;
- the edit would let transcript/chat summaries replace owner records;
- satisfying the ticket would require changes outside problem-shaping guidance.

Do not run `git fetch`, remote edits, Git config edits, destructive commands, or
shared Git metadata mutations. Do not edit parent-owned `.loom` records.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
`git diff --check` result, self-review, blockers/residual risks, and recommended
ticket state/next route.

# Working Notes

Parent compiled from clean `main` at `1b2aa2e` after closing and pushing
`ticket:pktorph21`. Saving this packet and activating the ticket made the
worktree `dirty_mixed` before child launch; those parent-owned `.loom` records
are outside child write scope. The product file in `child_write_scope.paths`
remains clean relative to `1b2aa2e` at launch.

# Child Output

Outcome: `stop`

Files changed:

- `skills/loom-workspace/references/problem-shaping.md`

Records changed by child:

- None. Parent retained ticket, evidence, critique, and packet reconciliation.

Observed result:

- Before: ambiguous-reading guardrail was unconditional and did not name
  `ask_user` or materiality.
- After: material ambiguity routes to `ask_user` when it would invent authority,
  accept material risk, change owner-record truth, or make irreversible/high-risk
  decisions.
- Before: no low-risk reversible assumption path was present.
- After: low-risk reversible assumptions inside delegated authority may proceed
  only after recording the assumption in the owning record.
- Before: owner-record requirement existed only as chat summary must not replace
  spec, plan, or ticket.
- After: chat/transcript summaries cannot replace spec, plan, ticket, or other
  owner-record ownership for persistent decisions or assumptions.

Verification:

- `git diff --check` passed with no output.

Self-review:

- Stayed within `child_write_scope.paths`.
- Did not modify `.loom` records.
- Preserved mandatory questioning for material authority/risk decisions.
- Did not create a chat-summary-as-owner loophole.

Blockers or residual risks:

- No blockers.
- Medium-risk protocol-authority change requires parent-side critique before
  acceptance.

Recommendation:

- Move `ticket:askpost22` to `review_required` and route to mandatory critique.

# Parent Merge Notes

- 2026-05-03T08:20:52Z: Parent accepted the bounded implementation output,
  recorded `evidence:problem-shaping-ask-user-posture-validation`, marked this
  packet `consumed`, and moved `ticket:askpost22` to `review_required` for
  mandatory critique.
