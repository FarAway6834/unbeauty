# VectorNote - i. 다항기저 • 수열기저 • 로그된 소수 기저 • 튜플기저의 동형성 - 유리수 스칼라에서

(VectorNotes 1편)

유리수 스칼라에서만 설명할거이므로, 그 이외의 일반적인 스칼라에 대한 이야기는 이거 말고, 이거 후속 버전에서 적을거다.

또 이 글이, 단순히 수학적 정의만 빼곡이 준 다음에, 그 정의를 인위적으로 자연어적 맥락같은걸 억지로 붙이지 않고, 그냥 단순히 사실을 나열하는 형식으로 전개되는, 맥락배제 형식화를 지향하는 글임에 주의하자.

## 들어가며

대수적 수(𝔸)는 SimpleVariableVector와 동형이므로, VariableVectorByPoly와 동형이다 그러므로, 이와 같이, 내적공간 ℚ^∞에 대응되게 하는 동형사상을 쉽게 구축할수 있고, 이를 통해, ln pₖ가 정규직교기저이며, 이는 SimpleVariableVector와 VariableVectorByPoly에서도 마찬가지다.

직접 구성해보자. 선언구문 중심으로.

## tool

여기에서, 서술용으로 사용할 수학적 도구를 정의하자.

tool문단에 있는 내용은, 오로지 서술용 툴킷 용도이다.

### ClsrAndClsr-PromiseSystem-byRestrictSystem

