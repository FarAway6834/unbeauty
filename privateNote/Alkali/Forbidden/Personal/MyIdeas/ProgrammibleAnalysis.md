# ProgrammibleAnalysis

1. 논의에 필요한 자료
2. 페아노 공리계부터 제귀 함수까지
3. 명제적 분포부터, 진리함수 산술까지

## 논의에 필요한 자료

1. Operodepredrofunctionalang
2. select
3. ProgrammibleAnalysis
4. About Language
5. tools

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

### About Language

1. Degamma Notation
2. Mad Grammer
3. Numberize System
4. Name-System

#### Degamma Notation

```markdown
# DigammaNotation 정의

ϝ를 구문론적으로 정의하는 노테이션이다.
보통을 L을 ZFC로 놓는다. 왜냐? 이건 함수를 표기하기 위한 용도이기에, 수학에서 많이 쓰일수밖에 없다. 수학을 L로 놓기 때문이다. 물론, 왜 하필 그 많은 공리계중 ZFC냐면, ZFC가 가장 많이 쓰이는 수학 공리계니까 그런거다.

## 서론

서술에 앞서 미리 요약하자면

dom (ϝx : X. y : Y) = X
codom (ϝx : X. y : Y) = Y
ran (ϝx : X. y : Y) = {y | x ∈ dom (ϝx : X. y : Y)}
graph (ϝx : X. y : Y) = {(x, y) | x ∈ dom (ϝx : X. y : Y)}
(ϝx : X. y : Y)(x) = y

인 기호 ϝ로 함수를 표기하는거다.

## 본론

TRS랑 자유 모노이드를 미리 정의한 후 DigammaNotation을 정의하겠다.

### 튜플 제귀 분할 모델 TRS(S)

들어가기 앞서, 
벡터에 대해서는 1도 생각 않고 기획했다는점을 기억하자, 벡터에 주어지는 dim은 결코 튜플의 길이가 될수 없다. 외냐면 모든 튜플은 최대길이가 L인 경우, 길이 1~L이나 L로 길이를 해석해도 무리가 없기 때문에, 하나로 정해졌다 하기 애매하다.

왜냐? 제귀적 정의에 따라서, n-tuple은 (n-1)-tuple의 일종이기 때문이다.

이제부턴 본론으로 들어간다.

TRS(S) ≜ <S*, ε, I, first, last, LengthEq>

I : S* ↦ S*
I(x) = x
first : S* ↦ S*
first|_{(S×S+)×(S×S+)}(x, y) = x
first|_{S¹}(x) = x
first|_{S⁰}() = ε
last : S* ↦ S*
last|_{(S×S+)×(S×S+)}(x, y) = y
last|_{S¹}(x) = ε
last|_{S⁰}() = ε

$LengthEqCore(p, f, x, y) : \begin{cases} f(x) = ε ↔ f(y) = ε, &(p), \ LengthEqCore(¬p, f, x, y) ∨ LengthEq(p, last◦f, x, y), &(¬p) \end{cases}$
LengthEq(x, y) : LengthEqCore(T, I, x, y)

LengthEq가 재대로 작동하는지는 근데 페아노 공리계에서 증명가능함.

에초에 LengthEq(x, y) ↔ ∃n ∈ ℕ₀, lastⁿ(x) = ε ↔ lastⁿ(y)임. ㅋㅋㅋ

### 자유모노이드 F(X)

F(X) ≜ <X*, ε, juxtaposition>

k는 튜플이 아닌 constant로, 아무거나 ㄱㄴ. k = {{∅}, {{∅}}}로 놓으면 이해하기 쉬워짐.

juxtaposition : X* × X* ↦ X*
$x juxtaposition y = \begin{cases} x, &(y = ε), \ y, &(x = ε), \ (x, y), &(LengthEq(x, last(k, k))), \ first(x) juxtaposition last(x) juxtaposition y, &(¬LengthEq(x, last(k, k))) \end{cases} $

### 디감마 표기법 DigammaNotation

parentheses ≜ {'(', ')', ','}

DigammaNotationStartSymbol ≜ 'ϝ'
DigammaNotationNonVarname ≜ parentheses ∪ DigammaNotationNonterminal
DigammaNotationNonterminal ≜ {'ϝ', ':', '.'}
DigammaNotationTerminal(L) ≜ L ∪ parentheses
CompileTargetOfDigammaNotationLang ≜ DigammaNotationTerminal
DigammaNotationLang(L) ≜ DigammaNotationTerminal(L) ∪ DigammaNotationNonterminal
DigammaNotationLformation(L) ≜ F(DigammaNotationLang(L))

아래 함수 DigammaNotationLFormat(L) / DigammaNotationRFormat(L)는 자유모노이드 DigammaNotationLformation(L)위에서 조합논리로써 조합된 함수다.
DigammaNotationLFormat(L) : (DigammaNotationLang(L)*)⁴↦DigammaNotationLang(L)*
DigammaNotationLFormat(L)(x, X, y, Y) ≜ "ϝ" juxtaposition x juxtaposition ":" juxtaposition X juxtaposition "." juxtaposition y juxtaposition ":" juxtaposition Y
DigammaNotationRFormat(L)(L) : (DigammaNotationLang(L)*)⁴↦DigammaNotationLang(L)*
DigammaNotationRFormat(L)(x, X, y, Y) ≜ "(" juxtaposition X juxtaposition "," juxtaposition Y juxtaposition "," juxtaposition "{(" juxtaposition x juxtaposition "," juxtaposition y juxtaposition ") | " juxtaposition x juxtaposition "∈" juxtaposition X juxtaposition "})"
모노이드 DigammaNotationLformation(L)에 대한건 여기까지다.

DigammaNotationFormationRule(L) ≜ {(DigammaNotationLFormat(L)(x, X, y, Y), DigammaNotationRFormat(L)(x, X, y, Y)) | X, x ∈ (DigammaNotationLang(L) ∖ DigammaNotationNonVarname)* ∧ Y, y ∈ DigammaNotationLang(L)*}
DigammaNotationFormalGrammer(L) ≜ (DigammaNotationNonterminal, DigammaNotationTerminal(L), DigammaNotationFormationRule(L), DigammaNotationStartSymbol)

이를통해 DigammaNotationFormalGrammer(L)가 변형행성문법임을 알수 있다.

Formation Rule이 사실상 PCRE(PCRE에 없는 문자집합 DigammaNotationLang(L), DigammaNotationNonVarname를 쓴건 양해해주길)코드 s/ϝ(?<x> [[DigammaNotationLang(L)]--[DigammaNotationNonVarname]]*?)[\s\t]*:[\s\t]*(?<X> [[DigammaNotationLang(L)]--[DigammaNotationNonVarname]]*?)[\s\t]*\.[\s\t]*(?<y>[DigammaNotationLang(L)]*?)[\s\t]*:[\s\t]*[[DigammaNotationLang(L)]--[DigammaNotationNonVarname]]*?/\($X, $Y, \{\($x, $y\) \| $x∈$X\}\)/나 다름없다. (이걸 python fstring같이 작성하자면, 변수(일수있는)기호(즉, (DigammaNotationLang(L) ∖ DigammaNotationNonVarname)*) X, x와 DigammaNotationLang(L)가 charset인 L-formula Y, y에 대하여, f"ϝ{x}:{X}.{y}:{Y}"가 감지되면 f"({X}, {Y}, {{({x}, {y}) | {x}∈{X}}})"로 치환하는거다.)

TMI : 촘스키 위계상 정규언어라고도 부른다.

변형생성문법이론에서 Lang이란 charset이다. DigammaNotation의 Lang는 DigammaNotationLang(L)이고, 그 Lang는 컴파일 타깃인 CompileTargetOfDigammaNotationLang(L)로 컴파일된다.

즉, DigammaNotation는 사실상의 메크로, 그러니까 표기법(Notation)이다. 구문론적으로 ϝ를 정의한것이다.

사실... 구문론적 등호를 =ₛ라 하면, 

임의의 모델론적언어 L에 대한 L-formula x, X, y, Y에 대하여,

ϝx : X. y : Y =ₛ (X, Y, {(x, y) | x∈X)})

라고 한줄요약 가능하다.

ㅅㅂ...

또한, f = (X, Y, {(x, y) | x∈X)})라 하면, {(x, y) | x∈X)} ⊆ X × ran f를 만족하므로,

다음 두 조건
1. ran f ⊆ Y를 만족할것.
2. {(x, y) | x∈X)}가 오른쪽 유일인 관계일것

을 만족하는 튜플 (X, Y, {(x, y) | x∈X)})은 ZFC에서 함수를 정의하는 표준 모델상 함수일 공리를 만족시킨다.

그렇다. 함수 간단하게 적겠답시고 이 ㅈㄹ 한거다.
```

