"""Lines in 3D: foot, distance, projector and the relation of two lines (pure, no I/O)."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

__all__ = ["Vec", "Line", "Relation", "make_line", "foot", "dist", "projector", "midpoint",
           "unit", "any_perp", "line_line", "EPS_MEET", "EPS_PARALLEL"]

Vec = NDArray[np.float64]
EPS_MEET = 1e-7       # two lines "meet" when their distance is below this
EPS_PARALLEL = 1e-9   # |d1 x d2| below this means parallel (unit directions)


@dataclass(frozen=True)
class Line:
    a: Vec  # point on the line
    d: Vec  # unit direction


@dataclass(frozen=True)
class Relation:
    kind: str   # "coincident" | "parallel" | "meet" | "skew"
    p: Vec      # nearest point on the first line
    q: Vec      # nearest point on the second line
    dist: float


def unit(v: Vec) -> Vec:
    n = float(np.linalg.norm(v))
    return v / n if n > 1e-15 else np.zeros(3)


def make_line(a: Vec, d: Vec) -> Line:
    d = np.asarray(d, dtype=float)
    if np.linalg.norm(d) < 1e-15:
        raise ValueError("zero direction")
    return Line(np.asarray(a, dtype=float).copy(), unit(d))


def foot(line: Line, c: Vec) -> Vec:
    return line.a + line.d * float((c - line.a) @ line.d)


def dist(line: Line, c: Vec) -> float:
    return float(np.linalg.norm(c - foot(line, c)))


def projector(line: Line) -> NDArray[np.float64]:
    return np.eye(3) - np.outer(line.d, line.d)


def midpoint(p: Vec, q: Vec) -> Vec:
    return (p + q) / 2


def any_perp(v: Vec) -> Vec:
    t = np.array([1.0, 0.0, 0.0]) if abs(v[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    return unit(np.cross(v, t))


def line_line(A: Line, B: Line) -> Relation:
    n = np.cross(A.d, B.d)
    if np.linalg.norm(n) < EPS_PARALLEL:
        p = A.a
        q = foot(B, p)
        dd = float(np.linalg.norm(q - p))
        return Relation("coincident" if dd < EPS_MEET else "parallel", p, q, dd)
    w = B.a - A.a
    b = float(A.d @ B.d)
    d1w, d2w = float(A.d @ w), float(B.d @ w)
    den = 1 - b * b
    s = (d1w - b * d2w) / den
    t = (b * d1w - d2w) / den
    p, q = A.a + A.d * s, B.a + B.d * t
    dd = float(np.linalg.norm(p - q))
    return Relation("meet" if dd < EPS_MEET else "skew", p, q, dd)
