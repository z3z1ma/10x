# Candidate: Lower-Cue Multi-Surface Spec Splitting

Candidate ID: `candidate-lower-cue-multi-surface-spec-splitting-v1`
Created: 2026-06-26
Canonical target: `SKILL.md`
Status: promoted
Promotion: manual-only

## Target Behavior

Stabilize focused specification splitting when a lower-cue greenfield app or
tool request is ratified but presented as one small/static/simple product. The
agent should not collapse independent behavioral surfaces into one app-level
god spec merely because implementation could fit in one file set.

## Motivation

`EXP-20260626-743-lower-cue-greenfield-multi-surface-splitting-live-micro`
showed canonical current-10x preserving 10x activation and the no-implementation
boundary, but creating one `static-todo-app` specification and one broad child
ticket for task workflow, project archive lifecycle, import/export replacement,
localStorage persistence, and activity-log behavior.

The no-op candidate happened to split correctly, which means the current
instruction set can reach the right behavior but does not make it reliable
enough under lower-cue prompts.

## Proposed Instruction Overlay

Add near the spec-first gate and focused-specification boundary:

```text
Before naming specifications for a ratified greenfield app, tool, UI, CLI, or
workflow, identify the behavioral surfaces inside the request. A single product
name, static implementation, small scope, local-only deployment, one file set,
or one user does not prove the behavior is one specification.

Split focused specifications when the ratified behavior contains independent
capability clusters whose acceptance scenarios would normally be implemented,
reviewed, or verified separately, including:

- primary user interaction workflow;
- lifecycle/state transitions;
- persistence, import/export, destructive replacement, or recovery behavior;
- audit, activity log, notification, or other side-effect history;
- platform shell or integration constraints when those constraints can be built
  or reviewed independently from the domain workflow.

Use one specification only when all acceptance scenarios belong to one cohesive
behavioral surface and would normally be implemented and reviewed together. If
separate behavior clusters exist, let a parent ticket coordinate the product
feature and derive child tickets from the focused specification set.
```

## Expected Score Movement

- Lower-cue multi-surface greenfield continuations should move from one god
  spec/one broad child ticket to focused specs plus parent/child tickets.
- S001 and S003 should hold because implementation remains forbidden in the
  spec/ticket creation turn.
- S005 should hold because trivial exact edits and no-code/reuse cases are not
  greenfield app/tool/workflow specification shaping.

## Scenario Coverage

Primary:

- Lower-cue continuation from `Create a to-do app` where the user ratifies a
  dependency-free static app with task/project workflow, project archive
  lifecycle, data import/export replacement, persistence, and activity log.

Regressions to preserve before promotion:

- Existing active spec reuse: do not create duplicate specs.
- No-code/reuse answer: do not create specs when the correct answer is no code.
- Exact mechanical edits: do not force records.
- Single cohesive net-new surface: do not split artificially.
- Blocked multi-surface request: do not create child tickets when real
  execution-critical blockers remain.

## Expected Failure Modes

- Candidate still creates one product-level spec because the implementation is
  static and local.
- Candidate over-splits tiny cohesive behavior into arbitrary records.
- Candidate creates specs but no child tickets despite ratified behavior.
- Candidate implements files in the same turn as spec/ticket creation.

## Promotion Boundary

Promote only if candidate passes the lower-cue multi-surface primary while
preserving the no-implementation boundary and without creating broad discretion
to split everything. A single successful no-op/stochastic arm is not promotion
authority.

## Result

Promoted after:

- `EXP-20260626-743-lower-cue-greenfield-multi-surface-splitting-live-micro`
- `EXP-20260626-744-lower-cue-multi-surface-splitting-candidate-live-micro`

Current canonical failed three lower-cue samples across EXP-743 and EXP-744 by
creating one app-level active specification and one broad child ticket while
avoiding implementation files. The no-op EXP-743 candidate passed once but was
not promotable. The real candidate passed both EXP-744 repetitions with focused
specification sets, parent plans, bounded child tickets, and no implementation
files.
