"""Build the circle (c, r, n) from a center, a radius and the active set."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .geometry import Line, Vec, any_perp, foot, unit

__all__ = ["Solution", "Circle", "build_circle"]


@dataclass(frozen=True)
class Solution:
    c: Vec
    r: float
    active: tuple[int, ...]   # () means r = 0, 2 or 3 line indices otherwise
    k: int | None             # third line for the 2-active case
    center_unique: bool
    branch: str


@dataclass(frozen=True)
class Circle:
    c: Vec
    r: float
    n: Vec


def _normal_three(c: Vec, q: list[Vec]) -> Vec:
    cands = [np.cross(q[0] - c, q[1] - c), np.cross(q[0] - c, q[2] - c),
             np.cross(q[1] - c, q[2] - c)]
    best = max(cands, key=lambda v: float(np.linalg.norm(v)))
    return unit(best) if np.linalg.norm(best) > 1e-12 else any_perp(q[0] - c)


def _normal_two(lines: list[Line], sol: Solution) -> Vec:
    c, r = sol.c, sol.r
    u = foot(lines[sol.active[0]], c) - c
    lk = lines[sol.k]
    w = lk.a - c
    wd = float(w @ lk.d)
    disc = max(0.0, wd * wd - float(w @ w) + r * r)
    s = lk.a + lk.d * (-wd + np.sqrt(disc))   # point of L_k on the sphere
    nn = np.cross(u, s - c)
    if np.linalg.norm(nn) < 1e-9 * r * r:
        nn = np.cross(u, any_perp(u))
    return unit(nn)


def build_circle(lines: list[Line], sol: Solution) -> Circle:
    if sol.r < 1e-9:
        return Circle(sol.c, 0.0, np.array([0.0, 0.0, 1.0]))
    if len(sol.active) == 3:
        q = [foot(ln, sol.c) for ln in lines]
        return Circle(sol.c, sol.r, _normal_three(sol.c, q))
    return Circle(sol.c, sol.r, _normal_two(lines, sol))
