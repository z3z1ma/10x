---
id: evidence:gemini-root-core-shim-check
kind: evidence
status: recorded
created_at: 2026-05-07T23:22:25Z
updated_at: 2026-05-07T23:22:25Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:mbkqbkgq
  spec:
    - spec:core-and-playbooks-package-contract
  decision:
    - decision:0009
  research:
    - research:gemini-extension-subdirectory-feasibility
external_refs: {}
---

# Summary

Gemini CLI `0.34.0` was observed validating and installing the repository root as
a `loom-core` extension after adding the Gemini root core shim. The installed root
extension listed the root `gemini-bootstrap.md` context file and the 15 core Loom
skills only; playbook skills were absent.

# Procedure

Observed at: 2026-05-07T23:22:25Z

Source state: commit `d021bc1` on branch `main`, with uncommitted split-package and
Gemini root-shim changes.

Procedure:

```bash
node -e "JSON.parse(require('fs').readFileSync('gemini-extension.json','utf8')); JSON.parse(require('fs').readFileSync('loom-core/gemini-extension.json','utf8')); JSON.parse(require('fs').readFileSync('loom-playbooks/gemini-extension.json','utf8')); console.log('json_ok')"
test -L skills && test "$(readlink skills)" = "loom-core/skills" && printf 'skills_symlink_ok\n'
tmp="$(mktemp -d "/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/gemini-root-core.XXXXXX")"
mkdir -p "$tmp/.gemini"
HOME="$tmp" gemini --version
HOME="$tmp" gemini extensions validate "$PWD"
HOME="$tmp" gemini extensions install "$PWD" --consent
HOME="$tmp" gemini extensions list
```

Expected result when applicable:

- Gemini JSON manifests parse.
- Root `skills` is a symlink to `loom-core/skills`, not a copied bundle.
- `gemini extensions validate "$PWD"` succeeds for the repository root.
- `gemini extensions install "$PWD" --consent` succeeds as `loom-core`.
- `gemini extensions list` shows core context and core skills only, with no
  playbook skills.

Actual observed result:

- JSON parse check printed `json_ok`.
- Symlink check printed `skills_symlink_ok`.
- `gemini --version` printed `0.34.0` and exited `0`.
- `gemini extensions validate "$PWD"` printed:

```text
Extension /Users/alexanderbutler/code_projects/personal/agent-loom has been successfully validated.
VALIDATE_EXIT=0
```

- `gemini extensions install "$PWD" --consent` printed:

```text
Extension "loom-core" installed successfully and enabled.
ROOT_INSTALL_EXIT=0
```

- `gemini extensions list` showed one installed extension, `loom-core`, with source
  type `local`, context file:

```text
/.../.gemini/extensions/loom-core/gemini-bootstrap.md
```

- The listed agent skills were the 15 core skills:
  `using-loom`, `loom-workspace`, `loom-wiki`, `loom-tickets`, `loom-specs`,
  `loom-retrospective`, `loom-research`, `loom-records`, `loom-ralph`,
  `loom-plans`, `loom-memory`, `loom-evidence`, `loom-initiatives`,
  `loom-critique`, and `loom-constitution`.

- The listed agent skills did not include playbook skills such as `loom-drive`,
  `loom-git`, `loom-debugging`, `loom-spike`, `loom-codemap`, `loom-ship`, or
  `loom-skill-authoring`.

Procedure verdict / exit code: pass for JSON, symlink, root validation, root
install, and extension list. Gemini printed a temp-home project-registry save
warning before the version output, but the validation/install/list commands all
completed with the expected exit codes.

# Artifacts

Key command excerpts:

```text
json_ok
skills_symlink_ok
0.34.0
VERSION_EXIT=0
Extension /Users/alexanderbutler/code_projects/personal/agent-loom has been successfully validated.
VALIDATE_EXIT=0
Extension "loom-core" installed successfully and enabled.
ROOT_INSTALL_EXIT=0
✓ loom-core (0.1.0)
 Context files:
  /var/folders/.../.gemini/extensions/loom-core/gemini-bootstrap.md
 Agent skills:
  using-loom
  loom-workspace
  loom-wiki
  loom-tickets
  loom-specs
  loom-retrospective
  loom-research
  loom-records
  loom-ralph
  loom-plans
  loom-memory
  loom-evidence
  loom-initiatives
  loom-critique
  loom-constitution
LIST_EXIT=0
```

# Raw Artifact Store

- Path: None - key command excerpts are recorded directly.
- Captured artifacts: None.
- Key excerpts / index: N/A.
- Redaction / sensitivity: local paths are abbreviated where possible and contain no
  secrets.
- Retention / tracking: N/A.

# Visual / Product Evidence

N/A.

# Supports Claims

- spec:core-and-playbooks-package-contract#ACC-006 — supports the Gemini docs claim
  that repository-root install is valid only as core install, not playbook install.
- spec:core-and-playbooks-package-contract#ACC-009 — supports that the root Gemini
  shim exposes core context/skills only.
- ticket:mbkqbkgq — supports implementation of the Gemini root core shim.
- decision:0009 — supports feasibility of the accepted root core shim exception.

# Challenges Claims

- None active. This evidence would challenge any future claim that repository-root
  Gemini install includes playbooks.

# Environment

Commit: `d021bc1` with uncommitted package-split and root Gemini shim changes.

Branch: `main`.

Runtime: Gemini CLI `0.34.0` from `/run/current-system/sw/bin/gemini`; Node.js was
used for JSON parsing.

OS: macOS / Darwin under the current OpenCode shell environment.

Relevant config: `HOME` was set to a temporary directory under
`/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/` and removed after
the probe.

External service / harness / data source when applicable: local Gemini CLI only;
the remote GitHub repository was not installed because these changes are not yet
present there.

# Validity

Valid for: current local Gemini CLI `0.34.0` behavior against this worktree's root
Gemini core shim.

Fresh enough for: `ticket:mbkqbkgq` acceptance that repository-root Gemini install
works as a core-only local install proxy and that root docs may describe root
install as core-only after this change lands.

Recheck when: Gemini CLI version changes, root `gemini-extension.json` changes,
root `gemini-bootstrap.md` changes, the root `skills` shim changes,
`loom-core/skills` membership changes, public Gemini install docs change, or the
remote repository is published with these changes.

Invalidated by: Gemini no longer following root `skills` symlinks, root install
showing playbook skills, or root install failing from a fresh source state.

Supersedes / superseded by: supersedes the root-install failure observation in
`evidence:gemini-extension-local-link-route-check` for the current source state.

# Limitations

- This evidence validates local repository-root install, not remote GitHub install;
  remote install should be rechecked after the changes are available in the remote
  source.
- This evidence does not validate playbook remote install.
- This evidence does not validate interactive Gemini session context ordering
  beyond `gemini extensions list` showing the root context file.
- This evidence relies on symlink behavior for root skill discovery; non-POSIX or
  archive-based distribution paths may need separate validation.

# Result

The repository-root Gemini core shim validates and installs locally as `loom-core`,
with root context preload and core skills only.

# Interpretation

It is now truthful to document repository-root Gemini install as a core-only
shortcut, while continuing to recommend clone and explicit package-root links for
full core plus playbooks installs.

# Related Records

- decision:0009
- ticket:mbkqbkgq
- spec:core-and-playbooks-package-contract
- research:gemini-extension-subdirectory-feasibility