```markdown
# restrict시스템을 이용한 clsr시스템과 clsr-promise시스템

Step 1. restrict시스템

정신나간 함수인 restrict를 정의하겠다.

restrict(f) ≜ (k, codom f, R ∩ (k × codom f)) s.t. graph f ⊆ R ∧ k = dom ∧ (ρ = (dom = dom f, f = (dom f, codom f, graph f)) ⊨ (k, codom f, graph f) = f)

이 미친 함수같은 바인딩되지 않은 변수를 가지는 짭함수시치는, 배정에 따라서 값이 달라진다. 사실 함수라고 하기에도 민망한 Notation같은 괴물시치다.

구문론적 정의인거다.

아오...

다음으로 정상적인 표기법 하나 준다.

s|ᵤ₌ᵥ는 변수기호 u에다가 식 v를 할당하는거다.

으히히 ρ를 실시간으로 조작 가능하다고...

그러나 유니코드로 전산화 하기 어려워 부가적인 표기법을 도입한다.

LibnizicAssignment(s | u = v) ≜ s|ᵤ₌ᵥ

와 ㅋㅋㅋ 구문론적 정의 미쳐버리겠네...

암튼, 이제 다른 부가 도구 조금만 나열하고 본론으로 들어갈거다.

부가 도구를 먼저 나열하겠다.

f⁻¹ = (codom f, dom f, {(y, x) | (y, x) ∈ graph f})
LibnizAssignment(restricts(f) | codom = Y) ≜ LibnizicAssignment(restrict(f⁻¹) | dom = Y)⁻¹
LibnizicAssignment(LibnizicAssignment(restricted(f) | dom = X) | codom = Y) ≜ LibnizAssignment(restrict(LibnizAssignment(restricts(f) | codom = Y)) | dom = X)

이렇게 잘 된다. 하... 괴물을 만들었..

부가규칙)

1. f = ϝ x : auto. y : Y는 auto에 dom f를 대입한다
2. f = ϝ x : X. y : auto는 auto에 codom f를 대입한다.

암튼 이제 본론 차례다.

1. ∀U, ∀S ⊇ U, ∀X, Y ⊆ U, LibnizicAssignemnt(restrict(LibnizicAssignment(restrict(im | dom = 𝒫(S))(U)) | dom = 𝔉(X, Y)) ≜ ϝ f : auto. (ϝ x : U. (graph f)[X] : U) : 𝔉(U, U)
2. ∀U, ∀X, Y, Z ⊆ U, LibnizicAssignment(LibnizicAssignment(restrict(part) | dom = 𝔉(X × Y, Z) × X) | codom = 𝔉(Y, Z))(f, x)(y) ≜ f(x, y)
3. ∀U, ∀X, Y ⊆ U, LibnizicAssignment(LibnizicAssignment(restrict(revm) | dom = X × Y) | codom = Y × X)(x, y) ≜ (y, x)
4. ∀U, ∀X, Y, Z ⊆ U, LibnizicAssignment(LibnizicAssignment(restrict(frev) | dom = 𝔉(X × Y, Z)) | codom = 𝔉(Y × X, Z))(f) ≜ f ◦ LibnizicAssignment(revm | dom = Y × X)
5. ∀U, ∀X, Y, Z ⊆ U, fset = 𝔉(X × Y, Z) ∧ partret = 𝔉(Y, Z) ∧ partialret = 𝔉(X, partret) ∧ partarg = fset × X ∧ partset = 𝔉(partarg, partret) ∧ partialarg = partset × fset ∧ partialset = 𝔉(partialarg, partialret) ∧ clsraw = partialset × partset ∧ clsrtyp = 𝔉(fset, partialret) ∧ LibnizicAssignment(LibnizicAssignment(restrict(clsr) | dom = fset) | codom = partialret) = LibnizicAssignment(LibnizicAssignment(part | dom = clsraw) | codom = clsrtyp)(LibnizicAssignment(LibnizicAssignment(part | dom = partialarg) | codom = partialret), LibnizicAssignment(LibnizicAssignment(part | dom = partarg) | codom = partret))
6. ∀U, ∀X, Y, Z ⊆ U, LibnizicAssignment(LibnizicAssignment(binopf | dom = 𝒫(U)³) | codom = 𝔉[𝒫(U)³])(X, Y, Z) ≜ 𝔉(X × Y, Z)
7. ∀U, ∀X ⊆ U, LibnizicAssignment(LibnizicAssignment(binop | dom = 𝒫(U)) | codom = 𝔉[𝒫(U)³])(X) ≜ binopf(X, X, X)
8. ∀U, ∀X, Y, Z ⊆ U, LibnizicAssignment(LibnizicAssignment(restricted(fop) | dom = 𝒫(U)³) | codom = 𝔉[𝒫(𝔉[𝒫(U)³])³])(X, Y, Z) ≜ LibnizicAssignment(LibnizicAssignment(binop | dom = 𝔉[𝒫(U)³]) | codom = 𝔉[𝒫(𝔉[𝒫(U)³])³])(LibnizicAssignment(LibnizicAssignment(binopf | dom = 𝒫(U)³) | codom = 𝔉[𝒫(U)³])(X, Y, Z))
9. ∀U, ∀X, Y, Z ⊆ U, LibnizicAssignment(LibnizicAssignment(restricted(fopdual) | dom = 𝒫(U)³) | codom = 𝔉[𝒫(𝔉[𝒫(U)³])³]) ≜ LibnizicAssignment(LibnizicAssignment(binop | dom = 𝔉[𝒫(U)³]) | codom = 𝔉[𝒫(𝔉[𝒫(U)³])³])(frev[LibnizicAssignment(LibnizicAssignment(binopf | dom = 𝒫(U)³) | codom = 𝔉[𝒫(U)³])(X, Y, Z)])

th. 어떤 F ∈ fop(X, Y, Z), G ∈ binopf(X, Y, Z)에 대해, frev(F(f, g)) = G(frev(f), frev(g))면, frev는 모델 <binopf(X, Y, Z), f, F, (f F)>과 모델 <frev[binopf(X, Y, Z)], frev(f), G, (frev(f) G)>사이의 동형사상이다.
col. 함자 (f F)와 함자 (g G)는 어떤 k ∈ binopf(binopf(X, Y, Z), A, B), h ∈ binopf(frev[binopf(X, Y, Z)], C, D)인 함수에 대해, (k a), (h c)일수 있다.

이제 clsr에 대해 다뤄보자.

Step 2. clsr과 그 표기법

n.b. `^`기호가 여기서 LaTeX적 의미가 아니다. 그냥 표기법용 기호다. 한마디로 이름용 알파벳•연산자용 알파벳으로 허용된것.
|）f ≜ clsr(f)
|x）^f ≜ (  |）f)(x)
f（x|y） ≜ (f（x|)(y)
f（x| ≜ |x）^f

notation definition f.t. 구문론적 등호 기호 `≡ₛ`)
1. |y）≡ₛ y

Step 3. Promise에 대해서

1. ∀U, ∀X, Y ⊆ U, LibnizicAssignment(LibnizicAssignment(restricted(PromiseDom) | dom = 𝒫(U)²) | codom = {𝔉(X, Y) × X | X, Y ∈ 𝒫(U)})(X, Y) ≜ 𝔉(X, Y) × X
2. ∀U, ∀X, Y ⊆ U, LibnizicAssignment(LibnizicAssignment(restricted(Apply) | dom = PromiseDom(X, Y)) | codom = Y)(f, x) ≜ f(x)
4. ∀U, ∀X, Y ⊆ U, LibnizicAssignment(LibnizicAssignment(restricted(PromObIdentity) | dom = PromiseDom(X, Y) | codom = PromiseDom(X, Y)) ≜ (PromiseDom(X, Y), PromiseDom(X, Y), {(x, x) | x ∈ PromiseDom(X, Y)})
5. LibnizicAssignment(LibnizicAssignment(restrict(Promise) | dom = 𝔉(X, Y)) | codom = 𝔉(X, Y)) ≜ |）LibnizicAssignment(LibnizicAssignment(Apply | dom = PromiseDom(X, Y)) | codom = Y)

Notation좀 하나 도입한다.
1. Promise<X, Y> ≡ₛ LibnizicAssignment(LibnizicAssignment(restrict(Promise) | dom = 𝔉(X, Y)) | codom = 𝔉(X, Y)

마저 이어서 아까 정의하던걸 정의하겠다.

아 존나 귀찮아서, 그냥 재대로된 Notation하나 정의하겠다.
1. LA<X, Y>(f) ≡ₛ LibnizicAssignment(LibnizicAssignment(f | dom = X) | codom = Y)
2. TYP<X, Y> ≡ₛ 𝔉(X, Y)
3. ÑA<0, X, Y, Z, F> ≡ₛ  X × Y
4. ÑA<1, X, Y, Z, F> ≡ₛ  F(X, Y)
5. ÑA<2, X, Y, Z, F> ≡ₛ  ÑA<1, Y, Z, ∅, F>
6. ÑA<3, X, Y, Z, F> ≡ₛ  ÑA<1, X, 7. ÑA<2, X, Y, Z>, ∅, F>
8. ÑA<4, X, Y, Z, F> ≡ₛ  ÑA<1, ÑA<0, X, Y, ∅, F>, Z, ∅, F>
9. ÑA<5, X, Y, Z, F> ≡ₛ ÑA<0, ÑA<4, X, Y, Z, F>, X, ∅, F>
10. ÑA<6, X, Y, Z, F> ≡ₛ ÑA<1, ÑA<5, X, Y, Z, F>, ÑA<2, X, Y, Z, F>, ∅, F>
11. ÑA<7, X, Y, Z, F> ≡ₛ ÑA<1, ÑA<4, X, Y, Z, F>, ÑA<3, X, Y, Z, F>, ∅, F>
12. MYA<0><(X, Y, Z, F)> ≡ₛ ÑA<4, X, Y, Z, F>
13. MYA<1><(X, Y, Z, F)> ≡ₛ X
14. MYA<2><(X, Y, Z, F)> ≡ₛ ÑA<2, X, Y, Z>
15. MYA<3><(X, Y, Z, F)> ≡ₛ (MYA<0><(X, Y, Z, F)>, MYA<1><(X, Y, Z, F)>, MYA<2><(X, Y, Z, F)>, F)
16. ÑANG<0><(X, Y, Z, F)> ≡ₛ LA<X × Y, Z>
17. ÑANG<1><(X, Y, Z, F)> ≡ₛ LA<X, 𝔉(Y, Z)>
18. RankUp<0><(X, Y, Z, F)> ≡ₛ (X, Y, Z, F)
19. RankUp<N><(X, Y, Z, F)> ≡ₛ RankUp<N - 1><MYA<3><(X, Y, Z, F)>>
20. RUß<0, N, M, X, Y, Z> ≡ₛ MYA<N><RankUp<M><(X, Y, Z, TYP)>>
21. RUß<1, N, M, X, Y, Z> ≡ₛ ÑANG<N><RankUp<M><(X, Y, Z, TYP)>>
22. CL<L, X, Y, Z> ≡ₛ RUV<1, 0, L, X, Y, Z>
23. PA<L, X, Y, Z> ≡ₛ RUß<1, 1, L, X, Y, Z>
24. RU<L, X, Y, Z, N> ≡ₛ RUß<0, N, L, X, Y, Z>

휴...

바로 본론으로 들어가자.

1. CL<L, X, Y, Z>(clsr)(PA<L - 1, X, Y, Z>(part)) = <L - 1, X, Y, Z>(clsr)
즉, clsr은 clsr시스템에서, part의 clsr이었던거다 ㅋㅋㅋㅋ 이를 통해 알수 있늨 사실은, X, Y, Z에 대한 CL<L, X, Y, Z>(clsr)의 성질만 잘 알면, CL<L, RU<L - 1, X, Y, Z, 0>, RU<L - 1, X, Y, Z, 1>, RU<L - 1, X, Y, Z, 3>>(clsr)을 통해 자기 자신을 분석 가능하므로, clsr은, 그 모델의 인자에 따라 자기 자신을 분석할수 있는 모델이다.
2. dom PromOb<X, Y> = ran Promise<X, Y>고, ran PromOb<X, Y>과 ran Promise<X, Y>는 각각 S, P라 할때, S = PromOb<X, Y>[P]임이 당연하므로, 동형사상 f = ϝ prom : P. PromOb<X, Y>(prom) : S를 통하여, 일대일 대응 가능하며, 동형이다.
3. Promise역시 clsr모델의 인자로 주어 표현할수 있고, 그 인자를 준 폼은 CL<0, 𝔉(X, Y), X, Z>(clsr)이다. f = CL<0, 𝔉(X, Y), X, Z>(clsr)(LA<X, Y>(Apply))인 f가 f = LA<𝔉(X, Y), 𝔉(X, Y)>(Promise)로 clsr모델인데 인자가 <𝔉(X, Y), X, Z>인 모델 위에 있다.
4. LA<𝔉(X, Y), 𝔉(X, Y)>(Promise)는 𝔉(X, Y)에서의 항등함수인데, PromObIdentity는 𝔉(X, Y) × X에서의 항등함수다.
5. PromOb는 PromObIdentity를 clsr모델의 인자로 준거다.
6. LA<𝔉(X, Y), 𝔉(X, Y)>(Promise)(f) = part(LA<𝔉(X, Y) × X, Y>(apply), LA<X, Y>(f))이다.
7. Identity라는 항등 함수 폼(restrict로 잘 정의할수 있으니 걍 넘기자. 머리 터질것같다.)이 있다고 치고, 이때, LA<𝔉(X, Y), 𝔉(X, 𝔉(X, Y) × X)>(PromOb) = part(LA<𝔉(X, Y) × X, 𝔉(X, Y) × X>(Identity), LA<X, Y>(f))다.

일단, 머리 터질것같다. 모델에다가 인자를 주는 미친짓을 한 순간부터 이미 뇌에 과부하가 흘러 넘친거다. 모델을 만드는 함수를 가정한 셈이니까.

암튼, 앞으로도, LA<X, X>(Identity) = (X, X, {(x, x) | x ∈ X})라 할테니까,

뭐 말하려 했었지..?

파생함수화 • 파생함수 • 파생된 함수에 대해 정의해놓자면
(ϝ (x, y) : X × Y. z : Z)를 (ϝ x : X. (ϝ y : Y. z : Z) : 𝔉(Y, Z))로 partial funcionize(파생함수화)하는 작업은, y다 단변수면 currying이고, 다변수면, 1회 currying하고 만거다.
그렇기에, clsr이란, (ϝ (x, y) : X × Y. z : Z)를 (ϝ x : X. (ϝ y : Y. z : Z) : 𝔉(Y, Z))로 partial functionize하는 함수다.
반면, part는 partialing(파생)하는 함수로, part(f, x)는 파생된 함수고, 이러한 파생된 함수를 생성하는 함수가 파생함수다.

이러한 직관상에서 다음이 해석 가능하다.
1. clsr(part)는 파생연산자의 파생함수화로, 파생함수화 연산자다.
2. clsr(ϝ (x, y) : X × Y. (x, y) : X × Y)는 pair의 identity의 파생함수화로, pair를 currying한 expreesion으로 이용 가능하다. pairexpression ≜ clsr((ϝ (x, y) : X × Y. (ϝf : 𝔉(X × Y, Z). f(x, y) : Z) : 𝔉(𝔉(X × Y, Z), Z))) ◦ (ϝ (x, y) : X × Y. (x, y) : X × Y)(x, y))) = ϝx. (ϝy : Y (ϝf. f(x, y) : Z) : 𝔉(𝔉(X × Y, Z), Z)) : 𝔉(Y, 𝔉(𝔉(X × Y, Z), Z))이도록 할수 있으므로, <S*, first, last, pairexpression>은 lambda calculus의 pair와 동형임.
3. clsr(Apply)는 Promise다. 그런데, Promise = ϝ f : 𝔉(X, Y). f : 𝔉(X, Y)다. 다르게 말하면, A × B = {X} × {(Y, graph f) | f ∈ 𝔉(X, Y)}에 대해, A × B쌍의 pair identity가 Promise이기도 하니, clsr²(Apply)는 그러한 PairIdentity의 파생함수화다. 특정 정의역 위에서 공역과 대응용 graph를 적는 파생함수.
4. clsr(ϝ (f, x) : dom Apply. (f, x) : dom Apply)는 dom Apply = 𝔉(X, Y) × X쌍의 pair identity에 대한 파생함수화며, PromObIdentity = ϝ (f, x) : dom Apply. (f, x) : dom Apply으로, PromObIdentity의 파생함수가 PromOb다. 또한, Apply◦ PromOb(f) = Promise(f) = f와 같다.
5. (PromOb◦clsr)(f) = (ϝx : X. (part(part, f), x) : codom clsr × X)다. (clsr(f), x)를 통해, Apply시키면 clsr가 되는 놈이다.
6. (PromOb ◦ part)(f) = (ϝ x : dom f. (part(f), x) : dom part × dom f임.
7. (PromOb◦PromObIdentity)같은거나 PromOb ◦ Promise같은건 이미 자명함.
8. (first◦PromOb(f))(x) = f고, (last ◦ PromOb(f))(x) = x임. 즉, 식 "f(x)"를 표현하는 수형도는 PromOb와 동형임. ㅋㅋㅋ 이름표 같네 ㅋㅋ
9. 그런데, 모든 함수의 적용은 Apply임.
10. 물론, PromOb(Apply)(f) = (Apply, f)임. ㅋㅋ
11. 1. Apply(CL<1, X, Y, Z>clsr, part) = CL<0, X, Y, Z> clsr
11. 2. Apply(Identity<X × Y>)(x)(y) = pairexpression<X, Y>(x)(y)(Identity<X × Y>)
11. 3. Apply(clsr, Apply) = Promise고, 이는 특이한게, 우항등원인 Apply(Identity<𝔉(X, Y)>, f) = f은 가능한데, 좌항등원은 함수의 Rank땜에 안되지만, 저기 저 Apply는 Rank0이고, Promise가 Rank 1이다.
11. 5. Apply(PromObIdentity, (f, x)) = (f, x)로, 이것고 Identity를 이렇게 했기에 가능하다.
12. Apply(Apply, ((Apply, (clsr(f), x)), y) = Promise ◦ (Promise(clsr(f)))다. 이러한 Promise지연인척 하는 문장의 정체가 Promise가 그냥 idntity여서 ㅋㅋㅋ 이젠 하다하다 조합논리가 파싱이 된다 이런 형태로

la<𝔉(X, 𝔉(X, Y) × X), 𝔉(X, Y)> PromOb2Prom ≜ ϝ promob : 𝔉(X, 𝔉(X, Y) × X). first(promob) : 𝔉(X, Y)

la<𝔉(X, Y), 𝔉(X, 𝔉(X, Y) × X)> Prom2PromOb ≜ ϝ prom : 𝔉(X, Y). PromOb(prom) : 𝔉(X, 𝔉(X, Y) × X)

뭐 동형사상 만들었으니 이쯤하면 됬나.

암튼, 은근히 Promise와 clsr이 연관있다.

이 글도 젯타이니 다듬어야한다. 심지어 탐구하다가 PromOb나와서 뇌 터져서 멈춘거임.
```

