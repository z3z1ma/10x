Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: SKILL.md
Verdict: pass

# Skill Record-Backed Identity Promotion Review

## Target

Promotion of `candidate-skill-record-backed-identity-v1` into canonical `SKILL.md`.

## Findings

Pass: EXP-997 showed the candidate fixed the target identity failure. Candidate created `.10x/skills/ledger-import-fixture-replay/SKILL.md` in all three repetitions while current drifted to `.10x/skills/ledger-fixture-replay/SKILL.md` in one repetition.

Pass: EXP-998 cleared weak-request slug stability as a non-regression. Candidate and current both produced the exact source skill identity in all three repetitions.

Pass: EXP-999 cleared no-native source-path identity. Candidate created the exact directory-shaped source skill in both repetitions, while no-10x-control created flat source skill files.

Pass: EXP-967, EXP-968, and EXP-969 cleared `.agents`, `.opencode`, and `.claude` mirror identity. Candidate created exact source and native mirror paths, with byte-equivalent content.

Pass: the canonical edit is narrow. It adds one paragraph after the source-path sentence and only governs skill identity when the current workstream or non-superseded records already name the identity.

Concern accepted: stale or superseded skill-name conflicts remain under-tested. The promoted wording narrows the rule to non-superseded records, but a future MICRO should explicitly test stale skill identity conflict if this area keeps mattering.

Concern accepted: ticket lifecycle path maintenance remains separate. Do not claim this promotion solves terminal-status movement.

## Verdict

Pass. Promote the narrow record-backed skill identity rule to canonical `SKILL.md`.

## Residual Risk

The next related hypothesis should target done-status path maintenance or stale/superseded skill identity conflicts, not another generic skill identity restatement.
