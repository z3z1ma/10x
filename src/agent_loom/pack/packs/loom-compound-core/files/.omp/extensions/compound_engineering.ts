// OMP Compound adapter.
//
// Responsibilities:
// - Forward OMP extension events to Loom's OMP adapter command.
// - Keep harness-specific capture logic in Loom Python (`loom compound omp-hook`).

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import { spawn } from "node:child_process";

const DEFAULT_LOOM_BIN = process.env.COMPOUND_LOOM_BIN ?? "loom";
const LOG_OBSERVATIONS = (process.env.COMPOUND_LOG_OBSERVATIONS ?? "1") !== "0";

function _asString(v: unknown): string {
  return String(v ?? "").trim();
}

function _sessionId(event: any): string {
  return _asString(event?.session_id ?? event?.sessionID ?? event?.sessionId ?? event?.session?.id);
}

function _toolResponseFromResult(event: any): Record<string, unknown> {
  const details = event?.details && typeof event.details === "object" ? event.details : {};
  const content = event?.content;
  const output =
    typeof (details as any)?.stdout === "string"
      ? String((details as any).stdout)
      : typeof (details as any)?.output === "string"
        ? String((details as any).output)
        : typeof content === "string"
          ? content
          : JSON.stringify(content ?? "");

  const stderr = typeof (details as any)?.stderr === "string" ? String((details as any).stderr) : "";
  const codeRaw = (details as any)?.exitCode ?? (details as any)?.exit_code ?? (details as any)?.code;
  const response: Record<string, unknown> = {
    title: `tool_result:${_asString(event?.toolName || event?.tool_name || "unknown")}`,
    output,
    stderr,
    metadata: details,
  };
  if (typeof codeRaw === "number" && Number.isFinite(codeRaw)) {
    response.exitCode = Math.trunc(codeRaw);
  }
  return response;
}

function _emitHook(repoRoot: string, eventName: string, payload: Record<string, unknown>): void {
  const child = spawn(
    DEFAULT_LOOM_BIN,
    ["compound", "omp-hook", "--repo", repoRoot, "--event", eventName],
    { cwd: repoRoot, env: process.env, stdio: ["pipe", "ignore", "ignore"] }
  );
  child.on("error", () => {});
  child.stdin.on("error", () => {});
  const body = JSON.stringify(payload);
  child.stdin.write(body);
  child.stdin.end();
}

export default function (pi: ExtensionAPI) {
  const forward = (ctx: any, eventName: string, payload: Record<string, unknown>) => {
    if (!LOG_OBSERVATIONS) return;
    const repoRoot = _asString(ctx?.cwd) || process.cwd();
    try {
      _emitHook(repoRoot, eventName, payload);
    } catch {
      // swallow
    }
  };

  pi.on("before_agent_start", async (event, ctx) => {
    const prompt = _asString((event as any)?.prompt);
    forward(ctx, "before_agent_start", {
      event_name: "before_agent_start",
      session_id: _sessionId(event),
      prompt,
    });
  });

  pi.on("tool_call", async (event, ctx) => {
    forward(ctx, "tool_call", {
      event_name: "tool_call",
      session_id: _sessionId(event),
      tool_name: _asString((event as any)?.toolName ?? (event as any)?.tool_name),
      tool_input: ((event as any)?.input && typeof (event as any).input === "object") ? (event as any).input : {},
    });
  });

  pi.on("tool_result", async (event, ctx) => {
    forward(ctx, "tool_result", {
      event_name: "tool_result",
      session_id: _sessionId(event),
      tool_name: _asString((event as any)?.toolName ?? (event as any)?.tool_name),
      tool_input: ((event as any)?.input && typeof (event as any).input === "object") ? (event as any).input : {},
      tool_response: _toolResponseFromResult(event),
      is_error: Boolean((event as any)?.isError),
    });
  });

  pi.on("turn_end", async (event, ctx) => {
    forward(ctx, "turn_end", {
      event_name: "turn_end",
      session_id: _sessionId(event),
    });
  });
}
