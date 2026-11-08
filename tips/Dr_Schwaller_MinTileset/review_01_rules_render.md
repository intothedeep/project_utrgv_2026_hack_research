# Review 01: 규칙과 렌더 점검 (study_tips.html + 문서 3개)

- 검토자: reviewer 에이전트. 검증만 했고 대상 파일은 고치지 않았다 (2026-11-07).
- 대상: `study_tips.html`, `01_study_guide.md`, `02_possible_solutions.md`, `03_plan_and_design.md`.
- 사실 출처: `00_research_notes.md` (아래 "notes").
- 렌더 스크립트와 스크린샷: `/private/tmp/claude-501/-Users-tio-Documents-project-utrgv-2026-hack-research/957682e3-7cb7-4d00-a99a-596fbb695b3a/scratchpad/render/`.

## 판정

**ISSUE.** 차단(blocker) 0, 중대(major) 5, 경미(minor) 13.

```
렌더/구조 ── PASS (오류 0, 가로 스크롤 0, 단계 수 일치)
문장 부호 ── PASS (줄표 0, 세미콜론 0, 원 숫자 0)
사실 추적 ── ISSUE (상태 표시 불일치, 출처 내부 모순을 단정)
그림     ── ISSUE (Step 6 라벨 가림, 색 뜻 뒤집힘)
용어/문장 ── ISSUE (경미: 약어 단독, 용어 혼용, 긴 문장 8.3%)
```

- 사다리 점검 L1–L4: 해당 없음. 시스템이나 앱 작업이 아니다.
- 위계 점검 H1–H2: 해당 없음. 디스패치가 PLAN.md나 AC 목록을 주지 않았다.

## 1. tips-page.md §7 점검표

| 항목 | 결과 | 근거 |
| --- | --- | --- |
| 단계 상자 N개, "Step k of N", 위 목록과 일치 | PASS | 탭 0: 8/8, 탭 1: 6/6, 탭 2: 3/3, 탭 3: 4/4. 하위 탭 단추 수와 `stepno` 값이 같다 |
| `·` 나열이 본문 문장에 없다 | PASS | 남은 `·`는 라벨(274, 288)과 곱셈 기호(`m·D`, `c·√n`)뿐 |
| "Abbreviations:" 줄 0개 | PASS | `grep -i 'abbreviation\|약어:'` 0건 |
| 모든 숫자에 출처가 있다 | ISSUE (경미) | §5 참조. 계산값 몇 개가 notes에 없다 |
| 효과 큰 순서 | 해당 없음 | run 결과 페이지가 아니다 |
| 설명용 값 표시 | PASS | Step 6 (587), 그림 7 (572), 탭 1 Step 2 (848)에 표시 있음 |
| 렌더 확인 1040px | PASS | §2 참조 |
| `<title>`이 프로젝트 약어로 시작 | PASS | `HACK · ...`. 루트 `CLAUDE.md` 6행과 맞다 |

## 2. answering.md §3 렌더 점검

- 방법: 헤드리스 Chrome, 폭 1040px, 상태 52개. Playwright는 없어서 쓰지 않았다.
- 페이지 사본에 탐침 스크립트를 넣었다. 탭을 고르고, 이전/다음을 누르고, 결과를 기록한다.
- 누른 것: 상위 탭 5개, 하위 단계 21개, 단계 그림 3개(6, 10, 6 상태)의 모든 상태와 "이전".
- 추가로 누른 것: 조립 보기(n = 1, 8, τ = 1), 차트 n 슬라이더(22), 용어 링크.

| 점검 | 결과 |
| --- | --- |
| JS 오류, console.error/warn | 52개 상태 모두 0 |
| 가로 스크롤 (`scrollWidth > clientWidth`) | 0 |
| 표 상자 안 가로 넘침 | 0 |
| SVG 글자끼리 겹침 (탐침) | 0. 단 글자와 도형 겹침은 탐침이 못 잡는다. 눈으로 본 결과는 F4 |
| 단계 버튼 | 첫 상태에서 "이전" 꺼짐, 끝 상태에서 "다음" 꺼짐, 카운터 값 맞음 |
| 밝은 테마만 | PASS. `prefers-color-scheme`, `.dark` 0건 |
| `href="#..."` 45개가 있는 `id`로 간다 | PASS. 없는 대상 0 |
| 용어 링크 → 용어 탭, "돌아가기" 단추 | PASS (`term-pumping`으로 확인) |
| 부록 용어 33개가 모두 본문에서 링크됨 | ISSUE (경미). F10 |

## 3. style.md 점검

