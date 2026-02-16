from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Tuple

from agent_loom.team.constants import (
    DEFAULT_HARNESS,
    ROLE_ARCHITECT,
    ROLE_INTEGRATOR,
    ROLE_MANAGER,
    ROLE_WORKER,
)
from agent_loom.team.errors import TeamError


@dataclass(frozen=True)
class ResolvedMemberProfile:
    member_id: str
    role: str
    lifecycle: str
    source: str
    agent: str
    harness: str
    model: str
    workspace: str
    worktree_key: str
    description: str
    triggers: Tuple[str, ...]
    primary_workflows: Tuple[str, ...]


def resolve_builtin_profile(
    run: Mapping[str, Any],
    role: str,
) -> ResolvedMemberProfile | None:
    spec = _composition_spec(run)
    if spec is None:
        return None

    role_norm = str(role or "").strip().lower()
    if not role_norm:
        return None

    builtins = _builtins_by_role(spec)
    builtin = builtins.get(role_norm)
    if not isinstance(builtin, dict):
        return None

    return _profile_from_builtin(role=role_norm, builtin=builtin)


def resolve_member_profile(
    run: Mapping[str, Any],
    *,
    role: str,
    ticket_id: str = "",
    worktree_key: str = "",
    member_id: str = "",
) -> ResolvedMemberProfile | None:
    _ = ticket_id
    _ = worktree_key

    spec = _composition_spec(run)
    if spec is None:
        return None

    role_norm = str(role or "").strip().lower()
    requested_member_id = str(member_id or "").strip()

    builtins = _builtins_by_role(spec)
    members = _members_by_id(spec)

    selected_member_id = ""
    selected_role = ""

    if requested_member_id:
        if requested_member_id in builtins:
            selected_member_id = requested_member_id
            selected_role = requested_member_id
            profile = _profile_from_builtin(
                role=selected_role,
                builtin=builtins[selected_member_id],
            )
        else:
            member = members.get(requested_member_id)
            if not isinstance(member, dict):
                raise TeamError(
                    f"Roster member not found: {requested_member_id}",
                    code="ARG",
                    exit_code=2,
                )
            selected_member_id = requested_member_id
            selected_role = str(member.get("role") or "").strip().lower()
            profile = _profile_from_member(member_id=selected_member_id, member=member)

        if role_norm and selected_role != role_norm:
            raise TeamError(
                (
                    f"Roster member '{selected_member_id}' has role={selected_role}, "
                    f"but role={role_norm} was requested"
                ),
                code="ARG",
                exit_code=2,
            )
        return profile

    if not role_norm:
        return None

    if role_norm in builtins:
        return _profile_from_builtin(role=role_norm, builtin=builtins[role_norm])

    role_members = [
        (member_key, member)
        for member_key, member in members.items()
        if str(member.get("role") or "").strip().lower() == role_norm
    ]
    if not role_members:
        return None

    if len(role_members) > 1:
        raise TeamError(
            f"Multiple roster members exist for role={role_norm}; set member_id explicitly",
            code="ARG",
            exit_code=2,
            hint="Use member:<id> targeting to disambiguate custom role recipients.",
        )

    selected_member_id, selected_member = role_members[0]
    return _profile_from_member(member_id=selected_member_id, member=selected_member)


def list_always_on_member_profiles(
    run: Mapping[str, Any],
) -> Tuple[ResolvedMemberProfile, ...]:
    spec = _composition_spec(run)
    if spec is None:
        return ()

    builtins = _builtins_by_role(spec)
    out: list[ResolvedMemberProfile] = []

    for role in (ROLE_MANAGER, ROLE_ARCHITECT, ROLE_INTEGRATOR):
        builtin = builtins.get(role)
        if not isinstance(builtin, dict):
            continue
        profile = _profile_from_builtin(role=role, builtin=builtin)
        if profile.lifecycle == "always_on":
            out.append(profile)

    members = _members_by_id(spec)
    for member_id, member in sorted(members.items(), key=lambda x: x[0]):
        always_on = bool(member.get("always_on"))
        if not always_on:
            continue
        out.append(_profile_from_member(member_id=member_id, member=member))

    deduped: dict[str, ResolvedMemberProfile] = {}
    for profile in out:
        deduped[str(profile.member_id)] = profile
    return tuple(deduped.values())


def enforce_member_lifecycle(
    *, profile: ResolvedMemberProfile | None, role: str
) -> None:
    if profile is None:
        return

    role_norm = str(role or "").strip().lower()
    lifecycle = str(profile.lifecycle or "").strip().lower()

    if role_norm == ROLE_WORKER and lifecycle != "ephemeral":
        raise TeamError(
            (
                f"Role '{role_norm}' must use ephemeral roster members; "
                f"resolved member='{profile.member_id}' lifecycle='{profile.lifecycle}'"
            ),
            code="ARG",
            exit_code=2,
            hint="Worker role is ticket-scoped and always ephemeral.",
        )

    if (
        role_norm in (ROLE_MANAGER, ROLE_ARCHITECT, ROLE_INTEGRATOR)
        and lifecycle != "always_on"
    ):
        raise TeamError(
            (
                f"Role '{role_norm}' must use always_on roster members; "
                f"resolved member='{profile.member_id}' lifecycle='{profile.lifecycle}'"
            ),
            code="ARG",
            exit_code=2,
            hint="Manager/architect/integrator roles are always-on and fixed by builtins.",
        )


