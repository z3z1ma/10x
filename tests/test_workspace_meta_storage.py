import tempfile
import unittest
from pathlib import Path


from agent_loom.core.fs import fs_escape
from agent_loom.workspace.worktree_meta import (
    poly_group_annotate,
    poly_group_meta_path,
    poly_group_touch,
    repo_worktree_annotate,
    repo_worktree_meta_path,
    repo_worktree_touch,
)


class TestWorkspaceMetaStorage(unittest.TestCase):
    def test_repo_worktree_meta_writes_under_meta_dir(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            repo.mkdir(parents=True, exist_ok=True)
            branch = "feature/one"

            res = repo_worktree_annotate(
                repo_root=repo,
                branch=branch,
                purpose="test",
                ttl="1d",
            )
            meta_path = Path(str(res.get("meta_path") or "")).resolve()
            self.assertTrue(meta_path.exists())
            self.assertIn(
                str(repo / ".loom-repo" / "meta" / "worktrees"), str(meta_path)
            )

            old = repo / ".loom-repo" / "worktrees" / f"{fs_escape(branch)}.json"
            self.assertFalse(old.exists())

    def test_poly_group_meta_writes_under_meta_dir(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            ws = Path(td) / "ws"
            ws.mkdir(parents=True, exist_ok=True)
            group = "g/one"

            res = poly_group_annotate(
                ws_root=ws,
                group=group,
                purpose="test",
                ttl="1d",
            )
            meta_path = Path(str(res.get("meta_path") or "")).resolve()
            self.assertTrue(meta_path.exists())
            self.assertIn(str(ws / ".loom" / "meta" / "groups"), str(meta_path))

            old = ws / ".loom" / "worktrees" / f"{fs_escape(group)}.json"
            self.assertFalse(old.exists())

    def test_repo_meta_migrates_from_v1_location(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td) / "repo"
            repo.mkdir(parents=True, exist_ok=True)
            branch = "feat/x"

            old = repo / ".loom-repo" / "worktrees" / f"{fs_escape(branch)}.json"
            old.parent.mkdir(parents=True, exist_ok=True)
            old.write_text(
                '{"branch": "feat/x", "ttl_seconds": 10}\n', encoding="utf-8"
            )

            repo_worktree_touch(repo_root=repo, branch=branch)

            new = repo_worktree_meta_path(repo, branch)
            self.assertTrue(new.exists())
            self.assertFalse(old.exists())

    def test_poly_meta_migrates_from_v1_location(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            ws = Path(td) / "ws"
            ws.mkdir(parents=True, exist_ok=True)
            group = "g1"

            old = ws / ".loom" / "worktrees" / f"{fs_escape(group)}.json"
            old.parent.mkdir(parents=True, exist_ok=True)
            old.write_text('{"group": "g1", "ttl_seconds": 10}\n', encoding="utf-8")

            poly_group_touch(ws_root=ws, group=group)

            new = poly_group_meta_path(ws, group)
            self.assertTrue(new.exists())
            self.assertFalse(old.exists())


if __name__ == "__main__":
    unittest.main()
