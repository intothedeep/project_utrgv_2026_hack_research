# 논문 리뷰: The Smallest Circle Touching Three Lines in 3D

- 대상: `papers/Wylie_SmallestCircle/main.tex` (2026-11-08 빌드)
- 심사 기준: 계산기하 학회(SoCG/ESA 수준) 심사 양식. 해커톤 2쪽 제출물.
- 검토자: reviewer agent. 논문은 고치지 않았다. 보고만 한다.
- 문체 기준: `.claude/rules/writing/paper.md`, `style.md`, `latex.md`.

## 0. 빌드 결과

| 항목 | 값 |
| --- | --- |
| 명령 | `latexmk -C` 뒤 `latexmk -xelatex main.tex` (`.latexmkrc`: `$pdf_mode = 5`) |
| 쪽 수 | 2 (stand-in `hackr26.cls`, article 10pt, 1in 여백. 실제 양식에서는 다를 수 있다) |
| 오류 | 0 |
| Overfull hbox | 3건, 모두 `main.tex` 210행(표 `tabularx`): 2.2 pt, 6.0 pt, 8.4 pt. Status 열("unchecked", "quadratic")이 열 폭 0.95 cm를 넘친다 |
| 산출물 | `papers/Wylie_SmallestCircle/main.pdf` (같은 폴더) |
| 2쪽 여백 | 참고문헌 아래 약 15 % 비어 있다. 10줄 정도 더 쓸 수 있다 |

## 1. 요약 (Summary)

논문은 세 직선에 닿는(intersect) 최소 원이 "세 직선을 모두 만나는 최소 공(ball)의 대원(great circle)"이라고 주장한다(Theorem 1).
그 공의 반지름 r* = min_c max_i dist_i(c)는 볼록 최소화 문제다. KKT 조건으로 활성(active) 직선이 2개 또는 3개임을 보이고, 각 경우에 대원이 존재함을 보인다.
2활성 경우는 "최대 ρ 쌍 하나만 검사"하는 O(1) 판정기(dispatcher)로 닫힌 형태를 준다.
문제의 Figure 1 16경우를 12행 표로 정리하고, 3활성 일반 경우(모두 꼬인 직선 등)는 열린 문제로 남긴다. SOCP 비교 검증은 자리표시자 상태다.

## 2. 강점 (Strengths)

- Theorem 1(원 → 공 환원)은 짧고 옳다. Lemma 1(하한)과 Lemma 2(도달)의 논리를 손으로 따라가 확인했다(§4).
- 판정기는 옳다. "최대 ρ 쌍이 통과하지 못하면 3활성"이라는 주장도 참이다(증명은 빠져 있다, §4.4).
- 열린 경우를 숨기지 않고 "open", "mixed", "sketch"로 표시한다. Bézout 한계 24 → 12도 맞다.
- 닫힌 형태 10/16 경우를 손 계산으로 확인했고(§4.5), 저장된 검증 결과(`summary.json`)와도 일치한다.
- 4직선 반례(정사면체 꼭짓점의 접선)는 옳고, 향후 과제가 분명하다.
- 그림 1(b)는 "평면이 직선에 수직일 필요가 없다"는 핵심을 잘 보인다.

## 3. 약점 (Weaknesses), 심각도 순

치명(fatal)은 없다. 주요(major) 4건, 경미(minor) 10건.

