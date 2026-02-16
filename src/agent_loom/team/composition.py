from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Mapping, Tuple

import yaml

from agent_loom.team.constants import DEFAULT_HARNESS, ROLE_ARCHITECT, ROLE_INTEGRATOR, ROLE_MANAGER, ROLE_WORKER
from agent_loom.team.errors import TeamError

SCHEMA_VERSION = 3

_BUILTIN_ROLES = (ROLE_MANAGER, ROLE_ARCHITECT, ROLE_WORKER, ROLE_INTEGRATOR)
_MEMBER_WORKSPACES = {"repo_root", "worktree"}
_HARNESS_VALUES = {"opencode", "claude", "omp", "codex"}

_ROLE_PATTERN = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")
_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")
_GROUP_PATTERN = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")


class TeamCompositionError(TeamError):
    def __init__(self, message: str, *, hint: str = "") -> None:
        super().__init__(message, code="ARG", exit_code=2, hint=hint)


@dataclass(frozen=True)
class CompositionMetadata:
    name: str
    purpose: str
    labels: Tuple[str, ...]

    def as_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        if self.name:
            out["name"] = self.name
        if self.purpose:
            out["purpose"] = self.purpose
        if self.labels:
            out["labels"] = list(self.labels)
        return out



@dataclass(frozen=True)
class BuiltinMember:
    role: str
    harness: str
    agent: str
    model: str

    def as_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "harness": self.harness,
            "agent": self.agent,
        }
        if self.model:
            out["model"] = self.model
        return out


@dataclass(frozen=True)
class TeamMember:
    id: str
    role: str
    harness: str
    agent: str
    model: str
    always_on: bool
    workspace: str
    description: str
    triggers: Tuple[str, ...]
    primary_workflows: Tuple[str, ...]

    def as_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "id": self.id,
            "role": self.role,
            "harness": self.harness,
            "agent": self.agent,
            "always_on": self.always_on,
            "workspace": self.workspace,
        }
        if self.model:
            out["model"] = self.model
        if self.description:
            out["description"] = self.description
        if self.triggers:
            out["triggers"] = list(self.triggers)
        if self.primary_workflows:
            out["primary_workflows"] = list(self.primary_workflows)
        return out



@dataclass(frozen=True)
class CommunicationRoute:
    from_role: str
    to: Tuple[str, ...]

    def as_dict(self) -> Dict[str, Any]:
        return {
            "from_role": self.from_role,
            "to": list(self.to),
        }


@dataclass(frozen=True)
class CommunicationPolicy:
    routes: Tuple[CommunicationRoute, ...]
    broadcast_groups: Tuple[Tuple[str, Tuple[str, ...]], ...]
    def as_dict(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}
        if self.routes:
            data["routes"] = [route.as_dict() for route in self.routes]
        if self.broadcast_groups:
            data["broadcast_groups"] = {
                name: list(members) for name, members in self.broadcast_groups
            }
        return data

@dataclass(frozen=True)
class TeamComposition:
    version: int
    metadata: CompositionMetadata
    mounts: Tuple[str, ...]
    builtins: Tuple[BuiltinMember, ...]
    members: Tuple[TeamMember, ...]
    communication: CommunicationPolicy | None
    def as_dict(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "version": self.version,
            "builtins": {builtin.role: builtin.as_dict() for builtin in self.builtins},
        }
        metadata = self.metadata.as_dict()
        if metadata:
            data["metadata"] = metadata
        if self.mounts:
            data["mounts"] = list(self.mounts)
        if self.members:
            data["members"] = [m.as_dict() for m in self.members]
        if self.communication is not None:
            comm = self.communication.as_dict()
            if comm:
                data["communication"] = comm
        return data

