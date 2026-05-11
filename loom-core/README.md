# Agent Loom Core

Markdown-native control plane for agent software work.

Loom Core gives agents the core skills for shaping, executing, reviewing, and
preserving work through grepable Markdown records.

[Agent Loom](../README.md) / [Protocol](../PROTOCOL.md) / [Install](../INSTALL.md) / [Loom Playbooks](../loom-playbooks/README.md)

## What Core Is For

Core is the Loom package an agent needs before it can do Loom work.

It teaches the operating posture:

- load `using-loom` before Loom work
- choose the surface that fits the durable claim or task
- keep live execution state in tickets
- separate evidence from inference
- use fresh-context audit before trusting closure claims
- use packets for bounded worker handoff
- run retrospective promotion after significant work
- preserve reusable understanding in knowledge

Core is portable. Claude Code, OpenCode, Codex, Cursor, Gemini CLI, a generic
skills directory, or another harness may expose it differently. The harness is
transport. The protocol is the skills corpus.

## Core Surfaces

| Surface | Role |
| --- | --- |
| `constitution` | durable identity, principles, constraints, decisions, roadmap direction |
| `tickets` | bounded executable work, live state, acceptance, closure |
| `research` | investigations, tradeoffs, rejected paths, null results, conclusions |
| `specs` | intended behavior, requirements, scenarios, interfaces |
| `plans` | complex-change decomposition, sequencing, recovery |
| `evidence` | observed artifacts and validation output |
| `audit` | fresh-context review, findings, verdicts, residual risk |
| `knowledge` | preferences, procedures, reusable understanding, retrieval cues |
| `packets` | bounded worker contracts |

## Skills

| Skill | Role |
| --- | --- |
| `using-loom` | entry doctrine and operating posture |
| `loom-constitution` | durable judgment, constraints, decisions, roadmap direction |
| `loom-tickets` | bounded executable work and closure |
| `loom-specs` | intended behavior, requirements, scenarios, interface contracts |
| `loom-plans` | complex-change planning and sequencing |
| `loom-evidence` | durable observations and artifacts |
| `loom-research` | durable investigations and synthesis |
| `loom-audit` | fresh-context review and findings |
| `loom-knowledge` | reusable knowledge and retrieval |
| `loom-ralph` | packet mechanics and bounded worker handoff |
| `loom-retrospective` | promotion and prevention after significant work |

## Route

```text
prompt -> shape -> record -> packet -> evidence -> audit -> closure -> retrospective -> knowledge
```

Not every task needs every surface. Durable claims should land where future agents
can find, inspect, and continue them.

## Installing Or Exposing Core

Expose this directory's `skills/` tree, or expose the package root when the
harness understands package roots.

Common local surfaces:

```text
/absolute/path/to/agent-loom/loom-core
/absolute/path/to/agent-loom/loom-core/skills
```

Some harnesses also consume adapter metadata or package-plugin entrypoints around
the same skills.

Harness-specific instructions live in [INSTALL.md](../INSTALL.md).

## Boundary

Core owns the Loom bootstrap doctrine and canonical core skills.

Core is not a runtime, service, daemon, MCP server, product CLI, hidden database,
or prompt dump. It is a Markdown-native skill corpus.

Optional workflow routes live in [Loom Playbooks](../loom-playbooks/README.md).
Playbooks depend on Core; Core owns the graph those workflows route through.
