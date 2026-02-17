from __future__ import annotations

import fnmatch
import re
from importlib import resources
from pathlib import Path
from typing import Iterable, List, Tuple

import yaml

from agent_loom.pack.models import PackManifest


_WILDCARD_CHARS = {"*", "?", "["}


def _packs_root():
    return resources.files("agent_loom.pack").joinpath("packs")


def list_pack_ids() -> List[str]:
    root = _packs_root()
    if not root.is_dir():
        return []
    ids: List[str] = []
    for child in root.iterdir():
        if child.is_dir() and child.joinpath("pack.yaml").is_file():
            ids.append(child.name)
    return sorted(ids)


def pack_dir(pack_id: str):
    return _packs_root().joinpath(pack_id)


def normalize_repo_relpath(path: str, *, pack_id: str, field: str) -> str:
    raw = str(path).strip().replace("\\", "/")
    if not raw:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: {field} must be a non-empty path"
        )
    if raw.startswith("/") or re.match(r"^[A-Za-z]:($|/)", raw):
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: {field} must be repo-relative (not absolute)"
        )

    parts = [part for part in raw.split("/") if part]
    if not parts:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: {field} must be a non-empty path"
        )
    if any(part in {".", ".."} for part in parts):
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: {field} cannot contain '.' or '..' segments"
        )
    return "/".join(parts)


def _normalize_roots(roots: List[str], *, pack_id: str) -> List[str]:
    normalized: List[str] = []
    seen: set[str] = set()
    for idx, root in enumerate(roots):
        value = normalize_repo_relpath(root, pack_id=pack_id, field=f"install_roots[{idx}]")
        if value in seen:
            raise ValueError(
                f"invalid pack.yaml for {pack_id}: duplicate install root '{value}'"
            )
        seen.add(value)
        normalized.append(value)
    return normalized


def _normalize_globs(globs: List[str], *, pack_id: str, field: str) -> List[str]:
    normalized: List[str] = []
    seen: set[str] = set()
    for idx, glob in enumerate(globs):
        value = normalize_repo_relpath(glob, pack_id=pack_id, field=f"{field}[{idx}]")
        if value in seen:
            raise ValueError(
                f"invalid pack.yaml for {pack_id}: duplicate {field} entry '{value}'"
            )
        seen.add(value)
        normalized.append(value)
    return normalized


def _path_within_root(path: str, root: str) -> bool:
    return path == root or path.startswith(f"{root}/")


def _glob_anchor(glob: str) -> str:
    wildcard_index = next((idx for idx, ch in enumerate(glob) if ch in _WILDCARD_CHARS), -1)
    if wildcard_index < 0:
        return glob
    prefix = glob[:wildcard_index]
    if prefix.endswith("/"):
        return prefix.rstrip("/")
    prefix = prefix.rstrip("/")
    if "/" in prefix:
        return prefix.rsplit("/", 1)[0]
    return prefix


def _validate_manifest_contract(manifest: PackManifest, *, pack_id: str) -> PackManifest:
    roots = _normalize_roots(manifest.install_roots, pack_id=pack_id)
    managed = _normalize_globs(manifest.managed_globs, pack_id=pack_id, field="managed_globs")
    scaffold = _normalize_globs(
        manifest.scaffold_globs, pack_id=pack_id, field="scaffold_globs"
    )
    protected = _normalize_globs(
        manifest.protected_globs, pack_id=pack_id, field="protected_globs"
    )

    managed_set = set(managed)
    scaffold_set = set(scaffold)
    protected_set = set(protected)
    managed_and_scaffold = sorted(managed_set & scaffold_set)
    if managed_and_scaffold:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: managed_globs and scaffold_globs overlap ({managed_and_scaffold[0]})"
        )
    managed_and_protected = sorted(managed_set & protected_set)
    if managed_and_protected:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: managed_globs and protected_globs overlap ({managed_and_protected[0]})"
        )
    scaffold_and_protected = sorted(scaffold_set & protected_set)
    if scaffold_and_protected:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: scaffold_globs and protected_globs overlap ({scaffold_and_protected[0]})"
        )

    for field_name, globs in (
        ("managed_globs", managed),
        ("scaffold_globs", scaffold),
    ):
        for glob in globs:
            anchor = _glob_anchor(glob)
            if not anchor:
                raise ValueError(
                    f"invalid pack.yaml for {pack_id}: {field_name} entry '{glob}' must include a non-wildcard path prefix"
                )
            if not any(_path_within_root(anchor, root) for root in roots):
                raise ValueError(
                    f"invalid pack.yaml for {pack_id}: {field_name} entry '{glob}' is outside install_roots"
                )

    return PackManifest(
        id=manifest.id,
        version=manifest.version,
        description=manifest.description,
        install_roots=roots,
        managed_globs=managed,
        scaffold_globs=scaffold,
        protected_globs=protected,
        upstream=manifest.upstream,
    )