def parse_team_roster_yaml(text: str, *, source: str = "<string>") -> TeamComposition:
    try:
        raw_doc = yaml.safe_load(text)
    except yaml.YAMLError as e:
        raise TeamCompositionError(f"{source}: invalid YAML: {e}") from e

    if raw_doc is None:
        raise TeamCompositionError(f"{source}: expected a YAML mapping/object at top level")
    if not isinstance(raw_doc, dict):
        raise TeamCompositionError(f"{source}: expected a YAML mapping/object at top level")

    root = _expect_mapping(f"{source}", raw_doc)
    _require_keys(f"{source}", root, {"version", "builtins"})
    _reject_unknown_keys(
        f"{source}",
        root,
        {"version", "metadata", "mounts", "builtins", "members", "communication"},
    )

    version = _expect_int(f"{source}.version", root.get("version"), min_value=1)
    if version != SCHEMA_VERSION:
        raise TeamCompositionError(
            f"{source}.version: unsupported schema version {version}",
            hint=f"Use version: {SCHEMA_VERSION}",
        )

    metadata = _parse_metadata(root.get("metadata"), source=source)
    mounts = _parse_mounts(root.get("mounts"), source=source)
    members = _parse_members(root.get("members"), source=source)
    builtins = _parse_builtins(root.get("builtins"), source=source)
    communication = _parse_communication(root.get("communication"), source=source)
    return TeamComposition(
        version=version,
        metadata=metadata,
        mounts=mounts,
        builtins=tuple(sorted(builtins, key=lambda x: _BUILTIN_ROLES.index(x.role))),
        members=tuple(sorted(members, key=lambda x: x.id)),
        communication=communication,
    )


def load_team_roster_yaml(path: Path | str) -> TeamComposition:
    p = Path(path)
    try:
        text = p.read_text(encoding="utf-8")
    except OSError as e:
        raise TeamCompositionError(f"Unable to read roster file {p}: {e}") from e
    return parse_team_roster_yaml(text, source=str(p))


def _parse_mounts(raw: Any, *, source: str) -> Tuple[str, ...]:
    if raw is None:
        return ()

    items = _expect_list(f"{source}.mounts", raw)

    def _validate_rel(path: str, raw_value: str) -> str:
        s = str(raw_value or "").strip()
        if not s:
            raise TeamCompositionError(f"{path}: empty mount path")
        if s.startswith(("/", "\\")) or s.startswith("~"):
            raise TeamCompositionError(
                f"{path}: mount path must be repo-root-relative: {s}",
            )
        p = Path(s)
        if p.is_absolute():
            raise TeamCompositionError(
                f"{path}: mount path must be repo-root-relative: {s}",
            )
        if any(part == ".." for part in p.parts):
            raise TeamCompositionError(
                f"{path}: mount path must not contain '..': {s}",
            )
        norm = p.as_posix().strip()
        if norm in {"", "."}:
            raise TeamCompositionError(
                f"{path}: mount path must not be empty or '.': {s}",
            )
        if norm == ".git" or norm.startswith(".git/"):
            raise TeamCompositionError(
                f"{path}: refusing to mount .git: {norm}",
            )
        return norm

    specs: list[str] = []
    for idx, item in enumerate(items):
        mount_path = f"{source}.mounts[{idx}]"
        tok = _expect_nonempty_str(mount_path, item)
        if ":" in tok:
            src_raw, dst_raw = tok.split(":", 1)
            src = _validate_rel(f"{mount_path}.src", src_raw)
            dst = _validate_rel(f"{mount_path}.dst", dst_raw)
            specs.append(src if src == dst else f"{src}:{dst}")
        else:
            src = _validate_rel(f"{mount_path}.src", tok)
            specs.append(src)

    return tuple(sorted(set(specs)))





def _parse_metadata(raw: Any, *, source: str) -> CompositionMetadata:
    if raw is None:
        return CompositionMetadata(name="", purpose="", labels=())
    obj = _expect_mapping(f"{source}.metadata", raw)
    _reject_unknown_keys(f"{source}.metadata", obj, {"name", "purpose", "labels"})

    name = _expect_optional_str(f"{source}.metadata.name", obj.get("name"))
    purpose = _expect_optional_str(f"{source}.metadata.purpose", obj.get("purpose"))
    labels = _expect_str_list(f"{source}.metadata.labels", obj.get("labels"), default=())
    return CompositionMetadata(name=name, purpose=purpose, labels=tuple(sorted(set(labels))))



