Status: recorded
Created: 2026-06-26
Updated: 2026-06-26
Target: SKILL.md source-backed split-spec child-ticket promotion
Verdict: pass

# Promote Source-Backed Child-Ticket Gate

## Target

The `SKILL.md` mutation promoted from
`.10x/research/2026-06-26-source-backed-split-spec-child-ticket-live-micro.md`.

## Findings

- Pass: the mutation targets the observed failure mode directly. Current-10x
  created one suite-wide spec and one broad executable ticket; the promoted
  text requires focused specs, a parent plan, and child tickets when records and
  source settle the substrate.
- Pass: the mutation preserves the Outer Loop/Inner Loop boundary. It says to
  create records in the same Outer Loop turn, but still forbids implementation
  in the spec/ticket creation turn.
- Pass: the mutation reinforces anti-god-spec behavior without requiring
  artificial splitting for cohesive single-surface work. It keeps one ticket
  allowed when the behavior is one coherent slice.
- Pass: the mutation does not relax assumption provenance, semantic
  ratification, evidence, closure, no-code/reuse, or minimalism invariants.

## Semantic Behavior Change

Failure mode targeted: a ratified multi-surface net-new feature with a settled
implementation substrate collapses into one suite-level spec and one broad
ticket.

Invariant that must not weaken: non-trivial net-new behavior still must not be
implemented in the same turn as governing specs and first tickets are created.

New behavior expected: after focused specs exist, the agent creates a parent
plan and child tickets immediately when the substrate and acceptance criteria
are settled.

Behavior it might accidentally permit: over-splitting cohesive small features
into unnecessary specs and tickets. The text limits this by preserving the
cohesive-single-surface exception and by tying child tickets to multiple
independent surfaces.

Eval cases expected to improve: source-backed multi-surface app/tool requests,
including the todo-app class of failure where the agent jumps from clarification
to one ticket instead of specs, parent, and children.

Regression cases that must not move: existing-spec reuse, no-code/reuse
answers, exact mechanical edits, single cohesive net-new surfaces, and blocked
multi-surface requests where a real execution-critical blocker remains.

## Verdict

Pass. Promote the rule and keep a lower-cue source-backed variant in the future
backlog.

## Residual Risk

This promotion is supported by one Codex repetition per arm. Lower-cue prompts
and non-Codex harnesses, especially Claude Sonnet, still need coverage because
the user observed a related todo-app failure there.
