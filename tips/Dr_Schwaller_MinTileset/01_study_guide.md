# Schwaller: 2×n 직사각형의 최소 타일 종류 수 학습 가이드

> 사실의 출처는 같은 폴더의 `00_research_notes.md` 하나다.
> 문제 원문은 `problems/Dr_Schwaller.txt`다.
> 해커톤 조건 (READMME.md): 11/7 09:00 → 11/8 09:00.
> 제출물은 **2쪽 Overleaf 논문 하나**이고, 그것만 심사한다.
> 정확한 모서리 시드 공식은 자료에서 찾지 못했다. 이 가이드는 그 공식을 만들어 쓰지 않는다.

---

## 0. 한눈에: 왜 이 가이드가 필요한가

문제 이름은 최소 타일 집합 문제(Minimum Tileset Problem)다.
일반 모양은 어렵다고 알려져 있다.
2×n 직사각형만 따로 보면 답이 어디까지 알려졌는지 먼저 알아야 한다.

| 칸 | 내용 |
| --- | --- |
| 풀려던 문제 | 2×n 직사각형의 복잡도를 모른다. 시드(seed)가 모서리일 때만 식이 있어 보인다 |
| 결과·목적 | 알려진 상한과 하한을 정리하고, 시드가 모서리가 아닌 경우의 열린 문제에 쓸 결과를 고른다 |
| 임무(mission) | 2쪽 논문에 증명된 결과와 미확인 결과를 구분해 쓴다 |
| 비전(vision) | 2×n 직사각형 문제의 복잡도를 한 걸음 더 밝힌다 |

전체 흐름은 다음과 같다.

```
모양 2×n (입력)
      |
      v
추상 타일 조립 모델(abstract Tile Assembly Model, aTAM)에서
결정적 조립으로 만들 최소 타일 종류 수 t
      |
      +-- 하한: t ≥ √n / 2        (시드 위치 무관, 증명됨)
      |
      +-- 상한: t ≤ 4⌈√n⌉ + 2     (온도 2, 모서리 시드, 증명됨)
      |
      v
정확한 값은?
   |                    |
 시드가 모서리         시드가 모서리가 아님
 (식이 있어 보임)       (열린 문제)
```

