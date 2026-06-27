Status: done
Created: 2026-06-27
Updated: 2026-06-27

# OpenCode CLI Harness Research

## Question

What is the current OpenCode CLI contract needed to run OpenCode as a live
autoresearch subject harness with `openai/gpt-5.5`?

## Sources And Methods

- Read official OpenCode CLI documentation:
  `https://opencode.ai/docs/cli/`.
- Read the official OpenCode installer script from
  `https://opencode.ai/install`.
- Installed OpenCode 1.17.11 with the official installer.
- Ran local help:
  `$HOME/.opencode/bin/opencode run --help`.
- Ran local credential inspection:
  `$HOME/.opencode/bin/opencode auth list`.
- Executed a live `run_once.py` smoke trial through OpenCode with
  `model: openai/gpt-5.5`.

## Findings

- OpenCode has a non-interactive `opencode run [message..]` command.
- `opencode run` supports `--model` with provider/model syntax; local help says
  the model format is `provider/model`.
- `opencode run` supports `--format json`, which emits raw JSON events suitable
  for command artifact capture.
- `opencode run` supports `--dir`, which sets the subject working directory.
- `opencode run` supports `--dangerously-skip-permissions`, which auto-approves
  permissions that are not explicitly denied. The autoresearch runner uses this
  only inside a private temporary workspace and records that limitation.
- OpenCode 1.17.11 stores token usage under JSON event `part.tokens`, not the
  Codex-style top-level `usage` field.
- Local credentials exist for OpenAI OAuth according to `opencode auth list`.
- The OpenCode binary installed to `$HOME/.opencode/bin/opencode`; the current
  shell did not already have `opencode` on `PATH`.

## Conclusions

The correct minimal OpenCode subject command for autoresearch is:

```bash
opencode run --model openai/gpt-5.5 --format json --dir <workspace> --dangerously-skip-permissions <prompt>
```

The runner should require `opencode` on `PATH` rather than guessing install
locations. Scientists can prefix `PATH="$HOME/.opencode/bin:$PATH"` when needed.

OpenCode can reach parity with the Codex harness for the current scientific
environment: command metadata, JSON stdout, stderr, last assistant message,
prompt artifact, raw trial artifact, workspace manifest, archived workspace,
summary, report, and canonical guard all exist.

## Limits

- OpenCode authenticated home state, provider configuration, plugins, and system
  context are outside complete runner control.
- The local live smoke proved `openai/gpt-5.5` access in this environment on
  2026-06-27, but model access can change.
