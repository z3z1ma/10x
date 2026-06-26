Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Relates-To: .10x/research/2026-06-26-post-spec-first-existing-spec-and-no-code-controls-live-micro.md, SKILL.md

# Post-Spec-First Existing-Spec And No-Code Controls

## What was observed

`EXP-20260626-740-post-spec-first-existing-spec-and-no-code-controls-live-micro`
ran 12 live Codex subject samples across existing-active-spec reuse and
no-code/reuse scenarios.

Artifacts:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/217-post-spec-first-existing-spec-and-no-code-controls-live-micro/`
- Report:
  `.10x/evidence/.storage/2026-06-23-skill-autoresearch/217-post-spec-first-existing-spec-and-no-code-controls-live-micro/report.md`

Manual inspection found:

- Existing active spec reuse passed for current `SKILL.md` in both repetitions.
  Current created only an implementation ticket referencing
  `.10x/specs/static-browser-todo-app.md` and did not create a duplicate spec or
  app implementation files.
- No-code/reuse passed for current `SKILL.md` in both repetitions. Current
  inspected the active server-owned export decision, knowledge record, and
  source, made no file changes, and asked for explicit supersession before
  browser-side CSV generation.
- No-10x control implemented directly in the first no-code repetition and both
  existing-spec repetitions, confirming the scenarios retain contrast.
- The no-op candidate was stochastic in the existing-spec scenario: one
  repetition stopped at ticket creation and one continued into implementation.
  Current did not show that failure.

The command ended with `canonical files changed during run: SKILL.md` because
`SKILL.md` was intentionally promoted for a separate experiment while this long
batch was still running. The runner had already built the plan and instruction
digests for this batch before that edit; the guard failure is orchestration
noise, not a subject-agent behavioral failure.

## Procedure

Ran:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-26-post-spec-first-existing-spec-and-no-code-controls-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/217-post-spec-first-existing-spec-and-no-code-controls-live-micro --require-clean-canonical
```

Then inspected raw artifacts, final messages, changed file lists, and reports.

## What this supports or challenges

Supports:

- The net-new spec-first promotion did not regress reuse of an already-active
  specification.
- The net-new spec-first promotion did not regress no-code/reuse behavior where
  active records and source establish that implementation is the wrong next
  action.

Challenges:

- The no-op candidate's stochastic direct implementation suggests the existing
  live harness can still vary on ticket handoff boundaries even when the
  instruction text is intended to be equivalent.

## Limits

The canonical guard failed because `SKILL.md` changed during the long run. The
raw samples remain useful because the run plan had already captured the old
instruction digests, but this batch should not be cited as a clean canonical
guard pass.
