"""Run entry: presets + N random instances per case -> results/rows.csv, summary.json,
manifest.json. Cluster only (cvxpy SOCP). Rows are appended and flushed one by one
(write-first, append-verified: a kill loses at most one row).

Usage (run.slurm): PYTHONPATH=src, module smallest_circle.run, flags --run --job --out [--n].
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import socket
import sys
from importlib.metadata import version
from pathlib import Path

import numpy as np

from .classify import classify
from .evaluate import ROW_FIELDS, TOL_CENTER_GAP, TOL_R, TOL_TOUCH, evaluate
from .instances import CASES, generate
from .presets import PRESETS, R_KNOWN
from .summarize import summarize
from .verify_socp import SocpSolver

CODE_VERSION = "v2"
SEED = 20261107
SRC = Path(__file__).resolve().parent


def _code_sha() -> str:
    h = hashlib.sha256()
    for f in sorted(SRC.glob("*.py")):
        h.update(f.name.encode() + f.read_bytes())
    return h.hexdigest()[:12]


def _commit(root: Path) -> str:
    f = root / "CODE_COMMIT"
    return f.read_text().strip() if f.exists() else "unknown"


def _env() -> dict:
    keys = ("SLURM_JOB_ID", "SLURM_JOB_NODELIST", "SLURM_CPUS_ON_NODE", "SLURM_JOB_PARTITION")
    return {"host": socket.gethostname(), "python": platform.python_version(),
            "platform": platform.platform(), "numpy": version("numpy"),
            "cvxpy": version("cvxpy"), "clarabel": version("clarabel"),
            "scipy": version("scipy"), **{k: os.environ.get(k) for k in keys}}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--job", required=True)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--n", type=int, default=1000, help="random instances per case")
    args = ap.parse_args()
    res = args.out / "results"
    res.mkdir(parents=True, exist_ok=True)

    cases = list(CASES)
    by_case: dict[str, list[tuple[str, list]]] = {c: [] for c in cases}
    unclassified = []
    for name, lines in PRESETS.items():
        key = classify(lines)
        (by_case[key] if key in by_case else unclassified).append((name, lines))
    if unclassified:
        print("presets outside CASES:", [n for n, _ in unclassified], file=sys.stderr)
        (res / "unclassified_presets.json").write_text(json.dumps([n for n, _ in unclassified]))
    # one stream per case: adding or reordering cases never changes another case's instances
    gens = {c: np.random.default_rng([SEED, i]) for i, c in enumerate(cases)}
    solver, rows = SocpSolver(), []
    with open(res / "rows.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=ROW_FIELDS)
        w.writeheader()
        for case in cases:
            items = [(f"preset:{n}", "preset", ln, R_KNOWN.get(n)) for n, ln in by_case[case]]
            rand = generate(case, args.n, gens[case])
            items += [(f"rand:{k:04d}", "random", ln, None) for k, ln in enumerate(rand)]
            for iid, source, lines, r_known in items:
                row = evaluate(lines, case, iid, source, solver, r_known)
                w.writerow(row)
                fh.flush()
                rows.append(row)
            print(f"case {case}: {len(items)} instances", flush=True)

    summary = summarize(rows, cases, {c: args.n for c in cases})
    (res / "summary.json").write_text(json.dumps(summary, indent=2))
    manifest = {
        "code_version": CODE_VERSION, "code_sha": _code_sha(),
        "code_commit": _commit(SRC.parent.parent),
        "params": {"n_per_case": args.n, "seed": SEED, "tol_r": TOL_R, "tol_touch": TOL_TOUCH,
                   "tol_center_gap": TOL_CENTER_GAP, "run": args.run, "job": args.job},
        "env": _env(), "metrics": {"overall": summary["overall"], "verdicts": summary["verdicts"]},
    }
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print("overall", summary["overall"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
