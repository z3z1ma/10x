# Architecture

Loom is boring by design.

The product is a Markdown skill corpus. The runtime state is Markdown under
`.loom/`. Package entrypoints, manifests, hooks, and extensions expose the corpus
to different harnesses. They do not own the protocol.

Loom ships no hidden runtime, daemon, database, dashboard, required helper script,
or product CLI.

## Product Boundary

The product surface lives in two package roots:

| Package | Job |
| --- | --- |
| `loom-core/` | mandatory `using-loom` doctrine, record skills, and optional named agents |
| `loom-playbooks/` | optional explicit workflow macros or explicit-only skills that assume the required package is installed |

Core skills, Playbook skills, and intentionally shipped agent prompt surfaces are
the source of behavior. Core skills live under `loom-core/skills/`; Playbook
skills live under `loom-playbooks/playbooks/`. The package root may add transport
files for OpenCode, Claude Code, Codex, Cursor, or Gemini CLI.

Content inside package skill corpora and agent prompt surfaces must stay
self-contained. Use generic `.loom/...` runtime paths. Do not teach
source-repo-only assumptions from this repository as Loom doctrine.

## Runtime State

A Loom workspace materializes records only when it needs them:

```text
.loom/
|-- constitution/
|   |-- constitution.md
|   |-- decisions/
|   `-- roadmap/
|-- tickets/
|-- research/
|   `-- artifacts/
|-- specs/
|-- plans/
|-- evidence/
|   `-- artifacts/
|-- audit/
`-- knowledge/
```

Missing empty directories are fine. A directory matters when the current work
needs that surface.

## Core Surfaces

Each surface owns one kind of truth.

| Surface | Runtime Path | Owns |
| --- | --- | --- |
| constitution | `.loom/constitution/` | durable judgment, policy, principles, constraints, ADRs, roadmap direction |
| tickets | `.loom/tickets/` | bounded executable work, live state, acceptance, closure |
| research | `.loom/research/` | investigations, tradeoffs, rejected paths, null results, conclusions |
| specs | `.loom/specs/` | intended behavior, requirements, scenarios, interfaces |
| plans | `.loom/plans/` | strategy and decomposition for complex work |
| evidence | `.loom/evidence/` | observations, outputs, reproductions, screenshots, logs, validation |
| audit | `.loom/audit/` | Ralph-backed review, findings, verdicts, residual risk |
| knowledge | `.loom/knowledge/` | preferences, procedures, accepted explanation, atlases, retrieval cues |

Retrospective is a promotion and prevention pass over existing surfaces. It has no
record directory of its own.

## Bootstrap

`using-loom` is mandatory before Loom work unless the adapter has already loaded
the same Core session kernel with clear source markers. Adapter preload is
convenience and transport; if preload is absent, the agent loads `using-loom` from
Core.

Preload alone is not the behavior. Core owns the first-action routing loop that
checks likely Loom surfaces and skills before questions, inspection, edits,
tickets, or Ralph when Loom may apply. Playbook package checks verify explicit
macro registration rather than natural-prompt autoactivation.

## Record Grammar

Skills use frontmatter because harnesses expect it. Loom records use grepable body
labels because humans and future agents can inspect and repair them without a
parser.

```text
ID: <typed-id>
Type: <record type>
Status: <status>
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
```

Templates stay small. They force the agent to name scope, evidence, risks,
acceptance, and links without turning Markdown into a hidden schema engine.

## The Two Loops

The outer loop shapes work with the operator. The agent inspects first, asks only
material questions, and routes durable truth to the surface that owns it. Work
stays in this loop while intent, scope, evidence, risk, or authority is unclear.

That gate is mandatory. A fuzzy ask must not become a ticket, worker run, or patch
until the missing outcome, boundary, constraints, evidence posture, non-goals,
system-shape, data-model or state implications, and design-coherence questions are
shaped with the operator or the owning Loom surface.

Record skills own Loom surfaces and their procedures. Playbooks run inside this
architecture as explicit workflow lenses: they add guidance after Loom routing has
identified the owning surface and whether the work is shaped enough to execute, or
after the operator deliberately invokes the Playbook. Ordinary natural prompts
should not auto-load Playbooks. When a workflow lens routes to another Loom skill,
the target skill's procedure and guidance still apply completely.

The inner loop executes bounded work. Tickets drive live execution state and carry
durable worker or review context. Ralph names the bounded worker and review
discipline. Evidence records what happened. Audit records adversarial review
returned from bounded Ralph review runs. The parent reconciles the result into the
owning surfaces.

This split is the core architecture. Coding harnesses can add transport, but they
should not replace the outer-loop shaping or the inner-loop contract.

## Ralph And Audit

Tickets are the durable contracts for one bounded worker or review run. They name
target, mission, linked records, read scope, write scope, constraints, stop
conditions, evidence or review expectations, and output reconciliation target.

Ralph is the discipline for running that bounded worker or review. The launch
prompt is transient transport: it points at the ticket or review target, states the
immediate objective, and asks for structured output. It is not a durable truth
surface.

After the worker returns, the parent reads the worker output, diffs, records, and
evidence, then updates the consuming ticket, evidence, audit, or knowledge surface
as appropriate.

Substantive audit requires a bounded Ralph review run. The same session can
prepare the audit request and record the result, but the adversarial judgment must
come from the Ralph review worker. Local inspection may help, but it should not be
saved as `Type: Audit`.

## Adapter Rule

Adapters may preload doctrine, expose skills, validate package shape, or make
installation easier. They must not define another ontology.

Generated context files, external issue trackers, dashboards, MCPs, and local
scripts may transport or mirror Loom work. The owning truth still lives in Loom
records unless a future constitutional record changes that boundary.

## Repository-Only Material

This repo has support material that is not product doctrine:

- `examples/` contains internal fixtures and traces for maintainer review
- `.loom/` contains dogfood records for this repo
- `.opencode/` is a local consumption surface

Use those for review or dogfooding. Keep product behavior in `loom-core/skills`,
`loom-core/agents`, `loom-core/codex/agents`, and `loom-playbooks/playbooks`.

## Design Checks

A Loom change should preserve these properties:

- a future agent can find the right record with filenames, IDs, labels, and grep
- tickets remain the only live execution ledger
- evidence records observations without deciding acceptance
- audit records review without closing work
- Ralph bounds worker and review runs while tickets own durable execution state
- knowledge stores accepted reusable understanding without replacing specs, evidence, audit, or tickets
- workflow-specific skills route through Loom surfaces instead of adding durable surfaces
- helper code stays derivative of the Markdown protocol
