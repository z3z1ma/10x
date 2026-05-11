---
name: loom-frontend-ui-engineering
description: "Use when user-facing UI engineering needs coordinated behavior/design handling: components, pages, flows, layouts, interactions, responsive/accessibility/visual quality, frontend state, data fetching, or browser runtime evidence."
---

# loom-frontend-ui-engineering

Frontend UI engineering is a Loom playbook for user-facing interface work.

It turns design intent into specs, slices implementation through tickets and Ralph
packets, records browser evidence, and routes accessibility, performance, and
visual risks through audit.

## Core Dependency

Use `loom-core` first. This playbook composes `loom-specs`, `loom-tickets`,
`loom-ralph`, `loom-evidence`, `loom-audit`, `loom-knowledge`, and
`loom-retrospective`.

## Use This Playbook When

Use this playbook when:

- creating or modifying UI components, pages, flows, layouts, or interactions
- visual quality, responsive behavior, or accessibility matters
- browser runtime state must be observed
- frontend state, data fetching, loading, error, or empty states are in scope
- design system adherence or existing UI patterns constrain the work
- UI work needs screenshots, DOM inspection, console/network checks, or performance
  observations

## Route

Use this route:

```text
intent -> contract -> slice -> build -> observe -> review -> preserve
```

## Intent

Clarify:

- user task or operator workflow
- primary state and secondary states
- success, empty, loading, error, disabled, permission, and offline states
- desktop and mobile behavior
- accessibility expectations
- design system or existing component patterns
- performance or responsiveness constraints
- non-goals and adjacent UI not being changed

Route durable intended behavior to `loom-specs` when it affects more than one
ticket or future work.

## Contract

Good UI specs include:

- `REQ-*` for behavior, state, accessibility, and quality constraints
- `SCN-*` for visible scenarios and interaction probes
- examples or non-examples when visual quality is fuzzy
- evidence plan for screenshots, DOM, accessibility tree, console, network, and
  runtime behavior

Use existing design-system docs, component atlases, and source patterns as context.
Promote reusable UI conventions to `loom-knowledge`.

## Build

Implement in thin slices:

- component structure before broad integration
- one user path before all variants
- data loading before interaction polish when the flow depends on data
- accessibility and keyboard behavior with the component, not after it
- responsive behavior before claiming visual completion

Prefer composition over configuration-heavy components. Separate data loading from
presentation when it improves clarity. Match the project's existing state and
styling conventions.

## Observe

For browser-backed UI work, use `loom-browser-testing-with-devtools` or equivalent
runtime observation.

Evidence may include:

- screenshots before and after
- DOM or accessibility tree excerpts
- console output showing no relevant errors
- network requests and payload shape
- viewport checks at important breakpoints
- keyboard navigation or focus observations
- performance trace or Core Web Vitals when relevant

Record observations with `loom-evidence` when they support ticket closure or audit.

## Review

Review UI against:

- intended behavior and scenarios
- accessibility
- responsive layout
- visual hierarchy and spacing
- loading, empty, error, and permission states
- state management and data-fetching boundaries
- security of rendered external data
- performance and unnecessary rerenders
- consistency with existing component patterns

Use `loom-audit` for fresh-context UI review when closure depends on subjective
quality, accessibility, performance, or browser evidence.

## Done Means

The UI pass is done when:

- behavior and quality expectations are written or scoped in the ticket
- desktop and mobile states in scope were checked
- accessibility and keyboard expectations were checked when interactive UI changed
- runtime browser observations exist when static code review is insufficient
- evidence supports the exact UI claim
- reusable UI patterns or traps are promoted through retrospective when useful