| 점검 | 결과 |
| --- | --- |
| §3 줄표 grep (4개 파일) | PASS. 0건 |
| 본문 세미콜론 (CSS/JS 제외) | PASS. 0건 |
| 원 숫자 | PASS. 0건 |
| §4 약어 단독 | ISSUE (경미). F8 |
| §2 용어 고정 | ISSUE (경미). F9 |
| 한국어 문장 15어절 이하 | ISSUE (경미). F13 |

## 4. figures.md 점검

| 점검 | 결과 |
| --- | --- |
| 캡션 두 문장 이하, 둘째 문장 "왜:" | 23개 중 22개 PASS. F11 |
| 출처 폴더 | 캡션 23개 PASS. 표 1, 표 3은 캡션이 아니다 (F11) |
| 범례가 그림 위 | 대부분 PASS. 범례가 없는 그림 2개 (F5) |
| 겹침 | ISSUE (중대). F4 |

## 5. 사실 추적

notes에 같은 값이 있는 것 (PASS):

| 값 | 페이지/문서 위치 | notes 위치 |
| --- | --- | --- |
| 하한 √n / 2, 시드 위치 무관 | HTML 344, 887. 01:32. 02:63 | 78, 111 |
| 상한 4⌈√n⌉ + 2, τ = 2, 모서리 시드 | HTML 344, 888. 01:34. 02:64 | 79 |
| n = 100 → 5 ≤ t ≤ 42, n = 10,000 → 50 ≤ t ≤ 402 | HTML 902, JS 표. 01:111–112. 02:65–66 | 80 |
| n = 49, 26종 (빗 50) | HTML 689, 696, 993. 02:93 | 151 |
| n = 10,035, 349종, D = 58, m = 173 | HTML 680, 701, 994. 02:94 | 151 |
| m + 3D + 2, n = 1 + m·D, 약 3.46√n | HTML 943, 987, 992. 02:83, 92 | 141–150 |
| 빗 n + 1, 2×1은 2종 | HTML 443, 964. 02:67–68 | 102–110 |
| 작은 n 표 (n = 1..6) | HTML 964–969. 02:172–177 | 158–165 |
| 출처 12건: 확인 4, 부분 6, 미확인 2 | HTML 1279 | 3 |
| CONJECTURE c ∈ [1/2, 2√3] | HTML 945. 02:111–112 | 154 |
| 순위 1–7 연구 방향 | HTML 1019–1025. 02:140–146 | 187–193 |

notes에 없지만 notes의 식으로 계산한 값 (산술은 검토자가 다시 확인함):

| 값 | 위치 | 확인 |
| --- | --- | --- |
| m = 3, D = 2 → n = 7, 11종 | HTML 587, 678 | 1 + 3·2 = 7, 3 + 6 + 2 = 11. 설명용 표시 있음 |
| n = 49 Aggarwal 상한 30, 하한 3.5 | HTML 697–698 | 4·7 + 2 = 30, 7 / 2 = 3.5. 캡션에 "식으로 계산" 있음 |
| n = 10,035 Aggarwal 상한 406, 하한 50.1 | HTML 702–703 | ⌈100.17⌉ = 101 → 406, 100.17 / 2 = 50.09 |
| 약 29배 | HTML 689 | 10,036 / 349 = 28.8 |
| 막대 길이 (로그 눈금) | HTML 695–703 | 10배당 158px. 8개 막대 모두 ±1px 안 |
| n = 22에서 처음 상한 < 빗 | HTML JS 1490 | 4·5 + 2 = 22 < 23 |

상태 표시와 일관성 문제는 F1, F2, F3, F7, F12에 적었다.

## Findings

### F1. major: 빗이 "어떤 시드든" 된다는 주장을 출처 모순 그대로 단정함

- 위치: `study_tips.html:493-507` (그림 5), `study_tips.html:732` ("빗은 어떤 시드든 가능", "끝 ✓"), `01_study_guide.md:85` ("모든 온도와 시드 위치").
- 반대 진술: `02_possible_solutions.md:67` ("모서리 시드"), `study_tips.html:938` (두 문장이 어긋나니 확인 필요).
- 출처: notes 106은 "corner seed"라 쓴다. notes 123은 "for any seed position"이라 쓴다. notes 안에서 모순이다.
- 왜 문제: source-citation 규칙은 모순된 주장을 단정하지 못하게 한다. 같은 페이지의 표 2만 모순을 밝힌다. 그림 5와 그림 10은 끝난 사실로 보인다.
- 분류: 추론 문제(reasoning issue). researcher가 notes 안의 F3 범위를 정해야 한다.

### F2. major: 같은 주장(τ = 1, 불일치 없음 → n + 1)에 상태 표시가 셋