| # | 심각도 | 위치 | 문제 | 왜 중요한가 | 2쪽 안에 맞는 수정 |
| --- | --- | --- | --- | --- | --- |
| W1 | major | 초록 45~46행, 서론 51~52행 | "the case analysis reduces to an O(1) test", "closed forms for the problem's Figure 1 cases"라고 쓴다. 표는 12행 중 5행이 mixed/sketch/partial이고 3활성 일반 경우는 열려 있다. 16경우 중 닫힌 것은 10개다 | 심사자는 초록으로 기여를 판단한다. 표와 다르면 과장(overclaim)으로 읽고 점수를 깎는다 | 초록 한 문장: "Closed forms for 10 of the 16 cases; for the other 6 the two-active subcase is closed and the three-active subcase is open." O(1) test는 "decides whether two or three lines are active"로 고친다 |
| W2 | major | Dispatcher 149~155행 | "Take the largest ρ_ij ... Otherwise three are active"가 주장만 있고 증명이 없다. 논문의 알고리즘 기여 전체가 이 한 줄에 걸린다 | 반례가 있으면 표의 "2 or 3" 행이 모두 틀린다. 참이지만 독자는 알 수 없다 | 세 줄 보조정리(§4.4에 증명을 적었다). 동률(tie)이면 최대 쌍을 모두 검사한다는 한 구절도 더한다 |
| W3 | major | Lemma 2 증명 82~83행 | "Optimality gives Σλ_i u_i = 0"에서 (a) 비활성 직선의 λ_i = 0(상보 여유)을 말하지 않고, (b) u_i가 단위벡터인 것은 활성 직선뿐인데 "at least two active"가 단위성을 쓴다. (c) 어떤 최적성 정리인지 이름이 없다 | 증명의 핵심 단계가 독자에게는 비약으로 보인다 | 한 구절: "By the subdifferential of a max of convex functions, 0 ∈ conv{u_i : dist_i(c*) = r*}; these u_i are unit vectors, so at least two are active." |
| W4 | major | §4 검증 222~225행, 표 193행 | `\todo` 상자 3개가 본문에 보인다. 실행 결과(`summary.json`)는 이미 있다 | 심사자는 논문만 본다. 빈 상자는 "검증 안 됨"으로 읽는다 | §3 "알려진 맥락" 참고. 숫자를 채우고 상자를 없앤다 |
| W5 | minor | 표 머리 174행 "Answer: c, r, plane", 서론 52행 "plane normal n" | 문제는 평면을 요구한다. 12행 중 평면을 주는 행은 3개(3 meet, prism, perp between)뿐이다. "2 parallel + perp outside"는 평면이 z=0(L_1, L_2의 평면)인데 쓰지 않았다 | 문제의 요구 출력 셋 중 하나가 빠진다 | 2활성 행에 공통 한 줄: "Plane: through the diameter q_i q_j and a point s ∈ L_k ∩ sphere (Lemma 2)." outside 행에 "plane z=0" 추가 |
| W6 | minor | 표 204행 "(one test: r≈0.70)" | 표 안의 숫자 하나가 어떤 입력인지 없다. 검증 불가 | 출처 없는 숫자는 심사자가 가장 먼저 지적한다 | 지운다. 검증은 §4의 `skew_perp` 573/573으로 대신한다 |
| W7 | minor | 55행 "Under the tangent reading, the answers differ in almost every case, except the coplanar triangle" | 증명도 예도 없는 주장이다 | "almost every"는 측정이 필요한 말이다 | "We do not treat the tangent reading."로 바꾼다 |
| W8 | minor | 표 201행 Status "unchecked" | `one_meet_perp`는 1001/1001 PASS다. 상태가 오래됐다 | 검증된 행을 미검증으로 쓰면 손해다 | "closed"로 고치고 §4에 검증 숫자 |
| W9 | minor | 표 179행 coincident | r은 1000/1000 일치하지만 touch_max가 최대 0.536이다(419건). 돌려주는 원이 직선을 안 지난다 | 틀린 평면을 "closed"라고 쓰면 반례 하나로 깨진다 | Fig. 1 밖 행이므로 뺀다. 남기면 "radius verified; circle placement under repair" |
| W10 | minor | §3 160~163행과 표의 순서 | 표가 `[!t]`로 2쪽 맨 위에 오고 기호 정의(δ, w, h, M, S, P, θ, b, v, q)는 그 아래 §3에 온다. 좌표계(L_{1,2}: x=∓h, z=0, y 방향)는 마지막 행 안에서만 정의되는데 193행이 먼저 x, z, e_y, e_z를 쓴다 | 기호를 쓰기 전에 정의해야 한다 | 표를 `[!b]`로 내리거나 §3 기호 문단을 Dispatcher 앞으로 옮긴다. 좌표계 한 문장을 §3에 둔다 |
| W11 | minor | 표 177행 ℓ_a | ℓ_a, ℓ_b, ℓ_c가 정의되지 않았다(A 맞은편 변 길이) | 한 단어면 된다 | "(ℓ_a = \|BC\| etc.)" |
| W12 | minor | 표 188행 "Only r² occurs, so at most 12 solutions have r>0" | 미지수를 (c, r)로 두면 24 → 12가 맞다. 미지수를 (c, r²)로 읽으면 독자는 24로 센다 | 문장이 모호하다 | "in the unknowns (c, r) the system is even in r, so at most 12 have r>0" 또는 "eliminating r² leaves degrees 2, 2, 3: 12" |
| W13 | minor | 표 182행, 185행 | "the skew pair", "the transversal", "the crossing pair's plane"이 모호하다. 꼬인 쌍이 둘일 때 어느 쪽인지, 꼬인 쌍에는 평면이 없다. 또 "n meet"이 교점 개수를 센다는 Figure 1 관례를 본문이 말하지 않는다 | 행을 독립적으로 읽을 수 없다 | 182행: "the skew pair with larger δ (only it can pass)". 185행: "plane of the meeting pair". §3 첫 줄에 "n meet counts intersection points (Figure 1)" |
| W14 | minor | 표 Status 열 | 값이 closed / mixed / sketch / quadratic / unchecked / partial 여섯 가지다. "quadratic"은 상태가 아니다 | 열 하나에 어휘 하나 | closed / 2-active closed / open 셋으로 통일하고, 검증 열(PASS n/n)을 더한다 |

