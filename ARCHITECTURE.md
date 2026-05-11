# Architecture Notes

Loom is a Markdown-native control plane for AI knowledge work.

It ships skills, references, and templates. It does not ship a hidden runtime,
daemon, database, dashboard, model router, MCP server, product CLI, or required
helper script.

## Product Surface

The product surface is split into two package roots:

| Package | Role |
| --- | --- |
| `loom-core/` | mandatory operating doctrine and core record skills |
| `loom-playbooks/` | optional workflow routes that require Core |

The durable product asset is the Markdown corpus inside each package's `skills/`
tree. Package entrypoints, native manifests, hooks, and extension files are
transport surfaces around that corpus.

## Core Invariant

Loom has one central invariant: records carry durable work, and tickets carry live
execution state.

Newer files do not win by recency. Longer files do not win by confidence. A claim
belongs where the relevant Core skill says it belongs.

## Core Graph

Core provides these record surfaces:

- constitution for durable identity, constraints, decisions, and roadmap direction
- tickets for bounded executable work, live state, acceptance, and closure
- research for investigations, tradeoffs, rejected paths, null results, and conclusions
- specs for intended behavior, requirements, scenarios, and interfaces
- plans for complex-change decomposition, sequencing, and recovery
- evidence for observed artifacts and validation output
- audit for fresh-context review, findings, verdicts, and residual risk
- knowledge for preferences, procedures, reusable understanding, and retrieval cues
- packets for bounded worker contracts

Retrospective is a workflow over those surfaces, not a separate record kind.

## Transaction Spine

The common spine is:

```text
shape -> ticket -> execute -> evidence -> audit -> accept -> close -> retrospective
```

The spine is not ceremony. It is the recovery path when an agent needs to prove
that work was shaped, executed, verified, reviewed, accepted, and preserved without
depending on chat history.

## Ralph And Packets

Ralph is the bounded fresh-context handoff loop.

Packets are explicit Markdown contracts. They declare:

- mission
- governing records
- source fingerprint
- read scope and write scope
- verification posture
- stop conditions
- expected output
- child output
- parent reconciliation notes

A packet is not project state, not acceptance, and not a transcript dump. It is the
contract that lets a disposable worker mutate a narrow slice without guessing.

## Evidence, Audit, Acceptance

Evidence stores observations. It can support or challenge claims, but it does not
own intended behavior, sequencing, live execution state, review verdicts, or
accepted explanation.

Audit pressure-tests claims, implementation shape, and evidence sufficiency. It
produces findings and verdicts, but it does not close work.

Acceptance disposition belongs to the ticket. Commands, commits, packets, PRs,
evidence, audit records, and child workers may inform acceptance, but the ticket
records whether scoped work may close.

## Promotion

Retrospective is the default promotion gate for significant completed work.

It routes durable learning to the surface that can maintain it:

- accepted explanation, procedures, preferences, and retrieval cues -> knowledge
- investigation results -> research
- intended behavior clarifications -> specs
- changed sequencing or recovery strategy -> plans
- principles, constraints, decisions, and roadmap direction -> constitution
- observed validation artifacts -> evidence
- prevention follow-up -> tickets

Retrospective is not a second ledger.

## Playbooks

Playbooks are reusable workflow routes, not new record surfaces.

They make common engineering paths explicit: idea refinement, incremental
implementation, TDD, source-driven work, doubt checks, UI engineering, browser
testing, API design, debugging, domain language, codebase atlases, architecture
deepening, prototyping, intake triage, Git isolation, parallel workers, code
review, review response, simplification, security, performance, CI/CD, migration,
branch finish, and launch.

Every playbook must route durable facts back to Core records.

## Native Adapters

Loom adapters may expose skills through OpenCode, Claude Code, Codex, Cursor,
Gemini CLI, or another harness.

Adapters may preload `using-loom` when the harness supports it cleanly. Preload is
an optimization over the same skill files, not a separate doctrine source.

## Examples And Dogfood

`examples/` contains internal fixtures for maintainer review. `.loom/` contains
dogfood records for this repository. Neither replaces the product surface in
`loom-core/skills` and `loom-playbooks/skills`.

## Design Biases

Loom optimizes for:

- legibility to a fresh agent
- bounded execution
- grep-friendly traceability
- evidence-backed completion
- fresh-context review
- knowledge compounding
- portability across harnesses

Loom rejects:

- hidden runtimes as the real protocol
- helper scripts as a second ontology
- one-command project management as protocol core
- generated context files as independent ledgers
- external trackers as owners of Loom state
- transcript memory as the execution record

A future agent should be able to install the skill package, load `using-loom`, read
the graph, and operate Loom without hidden runtime magic.
