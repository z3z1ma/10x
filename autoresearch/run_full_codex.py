from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from autoresearch import offline_score
except ImportError:  # pragma: no cover - supports direct script execution.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from autoresearch import offline_score


REPO_ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_PATH = REPO_ROOT / "autoresearch" / "catalogs" / "scenarios.json"
EXPERIMENT_ID_RE = re.compile(r"^EXP-\d{8}-\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_DEFINITION_START = "<!-- full-codex-runner-definition:start -->"
MARKDOWN_DEFINITION_END = "<!-- full-codex-runner-definition:end -->"
SUPPRESSED_INSTRUCTION_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".cursor/rules",
    ".agents/skills",
]
NO_10X_CODEX_ENV = {
    "CODEX_HOME": (
        "inherit operator-authenticated Codex home; do not replace with a "
        "fresh temporary home unless auth is provisioned there"
    ),
    "OPENAI_API_KEY": (
        "inherit only if the operator uses API-key auth; never record the value"
    ),
}
NO_10X_ISOLATION = {
    "suppress_instruction_files": SUPPRESSED_INSTRUCTION_FILES,
    "codex_args": ["--disable", "plugins", "--ignore-user-config"],
    "codex_env": NO_10X_CODEX_ENV,
    "workspace_strategy": (
        "Run from a generated fixture workspace that omits project-level "
        "instruction files and skill directories."
    ),
    "status": "live-smoke-checked",
    "limitation": (
        "Live smoke showed no CODEX_HOME plugin or skill loader warnings with "
        "--disable plugins, but this still relies on operator-provided auth "
        "and does not prove hidden context is absent."
    ),
}


class ExperimentError(ValueError):
    pass


class BudgetError(ExperimentError):
    pass


def load_definition(path: str | Path) -> dict[str, Any]:
    definition_path = Path(path)
    text = definition_path.read_text(encoding="utf-8")
    if definition_path.suffix == ".json":
        data = json.loads(text)
    else:
        data = _load_markdown_definition(text)
    if not isinstance(data, dict):
        raise ExperimentError("experiment definition must be a JSON object")
    return data


def build_plan(
    definition: dict[str, Any],
    *,
    repo_root: Path = REPO_ROOT,
    out_dir: str | Path | None = None,
) -> dict[str, Any]:
    catalog = _load_scenario_catalog(repo_root)
    _validate_definition_shape(definition)

    scenario_by_id = {scenario["id"]: scenario for scenario in catalog["scenarios"]}
    arms = _planned_arms(definition, list(catalog["default_arms"]), repo_root)
    scenarios = _planned_scenarios(definition, scenario_by_id)
    repetitions = _positive_int(definition.get("repetitions"), "repetitions")
    budget = _budget(definition, catalog, len(arms), len(scenarios), repetitions)
    artifact_root = Path(out_dir) if out_dir else _default_output_dir(definition)
    artifact_dirs = _artifact_dirs(artifact_root)

    samples = []
    for scenario in scenarios:
        fixtures = scenario.get("fixtures", {})
        for arm in arms:
            for rep in range(repetitions):
                full_run_key = run_key(
                    definition["experiment_id"],
                    scenario["id"],
                    arm["id"],
                    rep,
                    definition["model"],
                    definition["harness"],
                    arm["instruction_digest"],
                )
                stem = _artifact_stem(full_run_key)
                workspace_dir = artifact_dirs["workspaces"] / stem
                raw_path = artifact_dirs["raw"] / f"{stem}.json"
                score_path = artifact_dirs["scores"] / f"{stem}.score.json"
                last_message_path = artifact_dirs["codex"] / f"{stem}.last-message.txt"
                json_log_path = artifact_dirs["codex"] / f"{stem}.jsonl"
                fixture_path = fixtures.get(arm["id"])
                sample = {
                    "experiment_id": definition["experiment_id"],
                    "scenario_id": scenario["id"],
                    "variant_id": arm["id"],
                    "rep": rep,
                    "model": definition["model"],
                    "harness": definition["harness"],
                    "harness_kind": "codex-full",
                    "instruction_source": arm["instruction_source"],
                    "instruction_digest": arm["instruction_digest"],
                    "fixture_path": fixture_path,
                    "source_fixture_digest": _optional_fixture_digest(repo_root, fixture_path),
                    "full_run_key": full_run_key,
                    "planned_workspace_dir": str(workspace_dir),
                    "planned_raw_output_path": str(raw_path),
                    "planned_score_artifact_path": str(score_path),
                    "planned_codex_json_log_path": str(json_log_path),
                    "planned_codex_last_message_path": str(last_message_path),
                    "planned_codex_argv": _planned_codex_argv(
                        workspace_dir,
                        scenario["prompt"],
                        last_message_path,
                        arm["id"],
                    ),
                    "planned_codex_env": _planned_codex_env(arm["id"]),
                    "live_codex_calls": 0,
                }
                if arm["id"] == "no-10x-control":
                    sample["control_isolation"] = dict(NO_10X_ISOLATION)
                samples.append(sample)

    return {
        "experiment_id": definition["experiment_id"],
        "method_tier": "FULL",
        "mode": "dry-run",
        "registered_definition": True,
        "driver": definition.get("driver"),
        "model": definition["model"],
        "harness": definition["harness"],
        "harness_kind": "codex-full",
        "arms": arms,
        "scenarios": scenarios,
        "repetitions": repetitions,
        "budget": budget,
        "artifact_root": str(artifact_root),
        "artifact_dirs": {name: str(path) for name, path in artifact_dirs.items()},
        "samples": samples,
        "live_codex_calls": 0,
        "promotion_decision": "not-performed",
        "limits": [
            "Dry-run and fixture-smoke Codex FULL harness only; no live Codex calls.",
            "No-10x control isolation is represented and smoke-checked in generated fixture workspaces, not proven against a live Codex run.",
            "Promotion decisions are outside this runner.",
            "Fixture-smoke scores remain Trust Level 1 unless separately inspected.",
        ],
    }


