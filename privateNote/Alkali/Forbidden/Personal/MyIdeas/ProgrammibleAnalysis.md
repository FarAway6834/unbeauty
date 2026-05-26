# ProgrammibleAnalysis

1. 논의에 필요한 자료
2. 페아노 공리계부터 제귀 함수까지

## 논의에 필요한 자료

1. Operodepredrofunctionalang
2. select
3. ProgrammibleAnalysis

### Operodepredrofunctionalang

```markdown
# OperodepredrofunctionalLang

operodepredrofunctional lang의 정의와 operodepredrodel에 대해 다루겠다.

## operodepredrodel

WellOrdering(S, ≤) : (∀x, y, z ∈ S, (x ≤ y ∨ y ≤ x) ∧ ((x ≤ y ∧ y ≤ x) → x = y) ∧ ((x ≤ y ∧ y ≤ z) → x ≤ z) ∧ (∃!m ∈ S s.t. m ≤ x)) ∧ S ≠ ∅

Predrel(S) ≜ S ∪ 𝔹

first(x, y) ≜ x
last(x, y) ≜ y
x concat y = \begin{cases} (x, y), &(x ∉ dom first ∧ y ≠ ε ≠ x), \ first(x) concat (last(x) concat y), &(x ∈ first ∧ y ≠ ε ≠ x), \ x, &(y = ε), \ y, &(x = ε) \end{cases}

minf ≜ ϝ(S, ≤) : WellOrdering. (ϝx : P(S). εm (∀x ∈ S, m ≤ x) : S) : {𝔉(P(S), S) | S = first(x) ∧ x ∈ WellOrdering}
SetTuplize(S, ≤) ≜ \begin{cases} minf(S, ≤)(S) concat SetTuplize(S ∖ {minf(S, ≤)(S)}, ≤), &(S ≠ ∅, \ ε,  &(S = ∅) \end{cases}

뭐... SetTuplize는 알아서 잘 튜플을 만들겠지 뭐... 비가산길이에서 튜플이 작동하는지는 잘 모르겠지만...

참고로, 저 정의를 보면 dom minf과 dom SetTuplize가 같다는 개똥직관을 느낄수 있지만, 실제론, dom SetTuplize = dom minf ∪ {(∅, x) | x ∈ dom first}다. 에초에 S = ∅인 경우에 대해서 정의되어야 정의되는, 너무 당연한 소리지만.

oper(S) ≜ lim_{n ⟶ ∞} ∪ᵢ₌₀ⁿ 𝔉(Sⁱ, S)
pred(S) ≜ lim_{n ⟶ ∞} ∪ᵢ₌₀ⁿ P(Sⁱ)

oper는 모델의 도메인이 S일때, n=0~∞항연산자의 집합을, pred는 모델의 도메인이 S일떼, n=0~∞항 술어임이 너무 자명하므로, 전혀 탐구할 가치가 없다고 느낀다.

FullSpecifiedModel(S, ≤) = S concat SetTuplize(S, ≤) concar SetTuplize(oper(S), ≤) concat SetTuplize(pred(S), ≤)

이 (여기도 개똥직관으로 ≤가 S²의 부분집합이라고 착각하는 놈들이 있을까봐 말하는데, 여기서 ≤는 (S ∪ oper(S) ∪ pred(S))²의 부분집합이여야만 정의된다.) FullSpecifiedModel은 무엇인가 하면,
FullSpecifiedModel(S, ≤)는 상수기호들의 튜플 SetTuplize(S, ≤), 함수•연산자기호들의 튜플 SetTuplize(oper(S), ≤), 술어•관계•논리연결사기호들의 튜플 SetTuplize(pred(S), ≤)를 concat해서 만든 모델로, S위에서의 모든 원소를 상수로 다 선언하고, 모든 함수를 다 선언하고, 모든 술어를 다 선언한 상태라 보면 된다.

그냥 그걸 표기하는 용도다. 그러려고 만든거임.

operodel(S) ≜ oper(S) ∪ S

이러한 operodel(S)은 어떤 특별한 모델의 도메인이다. 조금 이따가 알아보자.

Kₛ|ₛ ≜ ϝx:s. (s⁰, s, s⁰ × {x}):oper(s)
Kₛ|ₒₚₑᵣ₍ₛ₎ ≜ ϝx:oper(s). x:oper(s)

이렇게 Kₛ가 정의된다.

이때, <operodel(s), Kₛ>는 닫힌 연산을 이룬다.

pf.

x ∈ operodel(s) ↔ (x ∈ oper(s) ∨ x ∈ s)이니,

x ∈ s → Kₛ(x) = Kₛ|ₛ(x), x ∈ oper(s) → Kₛ(x) = Kₛ|ₒₚₑᵣ₍ₛ₎(x)로,

$Kₛ(x) = \begin{cases} Kₛ|ₛ, & (x ∈ s), \ Kₛ|ₒₚₑᵣ₍ₛ₎(x), & (x ∈ oper(S)) \end{cases}$다.

즉, Kₛ : operodel(s) ↦ operodel(s)로 operodel(s)에 대해 닫혀있다.

Q.E.D.

t₀ = SetTuplize(S, ≤)
t₁ = SetTuplize(oper(S), ≤)
t₂ = SetTuplize(oper²(S), ≤)
t₃ = SetTuplize(pred(S), ≤),
t₄ = SetTuplize(pred(oper(S)), ≤)
t₅ = t₀ concat t₁
t₆ = t₁ concat t₂
t₇ = t₀ concat t₁ concat t₆
t₈ = t₃ concat t₄
s₀ = S
s₁ = oper(S)
s₂ = oper(operodel(S)) ∖ operodel(oper(S))
s₃ = pred(operodel(S)) \ (pred(S) ∪ pred(oper(S)))

FullSpecifiedModel(operodel(S), ≤) = operodel(S) concat t₇ concat SetTuplize(s₂ , ≤) concat t₈ concat SetTuplize(s₃ , ≤)다.

FullSpecifiedModel(S, ≤) = s₀ concat t₅ concat t₃
FullSpecifiedModel(oper(S), ≤) = s₁ concat t₆ concat t₄
으로, FullSpecifiedModel(S, ≤)와 FullSpecifiedModel(oper(S), ≤)의 구성 요소를 FullSpecifiedModel(operodel(S), ≤)가 그대로 가지고 있음을 알수 있고,

두 모델 FullSpecifiedModel(S, ≤), FullSpecifiedModel(oper(S), ≤)이 Kₛ ∈ SetTuplize(s₂ , ≤)를 통해 준동형임을 알 수 있다.

이러한 준동형성의 증명은, 모델 FullSpecifiedModel(operodel(S), ≤)에서 귀결이며, 이러한 특별한 모델의 도메인이 바로 operodel(S)인것이다.

operodel^∞(S) ≜ lim_{n ⟶ ∞} ∪ᵢ₌₀ⁿ operodelⁱ(S)

뭐... operodel을 k번 적용시 (k-1)번 적용한것을 포함하므로, 무한번째에도 대강 저렇게 되는걸 알수 있으니, 걍 넘어가라. 그냥 operodel^∞을 정의하기 위해서 저랬을 뿐이니.

Predel(S) ≜ P(S) ∪ S
x ∈ₛ y : (x, y) ∈ Predel(s)² ∧ x ∈ y
(∈ₛ y)(x) ≜ x ∈ₛ y

<Predel(S), ∈ₛ>는 멤버십을 서술하는 모델이다. 이 모델을 통해 맴버십을 서술할수 있다.

FullSpecifiedModel(Predel(S), ≤)에서, 튜플의 어느 인덱스에는 무조건 ∈ₛ가 존재한다.

Predrodel(S) ≜ Predel(Predrel(S))
smember : Predrodel(S)² ↦ Predrodel(S)
x smember y ≜ \begin{cases} T, &(y ∈ₛ x), \ F, &(y ∉ₛ x) \end{cases}

(tip : smember라는 명칭은 x's member라는 의미로 작한 명칭이다, 물론 명칭따위가 크게 중요하지 않고 beer로 바뀌더라도 무관하겠다만)

<Predrodel(S), smember>는 마그마를 이룬다만, 그 이상의 특별함점은 없다.

물론, 단순히 x ∉ₛ y : ¬(x ∈ₛ y)인지라, (x, y) ∈ S² ∪P(S)²에서 항상 x ∉ₛ y가 참이긴 하다. 뭐... 에초에 당연한거 아닌가? 그렇지 않을때 비교되지 않으라는 법은 인간의 착각이고, 똥멍청이나 하는 생각이다.

술어에선, 인자가 시스템 내에 있으면 항상 참이나 거짓으로 술어값이 정의되니까 (비결정적인 경우를 빼면), 당연히 술어에서 참 거짓으로 판단 대상이 아닌 경우 냅다 false를 뱉는게 당연한거다.

술어논리만 똑바로 쳐 알아도 그럼 바보같은 생각은 안하니 굳이 여기서 다룰 필욘 없지만.

참고로, ran smember = 𝔹 = {T, F}다. (너무 자명한 사실이긴 하지만, 에초에 아까전부터 자명한소리만 지껄이고 있었으니 뭐...)

operodepredrodel ≜ operodel ◦ predrodel
operodepredrodel^∞ ≜ operodel^∞ ◦ predrodel

뭐... 에초에 𝔹 ⊆ S면, operodepredrodelⁿ(S) = operodelⁿ(S)니, 굳이 설명 안해도, 똥멍청이가 아니면, operodepredrodel는, 𝔹 ⊆ S일시, S∖𝔹 ⊆ X ⊆ S 에서의, operodelⁿ(S) (=operodepredrodelⁿ(X))를 X에 대하여 표기할때 사용하는것이란걸 알것이라 보고 넘어가겠다.

## operodepredrofunctional lang

isFunctionalModelOf(M, S) : M = FullSpecifiedModel(oper(S), ≤)

 > ∀isFunctionalModelOf(M, S)에서, 표기"M " concat fn1 concat "(Mⁿ) " = " concat fn2은, fn1(x₁, ..., xₙ) = (Kₛ ◦ fn2)(Kₛ⁻¹(x₁), ..., Kₛ⁻¹(xₙ))
로 정의된다. 그리고, 이때 `fn1 :: M`는 참이다.

그렇다. operodepredrodel은 이러한 operodepredrofunctional lang을 규정하는데 사용된다.

이로써, `<type> <fname>(<type>ⁿ) : <type>`는 식의 형식언어체계로, 모델론을 더 쉽게 이해하는 언어인 operodepredrofunctional lang가 정의된다.
```

