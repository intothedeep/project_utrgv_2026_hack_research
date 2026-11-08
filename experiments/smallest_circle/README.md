# Smallest circle touching 3 lines: closed form vs SOCP

## What this checks

- Question: does each closed form (center c, radius r, plane normal n) equal the numeric optimum?
- Why: the 2-page paper claims a table of closed forms. A wrong cell must show up before submission.
- Meaning of "touch": intersect (owner, 2026-11-07, root `CLAUDE.md`).
- Numeric optimum: `min r  s.t.  ||P_i (c - a_i)|| <= r`, `P_i = I - d_i d_i^T` (SOCP, cvxpy + Clarabel).
- Closed forms: `tips/Wylie_SmallestCircle/study_tips.html` case table, `02_possible_solutions.md`.

```
instance (3 lines) --> classify --> closed_form --> circle (c, r, n) --> touch residual per line
                  \--> SOCP (c*, r*) ---------------------------------> |dr|, center gap
```

## Inputs

| Set | Count | Source |
| --- | --- | --- |
| Presets | 20 | `presets.py` = PRESETS of `study_tips.html` (fixed). Each goes to the case that `classify` gives |
| Random | 1000 per case, 18 cases | `instances.py`, seed `20261107`, one stream per case. Kept only if `classify` returns the wanted case |

Cases (classifier keys): triangle, concurrent, two_meet_one_cross, one_meet_over, one_meet_overunder,
all_skew, par_meet_both, par_meet_one, par_over, par_overunder, par3_coplanar, par3_acute,
par3_obtuse, one_meet_perp, skew_perp (half on a half-turn axis, half off), par_perp_between,
par_perp_outside, coincident.

## Pre-registered criteria (written before any run, do not edit after)

| Item | Value |
| --- | --- |
| Main metric | `scaled_dr = abs(r_closed - r_socp) / max(1, r_socp)` |
| Pass line (main) | `scaled_dr <= 1e-6` |
| Pass line (touch) | `max_i touch_residual_i <= 1e-6` (absolute) |
| Pass line (center) | `max_i dist_i(c_closed) - r_socp <= 1e-6 * max(1, r_socp)`: c_closed is an optimal point |
| Instance | `ok` only if all three lines hold. Else `fail` |
| Case | `PASS` if every instance is `ok` or `no_closed_form`, and at least one is `ok`. `SOCP_ONLY` if none has a closed form. Else `FAIL` |
| Failure ends as | one `fail`, `closed_form_error` or `socp_failed` in a case marks the case `FAIL`. The formula goes back to derivation. The line is not widened |
| No closed form | status `no_closed_form`: only the SOCP is recorded. If `r_known` exists (hyperboloid R = 1.5, r = 1.5) the SOCP must match it to 1e-6 |
| Reported only | `center_dist` (centers are not unique in parallel cases), per-case median and p95 |

Why 1e-6, not the design's 1e-9: Clarabel runs with gap and feasibility tolerance 1e-10. A 1e-9 line
is inside solver error. 1e-6 leaves a margin of about 4 orders. This is a design choice, not
measured noise. The run is deterministic (fixed seed), so a re-run is a repeat check, not a noise estimate.

Deviation from design V2: the touch test is exact (line-plane intersection), not 128 sample points.
Sampling resolves only about 3e-4 r, too coarse for 1e-6.

## Files

