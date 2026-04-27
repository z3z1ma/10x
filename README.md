# Loom

Loom is a Markdown-native project state protocol for AI agents.

It exists because long-running AI work needs somewhere to live that is not a chat.

The code changes. The transcript knows why. Then the session ends, the context fills up, compacts, or a new worker starts cold.

Loom puts that work in the repo.

It treats the filesystem as the interface, Markdown as the durable medium, and fresh-context packets as the default way to delegate bounded implementation. It is harness-agnostic. Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and local agents can all operate the same graph if they can read skills, edit files, and use ordinary shell tools.

This package is intentionally **not** a runtime, service, daemon, MCP server, or product CLI.

It ships:

- a mandatory `loom-bootstrap` skill with ordered doctrine references that teach the model how Loom thinks and how Loom must be used
- on-demand `skills/` that teach the model how to operate each subsystem in detail
- Markdown templates and query recipes instead of bundled Python helpers
- a cohesive explanation layer: **Loom Wiki**

Read `PROTOCOL.md` for the stable protocol summary.

Loom is best understood as a source-of-truth type system plus a transaction protocol for fallible AI workers.

The workers are disposable. The graph is durable. The parent is the transaction coordinator.

---

## The idea

None of the pieces in Loom are new.

Teams already write specs, plans, tickets, docs, and research notes. They run experiments. They collect evidence. They review changes. They write down decisions. They try things, reject them, and learn.

AI workflows added more pieces: prompts, scratchpads, memory files, context management, cleaner execution loops, and bounded subagents.

The problem is not missing ideas.

The problem is that they are scattered.

Loom weaves them back together and gives each one a job.

Once those jobs exist, workflows emerge from the structure. Debugging, planning, reviewing, shipping, repair, retrospective, wiki synthesis, and bounded implementation all become routes through the same graph instead of separate systems with separate hidden state.

That is the point of Loom: the project gets a vocabulary for where work belongs.

---

## The core shape

Loom has three operating axes:

- **layers**: typed owners for different kinds of truth
- **loops**: outer-loop shaping and inner-loop execution
- **packets**: bounded contracts for fresh-context work

A Loom transaction uses a small set of kernel roles:

- owners
- claims
- packets
- evidence
- critique
- acceptance disposition
- promotion

The layer model is the type system. Canonical owner layers own project truth. Support surfaces help recovery and handoff without becoming truth owners.

| Layer | Owns |
| --- | --- |
| constitution | durable identity, principles, hard constraints, precedent |
| initiative | strategic outcome |
| research | evidence synthesis, investigations, options, rejected paths, null results |
| spec | intended behavior and acceptance contract |
| plan | sequencing and rollout strategy |
| ticket | live execution state, scoped execution, acceptance disposition |
| evidence | observed artifacts |
| critique | adversarial findings and verdicts |
| wiki | accepted explanation |
| packet | bounded child-worker contract, not project truth |
| memory | optional support context only |

The rule that keeps the graph coherent is simple:

**truth ownership is by layer, not by recency.**

For software work, the source tree owns current implementation reality. Git owns file history. Specs own reusable intended behavior and acceptance contracts. Tickets own scoped execution, ticket-local criteria when no spec exists, and acceptance disposition. Evidence bridges implementation to claims. Critique judges whether the bridge is strong enough. Wiki holds the explanation that has become safe to reuse.

Memory can help the agent recover context. It does not own truth.

---

## What changes

The agent stops treating the transcript as the workspace.

Instead, it routes uncertainty:

- missing understanding routes to research
- unclear behavior routes to spec
- unclear sequencing routes to plan
- live work routes to ticket
- observed output routes to evidence
- concerns route to critique
- stable understanding routes to wiki
- bounded execution routes through packets
- support recall can live in memory until it needs promotion

The agent stops accumulating context.

It starts placing truth.

That changes how long-running work behaves. The next worker does not need to inherit a swollen transcript. It needs the graph, the relevant records, and a bounded contract for the next step.

---

## The two loops

Loom work moves through two loops.

The outer loop scopes and re-scopes the work. It decides which owner layer needs to change next.

The inner loop executes bounded work with a clean context window.

These loops are separate on purpose. Shaping work and doing work are different jobs.

### Outer loop

The outer loop asks what kind of problem the agent is solving.

Its backbone progression is:

```text
constitution -> initiative -> plan -> ticket
````

Use conditional gates before plan or ticket:

* route to research when evidence synthesis, tradeoffs, options, conclusions, or null results are missing
* route to spec when intended behavior or acceptance criteria are fuzzy
* route to plan when sequencing, rollout, dependency ordering, or staged execution is unclear
* route to ticket when work is scoped enough to execute

This keeps the agent from advancing on vibes.

If a step cannot be completed honestly, route backward to the owner that can fix the gap.

### Inner loop

The inner loop is Ralph.

In Loom, Ralph means:

```text
one bounded packet
one fresh worker
one iteration
one reconciliation pass
```

A parent agent compiles a packet, launches or delegates one fresh-context execution step, receives a bounded outcome, and merges truth back into the graph.

The child does one slice of work.

The parent decides what became true.

Critique and wiki work may reuse packet discipline, but their domain workflows own review and synthesis. They are sibling routes, not Ralph-governed implementation.

The deeper invariant is ownership-preserving mutation: every durable claim, behavior, evidence artifact, risk, and explanation lands in the artifact that owns that kind of truth.

---

## Packets

Packets create clean work.

They define:

* the task
* what the worker can read
* what the worker can write
* how to verify
* when to stop
* what the worker must return

They prevent context drift, hidden assumptions, uncontrolled changes, and accidental expansion of scope.

A packet is a contract.

It is not project truth.

The packet gives the child enough context to do one bounded job. After the child returns, the parent reconciles the result into tickets, evidence, critique, research, specs, plans, or wiki as needed.

---

## Transaction spine

Every non-trivial Loom transaction follows the same spine:

```text
route -> shape -> ready -> execute -> reconcile -> verify -> accept -> promote -> close
```

A transaction does not need to touch every layer. It does need to preserve ownership.

For example, a bug fix might move like this:

1. Route to research to reproduce and understand the failure.
2. Route to spec if the correct behavior is unclear.
3. Create or update a ticket for execution.
4. Compile a packet for one bounded implementation pass.
5. Run a fresh worker.
6. Record evidence from tests, logs, or inspection.
7. Route critique if the change needs pressure-testing.
8. Accept only when the ticket reflects reality.
9. Promote durable learning into research or wiki.
10. Close when the graph is consistent.

That is Loom.

---

## When work is done

Work is not done when code compiles.

It is done when the project is consistent.

For software work, closure usually requires:

* the relevant spec is satisfied, or the ticket-local acceptance criteria are explicit
* evidence supports the claim being made
* critique is resolved, accepted, or recorded as residual risk
* the ticket reflects the actual final state
* durable learning has been promoted to research or wiki when it should survive the task

“Done” is a property of the graph, not a moment in time.

A child worker saying “done” is not enough.

A commit is not enough.

The graph has to tell the truth.

---

## Research matters

A lot of software work is knowledge work before it is code.

Agents explore libraries, inspect implementation paths, test approaches, compare options, discover constraints, and learn that something does not work.

If that stays in chat, it gets lost.

Research gives that work a place to live:

* explored options
* rejected approaches
* experiments
* null results
* supporting evidence
* open questions
* recommendations grounded in evidence

This is where Loom crosses from coding workflow into knowledge-work protocol.

A failed path is often valuable. A rejected option can prevent the next worker from repeating the same mistake. A null result can be the most important thing the project learned that hour.

Research keeps that work from resetting every session.

---

## Why this works

Most systems define workflows.

Loom defines the pieces those workflows are made from.

Workflows such as brainstorm, debug, spike, sketch, map, Git-backed isolation, review, accept, ship, retrospective, repair, and wiki write or audit are compositions through the owner layers. They should not create new truth owners unless a genuinely new kind of truth exists.

Examples:

```text
debug:
research -> evidence -> ticket -> critique -> wiki if durable learning survives

spike:
research -> evidence -> plan or spec

review:
critique -> evidence -> ticket reconciliation

implementation:
ticket -> packet -> worker -> evidence -> reconcile

release:
ticket acceptance -> evidence -> critique if needed -> wiki or retrospective