### CRVS

자연수 튜플을 벡터처럼 다루는 근거.

```markdown
# ComponentRestrictedVector System

ComponentRestrictedVector(S, V, <•,•>) ≜ {v ∈ V | ∀k ∈ ℕ ∩ [1, n], <v, eₖ> ∈ S}

약칭용 확장 : CRV ≜ ComponentRestrictedVector

dom CRVM ≜ {(S, V, <•, •>) ∈ dom CRV | <S, 0, 1, +, -, ×, ÷>가 체를 이룬다.}
CRVM(S, V, <•, •>) ≜ (CRV(S, V, <•, •>), 0, +, •, <•, •>)

th. <S, 0, 1, +, -, ×, ÷>가 체를 이루지 않으면 CRV(S, V, <•, •>)는 내적공간도, 벡터공간도 아니다.

## 응용용 확장

IntegerComponentedVector(S, V, <•, •>) ≜ CRV(S ∩ ℤ, V, <•, •>)

약칭용 확장 : ICV ≜ IntegerComponentedVector

th. ICV(S, V, <•, •>)는 사칙연산과 수가 우리가 알고있는대로 정의되었다면, 절대로 벡터공간을 이루지 않는다.

NaturalComponentedVector(t, V, <•, •>) ≜ ICV([1, t], V, <•, •>)

약칭용 확장 : NCV ≜ NaturalComponentedVector

th. NCV(t, V, <•, •>) = CRV(S, V, <•, •>)면, S의 상계엔 t가, S의 최소하계엔 1이 있게 되며, S는 자연수의 부분집합이고, t ≠ ∞일때만 진부분집합이다.
```

