# Scope Doctrine

Loom scope keeps read and write authority tied to an explicit workspace, repository, or worktree instead of guesswork.

## Supported Scope

Supported scope includes:

- the root repository at the workspace root
- repositories nested under workspace subdirectories

Canonical Loom records still live in one shared `.loom/` tree at the workspace root. Nested repositories are scope owners, not separate canonical record roots.

Arbitrary remote or distributed repository discovery is out of scope.

## Workspace Root Resolution

Resolve the workspace root before trying to assign repository or worktree ownership.

Use this as a two-step algorithm:

1. resolve the single workspace root that owns the canonical `.loom/` tree
2. resolve the owning repository or worktree for the target path or record

Keep those answers separate. The workspace root answers where canonical Loom artifacts live. Repository and worktree scope answer which code surface the work is allowed to touch.

Use this order:

1. prefer the nearest ancestor that contains both `.git/` and `.loom/`
2. if no established workspace exists, allow the current working directory as the workspace root unless it is a non-root subdirectory of a git repository
3. once that root is chosen, scaffold `.loom/` there before treating Loom as initialized
4. keep all canonical Loom records in that one workspace-root `.loom/` tree even when nested repositories are later discovered

If the current working directory is a non-root subdirectory of a git repository and no established workspace exists above it, fail closed rather than creating or trusting one by guesswork.

Scope resolution is one of the few places where a deterministic CLI may be useful. Ordinary reading, searching, editing, and deletion are still normal native-tool work rather than scope-tool work.

## Scope Identities

Use these scope identities:

- workspace
- repository
- worktree
- packet scope

Recommended examples:

- workspace id: `workspace:main`
- root repository id: `repo:root`
- nested repository id: `repo:services-api`
- bounded multirepo record scope: `{"kind": "multi_repository", "repository_ids": ["repo:admin-ui", "repo:query-service"]}`
- root worktree id: `worktree:root:default`
- nested worktree id: `worktree:services-api:feature-x`

## Fail-Closed Behavior

If repository or worktree identity is ambiguous, the system MUST fail closed.

Fail closed means stop, surface the ambiguity, and ask for or compute a stronger answer. It does not mean pick the most likely path and hope the agent guessed right.

Read `appendices/validation-rules.md` when you need the validation interpretation of this fail-closed rule.

## Packet Scope Rule

Packets MUST declare:

- scope kind
- scope id
- allowed repositories
- allowed worktrees
- whether cross-repo reads are allowed
- whether writes are restricted to one repository or worktree

Canonical records should use these conventions:

- use `repository_scope.kind = repository` when one repository clearly owns the work
- use `repository_scope.kind = multi_repository` when the work intentionally spans a bounded set of child repositories inside one workspace
- use `repository_scope.kind = workspace` only for truly workspace-wide work such as the main constitution or broad cross-cutting governance

This convention applies across constitutions, initiatives, research, specs, plans, tickets, critique, docs, and verification.

## Worked Examples

### Example: root-repo packet

If a packet is meant to operate only in the root repository, a healthy scope description looks like:

- scope kind: repository
- scope id: `repo:root`
- allowed repositories: `[repo:root]`
- allowed worktrees: `[]` or one explicit worktree if relevant
- cross-repo reads: false
- writes restricted to scope: true

### Example: nested-repo path resolution

If the parent resolves a path like `services/api/src/index.ts` to `repo:services-api`, that repository should become the owning repository for packet scope and write decisions.

### Example: multirepo record and packet

If a plan, spec, or ticket intentionally spans `repo:admin-ui` and `repo:query-service`, a healthy canonical scope description looks like:

- record `repository_scope`: `{"kind": "multi_repository", "repository_ids": ["repo:admin-ui", "repo:query-service"]}`
- packet scope kind: `workspace`
- packet allowed repositories: `[repo:admin-ui, repo:query-service]`
- cross-repo reads: true
- writes restricted to scope: true

The workspace-wide packet scope there does not mean "all repositories are in scope". It means the packet is operating across multiple repositories inside one workspace, with the concrete write boundary still narrowed by `allowed_repositories` and allowed write refs.

### Example: fail-closed behavior

If a path is outside the workspace or cannot be assigned one unambiguous repository owner, the parent should stop and escalate rather than choosing a best guess.

### Example: parent workspace with child repositories

If the workspace root contains child repositories such as `services/api/` and `services/web/`, keep canonical records in the parent `.loom/` tree.

- create or update canonical records under the parent workspace `.loom/`
- resolve `services/api/...` to `repo:services-api`
- bind execution authority with `repository_scope`, packet `scope`, `allowed_repositories`, and `allowed_worktrees`
- do not create additional child `.loom/` trees just because the target code lives in a nested repository

Read `appendices/worked-example-flow.md` when you want to see scope resolution inside the larger parent workflow.
