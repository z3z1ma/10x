---
id: packet:ralph-ticket-evfresh8-20260503T024435Z
kind: packet
packet_kind: ralph
status: consumed
target: ticket:evfresh8
mode: execution
change_class: protocol-authority
risk_class: medium
style: reference-first
verification_posture: observation-first
iteration: 1
created_at: 2026-05-03T02:44:36Z
updated_at: 2026-05-03T02:47:50Z
scope:
  kind: repository
  repositories:
    - repo:root
child_write_scope:
  records:
    - None - child returns output only; parent reconciles ticket, evidence, critique, and packet status.
  paths:
    - skills/loom-evidence/templates/evidence.md
    - skills/loom-evidence/SKILL.md
    - skills/loom-evidence/references/evidence-quality.md
    - skills/loom-records/references/claim-coverage.md
parent_merge_scope:
  records:
    - ticket:evfresh8
  paths:
    - .loom/tickets/20260503-evfresh8-strengthen-evidence-freshness.md
    - .loom/evidence/20260503-evidence-freshness-validation.md
    - .loom/critique/evidence-freshness-review.md
    - .loom/packets/ralph/20260503T024435Z-ticket-evfresh8-iter-01.md
source_fingerprint:
  git_commit: a5b37b176f4a45159f155d41f7070ba6efcf2736
  integration_remote: origin
  integration_ref: origin/main
  integration_commit: a5b37b176f4a45159f155d41f7070ba6efcf2736
  git_status_summary: clean
  git_status_detail: clean working tree at packet compile time
  compiled_from:
    - ticket:evfresh8
    - plan:skills-corpus-residual-protocol-sharpening-pass
    - research:skills-corpus-residual-audit-synthesis
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
  max_excerpt_lines_per_file: 100
  avoid_full_file_reads: true
sources:
  constitution:
    - constitution:main
    - decision:0001
    - decision:0002
    - decision:0006
  initiative:
    - initiative:skills-corpus-residual-protocol-sharpening-pass
  research:
    - research:skills-corpus-residual-audit-synthesis
  spec: []
  plan:
    - plan:skills-corpus-residual-protocol-sharpening-pass
  ticket:
    - ticket:evfresh8
  files:
    - skills/loom-evidence/templates/evidence.md
    - skills/loom-evidence/SKILL.md
    - skills/loom-evidence/references/evidence-quality.md
    - skills/loom-records/references/claim-coverage.md
links: {}
---

# Mission

Fix `ticket:evfresh8` by strengthening evidence freshness metadata and adding a
concrete challenging-evidence example without making evidence own acceptance or
critique truth.

# Bound Context

The governing plan is `plan:skills-corpus-residual-protocol-sharpening-pass`.
This ticket follows `ticket:ralphchk7` in the strict sequential pass.

Keep these boundaries:

- evidence owns observations, not intended behavior, live execution state,
  critique verdicts, acceptance, or closure;
- tickets consume evidence for acceptance decisions;
- critique judges evidence sufficiency when required;
- do not require full raw logs inline for every evidence record;
- do not add validators, schemas, CLIs, helper scripts, runtime enforcement, or a
  new canonical owner layer.

# Source Snapshot

Current relevant state at baseline `a5b37b1`:

- `skills/loom-evidence/templates/evidence.md` already includes `Fresh enough
  for`, `Recheck when`, `Invalidated by`, and `Supersedes / superseded by`, but
  does not locally ask for explicit observed-at, source-state, procedure verdict,
  or exit-code fields.
- `skills/loom-evidence/SKILL.md` and `skills/loom-evidence/references/evidence-quality.md`
  explain freshness and limitations, but can make source state and procedure
  verdict more visible if needed.
- `skills/loom-records/references/claim-coverage.md` names `Supports Claims` and
  `Challenges Claims`, but lacks a concrete negative/challenging evidence example.

# Change Class

