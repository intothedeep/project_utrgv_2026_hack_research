# Research notes: Minimum Tileset Problem for 2×n rectangles (aTAM)

Tag: MTS. Accessed: 2026-11-07. Summary counts: sources 12 (verified 4, partial 6, unverified 2), rejected 3, unverified claims 7.
Interruption: one rate-limit stop during search. The search budget was spent, so sections were written from verified reads.

## 1. aTAM definitions

| Term | Definition | Source |
| --- | --- | --- |
| Tile type | A unit square. Each of its 4 sides (N, E, S, W) has a glue label. | [S-MTS-4] §2 |
| Tile | One copy of a tile type. Copies are unlimited. | [S-MTS-4] §2, [S-MTS-3] §2 |
| Glue strength | A function g gives each glue label a strength in {0, 1, 2, ...}. Two touching sides bind only if their labels are equal and the strength is positive. | [S-MTS-4] §2, [S-MTS-2] §2.1 |
| Temperature τ | The binding threshold. A tile attaches only if the total strength of its matching sides is at least τ. | [S-MTS-2] §2.1 |
| τ = 1 | "Non-cooperative". One matching glue is enough. | [S-MTS-5] abstract |
| τ = 2, cooperation | One strength-2 glue, or two strength-1 glues together (cooperative binding). | [S-MTS-2] §3 construction, [S-MTS-3] §2 |
| Seed | One fixed starting tile at a fixed position. Growth starts there. | [S-MTS-2] §2.1, [S-MTS-4] §2 |
| Assembly | A connected placement of tiles on the grid Z². | [S-MTS-4] §2 |
| Producible | Reachable from the seed by adding one tile at a time, each attaching with strength ≥ τ. | [S-MTS-4] §2 |
| Terminal assembly | A producible assembly to which no tile can attach. | [S-MTS-4] §2 |
| Uniquely self-assembles (directed) | Exactly one terminal assembly exists, and its shape is S. Same tile at every position in every run. | [S-MTS-4] §2: "A□[T] = {α̂} and dom α̂ = S" |
| Strictly self-assembles (not necessarily directed) | Every terminal assembly has shape S. Different runs may put different tile types at a position. | [S-MTS-3] §1–§2 |
| Uniquely produces (Aggarwal et al. wording) | A terminal supertile S of the shape exists, and every producible supertile can grow into S. This equals the directed notion. | [S-MTS-2] §2.1 |
| Tile complexity | The minimum number of tile types that uniquely assemble the shape. | [S-MTS-2] §1, §2.1 |

Which definition the Minimum Tileset Problem uses:
- Adleman et al. 2002 use "uniquely produces", which is the directed notion. [S-MTS-1] abstract, [S-MTS-3] p.1: "minimum number of deterministic tile types ... shown to be NP-complete by Adleman, Cheng, Goel, Huang, Kempe, Moisset de Espanés, and Rothemund".
- Bryans et al. study the non-directed (strict) version. [S-MTS-3]
- The hackathon question says "uniquely self-assemble". Read with the standard aTAM meaning, this is the directed version (inference). Section 7 open_questions asks the setter to confirm it.

Rotation:
- Tiles do not rotate. Each tile type is a fixed quadruple (north, east, south, west), and it is placed by translation only. [S-MTS-2] §2.1 (tile = "ordered quadruple"), [S-MTS-4] §2 (tile type as a function {N,S,E,W} → labels). No source states "no rotation" in those words, so the rule is read from the definitions (inference, partial).

Seed and glue conventions that matter for 2×n:
- Aggarwal et al. place the seed at (0,0) and use one temperature. Glues bind only to equal labels in the standard model: G(x,y) = 0 for x ≠ y. [S-MTS-2] §2.1
- Bryans et al. use a single-tile seed and τ = 2 for all their results. [S-MTS-3] §2
- Adleman et al.'s polynomial algorithm for squares assumes τ = 2. Chen, Doty and Seki later removed that assumption. [S-MTS-4] p.2

## 2. Known complexity results

