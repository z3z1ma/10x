from __future__ import annotations

import json
from importlib import resources
from pathlib import Path

from agent_loom.compound.install import install_opencode


def _template_text(*parts: str) -> str:
    traversable = (
        resources.files("agent_loom.pack")
        .joinpath("packs", "loom-compound-core", "files", ".opencode")
        .joinpath(*parts)
    )
    with resources.as_file(traversable) as p:
        return Path(p).read_text(encoding="utf-8")


def test_compound_install_does_not_overwrite_scaffold_without_force(
    tmp_path: Path,
) -> None:
    dest = tmp_path
    dest.mkdir(parents=True, exist_ok=True)

    plugin_path = dest / ".opencode" / "plugins" / "compound_engineering.ts"
    plugin_path.parent.mkdir(parents=True, exist_ok=True)
    plugin_path.write_text("// old\n", encoding="utf-8")

    res = install_opencode(dest=dest, dry_run=False)
    assert res.dest == str(dest.resolve())
    actual = plugin_path.read_text(encoding="utf-8")
    assert actual == "// old\n"


def test_compound_install_overwrites_scaffold_with_force(tmp_path: Path) -> None:
    dest = tmp_path
    dest.mkdir(parents=True, exist_ok=True)

    plugin_path = dest / ".opencode" / "plugins" / "compound_engineering.ts"
    plugin_path.parent.mkdir(parents=True, exist_ok=True)
    plugin_path.write_text("// old\n", encoding="utf-8")

    install_opencode(dest=dest, dry_run=False, force=True)
    expected = _template_text("plugins", "compound_engineering.ts")
    actual = plugin_path.read_text(encoding="utf-8")
    assert actual == expected


def test_compound_install_patches_agents_md_without_clobbering(tmp_path: Path) -> None:
    dest = tmp_path
    agents = dest / "AGENTS.md"
    agents.write_text("# AGENTS\n\nhello\n", encoding="utf-8")

    install_opencode(dest=dest, dry_run=False)
    new = agents.read_text(encoding="utf-8")
    assert "hello" in new

    assert new == "# AGENTS\n\nhello\n"


def test_compound_install_creates_loom_docs_if_missing(tmp_path: Path) -> None:
    dest = tmp_path
    install_opencode(dest=dest, dry_run=False)

    assert (dest / "LOOM.md").exists()
    assert (dest / ".loom" / "compound" / "ROADMAP.md").exists()
    assert (dest / ".loom" / "compound" / "config.json").exists()
    assert (dest / ".loom" / "compound" / "instincts" / "personal").exists()
    assert (dest / ".loom" / "compound" / "instincts" / "inherited").exists()
    assert not (dest / "LOOM_PROJECT.md").exists()
    assert not (dest / "LOOM_CHANGELOG.md").exists()

    loom_text = (dest / "LOOM.md").read_text(encoding="utf-8")
    roadmap_text = (dest / ".loom" / "compound" / "ROADMAP.md").read_text(encoding="utf-8")
    instincts_text = (dest / ".loom" / "compound" / "INSTINCTS.md").read_text(encoding="utf-8")
    agents_text = (dest / "AGENTS.md").read_text(encoding="utf-8")

    assert "BEGIN:compound:" not in loom_text
    assert "BEGIN:compound:" not in roadmap_text
    assert "BEGIN:compound:" not in instincts_text

    assert "LOOM.md" in agents_text
    assert ".loom/compound/ROADMAP.md" in agents_text
    assert ".loom/compound/INSTINCTS.md" in agents_text

    cfg = json.loads((dest / ".loom" / "compound" / "config.json").read_text(encoding="utf-8"))
    instincts_cfg = cfg.get("instincts") if isinstance(cfg.get("instincts"), dict) else {}
    derive_cmd = instincts_cfg.get("derive_command")
    assert isinstance(derive_cmd, list)
    assert "{prompt}" in derive_cmd
    assert "haiku" in derive_cmd


def test_compound_install_does_not_install_compoundspec_skill(tmp_path: Path) -> None:
    dest = tmp_path
    install_opencode(dest=dest, dry_run=False)

    assert not (
        dest / ".opencode" / "skills" / "compound-apply-spec" / "SKILL.md"
    ).exists()


