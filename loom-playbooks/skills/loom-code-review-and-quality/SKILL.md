---
name: loom-code-review-and-quality
description: "Use when a code diff, branch, PR, worker output, or implementation-complete ticket needs a code-focused quality review across correctness, tests, architecture, security, performance, scope, and evidence before audit or closure."
---

# loom-code-review-and-quality

Code review is an audit-oriented playbook for changed source and records.

It reviews intent, tests, implementation, risk, and evidence, then routes durable
findings into `loom-audit` or the consuming ticket.

## Core Dependency

Use `loom-core` first. This playbook composes `loom-audit`, `loom-evidence`,
`loom-tickets`, `loom-specs`, `loom-ralph`, and `loom-retrospective`.

## Use This Playbook When

Use this playbook when:

- reviewing a diff, branch, pull request, or worker output
- a ticket appears implementation-complete
- another agent produced code that needs independent review
- refactor, bug fix, package, security, or performance work needs a quality gate
- closure depends on code and evidence telling the same story

## Route

Use this route:

```text
intent -> tests -> implementation -> risks -> evidence -> findings -> disposition
```

## Intent

Start from the target record:

- ticket scope and `ACC-*`
- spec `REQ-*` and `SCN-*`
- plan execution unit
- packet mission and output
- linked evidence and audit records

Name what the change claims to accomplish before reading for style.

## Tests And Evidence

Review tests and evidence before implementation when possible.

Check:

- red/green story when behavior changed
- tests match behavior rather than implementation trivia
- important edge, error, empty, permission, compatibility, and migration states are
  covered or explicitly out of scope
- manual, browser, or runtime observations support non-testable claims
- evidence limitations are visible

Create or request `loom-evidence` when the review needs durable support.

## Implementation Axes

Review across:

- correctness: matches spec, acceptance, tests, and source reality
- readability: names, control flow, comments, and local clarity
- architecture: boundaries, dependencies, conventions, and abstraction level
- security: untrusted input, auth, secrets, data exposure, injection, and external
  data
- performance: unnecessary work, N+1 patterns, unbounded fetches, hot paths,
  browser rendering, and bundle impact
- scope: unrelated cleanup, hidden behavior changes, generated churn, and follow-up
  work mixed into the change

Use specialized playbooks for deeper passes: security, performance, browser, API,
or simplification.

## Findings

Use `loom-audit` when findings or verdict should survive.

Material findings should name:

- observed issue
- file/line, record ID, evidence ID, or diff ref
- claim or boundary challenged
- risk or impact
- required follow-up

Low-severity local comments can remain in the review output when no durable record
needs them.

## Disposition

The consuming surface owns disposition.

Common routes:

- fixed in current ticket
- accepted residual risk in ticket with authority
- follow-up ticket
- spec update for behavior gap
- evidence update for proof gap
- research for source uncertainty
- constitution for durable policy or precedent
- knowledge promotion after retrospective

## Done Means

The review pass is done when:

- intent and evidence were checked before verdict
- material issues have actionable findings or explicit absence
- review scope and uninspected areas are visible
- ticket or audit records carry durable findings when needed
- consuming records decide disposition rather than the review silently closing work