| Result | Setting | Status | Source |
| --- | --- | --- | --- |
| Minimum tile set: NP-complete in general | directed ("uniquely produces"), finite shapes | verified (abstract) | [S-MTS-1], restated in [S-MTS-3] p.1 |
| Minimum tile set: polynomial on trees | directed | verified (abstract only). Conditions such as τ and seed position are UNVERIFIED | [S-MTS-1] |
| Minimum tile set: polynomial on N×N squares | directed, τ = 2 | verified | [S-MTS-1], [S-MTS-4] p.2 |
| Squares at any temperature: polynomial | directed | verified | [S-MTS-4] abstract, p.2–3 |
| Verifying that a given system uniquely produces a shape: polynomial | standard model | verified | [S-MTS-1] abstract, [S-MTS-2] §1 |
| Minimum tile set, strict (non-directed): Σ2^P-complete | finite shapes, single-tile seed, τ = 2 | verified | [S-MTS-3] abstract, p.3, §2 |
| Unique-shape verification: co-NP-complete in the "unique shape" model | generalized model | verified | [S-MTS-2] §1, Table 1.1 |
| Rectangles k×N (k ≥ 2, not square): exact complexity of the minimum tile set problem | any | **no result found** (open as far as found) | searches in §7 log |

Why the square algorithm is polynomial (this matters for 2×n):
- It is a brute-force search over all τ = 2 systems with at most O(log n / log log n) tile types. [S-MTS-4] p.2
- For a fixed τ, the number of such systems is polynomial in n. [S-MTS-4] p.2
- Input is "a list of its points", so the input size is about n². [S-MTS-4] p.2 footnote 1
- The same trick fails for 2×n. The answer there is Θ(√n) tile types (§3). There are about (√n)^{O(√n)} = 2^{O(√n log n)} candidate systems, which is not polynomial (inference).

## 3. Known bounds for rectangles

| Shape | τ | Lower bound | Upper bound | Source |
| --- | --- | --- | --- | --- |
| N×N square | 2 | Ω(log N / log log N) for almost all N | O(log N / log log N), all N | [S-MTS-2] §1, [S-MTS-4] p.2 (citing Rothemund–Winfree [S-MTS-11] and Adleman–Cheng–Goel–Huang [S-MTS-12]) |
| N×N square, no glue mismatches | 1 | 2N − 1 | not checked | [S-MTS-6] (snippet only, partial) |
| k×N thin rectangle | any (standard model) | Ω(N^{1/k} / k) (Thm 3.1) | O(N^{1/k} + k) (Thm 3.2), built at τ = 2 | [S-MTS-2] pp.6–8 |
| k×N thin rectangle | 1 (2D) | Ω(N^{1/k}), with \|G\| ≥ N^{1/k}/128 glues | N + k − 1 (comb), best known | [S-MTS-5] Thm 1, intro |
| k×N, just-barely 3D | 1 | Ω(N^{1/k}) (snippet) | O(N^{1/⌊k/3⌋} + log N) | [S-MTS-5] (3D upper), [S-MTS-8] (UNVERIFIED details) |
| k×N, 2 temperatures | multi-τ model | Θ(log N / log log N) | same | [S-MTS-2] Table 1.1, Thm 4.1, 6.1 |

Exact constants in Aggarwal et al. (read in the full text) [S-MTS-2]:
- Thm 3.1 proof: fewer than (N / (2·k!))^{1/k} tile types cannot uniquely assemble k×N.
- The proof picks k-tile columns repeated more than 2(k!) times. At least 3 copies share the same attachment order. Two of them lie on the same side of the seed, and this makes an infinite pumping loop possible.
- Remark after Thm 3.1: the argument works for any length-N shape with column height ≤ k.
- The proof works **wherever the seed is** ("Wherever the seed tile of the construction occurs, it lies to either the west or east of two of the identically placed columns").
- Thm 3.2 construction: a k-digit, base-m counter with m = ⌈N^{1/k}⌉, τ = 2, and 4m + k tile types. Tile groups: m normal, 2(m−1) hairpin, return-probe R, probe P, m chain, and k seed column (Fig. 3.1).
- Seed placement: the seed column S0..S_{k−1} sits at the east end, and the seed S0 sits at its bottom. **The seed is a corner.** Fig. 3.1 shows it, and the chain grows west from it.
- Length control: the west glues of the seed column encode the starting value m^k − N. Any length 1..m^k is possible. [S-MTS-2] p.8

Plugging in k = 2 (arithmetic only, no run):
- Lower: t ≥ (n/4)^{1/2} = √n / 2, for any seed position.
- Upper (corner seed, τ = 2): t ≤ 4⌈√n⌉ + 2.
- Example n = 100: 5 ≤ t ≤ 42. Example n = 10,000: 50 ≤ t ≤ 402.
- So the 2×n answer at τ = 2 is Θ(√n). The constant gap is about 8 (inference).

