#!/usr/bin/env bash

set -euo pipefail
export LC_ALL=C

hook_input="$(cat || true)"
plugin_root="${CLAUDE_PLUGIN_ROOT:-}"

if [ -z "$plugin_root" ]; then
  script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
  plugin_root="$(CDPATH= cd -- "$script_dir/.." && pwd)"
fi

src_dir="$plugin_root/rules"
project_dir="${CLAUDE_PROJECT_DIR:-}"
plugin_data="${CLAUDE_PLUGIN_DATA:-${HOME:?missing HOME}/.claude/plugins/data/loom}"
dest_dir=""
dest_scope=""

session_id="$(printf '%s' "$hook_input" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')"
marker_key=""

if [ -n "$session_id" ]; then
  marker_key="$(printf '%s' "$session_id" | cksum)"
  marker_key="${marker_key%% *}"
fi

marker_path() {
  [ -n "$marker_key" ] || return 1
  printf '%s/%s/%s' "$plugin_data" "$1" "$marker_key"
}

write_marker() {
  local type message marker
  type="$1"
  message="${2:-}"
  marker="$(marker_path "$type")" || return 0
  mkdir -p "${marker%/*}"
  printf '%s\n%s\n' "$dest_dir" "$message" > "$marker"
}

clear_markers() {
  local marker
  marker="$(marker_path restart-required)" && rm -f "$marker"
  marker="$(marker_path sync-failed)" && rm -f "$marker"
  marker="$(marker_path sync-pending)" && rm -f "$marker"
  return 0
}

fail_closed() {
  local message
  message="$1"
  trap - ERR
  write_marker sync-failed "$message"
  exit 0
}

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

settings_loom_state() {
  local file compact
  file="$1"

  if command -v python3 >/dev/null 2>&1; then
    python3 - "$file" <<'PY'
import json
import sys

try:
    with open(sys.argv[1], "r", encoding="utf-8") as handle:
        data = json.load(handle)
except Exception:
    sys.exit(3)

enabled = data.get("enabledPlugins")
if enabled is None:
    sys.exit(1)
if not isinstance(enabled, dict):
    sys.exit(3)

state = None
for key, value in enabled.items():
    if key == "loom" or key.startswith("loom@"):
        if not isinstance(value, bool):
            sys.exit(3)
        state = value

if state is None:
    sys.exit(1)
sys.exit(0 if state else 2)
PY
    return $?
  fi

  compact="$(LC_ALL=C tr -d '[:space:]' < "$file")" || return 3
  case "$compact" in
    *'"enabledPlugins":{'*) ;;
    *) return 1 ;;
  esac

  if printf '%s' "$compact" | grep -Eq '"enabledPlugins":\{[^}]*"loom(@[^"]*)?":false'; then
    return 2
  fi
  if printf '%s' "$compact" | grep -Eq '"enabledPlugins":\{[^}]*"loom(@[^"]*)?":true'; then
    return 0
  fi
  return 1
}

project_enables_loom() {
  [ -n "$project_dir" ] || return 1

  local settings_file state rc
  state="missing"

  for settings_file in \
    "$project_dir/.claude/settings.json" \
    "$project_dir/.claude/settings.local.json"
  do
    [ -f "$settings_file" ] || continue
    set +e
    settings_loom_state "$settings_file"
    rc=$?
    set -e

    case "$rc" in
      0) state="true" ;;
      1) ;;
      2) state="false" ;;
      *) fail_closed "Could not parse Claude plugin settings: $settings_file" ;;
    esac
  done

  [ "$state" = "true" ]
}

ensure_dest_safe() {
  local dest_phys expected project_phys home_phys

  case "$dest_scope" in
    project)
      project_phys="$(CDPATH= cd -- "$project_dir" && pwd -P)" || fail_closed "Could not resolve Claude project directory: $project_dir"
      expected="$project_phys/.claude/rules/loom"
      [ ! -L "$project_dir/.claude" ] || fail_closed "Refusing to sync through symlinked Claude project config directory: $project_dir/.claude"
      [ ! -L "$project_dir/.claude/rules" ] || fail_closed "Refusing to sync through symlinked Claude project rules directory: $project_dir/.claude/rules"
      ;;
    user)
      home_phys="$(CDPATH= cd -- "${HOME:?missing HOME}" && pwd -P)" || fail_closed "Could not resolve HOME"
      expected="$home_phys/.claude/rules/loom"
      [ ! -L "$HOME/.claude" ] || fail_closed "Refusing to sync through symlinked Claude user config directory: $HOME/.claude"
      [ ! -L "$HOME/.claude/rules" ] || fail_closed "Refusing to sync through symlinked Claude user rules directory: $HOME/.claude/rules"
      ;;
    override)
      [ ! -L "$dest_dir" ] || fail_closed "Refusing to sync Loom rules into a symlinked directory: $dest_dir"
      mkdir -p "$dest_dir"
      return 0
      ;;
    *)
      fail_closed "Unknown Loom rule destination scope: $dest_scope"
      ;;
  esac

  [ ! -L "$dest_dir" ] || fail_closed "Refusing to sync Loom rules into a symlinked directory: $dest_dir"
  mkdir -p "$dest_dir"
  dest_phys="$(CDPATH= cd -- "$dest_dir" && pwd -P)" || fail_closed "Could not resolve Loom rules directory: $dest_dir"

  if [ "$dest_phys" != "$expected" ]; then
    fail_closed "Refusing to sync Loom rules outside expected $dest_scope scope: $dest_dir"
  fi
}

