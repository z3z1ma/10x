# Critique Lens

A good critique asks questions like:

- what could break in the changed code
- what claim here is weaker than it sounds
- what assumption is hidden
- what evidence is missing
- what scenario would break this
- where did the implementation or page overfit the happy path
- what did the author forget to update
- what future reader could misunderstand

## Common lenses

- correctness
- scope discipline
- evidence sufficiency
- operator clarity
- failure modes
- maintenance burden
- trust-boundary integrity

## Target Types

Critique can target:

- code diffs, branches, commits, or pull requests
- behavior changes after a Ralph iteration
- tickets, specs, plans, research, packets, evidence, and wiki pages
- release or handoff packages
- external summaries that mirror Loom work

The target type changes the evidence reviewed. It does not change the owner
model: critique owns findings and verdicts, while tickets own live execution
state.

## Implementation Review Order

For code or behavior changes, review the verification story before the
implementation details when practical:

1. tests, evidence, screenshots, performance numbers, or before/after observations
2. ticket/spec scope and acceptance coverage
3. implementation correctness, simplicity, architecture, security, and performance
4. cleanup, generated files, dependency/tooling changes, and residual risks

This order catches a common failure: an implementation that looks plausible but is
only weakly evidenced, tests implementation details, or satisfies a nearby behavior
instead of the requested claim.

Use the family-appropriate `review_target` shape when recording that target:
direct critique records keep a scalar, grep-friendly target handle in
frontmatter, while critique packets use a structured mapping for target kind,
summary, stable reference, diff handle, and optional paths.

## Packet Expectation

Use a critique packet for implementation/code review when a fresh reviewer
needs the ticket, parent plan or initiative, spec, research, evidence, prior
packet output, and git diff in one bounded review contract.

Do not compile a packet just to critique a Loom artifact by default. A ticket,
plan, spec, or wiki page can be reviewed directly as an artifact. Use a packet
only when the review is broad, high risk, or needs fresh-context isolation.

## Named Profiles

Use named profiles when a ticket or parent packet declares the review risk.
Profiles are lenses, not permanent agents or new layers.

### `protocol-change`

- authority drift
- layer ownership conflicts
- packet/ticket truth mismatch
- repair and retrospective implications

### `api-contract`

- backwards compatibility
- error semantics
- versioning
- client impact

### `code-change`

- correctness against the ticket and spec
- whether tests and observations verify behavior through public or shared
  interfaces rather than implementation details
- unintended side effects
- error handling
- edge cases
- integration boundaries
- maintainability of the changed code
- whether feature work, refactors, formatting, dependency changes, generated files,
  and cleanup were separated enough for honest review

For code changes, the default review axes are correctness, readability/simplicity,
architecture, security/trust boundary, and performance. Pick specialized profiles
when one axis carries material risk, but do not let a passing test suite erase the
other axes.

### `code-structure`

- behavior preservation during refactor or simplification
- whether module boundaries became deeper or shallower
- coupling, locality, and test seam quality
- removal of accidental complexity without hiding behavior changes
- whether evidence proves no intended behavior changed
- whether the simplification preserves all inputs, outputs, side effects, ordering,
  and error behavior
- whether the diff separates behavior-preserving cleanup from feature work

### `ai-artifact-cleanup`

- leftover debug statements, unique debug prefixes, console logs, or temporary
  instrumentation
- placeholder text, TODOs, stubs, no-op variables, commented-out code, dead
  branches, or orphaned helpers left by an implementation pass
- excessive explanatory comments that narrate obvious code instead of preserving
  intent
- over-engineered abstractions, wrappers, or generic utilities created before
  enough use cases exist
- hardcoded secrets, credentials, local paths, test data, or environment values
- whether cleanup evidence used targeted searches or diff review rather than a
  broad vibe that the code "looks clean"

### `test-coverage`

- missing regression coverage
- weak assertions
- untested edge cases
- mismatch between acceptance criteria and tests
- evidence gaps when automated tests are not practical

### `data-migration`

- schema drift
- rollback
- idempotency
- data loss
- migration evidence

### `security`

- secrets
- authentication and authorization
- injection
- dependency risk
- unsafe tool permissions

### `dependency-tooling`

- package, runtime, build, lint, typecheck, formatter, or toolchain drift
- compatibility and lockfile risk
- generated-file and local automation boundaries
- whether tooling changes affect developer or agent feedback loops
- security exposure from dependency changes

### `performance`

- asymptotic behavior
- hot path changes
- cache invalidation
- before/after measurement evidence
- whether the alleged bottleneck was measured rather than assumed
- whether the change affects representative data, devices, network, or runtime
  constraints
- whether one variable changed per experiment and repeated validation supports
  the result

### `product-ux`

- primary user task clarity
- whether the change solves a real user problem rather than only adding surface area
- discoverability and flow friction
- before/after quality delta against the baseline
- empty, loading, error, and edge-state usefulness
- whether the result is materially better or merely more complex

### `visual-design`

- information hierarchy and visual rhythm
- affordance clarity for primary and destructive actions
- density, spacing, typography, and scan path
- responsive composition at small and large viewports
- before/after screenshots or visual observations when available
- avoidance of generic AI-looking patterns unless they are project-appropriate

### `accessibility`

- keyboard path and focus order
- accessible names and visible labels
- heading and landmark structure
- color contrast and non-color indicators
- reduced-motion behavior when motion is used
- screen-reader legibility or accessibility-tree evidence when available

### `operator-clarity`

- whether the next agent will know what to do
- explicit stop conditions
- honest ticket, evidence, critique, retrospective / promotion disposition, and
  wiki-specific disposition when applicable
- whether explanatory pages overstate certainty

### `workflow-boundary`

- whether the workflow moves through existing owner layers instead of creating a
  hidden ledger
- whether plans, packets, critique, ship summaries, or external systems are
  accidentally owning ticket truth
- whether stop conditions and loopbacks prevent forced execution through
  ambiguity
- whether parallel or delegated work has non-overlapping write scopes and parent
  reconciliation

### `operator-surface`

- whether the project's user-facing instructions, Loom skills, templates,
  examples, adapters, or support docs tell the same story
- whether a change adds a required support surface outside the declared Loom
  owner graph without an explicit owner-layer reason
- whether harness-specific convenience is being mistaken for canonical project
  truth or protocol behavior
- whether skill descriptions and read order make activation discoverable without
  duplicating workflow truth

### `review-feedback-disposition`

- whether each external, human, subagent, or model-review finding was read fully
  and understood before action
- whether unclear multi-item feedback was clarified or split before partial
  implementation
- whether invalid feedback was rejected with evidence rather than performative
  agreement or avoidance
- whether accepted feedback was implemented one item at a time with verification
  and ticket-owned disposition where closure depends on it

## Profile Selection

- low risk: usually `operator-clarity` or no required profile
- medium risk: choose the one or two profiles matching the change class
- high risk: require the profile matching the domain plus `operator-clarity`
- user-facing UI/product changes usually need `product-ux` plus `visual-design`
  or `accessibility`, even when functional tests pass
- changes produced by AI implementation or broad refactor should consider
  `ai-artifact-cleanup` even when the main review profile is `code-change` or
  `code-structure`
- work that consumes review comments should consider `review-feedback-disposition`
  when the correctness of the feedback affects closure

If the risk class is unclear, treat it as medium and explain the uncertainty.

Use `skills/loom-records/references/change-class.md` when the review target
declares a `change_class` or when profile selection would otherwise be
ambiguous.
