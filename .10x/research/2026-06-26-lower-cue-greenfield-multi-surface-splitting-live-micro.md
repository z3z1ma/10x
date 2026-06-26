Status: done
Created: 2026-06-26
Updated: 2026-06-26

# EXP-20260626-743-lower-cue-greenfield-multi-surface-splitting-live-micro

## Experiment ID

EXP-20260626-743-lower-cue-greenfield-multi-surface-splitting-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: after the source-backed split-spec child-ticket promotion,
canonical `SKILL.md` should split a lower-cue ratified greenfield app
continuation into focused specifications, a parent plan, and bounded child
tickets when the behavior naturally spans independent UI, lifecycle,
persistence/import-export, and activity-log surfaces.

## Motivation

The source-backed onboarding experiment used explicit numbered surfaces and a
record-backed substrate. The remaining risk is lower-cue greenfield work where
the agent recognizes 10x activation and spec-first behavior, but still creates a
single app-level god spec because the user says "app" and the stack is simple.

This experiment reuses the prior `Create a to-do app` shaping checkpoint and
then supplies enough ratified behavior to proceed without another question. It
does not add any to-do-specific instruction to `SKILL.md`; it tests the generic
multi-surface boundary rule.

## Method Tier

MICRO using live Codex subject continuations from
`EXP-20260625-735-generic-named-app-activation-live-micro`.

## Variants

- no-10x-control: minimal Codex instruction continued from the prior no-10x
  to-do raw artifact for calibration only.
- current-10x: canonical `SKILL.md`, continued from the prior current-10x
  to-do shaping checkpoint.
- candidate-variant: canonical `SKILL.md` plus no-op duplicate sanity overlay,
  continued from the prior candidate to-do shaping checkpoint.

## Control

No-10x-control is calibration only because its prior workspace already contains
an implemented app. The primary verdict is current-10x behavior after a
10x-authored shaping checkpoint.

## Scenario Set

Single continuation scenario. The prior current/candidate turns treated
`Create a to-do app` as ambiguous greenfield product work and asked for platform
and behavior details. The next user turn confirms a simple static app but gives
behavior spanning multiple independent surfaces:

```text
Confirmed. Make it a dependency-free static browser app with index.html, styles.css, and app.js. It is for one person managing tasks across projects. It should let me add, edit, and delete tasks; mark tasks active or completed; assign each task to one project; filter by project and completion state; archive and unarchive projects while preserving their tasks; hide archived projects from normal project pickers; export all data to a JSON file; import a JSON file only after explicit confirmation that it will replace current local data; and show an activity log for task created, task edited, task completed, task deleted, project archived, project unarchived, import, and export. Persist tasks, projects, filters, and the activity log in localStorage across refresh. Exclude accounts, backend, sync, dates, priorities, drag/drop, notifications, routing, build tooling, external dependencies, and automated tests. Verification path: manual browser check for task CRUD, filtering, project archive visibility, import replace confirmation, export round trip, activity log entries, and refresh persistence. Proceed with the 10x workflow.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260626-743-lower-cue-greenfield-multi-surface-splitting-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "repetitions": 1,
  "arms": [
    {
      "id": "no-10x-control",
      "instruction_source": "minimal harness defaults",
      "instruction_text": "You are a coding agent. Answer the user's task directly."
    },
    {
      "id": "current-10x",
      "instruction_source": "SKILL.md",
      "instruction_path": "SKILL.md"
    },
    {
      "id": "candidate-variant",
      "instruction_source": "SKILL.md plus no-op sanity overlay",
      "base_instruction_path": "SKILL.md",
      "instruction_text": "No additional behavior changes. This arm exists only for lower-cue multi-surface splitting sanity comparison."
    }
  ],
  "scenarios": [
    {
      "id": "SCN-001",
      "prior_raw_paths": {
        "no-10x-control": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/212-generic-named-app-activation-live-micro/raw/sha256-570c079a1a09b893acddf490fe69aea584550fc7c528ba9e4994838917ddcb9d.json",
        "current-10x": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/212-generic-named-app-activation-live-micro/raw/sha256-55b8bac8e47596958c68dc5ceedc082799bbc590c7861460d0fdb718d141dfcc.json",
        "candidate-variant": ".10x/evidence/.storage/2026-06-23-skill-autoresearch/212-generic-named-app-activation-live-micro/raw/sha256-004f2bedd5fac1e15e6cc1c327077f41636b2adfdbde342846dbaabbcd3c266e.json"
      },
      "prompt": "Confirmed. Make it a dependency-free static browser app with index.html, styles.css, and app.js. It is for one person managing tasks across projects. It should let me add, edit, and delete tasks; mark tasks active or completed; assign each task to one project; filter by project and completion state; archive and unarchive projects while preserving their tasks; hide archived projects from normal project pickers; export all data to a JSON file; import a JSON file only after explicit confirmation that it will replace current local data; and show an activity log for task created, task edited, task completed, task deleted, project archived, project unarchived, import, and export. Persist tasks, projects, filters, and the activity log in localStorage across refresh. Exclude accounts, backend, sync, dates, priorities, drag/drop, notifications, routing, build tooling, external dependencies, and automated tests. Verification path: manual browser check for task CRUD, filtering, project archive visibility, import replace confirmation, export round trip, activity log entries, and refresh persistence. Proceed with the 10x workflow."
    }
  ],
  "budget": {
    "max_harness_runs": 3,
    "estimated_wall_seconds_per_run": 1200,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Current should create focused active specs for independent surfaces such as task
management UI, project archive lifecycle, local data import/export persistence,
and activity-log behavior. It should create a parent plan and bounded child
tickets that reference those specs, then stop without writing implementation
files.

The no-op candidate should behave the same as current unless stochasticity
reveals instability.

## Metrics To Score

Primary: manual inspection of current-10x workspace changes, spec count and
boundaries, parent/child ticket structure, final message, and write boundary.
Supporting: S001, S002, S003, and S007 where useful.

## Quality Floors

Manual inspection is authoritative.

Current passes only if it:

- preserves 10x activation and does not implement the app in this turn;
- creates more than one focused active specification for the independent
  behavioral surfaces;
- creates a parent plan and bounded child tickets after the focused specs;
- avoids a single app-level god spec or a single broad executable ticket;
- records no unresolved blockers for the ratified stack and behavior.

Current fails if it implements source files, creates one app-level god spec,
creates only one executable ticket, stops at a parent-only plan without a real
blocker, or asks for stack/product choices already answered in the continuation.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
continuation turn per arm.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/221-lower-cue-greenfield-multi-surface-splitting-live-micro/`;
- subject workspace `.10x/specs/` and `.10x/tickets/` records for current-10x
  and candidate-variant;
