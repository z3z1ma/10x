---
name: loom-specs
description: "Use when behavior, interfaces, invariants, requirements, scenarios, or intended outcomes need a stable source before tickets, worker runs, evidence, or audit rely on them."
---

# loom-specs

Specs own intended behavior: requirements, scenarios, interfaces, invariants,
boundaries, quality bars, and evidence expectations for one coherent product
slice.

Specs do not own sequencing, investigation notes, live execution, implementation
progress, evidence sufficiency, audit verdicts, ticket closure, durable policy, or
accepted reusable explanation.

## Use This Skill When

Use it when:

- intended behavior is fuzzy, disputed, shared, reusable, or easy to misstate
- an interface, command, workflow, UX, permission, data shape, record shape, error, compatibility promise, or invariant needs a contract
- product direction, state shape, data shape, abstraction boundary, or design coherence needs a behavior-level source before execution
- a ticket, plan, worker, evidence record, or audit would otherwise redefine what correct means
- requirements or scenarios need to be added, changed, superseded, accepted, retired, or referenced

## Inspect

Specs live under `.loom/specs/`.

```bash
find .loom/specs -maxdepth 1 -name '*.md' -print 2>/dev/null | sort
grep -R '^ID: spec:' .loom/specs 2>/dev/null || true
grep -R '^Type: Spec' .loom/specs 2>/dev/null || true
grep -R '^Status:' .loom/specs 2>/dev/null || true
grep -R 'REQ-[0-9][0-9][0-9]' .loom/specs 2>/dev/null || true
grep -R 'SCN-[0-9][0-9][0-9]' .loom/specs 2>/dev/null || true
```

Search by capability, domain term, interface, actor, error state, requirement ID,
scenario ID, related record, source path, command, API, or data shape.

Treat `active` and `accepted` specs as the current behavior map. If the current
surface no longer matches a spec, update, split, supersede, or retire it before
downstream work relies on it.

## Record Shape

Use stable semantic IDs and matching filenames:

```text
ID: spec:<slug>
.loom/specs/<slug>.md
```

Required labels:

```text
ID: spec:<slug>
Type: Spec
Status: draft
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
```

Optional links:

```text
Replaces: spec:<slug>
Superseded By: spec:<slug>
```

Statuses:

- `draft`: contract is still being shaped; downstream reliance must name the risk.
- `active`: current working behavior truth with named open questions and limits.
- `accepted`: stable enough for downstream records to rely on as current behavior truth.
- `superseded`: replaced by a named successor.
- `retired`: product surface or behavior no longer guides work.

Requirements use stable `REQ-*` IDs. Scenarios use stable `SCN-*` IDs. Do not
reuse IDs for different behavior; supersede old IDs when reuse would mislead.

## Write Or Update

Read `references/spec-shape.md` before creating or materially reshaping a spec.
Use `templates/spec.md`.

When creating or reshaping:

- inspect existing specs, related records, and source reality that constrain behavior
- choose one coherent product slice before writing requirements
- split separate actors, workflows, interfaces, permissions, evidence plans, or lifecycles
- shape requirements, scenarios, boundaries, non-goals, evidence expectations, and open questions together
- use examples, non-examples, data shapes, and interface boundaries when they prevent invented design direction

When updating:

- read the whole spec
- search inbound references before changing cited `REQ-*` or `SCN-*` IDs
- classify changes as added, modified, removed, renamed, split, retired, or superseded
- update requirements, scenarios, evidence expectations, open questions, and status together

When superseding or retiring:

- preserve the reason
- name the successor when one exists
- update `Status:`, `Updated:`, `Replaces:`, and `Superseded By:` as appropriate
- repair or flag inbound refs that would otherwise cite stale behavior

## Current Spec Set

The `active` and `accepted` spec set should be strong enough for a future agent to
rebuild intended product behavior without chat history or implementation
archaeology. This is a coverage goal, not permission to write umbrella specs.

Create or shape missing focused specs when downstream work depends on implicit
behavior. Split broad specs instead of expanding them.

## Stop Conditions

Stop and route before writing when:

- the slice collapses materially different product surfaces
- behavior depends on unresolved product, data, state, interface, permission, compatibility, or coherence choices
- evidence expectations are too vague to guide tickets or audit
- the work is sequencing, live execution, investigation, durable policy, observation, audit, or knowledge rather than intended behavior
- current implementation and intended behavior conflict and the operator or owning record has not resolved which should win

## Done Means

The spec has a truthful status, owns one coherent slice, names current behavior,
requirements, scenarios, boundaries, evidence expectations, and open questions,
keeps stale IDs from misleading downstream work, and can be cited by tickets
without redefining behavior.
