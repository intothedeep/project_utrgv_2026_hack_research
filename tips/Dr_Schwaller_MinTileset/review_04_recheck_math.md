# Review 04: re-check of the 2×n mathematics after the review_02 fixes

Scope: `00_research_notes.md`, `01_study_guide.md`, `02_possible_solutions.md`, `03_plan_and_design.md`, `study_tips.html`.
Method: hand reasoning and file reading only. No code, simulator, browser or search was run.
Coordinates: columns 1..n west to east, row 0 bottom, row 1 top.

## Verdict table

| # | review_02 item | Verdict |
| --- | --- | --- |
| 1.3 | F2 reason | CLOSED |
| 2 / 2.4 | Top-row seed, mirrored comb | CLOSED (math checked, 2.1 below) |
| 3a | "cut crosses 2 tiles" wording | OPEN in 3 places (Fig. 6 caption, two glossaries) |
| 3d | Pumping needs attachment order and producibility | CLOSED. New wording has a constant overclaim (2.2, 2.3) |
| 4a, 4b | τ = 1 claims | CLOSED |
| 5.4 | Counter spec omissions (p_j strength 2, δ_d, nulls, m ≥ 2, m = 2 count) | CLOSED |
| 6 | 4⌈√n⌉ + 2 examples | CLOSED (unchanged, still correct) |
| 7a | Mahaney canonicalization | CLOSED as written. NEW ERROR: k in binary breaks sparseness (2.6) |
| 7b | Approximation factors | CLOSED. Arithmetic correct (2.7) |
| 7c | 2^{O(√n log n)} conditions | CLOSED. Small gap for a fixed interior seed (2.8) |
| 8.1–8.8 | Figure issues | CLOSED (8.3 partly OPEN, see 3a) |
| new | τ = 2 interior seed shown with "upper bound unknown" | NEW ERROR: contradicts the comb (n + 1) and the two-arm counter (3, item N3) |
| new | Step 6 badge "설명용 예시" uses the UNVERIFIED style | Label mismatch (3) |

## 1. review_02 items: CLOSED / OPEN / NEW ERROR

1.3 F2. CLOSED. Notes §4.1 F2 now gives the one-sided-bond argument for both directions.

2 / 2.4 Top-row seed. CLOSED.
- Notes F3, guide §2, solutions "알려진 결과", HTML Fig. 5 text, Step 4 note, Fig. 10 box, Table 2 all say "top-row seed: mirrored comb, n + 1".

3a Wording "a vertical cut crosses 2 tiles". OPEN in three places.
- Fixed: notes §4.1, guide §3.1, HTML Fig. 6 box 1 ("세로 열 하나에 타일 2개").
- Still old: HTML Fig. 6 caption ("세로 자름 한 번에 지나는 정보가 타일 2개뿐").
- Still old: guide glossary `term-column-state` ("한 세로 절단선이 지나는").
- Still old: HTML glossary `term-state` ("세로로 자른 선이 지나는"). It also says "상태가 같은 두 열은 서로 바꿔 끼울 수 있음". That is the overclaim 3d removed elsewhere.

3d Producibility step. CLOSED.
- Notes §4.1 intuition bullets 4–5, guide §3.1, HTML Fig. 7 lines 2–3, Step 5 list and the attachment-order glossary all state the condition and cite [S-MTS-2] Thm 3.1.
- New sub-issue on the constant: 2.2, 2.3.

4a / 4b. CLOSED. Diameter + 1 = n + 1, the 2n − 1 consistency check, and the comb in the restricted class are all present.
4b's "τ = 1 lower bound adds nothing beyond F4" line is in the notes and guide.

5.4 Counter spec. CLOSED. All five omissions are in notes §4.3 lines 153–161 and 173. The re-trace is in 2.4.

6. CLOSED.

7a. CLOSED for the cell-list ordering. NEW ERROR in the same reduction (2.6).

7b. CLOSED (2.7).

7c. CLOSED (2.8).

8.x Figures.
- 8.1 CLOSED: Fig. 3 legend "글루 a (강도는 온도 τ 이상)". The SVG has class `neutral`, so CSS line 225 paints g1/g2 grey.
- 8.2 CLOSED: Fig. 4 is `neutral`, tile fills are `--muted`, legend "모든 글루 강도 = τ".
- 8.3 partly OPEN (3a).
- 8.4 CLOSED.
- 8.5 CLOSED: Fig. 7 letters avoid t. The note "t는 타일 종류 수에만 씁니다" was added.
- 8.6 CLOSED: state 5 now draws q, s, δ₀, p₁, g, δ₀, p₂, b (2.4).
- 8.7 fine.
- 8.8 CLOSED: the state 2 box reads "P₂, P₃ 동쪽 글루: p₁, p₂ (강도 2)".

