# Loom

**The agent-native operating system for terminal AI development.**

Loom turns a Git repo into a place where agents can plan, work, coordinate, remember, and learn over long horizons. It is intentionally Unixy: plain files on disk, deterministic outputs, and a fail-forward CLI that accepts a wide set of plausible inputs.

> Think of the ralph-wiggum loop, but it grows smarter over time, self organizes into teams, and iterates with builtin isolation and safety.

## Why Loom

- Persistence: intent, state, and lessons live in Git-backed files, not ephemeral prompts.
- Isolation: worktrees and snapshots keep `main` safe even under aggressive agent iteration.
- Coordination: tmux-native teams with durable inbox and merge queues.
- Learning: Obsidian-like memory plus compounding into skills.
- Agentic UX: forgiving argument normalization, actionable errors, JSON-first output.

## The stack (5 subsystems + server)

Everything is plain files on disk:

- Ticket (`.tickets/`): Markdown tickets with YAML frontmatter, dependency graph, claims.
- Team (`.team/`): tmux-native orchestration and run state (JSON on disk).
- Memory (`.memory/`): Markdown notes with YAML frontmatter; SQLite cache is derived.
- Workspace (`workspace.json`, `.loom/`, `.loom-repo/`): worktrees, snapshots, multi-repo service mesh.
- Compound (`.opencode/`): passive and active learning; skills are Markdown.
- Server (`loom server`): HTTP API for dashboards. Spec: `docs/openapi.yaml`.

## Quickstart (single repo)

Install from source:

```bash
uv tool install agent-loom
```

Initialize all subsystems (non-interactive):

```bash
loom init --yes --workspace-mode repo
```

Define intent, isolate work, and spawn a team:

```bash
loom ticket create "Ship agent dashboard" --type task --priority 1
loom workspace worktree ensure agent-dashboard --base-ref main
loom team start core --objective "Build the Loom dashboard"
loom team spawn core <ticket-id> # note: the manager will do this automatically too
```

Pause/resume a team (clock out/in):

```bash
loom team clock-out core
loom team clock-in core
```

## Agentic UX (fail forward)

Loom accepts a wide range of plausible inputs and normalizes them safely.

- `loom team clock in core` -> `clock-in`
- `loom team inbox core --unread` -> `--unacked`
- `loom ticket update <id> --add-note "Progress"` -> `add-note`
- `loom memory --json` / `--jsonl` -> `--format json|jsonl`

Most commands support `--json` output. When in doubt: `loom <cmd> -h`.

## The learning loop

Loom runs two learning channels in parallel:

- Passive: OpenCode compounding captures observations into skills.
- Active: Plan -> Work -> Review -> Compound writes SKILL.md files as procedural memory.

Memory and skills are complementary: memory is associative context, skills are reusable procedures.

## Workspace modes

- Repo mode: one repo, many worktrees.
- Poly mode: multi-repo service mesh with sets, tags, and group worktrees.

Example poly flow:

```bash
loom workspace poly init
loom workspace add api git@github.com:org/api.git --clone
loom workspace add web git@github.com:org/web.git --clone
loom workspace worktree add sprint-42 --all
loom workspace deps show api
```

## Lineage (Beads, Gastown, and the Loom tradeoffs)

Loom is built in the same problem space as Beads and Gastown, but with different tradeoffs.

- Tickets vs Beads: Loom keeps tickets as Markdown documents so agents and humans can read them directly. If you want JSONL-first issue storage with a whole Dolt db and hundreds of thousands of lines of code, Beads is in that family; Loom intentionally optimizes for simple document-shaped reasoning.
- Team vs Gastown: Loom keeps tmux visible, operational, and ephemeral. If you want deeper metaphor layers, Gastown explores that; Loom stays close to Unix primitives.

These are opinionated choices, not claims about correctness. Loom is optimized for agent reasoning, not abstraction density.

## Server API

This is really just an internal API that will soon power an operator dashboard.

```bash
loom server start --host 127.0.0.1 --port 8764
```

The (ai generated) OpenAPI spec is at `docs/openapi.yaml`.

## Development

Use uv for everything:

```bash
uv run basedpyright
uv run ruff check .
uv run pytest
```

## Docs

- `AGENTS.md` for agent usage and primitives.
- `LOOM.md` for system context.
- `LOOM_ROADMAP.md` for direction and AI-first changelog.
