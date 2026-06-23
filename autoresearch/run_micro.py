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
MARKDOWN_DEFINITION_START = "<!-- micro-runner-definition:start -->"
MARKDOWN_DEFINITION_END = "<!-- micro-runner-definition:end -->"
NO_10X_ISOLATION = {
    "suppress_instruction_files": [
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        ".cursor/rules",
        ".agents/skills",
    ],
    "reason": "Prevent project-level 10x instructions from contaminating the no-10x control arm.",
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


def build_plan(definition: dict[str, Any], *, repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    catalog = _load_scenario_catalog(repo_root)
    _validate_definition_shape(definition)

    scenario_ids = {scenario["id"] for scenario in catalog["scenarios"]}
    default_arms = list(catalog["default_arms"])
    arms = _planned_arms(definition, default_arms)
    scenarios = _planned_scenarios(definition, scenario_ids)
    repetitions = _positive_int(definition.get("repetitions"), "repetitions")
    budget = _budget(definition, catalog, len(arms), len(scenarios), repetitions)

    samples = []
    for scenario in scenarios:
        fixtures = scenario.get("fixtures", {})
        for arm in arms:
            for rep in range(repetitions):
                sample = {
                    "experiment_id": definition["experiment_id"],
                    "scenario_id": scenario["id"],
                    "variant_id": arm["id"],
                    "rep": rep,
                    "model": definition["model"],
                    "harness": definition["harness"],
                    "instruction_digest": arm["instruction_digest"],
                    "cache_key": cache_key(
                        scenario["id"],
                        arm["id"],
                        rep,
                        definition["model"],
                        arm["instruction_digest"],
                    ),
                    "fixture_path": fixtures.get(arm["id"]),
                    "live_calls": 0,
                }
                if arm["id"] == "no-10x-control":
                    sample["control_isolation"] = dict(NO_10X_ISOLATION)
                samples.append(sample)

    return {
        "experiment_id": definition["experiment_id"],
        "method_tier": "MICRO",
        "mode": "plan",
        "registered_definition": True,
        "driver": definition.get("driver"),
        "model": definition["model"],
        "harness": definition["harness"],
        "arms": arms,
        "scenarios": scenarios,
        "repetitions": repetitions,
        "budget": budget,
        "samples": samples,
        "live_calls": 0,
        "promotion_decision": "not-performed",
        "limits": [
            "Dry-run and fixture-backed MICRO runner only; no live provider or harness calls.",
            "Promotion decisions are outside this runner.",
            "Fixture-backed scores remain Trust Level 1 unless separately inspected.",
        ],
    }


def cache_key(
    scenario_id: str,
    variant_id: str,
    rep: int,
    model: str,
    instruction_digest: str,
) -> str:
    payload = {
        "instruction_digest": instruction_digest,
        "model": model,
        "rep": rep,
        "scenario_id": scenario_id,
        "variant_id": variant_id,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def run_fixture_backed(
    definition: dict[str, Any],
    out_dir: str | Path,
    *,
    repo_root: Path = REPO_ROOT,
) -> dict[str, Any]:
    plan = build_plan(definition, repo_root=repo_root)
    output_root = Path(out_dir)
    raw_dir = output_root / "raw"
    score_dir = output_root / "scores"
    raw_dir.mkdir(parents=True, exist_ok=True)
    score_dir.mkdir(parents=True, exist_ok=True)

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

        stem = _artifact_stem(sample["cache_key"])
        raw_path = raw_dir / f"{stem}.json"
        score_path = score_dir / f"{stem}.score.json"
        raw_fixture = _sample_fixture(source_fixture, sample, source_path, raw_path)
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
        sample["raw_output_path"] = str(raw_path)
        sample["score_artifact_path"] = str(score_path)
        written_samples.append(sample)

    plan["mode"] = "fixture-backed"
    plan["samples"] = written_samples
    plan["artifact_dirs"] = {
        "raw": str(raw_dir),
        "scores": str(score_dir),
    }
    (output_root / "plan.json").write_text(
        json.dumps(plan, indent=2) + "\n",
        encoding="utf-8",
    )

    summary = {
        "experiment_id": plan["experiment_id"],
        "mode": "fixture-backed",
        "samples_written": len(written_samples),
        "raw_output_dir": str(raw_dir),
        "score_artifact_dir": str(score_dir),
        "plan_path": str(output_root / "plan.json"),
        "live_calls": 0,
        "promotion_decision": "not-performed",
        "limits": plan["limits"],
    }
    (output_root / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Plan or run fixture-backed 10x MICRO experiments."
    )
    parser.add_argument(
        "--experiment",
        type=Path,
        help="Registered experiment record or equivalent local JSON definition.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned MICRO samples without writing artifacts.",
    )
    parser.add_argument(
        "--fixture-backed",
        action="store_true",
        help="Copy configured fixtures and score them with offline_score.py.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Output directory for fixture-backed raw and score artifacts.",
    )
    args = parser.parse_args(argv)

    if args.dry_run and args.fixture_backed:
        print("choose only one of --dry-run or --fixture-backed", file=sys.stderr)
        return 2
    if not args.experiment:
        print(
            "non-exploratory MICRO runs require a registered experiment definition via --experiment",
            file=sys.stderr,
        )
        return 2

    try:
        definition = load_definition(args.experiment)
        if args.fixture_backed:
            out_dir = args.out or _default_output_dir(definition)
            summary = run_fixture_backed(definition, out_dir)
            print(json.dumps(summary, indent=2))
        else:
            plan = build_plan(definition)
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
            "Markdown experiment records must include a micro-runner-definition JSON block"
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
    if definition["method_tier"] != "MICRO":
        raise ExperimentError("run_micro only supports method_tier MICRO")
    if not isinstance(definition["arms"], list) or not definition["arms"]:
        raise ExperimentError("arms must be a non-empty list")
    if not isinstance(definition["scenarios"], list) or not definition["scenarios"]:
        raise ExperimentError("scenarios must be a non-empty list")


def _planned_arms(definition: dict[str, Any], default_arms: list[str]) -> list[dict[str, Any]]:
    by_id = {}
    for arm in definition["arms"]:
        if not isinstance(arm, dict) or not arm.get("id"):
            raise ExperimentError("each arm must be an object with id")
        by_id[arm["id"]] = arm

    missing = [arm_id for arm_id in default_arms if arm_id not in by_id]
    if missing:
        raise ExperimentError(
            "MICRO definitions must include default arms unless a later runner slice supports exceptions: "
            + ", ".join(missing)
        )

    planned = []
    for arm_id in default_arms:
        arm = by_id[arm_id]
        digest = _instruction_digest(arm, arm_id)
        planned_arm = {
            "id": arm_id,
            "instruction_source": arm.get("instruction_source", ""),
            "instruction_digest": digest,
        }
        if arm_id == "no-10x-control":
            planned_arm["instruction_source"] = arm.get(
                "instruction_source",
                "minimal harness defaults",
            )
            planned_arm["control_isolation"] = dict(NO_10X_ISOLATION)
        planned.append(planned_arm)
    return planned


def _instruction_digest(arm: dict[str, Any], arm_id: str) -> str:
    digest = arm.get("instruction_digest")
    if isinstance(digest, str) and digest.strip():
        return digest
    text = arm.get("instruction_text")
    if isinstance(text, str):
        return _digest_bytes(text.encode("utf-8"))
    path = arm.get("instruction_path")
    if isinstance(path, str):
        return _digest_bytes(Path(path).read_bytes())
    raise ExperimentError(f"{arm_id}: missing instruction_digest")


def _planned_scenarios(
    definition: dict[str, Any],
    catalog_scenario_ids: set[str],
) -> list[dict[str, Any]]:
    scenarios = []
    for scenario in definition["scenarios"]:
        if isinstance(scenario, str):
            scenario = {"id": scenario}
        if not isinstance(scenario, dict) or not scenario.get("id"):
            raise ExperimentError("each scenario must be an object with id")
        if scenario["id"] not in catalog_scenario_ids:
            raise ExperimentError(f"unknown scenario_id {scenario['id']}")
        fixtures = scenario.get("fixtures", {})
        if fixtures and not isinstance(fixtures, dict):
            raise ExperimentError(f"{scenario['id']}: fixtures must be an object")
        scenarios.append({"id": scenario["id"], "fixtures": fixtures})
    return scenarios


def _budget(
    definition: dict[str, Any],
    catalog: dict[str, Any],
    arm_count: int,
    scenario_count: int,
    repetitions: int,
) -> dict[str, Any]:
    defaults = catalog["budget_defaults"]["micro_campaign"]
    requested = definition.get("budget", {})
    if requested and not isinstance(requested, dict):
        raise ExperimentError("budget must be an object")

    max_samples = min(
        int(requested.get("max_subject_agent_samples", defaults["max_subject_agent_samples"])),
        int(defaults["max_subject_agent_samples"]),
    )
    max_hours = min(
        float(requested.get("max_wall_clock_hours", defaults["max_wall_clock_hours"])),
        float(defaults["max_wall_clock_hours"]),
    )
    estimate_seconds = float(requested.get("estimated_wall_seconds_per_sample", 0))
    planned_samples = arm_count * scenario_count * repetitions
    planned_hours = planned_samples * estimate_seconds / 3600

    if planned_samples > max_samples:
        raise BudgetError(
            f"planned {planned_samples} subject-agent samples exceeds MICRO cap {max_samples}"
        )
    if planned_hours > max_hours:
        raise BudgetError(
            f"planned {planned_hours:.2f} wall-clock hours exceeds MICRO cap {max_hours:g}"
        )
    return {
        "planned_subject_agent_samples": planned_samples,
        "max_subject_agent_samples": max_samples,
        "estimated_wall_seconds_per_sample": estimate_seconds,
        "planned_wall_clock_hours": planned_hours,
        "max_wall_clock_hours": int(max_hours) if max_hours.is_integer() else max_hours,
    }


def _positive_int(value: Any, field: str) -> int:
    if not isinstance(value, int) or value <= 0:
        raise ExperimentError(f"{field} must be a positive integer")
    return value


def _resolve_path(repo_root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else repo_root / path


def _sample_fixture(
    source_fixture: dict[str, Any],
    sample: dict[str, Any],
    source_path: Path,
    raw_path: Path,
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
            "micro_cache_key": sample["cache_key"],
            "source_fixture_path": str(source_path),
            "source_fixture_digest": _digest_file(source_path),
        }
    )
    refs = [
        item
        for item in raw_fixture.get("raw_artifact_refs", [])
        if isinstance(item, str)
    ]
    for ref in (str(source_path), str(raw_path)):
        if ref not in refs:
            refs.append(ref)
    raw_fixture["raw_artifact_refs"] = refs
    return raw_fixture


def _default_output_dir(definition: dict[str, Any]) -> Path:
    return (
        REPO_ROOT
        / ".10x"
        / "evidence"
        / ".storage"
        / "micro-runs"
        / definition["experiment_id"]
    )


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


if __name__ == "__main__":
    raise SystemExit(main())
