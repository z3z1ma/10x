import { readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
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
    bootstrap: options.bootstrap !== false,
    skills: options.skills !== false,
  };
}

export function readOrderedBootstrapFiles(options = {}) {
  const { rootDir } = surfaceOptions(options);
  const referencesDir = join(rootDir, "skills", "loom-bootstrap", "references");
  return markdownFilesIn(referencesDir).map((path) => ({
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

export function configureOpenCode(config, options = {}) {
  const surfaces = surfaceOptions(options);

  if (surfaces.bootstrap) {
    const bootstrapReferences = readOrderedBootstrapFiles(surfaces);
    if (bootstrapReferences.length > 0) {
      config.instructions ??= [];
      for (const reference of bootstrapReferences) pushUnique(config.instructions, reference.absolutePath);
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

  return config;
}

export function inspectLoomBundle(options = {}) {
  const surfaces = surfaceOptions(options);
  const bootstrapReferences = readOrderedBootstrapFiles(surfaces);
  const skills = readSkillFiles(surfaces);

  return {
    bootstrap: {
      result: "registered through config.instructions as ordered bootstrap references",
      files: bootstrapReferences.map((reference) => reference.path),
    },
    skills: {
      result: "registered through config.skills.paths",
      path: directoryExists(join(surfaces.rootDir, "skills")) ? join(surfaces.rootDir, "skills") : undefined,
      items: skills,
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
    bootstrapReferenceCount: inspection.bootstrap.files.length,
    bootstrapReferenceFiles: inspection.bootstrap.files,
    firstBootstrapReference: inspection.bootstrap.files[0],
    lastBootstrapReference: inspection.bootstrap.files.at(-1),
    instructionCount: config.instructions.length,
    instructionsAreDeduped: config.instructions.length === beforeInstructionCount,
    firstInstruction: config.instructions[0],
    lastInstruction: config.instructions.at(-1),
    skillCount: inspection.skills.items.length,
    skillPath: config.skills?.paths?.[0],
    bootstrapResult: inspection.bootstrap.result,
    skillsResult: inspection.skills.result,
  }, null, 2));
}
