import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from autoresearch import offline_score, run_full_codex


REPO_ROOT = Path(__file__).resolve().parents[2]


class CodexFullRunnerTest(unittest.TestCase):
    def test_dry_run_plan_includes_metadata_artifact_paths_and_isolation(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan = run_full_codex.build_plan(
                _definition(repetitions=1),
                repo_root=REPO_ROOT,
                out_dir=Path(tmp),
            )

        self.assertEqual("EXP-20260623-201-codex-full", plan["experiment_id"])
        self.assertEqual("FULL", plan["method_tier"])
        self.assertEqual("codex-full", plan["harness_kind"])
        self.assertEqual(3, plan["budget"]["planned_harness_runs"])
        self.assertEqual(20, plan["budget"]["max_harness_runs"])
        self.assertEqual(36, plan["budget"]["max_wall_clock_hours"])
        self.assertEqual(3, plan["budget"]["suggested_per_run_cap_hours"])
        self.assertEqual(3, len(plan["samples"]))

        for sample in plan["samples"]:
            self.assertEqual("fixture-codex-model", sample["model"])
            self.assertEqual("codex-cli", sample["harness"])
            self.assertTrue(sample["instruction_digest"].startswith("sha256:"))
            self.assertTrue(sample["source_fixture_digest"].startswith("sha256:"))
            self.assertIn("/raw/", sample["planned_raw_output_path"])
            self.assertIn("/scores/", sample["planned_score_artifact_path"])
            self.assertEqual(0, sample["live_codex_calls"])

        no_10x = next(
            sample for sample in plan["samples"] if sample["variant_id"] == "no-10x-control"
        )
        self.assertEqual(
            ["AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursor/rules", ".agents/skills"],
            no_10x["control_isolation"]["suppress_instruction_files"],
        )
        self.assertEqual(
            ["codex", "--disable", "plugins", "exec"],
            no_10x["planned_codex_argv"][:4],
        )
        self.assertIn("--ignore-user-config", no_10x["planned_codex_argv"])
        self.assertIn("CODEX_HOME", no_10x["planned_codex_env"])
        self.assertEqual(
            no_10x["planned_codex_env"],
            no_10x["control_isolation"]["codex_env"],
        )
        self.assertIn("hidden context", no_10x["control_isolation"]["limitation"])

    def test_non_exploratory_run_without_experiment_is_refused(self):
        stderr = io.StringIO()

        with contextlib.redirect_stderr(stderr):
            exit_code = run_full_codex.main(["--dry-run"])

        self.assertEqual(2, exit_code)
        self.assertIn("registered experiment definition", stderr.getvalue())

    def test_budget_limit_enforcement(self):
        too_many_runs = _definition(repetitions=7)
        with self.assertRaises(run_full_codex.BudgetError):
            run_full_codex.build_plan(too_many_runs, repo_root=REPO_ROOT)

        too_much_time = _definition(repetitions=1)
        too_much_time["budget"] = {"estimated_wall_seconds_per_run": 4 * 3600}
        with self.assertRaises(run_full_codex.BudgetError):
            run_full_codex.build_plan(too_much_time, repo_root=REPO_ROOT)

    def test_fixture_smoke_writes_scoreable_artifacts_and_workspace_manifests(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_full_codex.run_fixture_smoke(
                _definition(repetitions=1),
                Path(tmp),
                repo_root=REPO_ROOT,
            )

            output_root = Path(tmp)
            raw_paths = sorted((output_root / "raw").glob("*.json"))
            score_paths = sorted((output_root / "scores").glob("*.score.json"))
            workspace_manifests = sorted(
                (output_root / "workspaces").glob("*/fixture-manifest.json")
            )

            self.assertEqual(3, result["samples_written"])
            self.assertEqual(0, result["live_codex_calls"])
            self.assertTrue((output_root / "plan.json").exists())
            self.assertTrue((output_root / "summary.json").exists())
            self.assertEqual(3, len(raw_paths))
            self.assertEqual(3, len(score_paths))
            self.assertEqual(3, len(workspace_manifests))

            no_10x_manifest = None
            for manifest_path in workspace_manifests:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                self.assertEqual([], manifest["present_suppressed_instruction_files"])
                if manifest["variant_id"] == "no-10x-control":
                    no_10x_manifest = manifest

            self.assertIsNotNone(no_10x_manifest)
            self.assertEqual(
                ["codex", "--disable", "plugins", "exec"],
                no_10x_manifest["planned_codex_argv"][:4],
            )
            self.assertIn("--ignore-user-config", no_10x_manifest["planned_codex_argv"])
            self.assertIn("never record", no_10x_manifest["planned_codex_env"]["OPENAI_API_KEY"])
            self.assertEqual(
                "live-smoke-checked",
                no_10x_manifest["control_isolation"]["status"],
            )

            variants = set()
            for raw_path in raw_paths:
                raw = json.loads(raw_path.read_text(encoding="utf-8"))
                variants.add(raw["variant_id"])
                self.assertEqual("EXP-20260623-201-codex-full", raw["experiment_id"])
                self.assertEqual("codex-cli", raw["harness"])
                self.assertEqual(0, raw["live_codex_calls"])
                self.assertIn("harness_metadata", raw)
                self.assertIn("planned_codex_env", raw)
                self.assertEqual(
                    raw["planned_codex_env"],
                    raw["harness_metadata"]["planned_codex_env"],
                )
                self.assertIn(str(raw_path), raw["raw_artifact_refs"])
                artifact = offline_score.score_fixture(raw_path)
                self.assertEqual([], offline_score.validate_score_artifact(artifact))

            self.assertEqual(
                {"no-10x-control", "current-10x", "candidate-variant"},
                variants,
            )


def _definition(repetitions):
    return {
        "experiment_id": "EXP-20260623-201-codex-full",
        "status": "active",
        "method_tier": "FULL",
        "driver": "unit-test",
        "model": "fixture-codex-model",
        "harness": "codex-cli",
        "repetitions": repetitions,
        "arms": [
            {
                "id": "no-10x-control",
                "instruction_source": "minimal harness defaults",
                "instruction_digest": "sha256:no10x",
            },
            {
                "id": "current-10x",
                "instruction_source": "SKILL.md",
                "instruction_digest": "sha256:current",
            },
            {
                "id": "candidate-variant",
                "instruction_source": "candidate.md",
                "instruction_digest": "sha256:candidate",
            },
        ],
        "scenarios": [
            {
                "id": "SCN-008",
                "fixtures": {
                    "no-10x-control": "autoresearch/fixtures/offline/scn008-pass.json",
                    "current-10x": "autoresearch/fixtures/offline/scn008-pass.json",
                    "candidate-variant": "autoresearch/fixtures/offline/scn008-pass.json",
                },
            }
        ],
        "budget": {
            "estimated_wall_seconds_per_run": 0,
        },
    }


if __name__ == "__main__":
    unittest.main()