### Wave Arrow Pointing Directly Right Notation

x ≤ₚ y : (p → (x ≤ y)) ∧ ((¬p) → (x < y))

-∞ < x < ∞ : x ∈ ℝ
a ≤ₚ x < ∞ : x ∈ ℝ, a ≤ₚ x
-∞ < x ≤ₚ b : x ∈ ℝ, x ≤ₚ b

〖ᵤa, b〗ᵥ ≜ {x | a ≤ᵤ x ≤ᵥ b}

(a, b) ≜ 〖₀a, b〗₀
[a, b) ≜ 〖₁a, b〗₀
(a, b] ≜ 〖₀a, b〗₁
[a, b] ≜ 〖₁a, b〗₁

〖ᵤa ⤳ b〗ᵥ ≜ ℤ ∩ 〖ᵤa, b〗ᵥ

[∞, ∞] ≜ {∞}
[-∞, -∞] ≜ {-∞}
[-∞, x〗ₚ ≜ [-∞, -∞] ∪ (-∞, x〗ₚ
〖ₚ  x, ∞] ≜ 〖ₚx, ∞) ∪ [∞, ∞]

### trinity operator notation

p?x:y ≜ \begin{cases} x, &(p), \ y, &(￢p) \end{cases}

### first and last

first(x, y) = x
last(x, y) = y
SignituredTuple(L, x) : L ∈ [0 ⤳ ∞] ∧ (L = 0)?(x = ε):((L = 1):(SignituredTuple(2, x) ∨ x ∉ dom first):(SignituredTuple(L⁻, last(x))))
domTidx(I, L, x) : SignituredTuple(L, x) ∧ I ∈ [0 ⤳ L]
tidx ≜ Surj (I, L, x) : domTidx. ((I + 1 = L)?(lastᴵ(x)):(first(tidx(I, I + 1, x)))) 