#### Mad Grammer

````markdown
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
 ````

#### Numberize System

````markdown
# Numberize System

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

```
seq`•` 연산의 정의)
1. seq`f`ₙ ≜ f(n)
2. seq`f`ₙ = (dom f, codom f, graph f)
3. seq`seq`f``(x) = f(x) (즉, 수열을 원래대로 돌리는 역할도 함 )
```

Surj x : X. y ≜ ϝ x : X. y : {y | x ∈ X}
{aₙ : Y}ₓ₍ₙ₎ ≜ seq`ϝn : x. aₙ : Y`
{aₙ}ₓ₍ₙ₎ ≜ seq`Surj n : x. aₙ`

NSDecoderTableize의 정의)
NSDecoderTableize(L, x) ≜ {NSDecoderTableize(L, x)}ₜ₍ₙ₎ (단. t = [0 ⤳ L))
NSDecoderTableize(1, x) ≜ {x}ₜ₍ₙ₎ (단. t = [0 ⤳ 1))
NSDecoderTableize(L, x)₀ ≜ first(x)
NSDecoderTableize(L, x)ₙ ≜ NSDecoderTableize(L - 1, last(x))₍ₙ₋₁₎

restrictedArr ≜ {a | dom a = [1 ⤳ card a]}
ArrLastMask ≜ {{n + 1}ₜ₍ₙ₎ (단. t = [1 ⤳ k)) : restrictedArr}ₜ₍ₙ₎ (단. t ≜ [2 ⤳ ∞))

