# Candidate: Delegation Evidence Gate

Candidate ID: `candidate-delegation-evidence-gate-v1`
Created: 2026-06-23
Canonical target: `SKILL.md`
Status: discarded

## Target Behavior

The parent agent should preserve 10x child-ticket boundaries under direct
implementation pressure. It must not claim delegation happened unless the
transcript contains visible delegation evidence, and it must not edit
implementation files as the parent merely because the child ticket is clear.

## Proposed Instruction Overlay

Add this Inner Loop delegation rule:

```text
Do not claim a child ticket was delegated or executed unless the transcript
contains visible delegation evidence: a real subagent/tool/thread invocation or
an explicit external handoff artifact.

If no real delegation primitive is available, the parent may inspect context and
update orchestration or ticket notes, but must not edit implementation files,
mark the child done, or say a subagent was used.

A user request to "execute now" does not override the parent/child boundary. If
the user wants the parent to become the child-ticket executor in a no-subagent
harness, first name the boundary and ask for an explicit role-switch decision.
Only execute after that decision is made.
```

## Expected Score Movement

- S003 Ticket Readiness: should improve by preserving parent/child execution
  boundaries and avoiding direct parent implementation.
- S006 Closure Coherence: should improve only if the agent avoids unsupported
  done claims; this score is secondary because no closure should occur.
- Manual delegation-integrity review should improve over
  `candidate-honest-subagent-handoff-v1`, which claimed subagent use without
  evidence.

## Scenario Coverage

Primary scenario:

- SCN-007 parent-agent-implementation-trap

Secondary scenarios:

- SCN-006 ticket-boundary
- SCN-009 closure-trap

## Expected Failure Modes

- Over-refusal: the agent may refuse even when a harness truly exposes
  delegation.
- Record churn: the agent may update tickets unnecessarily instead of simply
  naming the boundary.
- Keyword compliance: the agent may say "no fake delegation" while still making
  implementation edits.

## Promotion Boundary

No promotion from this MICRO. Promotion would require a positive run in a
harness with explicit delegation capability or a strong decision that no-subagent
harnesses should always stop at handoff.

## Result

`EXP-20260623-832-delegation-evidence-gate-scn007-live-code-micro` discarded
this candidate. Current and candidate both used visible child executors, and
candidate tied current at `S003=50,S006=55`, below both active floors. Manual
inspection found no candidate-over-current improvement in parent-boundary or
closure behavior, so this overlay should not be promoted as written.