Thin-rectangle papers, Summers / Furcy line:
- Furcy, Summers, Wendlandt (arXiv 1808.04358) are verified [S-MTS-5].
- A 2020 paper on just-barely-3D thin rectangles at τ = 1 exists (arXiv 2007.11093) [S-MTS-8]. Its authors and exact bounds are UNVERIFIED (snippet only).
- "Proving new directed tile complexity lower bounds at temperature 1 by folding between 2D and just-barely 3D self-assembly" exists (ResearchGate 379409972) [S-MTS-9]. The page returned 403, so its authors, year and bounds are UNVERIFIED. It may tighten the τ = 1 2D directed bound for 2×n. Check it first if there is time.
- "Optimal program-size complexity for self-assembled squares at temperature 1 in 3D" (Furcy, Micka, Summers): not searched. UNVERIFIED.

Problem setter:
- Robert T. Schweller is a co-author of [S-MTS-2], the source of the thin-rectangle bounds.
- A later paper (Chalk, Luchsinger, Schweller, Wylie) lists him at UTRGV Computer Science [S-MTS-10] (search snippet, partial).
- "Dr. Schwaller" is **likely** Robert Schweller, UTRGV. This is a flagged inference, not confirmed.
- No Schweller paper that solves 2×n exactly was found.

## 4. Focus: 2×n at τ=1 and τ=2

Labels: PROVEN (cite) / DERIVED-BY-HAND (argument shown) / CONJECTURE.
Coordinates: columns 1..n, rows 0 (bottom) and 1 (top). The 2×n shape is a k×N thin rectangle with k = 2, N = n.

### 4.1 Facts that hold for any τ

- **F1. DERIVED-BY-HAND: 2×1 needs exactly 2 tile types.**
  - Why 1 type fails: the seed type t also fills the second cell, so t.N = t.S with strength ≥ τ. Then t can attach above again, and the column grows forever.
  - 2 types suffice: seed A with N glue a of strength τ, and B with S glue a. All other sides are null.
- **F2. DERIVED-BY-HAND: any 2×n with n ≥ 1 needs ≥ 2 types.**
  - Why: the first tile placed next to the seed binds by one side only, so that glue has strength ≥ τ.
  - With one type, the same tile then repeats in that direction forever (vertical: t.N = t.S. Horizontal: t.E = t.W). [review_02 §1.3]
- **F3. DERIVED-BY-HAND: upper bound n + 1 (comb), any τ, seed at the corner or at any bottom-row cell.** A top-row seed needs the vertically mirrored comb (below). So n + 1 holds for every seed cell. [review_02 §2]
  - Bottom row: B_1 (seed, bottom-left corner), B_2, ..., B_n. B_i has E glue e_i of strength τ, and B_{i+1} has W glue e_i.
  - Every B_i has N glue u of strength τ. One top type T has S glue u. All other sides of T are null.
  - Check: each bottom cell has exactly one possible tile. Each top cell admits only T. T's null E/W sides stop growth past column n. B_n has a null E side. So the system is directed, and its terminal shape is 2×n.
  - Count: n + 1. This matches the "N + k − 1" comb for k = 2 [S-MTS-5].
  - Seed at any bottom cell B_s: east, only B_{s+1} has W = e_s. West, only B_{s−1} has E = e_{s−1}. Induction both ways. Tops as before. [review_02 §2.3]
  - Top-row seed with this tile set FAILS: the seed is T, and below it all n bottom types B_1..B_n offer N = u. They compete under the shared T, so it is not directed for n ≥ 2. [review_02 §2.4]
  - Mirrored comb for a top-row seed: chain T_1..T_n on the top row (T_i: E = e_i, W = e_{i−1}, S = u). One shared bottom type B with N = u. Seed T_s anywhere on the top row. Same proof, n + 1 types. [review_02 §2.4]
  - The comb (and its mirror) is mismatch-free: every abutting pair is equal (e_i/e_i, u/u, null/null). [review_02 §4a]
- **F4. PROVEN: lower bound √n / 2, seed anywhere** ([S-MTS-2] Thm 3.1 proof, k = 2: (n / (2·2!))^{1/2}).
  - Small caveat in that route: if the seed column is one of the 3 copies, the other 2 may sit on opposite sides. Excluding the seed column costs at most +1 or +2 in N. No effect on √n / 2 asymptotically. [review_02 §3b]
