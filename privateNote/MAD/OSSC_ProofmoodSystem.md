OSSC-ProofmoodSystem

술어논리에서, 算(서브루틴)•數 중심으로 수학하는 체계 

# O.S.S.C. Swany Subrootine Calculate Proofmood System

O.S.S.C.법 : (x = y), Φ ⊢ (Φ [x := y])

 - S. 「강한 수학적 귀납법」の「매거적 표현」
 - W. 「약한 수학적 귀납법」の「매거적 표현」
 - A. Subrootine Algorithn の 「순차표현」
 - N. 「진리열 수학적 귀납법」の 「매거적 표헌」

 - Y. 삼단논법 flow
    - 갹 ≜ ㄱㅑㄱ
    - 꺅 ≜ ㄱ갹
    - 갺 ≜ 갹ㄱ
    - 꺆 ≜ ㄱ갺

## 잔 표기법

### Code-Comment

표기 [NOTE: x] ≜ (λx.)(x)

### Segment

표기 Step t. Φ | [SEG : x] ≜ x = Φ

### 수식나열자 표기법
표기 step t. Φ | p ≜ [stepₜ := (Φ, p)]

## 개념 on 내용물 (구성)

### 매거적 표현

1. 오컴의 면도날에 걸리지 않은 부분을 매거적 귀납법으로
2. 오컴의 면도날에 걸린 재대로된 증명과정을 그 옆에 표기하여
3. 명시된 방식의 귀납법으로 증명됨을 보이는 표현법

### 순차표현

 - 미지수 이용
 - 상수할당
 - 미지수 반환
 - 계산

## 삼단논법 flow

O.S.S.C.법을 이용해서,

1. Φ ⊢ {(x = y) ⊢ (Φ [x := y])}로 삼단논법하거나
2. (x = y) ⊢ {Φ ⊢ (Φ [x := y])}로 삼단논법하여서
3. 대전제 (옆에 명시) ⊢ {소전제 (현재 칸) ⊢ 결론}

를 체이닝한다.

## Forms (형식, 작성 방식, 작성, 글)

- 형식 종류
     - Pettern : 귀납적 페턴이나 직관
     - Conjuncture : 추측
     - Proof : Conjuncture의 증명

- 구체적 명칭
     - Swany-X Pettern
     - Swany-S Pettern
     - Swany-W Pettern
     - Swany-N Pettern
     - Swany-Y Pettern : 직관에서 옴
     - Swany-X Conjuncture
     - Swany-S Conjunture
     - Swany-W Conjunture
     - Swany-N Conjuncture
     - Swany-Y Conjuncture
     - Swany-X Proof : 반례 귀류법
     - Swany-S Proof
     - Swany-W Proof
     - Swany-N Proof
     - Swany-Y Proof
     - Swany-A defination : 단순 정의

### (substandard) 노트 보조 부호

주석이 설명충이 되면 필요한 설명부호다

- 판단(details.) (변별, 분류, 비교•대조)
     - 구분하는 설명(explain)전제
     - 해시태그 : 분류
     - 변별 (N.B.) : 비교•대조 표
     - 비교•대조 표 : 「공통•차이 열」로 만든표
- 설명 (descript.)
     - 논•서술•해석(explain)기반
     - 예시(ex, e.g.) 표기

## defination of beautiful (지향해야할 가치)

 - 가독성은 교정하면 되니 둘제치고,
 - 내용이 핵심이다.
 - Simple (최소 복잡도) & Easy (쉬움)