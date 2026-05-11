---
id: evidence:harness-package-surface-skeleton-check
kind: evidence
status: recorded
created_at: 2026-05-07T22:26:09Z
updated_at: 2026-05-07T23:49:27Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:7h8u6oxp
  packet:
    - packet:ralph-ticket-7h8u6oxp-20260507T222124Z
  spec:
    - spec:core-and-playbooks-package-contract
external_refs: {}
---

# Summary

Recorded structural observations for `ticket:7h8u6oxp`, which rebuilt the
non-OpenCode native harness package skeleton around `loom-core/` and
`loom-playbooks/`.

# Procedure

Observed at: 2026-05-07T22:26:09Z

Source state: commit `d021bc1c4968f398f6ca7a666e006b4cced6d666` on branch
`main`, with local split-package work in progress and unrelated untracked example
files under `examples/00-todo-app`.

Procedure:

- Ran Ralph packet `packet:ralph-ticket-7h8u6oxp-20260507T222124Z` to create the
  common non-OpenCode harness package skeleton.
- Inspected changed manifests and catalogs with file reads.
- Parsed changed JSON files with Node:
  - `.claude-plugin/marketplace.json`
  - `.agents/plugins/marketplace.json`
  - `.cursor-plugin/marketplace.json`
  - `loom-core/.claude-plugin/plugin.json`
  - `loom-core/claude-hooks/hooks.json`
  - `loom-core/.codex-plugin/plugin.json`
  - `loom-core/.cursor-plugin/plugin.json`
  - `loom-core/gemini-extension.json`
  - `loom-playbooks/.claude-plugin/plugin.json`
  - `loom-playbooks/.codex-plugin/plugin.json`
  - `loom-playbooks/.cursor-plugin/plugin.json`
  - `loom-playbooks/gemini-extension.json`
- Ran existence checks for package skill roots and removed obsolete root files.
- Ran root-catalog checks for both `loom-core` and `loom-playbooks`.
- After mandatory critique found the missing Cursor root discovery surface, added
  `.cursor-plugin/marketplace.json` and included it in the JSON/catalog checks.
- Ran stale root-surface searches for `skills/using-loom`, `./skills`, and
  `/skills` across root catalogs and package-root manifests.
- Ran trailing-whitespace scans over new package-root JSON/Markdown surfaces with
  Grep pattern `[ \t]+$`.
- Ran `git diff --check -- .claude-plugin .agents .codex-plugin .cursor-plugin
  claude-hooks gemini-extension.json gemini-bootstrap.md` for tracked root-surface
  changes.

Expected result: package-root metadata exists for Claude, Codex, Cursor, and
Gemini; root catalogs list `loom-core` and `loom-playbooks`; obsolete root
single-package manifests/bootstrap files do not present root `skills/` as current
truth; changed JSON parses; checks do not find whitespace issues.

Actual observed result: structural checks passed. Runtime harness install behavior
was not validated.

Procedure verdict / exit code: pass for structural harness package skeleton checks.

# Artifacts

Files added:

```text
loom-core/.claude-plugin/plugin.json
loom-core/claude-hooks/hooks.json
loom-core/.codex-plugin/plugin.json
loom-core/.cursor-plugin/plugin.json
loom-core/gemini-extension.json
loom-core/gemini-bootstrap.md
loom-playbooks/.claude-plugin/plugin.json
loom-playbooks/.codex-plugin/plugin.json
loom-playbooks/.cursor-plugin/plugin.json
loom-playbooks/gemini-extension.json
```

