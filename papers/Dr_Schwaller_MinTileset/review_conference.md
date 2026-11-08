# PC Review: "The Minimum Tileset Problem for 2×n Rectangles"

Venue chosen: DNA Computing and Molecular Programming (DNA 32), short-paper track.
Reviewer basis: `main.tex` source (287 lines after the latest update, not compiled), the problem statement, and the tips-folder notes and math reviews.
Line numbers below refer to the current 287-line `main.tex`.
The binary-k fix has landed (l.69–70, l.223–224, l.236–238). It is resolved and is not a finding here.
Confidence caveat: source-only review, no compile, no access to the cited papers beyond the authors' notes.

## 1. Summary

- The paper studies the directed Minimum Tileset Problem (MTS) for a 2×n rectangle in the abstract Tile Assembly Model (aTAM).
- Bounds: t ≥ √n/2 at every τ and seed cell (cited, ACG05 Thm 3.1), a comb with n+1 types for every seed cell, the ACG05 corner counter 4⌈√n⌉+2 at τ=2, a new "leaner" counter with m+3D+2 ≈ 3.46√n types for n = 1+mD (hand-traced), and a sketched two-arm bound 4√2·√n+O(1) for an interior seed.
- Complexity: with n in unary (or a cell list) and τ fixed, the decision version is not NP-complete unless P = NP, by a sparse-set argument and Mahaney's theorem.
- Algorithms: a 2^{O(√n log n)} exact search at τ=2 and a ratio-about-8 approximation from the corner counter.
- The exact corner formula the setter mentions, the exact interior-seed value, and the exact τ=1 value are left open.

## 2. Scores

| Item | Score | Justification |
| --- | --- | --- |
| Overall | **Reject (as submitted)**. In the hackathon context, weak accept is reachable after Section 7.1 items 1–8 (DNA 32 itself has no such track) | Correct but mostly known or folklore content, with several overclaims and one false numeric sentence |
| Novelty | 1.5 / 5 | Only the leaner counter (a constant-factor gain on one residue class of n) is new. The rest is ACG05, FSW19, or standard |
| Technical soundness | 3 / 5 | No fatal math error found. One false claim (approximation ratio "below about 11"), several status labels inconsistent, one construction not checkable from the text |
| Significance | 2 / 5 | Does not resolve the setter's question (membership in P, the corner formula). The non-NP-hardness is generic to any unary-size problem |
| Clarity | 2.5 / 5 | Honest status labels are a plus. One-sentence-per-line prose, "read only in part" disclaimers, undefined glue names and an undefined problem variant hurt |
| Confidence | 3.5 / 5 | Familiar with aTAM thin-rectangle results and sparse-set arguments. Limited by not reading ACG05 or Mahaney directly and not compiling |

## 3. Does it answer the question asked?

**Short answer: partly. The paper bounds the optimum, but it does not answer "what is the complexity" crisply, and its headline complexity result is folklore.**

### 3.1 What the setter asked

- Input: a shape. Output: the minimum number of tile types (problem file).
- Question: the complexity when the shape is 2×n.
- Setter's hint: a corner seed seems to admit an "equation", hence a polynomial algorithm. Without the corner assumption, it is open.
- So the target is membership in P (an exact formula or a poly(n) algorithm), or hardness. The order Θ(√n) is already in ACG05 for k = 2.

### 3.2 The crisp answer the paper can honestly give today

1. Natural encoding: a shape is a cell list, so the input size is Θ(n) up to log factors. Unary n is the natural encoding, not a technicality. The paper should say this.
2. Under that encoding and fixed τ, the problem is in NP and is not NP-hard under many-one reductions unless P = NP.
3. An exact algorithm runs in 2^{O(√n log n)}, i.e. subexponential in the input size.
4. Membership in P is open, for the corner seed as well. The setter's formula was not found.
5. OPT = Θ(√n) at τ=2 for a corner seed (proved, ACG05) and for a free seed (proved, see 3.4). For a prescribed interior seed the upper bound is currently a sketch.

The paper contains items 2–5, but scattered. The abstract (l.37–42) leads with bounds, not with this answer.

### 3.3 Is the Mahaney result the right headline, and is it scoped correctly?

