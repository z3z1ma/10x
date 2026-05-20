import { statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import { readAgentFiles, readOrderedUsingLoomFiles } from "../loom-core.mjs";

const PACKAGE_ROOT = dirname(dirname(fileURLToPath(import.meta.url)));
const BOOTSTRAP_MARKER = "loom-core-using-loom-bootstrap";
const CUSTOM_MESSAGE_TYPE = "agent-loom-core";
const PI_AGENT_NAMES = new Set(["loom-weaver", "loom-driver"]);

function directoryExists(directory) {
  return statSync(directory, { throwIfNoEntry: false })?.isDirectory() === true;
}

function stripFrontmatter(text) {
  return text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, "").trim();
}

function textContentIncludes(content, marker) {
  if (typeof content === "string") return content.includes(marker);
  if (!Array.isArray(content)) return false;
  return content.some((part) => part?.type === "text" && typeof part.text === "string" && part.text.includes(marker));
}

function sessionHasBootstrap(ctx) {
  const entries = ctx?.sessionManager?.getEntries?.() ?? [];
  return entries.some((entry) => (
    entry?.type === "custom_message"
    && entry.customType === CUSTOM_MESSAGE_TYPE
    && textContentIncludes(entry.content, BOOTSTRAP_MARKER)
  ));
}

function sendUserMessage(pi, ctx, content) {
  if (ctx?.isIdle?.() === false) {
    pi.sendUserMessage(content, { deliverAs: "followUp" });
    ctx.ui?.notify?.("Loom command queued as a follow-up", "info");
    return;
  }

  pi.sendUserMessage(content);
}

function rootDirFrom(options = {}) {
  return options.rootDir || PACKAGE_ROOT;
}

export function getPiSkillPaths(options = {}) {
  const skillRoot = join(rootDirFrom(options), "skills");
  return directoryExists(skillRoot) ? [skillRoot] : [];
}

export function buildPiUsingLoomBootstrap(options = {}) {
  const rootDir = rootDirFrom(options);
  const files = readOrderedUsingLoomFiles({ rootDir });
  if (files.length === 0) return null;

  const sections = files.map((reference) => {
    const content = reference.path.endsWith("/SKILL.md") ? stripFrontmatter(reference.text) : reference.text;
    return `# Source: ${reference.path}\n\n${content}`;
  }).join("\n\n");

  return `<EXTREMELY_IMPORTANT>\n${BOOTSTRAP_MARKER}\nYou have Loom.\n\nIMPORTANT: The using-loom skill content and ordered references are included below. They are ALREADY LOADED - you are currently following them. Do NOT use /skill:using-loom again just to satisfy session start.\n\nFor every other relevant Loom skill, use Pi's native skill mechanism. Skill invocation comes before clarifying questions, code exploration, quick checks, edits, ticket creation, Ralph launches, evidence claims, audit claims, or closure.\n\n${sections}\n</EXTREMELY_IMPORTANT>`;
}

export function readPiAgentCommands(options = {}) {
  return readAgentFiles({ rootDir: rootDirFrom(options) })
    .filter((agent) => PI_AGENT_NAMES.has(agent.name))
    .map((agent) => ({
      name: agent.name,
      description: agent.description,
      prompt: agent.content,
      source: agent.path,
    }));
}

export function buildPiAgentCommandPrompt(agent, args = "") {
  const trimmedArgs = args.trim();
  const task = trimmedArgs || "Start by asking the operator what Loom work to shape or coordinate next.";
  return `<EXTREMELY_IMPORTANT>\nThe operator explicitly invoked the ${agent.name} Loom named agent for this task. Follow the bundled agent prompt below for this turn.\n\n# Source: ${agent.source}\n\n${agent.prompt}\n</EXTREMELY_IMPORTANT>\n\nTask: ${task}`;
}

export default function loomCorePiExtension(pi) {
  pi.on("resources_discover", async () => ({
    skillPaths: getPiSkillPaths(),
  }));

  pi.on("before_agent_start", async (_event, ctx) => {
    if (sessionHasBootstrap(ctx)) return undefined;

    const bootstrap = buildPiUsingLoomBootstrap();
    if (!bootstrap) return undefined;

    return {
      message: {
        customType: CUSTOM_MESSAGE_TYPE,
        content: bootstrap,
        display: false,
      },
    };
  });

  for (const agent of readPiAgentCommands()) {
    pi.registerCommand(agent.name, {
      description: agent.description,
      handler: async (args, ctx) => {
        sendUserMessage(pi, ctx, buildPiAgentCommandPrompt(agent, args));
      },
    });
  }
}
