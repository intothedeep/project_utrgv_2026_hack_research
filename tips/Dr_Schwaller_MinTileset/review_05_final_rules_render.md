# Review 05: 최종 검증 (2차 수정 후)

- 검토자: reviewer 에이전트. 검증만 했다. 대상 파일은 고치지 않았다 (2026-11-07).
- 대상: `study_tips.html` (1601줄), `01_study_guide.md`, `02_possible_solutions.md`, `03_plan_and_design.md`.
- 사실 출처: `00_research_notes.md` (아래 "notes").
- 기준: `review_03_recheck_rules_render.md` (F6–F13, 2.4 잔여, N1–N6), `review_04_recheck_math.md` §4 F1–F8.
- 다시 읽은 규칙 (Read 도구): `tips-page.md` §7, `answering.md` §3, `style.md` §3–§4, `figures.md`.
- 렌더 하네스와 스크린샷: `/private/tmp/claude-501/-Users-tio-Documents-project-utrgv-2026-hack-research/957682e3-7cb7-4d00-a99a-596fbb695b3a/scratchpad/render_v5/`.
- 정적 점검 스크립트: 같은 scratchpad의 `render_v3/static_checks.py`, `v5/links.py`, `v5/caps.py`, `v5/abbr.py`.

## 판정

**ISSUE (경미만).** 차단(blocker) 0, 중대(major) 0, 경미(minor) 열림 7.

```
review_03  F6–F13, 2.4, N1–N6 ── CLOSED 13 · PARTLY 2 (N5, N6) · OPEN 0
review_04  §4 F1–F8           ── CLOSED 8 · OPEN 0 (HTML 쪽 누락 둘은 새 지적 M2)
렌더       54상태 @1040px     ── JS 오류 0 · 가로 스크롤 0 · 겹침 0 · 단계 버튼 정상
번호       그림 1–15, 표 1–10 ── 빈 번호 0 · 본문 참조 2개 모두 맞음
링크       #term- 62개        ── 없는 대상 0 · 부록 용어 43개 모두 본문에서 링크
문장 부호  줄표 grep          ── 4개 파일 모두 0
15어절     초과 비율          ── HTML 0.6% · 01 0.0% · 02 1.3% · 03 0.0% (모두 3% 미만)
용어 8개   결합 … 사슬        ── 4개 파일 통일
질문 7개   HTML 대 03         ── 글자까지 같음
작성 지시 누출                ── 3곳 (M1)
```

- 이전 중대 지적과 수학 오류(review_04 NEW ERROR 2건)는 모두 닫혔다.
- 남은 것은 표현과 용어의 경미 항목이다. 내용 오류는 없다.
- 사다리 점검 L1–L4: 해당 없음. 시스템이나 앱 작업이 아니다.
- 위계 점검 H1–H2: 해당 없음. 디스패치가 PLAN.md, AC 목록, cycle 값을 주지 않았다.

## 1. review_03 지적 상태