- **Correct, but folklore.** Any problem whose instances are determined by O(1) integers bounded polynomially in the input length is sparse, in fact essentially tally. A PC member will say "this holds for every unary problem and says nothing about P".
- Berman (1978) already gives the tally version: a tally NP-hard set implies P = NP. That is older and simpler than Mahaney (1982). Encoding ⟨n, s, k⟩ as 1^{π(n,s,k)} with a polynomial pairing π makes the canonical language tally.
- **Scope of the statement (l.222–227).** "Not NP-complete" is weaker than what the proof shows. The proof (l.234) uses NP-hardness only. State "not NP-hard under polynomial-time many-one reductions unless P = NP". Mahaney's theorem holds for sparse NP-hard sets, so NP membership is not needed for the theorem.
- **NP membership (l.239).** The sentence "NP membership needs a fixed τ, since a certificate is a tile set of at most n+1 types" gives the wrong reason. A certificate with ≤ n+1 types, O(n) labels and strengths ≤ τ has size poly(n, log τ) even for binary τ. Verification is polynomial (Adleman et al. 2002 uniqueness check, not in the bibliography). Fixed τ is needed for **sparseness**, not for NP membership: with τ in binary, (n, s, k, τ) gives exponentially many strings per length.
- **Sparseness itself is established.** With s ≤ 2n, k ≤ n+1 after the k ≥ n+1 collapse, and unary n, a length-L slice has O(L²) strings. Correct.
- **Turing reductions.** Mahaney covers many-one reductions. Say so in one clause.

### 3.4 Free seed versus prescribed seed: a missing distinction that helps the paper

- The setter's "without this assumption" most likely means the designer may put the seed anywhere (free seed). The paper treats "interior seed" as a seed cell fixed by the input (l.200, l.249).
- For a free seed, OPT_free(n) = min over seed cells of OPT(n, s) ≤ OPT_corner(n) ≤ 4⌈√n⌉+2. With the seed-independent lower bound, **Θ(√n) for a free seed is proved, not sketched.**
- The paper should define three variants (corner, free, prescribed s) and report each. This turns the setter's "open" case into a proved Θ(√n) row.

### 3.5 Is the 2^{O(√n log n)} algorithm stated carefully?

- Mostly. τ=2, unary or cell-list input, and the binary-n caveat are all stated (l.242, l.250).
- Gap: for a prescribed interior seed the time bound rests on Proposition 2 (l.200), a sketch. The sketch status must propagate to Proposition 3 for that variant.
- Cleaner proof: enumerate t = 1, 2, … until a directed system is found. Correctness then needs no upper bound. Time is 2^{O(OPT log OPT)}·poly(n). Any O(√n) bound on OPT gives the stated time. This removes the dependency on "search up to the bound" (l.249).
- Enumeration should include the choice of seed type and, for the free variant, the 2n seed cells. Both are poly factors.

### 3.6 What would make the complexity part non-trivial

| Result | Effort | Effect on the verdict |
| --- | --- | --- |
| Poly(n) algorithm, or an exact formula, for the corner seed | research, not doable by the deadline | answers the question; accept |
| Pseudo-polynomial algorithm in unary n for prescribed s | same as above (it is the same question) | answers the question |
| Exact small-n table (R1) plus a conjectured formula matching the setter's "equation" | cluster run | strong evidence; moves to weak accept |
| Hardness of a nearby variant (τ or the strength function in the input, or k×n with k in the input) | research | non-trivial complexity content |
| Reframe the Mahaney point as a one-line remark with Berman/Mahaney cited, and state the poly-vs-subexponential gap as the open problem | edit, now | removes the "trivial headline" objection |

## 4. Technical soundness, claim by claim

