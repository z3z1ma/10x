# Branch And Remote Hygiene

Branch hygiene keeps implementation work fresh enough that Loom evidence and
critique are judging the intended repository state, not an accidentally stale or
misbased checkout.

## Starting Checks

Run these before creating a branch or compiling a packet for Git-backed work:

```bash
git rev-parse --show-toplevel
git status --short
git branch --show-current
git remote -v
```

If the worktree is dirty before you start, distinguish the user's existing work
from the ticket slice. Do not hide unrelated changes by folding them into the
new branch, packet, commit, or evidence.

## Integration Baseline

An integration baseline is the ref or commit the new work is meant to start from
and eventually reconcile back toward.

It might be:

- a remote-tracking branch such as `<remote>/<branch>`
- a local branch such as `trunk`, `develop`, `release/2.4`, or `main`
- a fork upstream rather than the push remote
- a patch-stack parent branch
- a release tag
- a specific commit SHA
- the current `HEAD` in a local-only repository

Do not assume the remote is named `origin`. Do not assume the integration branch
is named `main`. Do not assume there is a remote at all.

## Baseline Discovery Order

Prefer explicit sources over heuristics:

1. operator request, ticket, plan, release target, or external PR target
2. repository policy files, contribution docs, package release docs, or harness
   instructions
3. current branch upstream, when continuing an existing branch is the goal
4. remote metadata such as a remote HEAD, when there is a clear integration
   remote
5. local branch names and common conventions only as weak hints
6. operator clarification when the baseline affects safety or correctness

Useful discovery commands:

```bash
git remote
git remote -v
git branch --show-current
git rev-parse --abbrev-ref --symbolic-full-name @{u}
git for-each-ref --format='%(refname:short)' refs/heads refs/remotes
```

These commands are inspection tools, not a required ritual. Some will fail in a
repo with no current branch, no upstream, no remotes, or a detached `HEAD`. A
failure is information about the topology.

Some repositories have no upstream for the current branch. Some use a fork
remote for push and an upstream remote for integration. Some use release
branches. Some are local-only. Treat all of those as normal Git topologies, not
edge cases.

## Resolve To Commits

A ref name is movable. A packet needs the immutable commit it meant at compile
time.

Resolve the current checkout and the integration baseline:

```bash
git rev-parse --verify HEAD^{commit}
git rev-parse --verify <integration-ref-or-commit>^{commit}
```

The `^{commit}` suffix peels annotated tags and rejects objects that are not
commits. If the integration baseline is intentionally a tag, record both the tag
name and the resolved commit.

## Fetch Before Claiming Freshness

When the baseline is remote-backed, fetch the relevant remote refs before
claiming freshness:

```bash
git fetch --prune <remote>
```

If the integration remote is unknown but fetching all remotes is reasonable for
the repository, this can be a discovery step:

```bash
git fetch --all --prune
```

For large, slow, credential-sensitive, or unusual repositories, fetch the
smallest remote/ref set that answers the question.

In a parallel Ralph wave, the parent should fetch and resolve integration
commits before launch. A child should not run `git fetch`, `git fetch --prune`,
`git remote set-head`, `git gc`, or Git config mutations unless the packet
explicitly allows it, because linked worktrees can share refs, config, and object
storage.

Remote HEAD can help, but it is not authority by itself:

```bash
git symbolic-ref --quiet --short refs/remotes/<remote>/HEAD
```

If remote HEAD is missing, stale, or inconsistent with project policy, use the
stronger source and record the choice.

## Branch From The Resolved Baseline

For normal single-checkout work:

```bash
git switch -c loom/<ticket-token>/<short-slug> <integration-ref-or-commit>
```

For worktree-backed work:

```bash
git worktree add -b loom/<ticket-token>/<short-slug> ../<repo>-<ticket-token>-<short-slug> <integration-ref-or-commit>
```

If `git switch` is unavailable in an older Git installation, use the equivalent
`git checkout -b` form. If `git worktree` is unavailable or project policy
forbids linked worktrees, use a separate clone or another documented isolation
mechanism and record that in the packet execution context.

Examples of valid baselines include `<remote>/trunk`, `<remote>/develop`,
`release/2.4`, `main`, `v1.8.0`, or a specific commit SHA. The correct value is
the one owned by the repository's workflow and the Loom task, not the most
familiar convention.

## Local Integration Branch Refresh

If the repository workflow uses a local integration branch, update it only in a
clean worktree and only from its intended upstream:

```bash
git switch <local-integration-branch>
git pull --ff-only <remote> <remote-branch>
```

Do not pull, merge, or rebase across uncommitted user work unless the operator
explicitly asks and you have recorded what will happen.

## Branch Names

Good branch names make ownership visible without becoming the owner:

```text
loom/<ticket-token>/<short-slug>
loom/<ticket-token>/<repo-alias>-<short-slug>
loom/<ticket-token>/iter-01
```

Guidelines:

- include the Loom ticket token when one exists
- include the repo alias when several repositories are involved
- use one branch for one ticket-sized slice when possible
- use separate branches for parallel children
- do not reuse a branch for unrelated work because it is convenient

## Freshness Checks During Work

After resolving the baseline, this checks whether the current branch contains it:

```bash
git merge-base --is-ancestor <integration-ref-or-commit> HEAD
```

If it fails, the branch does not contain that baseline. Decide whether to merge,
rebase, restart from a fresh branch, stack intentionally on another branch, or
keep going with an explicit risk note. Do not silently claim baseline freshness.

Useful inspection commands:

```bash
git status --short
git diff --stat
git diff
git log --oneline --decorate HEAD..<integration-ref-or-commit>
```

## Rebase And History Rewrites

Rebasing unpublished local work can be a clean way to refresh a feature branch.

Do not rewrite published or shared history without explicit operator approval.
Do not force-push protected branches. If branch history policy is unclear, prefer
a merge from the resolved baseline or ask before rewriting.

## Repository Topologies

When more than one remote could be the integration source:

- inspect `git remote -v`
- check project documentation or existing branch patterns
- record the integration remote, integration ref, push remote, and review target
  separately when they differ
- stop if the choice changes safety or ownership

Common shapes include:

- `origin` is canonical and pushable
- `origin` is a fork, while `upstream` is canonical
- several product remotes exist for mirrors or deployment targets
- no remote exists because the repository is local-only or vendored
- the target is a release branch rather than trunk
- the target is a parent branch in a stacked-diff workflow
- the checkout is detached at a specific commit for reproduction or bisecting
- the repository uses sparse checkout, submodules, or Git LFS that affect what
  "fresh" means operationally

## Submodules And Tags

Only fetch tags or update submodules when the ticket or repository shape calls
for it.

Examples:

```bash
git fetch --prune --tags <remote>
git submodule update --init --recursive
```

These commands can materially change the working context. Record them as
evidence when they affect proof, release packaging, or reproduction.