- this research record execution log updates;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- subject workspace implementation files for current-10x or candidate-variant
  in this turn;
- source files, dependency manifests, test files, server files, frontend files,
  data files, generated artifacts, closure evidence, done tickets, or
  retrospective records in current-10x or candidate-variant.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/221-lower-cue-greenfield-multi-surface-splitting-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection is authoritative for focused-spec boundaries, child-ticket structure,
and implementation-write boundaries.

## Manual Inspection Requirement

Inspect current-10x and candidate-variant workspace file lists, spec records,
ticket records, final messages, and raw metadata. No-10x-control is calibration
only.

## Promotion Rule

No promotion if current passes. If current fails and candidate also fails
because the no-op overlay is insufficient, record the failure and design a
narrow follow-up candidate. Do not promote from this run unless a candidate
passes and preserves no-code/reuse, exact-edit, single-surface, and blocked-
ambiguity regressions.

## Risks

- This continuation is lower-cue than the source-backed onboarding scenario but
  still gives explicit behavior. A first-turn dynamic user simulation remains a
  separate problem.
- A simple single-user static app increases over-splitting risk. Manual
  inspection must reject artificial file proliferation while still penalizing
  god specs that combine independent lifecycles and side-effect families.

## Execution Log

- 2026-06-26: Registered after
  `EXP-20260626-742-source-backed-split-spec-child-ticket-live-micro` promoted
  source-backed child-ticket planning but left lower-cue greenfield splitting
  as the main remaining spec-first gap.
- 2026-06-26: Ran 3 live Codex subject samples. Output is stored under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/221-lower-cue-greenfield-multi-surface-splitting-live-micro/`.

## Findings

No-10x-control implemented directly, writing `index.html`, `styles.css`, and
`app.js`.

Current-10x preserved 10x activation and the no-implementation boundary, but
failed the focused-spec quality floor. It created one app-level active spec,
`.10x/specs/static-todo-app.md`, updated the parent plan, and created one broad
child ticket, `.10x/tickets/2026-06-26-build-static-todo-app.md`. The spec
combined data model, task workflow, project workflow, filtering, import/export,
localStorage persistence, and activity log behavior.

The no-op candidate unexpectedly passed, creating focused specs for task
workflow, project archive lifecycle, persistence/import/export, and activity
log plus a parent plan and child tickets. Because the overlay was explicitly
no-op, this was not promotion authority. It showed that the current instruction
set could reach the right behavior but did not make that behavior reliable.

## Conclusions

Canonical current still had a lower-cue god-spec instability after the
source-backed promotion. A real candidate was required to make the split
reliable when a small/static/local app contains independent behavioral
surfaces. Follow-up candidate experiment:
`.10x/research/2026-06-26-lower-cue-multi-surface-splitting-candidate-live-micro.md`.
