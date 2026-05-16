#!/usr/bin/env bash
# Run natural-prompt Loom routing tests.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPTS_DIR="$SCRIPT_DIR/prompts"

TESTS=(
  "none:$PROMPTS_DIR/loom-idea-refine.txt"
  "none:$PROMPTS_DIR/loom-debugging-and-error-recovery.txt"
  "loom-tickets:$PROMPTS_DIR/loom-tickets.txt"
  "loom-ralph:$PROMPTS_DIR/loom-ralph.txt"
)

FAILED=0

for item in "${TESTS[@]}"; do
  skill="${item%%:*}"
  prompt="${item#*:}"
  if ! bash "$SCRIPT_DIR/run-test.sh" "$skill" "$prompt" 3; then
    FAILED=$((FAILED + 1))
  fi
done

echo "=== Playbook Explicit Invocation Static Coverage ==="
if ! npm --prefix "$SCRIPT_DIR/../../loom-playbooks" run smoke; then
  FAILED=$((FAILED + 1))
fi

if [[ $FAILED -gt 0 ]]; then
  echo "FAIL: $FAILED Loom routing test(s) failed"
  exit 1
fi

echo "PASS: all Loom routing tests passed"
