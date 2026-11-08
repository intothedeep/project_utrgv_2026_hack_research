"""Dispatcher: pick the active pair or fall to the three-active closed forms.

Mirrors solve() in study_tips.html, but the three-active step is a closed form per
case instead of Nelder-Mead. A case with no closed form returns None.
"""
from __future__ import annotations

import numpy as np

from . import active3
from .circle import Solution
from .classify import PAIRS, classify
from .geometry import Line, dist, line_line, make_line, midpoint

__all__ = ["solve_closed_form"]


def _pair_center(L: list[Line], i: int, j: int):
    rel = line_line(L[i], L[j])
    m = midpoint(rel.p, rel.q)
    is_line = rel.kind in ("parallel", "coincident")
    return rel, m, is_line


def _active_two(L: list[Line]) -> Solution | None:
    pairs = []
    for i, j, k in PAIRS:
        rel, m, is_line = _pair_center(L, i, j)
        pairs.append((i, j, k, rel.dist / 2, m, is_line))
    rmax = max(p[3] for p in pairs)
    for i, j, k, rho, m, is_line in pairs:
        if rho < rmax - 1e-9 * (1 + rmax):
            continue
        if is_line:
            c_line = make_line(m, L[i].d)
            rel = line_line(c_line, L[k])
            dk, c = rel.dist, rel.p
        else:
            c, dk = m, dist(L[k], m)
        if dk <= rho + 1e-9 * (1 + rho):
            active = () if rho < 1e-9 else (i, j)
            return Solution(c, rho, active, k, not is_line, "active2")
    return None


def _active_three(L: list[Line], key: str) -> Solution | None:
    if key == "triangle":
        return active3.incircle(L)
    if key == "par3_acute":
        return active3.circumcircle(L)
    if key.startswith("par_"):
        i, j, k = next((i, j, k) for i, j, k in PAIRS if line_line(L[i], L[j]).kind == "parallel")
        return active3.two_parallel(L, i, j, k)
    if key == "one_meet_perp":
        i, j, k = next((i, j, k) for i, j, k in PAIRS if line_line(L[i], L[j]).kind == "meet")
        return active3.one_meet_perp(L, i, j, k)
    if key == "skew_perp":
        for i, j, k in PAIRS:
            if line_line(L[i], L[j]).kind == "skew" and _is_normal_to(L[k], L[i], L[j]):
                return active3.skew_perp_axis(L, i, j, k)
    return None   # two_meet_one_cross, one_meet_over*, all_skew, ...: no closed form


def _is_normal_to(Lk: Line, La: Line, Lb: Line) -> bool:
    n = np.cross(La.d, Lb.d)
    n = n / np.linalg.norm(n)
    return abs(abs(float(Lk.d @ n)) - 1.0) < 1e-9


def solve_closed_form(L: list[Line]) -> Solution | None:
    sol = _active_two(L)
    if sol is not None:
        return sol
    return _active_three(L, classify(L))