- notes 120: "PROVEN-conditional (snippet only, partial)".
- `study_tips.html:354`: 회색 `UNVERIFIED`.
- `study_tips.html:915-916`: 노랑(`st q`, 범례상 DERIVED-BY-HAND 색) "조건부 n + 1".
- `study_tips.html:935, 940`: "PROVEN-conditional"을 DERIVED-BY-HAND 노랑으로 칠함.
- 문서: `02_possible_solutions.md:28, 69`는 🟡.
- 같은 노랑을 "부분 확인"에도 쓴다: `study_tips.html:1202, 1204, 1264-1269, 1275, 1327, 1332-1336`.
- 왜 문제: 머리말 범례(280–283)는 노랑을 "손으로 유도"로 정의한다. 문헌 결과가 손 유도처럼 보인다.
- 분류: 구현 문제(implementation issue).

### F3. major: "열린 곳은 하나"가 notes와 페이지 자신에 어긋남

- 위치: `study_tips.html:310` ("열린 곳은 하나입니다"), 그림 1의 τ = 1 상자(339–342)는 열림 표시가 없다.
- 반대 근거: notes 125 "The exact τ = 1 value is open as far as found".
- 같은 페이지 `study_tips.html:1302`, `02_possible_solutions.md:29`(🔴)는 τ = 1 정확값을 빈칸으로 둔다.
- 분류: 추론 문제. 결론 문장이 notes보다 강하다.

### F4. major: Step 6 그림에서 접착 라벨이 가려짐

- 위치: `study_tips.html:598, 602, 607, 609, 613, 618, 620` (라벨 `r₁`, `q`, `p₁`, `p₂`, `d₁`, `r₀`).
- 증거: 2배 렌더 `.../scratchpad/render/shots/crop_f2.png`.
- 라벨의 중심이 타일 경계선 위(x = 498, 420, 342)라서 선이 글자를 지난다.
- 마지막 상태에서 블록 2 타일(623–628)이 X₁의 `r₀` 라벨을 덮는다. "0"만 보인다.
- 규칙: `rules/figures.md` §1 (글자가 데이터나 선에 가리지 않는다).
- 분류: 구현 문제.

### F5. major: 접착 세기 색의 뜻이 그림마다 뒤집힘

- `study_tips.html:361` (탭 0 그림 2): 청록 = 세기 1, 주황 = 세기 2.
- `study_tips.html:808-825` (탭 1 그림 1): 청록 = 세기 2, 주황 = 세기 1, 자홍 = 세기 1. 범례가 없다.
- `study_tips.html:448-463` (그림 4): 타일 채움에 청록과 주황을 다시 쓴다. 바로 위 범례(445)에서는 같은 색이 접착 종류다.
- `study_tips.html:413-425` (그림 3): 접착 색과 노랑 강조의 범례가 없다.
- 규칙: `rules/visualization.md` §5 (한 뜻에 한 색), `rules/figures.md` §2 (모든 색을 범례에서 설명).
- 분류: 구현 문제.

### F6. minor: 계산값이 notes에 없음 (값은 맞음)

