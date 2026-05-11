---
name: loom-debugging-and-error-recovery
description: "Use when an unexpected or unexplained failure needs diagnosis before fixes: failing tests/builds/CI/runtime/UI behavior, bug reports, regressions, intermittent failures, reproduction, localization, guard tests, or recovery evidence."
---

# loom-debugging-and-error-recovery

Debugging is a recovery playbook.

It preserves the failure, finds the root cause, fixes the scoped issue, guards
against recurrence, and records what future work needs.

## Core Dependency

Use `loom-core` first. This playbook composes `loom-evidence`, `loom-research`,
`loom-tickets`, `loom-specs`, `loom-ralph`, `loom-audit`, and
`loom-retrospective`.

## Use This Playbook When

Use this playbook when:

- a test, build, type check, lint, CI, browser, or runtime command fails
- a bug report arrives
- behavior does not match spec, ticket acceptance, or operator expectation
- a regression or intermittent failure needs localization
- recovery needs a guard test, evidence, or follow-up ticket

## Route

Use this route:

```text
stop -> feedback loop -> preserve -> reproduce -> localize -> trace -> hypothesize -> instrument -> reduce -> fix -> guard -> verify -> prevent
```

## Stop

Pause feature expansion when unexpected failure appears.

Do not pile unrelated changes on top of an unexplained failure. Update the active ticket
if the failure changes scope, risk, or state.

## Feedback Loop

Build the fastest reliable pass/fail loop you can before diagnosing deeply.

Useful loops include:

- focused failing test at the seam that reaches the bug
- CLI or HTTP script with fixture input and expected output
- browser automation for DOM, console, or network symptoms
- replay of a captured request, payload, or event log
- throwaway harness around one service, reducer, state machine, or adapter
- property, fuzz, stress, or repeated-run loop for intermittent failures
- bisection harness for commit, dataset, version, or config regressions

Improve the loop itself:

- make it faster
- make the signal more specific
- make it deterministic by pinning time, random seeds, filesystem, or network
- raise the reproduction rate for flaky issues before trying to fix them

If no loop can be built, record what was tried and ask for the missing artifact,
access, or permission to add temporary instrumentation. Do not pretend a guess is a
diagnosis.

## Preserve

Capture the failure before fixing when it will matter later.

Useful evidence:

- failing command and output excerpt
- reproduction steps
- environment and source state
- screenshot, console, network, or log excerpt
- CI job URL or artifact path
- data shape or input that triggers the bug

Use `loom-evidence` when the failure supports a ticket, audit, bug report, or
future diagnosis.

## Reproduce

Make the failure happen reliably.

If reproduction is not reliable, record what is known:

- frequency
- environment differences
- timing or concurrency suspicion
- state or data dependency
- recent changes
- monitoring or logs that may catch recurrence

For UI issues, use `loom-browser-testing-with-devtools` when browser runtime data
matters.

## Localize

Narrow the failure by layer:

- test itself
- source logic
- UI state or rendering
- API boundary
- database or migration
- build or dependency configuration
- environment
- external service
- generated artifact

Use source, tests, logs, diffs, and records. Use `loom-research` when the cause
depends on unfamiliar library, platform, protocol, or version behavior.

When multiple components are involved, instrument boundaries before proposing a
fix. Capture what enters and exits each layer so evidence shows where the failure
appears: UI to API, API to service, service to database, build step to signing,
test harness to system under test, or worker packet to parent reconciliation.

## Trace

Trace the failure back to the original trigger.

For stack or data-flow failures, ask repeatedly:

- what code directly produced the symptom?
- who called that code?
- what value, state, config, or environment was passed in?
- where did the bad value or assumption originate?
- what earlier guard should have caught it?

Fixing only where the error appears is usually a symptom patch. Fix at the source
when the source can be identified.

Add temporary diagnostics when manual tracing is unclear. Keep diagnostic output
focused and remove or deliberately preserve it as evidence, logging, or guard code
before closure.

## Hypothesize

Generate candidate hypotheses before testing fixes.

For hard bugs, list three to five ranked hypotheses when possible. Each should make
a falsifiable prediction. Then test one hypothesis at a time.

Good hypotheses say:

- what the root cause is
- why the evidence points there
- what minimal observation or change would confirm or reject it
- what result would falsify it

Test one variable at a time. If the hypothesis fails, remove or revert the probe
unless it is intentionally kept as instrumentation.

After three failed fix attempts, stop and question the architecture, contract,
plan, or assumptions before trying another patch. Route to `loom-specs`,
`loom-plans`, `loom-research`, `loom-constitution`, or the operator when the
pattern itself may be wrong.

## Instrument

Instrumentation should distinguish hypotheses, not dump noise.

Prefer:

- debugger or REPL inspection when available
- targeted logs at boundaries that separate hypotheses
- metrics, profiler output, query plans, or timing harnesses for performance issues
- unique debug prefixes so temporary instrumentation can be found and removed

Avoid broad logging that creates more evidence to sift than signal to act on.

## Reduce

Create the smallest failing case practical:

- focused test
- minimal input
- isolated command
- narrower route or component
- one failing request
- one data fixture

If reducing reveals the expected behavior is unspecified, route to `loom-specs`.

## Fix

Fix the root cause inside the ticket or packet scope.

If the fix requires broader behavior, migration, policy, or sequencing change,
stop and route to specs, plans, constitution, or operator decision.

## Guard

Add a guard when recurrence is plausible:

- regression test
- integration check
- browser scenario
- validation boundary
- monitoring or alert
- CI gate
- knowledge troubleshooting note after retrospective

For invalid data or unsafe operations, prefer layered guards:

- entry validation at the public boundary
- business-rule validation where the operation happens
- environment or mode guard for dangerous contexts
- diagnostic context that makes future failure cheaper to localize

For flaky asynchronous tests, replace arbitrary sleeps with condition-based waits
unless the timing itself is the behavior under test. If a timeout is genuinely part
of the behavior, document what event starts the wait and why that duration is
meaningful.

The guard should fail or alert on the original failure mode.

For regression tests, choose a seam that exercises the real bug pattern as it
occurred. If the only available seam is too shallow, record that as an architecture
finding and route to `loom-architecture-deepening` after the fix.

## Verify

Run the focused check first, then broader checks proportional to risk.

Record evidence for:

- failing before state when preserved
- passing after state
- remaining unverified areas
- known residual risk

Before declaring done, remove temporary instrumentation and throwaway debug
prototypes or route them intentionally. Search for unique debug prefixes when you
used them.

Use `loom-audit` before closure when the fix is high-risk or the evidence story is
easy to overstate.

## Prevent

Use `loom-retrospective` when the debug pass revealed:

- a repeated diagnostic path
- a missing test pattern
- a misleading spec or ticket
- a fragile interface
- a dependency or environment trap
- a useful troubleshooting record

## Done Means

The debug pass is done when:

- the failure is preserved or explicitly low-value to preserve
- reproduction and root cause are clear enough for the claim
- a reliable feedback loop or honest limitation is recorded
- the scoped fix addresses the cause, not only the symptom
- a guard exists when recurrence is plausible
- evidence supports the fixed claim
- temporary diagnostics and prototypes are cleaned up or routed intentionally
- follow-up and prevention records exist where useful
