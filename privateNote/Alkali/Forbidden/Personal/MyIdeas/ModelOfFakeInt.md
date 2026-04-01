# ModelOfFakeInt

취미로 만든 이상한거

# 3줄요약

FakeInt라는 봄자연수 행렬로 표현한 정수 소개
물론 행렬에 동치류를 줘야함
쥰@@내 골때리네 ㅋㅋㅋㅋ 이거 재밌다.

## 용어정의

주사랑 빈사라는 개념은 아리스토텔레스 정언논리를 취미로 배우면 잘 이해 ㄱㄴ하니 걍 봐주셈

### 주사(피서술항)들의 정의

페아노 공리계 1 공리

PeanoAxiom₁(Nₖ, k) : k ∈ Nₖ

페아노 공리계 2 공리

PeanoAxiom₂(Nₖ, k s) : n ∈ Nₖ → s(n) ∈ Nₖ

페아노 공리계 3 공리

PeanoAxiom₃(Nₖ, k, s) : ∄n ∈ Nₖ, s(n) = k

페아노 공리계 4 공리

PeanoAxiom₄(Nₖ, k, s) : ∀n, m ∈ Nₖ, s(n) = s(m) → n = m

페아노 공리계 5 공리

PeanoAxiom₅(Nₖ, k, s) : ∀X ⊆ Nₖ, PeanoAxiom₁(X, k, s) ∧ PeanoAxioms₃(X, k, s) → X = Nₖ

페아노 공리계

PeanoAxioms(Nₖ, k, s) : PeanoAxiom₁(Nₖ, k, s) ∧ PeanoAxiom₂(Nₖ, k, s) ∧ PeanoAxiom₃(Nₖ, k, s) ∧ PeanoAxiom₄(Nₖ, k, s) ∧ PeanoAxiom₅(Nₖ, k, s)

페아노 공리계를 만족하는 모델 M = <ℕₖ, k, (+1)>의 도메인 ℕₖ과 다음수 연산 s = (+1)의 정체

1. (+1)는 1만큼 더하는 함자다
2. ℕₖ는 k이상의 범자연수
3. 자연수 집합 ℕ ≜ ℕ₁
4. 범자연수 집합 𝕎 ≜ ℕ₀
5. 근데 사실 s도 폰 노이만 정의로 정의할수 있음.

### 빈사(서술어)들의 정의

술어 isSymmetricMatrix의 정의는 다음과 같다.

isSymmetricMatrix(M) : Mᵀ = M

대칭행렬임을 나타내는 술어다.

## ModelOfFakeInt

앞으로 행렬곱은 `@`라 적겠다.

그리고 아래의 단항술어(단항관계, 술어) isFakeInt및 상수 ZeroOfFakeInt, OneOfFakeInt, 이항함수(이항연산자) SubtractionOfFakeInt및 이항술어(이항관계) isSameFakeInt에 대해서, ModelOfFakeInt ≜ <isFakeInt, ZeroOfFakeInt, OneOfFakeInt, +, SubtractionOfFakeInt, @, isSameFakeInt>는 가환환을 이루는 모델이다.

1. ZeroOfFakeInt = [[0, 0], [0, 0]]
2. OneOfFakeInt = [[0, 1], [1, 0]]
3. SubtractionOfFakeInt(X, Y) ≜ X + ([[0, 1], [1, 0]] @ Y)
4. isFakeInt(M) : isSymmetricMatrix(M) ∧ isSymmetricMatrix(SubtractionOfFakeInt(ZeroOfFakeInt, M))
5. isSameFakeInt(X, Y) : (Y ≠ ZeroOfFakeInt) → isSameFakeInt(SubtractionOfFakeInt(X, Y), ZeroOfFakeInt) ∧ (Y = ZeroOfFakeInt) → (X = SubtractionOfFakeInt(ZeroOfFakeInt, X)) ∧ isFakeInt(X) ∧ isFakeInt(Y)

모델론상에서, 술어의 값은 모델에서 집합으로 배정되므로, isFakeInt엔 {M | isSymmetricMatrix(M) ∧ isSymmetricMatrix(SubtractionOfFakeInt(ZeroOfFakeInt, M))}가 배정되는거다.

아래 명제가 왜 전부 동치인지 알아보자 (그냥 12번째 1+1=2가 참이니까 1~11번까지 다 참이라는 소리다. ㅋㅋㅋㅋㅋㅋ)

TFAE

