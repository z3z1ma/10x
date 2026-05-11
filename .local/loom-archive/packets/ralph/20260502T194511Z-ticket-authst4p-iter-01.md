---
id: packet:ralph-ticket-authst4p-20260502T194511Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:authst4p
mode: execution
change_class: protocol-authority
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-02T19:45:43Z
updated_at: 2026-05-02T19:50:08Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - ticket:authst4p
    - evidence:initiative-authority-stop-conditions-validation
    - packet:ralph-ticket-authst4p-20260502T194511Z
  paths:
    - skills/loom-initiatives/**
    - skills/loom-drive/SKILL.md
    - skills/loom-drive/references/continuity-contract.md
    - skills/loom-drive/references/drive-loop.md
    - skills/loom-drive/references/checkpoint-resume-protocol.md
    - .loom/tickets/20260502-authst4p-add-initiative-authority-stop-conditions.md
    - .loom/evidence/20260502-initiative-authority-stop-conditions-validation.md
    - .loom/packets/ralph/20260502T194511Z-ticket-authst4p-iter-01.md
parent_merge_scope:
  records:
    - ticket:authst4p
    - evidence:initiative-authority-stop-conditions-validation
    - packet:ralph-ticket-authst4p-20260502T194511Z
  paths:
    - .loom/critique/initiative-authority-stop-conditions-review.md
source_fingerprint:
  git_commit: d98a2ef2a26a8519675235fc4c6624a8ab921a93
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: d98a2ef2a26a8519675235fc4c6624a8ab921a93
  git_status_summary: clean
  compiled_from:
    - initiative:skills-corpus-council-precision-pass
    - plan:skills-corpus-council-precision-pass
    - ticket:authst4p
    - ticket:rtvocab1
execution_context:
  branch: main
  push_remote: origin
  worktree: /Users/alexanderbutler/code_projects/personal/agent-loom
  isolation: none
  git_shared_metadata_mutations: forbidden
  destructive_commands: forbidden
  network: forbidden
context_budget:
  posture: normal
  max_source_files: 12
  max_excerpt_lines_per_file: 140
  avoid_full_file_reads: true
sources:
  constitution:
    - constitution:main
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:authst4p
  references:
    - skills/loom-initiatives/templates/initiative.md
    - skills/loom-initiatives/references/initiative-shape.md
    - skills/loom-drive/SKILL.md
    - skills/loom-drive/references/continuity-contract.md
    - skills/loom-drive/references/drive-loop.md
    - skills/loom-drive/references/checkpoint-resume-protocol.md
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:authst4p
---

# Mission

Add initiative-owned delegated authority and objective-level stop-condition cues
so autonomous drive work has recoverable owner-record boundaries instead of
depending on transcript memory.

# Bound Context

This is the fourth ticket in `plan:skills-corpus-council-precision-pass` and
covers `initiative:skills-corpus-council-precision-pass#OBJ-004`. Dependency
`ticket:rtvocab1` is closed. The preceding ticket added the standard ticket
`# Retrospective / Promotion Disposition`; this ticket should use it when
updating its own acceptance dossier.

# Source Snapshot

Council finding `CR-004` observed that `loom-drive` already says initiatives own
delegated autonomy, budget/time limits, and objective-level stop conditions, but
`loom-initiatives` template/reference do not cue those fields. Fresh agents need
the initiative record to say what the agent may decide, what must return to the
user, and when objective-level continuation must stop.

Current source observations:

- `skills/loom-initiatives/templates/initiative.md` has objective, scope, success
  metrics, risks, linked work, status, and completion sections, but no delegated
  authority/autonomy or objective-level stop-condition section.
- `skills/loom-initiatives/references/initiative-shape.md` lists core sections
  and objective criteria, but does not explain when drive/autonomy fields are
  required or optional.
- `skills/loom-drive/references/continuity-contract.md` already maps delegated
  autonomy, budget/time limits, and objective-level stop conditions to the
  initiative.

# Change Class

Declared as `protocol-authority`; this affects autonomous objective boundaries
and human-escalation behavior.

# Verification Targets

- `initiative:skills-corpus-council-precision-pass#OBJ-004`
- `ticket:authst4p#ACC-001`
- `ticket:authst4p#ACC-002`
- `ticket:authst4p#ACC-003`
- `ticket:authst4p#ACC-004`

# Task For This Iteration

1. Capture before-state observations for delegated authority, delegated autonomy,
   autonomy limits, human-decision triggers, budget/time limits, and
   objective-level stop conditions in the initiative and drive surfaces.
2. Add optional initiative template prompts for delegated authority/autonomy
   boundaries and objective-level stop conditions.
3. Update `skills/loom-initiatives/references/initiative-shape.md` so these
   fields are required for delegated drive/autonomous objective work and optional
   or not required for ordinary initiatives.
4. Align drive continuity guidance with the exact initiative-owned field names,
   without creating a new authority record type.
5. Create `.loom/evidence/20260502-initiative-authority-stop-conditions-validation.md`.
6. Update `ticket:authst4p` to `review_required` with evidence, claim matrix,
   retrospective/promotion disposition pending, and critique-next recommendation.
   Do not close it.

# Verification Posture

`observation-first`.

Record before/after searches for delegated-authority/autonomy terms,
human-decision triggers, budget/time limits, objective-level stop conditions, and
`git diff --check`.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- the fix would make all initiatives require autonomous drive fields;
- the fix would grant autonomy that the user did not record;
- the fix would create a new authority record type or hidden ledger;
- the fix would make the initiative own live ticket execution state;
- scope widens into broad drive-loop rewrite or unrelated template cleanup.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
validation commands/results, risks, and ticket recommendation. Include whether
the ticket should proceed to mandatory oracle critique profiles:
`protocol-change`, `operator-clarity`, and `routing-safety`.

# Working Notes

Parent compiled from clean `main` at `d98a2ef2a26a8519675235fc4c6624a8ab921a93`.

# Child Output

Outcome: `stop` - the bounded implementation iteration completed and the next
route is mandatory critique, not additional implementation in this packet.

Files changed:

- `skills/loom-initiatives/templates/initiative.md`
- `skills/loom-initiatives/references/initiative-shape.md`
- `skills/loom-drive/SKILL.md`
- `skills/loom-drive/references/continuity-contract.md`
- `skills/loom-drive/references/drive-loop.md`
- `skills/loom-drive/references/checkpoint-resume-protocol.md`
- `.loom/evidence/20260502-initiative-authority-stop-conditions-validation.md`
- `.loom/tickets/20260502-authst4p-add-initiative-authority-stop-conditions.md`
- `.loom/packets/ralph/20260502T194511Z-ticket-authst4p-iter-01.md`

Records changed:

- `ticket:authst4p`
- `evidence:initiative-authority-stop-conditions-validation`
- `packet:ralph-ticket-authst4p-20260502T194511Z`

Before observations:

- Initiative template had no delegated authority/autonomy boundary prompt and no
  objective-level stop-condition prompt.
- Initiative shape reference did not explain required vs optional use for those
  fields.
- Drive guidance already mapped delegated autonomy, budget/time limits, and
  objective-level stop conditions to initiatives, but did not consistently use
  the exact initiative-owned field names.

After observations:

- Initiative template now includes optional sections
  `# Delegated Authority / Autonomy Boundaries` and
  `# Objective-Level Stop Conditions`, required when delegated drive/autonomous
  objective work is in scope.
- Initiative shape reference now says those sections are required for delegated
  drive/autonomous objective work and optional/not applicable for ordinary
  initiatives.
- Drive skill and continuity/checkpoint references now point at the same field
  names without creating a new authority record type or assigning live ticket
  execution ownership to initiatives.
- `ticket:authst4p` is `review_required`; ACC-001 through ACC-004 and
  `initiative:skills-corpus-council-precision-pass#OBJ-004` cite
  `evidence:initiative-authority-stop-conditions-validation` as
  evidence-supported pending mandatory critique. ACC-005 remains pending critique.

Validation:

- Targeted searches found the new initiative field names in
  `skills/loom-initiatives` and aligned drive references in `skills/loom-drive`.
- `git diff --check` passed with no output.

Evidence:

- `evidence:initiative-authority-stop-conditions-validation` records before/after
  observations and the `git diff --check` result.

Risks:

- No known implementation blocker. Because this is `protocol-authority` and high
  risk, the ticket still requires mandatory critique.

Recommended next route:

- Run oracle critique profiles `protocol-change`, `operator-clarity`, and
  `routing-safety`; keep ticket closure blocked until critique disposition is
  recorded in `ticket:authst4p`.

# Parent Merge Notes

Parent inspected the child output, ticket update, evidence record, and product
diff. The implementation stayed inside the declared child write scope and is
ready for mandatory oracle critique. This packet is marked `consumed`; ticket
acceptance remains ticket-owned after critique.
