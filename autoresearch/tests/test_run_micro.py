import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from autoresearch import offline_score, run_micro


REPO_ROOT = Path(__file__).resolve().parents[2]


class MicroRunnerTest(unittest.TestCase):
    def test_dry_run_plan_includes_arms_cache_keys_and_isolation(self):
        definition = _definition(repetitions=2)

        plan = run_micro.build_plan(definition, repo_root=REPO_ROOT)

        self.assertEqual("EXP-20260623-101-micro-runner", plan["experiment_id"])
        self.assertEqual(
            ["no-10x-control", "current-10x", "candidate-variant"],
            [arm["id"] for arm in plan["arms"]],
        )
        self.assertEqual(6, plan["budget"]["planned_subject_agent_samples"])
        self.assertEqual(300, plan["budget"]["max_subject_agent_samples"])
        self.assertEqual(10, plan["budget"]["max_wall_clock_hours"])
        self.assertEqual(6, len(plan["samples"]))
        self.assertTrue(all(sample["cache_key"].startswith("sha256:") for sample in plan["samples"]))

        no_10x = next(arm for arm in plan["arms"] if arm["id"] == "no-10x-control")
        self.assertEqual("minimal harness defaults", no_10x["instruction_source"])
        self.assertEqual(
            ["AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursor/rules", ".agents/skills"],
            no_10x["control_isolation"]["suppress_instruction_files"],
        )

    def test_non_exploratory_run_without_experiment_is_refused(self):
        stderr = io.StringIO()

        with contextlib.redirect_stderr(stderr):
            exit_code = run_micro.main(["--dry-run"])

        self.assertEqual(2, exit_code)
        self.assertIn("registered experiment definition", stderr.getvalue())

    def test_budget_limit_enforcement(self):
        too_many_samples = _definition(repetitions=101)
        with self.assertRaises(run_micro.BudgetError):
            run_micro.build_plan(too_many_samples, repo_root=REPO_ROOT)

        too_much_time = _definition(repetitions=1)
        too_much_time["budget"] = {"estimated_wall_seconds_per_sample": 13000}
        with self.assertRaises(run_micro.BudgetError):
            run_micro.build_plan(too_much_time, repo_root=REPO_ROOT)

    def test_cache_key_is_deterministic(self):
        first = run_micro.cache_key(
            "SCN-001",
            "current-10x",
            0,
            "fixture-model",
            "sha256:current",
        )
        second = run_micro.cache_key(
            scenario_id="SCN-001",
            variant_id="current-10x",
            rep=0,
            model="fixture-model",
            instruction_digest="sha256:current",
        )
        changed = run_micro.cache_key(
            "SCN-001",
            "candidate-variant",
            0,
            "fixture-model",
            "sha256:current",
        )

        self.assertEqual(first, second)
        self.assertNotEqual(first, changed)
        self.assertTrue(first.startswith("sha256:"))

    def test_fixture_backed_run_writes_raw_and_score_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_micro.run_fixture_backed(
                _definition(repetitions=1),
                Path(tmp),
                repo_root=REPO_ROOT,
            )

            output_root = Path(tmp)
            raw_paths = sorted((output_root / "raw").glob("*.json"))
            score_paths = sorted((output_root / "scores").glob("*.score.json"))

            self.assertEqual(3, result["samples_written"])
            self.assertTrue((output_root / "plan.json").exists())
            self.assertTrue((output_root / "summary.json").exists())
            self.assertEqual(3, len(raw_paths))
            self.assertEqual(3, len(score_paths))

            variants = set()
            for raw_path in raw_paths:
                raw = json.loads(raw_path.read_text(encoding="utf-8"))
                variants.add(raw["variant_id"])
                self.assertEqual("EXP-20260623-101-micro-runner", raw["experiment_id"])
                self.assertEqual("micro-fixture", raw["harness"])
                self.assertIn(str(raw_path), raw["raw_artifact_refs"])

            self.assertEqual(
                {"no-10x-control", "current-10x", "candidate-variant"},
                variants,
            )

            for score_path in score_paths:
                artifact = json.loads(score_path.read_text(encoding="utf-8"))
                self.assertEqual([], offline_score.validate_score_artifact(artifact))
                self.assertIn(artifact["variant_id"], variants)


def _definition(repetitions):
    return {
        "experiment_id": "EXP-20260623-101-micro-runner",
        "status": "active",
        "method_tier": "MICRO",
        "driver": "unit-test",
        "model": "fixture-model",
        "harness": "micro-fixture",
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
                "id": "SCN-001",
                "fixtures": {
                    "no-10x-control": "autoresearch/fixtures/offline/scn001-fail.json",
                    "current-10x": "autoresearch/fixtures/offline/scn001-pass.json",
                    "candidate-variant": "autoresearch/fixtures/offline/scn001-pass.json",
                },
            }
        ],
        "budget": {
            "estimated_wall_seconds_per_sample": 0,
        },
    }


if __name__ == "__main__":
    unittest.main()
