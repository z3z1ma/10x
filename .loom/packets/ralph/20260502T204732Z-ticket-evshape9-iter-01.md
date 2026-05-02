---
id: packet:ralph-ticket-evshape9-20260502T204732Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:evshape9
mode: execution
change_class: protocol-authority
risk_class: medium
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-02T20:47:32Z
updated_at: 2026-05-02T20:51:37Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - ticket:evshape9
    - evidence:evidence-quality-guidance-validation
    - packet:ralph-ticket-evshape9-20260502T204732Z
  paths:
    - skills/loom-evidence/**
    - skills/loom-tickets/SKILL.md
    - skills/loom-tickets/templates/ticket.md
    - skills/loom-tickets/references/acceptance-gate.md
    - .loom/tickets/20260502-evshape9-strengthen-evidence-quality-guidance.md
    - .loom/evidence/20260502-evidence-quality-guidance-validation.md
    - .loom/packets/ralph/20260502T204732Z-ticket-evshape9-iter-01.md
parent_merge_scope:
  records:
    - ticket:evshape9
    - evidence:evidence-quality-guidance-validation
    - packet:ralph-ticket-evshape9-20260502T204732Z
  paths:
    - .loom/critique/evidence-quality-guidance-review.md
source_fingerprint:
  git_commit: 4ee1f67f07bf4428829f57460870d24e06f080bf
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: 4ee1f67f07bf4428829f57460870d24e06f080bf
  git_status_summary: clean
  compiled_from:
    - initiative:skills-corpus-council-precision-pass
    - plan:skills-corpus-council-precision-pass
    - ticket:evshape9
    - ticket:retrod3p
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
  max_source_files: 8
  max_excerpt_lines_per_file: 160
  avoid_full_file_reads: false
sources:
  constitution:
    - constitution:main
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:evshape9
  references:
    - skills/loom-evidence/SKILL.md
    - skills/loom-evidence/templates/evidence.md
    - skills/loom-tickets/references/acceptance-gate.md
    - skills/loom-tickets/templates/ticket.md
links:
  initiative:
    - initiative:skills-corpus-council-precision-pass
  plan:
    - plan:skills-corpus-council-precision-pass
  ticket:
    - ticket:evshape9
---

# Mission

Strengthen evidence quality guidance so evidence records remain observed,
freshness-aware, limitation-aware, and useful for ticket acceptance without
becoming closure owners.

# Bound Context

This is the ninth ticket in `plan:skills-corpus-council-precision-pass` and
covers `initiative:skills-corpus-council-precision-pass#OBJ-009`. Dependency
`ticket:retrod3p` is closed. This ticket changes evidence and ticket teaching,
not evidence ownership or acceptance authority.

# Source Snapshot

Baseline is clean `main` at `4ee1f67f07bf4428829f57460870d24e06f080bf`.

Current observations:

- `skills/loom-evidence/SKILL.md` names evidence posture and default procedure,
  but no dedicated evidence-quality reference exists under `skills/loom-evidence/references/`.
- `skills/loom-evidence/templates/evidence.md` has sections for procedure,
  artifacts, environment, validity, limitations, result, and interpretation.
- `skills/loom-tickets/references/acceptance-gate.md` asks whether evidence is
  fresh enough and supports covered claims, but ticket evidence teaching is thin.

# Change Class

Declared as `protocol-authority`; evidence quality affects closure honesty, but
the bounded change must preserve evidence as observed-artifact owner only.

# Verification Targets

- `initiative:skills-corpus-council-precision-pass#OBJ-009`
- `ticket:evshape9#ACC-001`
- `ticket:evshape9#ACC-002`
- `ticket:evshape9#ACC-003`
- `ticket:evshape9#ACC-004`

# Task For This Iteration

1. Add or expand dedicated evidence-quality guidance under `skills/loom-evidence`.
2. Teach freshness, environment, observed result, limitations, support/challenge,
   invalidation/supersession, and proportional change-class expectations.
3. Align ticket evidence teaching where acceptance depends on evidence
   sufficiency, without making evidence own acceptance or closure.
4. Create `.loom/evidence/20260502-evidence-quality-guidance-validation.md` with
   before/after searches for evidence quality terms and `git diff --check`.
5. Update `ticket:evshape9` to `review_required` with evidence links, claim
   matrix, retrospective/promotion disposition pending, and mandatory critique
   recommendation. Do not close it.

# Verification Posture

`observation-first`.

Record before/after searches for terms including `freshness`, `fresh enough`,
`limitations`, `observed`, `inference`, `support`, `challenge`, `invalidation`,
`supersession`, and `git diff --check`.

# Stop Conditions

Stop and return `blocked` or `escalate` if:

- evidence quality guidance would require a schema/runtime validator;
- the change would make evidence own acceptance, critique verdicts, intended
  behavior, or closure;
- the change would require heavy evidence for trivial local edits;
- the ticket needs a separate spec or plan split to proceed truthfully.

# Output Contract

Return outcome, files changed, records changed, before/after observations,
validation commands/results, risks, and ticket recommendation. Include whether
the ticket should proceed to mandatory oracle critique profiles
`evidence-sufficiency`, `operator-clarity`, and `routing-safety`.

# Working Notes

Prefer a small reference plus targeted ticket teaching over broad rewrites.

# Child Output

Outcome: `stop`.

Files changed:

- `skills/loom-evidence/references/evidence-quality.md`
- `skills/loom-evidence/SKILL.md`
- `skills/loom-evidence/templates/evidence.md`
- `skills/loom-tickets/SKILL.md`
- `skills/loom-tickets/templates/ticket.md`
- `skills/loom-tickets/references/acceptance-gate.md`
- `.loom/evidence/20260502-evidence-quality-guidance-validation.md`
- `.loom/tickets/20260502-evshape9-strengthen-evidence-quality-guidance.md`
- `.loom/packets/ralph/20260502T204732Z-ticket-evshape9-iter-01.md`

Records changed:

- `ticket:evshape9`
- `evidence:evidence-quality-guidance-validation`
- `packet:ralph-ticket-evshape9-20260502T204732Z`

Before observation: searched evidence and ticket guidance for `freshness`,
`fresh enough`, `limitations`, `observed`, `inference`, `support`, `challenge`,
`invalidation`, `supersession`, and `git diff --check`. The search found
scattered observed/support/challenge/fresh-enough/limitations wording, but no
dedicated evidence-quality reference and no invalidation, supersession, or
literal `git diff --check` in the searched guidance targets.

After observation: the same search found the new dedicated evidence-quality
reference plus updated evidence skill, evidence template, ticket skill, ticket
template, and acceptance-gate teaching for observed artifacts before inference,
freshness / fresh enough, limitations, support/challenge, invalidation,
supersession, proportional evidence expectations, and the acceptance boundary.

Validation:

- `rg -n "freshness|fresh enough|limitations|observed|inference|support|challenge|invalidation|supersession|git diff --check" "skills/loom-evidence" "skills/loom-tickets/SKILL.md" "skills/loom-tickets/templates/ticket.md" "skills/loom-tickets/references/acceptance-gate.md"` — before/after observations recorded in `evidence:evidence-quality-guidance-validation`.
- `git diff --check` — passed with no output.

Residual risks:

- Structural searches do not prove operator clarity or downstream adoption.
- Mandatory oracle critique has not yet run.
- Ticket closure remains blocked by `ticket:evshape9#ACC-005` until critique has
  no unresolved findings or the ticket records valid dispositions.

Ticket recommendation: keep `ticket:evshape9` in `review_required` and proceed
to mandatory oracle critique profiles `evidence-sufficiency`, `operator-clarity`,
and `routing-safety`.

# Parent Merge Notes

Parent accepted the bounded child output for critique handoff. Ticket
`ticket:evshape9` truthfully reflects `review_required`, links
`evidence:evidence-quality-guidance-validation`, and leaves acceptance/closure
pending mandatory oracle critique.
