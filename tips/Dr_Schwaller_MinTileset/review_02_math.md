# Review 02: mathematics of the 2×n Minimum Tileset study page

Scope: `00_research_notes.md` §4–§5 and `study_tips.html` tab 0 (steps 1–8, inline SVG, stepper JS at lines ~1495–1515).
Method: hand reasoning and file reading only. No code, simulator or search was run.
Coordinates: columns 1..n west to east, row 0 bottom, row 1 top.

## Verdict table

| # | Claim | Verdict |
| --- | --- | --- |
| 1 | F1: 2×1 needs exactly 2 types; 1 type fails at any τ | CORRECT (F2 reason is too terse, see 1.3) |
| 2 | F3 comb: n + 1 types, directed, corner seed and any bottom seed | CORRECT. Top-row seed: same set FAILS, mirrored comb works |
| 3a | states ≤ 2·t² | CORRECT |
| 3b | n ≲ 4t² follows | CORRECT as arithmetic (gives n ≤ 4t² + 1) |
| 3c | (n/(2·k!))^{1/k} at k = 2 equals √n/2 | CORRECT |
| 3d | pumping step and "any seed position" as written on the page | GAP |
| 4a | τ = 1, no mismatch: exactly n + 1 | CORRECT arithmetic, theorem statement UNVERIFIED (as the notes say) |
| 4b | τ = 1 general: Ω(√n) ≤ t ≤ n + 1 | CORRECT |
| 5 | §4.3 counter (m = 3, D = 2; D = 4, m = 12; counts; 2√(3n)) | CORRECT, with two spec omissions to state (5.4) |
| 6 | 4⌈√n⌉ + 2 and n = 100, 10,000 examples | CORRECT |
| 7a | Mahaney sparse-set argument | CORRECT under unary or canonical cell-list encoding. GAP: canonicalization step. WRONG under binary n (the notes already say so) |
| 7b | constant-factor approximation "for any seed position" | GAP: the "7" factor and the fixed-seed case need fixes (7.2) |
| 7c | 2^{O(√n log n)} algorithm | CORRECT at fixed τ = 2 and unary or list input. Not subexponential in binary input |
| 8 | Tab-0 figures vs spec | CORRECT in all numbers and stepper states. Minor wording and colour issues (8.x) |

No claim is outright WRONG in the sense of a false number or a false construction.
The items to fix are the GAPs in 3d, 7a, 7b and the top-row seed wording in 2.

## 1. F1: 2×1 needs exactly 2 types

Verdict: CORRECT.

1.1 One type fails, any τ ≥ 1.
- Let t be the only type. The seed is one cell; the other cell is directly above or below it.
- The second tile has exactly one placed neighbour (the seed). So that one bond alone has strength ≥ τ.
- Seed below: t.N = t.S = a with str(a) ≥ τ. Then a third t attaches above the second one with the same bond. The column grows forever. No finite terminal assembly exists.
- Seed above: the mirror case, t.S = t.N, grows forever downward.
- The argument does not depend on τ. It uses only "a lone bond must reach τ".

1.2 Two types suffice.
- A (seed): N = a, str(a) = τ, other sides null. B: S = a, other sides null.
- B can attach only above a tile whose N is a, i.e. only above A. A copies can attach only below a tile whose S is a, i.e. below B, and that cell is the seed cell.
- No other side is non-null. So the only terminal assembly is {A at (1,0), B at (1,1)}. Directed. Count 2.

1.3 F2 ("any 2×n with n ≥ 1 needs ≥ 2 types. Same argument: a seed alone covers 1 cell") is CORRECT, but the stated reason is not an argument.
- Fix (replace the reason): "The first tile placed next to the seed binds by one side only, so that glue has strength ≥ τ. With one type, the same tile then repeats in that direction forever (vertical: t.N = t.S; horizontal: t.E = t.W)."

## 2. F3 comb: n + 1 types

Verdict: CORRECT for a corner seed and for any bottom-row seed. The same tile set FAILS for a top-row seed. A vertically mirrored comb works there, so "n + 1 for any seed position" stays true.

2.1 Spec. B_i (i = 1..n): E = e_i (i < n), W = e_{i−1} (i > 1), N = u, S null. All strengths τ. T: S = u, others null.

