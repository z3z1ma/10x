import { readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const PACKAGE_ROOT = dirname(fileURLToPath(import.meta.url));
const LOOM_BLOCK_BEGIN = "<!-- BEGIN LOOM RULES: open-loom -->";
const LOOM_BLOCK_END = "<!-- END LOOM RULES: open-loom -->";

function posixPath(path) {
  return path.split("\\").join("/");
}

function directoryExists(directory) {
  return statSync(directory, { throwIfNoEntry: false })?.isDirectory() === true;
}

function markdownFilesIn(directory) {
  if (!directoryExists(directory)) return [];
  return readdirSync(directory)
    .filter((name) => name.endsWith(".md"))
    .map((name) => join(directory, name))
    .filter((path) => statSync(path).isFile())
    .sort((a, b) => a.localeCompare(b));
}

function readScalarFrontmatter(text, key) {
  const match = text.match(/^---\n([\s\S]*?)\n---\n/);
  if (!match) return undefined;
  const line = match[1]
    .split("\n")
    .find((candidate) => candidate.startsWith(`${key}:`));
  if (!line) return undefined;
  return line.slice(key.length + 1).trim().replace(/^['\"]|['\"]$/g, "");
}

export function readOrderedRuleFiles({ rootDir = PACKAGE_ROOT } = {}) {
  const rulesDir = join(rootDir, "rules");
  return markdownFilesIn(rulesDir).map((path) => ({
    path: posixPath(relative(rootDir, path)),
    text: readFileSync(path, "utf8").trimEnd(),
  }));
}

export function buildLoomRuleBlock(options = {}) {
  const rules = readOrderedRuleFiles(options);
  const sections = rules.flatMap((rule) => [
    `<!-- source: ${rule.path} -->`,
    rule.text,
  ]);

  return [
    LOOM_BLOCK_BEGIN,
    "# Loom Protocol Rules",
    "",
    "The following Markdown rules are bundled with the Loom package and are mandatory whenever Loom is present in the workspace.",
    "They are injected by the open-loom OpenCode plugin from ordered top-level `rules/*.md` files.",
    "",
    ...sections,
    LOOM_BLOCK_END,
  ].join("\n");
}

export function injectLoomRules(systemPrompt = "", options = {}) {
  const prompt = String(systemPrompt || "").trimEnd();
  const block = buildLoomRuleBlock(options);
  return prompt ? `${prompt}\n\n${block}` : block;
}

export function prependLoomRules(systemOutput, options = {}) {
  if (!systemOutput || !Array.isArray(systemOutput.system)) {
    throw new TypeError("Expected OpenCode system output with a system string array");
  }
  systemOutput.system.unshift(buildLoomRuleBlock(options));
}

export function inspectLoomBundle({ rootDir = PACKAGE_ROOT } = {}) {
  const skillRoot = join(rootDir, "skills");
  const commandRoot = join(rootDir, "commands");
  const skills = directoryExists(skillRoot)
    ? readdirSync(skillRoot)
        .map((name) => ({ name, path: join(skillRoot, name, "SKILL.md") }))
        .filter((entry) => statSync(entry.path, { throwIfNoEntry: false })?.isFile())
        .sort((a, b) => a.name.localeCompare(b.name))
        .map((entry) => {
          const text = readFileSync(entry.path, "utf8");
          return {
            directory: entry.name,
            path: posixPath(relative(rootDir, entry.path)),
            name: readScalarFrontmatter(text, "name") || entry.name,
            description: readScalarFrontmatter(text, "description") || "",
          };
        })
    : [];

  const commands = markdownFilesIn(commandRoot).map((path) => ({
    path: posixPath(relative(rootDir, path)),
    name: readScalarFrontmatter(readFileSync(path, "utf8"), "name") || relative(commandRoot, path).replace(/\.md$/, ""),
  }));

  return {
    rules: {
      result: "plugin-first via experimental.chat.system.transform",
      files: readOrderedRuleFiles({ rootDir }).map((rule) => rule.path),
    },
    skills: {
      result: "discoverable only; direct-copy fallback still required for OpenCode skill surfaces",
      reason: "No first-class OpenCode plugin skill registration hook is proven by open-loom validation yet.",
      items: skills,
    },
    commands: {
      result: "discoverable only; direct-copy fallback still required for OpenCode command surfaces",
      reason: "OpenCode command hooks run after command resolution and do not prove slash-command registration.",
      items: commands,
    },
  };
}

function createTransform(options = {}) {
  return async (_input, output) => {
    prependLoomRules(output, options);
  };
}

export function createOpenLoomPlugin(options = {}) {
  return {
    "experimental.chat.system.transform": createTransform(options),
  };
}

export async function server(_input = {}, options = {}) {
  return createOpenLoomPlugin(options || {});
}

export default {
  id: "open-loom",
  server,
};

if (process.argv[1] === fileURLToPath(import.meta.url) && process.argv.includes("--smoke")) {
  const inspection = inspectLoomBundle();
  const block = buildLoomRuleBlock();
  const hooks = await server({}, {});
  const output = { system: ["existing"] };
  await hooks["experimental.chat.system.transform"]({}, output);
  console.log(JSON.stringify({
    ok: true,
    ruleCount: inspection.rules.files.length,
    ruleFiles: inspection.rules.files,
    firstRule: inspection.rules.files[0],
    lastRule: inspection.rules.files.at(-1),
    blockHasMarkers: block.includes(LOOM_BLOCK_BEGIN) && block.includes(LOOM_BLOCK_END),
    transformPrependsBlock: output.system.length === 2 && output.system[0].includes(LOOM_BLOCK_BEGIN) && output.system[1] === "existing",
    skillCount: inspection.skills.items.length,
    commandCount: inspection.commands.items.length,
    skillsResult: inspection.skills.result,
    commandsResult: inspection.commands.result,
  }, null, 2));
}