- **Intuition, DERIVED-BY-HAND from [S-MTS-2]'s proof idea:**
  - One column holds only 2 tiles. So the state of a column is one pair (top type, bottom type) plus an attachment order (top first or bottom first).
  - With t types there are at most 2·t² such "states".
  - Remove the seed column. One side of the seed holds ≥ (n − 1)/2 columns. If (n − 1)/2 > 2t², a state repeats on that side.
  - Matching glues alone do not allow copying the stretch between the two copies. At τ = 2 a tile in that stretch may have attached cooperatively with help from a neighbour that, in the pumped assembly, is a different copy placed later.
  - So the attachment-order condition is needed: the copies must share types and order, and the pumped assembly must be producible (window-movie-lemma style argument). This producibility step is the non-trivial part. [review_02 §3d]
  - With that step, n ≤ 4t² + 1, so t ≥ √((n − 1)/4) ≈ √n / 2.
  - Which part is which: the counting above gives the constant 1/2 once the producibility step is granted. [S-MTS-2] Thm 3.1 proves that step. The Window Movie Lemma (Meunier, Patitz, Summers, Theyssier, Winslow, Woods, SODA 2014, UNVERIFIED: not read) also proves it. A movie count of ≤ 2t(t + 1) gives about √n / 2. A looser count gives √n / 4. [review_04 §2.2, §2.3]

### 4.2 τ = 1

- PROVEN-conditional ([S-MTS-6], snippet only, partial):
  - Under the "no binding-domain mismatches" assumption, a τ = 1 directed system needs at least (Manhattan diameter + 1) types.
  - The Manhattan diameter of 2×n is (n − 1) + 1 = n (arithmetic).
  - So, under that assumption, the answer is **exactly n + 1**. F3 gives the matching upper bound for every seed cell (top-row seed: the vertically mirrored comb). The comb is mismatch-free, so it lies inside the restricted class.
  - Consistency check: n×n gives 2(n − 1) + 1 = 2n − 1, which matches the "2N − 1 for squares" snippet of [S-MTS-6]. This supports the reading of "diameter". [review_02 §4a]
  - Check before citing: is "Manhattan diameter" defined as I used it? The full text was not read.
- Without the no-mismatch assumption, the best known 2D τ = 1 bounds for k×N are Ω(N^{1/k}) and N + k − 1 [S-MTS-5]. For k = 2 this gives Ω(√n) ≤ t ≤ n + 1.
  - The τ = 1 lower bound adds nothing beyond F4 at the Θ level, since F4 holds at every τ. [review_02 §4b]
- **Open (as far as found): the exact τ = 1 value without the no-mismatch assumption.**
- So two cells of the overview are open: (1) the exact τ = 2 interior-seed value, and (2) the exact τ = 1 value without the no-mismatch assumption. [review_03 N4]
  - The τ = 2 interior seed has a DERIVED upper bound O(√n) (§5). Only its exact value is open.
  - For the τ = 2 corner seed, the setter says a formula ("equation") exists, but it was not found (§4.3 CONJECTURE).
- Answer to the prompt's intuition ("in τ = 1, a 2×n can't reuse a tile type along a row without pumping"):
  - This is believed, and it is proven only under the no-mismatch assumption above.
  - In general it is not proven in 2D [S-MTS-5] (the gap is stated there).

### 4.3 τ = 2: can height 2 hold a counter?

- **Yes, but only a 2-digit counter of base about √n. A log n-bit binary counter does not fit.**
  - Aggarwal et al.'s k-digit base-m counter at k = 2 builds 2×m² with 4m + 2 types, corner seed [S-MTS-2] Thm 3.2. PROVEN.
  - A binary counter needs log n rows to store the bits. The F4 bound (√n / 2) rules out O(log n) types for height 2. PROVEN through F4.
