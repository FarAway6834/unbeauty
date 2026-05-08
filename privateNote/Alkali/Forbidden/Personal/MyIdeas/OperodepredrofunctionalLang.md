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

이로써, `<type> <fname>(<type>ⁿ) : <type>11는 식의 형식언어체계로, 모델론을 더 쉽게 이해하는 언어인 operodepredrofunctional lang가 정의된다.