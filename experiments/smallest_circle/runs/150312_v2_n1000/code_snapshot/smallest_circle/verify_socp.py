"""Numeric optimum: min r s.t. ||P_i (c - a_i)|| <= r (SOCP, cvxpy).

Run on the cluster only. The problem is built once with Parameters (DPP) and re-solved
per instance, so 20k instances do not recompile 20k times.

Solver stages (v2): the first stage that returns status "optimal" is accepted. Every stage is
at least 100 times tighter than the 1e-6 pass line. "optimal_inaccurate" is never accepted.
"""
from __future__ import annotations

from dataclasses import dataclass

import cvxpy as cp
import numpy as np

from .geometry import Line, Vec, projector

__all__ = ["SocpSolver", "SocpResult"]

# (name, solver, cvxpy solve kwargs). Stage 0 is the v1 setting.
_STAGES = (
    ("clarabel_1e-10", cp.CLARABEL, dict(tol_gap_abs=1e-10, tol_gap_rel=1e-10, tol_feas=1e-10)),
    ("clarabel_1e-8", cp.CLARABEL, dict(tol_gap_abs=1e-8, tol_gap_rel=1e-8, tol_feas=1e-8,
                                        max_iter=500)),
    ("scs_1e-9", cp.SCS, dict(eps_abs=1e-9, eps_rel=1e-9, max_iters=200000)),
)


@dataclass(frozen=True)
class SocpResult:
    c: Vec
    r: float
    status: str   # cvxpy status; "<status>[<stage>]" when a later stage ran
    ok: bool      # True only for status "optimal" from some stage


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
        last = SocpResult(np.full(3, np.nan), float("nan"), "no_stage", False)
        for k, (name, solver, kwargs) in enumerate(_STAGES):
            tag = "" if k == 0 else f"[{name}]"
            try:
                self._prob.solve(solver=solver, **kwargs)
            except cp.error.SolverError as err:
                last = SocpResult(np.full(3, np.nan), float("nan"),
                                  f"solver_error{tag}: {err}", False)
                continue
            status = str(self._prob.status)
            if self._c.value is None:
                last = SocpResult(np.full(3, np.nan), float("nan"), f"{status}{tag}", False)
                continue
            last = SocpResult(np.asarray(self._c.value, dtype=float), float(self._r.value),
                              f"{status}{tag}", status == "optimal")
            if last.ok:
                return last
        return last   # all stages failed: the row ends socp_failed, the value is for the record