- **DERIVED-BY-HAND (unchecked by simulation): a leaner 2-row counter with about m + 3D + 2 types for n = 1 + m·D.**
  - Status: hand-traced for m = 3, D = 2 and m = 12, D = 4 (review_02 §5.2–§5.3), not simulated. review_02 §5.2 also gives a general directedness argument for all m ≥ 2, D ≥ 1.
  - Seed at the bottom-right corner. Growth runs west in blocks of m columns. The bottom row counts the position in the block. The top row holds a digit d that counts blocks down from D − 1 to 0.
  - Bottom chain P_1..P_m (m types): P_j has W glue p_j of strength 2 for j < m. P_m has W glue q of strength 1. P_1 has E glue q (1) and N glue s (1). P_2..P_{m−1} have N glue g (1). P_m has N glue b (1).
  - P_{j+1} has E glue p_j of strength 2, for 1 ≤ j ≤ m − 1 (so P_2..P_m each have an E glue). [review_02 §5.4]
  - Why strength 2: with strength 1, P_{j+1} would need M above it, and M needs P below it (deadlock).
  - Digit glues: each digit value d has its own label δ_d. The δ_d are distinct per d and distinct from r_d, s, g, b, q, z, p_j.
  - Why distinct: with one shared label "d", X_1 and X_0 (and M_1 and M_0) would both fit the same cell, and the system would not be directed. [review_02 §5.4]
  - Start tiles S_d (D types): E glue r_d (2), W glue δ_d (1), S glue s (1).
  - Middle tiles M_d (D types): E glue δ_d (1), S glue g (1), W glue δ_d (1).
  - Decrement tiles X_d (D types): E glue δ_d (1), S glue b (1). W glue r_{d−1} (2) when d ≥ 1. W glue null when d = 0.
  - Seed Z: W glue q (1), N glue z (2). Top seed-column tile Y: S glue z (2), W glue r_{D−1} (2). Count: 2.
  - Null sides: N of S_d, M_d, X_d and Y. S of all P_j and of Z. E of Z and of Y. [review_02 §5.4]
  - Block cycle:
    1. S_d attaches on r_d (strength 2, alone).
    2. P_1 attaches below it on q + s = 1 + 1. This is cooperation.
    3. P_2..P_m follow on strength-2 chain glues.
    4. M_d fills the top on δ_d + g.
    5. X_d attaches above P_m on δ_d + b and emits r_{d−1}.
    6. After X_0, no S tile can attach. P_1 then has only q (1), so growth stops.
  - Total: m + 3D + 2 types, n = 1 + m·D columns.
  - Choose m ≈ 3D. Then about 2√(3n) ≈ 3.46√n types, versus 4√n + 2 in [S-MTS-2].
  - Examples (arithmetic): D = 4, m = 12 gives n = 49 with 26 types (comb: 50). D = 58, m = 173 gives n = 10,035 with 349 types.
  - Limits: it needs m ≥ 2 and handles only n = 1 + m·D exactly. Other lengths need a partial first block (as in [S-MTS-2] p.8). That is not worked out here.
  - For m = 2 the M_d types are unused, so the count is m + 2D + 2 there. [review_02 §5.4]
  - **Optional run** (R2): the hand traces settle directedness and shape for these instances. A cluster simulation would still be a good independent check (light: one aTAM simulation, no search). [review_02 §5.5]
- **CONJECTURE**: the corner-seed optimum at τ = 2 is c·√n + O(1) for some constant c between 1/2 and 2√3 ≈ 3.46. The setter's "equation" is probably an exact formula of this kind. Its form was not found in any source.

### 4.4 Small n table (n = 1..6)

| n | Proven / derived lower | Best upper found (construction) | Exact value |
| --- | --- | --- | --- |
| 1 | 2 (F1) | 2 | **2** (DERIVED-BY-HAND) |
| 2 | 2 | 3 (comb F3) | needs a run |
| 3 | 2 | 4 | needs a run |
| 4 | 2 | 5 | needs a run |
| 5 | 2 | 6 | needs a run |
| 6 | 2 | 7 | needs a run |

- At τ = 1 with no mismatches, every row is n + 1 [S-MTS-6] (partial).
- At τ = 2, the counter gains only for larger n. For n ≤ 6, the comb n + 1 is the best construction found (inference).
- Run needed (cluster only, never local):
  - Exhaustive search over τ = 2 directed systems with t ≤ n + 1 types for 2×n, n = 2..8.
  - Record the minimum t for each seed position (corner vs each interior cell).
  - Use the polynomial uniqueness check of [S-MTS-1] to test each candidate.
  - Output: a table of n, seed position, minimum t, and one witness tile set.

## 5. Candidate research directions (seed not at corner)