## 2. New math text added by the fixes

### 2.1 Top-row-seed flipped comb

Verdict: CORRECT.
- Spec: T_i has E = e_i (i < n), W = e_{i−1} (i > 1), S = u. One bottom B has N = u. All other sides are null. All strengths are τ.
- Top cell (i, 1): the only offered glue is e_{i−1} from the west or e_i from the east. Only T_i matches. One candidate.
- Bottom cell (i, 0): B has only the N glue, so B needs T_i above it first. Only B has N = u. No T_j fits below (T_j.N is null).
- A top cell can never be empty while its bottom cell is full. So no T_j ever attaches on top of a B through u.
- Outside: row 2 sees T.N = null. Row −1 sees B.S = null. E/W of the bottom row sees null/null.
- Count: n + 1. Seed T_s anywhere on the top row. Induction runs both ways.

### 2.2 Window-movie and attachment-order wording

Verdict: correct in substance. One overclaim about the constant.
- "Glues matching is not enough. Order must match and the pumped assembly must be producible." Correct (review_02 §3d).
- WML attribution (Meunier, Patitz, Summers, Theyssier, Winslow, Woods, SODA 2014): authors are right. The source is not in the notes' source table. Only the HTML glossary says "원문을 읽지 않았음". The notes and guide should mark it UNVERIFIED.
- Overclaim: "WML gives a worse constant, about √n/4". That came from a loose count in review_02 (2·(2t + 1)² ≈ 8t² movies).
  - A height-2 window has 2 edges.
  - The east-side glue labels number at most t.
  - Movies are: one bond (2 places × t labels), or two bonds (2 orders × t² labels).
  - Total ≤ 2t² + 2t = 2t(t + 1).
  - Two equal movies on one side of the seed give n − 1 ≤ 4t(t + 1), so t ≳ √n/2 − 1.
  - So WML can also reach the constant 1/2. "√n/4" is a valid but loose bound. It is not "what WML gives".
- Fix: see 4, fixes F2–F3.

### 2.3 "Θ(√n) from intuition vs constant 1/2 from [S-MTS-2]"

Verdict: internally inconsistent wording. The math is fine.
- Notes §4.1 bullet "With that step, n ≤ 4t² + 1, so t ≥ √n/2" derives the constant 1/2 from the intuition plus the producibility step.
- The next bullet says the intuition "gives only Θ(√n)". Both cannot be the intuition's output.
- The correct split:
  - The counting (≤ 2t² column states, one side of the seed) gives 1/2 once producibility is granted.
  - The producibility step is what [S-MTS-2] Thm 3.1 proves (or WML). Without it the intuition proves nothing.
- Same wording in guide §3.1 (lines 169–171) and HTML Step 5 (vzbar note and list items 4–5).

### 2.4 Counter δ_d labels, strength-2 p_j glue, and the m = 3, D = 2 re-trace vs HTML Step 6

Verdict: CORRECT. Spec, glue placement and stepper states match the hand trace.

Spec check (notes §4.3):
- P_{j+1}.E = p_j (2) and P_j.W = p_j (2) for j < m. Strength 2 is needed: with 1, P_{j+1} would wait for M above it, and M waits for P below it.
- δ_d is distinct per d. With one shared label, the cell above P_m offers δ + b. Both X_1 and X_0 get 1 + 1. Not directed. The fix is right.
- Nulls, m ≥ 2, D ≥ 1: stated.

Stepper source (lines 605–697). Column x positions: 498, 420, 342, 264, 186, 108, 30 = columns 7..1. y = 100 is the top row, y = 160 the bottom row. The JS shows data-from ≤ k and data-only = k (lines 1540–1541).

