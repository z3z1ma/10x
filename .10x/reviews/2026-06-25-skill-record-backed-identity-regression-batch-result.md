Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: autoresearch/candidates/2026-06-25-skill-record-backed-identity.md
Verdict: pass

# Skill Record-Backed Identity Regression Batch Review

## Target

Manual review of the remaining promotion gates for `candidate-skill-record-backed-identity-v1`: no-native source path, `.agents`, `.opencode`, and `.claude` mirror identity regressions.

## Findings

Pass: candidate preserved exact source skill identity in every corrected gate. The no-native gate produced `.10x/skills/ledger-import-fixture-replay/SKILL.md` in both candidate repetitions; the three mirror gates produced the same `.10x` source path plus exact native mirror paths.

Pass: candidate mirror content was byte-equivalent to the `.10x` source in `.agents`, `.opencode`, and `.claude`.

Pass: candidate generated no speculative native mirrors, no implementation edits, and no forbidden non-knowledge `.10x` record references inside generated skills.

Positive control: no-10x-control failed the no-native source-path gate by creating flat `.10x/skills/ledger-import-fixture-replay.md` files in both repetitions.

Minor harness issue: the first mirror registrations used four-digit experiment IDs and failed scorer validation. The corrected three-digit runs succeeded and are the authoritative evidence.

Residual concern: the candidate does not solve the terminal-ticket path lifecycle wrinkle seen in EXP-998. That concern belongs to a separate closure-maintenance hypothesis, not this identity candidate.

## Verdict

Pass. The remaining regression batch clears the promotion gate for a narrow canonical skill identity rule.

## Residual Risk

The promoted wording should avoid preserving stale or superseded skill names. The canonical edit should therefore refer to the current workstream or non-superseded records rather than any historical mention.
