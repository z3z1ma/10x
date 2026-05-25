# Spec Shape

A spec is a durable behavior contract for one coherent product slice. It should be
as small as the behavior allows and as precise as downstream work needs.

## Required Content

A useful spec says:

- what behavior, interface, workflow, record shape, permission boundary, error semantic, or quality contract it defines
- where the product slice starts and stops
- what problem or ambiguity requires a spec
- desired behavior and explicit non-goals
- relevant domain model, data shape, state shape, interface boundary, or abstraction constraint
- `REQ-*` requirements and `SCN-*` scenarios
- evidence expectations for the requirements and scenarios
- open questions, limits, and related records

Optional sections should earn their space: quality bar, interface contract,
examples and non-examples, constraints, amendment notes, or related records.

## Slice Discipline

Split specs by actor, workflow, interface, command, record type, permission domain,
risk boundary, evidence plan, or lifecycle when those parts can ship, regress,
retire, or be accepted independently.

Broad words such as `entire`, `all`, `platform`, `system`, `product`, or several
unrelated `and` clauses usually mean the slice is too large.

When a broad spec already exists, extract coherent successor specs or narrow the
old record until its status is truthful.

## Requirements

Requirements are durable behavior claims. Use `REQ-*` IDs starting at `REQ-001`.

Good requirements state one behavior, invariant, interface guarantee, error
semantic, permission rule, compatibility promise, or quality constraint. Name the
actor, system, API, workflow, record surface, trigger, and observable outcome when
they matter.

Use `MUST` for hard requirements and `SHOULD` only when legitimate exceptions are
named. Do not reuse a requirement ID for changed behavior.

## Scenarios

Scenarios are concrete probes. Use `SCN-*` IDs starting at `SCN-001` and cite the
requirements each scenario exercises.

GIVEN/WHEN/THEN/AND is useful when it clarifies state, trigger, and outcome.
Include happy, edge, failure, permission, compatibility, empty-state, and
idempotency cases when they affect behavior. Remove scenarios that cannot be
tested, observed, or reviewed.

## Evidence Plan

The evidence plan names how downstream work could prove the requirements and
scenarios: tests, command output, screenshots, logs, manual observations, diff
review, trace output, generated artifacts, or other durable observations.

Specs define expected evidence. Evidence records store observed artifacts.

## Quality And Interface Detail

Use a quality bar when correctness includes more than existence: task clarity,
discoverability, error clarity, density, affordance quality, compatibility,
examples, non-examples, or reduced ambiguity.

Use an interface contract for public APIs, module interfaces, commands, data
shapes, file formats, records, worker-run contracts, or cross-worker contracts.
Name inputs, outputs, side effects, ordering, idempotency, errors, validation,
compatibility, and deprecation expectations when they matter.

## Current Surface

An `active` or `accepted` spec must match the current product surface slice it
claims. If it does not:

- update in place when the same slice and IDs still own the behavior
- split when independent surfaces were collapsed
- mark `superseded` and name a successor when a new spec owns behavior
- mark `retired` when the behavior no longer exists or should no longer guide work

Do not leave stale specs as `active` or `accepted` for history.

## Shaping And Amendment

Before writing or accepting a spec, inspect existing specs, tickets, plans,
research, constitution, evidence, knowledge, and source files that constrain the
behavior. Shape until scope, design model, observable scenarios, downstream use,
and current spec-set coverage are clear.

When amending, classify changes as added, modified, removed, renamed, split,
retired, or superseded. Search inbound references before changing cited IDs. If a
requirement or scenario splits, narrows, or changes enough to mislead, mark the old
ID as superseded in prose and add successors.

## Routing

Route execution strategy to plans, live work to tickets, investigation to
research, durable judgment to constitution, observations to evidence, adversarial
review to audit, and accepted reusable explanation to knowledge.

Before downstream work relies on a spec, check completeness, correctness,
currency, slice, coverage, coherence, and citability. Audit is the separate
Ralph-backed challenge when a claim needs adversarial review.
