# Direction Record Skill Kernels Validation

ID: evidence:20260525-direction-record-skill-kernels-validation
Type: Evidence Dossier
Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

This dossier records validation for the bounded Ralph worker run that compressed
`loom-constitution`, `loom-specs`, `loom-plans`, and `loom-research` into smaller
station kernels.

## Observations

- Observation: Before line counts for the touched direction-setting skill families.
  - Procedure/source: `wc -l` over 21 files under `loom-constitution`, `loom-specs`, `loom-plans`, and `loom-research` before edits.
  - Actual result: 2,880 total lines before compression.

- Observation: After line counts for the same file set.
  - Procedure/source: Same `wc -l` target set after edits.
  - Actual result: 1,648 total lines after compression, a reduction of 1,232 lines.

- Observation: Scoped diff showed material compression.
  - Procedure/source: `git diff --stat -- loom-core/skills/loom-constitution loom-core/skills/loom-specs loom-core/skills/loom-plans loom-core/skills/loom-research`.
  - Actual result: 14 files changed, 651 insertions, and 1,883 deletions. Templates were retained unchanged.

- Observation: Core smoke validation passed.
  - Procedure/source: `npm --prefix loom-core run smoke` from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: command exited 0 and reported `"ok": true`.

- Observation: Core package check passed.
  - Procedure/source: `npm --prefix loom-core run pack:check` from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: command exited 0, reran Core smoke successfully, and completed `npm pack --dry-run` with 69 files in the dry-run tarball.

- Observation: Markdown whitespace check passed before and after record updates.
  - Procedure/source: `git diff --check` from `/Users/alexanderbutler/code_projects/personal/agent-loom` after source edits and before evidence/ticket record updates.
  - Actual result: command exited 0 with no output before evidence/ticket record updates, then exited 0 with no output again after those record updates.

- Observation: Targeted behavior searches found required station terms in touched skill families.
  - Procedure/source: grep-tool searches for constitution, decision, roadmap, principle, spec, `REQ-*`, `SCN-*`, plan, execution units, child tickets, milestones, current state, journal, research, findings, conclusions, tradeoffs, rejected paths, null results, statuses, templates, and reference links.
  - Actual result: matches were present across the relevant skill families, including owner truth, read/write paths, lifecycle/status terms, templates, and detail-card links.

- Observation: Product-surface leakage search found no contributor-process leakage in the touched skill families.
  - Procedure/source: grep-tool searches for `smoke`, `adapter`, `dogfood`, `package`, `npm`, `repo`, `repository workflow`, `test harness`, `skill-authoring`, and `why Loom is built` under the four touched families after cleanup.
  - Actual result: no files found.

## Artifacts

- `loom-core/skills/loom-constitution/**` - compressed constitution station kernel and detail cards.
- `loom-core/skills/loom-specs/**` - compressed specs station kernel and detail card.
- `loom-core/skills/loom-plans/**` - compressed plans station kernel and detail cards.
- `loom-core/skills/loom-research/**` - compressed research station kernel and detail cards.

## What This Shows

- `ticket:20260525-record-skill-kernels#ACC-001` - partially supports - the four touched direction-setting station kernels preserve owner truth, triggers, inspect/write paths, lifecycle/status rules or record shapes, stop conditions, and non-examples for this run's scope.
- `ticket:20260525-record-skill-kernels#ACC-002` - partially supports - references and templates for the four touched families remain linked from owning `SKILL.md` files and were retained as shorter detail cards.
- `ticket:20260525-record-skill-kernels#ACC-004` - partially supports - before/after line counts show material compression for the four touched skill families.
- `ticket:20260525-record-skill-kernels#ACC-005` - partially supports - Core smoke, Core pack check, and `git diff --check` passed for this bounded run; `git diff --check` was rerun after evidence/ticket record updates.

## What This Does Not Show

- This does not prove `loom-knowledge` or `loom-retrospective` are compressed.
- This does not replace fresh-context audit for the ticket or final compression plan.
- This does not prove every possible model behavior; it records source inspection, targeted searches, line counts, and package validation for this bounded run.
- This does not include a fresh audit of the compressed direction-setting skill families.

## Related Records

- `ticket:20260525-record-skill-kernels` - active ticket this evidence supports.
- `spec:loom-protocol-compression` - compression contract.
- `evidence:20260525-execution-spine-record-skill-kernels-validation` - prior bounded run evidence for ticket, Ralph, evidence, and audit skill families.