2.2 Directedness, seed B_1.
- Bottom cell (i+1, 0): its west neighbour B_i offers e_i. Only B_{i+1} has W = e_i. Its north neighbour can only be T after the cell is filled (see next bullet). So exactly one candidate.
- Top cell (i, 1): T has only an S glue, so T needs the bottom tile first. Every bottom tile offers N = u. Only T has S = u. One candidate.
- No B_j can attach under a T, because a T exists only above an already filled bottom cell.
- Outside cells: row −1 needs a match to B.S = null; row 2 needs a match to T.N = null. Top-row neighbours east/west of a T need a match to null. East of B_n and west of B_1 are null.
- Cooperative sums at τ = 2 add nothing, because every glue already has strength τ and every label occurs on exactly one matching pair of types.
- Hence exactly one terminal assembly, shape 2×n. Count n + 1. For n = 1 it equals F1 (2).

2.3 Seed at any bottom cell B_s.
- East: B_{s+1} binds to e_s as before. West: B_s.W = e_{s−1}, and only B_{s−1} has E = e_{s−1}. Induction both ways. Tops as before. CORRECT.

2.4 Seed on the top row (asked in the task).
- With this tile set the seed would be T. Below it, every B_1..B_n offers N = u, so all n types compete for the same cell. Not directed for n ≥ 2. FAILS.
- Fix: use the mirrored comb (chain on the top row, one shared type on the bottom row): T_i with E = e_i, W = e_{i−1}, S = u; one bottom type B with N = u. Seed T_s anywhere on the top row. Same proof, n + 1 types.
- Exact fix for the page: Step 8 box "빗은 어떤 시드든 가능" and notes §4.2 "for any seed position" should add "(seed on the top row: use the vertically mirrored comb)". Figure 5 itself is correct because it says "아래 행".

## 3. F4 lower bound

3a. "states ≤ 2·t²". Verdict: CORRECT.
- State of one column = (top type, bottom type, which of the two was placed first). t · t · 2! = 2t².
- Wording fix: the page (Fig. 6 box 1) and notes §4.1 say "a vertical cut crosses only 2 tiles". A cut between two columns crosses 2 edges and touches 4 tiles. The object counted is a column, which holds 2 tiles. Fix: "세로 열 하나에 타일 2개" / "a column holds only 2 tiles".

3b. "n ≲ 4t²". Verdict: CORRECT as arithmetic, given the pumping step.
- Remove the seed column. n − 1 columns remain on two sides. One side holds ≥ (n − 1)/2 columns.
- If (n − 1)/2 > 2t², some state repeats on that side. So a directed 2×n needs n ≤ 4t² + 1, i.e. t ≥ √((n − 1)/4) ≈ √n/2.
- The paper's own count differs in route but not in value: N > 2·k!·t^k = 4t² forces one type-column to appear ≥ 2·k! + 1 = 5 times, so ≥ 3 copies share an order, and two of them lie on one side of the seed.
- Small caveat in that route: if the seed column is one of the 3 copies, the other 2 may sit on opposite sides. Excluding the seed column costs at most +1 or +2 in N. No effect on √n/2 asymptotically, and none at n = 100 (t ≥ 5 either way).

3c. (n/(2·k!))^{1/k} at k = 2: (n/(2·2))^{1/2} = √(n/4) = √n/2. Verdict: CORRECT.

