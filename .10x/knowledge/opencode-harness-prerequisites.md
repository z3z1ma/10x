Status: active
Created: 2026-06-27
Updated: 2026-06-27

# OpenCode Harness Prerequisites

Autoresearch can use OpenCode as a live subject harness with
`harness: opencode-cli`.

Required local state before a live OpenCode trial can succeed:

- The `opencode` executable is on `PATH`.
- OpenCode provider credentials are already configured for the user account.
- The requested model is usable by that account. For the current subscription
  setup, use the OpenCode provider/model ID `openai/gpt-5.5`.
- The experiment definition uses the same registered scientific contract, arms,
  scenarios, and budget fields as Codex subject runs.

Runner behavior:

- The runner invokes OpenCode as `opencode run --model <provider/model>
  --format json --dir <workspace> --dangerously-skip-permissions <prompt>`.
- Command metadata and process output are stored under `<out>/opencode/`.
- The runner runs each sample in a private temporary workspace and archives that
  workspace under `<out>/workspaces/`.
- OpenCode authenticated home state, provider configuration, and system context
  are outside complete runner control. Scientists must inspect command artifacts
  and workspace manifests before recording verdicts.