- 위치: `study_tips.html:587, 689, 697-703`, JS 1490 (n = 22).
- 모두 notes의 식으로 다시 계산했고 맞다 (§5 표). 캡션이나 배지가 계산값임을 밝힌다.
- "약 29배"(689)만 계산이라는 표시가 없다.
- 문서 쪽: `03_plan_and_design.md:7` (14.5시간), `03_plan_and_design.md:47` (Discord #submissions), `01_study_guide.md:5` (해커톤 시간)은 notes가 아니라 저장소 README와 루트 `CLAUDE.md`가 출처다.
- `01_study_guide.md:5`: 파일 이름 오타 "READMME.md".

### F7. minor: S-MTS-11, 12의 상태가 표마다 다름

- `study_tips.html:1265-1266` (표 8): "부분 확인".
- `study_tips.html:1337` (표 9): "미확인".
- notes 219–220: "partial ... Title from memory: UNVERIFIED". 표 9가 출처 상태를 제목 상태로 바꿨다.

### F8. minor: 약어 단독 사용 (style.md §4)

- `aTAM`: `study_tips.html:1091` ("aTAM 시뮬레이션").
- `Thm`: 10곳 (515, 902, 932, 942, 943, 947, 1009, 1055, 1065, 1268).
- `Fig`: 1055. `OPT`: 1022. `WLOG`: 1021 (풀이 없음).
- `UTRGV`: 274, 278. `01_study_guide.md:230`, `03_plan_and_design.md:95`.
- `CPU`: `01_study_guide.md:237`.
- `DNA` 형식: `study_tips.html:1201, 1383`은 "DNA(디옥시리보핵산, deoxyribonucleic acid)". 규칙 형식은 "디옥시리보핵산(deoxyribonucleic acid, DNA)".
- τ: HTML은 "온도(temperature) τ" (310, 793, 1359). 문서는 "온도(temperature, τ)". 뒤의 "τ = 2"는 대부분 홀로 쓴다.

### F9. minor: 용어 혼용 (style.md §2 용어 고정)

| 대상 | 페이지 안 | 문서 |
| --- | --- | --- |
| cooperation | "협력 결합(cooperative binding)" 404, "협동 결합(cooperation)" 794, 1049, 1360 | 협력 결합 |
| directed | 유일 조립 | 지시 조립 |
| glue, strength | 글루, 강도 | 접착 라벨, 접착 세기 |
| terminal assembly | 끝 조립물 | 종단 조립체 |
| subexponential | 부분지수 시간 | 준지수 시간 (02:141) |
| Mahaney | Mahaney 정리 | 마하니 정리 |

- 뜻도 다르다: 부록 1360은 협동 결합을 "세기 1 접착 둘"로만 정의한다. 표 794와 notes 15는 "세기 2 하나"도 포함한다.

### F10. minor: 부록 용어 2개가 본문 링크가 없음

- `term-assembly` (1363), `term-null` (1387).
- 본문에 "널(null)"이 10번 넘게 나오지만 링크가 없다 (예: 424, 468, 629, 865, 873).
- 문서: `02_possible_solutions.md`와 `03_plan_and_design.md`의 부록에 본문 용어가 빠졌다. 예: 02의 지시 조립, 엄격 조립, 시드, 교환 논증. 03의 빗 구성, 시드.

### F11. minor: 캡션과 번호

- `study_tips.html:865` (탭 1 그림 2): 세 문장. 둘째 문장이 "왜:"가 아니다.
- `study_tips.html:902` (표 1), `study_tips.html:973` (표 3): `figcaption`이 아닌 `p.note`. "왜:"가 없다. 표 1은 출처 경로도 없다.
- `study_tips.html:923`: 표인데 "그림 4"로 번호를 붙였다.
- 그림 번호가 탭마다 1부터 다시 시작한다 ("그림 1"이 352, 830 두 곳).
- `study_tips.html:894`: "상수배(약 8)"를 사실처럼 쓴다. notes 81은 추정(inference)이다.

### F12. minor: 출제자에게 물을 질문이 HTML과 03 문서에서 다름

- `study_tips.html:1103-1107`: τ, directed/strict, 인코딩, 회전, 모서리 식의 꼴.
- `03_plan_and_design.md:91-95`: τ, directed/strict, 인코딩, 네 모서리 중 어느 것, Schweller 신원.
- 양쪽에 둘씩 빠졌다. `02_possible_solutions.md:6`의 ✅는 PROVEN과 DERIVED-BY-HAND를 한 기호로 묶는다. HTML은 둘을 나눈다.

### F13. minor: 15어절을 넘는 문장

- HTML 본문 문장 290개 중 24개가 넘는다 (8.3%). 일부는 표 칸을 이어 붙인 결과라 실제 위반은 이보다 적다.
- 확실한 예: 902 (28어절), 673 (23), 436 (19), 712 (19), 1166 (19).
- 문서: 01은 217개 중 4개 (1.8%), 02는 182개 중 7개 (3.8%), 03은 116개 중 2개 (1.7%).
- 예: `02_possible_solutions.md:142` (23어절), `03_plan_and_design.md:30` (19어절).

## 렌더 하네스 메모

- 하네스의 `asmN8` 상태는 n을 바꾸기 전에 클릭해서 k가 1로 되돌아갔다. 페이지 버그가 아니다. `asm9` 상태로 따로 확인했다.
- 첫 용어 클릭 시험에서 "돌아가기"가 안 보였다. 하네스의 비동기 hashchange 탓이었다. `termclick2`에서 정상으로 확인했다.

## 용어 부록 (terms appendix)

- **헤드리스(headless) Chrome**: 화면 없이 페이지를 그리는 Chrome 실행 방식.
- **탐침(probe) 스크립트**: 페이지 사본에 넣어 상태를 바꾸고 측정값을 기록하는 검사용 스크립트.
- **추상 타일 조립 모델(abstract Tile Assembly Model, aTAM)**: 타일이 접착 세기 합이 온도 이상일 때 붙는 모델.
- **어절(eojeol)**: 공백으로 나눈 한국어 단위. 문장 길이를 세는 단위.