## 4. 정확성 (Correctness)

모든 보조정리와 표의 닫힌 형태를 손으로 확인했다. 결론: **증명된 것 3, 주장만 있는 것 4, 틀린 것 0** (미세한 표현 오류 2).

| 항목 | 판정 | 비고 |
| --- | --- | --- |
| Lemma 1 하한 | 증명됨 | §4.1 |
| Lemma 2 도달, KKT 공면성 | 증명됨, 표현 빈틈 | §4.2, W3 |
| Lemma 2 2활성 대척점 회전 | 증명됨 | §4.3 |
| Theorem 1 | 증명됨 | "the smallest ball" → "a smallest ball" (중심은 유일하지 않을 수 있다) |
| Dispatcher "otherwise three active" | 주장만 | §4.4에 증명을 적었다. 참이다 |
| 표 닫힌 형태 10행 | 손 예제로 확인 | §4.5 |
| 1 meet + perp: z=0 제한 | 주장만 | KKT로 한 줄 증명 가능(§4.5) |
| 4직선 반례 | 주장만 | 참이다(§4.6) |
| 55행 tangent 비교 | 주장만 | 근거 없음(W7) |
| 표 완전성 vs Figure 1 | 완전 | §4.7 |

### 4.1 Lemma 1

p_i ∈ 원 ∩ L_i이면 dist_i(c) ≤ |c − p_i| = r. 따라서 r ≥ max_i dist_i(c) = f(c) ≥ r*. 옳다.

### 4.2 Lemma 2: 존재와 KKT

- 볼록성: dist_i(c) = |P_i(c − a_i)|는 아핀 사상의 노름이라 볼록. max도 볼록. 옳다.
- 강제성(coercive): d_1 ≠ ±d_2이면 ker(P_1) ∩ ker(P_2) = {0}이므로 P_1 + P_2가 양정치. |P_1c|² + |P_2c|² ≥ λ_min |c|² → f → ∞. 옳다.
- KKT: 0 ∈ ∂f(c*) = conv{∇dist_i(c*) : dist_i(c*) = r*}. ∇dist_i = P_i(c−a_i)/dist_i = (c − q_i)/r* = u_i. 옳다. 다만 논문은 u_i를 모든 i에 정의하고 λ_i = 0(비활성)을 말하지 않는다. "at least two active"는 |u_i| = 1(활성)에서 나온다. 이것이 W3다.
- 3활성: λ_1u_1 + λ_2u_2 + λ_3u_3 = 0, λ > 0 → 세 벡터가 원점을 지나는 한 평면에 있다. q_i = c* − r*u_i이므로 c*를 지나는 평면. 대원이 q_1, q_2, q_3을 지난다. 옳다. 참고: 두 u가 대척이고 셋째가 임의여도 공면이다.

