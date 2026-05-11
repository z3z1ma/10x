---
id: evidence:skill-package-root-split-check
kind: evidence
status: recorded
created_at: 2026-05-07T22:14:33Z
updated_at: 2026-05-07T22:17:35Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:u9vtemj3
  packet:
    - packet:ralph-ticket-u9vtemj3-20260507T220907Z
    - packet:ralph-ticket-u9vtemj3-20260507T221312Z
  spec:
    - spec:core-and-playbooks-package-contract
external_refs: {}
---

# Summary

Recorded structural observations for `ticket:u9vtemj3`, which moved Loom skills
from the retired root `skills/` tree into `loom-core/skills` and
`loom-playbooks/skills`, then cleaned up explicit playbook-to-core path references
inside moved playbook prose.

# Procedure

Observed at: 2026-05-07T22:14:33Z

Source state: commit `d021bc1c4968f398f6ca7a666e006b4cced6d666` on branch
`main`, with tracked and untracked local work from the active split plan and
unrelated untracked example files under `examples/00-todo-app`.

Procedure:

- Ran Ralph packet `packet:ralph-ticket-u9vtemj3-20260507T220907Z` to move skill
  directories into package roots.
- Ran parent structural checks:
  - `glob loom-core/skills/*/SKILL.md`
  - `glob loom-playbooks/skills/*/SKILL.md`
  - `glob skills/*/SKILL.md`
  - `test ! -d skills`
  - Python membership check comparing expected core/playbook sets
  - `rg -n 'top-level skills/product surface/repo-root skills' loom-core loom-playbooks`
  - `rg -n 'skills/loom-(drive|git|debugging|spike|codemap|ship|skill-authoring)' loom-core`
  - `rg -n 'skills/(core skill names)' loom-playbooks`
  - `git diff --check -- loom-core loom-playbooks`
- Ran Ralph packet `packet:ralph-ticket-u9vtemj3-20260507T221312Z` to remove
  explicit core skill file paths from playbook prose.
- Reran `rg -n 'skills/(core skill names)' loom-playbooks` and
  `git diff --check -- loom-core loom-playbooks`.
- After critique identified that new package-root files were untracked, reran
  package-root trailing-whitespace scans with the Grep tool using pattern
  `[ \t]+$` over `loom-core/**/*.md` and `loom-playbooks/**/*.md`; both scans
  returned no files found. Also ran `git diff --check -- skills` for the tracked
  root-skill deletions; it returned no output.

Expected result when applicable: `loom-core/skills` has the 15 expected core
skills, `loom-playbooks/skills` has the 7 expected playbook skills, root `skills/`
is absent, no duplicate/wrong-package skills exist, playbooks do not contain
explicit package-local core `skills/...` paths, and diff checks pass.

Actual observed result: expected package-root membership matched exactly; root
`skills/` is absent; duplicate/wrong-package checks found no overlap; explicit
core paths in playbook prose were removed by iteration 02; tracked deletion diff
checks and package-root trailing-whitespace scans passed with no output.

Procedure verdict / exit code: pass for structural package-root split checks.

# Artifacts

Core package skill list observed:

```text
using-loom
loom-workspace
loom-records
loom-memory
loom-ralph
loom-retrospective
loom-constitution
loom-initiatives
loom-research
loom-specs
loom-plans
loom-tickets
loom-evidence
loom-critique
loom-wiki
```

Playbook package skill list observed:

```text
loom-drive
loom-git
loom-debugging
loom-spike
loom-codemap
loom-ship
loom-skill-authoring
```

Membership check output:

```text
core_count 15 missing [] extra []
playbook_count 7 missing [] extra []
overlap []
```

Root `skills/` check:

```text
glob skills/*/SKILL.md -> No files found
test ! -d skills -> pass
```

Stale path / surface scans:

```text
rg ... loom-core loom-playbooks
loom-core/skills/loom-records/references/query-and-linking.md:41:repo-root `skills/` tree.
```