tuplize ≜  Surj a : tuplize(a)
tuplize|ₓ ≜ (ϝ a : ε : codom tuplize (단. x = {a | dom a = (0 ⤳ 0))) (tip : (0 ⤳ 0) = [1 ⤳ 0) = ∅)
tuplize|ₓ ≜ (ϝ a : restrictedArr. (a₁, tuplize(a ◦ (ArrLastMaskₖ))) (단. k = card a) : codom tuplize) (단. x = restrictedArr)
duptup(L, x) ≜ tuplize({x}ₜ₍ₙ₎) (단. t = [1 ⤳ L])
mask(L, f) ≜ ϝx : dom mask(L, f). mask(L, f) : codom mask(L, f)
mask(0, ε) ≜ Surj x : {ε}
mask(1, f) ≜ f
mask(n, f) ≜ Surj x : (dom first(f) × dom mask(n - 1, last(f))). (first(f)(first(x)), mask(n - 1, last(f))(last(x)))

abs(x) = |x|

n.b. 아래 m D = {m × d | d ∈ D}는 대수학의 그 ㅈㄹ났던 표기법이다. 뭐... 근데 아까 보여준 정의만 알면 장땡.
NSmod<D, L, I> ≜ ϝt : D². first(t) + last(t)D : {k ∈ D/last(t)D | t ∈ D²}
NSmodr<D, L, I> ≜ Surj m : D. (ϝ x : D. NSmod<D, L, I>(x, m) : D/mD)
Mod(NSmodr<D, L, I>(m)) = <codom NSmodr<D, L, I>(m), tuplize({NSmodr<D, L, I>(m) ◦ NSDecoderTableize(L, I)ₖ ◦ mask(arity(NSDecoderTableize(L, I)ₖ), duptup(arity(NSDecoderTableize(L, I)ₖ), (Surj x : codom NSmodr<D, L, I>(m). min(abs[x]))))}ₜ₍ₖ₎) (단. t = [1 ⤳ L))>
Tip : 그냥 I가 배정으로, 저기에 들어가는 D에서의 연산자들이, D/mD로 동형사상을 통해서 포팅되는거다.
NSEncoderTablize(L, x) ≜ NSEncoderTablize<ℤ>(L, x)
NSEncoderTablize<D>(L, x) ≜ NSmodr<D, K, I>(L) ◦ (NSDecoderizeTablize(L, x)⁻¹)
Decoderize(L, x) ≜ ϝ v : (codom NSEncoderTablize)* . Φ?ε:(Ψ?NSEncoderTablize(L, x)⁻¹(v):(Decoderize(L, x)(first(v)), Decoderize(L, x)(last(v)))) (단. Φ ↔ (v = ε), Ψ ↔ (v ∈ codom EncoderTablize)) : (com EncoderTablize)*
삼항연산자의 정의는, ProgrammibleAnalysis초기 설명에서 이미 정의한적 있음

Numberize(T) ≜ iₜ [t := T]
Numberize(T, G) ≜ ϝ x : T × dom Numberize(G). Numberize(G)(last(x)) × (card T) + first(X) : ℕ₀

FullyNumberize(T, G) ≜ Numberize(T, G) ◦ (Decoderize⁻¹)

FullyNumberize는 문자열을 숫자로 바꿔준다.

## Applicative Example

이건, 다음 편에 만들겠다.

ASCII가 구현되니까, 다음 글인 NameSystem에서 구현한다.
````

#### NameSystem

```markdown
# NameSystem

isNameFunc(name) : 
1. ∀a ∈ dom name, codom name(a) ∩ dom first = ∅ (튜플만 아니면 이름용 문자열론 다 된다.)
2. name(a) : dom a ↦ lang a
3. lang은... 젠장 걍, codom name(a)다.
4. 이건 사실 잘 형식화되지 않은 정의라, 가까운 시일 내에, name의 정의는 형식화된 정리된 형태로 바뀔거다.
5. 이 조항들 수정해야 함 ㅇㅇ.

{Σ name}_{k ∈ dom a} aₖ ≜ Σ_{k ∈ dom a} ||aₖ|| ObSys(codom name(a))(tuplize(name(a)), name(a))
이름을 가지고, 일급객체열 a를, 이름을 기저로 만든 벡터로 바꿔주는 그러한 함수다. (사실상 일급객체열을 벡터로 바꿔주는 일대일대응이나 다름없지만)

terminative x ≜ ('\0', x)
널 문자 (termination 문자)를, 인코드상 코드 0에 넣어놓는거다 ㅋㅋㅋ

shash(str-hash)er 정의)
shasher(L, x) ≜ Surj v : dom EncodingTablize(L, Terminative x)).  FullyNumberize(duptup(L, ℤ/Lℤ), encoderize(EncodingTablize(L, Terminative x))(v))
그냥, 터미널이 있큰 문자셋 Terminative x에 대해, 그걸 Numberize해서, 바이트열을, 자릿수순으로 나열해서, 숫자로 만든거임.

tokenL(L, X)ₙ(y) ≜ (n = 0)?ε:((n = 1)?(shasher(L, X)(y)):(shasher(L, X)(first(y)), tokenL(L, X)₍ₙ₋₁₎(last(y))))
문자셋 (L, X)의 언어로 된 문자열 튜플 y에 해당하는 놈들을 토큰으로 간주하는 언어. 토큰값을 shasher하여, 렉싱 결과에, 렉싱 이전 값을 볼수 있음. 렉싱이라는 묶기 과정이, shasher된 문자로 치환하는 두 자료구조를 변환하는 동형사상 역할의 알고리즘임을 시사함.

V((L, S), ρ)(x) ≜ ρ_{shasher(L, S)(x)}
배정 ρ의 shasher(L, S)(x)번째 인덱스에 해당하는 변항을 슬라이싱하는 Expression (Expression이 아닌데 용어가 생각이 안난다. 집중력이 갑자기 떨어지고, 몽롱하다.)

ObSys(L, S)ₙ(ρ, (N, t)) ≜ V((N, tokenL(L, S)ₙ(t)), ρ)
ObSys는, V를 tokenL화 시켜서, 사용되지 않은 인덱스를 줄일수있다!

(Spanᵤ)(B) ≜ {Σᵥ aₓx | a : B ↦ 𝔽} [u := 𝔽][v := (x ∈ B)]
와 생성 ㅋㅋㅋ

globals ≜ (Σ name)⁻¹
일급객체를 내이밍하는거의 역함수니, 네임의 값을 구하는거다.
Quntom(f) ≜ Surj (A, B) : dom f. Span(globals⁻¹[f(globals[Span⁻¹(A)], globals[Span⁻¹(B)])])
이게 왜 잘 작동하는지 설명 안하면 비형식적이라 욕먹을텐데, 이거 알고보면 ㅈㄴ 형식적임. 물론 증명과, 어떤 기호를 생략했는지 말 안 현제시점은 비형식적. 그러나, 뇌가 탄것같으니, 나중에 설명함 (에초에 걍 보기만 해도, 해당 공간의 정규직교기저를 대충 뽑는 놈을 의도함이 보일텐데, 아 그러고보니 저거 수정해야한다. Span⁻¹가 아니라 해당 공간의 정규직교기저인지라... 그리고, 관계연산에 대해서도 명시해야하는게 있다.)

QuntomNon_H Φ ≜ ∪ₜ ker <x| [t:=(x ∈ Φ)] ≜ Span(globals[globals⁻¹(Span⁻¹(H)) ∖ globals⁻¹[Span⁻¹(X)]])

엄... 헤헤.... 그..

뭐랄까, 상태공간의 각 물리량은, 물리량들이 가지고 있는 음함수적 성질을 만족시키는, 음함수 궤적이라는 배정의 벡터화 모델에 있는 기저고, 그 기저들은, 각각 일급객체로써, 변수 이름으로써의 속성을 지닌다는걸 발견해서 만든거라... 하하...

이건 젯타이니 형식화하야겠다. 나중에 다듬어야한다. 코어 아이디어라
```

### tool

서술용 툴 몇개다.

1. ClsrAndClsr-PromiseSystem-byRestrictSystem

#### ClsrAndClsr-PromiseSystem-byRestrictSystem

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

이 글도 젯타이니 다듬어야함.
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

...작성중... (이 문서는 아직 완성되지 않았도, 종이의 내용을 옮겨적는 중)

## 명제적 분포부터, 진리함수 산술까지

1. Propositional Distribution (명제적 분포)
2. Explict Named Connective (명시적 네이밍 결합자)

...작성중... (이 문서는 아직 완성되지 않았도, 종이의 내용을 옮겨적는 중)

### Propositional Distribution (명제적 분포)

Tips)
1. pmf : probability math function
2. P : probability measure

Definition)

X ~ Φ(A) : ∀v, P(X = v) + pmf(1 - v) = pmf(v) + pmf(1 - v) = pmf²(1) = pmf(P(A)) = 1

이때, Φ(A)를 A에 대한 Propositional Distribution이라 히고, X ~ Φ(X) (확률변수 X가 분포 Φ(A)를 따른다) 라는것은, 위 공식을 만족함을 의미한다.

Φₐ(A) : ∃X, X ~ Φ(A)

이때, Φₐ(A)인 A를 Propositional Event라 한다. 이게 어떤 제약사항이 있는지는 하단 참고.

Theorems)

th. P(X = v) = pmf(v)

pf. DICO QUOD ERAT ; 
1. i) P(X = v) ≠ pmf(v)
2. ⊭ P(X = v) + pmf(1 - v) = pmf(v) + pmf(1 - v)
∴ P(X = v) = pmf(v)

QUOD ERAT DEMONSTRADUM

의의 on 확률론적 POV : pmf가 X의 확률질량함수임을 의미한다.

lemma. P(X ≠ v) = pmf(1 - v)

pf. DICO QUOD ERAT ; 
1. P(X = v) + pmf(1 - v) = 1
2. pmf(1 - v) = 1 - P(X = v) = P(X ≠ v)

QUOD ERAT DEMONSTRADUM

th. k ∈ codom X → codom X = {k, 1 - k}

pf. X ≠ k HOC EST X = 1 - k ∵ P(X ≠ v) = pmf(1 - v)
∴ k ∈ codom X → codom X = {k, 1 - k}

QUOD ERAT DEMONSTRADUM

col. Φ(A)는 베르누이 분포 (이산확률변수를 확률변수로 가지는 분포) 의 일종이다. (i.e. X는 이산확률변수)

의의 on 분포 POV : Φ(A)가 오직 양자택일의 값인 분포라는 겁나 중요한 의의를 가진다.

lemma. pmf²(0) = 0

pf. DICO QUOD ERAT
1. pmf²(1) = P(X = P(X = 1)) = 1
2. P(X = P(X = 1)) = P(X = P(X = 1 - 0)) = P(X = P(X ≠ 0)) = P(X = 1 - P(X = 0)) = P(X ≠ P(X = 0)) = 1 - P(X = P(X = 0)) = 1 ∵ P(X ≠ v) = pmf(1 - v)
3. 1 - (1 - P(X = P(X = 0))) = 1 - (1) = P(X = P(X = 0)) = 0 ∵ 1 = 1, x = y ⊨ 1 - x = 1 - y
∴ pmf²(0) = 0