### 4.3 Lemma 2: 2활성

λ_iu_i + λ_ju_j = 0, |u_i| = |u_j| = 1 → λ_i = λ_j, u_i = −u_j. q_i, q_j는 대척점. dist_k(c*) ≤ r*이고 L_k는 무한하므로 구와 만나는 s가 있다. q_i, q_j, s를 지나는 평면은 지름을 품으므로 c*를 지난다. 옳다.
퇴화: s가 지름 직선 위(s = q_i)이면 평면이 유일하지 않지만 어느 것이든 된다. 논문은 이를 말하지 않는다. 경미.

### 4.4 Dispatcher: "otherwise three active"의 증명 (논문에 없음)

1. 2활성 (i, j)이면 u_i = −u_j이므로 q_j − q_i = 2(c* − q_i). 이 벡터는 d_i와 d_j 모두에 수직이다 (c* − q_i ⊥ d_i, c* − q_j ⊥ d_j).
2. 그러므로 q_iq_j는 L_i, L_j의 공통 수선이고 길이 2r* = dist(L_i, L_j). 즉 r* = ρ_ij.
3. r* ≥ ρ_max이므로 ρ_ij = ρ_max. 그리고 c* ∈ C_ij이고 dist(C_ij, L_k) ≤ dist_k(c*) ≤ r* = ρ_ij: 검사가 통과한다.
4. 대우: 최대 쌍(동률이면 모두)이 통과하지 못하면 3활성이다.

또 어느 쌍이든 통과하면 r* = 그 ρ다(통과 = 반지름 ρ_ij인 공이 셋을 만난다 → r* ≤ ρ_ij ≤ r*). 그래서 표 182행이 "어느 꼬인 쌍"인지 말하지 않아도 결과는 틀리지 않는다. 다만 최대가 아닌 쌍은 통과할 수 없다.

### 4.5 표의 닫힌 형태: 손 예제

