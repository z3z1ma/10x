from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from agent_loom.compound.instincts import Instinct, load_instincts
from agent_loom.compound.paths import CompoundPaths, compound_paths


def _slug(text: str) -> str:
    value = str(text or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "general"


def _normalize_trigger_key(trigger: str) -> str:
    key = str(trigger or "").strip().lower()
    for token in ["when", "creating", "writing", "adding", "implementing", "testing"]:
        key = key.replace(token, " ")
    key = " ".join(key.split())
    return key


def _cluster_key(inst: Instinct) -> str:
    normalized = _normalize_trigger_key(str(inst.trigger or ""))
    if normalized:
        return _slug(normalized)
    if str(inst.domain or "").strip():
        return _slug(inst.domain)
    if inst.tags:
        return _slug(inst.tags[0])
    return "general"


def _cluster_title(cluster: str) -> str:
    return (
        " ".join(part.capitalize() for part in cluster.split("-") if part) or "General"
    )


def _command_name_from_trigger(trigger: str, fallback: str) -> str:
    cmd_name = str(trigger or "").lower()
    cmd_name = (
        cmd_name.replace("when ", "").replace("implementing ", "").replace("a ", "")
    )
    cmd_name = "-".join(cmd_name.split())[:20]
    return _slug(cmd_name) or _slug(fallback)


def _skill_markdown(cluster: str, instincts: list[Instinct]) -> str:
    title = _cluster_title(cluster)
    lines: list[str] = [
        f"# {title} Instinct Skill",
        "",
        "## Purpose",
        "",
        f"Apply evolved instinct cluster `{cluster}` consistently.",
        "",
        "## Instincts",
        "",
    ]
    for inst in instincts:
        pct = int(round(float(inst.confidence or 0.0) * 100))
        lines.append(f"- **{inst.id}** ({pct}%)")
        lines.append(f"  - Trigger: {inst.trigger}")
        lines.append(f"  - Action: {inst.action}")
    lines.append("")
    return "\n".join(lines)


def _command_markdown(name: str, instinct: Instinct) -> str:
    lines: list[str] = [
        "---",
        f"description: Evolved command from instinct {instinct.id}",
        "---",
        "",
        f"Command: `{name}`",
        "",
        f"- Trigger: {instinct.trigger}",
        f"- Action: {instinct.action}",
        f"- Confidence: {int(round(float(instinct.confidence or 0.0) * 100))}%",
        "",
    ]
    return "\n".join(lines)


def _agent_markdown(name: str, instincts: list[Instinct]) -> str:
    lines: list[str] = [
        f"# {name}",
        "",
        "You are an evolved Loom instinct agent.",
        "",
        "Behavioral contract:",
    ]
    for inst in instincts:
        lines.append(f"- When {inst.trigger}, do: {inst.action}")
    lines.extend(
        ["", "Do not deviate from these instincts without explicit user override.", ""]
    )
    return "\n".join(lines)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@dataclass(frozen=True)
class EvolveResult:
    ok: bool
    repo: str
    threshold: float
    clusters: int
    instincts_used: int
    generated: bool


def _skill_candidates(instincts: list[Instinct]) -> list[dict[str, Any]]:
    by_cluster: dict[str, list[Instinct]] = {}
    for inst in instincts:
        by_cluster.setdefault(_cluster_key(inst), []).append(inst)

    candidates: list[dict[str, Any]] = []
    for cluster, cluster_items in by_cluster.items():
        if len(cluster_items) < 2:
            continue
        avg_conf = sum(float(i.confidence or 0.0) for i in cluster_items) / float(
            len(cluster_items)
        )
        candidates.append(
            {
                "cluster": cluster,
                "instincts": sorted(
                    cluster_items, key=lambda x: (-float(x.confidence or 0.0), x.id)
                ),
                "avg_confidence": avg_conf,
                "domains": sorted({str(i.domain or "general") for i in cluster_items}),
            }
        )

    candidates.sort(
        key=lambda x: (
            -len(x["instincts"]),
            -float(x["avg_confidence"]),
            str(x["cluster"]),
        )
    )
    return candidates


def _command_candidates(instincts: list[Instinct]) -> list[Instinct]:
    out = [
        i
        for i in instincts
        if str(i.domain or "") == "workflow" and float(i.confidence or 0.0) >= 0.7
    ]
    out.sort(key=lambda x: (-float(x.confidence or 0.0), x.id))
    return out


def _agent_candidates(skill_candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = [
        c
        for c in skill_candidates
        if len(list(c.get("instincts") or [])) >= 3
        and float(c.get("avg_confidence") or 0.0) >= 0.75
    ]
    out.sort(
        key=lambda x: (
            -len(list(x.get("instincts") or [])),
            -float(x.get("avg_confidence") or 0.0),
            str(x.get("cluster") or ""),
        )
    )
    return out


def evolve_instincts(*, root: Path, threshold: float, generate: bool) -> EvolveResult:
    repo = root.resolve()
    paths: CompoundPaths = compound_paths(repo)
    store = load_instincts(paths.instincts_file)

    selected = [
        inst
        for inst in list(store.instincts or [])
        if inst.status == "active" and float(inst.confidence or 0.0) >= float(threshold)
    ]
    selected.sort(key=lambda x: (_cluster_key(x), -float(x.confidence or 0.0), x.id))

    skill_candidates = _skill_candidates(selected)
    command_candidates = _command_candidates(selected)
    agent_candidates = _agent_candidates(skill_candidates)

    # Canonical evolved outputs in .loom/compound/evolved/**
    for skill in skill_candidates:
        cluster = str(skill["cluster"])
        instincts = list(skill["instincts"])
        _write(
            paths.evolved_skills_dir / f"{cluster}.md",
            _skill_markdown(cluster, instincts),
        )

    command_names_written: set[str] = set()
    for inst in command_candidates:
        name = _command_name_from_trigger(str(inst.trigger or ""), fallback=inst.id)
        if name in command_names_written:
            name = f"{name}-{_slug(inst.id)[:8]}"
        command_names_written.add(name)
        _write(
            paths.evolved_commands_dir / f"instinct-{name}.md",
            _command_markdown(name, inst),
        )

    for agent in agent_candidates:
        cluster = str(agent["cluster"])
        instincts = list(agent["instincts"])
        name = f"{cluster}-agent"
        _write(
            paths.evolved_agents_dir / f"instinct-{name}.md",
            _agent_markdown(name, instincts),
        )

    if generate:
        for skill in skill_candidates:
            cluster = str(skill["cluster"])
            instincts = list(skill["instincts"])
            skill_text = _skill_markdown(cluster, instincts)
            _write(
                repo / ".claude" / "skills" / "learned" / cluster / "SKILL.md",
                skill_text,
            )
            _write(
                repo / ".opencode" / "skills" / "learned" / cluster / "SKILL.md",
                skill_text,
            )

        command_names_written = set()
        for inst in command_candidates:
            name = _command_name_from_trigger(str(inst.trigger or ""), fallback=inst.id)
            if name in command_names_written:
                name = f"{name}-{_slug(inst.id)[:8]}"
            command_names_written.add(name)
            command_text = _command_markdown(name, inst)
            _write(repo / ".claude" / "commands" / f"instinct-{name}.md", command_text)
            _write(
                repo / ".opencode" / "commands" / f"instinct-{name}.md", command_text
            )

        for agent in agent_candidates:
            cluster = str(agent["cluster"])
            instincts = list(agent["instincts"])
            name = f"{cluster}-agent"
            agent_text = _agent_markdown(name, instincts)
            _write(repo / ".claude" / "agents" / f"instinct-{name}.md", agent_text)
            _write(repo / ".opencode" / "agents" / f"instinct-{name}.md", agent_text)

    return EvolveResult(
        ok=True,
        repo=str(repo),
        threshold=float(threshold),
        clusters=len(skill_candidates),
        instincts_used=len(selected),
        generated=bool(generate),
    )
