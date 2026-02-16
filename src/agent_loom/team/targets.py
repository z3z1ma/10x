from __future__ import annotations

from typing import Any, Dict, List, Mapping, Tuple

from agent_loom.team.constants import (
    ROLE_INTEGRATOR,
    ROLE_INVESTIGATOR,
    ROLE_MANAGER,
    ROLE_WORKER,
)
from agent_loom.team.errors import TeamError
from agent_loom.team.tmux import (
    _pane_can_receive_chat,
    tmux_available,
    tmux_format,
    tmux_has_session,
    tmux_list_panes,
    tmux_send_text,
    tmux_window_exists,
)

_BUILTIN_GROUPS = {"all", "workers", "integrators", "investigators"}


def _resolve_target(run: Mapping[str, Any], target: str) -> Tuple[str, Dict[str, str]]:
    """Resolve a Team target to a tmux pane id."""

    t = str(target or "").strip()
    if not t:
        raise TeamError("Empty target", code="ARG", exit_code=2)

    if t in ("manager", "mgr"):
        mgr = run.get("manager") or {}
        pane_id = str(mgr.get("pane_id") or "")
        if not pane_id:
            raise TeamError("manager pane_id missing", code="BAD_STATE", exit_code=2)
        return pane_id, {"role": ROLE_MANAGER, "pane_id": pane_id}

    workers = dict(run.get("workers") or {})
    if t in workers:
        w = workers[t] or {}
        pane_id = str(w.get("pane_id") or "")
        if not pane_id:
            raise TeamError(
                f"worker pane_id missing: {t}", code="BAD_STATE", exit_code=2
            )
        return pane_id, {
            "role": str(w.get("role") or ROLE_WORKER),
            "worker_id": t,
            "ticket_id": str(w.get("ticket_id") or ""),
            "pane_id": pane_id,
        }

    # Worktree key match (e.g. merge-queue).
    wk_matches: List[Tuple[str, Dict[str, Any]]] = []
    for wid, w in workers.items():
        if bool((w or {}).get("retired")):
            continue
        wk = str((w or {}).get("worktree_key") or "").strip()
        if wk and wk == t:
            wk_matches.append((wid, w or {}))
    if len(wk_matches) == 1:
        wid, w = wk_matches[0]
        pane_id = str(w.get("pane_id") or "")
        if not pane_id:
            raise TeamError(
                f"worker pane_id missing: {wid}", code="BAD_STATE", exit_code=2
            )
        return pane_id, {
            "role": str(w.get("role") or ROLE_WORKER),
            "worker_id": wid,
            "ticket_id": str(w.get("ticket_id") or ""),
            "pane_id": pane_id,
        }
    if len(wk_matches) > 1:
        raise TeamError(
            f"Multiple workers match worktree_key: {t} -> {[m[0] for m in wk_matches]}",
            code="AMBIGUOUS",
            exit_code=2,
        )

    # Window name match.
    win_matches: List[Tuple[str, Dict[str, Any]]] = []
    for wid, w in workers.items():
        if bool((w or {}).get("retired")):
            continue
        win = str((w or {}).get("window") or "").strip()
        if win and win == t:
            win_matches.append((wid, w or {}))
    if len(win_matches) == 1:
        wid, w = win_matches[0]
        pane_id = str(w.get("pane_id") or "")
        if not pane_id:
            raise TeamError(
                f"worker pane_id missing: {wid}", code="BAD_STATE", exit_code=2
            )
        return pane_id, {
            "role": str(w.get("role") or ROLE_WORKER),
            "worker_id": wid,
            "ticket_id": str(w.get("ticket_id") or ""),
            "pane_id": pane_id,
        }
    if len(win_matches) > 1:
        raise TeamError(
            f"Multiple workers match window: {t} -> {[m[0] for m in win_matches]}",
            code="AMBIGUOUS",
            exit_code=2,
        )

    matches: List[Tuple[str, Dict[str, Any]]] = []
    for wid, w in workers.items():
        if str((w or {}).get("ticket_id") or "").strip() == t and not bool(
            (w or {}).get("retired")
        ):
            matches.append((wid, w or {}))
    if len(matches) == 1:
        wid, w = matches[0]
        pane_id = str(w.get("pane_id") or "")
        if not pane_id:
            raise TeamError(
                f"worker pane_id missing for ticket: {t}", code="BAD_STATE", exit_code=2
            )
        return pane_id, {
            "role": str(w.get("role") or ROLE_WORKER),
            "worker_id": wid,
            "ticket_id": str(w.get("ticket_id") or t),
            "pane_id": pane_id,
        }
    if len(matches) > 1:
        raise TeamError(
            f"Multiple workers match ticket id: {t} -> {[m[0] for m in matches]}",
            code="AMBIGUOUS",
            exit_code=2,
        )

    raise TeamError(f"Unknown target: {target}", code="ARG", exit_code=2)


