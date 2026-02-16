# Loom Pack subsystem (agent guide)

Scope: `src/agent_loom/pack/**`

## What this module owns

Pack installs and maintains deterministic static assets (agents/skills/commands/docs) from pack manifests into a target repo, with checksum-based drift detection and lockfile tracking.

## Entry points

- CLI: `src/agent_loom/pack/cli.py` (`loom pack ...`)
- Business logic: `src/agent_loom/pack/core.py`
- Pack manifest discovery/loading: `src/agent_loom/pack/packs.py`
- Lockfile IO: `src/agent_loom/pack/lock.py`
- Diff output: `src/agent_loom/pack/diff.py`
- Data models: `src/agent_loom/pack/models.py`

## Control flow

Install/update/uninstall path:

1. `cli.py` parses command and resolves repo root.
2. `core.py` loads pack manifest and file inventory.
3. Managed/scaffold/protected sets are computed from manifest globs.
4. File writes/removals are applied with checksum + drift safeguards.
5. `.loom/pack/lock.json` is rewritten with current installed-state hashes.

Status/doctor path:

1. Load lockfile and manifests.
2. Re-scan managed files for drift/missing.
3. Emit summary (and textual diffs when requested).

## Internal module map

- `core.py`: lifecycle orchestration and drift policy.
- `packs.py`: pack ID listing, manifest loading, file iteration.
- `lock.py`: lockfile load/save + timestamp helpers.
- `diff.py`: textual diff computation/formatting for changed text files.
- `util.py`: checksums and safe filesystem helpers.
- `models.py`: manifest/lock/result dataclasses.

## Storage contract

- Pack definitions: `src/agent_loom/pack/packs/<pack-id>/`
  - `pack.yaml`
  - `files/**`
- Installed-state tracking: `.loom/pack/lock.json`

Manifest fields define install roots and glob semantics:

- `managed_globs`: tracked/managed files
- `scaffold_globs`: write-once files
- `protected_globs`: never overwrite/remove automatically

## Where to change code

- New CLI behavior: `cli.py`.
- Installation policy or drift semantics: `core.py`.
- Manifest schema/validation: `models.py` + `packs.py`.
- Lock format behavior: `lock.py` (+ migration handling if needed).
- Diff output style/limits: `diff.py`.

## Guardrails

- Preserve deterministic lockfile semantics.
- Never silently overwrite drifted managed files without explicit force behavior.
- Scaffold files remain non-destructive/write-once.
- Honor protected globs in install/update/uninstall flows.
- Keep all filesystem mutations rooted to resolved repo root.

## Fast tests for pack changes

- `uv run pytest tests/test_pack_cli_ux.py`
- `uv run pytest tests/test_pack_lifecycle.py`
- `uv run pytest tests/test_pack_loom_agile_core_invariants.py`
