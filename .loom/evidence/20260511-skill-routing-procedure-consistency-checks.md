# Skill Routing Procedure Consistency Checks

ID: evidence:20260511-skill-routing-procedure-consistency-checks
Type: Evidence Dossier
Status: recorded
Created: 2026-05-11
Updated: 2026-05-11
Observed: 2026-05-11

## Summary

Validation observations after clarifying record-skill versus workflow-specific skill semantics, adding routed-skill procedure requirements to playbook skills, and making Ralph launch wording transport-neutral.

## Observations

- Observation: `npm --prefix loom-core run smoke` passed from `/Users/alexanderbutler/code_projects/personal/agent-loom`.
  - Actual result: `ok: true`, `usingLoomFileCount: 7`, `instructionCount: 7`, and `skillCount: 11`.
- Observation: `npm --prefix loom-playbooks run smoke` passed.
  - Actual result: `ok: true`, `doesNotPreloadCoreDoctrine: true`, and `skillCount: 25`.
- Observation: `npm --prefix loom-core run pack:check` passed.
  - Actual result: smoke passed and dry-run pack completed with 65 files.
- Observation: `npm --prefix loom-playbooks run pack:check` passed.
  - Actual result: smoke passed and dry-run pack completed with 28 files.
- Observation: `git diff --check` passed.
  - Actual result: no output.
- Observation: grep over `loom-playbooks/skills` for `When routing to any named Loom skill, follow that skill's procedure and guidance` found 25 matches.
  - Actual result: one match appeared in each playbook `SKILL.md` file.
- Observation: grep over `loom-core/skills` for stale Ralph transport-specific phrases such as `For harness-native subagents`, `wrapper prompts short`, `launch prompt should`, `before invoking a harness subagent`, and `harness-native subagents only` returned no files.
- Observation: grep over `loom-core/skills` for `record skill`, `workflow-specific skill`, `target skill's procedure`, and `Every transport should point` found the new terminology and transport-neutral launch wording in the expected core doctrine and Ralph files.

## What This Shows

- Supports `ticket:20260511-skill-routing-procedure-consistency#ACC-001`: product-facing prose now names record skills and workflow-specific skills without using package-layer workflow precedence as the explanation.
- Supports `ticket:20260511-skill-routing-procedure-consistency#ACC-002`: all 25 playbook skill files contain the routed-skill procedure requirement.
- Supports `ticket:20260511-skill-routing-procedure-consistency#ACC-003`: core Ralph wording no longer contains the searched stale phrases that narrow packet-path launch guidance to harness-native subagents.
- Supports `ticket:20260511-skill-routing-procedure-consistency#ACC-004`: package smoke, package pack checks, and Markdown diff checks passed after the wording changes.

## What This Does Not Show

- It does not prove every possible synonym for stale wording is absent.
- It does not prove live agent behavior changes.
- It does not replace fresh-context review of whether the wording is logically consistent across the corpus.
- It does not inspect historical `.loom/` dogfood records as product-facing instruction surfaces.

## Related Records

- `ticket:20260511-skill-routing-procedure-consistency` - ticket supported by this evidence.
