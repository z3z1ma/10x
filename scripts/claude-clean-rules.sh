#!/usr/bin/env bash

set -euo pipefail

target="${1:-user}"

safe_rule_name() {
  local name
  name="$1"
  case "$name" in
    ''|.*|*/*|*\\*|*..*|*[!A-Za-z0-9._-]*) return 1 ;;
  esac
  case "$name" in
    *.md) return 0 ;;
    *) return 1 ;;
  esac
}

case "$target" in
  user)
    rules_dir="${HOME:?missing HOME}/.claude/rules/loom"
    ;;
  project)
    project_dir="${CLAUDE_PROJECT_DIR:-$PWD}"
    rules_dir="$project_dir/.claude/rules/loom"
    ;;
  *)
    printf 'Usage: %s [user|project]\n' "$0" >&2
    exit 2
    ;;
esac

manifest="$rules_dir/.loom-plugin-manifest"

if [ ! -d "$rules_dir" ]; then
  exit 0
fi

if [ -L "$rules_dir" ]; then
  printf 'Refusing to clean symlinked Loom rules directory: %s\n' "$rules_dir" >&2
  exit 1
fi

if [ -L "$manifest" ]; then
  printf 'Refusing to clean symlinked Loom managed manifest: %s\n' "$manifest" >&2
  exit 1
fi

if [ -e "$manifest" ] && [ ! -f "$manifest" ]; then
  printf 'Refusing to clean non-regular Loom managed manifest: %s\n' "$manifest" >&2
  exit 1
fi

if [ ! -f "$manifest" ]; then
  printf 'Refusing to clean Loom rules without managed manifest: %s\n' "$rules_dir" >&2
  exit 1
fi

while IFS= read -r name; do
  [ -n "$name" ] || continue
  safe_rule_name "$name" || {
    printf 'Refusing unsafe managed manifest entry: %s\n' "$name" >&2
    exit 1
  }
  if [ -L "$rules_dir/$name" ]; then
    printf 'Refusing to clean symlinked Loom rule file: %s\n' "$rules_dir/$name" >&2
    exit 1
  fi
  rm -f "$rules_dir/$name"
done < "$manifest"

rm -f "$manifest"
rmdir "$rules_dir" 2>/dev/null || true