def _parse_builtins(raw: Any, *, source: str) -> Tuple[BuiltinMember, ...]:
    obj = _expect_mapping(f"{source}.builtins", raw)
    _require_keys(f"{source}.builtins", obj, set(_BUILTIN_ROLES))
    _reject_unknown_keys(f"{source}.builtins", obj, set(_BUILTIN_ROLES))

    builtins: list[BuiltinMember] = []
    for role in _BUILTIN_ROLES:
        path = f"{source}.builtins.{role}"
        spec = _expect_mapping(path, obj.get(role))
        _require_keys(path, spec, {"agent"})
        _reject_unknown_keys(path, spec, {"harness", "agent", "model"})

        harness = _expect_optional_enum(
            f"{path}.harness",
            spec.get("harness"),
            _HARNESS_VALUES,
            default=DEFAULT_HARNESS,
        )
        agent = _expect_nonempty_str(f"{path}.agent", spec.get("agent"))
        model = _expect_optional_str(f"{path}.model", spec.get("model"))
        builtins.append(BuiltinMember(role=role, harness=harness, agent=agent, model=model))

    return tuple(builtins)


def _parse_members(raw: Any, *, source: str) -> Tuple[TeamMember, ...]:
    if raw is None:
        return ()

    items = _expect_list(f"{source}.members", raw)
    members: list[TeamMember] = []
    seen_ids: set[str] = set()
    for idx, item in enumerate(items):
        path = f"{source}.members[{idx}]"
        obj = _expect_mapping(path, item)
        _require_keys(path, obj, {"id", "role", "agent", "always_on"})
        _reject_unknown_keys(
            path,
            obj,
            {
                "id",
                "role",
                "harness",
                "agent",
                "model",
                "always_on",
                "workspace",
                "description",
                "triggers",
                "primary_workflows",
            },
        )

        member_id = _expect_identifier(f"{path}.id", obj.get("id"))
        if member_id in seen_ids:
            raise TeamCompositionError(f"{path}.id: duplicate member id {member_id!r}")
        if member_id in _BUILTIN_ROLES:
            raise TeamCompositionError(
                f"{path}.id: member id {member_id!r} conflicts with a reserved built-in role",
                hint="Use custom member ids that do not overlap manager/architect/worker/integrator.",
            )
        seen_ids.add(member_id)

        role = _expect_role(f"{path}.role", obj.get("role"))
        if role in _BUILTIN_ROLES:
            raise TeamCompositionError(
                f"{path}.role: built-in role {role!r} must be configured under builtins",
                hint="Use members[] only for additional always-on personas with custom roles.",
            )

        harness = _expect_optional_enum(
            f"{path}.harness",
            obj.get("harness"),
            _HARNESS_VALUES,
            default=DEFAULT_HARNESS,
        )
        agent = _expect_nonempty_str(f"{path}.agent", obj.get("agent"))
        model = _expect_optional_str(f"{path}.model", obj.get("model"))
        always_on = _expect_bool(f"{path}.always_on", obj.get("always_on"))
        workspace = _expect_optional_enum(
            f"{path}.workspace",
            obj.get("workspace"),
            _MEMBER_WORKSPACES,
            default="repo_root",
        )
        description = _expect_optional_str(f"{path}.description", obj.get("description"))
        triggers = _expect_str_list(f"{path}.triggers", obj.get("triggers"), default=())
        primary_workflows = _expect_str_list(
            f"{path}.primary_workflows",
            obj.get("primary_workflows"),
            default=(),
        )

        members.append(
            TeamMember(
                id=member_id,
                role=role,
                harness=harness,
                agent=agent,
                model=model,
                always_on=always_on,
                workspace=workspace,
                description=description,
                triggers=tuple(sorted(set(triggers))),
                primary_workflows=tuple(sorted(set(primary_workflows))),
            )
        )

    return tuple(members)



