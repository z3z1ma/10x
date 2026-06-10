# Compression Inventory Baseline

Status: recorded
Created: 2026-05-25
Updated: 2026-05-25
Observed: 2026-05-25

## Related Records

- `.loom/tickets/done/20260525-compression-contract-inventory.md`
- `.loom/tickets/20260525-loom-protocol-compression.md`
- `.loom/specs/loom-protocol-compression.md`
- `.loom/decisions/project-constitution.md`
- `roadmap:loom-mill`
- `.loom/research/20260524-loom-mill-software-factory.md`

## Procedure

Commands were run from `/Users/alexanderbutler/code_projects/personal/agent-loom`.

- `git status --short`
- `python3 - <<'PY' ... PY` line-count inventory over the ticket's model-visible surface categories using `pathlib.Path.glob()` and UTF-8 text line splitting.
- Corrective `python3 - <<'PY' ... PY` count for agent and hook directories after the first script's `**` directory glob omitted files under `loom-core/agents/`, `loom-core/codex/agents/`, and `loom-core/hooks/`.
- Targeted `grep` tool searches for possible contributor/product-surface leakage terms and for duplicated Loom behavior terms across Core skills, agents, Codex agents, and Playbooks.
- Manual record/source inspection of the ticket's related records, active specs, AGENTS.md, source inventory paths, and generated command surfaces.

## Observations

`git status --short` before evidence/ticket edits showed one pre-existing ticket edit from this run boundary: `.loom/tickets/done/20260525-compression-contract-inventory.md` had already moved from `open` to `active` and recorded launch state.

Baseline line counts observed for inventory categories:

| Category | Files | Lines | Notes |
|---|---:|---:|---|
| Core skills markdown | 62 | 7,254 | `loom-core/skills/**/*.md`, including skills, references, and templates. |
| Core agents | 2 | 446 | `loom-core/agents/loom-driver.md`, `loom-core/agents/loom-weaver.md`. |
| Core Codex agents | 2 | 444 | `loom-core/codex/agents/loom-driver.toml`, `loom-core/codex/agents/loom-weaver.toml`. |
| Playbook markdown | 25 | 3,945 | `loom-playbooks/playbooks/**/SKILL.md`. |
| Generated Playbook commands | 25 | 3,970 | `loom-playbooks/commands/*.toml`; each generated command is roughly source Playbook body plus TOML framing. |
| Core preload and entrypoint surfaces | 4 | 539 | `loom-core/loom-core.mjs`, `loom-core/gemini-bootstrap.md`, `loom-core/hooks/hooks.json`, `loom-core/hooks/hooks-cursor.json`. |
| Protocol docs | 5 | 931 | `README.md`, `PROTOCOL.md`, `ARCHITECTURE.md`, `loom-core/README.md`, `loom-playbooks/README.md`. |
| Inventory-relevant package manifests | 3 | 119 | Root, Core, and Playbooks `package.json` files. |
| Inventory-relevant activation tests | 4 | 352 | `tests/explicit-skill-requests/*.sh`, `tests/skill-triggering/*.sh`. |

Corrected total baseline across these inventory categories: 18,000 lines in 132 files.

Source and record inspection found these surface categories for later compression:

- Core session kernel: `using-loom` skill, ordered references, OpenCode preload transform, hook bootstrap files, and Gemini bootstrap.
- Core record stations: constitution, specs, plans, tickets, research, evidence, audit, knowledge, retrospective, and Ralph skills with references/templates.
- Agent prompt kernels: canonical Driver/Weaver markdown plus Codex TOML copies.
- Optional Playbook macro corpus and generated OpenCode command TOML mirrors.
- Human docs and tests that restate or validate protocol behavior, while not being reliable model-visible doctrine unless a harness injects them.

Notable risk areas for later compression:

- `using-loom` has multiple preload mirrors; compression must keep ordered references, OpenCode transform output, hooks, and Gemini bootstrap aligned.
- Playbook command files duplicate Playbook source bodies; generated surfaces need regeneration or synchronized edits, not hand drift.
- Driver/Weaver behavior appears in canonical markdown and Codex TOML copies; compression should preserve role semantics in both.
- Core record skills repeat surface ownership, evidence, audit, and closure doctrine across many files; this is a large compression target but also a guardrail-loss risk.
- Product-surface leakage searches returned broad hits for ordinary words like `repository`, `package`, `adapter`, and `report`; many are legitimate runtime concepts, but future compression should distinguish runtime source inspection from contributor-only package/smoke/dogfood process.

Contract consistency inspection:

- `.loom/specs/loom-protocol-compression.md` is active and matches `.loom/decisions/project-constitution.md` lines 62-69 and 90-98 on operational kernels, portability, protocol/Mill split, and compression as current direction.
- It matches `roadmap:loom-mill` lines 15-31 and 53-58 on protocol compression as the foundation chapter and the compression/completeness tension.
- It matches `.loom/research/20260524-loom-mill-software-factory.md` findings 2 and 10: the protocol is sound, too verbose, portable, and independent of Mill.
- It does not conflict with active specs inspected: `.loom/specs/ticket-owned-worker-handoffs.md`, `.loom/specs/loom-driver-agent.md`, `.loom/specs/loom-weaver-agent.md`, or `.loom/specs/playbook-explicit-macros.md`. Those specs define behaviors the compression spec explicitly preserves or leaves adjacent.
- Source inventory did not reveal a missing major model-visible surface beyond the plan's named categories. Core hooks/preload files are important under the session kernel slice, and tests/manifests are inventory-relevant rather than compression doctrine surfaces.

## What This Shows

- `.loom/tickets/done/20260525-compression-contract-inventory.md#ACC-001` is supported by inspection showing the compression spec is active and no contradiction was found with the current constitution, roadmap, research, active specs, or observed source inventory.
- `.loom/tickets/done/20260525-compression-contract-inventory.md#ACC-002` is supported by the baseline inventory and line-count categories above, including Core skills/references/templates, Core agents, Codex agent copies, Playbooks, generated commands, preload surfaces, docs, tests, and manifests relevant to inventory.
- `.loom/tickets/done/20260525-compression-contract-inventory.md#ACC-003` is supported by inspection showing no plan or downstream-ticket update was required for missing slices, wrong sequencing, or unsafe compression boundary. Core preload/hooks are already included in the session-kernel unit; Playbooks/generated commands/docs/tests are already included in later plan units or validation.

## What This Does Not Show

- This evidence does not prove later compression preserves behavior.
- This evidence does not audit the final compressed source surface.
- This evidence does not prove generated command files are currently synchronized byte-for-byte with Playbook source, only that the line-count baseline and category relationship were observed.
- This evidence does not replace package smoke, pack checks, Markdown diff checks, targeted behavior/leakage searches after source edits, or the final Ralph-backed audit planned in `.loom/tickets/done/20260525-compression-validation-audit.md`.