| ID | 상태 | 근거 |
| --- | --- | --- |
| F6 "약 29배" 출처 | CLOSED | `study_tips.html:700` "10,036 ÷ 349 = 28.8이라 약 29배입니다(계산값)" |
| F7 | CLOSED | review_03에서 이미 닫힘 |
| F8 약어 단독 | CLOSED | `UTRGV` 단독 0건 (HTML 279, 1129, 1299, 1360 모두 풀어 씀). τ 병기는 4개 파일 모두 "온도(temperature, τ)" (HTML 316, 792, 805, 1071, 1125, 1384) |
| F9 용어 혼용 | CLOSED | 준지수, 유일 조립, "지시 대" 0건. 글루, 접착, 강도, 끝 조립물, 일진수, 마하니, 체인 0건 (4개 파일) |
| F10 부록 링크 | CLOSED | 02 부록에 부분지수 시간, 카운터, 협력 결합 있음. 03 부록에 NP-완전, 부분지수 시간, 교환 논증 있음. "다대일"은 본문에서 빠짐 |
| F11 캡션과 번호 | CLOSED | 캡션 25개 모두 두 문장, 둘째 문장 "왜:", 출처 폴더 있음 (`v5/caps.py`). 그림 번호가 1–15로 이어짐. 케이스 지도는 "표 2"(941) |
| F12 질문 목록 | CLOSED | HTML 1125–1131과 03:109–115가 7개, 글자까지 같음. 02:5–8 범례가 ✅ PROVEN과 🟡 DERIVED-BY-HAND를 나눔 |
| F13 15어절 | CLOSED | 3. 회귀 점검 표 |
| 2.4 잔여 "세로 자름" | CLOSED | "자름", "자른", "절단선" 0건. HTML 554 "세로 열 하나에 타일이 2개뿐이라서", HTML 1418 `term-state`, 01:353 `term-column-state` 모두 "세로 열 하나" |
| N1 그림 7 묶음선 | CLOSED | `shots2x/crop_fig7.png`. 선이 라벨 위로 떨어져 있다 |
| N2 Step 6 강조 상자 | CLOSED | `shots2x/crop_f2k4.png`. 채움 없이 노랑 테두리만 남았다. 글자와 결합 색이 범례와 같다 |
| N3 그림 1 노랑 | CLOSED | `shots/viz-1.png`. 열린 경우가 파랑 점선이고 범례 줄(317) "그림 1의 열린 경우"와 맞는다 |
| N4 notes 139 | CLOSED | notes 139 "two cells … (1) the exact τ = 2 interior-seed value, (2) the exact τ = 1 value" |
| N5 Mahaney 진술, 7순위 문구 | PARTLY | 아래 |
| N6 NP, P 단독 | PARTLY | 아래 |

### N5. PARTLY

- 닫힘: Mahaney 정리 진술이 5개 파일 모두 NP-완전 꼴이다 (notes 212, 01:374, 02:178, 02:276, 03:136, HTML 1410). HTML 1410은 NP-어려움 꼴을 덧붙여 설명한다.
- 열림: 7순위 문구가 아직 파일마다 다르다.

| 파일 | 7순위 문구 |
| --- | --- |
| notes 218 | NP-hardness, "unary or canonical cell-list encoding" |
| `02_possible_solutions.md:184` | NP-완전 증명, "단항 인코딩과 칸 목록 인코딩에서" |
| `study_tips.html:1047` | NP-어려움 증명, "단항 인코딩에서는" (칸 목록이 빠짐) |

- 분류: 구현 문제 → `sonnet-writer`.

### N6. PARTLY

- 닫힘: HTML은 NP, P를 모두 풀어 쓴다. 남은 1412의 "P라 부름"은 다항 시간 용어 정의 자체다.
- 열림: 세 문서가 NP-완전을 `한글(약어)` 꼴로만 쓴다. 영어 전체 이름이 없다.
  - `style.md` §4 표: 한국어 문서의 약어는 `한글(full name, 약어)`다.
  - 위치: `01_study_guide.md:374`, `02_possible_solutions.md:65, 178, 184, 276`, `03_plan_and_design.md:37, 136`.
  - 예: "비결정 다항 시간 완전(NP-complete)". HTML은 "비결정적 다항 시간 완전(nondeterministic polynomial time complete, NP-complete)"이다.
- 분류: 구현 문제 → `sonnet-writer`.

## 2. review_04 §4 F1–F8 상태