### select

```markdown
# about, sequitur ad int select in predrel select

Predrel(S) ≜ S ∪ 𝔹
Select(X) ≜ <Predrel(X), •?•:•> s.t. •?•:• = (dom •?•:•, codom •?•:•, graph •?•:•) ∧ graph •?•:• = graph (•?•:•)|_{𝔹 × Prederel(X)²} ∪ graph (?•:•)|_{X × Predrel(X)²} ∧ (∀x, y ∈ Predel(X), ∀v ∈ X, (•?•:•)|_{𝔹 × Predrel(X)²}(T, x, y) = (•?•:•)|_{X × Predrel(X)²}(v, x, y) = x = graph (•?•:•)|_{𝔹 × Predrel(X)²}(F, y, x))
일 시, 모델 Select(X)에서, •?•:•는 선택 기능을 하지.

더 나아가서,

int : Predrel(X) ↦ X ∪ {0, 1}
bool : X ∪ {0, 1} ↦ Predrel(X)
int(x) ≜ (x ∈ 𝔹)?(x?1:0):x
bool(x) ≜ (x ∈ {0, 1})?((x∈[1,1])?T:F):x
에 대하여,

int(bool(x)) = x 이므로,

intSelect(X) = <X ∪ {0, 1}, •¿•:•> s.t. p¿x:y = int(bool(p)?bool(x):bool(y))

인 모델 intSelect(X)에 대해, 선택 로직은 intSelect(X)으로 처리 가능함이 귀결임.
```