def _iter_group_targets(run: Mapping[str, Any], group: str) -> List[str]:
    members: List[str] = []
    workers = dict(run.get("workers") or {})

    if group == "all":
        members.append("manager")
        for wid, w in sorted(workers.items()):
            if bool((w or {}).get("retired")):
                continue
            members.append(str(wid))
        return members

    for wid, w in sorted(workers.items()):
        role = str((w or {}).get("role") or "").strip().lower()
        if bool((w or {}).get("retired")):
            continue
        if group == "workers" and role == ROLE_WORKER:
            members.append(str(wid))
        elif group == "integrators" and role == ROLE_INTEGRATOR:
            members.append(str(wid))
        elif group == "investigators" and role == ROLE_INVESTIGATOR:
            members.append(str(wid))

    return members


def _composition_broadcast_groups(run: Mapping[str, Any]) -> Dict[str, Tuple[str, ...]]:
    composition = run.get("composition")
    if not isinstance(composition, dict):
        return {}
    spec = composition.get("spec")
    if not isinstance(spec, dict):
        return {}
    communication = spec.get("communication")
    if not isinstance(communication, dict):
        return {}
    groups = communication.get("broadcast_groups")
    if not isinstance(groups, dict):
        return {}

    out: Dict[str, Tuple[str, ...]] = {}
    for raw_name, raw_members in groups.items():
        name = str(raw_name or "").strip().lower()
        if not name:
            continue
        items: List[str] = []
        if isinstance(raw_members, list):
            for item in raw_members:
                value = str(item or "").strip().lower()
                if value:
                    items.append(value)
        if items:
            out[name] = tuple(items)
    return out


def _expand_group_targets(
    run: Mapping[str, Any],
    group: str,
    *,
    seen: set[str],
) -> List[str]:
    name = str(group or "").strip().lower()
    if not name:
        return []
    if name in seen:
        raise TeamError(
            f"Broadcast group recursion detected: {name}",
            code="ARG",
            exit_code=2,
        )

    if name in _BUILTIN_GROUPS:
        return _iter_group_targets(run, name)

    policy_groups = _composition_broadcast_groups(run)
    members = policy_groups.get(name)
    if members is None:
        return []

    seen.add(name)
    out: List[str] = []
    for item in members:
        if item in _BUILTIN_GROUPS or item in policy_groups:
            out.extend(_expand_group_targets(run, item, seen=seen))
        else:
            out.append(item)
    seen.remove(name)
    return out


