"""Does the circle meet each line? Exact test (line-plane intersection), not sampling.

Why not 128 sample points (design V2): sampling resolves ~r*(1-cos(pi/128)) ~ 3e-4 r,
too coarse for the 1e-6 criterion.
"""
from __future__ import annotations

import numpy as np

from .circle import Circle
from .geometry import Line, dist

__all__ = ["touch_residual"]


def touch_residual(line: Line, circ: Circle) -> float:
    """Distance from the line to the circle curve (0 means they share a point)."""
    if circ.r == 0:
        return dist(line, circ.c)
    dn = float(line.d @ circ.n)
    if abs(dn) > 1e-9:
        t = float(circ.n @ (circ.c - line.a)) / dn
        x = line.a + line.d * t
        return abs(float(np.linalg.norm(x - circ.c)) - circ.r)
    off = abs(float(circ.n @ (line.a - circ.c)))
    if off > 1e-9:
        return off
    return max(0.0, dist(line, circ.c) - circ.r)
