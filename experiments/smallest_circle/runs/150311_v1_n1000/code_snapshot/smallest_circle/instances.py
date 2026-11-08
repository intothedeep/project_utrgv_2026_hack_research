"""Random instances per case. Each generator draws a candidate; generate() keeps only
candidates that classify() puts in the wanted case (rejection sampling, fixed seed)."""
from __future__ import annotations

from typing import Callable

import numpy as np

from .classify import classify
from .geometry import Line, Vec, make_line, unit

__all__ = ["CASES", "generate"]

Gen = Callable[[np.random.Generator], list[Line]]
_MAX_TRIES_PER_INSTANCE = 500


def _pt(g: np.random.Generator) -> Vec:
    return g.uniform(-2, 2, 3)


def _dir(g: np.random.Generator) -> Vec:
    return unit(g.normal(size=3))


def _line(g: np.random.Generator) -> Line:
    return make_line(_pt(g), _dir(g))


def _on(g: np.random.Generator, ln: Line) -> Vec:
    return ln.a + ln.d * g.uniform(-2, 2)


def _par_pair(g: np.random.Generator) -> tuple[Line, Line, Vec, Vec]:
    """Parallel L1, L2 at distance 2h; returns also unit ex (L1 -> L2) and normal n."""
    d = _dir(g)
    ex = unit(np.cross(d, _dir(g)))
    h = g.uniform(0.3, 1.5)
    mid = _pt(g)
    return (make_line(mid - h * ex, d), make_line(mid + h * ex, d), ex, np.cross(d, ex))


def _triangle(g):
    o, e1 = _pt(g), _dir(g)
    e2 = unit(np.cross(e1, _dir(g)))
    return [make_line(o + g.uniform(-2, 2) * e1 + g.uniform(-2, 2) * e2,
                      g.normal() * e1 + g.normal() * e2) for _ in range(3)]


def _concurrent(g):
    p = _pt(g)
    return [make_line(p, _dir(g)) for _ in range(3)]


def _two_meet(g):
    l2, l3 = _line(g), _line(g)
    p, q = _on(g, l2), _on(g, l3)
    return [make_line(p, q - p), l2, l3]


def _one_meet(g):
    p = _pt(g)
    return [make_line(p, _dir(g)), make_line(p, _dir(g)), _line(g)]


def _three_random(g):
    return [_line(g) for _ in range(3)]


def _par_meet_both(g):
    l1, l2, _, _ = _par_pair(g)
    p, q = _on(g, l1), _on(g, l2)
    return [l1, l2, make_line(p, q - p)]


def _par_meet_one(g):
    l1, l2, _, _ = _par_pair(g)
    return [l1, l2, make_line(_on(g, l1), _dir(g))]


def _par_general(g):
    l1, l2, _, _ = _par_pair(g)
    return [l1, l2, _line(g)]


def _par3_coplanar(g):
    d = _dir(g)
    f = unit(np.cross(d, _dir(g)))
    base = _pt(g)
    return [make_line(base + g.uniform(-2, 2) * f, d) for _ in range(3)]


def _par3(g):
    d = _dir(g)
    e1 = unit(np.cross(d, _dir(g)))
    e2 = np.cross(d, e1)
    return [make_line(g.uniform(-2, 2) * e1 + g.uniform(-2, 2) * e2, d) for _ in range(3)]


def _in_plane_dirs(g) -> tuple[Vec, Vec, Vec]:
    d1, d2 = _dir(g), _dir(g)
    return d1, d2, unit(np.cross(d1, d2))


def _perp_one_meet(g):
    d1, d2, n = _in_plane_dirs(g)
    p = _pt(g)
    v = g.uniform(-2, 2) * d1 + g.uniform(-2, 2) * d2
    return [make_line(p, d1), make_line(p, d2), make_line(p + v, n)]


def _skew_pair(g) -> tuple[Line, Line, Vec, Vec]:
    """Skew L1, L2 with midpoint m of the common perpendicular and its direction n."""
    d1, d2, n = _in_plane_dirs(g)
    m = _pt(g)
    gap = g.uniform(0.2, 1.0)
    return make_line(m + gap * n, d1), make_line(m - gap * n, d2), m, n


def _perp_cross_axis(g):
    l1, l2, m, n = _skew_pair(g)
    u = unit(l1.d + l2.d) if g.random() < 0.5 else unit(l1.d - l2.d)
    return [l1, l2, make_line(m + g.uniform(-2, 2) * u, n)]


def _perp_cross_off(g):
    l1, l2, m, n = _skew_pair(g)
    s = g.uniform(-2, 2) * l1.d + g.uniform(-2, 2) * l2.d
    return [l1, l2, make_line(m + s, n)]


def _par_perp(g):
    l1, l2, ex, n = _par_pair(g)
    h = float(np.linalg.norm(l2.a - l1.a)) / 2
    mid = (l1.a + l2.a) / 2
    return [l1, l2, make_line(mid + g.uniform(-3 * h, 3 * h) * ex + g.uniform(-2, 2) * l1.d, n)]


def _coincident(g):
    l1 = _line(g)
    return [l1, make_line(l1.a + g.uniform(-2, 2) * l1.d, l1.d), _line(g)]


# case key -> generators drawn in turn (skew_perp mixes on-axis and off-axis instances)
CASES: dict[str, list[Gen]] = {
    "triangle": [_triangle], "concurrent": [_concurrent], "two_meet_one_cross": [_two_meet],
    "one_meet_over": [_one_meet], "one_meet_overunder": [_one_meet], "all_skew": [_three_random],
    "par_meet_both": [_par_meet_both], "par_meet_one": [_par_meet_one],
    "par_over": [_par_general], "par_overunder": [_par_general],
    "par3_coplanar": [_par3_coplanar], "par3_acute": [_par3], "par3_obtuse": [_par3],
    "one_meet_perp": [_perp_one_meet], "skew_perp": [_perp_cross_axis, _perp_cross_off],
    "par_perp_between": [_par_perp], "par_perp_outside": [_par_perp], "coincident": [_coincident],
}


def generate(case: str, n: int, g: np.random.Generator) -> list[list[Line]]:
    """Up to n instances of `case`; fewer if rejection sampling runs out (reported)."""
    gens, out, tries = CASES[case], [], 0
    while len(out) < n and tries < n * _MAX_TRIES_PER_INSTANCE:
        lines = gens[len(out) % len(gens)](g)
        tries += 1
        if classify(lines) == case:
            out.append(lines)
    return out
