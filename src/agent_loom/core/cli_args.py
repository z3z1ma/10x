from __future__ import annotations

from collections.abc import Collection, Mapping, Sequence


def rewrite_flag_aliases(
    argv: Sequence[str],
    aliases: Mapping[str, str],
) -> list[str]:
    out: list[str] = []
    alias_prefixes = tuple(f"{src}=" for src in aliases)
    for tok in argv:
        mapped = aliases.get(tok)
        if mapped is not None:
            out.append(mapped)
            continue
        if alias_prefixes and tok.startswith(alias_prefixes):
            for src, dst in aliases.items():
                prefix = f"{src}="
                if tok.startswith(prefix):
                    out.append(dst + tok[len(src) :])
                    break
            else:
                out.append(tok)
            continue
        out.append(tok)
    return out


def split_short_value_flags(
    argv: Sequence[str],
    value_flags: Collection[str],
) -> list[str]:
    out: list[str] = []
    for tok in argv:
        if len(tok) > 2 and tok.startswith("-") and not tok.startswith("--"):
            flag = tok[:2]
            if flag in value_flags:
                value = tok[2:]
                if value:
                    out.extend([flag, value])
                    continue
        out.append(tok)
    return out


__all__ = ["rewrite_flag_aliases", "split_short_value_flags"]
