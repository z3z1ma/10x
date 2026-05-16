#!/usr/bin/env bash
# Test Loom routing with natural prompts that do not name skills or Playbooks.
# Usage: bash tests/skill-triggering/run-test.sh <expected-core-skill|none> <prompt-file> [max-turns] [forbidden-playbook-csv]

set -euo pipefail

SKILL_NAME="${1:-}"
PROMPT_FILE="${2:-}"
MAX_TURNS="${3:-3}"
FORBIDDEN_PLAYBOOKS="${4:-}"

if [[ -z "$SKILL_NAME" || -z "$PROMPT_FILE" ]]; then
  echo "Usage: $0 <expected-core-skill|none> <prompt-file> [max-turns] [forbidden-playbook-csv]" >&2
  exit 2
fi

if ! command -v opencode >/dev/null 2>&1; then
  echo "SKIP: opencode not installed; cannot run Loom activation integration test"
  exit 0
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
TIMESTAMP="$(date +%s)"
OUTPUT_DIR="${LOOM_TEST_OUTPUT_DIR:-/tmp/loom-tests}/$TIMESTAMP/skill-triggering/$SKILL_NAME"
PROJECT_DIR="$OUTPUT_DIR/project"
LOG_FILE="$OUTPUT_DIR/opencode-output.json"

mkdir -p "$PROJECT_DIR"

cat > "$PROJECT_DIR/opencode.json" <<EOF
{
  "plugin": [
    "file://$REPO_ROOT/loom-core/loom-core.mjs",
    "file://$REPO_ROOT/loom-playbooks/loom-playbooks.mjs"
  ]
}
EOF

PROMPT="$(<"$PROMPT_FILE")"

echo "=== Loom Routing Test ==="
echo "Expected Core Skill: $SKILL_NAME"
echo "Prompt: $PROMPT_FILE"
echo "Max turns hint: $MAX_TURNS (OpenCode CLI currently uses timeout for this test)"
if [[ -n "$FORBIDDEN_PLAYBOOKS" ]]; then
  echo "Forbidden Playbooks: $FORBIDDEN_PLAYBOOKS"
fi
echo "Output: $LOG_FILE"

set +e
(
  cd "$PROJECT_DIR"
  timeout 300 opencode run --print-logs --format json --dangerously-skip-permissions "$PROMPT"
) > "$LOG_FILE" 2>&1
EXIT_CODE=$?
set -e

if [[ $EXIT_CODE -eq 124 ]]; then
  echo "FAIL: opencode timed out"
  exit 1
fi

if [[ -n "$FORBIDDEN_PLAYBOOKS" ]]; then
  IFS=',' read -r -a forbidden_names <<< "$FORBIDDEN_PLAYBOOKS"
  for forbidden in "${forbidden_names[@]}"; do
    forbidden="${forbidden//[[:space:]]/}"
    [[ -z "$forbidden" ]] && continue
    forbidden_pattern='"skill":"([^"/:]+[/|:])?'"$forbidden"'"|"name":"'"$forbidden"'"|"input":\{"name":"'"$forbidden"'"\}'
    if grep -Eq "$forbidden_pattern" "$LOG_FILE"; then
      echo "FAIL: forbidden Playbook '$forbidden' was detected from a natural prompt"
      echo "Skills mentioned in log:"
      grep -Eo '"skill":"[^"]+"|"name":"loom-[^"]+"|"name":"using-loom"' "$LOG_FILE" | sort -u || true
      echo "Full log: $LOG_FILE"
      exit 1
    fi
  done
fi

if [[ "$SKILL_NAME" == "none" ]]; then
  if grep -Eq 'using-loom|Use using-loom|loom-core|Loom' "$LOG_FILE"; then
    echo "PASS: natural prompt kept Playbooks out of implicit activation and Core routing remained visible"
    exit 0
  fi

  echo "FAIL: Core Loom routing was not visible in the log"
  echo "Full log: $LOG_FILE"
  exit 1
fi

SKILL_TOOL_PATTERN='"tool":"skill"|"name":"skill"|"name":"Skill"'
SKILL_NAME_PATTERN='"skill":"([^"/:]+[/|:])?'"$SKILL_NAME"'"|"name":"'"$SKILL_NAME"'"|\b'"$SKILL_NAME"'\b'

if grep -Eq "$SKILL_TOOL_PATTERN" "$LOG_FILE" && grep -Eq "$SKILL_NAME_PATTERN" "$LOG_FILE"; then
  echo "PASS: skill '$SKILL_NAME' was triggered"
  exit 0
fi

echo "FAIL: skill '$SKILL_NAME' was not detected"
echo "Skills mentioned in log:"
grep -Eo '"skill":"[^"]+"|"name":"loom-[^"]+"|"name":"using-loom"' "$LOG_FILE" | sort -u || true
echo "Full log: $LOG_FILE"
exit 1