1. isFakeInt(ZeroOfFakeInt)
2. isFakeInt(OneOfFakeInt)
3. isFakeInt([[0, 1], [1, 0]])
4. [[0, 1], [1, 0]] @ [[0, 1], [1, 0]] = OneOfFakeInt
5. ∀isFakeInt(X), ZeroOfFakeInt + X = OneOfFakeInt @ X = X ∧ (∀isFakeInt(Y), isSameFakeInt(X + Y, Y + X) ∧ isSameFakeInt(X @ Y, Y @ X) ∧ isSameFakeInt((X + Y) + Z, X + (Y + Z)) ∧ (∀isFakeInt(Z), isSameFakeInt((X @ Y) @ Z, X @ (Y @ Z))))
6. ∀isFakeInt(X), ∀isFakeInt(Y), isFakeInt(SubtractionOfFakeInt(X, Y))
7. SubtractionOfFakeInt(ZeroOfFakeInt, OneOfFakeInt) = [[0, 1], [1, 0]]
8. ∀isFakeInt(X), isSameFakeInt(SubtractionOfFakeInt(X, X), 0)
9. isSameFakeInt(X, Y) → isFakeInt(X) ∧ isFakeInt(Y)
10. [[0, 1], [1, 0]] @ X = SubtractionOfFakeInt(ZeroOfFakeInt, X)
11. isSameFakeInt(X + isFakeInt(ZeroOfFakeInt, X), ZeroOfFakeInt)
12. 1 + 1 = 2

그냥 다들 알아서 머리로 eval했다고 보겠다. 나는 그냥 저거 보면 프로그래밍 코드 보듯 eval되니까, 남들도 되겠거니 한거다. ㅋㅋㅋㅋㅋ

### isWholeNumber및 isNegativeInteger술어

WholeNumber란, 범자연수의 영어 명칭임. ㄹㅇㅋㅋ

isWholeNumber(X) : ∃!n ∈ 𝕎, isSameFakeInt(X, n OneOfFakeInt)

딱봐도, 행렬 실수배한걸로 아주 쉽게 이해 가능하구먼 ㅋㅋㅋ

isNegativeInteger(X) : isFakeInt(X) ∧ ¬isWholeNumber(X)

그치 ㅋㅋㅋㅋ 범자연수 아닌 정수는 음의정수임 ㅋㅋㅋ

### isSameFakeInt의 동치성

1. isSameFakeInt(X, X) ↔ isSameFakeInt(SubtractionOfFakeInt(X, X), ZeroOfFakeInt)로 반사성 만족
2. isSameFakeInt(SubtractionOfFakeInt(X, Y), ZeroOfFakeInt) → isSameFakeInt(SubtractionOfFakeInt(Y, X), ZeroOfFakeInt)임 ㅋㅋ 왜냐면, [[0, 1], [1, 0]] @ SubtractionOfFakeInt(Y, X) = SubtractionOfFakeInt(X, Y)인데, isSameFakeInt(Z, ZeroOfFakeInt)를 만족하는 Z는 에초에 isSameFakeInt([[0, 1], [1, 0]] @ Z, Z)임 ㅋㅋㅋㅋㅋㅋ (마무리 짓지 않아도 여기서부턴 어떤 함의를 말하려는건지 뻔하니 생략함. 논리적 귀결임 ㅋㅋㅋ. 가능한 논리적 귀결을 많이 찾아보는것도 좋고.) 그래서 대칭성 만족
3. isSameFakeInt(SubtractionOfFakeInt(X, Y), ZeroOfFakeInt) ∧  isSameFakeInt(SubtractionOfFakeInt(Z, X), ZeroOfFakeInt) → isSameFakeInt(SubtractionOfFakeInt(Z, X), ZeroOfFakeInt) 임 ㅋㅋ SubtractionOfFakeInt(X, Y) + SubtractionOfFakeInt(Z, X) = SubtractionOfFakeInt(ZeroOfFakeInt, Y) + SubtractionOfFakeInt(ZeroOfFakeInt, X) + X + Z임 ㄹㅇㅋㅋ (마무리 짓지 않아도 여기서부턴 어떤 함의를 말하려는건지 뻔하니 생략함. 논리적 귀결임 ㅋㅋㅋ. 가능한 논리적 귀결을 많이 찾아보는것도 좋고.) 그래서 추이성 만족

### abs함수와 GraterThenOnFakeInt • LessThenOnFakeInt

$abs(X) ≜ \begin{cases} X, & isWholeNumber(X), \\ [[0, 1], [1, 0]] @ X, & isNegativeInteger(X) \end{cases}$

ㄹㅇㅋㅋㅋㅋㅋㅋㅋ

GraterThenOnFakeInt(X, Y) : abs(SubtractionOfFakeInt(X, Y)) = SubtractionOfFakeInt(X, Y)
LessThenOnFakeInt(X, Y) : GreaterThenOnFakeInt(Y, X)