### ProgrammibleAnalysis

```markdown
# MadReal Model, Turing Complete Analysis

Kₛ|ₛ ≜ ϝx:s. (s⁰, s, s⁰ × {x}):oper(s)
Kₛ|ₒₚₑᵣ₍ₛ₎ ≜ ϝx:oper(s). x:oper(s)

oper(S) ≜ lim_{n ⟶ ∞} ∪ᵢ₌₀ⁿ 𝔉(Sⁱ, S)
operodel(S) ≜ oper(S) ∪ S

에서, 모델 <operodel(S), Kₛ>에 해당하며, 동시에,

intSelect(S)에 해당하는 모델은,

{0, 1} ⊆ S인 모델임.

MadReal ≜ (operodel(ℚ), K_ℚ, •¿•:•, TailReqOpt, ◦, =, <, >, ≤, ≥, lim•=lim•, lim•<lim•, lim•>lim•, lim•≤lim•, lim•≥lim•, lim•=∞, lim•=-∞, Cauchy, (∈oper(ℚ)))는

∀x, y ∈ ℚ, ∀f, g ∈ oper(ℚ)
1. x ◦ y = x
2. f ◦ g : ℚ ↦ ℚ
3. (f ◦ g)(x) = f(g(x))

1. ℚ ⊆ ker TailReqOpt
∀x ∈ ℚ, ∀p, f, g ∈ oper(ℚ) s.t. (p, f, g) ∉ ker TailReqOpt
1. TailReqOpt(p, f, g) : ℚ ↦ ℚ
2. TailReqOpt(p, f, g)(x) = (p(x)?(TailReqOpt(p, f, g)◦f):g)(x)
∀x ∈ ℚ, ∀p, f, g ∈ oper(ℚ) s.t. (p, f, g) ∈ ker TailReqOpt
1. ∃X ⊆ ℚ, ∀h ∈ 𝔉(X, ℚ), h(x) = (p(x)?(h◦f):g)(x) → h ∉ oper(ℚ)
1. Tip 1 : 어떤 실수 x에 대해서 단 한번이라도, h가 정의 안됨은, 그 x에서 무한 루프에 갇힌다는거다.
1. Tip 2 : 저러한 h의 경우엔 함수로 반환해주면, TailReqOpt는 더이상 모델에서 닫히지 않기에, 함수가 아닌 상수 0으로 반환한다. 그러므로, 해집합이 멈추지 않는 프로그램이라는거.
1. Tip 3. ∀p, f, g ∈ oper(ℚ), ∃X ⊆ ℚ, ∀h ∈ 𝔉(X, ℚ), ((∀x ∈ X, h(x) = (p(x)?(h◦f):g)(x)) ∧ X ≠ ℚ) → (p, f, g) ∈ ker TailReqOpt

(∈oper(ℚ))(f) : f ∈ oper(ℚ)
Cauchy(f) : (∈oper(ℚ))(f) ∧ (∀ε > 0, ∃N ∈ ℕ s.t. ∀n, m ∈ ℕ, n > N < m → |f(n) - f(m)| < ε)
(lim•=∞)(f) : (∈oper(ℚ))(f) ∧ (∀K > 0, ∃N ∈ ℕ s.t. ∀n ∈ ℕ, n > N → f(n) > K)
(lim•=-∞)(f) : (∈oper(ℚ))(f) ∧ (∀K > 0, ∃N ∈ ℕ s.t. ∀n ∈ ℕ, n > N → -f(n) > K)
(lim•=lim•)(f, g) : (f, g ∈ oper(ℚ)) ∧ (∀ε > 0, ∃N ∈ ℕ s.t. ∀n ∈ ℕ, n > N → |f(n) - g(n)| < ε)
(lim•>lim•)(f, g) : (f, g ∈ oper(ℚ)) ∧ (∀ε > 0, ∃N ∈ ℕ s.t. ∀n ∈ ℕ, n > N → f(n) - g(n) > K)
(lim•<lim•)(f, g) : (lim•>lim•)(g, f)
(lim•≤lim•)(f, g) : (lim•<lim•)(f, g) ∨ (lim•=lim•)(f, g)
(lim•≥lim•)(f, g) : (lim•≤lim•)(g, f)
이다. 즉, 이건 코시 수열의 공리계라는거다.

Fundamental Theorem of Mad Real : 
1. ran K_ℚ ⊆ Cauchy
2. ∀p ∈ {0, 1}, ∀f, g ∈ oper(ℚ), p¿f:g = $\begin{cases} f, &(p = 1), \ g, &(p = 0) \end{cases}$

이를 통해, MadReal은 튜링 완전하며, 동시에, 유리수의 폐포를 포함함을 알 수 있다.

Functional Programmible Halting Problem : ker TailReqOpt를 구하는 알고리즘은 존재하지 않는다.

joke : 알고리즘으로써 오라클은 없는데, 왜 파렴치한 자본주의자인 법인으로써 오라클은 있는걸까? ㅋㅋㅋㅋㅋ 독과점 오라클좌 ㄷㄷ ㅋㅋㅋㅋ
```

