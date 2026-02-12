// OpenCode Compound adapter.
//
// Responsibilities:
// - Forward OpenCode events to Loom's OpenCode adapter command.
// - Keep observation normalization and instincts logic in Loom Python.

import type { Plugin } from "@opencode-ai/plugin";
import { spawn } from "node:child_process";

const DEFAULT_LOOM_BIN = process.env.COMPOUND_LOOM_BIN ?? "loom";
const LOG_OBSERVATIONS = (process.env.COMPOUND_LOG_OBSERVATIONS ?? "1") !== "0";

function _asString(v: unknown): string {
  return String(v ?? "").trim();
}

function _sessionIdFromEvent(event: any): string {
  return _asString(
    event?.properties?.sessionID ??
      event?.properties?.sessionId ??
      event?.properties?.id ??
      event?.sessionID ??
      event?.sessionId
  );
}

function _extractUserPrompt(event: any): string {
  const props = event?.properties;
  if (!props || typeof props !== "object") return "";

  const candidates = [props?.message, props?.info, props?.payload, props];
  for (const c of candidates) {
    if (!c || typeof c !== "object") continue;
    const role = _asString((c as any)?.role ?? (c as any)?.info?.role).toLowerCase();
    if (role && role !== "user") continue;

    const parts = Array.isArray((c as any)?.parts) ? (c as any).parts : [];
    const fromParts = parts
      .map((p: any) => (String(p?.type ?? "") === "text" && typeof p?.text === "string" ? String(p.text) : ""))
      .filter(Boolean)
      .join("\n")
      .trim();
    const fromText = typeof (c as any)?.text === "string" ? String((c as any).text).trim() : "";
    const body = fromParts || fromText;
    if (body) return body;
  }

  return "";
}

async function _resolveRepoRoot(start: string): Promise<string> {
  return await new Promise((resolve) => {
    const child = spawn("git", ["rev-parse", "--show-toplevel"], { cwd: start, env: process.env });
    let out = "";
    child.stdout.on("data", (d: any) => (out += d.toString()));
    child.on("close", (code: any) => {
      const top = code === 0 ? _asString(out) : "";
      resolve(top || start);
    });
    child.on("error", () => resolve(start));
  });
}

function _emitHook(repoRoot: string, eventName: string, payload: Record<string, unknown>): void {
  const child = spawn(
    DEFAULT_LOOM_BIN,
    ["compound", "opencode-hook", "--repo", repoRoot, "--event", eventName],
    { cwd: repoRoot, env: process.env, stdio: ["pipe", "ignore", "ignore"] }
  );
  child.on("error", () => {});
  child.stdin.on("error", () => {});
  child.stdin.write(JSON.stringify(payload));
  child.stdin.end();
}

function _toolPayload(input: any, output: any): Record<string, unknown> {
  const toolName = _asString(input?.tool ?? input?.name ?? output?.tool ?? output?.name ?? "unknown");
  const args = (output?.args && typeof output.args === "object" ? output.args : input?.args) ?? {};
  const sessionID = _asString(input?.sessionID ?? input?.sessionId ?? output?.sessionID ?? output?.sessionId);
  return {
    tool_name: toolName,
    tool_input: args,
    session_id: sessionID,
  };
}

export const CompoundEngineeringPlugin: Plugin = async ({ directory, worktree }) => {
  const repoRoot = await _resolveRepoRoot(worktree ?? directory);

  const forward = (eventName: string, payload: Record<string, unknown>) => {
    if (!LOG_OBSERVATIONS) return;
    try {
      _emitHook(repoRoot, eventName, payload);
    } catch {
      // swallow
    }
  };

  const onEvent = async ({ event }: any) => {
    const type = _asString(event?.type || "");
    if (!type) return;
    if (type === "session.updated") return;

    if (type === "message.updated") {
      const prompt = _extractUserPrompt(event);
      if (!prompt) return;
      forward(type, {
        type,
        session_id: _sessionIdFromEvent(event),
        prompt,
        properties: event?.properties && typeof event.properties === "object" ? event.properties : {},
      });
      return;
    }

    if (type === "session.idle") {
      forward(type, {
        type,
        session_id: _sessionIdFromEvent(event),
      });
    }
  };

  const toolBefore = async (input: any, output: any) => {
    forward("tool.execute.before", {
      type: "tool.execute.before",
      ..._toolPayload(input, output),
    });
  };

  const toolAfter = async (input: any, output: any) => {
    const payload = _toolPayload(input, output);
    forward("tool.execute.after", {
      type: "tool.execute.after",
      ...payload,
      ok: typeof output?.ok === "boolean" ? output.ok : typeof output?.success === "boolean" ? output.success : undefined,
      tool_response: {
        title: _asString(output?.title || ""),
        output: typeof output?.output === "string" ? output.output : "",
        stderr: typeof output?.stderr === "string" ? output.stderr : "",
        metadata: output?.metadata && typeof output.metadata === "object" ? output.metadata : {},
        exitCode: typeof output?.exitCode === "number" ? Math.trunc(output.exitCode) : undefined,
        exit_code: typeof output?.exit_code === "number" ? Math.trunc(output.exit_code) : undefined,
      },
      reason: _asString(output?.error || ""),
    });
  };

  return {
    event: onEvent,
    "tool.execute.before": toolBefore,
    "tool.execute.after": toolAfter,
  };
};

export default CompoundEngineeringPlugin;
