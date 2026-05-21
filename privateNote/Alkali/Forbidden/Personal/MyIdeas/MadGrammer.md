# MadOperator

 - EncodedFree Monoid (isomorphismity of string and encoded tuple)
 - MadGrammer

## definition of encoded free monoid

Φ(decoder, x, y) : $\begin{cases} decodersize(x)(y) = EncodingTablize(x)⁻¹(y), &(y ∉ dom first), \ decoder(x)(y) = (EncodingTablize(L, s)⁻¹(first(y)), decoder(x)(last(y))), &(y ∈ dom first) \end{cases}$
decoding = ϝx : dom EncodingTablize. (ϝy : (codom EncodingTablize(x))*. decoding(x)(y) : (dom EncodingTablize(x))*) : {𝔉((codom EncodingTablize(x))*, (dom EncodingTablize(x))*) | x ∈ codom EncodingTablize} s.t. (decoding(x)("") = ε) ∧ Φ(decoder, x, y)
FLL(L, s) ≜ (<<F(𝔽) := (𝔽)*, zero<L>, basis<L>, concat<L>>, <𝔽 := (ℤ/Lℤ), 0, 1, +, -, ×>, <𝕍ₙ := Span(𝔽, {basis(n, k) | k ∈ [1, n] ∩ ℕ₀}, +, -), dim, •>, decoding<L, s>)
zero<L>(n) ≜ basis<L>(n) - basis<L>(n)
basis<L>(n, i) ≜ $\begin{cases} zero<L>(i - 1) concat<L> basis<L>(1, 1) concat<L> zero<L>(n - i), &(n ≠ 1), \ ε, &(n = 0), \ <1>, &(n = 1) end{cases} $
dim 𝕍ₙ ≜ n
∀n ∈ ℕ₀, ∀v, w ∈ 𝕍ₙ, v ± w ≜ $ \begin{cases} <first(v) ± first(w), last(v) ± last(w)>, &(dim v > 1), \ ε, &(dim v = 0), \ v ± w, &(dim v = 1) end{cases} $
∀x ∈ 𝔽, ∀y ∈ {x ∈ 𝕍ₙ | n ∈ ℕ₀}, x•y ≜ $ \begin{cases} <k first(v), k • last(v)>, &(dim v > 1), \ ε, &(dim v = 0), \ kv, &(dim v = 1) end{cases} $
x concat<L> y ≜ $ \begin{cases} (x, y), &(dim x = 1), \ (first(x), last(x) concat<L> y), &(dim x > 1), \ y, &(dim x = 0), \ x, &(dim y = 0) \end{cases} $

## defintion of MoeOperator

X? ≜ X¹ ∪ X⁰
F(X) ≜ (X⁺)?
X* ≜ F(X)
X⁺ ≜ X × X*
MadGrammer(<L, P, ⇒, ⇔, ≡ₛ>) : P ⊆ {(x, y) | x, y ∈ F(L)}, x ⇒¹ y ↔ P(x, y), x ⇒⁰ y ↔ x = y, x ⇔ⁿ y ↔ (x ⇒ⁿ y ∧ y ⇒ⁿ x), (∀n ∈ ℕ ∩ [2, ∞), x ⇒ⁿ y ↔ ∃z ⇒⁽ⁿ⁻¹⁾ y, x ⇒¹z), (x ⇒* y ↔ ∃n ∈ ℕ₀, x ⇒ⁿ y), x ⇒° y ↔ (x ⇒⁰ y ∨ x ⇒¹ y), x ≡ₛ y ↔ (∃z, (x ⇒* z) ↔ (y ⇒* z))
MadGrammerCore(<L, P>) : ∃<⇒, ⇔, ≡ₛ>, MadGrammer(<L, P, ⇒, ⇔, ≡ₛ>)
MadGrammerize ≜ ϝ<L, P> : MadGrammerCore. ε<L, P, ⇒, ⇔, ≡ₛ> (MadGrammer) : MadGrammer
EquivalenceRelation(R) : (∃x, R(x, x)), (∀R(x, y), R(y, x) ∧ (∀R(y, z), R(y, z)))
EquivalenceRangeRelation(R, S) : S = {x | ∃y, R(x, y)}
EquivalenceClass ≜ ϝR : EquivalenceRelation. (ϝx : εS. {y | R(x, y)} : 𝒫(S) (∈EquivalenceRelation[{R}])) : 𝔉(EquivalenceRangeRelation[EquivalenceRelation], {𝒫(x) | x ∈ EquivalenceRangeRelation[EquivalenceRelation]})
compile ≜ ϝ<L, P, ⇒, ⇔, ≡ₛ> : MadGrammer. EquivalenceClass(≡ₛ) : codom EquivalenceClass

