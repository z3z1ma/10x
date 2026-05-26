# Mill Scheduling Agent

ID: spec:mill-scheduling-agent
Type: Spec
Status: active
Created: 2026-05-25
Updated: 2026-05-25

## Summary

This spec defines the autonomous scheduling agent that pulls work into free workstations. It reads the `.loom/` graph, resolves dependencies, applies priority and WIP rules, and uses an LLM advisory for heijunka (load leveling) and readiness assessment.

## Product Slice

This spec owns the scheduling agent's decision logic: what ticket to execute next and when. It does NOT own workstation lifecycle (that's `spec:mill-factory-floor`), merge behavior (`spec:mill-shipping-dock`), or inter-iteration quality signals (`spec:mill-process-control`).

## Spec Set Coverage

Completes the "what enters the line" question for the production Factory Floor. Without this spec, the operator must manually select every ticket. With it, the factory pulls work autonomously when capacity exists.

## Problem

Manual ticket selection is fine for 1-2 tickets but breaks down at production scale. The operator shapes 10 tickets across 2 plans, sets priorities, and expects the factory to pull them in a sensible order without being told each time. Dependencies must be respected. Load should be leveled. The operator shouldn't need to babysit the queue.

## Desired Behavior

When a workstation becomes free and WIP limit allows, the scheduling agent:

1. Scans `.loom/tickets/` for tickets with status `open` or `shaped` (configurable ready statuses).
2. Filters to tickets whose dependencies are satisfied (referenced tickets are `closed` or `shipped`).
3. Ranks remaining candidates by priority (explicit field, plan ordering, or operator override).
4. Applies heijunka via LLM advisory: given the recent execution history and candidate types, recommends an ordering that avoids bunching similar work.
5. Pulls the top candidate into the free workstation.

The scheduling agent is optional and can be disabled. When disabled, only manual start works. When enabled, it respects WIP limits and only pulls when capacity exists.

## Not Doing

- Semantic interpretation of ticket prose beyond structured fields (ID, status, related records, priority)
- Creating or modifying tickets
- Deciding acceptance or closure
- Running the workstation (that's the engine)
- Multi-operator priority negotiation
- Cross-workspace scheduling

## Requirements

- REQ-001: The scheduling agent MUST only pull tickets whose status is in a configured set of ready statuses (default: `open`, `shaped`).

- REQ-002: The scheduling agent MUST resolve dependencies by inspecting `## Related Records` for references to other tickets. A ticket is dependency-satisfied only when all referenced tickets with blocking relationship indicators are `closed`, `shipped`, or `cancelled`.

- REQ-003: The scheduling agent MUST respect priority ordering. Priority sources in precedence order: (1) explicit `Priority:` field in ticket, (2) ordering within a parent plan's ticket list, (3) creation date (older first).

- REQ-004: The scheduling agent MUST respect WIP limits. It never pulls a ticket when active workstations equal or exceed the configured WIP limit.

- REQ-005: The scheduling agent SHOULD use an LLM advisory for heijunka. The advisory receives: the candidate list with ticket summaries, recent execution history (what types of work just completed), and returns a recommended ordering. The advisory model is configurable per-factory.

- REQ-006: The scheduling agent MUST be disableable. When disabled, workstations only start via manual operator action.

- REQ-007: The scheduling agent MUST log its decisions: which tickets were considered, which were filtered (and why), what the LLM advisory recommended, and which ticket was selected.

- REQ-008: The scheduling agent MUST trigger automatically when a workstation finishes (ticket reaches shipping dock or is stopped) AND WIP capacity exists AND enabled.

- REQ-009: The operator MUST be able to override scheduling by: pinning specific tickets to be next, excluding tickets from scheduling, or reordering the queue manually.

## Scenarios

### SCN-001: Automatic Pull After Completion

Exercises: REQ-001, REQ-004, REQ-008

GIVEN scheduling is enabled, WIP limit is 2, 1 workstation is active, 3 tickets are `open`
WHEN workstation W finishes (ticket closed)
THEN active workstations drop to 0
AND the scheduling agent pulls the highest-priority ready ticket into a new workstation
AND a second ticket is pulled (WIP allows 2)

### SCN-002: Dependency Blocking

Exercises: REQ-002

GIVEN ticket B references ticket A in Related Records with "depends on ticket:A"
AND ticket A is status `active`
WHEN the scheduler considers ticket B
THEN ticket B is filtered out as dependency-unsatisfied
WHEN ticket A later reaches `closed`
THEN ticket B becomes eligible on next scheduling pass

### SCN-003: Heijunka Advisory

Exercises: REQ-005

GIVEN 4 ready tickets: 2 refactoring, 1 feature, 1 test improvement
AND the last 2 completed tickets were both refactoring
WHEN the LLM advisory is consulted
THEN it recommends interleaving: feature or test next, not a 3rd refactor
AND the scheduler follows the advisory recommendation

### SCN-004: Disabled Scheduling

Exercises: REQ-006

GIVEN scheduling is disabled
WHEN a workstation finishes
THEN no automatic pull occurs
AND the workstation slot remains free until the operator manually starts work

### SCN-005: Operator Override

Exercises: REQ-009

GIVEN 5 ready tickets, scheduler would pick ticket C next
WHEN the operator pins ticket E as next
THEN the next pull selects ticket E regardless of priority or heijunka

## Evidence Plan

- REQ-001-002 / SCN-001-002: Unit test with fixture tickets showing correct filtering by status and dependency resolution.
- REQ-003: Test showing priority ordering from explicit field, plan ordering, and creation date fallback.
- REQ-005 / SCN-003: Integration test with mock LLM that verifies advisory input format and that scheduler uses the response.
- REQ-007: Test that scheduling decisions are logged with reasoning.
- REQ-009 / SCN-005: Test that pinned tickets override computed ordering.

## Interface Contract

### Scheduler Input

```python
@dataclass
class SchedulingContext:
    ready_tickets: list[TicketSummary]     # status in ready set
    active_workstations: list[WorkstationState]
    wip_limit: int
    recent_completions: list[CompletionRecord]  # for heijunka
    operator_overrides: ScheduleOverrides   # pins, exclusions
```

### Scheduler Output

```python
@dataclass
class SchedulingDecision:
    selected_ticket: str | None           # ticket ID or None if nothing ready
    candidates_considered: list[str]
    filtered_out: dict[str, str]          # ticket_id -> reason
    advisory_recommendation: list[str]    # LLM ordering suggestion
    reasoning: str                        # human-readable decision log
```

### LLM Advisory Prompt Shape

The advisory receives a structured summary (not full record prose) and returns a ranked list with brief reasoning. It does not have authority to modify tickets or override hard constraints (dependencies, WIP).

## Constraints

- The scheduling agent reads `.loom/` but MUST NOT write to it. It only triggers workstation creation through the Factory Floor engine.
- LLM advisory is best-effort. If the model is unavailable or times out, fall back to deterministic priority ordering.
- Dependency resolution uses only explicit references in `## Related Records`. Implicit semantic dependencies are not inferred.
- The scheduling agent MUST NOT reason about ticket prose meaning to determine readiness. Readiness is a status field check.

## Related Records

- `spec:mill-factory-floor` - the engine that runs workstations this agent feeds
- `spec:mill-process-control` - may cause tickets to re-enter the queue (rework after jidoka stop)
- `spec:mill-shipping-dock` - completion event triggers next scheduling pass
- `constitution:main` - factory principles (pull not push, WIP limits, heijunka)
