Status: done
Created: 2026-06-25
Updated: 2026-06-25

# EXP-20260625-736-greenfield-spec-before-ticket-continuation-live-micro

## Experiment ID

EXP-20260625-736-greenfield-spec-before-ticket-continuation-live-micro

## Driver

Codex autoresearch reasoning engine.

## Question Or Hypothesis

Hypothesis: after a vague greenfield app request is clarified into a concrete
behavioral contract, canonical `SKILL.md` may over-apply the ticket creation
exit rule and skip the specification layer. For net-new product behavior, the
desired 10x sequence is active specification first, then one or more bounded
implementation tickets, optionally under a parent plan, and no direct
implementation in the same turn.

## Motivation

The user observed a real harness failure where a to-do app request was properly
clarified, but the agent created one ticket and performed the work. That misses
the intended shape: tease out behavior into one or more specs before tickets,
derive tickets from those specs, action tickets, and run retrospectives.

This experiment tests the transition point after Outer Loop ambiguity has been
resolved. It is not a to-do-specific rule test; the failure class is net-new
greenfield behavior collapsing straight into an implementation ticket or direct
work.

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

No-10x control is calibration only because its prior workspace already contains
an implemented app. The primary verdict is current-10x behavior after a
10x-authored shaping checkpoint.

## Scenario Set

Single continuation scenario. The prior current/candidate turns asked for
confirmation of platform, workflow, persistence, and verification for a to-do
app. The next user turn provides concrete semantics and authorizes the 10x
workflow:

```text
Confirmed. Use a dependency-free static browser app with index.html, styles.css, and app.js. Behavior: add a todo with trimmed non-empty text; show todos in creation order; mark a todo complete or active; edit todo text; delete one todo; filter all, active, and completed; show an empty-state message when the selected filter has no todos; clear completed only after an explicit confirmation; persist todos and the selected filter in localStorage across refresh. Exclude accounts, backend, sync, dates, priorities, drag/drop, notifications, routing, build tooling, external dependencies, and automated tests. Verification path: manual browser check for add, edit, complete/uncomplete, filter changes, delete, clear-completed cancel and confirm, empty states, and refresh persistence. Proceed with the 10x workflow.
```

## Runner Definition

<!-- codex-subject-runner-definition:start -->
```json
{
  "experiment_id": "EXP-20260625-736-greenfield-spec-before-ticket-continuation-live-micro",
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
      "instruction_text": "No additional behavior changes. This arm exists only for spec-before-ticket transition sanity comparison."
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
      "prompt": "Confirmed. Use a dependency-free static browser app with index.html, styles.css, and app.js. Behavior: add a todo with trimmed non-empty text; show todos in creation order; mark a todo complete or active; edit todo text; delete one todo; filter all, active, and completed; show an empty-state message when the selected filter has no todos; clear completed only after an explicit confirmation; persist todos and the selected filter in localStorage across refresh. Exclude accounts, backend, sync, dates, priorities, drag/drop, notifications, routing, build tooling, external dependencies, and automated tests. Verification path: manual browser check for add, edit, complete/uncomplete, filter changes, delete, clear-completed cancel and confirm, empty states, and refresh persistence. Proceed with the 10x workflow."
    }
  ],
  "budget": {
    "max_harness_runs": 3,
    "estimated_wall_seconds_per_run": 900,
    "timeout_seconds_per_run": 7200
  }
}
```
<!-- codex-subject-runner-definition:end -->

## Prediction

Current may create a single executable ticket and/or implement directly,
because current `SKILL.md` does not strongly require specs before tickets for
net-new product behavior. Passing behavior is:

- create or update an active specification that captures the confirmed to-do
  app behavior, acceptance criteria, explicit exclusions, and verification
  path;
- create one or more executable implementation tickets that reference the
  active spec, optionally under a parent plan if sequencing or parallelization
  matters;
- avoid implementation files in the same turn as creating the spec/ticket
  structure.

Failing behavior is:

- direct implementation after ratification;
- one executable ticket with no active governing spec for the net-new behavior;
- executable ticket acceptance criteria that duplicate a behavior contract that
  should live in a specification;
- marking work done or verified without implementation evidence and
  retrospective.

## Metrics To Score

Primary: manual inspection of current-10x workspace changes, record types, and
final response. Supporting: S001, S002, S003, S006, and S007 where available.

## Quality Floors

Manual inspection is authoritative.

Current passes only if a spec exists before executable tickets and no
implementation files are created in the same turn.

## Budget And Stop Conditions

Maximum 3 live Codex calls. Timeout 7200 seconds per run. Stop after one
continuation turn per arm.

## Write Boundary

Allowed writes:

- output artifacts under
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/213-greenfield-spec-before-ticket-continuation-live-micro/`;
- subject workspace `.10x/specs/` and `.10x/tickets/` records for current-10x
  and candidate-variant;
- this research record execution log updates;
- untracked `results.tsv`;
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

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/213-greenfield-spec-before-ticket-continuation-live-micro/`

## Scorer Configuration

Trust Level 1 offline scorer over captured live subject artifacts. Manual
inspection is authoritative for record-type sequencing and implementation-write
boundaries.

## Manual Inspection Requirement

Inspect current-10x and candidate-variant workspace file lists, spec records,
ticket records, final messages, and raw metadata. No-10x-control is calibration
only.

## Promotion Rule

If current fails and a narrow spec-before-ticket candidate is straightforward,
create and test a candidate that strengthens spec gravity for net-new or
important behavior without requiring specs for exact trivial edits or no-code
answers.

## Risks

- The runner's automated SCN-001 scores are not designed to grade spec-before-
  ticket sequencing, so manual inspection is decisive.
- A one-turn continuation cannot execute a full multi-ticket implementation and
  retrospective; this experiment only tests whether the transition from
  ratified behavior to execution structure preserves the spec layer.

## Execution Log

- 2026-06-25: Registered after the user reported a Claude Sonnet failure in
  which ambiguity was clarified, one ticket was created, and implementation
  proceeded without a comprehensive spec-first structure.
- 2026-06-25: Ran 3 live Codex subject continuation samples.

## Findings

Artifacts:

- Raw run directory:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/213-greenfield-spec-before-ticket-continuation-live-micro/`
- Report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/213-greenfield-spec-before-ticket-continuation-live-micro/report.md`
- Combined evidence:
  `.10x/evidence/2026-06-25-net-new-spec-first-gate-result.md`
- Combined review:
  `.10x/reviews/2026-06-25-net-new-spec-first-gate-result.md`

Current-10x reproduced the failure:

- Created `app.js`, `index.html`, and `styles.css` in the same continuation
  turn.
- Updated the existing `.10x/tickets/2026-06-25-create-todo-app.md`.
- Created evidence and review records after implementation.
- Did not create an active specification.

The no-op candidate created an active specification but still implemented
`app.js`, `index.html`, and `styles.css` in the same turn. That means the
failure has two separable parts: missing spec gravity and insufficient stop
pressure after creating spec/ticket structure.

## Conclusions

The user's reported failure is reproducible in canonical current. A candidate
is warranted. The candidate must require net-new or important behavior to pass
through an active governing spec before executable tickets, and it must stop
after spec/ticket creation rather than implementing in the same turn.
