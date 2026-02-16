from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def parallel_map(fn: Callable[[T], R], items: Sequence[T], jobs: int) -> list[R]:
    if jobs <= 1:
        return [fn(x) for x in items]
    with ThreadPoolExecutor(max_workers=jobs) as ex:
        futs = [ex.submit(fn, x) for x in items]
        return [f.result() for f in futs]