| 행 | 예제 | 계산 | 판정 |
| --- | --- | --- | --- |
| 3 meet | A=(0,0), B=(3,0), C=(0,4) | ℓ_a=5, ℓ_b=4, ℓ_c=3. c = (5A+4B+3C)/12 = (1,1). r = 2·6/12 = 1 | 옳다. 내심에서 ℓ_a n_a + ℓ_b n_b + ℓ_c n_c = 0이므로 KKT 점 |
| 2 parallel, 0 meet (3활성) | h=1, L_3: a=(0,0,2), e=(1,0,1)/√2 | q(z) = (k − e_x z)²/(1−e_y²) − z², k = e_x a_z − e_z a_x = √2. A = −1/2 ✓, B = −2e_x k/(1−e_y²) = −2, C = k²/(1−e_y²) = 2 = dist(M, L_3)² ✓. q(z) = 1: z² + 4z − 2 = 0, z = −2+√6 = 0.449, r = √(1+0.2016) = 1.096. 쌍 (2,3): ρ = 1.06, 중점 (1/4,0,3/4)의 L_1까지 거리 1.458 > 1.06 → 불통과. 3활성. r = 1.096 > 1.06 ✓ | 옳다. **B, C 자리표시자의 답**: k = e_x a_z − e_z a_x, B = −2e_x k/(1−e_y²), C = k²/(1−e_y²). C = dist(M, L_3)²이므로 q(0) ≤ h²가 곧 2활성 검사다. e_z = 0(over)이면 A = 0, 일차식 |
| | 왜 y = argmin인가 | u_1, u_2 ⊥ ŷ이므로 KKT에서 (u_3)_y = 0, 즉 (c − q_3)·ŷ = 0 = ½ ∂_y dist_3². 논문은 이 이유를 안 쓴다 | 경미 |
| 1 meet + perp | L_1 = x축, L_2 = y축, S=(1,1) | θ=90°, b=(1,1)/√2, v=(1,1), b·v=√2. t²/2 − 2√2t + 2 = 0 → t = 2√2 ± 2. 작은 근 0.828, r = t sin45° = 0.586, c=(0.586,0.586,0). dist(c, x축) = 0.586 ✓, dist(c, L_3) = √2·0.414 = 0.586 ✓. KKT: u_1=(0,1), u_2=(1,0), u_3=(−1,−1)/√2, u_1+u_2+√2u_3 = 0 ✓. 쌍 (1,3): ρ=0.5, 중점 (1,0.5,0)의 y축 거리 1 > 0.5 불통과 ✓ | 옳다. 큰 근 t = 4.83은 c가 S 너머라 u_3가 +b 방향, KKT 실패. "smaller root" 옳다 |
| | z = 0의 근거 | u_3는 수평(L_3 ⊥ 평면, 발이 같은 높이). u_1, u_2의 수직 성분은 z/r. KKT 수직 성분: (λ_1+λ_2)z/r = 0 → z = 0 | 논문에 없다. 한 줄 추가 권장 |
| 2 parallel + perp, outside | h=1, a=3, S=(3,0) | 쌍 (1,3): δ = 4, ρ = 2 = (a+h)/2 ✓. 중점 (1,0,0), x_c = (a−h)/2 = 1 ✓. dist(c, L_2) = 0 ≤ 2 통과 ✓. 일반: dist(c, L_2) = \|3h−a\|/2 ≤ (a+h)/2 for a ≥ h ✓ | 옳다. 평면은 z=0(원이 (−h,s_y,0), (a,s_y,0)을 지나고 L_2와 두 점에서 만난다). L_3는 구에 접한다 |
| 2 parallel + perp, between | h=1, S=(0.5, 0) | c=(0,0,0), r=1. L_3 ∩ 구 = (0.5, 0, ±0.866). 평면 y=0이 L_3를 품는다 ✓ | 옳다 |
| 2 parallel, 1 meets both | | ρ_12 = w/2가 최대(다른 두 쌍은 0). L_3가 M을 지나므로 통과 ✓ | 옳다 |
| 2 parallel, 1 meet 1 cross | | δ_23 ≤ w (L_3가 L_1의 점을 지남) → ρ_12 최대. L_1 ∩ L_3의 점이 M에서 w/2 → 통과 ✓. c는 M에서 L_3에 가장 가까운 점 (논문에 없다) | 옳다. c 누락 경미 |
| 3 parallel coplanar | | 바깥 두 직선 지름 원이 공통 평면에서 가운데 직선을 가로지른다 ✓ | 옳다 |
| 3 parallel prism | | 예각: 외접원. 둔각: 최장변/2, 셋째 점이 공 안이라 기울인 평면. 직각: ⊥ 평면도 된다("tilted"가 필수는 아니다) | 옳다. 직각 표현 경미 |
| 0 meet, Bézout | | 미지수 (c, r): 2·2·2·3 = 24, r → −r 대칭 → r>0 최대 12. 또는 r² 소거 후 (2,2,3) = 12 ✓ | 옳다. 문장만 모호(W12) |
| concurrent | | r=0, 점 원 ✓ | 옳다 |
| coincident | | r = δ/2 ✓ (1000/1000). 원의 평면은 419/1000 틀림 (`summary.json` touch_max 0.536) | r 옳음, 배치 틀림(W9) |

### 4.6 4직선 반례

정사면체 꼭짓점 v_i에서 반지름에 수직인 접선 4개. 중심 O에서 u_i = −v_i/R, Σv_i = 0이므로 O가 KKT 점, r* = R. 최소화 집합은 볼록이고 사면체 군에 불변이므로 O를 품는다. 반지름 R인 원이 넷 모두에 닿으려면 접점 v_1..v_4(비공면)를 지나야 하므로 불가능. 옳다. 논문은 이유를 안 쓴다. 한 구절이면 된다.

### 4.7 완전성: 문제의 Figure 1 (16경우) 대 표 (12행)