The remaining `repo-root skills` mention is a negative warning: “Do not assume a
target Loom workspace has a repo-root `skills/` tree.”

Final explicit playbook-to-core path search:

```text
rg -n 'skills/(using-loom|loom-workspace|loom-records|loom-memory|loom-ralph|loom-retrospective|loom-constitution|loom-initiatives|loom-research|loom-specs|loom-plans|loom-tickets|loom-evidence|loom-critique|loom-wiki)' loom-playbooks
```

Result: no output.

Final tracked deletion diff check:

```text
git diff --check -- skills
```

Result: no output.

Package-root trailing-whitespace scans:

```text
grep pattern [ \t]+$ over loom-core/**/*.md -> no files found
grep pattern [ \t]+$ over loom-playbooks/**/*.md -> no files found
```

Earlier `git diff --check -- loom-core loom-playbooks` also returned no output,
but because new package-root files were untracked at observation time, that command
is not treated as the proof for package-root file contents.

# Raw Artifact Store

- Path: None - observations are summarized in this evidence record and can be
  reproduced with the commands above.
- Captured artifacts: None.
- Key excerpts / index: N/A.
- Redaction / sensitivity: no sensitive data observed or preserved.
- Retention / tracking: N/A.

# Visual / Product Evidence

N/A - no UI/product artifact was changed.

# Supports Claims

- spec:core-and-playbooks-package-contract#ACC-001 — structural support; package
  roots contain expected skill memberships.
- spec:core-and-playbooks-package-contract#ACC-002 — partial structural support;
  core skills are available under `loom-core/skills`, but harness runtime discovery
  is not covered by this ticket.
- spec:core-and-playbooks-package-contract#ACC-003 — structural support;
  playbooks contain no duplicated core skill directories, dependency wording is
  present in playbook `SKILL.md` files, and explicit core `skills/...` paths were
  removed from playbook prose.
- spec:core-and-playbooks-package-contract#ACC-007 — partial support; moved skill
  corpus was checked for retired root path/product-surface assumptions, but public
  docs, manifests, examples, and active owner records are later-ticket scope.

# Challenges Claims

None - no observed challenge to the scoped ticket claims.

# Environment

Commit: `d021bc1c4968f398f6ca7a666e006b4cced6d666`

Branch: `main`

Runtime: filesystem, git, glob, Python membership check, and `rg` inspection

OS: macOS / Darwin

Relevant config: dirty local checkout with split migration in progress

External service / harness / data source when applicable: N/A

# Validity

Valid for: package-root skill membership and moved-skill structural state at the
observed source state.

Fresh enough for: mandatory critique and ticket-owned acceptance review of
`ticket:u9vtemj3`.

Recheck when: any skill is moved, package-root paths change, playbook dependency
wording changes, or harness manifests/docs are updated.

Invalidated by: reintroducing root `skills/`, moving skills between package roots,
duplicating core skills under playbooks, or adding explicit core `skills/...` paths
inside playbook package prose.

Supersedes / superseded by: None.

# Limitations

- Does not validate Claude, Codex, Cursor, Gemini, OpenCode, or generic harness
  install behavior.
- Does not update or validate public docs, root catalogs, manifests, package
  metadata, or examples.
- Does not prove package tarball contents or runtime skill discovery.

# Result

The repository now has two physical skill package roots with exact expected
membership, no root `skills/` directory, no duplicate/wrong-package skill
membership, no explicit core `skills/...` paths inside playbooks, clean tracked
root-skill deletion diff output, and clean package-root trailing-whitespace scans.

# Interpretation

The observations support closing the source-layout migration slice if mandatory
critique agrees. They do not establish release readiness or harness install
support.

# Related Records

- ticket:u9vtemj3
- packet:ralph-ticket-u9vtemj3-20260507T220907Z
- packet:ralph-ticket-u9vtemj3-20260507T221312Z
- spec:core-and-playbooks-package-contract
- decision:0008
