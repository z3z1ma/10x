Status: done
Created: 2026-06-27
Updated: 2026-06-27
Depends-On: .10x/specs/10x-autoresearch-loop.md, .10x/tickets/2026-06-27-simplify-autoresearch-subject-runner.md

# Harden Autoresearch Instruction Delivery

## Scope

Make live subject instruction delivery explicit, harness-isolated, and
evidence-backed for Codex and OpenCode.

Included:

- Remove the prompt-wrapper instruction channel from new live subject runs.
- Deliver non-empty arm instructions through the harness instruction channel:
  Codex `developer_instructions` and OpenCode custom primary-agent `prompt`.
- Allow an explicitly empty arm instruction to mean no runner-supplied
  instruction layer beyond the subject harness defaults and the scenario prompt.
- Run OpenCode with `--pure` and Codex with `--ignore-rules` in addition to the
  existing isolation flags.
- Record instruction delivery metadata, instruction artifacts, command argv,
  and environment/config references without leaking full instructions into argv
  metadata.
- Update tests, docs, evidence, and review.

Excluded:

- Replacing Codex built-in model instructions.
- Inventing an OpenCode flag that disables built-in system prompts or all user
  configuration when the CLI does not document one.
- Changing the scientist's grading responsibility or the scenario catalog.

## Acceptance Criteria

- AC-001: New prompts contain only the scenario conversation and prior
  transcript, not wrapper instruction tags.
- AC-002: Codex plans include one canonical `planned_argv`, use
  `developer_instructions` for non-empty arm instructions, include
  `--ignore-rules`, and redact instruction text from public argv metadata.
- AC-003: OpenCode plans include one canonical `planned_argv`, run with
  `--pure`, use a custom agent prompt for non-empty arm instructions, and record
  the config/environment path needed to reproduce the run.
- AC-004: Empty `instruction_text` means no runner-supplied instruction layer.
- AC-005: Tests, validator, py_compile, diff check, and an empirical OpenCode
  config probe pass.

## Progress and Notes

- 2026-06-27: Opened after local help and official docs showed OpenCode `--pure`
  isolates plugins but is not a blank-system-prompt switch; OpenCode custom
  agents expose `prompt` as the system-prompt channel, and Codex exposes
  `developer_instructions` as the documented append-like instruction channel.
- 2026-06-27: Removed prompt-wrapper instruction delivery from new live subject
  runs; added instruction artifacts, `instruction_delivery` metadata, Codex
  `developer_instructions`, OpenCode `--pure` plus custom agent prompt config,
  empty-instruction controls, public argv instruction redaction, report
  instruction-delivery surfacing, docs/spec updates, evidence, and review.
  Evidence: `.10x/evidence/2026-06-27-autoresearch-instruction-delivery.md`.
  Review:
  `.10x/reviews/2026-06-27-autoresearch-instruction-delivery-review.md`.

## Blockers

None.

## Closure

All acceptance criteria met. New runs separate scenario prompts from arm
instructions, use one harness-neutral runner schema, record exact instruction
artifacts and delivery metadata, and preserve the documented limits of Codex
and OpenCode prompt control.