def _composition_spec(run: Mapping[str, Any]) -> Dict[str, Any] | None:
    roster = run.get("roster") if isinstance(run.get("roster"), dict) else None
    if roster is None:
        return None

    spec = roster.get("spec") if isinstance(roster.get("spec"), dict) else None
    if spec is None:
        return None
    return dict(spec)


def _builtins_by_role(spec: Mapping[str, Any]) -> Dict[str, Dict[str, Any]]:
    builtins_value = spec.get("builtins")
    raw = dict(builtins_value) if isinstance(builtins_value, dict) else {}

    out: Dict[str, Dict[str, Any]] = {}
    for role, data in raw.items():
        role_key = str(role or "").strip().lower()
        if not role_key or not isinstance(data, dict):
            continue
        out[role_key] = dict(data)
    return out


def _members_by_id(spec: Mapping[str, Any]) -> Dict[str, Dict[str, Any]]:
    members_value = spec.get("members")
    members_raw: list[Any] = (
        list(members_value) if isinstance(members_value, list) else []
    )
    members: Dict[str, Dict[str, Any]] = {}
    for item in members_raw:
        if not isinstance(item, dict):
            continue
        member_id = str(item.get("id") or "").strip()
        if not member_id:
            continue
        members[member_id] = dict(item)
    return members


def _derive_persona_worktree_key(member_id: str) -> str:
    raw = str(member_id or "").strip().lower()
    raw = raw.replace(".", "-")
    raw = re.sub(r"[^a-z0-9_-]+", "-", raw)
    raw = re.sub(r"[-_]{2,}", "-", raw).strip("-_ ")
    if not raw:
        raw = "persona"
    key = f"persona-{raw}"
    return key[:80]


def _profile_from_builtin(
    *,
    role: str,
    builtin: Mapping[str, Any],
) -> ResolvedMemberProfile:
    harness = str(builtin.get("harness") or "").strip().lower() or DEFAULT_HARNESS
    agent = str(builtin.get("agent") or "").strip()
    model = str(builtin.get("model") or "").strip()

    lifecycle = "ephemeral" if role == ROLE_WORKER else "always_on"
    workspace = "repo_root"
    worktree_key = ""
    if role == ROLE_WORKER:
        workspace = "worktree"
    elif role == ROLE_INTEGRATOR:
        workspace = "worktree"
        worktree_key = "merge-queue"

    source = "loom"
    return ResolvedMemberProfile(
        member_id=role,
        role=role,
        lifecycle=lifecycle,
        source=source,
        agent=agent,
        harness=harness,
        model=model,
        workspace=workspace,
        worktree_key=worktree_key,
        description="",
        triggers=(),
        primary_workflows=(),
    )


def _profile_from_member(
    *,
    member_id: str,
    member: Mapping[str, Any],
) -> ResolvedMemberProfile:
    always_on = bool(member.get("always_on"))
    lifecycle = "always_on" if always_on else "ephemeral"
    role = str(member.get("role") or "").strip().lower()
    agent = str(member.get("agent") or "").strip()
    harness = str(member.get("harness") or "").strip().lower() or DEFAULT_HARNESS
    model = str(member.get("model") or "").strip()
    workspace = str(member.get("workspace") or "").strip().lower() or "repo_root"
    worktree_key = ""
    if workspace == "worktree":
        worktree_key = _derive_persona_worktree_key(member_id)
    description = str(member.get("description") or "").strip()
    triggers = _string_tuple(member.get("triggers"))
    primary_workflows = _string_tuple(member.get("primary_workflows"))

    source = "loom"
    return ResolvedMemberProfile(
        member_id=member_id,
        role=role,
        lifecycle=lifecycle,
        source=source,
        agent=agent,
        harness=harness,
        model=model,
        workspace=workspace,
        worktree_key=worktree_key,
        description=description,
        triggers=triggers,
        primary_workflows=primary_workflows,
    )


def _string_tuple(raw: Any) -> Tuple[str, ...]:
    if not isinstance(raw, list):
        return ()
    values: list[str] = []
    for item in raw:
        text = str(item or "").strip()
        if text:
            values.append(text)
    return tuple(sorted(set(values)))


__all__ = [
    "ResolvedMemberProfile",
    "enforce_member_lifecycle",
    "list_always_on_member_profiles",
    "resolve_builtin_profile",
    "resolve_member_profile",
]