## 페아노 공리계부터 제귀 함수까지

1. 변형 폐아노 공리계
2. 제귀 정리
3. 수열의 귀납적 정의
4. 사칙연산
5. 사칙연산의 대수구조
6. 함수 합성 대수
7. 제귀 함수를 가진 모델의 언어를 특히 튜링 언어적인 관점에서

### 변형 폐아노 공리계

∀k ∈ ℤ, ∀ℕₖ s.t. ℙ(ℕₖ, k, s), ℕₛ₍ₖ₎ ≜ s[ℕₖ]

ℙ₁(ℕₖ, k, s) : k ∈ ℕₖ
ℙ₂(ℕₖ, k, s) : ∀n ∈ ℕₖ, s(n) ∈ ℕₖ
ℙ₃(ℕₖ, k, s) : ∄n ∈ ℕₖ, s(n) = k
ℙ₄(ℕₖ, k, s) : ∀n, m ∈ ℕₖ, s(n) = s(m) → n = m
ℙ₅(ℕₖ, k, s) : ∀X ⊆ ℕₖ, (ℙ₁(X, k, s) ∧ ℙ₂(X, k, s)) → X = ℕₖ
ℙ(ℕₖ, k, s) : ℙ₁(ℕₖ, k, s) ∧ ℙ₂(ℕₖ, k, s) ∧ ℙ₃(ℕₖ, k, s) ∧ ℙ₄(ℕₖ, k, s) ∧ ℙ₅(ℕₖ, k, s)

