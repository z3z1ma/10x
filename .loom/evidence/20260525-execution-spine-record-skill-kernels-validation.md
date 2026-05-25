# Execution Spine Record Skill Kernels Validation

ID: evidence:20260525-execution-spine-record-skill-kernels-validation
Type: Evidence Dossier
Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

This dossier records validation for the bounded Ralph worker run that compressed `loom-tickets`, `loom-ralph`, `loom-evidence`, and `loom-audit` into smaller station kernels.

## Observations

- Observation: Before line counts for the touched execution-spine skill families.
  - Procedure/source: `wc -l` over the 19 files under the touched `loom-tickets`, `loom-ralph`, `loom-evidence`, and `loom-audit` skill families.
  - Actual result: 2,372 total lines before compression.

- Observation: After line counts for the same file set.
  - Procedure/source: Same `wc -l` target set after edits.
  - Actual result: 1,358 total lines after compression, a reduction of 1,014 lines.

- Observation: Core smoke validation passed.
  - Procedure/source: `npm --prefix loom-core run smoke` from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: command exited 0 and reported `"ok": true`.

- Observation: Core package check passed.
  - Procedure/source: `npm --prefix loom-core run pack:check` from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: command exited 0, reran Core smoke successfully, and completed `npm pack --dry-run` with 69 files in the dry-run tarball.

- Observation: Markdown whitespace check passed before and after record updates.
  - Procedure/source: `git diff --check` from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: command exited 0 with no output before evidence/ticket record updates, then exited 0 with no output again after those record updates.

- Observation: Targeted behavior searches found the expected execution-spine terms in touched skills.
  - Procedure/source: `grep` tool searches for ticket, `ACC-*`, Ralph, evidence, audit, worker output, reconciliation, closure, statuses, bounded context, launch transport, observation limits, `FIND-*`, and verdict language under the touched skill families.
  - Actual result: matches were present across the relevant skill families, including ticket atomicity/status/closure, Ralph durable context/read-write scope/stop conditions/worker output, evidence observation and non-acceptance boundaries, and audit Ralph review/findings/verdict boundaries.

- Observation: Packet-retirement search found no active packet handoff language in the touched ticket/Ralph/audit skill files.
  - Procedure/source: `grep` tool searches for `packet:`, `.loom/packets`, and `packets/` under `loom-core/skills/loom-tickets`, `loom-core/skills/loom-ralph`, and `loom-core/skills/loom-audit`.
  - Actual result: no files found.

- Observation: Product-surface leakage search found no contributor-process leakage requiring correction in the touched skill files.
  - Procedure/source: `grep` tool search for `smoke`, `adapter`, `dogfood`, `package`, `npm`, `repo`, `repository workflow`, `test harness`, `skill-authoring`, and `why Loom is built` under touched skill files.
  - Actual result: matches for runtime concepts such as packages as audit targets, repository files/worktree in Ralph context, reports, and finding output; no package smoke, adapter mechanics, dogfood state, or contributor workflow instruction was found in the touched product doctrine.

## Artifacts

- `loom-core/skills/loom-tickets/**` - compressed ticket station kernel and detail cards.
- `loom-core/skills/loom-ralph/**` - compressed Ralph station kernel and detail cards.
- `loom-core/skills/loom-evidence/**` - compressed evidence station kernel and templates.
- `loom-core/skills/loom-audit/**` - compressed audit station kernel and templates.
- `git diff --stat -- loom-core/skills/loom-tickets loom-core/skills/loom-ralph loom-core/skills/loom-evidence loom-core/skills/loom-audit` - reported 19 files changed, 652 insertions, 1,666 deletions.

## What This Shows

- `ticket:20260525-record-skill-kernels#ACC-001` - partially supports - the four touched station kernels preserve owner truth, triggers, inspect/write paths, lifecycle/status rules or record shapes, stop conditions, and non-examples for this run's scope.
- `ticket:20260525-record-skill-kernels#ACC-002` - partially supports - references and templates for the four touched families remain linked from their owning `SKILL.md` files and were retained as shorter detail cards.
- `ticket:20260525-record-skill-kernels#ACC-003` - supports for this run's scope - ticket, Ralph, evidence, and audit source inspection/searches found the execution spine terms and no active packet handoff language.
- `ticket:20260525-record-skill-kernels#ACC-004` - partially supports - before/after line counts show material compression for the four touched skill families.
- `ticket:20260525-record-skill-kernels#ACC-005` - partially supports - Core smoke, Core pack check, and `git diff --check` passed for this bounded run; `git diff --check` was rerun after evidence/ticket record updates.

## What This Does Not Show

- This does not prove the remaining record skill families are compressed.
- This does not replace fresh-context audit for the ticket or final compression plan.
- This does not prove every possible model behavior; it records source inspection, targeted searches, line counts, and package validation for this bounded run.
- This evidence does not include a fresh audit of the compressed execution-spine skill families.

## Related Records

- `ticket:20260525-record-skill-kernels` - active ticket this evidence supports.
- `spec:loom-protocol-compression` - compression contract.
- `spec:ticket-owned-worker-handoffs` - execution-spine behavior contract.
