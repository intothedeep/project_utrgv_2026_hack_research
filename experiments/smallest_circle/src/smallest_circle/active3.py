"""Closed forms when all three lines are active. Each returns a Solution or None."""
from __future__ import annotations

import numpy as np

from .circle import Solution
from .geometry import Line, Vec, dist, foot, line_line, midpoint, projector, unit

__all__ = ["incircle", "circumcircle", "two_parallel", "one_meet_perp", "skew_perp_axis"]

_ALL = (0, 1, 2)


def incircle(L: list[Line]) -> Solution | None:
    A, B, C = _vertex(L[1], L[2]), _vertex(L[0], L[2]), _vertex(L[0], L[1])
    la, lb, lc = (float(np.linalg.norm(B - C)), float(np.linalg.norm(A - C)),
                  float(np.linalg.norm(A - B)))
    s = la + lb + lc
    area = 0.5 * float(np.linalg.norm(np.cross(B - A, C - A)))
    return Solution((la * A + lb * B + lc * C) / s, 2 * area / s, _ALL, None, True, "incircle")


def _vertex(A: Line, B: Line) -> Vec:
    rel = line_line(A, B)
    return midpoint(rel.p, rel.q)


def circumcircle(L: list[Line]) -> Solution | None:
    d = L[0].d
    A, B, C = (ln.a - d * float(ln.a @ d) for ln in L)
    a, b = A - C, B - C
    axb = np.cross(a, b)
    den = 2 * float(axb @ axb)
    if den < 1e-18:
        return None
    c = C + np.cross(float(a @ a) * b - float(b @ b) * a, axb) / den
    return Solution(c, float(np.linalg.norm(A - c)), _ALL, None, False, "circumcircle")


def _smallest_abs_root(A: float, B: float, C: float) -> float | None:
    """Root of A z^2 + B z + C = 0 with the smallest |z|."""
    if abs(A) < 1e-12:
        return None if abs(B) < 1e-14 else -C / B
    disc = B * B - 4 * A * C
    if disc < 0:
        return None
    roots = [(-B + s * np.sqrt(disc)) / (2 * A) for s in (1.0, -1.0)]
    return min(roots, key=abs)


def two_parallel(L: list[Line], i: int, j: int, k: int) -> Solution | None:
    """L_i parallel to L_j. Center c = M0 + y d + z ez (x = 0), r^2 = h^2 + z^2.

    Minimising |P3 (c - a3)|^2 over y leaves q(z) = A z^2 + B z + C; solve q(z) = h^2.
    """
    d = L[i].d
    w = foot(L[j], L[i].a) - L[i].a
    h = float(np.linalg.norm(w)) / 2
    ex = w / (2 * h)
    ez = np.cross(d, ex)
    M0 = L[i].a + w / 2
    P3 = projector(L[k])
    p, s, t = P3 @ (M0 - L[k].a), P3 @ d, P3 @ ez
    ss = float(s @ s)
    if ss < 1e-12:
        return None
    pp, tt = p - s * float(s @ p) / ss, t - s * float(s @ t) / ss
    z = _smallest_abs_root(float(tt @ tt) - 1.0, 2 * float(pp @ tt), float(pp @ pp) - h * h)
    if z is None:
        return None
    y = -float(s @ (p + z * t)) / ss
    return Solution(M0 + y * d + z * ez, float(np.sqrt(h * h + z * z)), _ALL, None, True,
                    "par2_quadratic")


def one_meet_perp(L: list[Line], i: int, j: int, k: int) -> Solution | None:
    """L_i, L_j meet at P, L_k is normal to their plane at S. c = P + t b, r = |t| sin(a)."""
    rel = line_line(L[i], L[j])
    P = midpoint(rel.p, rel.q)
    n = unit(np.cross(L[i].d, L[j].d))
    v = (L[k].a - n * float((L[k].a - P) @ n)) - P
    best: Solution | None = None
    for b in (unit(L[i].d + L[j].d), unit(L[i].d - L[j].d)):
        cos2 = float(L[i].d @ b) ** 2
        sin_a = float(np.linalg.norm(np.cross(L[i].d, b)))
        bv = float(b @ v)
        disc = bv * bv - cos2 * float(v @ v)
        if disc < 0 or cos2 < 1e-12:
            continue
        for sg in (1.0, -1.0):
            t = (bv + sg * np.sqrt(disc)) / cos2   # t^2 cos2 - 2 t bv + |v|^2 = 0
            r = abs(t) * sin_a
            if best is None or r < best.r:
                best = Solution(P + t * b, r, _ALL, None, True, "pll_bisector")
    return best


def skew_perp_axis(L: list[Line], i: int, j: int, k: int) -> Solution | None:
    """Skew L_i, L_j and L_k along their common normal. Closed form only if S is on a
    half-turn axis that swaps L_i and L_j; else None (not solved)."""
    rel = line_line(L[i], L[j])
    m = midpoint(rel.p, rel.q)
    n = unit(np.cross(L[i].d, L[j].d))
    S = L[k].a - n * float((L[k].a - m) @ n)
    best: Solution | None = None
    for u in (unit(L[i].d + L[j].d), unit(L[i].d - L[j].d)):
        off = S - m - u * float((S - m) @ u)
        if np.linalg.norm(off) > 1e-8 * (1 + np.linalg.norm(S - m)):
            continue
        q = [_quad(L[x], m, u) for x in (i, k)]   # |P (m + s u - a)|^2 = a s^2 + b s + c
        coef = [q[0][e] - q[1][e] for e in range(3)]
        for s in _quad_roots(*coef):
            c = m + s * u
            r = dist(L[i], c)
            if best is None or r < best.r:
                best = Solution(c, r, _ALL, None, True, "skew_perp_rot_axis")
    return best


def _quad(line: Line, m: Vec, u: Vec) -> tuple[float, float, float]:
    P = projector(line)
    w0, pu = P @ (m - line.a), P @ u
    return float(pu @ pu), 2 * float(w0 @ pu), float(w0 @ w0)


def _quad_roots(a: float, b: float, c: float) -> list[float]:
    if abs(a) < 1e-12:
        return [] if abs(b) < 1e-14 else [-c / b]
    disc = b * b - 4 * a * c
    if disc < 0:
        return []
    return [(-b + s * float(np.sqrt(disc))) / (2 * a) for s in (1.0, -1.0)]