Theorem of Naturality : ∀k ∈ ℤ, ∀ℕₖ, ∀ℕₛ₍ₖ₎, (ℕₛ₍ₖ₎ = s[ℕₖ] → (ℙ(ℕₛ₍ₖ₎, s(k), s) ↔ ℙ(ℕₖ, k, s))
explain)

하한유계정수집합열 ℕₖ는 변형 폐아노 공리계 ℙ를 만족시키는 집합이다.

### 수학적 귀납법

ℕₖ위의 술어 Φ가 Φₖ이고, Φₘ → Φₛ₍ₘ₎이면, Φ = ℕₖ다.

이는 변형 페아노 공리계 제 5 공리, 수학적 귀납 원리 ℙ₅(ℕₖ, k, s)에서 함의된다.

<ℕₖ, Φ> ⊨ ((Φₖ, Φₘ → Φₛ₍ₘ₎) → Φ = ℕₖ란 거다.

MathmaticalInductionₖ(Φ) : (<ℕₖ, Φ> ⊨ (Φₖ, Φₘ → Φₛ₍ₘ₎))
에 대해,

MathmaticalInductionₖ(Φ)인 Φ는 <ℕₖ, Φ>에서 항진술어고, 문장 "Φₖ"는 항진명제다.

### 재귀 정리

precessor p를
p = s⁻¹라 하자.

제귀 정리 : ∀A, ∀F ∈ 𝔉(A, A), ∀a ∈ A, ∃!g ∈ 𝔉(ℕ₀, A)
1. g(0) = a
2. g(s(n)) = F(g(n))
explain)
일단, ∀x ∈ ℕ₀, ∃!y = g(x)에 대하여 논증을 전개해나가자.
일단, g(x) = (x=0)?a:F(g(x))임이 당연하다.

g|_{[0, 0]} = ([0, 0], A, graph g|_{[0, 0]}) = ([0, 0], A, {(0, a)})
g|_{ℕₖ} = F ◦ g|_{ℕₚ₍ₖ₎} ◦ p = (ℕₖ, codom F, {(x, y) | y = F(u) ∧ u = g|_{ℕₚ₍ₖ₎}(t) ∧ t = p(x)})
이고,
ran g|_{[0, 0]} ⊆ A, ran g|_{ℕₖ} ⊆ ran F ⊆ codom F = codom g|_{ℕₖ}임이 당연하다.
뭐... 너무 당연하지...
암튼, h(k, g|_{ℕₖ}) = (ℕₖ, codom F, {(x, y) | y = F(u) ∧ u = g|_{ℕₖ}(t) ∧ t = p(x)})에 대해, h를 통해, 이후 그래프가 귀납적으로 정의됨이, 수학적 귀납법에 따라 당연하다.

임의의 x를 짚었을때, 그에 대응하는 증명이 존재한다는거.

### 수열의 귀납적 정의

제귀 정리를 만족시키는 ℕₖ에서 정의되는 수열 a는,

```
1. Aₖ = a
2. Aₖ = any formula
```

꼴로 작성해서 귀납적으로 정의하도록 한다.

### 사칙연산

임의의 ℕₖ위에서 사칙연산은 다음과 같이 정의된다. (즉, ℤ범위로 보는거다.)

덧셈 : m + n = addₘ(n)인 다음과 같이 정의되는 함수열 add로 정의한다.
1. addₘ(0) = m
2. addₘ(s(n)) = s(addₘ(n))

뺄셈 : m - n = subₘ(n)인 다음과 같이 정의되는 함수열 sub로 정의한다.
1. subₘ(0) = m
2. subₘ(s(n)) = d(subₘ(n))

아아... 이래서 뺄셈은 범자연수에서 정의되지 않는 경우가 존재할수 있다.

곱셈 : m × n = motₘ(n)
1. motₘ(0) = 0
2. motₘ(s(n)) = n + motₘ(n)

우효www이건 잘 정의되지롱

x | y : ∃n ∈ ℤ, y = xn이렇게 나누어 떨어짐이 정의될때

나눗셈 : m ÷ n = m / n
1. m ÷ 0은 정의되지 않는다.
2. n | m가 거짓이면 정의되지 않는다.
3. m ÷ n = s((m - n) ÷ n)다.
나눗셈만 뭣같다. 이걸 잘 정의하려면 ℚ여야 한다.

이제 다음 쳅터에선 사칙연산의 대수구조를 분석해보자.

### 사칙연산의 대수구조