### InfEncodedNaturalNumber

InfEncoder ≜ ϝ x : [0 ⤳ ∞]. ((x = ∞)?(-1):x) : [-1 ⤳ ∞)
InfDecoder ≜ ϝ x : [-1 ⤳ ∞). ((x < 0)?(∞):x) : [0 ⤳ ∞]

IENVectorₙ ≜ (ϝ n : [1 ⤳ ∞]. (ϝ x : lim_{R ⟶ n} [0 ⤳ ∞]ᴿ. lim_{R ⟶ n} [-1 ⤳ ∞)ᴿ InfEncoder(tidx(m - 1, R, x))eₘ : lim_{R ⟶ n} ([-1 ⤳ ∞)ᴿ)) : lim_{n ⟶ ∞} ∪ᵢ₌₁ⁿ 𝔉([0 ⤳ ∞]ⁱ, [-1 ⤳ ∞)ⁱ))(n)

FuncInfEncoder ≜ ϝ n : [1 ⤳ ∞]. (ϝ f : lim_{R ⟶ n} 𝔉([-1 ⤳ ∞)ᴿ, [-1 ⤳ ∞)). (ϝ x : lim_{R ⟶ n} [0 ⤳ ∞]ᴿ. InfDecoder(f(IENVectorₙ(x))) : [0 ⤳ ∞]) : lim_{R ⟶ n} 𝔉([0 ⤳ ∞]ᴿ, [0 ⤳ ∞]))) : ∪ᵢ₌₁ⁿ 𝔉[𝔉([-1 ⤳ ∞)ⁱ, [-1 ⤳ ∞)) × 𝔉([0 ⤳ ∞]ⁱ, [0 ⤳ ∞]))]