StringRelationship(<L, P>, x) : x ∈ F(L), MadGrammerCore(<L, P>), x ∈ dom compile(MadGrammerize(L, P))
MadString ≜ ϝ(<L, P>, x) : StringRelationship. compile(MadGrammerize(L, P))(x) : codom compile(MadGrammerize(L, P))

> 
> # definition of MoeOperator '♡'
> 
> <L, P>♡s ≜ MadString(<L, P>, s)
> 

## defintion of MadOperator

1. definition of encoderize
2. definition of MadOperator

### definition of encoderize

first(x, y) ≜ x
last(x, y) ≜ y
congruence ≜ ϝ(n, m) : ℤ². n + mℤ : 𝒫(ℤ)
tip) 하단 n.b.문단 참고
abs(x) ≜ +√(x²)
MinRelation(<S, ≤>, m) : (m ∈ S ∧ ∀x ∈ S, m ≤ x) ∧ (∀x, y ∈ S, (x ≤ y ∨ y ≤ x) ∧ ((x ≤ y ∧ y ≤ x) → x = y) ∧ (∀z ∈ S, (x ≤ y ∧ y ≤ z) → x ≤ z))
WellOrderdSet(S, ≤) : ∃m, WellOrderdSet(<S, ≤>, m)
min ≜ ϝ<S, ≤> : WellOrderdSet. (ϝX : 𝒫(S). εm (WellOrderdSet[{<X, ≤>}]) : S) : {f ∈ 𝔉(𝒫(S), S) | ∃(≤), WellOrderdSet(S, ≤)}
unsigned2natural ≜ ϝx : ran congruence. min(ℕ₀, ≤)(abs[x]) : ℕ₀
SignituredTuple(L, t) : L ∈ ℕ₀, (L = 0 → t = ε), (L = 1 → (t ∉ dom first ∨ SignituredTuple(2, t))), (L > 1 → (t ∈ dom first ∧ SignituredTuple(L - 1, last(t))))
isend ≜ ϝL : ℕ₀. (ϝi : ℕ₀. δ₍ᵢ₊₁₎ᴸ : {0, 1}) : 𝔉(ℕ₀, {0, 1})
tidx ≜ ϝ(i, L, t) : ℕ₀ × SignituredTuple. firstⁱˢᵉⁿᵈ⁽ᴸ⁾⁽ⁱ⁾(lastᴸ(t)) : {y = firstⁱˢᵉⁿᵈ⁽ᴸ⁾⁽ⁱ⁾(lastᴸ(t)) | (i, L, t) ∈ ℕ₀ × SignituredTuple}
EncodingTablize ≜ ϝ(L, s) : SignituredTuple. (ϝi : dom unsigned2natural. tidx(unsigned2natural(i), L, s) : codom tidx) : 𝔉(dom unsigned2natural, codom tidx)
Φ(encoderize, x, y) : $\begin{cases} encoderize(x)(y) = EncodingTablize(x)(y), &(y ∉ dom first), \ encoderize(x)(y) = (EncodingTablize(x)(first(y)), encoderize(x)(last(y))), &(y ∈ dom first) \end{cases}$
encoderize ≜ ϝx : dom EncodingTablize. (ϝy : (dom EncodingTablize(x))*. encoderize(x)(y) : (codom EncodingTablize(x))*) : {𝔉((dom EncodingTablize(x))*, (codom EncodingTablize(x))*) | x ∈ dom EncodingTablize} s.t. (encoderize(x)(ε) = "") ∧ Φ(encoderize, x, y)

#### n.b. 주의 : 대수학의 지랄난 표기법을 이용했음에 주의.

