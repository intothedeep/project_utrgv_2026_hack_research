# 연구 계획 및 설계 (논문 집필 전 단계)

## 0. 한눈에: 왜 이 계획인가

| 칸 | 내용 |
| --- | --- |
| 풀려던 문제 | 제출까지 시간이 한정되어 있다. 2쪽에 담을 결과를 골라야 한다 |
| 결과·목적 | 우선순위가 정해진 결과 목록과 시간표를 만든다 |
| 임무(mission) | 2쪽 논문 하나를 마감 안에 낸다 |
| 비전(vision) | 케이스 분석을 한 정리로 줄인 논문을 낸다 |

전체 흐름은 다음과 같다.

```
질문 확정 → 증명 정리 → 닫힌 해 유도 → 구현·검증 → 보너스 실험 → 집필 → 교정·제출
16:30       17:30        19:30          22:30        00:30         03:00   06:00
```

## 목표와 산출물

- 심사 대상은 2쪽 논문이다. 파일은 `papers/Wylie_SmallestCircle/main.tex`이고 템플릿은 `hackr26.cls`이다.
- 파일은 현재 비어 있다. 이 단계에서는 쓰지 않는다.

주장할 결과를 우선순위 순으로 쓴다.

1. **통합 정리.** 최소 원은 세 직선과 만나는 [최소 접촉 구(minimum touching ball)](#term-min-touching-ball)의 [대원(great circle)](#term-great-circle)이다. 이 정리가 케이스 분석을 활성 집합 판정으로 줄인다.
2. **O(1) dispatcher**와 케이스별 닫힌 해 표. Figure 1의 모든 케이스를 담는다. PDF에 없는 [공점(concurrent lines)](#term-concurrent-lines) 케이스도 담는다.
3. 놀라운 결과 1개를 그림으로 보인다. 3평행 둔각 케이스에서 평면이 기울어진다.
4. (보너스) 일반 꼬인 케이스의 대수적 차수. 닫힌 해의 한계를 보인다.

## 타임라인 (11/7 16:30 → 11/8 09:00, 약 16.5시간)

| 시간 | 단계 | 완료 기준 |
| --- | --- | --- |
| 16:30–17:30 | Wylie에게 해석 질문 (touch = intersect?). 입력 형식 확정 | 답을 받아 메모 |
| 17:30–19:30 | Lemma 1·2 증명 정리. dispatcher 확정 | 손으로 쓴 증명 1쪽 |
| 19:30–22:30 | 케이스 A–E 닫힌 해 유도 (B의 2차식 전개, D1 [아폴로니우스 점-직선-직선 문제(Apollonius point-line-line problem, PLL)](#term-pll)) | 표의 🟡 → ✅ |
| 22:30–00:30 | 구현: 닫힌 해 함수 + [이차 원뿔 계획법(second-order cone programming, SOCP)](#term-socp) 검증기. 코드 작성은 로컬, **실행은 계산 환경** | V1, V2 통과 |
| 00:30–03:00 | F: 일반 꼬인 케이스 [그뢰브너 기저(Gröbner basis)](#term-groebner) 차수 실험 (V3). over/under 대응 (V4) | 차수 표 |
| 03:00–06:00 | 그림 2–3개 + 2쪽 논문 집필 | 컴파일되는 초안 |
| 06:00–08:30 | 교정. 수식 재확인. Overleaf 링크 제출 | Discord #submissions 게시 |
| 08:30–09:00 | 버퍼 | 없음 |

수면 없이 가는 일정이다.
2–3시간 수면이 필요하면 F(보너스)를 먼저 잘라내줘.

## 2쪽 논문 설계 (구조만, 본문은 아직 쓰지 않음)

왜 이 배분인가. 핵심 정리와 케이스 표에 지면을 가장 많이 준다.

| 섹션 | 분량 | 내용 |
| --- | --- | --- |
| Abstract | 4줄 | 통합 정리 + dispatcher + 커버한 케이스 수 |
| 1 Introduction | 0.25쪽 | 문제, Figure 1 참조, 해석 명시 |
| 2 Main Theorem | 0.5쪽 | Lemma 1, 2 + 증명 (짧음) |
| 3 Case Analysis | 0.6쪽 | 큰 표 하나. 케이스 → 활성 집합 → (c, r, n) 공식 |
| 4 Figures | 0.3쪽 | (a) 구 + 대원 다이어그램 (b) 3평행 둔각 기울어진 원 |
| 5 Verification / Open | 0.25쪽 | [이차 원뿔 계획법(second-order cone programming, SOCP)](#term-socp) 비교 결과. 일반 꼬인 케이스 차수 |
| 6 Future Work | 0.15쪽 | 직선 4개의 [기저 연산(basis computation)](#term-basis-computation). 선분 버전. 3차원 정확 알고리즘. Phillips-Schou 2025의 빈칸에서 고른다 |
| References | 0.1쪽 | 3–4개 |

## 구현 설계 (나중 단계용)

왜 이렇게 나누나. 계산 환경에서 돌릴 파일과 로컬에서 돌릴 파일을 분리한다.

```
smallest_circle/
  geometry.py      # Line, dist, foot, line_line(): 관계/최근접점/거리
  classify.py      # Figure 1 케이스 라벨 (+ over/under: 교차 높이 부호)
  closed_form.py   # dispatcher + 케이스별 공식 → Circle(c, r, n)
  verify_socp.py   # cvxpy SOCP: min r s.t. ||P_i(c−a_i)|| ≤ r   ← 계산 환경에서 실행
  check_touch.py   # 원 위 샘플점과 직선 최소거리 → 0인지
  figures.py       # 저장된 결과(JSON/CSV)로 그림 생성 ← 로컬 허용
```

## 출제자에게 물어볼 질문

1. "touches"는 intersects인가요, [접함(tangent)](#term-tangent)인가요? intersects는 원 곡선이 직선과 공유점을 갖는 경우입니다.
2. [공점(concurrent lines)](#term-concurrent-lines)일 때 r = 0인 [퇴화(degenerate)](#term-degenerate) 원을 답으로 인정하나요? 공점은 세 직선이 한 점에서 만나는 경우입니다.
3. 해가 여러 개(평행 케이스)일 때 하나만 내면 되나요? 아니면 해의 족 전체를 서술해야 하나요?
4. 입력 형식에 선호가 있나요? 벡터형, 두 점, [플뤼커 좌표(Plücker coordinates)](#term-plucker) 중에서 골라주세요.

---

## 용어 부록 (terms appendix)

<a id="term-socp"></a>
- **이차 원뿔 계획법(second-order cone programming, SOCP)**: 노름 부등식 `‖Ax + b‖ ≤ cᵀx + d` 아래에서 선형 함수를 최소화하는 볼록 최적화.

<a id="term-pll"></a>
- **아폴로니우스 점-직선-직선 문제(Apollonius point-line-line problem, PLL)**: 점 하나와 직선 둘에 접하는 원을 구하는 문제. 2차방정식으로 풀린다.

<a id="term-min-touching-ball"></a>
- **최소 접촉 구(minimum touching ball)**: 세 직선 모두와 만나는 가장 작은 구.

<a id="term-great-circle"></a>
- **대원(great circle)**: 구의 중심을 지나는 평면이 구면과 만나서 생기는 원.

<a id="term-concurrent-lines"></a>
- **공점(concurrent lines)**: 한 점에서 만나는 세 개 이상의 직선.

<a id="term-degenerate"></a>
- **퇴화(degenerate)**: 일반 경우의 구조가 무너진 특수 경우. 여기서는 r = 0인 경우.

<a id="term-groebner"></a>
- **그뢰브너 기저(Gröbner basis)**: 다항식 연립방정식을 변수 소거가 쉬운 형태로 바꾼 생성 집합.

<a id="term-tangent"></a>
- **접함(tangent)**: 곡선과 직선이 한 점에서 스치듯 만나는 관계.

<a id="term-plucker"></a>
- **플뤼커 좌표(Plücker coordinates)**: 방향 벡터와 모멘트 벡터 한 쌍으로 3D 직선을 나타내는 좌표.

<a id="term-basis-computation"></a>
- **기저 연산(basis computation)**: LP형 문제(LP-type problem) 알고리즘이 매 단계에서 작은 부분집합의 최적해를 정확히 구하는 연산.
