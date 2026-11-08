# CHANGELOG (code versions, rules/measurement.md section 2.2)

| Version | Date | Change | Affected runs |
| --- | --- | --- | --- |
| v1 | 2026-11-08 | First version: geometry, classify, closed_form, active3, circle, check_touch, verify_socp, evaluate, run | 150311_v1_n1000 (overall FAIL) |
| v2 | 2026-11-08 | (1) `circle.py::_normal_two`: if line k coincides with an active line, build n = unit(e1 + e2) from u and d, not from the tangent intersection. (2) `verify_socp.py`: solver stages Clarabel 1e-10, Clarabel 1e-8, SCS 1e-9. First `optimal` is accepted, `optimal_inaccurate` never. `SocpResult.ok` added, `evaluate.py` tests it. `CODE_VERSION` = v2 | next run (v2_n1000) |

v2 findings (details: `runs/150311_v1_n1000/diagnosis.md`). README criteria are unchanged.

- Finding 1, `coincident` 419 of 1000 `fail`: `scaled_dr` max 4.4e-10 and `center_gap` max 5.9e-11 pass, only the touch residual fails (1e-6 up to 0.54). Line k is tangent to the sphere, so the sphere intersection is rounding noise and n is wrong by up to 1e-7. The touch test divides by n.d, which is also noise, so the residual is O(1). The formula for c and r is right.
- Finding 2, one `socp_failed` in each of one_meet_over, one_meet_overunder, all_skew, par_meet_one, par3_obtuse: Clarabel status `optimal_inaccurate` at tolerance 1e-10 (instrument, not formula). Fix is the solver stage chain. A row failing all stages stays `socp_failed`.

Invariance check: v2 does not change the closed forms, the classifier, the generators or the seeds. The 581 `ok` coincident rows used the old fallback n and keep r. Not yet confirmed by a run: compare `r_closed` and `r_socp` of v2_n1000 with run 150311 on the other 17 cases (expected equal within 1e-9). The last comparison is for the reviewer.
