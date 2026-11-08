"""Numeric optimum: min r s.t. ||P_i (c - a_i)|| <= r (SOCP, cvxpy + Clarabel).

Run on the cluster only. The problem is built once with Parameters (DPP) and re-solved
per instance, so 20k instances do not recompile 20k times.
"""
from __future__ import annotations

from dataclasses import dataclass

import cvxpy as cp
import numpy as np

from .geometry import Line, Vec, projector

__all__ = ["SocpSolver", "SocpResult"]

_TOL = 1e-10


@dataclass(frozen=True)
class SocpResult:
    c: Vec
    r: float
    status: str   # cvxpy status; only "optimal" is used for pass/fail


class SocpSolver:
    def __init__(self) -> None:
        self._c = cp.Variable(3)
        self._r = cp.Variable()
        self._P = [cp.Parameter((3, 3)) for _ in range(3)]
        self._b = [cp.Parameter(3) for _ in range(3)]
        cons = [cp.norm(P @ self._c - b) <= self._r for P, b in zip(self._P, self._b)]
        self._prob = cp.Problem(cp.Minimize(self._r), cons)
        if not self._prob.is_dpp():
            raise RuntimeError("SOCP is not DPP: parameters would force recompilation")

    def solve(self, lines: list[Line]) -> SocpResult:
        for line, P, b in zip(lines, self._P, self._b):
            proj = projector(line)
            P.value = proj
            b.value = proj @ line.a
        try:
            self._prob.solve(solver=cp.CLARABEL, tol_gap_abs=_TOL, tol_gap_rel=_TOL,
                             tol_feas=_TOL)
        except cp.error.SolverError as err:
            return SocpResult(np.full(3, np.nan), float("nan"), f"solver_error: {err}")
        if self._c.value is None:
            return SocpResult(np.full(3, np.nan), float("nan"), str(self._prob.status))
        return SocpResult(np.asarray(self._c.value, dtype=float), float(self._r.value),
                          str(self._prob.status))