What changes when the seed is in column s, with 1 < s < n (inference):
- Growth runs both west and east. The two arms have lengths s − 1 and n − s.
- The F4 lower bound still holds, because [S-MTS-2] Thm 3.1 is seed-independent.
- Upper bound, DERIVED-BY-HAND: n + 1 (comb, F3). Also 4⌈√a⌉ + 4⌈√b⌉ + O(1) ≤ 4√2·√n + O(1) (two-arm counter, rank 5). It rests on the [S-MTS-2] p.8 length claim. [review_04 §2.7, F5]
- So the τ = 2 interior-seed answer is Θ(√n) (lower PROVEN, upper DERIVED). Only the exact value is open.
- Two separate one-sided counters cost about c√a + c√b with a + b = n − 1. That is larger than c√n, so splitting alone is worse than a corner seed.
- An interior seed can win only if the arms **share tile types**. West-growing and east-growing tiles can share a type only if its glues fit both directions (tiles do not rotate, §1). This is the crux.

Ranked directions for a 2-page paper in 24 h:

| Rank | Direction | Claim it could support | Risk |
| --- | --- | --- | --- |
| 1 | **Non-hardness by sparseness.** Holds for n in unary or a canonical sorted cell list (Θ(n log n) bits). Then each input length has O(n) values of k and O(n) seed cells s, so the language is sparse. Mahaney: a sparse NP-complete set implies P = NP [S-MTS-7]. Normalization note: a cell list in arbitrary order has (2n)! encodings of one shape, so the raw language is not sparse. Add the poly-time reduction "any encoding ↦ canonical ⟨1^n, s, k⟩, with k and s in unary (or fixed width ⌈log₂(2n + 2)⌉ bits), and every instance with k ≥ n + 1 mapped to one fixed yes-instance (the comb gives OPT ≤ n + 1)". Non-rectangles map to a fixed no-instance. A binary k is not sparse: n = 1 with any ℓ-bit k gives about 2^ℓ yes-instances of length ℓ. The canonical set is in NP at fixed τ. If the raw problem were NP-complete, the sparse canonical set would be too. [review_02 §7a, review_04 §2.6, F4] | "Min tile set for 2×n is not NP-complete unless P = NP" (any seed rule). A short, rigorous theorem. | Low. State the encoding. Fails for n in binary: the set is not sparse, and NP membership is unclear. NP membership needs τ fixed or strengths bounded. |
| 2 | **Subexponential algorithm.** At fixed τ = 2, enumerate all systems with ≤ 4⌈√n⌉ + 2 types (seed free or corner seed). That is 2^{O(√n log n)} candidates, each checked in polynomial time [S-MTS-1]. For a seed cell fixed by the input, search up to the two-arm bound 4⌈√a⌉ + 4⌈√b⌉ + O(1) (rank 5), not 4⌈√n⌉ + 2. That is still O(√n). [review_04 §2.8, F6] | "Solvable in 2^{O(√n log n)} time", only for fixed τ = 2 and unary or cell-list input. In binary, input length ℓ = log n, so this is not subexponential in ℓ. At τ = 1 the only upper bound is n + 1, so the same enumeration is 2^{O(n log n)}. [review_02 §7c] Pairs well with rank 1. | Low. Must fix τ, or cite [S-MTS-4] for bounding strengths. |
| 3 | **WLOG-corner lemma (exchange argument).** Show that any optimal interior-seed system converts to a corner-seed system with no more types. Then the general case equals the corner formula, which is polynomial. | Resolves the open case. | High. It may be false if the arms can share tiles. |
| 4 | **Seed-position decomposition.** Write OPT = min over s of f(s − 1, n − s), where f is the cost of two arms with sharing. If f has a closed form, this is an O(n)-time algorithm. | Polynomial algorithm, conditional on f. | Medium–high. |
| 5 | **Constant-factor approximation.** Seed free (part of the solution): output the corner construction of [S-MTS-2] (4⌈√n⌉ + 2, proven) against the √n / 2 lower bound. Ratio → about 8 (≤ about 11 for small n). The "7×" (3.46 / 0.5) uses the §4.3 counter, is asymptotic only, and covers only n = 1 + mD. Seed cell fixed by the input: two arms (lengths s − 1 and n − s), one counter growing west and its horizontal mirror growing east, sharing the seed column, disjoint glue labels. Types ≤ 4√2·√n + O(1), ratio → about 8√2 ≈ 11.3. Top-row seed cell: also flip vertically. [review_02 §7b, review_04 F7] | "About 8-approximation (seed free) by [S-MTS-2], 7 for n = 1 + mD by §4.3. About 8√2 for a fixed seed cell." | Low. The fixed-seed case relies on [S-MTS-2]'s counter handling any arm length 1..m² (paper claim, §3, not re-checked). |
| 6 | **Small-n exact table via a cluster run (§4.4).** Compare the corner optimum with the interior optimum for n ≤ 8. | Evidence for or against rank 3. | Needs a cluster run and the owner's OK. |
| 7 | **Hardness.** NP-hardness of 2×n is blocked by rank 1 under unary or canonical cell-list encoding. | Not recommended. | Very high. |

