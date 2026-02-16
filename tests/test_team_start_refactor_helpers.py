import json
import tempfile
import unittest
from pathlib import Path

from agent_loom.team import core as team


class TestTeamStartRefactorHelpers(unittest.TestCase):
    def _paths(self, repo_root: Path, team_name: str = "cobra") -> team.RunPaths:
        paths = team.RunPaths(repo_root=repo_root, team=team_name)
        team._ensure_start_run_paths(paths)
        return paths

    def test_validated_start_max_headcount(self) -> None:
        self.assertIsNone(team._validated_start_max_headcount(None))
        self.assertEqual(team._validated_start_max_headcount(3), 3)
        self.assertEqual(team._validated_start_max_headcount("4"), 4)
        with self.assertRaises(team.TeamError) as ctx:
            team._validated_start_max_headcount(-1)
        self.assertEqual(ctx.exception.code, "ARG")

    def test_start_create_run_persists_core_defaults(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            paths = self._paths(repo_root)

            run = team._start_create_run(
                paths=paths,
                root=repo_root,
                team="cobra",
                objective="ship phase three",
                session="session-cobra",
                requested_harness="opencode",
                requested_bin="custom-opencode",
                roster_state=None,
                mounts=None,
                clear_mounts=False,
                max_headcount=5,
                target_branch="dev/next",
                remote="origin",
                push=True,
                model="gpt-main",
                manager_model="gpt-manager",
                architect_model="",
                worker_model="",
                integrator_model="",
            )

            self.assertEqual(str(run.get("harness") or ""), "opencode")
            self.assertEqual(str(run.get("session") or ""), "session-cobra")
            self.assertEqual(
                str(((run.get("merge") or {}).get("config") or {}).get("target_branch") or ""),
                "dev/next",
            )
            self.assertEqual(
                str((run.get("defaults") or {}).get("base_ref") or ""),
                "dev/next",
            )
            self.assertEqual(
                str((((run.get("opencode") or {}).get("models") or {}).get("manager") or "")),
                "gpt-manager",
            )
            self.assertEqual(
                str((run.get("opencode") or {}).get("bin") or ""),
                "custom-opencode",
            )
            self.assertEqual(
                int(((run.get("limits") or {}).get("max_headcount") or 0)),
                5,
            )

            persisted = json.loads(paths.run_file.read_text(encoding="utf-8"))
            self.assertEqual(str(persisted.get("session") or ""), "session-cobra")

    def test_start_update_existing_run_adopts_persisted_session(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            paths = self._paths(repo_root)
            team._start_create_run(
                paths=paths,
                root=repo_root,
                team="cobra",
                objective="seed",
                session="persisted-session",
                requested_harness="opencode",
                requested_bin="",
                roster_state=None,
                mounts=None,
                clear_mounts=False,
                max_headcount=None,
                target_branch="main",
                remote="origin",
                push=None,
                model="",
                manager_model="",
                architect_model="",
                worker_model="",
                integrator_model="",
            )

            updated_run, adopted_session = team._start_update_existing_run(
                paths=paths,
                root=repo_root,
                session="cli-session",
                session_provided=False,
                requested_harness="opencode",
                requested_bin="",
                harness_provided=False,
                roster_state=None,
                roster_harness="",
                mounts=None,
                clear_mounts=False,
                max_headcount=None,
                target_branch="",
                remote="",
                push=None,
                model="",
                manager_model="override-manager",
                architect_model="",
                worker_model="",
                integrator_model="",
            )

            self.assertEqual(adopted_session, "persisted-session")
            self.assertEqual(
                str(
                    (((updated_run.get("opencode") or {}).get("models") or {}).get("manager") or "")
                ),
                "override-manager",
            )

    def test_start_update_existing_run_respects_explicit_session_and_clear_mounts(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            (repo_root / ".venv").mkdir(parents=True, exist_ok=True)
            paths = self._paths(repo_root)
            team._start_create_run(
                paths=paths,
                root=repo_root,
                team="cobra",
                objective="seed",
                session="persisted-session",
                requested_harness="opencode",
                requested_bin="",
                roster_state=None,
                mounts=[".venv:.venv"],
                clear_mounts=False,
                max_headcount=None,
                target_branch="main",
                remote="origin",
                push=None,
                model="",
                manager_model="",
                architect_model="",
                worker_model="",
                integrator_model="",
            )

            updated_run, updated_session = team._start_update_existing_run(
                paths=paths,
                root=repo_root,
                session="explicit-session",
                session_provided=True,
                requested_harness="opencode",
                requested_bin="",
                harness_provided=False,
                roster_state=None,
                roster_harness="",
                mounts=None,
                clear_mounts=True,
                max_headcount=None,
                target_branch="",
                remote="",
                push=None,
                model="",
                manager_model="",
                architect_model="",
                worker_model="",
                integrator_model="",
            )

            self.assertEqual(updated_session, "explicit-session")
            self.assertEqual(str(updated_run.get("session") or ""), "explicit-session")
            self.assertEqual(list(updated_run.get("mounts") or []), [])

    def test_start_create_run_cli_mounts_take_precedence_over_roster_mounts(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            (repo_root / ".env").write_text("KEY=VALUE\n", encoding="utf-8")
            (repo_root / ".venv").mkdir(parents=True, exist_ok=True)
            paths = self._paths(repo_root)

            run = team._start_create_run(
                paths=paths,
                root=repo_root,
                team="cobra",
                objective="seed",
                session="persisted-session",
                requested_harness="opencode",
                requested_bin="",
                roster_state={
                    "source": str((repo_root / "roster.yaml").resolve()),
                    "loaded_at": "2026-02-16T00:00:00Z",
                    "spec": {"mounts": [".venv:.venv"]},
                },
                mounts=[".env:.env"],
                clear_mounts=False,
                max_headcount=None,
                target_branch="main",
                remote="origin",
                push=None,
                model="",
                manager_model="",
                architect_model="",
                worker_model="",
                integrator_model="",
            )

            self.assertEqual(
                list(run.get("mounts") or []),
                [{"src": ".env", "dst": ".env"}],
            )


if __name__ == "__main__":
    unittest.main()
