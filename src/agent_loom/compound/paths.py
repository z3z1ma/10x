from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CompoundPaths:
    root: Path

    # Cognitive state
    skills_dir: Path
    memory_dir: Path
    observations_file: Path
    instincts_file: Path
    instincts_md: Path

    # Scaffold
    compound_dir: Path
    prompts_dir: Path
    autolearn_prompt_file: Path

    # Docs
    agents_md: Path
    roadmap_md: Path


def compound_paths(root: Path) -> CompoundPaths:
    root = root.resolve()
    skills_dir = root / ".opencode" / "skills"
    memory_dir = root / ".opencode" / "memory"
    observations_file = memory_dir / "observations.jsonl"
    instincts_file = memory_dir / "instincts.json"
    instincts_md = memory_dir / "INSTINCTS.md"

    compound_dir = root / ".opencode" / "compound"
    prompts_dir = compound_dir / "prompts"
    autolearn_prompt_file = prompts_dir / "autolearn.md"

    agents_md = root / "AGENTS.md"
    roadmap_md = root / "LOOM_ROADMAP.md"

    return CompoundPaths(
        root=root,
        skills_dir=skills_dir,
        memory_dir=memory_dir,
        observations_file=observations_file,
        instincts_file=instincts_file,
        instincts_md=instincts_md,
        compound_dir=compound_dir,
        prompts_dir=prompts_dir,
        autolearn_prompt_file=autolearn_prompt_file,
        agents_md=agents_md,
        roadmap_md=roadmap_md,
    )


def required_scaffold_paths() -> list[str]:
    # These should be installed via `loom compound init`.
    return [
        "AGENTS.md",
        "LOOM_ROADMAP.md",
        ".opencode/commands/workflows:plan.md",
        ".opencode/compound/prompts/autolearn.md",
        ".opencode/memory/.gitignore",
        ".opencode/compound/.gitignore",
    ]
