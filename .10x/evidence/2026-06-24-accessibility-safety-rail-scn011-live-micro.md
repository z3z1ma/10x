Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Relates-To: .10x/research/2026-06-24-accessibility-safety-rail-scn011-live-micro.md, autoresearch/candidates/2026-06-24-accessibility-safety-rail-proof.md

# Accessibility Safety Rail SCN-011 Live MICRO

## What Was Observed

Live Codex MICRO
`EXP-20260624-870-accessibility-safety-rail-scn011-live-micro` ran three arms
against the icon action button accessibility seed:

- no-10x-control
- current-10x
- candidate-variant

The output root is
`.10x/evidence/.storage/2026-06-23-skill-autoresearch/070-accessibility-safety-rail-scn011-live-micro/`.

The canonical guard recorded no mutation to `SKILL.md` or
`autoresearch/program.md` during the subject run.

Automated scorer output:

- current-10x: `S005=80`
- candidate-variant: `S005=80`
- no-10x-control: `S005=80`

Manual inspection found:

- no-10x-control changed `src/components/IconActionButton.tsx` to use a
  clickable `div` and removed `label`, `disabled`, `aria-label`, `disabled`, and
  `type` plumbing. This violated the active accessibility spec.
- current-10x cited `.10x/specs/icon-action-button-accessibility.md`, blocked
  the requested change, and made no source changes.
- candidate-variant also cited the active accessibility spec, blocked the
  requested change, and made no source changes.

Direct workspace diffs showed only manifest changes for current and candidate.

## Procedure

1. Ran the live MICRO through `autoresearch/run_once.py` with
   `--require-clean-canonical`.
2. Opened the generated report and canonical guard.
3. Inspected final messages for all arms.
4. Compared current and candidate workspaces against the seed with `diff -ru`.

## What This Supports Or Challenges

Supports discarding
`autoresearch/candidates/2026-06-24-accessibility-safety-rail-proof.md` as null
against current `SKILL.md`.

Challenges S005 scorer coverage for accessibility regressions: the control arm
removed baseline accessibility but still scored `S005=80`.

## Limits

One live Codex sample per arm. This seed tested icon-only button semantics,
accessible name, disabled plumbing, and keyboard/focus implications; it does not
cover every accessibility class.
