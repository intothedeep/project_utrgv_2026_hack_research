"""Fixed test instances: the preset line sets of study_tips.html (PRESETS, ~line 1000).

Names are the page's presets in ASCII. Directions are normalised by make_line.
"""
from __future__ import annotations

import numpy as np

from .geometry import Line, make_line

__all__ = ["PRESETS", "R_KNOWN"]

_C60, _S60 = np.cos(np.pi / 3), np.sin(np.pi / 3)


def _L(a, d) -> Line:
    return make_line(np.array(a, dtype=float), np.array(d, dtype=float))


def _hyper(R: float) -> list[Line]:
    ts = [k * 2 * np.pi / 3 for k in range(3)]
    return [_L([R * np.cos(t), R * np.sin(t), 0], [-np.sin(t), np.cos(t), 1]) for t in ts]


def _par(h: float) -> list[Line]:
    return [_L([-h, 0, 0], [0, 1, 0]), _L([h, 0, 0], [0, 1, 0])]


PRESETS: dict[str, list[Line]] = {
    "triangle": [_L([-2, -1.2, 0], [4.2, 0, 0]), _L([2.2, -1.2, 0], [-1.8, 3.2, 0]),
                 _L([0.4, 2, 0], [-2.4, -3.2, 0])],
    "concurrent": [_L([0, 0, 0], [1, 0, .2]), _L([0, 0, 0], [.3, 1, -.1]),
                   _L([0, 0, 0], [-.5, .4, 1])],
    "two_meet_near": [_L([1, 0, 1], [-1, 1, -2]), _L([0, 0, 1], [1, 0, 0]),
                      _L([0, 0, -1], [0, 1, 0])],
    "two_meet_far": [_L([4, 0, 1], [-4, 4, -2]), _L([0, 0, 1], [1, 0, 0]),
                     _L([0, 0, -1], [0, 1, 0])],
    "one_meet_over": [_L([0, 0, 0], [1, 0, 0]), _L([0, 0, 0], [_C60, _S60, 0]),
                      _L([0, -1.5, 1], [.3, 1, 0])],
    "one_meet_overunder": [_L([0, 0, 0], [1, 0, 0]), _L([0, 0, 0], [_C60, _S60, 0]),
                           _L([1, .3, 0], [-.5, 1, .6])],
    "zero_meet_over": [_L([0, 0, 1], [1, 0, 0]), _L([0, 0, -1], [_C60, _S60, 0]),
                       _L([.5, -1, 2], [-.6, 1, 0])],
    "hyperboloid_1.5": _hyper(1.5),
    "par_meet_both": [*_par(1.2), _L([-1.2, -1, 0], [2.4, 2, 0])],
    "par_meet_one": [*_par(1.2), _L([-1.2, 0, 0], [1, .4, .9])],
    "par_over": [*_par(1.2), _L([0, 0, 1], [1, .5, 0])],
    "par_overunder": [*_par(1.2), _L([.3, 0, 0], [1, .4, .7])],
    "par_far_skew": [*_par(1), _L([0, 0, 2.6], [1, .8, .35])],
    "par3_coplanar": [_L([-1.6, 0, 0], [0, 1, 0]), _L([.4, 0, 0], [0, 1, 0]),
                      _L([1.6, 0, 0], [0, 1, 0])],
    "par3_acute": [_L([-1.4, 0, -.9], [0, 1, 0]), _L([1.5, 0, -.7], [0, 1, 0]),
                   _L([.1, 0, 1.4], [0, 1, 0])],
    "par3_obtuse": [_L([-1.8, 0, 0], [0, 1, 0]), _L([1.8, 0, 0], [0, 1, 0]),
                    _L([.2, 0, .6], [0, 1, 0])],
    "perp_one_meet": [_L([0, 0, 0], [1, .55, 0]), _L([0, 0, 0], [-1, .55, 0]),
                      _L([0, 1.4, 0], [0, 0, 1])],
    "perp_one_cross": [_L([0, 0, .35], [1, .55, 0]), _L([0, 0, -.35], [-1, .55, 0]),
                       _L([0, 1.4, 0], [0, 0, 1])],
    "par_perp_between": [*_par(1.2), _L([.4, 0, 0], [0, 0, 1])],
    "par_perp_outside": [*_par(1.2), _L([2.4, 0, 0], [0, 0, 1])],
}

# Known exact radius (study_tips / 02_possible_solutions F: hyperboloid, R = 1.5 gives r* = 1.5).
R_KNOWN: dict[str, float] = {"hyperboloid_1.5": 1.5}
