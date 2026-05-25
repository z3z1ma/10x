# Reusable Learning Record Skill Kernels Validation

ID: evidence:20260525-reusable-learning-record-skill-kernels-validation
Type: Evidence Dossier
Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Summary

This dossier records validation for the bounded Ralph worker run that compressed `loom-knowledge` and `loom-retrospective` into smaller station kernels.

## Observations

- Observation: Before line counts for the touched reusable-learning skill families.
  - Procedure/source: `wc -l` over `loom-core/skills/loom-knowledge/SKILL.md`, `loom-core/skills/loom-knowledge/references/*.md`, `loom-core/skills/loom-knowledge/templates/*.md`, `loom-core/skills/loom-retrospective/SKILL.md`, and `loom-core/skills/loom-retrospective/references/*.md` before edits.
  - Actual result: 1,047 total lines before compression.

- Observation: After line counts for the same file set.
  - Procedure/source: Same `wc -l` target set after edits.
  - Actual result: 846 total lines after compression, a reduction of 201 lines.

- Observation: Scoped diff showed material compression.
  - Procedure/source: `git diff --stat -- loom-core/skills/loom-knowledge loom-core/skills/loom-retrospective`.
  - Actual result: 14 files changed, 218 insertions, and 419 deletions.

- Observation: Core smoke validation passed.
  - Procedure/source: `npm --prefix loom-core run smoke` from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: command exited 0 and reported `"ok": true`.

- Observation: Core package check passed.
  - Procedure/source: `npm --prefix loom-core run pack:check` from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: command exited 0, reran Core smoke successfully, and completed `npm pack --dry-run` with 69 files in the dry-run tarball.

- Observation: Markdown whitespace check passed before and after record updates.
  - Procedure/source: `git diff --check` from `/Users/alexanderbutler/code_projects/personal/agent-loom` after source edits before evidence/ticket record updates, then again after those record updates.
  - Actual result: command exited 0 with no output both times.

- Observation: Targeted behavior searches found required reusable-learning terms in touched skill families.
  - Procedure/source: grep-tool searches for knowledge, `Knowledge Preference`, `Triggers:`, `Applies To:`, retrieval, eager loading, procedure, preference, troubleshooting, atlas, entity, `Status: active`, retrospective, promotion, prevention, originating records, follow-up, and destination surface terms.
  - Actual result: matches were present across the relevant skill families, including active preference loading, task retrieval, knowledge maintenance, retrospective promotion/prevention routing, originating record updates, and evidence/audit/ticket follow-up routes.

- Observation: Reference-link search found the retained detail cards are still linked.
  - Procedure/source: grep-tool search for `references/knowledge-shape.md`, `references/retrieval-and-loading.md`, `references/maintaining-knowledge.md`, `references/promotion-and-prevention.md`, and `templates/` in skill kernels.
  - Actual result: `loom-knowledge/SKILL.md` links its three references and templates; `loom-retrospective/SKILL.md` links `references/promotion-and-prevention.md`.

- Observation: Product-surface leakage search found no contributor-process leakage requiring correction.
  - Procedure/source: grep-tool searches for `smoke`, `adapter`, `dogfood`, `package`, `npm`, `repo`, `repository workflow`, `test harness`, `skill-authoring`, and `why Loom is built` under `loom-core/skills/loom-knowledge` and `loom-core/skills/loom-retrospective`.
  - Actual result: `loom-retrospective` had no matches. `loom-knowledge` matches were runtime terms such as package/service retrieval cues, record reporting, and package atlas examples; no package smoke, adapter mechanics, dogfood state, or contributor workflow instruction was found in the touched product doctrine.

## Artifacts

- `loom-core/skills/loom-knowledge/**` - compressed knowledge station kernel, detail cards, and templates.
- `loom-core/skills/loom-retrospective/**` - compressed retrospective station kernel and promotion/prevention detail card.

## What This Shows

- `ticket:20260525-record-skill-kernels#ACC-001` - supports for this run's scope - the two touched station kernels preserve owner truth, triggers, inspect/write paths, lifecycle/status rules or record shape, stop conditions, and non-examples.
- `ticket:20260525-record-skill-kernels#ACC-002` - supports for this run's scope - retained references and templates remain linked from their owning `SKILL.md` files and are shorter detail cards or compact templates.
- `ticket:20260525-record-skill-kernels#ACC-004` - supports for this run's scope - before/after line counts show compression for the two touched skill families.
- `ticket:20260525-record-skill-kernels#ACC-005` - supports for this run's scope - Core smoke, Core pack check, and `git diff --check` passed before and after record updates.

## What This Does Not Show

- This does not replace fresh-context audit for the ticket or final compression plan.
- This does not prove every possible model behavior; it records source inspection, targeted searches, line counts, and package validation for this bounded run.
- This evidence does not include a fresh audit of the compressed reusable-learning skill families.
- This evidence does not include Playbooks validation because this run did not touch Playbooks surfaces.

## Related Records

- `ticket:20260525-record-skill-kernels` - active ticket this evidence supports.
- `spec:loom-protocol-compression` - compression contract.
- `evidence:20260525-execution-spine-record-skill-kernels-validation` - prior bounded run evidence for ticket, Ralph, evidence, and audit skill families.
- `evidence:20260525-direction-record-skill-kernels-validation` - prior bounded run evidence for constitution, specs, plans, and research skill families.
