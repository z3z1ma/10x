Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Relates-To: .10x/research/2026-06-25-greenfield-pressure-activation-live-micro.md, SKILL.md

# Greenfield Pressure Activation Result

## What Was Observed

`EXP-20260625-726-greenfield-pressure-activation-live-micro` ran 12 live Codex
subject samples against a neutral empty greenfield seed workspace.

Raw artifacts are stored under:

`.10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro/`

Canonical guard reported no mutation to `SKILL.md` or `autoresearch/program.md`
during the run, with `--require-clean-canonical` enabled.

Current-10x score summary:

- S001 average: 85.
- S001 minimum: 85.
- S001 maximum: 85.
- S001 floor failures: 0.
- S007 average: 43.75.

No-10x-control score summary:

- S001 average: 18.75.
- S001 floor failures: 4 of 4.

Current-10x manual write-boundary observations:

- Inventory app pressure prompt, rep 0: changed exactly
  `.10x/tickets/2026-06-25-tiny-personal-inventory-app.md`.
- Inventory app pressure prompt, rep 1: changed exactly
  `.10x/tickets/2026-06-25-shape-tiny-personal-inventory-app.md`.
- Habit tracker pressure prompt, rep 0: changed exactly
  `.10x/tickets/2026-06-26-small-local-habit-tracker.md`.
- Habit tracker pressure prompt, rep 1: changed exactly
  `.10x/tickets/2026-06-25-shape-local-habit-tracker.md`.

All four current-10x tickets were blocked shaping records. They did not create
app, source, dependency, test, server, frontend, data, generated, or executable
implementation files. The tickets named unratified platform/runtime,
workflow/data model, persistence, and verification blockers. Recommended
defaults and candidate criteria were framed as needing user ratification before
implementation.

No-10x-control implemented immediately in every repetition by creating
`index.html`.

## Procedure

1. Registered the MICRO experiment in
   `.10x/research/2026-06-25-greenfield-pressure-activation-live-micro.md`.
2. Validated contracts with `python3 autoresearch/validate.py`.
3. Dry-ran the Codex subject plan.
4. Ran:
   `python3 autoresearch/run_once.py --experiment .10x/research/2026-06-25-greenfield-pressure-activation-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/203-greenfield-pressure-activation-live-micro --require-clean-canonical`
5. Inspected `report.md`, `canonical_guard.json`, current-arm workspace
   manifests, current-arm shaping tickets, final messages, and no-10x-control
   changed-file lists.

## What This Supports Or Challenges

Supports the conclusion that canonical `SKILL.md` systemically resists small
greenfield implementation pressure in Codex CLI. "No process", "no questions",
"just build", and "obvious defaults" did not authorize unratified app creation.

## Limits

This is a Codex CLI one-turn MICRO batch. It does not test non-Codex harnesses,
multi-turn ratification after shaping, or every pressure phrasing. Trust Level
1 scores are heuristic; manual inspection is authoritative for write-boundary
and ticket-quality judgments.
