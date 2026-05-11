# Agent Loom Playbooks

Workflow paperwork for coding agents.

Agent Loom gives coding agents a graph of shaped work products. Playbooks help agents move through that graph when a task has a recognizable workflow shape: debug this, review this, migrate this safely, verify this UI, ground this in current docs, simplify this without changing behavior, prepare this for release.

Playbooks are optional. They do not replace [Loom Core](../loom-core/README.md).

Core gives the record surfaces. Playbooks give practiced routes through them.

[Agent Loom](../README.md) / [Protocol](../PROTOCOL.md) / [Install](../INSTALL.md) / [Loom Core](../loom-core/README.md)

## Why Playbooks Exist

Many agent workflows are useful but easy to let disappear into chat.

An agent can debug by poking around, but never preserve the reproduction. It can review a diff, but leave findings as transient comments. It can prepare a release note, but accidentally overstate what the ticket accepted. It can run a migration, but skip usage proof and cleanup evidence. It can polish a UI, but leave no browser observation behind.

The workflow happened.

The work products did not compound.

Playbooks add workflow-specific pressure while routing durable facts back to Core
records.

```text
workflow route, not durable record
```

A playbook can guide how the agent works. Durable project facts still belong in
Core records.

## What They Add

Playbooks are for recurring engineering shapes that need more than generic routing.

They help agents remember to:

- reproduce before fixing
- write or observe a failing check before claiming behavior changed
- measure before optimizing
- isolate Git scope before parallel work
- preserve review findings in audit
- route security-sensitive work through threat-aware review
- keep migration cleanup tied to evidence and ticket disposition
- verify UI changes in the browser when runtime behavior matters
- ground framework or library choices in current source and official docs
- make docs, release notes, and PR summaries mirror Core records instead of
  inventing claims

Playbooks make the workflow path explicit, repeatable, and recoverable.

## The Playbook Set

The list is workflow-oriented. These are not new record layers.

- `loom-idea-refine` - turns rough concepts into the next core record move
- `loom-incremental-implementation` - executes bounded slices through tickets,
  Ralph, evidence, and audit
- `loom-test-driven-development` - applies test-first verification and preserves
  red/green evidence
- `loom-source-driven-development` - grounds framework and library work in current
  sources, research, and evidence
- `loom-doubt-driven-development` - challenges non-trivial in-flight claims through
  Ralph, audit, evidence, and follow-up routing
- `loom-domain-language-and-decisions` - sharpens project vocabulary and routes
  real tradeoffs to constitution decisions
- `loom-codebase-atlas` - maps unfamiliar code areas into reusable knowledge
- `loom-architecture-deepening` - finds higher-leverage module seams, interfaces,
  and refactor routes
- `loom-frontend-ui-engineering` - routes UI behavior, accessibility, visual
  quality, browser observations, and audit
- `loom-api-and-interface-design` - designs shared interfaces through specs,
  compatibility checks, evidence, and audit
- `loom-browser-testing-with-devtools` - captures browser runtime observations as
  evidence
- `loom-debugging-and-error-recovery` - preserves failures, finds root cause, fixes,
  guards, and runs prevention follow-up
- `loom-prototype-and-spike` - builds disposable artifacts to answer design,
  logic, UI, interface, or integration questions
- `loom-intake-triage` - classifies incoming reports and routes them to tickets,
  evidence, specs, knowledge, or rejection rationale
- `loom-git-workspace-isolation` - isolates branch or worktree execution and
  records baseline provenance
- `loom-parallel-worker-coordination` - dispatches independent Ralph packets and
  reconciles combined output
- `loom-code-review-and-quality` - reviews diffs as an audit-oriented quality route
- `loom-review-response` - evaluates and acts on incoming review feedback
- `loom-code-simplification` - simplifies code while preserving behavior and
  evidence
- `loom-security-and-hardening` - routes security-sensitive work through specs,
  evidence, audit, and prevention
- `loom-performance-optimization` - measures, optimizes, remeasures, and records
  performance evidence
- `loom-ci-cd-and-automation` - specifies and verifies CI/CD gates and deployment
  automation
- `loom-deprecation-and-migration` - plans and executes migrations, deprecations,
  proof, cleanup, and prevention
- `loom-branch-finish` - finishes development branches through merge, PR, keep,
  discard, and cleanup decisions
- `loom-shipping-and-launch` - coordinates readiness, rollout, observation,
  rollback, communication, and cleanup

## How They Stay Loom

Every playbook routes durable facts back to Core.

- debugging may create evidence, research, a spec update, a ticket, audit, or
  knowledge promotion
- domain language may create knowledge, specs, tickets, or constitution decisions,
  but conversation does not become the durable record
- architecture deepening may create plans, specs, tickets, evidence, and audit, but
  refactor execution still closes through tickets
- intake triage may mirror external issue state, but tickets remain the live
  execution ledger
- code review may create audit findings, but the ticket owns finding disposition
  and acceptance
- review response may update tickets, audit, specs, evidence, research,
  constitution, or knowledge, but feedback itself is not authority
- Git coordination may protect branches and worktrees, but the ticket still owns live execution state
- docs sync may update README files, but Core records still carry decisions,
  behavior, evidence, risk, and accepted explanation
- ship may draft summaries, but the ticket and evidence decide what can honestly be claimed

This keeps workflows from becoming competing ledgers.

The playbook is the route. Core records carry the durable result.

## Installing Or Exposing Playbooks

Install or expose Loom Core first. Playbooks expect Core to supply `using-loom`,
record grammar, packet discipline, evidence, audit, knowledge, and ticket
acceptance rules.

The portable local setup exposes both package roots or both skill trees:

```text
/absolute/path/to/agent-loom/loom-core
/absolute/path/to/agent-loom/loom-playbooks
/absolute/path/to/agent-loom/loom-core/skills
/absolute/path/to/agent-loom/loom-playbooks/skills
```

Some harnesses also consume adapter metadata or the JavaScript package-plugin entrypoint in this directory. Those are transport surfaces around the same skills.

Harness-specific instructions live in [INSTALL.md](../INSTALL.md).

## Boundary

Playbooks are not a second protocol, not a workflow engine, and not a replacement
for tickets, evidence, audit, specs, research, plans, knowledge, or constitution.

They are reusable workflow routes for coding agents.

Use Core when the next record move is obvious. Add Playbooks when the workflow
itself needs structure.

The workflow is disposable. Core records are not.
