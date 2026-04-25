import { readdirSync, readFileSync, statSync } from "node:fs";
import { basename, dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const PACKAGE_ROOT = dirname(fileURLToPath(import.meta.url));
const PLUGIN_ID = "open-loom";

function posixPath(path) {
  return path.split("\\").join("/");
}

function directoryExists(directory) {
  return statSync(directory, { throwIfNoEntry: false })?.isDirectory() === true;
}

function fileExists(file) {
  return statSync(file, { throwIfNoEntry: false })?.isFile() === true;
}

function markdownFilesIn(directory, { recursive = false } = {}) {
  if (!directoryExists(directory)) return [];

  const result = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);
    if (entry.isDirectory() && recursive) {
      result.push(...markdownFilesIn(path, { recursive }));
      continue;
    }
    if (entry.isFile() && entry.name.endsWith(".md")) result.push(path);
  }

  return result.sort((a, b) => a.localeCompare(b));
}

function readMarkdownDocument(file) {
  const text = readFileSync(file, "utf8").trimEnd();
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  if (!match) return { data: {}, content: text };

  const data = {};
  for (const line of match[1].split(/\r?\n/)) {
    const scalar = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (!scalar) continue;
    const value = scalar[2].trim().replace(/^['"]|['"]$/g, "");
    data[scalar[1]] = value;
  }

  return {
    data,
    content: text.slice(match[0].length).trim(),
  };
}

function pushUnique(array, value) {
  if (!array.includes(value)) array.push(value);
}

function surfaceOptions(options = {}) {
  return {
    rootDir: resolve(String(options.rootDir || PACKAGE_ROOT)),
    rules: options.rules !== false,
    skills: options.skills !== false,
    commands: options.commands !== false,
  };
}

export function readOrderedRuleFiles(options = {}) {
  const { rootDir } = surfaceOptions(options);
  const rulesDir = join(rootDir, "rules");
  return markdownFilesIn(rulesDir).map((path) => ({
    path: posixPath(relative(rootDir, path)),
    absolutePath: path,
    text: readFileSync(path, "utf8").trimEnd(),
  }));
}

export function readSkillFiles(options = {}) {
  const { rootDir } = surfaceOptions(options);
  const skillRoot = join(rootDir, "skills");
  if (!directoryExists(skillRoot)) return [];

  return readdirSync(skillRoot)
    .map((name) => ({ name, path: join(skillRoot, name, "SKILL.md") }))
    .filter((entry) => fileExists(entry.path))
    .sort((a, b) => a.name.localeCompare(b.name))
    .map((entry) => {
      const md = readMarkdownDocument(entry.path);
      return {
        directory: entry.name,
        path: posixPath(relative(rootDir, entry.path)),
        name: md.data.name || entry.name,
        description: md.data.description || "",
      };
    });
}

export function readCommandFiles(options = {}) {
  const { rootDir } = surfaceOptions(options);
  const commandRoot = join(rootDir, "commands");

  return markdownFilesIn(commandRoot, { recursive: true }).map((path) => {
    const md = readMarkdownDocument(path);
    const relativePath = posixPath(relative(commandRoot, path));
    const fallbackName = relativePath.replace(/\.md$/, "");
    return {
      path: posixPath(relative(rootDir, path)),
      name: md.data.name || fallbackName || basename(path, ".md"),
      description: md.data.description || undefined,
      template: md.content,
    };
  });
}

export function configureOpenCode(config, options = {}) {
  const surfaces = surfaceOptions(options);

  if (surfaces.rules) {
    const rules = readOrderedRuleFiles(surfaces);
    if (rules.length > 0) {
      config.instructions ??= [];
      for (const rule of rules) pushUnique(config.instructions, rule.absolutePath);
    }
  }

  if (surfaces.skills) {
    const skillRoot = join(surfaces.rootDir, "skills");
    if (readSkillFiles(surfaces).length > 0) {
      config.skills ??= {};
      config.skills.paths ??= [];
      pushUnique(config.skills.paths, skillRoot);
    }
  }

  if (surfaces.commands) {
    const commands = readCommandFiles(surfaces);
    if (commands.length > 0) {
      config.command ??= {};
      for (const command of commands) {
        config.command[command.name] ??= {
          template: command.template,
          ...(command.description ? { description: command.description } : {}),
        };
      }
    }
  }

  return config;
}

export function inspectLoomBundle(options = {}) {
  const surfaces = surfaceOptions(options);
  const rules = readOrderedRuleFiles(surfaces);
  const skills = readSkillFiles(surfaces);
  const commands = readCommandFiles(surfaces);

  return {
    rules: {
      result: "registered through config.instructions",
      files: rules.map((rule) => rule.path),
    },
    skills: {
      result: "registered through config.skills.paths",
      path: directoryExists(join(surfaces.rootDir, "skills")) ? join(surfaces.rootDir, "skills") : undefined,
      items: skills,
    },
    commands: {
      result: "registered through config.command",
      items: commands.map(({ template: _template, ...command }) => command),
    },
  };
}

export async function server(_input = {}, options = {}) {
  return {
    config(config) {
      configureOpenCode(config, options || {});
    },
  };
}

export default {
  id: PLUGIN_ID,
  server,
};

if (process.argv[1] === fileURLToPath(import.meta.url) && process.argv.includes("--smoke")) {
  const inspection = inspectLoomBundle();
  const config = configureOpenCode({});
  const beforeInstructionCount = config.instructions.length;
  configureOpenCode(config);

  console.log(JSON.stringify({
    ok: true,
    pluginId: PLUGIN_ID,
    ruleCount: inspection.rules.files.length,
    ruleFiles: inspection.rules.files,
    firstRule: inspection.rules.files[0],
    lastRule: inspection.rules.files.at(-1),
    instructionCount: config.instructions.length,
    instructionsAreDeduped: config.instructions.length === beforeInstructionCount,
    firstInstruction: config.instructions[0],
    lastInstruction: config.instructions.at(-1),
    skillCount: inspection.skills.items.length,
    skillPath: config.skills?.paths?.[0],
    commandCount: inspection.commands.items.length,
    hasLoomPlanCommand: Boolean(config.command?.["loom-plan"]),
    rulesResult: inspection.rules.result,
    skillsResult: inspection.skills.result,
    commandsResult: inspection.commands.result,
  }, null, 2));
}
