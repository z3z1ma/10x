---
id: evidence:gemini-extension-local-link-route-check
kind: evidence
status: recorded
created_at: 2026-05-07T23:06:08Z
updated_at: 2026-05-07T23:25:03Z
scope:
  kind: repository
  repositories:
    - repo:root
links:
  ticket:
    - ticket:sbzmrvqv
  spec:
    - spec:core-and-playbooks-package-contract
  research:
    - research:gemini-extension-subdirectory-feasibility
  decision:
    - decision:0008
external_refs: {}
---

# Summary

Gemini CLI `0.34.0` was observed against the split package-root extension
skeletons at an earlier source state. At that source state, the repository root
was not installable as a Gemini extension, while explicit local links for
`loom-core/` and `loom-playbooks/` succeeded and listed the expected context file
and skills.

This evidence supports the Gemini ticket's earlier local-link-supported route. It
does not decide ticket acceptance, critique verdict, or public docs.

Supersession note: `evidence:gemini-root-core-shim-check` supersedes this record's
repository-root install failure for the later source state that adds a root Gemini
core shim. This record remains valid for the explicit package-root local-link
observation.

# Procedure

Observed at: 2026-05-07T23:06:08Z

Source state: commit `d021bc1` on branch `main`, with uncommitted package-split
worktree changes including `loom-core/`, `loom-playbooks/`, and Gemini ticket
records.

Procedure:

```bash
tmp="$(mktemp -d "/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/gemini-sbzmrvqv.XXXXXX")"
HOME="$tmp" gemini --version
HOME="$tmp" gemini extensions install "$PWD" --consent
HOME="$tmp" gemini extensions link "$PWD/loom-core" --consent
HOME="$tmp" gemini extensions link "$PWD/loom-playbooks" --consent
HOME="$tmp" gemini extensions list
```

Expected result when applicable:

- Repository-root install should not be treated as a valid Gemini split-package
  route because the root is no longer a Gemini extension root.
- Explicit local links to `loom-core/` and `loom-playbooks/` should succeed if the
  package-root extension skeletons are valid for local/developer use.
- `gemini extensions list` should show `loom-core` with `gemini-bootstrap.md` as
  context and should show separate core and playbook skill sets.

Actual observed result:

- `gemini --version` printed `0.34.0` and exited `0`.
- `gemini extensions install "$PWD" --consent` failed with:

```text
Configuration file not found at /Users/alexanderbutler/code_projects/personal/agent-loom/gemini-extension.json
ROOT_INSTALL_EXIT=1
```

- `gemini extensions link "$PWD/loom-core" --consent` printed:

```text
Extension "loom-core" linked successfully and enabled.
CORE_LINK_EXIT=0
```

- `gemini extensions link "$PWD/loom-playbooks" --consent` printed:

```text
Extension "loom-playbooks" linked successfully and enabled.
PLAYBOOKS_LINK_EXIT=0
```

- `gemini extensions list` showed both linked extensions enabled. `loom-core`
  listed `loom-core/gemini-bootstrap.md` under context files and listed 15 core
  skills from `using-loom` through `loom-constitution`. `loom-playbooks` listed 7
  playbook skills: `loom-spike`, `loom-skill-authoring`, `loom-ship`,
  `loom-drive`, `loom-git`, `loom-debugging`, and `loom-codemap`.

Procedure verdict / exit code: mixed but expected. Root install failed with exit
code `1`; core link, playbooks link, and extension list each exited `0`.

# Artifacts

Relevant command excerpts:

```text
0.34.0
VERSION_EXIT=0
Configuration file not found at /Users/alexanderbutler/code_projects/personal/agent-loom/gemini-extension.json
ROOT_INSTALL_EXIT=1
Extension "loom-core" linked successfully and enabled.
CORE_LINK_EXIT=0
Extension "loom-playbooks" linked successfully and enabled.
PLAYBOOKS_LINK_EXIT=0
✓ loom-core (0.1.0)
 Context files:
  /Users/alexanderbutler/code_projects/personal/agent-loom/loom-core/gemini-bootstrap.md
 Agent skills:
  using-loom: Use Loom before work...
  loom-workspace: Orient and route Loom work...
  loom-wiki: Maintain accepted explanation...
  loom-tickets: Maintain bounded execution and acceptance...
  loom-specs: Define intended behavior and acceptance contracts...
  loom-retrospective: Run Loom's compounding pass before closure...
  loom-research: Preserve reusable investigations...
  loom-records: Use Loom's shared record grammar...
  loom-ralph: Run Ralph implementation packets...
  loom-plans: Decompose high-level work into ticket-ready execution units...
  loom-memory: Maintain support recall...
  loom-initiatives: Maintain strategic outcome framing...
  loom-evidence: Preserve observed artifacts as evidence...
  loom-critique: Run adversarial review...
  loom-constitution: Maintain durable project identity and constraints...
✓ loom-playbooks (0.1.0)
 Agent skills:
  loom-spike: Run bounded spike or sketch investigations...
  loom-skill-authoring: Maintain Loom-compatible skills...
  loom-ship: Package already-truthful Loom work...
  loom-drive: Drive delegated objectives through Loom owner layers...
  loom-git: Coordinate Git isolation and provenance for Loom work...
  loom-debugging: Run reproduce-first debugging...
  loom-codemap: Map repository or module structure...
LIST_EXIT=0
```