def _parse_communication(raw: Any, *, source: str) -> CommunicationPolicy | None:
    if raw is None:
        return None
    obj = _expect_mapping(f"{source}.communication", raw)
    _reject_unknown_keys(
        f"{source}.communication",
        obj,
        {"routes", "broadcast_groups"},
    )
    routes: list[CommunicationRoute] = []
    routes_raw = obj.get("routes")
    if routes_raw is not None:
        route_items = _expect_list(f"{source}.communication.routes", routes_raw)
        for idx, route_item in enumerate(route_items):
            path = f"{source}.communication.routes[{idx}]"
            route_obj = _expect_mapping(path, route_item)
            _require_keys(path, route_obj, {"from_role", "to"})
            _reject_unknown_keys(path, route_obj, {"from_role", "to"})
            from_role = _expect_role(f"{path}.from_role", route_obj.get("from_role"))
            if from_role in _BUILTIN_ROLES:
                raise TeamCompositionError(
                    f"{path}.from_role: built-in route overrides are not allowed for {from_role!r}",
                    hint="Define routes only for custom roles; built-in manager/worker/architect/integrator routes are fixed.",
                )
            to_items = _expect_str_list(f"{path}.to", route_obj.get("to"), default=())
            if not to_items:
                raise TeamCompositionError(f"{path}.to: must include at least one target")
            normalized_to: list[str] = []
            for target_idx, raw_target in enumerate(to_items):
                normalized_to.append(
                    _normalize_target_token(
                        f"{path}.to[{target_idx}]",
                        raw_target,
                    )
                )
            routes.append(
                CommunicationRoute(from_role=from_role, to=tuple(sorted(set(normalized_to))))
            )
    group_items: list[Tuple[str, Tuple[str, ...]]] = []
    groups_raw = obj.get("broadcast_groups")
    if groups_raw is not None:
        groups_obj = _expect_mapping(f"{source}.communication.broadcast_groups", groups_raw)
        for raw_group_name in sorted(groups_obj.keys(), key=str):
            group_name = _expect_group_name(
                f"{source}.communication.broadcast_groups.<key>",
                raw_group_name,
            )
            members = _expect_str_list(
                f"{source}.communication.broadcast_groups.{group_name}",
                groups_obj.get(raw_group_name),
                default=(),
            )
            if not members:
                raise TeamCompositionError(
                    f"{source}.communication.broadcast_groups.{group_name}: must include at least one target"
                )
            normalized_members: list[str] = []
            for target_idx, raw_target in enumerate(members):
                normalized_members.append(
                    _normalize_target_token(
                        f"{source}.communication.broadcast_groups.{group_name}[{target_idx}]",
                        raw_target,
                    )
                )
            group_items.append((group_name, tuple(sorted(set(normalized_members)))))
    if not routes and not group_items:
        return None
    return CommunicationPolicy(
        routes=tuple(sorted(routes, key=lambda x: x.from_role)),
        broadcast_groups=tuple(sorted(group_items, key=lambda x: x[0])),
    )

def _normalize_target_token(path: str, raw: str) -> str:
    token = _expect_nonempty_str(path, raw).lower()
    if token in {
        "all",
        "escalate",
        "manager",
        "mgr",
        "worker",
        "workers",
        "integrator",
        "integrators",
        "architect",
        "architects",
    }:
        return token
    if token.startswith("member:"):
        member_id = token.split(":", 1)[1].strip()
        if not _IDENTIFIER_PATTERN.match(member_id):
            raise TeamCompositionError(f"{path}: invalid member token {token!r}")
        return f"member:{member_id}"
    if token.startswith("role:"):
        role = token.split(":", 1)[1].strip()
        if not _ROLE_PATTERN.match(role):
            raise TeamCompositionError(f"{path}: invalid role token {token!r}")
        return f"role:{role}"
    if token.startswith("group:"):
        group = token.split(":", 1)[1].strip()
        if not _GROUP_PATTERN.match(group):
            raise TeamCompositionError(f"{path}: invalid group token {token!r}")
        return f"group:{group}"
    return token


def _expect_mapping(path: str, raw: Any) -> Mapping[str, Any]:
    if not isinstance(raw, dict):
        raise TeamCompositionError(f"{path}: expected mapping/object")
    return raw