QUOD ERAT DEMONSTRADUM

th. s = {0, 1}, (pmf|ₛ)²(v) = v

pf. FACT) pmf²(0) = 0, pmf²(1) = 1

QUOD ERAT DEMONSTRADUM

col. pmf(pmf(x)) = x ⊢ pmf⁻¹ = pmf

의의 on 추상대수 POV : pmf가 정의역 s로 restrict될시, 대합사상이라는 중요한 함의를 말한다.
n.b. 사실 근데, 대합이라는 점은 별로 중요하지 않다. ∃pmf⁻¹라는것만 중요하다. 그 이외의 정보는 증명에 안쓰이니까.

th. codom X = {0, 1}

pf. FACT) 1 ∈ codom X ∵ pmf²(1) = 1

th. pmf⁻¹(pmf²(1)) = pmf⁻¹(pmf(P(A)) = pmf(1) = P(A) ∵ ∃pmf⁻¹

요약 : 
1. X ~ Φ(A)면, A를 Propositional Event라 하며, X는 0 또는 1인 이상확률변수임.
2. pmf(1) = P(A), 1 - pmf(0) = pmf(1)
3. 위 요약 내용을 통해 알수 있는 사실은, Propositional Event는 100%일어(0%안일어)나거나, 0%로 일어(100%로 안일어)나거나, 한다는거다.

### Explict Named Connective (명시적 네이밍 결합자)

n.b. 비트겐슈타인에 대해서는 2019 고 1 11모 25~29번 지문으로 접했음을 명시하겠음.

이 문단에선 비트겐슈타인이 명제와 사실의 관계를 분명히 밝히기 위해 만든 진리표와 진리함수이론을 통하여, 명시적 네이밍과, 그 성질을 서술하겠다.

#### 명시적 네이밍

결합자 p가, x, y, z ∈ {T, F}인 유일한 z와 유일한 x, y에서만 x p y ↔ z이고, 나머지 경우에 a, b ∈ {T, F}b, (a, b) ≠ (x, y)에서, a p b ↔ ¬z라면, x인 left와 y인 right에서만 z가 되는 결합자라 하여 다음과 같이 명명 규칙으로 나타낸다.

FullPrefixName ≜ ϝ v : {"T", "F"}. (v = "T")?"True":"False" : {"True", "False"}
PrefixInitial ≜ ϝ v : {"T", "F"}. (v = "T")?"True":"False" : {"t", "f"}

FullName(Left, Right, Value) ≜ optformat({"True", "False"}, {"True", "False"}, {"True", "False"}, "{2}In{0}Left{1}Right", FullPrefixName(Left), FullPrefixName(Right), FullPrefixName(Value))
Initial(L, R, V) ≜ optformat({"t", "f"}, {"t", "f"}, {"t", "f"}, "{2}i{0}l{1}r", PrefixInitial(L), PrefixInitial(R), PrefixInitial(V))

또한, 결합자 p가 여러개의 좌인자•우인자에서 z면, 이건 이것대로 특이한 표기법으로 적는다.

FNV2C ≜ Surj x : {x ∈ ({"T", "F"}²)ⁿ | n ∈ [1 ⤳ 4]}. (x ∈ {"T", "F"}²)?optformat({"True", "False"}, {"True", "False"}, "{0}Left{1}Right", FullPrefixName(first(x)), FullPrefixName(last(y))):optformat({"True", "False"}, {"True", "False"}, codom FNV2C, "{0}Left{1}RightEt{2}", FullPrefixName(first(first(x))), FullPrefixName(last(first(y))), FNV2C(last(x)))
FullNameV2 ≜ Surj x : {x ∈ {"T", "F"} × ({"T", "F"}²)ⁿ | n ∈ [1 ⤳ 4]}. optformat({"True", "False"}, codom FNV2C, "{0}In{1}", FullPrefixName(first(x)), FNV2C(last(x)))

IV2C ≜ Surj x : {x ∈ ({"T", "F"}²)ⁿ | n ∈ [1 ⤳ 4]}. (x ∈ {"T", "F"}²)?optformat({"t", "f"}, {"t", "f"}, "{0}l{1}r", PrefixInitial(first(x)), PrefixInitial(last(y))):optformat({"t", "f"}, {"t", "f"}, codom IV2C, "{0}l{1}re{2}", PrefixInitial(first(first(x))), PrefixInitial(last(first(y))), IV2C(last(x)))
InitialV2 ≜ Surj x : {x ∈ {"T", "F"} × ({"T", "F"}²)ⁿ | n ∈ [1 ⤳ 4]}. optformat({"t", "f"}, codom IV2C, "{0}i{1}", PrefixInitial(first(x)), IV2C(last(x)))

물론, f ∈ {InitialV2, FullNameV2}에서 f(V, (L1, R2), (L2, R2), ...)인 경우만.

결론적으로, (f, g) ∈ {(Initial, InitialV2), (FullName, FullNameV2)}에서, g(V, L, R) = f(L, R, V)이고, 그 외에, 여러개의 좌인자 • 우인자인 경우를 다룬다.

#### 명시적 네이밍 결합자

먼저, Initial을 구문론적으로 정의해주는 Notation은 다음과 같은 문법규칙을 가진다.

InitialNotation = {(x, y) | {x, y} = {a, b} ∧ a = FullNameV2(arg) ∧ b = InitialV2(arg) ∧ arg ∈ dom InitialV2}

이제, 각 결합자의 정의를 보자.

먼저, 논리식으로는 다음과 같이 쓰여진다.

DOCC ≜ Surj x : dom FNV2C. (x ∈ {"T", "F"}²)?optformat({"T", "F"}, {"T", "F"}, "((L ↔ {0}) ∧ (R ↔ {1}))", first(x), last(x)):optformat({"T", "F"}, {"T", "F"}, codom DOCC, "((L ↔ {0}) ∧ (R ↔ {1})) ∨ {2}", first(first(x)), last(first(x)), DOCC(last(x)))
DefineOfConnectives ≜ Surj x : dom FullNameV2. optformat({"T", "F"}, codom DOCC, "({1}) ↔ {0}", first(x), DOCC(last(x)))

그리고, 이는 정의문을 만들때 다음과 같이 쓰인다.

AxiomOfNotation ≜ Surj x : dom FullNameV2. optformat(codom FullNameV2, codom DefineOfConnectives, "(L {0} R) ↔ ({1})", FullNameV2(x), DefineOfConnectives(x))

ExplictNamedConnectiveNotation ≜ {(y, "T") | y = AxiomOfNotation(x) ∧ x ∈ dom AxiomOfNotation}

이를 통하여, 명시적 네이밍 결합자 표기법의 문법규칙을 통해, 각 결합자의 의미를 규정하는 구문을 참으로 평가한다.

#### ExplictNamedConnectiveNotation의 모델과 InitialNotation의 모델

각 언어의 모델은 "값-배정(assignemnt)"의 형태로 나타낼수 있다.

그러나, 내가 미쳤다고 일일이 타이핑하고싶지 않다.

```python
# ㅅㅂ 솔찍히 사람이 어떻게 일일이 True/False를 타이핑하겠는가, 이거 실행해올테니 잠시만 wait.

core = lambda s, p, q : (lambda k = [["True", "False"], "tf"][s] : f"{k[p]}{['Left', 'l'][s]}{k[q]}{['Right', 'r'][s]}")()
conn = lambda s, v, *arg : f"{[['True', 'False'], 'tf'][s][v]}{['In', 'i'][s]}{['Et', 'e'][s].join((core(v, *k)) for k in arg)}"

# n.b. ['True', 'False']의 순서는 상관 없다. 둘이 베타적으로 0, 1로 대응만 된다면, 이름이 True이든 False이든 상관없다. 그리고 어짜피 모두 프린트할 목적임.
# n.b. 이 코드에서, 순서가 나빠서 코드가 나쁘다고 느낀다면 당장 이 긁을 읽지 마라. 나랑 상성이 안맞는 부류다. 나는 형식주의자고, 코드의 네이밍을 보고 타당성을 따지는 자연어적 직관을 강요하는 사람을 배제하고 글을 썼다.

value_core = lambda p, q : f"((L ↔ {['T', 'F'][p]}) ∧ (R ↔ {['T', 'F'][q]}))"
defvalue = lambda v, *arg : f"({' ∨ '.join((value_core(*x) for x in arg))}) ↔ {['T', 'F'][v]}"

defs = lambda v, *arg : f"{conn(v, 0, *arg)} = * s.t. L * R = ({defvalue(v, *arg)})"

assignments = lambda v, *arg : f"{conn(v, 1, *arg)} = {conn(v, 0, *arg)}"
OutputFormat = lambda iter, f = assignments : f"({','.join((f(v, *arg) for v, arg in iter))})"
ArgGenerCore = lambda arr : [tuple(([(0, 0), (0, 1), (1, 0), (1, 1)][k] for k in x)) for x in arr]

coreworkc = lambda f : [f(x) for x in [0, 1, 2, 3]]
flat = lambda iter : iter[0] if len(iter) == 1 else iter[0] + flat(iter[1:])
corework = lambda f : flat(coreworkc(f))

ArgGener = ArgGenerCore(coreworkc(lambda x : [x])) + ArgGenerCore(corework(lambda a : coreworkc(lambda b : [a, b]))) + ArgGenerCore(corework(lambda a : corework(lambda b : coreworkc(lambda c : [a, b, c])))) + ArgGenerCore(corework(lambda a : corework(lambda b : corework(lambda c : coreworkc(lambda d : [a, b, c, d])))))
argslst = list(zip([0] * len(ArgGener), ArgGener)) + list(zip([1] * len(ArgGener), ArgGener))

print(OutputFormat(argslst))

print()

print("---")

# 그 다음 포멧도

print()

print(OutputFormat(argslst, f = defs))
```

기계한테 시켜야징

자, 실행해왔다. 이야기를 마저 하겠다.

InitialNotation의 경우,

`ρ = (FalseIntltr = TrueInTrueLeftTrueRight,FalseIntlfr = TrueInTrueLeftFalseRight,FalseInfltr = TrueInFalseLeftTrueRight,FalseInflfr = TrueInFalseLeftFalseRight,FalseIntltrEttltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEttltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEttltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEttltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEttltrEttltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEttltrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEttltrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEttltrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEttlfrEttltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEttlfrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEttlfrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEttlfrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEtfltrEttltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEtfltrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEtfltrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEtfltrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEtflfrEttltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEtflfrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEtflfrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEtflfrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEttltrEttltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEttltrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEttltrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEttltrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEttlfrEttltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEttlfrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEttlfrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEttlfrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEtfltrEttltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEtfltrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEtfltrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEtfltrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEtflfrEttltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEtflfrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEtflfrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEtflfrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEttltrEttltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEttltrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEttltrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEttltrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEttlfrEttltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEttlfrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEttlfrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEttlfrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEtfltrEttltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEtfltrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEtfltrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEtfltrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEtflfrEttltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEtflfrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEtflfrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEtflfrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEttltrEttltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEttltrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEttltrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEttltrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEttlfrEttltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEttlfrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEttlfrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEttlfrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEtfltrEttltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEtfltrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEtfltrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEtfltrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEtflfrEttltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEtflfrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEtflfrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEtflfrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEttltrEttltrEttltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEttltrEttltrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEttltrEttltrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEttltrEttltrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEttltrEttlfrEttltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEttltrEttlfrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEttltrEttlfrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEttltrEttlfrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEttltrEtfltrEttltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEttltrEtfltrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEttltrEtfltrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEttltrEtfltrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEttltrEtflfrEttltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEttltrEtflfrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEttltrEtflfrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEttltrEtflfrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEttlfrEttltrEttltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEttlfrEttltrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEttlfrEttltrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEttlfrEttltrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEttlfrEttlfrEttltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEttlfrEttlfrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEttlfrEttlfrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEttlfrEttlfrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEttlfrEtfltrEttltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEttlfrEtfltrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEttlfrEtfltrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEttlfrEtfltrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEttlfrEtflfrEttltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEttlfrEtflfrEttlfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEttlfrEtflfrEtfltr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEttlfrEtflfrEtflfr = TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEtfltrEttltrEttltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEtfltrEttltrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEtfltrEttltrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEtfltrEttltrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEtfltrEttlfrEttltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEtfltrEttlfrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEtfltrEttlfrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEtfltrEttlfrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEtfltrEtfltrEttltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEtfltrEtfltrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEtfltrEtfltrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEtfltrEtfltrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEtfltrEtflfrEttltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEtfltrEtflfrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEtfltrEtflfrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEtfltrEtflfrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEtflfrEttltrEttltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEtflfrEttltrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEtflfrEttltrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEtflfrEttltrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEtflfrEttlfrEttltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEtflfrEttlfrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEtflfrEttlfrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEtflfrEttlfrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntltrEtflfrEtfltrEttltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntltrEtflfrEtfltrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntltrEtflfrEtfltrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntltrEtflfrEtfltrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntltrEtflfrEtflfrEttltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntltrEtflfrEtflfrEttlfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntltrEtflfrEtflfrEtfltr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntltrEtflfrEtflfrEtflfr = TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEttltrEttltrEttltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEttltrEttltrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEttltrEttltrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEttltrEttltrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEttltrEttlfrEttltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEttltrEttlfrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEttltrEttlfrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEttltrEttlfrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEttltrEtfltrEttltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEttltrEtfltrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEttltrEtfltrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEttltrEtfltrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEttltrEtflfrEttltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEttltrEtflfrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEttltrEtflfrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEttltrEtflfrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEttlfrEttltrEttltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEttlfrEttltrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEttlfrEttltrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEttlfrEttltrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEttlfrEttlfrEttltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEttlfrEttlfrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEttlfrEttlfrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEttlfrEttlfrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEttlfrEtfltrEttltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEttlfrEtfltrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEttlfrEtfltrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEttlfrEtfltrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEttlfrEtflfrEttltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEttlfrEtflfrEttlfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEttlfrEtflfrEtfltr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEttlfrEtflfrEtflfr = TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEtfltrEttltrEttltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEtfltrEttltrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEtfltrEttltrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEtfltrEttltrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEtfltrEttlfrEttltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEtfltrEttlfrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEtfltrEttlfrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEtfltrEttlfrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEtfltrEtfltrEttltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEtfltrEtfltrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEtfltrEtfltrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEtfltrEtfltrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEtfltrEtflfrEttltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEtfltrEtflfrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEtfltrEtflfrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEtfltrEtflfrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEtflfrEttltrEttltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEtflfrEttltrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEtflfrEttltrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEtflfrEttltrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEtflfrEttlfrEttltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEtflfrEttlfrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEtflfrEttlfrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEtflfrEttlfrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseIntlfrEtflfrEtfltrEttltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseIntlfrEtflfrEtfltrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseIntlfrEtflfrEtfltrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseIntlfrEtflfrEtfltrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseIntlfrEtflfrEtflfrEttltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseIntlfrEtflfrEtflfrEttlfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseIntlfrEtflfrEtflfrEtfltr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseIntlfrEtflfrEtflfrEtflfr = TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEttltrEttltrEttltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEttltrEttltrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEttltrEttltrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEttltrEttltrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEttltrEttlfrEttltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEttltrEttlfrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEttltrEttlfrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEttltrEttlfrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEttltrEtfltrEttltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEttltrEtfltrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEttltrEtfltrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEttltrEtfltrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEttltrEtflfrEttltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEttltrEtflfrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEttltrEtflfrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEttltrEtflfrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEttlfrEttltrEttltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEttlfrEttltrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEttlfrEttltrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEttlfrEttltrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEttlfrEttlfrEttltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEttlfrEttlfrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEttlfrEttlfrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEttlfrEttlfrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEttlfrEtfltrEttltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEttlfrEtfltrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEttlfrEtfltrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEttlfrEtfltrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEttlfrEtflfrEttltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEttlfrEtflfrEttlfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEttlfrEtflfrEtfltr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEttlfrEtflfrEtflfr = TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEtfltrEttltrEttltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEtfltrEttltrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEtfltrEttltrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEtfltrEttltrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEtfltrEttlfrEttltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEtfltrEttlfrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEtfltrEttlfrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEtfltrEttlfrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEtfltrEtfltrEttltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEtfltrEtfltrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEtfltrEtfltrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEtfltrEtfltrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEtfltrEtflfrEttltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEtfltrEtflfrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEtfltrEtflfrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEtfltrEtflfrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEtflfrEttltrEttltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEtflfrEttltrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEtflfrEttltrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEtflfrEttltrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEtflfrEttlfrEttltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEtflfrEttlfrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEtflfrEttlfrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEtflfrEttlfrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInfltrEtflfrEtfltrEttltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInfltrEtflfrEtfltrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInfltrEtflfrEtfltrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInfltrEtflfrEtfltrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInfltrEtflfrEtflfrEttltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInfltrEtflfrEtflfrEttlfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInfltrEtflfrEtflfrEtfltr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInfltrEtflfrEtflfrEtflfr = TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEttltrEttltrEttltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEttltrEttltrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEttltrEttltrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEttltrEttltrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEttltrEttlfrEttltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEttltrEttlfrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEttltrEttlfrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEttltrEttlfrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEttltrEtfltrEttltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEttltrEtfltrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEttltrEtfltrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEttltrEtfltrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEttltrEtflfrEttltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEttltrEtflfrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEttltrEtflfrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEttltrEtflfrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEttlfrEttltrEttltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEttlfrEttltrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEttlfrEttltrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEttlfrEttltrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEttlfrEttlfrEttltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEttlfrEttlfrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEttlfrEttlfrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEttlfrEttlfrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEttlfrEtfltrEttltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEttlfrEtfltrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEttlfrEtfltrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEttlfrEtfltrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEttlfrEtflfrEttltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEttlfrEtflfrEttlfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEttlfrEtflfrEtfltr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEttlfrEtflfrEtflfr = TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEtfltrEttltrEttltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEtfltrEttltrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEtfltrEttltrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEtfltrEttltrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEtfltrEttlfrEttltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEtfltrEttlfrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEtfltrEttlfrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEtfltrEttlfrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEtfltrEtfltrEttltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEtfltrEtfltrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEtfltrEtfltrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEtfltrEtfltrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEtfltrEtflfrEttltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEtfltrEtflfrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEtfltrEtflfrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEtfltrEtflfrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEtflfrEttltrEttltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEtflfrEttltrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEtflfrEttltrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEtflfrEttltrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEtflfrEttlfrEttltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEtflfrEttlfrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEtflfrEttlfrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEtflfrEttlfrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight,FalseInflfrEtflfrEtfltrEttltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight,FalseInflfrEtflfrEtfltrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight,FalseInflfrEtflfrEtfltrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight,FalseInflfrEtflfrEtfltrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight,FalseInflfrEtflfrEtflfrEttltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight,FalseInflfrEtflfrEtflfrEttlfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight,FalseInflfrEtflfrEtflfrEtfltr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight,FalseInflfrEtflfrEtflfrEtflfr = TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight,fitltr = tiTrueLeftTrueRight,fitlfr = tiTrueLeftFalseRight,fifltr = tiFalseLeftTrueRight,fiflfr = tiFalseLeftFalseRight,fitltretltr = tiTrueLeftTrueRighteTrueLeftTrueRight,fitltretlfr = tiTrueLeftTrueRighteTrueLeftFalseRight,fitltrefltr = tiTrueLeftTrueRighteFalseLeftTrueRight,fitltreflfr = tiTrueLeftTrueRighteFalseLeftFalseRight,fitlfretltr = tiTrueLeftFalseRighteTrueLeftTrueRight,fitlfretlfr = tiTrueLeftFalseRighteTrueLeftFalseRight,fitlfrefltr = tiTrueLeftFalseRighteFalseLeftTrueRight,fitlfreflfr = tiTrueLeftFalseRighteFalseLeftFalseRight,fifltretltr = tiFalseLeftTrueRighteTrueLeftTrueRight,fifltretlfr = tiFalseLeftTrueRighteTrueLeftFalseRight,fifltrefltr = tiFalseLeftTrueRighteFalseLeftTrueRight,fifltreflfr = tiFalseLeftTrueRighteFalseLeftFalseRight,fiflfretltr = tiFalseLeftFalseRighteTrueLeftTrueRight,fiflfretlfr = tiFalseLeftFalseRighteTrueLeftFalseRight,fiflfrefltr = tiFalseLeftFalseRighteFalseLeftTrueRight,fiflfreflfr = tiFalseLeftFalseRighteFalseLeftFalseRight,fitltretltretltr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fitltretltretlfr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fitltretltrefltr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fitltretltreflfr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fitltretlfretltr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fitltretlfretlfr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fitltretlfrefltr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fitltretlfreflfr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fitltrefltretltr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fitltrefltretlfr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fitltrefltrefltr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fitltrefltreflfr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fitltreflfretltr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fitltreflfretlfr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fitltreflfrefltr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fitltreflfreflfr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fitlfretltretltr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fitlfretltretlfr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fitlfretltrefltr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fitlfretltreflfr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fitlfretlfretltr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fitlfretlfretlfr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fitlfretlfrefltr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fitlfretlfreflfr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fitlfrefltretltr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fitlfrefltretlfr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fitlfrefltrefltr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fitlfrefltreflfr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fitlfreflfretltr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fitlfreflfretlfr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fitlfreflfrefltr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fitlfreflfreflfr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fifltretltretltr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fifltretltretlfr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fifltretltrefltr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fifltretltreflfr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fifltretlfretltr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fifltretlfretlfr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fifltretlfrefltr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fifltretlfreflfr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fifltrefltretltr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fifltrefltretlfr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fifltrefltrefltr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fifltrefltreflfr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fifltreflfretltr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fifltreflfretlfr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fifltreflfrefltr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fifltreflfreflfr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fiflfretltretltr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fiflfretltretlfr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fiflfretltrefltr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fiflfretltreflfr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fiflfretlfretltr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fiflfretlfretlfr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fiflfretlfrefltr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fiflfretlfreflfr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fiflfrefltretltr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fiflfrefltretlfr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fiflfrefltrefltr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fiflfrefltreflfr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fiflfreflfretltr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fiflfreflfretlfr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fiflfreflfrefltr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fiflfreflfreflfr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fitltretltretltretltr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fitltretltretltretlfr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fitltretltretltrefltr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fitltretltretltreflfr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fitltretltretlfretltr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fitltretltretlfretlfr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fitltretltretlfrefltr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fitltretltretlfreflfr = tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fitltretltrefltretltr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fitltretltrefltretlfr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fitltretltrefltrefltr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fitltretltrefltreflfr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fitltretltreflfretltr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fitltretltreflfretlfr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fitltretltreflfrefltr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fitltretltreflfreflfr = tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fitltretlfretltretltr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fitltretlfretltretlfr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fitltretlfretltrefltr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fitltretlfretltreflfr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fitltretlfretlfretltr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fitltretlfretlfretlfr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fitltretlfretlfrefltr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fitltretlfretlfreflfr = tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fitltretlfrefltretltr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fitltretlfrefltretlfr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fitltretlfrefltrefltr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fitltretlfrefltreflfr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fitltretlfreflfretltr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fitltretlfreflfretlfr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fitltretlfreflfrefltr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fitltretlfreflfreflfr = tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fitltrefltretltretltr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fitltrefltretltretlfr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fitltrefltretltrefltr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fitltrefltretltreflfr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fitltrefltretlfretltr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fitltrefltretlfretlfr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fitltrefltretlfrefltr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fitltrefltretlfreflfr = tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fitltrefltrefltretltr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fitltrefltrefltretlfr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fitltrefltrefltrefltr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fitltrefltrefltreflfr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fitltrefltreflfretltr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fitltrefltreflfretlfr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fitltrefltreflfrefltr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fitltrefltreflfreflfr = tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fitltreflfretltretltr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fitltreflfretltretlfr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fitltreflfretltrefltr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fitltreflfretltreflfr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fitltreflfretlfretltr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fitltreflfretlfretlfr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fitltreflfretlfrefltr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fitltreflfretlfreflfr = tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fitltreflfrefltretltr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fitltreflfrefltretlfr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fitltreflfrefltrefltr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fitltreflfrefltreflfr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fitltreflfreflfretltr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fitltreflfreflfretlfr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fitltreflfreflfrefltr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fitltreflfreflfreflfr = tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fitlfretltretltretltr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fitlfretltretltretlfr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fitlfretltretltrefltr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fitlfretltretltreflfr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fitlfretltretlfretltr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fitlfretltretlfretlfr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fitlfretltretlfrefltr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fitlfretltretlfreflfr = tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fitlfretltrefltretltr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fitlfretltrefltretlfr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fitlfretltrefltrefltr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fitlfretltrefltreflfr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fitlfretltreflfretltr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fitlfretltreflfretlfr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fitlfretltreflfrefltr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fitlfretltreflfreflfr = tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fitlfretlfretltretltr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fitlfretlfretltretlfr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fitlfretlfretltrefltr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fitlfretlfretltreflfr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fitlfretlfretlfretltr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fitlfretlfretlfretlfr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fitlfretlfretlfrefltr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fitlfretlfretlfreflfr = tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fitlfretlfrefltretltr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fitlfretlfrefltretlfr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fitlfretlfrefltrefltr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fitlfretlfrefltreflfr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fitlfretlfreflfretltr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fitlfretlfreflfretlfr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fitlfretlfreflfrefltr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fitlfretlfreflfreflfr = tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fitlfrefltretltretltr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fitlfrefltretltretlfr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fitlfrefltretltrefltr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fitlfrefltretltreflfr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fitlfrefltretlfretltr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fitlfrefltretlfretlfr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fitlfrefltretlfrefltr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fitlfrefltretlfreflfr = tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fitlfrefltrefltretltr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fitlfrefltrefltretlfr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fitlfrefltrefltrefltr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fitlfrefltrefltreflfr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fitlfrefltreflfretltr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fitlfrefltreflfretlfr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fitlfrefltreflfrefltr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fitlfrefltreflfreflfr = tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fitlfreflfretltretltr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fitlfreflfretltretlfr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fitlfreflfretltrefltr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fitlfreflfretltreflfr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fitlfreflfretlfretltr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fitlfreflfretlfretlfr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fitlfreflfretlfrefltr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fitlfreflfretlfreflfr = tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fitlfreflfrefltretltr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fitlfreflfrefltretlfr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fitlfreflfrefltrefltr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fitlfreflfrefltreflfr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fitlfreflfreflfretltr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fitlfreflfreflfretlfr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fitlfreflfreflfrefltr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fitlfreflfreflfreflfr = tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fifltretltretltretltr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fifltretltretltretlfr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fifltretltretltrefltr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fifltretltretltreflfr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fifltretltretlfretltr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fifltretltretlfretlfr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fifltretltretlfrefltr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fifltretltretlfreflfr = tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fifltretltrefltretltr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fifltretltrefltretlfr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fifltretltrefltrefltr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fifltretltrefltreflfr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fifltretltreflfretltr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fifltretltreflfretlfr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fifltretltreflfrefltr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fifltretltreflfreflfr = tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fifltretlfretltretltr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fifltretlfretltretlfr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fifltretlfretltrefltr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fifltretlfretltreflfr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fifltretlfretlfretltr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fifltretlfretlfretlfr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fifltretlfretlfrefltr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fifltretlfretlfreflfr = tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fifltretlfrefltretltr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fifltretlfrefltretlfr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fifltretlfrefltrefltr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fifltretlfrefltreflfr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fifltretlfreflfretltr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fifltretlfreflfretlfr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fifltretlfreflfrefltr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fifltretlfreflfreflfr = tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fifltrefltretltretltr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fifltrefltretltretlfr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fifltrefltretltrefltr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fifltrefltretltreflfr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fifltrefltretlfretltr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fifltrefltretlfretlfr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fifltrefltretlfrefltr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fifltrefltretlfreflfr = tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fifltrefltrefltretltr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fifltrefltrefltretlfr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fifltrefltrefltrefltr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fifltrefltrefltreflfr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fifltrefltreflfretltr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fifltrefltreflfretlfr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fifltrefltreflfrefltr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fifltrefltreflfreflfr = tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fifltreflfretltretltr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fifltreflfretltretlfr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fifltreflfretltrefltr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fifltreflfretltreflfr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fifltreflfretlfretltr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fifltreflfretlfretlfr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fifltreflfretlfrefltr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fifltreflfretlfreflfr = tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fifltreflfrefltretltr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fifltreflfrefltretlfr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fifltreflfrefltrefltr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fifltreflfrefltreflfr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fifltreflfreflfretltr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fifltreflfreflfretlfr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fifltreflfreflfrefltr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fifltreflfreflfreflfr = tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fiflfretltretltretltr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fiflfretltretltretlfr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fiflfretltretltrefltr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fiflfretltretltreflfr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fiflfretltretlfretltr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fiflfretltretlfretlfr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fiflfretltretlfrefltr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fiflfretltretlfreflfr = tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fiflfretltrefltretltr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fiflfretltrefltretlfr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fiflfretltrefltrefltr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fiflfretltrefltreflfr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fiflfretltreflfretltr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fiflfretltreflfretlfr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fiflfretltreflfrefltr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fiflfretltreflfreflfr = tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fiflfretlfretltretltr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fiflfretlfretltretlfr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fiflfretlfretltrefltr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fiflfretlfretltreflfr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fiflfretlfretlfretltr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fiflfretlfretlfretlfr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fiflfretlfretlfrefltr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fiflfretlfretlfreflfr = tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fiflfretlfrefltretltr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fiflfretlfrefltretlfr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fiflfretlfrefltrefltr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fiflfretlfrefltreflfr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fiflfretlfreflfretltr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fiflfretlfreflfretlfr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fiflfretlfreflfrefltr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fiflfretlfreflfreflfr = tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight,fiflfrefltretltretltr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight,fiflfrefltretltretlfr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight,fiflfrefltretltrefltr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight,fiflfrefltretltreflfr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight,fiflfrefltretlfretltr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight,fiflfrefltretlfretlfr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight,fiflfrefltretlfrefltr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight,fiflfrefltretlfreflfr = tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight,fiflfrefltrefltretltr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight,fiflfrefltrefltretlfr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight,fiflfrefltrefltrefltr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight,fiflfrefltrefltreflfr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight,fiflfrefltreflfretltr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight,fiflfrefltreflfretlfr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight,fiflfrefltreflfrefltr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight,fiflfrefltreflfreflfr = tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight,fiflfreflfretltretltr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight,fiflfreflfretltretlfr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight,fiflfreflfretltrefltr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight,fiflfreflfretltreflfr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight,fiflfreflfretlfretltr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight,fiflfreflfretlfretlfr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight,fiflfreflfretlfrefltr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight,fiflfreflfretlfreflfr = tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight,fiflfreflfrefltretltr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight,fiflfreflfrefltretlfr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight,fiflfreflfrefltrefltr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight,fiflfreflfrefltreflfr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight,fiflfreflfreflfretltr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight,fiflfreflfreflfretlfr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight,fiflfreflfreflfrefltr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight,fiflfreflfreflfreflfr = tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight)` (n.b. x = y꼴의 할당문이 너무 길어서 편집에 지장이 가니, 코드블럭화 한다.)

인 배정이다. 이니셜 논리연산자 op1에 풀네임 논리연산자 op2를 할당하는, op1 := op2식이라는거다.

그리고, ExplictedNamedConnectiveNotation의 경우엔,

`ρ = (TrueInTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ T),TrueInFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRightEtFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ T),tiTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteTrueLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ T) ∧ (R ↔ F))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftTrueRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ T))) ↔ F),tiFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRighteFalseLeftFalseRight = * s.t. L * R = ((((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F)) ∨ ((L ↔ F) ∧ (R ↔ F))) ↔ F))` (n.b. x = y꼴의 할당문이 너무 길어서 편집에 지장이 가니, 코드블럭화 한다.)

로, 좌인자와 우인자에 대한 이름에 명시된 조건에 따른다.

이름 수가 80개인 이유는, 진리 가능성이 4개밖에 안되므로, 특정 진리값의 좌인자와 우인자에 대한 조건이, 진리값당 4 × (4×(4+1)/2)개밖에 없기 때문이다.

#### 「ExplictNamedConnectiveNotation의 모델의 모델론적 언어에서, 명제와 사실의 관계의 분석 - 진리표」에 앞서, 형식언어에서, 명제를 생성수형도로 나타낼수 있음을 보이자.

Step 1. 형식언어에서는 겉뜻 외의 속뜻은 부당하기에, 그 언어 밖이다.

뭐... 너무 당연해서 설명할 필요는 없지만, ExplictNamedConnectiveNotation의 모델의 모델론적 언어란, ExplictNamedConnectiveNotation를 말한다.

아무튼 본론으로 돌아가자.

비트겐슈타인은 진리표로 문장의 진리값을 결정하기 위해, 복합명제를 요소명제로 분리하였다.

나는 반대로, 
connectiveFormat(L) ≜ ϝ connective : L*. (ϝ t : (L*)². format("{1} {0} {2}, connective, first(t), last(t)) : L*) : 𝔉((L*)², L*)
인 connectiveFormat에 대해, 우리가 connectiveFormat이란놈이 언어 L위에서 결합자의 역할을 하더라도, 언어 L에서 무조건 "T"나 "F"로 평가되는 명제 x, y에 대하여,

Φ : truthFunction(x =>* "T", y =>* "T") ↔ (connectiveFormat(L)(connective)(x, y) =>* "T")

인 Φ가 성립하리라는 보장은 없다고 본다.

왜냐하면, Φ는 의미해석의 문법규칙 `=>*`가 의미론적인(겉뜻인)경우만 언어의 사용이라는 화용론(속뜻)일때는 작동 안하는 언어가 존재하기 때문이다.

언어의 의미가 사용에 있다. 의미해석의 문법규칙은, 해당 언어에서 화용론으로 정해지기 때문이다.

그렇기에,

th (겉뜻-속뜻 교집합상 명제의 파싱 정리). 요소명제로 분리될수 있는 경우는, 언어의 사용과 겉뜻이 일치하는 경우에 한정한다. 

형식언어는 겉뜻과 속뜻의 교집합이 겉뜻인 언어다.
왜냐하면, 겉뜻과 맞지 않는 속뜻은 해당 언어에서 틀린 문장이기에, 존재하지 않기 때문이다.

형식언어를 겉뜻으로 분석하지 않고 속뜻을 부여하는 순간, 그건 형식언어가 아닌, 그 화용론적 확장인 인공어이다.

Step 2. 겉뜻인 명제를 생성수형도로 분리해보자.

잠만



### ...작성중... (이 문서는 아직 완성되지 않았도, 종이의 내용을 옮겨적는 중)

...작성중... (이 문서는 아직 완성되지 않았도, 종이의 내용을 옮겨적는 중)