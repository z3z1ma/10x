from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from typing import Any, Dict, List, Optional

from agent_loom.compound.episodes import canonical_json_bytes, pretty_json


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def compute_decision_id(version: int, payload: Dict[str, Any]) -> str:
    return sha256(
        canonical_json_bytes({"version": int(version), **payload})
    ).hexdigest()


@dataclass(frozen=True)
class Decision:
    version: int
    decision_id: str
    created_at: str
    episode_id: str
    proposal_blob_sha256: str
    ops: List[Dict[str, Any]]

    def identity_payload(self) -> Dict[str, Any]:
        return {
            "created_at": str(self.created_at),
            "episode_id": str(self.episode_id),
            "proposal_blob_sha256": str(self.proposal_blob_sha256 or ""),
            "ops": list(self.ops or []),
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": int(self.version),
            "decision_id": str(self.decision_id),
            "created_at": str(self.created_at),
            "episode_id": str(self.episode_id),
            **(
                {"proposal_blob_sha256": str(self.proposal_blob_sha256)}
                if str(self.proposal_blob_sha256 or "").strip()
                else {}
            ),
            "ops": list(self.ops or []),
        }


def decision_path_for_id(
    *, decisions_dir: Path, created_at: str, decision_id: str
) -> Path:
    try:
        dt = datetime.fromisoformat(str(created_at).replace("Z", "+00:00"))
    except Exception:
        dt = datetime.now(timezone.utc)
    return decisions_dir / f"{dt.year:04d}" / f"{dt.month:02d}" / f"{decision_id}.json"


def write_decision(path: Path, decision: Decision, *, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(pretty_json(decision.to_dict()), encoding="utf-8")


def build_decision(
    *,
    created_at: Optional[str],
    episode_id: str,
    proposal_blob_sha256: str,
    ops: List[Dict[str, Any]],
) -> Decision:
    ts = str(created_at or "").strip() or _now_iso()
    tmp = Decision(
        version=1,
        decision_id="",
        created_at=ts,
        episode_id=str(episode_id or ""),
        proposal_blob_sha256=str(proposal_blob_sha256 or ""),
        ops=list(ops or []),
    )
    decision_id = compute_decision_id(tmp.version, tmp.identity_payload())
    return Decision(
        version=tmp.version,
        decision_id=decision_id,
        created_at=tmp.created_at,
        episode_id=tmp.episode_id,
        proposal_blob_sha256=tmp.proposal_blob_sha256,
        ops=tmp.ops,
    )


__all__ = [
    "Decision",
    "build_decision",
    "decision_path_for_id",
    "write_decision",
]
