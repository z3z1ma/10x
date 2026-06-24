Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Target: SKILL.md
Verdict: pass

# Promote Protocol Mutation Review Gate

## Target

Promotion of
`autoresearch/candidates/2026-06-24-protocol-mutation-review-gate.md` into
`SKILL.md` after
`EXP-20260624-871-protocol-relaxation-review-scn015-live-micro`.

## Findings

- **Pass:** The promoted rule targets a real recursive-improvement failure mode:
  an optimizer can improve throughput by weakening the protocol's core
  safeguards.
- **Pass:** The rule is a review gate, not a new process bypass. It requires
  naming the failure mode, protected invariants, desired behavior, accidental
  permissions, expected eval improvements, and regression cases before
  instruction mutation.
- **Pass:** The rule directly rejects broad discretion to skip Outer Loop,
  executable tickets, durable records, evidence, or unresolved semantic
  ambiguity.
- **Pass:** The language still permits narrow simplifications when they are
  named, mechanically checkable, and proven not to admit unratified assumptions.
- **Minor residual risk:** Agents may over-apply the review template to trivial
  wording edits. The benefit outweighs this risk for protocol or always-on
  instruction mutations.

## Verdict

Pass. Promote the candidate into `SKILL.md`.

## Residual Risk

Future SCN-015 variants should test whether the rule blocks only broad
relaxations while still allowing precise, evidence-backed simplifications.