| ID | 상태 | 근거 |
| --- | --- | --- |
| F1 "세로 자름" 3곳 | CLOSED | HTML 554, HTML 1418, 01:353. "바꿔 끼울" 0건. 1418은 "복사할 수 있음 (증명: [S-MTS-2] 정리 3.1)" |
| F2 notes 상수 나눔 | CLOSED | notes 126 "Which part is which … 2t(t + 1) gives about √n / 2. A looser count gives √n / 4." WML은 UNVERIFIED |
| F3 가이드와 HTML 상수 나눔 | CLOSED | 01:173–178. HTML Step 5 상자(`shots/viz-5.png`) "생성 가능 단계는 [S-MTS-2]가 증명합니다", 목록 4–5 (HTML 595–597) |
| F4 정규형과 Mahaney 꼴 | CLOSED | "k ≥ n + 1" 고정 예 입력, 단항 또는 고정 폭: notes 212, 02:178, HTML 1041, 01, 03 각 1곳. Mahaney는 한 꼴(NP-완전)로 통일. review_04가 요구한 "한 꼴"을 만족한다 |
| F5 안쪽 시드 상한 | CLOSED | HTML 그림 1 상자(`shots/viz-1.png`) "상한 n + 1 (빗), O(√n) (두 팔 카운터, 손 유도)". 표 2 "Θ(√n) 손 유도". 표 3 "n + 1 (빗, F3) … ≤ 4√2·√n + O(1)". `02_possible_solutions.md:33` "t ≤ 4√2·√n + O(1)" |
| F6 고정 시드 탐색 상한 | CLOSED | notes 213. 02:179도 반영. HTML 1042는 빠짐 (M2) |
| F7 위 줄 시드 뒤집기 | CLOSED | notes 216. 02:182도 반영. HTML 1045는 빠짐 (M2) |
| F8 Step 6 "설명용 예시" 배지 | CLOSED | `shots/f2k4.png`. 배지가 아닌 보통 글자다 |

## 3. 회귀 점검

### 3.1 렌더 (`answering.md` §3, `tips-page.md` §7)

- 방법: 헤드리스(headless) Chrome, 폭 1040px, 54상태. review_03 하네스를 현재 페이지로 다시 만들었다.
- 누른 것: 상위 탭 5개, 하위 단계 21개, 단계 그림 3개의 모든 상태(6, 10, 6)와 "이전", 조립 보기 3상태, 차트 n = 22, 용어 링크 3개.
- 2배 배율 재렌더: 그림 7, Step 6 상태 3–5 (`shots2x/`).
- 눈으로 본 스크린샷: viz-1, viz-2, viz-5, f1k9, f2k4, now-1, asmN8, chN22, now-4, papers-1, 2배 확대 4장.

| 점검 | 결과 |
| --- | --- |
| JS 오류, console.error/warn | PASS. 54상태 모두 0 |
| 가로 스크롤 (`scrollWidth > clientWidth`) | PASS. 0 |
| 표 상자 안 가로 넘침 | PASS. 0 |
| SVG 글자 겹침, SVG 밖 글자 (탐침) | PASS. 0 |
| 단계 버튼 | PASS. 첫 상태 "이전" 꺼짐, 끝 상태 "다음" 꺼짐, 카운터 값 맞음 |
| 용어 링크 → 용어 탭 | PASS. 3개 모두 `#terms` |
| 단계 상자, "Step k of N", 목록 일치 | PASS. 탭 0: 8, 탭 1: 6, 탭 2: 3, 탭 3: 4 |
| `·` 나열 | PASS. 본문 0건. 탭 이름 1건은 라벨 |
| "Abbreviations:" 줄 | PASS. 0건 |
| `<title>` | PASS. `HACK · 2×n 최소 타일 집합 학습 팁` |
| 밝은 테마만 | PASS |

- 참고: 하네스 `asmN8` 상태는 클릭 순서 때문에 n을 바꾼 뒤 처음 상태로 돌아간다. 페이지 문제가 아니다.

### 3.2 번호와 참조

| 점검 | 결과 | 근거 |
| --- | --- | --- |
| 그림 1–15 | PASS | 360, 412, 445, 500, 517, 554, 585, 684, 723, 771, 843, 879, 909, 1211, 1274. 문서 순서대로, 빈 번호 없음 |
| 표 1–10 | PASS | 918, 941, 972, 992, 1051, 1117, 1188, 1232, 1303, 1365 |
| 본문 참조 | PASS | 317 "그림 1의 열린 경우"는 그림 1 범례. 941 "표 3에서 칸마다 근거"는 표 3(케이스 네 칸)을 가리킨다 |
| SVG마다 번호 캡션 | PASS | SVG 14개와 JS 조립 화면 1개 모두 그림 번호가 있다 |
| 자료 표마다 번호 | 경미 | M3 |

### 3.3 링크, 문장 부호, 문장 길이