Realistic 24 h paper (inference): ranks 1 + 2 as theorems, rank 5 as a theorem (the 8× form needs only [S-MTS-2], the 7× form needs §4.3), rank 3 as a conjecture backed by rank 6 data.

## 6. Computation note

- Any brute-force search over tile sets is computation. `~/.claude/CLAUDE.md` "No local execution: cluster first" forbids running it on this machine.
- No code, simulation or search over tile sets was run for these notes. Only reading and web search were done.
- Runs needed (main session submits, cluster only):
  - R1: exhaustive minimum tile set search for 2×n, n = 2..8, τ = 1 and τ = 2, every seed position (§4.4).
  - R2 (optional, independent check): one aTAM simulation of the §4.3 counter for a few (m, D), to check directedness and the terminal shape. Hand traces exist (review_02 §5).

## 7. Sources

| ID | Citation | Supports | Verified |
| --- | --- | --- | --- |
| S-MTS-1 | Adleman, Cheng, Goel, Huang, Kempe, Moisset de Espanés, Rothemund. Combinatorial optimization problems in self-assembly. STOC 2002, pp. 23–32, doi 10.1145/509907.509913 | NP-complete in general, polynomial on trees and squares, polynomial verification | partial (abstract only, full text not reached) |
| S-MTS-2 | Aggarwal, Cheng, Goldwasser, Kao, Moisset de Espanés, Schweller. Complexities for generalized models of self-assembly. SIAM J. Comput. 2005 (prelim. SODA 2004, pp. 873–882) | definitions, Thm 3.1 lower bound, Thm 3.2 construction, corner seed | yes (full text pp. 1–8) |
| S-MTS-3 | Bryans, Chiniforooshan, Doty, Kari, Seki. The power of nondeterminism in self-assembly. SODA 2011, arXiv 1006.2897 | Σ2^P-completeness (strict), directed vs strict definitions | yes (pp. 1–5) |
| S-MTS-4 | Chen, Doty, Seki. Program size and temperature in self-assembly. arXiv 1011.3493 (journal: Algorithmica 2014, per search snippet) | τ = 2 condition of the square algorithm, any-τ squares polynomial, model definitions | yes (pp. 1–3); journal venue partial |
| S-MTS-5 | Furcy, Summers, Wendlandt. New bounds on the tile complexity of thin rectangles at temperature-1. arXiv 1808.04358 (2018, v2 2019) | τ = 1 bound Ω(N^{1/k}), best upper N + k − 1 | yes (ar5iv text, first 100k chars) |
| S-MTS-6 | Maňuch, Stacho, Stoll. Two lower bounds for self-assemblies at temperature 1. J. Comput. Biol. 17(6):841–852, 2010 (SAC 2009) | diameter + 1 bound under no-mismatch, 2N − 1 for squares | partial (search snippet) |
| S-MTS-7 | Mahaney. Sparse complete sets for NP: solution of a conjecture of Berman and Hartmanis. JCSS 1982, doi 10.1016/0022-0000(82)90002-2 | sparse NP-complete ⇒ P = NP | partial (Wikipedia + snippet) |
| S-MTS-8 | Improved lower and upper bounds on the tile complexity of uniquely self-assembling a thin rectangle non-cooperatively in 3D. arXiv 2007.11093 | 3D τ = 1 thin rectangles | UNVERIFIED (authors and bounds not read) |
| S-MTS-9 | Proving new directed tile complexity lower bounds at temperature 1 by folding between 2D and just-barely 3D self-assembly. ResearchGate 379409972 | possible tighter τ = 1 2D directed bound | UNVERIFIED (403) |
| S-MTS-10 | Chalk, Luchsinger, Schweller, Wylie (UTRGV paper), core.ac.uk/download/160477919.pdf | Schweller affiliated with UTRGV | partial (snippet) |
| S-MTS-11 | Rothemund, Winfree. The program-size complexity of self-assembled squares. STOC 2000 | Ω(log N / log log N) for squares | partial (cited in S-MTS-2, S-MTS-4). Title from memory: UNVERIFIED |
| S-MTS-12 | Adleman, Cheng, Goel, Huang. Running time and program size for self-assembled squares. STOC 2001 | matching O(log N / log log N) | partial (cited in S-MTS-3, S-MTS-4). Title from memory: UNVERIFIED |

