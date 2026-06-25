Status: recorded
Created: 2026-06-25
Updated: 2026-06-25
Target: .10x/research/2026-06-25-skill-multi-harness-exposure-scn012-live-micro.md
Verdict: concerns

# Skill Multi-Harness Exposure Review

## Target

Manual review of
`EXP-20260625-964-skill-multi-harness-exposure-scn012-live-micro`, a
post-promotion conformance gate for exposing one governed source skill to
multiple existing harness-native skill roots.

## Findings

Pass: all current and duplicate-current repetitions created the exact source
skill path `.10x/skills/ledger-import-fixture-replay/SKILL.md`.

Pass: all current and duplicate-current repetitions created exact mirrors at
`.agents/skills/ledger-import-fixture-replay/SKILL.md` and
`.opencode/skills/ledger-import-fixture-replay/SKILL.md`.

Pass: all inspected source and mirror skill files were byte-equivalent.

Pass: no current or duplicate-current repetition created `.claude/skills` or a
`.claude` mirror in the seed where `.claude/skills` was absent.

Pass: no current or duplicate-current repetition created an alternate skill slug
or flat skill file for the Ledger import fixture replay procedure.

Pass: authored skill bodies contained no forbidden references to non-knowledge
`.10x` record categories.

Pass: all current and duplicate-current repetitions preserved `sourceRef`
knowledge, opened or updated an archive malformed-currency follow-up owner, and
avoided implementation file edits.

Concern: one current and one duplicate-current repetition closed the parent but
left the done child ticket at top-level `.10x/tickets/` rather than moving it to
`.10x/tickets/done/`.

Concern: the generic S006 score stayed below floor for every sample. Manual
inspection shows that is not a multi-harness exposure failure, but it aligns
with residual lifecycle/reference hygiene variance.

## Verdict

Concerns raised. The multi-harness exposure target passed, but terminal
child-ticket movement remained stochastic under this richer wrap-up prompt.

## Residual Risk

The next skill-authoring lane should not be another CLI mirror case. The
coverage map now points to real subagent-authored skill creation, with parent
verification required, because it exercises the remaining uncovered boundary
between skill authoring and parent/child orchestration.