열린 칸은 여럿이다.
- 온도 2, 안쪽 시드: 정확한 값이 열림 (해커톤 문제).
- 같은 칸의 차수는 Θ(√n)이다. 하한은 증명됨이고 상한은 손 유도다 (3.3).
- 온도 1, 정확한 값: 열림 ([결합 불일치(binding-domain mismatch)](#term-mismatch) 없음 가정 없이는).
- 온도 2, 모서리 시드: 출제자는 식이 있다고 한다. 우리는 찾지 못했다.

각 상자의 용어는 문서 끝 [용어 부록](#용어-부록-terms-appendix)에 있다.

---

## 1. 문제를 한 줄로

모양 하나가 입력으로 주어진다.
그 모양을 [결정적 조립(directed self-assembly)](#term-directed)으로 만드는 최소 [타일 종류(tile type)](#term-tile-type) 수를 구한다.
모양이 2×n 직사각형일 때 이 문제의 복잡도를 묻는다.

문제 원문의 힌트는 둘이다.
- [시드(seed)](#term-seed)가 모서리에 있어야 한다면, 식과 [다항 시간(polynomial time)](#term-poly) 알고리즘이 있어 보인다.
- 그 가정이 없으면 문제는 열려 있다.

원문 진술은 `uniquely self-assemble`이다.
표준 뜻으로 읽으면 이것은 [결정적 조립(directed self-assembly)](#term-directed)이다 (추정).
출제자에게 확인할 질문이다 (`03_plan_and_design.md`의 질문 목록).

---

## 2. 먼저 익힐 기초 (순서대로, 각 30분 이내)

왜 이 순서인가. 아래 통찰(3장)의 하한 논증을 읽는 도구를 앞에서부터 쌓는다.

```mermaid
flowchart LR
  A[타일 종류] --> B[결합 세기]
  B --> C[온도]
  C --> D[시드와 조립]
  D --> E[결정적 조립 대 엄격 조립]
  E --> F[카운터]
  F --> G[하한 셈 논증]
```

| # | 주제 | 왜 필요한가 | 셀프 체크 |
| --- | --- | --- | --- |
| 1 | [추상 타일 조립 모델(abstract Tile Assembly Model, aTAM)](#term-atam)과 [타일 종류(tile type)](#term-tile-type). 사각형 한 칸, 네 변 N, E, S, W마다 [결합 라벨(glue label)](#term-glue). 타일은 회전하지 않고 평행이동만 한다 | 문제 전체의 언어다 | 타일 종류를 네 결합 라벨의 순서쌍으로 쓸 수 있는가 |
| 2 | [결합 세기(glue strength)](#term-strength). 마주 본 변은 라벨이 같고 세기가 양수일 때만 붙는다 | 타일이 언제 붙는지 정한다 | 라벨이 달라도 붙는가 (아니다) |
| 3 | [온도(temperature, τ)](#term-temperature). 붙는 변들의 세기 합이 τ 이상이어야 타일이 붙는다 | 온도 1과 온도 2의 문제가 갈린다 | 온도 1에서 결합 하나로 붙는 이유를 설명할 수 있는가 |
| 4 | [협력 결합(cooperative binding)](#term-cooperation). 온도 2에서 세기 2 결합 하나, 또는 세기 1 결합 둘 | [카운터(counter)](#term-counter)가 가능해지는 이유다 | 세기 1 결합 하나만으로 붙지 못함을 확인하는가 |
| 5 | [시드(seed)](#term-seed), [생성 가능 조립체(producible assembly)](#term-producible), [종단 조립체(terminal assembly)](#term-terminal) | "만든다"의 정의다 | 종단 조립체가 왜 더 못 자라는지 말할 수 있는가 |
| 6 | [결정적 조립(directed self-assembly)](#term-directed) 대 [엄격 조립(strict self-assembly)](#term-strict) | 같은 문제의 두 판이 있다 | 두 정의의 차이를 한 줄로 쓸 수 있는가 |
| 7 | [빗 구성(comb construction)](#term-comb) | 모든 온도와 모든 시드 칸에 맞는 상한 n + 1을 준다. 위 줄 시드는 위아래로 뒤집은 빗을 쓴다 | n = 3일 때 타일 종류 4개를 그릴 수 있는가 |
| 8 | [카운터(counter)](#term-counter), k자리 m진수 | 상한 4⌈√n⌉ + 2의 뼈대다 | 높이 2에서 왜 이진 카운터가 안 맞는지 설명할 수 있는가 |
| 9 | [하한(lower bound)](#term-lower-bound)의 [셈 논증(counting argument)](#term-counting)과 [펌핑(pumping)](#term-pumping) | 하한 √n / 2의 근거다 | 열 하나에 타일이 두 개뿐인 이유를 아는가 |

결정적 조립과 엄격 조립의 정의는 다음과 같다.

```
결정적 조립: 종단 조립체가 정확히 하나, 모양이 S
           어느 실행에서나 같은 자리에 같은 타일 종류
엄격 조립: 모든 종단 조립체의 모양이 S
           실행마다 같은 자리에 다른 타일 종류가 올 수 있음
```

빗 구성(F3, 손 유도)은 다음과 같다.

```
위 줄    T  T  T  T  T      T: 위 타일 하나, 남쪽 결합 u
아래 줄  B1 B2 B3 B4 B5     B1이 시드 (왼쪽 아래 모서리)
         → 아래 줄은 동쪽 결합 e_i가 세기 τ, 모든 B_i는 북쪽 결합 u가 세기 τ
타일 종류 수 = n + 1
```

시드 위치별로 쓰는 빗은 다음과 같다.
- 모서리 시드나 아래 줄 아무 칸의 시드: 위 빗 그대로. 증명은 양쪽으로 귀납한다.
- 위 줄 시드: 위의 빗은 실패한다. 시드 T 아래에 B1..Bn이 모두 북쪽 결합 u를 내밀어 경쟁한다.
- 위 줄 시드는 위아래로 뒤집은 빗을 쓴다. 위 줄에 사슬 T_1..T_n, 아래 줄에 공유 타일 하나.
- 뒤집은 빗도 n + 1종이다. 그래서 상한 n + 1은 모든 시드 칸에서 성립한다.

높이 2 카운터의 숫자는 다음과 같다.

```
상한 (온도 2, 모서리 시드):  t ≤ 4⌈√n⌉ + 2
예 n = 100:    5 ≤ t ≤ 42
예 n = 10,000: 50 ≤ t ≤ 402
```

참고문헌이다. 논문에 인용하기 전에 서지 정보를 직접 확인해줘.

- Aggarwal, Cheng, Goldwasser, Kao, Moisset de Espanés, Schweller. *Complexities for generalized models of self-assembly*. SIAM J. Comput. 2005 [S-MTS-2]. 읽은 범위: 본문 1–8쪽. 정의, 정리 3.1 하한, 정리 3.2 구성.
- Adleman, Cheng, Goel, Huang, Kempe, Moisset de Espanés, Rothemund. *Combinatorial optimization problems in self-assembly*. STOC 2002 [S-MTS-1]. 읽은 범위: 초록만.
- Furcy, Summers, Wendlandt. *New bounds on the tile complexity of thin rectangles at temperature-1*. arXiv 1808.04358 [S-MTS-5].
- Bryans, Chiniforooshan, Doty, Kari, Seki. *The power of nondeterminism in self-assembly*. SODA 2011 [S-MTS-3].
- Chen, Doty, Seki. *Program size and temperature in self-assembly*. arXiv 1011.3493 [S-MTS-4].
- Mahaney (1982), 희소 집합 정리 [S-MTS-7]. 읽은 범위: 위키백과와 검색 요약만.
- 정리 진술은 [Mahaney 정리(Mahaney's theorem)](#term-mahaney)에 있다.
- 창 영화 보조정리(Window Movie Lemma): Meunier, Patitz, Summers, Theyssier, Winslow, Woods. SODA 2014. 원문을 읽지 않았다 (UNVERIFIED).

---

## 3. 가장 중요한 통찰 (먼저 이해할 것)

### 3.1 높이 2는 정보를 타일 두 개로만 나른다

왜 중요한가. 하한 √n / 2가 이 한 문장에서 나온다.

2×n 띠에서 세로 열 하나에는 타일이 두 개뿐이다.
그래서 열 하나가 나르는 정보는 세 가지뿐이다.
- 위 타일 종류
- 아래 타일 종류
- 붙은 순서 (위가 먼저인가, 아래가 먼저인가)

```
  열 j:   [위]
          [아래]
  상태(state) = 위 타일 종류 + 아래 타일 종류 + 붙은 순서
```

타일 종류가 t개면 [열 상태(column state)](#term-column-state)는 최대 2·t²개다 (손 유도, 직관).
시드 열을 빼면 시드 한쪽에 열이 (n − 1)/2개 이상 남는다.
그 수가 2·t²보다 크면 같은 상태가 한쪽에서 반복된다.
반복 사이를 [펌핑(pumping)](#term-pumping)하면 모양이 무한해진다.
이로부터 n ≤ 4·t² + 1이 나온다.
곧 t ≥ √((n − 1)/4) ≈ √n / 2다.

결합 라벨이 맞는다고 해서 사이 구간을 복사할 수는 없다.
- 온도 2에서 그 구간의 타일은 이웃의 도움을 받아 붙었을 수 있다 ([협력 결합(cooperative binding)](#term-cooperation)).
- 복사 조립체에서 그 이웃은 나중에 놓이는 다른 복사본이다.
- 그래서 같은 타일 종류와 같은 붙은 순서가 모두 필요하다.
- 그래야 복사 조립체가 [생성 가능(producible)](#term-producible)해진다.
- 이 생성 가능 확인이 증명에서 어려운 부분이다.

상수 1/2는 위 셈에서 나온다.
단, 복사 조립체가 생성 가능하다는 단계가 필요하다.
그 단계는 [S-MTS-2] 정리 3.1이 증명한다.
[창 영화 보조정리(Window Movie Lemma)](#term-window-movie)로도 증명할 수 있다 (원문 미확인, UNVERIFIED).
영화 수를 2t(t + 1) 이하로 세면 약 √n / 2가 나온다 (손 유도).
더 느슨하게 세면 약 √n / 4가 나온다.

증명된 하한의 정확한 형태는 다음과 같다 ([S-MTS-2] 정리 3.1의 증명, k = 2).

```
t < (n / (2·2!))^{1/2} 이면 2×n을 결정적 조립으로 못 만든다
따라서 t ≥ √n / 2
```

- 시드가 어디에 있어도 성립한다. 증명이 "시드 위치와 무관"하다고 명시한다.
- 시드 열이 세 복사본 중 하나이면 N에 +1이나 +2가 든다. √n / 2의 점근 크기는 그대로다.
- 높이 k ≤ 2인 길이 n 모양 어디에나 쓸 수 있다는 주석이 증명 뒤에 있다.

### 3.2 온도 2에서는 높이 2라도 카운터가 들어간다

왜 중요한가. 상한이 n + 1에서 약 √n으로 내려온다.

| 사실 | 상태 | 출처 |
| --- | --- | --- |
| 높이 2에 k = 2자리 m진수 카운터가 들어간다. m = ⌈√n⌉, 타일 종류 4m + 2개, 온도 2, 모서리 시드 | 증명됨 (PROVEN) | [S-MTS-2] 정리 3.2 |
| 길이 n은 서쪽 결합의 시작값 m^k − N으로 조절한다. 1..m^k 중 어떤 길이도 가능하다 | 증명됨 (PROVEN) | [S-MTS-2] 8쪽 |
| log n 비트 이진 카운터는 높이 2에 안 들어간다 | 증명됨 (하한 √n / 2에서 따라옴) | [S-MTS-2] |

결론은 온도 2에서 2×n의 답이 Θ(√n)이라는 것이다.
상수 차이는 약 8이다 (추정).

### 3.3 시드 위치가 문제를 가른다

왜 중요한가. 열린 부분이 정확히 여기다.

| 시드 | 상태 | 이유 |
| --- | --- | --- |
| 모서리 | 출제자는 식이 있다고 한다. 우리는 그 식을 못 찾았다 | 한쪽으로만 자란다 |
| 안쪽 칸, 온도 2 | 정확한 값은 열림 (해커톤 문제). 차수는 Θ(√n) | 서쪽과 동쪽 두 팔이 자란다 |

안쪽 시드에서 달라지는 점은 다음과 같다.
- 하한 √n / 2는 그대로 성립한다 (증명됨).
- 상한은 O(√n)이다 (손 유도).
- 상한 하나는 빗 구성의 n + 1이다.
- 다른 상한은 두 팔 카운터의 4√2·√n + O(1)이다.
- 두 팔 상한은 팔 길이 a, b에서 4⌈√a⌉ + 4⌈√b⌉ + O(1)을 쓴다.
- 이 상한은 [S-MTS-2] 8쪽의 길이 주장에 기댄다.
- 정확한 값과 복잡도는 열려 있다 (추정).
- 두 팔에 카운터를 따로 쓰면 모서리보다 비싸다.
- 두 팔이 타일 종류를 **공유**해야 이긴다.
- 타일은 회전하지 않는다.
- 서쪽으로 자라는 타일과 동쪽으로 자라는 타일은 결합이 두 방향에 모두 맞아야 공유한다.
- 이것이 이 문제의 핵심 어려움이다.

### 3.4 온도 1은 거의 다 열려 있다

| 설정 | 하한 | 상한 | 상태 |
| --- | --- | --- | --- |
| [결합 불일치(binding-domain mismatch)](#term-mismatch) 없음 가정 | n + 1 | n + 1 | 조건부 증명(PROVEN-conditional), 부분 확인 |
| 가정 없음 (2차원) | Ω(√n) | n + 1 | 열림. 정확한 값은 찾지 못함 |

- 조건부 결과는 [S-MTS-6]이고 부분 확인이다. 요약문 조각만 읽었다.
- [맨해튼 지름(Manhattan diameter)](#term-manhattan)의 정의를 전문에서 확인하지 못했다.
- 상한 n + 1은 모든 시드 칸에서 성립한다. 위 줄 시드는 뒤집은 빗을 쓴다. 빗은 불일치가 없다.
- 가정 없는 범위는 [S-MTS-5]의 Ω(N^{1/k})와 N + k − 1에서 k = 2로 얻는다.
- 온도 1의 하한은 F4(√n / 2)보다 나은 점이 없다. F4는 모든 온도에서 성립한다.
- 우리가 받은 직관은 "온도 1에서는 2×n의 한 줄이 같은 타일 종류를 반복하면 펌핑이 생긴다"였다.
- 이 직관은 가정 아래서만 증명되어 있다.
- 2차원 일반 경우는 [S-MTS-5]도 격차를 명시한다.

---

## 4. 학습 순서 체크리스트

- [ ] 2장 1–6번 행을 읽고 [타일 종류(tile type)](#term-tile-type)를 네 결합으로 직접 쓴다.
- [ ] 2×1이 타일 종류 정확히 2개를 요구함을 직접 쓴다. 한 종류면 위로 무한히 자란다 (F1, 손 유도).
- [ ] [빗 구성(comb construction)](#term-comb)이 결정적 조립이고 종단 모양이 2×n임을 확인한다 (F3).
- [ ] [S-MTS-2]의 정리 3.1 증명을 k = 2로 다시 읽는다.
- [ ] 정리 3.2의 타일 묶음 그림 3.1을 따라 그린다. 시드 열이 동쪽 끝 모서리에 있다.
- [ ] 안쪽 시드에서 두 팔이 타일 종류를 공유하는 예를 하나 만들어 본다 (3.3).
- [ ] 계산이 필요한 항목을 표로 정리한다. 실행은 클러스터에서 한다 (6장).

```
2×1 → 빗 구성 → 하한 √n/2 → 카운터 상한 → 안쪽 시드 (열림)
(쉬움)                                          (어려움)
```

---

## 5. 함정 (Pitfalls)

1. **모델이 모호하다.** 온도 τ가 1인지 2인지, 풀이자가 고르는지 문제에 없다. 결과가 온도마다 다르다. [온도(temperature, τ)](#term-temperature)를 논문에 명시해줘.
2. **결정적 조립인지 엄격 조립인지 모호하다.** Adleman 등 2002는 결정적 조립을 쓴다. Bryans 등은 엄격 조립을 쓰고, 그 문제는 [다항 계층 2층 완전(second-level polynomial-hierarchy complete, Σ2^P-complete)](#term-sigma2)이다. 판마다 다른 정리를 쓴다.
3. **입력 인코딩이 모호하다.** [단항(unary)](#term-unary) n은 입력 크기가 Θ(n)이다. 이진수 n은 크기가 log n이다.
   - 희소성 논증(`02_possible_solutions.md`의 방향 1)은 단항 n 또는 정렬된 칸 목록에서 성립한다.
   - 정렬 안 된 칸 목록은 [정규화 환원(normalization reduction)](#term-normred)이 필요하다.
   - 정규형 ⟨1^n, s, k⟩에서 k와 s는 단항이나 고정 폭으로 쓴다.
   - k ≥ n + 1인 입력은 모두 고정된 예 입력(yes-instance)으로 보낸다. 빗 구성이 최적값(optimum, OPT) ≤ n + 1을 주기 때문이다.
   - 정규형에 이진수 k를 쓰면 [희소 집합(sparse set)](#term-sparse)이 아니다.
   - 입력의 k는 이진수여도 된다. 환원이 k를 단항이나 고정 폭으로 다시 쓴다.
   - 논증은 이진수 n에서만 실패한다.
4. **"시드가 모서리"의 뜻이 모호하다.** 네 모서리 중 어느 것도 되는지 불분명하다. 이 점을 질문으로 넘긴다.
5. **하한 √n / 2는 시드 위치와 무관하다.** 상한 4⌈√n⌉ + 2는 모서리 시드를 쓴다. 두 값을 섞어 "시드 위치에 따른 정확한 값"이라고 쓰지 마.
6. **손으로 만든 카운터는 시뮬레이션 전이다.** 타일 종류가 m + 3D + 2개인 구성이다. (m, D) = (3, 2)와 (12, 4)에서 손으로 추적했다. 시뮬레이션은 하지 않았다. 증명된 것처럼 쓰지 마. 논문에는 "손 유도"로 쓴다. R2 시뮬레이션은 선택이다.
7. **정확한 모서리 시드 공식은 못 찾았다.** 출제자 진술에 식이 있다고만 나온다. 자료에서 공식을 찾지 못했다. 식을 지어내지 마.
8. **출제자 신원은 추정이다.** "Dr. Schwaller"가 Robert Schweller인지 확인하지 못했다. 그 사람이 있다면 텍사스 대학교 리오그란데 밸리 캠퍼스(University of Texas Rio Grande Valley, UTRGV) 소속이다. 논문에 이름을 단정해 쓰지 마.
9. **읽지 못한 자료가 있다.** [S-MTS-8], [S-MTS-9]의 저자와 결과는 미확인이다. 인용하지 마.

---

## 6. 계산 작업에 관한 주의 (이 머신 규칙)

왜 막는가. 이 머신에서 계산을 돌리면 중앙 처리 장치(central processing unit, CPU)를 오래 점유한다. 규칙은 `~/.claude/CLAUDE.md`에 있다.

```
로컬 금지                        로컬 허용
-----------------------------    -----------------------------
타일 집합 전수 탐색(R1)          저장된 결과로 그림과 표 그리기
카운터 시뮬레이션(R2, 선택)
```

- [전수 탐색(brute-force search)](#term-brute-force)과 시뮬레이션은 로컬에서 바로 실행하지 않는다.
- R1: 2×n, n = 2..8, 온도 1과 2, 시드 위치마다 최소 타일 종류 수를 찾는다.
- R2 (선택): 손으로 추적한 카운터를 몇 개의 (m, D)로 시뮬레이션해 독립 확인한다.
- 둘 다 클러스터에서 한다. 제출은 소유자 승인 뒤에 한다.
- 프로젝트 루트 `CLAUDE.md`에 계산 환경이 아직 없으면, 먼저 어떤 클러스터나 Colab을 쓸지 정해줘.
- 저장된 결과로 그림을 그리는 작업은 로컬에서 해도 된다.

---

## 용어 부록 (terms appendix)

<a id="term-atam"></a>
- **추상 타일 조립 모델(abstract Tile Assembly Model, aTAM)**: 타일이 붙어 모양을 만드는 수학 모델.

<a id="term-tile-type"></a>
- **타일 종류(tile type)**: 네 변(N, E, S, W)에 결합 라벨이 하나씩 붙은 사각형 한 종류. 같은 종류의 타일은 얼마든지 쓴다.

<a id="term-glue"></a>
- **결합 라벨(glue label)**: 타일 변에 붙은 이름. 마주 본 변의 라벨이 같아야 결합이 생긴다.

<a id="term-strength"></a>
- **결합 세기(glue strength)**: 결합 라벨마다 정한 0, 1, 2, ... 중 하나의 수. 양수여야 붙는다.

<a id="term-temperature"></a>
- **온도(temperature, τ)**: 타일이 붙기 위해 필요한 결합 세기 합의 문턱값.

<a id="term-cooperation"></a>
- **협력 결합(cooperative binding)**: 온도 2에서 일어난다. 세기 2 결합 하나나 세기 1 결합 둘이 타일을 붙인다.

<a id="term-seed"></a>
- **시드(seed)**: 정해진 자리에 놓인 첫 타일. 모든 성장이 여기서 시작한다.

<a id="term-producible"></a>
- **생성 가능 조립체(producible assembly)**: 시드에서 시작해 세기 τ 이상으로 타일을 한 장씩 붙여 도달하는 조립체.

<a id="term-terminal"></a>
- **종단 조립체(terminal assembly)**: 더 이상 타일이 붙을 수 없는 생성 가능 조립체.

<a id="term-directed"></a>
- **결정적 조립(directed self-assembly)**: 종단 조립체가 정확히 하나이고 그 모양이 목표 모양인 경우. 어느 실행에서나 같은 자리에 같은 타일 종류가 온다.

<a id="term-strict"></a>
- **엄격 조립(strict self-assembly)**: 모든 종단 조립체의 모양이 목표 모양인 경우. 실행마다 타일 종류가 달라도 된다.

<a id="term-comb"></a>
- **빗 구성(comb construction)**: n + 1종 구성이다. 아래 줄에 타일 n종, 위 줄에 타일 1종을 쓴다. 위 줄 시드는 뒤집은 빗을 쓴다.

<a id="term-counter"></a>
- **카운터(counter)**: 열을 지날 때마다 수를 세어 길이를 정하는 타일 구성.

<a id="term-lower-bound"></a>
- **하한(lower bound)**: 어떤 구성도 이보다 적은 타일 종류로는 안 된다는 증명된 값.

<a id="term-counting"></a>
- **셈 논증(counting argument)**: 가능한 상태의 수를 세어 한계를 보이는 증명 방법.

<a id="term-pumping"></a>
- **펌핑(pumping)**: 반복되는 상태 사이의 조각을 되풀이해 모양을 무한히 늘리는 논증.

<a id="term-column-state"></a>
- **열 상태(column state)**: 세로 열 하나의 위, 아래 타일 종류와 붙은 순서의 묶음.

<a id="term-manhattan"></a>
- **맨해튼 지름(Manhattan diameter)**: 모양 안 두 칸 사이 격자 거리의 최댓값. 이 자료에서 정의는 전문 확인 전이다.

<a id="term-sigma2"></a>
- **다항 계층 2층 완전(second-level polynomial-hierarchy complete, Σ2^P-complete)**: 비결정 다항 시간(nondeterministic polynomial time, NP)보다 한 층 위 부류의 가장 어려운 문제군.

<a id="term-poly"></a>
- **다항 시간(polynomial time, P)**: 입력 크기의 다항식으로 늘어나는 계산 시간. 그 시간에 풀리는 문제의 부류도 가리킨다.

<a id="term-np"></a>
- **비결정 다항 시간(nondeterministic polynomial time, NP)**: 답을 다항 시간에 검증할 수 있는 결정 문제의 부류.

<a id="term-np-complete"></a>
- **비결정 다항 시간 완전(nondeterministic polynomial-time complete, NP-complete)**: 비결정 다항 시간(nondeterministic polynomial time, NP) 부류에 속한다. 그 부류의 모든 문제를 이 문제로 바꿀 수 있다.

<a id="term-sparse"></a>
- **희소 집합(sparse set)**: 길이 L인 원소의 수가 L의 다항식 이하인 집합.

<a id="term-mahaney"></a>
- **Mahaney 정리(Mahaney's theorem)**: 다음 정리다. 희소 집합이 비결정 다항 시간 완전(nondeterministic polynomial-time complete, NP-complete)이면 다음이 성립한다. 다항 시간(polynomial time, P)과 비결정 다항 시간(nondeterministic polynomial time, NP)이 같다.

<a id="term-unary"></a>
- **단항(unary) 인코딩**: 수 n을 1이 n개인 문자열로 쓰는 방식. 입력 길이가 n에 비례한다.

<a id="term-normred"></a>
- **정규화 환원(normalization reduction)**: 어떤 인코딩이든 정규형 ⟨1^n, s, k⟩로 바꾸는 다항 시간 변환.

<a id="term-mismatch"></a>
- **결합 불일치(binding-domain mismatch)**: [S-MTS-6]의 조건 이름이다. 정의는 요약 조각만 읽었고 전문 확인 전이다.

<a id="term-window-movie"></a>
- **창 영화 보조정리(Window Movie Lemma)**: 창 안의 결합 기록으로 펌핑을 엄밀하게 하는 도구. 원문 미확인.

<a id="term-brute-force"></a>
- **전수 탐색(brute-force search)**: 가능한 후보를 모두 만들어 하나씩 검사하는 방법.
