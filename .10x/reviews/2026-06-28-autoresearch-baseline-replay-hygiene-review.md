Status: recorded
Created: 2026-06-28
Updated: 2026-06-28
Target: .10x/evidence/2026-06-28-autoresearch-baseline-replay-hygiene.md
Verdict: pass

# Autoresearch Baseline Replay Hygiene Review

## Target

Review of replay-hygiene changes and evidence record
`.10x/evidence/2026-06-28-autoresearch-baseline-replay-hygiene.md`.

## Findings

- Pass: The deterministic seed-backed inventory is now tracked in
  `index.json`, and the 44 historical exclusions have a separate tracked ledger
  with exact class counts and rationale.
- Pass: Continuation definitions that depend on ignored `.storage` raw artifacts
  are no longer ambiguous baseline inputs; they are explicitly outside the
  seed-backed baseline until promoted to tracked seeds.
- Pass: OpenCode prerequisite behavior is materially better. Missing binaries
  fail with a clear message, and the installed user-local binary is discovered
  without requiring ad hoc `PATH` edits.
- Pass: `.opencode/node_modules/**` is filtered only from summaries, not from the
  archived workspace. The raw/manifest suppression count and sample keep the
  omission inspectable.
- Minor: The historical exclusions are classified, not converted into new seed
  packages. This is an intentional simplicity choice and matches the ticket's
  "or explicitly classified" path.

## Verdict

Pass.

The replay-hygiene acceptance criteria are satisfied without adding another
runner path or reintroducing fixture-backed machinery.

## Residual Risk

- If a future OpenCode version writes meaningful non-generated changes under
  `.opencode/node_modules/**`, those changes will be summarized only through the
  suppression count/sample and archived workspace inspection.
- Provider credentials and model access remain runtime prerequisites outside the
  runner's full control.
