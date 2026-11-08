# Diagnosis of run 150311_v1_n1000 (code commit 8a80e7a, node gpu011)

Source: `results/rows.csv`, `results/summary.json`, `job.out.150311`. Read only, nothing re-run.
README criteria are unchanged.

## Finding 1: `coincident` 419 of 1000 fail

Verdict: the closed form (center, radius) is right. The circle normal is numerically unstable. The touch test then amplifies it.

Evidence (all 419 `fail` rows, branch `active2`, active `1,3`):

| Criterion | Worst value over the 419 fail rows | Line |
| --- | --- | --- |
| `scaled_dr` | 4.4e-10 | 1e-6 (passes) |
| `center_gap` | 5.9e-11 | 1e-6 (passes) |
| `touch_max` | 1.0e-6 up to 0.54 | 1e-6 (fails) |

- Only the touch criterion fails. `touch_3` is at most 3.8e-15 in every fail row.
- `touch_1` and `touch_2` carry the whole residual, and they agree to 3e-4 relative (lines 1 and 2 are the same line).
- Example `rand:0001`: touch_1 = 2.33e-4 and the line-plane hit is 0.022 away from the tangent point (e = sqrt(2 r touch)). `rand:0008`: touch 4.1e-3, e = 0.097.

Hand derivation:

1. Lines 1 and 2 coincide (generator `_coincident`: same direction, base point shifted along it). Pair (1,3) gives the optimum: center c = midpoint of the common perpendicular, r = half its length. Line 2 is the "third line" k.
2. The sphere (c, r) touches line 1 at p and line 3 at q, with q - c = -(p - c) = -u.
3. Any normal n with n . u = 0 gives a circle through p and q. That circle meets line 1 (at p), line 2 (same line) and line 3 (at q). So the right answer is any n perpendicular to u.
4. `_normal_two` in `circle.py` instead intersects line k with the sphere. Line k is tangent to the sphere at p, so `disc = wd^2 - w.w + r^2` is pure rounding noise (about 1e-16). Then a = sqrt(disc) is 0 to 3e-8, s = p + a d, and `nn = u x (s - c) = a (u x d)`.
5. When a is below the 1e-9 r^2 guard, a clean fallback runs and the row passes (581 ok rows). When a is between the guard and 3e-8, `nn` is a difference of nearly parallel vectors. The cross product's rounding error is about 1e-16 r^2 in absolute size, so the direction of n is off by about 1e-16 / a, up to 1e-7.
6. A tilted n has n . u of about delta and n . d of about delta (same delta, since the true n is perpendicular to d). `touch_residual` hits the line with the plane at t = n.(c - a)/(n . d). That ratio is O(1) however small delta is, as long as n . d > 1e-9. So the plane-line hit point e slides 1e-3 to 0.5 along line 1, and the residual e^2/(2r) is 1e-6 to 0.5.
7. True distance from the circle to line 1 is at most about delta * r (below 1e-7), so the circle does touch. The residual is an artifact of an unstable n. It is not a formula error.

Why it is only `coincident`: other cases take lk through a non-tangent point of the sphere, so `nn` is well conditioned.

Not wrong: the closed form r, the classifier (all 1000 rows classify `coincident`), the instance generator, the SOCP (center_dist 4e-10 vs the unique center).

Fix: in `circle.py::_normal_two`, when line k coincides with an active line, line k is tangent at p or q by structure. Use a well-conditioned normal n = unit(e1 + e2) with e1 = unit(u x d), e2 = unit(u x e1). Then n . u is exactly 0 to 1e-16 and n . d is +-0.707, so the touch test is well conditioned.

## Finding 2: one `socp_failed` row each in 5 cases

Evidence: all 5 rows have `socp_status = optimal_inaccurate`.

| Case | Row | r_socp | Lines |
| --- | --- | --- | --- |
| one_meet_over | rand:0371 | 0.8482 | lines 1 and 2 share a base point |
| one_meet_overunder | rand:0366 | 0.5268 | lines 1 and 2 share a base point |
| all_skew | rand:0062 | 1.3063 | generic, \|d_i . d_j\| = 0.70, 0.46, 0.47 |
| par_meet_one | rand:0774 | 1.4510 | lines 1 and 2 parallel, line 3 meets line 1 |
| par3_obtuse | rand:0437 | 1.3055 | three parallel lines |

- The solver was Clarabel with `tol_gap_abs = tol_gap_rel = tol_feas = 1e-10`. cvxpy reports `optimal_inaccurate` when Clarabel stops with its reduced tolerance only (`AlmostSolved`). That reduced tolerance is far looser than the 1e-6 pass line, so the value cannot be trusted. Strict handling (mark `socp_failed`) was correct.
- `evaluate` returns at that point, so the closed form never ran for these rows. "Closed form had 0 fail" is empty for them, not evidence.
- 5 of about 18,000 SOCP solves. No `job.out` error line (the log has no solver message).
- Cause inferred, not proven (no solver output saved): the stage tolerance 1e-10 is at the edge of what the interior-point method reaches on a rank-deficient problem. `P_i = I - d_i d_i^T` has rank 2, and for par3_obtuse the free direction along d is shared by all three constraints. The all_skew row is generic, so tolerance alone is the likely reason there.
- No `r_socp` check is possible without a re-solve.

Fix (instrument only, criteria unchanged): `verify_socp.py` tries a fixed chain of solver stages and accepts the first one that returns status `optimal`.

| Stage | Solver | Tolerance |
| --- | --- | --- |
| 0 | Clarabel | 1e-10 (as v1) |
| 1 | Clarabel | 1e-8 |
| 2 | SCS 3.3.1 (in `uv.lock`) | eps_abs = eps_rel = 1e-9, 200000 iterations |

- Every accepted stage is at least 100 times tighter than the 1e-6 pass line.
- `optimal_inaccurate` is never accepted. A row that fails all stages stays `socp_failed`. No row is dropped.
- The stage that solved is written into `socp_status` (`optimal` for stage 0, `optimal[clarabel_1e-8]` or `optimal[scs_1e-9]` otherwise), so a retried row is visible.
