---
id: evidence:grill-spec-plan-validation
kind: evidence
status: recorded
created_at: 2026-05-07T14:59:56Z
updated_at: 2026-05-07T15:04:23Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:grill507
  research:
    - research:grill-diagnose-gap-analysis
  critique:
    - critique:grill-spec-plan-review
external_refs: {}
---

# Summary

Structural validation and targeted content observations for the spec/plan grilling
and diagnose-gap skill edits under `ticket:grill507`.

This evidence records observations. It does not decide ticket acceptance or close
critique findings.

# Procedure

Observed at: 2026-05-07T14:59:56Z

Source state: branch `main`, with tracked skill edits plus untracked root `.loom`
records for this Loom work. Unrelated todo-app example files were present in the
worktree and were not part of this validation scope.

Procedure:

- Ran `git diff --check -- skills/loom-specs skills/loom-plans skills/loom-debugging .loom/tickets/20260507-grill507-bake-grilling-into-spec-plan.md .loom/research/20260507-grill-diagnose-gap-analysis.md`.
- After critique follow-up edits, reran scoped `git diff --check` including this
  evidence record.
- Searched scoped `loom-specs`, `loom-plans`, and `loom-debugging` Markdown files
  for trailing whitespace.
- Searched active `ticket:grill507` and `research:grill-diagnose-gap-analysis`
  records for trailing whitespace and unresolved placeholder patterns.
- Searched changed skill files for guidance anchors: `Spec Grilling Pass`,
  `Planning Grilling Pass`, `Execution Units / Ticket Slices`, `feedback loop is
  the work`, `no credible loop`, `orient -> feedback loop`, and `Material ...
  question, one row at a time` template wording.
- Listed changed scoped skill files with `git diff --name-only -- skills/loom-specs skills/loom-plans skills/loom-debugging`.
- Searched scoped changed skill directories for hidden-runtime drift terms: `MCP`,
  `DevTools`, `subagent`, `hook`, `daemon`, `installer`, `command wrapper`,
  `commit`, and `runtime`.

Expected result: no whitespace errors; no trailing whitespace in scoped skill or
active root `.loom` files; no unresolved placeholders in active saved records;
new guidance anchors appear in the intended spec, plan, and debugging surfaces;
hidden-runtime search does not show newly required runtime, command, hook, MCP,
subagent, or commit mechanics as Loom core.

Actual observed result:

- `git diff --check` produced no output for the scoped skill and active-record
  paths.
- Trailing-whitespace searches returned no files for scoped `loom-specs`,
  `loom-plans`, `loom-debugging`, active `ticket:grill507`, and active research.
- Placeholder-pattern searches returned no files for active `ticket:grill507` and
  `research:grill-diagnose-gap-analysis`.
- Anchor search found `Spec Grilling Pass` in `skills/loom-specs/references/spec-shape.md` and `skills/loom-specs/templates/spec.md`.
- Anchor search found `Planning Grilling Pass` and `Execution Units / Ticket Slices` in `skills/loom-plans/references/plan-shape.md` and `skills/loom-plans/templates/plan.md`.
- Anchor search found `feedback loop is the work` and `no credible loop` in `skills/loom-debugging/references/systematic-debugging.md`.
- Post-critique anchor search found `orient -> feedback loop` in
  `skills/loom-debugging/SKILL.md`, `Material operator question, one row at a time`
  in `skills/loom-specs/templates/spec.md`, and `Material decomposition question,
  one row at a time` in `skills/loom-plans/templates/plan.md`.
- Changed scoped skill files were:
  `skills/loom-debugging/SKILL.md`,
  `skills/loom-debugging/references/systematic-debugging.md`,
  `skills/loom-plans/SKILL.md`,
  `skills/loom-plans/references/plan-shape.md`,
  `skills/loom-plans/references/slicing.md`,
  `skills/loom-plans/templates/plan.md`,
  `skills/loom-specs/SKILL.md`,
  `skills/loom-specs/references/spec-shape.md`, and
  `skills/loom-specs/templates/spec.md`.
- Hidden-runtime term search found benign matches only: existing `slicing.md`
  commit-save-point guardrail that says commits are not required unless the
  operator or project workflow asks, `plan-shape.md` using `commitments` as normal
  roadmap language, and `systematic-debugging.md` using `commits` for bisection
  and `runtime` for performance measurement context.

Procedure verdict / exit code: pass for scoped structural checks. Mandatory
critique is recorded separately as `critique:grill-spec-plan-review`.

# Supports Claims

- `ticket:grill507#ACC-001` - gap research records direct source comparison and
  remaining spec/plan/debugging gaps.
- `ticket:grill507#ACC-002` - spec guidance and template now include active spec
  grilling around codebase-first inspection, one material question at a time,
  recommended answers, terminology conflicts, scenarios, and decision routing.
- `ticket:grill507#ACC-003` - plan guidance and template now center decomposition
  into execution units / ticket slices with source claims, outcomes, write scope,
  verification, non-goals, dependencies, and loopbacks.
- `ticket:grill507#ACC-004` - debugging guidance now stresses domain orientation,
  feedback-loop construction, and stopping when no credible loop can be built.
- `ticket:grill507#ACC-005` - structural checks, hidden-runtime scan, and mandatory
  critique support no unresolved high/medium blocker, hidden-runtime drift, or
  owner-layer boundary regression in the scoped files.

# Challenges Claims

None from the scoped checks. Mandatory critique recorded only low, non-blocking
findings and a ticket-reconciliation requirement.

# Limitations

- This is structural and content-anchor evidence, not proof that future agents will
  follow the guidance correctly.
- This repository has no automated test suite for Markdown skill behavior.
- The evidence does not validate unrelated todo-app example files or unrelated
  historical root `.loom` records.

# Result

The scoped validation observed clean whitespace checks, clean active saved-record
placeholder scans, intended guidance anchors in spec/plan/debugging surfaces, and
no hidden-runtime requirement drift in the searched scoped skill directories.

# Related Records

- `ticket:grill507`
- `research:grill-diagnose-gap-analysis`
- `critique:grill-spec-plan-review`