URLs:
- [S-MTS-1] Combinatorial optimization problems in self-assembly | https://authors.library.caltech.edu/3141 | published: 2002 | accessed: 2026-11-07 | type: paper | note: abstract only
- [S-MTS-2] Complexities for generalized models of self-assembly | https://users.cs.northwestern.edu/~schwellerr/papers/CGM_siam.pdf | published: 2005 | accessed: 2026-11-07 | type: paper | note: full text pp. 1–8
- [S-MTS-3] The power of nondeterminism in self-assembly | https://arxiv.org/abs/1006.2897 | published: 2010-11-25 v3 | accessed: 2026-11-07 | type: paper | note: pp. 1–5
- [S-MTS-4] Program size and temperature in self-assembly | https://arxiv.org/abs/1011.3493 | published: 2011-03-02 v2 | accessed: 2026-11-07 | type: paper | note: pp. 1–3 of web.cs.ucdavis.edu/~doty/papers/ptsa.pdf
- [S-MTS-5] New bounds on the tile complexity of thin rectangles at temperature-1 | https://arxiv.org/abs/1808.04358 | published: 2019-06-14 v2 | accessed: 2026-11-07 | type: paper | note: ar5iv HTML
- [S-MTS-6] Two lower bounds for self-assemblies at temperature 1 | https://journals.sagepub.com/doi/pdf/10.1089/cmb.2009.0067 | published: 2010 | accessed: 2026-11-07 | type: paper | note: search snippet
- [S-MTS-7] Mahaney's theorem | https://en.wikipedia.org/wiki/Mahaney%27s_theorem | published: 1982 (paper) | accessed: 2026-11-07 | type: aggregator | note: snippet
- [S-MTS-8] Improved bounds, thin rectangle, 3D | https://arxiv.org/abs/2007.11093 | published: 2020 | accessed: 2026-11-07 | type: paper | note: snippet only
- [S-MTS-9] Folding between 2D and just-barely 3D | https://www.researchgate.net/publication/379409972 | published: UNVERIFIED | accessed: 2026-11-07 | type: paper | note: 403
- [S-MTS-10] UTRGV Schweller paper | https://core.ac.uk/download/160477919.pdf | published: UNVERIFIED | accessed: 2026-11-07 | type: paper | note: snippet
- [S-MTS-11], [S-MTS-12]: no URL fetched, cited through S-MTS-2/3/4.

Selection log (rejected):
- "Self-assemblying classes of shapes with a minimum number of tiles" (ResearchGate 221583734): not read, and its model may differ. Rejected: not verified.
- "Toward minimum size self-assembled counters" (Springer 10.1007/s11047-008-9070-3): relevant to counters, not read. Rejected: not verified. Worth reading next.
- "Size-dependent tile self-assembly: constant-height rectangles" (arXiv 1509.06898): uses a size-dependent temperature, which is a different model. Rejected: out of the standard model.

open_questions:
- Setter's model: fixed τ = 2, τ = 1, or τ chosen by the solver? Directed or strict? Shape as a cell list (unary n) or n in binary? Rank 1 in §5 depends on the encoding.
- Is "Dr. Schwaller" Robert Schweller (UTRGV)? Inference only.
- S-MTS-1 full text: conditions (τ, seed) of the tree and square algorithms. UNVERIFIED.
- S-MTS-6 definition of Manhattan diameter, and whether the n + 1 τ = 1 result really follows. Partial.
- S-MTS-8, S-MTS-9 authors and bounds. UNVERIFIED.
- S-MTS-11, S-MTS-12 exact titles. UNVERIFIED.
- Furcy–Micka–Summers 3D squares paper: not searched. UNVERIFIED.
- §4.3 counter construction: hand-traced for (m, D) = (3, 2) and (12, 4) in review_02, not simulated. R2 is optional.
- Exact τ = 1 value without the no-mismatch assumption: open as far as found (§4.2).
- Exact small-n values (n = 2..6) and the corner-seed "equation": needs run R1. Not found in literature.