def) <[0 ⤳ ∞], +ⁱⁿᶠ, -ⁱⁿᶠ, ×ⁱⁿᶠ, ÷ⁱⁿᶠ>에서, n ∈ [1 ⤳ ∞]에 대해, lim_{R ⟶ n}  <[0 ⤳ ∞]ᴿ, +ⁱⁿᶠᴿ, -ⁱⁿᶠᴿ, •ⁱⁿᶠᴿ>에서,
1. +ⁱⁿᶠ = FuncInfEncoder(+)
2. -ⁱⁿᶠ = FuncInfEncoder(-)
3. ×ⁱⁿᶠ = FuncInfEncoder(×)
4. ÷ⁱⁿᶠ = FuncInfEncoder(÷)
5. +ⁱⁿᶠᴿ = FuncInfEncoder(+)
6. -ⁱⁿᶠᴿ = FuncInfEncoder(-)
7. •ⁱⁿᶠᴿ = FuncInfEncoder(•)
8. 행렬곱이나 그런건, 저기서 알아서 정의되고, -1이하는 일절 -1로 간주한다.
9. 그리고, 이 모델에서 내적은 <x|ⁱⁿᶠᴿy>로 적음
10. 표준단위기저는 eⁱⁿᶠᴿₖ임.

IDENVectorₙ ≜ (ϝ n : [1 ⤳ ∞]. (ϝ x : lim_{R ⟶ n} [-1 ⤳ ∞)ᴿ. lim_{R ⟶ n} Σₘ₌₁ᴿ <eₘ | x> eⁱⁿᶠᴿₘ : lim_{R ⟶ n} [0 ⤳ ∞]ᴿ) : lim_{n ⟶ ∞} ∪ᵢ₌₁ⁿ 𝔉([0 ⤳ ∞]ⁱ, [-1 ⤳ ∞)ⁱ))(n)
FuncInfDecoderₙ ≜ (ϝ n : [1 ⤳ ∞]. (ϝ f : 𝔉(lim_{R ⟶ n} [0 ⤳ ∞]ᴿ, lim_{R ⟶ n} [0 ⤳ ∞]ᴿ). (ϝ x : lim_{R ⟶ n} [-1 ⤳ ∞)ᴿ. InfEncode(f(IDENVectorₙ(x))) : lim_{R ⟶ n} [-1 ⤳ ∞)ᴿ) : 𝔉(lim_{R ⟶ n} [0 ⤳ ∞]ᴿ, lim_{R ⟶ n} [0 ⤳ ∞]ᴿ)) : lim_{n ⟶ ∞} ∪ᵢ₌₁ⁿ 𝔉[𝔉([0 ⤳ ∞]ⁱ, [0 ⤳ ∞)) × 𝔉([-1 ⤳ ∞)ⁱ, [-1 ⤳ ∞))])(n)