| File | Job |
| --- | --- |
| `src/smallest_circle/geometry.py` | Line, foot, distance, line-line relation |
| `classify.py` | case key of three lines (port of the page's `classify`) |
| `closed_form.py` | dispatcher: active pair test, then three-active forms |
| `active3.py` | incircle, circumcircle, 2-parallel quadratic, 1-meet-perp (PLL), skew-perp half-turn axis |
| `circle.py`, `check_touch.py` | circle (c, r, n) from a solution, exact touch residual |
| `verify_socp.py` | SOCP, built once with cvxpy Parameters |
| `presets.py`, `instances.py` | fixed and random instances |
| `evaluate.py`, `summarize.py`, `run.py` | row per instance, summary per case, entry |
| `run.slurm` | Cradle job, CPU only, node `gpu011` |

Output per run (`runs/<JOB>_<RUN>/`): `results/rows.csv` (one row per instance, includes the three
lines as JSON), `results/summary.json`, `manifest.json` (code commit, code sha, params, env),
`code_snapshot/`, `code.sha256`, `CODE_COMMIT`.

## Node choice

- The owner set node `gpu011` (root `CLAUDE.md`, 2026-11-07).
- `cradle-cluster` SKILL.md section 3 lists `gpu[011-012]` as partition `gpul40q`: time limit infinite,
  other research group's equipment, submit permission separate. `run.slurm` uses `-p gpul40q --nodelist=gpu011`.
- No GPU is requested: the job is CPU work (1 core, 4 GB). The skill does not say gpu011 needs a GPU.
- Not verified: partition name, whether a GPU request is forced, CPU count of gpu011. Check read-only first (step 3).
- `--time=02:00:00` is a guess (no measured time yet).

## Main session steps (agents do not ssh, upload, submit or fetch)

Set `HOST=utrgv_cluster`, `PROJ=smallest_circle` (relative, per the skill). VPN on.

1. Commit the code, then stamp the commit. Stamp only on a clean tree.
```
cd /Users/tio/Documents/project_utrgv_2026_hack_research
git status --porcelain -- experiments/smallest_circle      # must print nothing
git rev-parse HEAD > experiments/smallest_circle/CODE_COMMIT
```
2. Create folders and the environment (first time only).
```
ssh "$HOST" "mkdir -p ~/$PROJ/{code,jobs,logs,runs}"
ssh "$HOST" 'export PATH=$HOME/.local/bin:$PATH; cd ~ && uv python install 3.12.12 && uv venv -p 3.12.12 ~/myEnvs/smallest_circle'
```
3. Upload, build the environment, check the node (read-only).
```
rsync -av --exclude '.venv' --exclude '__pycache__' --exclude 'runs' --exclude 'run.slurm' \
  experiments/smallest_circle/ "$HOST:~/$PROJ/code/"
scp experiments/smallest_circle/run.slurm "$HOST:~/$PROJ/jobs/"
ssh "$HOST" 'export PATH=$HOME/.local/bin:$PATH; cd ~/smallest_circle/code && UV_PROJECT_ENVIRONMENT=$HOME/myEnvs/smallest_circle uv sync'
scp "$HOST:~/$PROJ/code/uv.lock" experiments/smallest_circle/uv.lock      # pins the resolved versions in the repo
ssh "$HOST" 'sinfo -a -N -n gpu011 -o "%N %P %c %m %G %T"'
```
   If a pinned version does not resolve, fix `pyproject.toml` (new commit, new stamp). Do not edit the criteria.
4. Submit (ask the owner about `gpul40q` permission first).
```
ssh "$HOST" 'cd ~/smallest_circle && sbatch jobs/run.slurm v1_n1000'     # prints: Submitted batch job <JOB>
```
5. Watch, then fetch (waits until the job leaves the queue).
```
ssh "$HOST" 'squeue -u $USER -r'
HOST=$HOST PROJ=$PROJ DEST=experiments/smallest_circle/runs \
  bash .claude/skills/cradle-cluster/templates/fetch_runs.sh "<JOB> v1_n1000"
```
6. Check the fetched folder: `job.out.<JOB>` ends with `=== done`, `results/summary.json` has `overall`,
   `manifest.json` has `code_commit`. Then add one line to `00.runs.md` (not created yet).

## Known limits

- Right-angled prism (`par3_right`) has no random generator and no preset. It is not tested.
- `skew_perp` off the half-turn axis, `two_meet_one_cross`, `one_meet_over*`, `all_skew` with three active lines
  have no closed form here. They are `no_closed_form`.
