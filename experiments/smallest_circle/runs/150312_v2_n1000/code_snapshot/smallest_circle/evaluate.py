"""One instance -> one row. Pass criteria are the pre-registered ones (README), fixed here."""
from __future__ import annotations

import json
import math

import numpy as np

from .check_touch import touch_residual
from .circle import build_circle
from .closed_form import solve_closed_form
from .geometry import Line, dist
from .verify_socp import SocpSolver

__all__ = ["evaluate", "ROW_FIELDS", "TOL_R", "TOL_TOUCH", "TOL_CENTER_GAP"]

TOL_R = 1e-6           # |r_closed - r_socp| <= TOL_R * max(1, r_socp)
TOL_TOUCH = 1e-6       # touch residual per line, absolute
TOL_CENTER_GAP = 1e-6  # max_i dist_i(c_closed) - r_socp <= TOL_CENTER_GAP * max(1, r_socp)

ROW_FIELDS = ["case", "instance_id", "source", "r_closed", "r_socp", "abs_dr", "scaled_dr",
              "center_dist", "center_gap", "touch_1", "touch_2", "touch_3", "touch_max",
              "r_known", "branch", "active", "center_unique", "socp_status", "status",
              "detail", "lines_json"]


def _lines_json(lines: list[Line]) -> str:
    return json.dumps([{"a": ln.a.tolist(), "d": ln.d.tolist()} for ln in lines])


def _blank(case: str, iid: str, source: str, lines: list[Line]) -> dict:
    row = {f: "" for f in ROW_FIELDS}
    row.update(case=case, instance_id=iid, source=source, lines_json=_lines_json(lines))
    return row


def evaluate(lines: list[Line], case: str, iid: str, source: str, solver: SocpSolver,
             r_known: float | None = None) -> dict:
    row = _blank(case, iid, source, lines)
    row["r_known"] = "" if r_known is None else r_known
    socp = solver.solve(lines)
    row["r_socp"], row["socp_status"] = socp.r, socp.status
    if not socp.ok:
        row["status"] = "socp_failed"
        return row
    try:
        sol = solve_closed_form(lines)
    except Exception as err:   # noqa: BLE001  a crash is a result, recorded per instance
        row.update(status="closed_form_error", detail=f"{type(err).__name__}: {err}")
        return row
    if sol is None:
        known_ok = r_known is None or abs(socp.r - r_known) <= TOL_R * max(1.0, socp.r)
        row["status"] = "no_closed_form" if known_ok else "fail"
        row["detail"] = "" if known_ok else "socp r differs from r_known"
        return row
    circ = build_circle(lines, sol)
    scale = max(1.0, socp.r)
    touch = [touch_residual(ln, circ) for ln in lines]
    gap = max(dist(ln, sol.c) for ln in lines) - socp.r
    dr = abs(sol.r - socp.r)
    row.update(r_closed=sol.r, abs_dr=dr, scaled_dr=dr / scale,
               center_dist=float(np.linalg.norm(sol.c - socp.c)), center_gap=gap,
               touch_1=touch[0], touch_2=touch[1], touch_3=touch[2], touch_max=max(touch),
               branch=sol.branch, active=",".join(str(i + 1) for i in sol.active),
               center_unique=sol.center_unique)
    finite = all(math.isfinite(x) for x in (sol.r, gap, *touch))
    ok = finite and dr <= TOL_R * scale and max(touch) <= TOL_TOUCH \
        and gap <= TOL_CENTER_GAP * scale
    row["status"] = "ok" if ok else "fail"
    return row
