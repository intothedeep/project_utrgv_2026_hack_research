"""Figure 1 case key of three lines (port of classify() in study_tips.html).

Deviation: the perpendicular test is exact (1e-9), not the page's 0.999, so a
"perp" key means L3 really is normal to the plane of the other two.
"""
from __future__ import annotations

import numpy as np

from .geometry import Line, foot, line_line, unit

__all__ = ["classify", "PAIRS"]

PAIRS = ((0, 1, 2), (0, 2, 1), (1, 2, 0))  # (i, j, k): pair (i, j), third line k
_PERP = 1e-9


def _is_normal(d: np.ndarray, n: np.ndarray) -> bool:
    return abs(abs(float(d @ n)) - 1.0) < _PERP


def _par3_key(L: list[Line]) -> str:
    d = L[0].d
    pts = [ln.a - d * float(ln.a @ d) for ln in L]
    if np.linalg.norm(np.cross(pts[1] - pts[0], pts[2] - pts[0])) < 1e-7:
        return "par3_coplanar"
    e = sorted([float(np.linalg.norm(pts[1] - pts[2])), float(np.linalg.norm(pts[0] - pts[2])),
                float(np.linalg.norm(pts[0] - pts[1]))])
    k = e[0] ** 2 + e[1] ** 2 - e[2] ** 2
    return "par3_right" if abs(k) < 1e-9 else ("par3_acute" if k > 0 else "par3_obtuse")


def _par_pair_key(L: list[Line], i: int, j: int, k: int, n_meet: int) -> str:
    if n_meet == 2:
        return "par_meet_both"
    if n_meet == 1:
        return "par_meet_one"
    n = unit(np.cross(L[i].d, foot(L[j], L[i].a) - L[i].a))
    dn = float(L[k].d @ n)
    if abs(dn) < 1e-9:
        return "par_over"
    t = float((n @ (L[i].a - L[k].a)) / dn)
    s = L[k].a + L[k].d * t
    m = np.cross(n, L[i].d)
    si, sj = float((s - L[i].a) @ m), float((s - L[j].a) @ m)
    between = si * sj < 0
    if _is_normal(L[k].d, n):
        return "par_perp_between" if between else "par_perp_outside"
    return "par_overunder" if between else "par_over"


def _one_meet_key(L: list[Line], i: int, j: int, k: int, p: np.ndarray) -> str:
    n = unit(np.cross(L[i].d, L[j].d))
    if _is_normal(L[k].d, n):
        return "one_meet_perp"
    hs = []
    for line in (L[i], L[j]):
        m = np.cross(n, line.d)
        dm = float(L[k].d @ m)
        if abs(dm) < 1e-9:
            return "one_meet_over"
        t = float((p - L[k].a) @ m) / dm
        hs.append(float((L[k].a + L[k].d * t - p) @ n))
    return "one_meet_over" if hs[0] * hs[1] > 0 else "one_meet_overunder"


def classify(L: list[Line]) -> str:
    rels = [(i, j, k, line_line(L[i], L[j])) for i, j, k in PAIRS]
    if any(r.kind == "coincident" for *_, r in rels):
        return "coincident"
    par = [(i, j, k) for i, j, k, r in rels if r.kind == "parallel"]
    meet = [(i, j, k, r) for i, j, k, r in rels if r.kind == "meet"]
    if len(par) == 3:
        return _par3_key(L)
    if len(par) == 1:
        return _par_pair_key(L, *par[0], len(meet))
    if len(meet) == 3:
        same = np.linalg.norm(rels[0][3].p - rels[1][3].p) < 1e-6
        return "concurrent" if same else "triangle"
    if len(meet) == 2:
        return "two_meet_one_cross"
    if len(meet) == 1:
        i, j, k, r = meet[0]
        return _one_meet_key(L, i, j, k, r.p)
    for idx in range(3):
        o = [L[t] for t in range(3) if t != idx]
        n = unit(np.cross(o[0].d, o[1].d))
        if _is_normal(L[idx].d, n) and line_line(o[0], o[1]).kind == "skew":
            return "skew_perp"
    return "all_skew"