| k | Shown placed | Glue marks (position, class) | Hand trace | Match |
| --- | --- | --- | --- | --- |
| 0 | Z, Y (col 7), S₁ (col 6 top), highlight S₁ | z on the row boundary of col 7 (g2). r₁ at x 491–505 = col 6/7 top edge (g2) | S₁ on r₁ (2) | yes |
| 1 | + P₁ (col 6 bottom) | q at x 493–503 = col 6/7 bottom edge (g1). s on the col 6 row boundary (g1) | P₁ on q + s = 1 + 1 | yes |
| 2 | + P₂ (col 5), P₃ (col 4) bottom | p₁ at the 420 edge (g2). p₂ at the 342 edge (g2) | chain, strength 2 | yes |
| 3 | + M₁ (col 5 top) | δ₁ at the 420 top edge (g1). g on the col 5 boundary (g1) | M₁ on δ₁ + g. X₁ gets 1, M₀ gets 1 | yes |
| 4 | + X₁ (col 4 top) | δ₁ at the 342 top edge (g1). b on col 4 (g1). r₀ at x 257–271 = 264 edge (g2) | X₁ on δ₁ + b, emits r₀ | yes |
| 5 | + S₀, P₁ (col 3), M₀, P₂ (col 2), X₀, P₃ (col 1) | r₀ (g2), q at the 264 bottom edge (g1), s col 3 (g1), δ₀ at 186 top (g1), p₁ at 186 bottom (g2), g col 2 (g1), δ₀ at 108 top (g1), p₂ at 108 bottom (g2), b col 1 (g1). "X₀ 서쪽 = 널" | block d = 0, then stop: col 0 top sees null, col 0 bottom sees q (1) < 2 | yes |

- Counter labels data-c "1 / 6" … "6 / 6" match the six messages.
- Type count box: P₁–P₃ (3) + S₀, S₁, M₀, M₁, X₀, X₁ (6) + Z, Y (2) = 11 = 3 + 3·2 + 2. n = 1 + 3·2 = 7. Comb at n = 7: 8.
- Directedness, any order: a top cell never has strength 2 before its bottom cell, except via r_d, which only S_d has. A bottom P₁ needs S_d above it. Every cell has at most one candidate at every time. Shape 2×7.
- Minor (not math): Fig. 8 vzbar uses the `st dead` badge for "설명용 예시". That is the UNVERIFIED style from the Step 1 legend (3).

### 2.5 m = 2 type count

Verdict: CORRECT.
- m = 2: P₁ (N = s, W = p₁, E = q), P₂ = P_m (N = b, E = p₁, W = q). There is no middle P, so M_d never attaches.
- X_d binds on δ_d (from S_d.W) + b. Types = 2 + 2D + 2 = m + 2D + 2. n = 1 + 2D.
- Note: that is n + 3 types, more than the comb. Not an error, just never useful.

### 2.6 Mahaney encoding conditions and the normalization reduction

Verdict: the cell-order normalization is right. NEW ERROR: the canonical form ⟨1^n, s, k⟩ is not sparse if k is written in binary.
- Direction: the reduction maps raw ≤_m^p canonical. So raw NP-hard ⇒ canonical NP-hard. Then sparse + NP-hard ⇒ P = NP (Mahaney, NP-hard form). Correct.
- Gap: with k in binary, length-ℓ strings include n = 1 with any k of about ℓ bits. That is about 2^ℓ yes-instances. Not sparse.
- The notes rely on "k ≤ n + 1", but the reduction never enforces it.
- Fix: in the reduction, map every instance with k ≥ OPT-cap (k ≥ n + 1, since the comb gives n + 1) to one fixed yes-instance. Write k (and s) in unary, or in fixed width ⌈log₂(2n + 2)⌉ bits.
- Then each length has O(n²) strings. Sparse.
- Also: HTML Table 4 rank 1 and the glossaries of `03_plan_and_design.md` and `study_tips.html` state Mahaney's theorem in the NP-complete form. The notes and `02_possible_solutions.md` use the NP-hard form.
  - Both are valid here, because NP membership holds at fixed τ.
  - The argument uses the NP-hard form. Use one form everywhere.
- Non-rectangles ↦ fixed no-instance: correct, because the language contains only 2×n shapes.
- Binary n: correctly flagged as failing.

### 2.7 Approximation factors 8×, 7×, 8√2×

Verdict: CORRECT arithmetic.
- 8×: (4⌈√n⌉ + 2)/(√n/2) → 4/(1/2) = 8.
- Small n, with OPT ≥ max(2, √n/2):
  - n = 2–4 gives 10/2 = 5.
  - n = 5–9 gives 14/2 = 7.
  - n = 10–16 gives 18/2 = 9.
  - n = 17 gives 22/2.06 = 10.67 (the maximum).
  - n = 26 gives 26/2.55 = 10.2. The ratio falls after that.
  - So "≤ about 11" holds.