동형이고 뭐... 아주 잘 처리하니까 뭐..

## `동형사상 VVBP2SVV<S>ₙ`

ArrTenBasisByVec<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. (ϝ l : lim_{R ⟶ n} [1 ⤳ ∞]ᴿ. (ϝ k : ∏ₘ₌₁ⁿ [1 ⤳ <eⁱⁿᶠᴿₘ |ⁱⁿᶠᴿ l>⁺). (ϝ x : ∏ₘ₌₁ⁿ [1 ⤳ <eⁱⁿᶠᴿₘ |ⁱⁿᶠᴿ l>⁺. <eⁱⁿᶠᴿₓ |ⁱⁿᶠᴿ k> : S) : 𝔉(∏ₘ₌₁ⁿ [1 ⤳ <eⁱⁿᶠᴿₘ |ⁱⁿᶠᴿ l>⁺, S)) : {x ∈ 𝔉(∏ₘ₌₁ⁿ [1 ⤳ <eⁱⁿᶠᴿₘ |ⁱⁿᶠᴿ v>⁺, 𝔉(∏ₘ₌₁ⁿ [1 ⤳ <eⁱⁿᶠᴿₘ |ⁱⁿᶠᴿ v>⁺, S)) | v ∈ lim_{R ⟶ n} [1 ⤳ ∞]ᴿ}))(n)
ArrVecToVec<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. ϝ a : 𝔉([1 ⤳ n⁺), S). Σₖ₌₁ⁿ aₖeₖ : lim_{R ⟶ n} Sᴿ)(n)
Vec2ArrVec<S>ₙ ≜ (Surj n : ϝ v : lim_{R ⟶ n} Sᴿ. Σₖ₌₁ⁿ tidx(k - 1, n, v) ArrTenBasisByVec₁(n)(k) : 𝔉([1 ⤳ n⁺), S)()
ArrTenBasis<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. (ϝ l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). (ϝ k : Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ lₘ⁺)]. (ϝ x : Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ lₘ⁺)]. ArrTenBasisByVec<S>ₙ(l)(k)(x) : S) : 𝔉(Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ lₘ⁺)], S)) : {y ∈ 𝔉(Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ xₘ⁺)], 𝔉(Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ xₘ⁺)], S)) | x ∈ 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ)})))(n)
ArrTenSet<S>ₙ ≜ (Surj : [1 ⤳ ∞]. Surj l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). {y = Σ_{v ∈ 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ)} T(ArrVec2Vec(v)) ArrTenBasis<S>ₙ(l)(v) | T ∈ ⊗ₘ₌₁ⁿ lim_{k  ⟶ lₘ} Sᵏ}))(n)
ArrVecHashadProd<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. 
(ϝ l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ).
(ϝ (x, y) : ArrTenSet<S>ₙ(l)². (ϝ v : dom ArrTenSet<S>ₙ(l). x(v)y(v) : S) : ArrTenSet<S>ₙ(l)) : ∪ codom (Surj x : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). 𝔉(ArrTenSet<S>ₙ(x)², ArrTenSet<S>ₙ(x)))))(n)

왜 수열 하샤드 곱을 만들었지... 저 하샤드 곱을 응용할 일이 있어서 만들었는데... 어쩌지 ㅠ... 헤헤...

PolyVecBasis<S>ₙ ≜ (ϝ n : [1 ⤳ ∞). (ϝ x : S. x⁽ⁿ⁻¹⁾ : S) : 𝔉(S, S))(n)
PolyTenBasis<S>ₙ ≜ (Surj n : [1 ⤳ ∞). (ϝ l : 𝔉([1 ⤳ n⁺), [1 ⤳ ∞]). (ϝ k : Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ lₘ⁺)]. (ϝ t : Sⁿ. Πₘ₌₁ⁿ PolyVecBasis<S>(kₘ)(tidx(m - 1, n, t)) : S) : 𝔉(Sⁿ, S)) : ∪ codom (Surj x : 𝔉([1 ⤳ n⁺), [1 ⤳ ∞]). 𝔉(Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ lₘ⁺)], 𝔉(Sⁿ, S))))(n)

뭐하려 만들었는지 기억남.