에초에, 수 k는 k = sᵏ(0)으로 정의되니까, 그걸 감안하고 듣자.

1. 0을 포함한 집합에서, 덧셈의 단위모노이드성 : 덧셈의 우항등원 0에 대해, add₀(k) = sᵏ(0)임이 수학적 귀납법으로 증명되므로, 덧셈은 0을 항등원으로 가진다.
2. x + 1 = s(x)이므로, (x + sⁿ(0)) + 1 = x + sˢ⁽ⁿ⁾(0) = sˢ⁽ⁿ⁾(0)임.
3. s(n + m) = s(sᵐ(n)) = (s◦sᵐ)(n) = sˢ⁽ᵐ⁾(n) = (sᵐ◦s)(n) = sᵐ(s(n)) = s(n) + m임.
4. addₛ₍ₖ₎ = s◦addₖ
5. 그러므로, 1 + x = x + 1임.
6. 0을 포함한 집합에서, 덧셈의 가환단위마그마가 되는 특성 : sᵐ(0 + x) = sᵐ(x) = x + m = m + x임. 그러므로, 가환단위마그마가 됨.
7. 0을 포함한 집합에서, 덧셈은 가환모노이드임. (x + m) + n = sⁿ(x + m) = sⁿ(m + x) = sⁿ(m) + x = x + sⁿ(m) = x + (m + n)임. ㅋㅋㅋㅋ
8. ℕₖ에서, k < 0면, p(0) ~ pᵏ(0)는 각각 1 ~ k의 역원임.
9. 정수에서 덧셈은 가환군을 이룸 : ℤ ≜ lim_{n ⟶ ∞} ∪ₖ₌₀ⁿ ℕ_{pᵏ(0)}인지라, 정수에선, 항상 가역임.

뺄셈을 보자.
(x + y) - y = x다. 그렇다. 항상 Quasigroup(S, +, -)즉, 유사군을 이루는, 다시말해, 뺄셈은 걍 덧셈의 역산따리일 뿐.
나눗셈도, Quasigroup(S, ×, ÷)로 곱셈의 역산일 뿐인 놈이다.

곱셈을 보자.

1. 우분배 법칙 성립 : x × (n + sᵏ(0)) = x × (sᵏ(n)) = Σᵢ₌₁ⁿ⁺ᵏ x = Σᵢ₌₁ᵏ x + Σᵢ₌₁ⁿ x인데, 이는, 곱셈의 정의에서, 제귀함수로 정의했기테, sᵏ(n)이라면, Σᵢ₌₁ᵏ x가 미리 추가될수밨에 없는거다.

잠시 거듭제곱을 좀 보자.

x ↑ y = xʸ

(thanks! kunth)

x ↑ s(y) = x × (x ↑ y)로,

아 근데 도저히 functor표기 못참겠다

(* x)(y) = y * x = (y *)(x)라고 일단 알아놔라. *가 <S, *>위에 있다면, oper(S)의 원소인 함수로 대충 표기되니, 엄밀한 정의 신경쓰지 말고.

x ↑ (n + m) = (x ×)ⁿ × (x ×)ᵐ라,

log(x × y) = log(x) + log(y)면,
log⁻¹(x + y) = log⁻¹(x) × log⁻¹(y)가 되는데, 

(x ↑)가 바로 이러한 log⁻¹중 하나다.

암튼, 그래서, 덧셈과 곱셈은 동형이다.

일단, 잠시 급발진을 멈추고, 다시 곱셈으로 돌아가자. 곱셈이 가환군을 이룬다는걸 증명해야, 저런 지수법칙을 증명 가능하기에, 설명을 위해 순환논증을 통해 어거지로 설명할순 없는 노릇이니.

(x × m) × n = ((x × m) +)ⁿ(0) = (((x +)ᵐ(0)) + )ⁿ(0) = Σᵢ₌₁ⁿ Σᵢ₌₁ᵐ x = Σᵢ₌₁ᵐ Σᵢ₌₁ⁿ x = (x × n) × m이다.
x = 1을 대입하면 교환법칙이 성립함을 알 수 있다.
왜냐? 그냥 ab = c에서, a나 b에 1을 대입함으로써, 곱셈이 1을 항등원으로 가짐을 증명할수 있으니, 1이 곱셈의 항등원이기에, 항등원으로 쓸수 있기 때문이다.

(x × y) × z = (y × x) × z = (y × z) × x = x × (y × z)이므로, 결합법칙도 성립한다.

그렇다. 덧셈과 동형이 될수 있다는거다.

암튼, 함수 합성에서 fⁿ의 경우엔, n이 정수일시 fⁿ들의 집합은 정수와 동형이기에, 이런 일이 가능하다.