| 점검 | 결과 |
| --- | --- |
| HTML `href="#…"` 62개 | PASS. 없는 대상 0 |
| HTML 부록 `term-` 43개 | PASS. 모두 본문에서 링크됨 |
| 문서 앵커 (01, 02, 03) | PASS. 없는 대상은 01의 `#용어-부록-terms-appendix` 하나. Markdown 제목 앵커라 렌더러에서 해결된다 |
| 줄표 grep (`style.md` §3 명령) | PASS. 4개 파일 모두 0 |
| 세미콜론, 원 숫자 | PASS. 0건 |

15어절 초과 비율 (`static_checks.py`, review_03과 같은 방법):

| 파일 | review_03 | 지금 |
| --- | --- | --- |
| `study_tips.html` | 20 / 332 (6.0%) | 2 / 363 (0.6%) |
| `01_study_guide.md` | 7 / 253 (2.8%) | 0 / 292 (0.0%) |
| `02_possible_solutions.md` | 11 / 224 (4.9%) | 4 / 298 (1.3%) |
| `03_plan_and_design.md` | (경계) | 0 / 160 (0.0%) |

- HTML 2건 중 1건은 영어 논문 제목 원문이다 (1203 근처, S-MTS-8).

### 3.4 용어 8개 (HTML, 01, 02, 03 등장 횟수)

| 용어 | HTML | 01 | 02 | 03 | 옛 이름 |
| --- | --- | --- | --- | --- | --- |
| 결합 | 67 | 22 | 16 | 2 | 글루, 접착 0 |
| 세기 | 48 | 9 | 9 | 2 | 강도 0 |
| 단항 | 8 | 4 | 4 | 5 | 일진수 0 |
| 부분지수 | 2 | 0 | 2 | 5 | 준지수 0 |
| 협력 결합 | 10 | 3 | 2 | 0 | 협동 0 |
| 결정적 조립 | 11 | 11 | 7 | 6 | 지시, 유일 조립 0 |
| 종단 조립체 | 7 | 6 | 2 | 2 | 끝 조립물 0 |
| 사슬 | 4 | 1 | 4 | 0 | 체인 0 |

- PASS. 0회는 그 문서가 그 대상을 다루지 않는 경우다.
- 8개 밖의 용어 차이는 M4에 모았다.

### 3.5 질문 7개

- PASS. HTML 1125–1131과 `03_plan_and_design.md:109–115`가 순서와 글자까지 같다.
- 단, 5번 질문 끝 괄호는 M1에 넣었다.

### 3.6 작성 지시 누출

- ISSUE (경미). M1.
- 누출이 아닌 것: 01:274–278의 "쓰지 마"는 논문을 쓸 학생에게 주는 함정 목록이다. 03은 팀 계획 문서라 실행 규칙(103–105)이 본문에 맞다.

## 4. 새 지적

### M1. minor: 작성 지시와 하네스 용어가 독자 본문에 남음

- `study_tips.html:1119`: "클러스터 제출은 메인 세션이 소유자 승인 후에 합니다. 에이전트는 제출하지 않습니다."
- `02_possible_solutions.md:220–221`: "이 머신 규칙상 로컬에서 돌리지 않는다. 메인 세션만 제출한다. 에이전트는 작업 스크립트를 쓰고 넘긴다."
- 메인 세션, 에이전트는 작성 파이프라인 용어다. 초보자 독자에게 뜻이 없다.
- HTML 1129, 03:113 (질문 5): "(확인하지 못한 질문입니다. 사실로 단정하지 않습니다.)" 출제자에게 그대로 물을 질문 안에 작성자 메모가 있다.
- 분류: 구현 문제 → `sonnet-writer`.

### M2. minor: HTML 연구 방향 표가 review_04 F6, F7 반영을 빠뜨림

- `study_tips.html:1042` 2순위: 고정 시드 칸이면 두 팔 상한 4⌈√a⌉ + 4⌈√b⌉ + O(1)까지 찾는다는 조건이 없다. notes 213, 02:179에는 있다.
- `study_tips.html:1045` 5순위: "위 줄 시드 칸이면 위아래로도 뒤집는다"가 없다. notes 216, 02:182에는 있다.
- review_04 F6, F7은 notes만 지정했다. 그래서 F6, F7 자체는 닫혔다. 파일 사이 내용 차이로 남는다.
- 분류: 구현 문제 → `sonnet-writer`.