trap 'fail_closed "Loom Claude rule sync failed before completion."' ERR
trap 'fail_closed "Loom Claude rule sync was interrupted before completion."' HUP INT TERM

if [ -n "${CLAUDE_LOOM_RULES_DIR:-}" ]; then
  dest_dir="$CLAUDE_LOOM_RULES_DIR"
  dest_scope="override"
elif project_enables_loom; then
  dest_dir="$project_dir/.claude/rules/loom"
  dest_scope="project"
else
  dest_dir="${HOME:?missing HOME}/.claude/rules/loom"
  dest_scope="user"
fi

manifest="$dest_dir/.loom-plugin-manifest"
managed_rule="loom.md"

write_marker sync-pending "Loom rule synchronization did not finish."

if [ ! -d "$src_dir" ]; then
  fail_closed "Missing bundled Loom rules directory: $src_dir"
fi

ensure_dest_safe

managed_now="$(mktemp "$dest_dir/.loom-managed-now.XXXXXX")"
tmp_manifest="$(mktemp "$dest_dir/.loom-plugin-manifest.XXXXXX")"
tmp_rule="$(mktemp "$dest_dir/.loom-generated-rule.XXXXXX")"
trap 'rm -f "$managed_now" "$tmp_manifest" "$tmp_rule"' EXIT
trap 'fail_closed "Loom Claude rule sync failed before completion."' ERR

printf '%s\n' "$managed_rule" >> "$managed_now"

{
  printf '<!-- Generated by the Loom Claude plugin from canonical rules/*.md. Do not edit this file directly. -->\n\n'
  printf '# Loom Rules\n'
} > "$tmp_rule"

rule_count=0
for file in "$src_dir"/*.md; do
  [ -e "$file" ] || continue
  [ -f "$file" ] || continue
  name="${file##*/}"
  safe_rule_name "$name" || fail_closed "Unsafe bundled Loom rule filename: $name"
  {
    printf '\n\n<!-- source: rules/%s -->\n\n' "$name"
    cat "$file"
  } >> "$tmp_rule"
  rule_count=$((rule_count + 1))
done

if [ "$rule_count" -eq 0 ]; then
  fail_closed "No bundled Loom rule files found in: $src_dir"
fi

sort -u "$managed_now" > "$tmp_manifest"
mv "$tmp_manifest" "$managed_now"

if [ -L "$manifest" ]; then
  fail_closed "Refusing to read symlinked Loom managed manifest: $manifest"
fi

if [ -e "$manifest" ] && [ ! -f "$manifest" ]; then
  fail_closed "Refusing to read non-regular Loom managed manifest: $manifest"
fi

if [ -f "$manifest" ]; then
  while IFS= read -r old_name; do
    [ -n "$old_name" ] || continue
    safe_rule_name "$old_name" || fail_closed "Unsafe Loom managed manifest entry: $old_name"
  done < "$manifest"
fi

if [ -L "$dest_dir/$managed_rule" ]; then
  fail_closed "Refusing to overwrite symlinked Loom managed rule file: $dest_dir/$managed_rule"
fi

for dest_file in "$dest_dir"/*.md; do
  [ -e "$dest_file" ] || continue
  [ ! -L "$dest_file" ] || fail_closed "Refusing to manage symlinked Loom rule file: $dest_file"
  [ -f "$dest_file" ] || fail_closed "Refusing to manage non-regular Loom rule file: $dest_file"
  dest_name="${dest_file##*/}"
  safe_rule_name "$dest_name" || fail_closed "Unsafe Loom destination rule filename: $dest_name"
  if ! grep -Fxq "$dest_name" "$managed_now"; then
    if [ -f "$manifest" ] && grep -Fxq "$dest_name" "$manifest"; then
      continue
    fi
    fail_closed "Unmanaged Markdown file exists in Loom rules directory: $dest_file"
  fi
done

current=true

if [ ! -f "$manifest" ] || ! cmp -s "$manifest" "$managed_now"; then
  current=false
fi

if [ ! -f "$dest_dir/$managed_rule" ] || ! cmp -s "$tmp_rule" "$dest_dir/$managed_rule"; then
  current=false
fi

if [ "$current" = true ]; then
  clear_markers
  exit 0
fi

mv -f "$tmp_rule" "$dest_dir/$managed_rule"

if [ -f "$manifest" ]; then
  while IFS= read -r old_name; do
    [ -n "$old_name" ] || continue
    if ! grep -Fxq "$old_name" "$managed_now"; then
      rm -f "$dest_dir/$old_name"
    fi
  done < "$manifest"
fi

mv -f "$managed_now" "$manifest"
clear_markers
write_marker restart-required "Loom rules were installed or updated after Claude loaded instructions."
