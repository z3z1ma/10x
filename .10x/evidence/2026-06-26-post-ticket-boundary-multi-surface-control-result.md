Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Relates-To: .10x/research/2026-06-26-post-ticket-boundary-multi-surface-splitting-control-live-micro.md, .10x/reviews/2026-06-26-post-ticket-boundary-multi-surface-control.md, .10x/research/2026-06-24-10x-conformance-coverage-map.md

# Post Ticket Boundary Multi-Surface Control Result

## What Was Observed

`EXP-20260626-747-post-ticket-boundary-multi-surface-splitting-control-live-micro`
ran three live Codex subject samples after promoting the child-ticket-boundary
corrective mutation. Artifacts are under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/225-post-ticket-boundary-multi-surface-splitting-control-live-micro/`

Manual inspection found:

- `no-10x-control` implemented `index.html`, `styles.css`, and `app.js`
  directly.
- `current-10x` created no app files.
- `current-10x` created focused specs for task/project workflow, local data
  portability, and activity log:
  `.10x/specs/todo-task-project-workflow.md`,
  `.10x/specs/todo-local-data-portability.md`, and
  `.10x/specs/todo-activity-log.md`.
- `current-10x` updated one parent plan:
  `.10x/tickets/2026-06-25-create-todo-app.md`.
- `current-10x` created bounded child tickets for workflow, data portability,
  and activity log:
  `.10x/tickets/2026-06-25-implement-task-project-workflow.md`,
  `.10x/tickets/2026-06-25-implement-data-portability.md`, and
  `.10x/tickets/2026-06-25-implement-activity-log.md`.
- The current-arm child tickets had real dependencies rather than activity-
  phase churn: data portability depends on the workflow state shape; activity
  log depends on workflow event sources and data portability persistence.
- `candidate-variant` also avoided implementation and created focused specs
  plus child tickets.
- The canonical guard reported `unchanged_during_run: true` and
  `require_clean_canonical: true`.

The Trust Level 1 offline report scored current and candidate S001 Outer Loop
Discipline at 85, with no-10x-control capped at 15 for unauthorized
implementation.

## Procedure

1. Registered the post-corrective multi-surface control.
2. Validated the experiment with `python3 autoresearch/validate.py`.
3. Dry-ran the live subject plan.
4. Ran `python3 autoresearch/run_once.py` with `--require-clean-canonical`.
5. Inspected report, canonical guard, raw final messages, archived workspace
   file lists, current-arm specs, parent plan, and child tickets.

## What This Supports Or Challenges

This supports the conclusion that the child-ticket-boundary corrective
mutation did not weaken focused specification splitting for genuinely
multi-surface work.

## Limits

This is one Codex live repetition of one lower-cue static app scenario. It does
not prove non-Codex harness behavior, broader app domains, or every possible
multi-surface decomposition pressure.