def _expect_list(path: str, raw: Any) -> list[Any]:
    if not isinstance(raw, list):
        raise TeamCompositionError(f"{path}: expected list")
    return raw


def _expect_nonempty_str(path: str, raw: Any) -> str:
    if not isinstance(raw, str) or not raw.strip():
        raise TeamCompositionError(f"{path}: expected non-empty string")
    return raw.strip()


def _expect_optional_str(path: str, raw: Any) -> str:
    if raw is None:
        return ""
    return _expect_nonempty_str(path, raw)


def _expect_bool(path: str, raw: Any) -> bool:
    if not isinstance(raw, bool):
        raise TeamCompositionError(f"{path}: expected boolean")
    return raw


def _expect_int(path: str, raw: Any, *, min_value: int | None = None) -> int:
    if isinstance(raw, bool) or not isinstance(raw, int):
        raise TeamCompositionError(f"{path}: expected integer")
    if min_value is not None and raw < min_value:
        raise TeamCompositionError(f"{path}: expected integer >= {min_value}")
    return raw


def _expect_enum(path: str, raw: Any, allowed: set[str]) -> str:
    value = _expect_nonempty_str(path, raw)
    if value not in allowed:
        opts = ", ".join(sorted(allowed))
        raise TeamCompositionError(f"{path}: invalid value {value!r}; expected one of: {opts}")
    return value


def _expect_optional_enum(path: str, raw: Any, allowed: set[str], *, default: str) -> str:
    if raw is None:
        return default
    return _expect_enum(path, raw, allowed)


def _expect_identifier(path: str, raw: Any) -> str:
    value = _expect_nonempty_str(path, raw)
    if not _IDENTIFIER_PATTERN.match(value):
        raise TeamCompositionError(
            f"{path}: invalid identifier {value!r}",
            hint="Use letters, numbers, '.', '_' or '-'; must start with a letter or number.",
        )
    return value


def _expect_optional_identifier(path: str, raw: Any) -> str:
    if raw is None:
        return ""
    return _expect_identifier(path, raw)


def _expect_role(path: str, raw: Any) -> str:
    value = _expect_nonempty_str(path, raw).lower()
    if not _ROLE_PATTERN.match(value):
        raise TeamCompositionError(
            f"{path}: invalid role {value!r}",
            hint="Use lowercase role names matching ^[a-z][a-z0-9_-]{0,63}$",
        )
    return value


def _expect_group_name(path: str, raw: Any) -> str:
    value = _expect_nonempty_str(path, raw).lower()
    if not _GROUP_PATTERN.match(value):
        raise TeamCompositionError(
            f"{path}: invalid group name {value!r}",
            hint="Use lowercase group names matching ^[a-z][a-z0-9_-]{0,63}$",
        )
    return value


def _expect_str_list(path: str, raw: Any, *, default: Tuple[str, ...]) -> list[str]:
    if raw is None:
        return list(default)
    items = _expect_list(path, raw)
    out: list[str] = []
    for idx, item in enumerate(items):
        out.append(_expect_nonempty_str(f"{path}[{idx}]", item))
    return out


def _require_keys(path: str, obj: Mapping[str, Any], required: set[str]) -> None:
    missing = sorted(k for k in required if k not in obj)
    if missing:
        raise TeamCompositionError(f"{path}: missing required key(s): {', '.join(missing)}")


def _reject_unknown_keys(path: str, obj: Mapping[str, Any], allowed: set[str]) -> None:
    unknown = sorted(str(k) for k in obj.keys() if str(k) not in allowed)
    if unknown:
        allowed_s = ", ".join(sorted(allowed))
        raise TeamCompositionError(
            f"{path}: unknown key(s): {', '.join(unknown)}",
            hint=f"Allowed keys: {allowed_s}",
        )


__all__ = [
    "BuiltinMember",
    "CommunicationPolicy",
    "CompositionMetadata",
    "SCHEMA_VERSION",
    "TeamComposition",
    "TeamCompositionError",
    "TeamMember",
    "CommunicationRoute",
    "load_team_roster_yaml",
    "parse_team_roster_yaml",
]