| # | Claim (line) | Label in paper | Verdict | Issue |
| --- | --- | --- | --- | --- |
| 1 | Abstract: Θ(√n) "for every seed position" at τ=2 (l.37) | stated as fact | **Overclaimed** | l.38 and Prop. 2 call the interior upper bound a sketch. True as proved only for corner and free seed |
| 2 | Thm 1: 2×1 needs exactly 2 types (l.108–118) | proved | Correct, terse | Covers only the second tile above the seed. Add "below" by symmetry. One-type argument gives t ≥ 2 for every n ≥ 1; say so (used in item 9) |
| 3 | Thm 2: comb, n+1 types, every seed cell, every τ (l.120–137) | proved | Correct | Known: FSW19 state the N+k−1 comb (authors' notes l.112). Present as known, restated for every seed cell. The top-row flip is the only addition |
| 4 | Thm 3: t ≥ √n/2 at every τ, any seed (l.158–163) | cited, ACG05 Thm 3.1 | **Mis-attributed in part** | ACG05 fix the seed at (0,0) (notes l.34). Seed independence is the authors' adaptation. For an interior seed one side has ≥ (n−1)/2 columns, giving about (√n−1)/2 (review_06 §2.4), not a clean √n/2. ACG05's own count on the longer side gives only √((n−1)/8); the √n/2 − O(1) form needs the authors' finer movie count. See §7.1 item 7 for the two options. The proof description "three identically placed columns" (l.163) is not confirmed by the notes; check against ACG05 or drop it |
| 5 | Corner counter 4⌈√n⌉+2 (l.89, l.165) | proved, cited | Correct use of ACG05 Thm 3.2 | 4m+k with k = 2, m = ⌈√n⌉. Arbitrary n relies on ACG05 p.8 (start value m^k − N). Same dependency as item 7 |
| 6 | Leaner counter, m+3D+2 types for n = 1+mD (l.172–196) | construction, hand-traced | **Plausible, not checkable from the text** | Glues q, s, g, b and tiles Z, Y are used but never defined. The steps work only if P_1 has north s, P_2…P_{m−1} have north g, P_m has north b and west q (strength 1), and Z has west q. l.177 ("strength 1 would deadlock P_{j+1}") is unclear. Our hand check of (m, D) = (3, 2) agrees with review_06 §4. The determinism argument is a 5-case local check that generalizes to all m ≥ 2, D ≥ 1. It can be a proved Proposition now |
| 7 | Prop. 2: interior seed ≤ 4⌈√a⌉+4⌈√b⌉+O(1) ≤ 4√2·√n+O(1) (l.200–208) | sketch | **Under-claimed** | The math is correct (review_06 §2.3: mirror arm, disjoint labels, constant seed column, Cauchy–Schwarz). It depends on the same ACG05 p.8 claim as item 5, which the paper calls "proved". Make the labels consistent: upgrade to a proved proposition with a 4-line proof |
| 8 | τ=1, no mismatches: exactly n+1 (l.96, l.211–214) | "source read only in part" | **Overclaimed** | Source (Maňuch, Stacho, Stoll) is snippet-only, not in the bibliography, and "Manhattan diameter" is undefined. "exact" in the table should be "conditional, cited" or the row cut |
| 9 | Prop. 3 approximation: ratio "tends to about 8 and stays below about 11 for small n" (l.251–252) | sketch | **False as stated** | Against √n/2: n = 1 gives 6/0.5 = 12. n = 2 gives 10/0.71 = 14.1. n = 5 gives 14/1.12 = 12.5. n = 10 gives 18/1.58 = 11.4. Fix: use the lower bound max(2, √n/2) (item 2). The ratio is then at most about 10.7, at n = 17 (22/2.06). Or state the asymptotic bound 8 + 12/√n, from 4⌈√n⌉+2 ≤ 4√n+6 |
| 10 | Prop. 3 exact algorithm 2^{O(√n log n)} (l.241–250) | sketch | Correct for corner and free seed | Prescribed interior seed inherits item 7's status. Polynomial uniqueness check is cited only in a comment (l.248). See §3.5 |
| 11 | Thm 4: not NP-complete unless P = NP (l.222–235) | proved | Correct, folklore | Mahaney (JCSS 1982) not in the bibliography (comment l.235). Statement weaker than the proof (NP-hard suffices). See §3.3 |
| 12 | NP membership "needs a fixed τ" (l.239) | remark | **Wrong reason** | See §3.3. Fixed τ is needed for sparseness only |
| 13 | Intro: general MTS NP-complete; squares polynomial at τ=2 and at every τ (l.48–52) | footnote: "read only in abstract form" | Claims fine, citation missing | Adleman et al. STOC 2002 must be in the bibliography. "At every temperature" should say whether τ is fixed or part of the input (CDS11) |
| 14 | 3.46√n "against 4√n+2 in ACG05" (l.191) | construction | Fair only with scope | ACG05 covers every n. The leaner counter covers one residue class n ≡ 1 (mod m). At n = 49 the true comparison is 26 versus 30 (ACG05), not 26 versus 50 (comb, l.193) |

### Citation check: Aggarwal et al. 2005

- Thm 3.1 (lower bound): used correctly for the corner seed. The constant comes from the proof ((N/(2·k!))^{1/k}, notes l.69), not the theorem statement (Ω(N^{1/k}/k)). Say "from the proof of Thm 3.1".
- Thm 3.2 (upper bound): used correctly. Cite p.8 for the length control.
- Missing: volume and pages (SIAM J. Comput. 34(6), 2005, per our recollection; the authors should verify).

### Extension the authors can add for free

- Every τ=2 construction works at any τ ≥ 2. Map strength 1 to ⌈τ/2⌉ and strength 2 to τ. A sum of original strengths is ≥ 2 exactly when the scaled sum is ≥ τ, because one ⌈τ/2⌉ is < τ for τ ≥ 2. So the corner, free-seed and leaner-counter rows hold for every τ ≥ 2 (reviewer's hand argument; authors should re-check).

## 5. Novelty versus prior work

| Item | Prior work | New here? |
| --- | --- | --- |
| Θ(√n) at τ=2, corner seed | ACG05 Thm 3.1, 3.2 with k = 2 | No |
| Ω(√n) and n+1 at τ=1 | FSW19 | No |
| Comb, n+1 types | FSW19 (N+k−1 comb) | No. Seed-anywhere and top-row flip are routine |
| 2×1 needs 2 types | trivial | No |
| Seed-independent lower bound | ACG05 proof idea, adapted | Minor adaptation, should be stated as such |
| Free-seed Θ(√n) | follows from ACG05 | Not claimed; should be (observation) |
| Two-arm interior bound 4√2·√n | composition of ACG05 counters | Minor, straightforward |
| Leaner counter m+3D+2 ≈ 3.46√n | none found by the authors | **Yes**, a constant improvement 4 → 2√3 on n = 1+mD. Not compared with any later thin-rectangle optimizations; a PC member may know one |
| Non-NP-hardness (sparse/tally) | Berman 1978, Mahaney 1982; folklore for unary problems | No, as a technique. New only as an explicit statement for this problem |
| 2^{O(√n log n)} exact search | same brute force as Adleman et al. for squares | No, as a technique |

- Net: the contribution is a clean **survey-plus-synthesis** of the 2×n case with one small new construction.
- That fits a hackathon. At DNA or SODA it would need either the exact corner formula or a poly-time algorithm.

## 6. Weaknesses, ranked

| Rank | Weakness | Fatal? | Fixable by 11/8 09:00? |
| --- | --- | --- | --- |
| 1 | Does not answer membership in P, and does not find the setter's corner formula | Fatal at a real venue. Not fatal for a hackathon if framed honestly | Framing: yes. Formula: no (needs R1 data and an idea) |
| 2 | Headline complexity result is folklore and stated weaker than proved (not NP-complete vs not NP-hard); key citations (Mahaney, Berman, Adleman et al.) missing | Serious: setter and faculty will spot it | Yes, edit only |
| 3 | Abstract overclaims Θ(√n) "for every seed position"; free-seed vs prescribed-seed variants undefined | Serious | Yes, edit only |
| 4 | False sentence: approximation ratio "below about 11 for small n" | Serious (a checkable false number) | Yes, edit only |
| 5 | Only new construction (leaner counter) cannot be verified from the text: undefined glues, unclear l.177 | Serious for the novelty case | Yes: glue table plus 5-case lemma |
| 6 | Inconsistent status labels: corner "proved" and interior "sketch" share the same ACG05 p.8 dependency; lower bound attributed to ACG05 "wherever the seed lies" | Moderate | Yes |
| 7 | τ=1 "exact" row rests on a snippet-only, uncited source | Moderate | Yes: demote or cut |
| 8 | Wrong reason given for NP membership (l.239) | Minor | Yes |
| 9 | Placeholder authors, "read only in abstract form/in part" disclaimers, TODO comments, arXiv-only bib entries | Minor but looks unfinished | Yes |
| 10 | Probable 2-page overflow; prose style (one sentence per line, "Why:" captions) unusual for theory | Minor | Yes, cut list in §8 |

## 7. Required changes to pass

### 7.1 Edits doable now (no computation), in priority order

1. **Rewrite the abstract around the answer (l.36–42).** Replacement:
   > We study the directed Minimum Tileset Problem for $2\times n$ rectangles in the aTAM, for a corner seed, a free seed, and a prescribed seed cell.
   > At every $\tau\ge2$ the optimum is $\Theta(\sqrt n)$ for a corner or free seed; for a prescribed interior cell we give $4\sqrt2\sqrt n+O(1)$.
   > We give a new counter with $m+3D+2\approx2\sqrt3\sqrt n$ types for $n=1+mD$, improving the constant 4 of Aggarwal et al.
   > Under the natural encoding (a cell list, so $n$ is unary), the problem is in NP, is not NP-hard unless P $=$ NP, and is solvable exactly in time $2^{O(\sqrt n\log n)}$.
   > Whether it is in P, as an exact corner formula would imply, remains open.
2. **Define the three variants in the Model paragraph (after l.67).** Replacement:
   > We write $t_\tau(n,s)$ for a seed at cell $s$, $t^{\mathrm{corner}}_\tau(n)=t_\tau(n,(1,1))$, and $t^{\mathrm{free}}_\tau(n)=\min_s t_\tau(n,s)\le t^{\mathrm{corner}}_\tau(n)$. The input is the cell list of the shape, so its size is $\Theta(n\log n)$ bits.
   Add a free-seed row to Table 1: lower √n/2 − O(1), upper 4⌈√n⌉+2, "proved (from ACG05)".
3. **Restate Thm 4 as a remark-strength observation, stronger form (l.222–239).** Replacement statement:
   > Observation. Fix $\tau$. Under the cell-list (or unary) encoding, deciding $t_\tau(n,s)\le k$ is in NP and is not NP-hard under many-one reductions unless P $=$ NP.
   Proof: keep l.229–233. Replace "sparse ... Mahaney" with: "Pairing $(n,s,k)$ into $1^{\pi(n,s,k)}$ gives a tally set, so Berman's theorem [Ber78] (or Mahaney's [Mah82]) applies." Add: "This holds for any problem whose instances are a polynomially bounded number; the real question is membership in P." Replace l.239 with: "NP membership holds for any $\tau$: a certificate has $\le n+1$ types and strengths $\le\tau$, and uniqueness is checked in polynomial time [ACGHKMR02]. Fixing $\tau$ is needed only for sparseness."
4. **Fix the approximation sentence (l.251–252).** Replacement:
   > Every shape with two or more cells needs $t\ge2$ (the one-type argument of Theorem 1). Against $\max(2,\sqrt n/2)$ the corner counter has ratio at most about 10.7 (worst at $n=17$), and $8+12/\sqrt n$ in general.
   This uses √n/2 as the lower bound. For a corner seed that is ACG05. For a free seed it needs option (b) of item 7; under option (a) the free-seed ratio is about 8√2.
5. **Make the leaner counter checkable, and promote it (l.172–196).** Add a 6-row glue table: tiles Z, Y, P_1, P_j (1<j<m), P_m, S_d, M_d, X_d; columns N, E, S, W with strengths. Required values: P_1.N = s, P_j.N = g, P_m.N = b, P_m.W = q (1), Z.W = q (1), Y.W = r_{D−1} (2), X_0.W = null. State it as Proposition (counter): "For $m\ge2$, $D\ge1$ and $n=1+mD$, the system is directed at $\tau=2$." Proof: one line per step of the 5-step cycle, showing exactly one tile type fits each new cell (the case list of review_06 §4 generalizes). Replace l.177 with "Chain glues have strength 2, so $P_{j+1}$ attaches without a tile above it." Replace l.193 comparison by "26 types against 30 for ACG05 and 50 for the comb". Replace l.191's comparison with "for these $n$" scope.
6. **Upgrade Prop. 2 to a proved proposition and align labels (l.200–208, Table rows l.89–94).** Proof in 4 lines: west arm = ACG05 counter of length a; east arm = its mirror with fresh labels; the seed column carries both W and E arm glues; no cross-attachment because arm labels are disjoint. Cite ACG05 p.8 for arbitrary arm length in both the corner and interior rows. Same status in both rows.
7. **Fix the lower-bound attribution (l.158–163).** Replacement statement:
   Pick one of two options. Do not attribute √n/2 − O(1) for an interior seed to ACG05: their count (2·k!·t^k = 4t² states) applied to the longer side only gives √((n−1)/8).
   - (a) Cite ACG05 only:
     > Theorem 3 (from the proof of [ACG05, Thm 3.1]). For a corner seed, $t\ge\sqrt n/2$. For any seed cell, the longer side has $\ge(n-1)/2$ columns, so $t\ge\sqrt{(n-1)/8}$.
     Then the free-seed and interior ratios in item 4 become about $8\sqrt2\approx11.3$ asymptotically.
   - (b) Keep $t\ge\sqrt n/2-O(1)$ for any seed as the authors' own Lemma, with the window-movie count $\le2t(t+1)$ proved in the paper (4 lines, review_06 §2.4). Then item 4 stands as written.
   Drop the "three identically placed columns" sentence unless checked against ACG05.
8. **Restructure Prop. 3 (l.241–250).** Replacement sketch:
   > Try $t=2,3,\dots$; for each $t$ enumerate the $t^{O(t)}$ systems with strengths $\le2$, every seed type, and (free seed) every seed cell, and test each in polynomial time [ACGHKMR02]. The first success is optimal, so the time is $2^{O(\mathrm{OPT}\log\mathrm{OPT})}\mathrm{poly}(n)$, which is $2^{O(\sqrt n\log n)}$ by Table 1.
   For a prescribed interior seed this uses item 6.
9. **τ=1 row (l.96, l.211–214).** Either cite Maňuch–Stacho–Stoll properly (verify venue: likely J. Comput. Biol. 2010) and define Manhattan diameter in one clause, with the label "conditional on no mismatches, cited", or cut the row and the paragraph to save space.
10. **Add the τ ≥ 2 scaling remark** (§4 "Extension"), one sentence. It upgrades every τ=2 row to τ ≥ 2.
11. **Bibliography.** Add Adleman, Cheng, Goel, Huang, Kempe, Moisset de Espanés, Rothemund, "Combinatorial optimization problems in self-assembly", STOC 2002. Add Mahaney, "Sparse complete sets for NP: solution of a conjecture of Berman and Hartmanis", JCSS 25(2), 1982. Add Berman, "Relationship between density and deterministic complexity of NP-complete languages", ICALP 1978. Give journal versions for CDS11 and FSW19 if they exist. Verify every title before submission; the reviewer did not open these sources.
12. **Clean-up.** Real author names (l.17–28). Remove "which we read only in abstract form" (l.48) and "a source we read only in part" (l.96, l.214) by citing properly. Remove `% TODO` comments.
13. **Open problems (l.257–265).** Lead with: "Is $t^{\mathrm{corner}}_2(n)$ computable in time poly$(n)$, and does it have a closed form? The gap is between $2^{O(\sqrt n\log n)}$ and poly$(n)$." Keep interior and τ=1 as items 2–3.

### 7.2 Changes that need a run (cluster only, main session submits)

| Run | What | Why it matters | Fits before deadline? |
| --- | --- | --- | --- |
| R1 | Exact t_2(n, s) for small n (n ≤ 6–8), corner, free and every s, by SAT or pruned search | Gives anchor values and a candidate corner formula, the setter's actual question. Strongest single upgrade | Only if a SAT encoding already exists; otherwise after the deadline |
| R2 | Simulate the leaner counter for many (m, D) and the two-arm construction for several (a, b) | Turns "hand-traced" into "verified by simulation" for the paper's only new construction | Yes, if a simulator is at hand; small runs |
| R3 | Simulate the ACG05 counter for all lengths 1..m² for small m | Confirms the p.8 dependency shared by the corner and interior rows | Yes, small |

- Without R1 the honest status of the corner formula is "not found". Do not guess one.
- n = 2 anchor, hand only: the comb gives 3, Theorem 1's argument gives ≥ 2, so t(2) ∈ {2, 3}. Closing it needs a case analysis the authors must verify themselves; the reviewer did not.

## 8. Presentation

| Element | Problem | Fix |
| --- | --- | --- |
| Title (l.14) | Neutral; does not signal a complexity result | "On the Complexity of the Minimum Tileset Problem for 2×n Rectangles" |
| Abstract (l.36–42) | Leads with bounds; l.38 opens with a weakness; overclaim in l.37 | §7.1 item 1 |
| Results table (l.77–103) | 4 columns, p-widths sum to ~15.2 cm plus padding, likely too wide for the class; no free-seed row; mixed statuses ("from a source we read only in part") | Three columns (Variant, Bounds, Status); add free-seed row; one status vocabulary: proved / cited / construction / sketch / conditional |
| Figure 1 (comb, l.139–154) | Low information; the comb is known and easy | Replace with the leaner-counter glue table, or a one-block trace for (m, D) = (3, 2) |
| Captions | "Why:" second sentences are house style, unusual at DNA/SODA | Plain one-sentence captions |
| 2-page budget | Likely over: table, figure, 4 theorems, 2 propositions, 3 open problems, AI statement, bibliography of 4 growing to 7 | Cut list below |
| Prose | One sentence per line reads as a list; theory readers expect paragraphs | Merge into short paragraphs in the final pass |
| Notation | t defined without τ and seed in the symbol (l.67); s used as a cell index and as a glue name (l.184); D also a common symbol for diameter | t_τ(n, s); rename glue s to σ or y |
| Missing definitions | Free vs prescribed seed; producible and terminal assembly; strength function range; input encoding as a cell list; Manhattan diameter; glues q, s, g, b, tiles Z, Y | One sentence each in the Model paragraph, or the glue table |
| Directed vs strict | Defined (l.65) and contrasted (l.53). Good. Add one clause that the result is about directed only |
| τ | "Fix τ" in Thm 4 vs "at every τ" in Thm 3 vs τ=2 constructions | State once: constructions at τ=2 extend to τ ≥ 2 (scaling remark); complexity at fixed τ |
| AI statement (l.270–272) | "hand-checked" by an AI assistant reads oddly | "The authors checked the constructions by hand; no simulation was run" (only if the authors did) |

Budget note: §7.1 adds a glue table, a free-seed row, three bibliography entries and two short proofs. That is feasible only if cut-list items 1–3 are applied. If they are not, §7.1 item 9 (cut the τ=1 row) is mandatory.

Cut list to fit 2 pages, in order:
1. Comb figure (save about 1/8 page). Replace with the glue table only if space allows.
2. Theorem 1 becomes one sentence inside the comb paragraph ("t ≥ 2 for n ≥ 1, and the comb is optimal at n = 1").
3. τ=1 paragraph shrinks to one sentence with the FSW19 bounds; drop the MSS row unless properly cited.
4. Comb proof shortened to 3 sentences; cite FSW19.

## 9. Questions to the authors

1. What does the setter mean by "without this assumption": seed placed by the designer (free) or seed cell given in the input? Your results differ between the two.
2. Can you prove or refute t^corner_2(n) = t^free_2(n)? An interior seed might halve the arm length.
3. Is τ part of the input? If yes, does your non-NP-hardness survive, given that binary τ breaks sparseness?
4. Did you check the "three identically placed columns" description and the seed-independence against ACG05 itself?
5. What are the exact values of t_2(n) for n = 2, 3, 4? Even these would anchor a conjectured formula.
6. Can the top row of the leaner counter use 2 types per digit instead of 3 (merging S_d and M_d)? That would give 2√2·√n.
7. Does the leaner counter extend to every n with a partial first block, and at what cost in types?
8. Is there any known thin-rectangle construction with a constant below 4 for k = 2 that you compare against?
9. Is the problem in P for every fixed seed rule if one only asks for OPT up to an additive O(1)? (This would be a meaningful partial answer.)
10. Who verified the constructions: the authors, or only the AI assistant? The AI statement should say.
