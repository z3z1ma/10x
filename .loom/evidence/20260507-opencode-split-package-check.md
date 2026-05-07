---
id: evidence:opencode-split-package-check
kind: evidence
status: recorded
created_at: 2026-05-07T22:41:46Z
updated_at: 2026-05-07T22:45:12Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:xtt24452
  packet:
    - packet:ralph-ticket-xtt24452-20260507T223743Z
  spec:
    - spec:core-and-playbooks-package-contract
external_refs: {}
---

# Summary

Recorded structural and package dry-run observations for `ticket:xtt24452`, which
split the OpenCode package surface into `open-loom-core` and
`open-loom-playbooks` and converted the repository root package to private
non-published repo metadata.

# Procedure

Observed at: 2026-05-07T22:41:46Z

Source state: commit `d021bc1c4968f398f6ca7a666e006b4cced6d666` on branch
`main`, with local split-package work in progress and unrelated untracked example
files under `examples/00-todo-app`.

Procedure:

- Ran Ralph packet `packet:ralph-ticket-xtt24452-20260507T223743Z` to implement the
  OpenCode split package files.
- Inspected root and package-root OpenCode package files.
- Ran core smoke: `node loom-core/open-loom-core.mjs --smoke`.
- Ran playbooks smoke: `node loom-playbooks/open-loom-playbooks.mjs --smoke`.
- Ran package-root dry-runs:
  - `npm pack --dry-run ./loom-core`
  - `npm pack --dry-run ./loom-playbooks`
  - `npm --prefix loom-core run pack:check`
  - `npm --prefix loom-playbooks run pack:check`
- Inspected root `package.json` for `private: true` and absence of `main`,
  `exports`, and `files` publish fields.
- Searched changed OpenCode files for stale root `skills/` or single `open-loom`
  package claims.
- Ran trailing-whitespace scans over new package-root OpenCode JSON/MJS files with
  Grep pattern `[ \t]+$`.
- Ran `git diff --check -- package.json open-loom.mjs loom-core/package.json
  loom-core/open-loom-core.mjs loom-playbooks/package.json
  loom-playbooks/open-loom-playbooks.mjs` for tracked root package/update/deletion
  checks. New package-root files are currently untracked, so their content
  whitespace is covered by the explicit trailing-whitespace scans and package
  dry-runs, not by normal `git diff --check`.
- After mandatory critique found that playbook package metadata did not state the
  core package dependency, added `open-loom-core` to the playbook package
  description and `peerDependencies`, then reran playbooks smoke/dry-run checks.

Expected result: core package smoke shows 8 using-Loom references and 15 core
skills; playbooks package smoke shows 0 using-Loom references and 7 playbook
skills; dry-runs package the two split package roots; root package is private and
not publishable; diff/whitespace checks pass.

Actual observed result: expected smoke and package-root dry-run checks passed.
Runtime OpenCode install behavior was not validated.

Procedure verdict / exit code: pass for structural OpenCode split package checks.

# Artifacts

Files added:

```text
loom-core/package.json
loom-core/open-loom-core.mjs
loom-playbooks/package.json
loom-playbooks/open-loom-playbooks.mjs
```

Files updated:

```text
package.json
```

Files removed:

```text
open-loom.mjs
```

Core smoke excerpt:

```text
pluginId: open-loom-core
usingLoomReferenceCount: 8
firstUsingLoomReference: skills/using-loom/references/01-core-identity.md
lastUsingLoomReference: skills/using-loom/references/08-trust-boundaries.md
instructionCount: 8
instructionsAreDeduped: true
skillCount: 15
skillPath: /Users/alexanderbutler/code_projects/personal/agent-loom/loom-core/skills
```

Playbooks smoke excerpt:

```text
pluginId: open-loom-playbooks
usingLoomReferenceCount: 0
instructionCount: 0
doesNotPreloadCoreDoctrine: true
skillCount: 7
skillPath: /Users/alexanderbutler/code_projects/personal/agent-loom/loom-playbooks/skills
skillPathsAreDeduped: true
```

Package dry-run excerpts:

```text
npm pack --dry-run ./loom-core -> open-loom-core@0.1.10, total files 101,
includes open-loom-core.mjs, package.json, and skills/.

npm pack --dry-run ./loom-playbooks -> open-loom-playbooks@0.1.10, total files 27,
includes open-loom-playbooks.mjs, package.json, skills/, and peer dependency on
open-loom-core.

npm --prefix loom-core run pack:check -> smoke and package-local npm pack passed.
npm --prefix loom-playbooks run pack:check -> smoke and package-local npm pack passed.
```

Verification command nuance:

```text
npm --prefix loom-core pack --dry-run
npm --prefix loom-playbooks pack --dry-run
```

In npm `10.9.4` from the repository root, those exact command forms returned
success but packed the private root workspace package instead of the package root.
This evidence therefore relies on package-root dry-run forms and package-local
`pack:check` scripts rather than treating that npm-prefix form as proof.

Root private package inspection:

```text
package.json private: true
no main
no exports
no files
scripts: smoke:core, smoke:playbooks, smoke:packages, pack:check:core,
pack:check:playbooks, pack:check
```

Stale root/single-package claim searches:

```text
changed OpenCode package files: no stale root skills product-truth matches
changed OpenCode package files: no single publishable "open-loom" package claim
package-local skills/ mentions appear only in loom-core/package.json and
loom-playbooks/package.json files arrays
```

Trailing-whitespace scans:

```text
grep [ \t]+$ over loom-core/*.{json,mjs} -> no files found
grep [ \t]+$ over loom-playbooks/*.{json,mjs} -> no files found
```

Diff check:

```text
git diff --check -- package.json open-loom.mjs loom-core/package.json \
  loom-core/open-loom-core.mjs loom-playbooks/package.json \
  loom-playbooks/open-loom-playbooks.mjs
```

Result: no output.

Because the split package files are currently untracked, this diff check is not
treated as proof for their full content. Package-root dry-runs and explicit
trailing-whitespace scans cover those new files until staging/commit review.

Playbook core dependency metadata:

```text
description: requires open-loom-core
peerDependencies.open-loom-core: ^0.1.10
```

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

- spec:core-and-playbooks-package-contract#ACC-005 — structural support;
  `open-loom-core` registers 8 using-Loom references and 15 core skills,
  `open-loom-playbooks` registers 7 playbook skills and no core preload, both
  package roots dry-run successfully, playbooks metadata names its `open-loom-core`
  peer dependency, and root `package.json` is private.
- spec:core-and-playbooks-package-contract#ACC-007 — partial support scoped to
  changed OpenCode package files and root package metadata; root `skills/` is no
  longer presented as current OpenCode package truth.

# Challenges Claims

None - no observed challenge to scoped package metadata after using package-root
dry-run commands.

# Environment

Commit: `d021bc1c4968f398f6ca7a666e006b4cced6d666`

Branch: `main`

Runtime: Node.js, npm `10.9.4`, git, filesystem, and Grep inspection

OS: macOS / Darwin

Relevant config: dirty local checkout with split migration in progress

External service / harness / data source when applicable: N/A

# Validity

Valid for: local OpenCode package module smoke behavior, package-root npm dry-runs,
and root private package metadata at the observed source state.

Fresh enough for: mandatory critique and ticket-owned acceptance review of
`ticket:xtt24452`.

Recheck when: OpenCode package files, package names, package files arrays, skill
membership, root package metadata, or runtime OpenCode validation claims change.

Invalidated by: reintroducing root publishable `open-loom`, changing playbooks to
preload core doctrine, changing core using-Loom reference paths, or package dry-run
outputs that omit required package files.

Supersedes / superseded by: None.

# Limitations

- Does not validate a real OpenCode install from npm, file path, or package array.
- Does not publish packages.
- Does not update public docs or examples.
- Does not decide a future deprecation notice for the previously published
  `open-loom` package.

# Result

The repository now has two structural OpenCode package roots, `open-loom-core` and
`open-loom-playbooks`, while root package metadata is private/non-published. Local
smoke and package-root dry-run checks passed.

# Interpretation

The observations support mandatory critique of the OpenCode split package slice.
They do not establish release readiness or real OpenCode runtime install support.

# Related Records

- ticket:xtt24452
- packet:ralph-ticket-xtt24452-20260507T223743Z
- spec:core-and-playbooks-package-contract
- decision:0008