- 7×: 2√3/(1/2) = 4√3 = 6.93. Asymptotic only, n = 1 + mD only, and it rests on the DERIVED counter. Correctly labelled.
- 8√2×: arms a + b = n − 1. 4⌈√a⌉ + 4⌈√b⌉ + O(1) ≤ 4(√a + √b) + O(1) ≤ 4√2·√(a + b) + O(1), by √a + √b ≤ √(2(a + b)).
  - Ratio ≤ 4√2/(1/2) = 8√2 ≈ 11.31. The worst case is a = b.
- The two-arm sharing of the seed column is sound. The labels are disjoint, the arms touch only at that column, and the aTAM is symmetric under left-right reflection.
- For a top-row seed, also flip vertically. Not stated, only a one-line add.

### 2.8 The 2^{O(√n log n)} condition

Verdict: CORRECT for seed free or corner seed, at fixed τ = 2, with unary or list input. Small gap for a fixed interior seed.
- Count: t ≤ t_max = 4⌈√n⌉ + 2.
  - Each type has 4 sides. Each side takes a label from ≤ 4t + 1 values.
  - Strengths can be capped at τ = 2 without changing behaviour.
  - So ≤ (O(t))^{4t} = 2^{O(√n log n)} systems.
  - Multiply by 2n seed cells and t seed types. Each check is poly(n).
- Gap: the search must stop at a proven upper bound on OPT. For a seed cell fixed by the input, the corner bound 4⌈√n⌉ + 2 is not proven.
  - Use t_max = 4⌈√a⌉ + 4⌈√b⌉ + O(1) (two-arm, 2.7). That is still O(√n).
  - Or fall back to n + 1, which gives 2^{O(n log n)}.
- The rest is correct: not subexponential in binary input, and τ = 1 gives 2^{O(n log n)}.

### 2.9 "The comb has no glue mismatches"

Verdict: CORRECT, for the comb and the flipped comb, under either reading of "mismatch".
- One reading: two adjacent sides with different labels.
- The other reading also counts non-null against null.
- Comb abutting pairs: B_i/B_{i+1} = e_i/e_i. B_i/T = u/u. T/T = null/null.
- Flipped comb: T_i/T_{i+1} = e_i/e_i. T/B = u/u. B/B = null/null.

## 3. Status labels

| Claim | Where | Badge shown | Should be | OK? |
| --- | --- | --- | --- | --- |
| F1, F2, F3 (comb, flipped comb) | notes, HTML Steps 3–4, 02 | DERIVED-BY-HAND | DERIVED | yes |
| F4 √n/2, any seed | all | PROVEN [S-MTS-2] | PROVEN | yes |
| Intuition walk-through of F4 | HTML Step 5, notes | DERIVED-BY-HAND | DERIVED (needs the 2.3 wording fix) | yes |
| 4⌈√n⌉ + 2, corner | all | PROVEN | PROVEN | yes |
| τ = 1 no-mismatch n + 1 | all | PROVEN-conditional, partial | PROVEN-conditional (source UNVERIFIED beyond snippet) | yes |
| §4.3 counter | all | DERIVED-BY-HAND, not simulated | DERIVED | yes |
| HTML Step 6 "설명용 예시" | Fig. 8 vzbar | `st dead` (UNVERIFIED style) | plain note, not a status badge | no (cosmetic) |
| WML citation | notes §4.1, guide §3.1 | none | UNVERIFIED (not read) | no |
| Mahaney theorem (rank 1) | notes, 02, HTML | "short rigorous theorem", 🟡 | DERIVED, with the 2.6 fix | needs 2.6 |
| τ = 2 interior seed, upper bound | HTML Fig. 1, Fig. 4, Table 2; 02 case map | "상한 모름" / "t ≤ ?" / "구성을 찾지 못했습니다" | n + 1 (DERIVED, comb). 4√2·√n + O(1) (DERIVED from [S-MTS-2] p.8 length claim) | NEW ERROR |
| τ = 2 interior seed, order | same | open | Θ(√n), DERIVED (lower PROVEN, upper DERIVED). The exact value and the complexity stay open | NEW ERROR |
| CONJECTURE c·√n + O(1), 1/2 ≤ c ≤ 2√3 | notes, 02, HTML | CONJECTURE | CONJECTURE. Note: the upper end 2√3 rests on the DERIVED counter | yes |

## 4. Exact fixes

