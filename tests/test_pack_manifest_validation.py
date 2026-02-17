from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

import agent_loom.pack.packs as packs


def _write_pack(
    root: Path, *, pack_id: str, manifest: dict[str, Any], files: dict[str, str]
) -> None:
    pack_root = root / pack_id
    files_root = pack_root / "files"
    files_root.mkdir(parents=True, exist_ok=True)
    (pack_root / "pack.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False),
        encoding="utf-8",
    )
    for rel, content in files.items():
        p = files_root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")


def _base_manifest(pack_id: str) -> dict[str, Any]:
    return {
        "id": pack_id,
        "version": "1.0.0",
        "description": "test pack",
        "install_roots": [".opencode"],
        "managed_globs": [".opencode/**"],
        "protected_globs": [".git/**"],
    }


def test_load_manifest_rejects_absolute_install_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(packs, "_packs_root", lambda: tmp_path)
    manifest = _base_manifest("unsafe-absolute-root")
    manifest["install_roots"] = ["/etc"]
    _write_pack(
        tmp_path,
        pack_id="unsafe-absolute-root",
        manifest=manifest,
        files={".opencode/commands/a.md": "hello\n"},
    )

    with pytest.raises(ValueError, match="install_roots\\[0\\].*repo-relative"):
        packs.load_manifest("unsafe-absolute-root")


def test_load_manifest_rejects_parent_traversal_glob(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(packs, "_packs_root", lambda: tmp_path)
    manifest = _base_manifest("unsafe-parent")
    manifest["managed_globs"] = [".opencode/../secret/**"]
    _write_pack(
        tmp_path,
        pack_id="unsafe-parent",
        manifest=manifest,
        files={".opencode/commands/a.md": "hello\n"},
    )

    with pytest.raises(ValueError, match="managed_globs\\[0\\].*cannot contain"):
        packs.load_manifest("unsafe-parent")


def test_load_manifest_rejects_glob_outside_install_roots(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(packs, "_packs_root", lambda: tmp_path)
    manifest = _base_manifest("outside-root")
    manifest["managed_globs"] = [".claude/**"]
    _write_pack(
        tmp_path,
        pack_id="outside-root",
        manifest=manifest,
        files={".opencode/commands/a.md": "hello\n"},
    )

    with pytest.raises(ValueError, match="managed_globs entry.*outside install_roots"):
        packs.load_manifest("outside-root")


def test_load_manifest_rejects_duplicate_globs_across_invariants(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(packs, "_packs_root", lambda: tmp_path)
    manifest = _base_manifest("overlap")
    manifest["scaffold_globs"] = [".opencode/**"]
    _write_pack(
        tmp_path,
        pack_id="overlap",
        manifest=manifest,
        files={".opencode/commands/a.md": "hello\n"},
    )

    with pytest.raises(ValueError, match="managed_globs and scaffold_globs overlap"):
        packs.load_manifest("overlap")


def test_iter_pack_files_rejects_unmatched_pack_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(packs, "_packs_root", lambda: tmp_path)
    manifest = _base_manifest("unmatched-file")
    manifest["managed_globs"] = [".opencode/commands/*.md"]
    _write_pack(
        tmp_path,
        pack_id="unmatched-file",
        manifest=manifest,
        files={".opencode/commands/readme.txt": "hello\n"},
    )

    with pytest.raises(
        ValueError, match="is not matched by managed_globs or scaffold_globs"
    ):
        list(packs.iter_pack_files("unmatched-file"))


def test_iter_pack_files_rejects_managed_file_matched_by_protected_glob(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(packs, "_packs_root", lambda: tmp_path)
    manifest = _base_manifest("protected-overlap")
    manifest["protected_globs"] = [".opencode/commands/**"]
    _write_pack(
        tmp_path,
        pack_id="protected-overlap",
        manifest=manifest,
        files={".opencode/commands/readme.md": "hello\n"},
    )

    with pytest.raises(ValueError, match="matches protected_globs"):
        list(packs.iter_pack_files("protected-overlap"))


def test_iter_pack_files_rejects_non_matching_managed_glob(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(packs, "_packs_root", lambda: tmp_path)
    manifest = _base_manifest("managed-miss")
    manifest["managed_globs"] = [
        ".opencode/commands/*.md",
        ".opencode/skills/**",
    ]
    _write_pack(
        tmp_path,
        pack_id="managed-miss",
        manifest=manifest,
        files={".opencode/commands/readme.md": "hello\n"},
    )

    with pytest.raises(ValueError, match="does not match any pack files"):
        list(packs.iter_pack_files("managed-miss"))