repair:
evidence -> critique -> ticket -> packet -> evidence -> accept
```

You do not invent a new workflow every time.

You follow the structure.

---

## Markdown, on purpose

Loom is Markdown-native.

No service. No daemon. No hidden runtime database.

The graph is files.

Agents already know how to:

* search with `grep` or `rg`
* traverse with `find`
* inspect with `cat`
* compare with `git diff`
* edit records
* move files
* version with `git`
* compose shell tools

That is enough.

Optional utilities may validate, project, or summarize state. They do not own Loom semantics.

Harness adapters may preload `loom-bootstrap` references where the harness supports it cleanly. That is an adapter optimization over the same skill package, not a separate doctrine source.

The protocol is the corpus.

---

## Repository layout

```text
.
├── README.md
├── PROTOCOL.md
├── ARCHITECTURE.md
├── AGENTS.md
├── examples/         # golden protocol fixtures and traces, not truth owners
├── optional-utilities/
└── skills/
```

Expose the frontmatter `name` and `description` from each `skills/*/SKILL.md`.

Agents must use `skills/loom-bootstrap` first unless its ordered bootstrap references are already loaded in the current context by a harness adapter. Then hydrate the task-specific skill when relevant.

Inside a Loom-enabled project, the canonical runtime tree is expected to look roughly like this:

```text
.loom/
├── constitution/
│   ├── constitution.md
│   ├── decisions/
│   └── roadmap/
├── initiatives/
├── research/
├── specs/
├── plans/
├── tickets/
├── evidence/
├── critique/
├── wiki/
├── packets/
│   ├── ralph/
│   ├── critique/
│   └── wiki/
└── memory/        # optional
```

Use `skills/loom-workspace`, `skills/loom-constitution`, and `skills/loom-tickets` for the first records.

---

## Installation model

Loom installs as a skills package.

The product surface is `skills/`. Native harness adapters may add metadata, manifests, or preload hooks around that directory, but they do not add a second Loom ontology and they do not replace the skills.

The intended installation pattern is:

1. install or expose `skills/` as the Loom package
2. keep skill names and descriptions from `skills/*/SKILL.md` visible
3. use `skills/loom-bootstrap` first unless the same ordered doctrine is already loaded by the adapter
4. hydrate the full `skills/<name>/SKILL.md` only when that skill is relevant
5. let the model read templates and references from that skill as needed

### Required loading model

The `loom-bootstrap` skill is mandatory. Agents should use it before starting any work unless the same ordered bootstrap doctrine is already loaded in the current context by a native adapter.

`loom-bootstrap` reads these references in order:

1. `skills/loom-bootstrap/references/01-core-identity.md`
2. `skills/loom-bootstrap/references/02-truth-and-authority.md`
3. `skills/loom-bootstrap/references/03-outer-loop.md`
4. `skills/loom-bootstrap/references/04-ralph-inner-loop.md`
5. `skills/loom-bootstrap/references/05-critique-and-wiki.md`
6. `skills/loom-bootstrap/references/06-filesystem-and-tooling.md`
7. `skills/loom-bootstrap/references/07-validation-and-honesty.md`

When a harness has an `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, user rules, or a similar instruction surface, point it at the skill rather than copying doctrine:

```md
Loom is active in this workspace. Before any work, use the `loom-bootstrap` skill unless Loom's ordered bootstrap doctrine is already loaded in the current context. After bootstrap, route work through the Loom skill that owns the next truth change.
```

That instruction is a pointer, not a new source of truth.

### Native harness installs

Use the native package system for each harness.

| Harness     | Native path                                     | Loom surface                                                                     |
| ----------- | ----------------------------------------------- | -------------------------------------------------------------------------------- |
| Claude Code | Claude plugin manifest and marketplace metadata | `skills/`, plus optional `SessionStart` preload from `loom-bootstrap` references |
| Codex       | Codex plugin manifest and marketplace metadata  | `skills/` with `loom-bootstrap` as the required entry skill                      |
| OpenCode    | `open-loom` plugin                              | `skills/`, plus OpenCode `instructions` preload from `loom-bootstrap` references |
| Cursor      | Cursor plugin/skill package                     | `skills/` with `loom-bootstrap` as the required entry skill                      |
| Gemini CLI  | Gemini extension/skill package                  | `skills/` with `loom-bootstrap` as the required entry skill                      |

There is no supported Makefile, shell installer, or cross-harness fallback copy script. Older generated installs should be treated as legacy local state and cleaned up manually if they are still present.

### Quick install commands

| Harness     | Command                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| Claude Code | `claude plugin marketplace add z3z1ma/agent-loom && claude plugin install loom@agent-loom --scope user`                     |
| OpenCode    | `opencode plugin open-loom --global`                                                                                        |
| Codex       | `codex plugin marketplace add z3z1ma/agent-loom`                                                                            |
| Cursor      | `mkdir -p ~/.cursor/plugins/local && git clone https://github.com/z3z1ma/agent-loom.git ~/.cursor/plugins/local/agent-loom` |
| Gemini CLI  | `gemini extensions install https://github.com/z3z1ma/agent-loom`                                                            |

Codex currently requires opening `/plugins` after marketplace registration to install or enable `loom`.

Cursor's command above uses Cursor's native local plugin directory until `agent-loom` is listed in Cursor Marketplace. After listing, the Cursor Agent chat command should be:

```text
/add-plugin agent-loom
```

---

## Harness notes

### Claude Code

