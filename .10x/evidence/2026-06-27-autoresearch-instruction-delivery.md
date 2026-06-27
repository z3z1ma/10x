Status: recorded
Created: 2026-06-27
Updated: 2026-06-27
Relates-To: .10x/tickets/2026-06-27-harden-autoresearch-instruction-delivery.md, .10x/specs/10x-autoresearch-loop.md

# Autoresearch Instruction Delivery Evidence

## What Was Observed

The live subject runner now separates scenario prompts from arm instructions.
Non-empty instructions are delivered through the harness instruction channel:
Codex `developer_instructions` for `codex-cli`, and an OpenCode custom
primary-agent `prompt` loaded through `OPENCODE_CONFIG` for `opencode-cli`.
Explicit empty `instruction_text` produces no runner-supplied instruction layer.

## Procedure

Documentation and local help inspected:

- `codex exec --help`: confirms `codex exec [PROMPT]` accepts initial
  instructions and supports `--ignore-user-config`, `--ignore-rules`, `--json`,
  `--output-last-message`, `--cd`, and sandbox flags.
- Fresh Codex manual fetched with
  `/mnt/c/Users/butle/.codex/skills/.system/openai-docs/scripts/fetch-codex-manual.mjs`.
  Relevant manual sections describe `developer_instructions` as additional
  instructions injected before `AGENTS.md`, `model_instructions_file` as a
  replacement for built-in base instructions, and non-interactive
  `--ignore-user-config` / `--ignore-rules` behavior.
- `opencode run --help`: confirms `--pure`, `--agent`, `--model`,
  `--format json`, `--dir`, and `--dangerously-skip-permissions`.
- Official OpenCode docs at `https://opencode.ai/docs/cli/` state `--pure`
  runs without external plugins and `agent create` creates a custom system
  prompt.
- Official OpenCode docs at `https://opencode.ai/docs/agents/` state agents can
  be configured in `opencode.json`, `prompt` specifies a custom system prompt
  file or inline prompt, and markdown/config agent names become selectable
  agents.
- Official OpenCode docs at `https://opencode.ai/docs/config/` state
  `OPENCODE_CONFIG` points at a custom config file and project/global config
  files are merged by precedence.

Commands run:

```bash
python3 -m unittest discover -s autoresearch/tests
python3 autoresearch/validate.py
python3 -m py_compile autoresearch/*.py
git diff --check
codex --config 'developer_instructions="AUTORESEARCH_SENTINEL"' exec --help
```

OpenCode config probe:

```bash
tmp=$(mktemp -d)
mkdir -p "$tmp/opencode" "$tmp/prompts"
printf '%s\n' 'AUTORESEARCH_SENTINEL_PROMPT' > "$tmp/prompts/sample.instructions.txt"
printf '%s\n' '{"$schema":"https://opencode.ai/config.json","agent":{"autoresearch-subject":{"mode":"primary","prompt":"{file:../prompts/sample.instructions.txt}","permission":{"edit":"allow","bash":"allow"}}}}' > "$tmp/opencode/sample.opencode.json"
(
  cd "$tmp" &&
  OPENCODE_CONFIG="$tmp/opencode/sample.opencode.json" \
  PATH="$HOME/.opencode/bin:$PATH" \
  opencode debug agent autoresearch-subject --pure --log-level ERROR --print-logs
)
```

Result: `opencode debug agent autoresearch-subject` returned resolved JSON with
`"prompt": "AUTORESEARCH_SENTINEL_PROMPT"`, confirming the runner's planned
config-file-plus-instruction-file shape resolves before any model call.

Validation results:

- `python3 -m unittest discover -s autoresearch/tests`: 55 tests, OK.
- `python3 autoresearch/validate.py`: `autoresearch contracts valid`.
- `python3 -m py_compile autoresearch/*.py`: OK.
- `git diff --check`: OK.
- Codex config syntax probe printed `codex exec --help` successfully with the
  `developer_instructions` override present.
- Dry-run public plans for both `codex-cli` and `opencode-cli` used only
  harness-neutral artifact keys (`raw`, `workspaces`, `harness`, `prompts`),
  contained no `planned_codex_argv`, `planned_opencode_argv`, or
  `planned_subject_argv`, recorded `.instructions.txt` instruction artifacts,
  and showed `instruction_delivery.prompt_wrapper = false`.

## What This Supports Or Challenges

Supports:

- New Codex plans and command metadata can use `developer_instructions` without
  replacing Codex built-in base instructions.
- New OpenCode plans and command metadata can use `--pure` plus a custom
  primary-agent prompt loaded from saved artifacts.
- Empty `instruction_text` is now a real no-runner-instruction control path.
- Prompt artifacts no longer need wrapper tags; instruction artifacts preserve
  the exact delivered arm instruction text.

Challenges:

- `--pure` is not a blank-system-prompt switch. It only suppresses external
  plugins.
- Neither harness gives the runner authority over the vendor-shipped built-in
  system context or authenticated home/provider configuration. The runner can
  isolate and record its own instruction layer, not prove absence of all
  upstream implementation context.

## Limits

This evidence verifies CLI help, official docs, no-model config resolution, and
unit/static contracts. It does not prove model behavior quality; comparative
live Codex/OpenCode trials provide that separate evidence.