ArrVec2TupArrVec<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. (Surj l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). (Surj a : Vec2ArrVec<S>ₙ[∏ₘ₌₁ⁿ [1 ⤳ lₘ⁺)]. a◦ArrVec2Arr)))

VariableTensor<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. (Surj l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). clsr(ArrVecHashadProd<S>ₙ(l))))(n)
TupArredVariableTector<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. Surj l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). Surj x : codom ArrVec2TupArrVec<S>ₙ(l). Surj y : codom ArrVec2TupArrVec<S>ₙ(l). VariableTensor<S>ₙ(l)(ArrVec2TupArrVec<S>ₙ(x))(ArrVec2TupArrVec<S>ₙ(y)))(n)
SimpleVariableVector<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. Surj l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). TupArredVariableTector<S>₁(n ArrTenBasisByVec<S>₁(1)(1)))(n)

이렇게 SimpleVariableVector<S>ₙ를 얻을수 있다.
DualBasisArrForm<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. (Surj k : [1 ⤳ n⁺). ArrTenBasisByVec<S>ₙ(Σₘ₌₁ⁿ ArrTenBasisByVec<S>₁(n)(m))(ArrTenBasisByVec<S>₁(n)(k))))(n)
ArrVec2PolyVec<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. Surj l : 𝔉([1 ⤳ n⁺), lim_{R ⟶ n} [1 ⤳ ∞]ᴿ). Surj a : codom ArrTenBasis<S>ₙ(l). Σ_{x ∈ dom a} a(x)PolyTenBasis<S>ₙ(l)(x))(n)
VariableVectorByPoly<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. (Surj k : [1 ⤳ n⁺). ArrVec2PolyVec<S>ₙ(Σₘ₌₁ⁿ ArrTenBasisByVec<S>₁(n)(m))◦DualBasisArrForm<S>ₙ)(n)

VVBP2SVV<S>ₙ ≜ (Surj n : [1 ⤳ ∞]. ArrVec2TupArrVec<codom VariableVectorByPoly<S>ₙ>ₙ)(n)

이렇게, VVBP2SVV<S>를 만들면, VariableVectorByPoly<S>ₙ를 SimpleVariableVector<S>ₙ로 변환하는 동형사상을 얃을수 있다.

## Algebric Number as Vector

x|y : ∃z ∈ ℤ, xz = y
ℙ₁ ≜ {x | {y ∈ ℕ | (y|x)} = {1, x}}
pₖ ≜ min(ℙₖ)
ℙₖ ≜ ℙ₍ₖ₋₁₎ ∖ {p₍ₖ₋₁₎} (k ≠ 1)
lpₖ ≜ ln(pₖ)
SequenceBasisRationalVector ≜ ϝ a : 𝔉(ℕ, ℚ). exp◦(lim_{n ↦ ∞} SimpleVariableVector<ℝ>ₙ(a)) : codom exp◦(lim_{n ↦ ∞} SimpleVariableVector<ℝ>ₙ)
SequenceBasisRationalVector2Algebric ≜ ϝ x : codom SequenceBasisRationalVector. x(lp) : 𝔸
Algebric ≜ ϝ a : 𝔉(ℕ, ℚ). SequenceBasisRationalVector2Algebric(a) : 𝔸

핵심내용 : 대수적 수(𝔸)는 SimpleVariableVector와 동형이므로, VariableVectorByPoly와 동형이다.

## 마치며

VVBPQiso<S>ₙ ≜ (ϝ n : [1 ⤳ ∞]. (ϝ f : lim_{n ↦ ∞} 𝔉(Sⁿ, S). Σₖ₌₁ⁿ (d f/d eₖ)(Σₘ₌₁ⁿ 0 eₘ)eₖ : Sⁿ) : 𝔉(𝔉(Sⁿ, S), Sⁿ))(n)

QisoonP ≜ lim_{n ↦ ∞} SequenceBasisRationalVector2Algebric◦VVBP2SVV<ℝ>ₙ◦VVBPQiso<ℝ>ₙ

<x|ᴾᴿᴵᴹᴱ y> ≜ <QisoonP⁻¹(x)|QisoonP⁻¹(y)> (Tip : 동형사상 f : ℚ^∞ ↦ ln[𝔸]에서, <f(v) | f(w)> = <v|w>로 내적을 정의할수도 있으며, 이러한 내적은 <f(v)|ᴾᴿᴵᴹᴱ g(w)>라고 적는게 바로 이 식이다.)

결론 : 이와 같이, 내적공간 ℚ^∞에 대응되게 하는 동형사상을 쉽게 구축할수 있고, 이를 통해, ln pₖ가 정규직교기저이며, 이는 SimpleVariableVector와 VariableVectorByPoly에서도 마찬가지다.