Files updated:

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
.cursor-plugin/marketplace.json
```

Files removed:

```text
.claude-plugin/plugin.json
.codex-plugin/plugin.json
.cursor-plugin/plugin.json
claude-hooks/hooks.json
gemini-extension.json
gemini-bootstrap.md
```

JSON parse check:

```text
json_ok 12
```

Removed root single-package files check:

```text
test ! -e .claude-plugin/plugin.json -> pass
test ! -e .codex-plugin/plugin.json -> pass
test ! -e .cursor-plugin/plugin.json -> pass
test ! -e claude-hooks/hooks.json -> pass
test ! -e gemini-extension.json -> pass
test ! -e gemini-bootstrap.md -> pass
```

Root catalog checks:

```text
.claude-plugin/marketplace.json: loom-core source ./loom-core
.claude-plugin/marketplace.json: loom-playbooks source ./loom-playbooks
.agents/plugins/marketplace.json: loom-core path ./loom-core
.agents/plugins/marketplace.json: loom-playbooks path ./loom-playbooks
.cursor-plugin/marketplace.json: loom-core source loom-core
.cursor-plugin/marketplace.json: loom-playbooks source loom-playbooks
```

Root catalog stale `skills` checks:

```text
grep skills/using-loom|\.\/skills|/skills in .claude-plugin/*.json -> no files found
grep skills/using-loom|\.\/skills|/skills in .agents/**/*.json -> no files found
grep skills/using-loom|\.\/skills|/skills in .cursor-plugin/*.json -> no files found
```

Package-root `skills` checks:

```text
loom-core manifests/hooks contain package-root-local ./skills and
${CLAUDE_PLUGIN_ROOT}/skills/using-loom references.
loom-playbooks manifests contain package-root-local ./skills references only.
```

Trailing-whitespace scans:

```text
grep [ \t]+$ over loom-core/**/*.{json,md} -> no files found
grep [ \t]+$ over loom-playbooks/**/*.{json,md} -> no files found
```

Tracked root-surface diff check:

```text
git diff --check -- .claude-plugin .agents .codex-plugin .cursor-plugin claude-hooks gemini-extension.json gemini-bootstrap.md
```

Result: no output.

Because package-root metadata files are currently untracked, the trailing-whitespace
scans above are the proof for their content whitespace, not normal `git diff
--check`.

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

- spec:core-and-playbooks-package-contract#ACC-004 — structural support; package
  metadata exists under `loom-core` and `loom-playbooks`, and root catalogs list
  both package roots.
- spec:core-and-playbooks-package-contract#ACC-006 — support only for explicit
  deferral posture; no Codex installed-plugin preload or Gemini two-extension
  runtime claim is made by this evidence.
- spec:core-and-playbooks-package-contract#ACC-007 — partial support scoped to
  changed harness manifests and root catalogs; root single-package manifests and
  root Gemini bootstrap files no longer present root `skills/` as current truth.

# Challenges Claims

None - no observed challenge to the scoped structural ticket claims.

# Environment

Commit: `d021bc1c4968f398f6ca7a666e006b4cced6d666`

Branch: `main`

Runtime: filesystem, Node JSON parse, git, glob, and Grep inspection

OS: macOS / Darwin

Relevant config: dirty local checkout with split migration in progress

External service / harness / data source when applicable: N/A

# Validity

Valid for: structural harness package metadata and root catalog state at the
observed source state.

Fresh enough for: mandatory critique and ticket-owned acceptance review of
`ticket:7h8u6oxp`.

Recheck when: package metadata, root catalogs, hook/context files, package-root
paths, or harness validation claims change.

Invalidated by: reintroducing root single-package manifests that point at root
`skills/`, removing package-root manifests, changing root catalogs away from both
package roots, or making Codex/Gemini runtime claims without evidence.

Supersedes / superseded by: None.

# Limitations

- Does not validate Claude, Codex, Cursor, Gemini, OpenCode, or generic harness
  runtime install/discovery behavior.
- Does not create or validate `@z3z1ma/open-loom-core` or
  `@z3z1ma/open-loom-playbooks` packages.
- Does not update public docs, examples, root `package.json`, or `open-loom.mjs`.
- Does not prove package tarball contents.

# Result

The repository now has a structurally valid non-OpenCode harness package skeleton:
package-root metadata exists for Claude, Codex, Cursor, and Gemini, root catalogs
list `loom-core` and `loom-playbooks`, obsolete root single-package metadata files
were removed, and changed JSON/path/whitespace checks passed.

# Interpretation

The observations support mandatory critique of the harness package skeleton. They
do not establish runtime support or release readiness.

# Related Records

- ticket:7h8u6oxp
- packet:ralph-ticket-7h8u6oxp-20260507T222124Z
- spec:core-and-playbooks-package-contract
- decision:0008