| Figure 1 | 표의 행 | 상태 |
| --- | --- | --- |
| 3 meet | 3 meet | closed |
| 2 meet 1 cross | 2 meet, 1 cross | 2활성 closed, 3활성 open |
| 1 meet 2 cross over | 1 meet, 2 cross | 2활성 closed(dispatcher), 3활성 open |
| 1 meet 2 cross over/under | 같은 행 | 같음 |
| 0 meet 1 cross over 2 | 0 meet (all skew) | 2활성 closed, 3활성 open |
| 0 meet all cross over/under | 같은 행 | 같음 |
| 2 parallel 1 meets both | 2 parallel, 1 meets both or ... | closed |
| 2 parallel 1 meet 1 cross | 같은 행 | closed (c 누락) |
| 2 parallel 0 meet 1 cross over | 2 parallel, 0 meet | closed (B, C 자리표시자) |
| 2 parallel 0 meet 1 cross over/under | 같은 행 | closed (B, C 자리표시자) |
| 3 parallel 3 coplanar | 3 parallel, coplanar | closed |
| 3 parallel 2 coplanar | 3 parallel, 2 coplanar (prism) | closed |
| 1 meet 1 perpendicular | 1 meet + perpendicular | closed (검증 1001/1001) |
| 1 cross 1 perpendicular | 1 cross + perpendicular | 대칭 축 위: closed. 아니면 2활성 closed, 3활성 open |
| 2 parallel 0 meet 1 perp between | 2 parallel + perpendicular | closed |
| 2 parallel 0 meet 1 perp outside | 같은 행 | closed |

16경우 모두 행이 있다. 닫힌 형태 10, 부분 6. 이 숫자가 초록에 들어가야 한다(W1).
"1 cross + perpendicular"에서 "perpendicular"의 정의(161행 "normal to the plane of the other two")는 꼬인 쌍에는 평면이 없어 맞지 않는다. "parallel to the common perpendicular of L_1, L_2"로 고쳐야 한다.

## 5. 새로움과 관련 연구 (Novelty, related work)

- 기여가 정확히 무엇인지 한 문장이 없다. 실제 기여는 셋이다: (1) 원 → 공 환원(Theorem 1), (2) 2활성/3활성 O(1) 판정기, (3) 16경우 중 10경우 닫힌 형태. 초록은 (3)을 과장한다(W1).
- "세 직선을 만나는 최소 공"은 문헌의 intersection radius 문제다. BJMR94가 바로 그 이름이다. 논문은 이를 "cf."로만 쓴다. 한 문장으로 "the ball subproblem is the intersection radius problem [BJMR94]; our contribution is the circle-to-ball reduction and the closed forms"라고 자리를 잡아야 한다.
- MPT01 인용은 맞게 쓰였다(네 단위 공의 공통 접선 최대 12개). "degree and Galois group decide whether radicals suffice"는 일반적으로 참인 말이다. 다만 MPT01이 Galois 군을 다뤘는지는 오프라인으로 확인하지 못했다.
- PS25: "Touching balls of segments are LP-type of combinatorial dimension 4 in R³"는 오프라인으로 확인 불가. arXiv 번호 2505.02472와 제목도 미확인. **unverified**.
- BJMR94: 제목과 저자는 기억과 일치한다. *Computing* 52(3), 1994는 미확인. **unverified**.
- MPT01: *Discrete Comput. Geom.* 26(1), 2001. 권·호 미확인. **unverified**.
- 세 참고문헌 모두 쪽 번호가 없다.
- `% src:` 주석: Sources 표가 없고 tips 파일 경로를 가리킨다(서문 5~12행이 이를 밝힌다). `source-citation` 기준으로는 ID가 해석되지 않지만, 이 과제에는 Sources 표가 없으므로 구조적 예외로 본다. 참고문헌 세 항목은 `% src:`가 없다.

## 6. 발표 (Presentation)