이게 내가 고 2 때 개발한, 페아노 공리계를 구조적으로 이해하는 핵심적인 방법이다.

think on functional, then put in model.

그냥 모델로 만들어서 이해하는거. 그러면 핵심적인 원리가 추상대수적으로 이해되니까.

### 함수 합성 대수

1. 일반적인 합성 대수
2. fⁿ에서의 합성 대수

#### 일반적인 합성 대수

fun(S) ≜ 𝔉(S, S)라 하자.

이제부터 대수구조 <fun(S), ◦|_{fun(S)²}>에 대해 다룰거다

먼저 ◦가 fun(S)위에 닫혀있는지 확인하기 위해,
f ◦ g가 <S, f, g>인 모델 위에서 있음을 보이자.

해당 모델 위에 있다면, S위에서 정의되야하는데,
dom f ◦ g = dom g = S로 맞다.
그러면, S위에서 닫히기만 하면, 그 위에 있는것인데,
codom f ◦ g = codom f = S로 맞다.

좋다. 그럼 이제 graph ◦|_{fun(S)²}에 대해 알아보자.

(f, g, (dom f ◦ g, codom f ◦ g, graph f ◦ g)) ∈ graph ◦|_{fun(S)²}임이 해설할 필요없이 당연하다.

graph f ◦ g = {(x, f(u)) | u = g(x)}임은, 함수 합성의 정의에 따라 당연하다.

모델 M = <fun(S), ◦|_{fun(S)²}>는 oper(S)가 이루는 모델이 대해, 부분모델(도메인이 부분집합 관계고, 일부 술어와 연산도 모델의 도메인 제한을 통해 제한된 모델)이고, oper(S)는 operodel(S)의 부분모델이다.

그러므로,◦|_{fun(S)²에 대해, f ◦ g는 operodel(S)에서,

(f ◦ g) = (S, S, {(x, f(u)) | u = g(x)})인 원소가 되며,

(f ◦ g)(x) = f(g(x))임과 동치로, 이는 operodel(S)에서, (f ◦ g)(x) = f(g(x))임과 M = <fun(S), ◦|_{fun(S)²}>에서 ◦|_{fun(S)²}의 정의는, 서로가 서로를 증명하는 동치관계다.

즉, 앞선 ◦|_{fun(S)²}의 정의는 (f ◦ g)(x) = f(g(x))라는 기존 정의와 동치다.

operodel에서 볼때)

((f ◦ g)◦h)(x) = f(g(h(x))) = (f ◦ (g ◦ h))(x)
근데, 둘다 fun(S)에 해당하므로, 그래프만 같으면 같은데, 진짜 같아버렸으므로...

◦|_{fun(S)²}는 앞서 말한 모델 M에서 Semigroup을 이룬다.

항등함수의 정의

i_X ≜ (X, X, {(x, x) | x ∈ X})에 따라서,

I = i_S는 fun(S)의 원소이다.

(I◦f)(x) = I(f(x)) = f(x)로, I는 ◦|_{fun(S)²}의 좌항등원이다.
(f ◦ I)(x) = f(I(x)) = f(x)이므로, I는 우항등원이기도 하다.

고로, ◦|_{fun(S)²}는 모노이드를 이룬다.

M을 부분모델로 가지는, oper(S)가 이루는 모델의 부분모델

synmod(S) = <fun(S) ∪ S, ◦|_{(fun(S) ∪ S)²}, •⁻¹>

은 모든 S에 대해 항상 존재한다.

전단사인 f에 대해서, f⁻¹ = (S, S, {(f(x), x) | x ∈ graph f})이기 때문이다.

예외처리를 위해,
1. ∀f ∈ fun(S), ∀x ∈ S, f ◦ x = f(x)
2.  ∀x ∈ S, x ◦ y = x
3.  ∀x s.t. (x ∈ S ∨ ∃(y, z) ∈ S², x(y) = s(z) → x ≠ y), x⁻¹ = 0
로 정의한다.

즉, ker •⁻¹에 해당하는 놈들은 싹다 전단사가 아닌 놈들이다.

하... 닫히게 만들며 예외처리까지 하는거 ㅈㄴ 피곤하다. CPU설계자들도 이렇게 피곤하려나?

재밌는건, 위의 함수합성의 예외처리는, Kₛ를 통해 만든 x로, x ∈ S를 취급해 예외처리를 한다는 점 ㅋ

최종)

어떤 X에선, 모델 M = <X, ◦|_{X²}은 군의 모델이나, 어떤 X에선, 결코 가환모노이드가 될 수 없다.

일단 어떤 X에선, 군이라는 근거론, X ⊆ fun(S), ker •⁻¹|_{X} = ∅이도록 하는 X가 전단사 함수이기만 하면 된다.

