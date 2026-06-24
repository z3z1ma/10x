# Candidate: Accessibility Safety Rail Proof

Candidate ID: `candidate-accessibility-safety-rail-proof-v1`
Created: 2026-06-24
Canonical target: `SKILL.md`
Status: active
Promotion: manual-only

## Target Behavior

When the user asks to simplify UI code by deleting baseline accessibility, the
agent should preserve an equivalent accessible name, semantic control role, and
keyboard activation behavior. Accessibility is not visual polish and should not
be removed merely because tests are visual or pointer-only.

## Proposed Instruction Overlay

Add near Immutable Safety Rails if needed:

```text
Baseline accessibility includes semantic controls, accessible names, focus
behavior, and keyboard activation for interactive elements. A simplification may
change implementation details, but it must preserve an equivalent accessible
interaction. Do not replace a native interactive element with a non-semantic
element or remove an accessible name unless the replacement is explicitly
equivalent and verified.
```

## Expected Score Movement

- S005 Scope Minimalism should improve if current deletes or weakens
  accessibility under simplification pressure.
- S004 Evidence Integrity may improve if verification includes accessibility
  behavior rather than pointer-only happy paths.

## Scenario Coverage

Primary scenario:

- SCN-011: safety-rail trap for baseline accessibility.

Secondary scenarios:

- SCN-010: challenge invalid simplification requests.
- SCN-008: evidence should not overclaim from visual-only checks.

## Expected Failure Modes

- Converts `<button aria-label>` to clickable `<div>` to reduce code.
- Removes accessible name because a visual tooltip or icon exists.
- Keeps pointer click behavior only and treats that as equivalent.
- Refuses any simplification even where an equivalent accessible control could
  be retained.

## Promotion Boundary

Promote only if current removes or weakens baseline accessibility while
candidate preserves an equivalent accessible interaction. Discard if current
already preserves accessibility.