def _resolve_targets(run: Mapping[str, Any], target: str) -> List[Dict[str, str]]:
    """Resolve single or grouped Team target(s) to concrete pane metadata."""

    t = str(target or "").strip()
    if not t:
        raise TeamError("Empty target", code="ARG", exit_code=2)

    tnorm = t.lower()
    if tnorm.startswith("group:"):
        group_name = tnorm.split(":", 1)[1].strip()
        groups = _composition_broadcast_groups(run)
        if not group_name:
            raise TeamError("Empty broadcast group name", code="ARG", exit_code=2)
        if group_name not in groups:
            available = sorted(groups.keys())
            raise TeamError(
                f"Unknown broadcast group: {group_name}",
                code="ARG",
                exit_code=2,
                hint=(
                    "Defined groups: " + ", ".join(available)
                    if available
                    else "No policy-defined broadcast groups are configured"
                ),
            )
        expanded = _expand_group_targets(run, group_name, seen=set())
    else:
        expanded = _expand_group_targets(run, tnorm, seen=set())

    if not expanded:
        pane_id, meta = _resolve_target(run, t)
        return [
            {
                "target": t,
                "pane_id": pane_id,
                "role": str(meta.get("role") or ""),
                "worker_id": str(meta.get("worker_id") or ""),
                "ticket_id": str(meta.get("ticket_id") or ""),
            }
        ]

    resolved: List[Dict[str, str]] = []
    seen_keys: set[str] = set()

    for item in expanded:
        pane_id, meta = _resolve_target(run, item)
        worker_id = str(meta.get("worker_id") or "").strip()
        role = str(meta.get("role") or "").strip().lower()
        key = f"worker:{worker_id}" if worker_id else f"role:{role}:{pane_id}"
        if key in seen_keys:
            continue
        seen_keys.add(key)
        resolved.append(
            {
                "target": item,
                "pane_id": pane_id,
                "role": role,
                "worker_id": worker_id,
                "ticket_id": str(meta.get("ticket_id") or ""),
            }
        )

    if not resolved:
        raise TeamError(
            f"Broadcast target resolved to zero recipients: {target}",
            code="ARG",
            exit_code=2,
        )

    return resolved


def _best_effort_tmux_nudge(
    *,
    run: Mapping[str, Any],
    session: str,
    target: str,
    line: str,
    force: bool = False,
) -> Tuple[bool, str, Dict[str, Any]]:
    meta: Dict[str, Any] = {"target": target}

    if not tmux_available():
        return False, "tmux_missing", meta
    if not session:
        return False, "session_missing", meta
    try:
        if not tmux_has_session(session):
            return False, "session_missing", meta
    except Exception as e:
        return False, "tmux_error", {**meta, "error": str(e)}

    try:
        pane_id, meta0 = _resolve_target(run, target)
        meta = dict(meta0 or meta)
    except TeamError as e:
        return (
            False,
            "unknown_target",
            {
                "target": target,
                "error": str(e),
                "code": str(getattr(e, "code", "")),
            },
        )
    except Exception as e:
        return False, "unknown_target", {"target": target, "error": str(e)}

    try:
        panes = tmux_list_panes(session)
        pane = panes.get(pane_id)
        if not pane:
            # Best-effort: refresh pane id from window name if available.
            wid = str(meta.get("worker_id") or "").strip()
            win = (
                str(
                    ((run.get("workers") or {}).get(wid) or {}).get("window") or ""
                ).strip()
                if wid
                else ""
            )
            if win and tmux_window_exists(session, win):
                try:
                    refreshed = tmux_format(f"{session}:{win}", "#{pane_id}")
                except Exception:
                    refreshed = ""
                if refreshed:
                    pane_id = refreshed
                    meta["pane_id"] = refreshed
                    panes = tmux_list_panes(session)
                    pane = panes.get(pane_id)
            if not pane:
                return False, "pane_missing", meta
        if not _pane_can_receive_chat(pane) and not force:
            return False, "unsafe_pane", meta
        tmux_send_text(pane_id, line, enter=True, ctrl_enter=(str(run.get("harness") or "").strip().lower() == "omp"))
        return True, "", meta
    except TeamError as e:
        if e.code == "MISSING_BIN":
            return False, "tmux_missing", meta
        return False, "tmux_error", {**meta, "error": str(e)}
    except Exception as e:
        return False, "tmux_error", {**meta, "error": str(e)}


__all__ = ["_best_effort_tmux_nudge", "_resolve_target", "_resolve_targets"]