| 항목 | 판정 |
| --- | --- |
| 제목 | 분명하다. 문제 제목과 같은 말을 쓴다 |
| 초록 | 세 문장, 간결. 그러나 과장(W1). "Tim Wylie's problem"은 해커톤 맥락에서 괜찮다 |
| 그림 1(a) | 인쇄 크기 약 3 cm. 라벨은 읽힌다. "(a)" 라벨이 L_2 위에 가깝지만 겹치지 않는다 |
| 그림 1(b) | 좋다. 다만 L_A, L_B, L_C 표기가 본문의 L_1, L_2, L_3와 다르다 |
| 그림 캡션 | "Why:" 문장이 있다(`figures.md` §3). 세 문장이지만 논문은 학회 양식 우선 |
| 표 1 | 2쪽의 핵심. 12행이 scriptsize로 읽힌다. Status 열 넘침(overfull 3건). 기호가 정의 전에 쓰인다(W10). 한 칸에 수식 여러 개(193행은 4개, `style.md` §2.1) |
| 표 순서 | 표가 Dispatcher 문단과 §3보다 앞에 뜬다. 기호 정의가 뒤에 온다 |
| 표기 | ℓ_a 미정의(W11). 마지막 행의 a가 a_i와 충돌. 좌표계 미정의(W10). "perpendicular"가 꼬인 쌍에서 미정의(§4.7) |
| `\todo` 상자 | 3개가 보인다(W4) |
| 쪽 예산 | 2쪽 꽉 참. 2쪽 하단 약 10줄 여유. 판정기 보조정리(3줄)와 검증 숫자(3줄)가 들어간다 |
| AI 사용 문장 | 있다 |

### 6.1 `paper.md` / `style.md` 위반

- 15단어 초과 문장 21개 (`style.md` §2). 가장 긴 것: 224행(30), 193행(25, 24), 230행(25), 231행(24), 45행(23), 51행(23). 표 칸도 센다.
- 세미콜론: 본문에 없다. 줄표: 없다. 통과.
- 콜론 중첩: 없다. 통과.
- `style.md` §2.1 한 줄에 수식 하나: 표 193, 201, 207행 위반. 표라서 완화 가능하지만 193행은 둘로 나눌 수 있다.
- `latex.md` §10 `\Cref` 미사용(`\ref` 직접). §14 `[H]` 대신 `[!t]`, `[!b]`. `paper.md` §1 "학회 양식 우선"으로 경미.
- `latex.md` §8 행 사이 `\midrule`: 있다. 통과.
- `latex.md` §1.1 `.latexmkrc`: 있다. 통과.

## 7. 저자에게 묻는 질문

1. 초록의 "closed forms for the problem's Figure 1 cases"는 16경우 중 몇 개인가. 표로 세면 10이다. 맞는가.
2. Dispatcher에서 최대 ρ 쌍이 동률이면 어느 쌍을 검사하는가. 모두 검사해야 한다(§4.4).
3. "2 parallel, 0 meet" 행의 B, C는 무엇인가. 검토자 계산: k = e_x a_z − e_z a_x, B = −2e_x k/(1−e_y²), C = k²/(1−e_y²). 일치하는가.
4. "1 cross + perpendicular"에서 "perpendicular"는 무엇에 수직인가. 꼬인 쌍에는 평면이 없다.
5. 표 204행 "(one test: r≈0.70)"의 입력 직선은 무엇인가. 논문에 없으면 지워야 한다.
6. coincident 행: 반지름은 맞고 원의 배치가 419/1000 틀린다(`summary.json`). 어느 평면을 돌려주는가.
7. "touch" = intersect를 택한 이유를 한 줄로 쓸 수 있는가. 문제의 "circle enscribing the center" 문구는 접선(tangent) 읽기와도 맞는다.
8. 2활성 행에서 원의 평면을 왜 쓰지 않았나. Lemma 2가 이미 준다(지름 + s).

## 8. 점수

- **종합: weak accept** (해커톤 기준). SoCG 본 트랙 기준이면 borderline.
- **확신도: 4/5.** 모든 증명과 닫힌 형태를 손으로 확인했다. 참고문헌 세부와 PS25의 주장은 확인하지 못했다.

