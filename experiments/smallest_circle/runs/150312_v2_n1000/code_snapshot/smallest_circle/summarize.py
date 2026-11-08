"""Per-case summary from the per-instance rows (reads rows, never re-derives them)."""
from __future__ import annotations

import numpy as np

__all__ = ["summarize"]


def _f(rows: list[dict], key: str) -> np.ndarray:
    return np.array([float(r[key]) for r in rows if r[key] != ""], dtype=float)


def _stats(x: np.ndarray) -> dict:
    if x.size == 0:
        return {"n": 0}
    return {"n": int(x.size), "max": float(x.max()), "median": float(np.median(x)),
            "p95": float(np.percentile(x, 95))}


def _verdict(counts: dict[str, int]) -> str:
    bad = counts["fail"] + counts["closed_form_error"] + counts["socp_failed"]
    if bad:
        return "FAIL"
    if counts["ok"]:
        return "PASS"
    return "SOCP_ONLY" if counts["no_closed_form"] else "EMPTY"


def summarize(rows: list[dict], cases: list[str], requested: dict[str, int]) -> dict:
    out: dict[str, dict] = {}
    for case in cases:
        rs = [r for r in rows if r["case"] == case]
        counts = {s: sum(r["status"] == s for r in rs)
                  for s in ("ok", "fail", "no_closed_form", "closed_form_error", "socp_failed")}
        uniq = [r for r in rs if r["center_unique"] is True and r["center_dist"] != ""]
        out[case] = {
            "n_rows": len(rs), "n_random_requested": requested[case],
            "n_random_generated": sum(r["source"] == "random" for r in rs),
            "n_preset": sum(r["source"] == "preset" for r in rs),
            "counts": counts, "verdict": _verdict(counts),
            "abs_dr": _stats(_f(rs, "abs_dr")), "scaled_dr": _stats(_f(rs, "scaled_dr")),
            "touch_max": _stats(_f(rs, "touch_max")), "center_gap": _stats(_f(rs, "center_gap")),
            "center_dist_unique_center": _stats(_f(uniq, "center_dist")),
            "failed_ids": [r["instance_id"] for r in rs if r["status"] in
                           ("fail", "closed_form_error", "socp_failed")][:50],
        }
    verdicts = {c: v["verdict"] for c, v in out.items()}
    overall = "PASS" if all(v in ("PASS", "SOCP_ONLY") for v in verdicts.values()) else "FAIL"
    return {"overall": overall, "verdicts": verdicts, "cases": out}
