Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Relates-To: .10x/research/2026-06-26-lower-cue-greenfield-multi-surface-splitting-live-micro.md, .10x/research/2026-06-26-lower-cue-multi-surface-splitting-candidate-live-micro.md, .10x/reviews/2026-06-26-promote-lower-cue-multi-surface-spec-splitting.md, autoresearch/candidates/2026-06-26-lower-cue-multi-surface-spec-splitting.md

# Lower-Cue Multi-Surface Spec Splitting Result

## What was observed

Two linked live Codex MICRO experiments tested lower-cue multi-surface
greenfield spec splitting:

1. `EXP-20260626-743-lower-cue-greenfield-multi-surface-splitting-live-micro`
   tested canonical current and a no-op candidate.
2. `EXP-20260626-744-lower-cue-multi-surface-splitting-candidate-live-micro`
   tested `candidate-lower-cue-multi-surface-spec-splitting-v1` with two
   repetitions.

Raw artifact directories:

- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/221-lower-cue-greenfield-multi-surface-splitting-live-micro/`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/222-lower-cue-multi-surface-splitting-candidate-live-micro/`

EXP-743 current-10x failed by creating one app-level spec,
`.10x/specs/static-todo-app.md`, and one broad child ticket,
`.10x/tickets/2026-06-26-build-static-todo-app.md`, while avoiding
implementation files.

EXP-743 no-op candidate passed once, but it was not promotable because the
overlay contained no behavioral change.

EXP-744 current-10x failed both repetitions with one app-level active spec and
one broad child ticket. It did not create implementation files.

EXP-744 candidate-variant passed both repetitions with focused active specs,
parent plans, bounded child tickets, and no `index.html`, `styles.css`, or
`app.js` implementation files.

## Procedure

Commands:

```text
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-26-lower-cue-greenfield-multi-surface-splitting-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/221-lower-cue-greenfield-multi-surface-splitting-live-micro --require-clean-canonical
python3 autoresearch/run_once.py --experiment .10x/research/2026-06-26-lower-cue-multi-surface-splitting-candidate-live-micro.md --out .10x/evidence/.storage/2026-06-23-skill-autoresearch/222-lower-cue-multi-surface-splitting-candidate-live-micro --require-clean-canonical
```

Manual inspection read raw outputs, workspace file lists, current app-level
specs, current broad tickets, candidate focused specs, candidate parent plans,
candidate child tickets, final messages, and canonical guard reports.

## What this supports or challenges

This supports promoting
`candidate-lower-cue-multi-surface-spec-splitting-v1` into `SKILL.md`.

It challenges the prior canonical wording because current could obey
spec-first and no-implementation gates while still creating a god spec and a
broad child ticket for lower-cue static app work.

## Limits

This covers Codex CLI only. The prompt is a ratified continuation, not a full
dynamic user simulator. It does not prove Claude, OpenCode, OMP, or app-level
subagent behavior. It does not prove every greenfield app should split; the
promotion preserves a single-cohesive-surface exception.
