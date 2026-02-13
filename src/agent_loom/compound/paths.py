from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CompoundPaths:
    root: Path
    loom_compound_dir: Path
    runtime_dir: Path
    observations_file: Path
    observer_pid_file: Path
    observer_log_file: Path
    observer_nudge_file: Path
    instincts_dir: Path
    instincts_local_dir: Path
    instincts_inherited_dir: Path
    instincts_file: Path
    instincts_markdown_file: Path
    state_file: Path
    config_file: Path
    evolved_dir: Path
    evolved_skills_dir: Path
    evolved_commands_dir: Path
    evolved_agents_dir: Path


def compound_paths(root: Path) -> CompoundPaths:
    repo_root = root.resolve()
    loom_compound_dir = repo_root / ".loom" / "compound"
    runtime_dir = loom_compound_dir / "runtime"
    observations_file = runtime_dir / "observations.jsonl"
    observer_pid_file = runtime_dir / "observer.pid"
    observer_log_file = runtime_dir / "observer.log"
    observer_nudge_file = runtime_dir / "observer.nudge"

    instincts_dir = loom_compound_dir / "instincts"
    instincts_local_dir = instincts_dir / "local"
    instincts_inherited_dir = instincts_dir / "inherited"
    instincts_file = loom_compound_dir / "instincts.json"
    instincts_markdown_file = loom_compound_dir / "INSTINCTS.md"

    state_file = loom_compound_dir / "state.json"
    config_file = loom_compound_dir / "config.json"

    evolved_dir = loom_compound_dir / "evolved"
    evolved_skills_dir = evolved_dir / "skills"
    evolved_commands_dir = evolved_dir / "commands"
    evolved_agents_dir = evolved_dir / "agents"

    return CompoundPaths(
        root=repo_root,
        loom_compound_dir=loom_compound_dir,
        runtime_dir=runtime_dir,
        observations_file=observations_file,
        observer_pid_file=observer_pid_file,
        observer_log_file=observer_log_file,
        observer_nudge_file=observer_nudge_file,
        instincts_dir=instincts_dir,
        instincts_local_dir=instincts_local_dir,
        instincts_inherited_dir=instincts_inherited_dir,
        instincts_file=instincts_file,
        instincts_markdown_file=instincts_markdown_file,
        state_file=state_file,
        config_file=config_file,
        evolved_dir=evolved_dir,
        evolved_skills_dir=evolved_skills_dir,
        evolved_commands_dir=evolved_commands_dir,
        evolved_agents_dir=evolved_agents_dir,
    )
