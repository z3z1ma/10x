#!/usr/bin/env bash

set -euo pipefail

hook_input="$(cat || true)"
plugin_data="${CLAUDE_PLUGIN_DATA:-${HOME:?missing HOME}/.claude/plugins/data/loom}"
session_id="$(printf '%s' "$hook_input" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')"

if [ -z "$session_id" ]; then
  exit 0
fi

marker_key="$(printf '%s' "$session_id" | cksum)"
marker_key="${marker_key%% *}"

json_escape() {
  local value
  value="$1"
  value="${value//\\/\\\\}"
  value="${value//\"/\\\"}"
  value="${value//$'\n'/\\n}"
  value="${value//$'\r'/\\r}"
  value="${value//$'\t'/\\t}"
  printf '%s' "$value"
}

block_prompt() {
  local reason escaped_reason
  reason="$1"
  escaped_reason="$(json_escape "$reason")"
  printf '{"decision":"block","reason":"%s"}\n' "$escaped_reason"
}

failure_marker="$plugin_data/sync-failed/$marker_key"
restart_marker="$plugin_data/restart-required/$marker_key"
pending_marker="$plugin_data/sync-pending/$marker_key"

if [ -f "$failure_marker" ]; then
  rules_dir="$(sed -n '1p' "$failure_marker" 2>/dev/null || true)"
  message="$(sed -n '2p' "$failure_marker" 2>/dev/null || true)"
  [ -n "$rules_dir" ] || rules_dir="the Claude rules directory"
  [ -n "$message" ] || message="Loom rule synchronization failed."
  block_prompt "Loom rules could not be synchronized for this Claude session at $rules_dir: $message Your prompt was not processed because Loom operating knowledge may be missing. Fix the sync issue, then start a new Claude session and resubmit the prompt."
  exit 0
fi

if [ ! -f "$restart_marker" ]; then
  if [ ! -f "$pending_marker" ]; then
    exit 0
  fi

  rules_dir="$(sed -n '1p' "$pending_marker" 2>/dev/null || true)"
  message="$(sed -n '2p' "$pending_marker" 2>/dev/null || true)"
  [ -n "$rules_dir" ] || rules_dir="the Claude rules directory"
  [ -n "$message" ] || message="Loom rule synchronization did not finish."
  block_prompt "Loom rule synchronization is still pending or did not finish for this Claude session at $rules_dir: $message Your prompt was not processed because Loom operating knowledge may be missing. Start a new Claude session and resubmit the prompt."
  exit 0
fi

rules_dir="$(sed -n '1p' "$restart_marker" 2>/dev/null || true)"

if [ -z "$rules_dir" ]; then
  rules_dir="the Claude rules directory"
fi

block_prompt "Loom rules were just installed at $rules_dir, but Claude loaded instructions before those files existed. Your prompt was not processed. Start a new Claude session in this project, then resubmit the prompt so Loom always-on rules are loaded."
