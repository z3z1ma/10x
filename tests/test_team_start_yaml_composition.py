import json
import subprocess
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest import mock

from agent_loom.team import core as team
from agent_loom.team.composition import TeamCompositionError

_FIXTURE_DIR = Path(__file__).parent / "fixtures" / "team_composition"


def _fake_tmux_cmd(argv, **kwargs):
    _ = kwargs
    return subprocess.CompletedProcess(list(argv), 0, stdout="", stderr="")


@contextmanager
def _patched_team_start(repo_root: Path):
    with (
        mock.patch.object(team, "canonical_repo_root", return_value=repo_root),
        mock.patch.object(team, "_require_bin"),
        mock.patch.object(team, "_deny_if_role_set"),
        mock.patch.object(team, "tmux_has_session", return_value=False),
        mock.patch.object(team, "tmux_cmd", side_effect=_fake_tmux_cmd),
        mock.patch.object(team, "tmux_set_option"),
        mock.patch.object(team, "tmux_window_exists", return_value=False),
        mock.patch.object(team, "tmux_mark_pane"),
        mock.patch.object(team, "tmux_format", return_value="%1"),
    ):
        yield


class TestTeamStartYamlComposition(unittest.TestCase):
    def test_missing_composition_file_fails_fast(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            missing_path = repo_root / "missing-composition.yaml"
            with _patched_team_start(repo_root):
                team.init_agents(repo=repo_root, create_missing=True)
                with self.assertRaises(TeamCompositionError) as ctx:
                    team.start(
                        team="MiyagiDo",
                        repo=repo_root,
                        composition=str(missing_path),
                    )

            self.assertIn("Unable to read composition file", str(ctx.exception))

    def test_invalid_yaml_fails_fast(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            composition_path = repo_root / "composition.yaml"
            composition_path.write_text("version: [1", encoding="utf-8")

            with _patched_team_start(repo_root):
                team.init_agents(repo=repo_root, create_missing=True)
                with self.assertRaises(TeamCompositionError) as ctx:
                    team.start(
                        team="MiyagiDo",
                        repo=repo_root,
                        composition=str(composition_path),
                    )

            self.assertIn("invalid YAML", str(ctx.exception))

    def test_invalid_schema_fails_fast(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            composition_path = repo_root / "composition.yaml"
            composition_path.write_text(
                (_FIXTURE_DIR / "invalid_enum.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            with _patched_team_start(repo_root):
                team.init_agents(repo=repo_root, create_missing=True)
                with self.assertRaises(TeamCompositionError) as ctx:
                    team.start(
                        team="MiyagiDo",
                        repo=repo_root,
                        composition=str(composition_path),
                    )

            self.assertIn("members[0].lifecycle", str(ctx.exception))

    def test_valid_composition_persists_and_survives_resume(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo_root = Path(td)
            composition_path = repo_root / "composition.yaml"
            composition_path.write_text(
                (_FIXTURE_DIR / "valid_minimal.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            with _patched_team_start(repo_root):
                team.init_agents(repo=repo_root, create_missing=True)
                start_res = team.start(
                    team="MiyagiDo",
                    repo=repo_root,
                    composition=str(composition_path),
                )

                run_path = Path(start_res.run_dir) / "run.json"
                first_run = json.loads(run_path.read_text(encoding="utf-8"))
                self.assertIn("composition", first_run)
                self.assertEqual(
                    str(((first_run.get("composition") or {}).get("spec") or {}).get("version") or 0),
                    "1",
                )
                self.assertEqual(
                    str(
                        ((((first_run.get("composition") or {}).get("spec") or {}).get("metadata") or {}).get("name") or "")
                    ),
                    "YAML Sprint Foundations",
                )

                composition_path.write_text(
                    composition_path.read_text(encoding="utf-8").replace(
                        "YAML Sprint Foundations", "Mutated After Start"
                    ),
                    encoding="utf-8",
                )

                team.start(team="MiyagiDo", repo=repo_root)
                second_run = json.loads(run_path.read_text(encoding="utf-8"))

                self.assertEqual(
                    str(
                        ((((second_run.get("composition") or {}).get("spec") or {}).get("metadata") or {}).get("name") or "")
                    ),
                    "YAML Sprint Foundations",
                )

                with mock.patch.object(
                    team,
                    "_paths_for",
                    return_value=team.RunPaths(repo_root=repo_root, team="MiyagiDo"),
                ):
                    status_res = team.status(team="MiyagiDo", repo=repo_root)
                self.assertEqual(str(status_res.composition.get("name") or ""), "YAML Sprint Foundations")
                self.assertEqual(int(status_res.composition.get("members") or 0), 2)


if __name__ == "__main__":
    unittest.main()