3d. Pumping step and "holds for any seed position" as written. Verdict: GAP.
- What the page argues (Fig. 7 and its line "E/D 사이 구간을 한 번 더 이어 붙여도 모든 글루가 맞습니다"): two equal columns ⇒ the pumped assembly has all glues matching ⇒ it can be built.
- Why that does not follow: "every glue matches" only makes the pumped assembly locally consistent (stable). Producible needs an attachment order in which each tile meets τ when it is placed. At τ = 2 a tile in the copied stretch may have attached cooperatively with help from its east neighbour (growth went east past column j and came back west). In the pumped assembly that east neighbour is a different copy, placed later. The dependency order can break.
- This is exactly why [S-MTS-2] adds "same attachment order" and needs 3 copies. The page's state definition (Fig. 6 box 2) includes the order, but Fig. 7 and its text use only tile types.
- The "same side of the seed" condition is the part that makes the bound seed-independent. That part is right: growth on one side never needs the far side, and the seed column is excluded.
- I did not re-derive [S-MTS-2]'s producibility proof by hand from the paraphrase. A rigorous route that I can vouch for is the Window Movie Lemma (Meunier, Patitz, Summers, Theyssier, Winslow, Woods, SODA 2014; any τ). For a height-2 window the bond-forming submovie has at most about 2·(2t + 1)² ≈ 8t² values, which gives a Θ(√n) bound with a worse constant (about √n/4). So Θ(√n) is safe; the exact constant 1/2 rests on [S-MTS-2].
- Exact fix for the page:
  - Fig. 7 last line: replace "모든 글루가 맞습니다" with "글루가 모두 맞고, 붙는 순서도 같아서 같은 순서로 다시 붙일 수 있습니다 (증명: [S-MTS-2] Thm 3.1)".
  - Step 5 note: add "글루만 같아서는 부족합니다. 붙는 순서까지 같아야 합니다."
  - Notes §4.1 intuition bullet 3: "If a state (types and order) repeats ..." and add "producibility of the pumped assembly is the non-trivial step; see [S-MTS-2]".

## 4. τ = 1 claims

