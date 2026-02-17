---
"id": "al-d94d"
"status": "review"
"deps": []
"links": []
"created": "2026-02-17T06:25:54Z"
"type": "task"
"priority": 1
"assignee": "z3z1ma"
"parent": "al-a1ba"
"tags":
- "sprint:Pack-Module-Improvements"
- "pack"
- "lockfile"
- "correctness"
"external": {}
---
# Pack lockfile resilience: strict validation + deterministic repair path

## Objective alignment
Improve pack module robustness by making lockfile handling explicit, deterministic, and resilient to malformed states.

## Scope
- Tighten lockfile validation in `src/agent_loom/pack/lock.py`.
- Define deterministic behavior for duplicate pack IDs / duplicate file entries / invalid schema fragments.
- Ensure `status`, `doctor`, and lifecycle actions handle bad lock states with clear operator guidance.
- Add regression tests for malformed lockfile scenarios.

## Non-goals
- Introducing lockfile version migrations beyond what is needed for current format.
- Reworking pack manifest semantics.
- Adding new CLI subcommands.

## Implementation plan
1. Add strict parse + validation layer in `load_lock()`:
   - validate top-level types,
   - reject or normalize duplicate IDs deterministically,
   - validate file entry path/hash invariants.
2. Define one repair strategy for recoverable states (e.g., deterministic de-duplication with warning) and one hard-fail path for unsafe/ambiguous states.
3. Ensure callers (`core.py` + `cli.py`) surface actionable messages that preserve current command ergonomics.
4. Add test coverage for:
   - malformed JSON shape,
   - duplicate pack entries,
   - duplicate file entries,
   - partial/invalid fields.
5. Keep lockfile write path stable (`save_lock`) and deterministic sort order.

## Verification commands
- `uv run ruff check .`
- `uv run basedpyright`
- `uv run pytest tests/test_pack_lifecycle.py`
- `uv run pytest tests/test_pack_cli_ux.py`

## Acceptance criteria
- Lockfile parse behavior is explicit for malformed and duplicate-entry states.
- `loom pack status/doctor` fail safely or repair deterministically per policy.
- Valid lockfiles remain backward-compatible in behavior.
- Tests cover corrupted/edge lockfile inputs.

## Risks / edge cases
- Strict validation may expose preexisting messy repos.
- Need to avoid silent data loss while repairing duplicates.
- Mitigation: deterministic rules + explicit warnings/tests for each branch.

## Notes

**2026-02-17T06:28:18Z**

Started work: auditing current pack lock load/save behavior and caller error handling before implementing strict validation + deterministic repair.

**2026-02-17T06:32:43Z**

Implemented strict lockfile parser in pack/lock.py with schema validation, sha/path invariants, deterministic dedupe repair for safe duplicate entries, and hard-fail on conflicting duplicates. Next: finalize CLI guidance/error handling + regression test pass.

**2026-02-17T06:34:33Z**

Validation + CLI UX + regression tests implemented. Verified: uv run ruff check . (pass), uv run basedpyright (pass), uv run pytest tests/test_pack_lifecycle.py (pass), uv run pytest tests/test_pack_cli_ux.py (pass). Full uv run pytest currently fails in existing unrelated suites (compound adapter hooks + loom init expectations), no failures in pack suites.

**2026-02-17T06:35:28Z**

Committed 1763178: strict lock schema validation (top-level + pack + file entry invariants), deterministic duplicate repair path (safe dedupe + lock rewrite), hard-fail on conflicting duplicates, CLI LOCK_INVALID error envelope with actionable hint, and malformed-lock regression tests in lifecycle + CLI UX suites. Added changelog fragment .changes/unreleased/Fixed-20260216-233508.yaml.
