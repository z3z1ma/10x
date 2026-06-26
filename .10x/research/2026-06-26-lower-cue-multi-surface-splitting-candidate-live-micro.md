Status: done
Created: 2026-06-26
Updated: 2026-06-26

# EXP-20260626-744-lower-cue-multi-surface-splitting-candidate-live-micro

## Experiment ID

EXP-20260626-744-lower-cue-multi-surface-splitting-candidate-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis:
`candidate-lower-cue-multi-surface-spec-splitting-v1` will make focused
specification splitting reliable for a lower-cue ratified greenfield app whose
behavior spans independent workflow, lifecycle, data portability/persistence,
and activity-log surfaces.

## Motivation

`EXP-20260626-743-lower-cue-greenfield-multi-surface-splitting-live-micro`
showed canonical current-10x failing the lower-cue version of the god-spec
problem. Current created one active `.10x/specs/static-todo-app.md` and one
broad child ticket. A no-op candidate arm split correctly, but that is
stochastic evidence only and not promotable.

This experiment tests a real candidate overlay against the same continuation.

## Method Tier

MICRO using live Codex subject continuations from
`EXP-20260625-735-generic-named-app-activation-live-micro`.

## Variants

- no-10x-control: minimal Codex instruction continued from the prior no-10x
  to-do raw artifact for calibration only.
- current-10x: canonical `SKILL.md`, continued from the prior current-10x
  to-do shaping checkpoint.
- candidate-variant: canonical `SKILL.md` plus
  `autoresearch/candidates/2026-06-26-lower-cue-multi-surface-spec-splitting.md`,
  continued from the prior candidate to-do shaping checkpoint.

## Control

No-10x-control is calibration only. Current already failed once in EXP-743; if
current passes in this batch, interpret it as stochastic instability, not proof
that the gap is absent.

## Scenario Set

Single continuation scenario, repeated twice to reduce one-run noise. Prompt:

```text
Confirmed. Make it a dependency-free static browser app with index.html, styles.css, and app.js. It is for one person managing tasks across projects. It should let me add, edit, and delete tasks; mark tasks active or completed; assign each task to one project; filter by project and completion state; archive and unarchive projects while preserving their tasks; hide archived projects from normal project pickers; export all data to a JSON file; import a JSON file only after explicit confirmation that it will replace current local data; and show an activity log for task created, task edited, task completed, task deleted, project archived, project unarchived, import, and export. Persist tasks, projects, filters, and the activity log in localStorage across refresh. Exclude accounts, backend, sync, dates, priorities, drag/drop, notifications, routing, build tooling, external dependencies, and automated tests. Verification path: manual browser check for task CRUD, filtering, project archive visibility, import replace confirmation, export round trip, activity log entries, and refresh persistence. Proceed with the 10x workflow.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260626-744-lower-cue-multi-surface-splitting-candidate-live-micro",
  "status": "active",
  "method_tier": "MICRO",
  "driver": "Codex autoresearch reasoning engine",
  "model": "codex-cli-default",
  "harness": "codex-cli",
  "repetitions": 2,
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
      "instruction_source": "SKILL.md plus candidate-lower-cue-multi-surface-spec-splitting-v1",
      "base_instruction_path": "SKILL.md",
      "instruction_path": "autoresearch/candidates/2026-06-26-lower-cue-multi-surface-spec-splitting.md"
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
    "max_harness_runs": 6,
    "estimated_wall_seconds_per_run": 1200,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Candidate should consistently create multiple focused active specs, a parent
plan, and bounded child tickets, then stop without app implementation files.

Current may either repeat the EXP-743 god-spec failure or pass stochastically.

## Metrics To Score

Primary: manual inspection of current and candidate workspace changes, spec
boundaries, parent/child ticket structure, final messages, and implementation
write boundaries.

## Quality Floors

Manual inspection is authoritative.

Candidate passes only if every candidate repetition:

- preserves 10x activation and avoids implementation files;
- creates more than one focused active specification for independent surfaces;
- creates a parent plan and bounded child tickets after focused specs;
- avoids a single app-level god spec or a single broad executable ticket;
- records no unresolved blockers for the ratified stack and behavior.

Candidate fails if it implements, over-splits arbitrarily, creates one app-level
spec, creates only one broad child ticket, or stops at a parent-only plan
without a real blocker.

## Budget And Stop Conditions

Maximum 6 live Codex calls. Timeout 7200 seconds per run. Stop after one
continuation turn per arm and repetition.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/222-lower-cue-multi-surface-splitting-candidate-live-micro/`;
- subject workspace `.10x/specs/` and `.10x/tickets/` records for current-10x
  and candidate-variant;
- this research record execution log updates;
- evidence/review records after inspection;
- a narrow `SKILL.md` mutation only after current-failure/candidate-pass
  evidence plus semantic review.

Disallowed writes:

- canonical `SKILL.md` before current-failure/candidate-pass evidence exists;
- `autoresearch/program.md`;
- subject workspace implementation files for current-10x or candidate-variant
  in this turn.

## Raw Output Destination

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/222-lower-cue-multi-surface-splitting-candidate-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection is authoritative.

## Manual Inspection Requirement

Inspect all candidate workspaces and current workspaces. Compare file outputs,
created specs, created tickets, final messages, and raw metadata.

## Promotion Rule

Promote only if candidate passes and the semantic review shows no weakening of
existing-spec reuse, no-code/reuse, exact-edit, single-surface, blocked-
ambiguity, no-implementation, or assumption-provenance invariants.

## Risks

- Candidate behavior may pass because of stochasticity rather than overlay
  strength. Two repetitions reduce but do not eliminate that risk.
- The primary prompt is lower-cue but still explicitly ratified. First-turn
  dynamic user simulation remains separate.

## Execution Log

- 2026-06-26: Registered after EXP-743 found a lower-cue current failure and a
  non-promotable no-op candidate pass.
- 2026-06-26: Ran 6 live Codex subject samples. Output is stored under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/222-lower-cue-multi-surface-splitting-candidate-live-micro/`.

## Findings

No-10x-control implemented directly in both repetitions, writing `index.html`,
`styles.css`, and `app.js`.

Current-10x failed both repetitions while preserving the no-implementation
boundary:

- Rep 0 created one app-level spec,
  `.10x/specs/static-project-todo-app.md`, and one broad child ticket,
  `.10x/tickets/2026-06-25-implement-static-project-todo-app.md`.
- Rep 1 created one app-level spec, `.10x/specs/static-todo-app.md`, and one
  broad child ticket, `.10x/tickets/2026-06-25-implement-static-todo-app.md`.

Candidate-variant passed both repetitions:

- Rep 0 created focused specs for task workflow, project archive lifecycle,
  persistence/import/export, and activity log; created a parent plan and child
  tickets; and wrote no implementation files.
- Rep 1 created focused specs for static browser shell, task/project workflow,
  project archive lifecycle, data import/export, localStorage persistence, and
  activity log; created a parent plan and child tickets; and wrote no
  implementation files.

Manual inspection judged the candidate split behaviorally meaningful rather
than arbitrary. The candidate separated primary workflow, lifecycle, destructive
data replacement/persistence, and side-effect history. The shell split in rep 1
is acceptable because the platform/file-set constraint can be built and reviewed
independently from the domain workflow.

## Conclusions

Promote `candidate-lower-cue-multi-surface-spec-splitting-v1`.

The promotion should make `SKILL.md` explicitly require behavioral-surface
identification before naming specs for ratified greenfield apps/tools/workflows.
It should also preserve the single-cohesive-surface exception so small features
are not split mechanically.
