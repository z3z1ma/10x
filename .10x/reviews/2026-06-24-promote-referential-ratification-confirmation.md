Status: recorded
Created: 2026-06-24
Updated: 2026-06-24
Target: SKILL.md
Verdict: pass

# Promote Referential Ratification Confirmation

## Target

`SKILL.md` Assumption Provenance referential-ratification paragraph, based on
`candidate-referential-ratification-confirmation-v1`.

## Findings

- Significant: The candidate should be promoted narrowly. The validated EXP-859
  rerun showed current-10x had the right safety posture but omitted missing
  notification behavior and operational ownership from the actual
  confirm/correct question. The proposed change targets that gap by requiring
  all execution-critical recovered and missing semantics to be user-legible at
  the checkpoint.
- Minor: The added language increases prompt length in a dense section. The
  wording remains local to high-impact referential semantics and does not create
  a broad new process requirement.

## Verdict

Pass. Promote the narrow checkpoint clarification.

## Residual Risk

The agent may over-ask for all listed semantic categories even when a category
cannot affect the decision or acceptance criteria. The phrase
`execution-critical` limits the expected scope.
