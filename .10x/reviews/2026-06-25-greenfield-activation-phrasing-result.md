Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/research/2026-06-25-greenfield-activation-phrasing-live-micro.md
Verdict: pass

# Review: Greenfield Activation Phrasing

## Target

Greenfield activation phrasing evidence for canonical `SKILL.md`:

- `SKILL.md`
- `.10x/research/2026-06-25-greenfield-activation-phrasing-live-micro.md`
- `.10x/evidence/2026-06-25-greenfield-activation-phrasing-result.md`
- `.10x/evidence/.storage/2026-06-23-skill-autoresearch/201-greenfield-activation-phrasing-live-micro/`

## Findings

- Significant: current-10x passed all six varied small-greenfield phrasings.
  It created exactly one blocked shaping ticket per run and no implementation
  files.
- Significant: no-10x-control failed all six S001 floor checks and built files
  immediately, confirming the batch discriminates the 10x activation behavior
  rather than merely testing harmless prompts.
- Significant: current-10x tickets preserved the Outer Loop boundary. They
  named unresolved platform/runtime, workflow or command surface, persistence,
  data shape, and verification blockers without making executable tickets.
- Minor: S007 was uneven. Some current responses leaned on a provisional
  default plus confirm-or-correct instead of listing every blocker as a compact
  question. This is acceptable because the tickets preserved the blockers and
  no implementation occurred, but future human-voice work can tune the
  question shape.

## Verdict

Pass. The canonical scaled-down activation rule generalizes across these Codex
greenfield phrasings and does not rely on the original bookmark-tracker
language.

## Residual Risk

Test non-Codex harnesses, multi-turn ratification after shaping, and stronger
implementation-pressure phrasings. Keep exact trivial-edit and one-line
mechanical-edit controls active so the activation rule does not become
bureaucratic.