과거 포스트와, 형식적 정의 : 
```
# 대수학의 이상한(へんな) 표기법

Step 1. へんの정의

Φ(x, t, a, c) : $\begin{cases} t = (a, c), &(x), \ t = (c, a), &(¬x) \end{cases}$
Ψ(f) : f ∈ 𝔉((codom f)², codom f)
∀Ψ(f), LR(f) = (𝔹, 𝔉(codom f, 𝔉(codom f, codom f)), {(x, y) | y = (codom f, 𝔉(codom f, codom f), graph y) ∧ (graph y = {(a, b) | b = (codom f, codom f, graph b) ∧ (graph b = {(c, d) | d = f(t) ∧ Φ(x, t, a, c)})})})
인 LR(f)에 대해서,

만약, (ϝx : X. y : Y) = (X, Y, {(x, y) | x ∈ X})이라면,

LR(f) = (ϝx : 𝔹. (ϝa : codom f. (ϝc : codom f. f(t) s.t. Φ(x, t, a, c) : codom f) : 𝔉(codom f, codom f)) : 𝔉(codom f, 𝔉(codom f, codom f)))임이 당연하므로,

LR(f)(x)(a)(c) = f(t) s.t. Φ(x, t, a, c)이므로,

LR(f)(x)(a)(c) = f(t) [t := $\begin{cases} (a, c), &(x), \ (c, a), &(¬x) \end{cases}$]임이 당연하고,

그러므로,

LR(f)(T) = (ϝx : codom f. (ϝy. codom f. f(x, y) : codom f) : 𝔉(codom f, codom f))이며
LR(f)(F) = (ϝx : codom f. (ϝy. codom f. f(y, a) : codom f) : 𝔉(codom f, codom f))임이 당연하다.

이때,

∀Ψ(f), (Left(f), Right(f)) = (LR(f)(F), LR(f)(T))인 Left, Right에 대하여,

Left(f)(x) = ϝy : codom f. f(x, y) : codom f
Right(f)(x) = ϝy : codom f. f(y, x) : codom f
임이 당연하다.

그리고,

P(A) = 2ᴬ = {S | S ⊆ A}
Θ(f, x, y) : Θ(y, x) ∨ (x ∈ codom f ∧ (y ∈ P(codom f) ∨ ∃S, 𝔉(S, codom f))
K(f, x, y, p, q) : $\begin{cases} p, &(x ∈ codom f), \ q, &(y ∈ codom f) \end{cases}$
∀Ψ(f), ∀Θ(f, x, y), K(f, x, y, へんな(f, x, y) = へんな(L(f)(x))(y), へんな(R(f)(y))(x)))이며
B(f, x, p, q) : $\begin{cases}, p, &(x ∈ P(codom f)), \ q, &(x ∉ P(codom f))
A(f, x) : x ∈ P(codom f) ∨ (∃S, x ∈ 𝔉(S, codom f))
∀f ∈ 𝔉(dom f, dom f), ∀A(f, x), B(f, x, へんな(f)(x) = {f(y) | y ∈ x}, へんな(f)(x) = f ◦ x)인 へんな에 대해,

へんな는 함수라기보단 수식 へんな(f)(x)으로 정의된다.

Step 2. 대수학도 == へんなひと

+ : S² ↦ S
× : S² ↦ S
일 시,

x ∈ S, y ∉ S인데, x + y나 xy라 적었다면 빼박, へんなことです。wwww

진짜 ㅈㄴ ㅈㄴ ㅈㄴ まじで はん。

x + y = へんな(+, x, y)
xy = へんな(×, x, y)임.

미친거 아님?ㅋㅋㅋㅋ

대체 왜 집합 y에 S의 원소 x을 덧셈 뺄쌤하고, 함수 y에, S의 원소 x를 덧셈 뺄샘할 발상을 하는거임? 왜????

수학자들이 ㅈㄴ へんーです。

## 재일 ㅈㄹ난 이유

ㅈㄴ 골때리는건, A/B = {x + B | x ∈ A}란거임.

Step 1. 하... 일단 정수론에서, 나머지와 나누어떨어짐을, 정수론적 시각에서 접근해보자.

연산기호 '+', '-', '×'와, 나누어 이항관계 기호인 떨어짐 기호 '|'및 삼한관계 기호인, 합동기호 '≡'에 대하여,

모델 M(D) = <D, 0, +, -, ×, |, ≡>이 뭐냐 하면,

x | y : ∃z ∈ D, x = yz
x ≡ y (mod. m) : m | (x - y)

임. 그래서, 나머지가 0인게 나누어 떨어지는거임.

그리고, 만약 나눗셈 기호 '÷'를 정의하고싶거든,

집합론적으로, ÷ : {(m, n) | n ≡ 0 (mod. m)} ↦ D.에서 정의하는수밖에 없고.

근데, D에다가 유리수같은거 넣는건 쓸대없는짓임. 나누어떨어짐 개념은, 체같은거 말고, 정수론에서 다루어지는거라.

즉, 정수론에서, D = ℤ고, 에초에, D가 자연수인경우를 논하든 뭐하든, 에초에, "D에서"라는 말 하나만 붙여주므로써, M(D)에서의 논의를 다 하기 때문에 뭐... 문제 없는거임.

그리고 대망의... 몫군의 원소로 만들어버리기.

추상대수적으로 보자면, mod : D² ↦ ∪{D/mD | m ∈ D}인 준동형사상이고

실은 그냥, x mod m = {y | x ≡ y (mod. m)}인 동치류임.

하하.... 나머지 동치류가 몫군이다 이거임.

나머지가 0이면 나누어 떨어지니, 그냥 합동은, 나누어떻어짐으로 정의되며, x ÷ y가 나누어 떻어지면 결괏값 z가 존재하므로, 곱셈의 역산이 나눗셈이니, x = yz란 ㅈㄴ 당연한 소리를 하는게 모델 M(D)랑 '÷'고.

여기까지는 명쾌함.

Step 2. 골때리는 부분

근데 대수학자들이, 수묶음을 추상화하고싶은 욕구가 존나 욕구불만이었는진 모르겠지만,

x mod m = x + mD로 정의해버린거임.

크아아아아아악 미친놈들아!!!

Q. 이봐요, 대체 왜 집합에 곱셈을 하는데? 벌써 모델 M(D)를 벗어났잖아.
A. 그거? 집합에도 연산 정의되면 편하잖아 한잔 혀
Q. 미친놈들아, 그럼 일관되게, 나눗셈 '/'에 대해서도, X/Y를 재대로 정의하시든가!! 일관되지 않잖아! 너희가 그렇게 정의하지만 않으면, 다른 수학분야도 일관될수 있어!
A. 알아 ㅋ, 그치만, {y | x ≡ y (mod. m)} = x + mD식으로 몫군 만들때 쓸래.

대수학자 : 수 묶음으로 생각하고 싶으니까, 대수학 중심적으로 생각할래.
대수학자 중심주의 왈 : 집합에 연산을 정의했어. 근데, 질문자는 불만이 있는데 대수학자는 없네? 무슨차일까? 한쪽은, 집합을 수 묶음으로 보네?

(그날 형식주의자는 떠올렸다.)

크아아악!! 왜 A/B = {x + B | x ∈ A}인거야!!!

미친 직관주의자들아!!! A/kB를, a ∈ A, kb ∈ B일시, a ÷ k = b ••• r일시 동치류 r로 정의하는건, 지극히 인간적인 직관인거 아니냐!!

직관을 주장할거면 형식화하라고!!! 형식으로 정의 안되는 직관은, 수학 언어 밖에 있는거잖아!!!
```

### definition of MadOperator

EvilLary(<L, s, R>, <X, P>) : X = codom EncodingTablize(L, s), P = {(encoderize(L, s)(x), encoderize(L, s)(y)) | R(x, y)}
LaryLattice(L, s, R) : (L, s) ∈ EncoderTable ∧ R ⊆ {(x, y) | x, y ∈ (dom EncoderTable(L, s))*} ∧ (∃<X, P>, EvilLary(<L, s, R>, <X, P>))
EvalLary ≜ ϝLL : LaryLattice. εG (EvilLary[{LL}]) : MadGrammerCore
Larry(<L, s, R>, v) : LaryLattice(L, s, R), v ∈ (ℤ/Lℤ), StringRelationship(EvalLarry(L, s, R), encoder(L, s, R)(v))
AngelLary ≜ ϝ(LL, s) : Larry. EvalLarg(LL)♡(encoder(LL)(s)) : codom MadString

 > 
 > # definition of MadOperator '♥︎'
 > 
 > LL♥︎s ≜ AngelLary(LL, s)
 > 