Declared above as `protocol-authority` with medium risk because evidence guidance
affects acceptance honesty and critique's ability to assess observed artifacts.

# Verification Targets

- `initiative:skills-corpus-residual-protocol-sharpening-pass#OBJ-010`
- `ticket:evfresh8#ACC-001`
- `ticket:evfresh8#ACC-002`
- `ticket:evfresh8#ACC-003`
- `ticket:evfresh8#ACC-004`

# Task For This Iteration

Make the smallest corpus edits that satisfy `ticket:evfresh8`:

1. Add observed-at/source-state/procedure/verdict metadata, or equivalent fields,
   to the evidence template.
2. Make freshness, invalidation, and recheck triggers visible enough that a copied
   evidence record cannot easily skip them.
3. Add a concrete challenge/negative-evidence example in claim coverage or
   evidence guidance.
4. Preserve evidence's owner boundary: evidence records observations and support
   or challenge links; tickets/specs/critique/wiki own their own truth decisions.

Do not update Loom tickets, evidence, critique, or this packet. The parent will
reconcile those after inspecting the returned diff.

# Verification Posture

Declared above as `observation-first`.

Before editing, inspect/report current matches for `Fresh enough for`,
`Invalidated by`, `Challenges Claims`, `exit code`, `verdict`, `source state`,
`observed at`, and challenge examples in the write-scope files. After editing,
report the same targeted observations and whether `git diff --check` passes.

# Stop Conditions

Stop and report `blocked` or `escalate` if:

- governing records or child-write-scope files differ materially from this packet;
- the fix would make evidence own acceptance, critique verdicts, intended
  behavior, ticket closure, or wiki explanation;
- the fix would require full raw logs inline for every evidence record;
- the fix would add runtime validation, schemas, command wrappers, helper scripts,
  or new canonical owner layers;
- satisfying the ticket requires wider source provenance policy that belongs in
  `ticket:srcmeta13`.

# Output Contract

Return:

- outcome (`continue|stop|blocked|escalate`);
- files changed;
- records changed (`None` expected);
- before/after observations and `git diff --check` result;
- self-review findings or concerns;
- blockers or residual risks;
- recommended ticket state and next route.

# Working Notes

Parent compiled from clean `main` at `a5b37b1` after pushing `ticket:ralphchk7`.

# Child Output

Outcome: stop

Files changed:

- `skills/loom-evidence/templates/evidence.md`
- `skills/loom-evidence/SKILL.md`
- `skills/loom-evidence/references/evidence-quality.md`

Records changed: None.

Before observations:

- Template had `Fresh enough for`, `Invalidated by`, and `# Challenges Claims`,
  but no explicit `Observed at`, `Source state`, `Procedure verdict`, or `exit
  code` fields.
- Guidance had generic challenge language, but no concrete negative-evidence
  example.

After observations:

- Template includes `Observed at`, `Source state`, `Procedure verdict / exit
  code`, stronger `Fresh enough for`, `Recheck when`, and `Invalidated by`
  prompts.
- Evidence skill/guidance now names observed-at, source-state, and
  procedure-verdict freshness expectations.
- Evidence quality includes a concrete failed `git diff --check` challenge
  example.

Validation: `git diff --check` passed with no output.

Self-review:

- Evidence remains observation-only and does not claim acceptance, critique
  verdicts, intended behavior, ticket closure, or wiki explanation.
- Full raw logs are explicitly not required inline.
- `skills/loom-records/references/claim-coverage.md` was not changed because the
  challenge example was added in evidence guidance, which the packet allowed.

Blockers/residual risks: no blockers. Parent should reconcile product diff with
ticket evidence and critique disposition.

Recommendation: set ticket to `review_required`; next route is parent evidence
recording, then critique/acceptance review.

# Parent Merge Notes

Accepted child output as in scope. Parent reviewed the diff, recorded evidence
`evidence:evidence-freshness-validation`, moved `ticket:evfresh8` to
`review_required`, and routed next to mandatory oracle critique.
