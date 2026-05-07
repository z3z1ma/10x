---
id: evidence:core-doctrine-playbook-decoupling-check
kind: evidence
status: recorded
created_at: 2026-05-07T22:01:44Z
updated_at: 2026-05-07T22:05:48Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:hi5e7nbr
  packet:
    - packet:ralph-ticket-hi5e7nbr-20260507T215704Z
  spec:
    - spec:core-and-playbooks-package-contract
external_refs: {}
---

# Summary

Recorded structural observations from Ralph iteration 01 for
`ticket:hi5e7nbr`, which decoupled current core skill prose from optional
playbook assumptions before the package-root move.

This evidence supports only the scoped core doctrine/prose portion of
`spec:core-and-playbooks-package-contract#ACC-002` and `#ACC-007`. It does not
prove package-root creation, harness install behavior, or public documentation
reconciliation.

# Procedure

Observed at: 2026-05-07T22:01:44Z

Source state: commit `d021bc1c4968f398f6ca7a666e006b4cced6d666` on branch
`main`, with untracked unrelated example files under `examples/00-todo-app` and
local Loom planning records in progress.

Procedure:

- Launched Ralph packet `packet:ralph-ticket-hi5e7nbr-20260507T215704Z` with
  child write scope limited to selected current core skill paths.
- Child searched scoped core files for optional playbook names and hardcoded
  optional playbook paths before editing.
- Child edited current core skill prose only.
- Parent reran targeted scoped search:
  `rg -n 'loom-(drive|git|debugging|spike|codemap|ship|skill-authoring)|skills/loom-(drive|git|debugging|spike|codemap|ship|skill-authoring)' skills/using-loom skills/loom-workspace skills/loom-records skills/loom-plans skills/loom-tickets skills/loom-research skills/loom-ralph`.
- Parent ran `git diff --stat -- skills/using-loom skills/loom-workspace skills/loom-records skills/loom-plans skills/loom-tickets skills/loom-research skills/loom-ralph`.
- Parent ran `git diff --check -- skills/using-loom skills/loom-workspace skills/loom-records skills/loom-plans skills/loom-tickets skills/loom-research skills/loom-ralph`.
- After critique finding `critique:core-doctrine-playbook-decoupling-review#FIND-003`,
  parent made a small wording clarification in
  `skills/loom-workspace/references/task-routing-catalog.md` and reran the scoped
  optional mention/path searches plus `git diff --check`.

Expected result when applicable: scoped core prose should frame optional playbook
skills as optional, installed, package-dependent, or replaceable by equivalent
project workflows; hardcoded optional playbook source paths should be absent from
scoped core files; diff whitespace check should pass.

Actual observed result: scoped remaining optional playbook mentions are framed as
optional, installed, package-dependent, or equivalent. Parent scoped search found
no `skills/loom-drive`, `skills/loom-git`, `skills/loom-debugging`,
`skills/loom-spike`, `skills/loom-codemap`, `skills/loom-ship`, or
`skills/loom-skill-authoring` path references inside the child write scope.
`git diff --check` produced no output.

Procedure verdict / exit code: pass for structural checks; acceptance remains
ticket-owned and critique is still required.

# Artifacts

Ralph child changed 15 files in scoped core skill paths:

```text
skills/loom-plans/references/plan-shape.md         |  5 ++--
skills/loom-ralph/SKILL.md                         | 10 +++++---
skills/loom-ralph/references/packet-contract.md    |  3 ++-
skills/loom-ralph/references/work-driver.md        |  5 ++--
skills/loom-records/references/frontmatter.md      |  4 +--
skills/loom-records/references/implementation-reality.md | 2 +-
skills/loom-records/references/route-vocabulary.md |  2 +-
skills/loom-research/SKILL.md                      |  4 +--
skills/loom-research/references/research-shape.md  |  8 +++---
skills/loom-tickets/references/local-execution.md  |  6 +++--
skills/loom-workspace/references/problem-shaping.md |  7 +++---
skills/loom-workspace/references/routing.md        | 19 ++++++++------
skills/loom-workspace/references/status-snapshot.md |  7 +++---
skills/loom-workspace/references/task-routing-catalog.md | 29 +++++++++++++---------
skills/using-loom/references/02-truth-and-authority.md | 8 +++---
```

Before-state observations reconstructed from the scoped diff show the iteration
changed direct or path-coupled playbook assumptions such as:

```text
`skills/loom-git/references/parallel-ralph-with-git.md`. Ralph packet
6. for Git-backed file changes, use `loom-git` to choose branch/worktree
5. `skills/loom-git/SKILL.md` when the iteration mutates repository files,
Use `skills/loom-git/SKILL.md` when choosing these values for Git-backed work.
5. For Git-backed file changes, use `skills/loom-git/SKILL.md` to resolve the
- current behavior unknown -> evidence or `loom-debugging`
| already-truthful work needs PR, release, merge, or handoff packaging | `loom-ship` |
that should become reusable research; use `loom-spike` for procedural spike or
Use `skills/loom-spike/SKILL.md` for procedural spike or sketch workflow detail
- root cause is unknown -> use `loom-debugging`;
- the design, API, data model, or UI shape is exploratory -> use `loom-spike`;
than more prose. Use `loom-spike` sketch flow when mockups, diagrams, screenshots,
`loom-drive`
`loom-git` support coordinator
- debugging or incident flow -> `loom-debugging`
- bounded experiment, prototype, or sketch -> `loom-spike`
- codebase/module atlas work -> `loom-codemap`
`loom-ship`
`loom-ship` packages PR summaries, release notes, handoff packages,
invoking the full `loom-drive` loop. Use `loom-drive` when the work is a
| "Fix this bug" ... | `loom-debugging` -> evidence -> `loom-tickets` -> local execution or `loom-ralph` |
| Performance problem ... | `loom-evidence` baseline -> `loom-research` or `loom-spike` -> ticket -> after evidence -> performance critique |
| UI page ... | `loom-specs` if fuzzy -> `loom-spike` for variants when needed -> ticket -> visual/product evidence -> critique |
| Architecture improvement ... | `loom-codemap`/`loom-research` -> `loom-specs` or `loom-constitution` for decisions -> plan/ticket |
| Prototype this ... | `loom-spike` -> evidence/research -> spec/wiki/ticket route after conclusion |
| "Where is X?" ... | `loom-codemap` -> evidence/research -> wiki atlas when accepted |
| PR description ... | `loom-ship`; route back to tickets/evidence/critique if not truthful |
| "Is this done?" ... | `loom-tickets` acceptance gate; `loom-ship` only after truth is current |
| User asks to keep going ... | `loom-drive` -> owner layers -> tickets/Ralph/evidence/critique |
- `loom-debugging` when root cause is unknown;
- `loom-spike` when the right design, API, data model, or UI shape is still being
layers. Workspace entry, record grammar, `loom-drive` objective/workflow driving,
```

Parent scoped search after the edit and the critique follow-up wording fix found
remaining optional playbook mentions in core paths, all framed as optional,
installed, package-dependent, or equivalent:

```text
skills/loom-research/SKILL.md:42: use optional `loom-spike` or an equivalent exploration workflow
skills/loom-workspace/references/status-snapshot.md:57: Use installed `loom-drive`, or a project-provided equivalent
skills/loom-ralph/SKILL.md:58: use an installed `loom-git` support coordinator or project Git practice
skills/loom-workspace/references/task-routing-catalog.md:19: optional `loom-debugging` or equivalent investigation
skills/loom-workspace/references/task-routing-catalog.md:36: optional `loom-ship` or equivalent shipping workflow
skills/loom-workspace/references/routing.md:35: optional `loom-drive` or a project-provided objective driver
skills/loom-records/references/frontmatter.md:136: When optional `loom-drive` is installed
```

The full parent search output contained additional similarly framed optional
mentions and no hardcoded optional playbook paths in scoped core files. The final
path-specific search for `skills/loom-(drive|git|debugging|spike|codemap|ship|skill-authoring)`
inside scoped core paths produced no output.

# Raw Artifact Store

- Path: None - the relevant observations are summarized in this record and can be
  reproduced with the commands above.
- Captured artifacts: None.
- Key excerpts / index: N/A.
- Redaction / sensitivity: no sensitive data observed or preserved.
- Retention / tracking: N/A.

# Visual / Product Evidence

N/A - no UI/product artifact was changed.

# Supports Claims

- spec:core-and-playbooks-package-contract#ACC-002 — partial support only; core
  doctrine/operator prose was edited and observed, but package-root creation and
  core-only harness discovery are not in this ticket scope.
- spec:core-and-playbooks-package-contract#ACC-007 — partial support only; scoped
  core skill references no longer hardcode optional playbook source paths and
  remaining playbook mentions are framed as optional/equivalent, but public docs,
  manifests, examples, and all active records are not covered here.

# Challenges Claims

None - no observed challenge to the scoped ticket claims.

# Environment

Commit: `d021bc1c4968f398f6ca7a666e006b4cced6d666`

Branch: `main`

Runtime: file and git inspection only

OS: macOS / Darwin

Relevant config: current dirty checkout with unrelated untracked example files

External service / harness / data source when applicable: N/A

# Validity

Valid for: scoped core skill prose diff from Ralph iteration 01 and structural
search/whitespace observations listed above.

Fresh enough for: critique of `ticket:hi5e7nbr` implementation and ticket-owned
acceptance review for the scoped doctrine decoupling slice.

Recheck when: any scoped core skill file changes, package-root move happens,
public docs are updated, or critique asks for broader search coverage.

Invalidated by: edits to scoped core skill prose that reintroduce mandatory
optional-playbook assumptions or hardcoded optional playbook package paths.

Supersedes / superseded by: None.

# Limitations

- Does not prove `loom-core/skills` exists.
- Does not prove core-only harness skill discovery.
- Does not prove public docs, examples, manifests, or all owner records have been
  reconciled.
- Does not prove optional playbook package dependency wording, because playbook
  skills were out of scope.
- Does not replace mandatory critique for this high-risk protocol-authority
  change.

# Result

The scoped Ralph iteration produced core skill prose changes that make optional
playbooks explicitly optional, installed, package-dependent, or equivalent to
project-provided workflows. The parent rerun of scoped searches found no
hardcoded optional playbook source paths in child write scope, and whitespace
checks passed.

# Interpretation

The observations support that `ticket:hi5e7nbr` made progress toward a coherent
core-only package before the physical package move. They do not establish full
spec acceptance or release readiness.

# Related Records

- ticket:hi5e7nbr
- packet:ralph-ticket-hi5e7nbr-20260507T215704Z
- spec:core-and-playbooks-package-contract
- decision:0008
