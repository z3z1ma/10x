import unittest

from agent_loom.team.constants import ROLE_ARCHITECT, ROLE_INTEGRATOR, ROLE_MANAGER, ROLE_WORKER
from agent_loom.team.errors import TeamError
from agent_loom.team.start_state import (
    StartMergeOptions,
    StartModelOverrides,
    adopt_start_session,
    apply_merge_options,
    apply_model_overrides,
    normalize_harness_configs,
)


class TestTeamStartState(unittest.TestCase):
    def test_normalize_harness_configs_migrates_merge_agent_and_model_slots(self) -> None:
        run = {
            "opencode": {
                "merge_agent": "legacy-integrator",
                "models": {ROLE_WORKER: "worker-model"},
            },
            "run_id": "abcd1234efgh5678",
        }

        normalize_harness_configs(run)
        opencode = dict(run.get("opencode") or {})
        self.assertEqual(str(opencode.get("integrator_agent") or ""), "legacy-integrator")
        self.assertNotIn("merge_agent", opencode)

        models = dict(opencode.get("models") or {})
        self.assertEqual(str(models.get(ROLE_WORKER) or ""), "worker-model")
        self.assertIn(ROLE_MANAGER, models)
        self.assertIn(ROLE_ARCHITECT, models)
        self.assertIn(ROLE_INTEGRATOR, models)

    def test_apply_model_overrides_updates_selected_roles_only(self) -> None:
        run = {
            "opencode": {
                "model": "",
                "models": {
                    ROLE_MANAGER: "",
                    ROLE_WORKER: "",
                    ROLE_ARCHITECT: "",
                    ROLE_INTEGRATOR: "",
                },
            }
        }

        apply_model_overrides(
            run,
            harness="opencode",
            overrides=StartModelOverrides.from_inputs(
                model="gpt-main",
                manager_model="",
                worker_model="gpt-worker",
                architect_model="",
                integrator_model="gpt-integrator",
            ),
        )

        opencode = dict(run.get("opencode") or {})
        self.assertEqual(str(opencode.get("model") or ""), "gpt-main")
        models = dict(opencode.get("models") or {})
        self.assertEqual(str(models.get(ROLE_WORKER) or ""), "gpt-worker")
        self.assertEqual(str(models.get(ROLE_INTEGRATOR) or ""), "gpt-integrator")
        self.assertEqual(str(models.get(ROLE_MANAGER) or ""), "")

    def test_apply_merge_options_updates_config_and_branch(self) -> None:
        run = {
            "run_id": "abcd1234efgh5678",
            "merge": {"items": [], "branch": "", "config": {}},
        }
        cfg = apply_merge_options(
            run,
            options=StartMergeOptions(target_branch="release/v1", remote="upstream", push=False),
        )

        self.assertEqual(str(cfg.get("target_branch") or ""), "release/v1")
        self.assertEqual(str(cfg.get("remote") or ""), "upstream")
        self.assertEqual(bool(cfg.get("push")), False)
        branch = str(((run.get("merge") or {}).get("branch") or ""))
        self.assertEqual(branch, "team/merge-queue-abcd1234")

    def test_apply_merge_options_rejects_invalid_branch(self) -> None:
        run = {
            "run_id": "abcd1234efgh5678",
            "merge": {"items": [], "branch": "", "config": {}},
        }
        with self.assertRaises(TeamError) as ctx:
            apply_merge_options(
                run,
                options=StartMergeOptions(target_branch="!!!!", remote="origin", push=True),
            )
        self.assertEqual(ctx.exception.code, "ARG")

    def test_adopt_start_session_prefers_persisted_when_not_explicit(self) -> None:
        run = {"session": "persisted-session"}
        adopted = adopt_start_session(
            run,
            session="cli-session",
            session_provided=False,
        )
        self.assertEqual(adopted, "persisted-session")

        explicit = adopt_start_session(
            run,
            session="explicit-session",
            session_provided=True,
        )
        self.assertEqual(explicit, "explicit-session")
        self.assertEqual(str(run.get("session") or ""), "explicit-session")


if __name__ == "__main__":
    unittest.main()
