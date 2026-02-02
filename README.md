# Loom

**An agent-native operating system for terminal-first AI development.**

Loom exists because agent work deserves permanence.

Most tools treat agents like chat sessions: momentary, stateless, disposable. Useful in bursts, then gone. Decisions evaporate. Context collapses. The same mistakes repeat with uncanny consistency.

Loom asks a different question.

What if agent work could *accumulate*? What if intent survived past a single run? What if learning left a trace you could open, inspect, argue with, and reuse?

> Loom turns a Git repository into a place where agents can think, remember, coordinate, and try again.

It does this without magic or metaphors. Just files. Folders. Worktrees. Unix primitives that hold up under stress.

---

## What Loom is really about

A lot of agent tooling focuses on novelty. Loom focuses on consequences.

When work matters, you eventually need to answer questions like:

* Why did this change happen?
* What alternatives were already tried?
* What broke last time?
* Where did we leave off?

Most systems cannot answer these questions reliably, because they were never designed to. Loom can, because it preserves the *shape of the work itself*.

Loom gives agents:

* A place to express intent
* A structure to reason within
* A memory that persists
* A way to compound skill over time

And it gives humans visibility. Everything agents do leaves behind artifacts you can read, diff, and trust.

---

## One agent is enough

Loom is valuable even when you are running a single agent.

In its simplest form, Loom is a serious CLI for thoughtful agentic work:

* Intent lives in Markdown tickets
* Work happens in isolated worktrees
* Memory persists across runs
* Errors fail forward instead of stopping you cold

You get many of the same benefits that motivated systems like Beads: agents reason better when work is local, document-shaped, and inspectable.

No scrollback archaeology. No fragile prompt chains. No hallucinated state.

Just one agent, a clear goal, and a system that remembers what happened.

Everything else Loom offers builds on this foundation.

---

## When the work grows

As work stretches across time, complexity increases naturally.

Goals fracture. Dependencies emerge. Parallelism becomes tempting and dangerous.

This is where Loom’s **team** layer appears.

A team is not a metaphor. It is an operational construct:

* A tmux session
* A shared inbox
* Explicit claims on tickets
* State written to disk

Teams can be started, paused, resumed, and inspected like any other process. Nothing is hidden. Nothing disappears.

Teams exist to make long-horizon work boring again.

---

## Why everything is files

Loom is aggressively file-backed by design.

Files have properties that both humans and agents exploit well:

* They are visible
* They are durable
* They can be versioned
* They fail loudly and honestly

Every Loom subsystem leaves behind artifacts you can open with a text editor. This is not logging. It is evidence.

When something goes wrong, you can trace it. When something goes right, you can reuse it.

---

## The system, piece by piece

Loom is composed of five subsystems and one optional server. Each does one job and leaves a footprint.

### Tickets (`.tickets/`)

Markdown documents with YAML frontmatter. They express intent, dependencies, and ownership. Agents reason over them directly.

### Teams (`.team/`)

Tmux-native orchestration with run state stored as JSON. Teams are visible, pausable, and inspectable.

### Memory (`.memory/`)

Markdown notes with frontmatter. Associative, human-readable, and agent-searchable. SQLite exists only as a derived cache.

### Workspace (`workspace.json`, `.loom/`, `.loom-repo/`)

Worktrees, snapshots, and multi-repo layouts. Isolation is the default, not a suggestion.

### Compound (`.opencode/`)

Where learning lives. Observations become procedures. Procedures become reusable skills.

### Server (`loom server`)

A lightweight HTTP API for dashboards and operator tooling. Optional by design.

---

## A quick start

Install Loom:

```bash
uv tool install agent-loom
```

Initialize a repository:

```bash
loom init --yes --workspace-mode repo
```

Create intent:

```bash
loom ticket create "Ship agent dashboard" --type task --priority 1
```

Isolate the work:

```bash
loom workspace worktree ensure agent-dashboard --base-ref main
```

At this point you can:

* Run a single agent with memory
* Or start a team for coordinated work

```bash
loom team start core --objective "Build the Loom dashboard"
loom team spawn core <ticket-id>
```

Stop and resume safely:

```bash
loom team clock-out core
loom team clock-in core
```

Work continues exactly where it left off.

---

## Fail-forward UX

Loom assumes intent matters more than syntax.

Partial, fuzzy inputs are normalized safely:

* `clock in` → `clock-in`
* `--unread` → `--unacked`
* `--jsonl` → `--format jsonl`

When something fails, Loom explains what it tried to do and why it chose a different path.

Most commands support structured output. When in doubt:

```bash
loom <cmd> -h
```

---

## How learning compounds

Agents learn in two parallel loops:

* **Passive**: observations are captured continuously
* **Active**: Plan → Work → Review → Compound

The result is not opaque state. It is files on disk.

Memory captures context. Skills capture procedure. Together, they prevent the same mistakes from happening twice.

---

## Workspace modes

Loom adapts to your project structure.

* **Repo mode**: one repository, many worktrees
* **Poly mode**: multiple repositories, shared worktrees, explicit dependencies

Example poly flow:

```bash
loom workspace poly init
loom workspace add api git@github.com:org/api.git --clone
loom workspace add web git@github.com:org/web.git --clone
loom workspace worktree add sprint-42 --all
loom workspace deps show api
```

---

## Tradeoffs, consciously made

Loom operates near systems like Beads and Gastown, but chooses differently.

* Tickets are Markdown, not a database
* Teams are tmux, not metaphor
* Learning is files, not opaque state

These are not claims of correctness. They are constraints chosen to keep agent work legible, debuggable, and human-compatible.

Loom optimizes for clarity over cleverness.

---

## Server API

For dashboards and operator tooling:

```bash
loom server start --host 127.0.0.1 --port 8764
```

The OpenAPI spec lives at:

```
docs/openapi.yaml
```

---

## Development

Loom uses `uv`:

```bash
uv run basedpyright
uv run ruff check .
uv run pytest
```

---

## Further reading

* `AGENTS.md`: agent primitives and expectations
* `LOOM.md`: system context and design rationale
* `LOOM_ROADMAP.md`: direction, priorities, and an AI-first chang