그리고, 어떤 X에선 불가능하다는 것에 대한 증명은, 걍 그 X를 보여주겠다.

X = {Kₛ 0, Kₛ 1}

ㄹㅇㅋㅋ, 상수함수들만 있는 X에서 반례인데 당연하지 ㅋㅋㅋ

X = {sha256, md5}

이것도, 아마도, 해쉬함수 순서 다르게 적용하면, 결과 다르다고 알고있다. 코딩 안한지 워낙 오래되서 확실하진 않지만.

암튼 ㅋㅋㅋ 그렇다고.

#### fⁿ에서의 합성 대수

범자연수 집합의 정의
𝕎 ≜ ℕ₀
즉, 하한유계정수집합렬에서 ℕ₀이 바로, 범자연수(Whole Num)집합 𝕎라는 점. 기억하자. 앞으로 이 기호 많이 쓸거다.

fˢ⁽ⁿ⁾ ≜ f ◦ fⁿ에 대해, powersyn(f) = {fⁿ | n ∈ (f ∈ ker •⁻¹)?𝕎:ℤ}라 하자.

powersynmod(f) ≜ <powersyn(f), ◦|_{powersyn(f)²}>라 하자.

모델 powersynmod(f)은 자연수 덧셈이나, 정수 덧셈과 동형이다. 이를 동형사상 없이 보여보자.

일단 시작하기도 전에, 기본적으로 함수 합성 모델은 반군이며, f⁰ = I로, 항등원을 가지므로, 모노이드를 이룬다는 점에서 공통점-1

fⁿ ◦ f = (f◦)ⁿ(f)인지라, f¹에 대해서, 덧셈과 동형이라는 점을 동형사상 없이 생각해보자면,

S? = S¹ ∪ S⁰
S+ = S × S*
S* = (S+)*

모노이드 (S, e, f), 공튜플 ε에 대해서,
first(x, y) = x
last(x, y) = y
일시,
star(S, e, f) : S* ↦ S
star(S, e, f)(ε) = e
star(S, e, f)(x) = x (단. x ∉ dom first)
star(S, e, f)(x, y) = f(x, y) (단. y ∉ dom first)
star(S, e, f)(x, y) = f(x, f(y)) (단. y ∈ dom first)
라 하면...

(뭐... 근데 튜플의 제귀적 정의에 따라, (x, v, ..., y) = (x, (v, ..., y))란 점을 알거라고 가정하고 말한거긴 한데... 잘 알아듣겠지)

star(S, e, f)를 통해서, 많은 모노이드의 계산을 설명 가능하다.

FuncPI ≜ star(fun(S), I, ◦)라 하면,

이 FuncPI라는 놈... 이놈으로 대부분의 반복연산이 서술된다. 하... ㅋㅋㅋ

<S, *>에서, FuncPI((* x))(e)식으로도 서술되고, 트릭 쓰면, 이것보다도 zfc의 기초에 가깝게 low level한 대수구조의 경우도 연속한 반복연산, 그게 표현 된단다 하... 이건 고2~고3 넘어갈때 쯤, star라는 체계를 만들었었다. 왜냐면, 자유모노이드랑, 문법 서술할때마다, 기초론적으로 엄밀하게 구성했었기에, 그게 귀찮아서 만들었었다.

fˢ⁽ⁿ⁾ = FuncPI(fⁿ, f) = Func(f, fⁿ)임이 당연하다.

왜냐?

ftup₀ = ε
ftupₖ = (f, ftupₖ)

인데,

FuncPI(ftupₖ) = fᵏ이기 때문이다.
FuncPI가 결합법칙도 성립하기에?

FuncPI(FuncPI(ftupₖ), tfup₁) = FuncPI(ftupₛ₍ₖ₎)인거다.

암튼 이런식으로 잘 성립하고, 

심지언, f⁻ⁿ = (f⁻¹)ⁿ이다.

왜냐? f⁻ⁿ ◦ fⁿ = I = fⁿ ◦ f⁻ⁿ임은, 에초에 f가 전단사면, 역함수와 정함수의 합성은 어느 순서든 항등함수니까, 저게 맞긴 함 일단. 근데 저걸 통해 다음을 보일수 있음.

f⁻ˢ⁽ⁿ⁾◦ f ◦fⁿ = I임.

즉, f⁻ˢ⁽ⁿ⁾ = fⁿ ◦ f⁻¹여야만 함.

아무튼, 보일거 다 보임 ㅋㅋ

### 제귀 함수, 제귀 함수를 가진 모델의 언어를 특히 튜링 언어적인 관점에서

...작성중...