def run_key(
    experiment_id: str,
    scenario_id: str,
    variant_id: str,
    rep: int,
    model: str,
    harness: str,
    instruction_digest: str,
) -> str:
    payload = {
        "experiment_id": experiment_id,
        "harness": harness,
        "instruction_digest": instruction_digest,
        "model": model,
        "rep": rep,
        "scenario_id": scenario_id,
        "variant_id": variant_id,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def run_fixture_smoke(
    definition: dict[str, Any],
    out_dir: str | Path,
    *,
    repo_root: Path = REPO_ROOT,
) -> dict[str, Any]:
    plan = build_plan(definition, repo_root=repo_root, out_dir=out_dir)
    output_root = Path(out_dir)
    artifact_dirs = {name: Path(path) for name, path in plan["artifact_dirs"].items()}
    for path in artifact_dirs.values():
        path.mkdir(parents=True, exist_ok=True)

    written_samples = []
    for sample in plan["samples"]:
        if not sample.get("fixture_path"):
            raise ExperimentError(
                f"{sample['scenario_id']} {sample['variant_id']}: missing fixture path"
            )
        source_path = _resolve_path(repo_root, sample["fixture_path"])
        source_fixture = json.loads(source_path.read_text(encoding="utf-8"))
        if source_fixture.get("scenario_id") != sample["scenario_id"]:
            raise ExperimentError(
                f"{source_path}: scenario_id does not match planned {sample['scenario_id']}"
            )

        raw_path = Path(sample["planned_raw_output_path"])
        score_path = Path(sample["planned_score_artifact_path"])
        workspace_manifest_path = _write_workspace_manifest(sample, source_path)
        raw_fixture = _sample_fixture(
            source_fixture,
            sample,
            source_path,
            raw_path,
            workspace_manifest_path,
        )
        raw_path.write_text(json.dumps(raw_fixture, indent=2) + "\n", encoding="utf-8")

        score_artifact = offline_score.score_fixture(raw_path)
        errors = offline_score.validate_score_artifact(score_artifact)
        if errors:
            raise ExperimentError(
                f"{raw_path}: invalid score artifact: {'; '.join(errors)}"
            )
        score_path.write_text(
            json.dumps(score_artifact, indent=2) + "\n",
            encoding="utf-8",
        )

        sample["source_fixture_path"] = str(source_path)
        sample["source_fixture_digest"] = _digest_file(source_path)
        sample["workspace_manifest_path"] = str(workspace_manifest_path)
        sample["raw_output_path"] = str(raw_path)
        sample["score_artifact_path"] = str(score_path)
        written_samples.append(sample)

    plan["mode"] = "fixture-smoke"
    plan["samples"] = written_samples
    plan_path = output_root / "plan.json"
    plan_path.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")

    summary = {
        "experiment_id": plan["experiment_id"],
        "mode": "fixture-smoke",
        "samples_written": len(written_samples),
        "raw_output_dir": plan["artifact_dirs"]["raw"],
        "score_artifact_dir": plan["artifact_dirs"]["scores"],
        "workspace_dir": plan["artifact_dirs"]["workspaces"],
        "plan_path": str(plan_path),
        "live_codex_calls": 0,
        "promotion_decision": "not-performed",
        "budget": plan["budget"],
        "limits": plan["limits"],
    }
    (output_root / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Plan or run fixture-smoke 10x FULL experiments with Codex."
    )
    parser.add_argument(
        "--experiment",
        type=Path,
        help="Registered experiment record or equivalent local JSON definition.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned Codex FULL samples without writing artifacts.",
    )
    parser.add_argument(
        "--fixture-smoke",
        action="store_true",
        help="Write fixture-backed smoke artifacts and score them offline.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Output directory for fixture-smoke raw and score artifacts.",
    )
    args = parser.parse_args(argv)

    if args.dry_run and args.fixture_smoke:
        print("choose only one of --dry-run or --fixture-smoke", file=sys.stderr)
        return 2
    if not args.experiment:
        print(
            "non-exploratory FULL runs require a registered experiment definition via --experiment",
            file=sys.stderr,
        )
        return 2

    try:
        definition = load_definition(args.experiment)
        if args.fixture_smoke:
            out_dir = args.out or _default_output_dir(definition)
            summary = run_fixture_smoke(definition, out_dir)
            print(json.dumps(summary, indent=2))
        else:
            plan = build_plan(definition, out_dir=args.out)
            print(json.dumps(plan, indent=2))
    except (ExperimentError, OSError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


def _load_scenario_catalog(repo_root: Path) -> dict[str, Any]:
    return json.loads(
        (repo_root / "autoresearch" / "catalogs" / "scenarios.json").read_text(
            encoding="utf-8"
        )
    )


def _load_markdown_definition(text: str) -> dict[str, Any]:
    start = text.find(MARKDOWN_DEFINITION_START)
    end = text.find(MARKDOWN_DEFINITION_END)
    if start == -1 or end == -1 or end <= start:
        raise ExperimentError(
            "Markdown experiment records must include a full-codex-runner-definition JSON block"
        )
    block = text[start + len(MARKDOWN_DEFINITION_START) : end].strip()
    if block.startswith("```json"):
        block = block.removeprefix("```json").strip()
    if block.endswith("```"):
        block = block.removesuffix("```").strip()
    return json.loads(block)


def _validate_definition_shape(definition: dict[str, Any]) -> None:
    required = ("experiment_id", "method_tier", "model", "harness", "arms", "scenarios")
    for field in required:
        if field not in definition:
            raise ExperimentError(f"experiment definition missing {field}")
    if not EXPERIMENT_ID_RE.fullmatch(str(definition["experiment_id"])):
        raise ExperimentError("experiment_id must match EXP-YYYYMMDD-NNN-slug")
    if definition["method_tier"] != "FULL":
        raise ExperimentError("run_full_codex only supports method_tier FULL")
    if "codex" not in str(definition["harness"]).lower():
        raise ExperimentError("run_full_codex requires a Codex harness")
    if not isinstance(definition["arms"], list) or not definition["arms"]:
        raise ExperimentError("arms must be a non-empty list")
    if not isinstance(definition["scenarios"], list) or not definition["scenarios"]:
        raise ExperimentError("scenarios must be a non-empty list")


def _planned_arms(
    definition: dict[str, Any],
    default_arms: list[str],
    repo_root: Path,
) -> list[dict[str, Any]]:
    by_id = {}
    for arm in definition["arms"]:
        if not isinstance(arm, dict) or not arm.get("id"):
            raise ExperimentError("each arm must be an object with id")
        by_id[arm["id"]] = arm

    missing = [arm_id for arm_id in default_arms if arm_id not in by_id]
    if missing:
        raise ExperimentError(
            "FULL Codex definitions must include default arms in this first slice: "
            + ", ".join(missing)
        )

    planned = []
    for arm_id in default_arms:
        arm = by_id[arm_id]
        planned_arm = {
            "id": arm_id,
            "instruction_source": arm.get("instruction_source", ""),
            "instruction_digest": _instruction_digest(arm, arm_id, repo_root),
        }
        if arm_id == "no-10x-control":
            planned_arm["instruction_source"] = arm.get(
                "instruction_source",
                "minimal harness defaults",
            )
            planned_arm["control_isolation"] = dict(NO_10X_ISOLATION)
        planned.append(planned_arm)
    return planned


def _instruction_digest(arm: dict[str, Any], arm_id: str, repo_root: Path) -> str:
    digest = arm.get("instruction_digest")
    if isinstance(digest, str) and digest.strip():
        return digest
    text = arm.get("instruction_text")
    if isinstance(text, str):
        return _digest_bytes(text.encode("utf-8"))
    path = arm.get("instruction_path")
    if isinstance(path, str):
        return _digest_file(_resolve_path(repo_root, path))
    raise ExperimentError(f"{arm_id}: missing instruction_digest")


def _planned_scenarios(
    definition: dict[str, Any],
    scenario_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    scenarios = []
    for scenario in definition["scenarios"]:
        if isinstance(scenario, str):
            scenario = {"id": scenario}
        if not isinstance(scenario, dict) or not scenario.get("id"):
            raise ExperimentError("each scenario must be an object with id")
        scenario_id = scenario["id"]
        catalog_scenario = scenario_by_id.get(scenario_id)
        if catalog_scenario is None:
            raise ExperimentError(f"unknown scenario_id {scenario_id}")
        fixtures = scenario.get("fixtures", {})
        if fixtures and not isinstance(fixtures, dict):
            raise ExperimentError(f"{scenario_id}: fixtures must be an object")
        scenarios.append(
            {
                "id": scenario_id,
                "fixtures": fixtures,
                "prompt": scenario.get(
                    "prompt",
                    catalog_scenario.get("user_prompt_or_task_input", ""),
                ),
                "fixture_reset": scenario.get(
                    "fixture_reset",
                    catalog_scenario.get("fixture_reset", ""),
                ),
            }
        )
    return scenarios


def _budget(
    definition: dict[str, Any],
    catalog: dict[str, Any],
    arm_count: int,
    scenario_count: int,
    repetitions: int,
) -> dict[str, Any]:
    defaults = catalog["budget_defaults"]["full_campaign"]
    requested = definition.get("budget", {})
    if requested and not isinstance(requested, dict):
        raise ExperimentError("budget must be an object")

    max_runs = min(
        int(requested.get("max_harness_runs", defaults["max_harness_runs"])),
        int(defaults["max_harness_runs"]),
    )
    max_hours = min(
        float(requested.get("max_wall_clock_hours", defaults["max_wall_clock_hours"])),
        float(defaults["max_wall_clock_hours"]),
    )
    per_run_cap = float(
        requested.get(
            "suggested_per_run_cap_hours",
            defaults["suggested_per_run_cap_hours"],
        )
    )
    estimate_seconds = float(requested.get("estimated_wall_seconds_per_run", 0))
    planned_runs = arm_count * scenario_count * repetitions
    planned_hours = planned_runs * estimate_seconds / 3600

    if planned_runs > max_runs:
        raise BudgetError(
            f"planned {planned_runs} harness runs exceeds FULL cap {max_runs}"
        )
    if estimate_seconds / 3600 > per_run_cap:
        raise BudgetError(
            f"planned individual run exceeds suggested FULL per-run cap {per_run_cap:g} hours"
        )
    if planned_hours > max_hours:
        raise BudgetError(
            f"planned {planned_hours:.2f} wall-clock hours exceeds FULL cap {max_hours:g}"
        )
    return {
        "planned_harness_runs": planned_runs,
        "max_harness_runs": max_runs,
        "estimated_wall_seconds_per_run": estimate_seconds,
        "planned_wall_clock_hours": planned_hours,
        "max_wall_clock_hours": _int_if_whole(max_hours),
        "suggested_per_run_cap_hours": _int_if_whole(per_run_cap),
    }


def _planned_codex_argv(
    workspace_dir: Path,
    prompt: str,
    last_message_path: Path,
    variant_id: str,
) -> list[str]:
    argv = ["codex"]
    if variant_id == "no-10x-control":
        argv.extend(["--disable", "plugins"])
    argv.extend(
        [
        "exec",
        "--cd",
        str(workspace_dir),
        "--ephemeral",
        "--json",
        "--output-last-message",
        str(last_message_path),
        ]
    )
    if variant_id == "no-10x-control":
        argv.append("--ignore-user-config")
    argv.append(prompt)
    return argv


def _planned_codex_env(variant_id: str) -> dict[str, str]:
    if variant_id == "no-10x-control":
        return dict(NO_10X_CODEX_ENV)
    return {}


def _write_workspace_manifest(sample: dict[str, Any], source_path: Path) -> Path:
    workspace_dir = Path(sample["planned_workspace_dir"])
    workspace_dir.mkdir(parents=True, exist_ok=True)
    present = [
        path
        for path in SUPPRESSED_INSTRUCTION_FILES
        if (workspace_dir / path).exists()
    ]
    manifest = {
        "experiment_id": sample["experiment_id"],
        "scenario_id": sample["scenario_id"],
        "variant_id": sample["variant_id"],
        "rep": sample["rep"],
        "source_fixture_path": str(source_path),
        "source_fixture_digest": _digest_file(source_path),
        "planned_codex_argv": sample["planned_codex_argv"],
        "planned_codex_env": sample["planned_codex_env"],
        "live_codex_call": "not-run",
        "suppressed_instruction_files": SUPPRESSED_INSTRUCTION_FILES,
        "present_suppressed_instruction_files": present,
        "control_isolation": sample.get("control_isolation"),
    }
    manifest_path = workspace_dir / "fixture-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest_path


def _sample_fixture(
    source_fixture: dict[str, Any],
    sample: dict[str, Any],
    source_path: Path,
    raw_path: Path,
    workspace_manifest_path: Path,
) -> dict[str, Any]:
    raw_fixture = dict(source_fixture)
    raw_fixture.update(
        {
            "experiment_id": sample["experiment_id"],
            "scenario_id": sample["scenario_id"],
            "variant_id": sample["variant_id"],
            "rep": sample["rep"],
            "model": sample["model"],
            "harness": sample["harness"],
            "instruction_digest": sample["instruction_digest"],
            "full_run_key": sample["full_run_key"],
            "source_fixture_path": str(source_path),
            "source_fixture_digest": _digest_file(source_path),
            "workspace_manifest_path": str(workspace_manifest_path),
            "planned_codex_argv": sample["planned_codex_argv"],
            "planned_codex_env": sample["planned_codex_env"],
            "live_codex_calls": 0,
            "control_isolation": sample.get("control_isolation"),
            "harness_metadata": {
                "kind": "codex-full",
                "mode": "fixture-smoke",
                "planned_workspace_dir": sample["planned_workspace_dir"],
                "planned_codex_json_log_path": sample["planned_codex_json_log_path"],
                "planned_codex_last_message_path": sample[
                    "planned_codex_last_message_path"
                ],
                "planned_codex_env": sample["planned_codex_env"],
                "smoke_limit": "Codex was not invoked in this first slice.",
            },
        }
    )
    refs = [
        item
        for item in raw_fixture.get("raw_artifact_refs", [])
        if isinstance(item, str)
    ]
    for ref in (str(source_path), str(raw_path), str(workspace_manifest_path)):
        if ref not in refs:
            refs.append(ref)
    raw_fixture["raw_artifact_refs"] = refs
    return raw_fixture


def _artifact_dirs(root: Path) -> dict[str, Path]:
    return {
        "raw": root / "raw",
        "scores": root / "scores",
        "workspaces": root / "workspaces",
        "codex": root / "codex",
    }


def _default_output_dir(definition: dict[str, Any]) -> Path:
    return (
        REPO_ROOT
        / ".10x"
        / "evidence"
        / ".storage"
        / "codex-full-runs"
        / definition["experiment_id"]
    )


def _positive_int(value: Any, field: str) -> int:
    if not isinstance(value, int) or value <= 0:
        raise ExperimentError(f"{field} must be a positive integer")
    return value


def _resolve_path(repo_root: Path, value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else repo_root / path


def _optional_fixture_digest(repo_root: Path, value: str | None) -> str | None:
    if not value:
        return None
    return _digest_file(_resolve_path(repo_root, value))


def _artifact_stem(cache_key_value: str) -> str:
    return cache_key_value.replace(":", "-")


def _digest_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _digest_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _int_if_whole(value: float) -> int | float:
    return int(value) if value.is_integer() else value


if __name__ == "__main__":
    raise SystemExit(main())