The command output also printed a synthetic temporary-home project-registry save
warning before the version output. The warning did not prevent the observed
link/list commands from succeeding, but it is a limitation of the temp-home probe.

# Raw Artifact Store

- Path: None - key command excerpts are recorded directly in this evidence.
- Captured artifacts: None.
- Key excerpts / index: N/A.
- Redaction / sensitivity: no secrets, tokens, or private data captured; local
  filesystem paths are non-sensitive operational context for this repository.
- Retention / tracking: N/A.

# Visual / Product Evidence

N/A.

# Supports Claims

- spec:core-and-playbooks-package-contract#ACC-006 — partially supports the Gemini
  route by showing local package-root linking works. Root-core install behavior is
  superseded by `evidence:gemini-root-core-shim-check`.
- ticket:sbzmrvqv — supports the local-link-supported disposition for the earlier
  Gemini route.
- research:gemini-extension-subdirectory-feasibility — corroborates the conclusion
  that package-root Gemini skeletons are useful for explicit local linking.

# Challenges Claims

- None active. The failed root install challenged root install only for this earlier
  source state and is superseded for current root-core install behavior.

# Environment

Commit: `d021bc1` with uncommitted split-package worktree changes.

Branch: `main`.

Runtime: Gemini CLI `0.34.0` from `/run/current-system/sw/bin/gemini`.

OS: macOS / Darwin under the current OpenCode shell environment.

Relevant config: `HOME` was set to a temporary directory under
`/var/folders/1b/6mg4g2fs2zx99h46b9j5r7mh0000gp/T/opencode/` and removed after
the probe.

External service / harness / data source when applicable: local Gemini CLI only;
no remote Gemini repository or release artifact was installed.

# Validity

Valid for: current local Gemini CLI `0.34.0` behavior against this worktree's
`loom-core/` and `loom-playbooks/` package-root extension skeletons.

Fresh enough for: local package-root link behavior. Not fresh for current
repository-root core install behavior after `decision:0009` and
`evidence:gemini-root-core-shim-check`.

Recheck when: Gemini CLI version changes, Gemini extension docs add subdirectory
install support, `loom-core/gemini-extension.json` changes,
`loom-playbooks/gemini-extension.json` changes, a remote distribution artifact is
created, or public Gemini install docs are drafted.

Invalidated by: successful observed `gemini extensions install <source>` from a
validated remote source for each package root, or upstream support for extension
subdirectory install that changes the command semantics.

Supersedes / superseded by: superseded by
`evidence:gemini-root-core-shim-check` for repository-root core install behavior;
still current for explicit local package-root link behavior at the observed source
state.

# Limitations

- This evidence does not validate remote Gemini install from a Git URL, GitHub
  release, distribution branch, or separate repository.
- This evidence does not validate an interactive Gemini session's context ordering
  beyond `extensions list` showing the core context file.
- This evidence does not validate Gemini hooks, and no hooks are needed for the
  current static preload claim.
- This evidence does not update public documentation or close the ticket's
  mandatory critique gate.

# Result

The observed package-root Gemini skeleton is valid for explicit local linking of
`loom-core/` and `loom-playbooks/`. At this earlier source state, the repository
root was not a valid Gemini extension root; later root-core behavior is superseded
by `evidence:gemini-root-core-shim-check`.

# Interpretation

The justified ticket-level interpretation for this earlier source state is
local-link-supported and remote-deferred for Gemini. After `decision:0009`, this
evidence no longer speaks to current repository-root core install behavior, and it
still does not justify claiming seamless one-repository two-extension Gemini
install support.

# Related Records

- ticket:sbzmrvqv
- spec:core-and-playbooks-package-contract
- research:gemini-extension-subdirectory-feasibility
- decision:0008