def validate_pack_files(
    *, pack_id: str, manifest: PackManifest, pack_files: List[str]
) -> List[str]:
    normalized_files: List[str] = []
    seen: set[str] = set()
    for idx, path in enumerate(pack_files):
        rel = normalize_repo_relpath(path, pack_id=pack_id, field=f"files[{idx}]")
        if rel in seen:
            raise ValueError(
                f"invalid pack.yaml for {pack_id}: duplicate file path '{rel}' in files/"
            )
        seen.add(rel)
        normalized_files.append(rel)

        if not any(_path_within_root(rel, root) for root in manifest.install_roots):
            raise ValueError(
                f"invalid pack.yaml for {pack_id}: pack file '{rel}' is outside install_roots"
            )

    managed_matches = {
        rel
        for rel in normalized_files
        if any(fnmatch.fnmatch(rel, glob) for glob in manifest.managed_globs)
    }
    scaffold_matches = {
        rel
        for rel in normalized_files
        if any(fnmatch.fnmatch(rel, glob) for glob in manifest.scaffold_globs)
    }
    protected_matches = {
        rel
        for rel in normalized_files
        if any(fnmatch.fnmatch(rel, glob) for glob in manifest.protected_globs)
    }

    unmanaged_files = sorted(set(normalized_files) - managed_matches - scaffold_matches)
    if unmanaged_files:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: pack file '{unmanaged_files[0]}' is not matched by managed_globs or scaffold_globs"
        )

    managed_scaffold_overlap = sorted(managed_matches & scaffold_matches)
    if managed_scaffold_overlap:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: file '{managed_scaffold_overlap[0]}' matches both managed_globs and scaffold_globs"
        )

    protected_overlap = sorted((managed_matches | scaffold_matches) & protected_matches)
    if protected_overlap:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: file '{protected_overlap[0]}' matches protected_globs and cannot be managed or scaffolded"
        )

    for field_name, globs in (
        ("managed_globs", manifest.managed_globs),
        ("scaffold_globs", manifest.scaffold_globs),
    ):
        for glob in globs:
            if not any(fnmatch.fnmatch(rel, glob) for rel in normalized_files):
                raise ValueError(
                    f"invalid pack.yaml for {pack_id}: {field_name} entry '{glob}' does not match any pack files"
                )
    return normalized_files


def load_manifest(pack_id: str) -> PackManifest:
    pd = pack_dir(pack_id)
    mf = pd.joinpath("pack.yaml")
    if not mf.is_file():
        raise FileNotFoundError(f"unknown pack: {pack_id}")
    with resources.as_file(mf) as p:
        raw = Path(p).read_text(encoding="utf-8")
    doc = yaml.safe_load(raw)
    if not isinstance(doc, dict):
        raise ValueError(f"invalid pack.yaml for {pack_id}: expected mapping")

    def _require_str(k: str) -> str:
        v = doc.get(k)
        if not isinstance(v, str) or not v.strip():
            raise ValueError(
                f"invalid pack.yaml for {pack_id}: {k} must be a non-empty string"
            )
        return v.strip()

    def _require_list_str(k: str) -> List[str]:
        v = doc.get(k)
        if not isinstance(v, list) or not all(
            isinstance(x, str) and x.strip() for x in v
        ):
            raise ValueError(
                f"invalid pack.yaml for {pack_id}: {k} must be a list of strings"
            )
        return [str(x).strip() for x in v]

    def _optional_list_str(k: str) -> List[str]:
        v = doc.get(k)
        if v is None:
            return []
        if not isinstance(v, list) or not all(
            isinstance(x, str) and x.strip() for x in v
        ):
            raise ValueError(
                f"invalid pack.yaml for {pack_id}: {k} must be a list of strings"
            )
        return [str(x).strip() for x in v]

    upstream = doc.get("upstream")
    if upstream is not None and not isinstance(upstream, dict):
        raise ValueError(f"invalid pack.yaml for {pack_id}: upstream must be a mapping")
    if isinstance(upstream, dict):
        upstream = {str(k): str(v) for k, v in upstream.items()}

    mid = _require_str("id")
    if mid != pack_id:
        raise ValueError(
            f"invalid pack.yaml for {pack_id}: id must match directory name"
        )

    manifest = PackManifest(
        id=mid,
        version=_require_str("version"),
        description=_require_str("description"),
        install_roots=_require_list_str("install_roots"),
        managed_globs=_require_list_str("managed_globs"),
        scaffold_globs=_optional_list_str("scaffold_globs"),
        protected_globs=_require_list_str("protected_globs"),
        upstream=upstream,
    )
    return _validate_manifest_contract(manifest, pack_id=pack_id)


def iter_pack_files(pack_id: str) -> Iterable[Tuple[str, Path]]:
    """Yield (repo-relative path, concrete file path) for pack files."""
    manifest = load_manifest(pack_id)
    pd = pack_dir(pack_id)
    files_root = pd.joinpath("files")
    if not files_root.is_dir():
        return []

    def _walk(base, prefix: str) -> List[Tuple[str, Path]]:
        out: List[Tuple[str, Path]] = []
        for child in base.iterdir():
            name = str(getattr(child, "name", ""))
            if not name:
                continue
            next_prefix = f"{prefix}/{name}" if prefix else name
            if child.is_dir():
                out.extend(_walk(child, next_prefix))
            elif child.is_file():
                with resources.as_file(child) as p:
                    out.append((next_prefix, Path(p)))
        return out

    out = _walk(files_root, "")
    out.sort(key=lambda x: x[0])

    validated = validate_pack_files(
        pack_id=pack_id, manifest=manifest, pack_files=[rel for rel, _ in out]
    )
    by_rel = {rel: p for rel, p in out}
    return [(rel, by_rel[rel]) for rel in validated]
