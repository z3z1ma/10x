---
name: loom-specs
description: "Manages Loom specs: creates, shapes, updates, supersedes, and retires durable intended-behavior contracts under .loom/specs. Use when behavior, interfaces, invariants, requirements, or scenarios need a stable source before tickets, packets, evidence, or audit rely on them."
---

# loom-specs

Specs own intended behavior.

A spec says what a system, workflow, interface, product surface, command, data
shape, permission boundary, error state, or record shape should do.

It turns fuzzy intent into requirements and scenarios that downstream tickets,
packets, evidence, and audit can cite.

Specs do not own live execution state, implementation progress, evidence
sufficiency, audit verdicts, or ticket closure. Tickets own scoped acceptance for
a work unit and may cite spec requirements and scenarios.

## Use This Skill When

Use this skill when:

- intended behavior is fuzzy, disputed, reusable, shared, or easy to misstate
- interface, API, workflow, UX, permission, error, compatibility, or invariant
  behavior needs a durable contract
- a ticket, plan, audit, packet, or worker would otherwise redefine what correct
  means
- operator answers need to become behavior truth before execution
- requirements or scenarios need to be added, modified, removed, renamed,
  superseded, accepted, or retired
- evidence or audit needs a stable behavior claim to evaluate

Do not use specs for execution sequencing, investigation notes, observed evidence,
audit findings, implementation journals, or reusable explanation that does not own
intended behavior.

## Dispatch

If creating or reshaping a spec:

- read `references/spec-shape.md`
- inspect existing specs and related records before asking the operator to repeat
  facts
- inspect source reality when current behavior, interfaces, errors, or constraints
  matter
- shape fuzzy behavior until requirements, scenarios, boundaries, and open
  questions are clear enough for downstream work
- use `templates/spec.md`
- write the smallest citable spec

If updating a spec:

- read the whole spec
- search for inbound references to affected `REQ-*` and `SCN-*` IDs when behavior
  changes
- classify the amendment as added, modified, removed, renamed, or superseded
- update requirements, scenarios, evidence expectations, and open questions
  together
- supersede old IDs when reuse would mislead downstream records

If superseding or retiring a spec:

- preserve the reason
- name the successor when one exists
- update `Status:`, `Updated:`, `Replaces:`, or `Superseded By:` as appropriate
- repair or flag inbound refs when downstream records would otherwise cite stale
  behavior

If only finding or summarizing specs:

- inspect `.loom/specs/`
- report status, relevant requirements, scenarios, boundaries, and open questions
- do not mutate records unless the operator asked for a change

## Finding Specs

Specs live under `.loom/specs/`.

Useful starting points:

```bash
find .loom/specs -maxdepth 1 -name '*.md' -print | sort
grep -R '^ID: spec:' .loom/specs || true
grep -R '^Type: Spec' .loom/specs || true
grep -R '^Status:' .loom/specs || true
grep -R 'REQ-[0-9][0-9][0-9]' .loom/specs || true
grep -R 'SCN-[0-9][0-9][0-9]' .loom/specs || true
```

Search by capability, domain term, interface name, user task, error state,
requirement ID, scenario ID, related record ID, source path, command, API, or data
shape.

## Spec IDs And Filenames

Use stable semantic IDs:

```text
spec:<slug>
```

Use matching filenames without the `spec:` prefix:

```text
.loom/specs/<slug>.md
```

Choose a slug future agents will search for.

Do not use date prefixes for ordinary spec filenames.

## Required Top Labels

Specs use plain body labels near the top:

```text
ID: spec:<slug>
Type: Spec
Status: draft
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
```

Add only when useful:

```text
Replaces: spec:<slug>
Superseded By: spec:<slug>
```

## Status Lifecycle

Use this lifecycle:

- `draft`: the contract is being shaped and downstream work should not rely on it
  unless the open risk is explicit
- `active`: current working behavior truth, usable by downstream work with named
  open questions and limits
- `accepted`: reviewed enough that downstream tickets, packets, evidence, and
  audit can rely on it as the behavior contract
- `superseded`: replaced by a named successor
- `retired`: intentionally no longer used

Use `active` for current contracts that are useful but still evolving.

Use `accepted` when the contract is stable enough for downstream records to rely on.

## Requirements And Scenarios

Every spec should include at least one requirement and one scenario unless the
record is still an early `draft`.

Requirements use stable local IDs:

```text
REQ-001
```

A requirement states one intended behavior, invariant, interface guarantee, error
semantic, permission rule, compatibility promise, or quality constraint.

Scenarios use stable local IDs:

```text
SCN-001
```

A scenario is an observable probe of behavior. It should describe state, trigger,
and outcome clearly enough for tickets, evidence, and audit to use.

Ticket acceptance owns closure criteria for scoped work and can cite
`spec:<slug>#REQ-001` or `spec:<slug>#SCN-001` when useful.

## Shaping Posture

When operator input is needed:

- ask one material question at a time
- recommend an answer when the repository, records, risk, or product shape supports
  one path
- challenge vague or overloaded terms before they become requirements
- test proposed wording against concrete scenarios
- invent success, edge, failure, permission, empty-state, compatibility, and
  idempotency scenarios when they reveal boundaries
- route unresolved investigation to research, complex execution strategy to plans,
  live work to tickets, durable judgment to constitution, and reusable explanation
  to knowledge

Stop shaping when remaining questions no longer change intended behavior or can be
recorded as open questions with clear downstream limits.

## Spec Invariants

Every spec should preserve these invariants:

- intended behavior is separated from implementation plan
- requirements and scenarios are stable, citable, and observable
- important boundaries, non-goals, constraints, and open questions are explicit
- evidence expectations are concrete enough to guide tickets and audit
- public or shared interfaces name inputs, outputs, errors, validation, and
  compatibility expectations when those details matter
- quality claims have examples, non-examples, probes, or evidence expectations when
  they affect downstream work
- cited `REQ-*` and `SCN-*` IDs are not silently reused for different behavior
- specs do not claim ticket closure, evidence sufficiency, audit verdict, or
  implementation progress

## Done Means

Spec work is done when:

- the spec has a truthful status
- behavior-bearing requirements and scenarios are clear enough to cite
- open questions and downstream limits are visible
- related records that constrain the behavior are linked or named
- tickets can cite the spec without redefining intended behavior