F1 (3a, OPEN).
- HTML Fig. 6 caption: replace "세로 자름 한 번에 지나는 정보가 타일 2개뿐이라서" with "세로 열 하나에 타일이 2개뿐이라서".
- Guide glossary `term-column-state`: replace "한 세로 절단선이 지나는 위, 아래 타일 종류" with "세로 열 하나의 위, 아래 타일 종류".
- HTML glossary `term-state`: replace "세로로 자른 선이 지나는 위 타일, 아래 타일, 붙은 순서의 묶음. 상태가 같은 두 열은 서로 바꿔 끼울 수 있음" with "세로 열 하나의 위 타일, 아래 타일, 붙은 순서의 묶음. 상태가 같은 두 열 사이는 복사할 수 있음 (증명: [S-MTS-2] 정리 3.1)".

F2 (2.2, 2.3, constant split). Notes §4.1 last bullet: replace it with
"Which part is which: the counting above gives the constant 1/2 once the producibility step is granted. [S-MTS-2] Thm 3.1 proves that step. The Window Movie Lemma (Meunier et al., SODA 2014, UNVERIFIED: not read) also proves it; a movie count of ≤ 2t(t + 1) gives about √n/2, a looser count gives √n/4."

F3 (same split, guide and HTML).
- Guide §3.1 lines 169–171: replace them with "상수 1/2는 위 세기에서 나온다. 단, 복사 조립체가 생성 가능하다는 단계가 필요하다. 그 단계는 [S-MTS-2] 정리 3.1이 증명한다. 창 영화 보조정리로도 증명할 수 있다 (원문 미확인)."
- HTML Step 5: vzbar note "직관만으로는 Θ(√n)까지 얻습니다" becomes "생성 가능 단계는 [S-MTS-2]가 증명합니다".
- HTML Step 5: list item 4 becomes "상수 1/2은 위 세기에서 나오고, 생성 가능 단계는 [S-MTS-2] 정리(Theorem) 3.1이 증명합니다."
- HTML Step 5: list item 5 becomes "창 영화 보조정리(Window Movie Lemma)로도 같은 단계를 증명할 수 있습니다(원문 미확인)."

F4 (2.6, NEW ERROR).
- Notes §5 rank 1, 02 rank 1, HTML Table 4 rank 1: after "canonical ⟨1^n, s, k⟩" add "with k and s in unary (or fixed width), and every instance with k ≥ n + 1 mapped to one fixed yes-instance (the comb gives OPT ≤ n + 1)".
- Use the NP-hard form of Mahaney in the HTML and `03` glossaries: "희소한 NP-어려움 집합(다대일 다항 시간 환원)이 있으면 P = NP".

F5 (interior seed upper bound, NEW ERROR).
- HTML Fig. 1 bottom box line "상한과 정확한 값은 모름": replace it with "상한 n + 1 (빗), O(√n) (두 팔 카운터, 손 유도). 정확한 값은 모름".
- HTML Fig. 4 τ = 2 interior cell: replace "상한과 정확한 값 열림" with "Θ(√n) 손 유도. 정확한 값 열림".
- HTML Table 2 τ = 2 interior, upper cell: replace "이 노트에서 안쪽 시드용 구성을 찾지 못했습니다." with "n + 1 (빗, F3). 4⌈√a⌉ + 4⌈√b⌉ + O(1) ≤ 4√2·√n + O(1) (두 팔 카운터, 손 유도, [S-MTS-2] 8쪽 길이 주장에 기댐)".
- `02_possible_solutions.md` case map line "안쪽 시드: √n/2 ≤ t ≤ ?": replace "?" with "4√2·√n + O(1) (손 유도)".

F6 (2.8). Notes §5 rank 2: add "For a seed cell fixed by the input, search up to the two-arm bound 4⌈√a⌉ + 4⌈√b⌉ + O(1) (rank 5), not 4⌈√n⌉ + 2."

F7 (2.7). Notes §5 rank 5: add "Top-row seed cell: also flip vertically."

F8 (3, cosmetic). HTML Fig. 8 vzbar: change `<span class="st dead">설명용 예시(Illustrative example)</span>` to a plain `<span class="note">`.

## Needs a run

- No verdict above needs a run.
- Optional, cluster only: R2 for the §4.3 counter (independent check of 2.4). R1 for the small-n table.
- The two-arm interior construction (F5) would also benefit from an R2-style simulation for a few (a, b).