### M3. minor: 번호 없는 자료 표 2개

- `study_tips.html:800` 추상 타일 조립 모델 용어 표 (`h3` 제목, 캡션 없음).
- `study_tips.html:999` 손 유도 카운터 타일 묶음 표 (`h3` 제목, 캡션 없음).
- 규칙: `rules/visualization.md` §3 "모든 그림, 흐름도, 자료 표에 번호와 캡션을 단다".
- 지금 번호 1–10에는 빈 번호가 없다. 이 둘을 넣으면 번호가 다시 매겨진다.
- review_03 판(`x_study_tips_v3.html`)에도 같았다. 회귀가 아니다.
- 분류: 구현 문제 → `sonnet-writer`.

### M4. minor: 8개 밖 용어가 파일 사이, 파일 안에서 갈림

| 대상 | HTML | 문서 |
| --- | --- | --- |
| nondeterministic | 비결정적 다항 시간 (15) | 비결정 다항 시간 (01: 4, 02: 7, 03: 5) |
| mismatch 영어 병기 | glue mismatch (950, 1415) | binding-domain mismatch (01, 02) |
| canonical form | 표준형 | 본문 정규형, 부록 표준형 (01:269 대 01:380, 02:178 대 02:282, 03:42 대 03:142) |
| corner lemma | 모서리로 옮기기 보조정리 (1043) | 모서리로 일반성을 잃지 않는다는 보조정리 (02:180), 모서리 일반성 보조정리 (03:54) |
| terminal shape | 끝 모양 (1113, 표 6 R2) | 종단 모양 (03:107) |

- 파일 안 동의어(정규형, 표준형)는 `style.md` §2 "용어 고정" 위반이다.
- 분류: 구현 문제 → `sonnet-writer`.

### M5. minor (외관): Step 6 강조 테두리가 일부만 보임

- 위치: `study_tips.html:611–616` (`rect.hnew`, 타일보다 5px 큰 상자, 타일 그룹 앞에 그림).
- 증거: `shots2x/crop_f2k4.png`. 오른쪽, 아래 변은 나중에 그린 이웃 타일이 덮는다. 노랑이 "ㄱ" 꼴로만 보인다.
- 어느 타일인지는 읽힌다. 글자는 가리지 않는다.
- 분류: 구현 문제 → `sonnet-writer`.

## 5. READMME.md

- PASS. 저장소 뿌리의 파일 이름은 정말 `READMME.md`다 (`ls -a` 결과). `README.md`는 없다.

## 라우팅 요약

| 묶음 | 항목 | 보낼 곳 |
| --- | --- | --- |
| 구현 문제 | N5, N6, M1, M2, M3, M4, M5 | `sonnet-writer` |
| 추론 문제 | 없음 | 해당 없음 |
| 사다리, 위계 | 없음 | 해당 없음 |

- 남은 항목은 모두 경미다. 고칠지는 메인 세션과 소유자가 정한다.
- 이번이 같은 접근의 두 번째 게이트 검토라면, 세 번째 순환은 `.claude/CLAUDE.md` 상한상 허용되지 않는다. `recover` 또는 소유자 결정 몫이다.

## 용어 부록 (terms appendix)

- **헤드리스(headless) Chrome**: 화면 없이 페이지를 그리는 Chrome 실행 방식.
- **탐침(probe) 스크립트**: 페이지 사본에 넣어 상태를 바꾸고 측정값을 기록하는 검사용 스크립트.
- **어절(eojeol)**: 공백으로 나눈 한국어 단위. 문장 길이를 세는 단위.
- **비결정적 다항 시간 완전(nondeterministic polynomial time complete, NP-complete)**: 비결정적 다항 시간 부류에서 가장 어려운 결정 문제의 부류.
- **창 영화 보조정리(Window Movie Lemma, WML)**: 창 하나를 지나는 결합 기록으로 펌핑을 엄밀하게 하는 도구.