def test_compound_install_provides_plugin_required_scaffolding(tmp_path: Path) -> None:
    dest = tmp_path
    install_opencode(dest=dest, dry_run=False)

    required = [
        dest / "AGENTS.md",
        dest / "LOOM.md",
        dest / ".claude" / "settings.json",
        dest / ".claude" / "commands" / "loom-plan.md",
        dest / ".claude" / "commands" / "loom-work.md",
        dest / ".claude" / "commands" / "loom-review.md",
        dest / ".claude" / "commands" / "loom-compound.md",
        dest / ".claude" / "commands" / "instinct-status.md",
        dest / ".claude" / "commands" / "instinct-import.md",
        dest / ".claude" / "commands" / "instinct-export.md",
        dest / ".claude" / "commands" / "evolve.md",
        dest / ".claude" / "commands" / "observer.md",
        dest / ".claude" / "skills" / "skill-authoring" / "SKILL.md",
        dest / ".claude" / "agents" / "loom-review-quality.md",
        dest / ".claude" / "agents" / "loom-review-security.md",
        dest / ".claude" / "agents" / "loom-review-docs.md",
        dest / ".omp" / "extensions" / "compound_engineering.ts",
        dest / ".loom" / "compound" / "ROADMAP.md",
        dest / ".loom" / "compound" / "README.md",
        dest / ".loom" / "compound" / "config.json",
        dest / ".loom" / "compound" / "instincts" / "personal" / ".gitkeep",
        dest / ".loom" / "compound" / "instincts" / "inherited" / ".gitkeep",
        dest / ".opencode" / "commands" / "loom-plan.md",
        dest / ".opencode" / "commands" / "loom-work.md",
        dest / ".opencode" / "commands" / "loom-review.md",
        dest / ".opencode" / "commands" / "loom-compound.md",
        dest / ".opencode" / "commands" / "instinct-status.md",
        dest / ".opencode" / "commands" / "instinct-import.md",
        dest / ".opencode" / "commands" / "instinct-export.md",
        dest / ".opencode" / "commands" / "evolve.md",
        dest / ".opencode" / "commands" / "observer.md",
        dest / ".opencode" / "memory" / ".gitignore",
        dest / ".opencode" / "compound" / ".gitignore",
        dest / ".loom" / "compound" / "runtime" / ".gitignore",
    ]
    for p in required:
        assert p.exists(), str(p)

    mem_ignore = (dest / ".opencode" / "memory" / ".gitignore").read_text(
        encoding="utf-8"
    )
    assert "observations.jsonl" in mem_ignore
    assert "observations.jsonl.*.bak" in mem_ignore

    omp_adapter = (dest / ".omp" / "extensions" / "compound_engineering.ts").read_text(
        encoding="utf-8"
    )
    assert "loom compound omp-hook" in omp_adapter

    compound_ignore = (dest / ".opencode" / "compound" / ".gitignore").read_text(
        encoding="utf-8"
    )
    assert "instincts_status.json" in compound_ignore
    assert "*.tmp.*" in compound_ignore

    runtime_ignore = (dest / ".loom" / "compound" / "runtime" / ".gitignore").read_text(
        encoding="utf-8"
    )
    assert "observations.jsonl" in runtime_ignore
    assert "observations.jsonl.*.bak" in runtime_ignore
    assert "observer.pid" in runtime_ignore
    assert "observer.log" in runtime_ignore
    assert "observer.nudge" in runtime_ignore

    claude_settings = json.loads(
        (dest / ".claude" / "settings.json").read_text(encoding="utf-8")
    )
    hooks = claude_settings.get("hooks")
    assert isinstance(hooks, dict)
    for event in [
        "SessionStart",
        "UserPromptSubmit",
        "PreToolUse",
        "PostToolUse",
        "PostToolUseFailure",
        "PreCompact",
        "Notification",
        "Stop",
        "SubagentStop",
        "SessionEnd",
    ]:
        assert event in hooks

    for event_hooks in hooks.values():
        if not isinstance(event_hooks, list):
            continue
        for evt in event_hooks:
            if not isinstance(evt, dict):
                continue
            for hook in evt.get("hooks") or []:
                if isinstance(hook, dict) and str(hook.get("type") or "") == "command":
                    assert "loom compound claude-hook" in str(hook.get("command") or "")


def test_compound_install_dry_run_does_not_write_files(tmp_path: Path) -> None:
    dest = tmp_path
    res = install_opencode(dest=dest, dry_run=True)

    assert res.dry_run is True
    assert not (dest / ".opencode").exists()
    assert not (dest / ".loom").exists()
    assert not (dest / "LOOM.md").exists()
    assert not (dest / ".loom" / "compound" / "ROADMAP.md").exists()
    assert not (dest / "AGENTS.md").exists()

    assert any(
        p.endswith(".opencode/plugins/compound_engineering.ts") for p in res.wrote
    )


def test_compound_install_never_overwrites_instinct_markdown_without_force(tmp_path: Path) -> None:
    dest = tmp_path
    install_opencode(dest=dest, dry_run=False)

    instinct = dest / ".loom" / "compound" / "instincts" / "personal" / "custom.md"
    instinct.parent.mkdir(parents=True, exist_ok=True)
    instinct.write_text("# custom\n", encoding="utf-8")

    install_opencode(dest=dest, dry_run=False)
    assert instinct.read_text(encoding="utf-8") == "# custom\n"