This repository includes a Claude Code plugin manifest at `.claude-plugin/plugin.json` and a local marketplace catalog at `.claude-plugin/marketplace.json`.

The plugin exposes canonical `skills/` directly from the repository root and declares `claude-hooks/hooks.json` as its Claude hook config. Loom uses that hook surface to emit the ordered `loom-bootstrap` references as same-session `SessionStart` hook stdout.

Local development:

```bash
claude --plugin-dir /absolute/path/to/agent-loom
```

Local marketplace testing:

```bash
claude plugin marketplace add /absolute/path/to/agent-loom
claude plugin install loom@agent-loom --scope project
```

Remote install:

```bash
claude plugin marketplace add z3z1ma/agent-loom && claude plugin install loom@agent-loom --scope user
```

Validate the local plugin structure with:

```bash
claude plugin validate /absolute/path/to/agent-loom
```

The hook preload is a bonus. The canonical surface remains `skills/`, especially `skills/loom-bootstrap`.

### Codex

This repository includes a Codex plugin manifest at `.codex-plugin/plugin.json` and a marketplace catalog at `.agents/plugins/marketplace.json`. The plugin exposes canonical `skills/` directly from the repository root and is shaped for a Git-backed remote marketplace entry.

The target native remote path is Codex marketplace registration with the repository URL:

```bash
codex plugin marketplace add z3z1ma/agent-loom
```

Once installed plugin skill discovery is validated, users should be able to open Codex's `/plugins` browser and install or enable `loom` from the `agent-loom` marketplace.

Current evidence still needs installed plugin skill-discovery validation for `loom-bootstrap`, so this is not yet a broadly accepted Codex release path. The repository `.codex/` hook fixture proves optional trusted project preload of bootstrap references. It is not the product install path.

### OpenCode

This repository includes the `open-loom` OpenCode plugin at `open-loom.mjs`.

`open-loom` requires OpenCode `>=1.14.22 <2`.

Normal users can install the OpenCode plugin and update global config with:

```bash
opencode plugin open-loom --global
```

Equivalent package plugin entry:

```json
{
  "plugin": ["open-loom"]
}
```

Users working from a cloned repository should point OpenCode at the local plugin file instead:

```json
{
  "plugin": ["file:///absolute/path/to/agent-loom/open-loom.mjs"]
}
```

`open-loom` registers the bundled skill root with `config.skills.paths` and adds ordered `loom-bootstrap` references to `config.instructions`.

For a local structural check that does not require a model request, run:

```bash
node open-loom.mjs --smoke
```

### Cursor

This repository includes a Cursor plugin manifest at `.cursor-plugin/plugin.json`.

The manifest follows Cursor's native plugin format and exposes canonical `skills/` with `"skills": "./skills/"`.

Until `agent-loom` is listed in Cursor Marketplace, install from the Git repository as a local native Cursor plugin:

```bash
mkdir -p ~/.cursor/plugins/local && git clone https://github.com/z3z1ma/agent-loom.git ~/.cursor/plugins/local/agent-loom
```

Restart Cursor or run Developer: Reload Window after cloning.

Once the Marketplace listing exists, install from Cursor Agent chat with:

```text
/add-plugin agent-loom
```

### Gemini CLI

This repository includes a Gemini CLI extension manifest at `gemini-extension.json`.

The extension exposes canonical `skills/` and uses `contextFileName` to load `gemini-bootstrap.md`, which imports the ordered `skills/loom-bootstrap/references/*.md` files with Gemini's native context import syntax.

Install from the Git repository with:

```bash
gemini extensions install https://github.com/z3z1ma/agent-loom
```

Local development can link the repository instead:

```bash
gemini extensions link /absolute/path/to/agent-loom
```

Validate the local extension structure with:

```bash
gemini extensions validate /absolute/path/to/agent-loom
```

The context preload is a bonus. The canonical surface remains `skills/`, especially `skills/loom-bootstrap`.

---

## What Loom is

Loom is a way to keep AI work from dissolving into conversation.

It gives agents a vocabulary for placing work where it belongs.

It gives projects a memory that survives context windows, compaction, worker handoff, and time.

It is a project-state protocol for long-horizon AI knowledge work.

---

## What Loom is not

Loom is not a replacement for your codebase.

It is not a replacement for Git.

It is not a runtime, service, daemon, MCP server, product CLI, workflow engine, or prompt system.

It does not ask every task to use every layer.

It makes sure meaningful work has somewhere honest to go.

For small edits, skip the graph.

For long-running work, the graph prevents collapse.

---

## The point

The pieces already existed.

Loom puts them in one place and gives each one a job.

Once that happens:

```text
the work stops drifting
the agent stops carrying everything
the project starts remembering
```
