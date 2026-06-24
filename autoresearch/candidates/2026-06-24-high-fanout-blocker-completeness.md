# Candidate: High-Fanout Blocker Completeness

Candidate ID: `candidate-high-fanout-blocker-completeness-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: active
Promotion: manual-only

## Target Behavior

When inspection reveals more than three independent, execution-critical blockers
at the same upstream layer, the agent should ask all of those current blockers
together. The "default to at most three" question guideline should prevent noisy
questionnaires, not suppress material ambiguity that would otherwise enter
implementation as an unratified assumption.

## Proposed Instruction Overlay

Add near the blocker-question guidance:

```text
The first-turn "at most three" question default is not a ceiling. If inspection
exposes more than three independent current blockers at the same upstream layer,
and each answer could change implementation, acceptance criteria, tests, user
visible behavior, security, privacy, money, or operational ownership, ask all of
those blockers together in one compact grouped set. Do not defer a current
blocker solely to reduce question count.

Keep the grouped set disciplined: exclude downstream details whose relevance
depends on an upstream answer, preferences that do not change the next safe
action, and facts the codebase or records already answer. For high-fanout
ambiguity, name why the grouped set is necessary and invite the user to answer
only the branches that are already decided.
```

## Expected Score Movement

- S001 Outer Loop Discipline should hold by preventing implementation while
  independent semantic blockers remain.
- S007 Human Shaping Quality should improve if current under-asks due the
  three-question default and would require avoidable extra turns.

## Scenario Coverage

Primary scenario:

- SCN-001: complex compliance export approval workflow with six independent
  current blockers already visible in draft records/source.

Secondary scenarios:

- SCN-002: user pressure to just start despite unresolved blockers.
- SCN-006: ticket-readiness protection; no executable ticket should encode the
  missing semantic branches.

## Expected Failure Modes

- Questionnaire inflation: asks downstream UI copy, pagination, or styling
  questions before the semantic blockers are settled.
- Under-asking: asks only three blockers and leaves other current blockers
  implicit.
- Source bypass: creates an executable ticket or code using plausible compliance
  defaults from the source names rather than ratified semantics.

## Promotion Boundary

Promote only if current under-asks or encodes an implicit assumption while the
candidate asks all current independent blockers compactly without downstream
noise. Discard if current already asks the full material blocker set.
