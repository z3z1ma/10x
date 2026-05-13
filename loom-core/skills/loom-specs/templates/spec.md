# <Spec Title>

ID: spec:<slug>
Type: Spec
Status: draft
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>

<!--
Add only when useful. Remove this comment before saving if unused.

Replaces: spec:<slug>
Superseded By: spec:<slug>
-->

## Summary

<Describe what behavior this spec defines, who or what surface it affects, and
which downstream work should cite it.>

## Product Slice

<Name the single product surface area this spec owns and where that slice stops.
If the intended behavior spans materially different actors, workflows, interfaces,
permissions, evidence plans, or lifecycles, split it into multiple specs instead of
creating one umbrella contract.>

## Spec Set Coverage

<Say how this spec contributes to the current `active`/`accepted` spec set's goal
of regenerating intended product behavior from scratch. Name adjacent behavior that
needs separate specs or is intentionally out of scope.>

## Problem

<State the ambiguity, user need, quality gap, interface contract, or owner-record
mismatch this spec resolves. Include current behavior, baseline, or counterfactual
when it matters.>

## Desired Behavior

<Describe the intended behavior in plain language. Keep implementation sequencing
out unless the public interface or command shape is the behavior.>

## Not Doing

<Name adjacent product surfaces, attractive exclusions, non-goals, and boundaries
that keep the contract focused.>

## Requirements

Use stable `REQ-*` IDs. Each requirement should state one observable behavior,
invariant, interface guarantee, error semantic, permission rule, compatibility
promise, or quality constraint.

- REQ-001: <MUST/SHOULD + actor or surface + condition + observable outcome>

## Scenarios

Use stable `SCN-*` IDs. Each scenario should cite the requirements it exercises and
be concrete enough to test, observe, or review.

### SCN-001: <Scenario Name>

Exercises: REQ-001

GIVEN <initial observable state>
WHEN <trigger or action>
THEN <observable outcome>
AND <additional outcome or invariant when useful>

## Evidence Plan

<Name the tests, commands, screenshots, observations, traces, manual checks, or
evidence records that could prove the requirements and scenarios.>

- REQ-001 / SCN-001: <evidence type, expected artifact, and limits>

## Open Questions

<Name unresolved questions and whether they block downstream work. Remove this
section only when no material questions remain.>

- <question or None - current contract is ready>: <blocks downstream work? yes/no>

## Quality Bar

<Use for UI, UX, product, workflow, API ergonomics, developer experience, or other
quality-sensitive behavior. Name what makes the result materially better than the
baseline and how a reviewer could tell. Remove if not useful.>

## Interface Contract

<Use for public APIs, module interfaces, component props, commands, data shapes,
file formats, packets, or cross-worker contracts. Remove if not useful.>

- Inputs:
- Outputs:
- Side effects:
- Error semantics:
- Validation boundary:
- Compatibility or deprecation:

## Examples And Non-Examples

<Use examples, non-examples, screenshots, comparable flows, short prose examples,
or anti-patterns when they make fuzzy behavior concrete. Remove if not useful.>

## Constraints

<Name constraints, compatibility requirements, safety limits, design-system rules,
or authority boundaries that shape acceptable behavior. Remove if not useful.>

## Amendment Notes

<Use when changing an existing spec. Classify changes as added, modified, removed,
renamed, split, retired, or superseded. Name affected `REQ-*` and `SCN-*` IDs,
successor IDs, inbound reference checks, and any status changes needed because the
current product surface moved. Remove for new specs.>

## Related Records

<List only records or paths that materially constrain or explain this spec. Say why
each matters. Remove this section if none are useful.>

- `<record-id or path>` - <why this record matters>