근거: 원 → 공 환원(Theorem 1)은 짧고 옳고, 이 문제를 볼록 최적화와 KKT로 깨끗하게 정리한다. 판정기는 옳고 O(1)이다. 10/16 경우의 닫힌 형태는 초등적이지만 손 계산과 1000건 SOCP 비교가 모두 일치한다. 열린 경우를 숨기지 않는다. 깎이는 이유는 셋이다. 초록이 표보다 많이 약속한다(W1). 판정기의 핵심 주장("otherwise three active")에 증명이 없다(W2). 본문에 `\todo` 상자 3개와 출처 없는 숫자 하나가 남아 있다(W4, W6). 셋 다 09:00 전에 고칠 수 있고, 고치면 accept다. 3활성 일반 경우가 열려 있는 것은 해커톤 2쪽에서는 결함이 아니다.

## 9. 09:00 전에 점수를 가장 올리는 수정 5가지 (순서대로)

1. **초록과 서론의 과장을 없앤다.** "Closed forms for 10 of 16 cases. For the other 6, the two-active subcase is closed and the three-active subcase is open." "reduces to an O(1) test" → "an O(1) test decides whether two or three lines are active." (W1)
2. **§4 검증을 `summary.json` 숫자로 채우고 `\todo` 상자를 모두 없앤다.** 쓰는 법은 아래 "알려진 맥락" 참고. 표 Status "unchecked" → "closed". (W4, W8, W9)
3. **판정기 보조정리 3줄을 더한다** (§4.4의 1~4). KKT 문장에 "λ_i = 0 unless dist_i(c*) = r*; the active u_i are unit vectors" 한 구절. (W2, W3)
4. **B, C 자리표시자를 푼다.** 식은 §4.5에 있다. 공간이 없으면 "A = …; B, C by the same expansion of q(z) = (k − e_x z)²/(1−e_y²) − z²" 한 줄. (W4)
5. **표의 빈 곳을 메운다.** 2활성 행에 평면 한 줄, ℓ_a 정의, 좌표계 한 문장, "n meet counts intersection points", 204행 숫자 삭제, Status 열 어휘 통일. Status 열 폭을 1.15 cm로 늘려 overfull 제거. (W5, W6, W10~W14)

## 알려진 맥락: 어떻게 쓸 것인가 (결함으로 세지 않음)

### 검증 문단 (`summary.json`, job 150311, code 8a80e7a)

- 생성된 18경우 중 12경우 PASS(표 행이 아니라 summary.json의 경우 이름). 쓰는 법: "In 12 of 18 generated cases every instance agreed (max relative error in r 6.7e−10)."
- SOCP 1건 실패 5행(one_meet_over, one_meet_overunder, all_skew, par_meet_one, par3_obtuse): "FAIL"로 쓰지 않는다. "In five cases the solver did not converge on 1 of 1,000 instances; all other instances agreed." 숨기지도 않는다.
- 닫힌 형태 적용 비율(coverage)을 쓴다. 이것이 "mixed"의 실제 뜻이다: two_meet_one_cross 296/1002, one_meet_over 445/1001, one_meet_overunder 216/1001, all_skew 289/1002, skew_perp 573/1001. 나머지는 3활성(no_closed_form). 한 문장: "The two-active closed form covers 22 % to 57 % of random instances in the open cases; the rest are three-active."
- coincident: "r agreed in 1000/1000; the returned circle missed a line in 419 (plane choice, under repair)". 또는 행을 뺀다(Fig. 1 밖).
- 판정 기준(상대 오차 < 1e−9)은 실행 전에 정한 그대로 쓴다. 측정값 max scaled_dr 6.7e−10(triangle)이 기준 안이다.
- Gröbner 실행은 결과가 없으므로 `\todo` 대신 Future work 한 줄로 옮긴다.

### B, C 자리표시자

- 식이 있다(§4.5). 채운다. 공간이 없으면 위 4번처럼 한 줄.
- 보이는 `\todo` 상자는 어느 경우에도 남기지 않는다. 심사자는 논문만 본다.

### "touch" = intersect

- 소유자 결정이다. 54행의 정의 문장은 좋다.
- 55행의 비교 주장은 근거가 없으므로 "We do not treat the tangent reading."으로 바꾼다(W7).
