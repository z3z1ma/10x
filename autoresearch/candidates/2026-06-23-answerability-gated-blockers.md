# Candidate: Answerability-Gated Blockers

Candidate ID: `candidate-answerability-gated-blockers-v1`
Created: 2026-06-23
Canonical target: `SKILL.md`
Status: discarded

## Target Behavior

The agent should subtract answered facts from its blocker list before
questioning the user. This targets mixed workspaces where source, active specs,
decisions, research, and stale tickets all mention the same surface.

## Proposed Instruction Overlay

Add this rule under the existing blocker-question guidance:

```text
Before asking blocker questions, classify each apparent unknown as:

1. answered by inspected records or source;
2. unresolved current blocker;
3. stale or conflicting risk.

Do not ask the user to confirm facts already answered by records or code. Cite
or briefly state those facts only when needed to show why they are not blockers.

Ask only unresolved blockers or stale/conflict risks whose answer changes the
next safe action. If older ticket notes conflict with newer active specs,
decisions, research, or source, treat the newer authority as settled unless two
active authorities conflict. When active authorities conflict, ask the smallest
question that resolves precedence.
```

## Expected Score Movement

- S001 Outer Loop Discipline: should hold or improve by preserving inspection,
  no implementation, and current-blocker questioning.
- S007 Human Shaping Quality: should improve by avoiding user questions about
  component path, actor, token, copy, non-goals, or data fields already answered
  by records/source.
- S002 Record Graph Fitness: should hold by avoiding duplicate records and
  unnecessary stale-ticket rewrites.

## Scenario Coverage

Primary scenario:

- SCN-001 ambiguous-implementation-request

Secondary scenarios:

- SCN-003 existing-records-answer-the-question
- SCN-006 ticket-boundary

## Expected Failure Modes

- Under-questioning: treating source behavior as product intent when records do
  not support that inference.
- Stale-record overtrust: accepting old ticket notes over newer active specs or
  decisions.
- Conflict blindness: failing to ask when two active authorities disagree.
- Citation theater: citing paths while still asking the user to restate facts
  those paths already answer.

## Promotion Boundary

No promotion from one MICRO. Promotion requires at least one positive live run,
manual inspection that the candidate really suppresses answered questions
without ignoring active conflicts, and a follow-up held-out or continuation
check.

## Result

`EXP-20260623-831-answerability-gated-blockers-scn001-live-micro` produced an
automated candidate lift (`S001=100;S007=75`) over current
(`S001=100;S007=60`), but manual inspection found current already passed the
subtraction trap. Candidate and current both asked only the two unresolved
blockers. Candidate is not promotion-ready because it also provisionally named a
success threshold that the seed intentionally left unresolved.

Verdict: `mutate`, not promoted. The next useful mutation is continuation-state
handling after partial blocker answers or a stricter rule against provisional
business-threshold defaults.
