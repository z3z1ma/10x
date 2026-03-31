# AGENTS.md

## Repo Shape

This repository is the source tree for Loom's portable `src/rules/` and `src/skills/` bundle.

The main maintained surfaces are:
- `src/rules/`
- `src/skills/`
- `build/shared/`
- `src/rules/appendices/`

Treat it as a Markdown-first product with bundled Python helpers.
Do not assume a normal app layout, package manager workflow, service runtime, or test framework.

## Distributable Artifact

Treat `src/rules/` and `src/skills/` as the packaged Loom artifact.

- package-facing docs inside those surfaces must use package-local paths such as `scripts/...`, `references/...`, and sibling files under `src/rules/` or `src/skills/`
- do not point bundled operator guidance at source-repo-only paths like `build/shared/...` or `build/assemble-skills.py`
- `build/shared/` is assembly source for maintainers, not a packaged invocation surface for operators
- if you are documenting a bundled script in a skill, document it through that skill's `scripts/` path and local references, not through the build source path

## Directory Roles

- `src/rules/`: always-on doctrine source.
- `src/rules/appendices/`: supporting schema, naming, validation, and invocation guidance.
- `src/skills/`: subsystem skill source; each skill should stay self-contained.
- `build/shared/`: shared helpers used to assemble skill-local script bundles.

`build/assemble-skills.py` is the assembly source for the copied skill-local scripts.

## Tooling Reality

The repo has no `package.json`, `pyproject.toml`, `Makefile`, ESLint config, Prettier config, or dedicated unit-test runner.
The only repo-maintenance command agents generally need here is the assembly step.

## Command Reference

Assembly:

```bash
python3 build/assemble-skills.py
```

This copies skill-local scripts from `build/shared/scripts/` to each skill's `scripts/` directory, where they are expected by the skill's `SKILL.md` and references.

## Python Style

Match the existing helper style in `build/assemble-skills.py` and `build/shared/scripts/*.py`.
- Use `#!/usr/bin/env python3` for executable scripts.
- Use `from __future__ import annotations`.
- Prefer standard-library-only code unless the repo already introduces a dependency.
- Prefer `pathlib.Path` for path work.
- Write small CLI entrypoints with `argparse`.
- Use `main() -> int` and `raise SystemExit(main())`.
- Add type hints to functions and non-trivial locals.
- Prefer modern built-in generics such as `dict[str, ...]` and `list[str]`.
- Keep functions small, direct, and deterministic.
- For JSON output, prefer `json.dumps(..., indent=2, sort_keys=True)`.
- Keep imports simple and readable.
- Default to standard-library imports only.
- Preserve the surrounding file's formatting style instead of restyling unrelated code.
- Keep prose and code examples direct rather than decorative.

## Error Handling

- Fail closed when scope, ownership, or authority is ambiguous.
- Raise explicit errors instead of guessing.
- Prefer clear `SystemExit` messages in CLI tools.
- Treat missing required files, malformed frontmatter, and invalid statuses as hard failures.
- Do not silently widen scope, write authority, or packet behavior.

## Editing Guidance

- Prefer the smallest correct change.
- Keep changes portable across harnesses.
- Do not invent a monolithic Loom CLI unless the repo explicitly moves there.
- Do not add new dependencies or scaffolding without a concrete need.
- When changing a rule, check related skills, references, and helper scripts.
- When writing or editing content under `src/rules/` or `src/skills/`, keep examples and references package-local; never leak `build/` implementation paths into shipped operator docs unless the doc is explicitly about source-tree maintenance.

If a change crosses surfaces, review:
- `src/rules/` doctrine wording
- `src/skills/*/SKILL.md`
- skill reference docs under `src/skills/*/references/`
- shared helper scripts under `build/shared/scripts/`
- assembly logic in `build/assemble-skills.py`
