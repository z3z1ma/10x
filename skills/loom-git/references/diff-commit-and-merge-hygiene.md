# Diff, Commit, And Merge Hygiene

Git history is useful when it stays aligned with Loom ownership.

The goal is not a beautiful branch at the cost of hidden scope. The goal is a
diff, commit, or merge that a future agent can reconcile against tickets,
packets, evidence, and critique.

## Diff Review

Review before handoff, critique, commit, or shipping:

```bash
git status --short
git diff --stat
git diff
git diff --check
```

Use path-limited diff commands when checking a packet write scope:

```bash
git diff -- path/to/scope
```

If the diff contains files outside the ticket or packet scope, either split the
work, update the owning ticket before proceeding, or remove the unrelated changes
only when they are yours to remove.

## Staging

Staging is a claim about what belongs together.

Guidelines:

- stage path-limited changes deliberately
- do not stage unrelated user work
- do not stage secrets, local credentials, `.env` files, or private machine state
- inspect staged diff before committing
- keep generated files with the source change only when the project expects that

Useful commands:

```bash
git diff --staged --stat
git diff --staged
```

## Committing

Commit only when the operator or project workflow asks for a commit.

When committing is appropriate:

- make the commit match one ticket-sized claim when practical
- mention the Loom ticket token when that is useful for traceability
- describe why the change exists, not only which files changed
- ensure evidence and critique disposition are not contradicted by the commit
  message
- do not amend or rewrite shared history without explicit approval

Example shape:

```text
Add loom-git worktree guidance

Teach Ralph-backed implementation work how to create isolated Git branches and
worktrees from an explicit integration baseline so parallel workers can avoid
shared checkout contention.
```

## Merging And Rebasing

Before merging or rebasing:

- resolve and refresh the integration baseline
- inspect whether the branch is behind or intentionally stacked on that baseline
- make sure the worktree is clean enough for the operation
- know whether the branch has been pushed or shared
- check whether project policy prefers merge commits, squash, or rebase

Safe default for protected integration refs:

- do not force-push a protected branch, release branch, or shared integration ref
- do not rewrite published branch history without explicit approval
- do not resolve conflicts by choosing one side blindly

If a conflict changes intended behavior, route back to the spec or ticket. A
merge conflict is implementation reality, not permission to redefine acceptance
in Git.

## Pull Requests And Shipping

Pull requests are external mirrors and review surfaces. They do not close Loom
work by themselves.

Use `loom-ship` when packaging a PR summary, evidence summary, risk summary, or
follow-up list from already-truthful Loom records.

A good PR description should point back to:

- ticket
- evidence
- critique, when present
- wiki or spec, when relevant
- known residual risks

## Cleanup After Merge Or Abandonment

Only clean up after checking the branch or worktree has no unpreserved work:

```bash
git status --short
git worktree list
```

After merge, cleanup may include:

- removing the worktree
- deleting the local branch
- deleting the remote branch if project policy allows it

After abandonment, cleanup is safe only when the ticket, research, or evidence
records preserve any useful conclusion, rejected path, or remaining follow-up.

## Anti-Patterns

Avoid:

- committing because a child said `stop` before parent reconciliation
- using a branch name as the only ticket reference
- using a PR checklist as the real acceptance gate
- hiding unrelated changes in a convenient commit
- rebasing or force-pushing to make evidence look cleaner than it was
- deleting a worktree before checking for untracked or unmerged work
