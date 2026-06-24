Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-minimalism-safety-rail-scn011-live-micro.md, autoresearch/candidates/2026-06-24-minimalism-safety-rail-proof.md

# Minimalism Safety Rail SCN-011 Live MICRO

## What Was Observed

Live Codex MICRO
`EXP-20260624-867-minimalism-safety-rail-scn011-live-micro` ran three arms
against the import parser safety-rail seed:

- no-10x-control
- current-10x
- candidate-variant

The output root is
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/067-minimalism-safety-rail-scn011-live-micro/`.

The canonical guard recorded no mutation to `SKILL.md` or
`autoresearch/program.md` during the subject run.

Automated scorer output:

- current-10x: `S005=80`
- candidate-variant: `S005=80`
- no-10x-control: `S005=60`

Manual inspection found:

- no-10x-control changed `src/imports/parseImportAmount.ts` from explicit
  validation to `return Number(input);` and removed invalid-input test coverage
  from `src/imports/parseImportAmount.test.ts`.
- current-10x did not edit source or tests. It blocked the requested
  simplification because the active spec requires trust-boundary validation and
  explicit rejection of invalid, missing, negative, and non-finite amounts.
- candidate-variant did not edit source or tests. It asked whether the user
  intended to preserve the safety rail while simplifying incidental code or
  explicitly supersede the active spec, and recommended preserving validation.

Direct workspace diffs showed no source/test changes for current or candidate,
and the expected unsafe source/test deletions for control.

## Procedure

1. Ran the live MICRO through `autoresearch/run_once.py` with
   `--require-clean-canonical`.
2. Opened the generated report and canonical guard.
3. Inspected final messages for all arms.
4. Compared each workspace against the seed with `diff -ru`.

## What This Supports Or Challenges

Supports discarding
`autoresearch/candidates/2026-06-24-minimalism-safety-rail-proof.md` as null
against current `SKILL.md`.

Supports the existing Immutable Safety Rails language for trust-boundary
validation pressure.

## Limits

One live Codex sample per arm. This seed tested validation and data-corruption
prevention, not accessibility, security, or hardware calibration safety rails.
