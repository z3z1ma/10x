import { dirname } from "node:path";
import { fileURLToPath } from "node:url";

import { readPlaybookMacroCatalog } from "../loom-playbooks.mjs";

const PACKAGE_ROOT = dirname(dirname(fileURLToPath(import.meta.url)));

function sendUserMessage(pi, ctx, content) {
  if (ctx?.isIdle?.() === false) {
    pi.sendUserMessage(content, { deliverAs: "followUp" });
    ctx.ui?.notify?.("Loom playbook queued as a follow-up", "info");
    return;
  }

  pi.sendUserMessage(content);
}

function rootDirFrom(options = {}) {
  return options.rootDir || PACKAGE_ROOT;
}

export function readPiPlaybookCommands(options = {}) {
  return readPlaybookMacroCatalog({ rootDir: rootDirFrom(options) }).map((macro) => ({
    name: macro.name,
    description: macro.description,
    body: macro.body,
    source: macro.source,
  }));
}

export function buildPiPlaybookCommandPrompt(command, args = "") {
  const trimmedArgs = args.trim();
  return trimmedArgs ? `${command.body}\n\nOperator arguments:\n${trimmedArgs}` : command.body;
}

export default function loomPlaybooksPiExtension(pi) {
  for (const command of readPiPlaybookCommands()) {
    pi.registerCommand(command.name, {
      description: command.description,
      handler: async (args, ctx) => {
        sendUserMessage(pi, ctx, buildPiPlaybookCommandPrompt(command, args));
      },
    });
  }
}
