Status: done
Created: 2026-06-26
Updated: 2026-06-26

# EXP-20260626-747-post-ticket-boundary-multi-surface-splitting-control-live-micro

## Experiment ID

EXP-20260626-747-post-ticket-boundary-multi-surface-splitting-control-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: after promoting the child-ticket-boundary corrective mutation,
canonical `SKILL.md` should still split genuinely multi-surface greenfield app
behavior into focused specifications, a parent plan, and bounded child tickets.
The new anti-over-ticketing language must not collapse independent workflows,
lifecycles, destructive data replacement, persistence, and activity-log side
effects into a god spec or one broad child ticket.

## Motivation

The previous corrective mutation was intentionally narrow: keep cohesive
implementation plus its proof in one child ticket. Its regression risk is
under-decomposition. This control replays the lower-cue multi-surface app
scenario that previously justified the anti-god-spec promotion.

## Method Tier

MICRO using live Codex subject continuations from
`EXP-20260625-735-generic-named-app-activation-live-micro`.

## Variants

- no-10x-control: minimal Codex instruction continued from the prior no-10x
  to-do raw artifact for calibration only.
- current-10x: canonical `SKILL.md` after the ticket-boundary corrective
  promotion.
- candidate-variant: canonical `SKILL.md` plus no-op duplicate sanity overlay.

## Scenario Set

Single lower-cue multi-surface continuation:

```text
Confirmed. Make it a dependency-free static browser app with index.html, styles.css, and app.js. It is for one person managing tasks across projects. It should let me add, edit, and delete tasks; mark tasks active or completed; assign each task to one project; filter by project and completion state; archive and unarchive projects while preserving their tasks; hide archived projects from normal project pickers; export all data to a JSON file; import a JSON file only after explicit confirmation that it will replace current local data; and show an activity log for task created, task edited, task completed, task deleted, project archived, project unarchived, import, and export. Persist tasks, projects, filters, and the activity log in localStorage across refresh. Exclude accounts, backend, sync, dates, priorities, drag/drop, notifications, routing, build tooling, external dependencies, and automated tests. Verification path: manual browser check for task CRUD, filtering, project archive visibility, import replace confirmation, export round trip, activity log entries, and refresh persistence. Proceed with the 10x workflow.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260626-747-post-ticket-boundary-multi-surface-splitting-control-live-micro",
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
      "instruction_text": "No additional behavior changes. This arm exists only for post-ticket-boundary anti-god-spec sanity comparison."
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

Current should create multiple focused active specifications, a parent plan,
and bounded child tickets, then stop without app implementation files.

## Metrics To Score

Manual inspection of spec boundaries, parent/child ticket structure, final
message, raw metadata, and archived workspace file list.

## Quality Floors

Manual inspection is authoritative.

Current passes if it:

- preserves 10x activation and does not implement app files;
- creates more than one focused active specification for independent behavior
  surfaces;
- creates a parent plan and bounded child tickets after the focused specs;
- avoids a single app-level god spec;
- avoids one broad executable child ticket for all surfaces;
- records no unresolved blockers for the ratified stack and behavior.

Current fails if it implements source files, creates one app-level god spec,
creates only one broad child ticket, stops at a parent-only plan without a real
blocker, or asks for already-ratified stack/product choices.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
continuation turn per arm.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/225-post-ticket-boundary-multi-surface-splitting-control-live-micro/`;
- subject workspace `.10x/specs/` and `.10x/tickets/` records for current-10x
  and candidate-variant;
- this research record execution log updates;
- evidence/review records after inspection.

Disallowed writes:

- canonical `SKILL.md`;
- `autoresearch/program.md`;
- subject workspace implementation files for current-10x or candidate-variant.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/225-post-ticket-boundary-multi-surface-splitting-control-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection is authoritative.

## Manual Inspection Requirement

Inspect current-10x and candidate-variant workspace file lists, spec records,
ticket records, final messages, and raw metadata.

## Promotion Rule

No promotion if current passes. If current fails by collapsing independent
surfaces into a god spec or one broad ticket, design a corrective candidate
that preserves the anti-over-ticketing rule for genuinely cohesive surfaces.

## Risks

- One repetition may miss stochastic under-decomposition. If this passes, run
  broader multi-surface controls later, especially in non-Codex harnesses.

## Execution Log

- 2026-06-26: Registered after promoting the child-ticket-boundary corrective
  mutation in `4f421247`.
- 2026-06-26: Ran 3 live Codex subject samples with
  `--require-clean-canonical`. Output is stored under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/225-post-ticket-boundary-multi-surface-splitting-control-live-micro/`.

## Findings

Current-10x passed manual inspection:

- It created three focused active specifications:
  `.10x/specs/todo-task-project-workflow.md`,
  `.10x/specs/todo-local-data-portability.md`, and
  `.10x/specs/todo-activity-log.md`.
- It updated one parent plan:
  `.10x/tickets/2026-06-25-create-todo-app.md`.
- It created three bounded child tickets:
  `.10x/tickets/2026-06-25-implement-task-project-workflow.md`,
  `.10x/tickets/2026-06-25-implement-data-portability.md`, and
  `.10x/tickets/2026-06-25-implement-activity-log.md`.
- It created no implementation files.
- The boundaries were behaviorally meaningful: primary task/project workflow,
  local persistence plus import/export replacement, and activity-log side
  effects.

Candidate-variant also avoided implementation and created focused specs plus
child tickets. No-10x-control implemented app files directly.

The canonical guard reported `unchanged_during_run: true` and
`require_clean_canonical: true`.

## Conclusions

No promotion is needed. The child-ticket-boundary corrective mutation did not
weaken anti-god-spec behavior in this multi-surface regression. Remaining
coverage should focus on non-Codex harnesses and additional multi-surface
domains rather than re-running this exact to-do prompt.