4a. "No mismatch ⇒ exactly n + 1". Verdict: CORRECT conditional; source theorem UNVERIFIED (the notes flag it).
- Manhattan diameter of 2×n: max over cell pairs of |Δx| + |Δy| = (n − 1) + 1 = n. Plus 1 gives n + 1. Arithmetic correct.
- Consistency check: n×n gives 2(n − 1) + 1 = 2n − 1, which matches the "2N − 1 for squares" snippet of [S-MTS-6]. This supports the reading of "diameter".
- The comb is mismatch-free (every abutting pair is equal: e_i/e_i, u/u, null/null between T's). So it is a legal upper bound inside the restricted class, and the bound is tight there.
- "For any seed position": true, with the mirrored comb for a top-row seed (2.4).

4b. "Ω(√n) ≤ t ≤ n + 1, exact value open". Verdict: CORRECT.
- Lower: [S-MTS-5] Ω(N^{1/k}) at k = 2. It also follows directly from F4, which holds at every τ including τ = 1.
- Upper: comb, n + 1.
- Note: the τ = 1 lower bound adds nothing beyond F4 for k = 2 at the Θ level. The page could say so in one line.

## 5. §4.3 τ = 2 counter

Verdict: CORRECT. The construction is directed, attaches in the claimed order, stops at n = 1 + m·D, and has m + 3D + 2 types. Two omissions in the spec must be written out (5.4).

5.1 Full spec as I read it (δ_d = the digit glue the notes call "d").

| Type | N | E | S | W |
| --- | --- | --- | --- | --- |
| Z (seed, bottom, col n) | z (2) | null | null | q (1) |
| Y (top, col n) | null | null | z (2) | r_{D−1} (2) |
| S_d | null | r_d (2) | s (1) | δ_d (1) |
| M_d | null | δ_d (1) | g (1) | δ_d (1) |
| X_d (d ≥ 1) | null | δ_d (1) | b (1) | r_{d−1} (2) |
| X_0 | null | δ_0 (1) | b (1) | null |
| P_1 | s (1) | q (1) | null | p_1 (2) |
| P_j, 2 ≤ j ≤ m−1 | g (1) | p_{j−1} (2) (omitted in notes) | null | p_j (2) |
| P_m | b (1) | p_{m−1} (2) (omitted in notes) | null | q (1) |

5.2 Trace, m = 3, D = 2, n = 7 (seed column 7; block d = 1 in columns 6–4; block d = 0 in columns 3–1).

| Step | Cell | Offered glues (strength) | Candidates with sum ≥ 2 | Placed |
| --- | --- | --- | --- | --- |
| 0 | (7,0) | seed | | Z |
| 1 | (7,1) | S: z (2) | Y only | Y |
| 2 | (6,1) | E: r_1 (2) | S_1 only | S_1 |
| 3 | (6,0) | E: q (1), N: s (1) | P_1 (1 + 1). No other type has E = q or N = s | P_1 |
| 4 | (5,0) | E: p_1 (2) | P_2 only | P_2 |
| 5 | (5,1) | E: δ_1 (1), S: g (1) | M_1 (1 + 1). X_1 gets 1, M_0 gets 1 | M_1 |
| 6 | (4,0) | E: p_2 (2) | P_3 only | P_3 |
| 7 | (4,1) | E: δ_1 (1), S: b (1) | X_1 (1 + 1). M_1 gets 1, X_0 gets 1 | X_1 |
| 8 | (3,1) | E: r_0 (2) | S_0 only | S_0 |
| 9 | (3,0) | E: q (1) from P_3, N: s (1) | P_1 | P_1 |
| 10 | (2,0) | E: p_1 (2) | P_2 | P_2 |
| 11 | (2,1) | E: δ_0 (1), S: g (1) | M_0 | M_0 |
| 12 | (1,0) | E: p_2 (2) | P_3 | P_3 |
| 13 | (1,1) | E: δ_0 (1), S: b (1) | X_0 | X_0 |
| stop | (0,1) | E: null | none | |
| stop | (0,0) | E: q (1) only, N empty | none (1 < 2) | |

- Other cells: row 2 sees only null N glues; row −1 sees only null S glues; east of column 7 sees null. Nothing grows outside.
- Any order: the top cell of a column never has 2 strength before its bottom cell is filled (its only strength-2 east glues are r_d, which go only to S_d). The bottom cell of a block start (P_1) needs S_d above it, and S_d needs r_d. So every cell, at every time, in every order, has at most one candidate, and it is the one in the table. Directed.
- Length: blocks d = D−1, ..., 0 give D blocks of m columns, plus the seed column: n = 1 + m·D. For (3, 2): 7. Correct.

5.3 D = 4, m = 12.
- Blocks d = 3, 2, 1, 0, each 12 columns: P_1 (coop q + s), P_2..P_11 (chain, tops M_d coop δ_d + g), P_12 (chain, top X_d coop δ_d + b), X_d emits r_{d−1}. After X_0, column 0 gets only q (1). n = 1 + 48 = 49. Types 12 + 12 + 2 = 26. Correct.

5.4 Omissions to write into the spec (exact fix).
- P_j.E for 2 ≤ j ≤ m = p_{j−1}, strength 2. Equivalently P_{j+1}.E = p_j. The strength must be 2: with strength 1, P_{j+1} would need M above, and M needs P below (deadlock).
- "W glue d" / "E glue d" must be a digit-specific label δ_d, distinct per d and distinct from r_d, s, g, b, q, z, p_j. With one shared label "d", X_1 and X_0 (and M_1 and M_0) would both fit, and the system would not be directed.
- State the null sides explicitly: N of S_d, M_d, X_d, Y; S of all P_j and Z; E of Z and Y.
- m ≥ 2 is needed (P_1 ≠ P_m). For m = 2 the M_d types are unused, so the count is m + 2D + 2 there.

5.5 Counts and asymptotics.
- m + 3D + 2: m P's, D each of S, M, X, plus Z, Y. Correct. (3, 2): 3 + 6 + 2 = 11. Correct.
- n = 10,035: 173 · 58 = 8,650 + 1,384 = 10,034; + 1 = 10,035. Types 173 + 174 + 2 = 349. Correct.
- Minimize m + 3D with m·D = n − 1: AM-GM gives m = 3D, so 3D² = n − 1, D = √((n−1)/3), m = √(3(n−1)). Sum 2√(3(n−1)) ≈ 2√3·√n = 3.464√n. Correct. Check n = 10,035: 2√30,102 = 347.0, plus 2 = 349.0.
- Limit (stated in notes, correct): only n ≡ 1 (mod m) with the chosen D; other n need a partial first block.
- The "needs a run" (R2) in the notes is now optional for these two instances: the hand trace above settles directedness and shape for (3, 2) and the general (m, D) argument in 5.2 covers all m ≥ 2, D ≥ 1. A run would still be a good independent check.

## 6. Upper bound 4⌈√n⌉ + 2 and examples

Verdict: CORRECT.
- [S-MTS-2] Thm 3.2 groups: m + 2(m − 1) + 1 + 1 + m + k = 4m + k. At k = 2, m = ⌈√n⌉: 4⌈√n⌉ + 2.
- n = 100: m = 10, upper 42; lower √100/2 = 5. 5 ≤ t ≤ 42. Correct.
- n = 10,000: m = 100, upper 402; lower 50. Correct.
- "Constant gap about 8": 4/(1/2) = 8. Correct.
- Fig. 9 extra values: n = 49 → 4·7 + 2 = 30, √49/2 = 3.5. n = 10,035 → ⌈100.17⌉ = 101 → 406, √10,035/2 = 50.09. All correct.

## 7. §5 research directions

7a. Mahaney sparse-set argument. Verdict: CORRECT under unary n, or a canonical cell list. GAP: one step must be added. Fails under binary n (the notes say so).
- Language: L = {⟨2×n shape, k⟩ : OPT ≤ k}, plus the seed position s if the seed is fixed by the input.
- Unary n (or canonical sorted cell list, Θ(n log n) bits): for each input length ℓ there are O(n) values of k (k ≤ n + 1) and O(n) values of s. So poly(ℓ) strings of length ℓ. Sparse.
- GAP: a "list of cells" in arbitrary order has (2n)! encodings of one shape, so the raw language is not sparse. Fix: add the reduction "any encoding ↦ canonical ⟨1^n, s, k⟩" (poly time; non-rectangles map to a fixed no-instance). If the raw problem were NP-hard, the sparse canonical set would be NP-hard under ≤_m^p, and Mahaney gives P = NP. Mahaney's theorem covers sparse NP-hard sets under many-one reductions, so NP membership is not needed for this step.
- NP membership (for "NP-complete" wording): certificate = a tile set with ≤ k ≤ n + 1 types; directed-shape verification is polynomial [S-MTS-1]. Needs τ fixed (or strengths bounded); state it.
- Binary n: ℓ ≈ log n, about 2^ℓ instances per length. Not sparse; the argument says nothing. Also NP membership is unclear, since the certificate has Θ(√n log n) bits, exponential in ℓ.
- "Any seed rule": true, since adding s keeps the count polynomial.

7b. "Constant-factor approximation for any seed position (7-approximation)". Verdict: GAP.
- Seed free (part of the solution): output the corner construction. OPT ≥ √n/2 holds for every seed (3d caveat aside). Using the PROVEN [S-MTS-2] bound, ratio ≤ (4⌈√n⌉ + 2)/max(2, √n/2) → 8, and stays bounded (≤ about 11) for small n. Valid, and it does not need §4.3.
- "7" (3.46/0.5): only asymptotic, only for n = 1 + m·D, and depends on §4.3. Fix: "8-approximation asymptotically by [S-MTS-2]; 7 for n = 1 + mD by §4.3".
- Seed fixed by the input at an interior cell: the corner construction is not a legal output. Fix: two arms of lengths a = s − 1 and b = n − s, one counter growing west and its horizontal mirror growing east, sharing the seed column, with disjoint glue labels. Types ≤ 4⌈√a⌉ + 4⌈√b⌉ + O(1) ≤ 4√2·√n + O(1). Ratio → 8√2 ≈ 11.3. This relies on [S-MTS-2]'s counter handling any arm length 1..m²; that is a claim of the paper (notes §3) that I did not re-check.
- Approximating the number (not the tile set) is trivial in time poly(log n).

7c. 2^{O(√n log n)} algorithm. Verdict: CORRECT with stated conditions.
- At fixed τ = 2, OPT ≤ t_max = 4⌈√n⌉ + 2. A system with t types has 4t sides, each with a label from ≤ 4t + 1 values and a strength in {0, 1, 2}. So ≤ (O(t))^{4t} = 2^{O(t log t)} = 2^{O(√n log n)} systems. Times 2n seed positions and t seed types. Each check is poly(n) [S-MTS-1].
- Subexponential in input length only for unary or list input (ℓ = Θ(n) or Θ(n log n)). In binary, ℓ = log n and the time is 2^{O(2^{ℓ/2} ℓ)}.
- At τ = 1 the only known upper bound is n + 1, so the same enumeration is 2^{O(n log n)}, not subexponential. With τ free, strengths must be bounded first ([S-MTS-4]). The notes' risk column says "must fix τ"; correct.

7d. Other §5 lines.
- "Two one-sided counters cost c√a + c√b ≥ c√(n − 1)": correct by concavity (√a + √b ≥ √(a + b)).
- "Binary counter needs log n rows; F4 rules out O(log n) types": correct.

## 8. Tab-0 figures and stepper states

Verdict: CORRECT for every number, tile, glue position and running count. Minor issues below.
Stepper JS: state k shows groups with data-from ≤ k and data-only = k; the counter shows li[k].data-c. Checked against each figure.

| Figure | Check | Result |
| --- | --- | --- |
| Fig. 1 | Bounds per branch | CORRECT. τ = 2 corner: √n/2 ≤ t ≤ 4⌈√n⌉ + 2 |
| Fig. 2 | 4 cases, sums | CORRECT. Case c glues sit on the west and south edges of the new tile |
| Fig. 3 | 6 states, counts 1,1,1,1,1,2 | CORRECT. Glue a sits on tile boundaries |
| Fig. 4 | 10 states, counts 1,2,3,3,4,4,5,5,6,6; ✓ marks at states 0,1,2,4,6,8 | CORRECT. e_i on the B_i/B_{i+1} boundary, u on each B top edge |
| Fig. 5 | Bottom-row seed | CORRECT |
| Fig. 6 | Box 3 "≤ 2·t²", box 6 "n ≲ 4·t²" | CORRECT numbers. Box 1 wording (3a) |
| Fig. 7 | Copied stretch = columns 5–8 (d,e,f,E) | CORRECT columns. Pumping text is a GAP (3d) |
| Fig. 8 | 6 states vs trace 5.2 | CORRECT. Columns x = 498, 420, 342, 264, 186, 108, 30 = columns 7..1; every glue rect is on the right edge and has the right strength class |
| Fig. 9 | Values and log bar widths (158 px per decade) | CORRECT. 50 → 269, 26 → 224, 30 → 234, 3.5 → 86, 10,036 → 633, 349 → 402, 406 → 412, 50.1 → 269 |
| Step 7 text | 10,036/349 = 28.8 ≈ 29 | CORRECT |
| Fig. 10 | "빗은 어떤 시드든 가능" | Needs the mirror note (2.4) |

Minor issues (exact fixes):
- 8.1 Fig. 3 draws glue a with class `g1` (strength-1 colour), but the argument is "any τ" and needs str(a) ≥ τ. Fix: label it "a (강도 ≥ τ)" or use a neutral colour.
- 8.2 Fig. 4 reuses `--series-l1` / `--series-l2` with a new meaning (e / u), while Step 2 uses them for strength 1 / 2. Also B1's tile fill is the "e" colour and B2's fill is the "u" colour. Fix: use a neutral tile fill, and add "(색은 글루 이름, 강도는 모두 τ)" to the legend.
- 8.3 Fig. 6 box 1 "자른 선이 타일 2개를 지남" → "열 하나에 타일 2개".
- 8.4 Fig. 7 last line and Step 5 note: add the attachment-order condition (3d).
- 8.5 Fig. 7 uses the letter "t" for a tile, which collides with t = number of types. Fix: rename to another letter.
- 8.6 Fig. 8 state 5 draws block 2 without glue marks. The key cooperative bond (q from P_3 + s from S_0 into the second P_1) is not shown. Optional fix: draw q at x = 186 and s at y = 160 for that column.
- 8.7 Fig. 8 state 0 shows Y already placed; the step text starts at S_1. Fine as is; optionally say "Z, Y는 시드 열".
- 8.8 Fig. 8 note box at state 2 ("P₂, P₃ 동쪽 글루 없음, p₁, p₂로 읽음") is the correct reading. After 5.4 is added to the notes, it can say "노트: P_{j+1}.E = p_j (강도 2)".

## Needs a run

- None of the 8 items needs a run to reach its verdict.
- Still useful (cluster only, main session submits): R2 simulation of §4.3 for a few (m, D) as an independent check; R1 exhaustive search for n ≤ 8 to settle the small-n table (§4.4), which hand reasoning cannot settle.
