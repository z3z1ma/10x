Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Target: SKILL.md lower-cue multi-surface spec splitting promotion
Verdict: pass

# Promote Lower-Cue Multi-Surface Spec Splitting

## Target

`SKILL.md` mutation promoted from
`autoresearch/candidates/2026-06-26-lower-cue-multi-surface-spec-splitting.md`.

## Findings

- Pass: the mutation targets the observed lower-cue failure. Current created
  one product-level spec and one broad child ticket across three current
  samples; the candidate created focused specs and child tickets across both
  candidate repetitions.
- Pass: the mutation preserves the no-implementation boundary. It governs how
  to name specs and tickets; it does not authorize app files during the
  spec/ticket creation turn.
- Pass: the mutation is not a todo-app-specific rule. It names generic
  behavioral-surface categories: interaction workflow, lifecycle/state,
  persistence/import/export/recovery, side-effect history, and platform shell
  when independently reviewable.
- Pass: over-splitting risk is bounded by the explicit single-cohesive-surface
  exception.

## Semantic Behavior Change

Failure mode targeted: lower-cue greenfield work presented as one small/static
app collapses independent behavioral contracts into one god spec and one broad
child ticket.

Invariant that must not weaken: small, cohesive, exact, no-code, already
spec-backed, or blocked work must not be split mechanically.

New behavior expected: before naming specs for ratified greenfield apps/tools/
workflows, the agent identifies behavioral surfaces and splits only independent
capability clusters whose acceptance scenarios are normally implemented,
reviewed, or verified separately.

Behavior it might accidentally permit: excessive spec files for cohesive
single-surface work. The promoted text explicitly keeps one spec when all
acceptance scenarios belong to one cohesive behavioral surface.

Eval cases expected to improve: lower-cue multi-surface greenfield app/tool
continuations, including the todo-app-shaped failure class without encoding any
todo-specific rule.

Regression cases that must not move: existing active spec reuse, no-code/reuse
answers, exact mechanical edits, single cohesive net-new surfaces, blocked
multi-surface requests, assumption provenance, and no-implementation boundary.

## Verdict

Pass. Promote the candidate.

## Residual Risk

Non-Codex harnesses remain unproven. The user specifically observed Claude
Sonnet failing this class, so Claude/OpenCode/OMP harness coverage remains the
next useful axis when those runners are available.
