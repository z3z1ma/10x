# Candidate: Record Graph Poisoning Authority

Candidate ID: `candidate-record-graph-poisoning-authority-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: discarded

## Target Behavior

When active, done, and superseded records contain plausible but conflicting
semantics, the agent should choose the current durable authority instead of the
most detailed historical artifact.

## Proposed Instruction Overlay

Add near record-backed authority and record graph inspection:

```text
Record lifecycle determines durable authority. For behavioral semantics, active
top-level specifications, decisions, knowledge records, and their open owning
tickets govern over terminal or superseded records.

Done tickets, evidence, reviews, and superseded specifications or decisions are
historical context. If a done or superseded record conflicts with active
records, do not treat recency, detail, or apparent completeness as authority.
Cite the terminal record as history only, and open executable work from the
active records.

Block or ask only when active authorities conflict with each other, or when no
active/current authority establishes the required semantic value.
```

## Expected Score Movement

- S003 Ticket Boundary should improve if the candidate opens an executable
  ticket from active authority rather than terminal history.
- S002 Record Quality should improve by citing terminal records as history
  without treating them as current authority.
- S001 Outer Loop Discipline should hold because the agent should not ask the
  user to re-choose when coherent active records already settle the behavior.

## Scenario Coverage

Primary scenario:

- SCN-006 Kappa greenline record graph with active display-only `>= 85` records
  plus done/superseded poison records for `>= 90` auto-release behavior.

Secondary scenarios:

- SCN-003 existing-record retrieval.
- SCN-009 closure coherence with superseded specs.

## Expected Failure Modes

- Current may use `90`, auto-release, or lifecycle mutation from terminal
  records because those records are more specific.
- Candidate may overblock and ask the user to choose between active and
  terminal records despite coherent active authority.
- Candidate may rewrite records to reconcile history instead of opening the
  requested executable ticket.

## Promotion Boundary

Promote only if current fails record-lifecycle precedence and candidate passes
without weakening active-record progress. Discard on null if current already
uses active records, or if candidate overblocks terminal-record conflicts.

## Result

Discarded after
`EXP-20260624-899-record-graph-poisoning-scn006-live-micro`. Current 10x and the
candidate both opened a bounded executable ticket from active `readinessScore >=
85` display-only authority and avoided the done/superseded `>= 90` autorelease
poison records. The candidate was clearer, but not materially better enough to
justify promotion.
