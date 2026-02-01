# Lava System

아래 내용을 보라.

```markdown
# 명제논리와 귀결관계의 술어논리적 • 대수적의미 해석

이 문서에서는 RPN및 중위표기를 혼용하여 표기할것을 먼저 선언한다.

이하에서 명제논리 Lang인 L은 다음으로 한다.

L = {'→', '←', '↔', '∧', '∨', '⊕', '↛', '↚', '↮, '⊼', '⊽', '¬'} (주의 : ⊕는 베타적 논리합임)

## 0. 만족관계의 귀결관계화

만족관계에서, 값이 할당되는 값-배정과 구조체 모델은 값 할당 [x := y]에서 x = y의 의미를 가진다.
이는 [x := y]와 [y := x]가 x = y의 모델일수 있으며, "심볼 x가 정의되지 않음 ⊸ [x := y]가 모델" (선형논리식) 및 "심볼 y가 정의되지 않음 ⊸ [y := x]가 모델" (선형논리식)이 참이기에, 모델이 각각 정해지며, 도가지가 다 모델이 아닐때, x = y의 모델은 x = y를 증명해야 나오며, 반증되거나 증명될때 조건부로 참 거짓이거나 거짓임이 증명됨 (만족되는 모델도 당연히 없음)이나 참임이 증명됨 (항진명제이고 정리임), 혹은 증명•반증 불가함 (이 언어에서 다룰 수 없음)이 된다.
즉, 심볼 x와 값 y에 대해, 논리식 x = y는 할당 [x := y]에서 유일하게 참이되게 모델이 유일하므로, 이 만족관계에서 두가지의 의미는 같다.

즉, 만족관계는 할당 [x := y]의 의미의 명제이다.

정리하자면,

"심볼 x와 값 y에 대해 x = y" = {<x [x := y]>}이다.

아래 흐름을 따라서, `0. 0. 값-배정의 귀결관계화`와 `0. 1. 구조체를 통하여 알아보자.`를 보자.

### 0. 0. 값-배정의 귀결관계화

어떤 술어 Φ를 생각해보자.

이 술어의 변항 var₁, ..., varₙ₊ₘ에서, 
var₁, ..., varₙ을 술어의 인자(argument, parameter)로써, 술어의 입력에 binding된 변항으로 치겠다.

그리고, 나머지는 자유변항(Free Variable)으로, 술어의 입력에 binding되지 않은 변항으로 치겠다.

참고로, n > 1인 술어는 n > 1인 관계이다.

그리고 단변항 술어는 n = 1인 술어이다. (이후에 설명으로 알겠지만, 단변항인지 다변항인지는 크게 구분이 없다 ; 그 예시로 벡터공간에 대한 술어가 그렇다.)

#### 0. 0. 0. 술어와 관계는 모델론에서 같다

모델론에서 관계와 술어에 대해 살펴보자.

 + k항 관계 R은 도메인 D에 대하여, R ⊆ Dᵏ인 R이다.
 + (따라서, ) 단항관계 R은 도메인 D에 대하여, R ⊆ D¹인 R이다.
 + 술어 Φ는 도메인 D에 대하여, Φ ⊆ D인 Φ이다.

카데시안 곱에 따라서, D¹ = D다.

다변항 함자는 그 입력이 튜플이다.
즉, 도메인 D위에서 정의되는 k항함자 f에 대해, dom f = Dᵏ이다.

이하에서,

 + 단항관계는 술어와 같고
 + 다변항 술어는 입력이 튜플인 술어이며,
 + 입력이 튜플인 술어는 관계와 같다.

그리고 모델론에서 이들(관계 혹은 술어를 말한다)이 S ⊆ Dᵏ로 표현되었는데,

관계 혹은 술어 S와 인자 튜플 혹은 인자 v(Tip : 왜 v인지 의구심 같지 말길. vector여서 v면 튜플이니 인자튜플이고, value여서 v면 인자여서 v이지 않는가? 맥락은 중요치 않다. S가 취하는 값에 맞는다는 형식적 사실만 중요하다.)에 대하여, S(v)는 도메인 D에서 Boolean Domain 𝔹 = {T, F}로 가는 functor 혹은 사상으로 볼수있다.

그리고, 모델론적으로,

1. (var₁, ..., varₙ₊ₘ ⊨ Φ) ⇔ (varₘ₊₁, ..., varₘ ⊨ Φ(var₁, ..., varₙ)) (즉, 술어 S에서, 그 변항이 값을 대입한것과 같음) 이고, 
2. (S(v)) ⇔ ((∈ S)(v)) 이다.

즉, 해당 집합에 속하는지, 즉 평가(해석)하여 값-배정이 참이되는지가 그 술어이다.

따라서 이러한 맥락에서 술어는 멤버십 연산자 `∈`에 대해서 오른쪽 작용을 서술하는,
즉, 집합의 맴버십 판별을 하는 함자로,

맴버십 함자이다.


#### 0. 0. 1. 값-배정

n = 0인 경우, 보통 Σ₁⁰ A = 0으로 간주하니, 인자가 없는것으로 간주하겠다.

n = 0인경우 인자 (Argument, Parameter)가 없고, 이런 경우에는 변인은 오로지 자유 변항이 변인으로, 자유 변항의 유무에 따라 그 특성이 결정된다.

m = 0인 경우 자유 변항 (free Variable)이 없고, 이런 경우에는 인자 (Argument, Parameter), 즉 매개되는 변항인 인자만 오로지 변인이므로, 인자의 유무에 따라 그 특성이 결정된다.

n = 0, m = 0인 경우, 인자와 자유 변항이 없다.
즉, 항진 술어나 항위 술어로 작용하며, 이는 변인에 무관하게 항상 T거나 항상 F이므로, 참이나 거짓을 판단할수 있는, 이미 결정된 명제이다.

n = 0, m ≠ 0인 경우, 무항(nullary) 술어로, 이는 문장 (sentence)이다.

n ≠ 0, m = 0인 경우, 자유 변항이 없으므로, 사실 이 경우를 보통 술어라고 하며, 다른 경우는 술어로 치지 않는 겅우로, 이것은 좁은 의미의 술어다.

이경우가 술어의 표준으로 "참술어"라고 명명하겠다. 표준이 아닌 넓은 의미의 술어를 "가술어"라고 하겠다.

n ≠ 0, m ≠ 0인 경우, 인자와 자유변항이 있고, 이런 경우가 "인자와 자유 변항이 있는 가술어"이다.

"참술어"에 대한 술어논리에서는, 자유 변항과 인자의 집합론적 랭크가 rank x = 0인 집합이 아닌것 ~ rank x = 1인 집합 혹은 FOL의 술어, ..., 해서 최대 랭크가 n이라도 m = 0인 경우만 n계논리이고, 다른 자유변항은 사실상 그 위의 논리로 다뤄야 하므로, 이는 명제꼴같이 술어꼴이 되므로, (n+1)계논리의 술어의 값, 즉, n계논리 술어꼴로, 술어의 묶음이 되야 한다.

즉, "맴버십 함자"라고 방금전 우리가 탐구했던것은, 변항이 변할때를 포함해서 변항이 변할때는 술어꼴이요, 아닐때는 참술어인 가술어를 포함하는것으로, 술어논리 논리식의 평가요, 변항에 가변적인 집합 S의 맴버십 함자다.

즉, 일반적인(=자유 변항같은 술어꼴은 일부로 술어로 안쳐주는) n계논리에서 술어의 모델 (model)이란 그 술어를 만족시키는 값의 배정으로 인자 t가 길이 0 튜플인 ε, 즉 인자 없음, 혹은 t의 길이라 1로, 인자로 튜플을 안받거나, 길이가 2 이상으로 단변항 아닌 다변항인 술어로,

술어의 변항에 대한 값의 대입과 동치다.

즉,

값-배정

(v₁, ..., vₙ₊ₘ) ⊨ Φ는, varₖ = vₖ로 대입한 경우이다.

위 모양이 단순히 값-배정일수도 있으나, 튜플이다.

따라서, k항 벡터에 대한 술어로 술어의 의미론적 해석이 가능하다.

다음 네가지 Fact를 보자.

참고로, 함의 `⇒`에 대해, p ⇒ q ⇒ r을 p ⇒ q, q ⇒ r로 해석하는 규칙을 썻다. 즉, 어느 타당한 증명의 graph가 됨과 마찬가지이므로 각 명제(=논리식)들에 대한 관계의 기호로써 양 옆에 서술하는 식으로 사용되었음에 주의하자. 그래서, `⇒`및 `⇔`는 각각각 p ⇒ q ⇒ r이 p ⇒ q, q ⇒ r로, p ⇔ q가 p ⇒ q ⇒ p ⇒ q (즉, p ⇒ q, q ⇒ p, p ⇒ q로써, p ⇔ q ⇔ r이 p ⇒ q, q ⇒ p, p ⇒ q로, p ⇔ q ⇔ r이 p ⇒ q, q ⇒ p, p ⇒ q, q ⇒ r, r ⇒ q, q ⇒ p로, p ⇔ q ⇒ r이 p ⇒ q, q ⇒ p, p ⇒ q, q ⇒ r식으)로 모호하지 않게 형식문법에 맞게 형식적이고 명확하게 해석된다.)

Fact1) (∀x)(¬Φ(x)) ⇔ (∄x)(Φ(x)) ⇔ (⊭ Φ) ⇔ (⊭ ¬Φ) ⇔ (Card Mod(Φ) = 0) ⇔ (Card Mod(¬Φ) = Card U) ⇒ (∃x)(¬Φ(x)) ⇔ (Card Mod(Φ) ≠ 0) (단. U는 전체집합으로, Card Mod(¬Φ) = Card U라고 하는 문장은 괭장히 모호한 문장으로써, 실제로는 저 부분은 그냥 무시(=항진명제로 치환하여 생각)하도록 하자. 참고로, 어떤 임의의 x를 준비하더라도, 항진명제 Ψ에 대하여서 참이다. 왜냐하면 항진명제는 항상 참이기 때문이다. 그러므로, 어떤 임의의 x를 준비하더라도, 항진명제 Ψ에 대하여서 참이다, 또한 구성적 증명에서 존재성을 구성으로 증명하는데, 이는 존재성을 보이기 위해, x를 준비하는것과 같다. 따라서, ∃x를 증명할때 단순히 그 x를 가져오면 븡명할수 있다. 즉, 어떤 임의의 x를 준비하더라도, 항진명제 Ψ에 대하여서 참이라는걸 바꿔말하자면, 항진명제 Ψ는 어떤 임의의 x를 준비하더라도 항상 만족되어 참으로, 존재성이 증명된다.)
Fact2) (∀x)(Φ(x)) ⇔ (⊨ Φ) ⇒ (Card Mod(Φ) ≠ 0)
Fact3) (∃x)(Φ(x)) ⇔ (∃x)(x ⊨ Φ) ⇔ (Card Mod(Φ) ≠ 0)
Fact4) (∃!x)(Φ(x)) ⇔ (Card Mod(Φ) = 1)

즉, 서술하는 대상의 존재성이 존재론의 해법이라느니 (사실 당연한 소리고, 그 존재기호는 수리논리 이외에 많은 언어를 포함해서 대체 어디서 오냐고 묻고싶어 답답하다.), 양화사가 Quntitifier인것은 Quntiti + fing하는것이니 다 맞다.

즉, 만족되는 모델의 크기를 집합의 기수로, 측도로 볼수 있으며, 그것에 대해 균등분포로 경우의 수나 확률로 분석할수 있음도 당연하고,

모델론과 술어논리가 그 의미에 있어서 동일한(즉, `⇔`로 서술된)일부 맥락을 공유하며,

모델을 통하여, 술어논리를 값-대입으로 볼 수 있음을 알수 있다.

### 0. 1. 구조체를 통하여 알아보자.

구조체에 튜플을 사용함은 튜플이 벡터이니 그리 해석할수 있음도 알수 있다.
다변수 함자의 맥락에서, 다변수 함수는 튜플을 인자로 받는 함수이다. 즉, 벡터에 대한 함수이다.

모델론적 언어 L에 대하여, 그 L의 심볼에 값을 바인딩시키는것은
모델 M이 한다. 즉 기표 L과 기의를 연결시키는 lang이다.
모델 M의 도메인 D에 대해,
M = <
D,
  ConstantSymbol₁ := ConstantSymbolValue₁,
  ...,
  ConstantSymbolᵢ := ConstantSymbolValueᵢ,
  
  FunctionSymbol₁ := ConstantSymbolValue₁,
  ...,
  FunctionSymbolⱼ := FunctionSymbolValueⱼ,
  
  RelationSymbol₁ := RelationSymbolValue₁,
  ...,
  RelationSymbolₖ := RelationSymbolValueₖ,
  
  PredicateSymbol₁ := PredicateSymbolValue₁,
  ...,
  PredicateSymbolₗ := PredicateSymbolValueₗ,
  
  LogicSymbol₁ := LogicSymbolValue₁,
  ...,
  LogicSymbolₘ := LogicSymbolValueₘ,
  
  VariableSymbol₁ := VariableSymbolValue₁,
  ...,
  VariableSymbolₙ := VariableSymbolValueₙ
> (Tip : 따라서, 술어의 값-배정 역시 도메인 D에 대한 `변항ᵥ := 변항값ᵥ`로 볼 수 있음이 당연하다. (중요))

이는 Alkalic의 대입 연산 `[x := y], 혹은 Python에서, `:=`연산자와 같기에,

M = <
D,
  ConstantSymbol₁ [ConstantSymbol₁ := ConstantSymbolValue₁],
  ...,
  ConstantSymbolᵢ [ConstantSymbolᵢ := ConstantSymbolValueᵢ],
  
  FunctionSymbol₁ [FunctionSymbol₁ := ConstantSymbolValue₁],
  ...,
  FunctionSymbolⱼ [FunctionSymbolⱼ := FunctionSymbolValueⱼ],
  
  RelationSymbol₁ [RelationSymbol₁ := RelationSymbolValue₁],
  ...,
  RelationSymbolₖ [RelationSymbolₖ := RelationSymbolValueₖ],
  
  PredicateSymbol₁ [PredicateSymbol₁ := PredicateSymbolValue₁],
  ...,
  PredicateSymbolₗ [PredicateSymbolₗ := PredicateSymbolValueₗ],
  
  LogicSymbol₁ [LogicSymbol₁ := LogicSymbolValue₁],
  ...,
  LogicSymbolₘ [LogicSymbolₘ := LogicSymbolValueₘ],
  
  VariableSymbol₁ [VariableSymbol₁ := VariableSymbolValue₁],
  ...,
  VariableSymbolₙ [VariableSymbolₙ := VariableSymbolValueₙ]
> (Tip : 《동일하다!》따라서, 술어의 값-배정 역시 도메인 D에 대한 `[변항ᵥ := 변항값ᵥ]`로 볼 수 있음이 당연하다. (중요))

임과 같다.

만족관계 M ⊨ T에 대해,

T의 기호들은 모델론적 언어 L에 의해 해석되며,

이는,

다음과 같은 값-배정 x̄

x̄ = (
  DomainOfM := ValueOfDomainOfM,
  
  ConstantSymbol₁ := ConstantSymbolValue₁,
  ...,
  ConstantSymbolᵢ := ConstantSymbolValueᵢ,
  
  FunctionSymbol₁ := FunctionSymbolValue₁,
  ...,
  FunctionSymbolⱼ := FunctionSymbolValueⱼ,
  
  RelationSymbol₁ := RelationSymbolValue₁,
  ...,
  RelationSymbolₖ := RelationSymbolValueₖ,
  
  PredicateSymbol₁ := PredicateSymbolValue₁,
  ...,
  PredicateSymbolₗ := PredicateSymbolValueₗ,
  
  LogicSymbol₁ := LogicSymbolValue₁,
  ...,
  LogicSymbolₘ := LogicSymbolValueₘ,
  
  VariableSymbol₁ := VariableSymbolValue₁,
  ...,
  VariableSymbolₙ := VariableSymbolValueₙ
)

과 같으며,

연산은 Function Symbol이므로, 함수이기 때문에

자명히 (사실 스스로 evidance인건 없기에, "다명히"가 아닌 "당연히")

다가함수로 쓸 수 있고,

M = <
  DomainOfM,
  
  ConstantSymbol₁ [ConstantSymbol₁ := ConstantSymbolValue₁],
  ...,
  ConstantSymbolᵢ [ConstantSymbolᵢ := ConstantSymbolValueᵢ],
  
  FunctionSymbol₁ [FunctionSymbol₁ := FunctionSymbolValue₁],
  ...,
  FunctionSymbolⱼ [FunctionSymbolⱼ := FunctionSymbolValueⱼ],
  
  RelationSymbol₁ [RelationSymbol₁ := RelationSymbolValue₁],
  ...,
  RelationSymbolₖ [RelationSymbolₖ := RelationSymbolValueₖ],
  
  PredicateSymbol₁ [PredicateSymbol₁ := PredicateSymbolValue₁],
  ...,
  PredicateSymbolₗ [PredicateSymbolₗ := PredicateSymbolValueₗ],
  
  LogicSymbol₁ [LogicSymbol₁ := LogicSymbolValue₁],
  ...,
  LogicSymbolₘ [LogicSymbolₘ := LogicSymbolValueₘ],
  
  VariableSymbol₁ [VariableSymbol₁ := VariableSymbolValue₁],
  ...,
  VariableSymbolₙ [VariableSymbolₙ := VariableSymbolValueₙ]
> [DomainOfM := ValueOfDomainOfM]

대신

(peano 산술상의 집합 𝔹 = {0, 1}를 dom f = 𝔹로 하고 codom f = dom f인 함수로 논리연산을 할당할때) 수열의 곱 혹은 (Zhegalkin Boolean Domain 𝔹 = {0, 1}에서) Zhegalkin 논리곱, 혹은 𝔹 = {F, T}에서 논리곱은 전부 동형으로, 그 논리연산이라는 부울-대수에서 동형이므로, 즉, 메타논리 입장에서 각 기호들에 대한 논리식들이 해석되는 모든 모델론적 입장이 같으므로, 같게 취급하여,
논리곱, Zhegalkin 논리곱, 대수학에서 곱셈은 가환군을 이루므로, 이들을 모두 수열의 곱 Π으로 취급해서 (사실은 x̄ = (Symbol := value)의 바인딩일때 이 곱이 구조체 M임은 당연하다 (중요!), 이것이 근거임, 동형성의 근거이고 사실상 증명에 준하는 핵심 원리)

z = x [x := y] ⊨ z = x, x = y 이므로, 논리적 귀결관계 x [x := y] ⊨ x (선택적 ; x가 술어나 명제가 아니면 귀결되지 아니한다), x = y에서, 만족관계 (x := y) ⊨ (x = y) 와 동등한 의미로,

대입 연산(진리값을 가지는 대상을 귀결관계를 통해 함의하는 논리 연산이기도 하다)을 담은 논리식을 정의역으로 하는 벡터, 즉 값-배정 x̄는

x̄ = <
  [DomainOfM := ValueOfDomainOfM],
  
  [ConstantSymbol₁ := ConstantSymbolValue₁],
  ...,
  [ConstantSymbolᵢ := ConstantSymbolValueᵢ],
  
  [FunctionSymbol₁ := FunctionSymbolValue₁],
  ...,
  [FunctionSymbolⱼ := FunctionSymbolValueⱼ],
  
  [RelationSymbol₁ := RelationSymbolValue₁],
  ...,
  [RelationSymbolₖ := RelationSymbolValueₖ],
  
  [PredicateSymbol₁ := PredicateSymbolValue₁],
  ...,
  [PredicateSymbolₗ := PredicateSymbolValueₗ],
  
  [LogicSymbol₁ := LogicSymbolValue₁],
  ...,
  [LogicSymbolₘ := LogicSymbolValueₘ],
  
  [VariableSymbol₁ := VariableSymbolValue₁],
  ...,
  [VariableSymbolₙ := VariableSymbolValueₙ]
>

로, 수열의 곱 연산을 통해

(M ⊨ T) ⇔ (Πx̄ ⊨ T)

임이

> 
>  [DomainOfM := ValueOfDomainOfM],
>  
>  [ConstantSymbol₁ := ConstantSymbolValue₁],
>  ...,
>  [ConstantSymbolᵢ := ConstantSymbolValueᵢ],
>  
>  [FunctionSymbol₁ := FunctionSymbolValue₁],
>  ...,
>  [FunctionSymbolⱼ := FunctionSymbolValueⱼ],
>  
>  [RelationSymbol₁ := RelationSymbolValue₁],
>  ...,
>  [RelationSymbolₖ := RelationSymbolValueₖ],
>  
>  [PredicateSymbol₁ := PredicateSymbolValue₁],
>  ...,
>  [PredicateSymbolₗ := PredicateSymbolValueₗ],
>  
>  [LogicSymbol₁ := LogicSymbolValue₁],
>  ...,
>  [LogicSymbolₘ := LogicSymbolValueₘ],
>  
>  [VariableSymbol₁ := VariableSymbolValue₁],
>  ...,
>  [VariableSymbolₙ := VariableSymbolValueₙ]
>  
>  ⊨
>  
>  T
> 

인 귀결관계를 만족한다는것과 같으므로, 당연한 이치이다.

## 1. 명제논리 결합자(연결사)의 해석

명제논리 결합자, 즉 논리연산자는 술어로 해석할수 있으며, 동시에 연산으로 해석할수 있다.

### 1. 1. 진리 함자

임의의 논리 결합자 기호 S₁에 대해 그 결합자의 역할을 하는 술어 Φ(S₁)을 다음과 같이 정의한다.

DEFINITION) ∀S₁ ∈ L, "⋯" Φ("S₁") : "⋯ S₁"

예컨데,

 + p q Φ("→")는 p가 q를 함의하는것이고,
 + p Φ("¬")는 p의 부정이다.

즉, 이 진리 함자 Φ("S₁")를 치역으로 하는 길이 1의 문자열 집합 S ⊆ L+이 치역인 함수 Φ에 대해, Φ("S₁")와 "S₁"은 평가가 같으므로, 의미론적으로, 같다 볼수 있고,

사실, "⋯ S₁" ⇔ "⋯" Φ("S₁") 이므로, 걍 사용에 있어서 같다.

즉, 술어로써의 Φ("S₁")는 Card를 정의하지 않았을때의 언어에서 S₁과 언어 내 의미론적으로 같고, 실제 개념상으로 부터 다르며 구문론적으로 다르다.

### 1. 2. 명제논리 모델간의 동형성

#### 1. 2. 1. Zhegalkin 다항식 혹은 {0, 1}이 정의역이자 공역인 사상으로써의 동형성

명제논리와 Zhegalkin Polynomial (Algebric Normal Form)에서, 다음 함자를 준비하자.

두 집합 B, 𝔹에 대해,

Zhegalkin Polynomial의 대수에서,

Zhegalkin Boolean Domain B는 B = {0, 1}

부울 대수(=불 대수)에서,

Boolean Domain 𝔹는 𝔹 = {F, T}

𝔹에서 B로 가는 함수 int와 B위의 술어 bool에 대해,

+ bool(x) : x = 1
+ $ int(x) = \begin{cases} 1, & x, \ 0, & ¬x \end{cases} $

참고로, "x ∈ B" ⇔ "x가 Zhegalkin Polynomial의 대수 위에 있음" 이고, 항진명제 a ≠ b ↔ ¬(a = b), 0 ≠ 1에서, 등호는 동치관계이므로, "⊭ x = 0, x = 1"임이 증명되므로, B = {0, 1} = {x | x = 0 ∨ x = 1}에서, x ∈ B ↔ x = 0 ∨ x = 1이므로, x = 0과 x = 1은 x가 Zhegalkin Polynomial의 대수 위에 있을때, 반대이며 소반대이므로, x ≠ 0 ↔ ¬(x = 0) ↔ x = 1이며, x ≠ 1 ↔ ¬(x = 1) ↔ x = 0이다.

즉, bool(x) ↔ x ≠ 0이다.

y = int(x)에서, y ∈ B ↔ y ≠ 0 ↔ ¬(y = 0) ↔ y = 1이며, y ≠ 1 ↔ ¬(y = 1) ↔ y = 0이고, y = 0 ⊕ y = 1 이다.

함자 (int)및 함자 (bool)은 각각

 + dom (int) = 𝔹 = codom (bool)
 + codom (int) = B = dom (bool)

이고 동형사상이다. 왜냐?

부정논리곱을 x▪︎y = 1 - xy로 표현 가능하다.

이는 (1 -)(x) = 1 - x가 대합 사상으로, 전단사이기 때문에, 

이가 원리에 따라서,

Alkalic관련 포스트에서 말했던것처럼,

사상 (int)및 (bool)은 그 연산이 대응되도록 보존하는 고전적 정의에서의 준동형사상이자, 전단사 사상으로, 서로 역함자인 동형사상이다.

따라서, 모든 명제논리가 Zhegalkin이나 {0, 1}이 정의역이거나 공역인 사상과 동형으로, 동형임을 알 수 있다.

#### 1. 2. 2. 동일 형식시스템의 공리계로써의 동형성

(x, y) Φ("S₁")이거나, x Φ("S₁")이거나로, 그 진리 함자로 논리연산자를 취급하여보겠다. 

즉, 전부 t Φ("S₁")로 퉁치겠다.

어떤 논리식(=문장) Ψ("S₁")을 정의하겠다.

t Ψ("S₁") : t Φ("S₁")

SOL을 쓴게 흠이지만...

 + Ψ("S₁") ⇔ Φ("S₁") 이므로,
 + Mod(Ψ("S₁")) = Mod(Φ("S₁")) 이다.

즉, 평가(=해석)가 같다.

어떤 논리식 논리식 Ψ("S₁")은 문장이다.

어떤 형식시스템에서, 법칙 (Ψ("S₁") ↔ Φ("S₁"))을 만족하는 Ψ("S₁")로 Ψ("S₁")가 정의됨은 당연하다 (중요)

따라서, 그 형식시스템에서의 법칙을 통하여, Ψ("S₁")가 정의된다.

M ⊨ (Ψ("S₁") ↔ Φ("S₁"))인 경우는 경우를 나누어 크게 두가지가 있다.

1. (Φ("S₁") : Ψ("S₁"))로 정의된경우, 즉, [(t S₁) := (t Ψ("S₁"))]로 모델이 정의시켜버리는 경우
2. (Φ("S₁") : Ψ("S₁"))로 정의되지 아니하고, 모델이 법칙 (Ψ("S₁") ↔ Φ("S₁"))를 만족시키는 경우

두번째 경우가 존재하지 아니하면 무조건 첫번째 경우이다.

그치만 저 경우에, 두 모델에서 S₁이 완전히 동일하게 동작하도록 정의되었다는 사실은 변하지 않는다. 
즉,

M = <𝔹, S₁>과 M = <𝔹, S₁'>에서, M ⊨ (Ψ("S₁") ↔ Φ("S₁"))에서, 두 M은 동형이요, 동일한 이론의 모델이다.

따라서 명제논리가 표준과 호환이라면 다음 정의가 명시하는 논리식을 만족한다.

DEFINATION 1)

1. p ← q : q → p

DEFINATION 2)

1. p ↔ q : p → q, q → p


아래 DEFINATION 3.A.와 DEFINATION 3.B.와 DEFINATION 3.C. 는 서로 동형인 정의이다. 즉, TFAE이다.

DEFINATION 3.A.)

1. ↔가 반사성을 만족
2. ↔가 대칭성을 만족
3. ↔가 추이성을 만족

DEFINATION 3.B.)

1. (p → q, q → r) → (p → r)
2. (p, p → q) → (q)
3. ⊨ p → T

웃긴 사실은 이를 통해서, →가 항상 건전한 추론규칙으로 작용한다는걸 알 수 있다. 아니 건전한게 이거인가?

아무튼, 어떤 Theorem t에 대해? p → t가 건전함은 곧 p가 참임이다.

DEFINATION 3.C.)

1. p → q : ¬p ∨ q

DEFINAFION 4. & 5. & 6. & 7. & 8. & 9.)

1. TREF on De Morgan's Law & 이중부정의 법칙
1. 1. p ↛ q : ¬(p → q)
1. 2. p ↛ q : p ∧ ¬r
1. 3. p ↚ q : ¬(q → p)
1. 4. p ↚ q : ¬p ∧ q
1. 5. p ↮ q : ¬(p ↔ q)
1. 6. p ↮ q : p ⊕ q
1. 7. p ⊕ q : (p ∨ q) ↛ (p ∧ q)
1. 8. p ⊼ q : ¬p ∨ ¬q
1. 9. p ⊽ q : ¬p ∧ ¬q
1. 10. p ⊼ q : ¬(p ∧ q)
1. 11. p ⊽ q : ¬(p ∨ q)
1. 12. p ∧ q : ¬p ⊽ ¬q
1. 13. p ∨ q : ¬p ⊼ ¬q
1. 14. ¬x ↮ x
1. 15. x : ¬¬x
1. 16. ¬x : x ⊕ x

## 2. 아리스토텔레스 논리학에서 온 형식적 조작의 비형식적 맥락과 불 및 기타 논리학자 및 수학자 및 전산학자들을 통한 후대의 추가된 맥락과 원래부터 있던 맥락 등 등 보통의 논리에서 취급되는 맥락

 + ↔는 동등함, 즉 동등성의 원리를 만족시키고 동치 (순화어로는 동등)관계이며, 정언논리상의 모순관계와 반대에 있는 관계이다. 즉, 논리적 동등.
 + 베타적 논리합, 베타적 선언인 ⊕는 (p, q)인 경우에 베타적이며, 이의 부정은 논리적 동등이다.
 + 가언, 즉, 함의(→)는 건전성을 만족시킨다. 왜냐하면 건전겅 그 자체인 명제논리 기호이기 때문이다.
 + 선언, 즉 포함적 선언인 "혹은"은 즉, ∨는 ∧와 쌍대인 관계이며, p ∨ q에서 [p | q]로 선택할때 어느 하나로 계산되어도 참이여야 하므로, p와 q가 참이라도, 어느 하나를 선택하였을때 p = q = 참이므로 참이다. 어느 하나라도 참이면 된다.
 + 연언, 즉, 연속해서 x, y, z를 놓았을때 모델론으로 보면 참 편하게 해석할수 있는데, 암튼 연언은 "그리고"의 뜻으로 연연이 서술하는 말들은 전부 참이여야 한다.
 + 부정은 부정문의 형태를 띄며, 긍정문을 부정하면 부정문이고, 부정문을 부정하면 긍정문이며, 긍정이 아님을 뜻하며, 긍정함은 참이라고 함을 뜻하므로, 부정은 "T↮"를 의미한다.
 + 전건이 부정문인 함의문은 전건의 부정과 후건의 긍정의 선언과 논리적으로 같다.
 + 후건이 부정문인 함의문은, 전건의 부정과 후건의 긍정의 부정연언문과 과 논리적으로 같다.
 + ↔가 쌍조건문으로써 작용한다. 즉, ↔임이 함의와 역함의임이다.
 + 연언은 모델론의 언어에서 ∧가 `,`로 취급된다.
 + 가언은 모델론의 언어에서 →가 `⊨`로 취급된다. (겐첸의 연역정리에 따라서 말이다)
 + 모델론에 언어에서, 부정문 중 x가 항위인건 `⊭ x`로써, x에 대해 부정한다. 사실 `x ⊨ F`로써, 후건을 부정해서 만족불가능화할수도 있지만. 주의할점은 만족 불가능은 만족관계에서 나온 개념이다.
 + 모델론의 언어에서, 긍정문 중 x가 항진인건 `⊨ x`로서, x에 대해 긍정한다. 사실 `T ⊨ x`로써, 전건을 긍정해주거나, 정리를 넣어 참에서 함축시켜버리는것과 같지만. 주의할점은 만족가능은 만족관계에서 나온 개념이다.
 + 모델론의 언어에서, x ⊨ y이고, y ⊨ x이면, x와 y가 같다. 만족관계를 이야기하는것이 아니다.

## 3. L = {'→', '←', '↔', '∧', '∨', '⊕', '↛', '↚', '↮, '⊼', '⊽', '¬'}의 표의문자성에 근거한 설명

 + 긍정문 x에 대해 ¬x는 부정문이다.
 + 우향화살표를 쓰는 구문 x → y는 함의문이다.
 + 좌향화살표를 쓰는 구문 x ← y는 역함의문이다.
 + 우향의 역항은 좌향이다. 따라서, 주결합자를 기준으로 법선을 새워서 법선에 대해 대칭이동하면, 함의문의 모양이 된다.
 + 좌향화살표와 우향화살표 모두, 화살표에 의한 가리킴을 당하는쪽과 시키는쪽이 함의문에서의 후건과 전건의 역할을 하게 된다.
 + 보통 화살표는 다이어그램에서 생기다 보니, 그런 보편적인 직관에서 생긴 기호의 설명으로 해석할수 있다. 그러나 기표와 기의 자체의 필연적 연결은 없다.
 + 빗금(□̸)친 곳에 위치한 기표 혹은 바(bar, ō)표시된데에 위치한 기표는 주결합자의 치역에 부정을 취한것이다. 이건 문법규칙으로 작용시켜도, 실제 형식언어의 동작과 일치한다. 근데 사실 빗금은 조건문(함의문) 및 쌍조건문에만 쓰였다는게 특징.
 + 쌍조건문은 정방향 조건문이자 역방향 조건문으로 쌍방향이다. 뭐... 이렇게 양방향함의에만 적용되는 규칙(실제 동작과 일치하므로)도 기표와 기의 자체의 필연적 연결이 없으니 그저 설명일 뿐이다.
 + ∧와 ∨는 쌍대성의 관점에서 서로 쌍대(dual)로 거울처럼 맞물려 설명되기에 저리 상하반전된 대칭이동상태로 쓴다. 갑자기 그런 관점이 왜 나오냐고? 이의 있다면 dual(유희왕 듀얼리스트 드립)을 하여 결정하자. (원래 ∨가 먼저 쓰였다. 러셀과 화이트헤드의 Principia Mathematica에서부터.) 마찬가지로 근본적 필연은 아니다. 사실 그래서 a & b (a and b), a | b (a or b)로 표기하는 경우도 많다. 대표적으로 c에서 파생한 문법을 가지는 튜링 언어들의 비트연산.
 + pm (Principia Mathematica, 형식화) : Φ & Ψ, Φ ∨ Ψ
 + la (LINGUA LATINA, Όργανον 번역) : Φ et Ψ, Φ vel Ψ
 + Ελ (Ελληνικά, Όργανον) : Φ καί Ψ, Φ ἤ Ψ
 + 베타적 논리합 Φ aut Ψ는 중세 스콜라 철학자들테 의해 (포함적) 논리합과 구분됨.
```
만족관계는 해당 내용으로 귀결관계로 해석할 수 있고, 명제논리 결합자는 그저 연산자 혹은 술어이다.

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 만족•귀결기호 `⊨`가 존나 흥건히 나오지만, 그건 만족•귀결의 의미로 의미론적으로 같아 해석하여 이해하면 "변인에 대한 값의 할당"을 「만족」과 「명제의 귀결」로 구체적으로 이해해보자 • 그리고 하게 할 것의 목적이며, 정의 기호와의 혼용은 전혀, 전혀, 전혀 없이, 잘 쓰여있다. 간혹 정의같이 나온다면, 정의의 의미를 가진 귀결로, 귀결에는 오류가 없다 단언한다. 미지막으로, `≜`가 나올것같은데에 `⊨`를 쓴거는 바로 당신이 문맥으로 읽다가 뒤통수맞은거다... 수학을 할때는 문맥을 버려라. 문맥이 아닌 형식주의적인 조작이기 때문에, 진짜로 `⊨`를 써서 설명했기 때문이다. 정의가 아니라 만족 혹은 귀결을 썼다면 문자 그대로 이해해야한다. 그것이 참이기 때문이다. (글 읽을땨마다 이곳을 참고헐것)

(내가 추상대수학 배우려고 만든 체계)

닫힌형태의 대수구조를 폐구조라고 명명하고, Lava라고 부르겠음.

관계가 주어지지 않은 n개의 함수와 m개의 심볼을 가진 Structure

M = <D, Sym₁, ..., Symₘ, fun₁, ..., funₙ>를 (m, n)-Lava라고 하겠음

(m, 0)-Lava는 (심볼을 정의한, 즉 정의용) 집합인 기본적인 대수구조이다.

참고로, (m, 1)-Lava이상은, 각 연산이 전부 D와 마그마를 이룬다.

Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ) ≜ <D, Sym₁, ..., Symₘ, fun₁, ..., funₙ>

라 하겠다.

Volcano는 (m, n)-Lava를 생성하는 무한 차원의 (= 행과 열의 총 길이가 자연수 기수 길이인) 함수행렬이다.

그래서 (=행렬이기 때문에) Volcanoₘ,ₙ식으로 표현한거다.

Volcanoₘ,ₙ은 (m, n)-Lava를 구성하는 함수이다.

이하에서 대부분 저런 행렬 형식은 인자가 무제한으로 (= 자연수 기수 크기까지인 무한정 = ℵ₀가 최대길이인것임)

예컨데, Volcano₂,₀(𝔹, F, T)는 부울-도메인으로 유명하다.

내가 스스로 정의한
Lava에서 확장한걸로 구조꼴 (structure form)이라는게 있는데, 아래와 같다.

StructureFormₗ,ₘ,ₙ(D, Sym₁, ..., Symₗ, fun₁, ..., funₘ, Pre₁, ..., Preₙ) ≜ <D, Sym₁, ..., Symₗ, fun₁, ..., funₘ, Pre₁, ..., Preₙ>

Pre₁, ..., Preₙ는 술어이고, 이게 뭐하나 미스되지 않고, Lava랑은 달리 있을거 다있게 정의된 구조의 최소 단위이므로, 이를 "구조꼴"이라고 하고, 삼차원 행렬 (= 이제 텐서 ㅋㅋㅋㅋ) StructureForm를 통해 만들 수 있다.

텐서라고 웃은 맥락은, 행렬은 이차원 텐서라고들 해서, 삼차원 행렬이 텐서라고 말한거긴 하다.

(근데 나 멀미나와서 오늘은 여기까지 작성하겠고, 추상대수학은 여기까지 배우겠음.)

StructureForm이 삼차원 행렬이기에, StructureFormₗ,ₘ,ₙ식으로 쓸 수 있었던것이다.

(l, m, n)-구조꼴을 생성하는 함수는 StructureFormₗ,ₘ,ₙ이다.

## 대수 구조 공부

### 극한에 대하여

`⟶` 요 기호는 함의 기호 `→` 가 아니다.
단지, 교과서에 나온 접근 기호와 가장 비슷한 기호를 골라 접근 기호로 쓰는 것 뿐.
앞으로 접근 기호 `⟶`는 접근의 기호로 쓰일것이다.

나는 대충 아래 새가지가 성립한다고 안다.

1. x ∈ {x | Φ(x)} : Φ(x)
2. {Φ(x) | Ψ(x)} = {x | Φ(x), Ψ(x)}
3. {f(x) | Φ(x)} = {y | y = f(x), Φ(x)

2, 3부분은 분류공리꼴땜에 된다고 안다.

그리고 나는 상을 이렇게 알고있다.

f[X] ≜ {f(x) | x ∈ X}

그러므로, 이를 전제에 깔고 가겠다.

그리고 구문론적 정의로 표기법 하나만 도입하겠다.

def) NOTATION(Φ ? x : y) ≡ $ \begin{cases} x, & Φ, \ y, & ¬Φ \end{cases} $

예컨데, 

> 
> $ \begin{cases} 1/x, & x ≠ 0, \ 0, & x = 0 \end{cases} $
> 

이런식의 수식을 작성하고 싶다면,

> 
> NOTATION(x ≠ 0 ? 1/x : 0)
> 

이런식으로 작성 가능하다. C 코드같이 생긴 저건 표기법이다. 절대로 삼항연산자가 아닌거다!!

다음으로 defined, undefined 표기법을 도입하겠다.

x is defined : ∃!k, x = k
x is undefined : ¬(x is defined)

defined, undefined는 함숫값이 정의되는지를 판단하는 enum이기에, 유일성을 따진다.

ℝdist는 수직선 위의 두 실수 사이의 거리를 구하는 함수이다.

ℝdist(x, y) ≜ |x - y|

따라서 차의 절댓값(일차원 벡터의 노름이기도 하다.)을 그 값으로 한다

"한계 오차 ε를 기준으로 x가 y에 접근함"은 `x ⟶ y (by ε)`라고 쓰고, 다음과 같이 정의한다.

x ⟶ y (by ε) : NOTATION(ε > 0, NOTATION(y = ∞, x > ε, NOTATION(y = -∞, x < -ε, ℝdist(x, y) < ε)), x is undefined)


예컨데,

(x ⟶ a (by ε)) ↔ (|x - a| < ε) (단. ε > 0)

이고,

(x ⟶ ∞ (by M)) ↔ (x > M) (단. M > 0)

이며,

(x ⟶ -∞ (by M)) ↔ (x < - M) (단. M > 0)

이다.

참고로,

t ≥ 0에서,

(x ⟶ y (by 0 - t)) ↔ x is undefined

이다.

다음으로 좌접근, 우접근을 정의하겠다.

x ⟶ y ± (by ε) : NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, NOTATION(±1 = 1, y < x < y + ε, y - ε < x < y), x is undefined) (복부호 동순)

예컨데,

x ⟶ y+ (by ε) ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, NOTATION(+1 = 1, y < x < y + ε, y - ε < x < y), x is undefined)

이며

x ⟶ y- (by ε) ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, NOTATION(-1 = 1, y < x < y + ε, y - ε < x < y), x is undefined)

이다.

즉,

+1 = 1 ↔ T, -1 = 1 ↔ F 이므로,
x ⟶ y+ (by ε)
 ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, NOTATION(+1 = 1, y < x < y + ε, y - ε < x < y), x is undefined)
 ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, NOTATION(T, y < x < y + ε, y - ε < x < y), x is undefined)
 ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, y < x < y + ε, x is undefined)

이며

x ⟶ y- (by ε)
 ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, NOTATION(-1 = 1, y < x < y + ε, y - ε < x < y), x is undefined)
 ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, NOTATION(F, y < x < y + ε, y - ε < x < y), x is undefined)
 ↔ NOTATION(y ≠ ∞ ⊼ y ≠ -∞ ⊼ ε > 0, y - ε < x < y, x is undefined)

이다.

그러므로,

t ≥ 0에 대해,

x ⟶ ∞± (by ε) ↔
x ⟶ -∞± (by ε) ↔
x ⟶ a± (by 0 - t)
 ↔ x is undefined

이다.

이하에서 a ∈ ℝ에서,

x ⟶ a+ (by ε) : a < x < a + ε (단. ε > 0)

이며

x ⟶ a- (by ε) : a - ε < x < a (단. ε > 0)

이다.

다음으로는 x ≠ y일때의 접근을 정의하겠다.

참고로, `x ⟶ y (by ε)`에서, y가 `a+`거나 `a-`여도 좋다.

x ⟶̣ y (by ε) : (x ≠ y), x ⟶ y (by ε)

`x ⟶̣ y (by ε)`는 "(x ≠ y)이고 x ⟶ y (by ε)"임을 의미한다.

그게 다다. ㅋㅋㅋㅋ

x ⟶̣ y+ (by ε) ↔ (x ≠ y), x ⟶ y+ (by ε)

이며,

x ⟶̣ y (by ε) ↔ (x ≠ y), x ⟶ y (by ε)

이고,

x ⟶̣ y- (by ε) ↔ (x ≠ y), x ⟶ y- (by ε)

이다.

이제 극한 • 좌극한 • 우극한을 정의하겠다.

lim f(x) = L (x ⟶ a) : ∀ε>0, ∃δ>0 s.t. ((x ⟶̣ a (by δ)) → (f(x) ⟶ L (by ε))

이에 따라,

(lim f(x) = L ∈ ℝ (x ⟶ ±∞))
 ↔ (∀ε>0, ∃K>0 s.t. ((x ⟶̣ ±∞ (by K)) → (f(x) ⟶ L ∈ ℝ (by ε)))
 ↔ (∀ε>0, ∃K>0 s.t. NOTATION(±1 = 1, x > K, x < -K) → (f(x) ⟶ L ∈ ℝ (by ε)))

이고,

(lim f(x) = ±∞ (x ⟶ ±∞))
 ↔ (∀M>0, ∃K>0 s.t. ((x ⟶̣ ±∞ (by K)) → (f(x) ⟶ ±∞ (by M)))
 ↔ (∀M>0, ∃K>0 s.t. NOTATION(±1 = 1, x > K, x < -K) → NOTATION(±1 = 1, x > M, x < -M))

이며,

(lim f(x) = ∓∞ (x ⟶ ±∞))
 ↔ (∀M>0, ∃K>0 s.t. ((x ⟶̣ ±∞ (by K)) → (f(x) ⟶ ∓∞ (by M)))
 ↔ (∀M>0, ∃K>0 s.t. NOTATION(±1 = 1, x > K, x < -K) → NOTATION(∓1 = 1, x > M, x < -M))

이고,

(lim f(x) = ∓∞ (x ⟶ a ∈ ℝ))
 ↔ (∀M>0, ∃δ>0 s.t. (x ⟶̣ a (by δ)) → (f(x) ⟶ ∓∞ (by M)))
 ↔ (∀M>0, ∃δ>0 s.t. (x ⟶̣ a (by δ)) → NOTATION(∓1 = 1, x > M, x < -M))

이며,

(lim f(x) = ±∞ (x ⟶ a± ∈ ℝ))
 ↔ (∀M>0, ∃δ>0 s.t. (x ⟶̣ a± (by δ)) → (f(x) ⟶ ±∞ (by M)))
 ↔ (∀M>0, ∃δ>0 s.t. (x ⟶̣ a± (by δ)) → NOTATION(±1 = 1, x > M, x < -M))

이고

(lim f(x) = ±∞ (x ⟶ a∓ ∈ ℝ))
 ↔ (∀M>0, ∃δ>0 s.t. (x ⟶̣ a∓ (by δ)) → (f(x) ⟶ ±∞ (by M)))
 ↔ (∀M>0, ∃δ>0 s.t. (x ⟶̣ a∓ (by δ)) → NOTATION(±1 = 1, x > M, x < -M))

이다.

이제, 실수에서의 유계를 정의하자.

UpperBound(x, S) : ∀t ∈ S, t ≤ x
LowerBound(x, S) : ∀t ∈ S, t ≥ x

UpperBoundSet(S) ≜ {x | UpperBound(x, S)}
LowerBoundSet(S) ≜ {x | LowerBound(x, S)}

BoundedAbove(S) : UpperBoundSet(S) ≠ ∅
BoundedBelow(S) : LowerBoundSet(S) ≠ ∅

LeastUpperBound(S) ≜ NOTATION(BoundedAbove(S) ? min UpperBoundSet(S) : ∞)
GreatestLowerBound ≜ NOTATION(BoundedBelow(S) ? max LowerBoundSet(S) : -∞)

sup S ≜ LeastUpperBound(S)
inf S ≜ GreatestLowerBound(S)

그리고 함수값의 상•하한은 다음으로 정의한다.

sup f(x) (Φ(x)) ≜ sup f[Φ]
inf f(x) (Φ(x)) ≜ inf f[Φ]

Mₒ(a) ≜ sup f(x) (x ⟶̣ a (by o))
mₒ(a) ≜ inf f(x) (x ⟶̣ a (by o))

lim sup f(x) (x → a) ≜ inf Mₒ(a) (o > 0)
lim inf f(x) (x → a) ≜ sup mₒ(a) (o > 0)

이렇세 상극한 하극한을 나무위키를 참고하여 정의하였다.

나무위키 ε-δ논법 해설을 참고하라.
극한을 배우는데 매우 유용하다.

참고로, 저 극한들이 동작하는 원리는 나무위키에 첨부된 Ray수학의 "극한을 정의하는 가장 세련된 방법"에서 그래프로 이해하자.

그게 제일 편하고 쉽다.

에초에 도약(jump) 불연속같은 개념이나 좌극한 우극한 같은 개념을 직관적으로 숙지해 두면, 수렴할때 극한의 유일성을 납득하는데 도움이 많이 된다.

한마디로 머릿속에 논리식과 그래프가 한번에 그려지고 죄다 설명된다.

뭐... 그런 직관은 이미 수II시간이나 미적분시간에 주입받았을테니까 문제없긴 한데...

지금까지 정의한 ×나많은 개념들이 이상하다고 느껴질수 있으니 초실수체로 직관를 잡는법도 있다.

입시에 쓰기에는 비효율적이지만 무한소식 사고방식이다.

나무위키 초실수체 문서의 ultrapower construction를 참고하라.

울트라곱을 이용했을때, 무한소가 되는 실수열의 특성과, 그것이 ε-δ랑 호환되는 꼴을 보아하면,
ε-δ가 만든 한계 오차의 개념이 얼마나 정신나간 개념인지 체감할 수 있는데,

이번에 정의한 `x ⟶̣ a` 및 `x ⟶ a` 개념이 좌극한 우극한 포함해서 어떻게 초실수로 옮겨지는지를 생각하면....

...

극한은 무한소가 한없이 0에 가까운 정신나간 특성을 가지는...

즉, x ⟶̣ 0 인 정신나간 성질을 이용하는 체계로써, 
실수 자체도 초유리수에서 초실수로 확장한걸 표준부분을 쓰지 않고서야 코시 수열로는 참으로 터무니없이 어렵고,
초실수체의 울트라곱 대수구조를 생각하면, 극한은 터무니없이 정신나간 체계이다.

설명을 마치며, 이번 "극한에 대하여"문단은, 

<Checklist>

 + [✅️] 0. 일단 이것부터 다 작성한 후
 + [☑️] 1. 초실수애 대한 설명추가 후,
 + [☑️] 2. "미분에 대하여"문단을 따로 만들고
 + [☑️] 3. 합쳐서
 + [☑️] 4. 내용을 전부 분할해서, 이 Lava설명 내부에 녹일것이다.

끝.

### 참고 함수

참고사항일 뿐이다...

뭐...

#### limer 함수 lime

limer [발음 : limmiter [리미터], limer [리머], 약칭 : lime] 함수 lime (limer는 너무 이름이 길어서 라임(lime)이 됨)

+ `lime ≜ ((st◦)◦lime*◦(st⁻¹◦))`
+ `lime* ≜ (◦(+ε))`

> 참고 : `lime(f) = ((st◦)◦lime*◦(st⁻¹◦))(f) = (st◦)(lime*((st⁻¹◦)(f))) = st◦lime*(st⁻¹◦f) = st◦lime*(f*) 이고, lime*(f*) = (◦(+ε))(f*) = f*◦(+ε)이며, (f*◦(+ε))(x) = f*((+ε)(x)) = f*(x + ε)이므로, lime(f) = st◦lime*(f*)이고, lime*(f*)(x) = f*(x + ε)이며 (st◦lime*(f*))(x) = st(lime*(f*)(x)) = st(lime*(f*(x))) = st(f*(x + ε)) = lim f(t) (t → x)에서, 당연히 lime(f)(x) = st◦lime*(f*) = lim f(t) (t → x)인, 즉 극한을 취해주는 함수임 (주의 함수st⁻¹(f) = f*는 그저 transfer원리를 통해 초실수로 확장하는 f*과정을 은유적으로 표현한것. 사실상 "g(f) = f*"인 g로 고쳐야함.)`

특징 : `점 불연속을 복원함, 초실수체에서 lime* f는 "불연속 이면이 도약 불연속"임. 진동의 경우에는 유한 초실수의 종류에 따라 구간에서의 선택이 달라지기에, 사실 "불연속 이면이 진동 혹은 도약 불연속"임. (극한이 논리적으로 aproximate하게되어 진행중인것처럼 취급되는지, 아니면 그 논법을 숫자로 압축시켰는지 차이로, 실수에서는 수가 무한까지 크게 잡아져있지 않고, 초실수는 무한이 있어서, 실수에서 무한으로 발산해서 끊어지는게 초실수에서는 안 끊어지는, 연속적 • 위상적 관점에 특징 때문에, 제거 가능한 불연속인 점 불연속 이외의 도약 불연속만이 유일한 후보가 되는 원리, 그리고 도약 불연속에서 좌극한과 우극한은 다름. 그러나 실수에서는 끊어져 버리기에 연속이 아님.), FOL에서는 d/dx f* = ((lime* f*) - f*)/ε 인 성질에 따라서, FOL에서, 미분에 활용 가능 (또 여기서 알수있는 특징이, f가 연속 이면이 ((lime* f*) - f*)/ε가 연속. (주의 : f는 실함수로, 가 점 불연속과 도약 불연속과 발산 불연속과 진동이 아닐때 연속이고, f*이 연속이어도, f가 연속이 아니면 이계도함수를 만들수 없을수 있음) 초실수 범위에서 발산불연속이 상쇠되기에 연속이면 미분가능.) (또한, (((lime* f*) - f*)/ε)(x) = ((lime* f*)(x) - f*(x))/ε = (f*(x + ε) - f*(x))/ε 으로써, x = 0에서 f*(0) = Ω = undefined이거나, x = ε일때 진동하여, ε의 종류마다 달라지거나, f*가 점 불연속일때도 제거해주지 않으면, 그 점에서 미분 불가능하므로, (lime* f*)의 도함수에서, 실함수 f의 모든 불연속점을 정의 불가능으로 새로 규정해줘야 f*의 도함수임)`

참고로, ε를 임의의 양의 무한소 혹은 임의의 음의 무한소로 제한하면, 일반화된 (lime*)으로 설정되며, 그렇지 아니한 경우, ε에 따라, (lime*)이 결정된다. 유일한 경우 정의되게 정의역을 한정하면, 다가함수가 아닌 제대로된 단가함수다. 그 경우를 "극한이 정의된다."고 한다.

이때,

1. Cⁿ f : Cⁿ⁻¹ f, Cⁿ⁻¹ f ⊨ C ((dⁿ⁻¹ f)/(d xⁿ⁻¹))
2. C¹ f : C f : ∃! dy/dx = (df/dx)(x) = st((((lime* f) - f)/ε)(x)) (단. ε는 임의의 0이 아닌 모든 무한소이다)

로 제귀적으로 정의되고, 미분이 저런건 당연한거라서 뭐... 할말이 없지만...

#### 부록 : 혼자 만든 극한 이해 시스템

1. Endofunctor Type System

````markdown
# 엔도펑터 타입 시스템 - 추상화 Ver

이전에 내가 정의한 엔도펑터 타입 시스템을 조금 추상화해봤다.

## first / last / reverse / hold 연산

튜플에 제귀적 정의 `(x, ⋯) := (x, (⋯))`에 따라서, dom reversed = {x | dim x ≥ 2} 이다.

first(x, y) = x
last(x, y) = y

reverse(x) = (last(x), firsr(x))
i.e. reverse(x, y) = (y, x)

hold = reverse²
i.e. hold(x, y) = (x, y)

(∈ ker (dim - 1) ∪ ker dim)(x) : ¬(∈ dom reverse)

pf.

ker (dim - 1))
 = {x | (dim - 1)(x) = 0}
 = {x | dim(x) - 1 = 0}
 = {x | dim(x) = 1}

ker dim
 = {x | dim x = 0}

ker (dim - 1) ∪ ker dim
 = {x | dim x = 1 ∨ dim x = 0}

dom reverse
 = {x | dim x ≥ 2}

## concat 연산

1. concat(x, y) = hold(x, y) (단. dim x = 1)
2. concat(x, y) = first(x) `concat` (last(x) `concat` y) (단. dim x ≠ 1)

반군을 이룬다. 자유모노이드의 붙여쓰기 연산자기 때문이다.

## len 연산

0. InnerProductSpace(<(len² x) ⊗ ℝ, +, ×, <•|•>>), dim len² x) ⊗ ℝ = 1 (단. ×는 스칼라배, +는 벡터 합, <•|•>는 bra-cket 내적, (len² x)는 정규직교기저)
1. lenⁿ x = len² x (단. n > 1)
2. card ker len = 1, ker len = {HaskellNullModelConstant}
3. dim x = 1 ↔ len x = len²(x)
4. lentwo ≜ len²(HaskellNullModelConstant)
5. len HaskellNullModelConstant = 0 lentwo
6. len x = (dim x)lentwo
7. len x[:L lentwo] = L lentwo
8. len x[::-1] = len x
9. len concat(x, y) = len x + len y
10. lentwoⁿ = lentwo

## [::-1]함자

1. x[::-1] = x[len x] `concat` x[:len x][::-1] (dim x > 1)
2. x[::-1] = x (dim x < 2)

## [::y]함자와 x[::y]연산, [:y]함자와 x[:y]연산, x[y:]연산과, [y:]함자, x[y]연산과, [y]함자.

1. [:: i j lentwo] = [:: i lentwo][:: j lentwo]
2. [:: x][:: y] = [:: y] ◦ [:: x]
3. [: x][: y] = [: y] ◦ [: x]
4. [x :][y :] = [y :] ◦ [x :]
5. x[y :] = [::-1][: len(x) - y][::-1]
6. x[: 0] = HaskellNullModelConstant
7. x[y :][z :] = x[y + z :]
8. x[::1] = x
9. [::0] = [: 0]
10. [: 0][:: y] = [: 0]
11. x[:: y] = x[0] `concat` x[y :][::y]
12. concat(x, y)[: len x] = x
13. concat(x, y)[len x :] = y
14. [x] = [x:][:lentwo] = [:x + lentwo][0:]
15. [:: x][y] = [xy]
16. x[len x - lentwo] = last^{<lentwo | len x - lentwo>}(x) lentwo (즉, (<lento |)(v) = ||v|| = 이고, <lento | x lento> = x이므로, <lentwo | len x - lentwo> = dim x - 1)
17. x[0 lentwo] = first(x) lentwo
18. x[lentwo:] = last(x)
19. x[y] = x[lentwo:][y - lentwo]
20. x[n lentwo : ] = lastⁿ(x)
21. x[n lentwo] = first(lastⁿ(x)) lentwo (n < dim x - 1)
32. Param(concat)ᵢ₌ₐᵇ x = x[a:b] (코멘트 : python의 str이 갑자기 문자셋에 숫자가 추가된 느낌 wwwwwww perl마냥 ㅋㅋㅋ)
33. [x : y] = [: y][x :] = [x :][: y - x]
34. [x : x + lentwo] = [x]

## HLON(Haskell-Like Operator Notation) : 내가 만든 웃긴 노테이션

Definition)

```HLON
0. Param(f)ᵢ₌ₐᵇ termᵢ = Param(f)(Param(concat)ᵢ₌ₐᵇ termᵢ)
1. ∀f(x) = `x`, f(f(x)) = x
2. ∀f : X × Y ↦ Z, x `f` y = f(x, y)
3. ∀g(f, x)ᵢ = (`f` xᵢ), (Param(`◦`)ᵢ₌₀ⁿ⁻¹ g(f, x)ᵢ)(y) = f(concat(y, Param(`◦`)ᵢ₌₀ⁿ⁻¹ x))
```

예컨데,
 + x ``?`` y ``:`` z = x ? y : z 이며
 + (x ?)(y : z) = (:z)(x ? y) = (x ? • : z)(y) = x ? y : z 이고
 + (? y) = (y :) = (? y :) 이며
 +  (? y :)(x, z) = x ? y : z 이고,
 + (x ? • : •) = (x ?:) 이며
 + (• ? x : •) = (? x : ) 이며
 + (• ? • : x) = (?: x) 이다.
 + 아예, (`? `◦`:`)(x, y, z) = x?y:z 다.
 + x `(`? `◦`:`)` y (`? `◦`:`) z = x?y:z 라고까지 볼수 있다.

그렇다. 이건 결과적으로,

a `f` ⋯ `f` z = f(a, ⋯, z) 따위를 구현 가능하게 해준다.

### 주의사항

`f`는 객체(object)다. 클래스는 ∀g(f) = `f`인 g가 클래스가 된다.

## TOS(Top Of Stack) 연산자

TOS는 TOSC (TOS-Core)를 통해 작동하는데,

∀dim dom f < 2, `TOSC`(concat(⋯, f)) = f(⋯) (단. ⋯는 비어있을수 있다. 길이는 0이나 1이다)
∀dim dom f > 1, x TOSC f = (TOSC (`x` f))

(TOS f) ≜ (TOSC f◦[::-1])

그래서 작동은 어떻게 하냐?

a ⋯ x y z TOSC f
 = a ⋯ x y TOSC (z `f`)
 = a ⋯ x TOS (y `(z `f`)`)
 = a ⋯ x TOS (z `f` y `f`)
 = ...
 = f(z, ⋯, a) 이다.

HOLN에 따르면, f가 n항연산이면, `(z `f`)`는 n - 1항 연산이다.

그건 펙트다.

TOSC f◦[::-1]는 그저, 인자를 거꾸로 받는 버전일 뿐.

RevTOS는 TOS의 역연산이고, RevTOSC는 TOSC의 역연산이다. 각각, 후위 연산자를 받아서 전위 연산으로 변형한다.

## 삼항연산자 표기법

x?y:z ≜ $\begin{cases} y, & (x), \ z, & (¬x) \end{cased}$

## 수량자 표기법

0. S⁽ⁿ⁺¹⁾ ≜ Sⁿ × S¹ (단. S² ≜ S × S)
1. 클레이니 스타 쓴다.
2. S? ≜ S°¹°
3. S+ ≜ S × S*
4. S* ≜ S+? 로 재정의되었다.
5. S°ⁿ° ≜ S* ∩ {v | dim v ≤ n} ≜ (n=0)?HaskellNullModelDomain:((n=1)?S∪S°⁰°:S°ⁿ⁻¹°∪Sⁿ)

## HaskellNullModel 상수

1. HaskellNullModelConstant ≜ first(HaskellNullModel) ≜ ε ≜ ()
2. HaskellNullModelDomain ≜ last(HaskellNullModel) ≜ S°⁰° ≜ {HaskellNullModelConstant}
3. HaskellNullModel ≜ <HaskellNullModelDomain, HaskellNullModelConstant>

그렇다. 그냥 평범한 공튜플이다.

## int함수와 bool술어

함자 (?1:0) : 𝔹 ↦ {0, 1} 에 대해,
int ≜ (?1:0)

bool ≜ last(<{0, 1}, bool>) ≜ int⁻¹ ≜ {1} ≜ (=1) ≜ (≠ 0) s.t. bool(x) : 1 = x ≠ 0

## 이항연산으로써의 함수 합성

dom f◦g ≜ dom g
codom f◦g ≜ codom f
graph f◦g ≜ (`graph f` εu `graph g`)

이항 관계에 대한 HLON에 따라서,

(graph f◦g)(x, y)
 = (`graph f` εu `graph g`)(x, y)
 = x `{`graph f` εu `graph g`}` y
 = x `graph f` εu `graph g` y

즉,

x `graph f◦g` y : ∃u, x `graph f` u `graph g` y

이다.

## 이항관계에 대한 HLON

<D, R>에 대해, R ⊆ Dⁿ이면,

R : Dⁿ ↦ 𝔹 이다.

pf.

R = bool◦int◦R

그런데, int◦R : Dⁿ ↦ {0, 1}

Q.E.D.

## Param 시스템

Definition)
1. ∀Antigroup(<S, f>), Param <S, f> ≜ <S × S+, Param f)
2. (x `Param f`)(y) ≜ (x `f`)((Param f)^{int(dim y ≠ 1)}(y))

## My Endofunctor Type System : 내가 만든 웃긴 타입 시스템

ET = EndofunctorType

T EndofunctorType v ≜ (dom (T EndofunctorType v), codom (T EndofunctorType v), graph (T EndofunctorType v)) ≜ (HaskellNullModelDomain, T, HaskellNullModelDomain × {v})
(단. (T EndofunctorType) = (dom (T EndofunctorType), codom (T EndofunctorType), graph (T EndofunctorType)) = (T, Func(HaskellNullModelDomain, T), {(v, (HaskellNullModelDomain, T, HaskellNullModelDomain × {v}) | v ∈ T}))

이항관계 ``::``를 다음과 같이 정의한다.

(v :: T) : (v ∈ (T EndofunctorType)[dom (T EndofunctorType)])

(T EndofunctorType)의 치역이 (T EndofunctorType)[dom (T EndofunctorType)]니까 말 다했다.

## 합타입

(x :: (T | G)) : (x :: T) ∨ (x :: G)

누구나 알수 있듯, 이항관계 ``::``를 확장하여,

(x :: T | G) : (x :: T) ∨ (x :: G)

식의 삼항관계를 만들었고, 

(T | G)는 HLON으로 정의된 함자 객체인 셈이다.

HLON에서만 펙트다.

### 주의사항

(T | G)도 결국 타입생성자 ``|``를 통해 조합되는 객체다.

## 곱타입

곱타입은 세미콜론 ``;`` 타입생성자를 통해서 작성된다.

(RevTOS ``;``)(T, v) 는 길이-1 곱타입

(RevTOS ``;``)(T, v) (RevTOS ``;``)(T, v) 는 길이 - 2 곱타입이다.

(RevTOS ``;``)(T, v) (RevTOS ``;``)(T, v) = (RevTOS ``;``)(T, v) × (RevTOS ``;``)(T, v)이다. 곱셈이 정의된 객체(Object)다.

당연히
Πᵢ₌₀ⁿ (RevTOS ``;``)(Tᵢ, vᵢ) ≜ (RevTOS ``;``)(T₀, v₀) × Πᵢ₌₁ⁿ (RevTOS ``;``)(Tᵢ, vᵢ)

인데,

(RevTOS ``;``)(T₀, v₀) × Πᵢ₌₁ⁿ (RevTOS ``;``)(Tᵢ, vᵢ) ≜ (RevTOS ``;``)(T₀, v₀) × (RevTOS ``;``)(Πᵢ₌₁ⁿ (RevTOS ``;``)(Tᵢ, vᵢ), ŷ)

이며,

(RevTOS ``;``)(T₀, v₀) × (RevTOS ``;``)(T₁, v₁)는

<(RevTOS ``;``)(T₀, v₀) × (RevTOS ``;``)(T₁, v₁) | T₀ | T₁, v₀, v₁>이라는 연산을 이루는데,

x성분 x̂, y성분 ŷ에 대해,
v :: ((RevTOS ``;``)(T, v) dom; T codom; dom v × codom v graph)
x :: (RevTOS ``;``)(T, v)
v(x) ≜ <x̂ | x()>

NOTE : x가 Endofunctor type객체면, 무조건 ()를 이용해야하는게 당연한거다. x의 값은, 항상 x()다.

v₀ :: ((RevTOS ``;``)(T₀, v₀) × (RevTOS ``;``)(T₁, v₁) dom; T codom; dom v₀ × codom v₀ graph)
x :: (RevTOS ``;``)(T, v₀)
v₀(x) ≜ <x̂ | x()>

NOTE : x가 Endofunctor type객체면, 무조건 ()를 이용해야하는게 당연한거다. x의 값은, 항상 x()다.

v₁ :: ((RevTOS ``;``)(T₀, v₀) × (RevTOS ``;``)(T₁, v₁) dom; T codom; dom v₁ × codom v₁ graph)
x :: (RevTOS ``;``)(T, v₁)
v₁(x) ≜ <ŷ | x()> 로 정의되며,

NOTE : x가 Endofunctor type객체면, 무조건 ()를 이용해야하는게 당연한거다. x의 값은, 항상 x()다.

vᵢ :: ((RevTOS ``;``)(T₀, v₀) × (RevTOS ``;``)(Πᵢ₌₁ⁿ (RevTOS ``;``)(Tᵢ, vᵢ), ŷ) dom, Tᵢ codom, dom vᵢ × codom vᵢ graph)
x :: (RevTOS ``;``)(T₀, v₀) × (RevTOS ``;``)(Πᵢ₌₁ⁿ (RevTOS ``;``)(Tᵢ, vᵢ), ŷ)
vᵢ(x) ≜ vᵢ(ŷ(x)) 로 정의된다.

그래서, Haskell의 곱타입마냥 저딴 어트리뷰트 사용법마냥 사용 가능하게 정의되었다.

이것도 합타입처럼, 객체-클래스-메타클래스 구조다.

### 주의사항

객체-클래스-메타클래스 구조이긴 한데...

```
x :: 곱타입
```

식으로 선언해주었다면, x()가 그 객체다.

NOTE : 이전 노트에서 곱타입에 굳이 엔도펑터 호출식을 적은 이유가 바로 그러한 이유에서다.

### 생성자

```
Πᵢ₌₀ⁿ (RevTOS ``;``)(Tᵢ, vᵢ) ET (Param(concat)ᵢ₌₀ⁿ Tᵢ ET wᵢ)
```

식으로, 튜플을 해당 타입으로 초기화가 가능하다.

Initialize-Notation으로,

```
Πᵢ₌₀ⁿ (RevTOS ``;``)(Tᵢ, vᵢ) ET (Param(concat)ᵢ₌₀ⁿ vᵢ = wᵢ)
```

로도 적을수 있다.

## 멱집합 타입

P(X) = 2^X = {S | S ⊆ X}로 집합명 만들고 생성하는게 설마 어려울리가 없겠지

## 함수 타입

(X -> Y) ≜ (X dom; Y codom; P(X × Y) graph;)
라고 정의하겠다.

ㅋㅋㅋ 에초에 함수가 튜플이라 かんぺき한 정의다 ㅋㅋ

## 결론적으로 모든 타입을 모으자면

술어 iset = isET가 합타입 • 곱타입 • ET타입으로 이루어진 타입을 이르는 명칭이다.

## 지네릭 타입

X :: ETemplate(iset*, codom, graph)인 사실상 함수 타입인데,

X<⋯>식으로 작성한다.

그렇다. 이건 그저 Notation일 뿐.

Notation은 Notation인데, 타입을 객체로 취급해주는 레벨인거다.

## tuplic-definion (Notation)

tuplic-definion (Notation)이란, 함수를 "(dom = X, codom = Y, graph f)(⋯) ≜ ~"스타일로 엄밀하게 한줄로 정의하는 표기법(Notation)이다.

당연히, 곱타입 명시도 아니고서, 저런식으로 작성을 할수가 없고, graph f는 심지어 타입 초기화가 아닌 f라는 심볼의 타입을 알지 않고서야, 유효하지 않을수 있다. 다만, 그렇기에, 해당 구문에 해당하는 기의가 없었기에, 표기법 (Notation)용도로 사용한것이다.

한마디로

표기

```
(dom = X, codom = Y, graph f)(⋯) ≜ ~
```

를

```
f :: X -> Y
f(⋯) ≜ ~
```

로 정의하는 표기법 (Notaion)이다.

이 최강의 표기법을 얻고싶어서 이지랄을 떨었던거다.

앞으로는, "(dom = X, codom = Y, graph f)(⋯) ≜ ~"식으로 함수 f를 정의할 생각이다.

## 주의사항

타입 시스템이라는 말이 프로그래밍에 주로 쓰여서 오해를 방지하기 위해 한가지 명시하겟다.

이건 수학용 타입 시스템이다. 뭣같은 코딩이 아니고.

## 참고사항

### 추상화 이전 버전

#### 엔도펑터 타입 시스템

나는 지난 고2때 배운 수 II를 정리하다, 문득 내가 요즘 탐구하고 있는, 연산자의 Haskell식 표현이나, 문법 compile함수의 특성, 그리고, 연산 법칙의 문법규칙화를 통해서, AC와 엔도펑터를 이용한, 타입 시스템을 만들수 있고, 이는 극한점의 타입을, 함수의 그래프로 사용하는데 유용하다는걸 알게 되었다

요약 : 이 글은, v on f : (v :: graph f)라는 이항관계, on을 정의하고 싶어서 만든것이기도 하며, 우연히 발견한 구조에 대한 노트다.

모노이드 <L, e, f>에 대하여, 자유모노이드 <L*, ε, .>는 모노이드 <L, e, f>의 도메인 L을 charset(문자셋), 즉 언어로 하는 문자열의 집합 L*을 도메인으로 하는 문자열 concat의 모노이드다. 앞으로 문자열 L"⋯"라고 적는다면, "⋯"는 언어 L의 문자열인것으로 하겠다.
형식문법 G = <N, Σ, P, S>가 생성하는 언어 L(G)를 자유 모노이드 L(G) = <L*, ε, L(G).compile, .>라고 하겠다. 언어 L에서의 문법적 동치는, 문법적 동치류 L(G).same(y) = {x | L(G).compile(x) = L(G).compile(y)}를 동치류로 가지는 동치관계다.
반군 <S, f>에 대하여, 유사-Haskell식 중위표기법 x `g` ⋯ `g` y = g(x, ⋯, y)는 f에 대해, (x `f` y) = f(x, y)로 중위표기를 가능하게 하여, 함자로 표기하기 용이하게 한다.
Plus <L, f> = <L+, Plus f>이며, L+ = L × L*이다.
(x `Plus f`)(y) = (x `f`)({Plus f}^{int(dim y ≠ 1)}(y))로 귀납적으로 정의된다.
왜냐하면, y는 카데시안 곱으로 된 집합 L+의 원소고, L* = (L+)?으로, L? = L⁰ ∪ L¹로 정의되어있고, 이는, dim이 1 이상인 튜플이며, 해당 튜플은 튜플의 제귀적 정의에 따라서, (x, ⋯) := (x, (⋯))로 작성되어있기 때문이다. 에초에 다변수 함수의 입력도 튜플이다.
카데시안 곱으로 된 서로다른 벡터공간들의 합집합과, 클래이니 스타로 된 문자열과 튜플의 집합을 튜플로 취급하는 이유는, 결국 그것들이 튜플로 이루어졌기 때문이다. ZFC의 문법 G_{ZFC}에 대해, ZFC의 기표 언어 L_{ZFC}는 대수구조 L_{ZFC}(G_{ZFC})로 그 형식적 작동을 설명할수 있으며, L_{ZFC}(G_{ZFC}).compile의 결과가 동일하면, 동일한 대상이기 때문에, 같게 취급하는거다. 형식이 전부다. 나머지는 없다. 있다고 단정할수 없다. 그러나, 우리는 직관적으로 없는걸 해석할때가 많은것 뿐이다. (형식을 직관화하는것과, 직관을 형식화하는것 중에, 직관을 형식화하는것만 가능하고, 형식을 직관화하는건, 일개 자연어적 해석일 뿐이지, 해당 형식언어에서는 L(G).compile이 작동하는 사실과 무관한 해석이 되는거다.)
Definition)
1. 정의용 제 1 규칙 : 모델 Plus <S, f>의 모델론적 언어 L에 대하여, 해당 언어 L의 변수문자와 상수문자와 쉼표로 구성된 문자열 k, v에 대해, L"(Plus f)(⋯, " . k . L", y) = (Plus f)(⋯, " . v . L", y)"인 경우, 모델 Star <S, f> = <S*, Star f>의 모델론적 언어 N에 대하여, N"(Star f)(" . k . ") = (Star f)(" . v . ")"이다.
2. 정의용 제 2 규칙 : (Star f)(v) = (Plus f)(v)이다.
이로써, Star를 정의했는데, 사실, Star는 멱등법칙을 만족하는 반군이나, 모노이드에서나 정의된다. 그 이유를 말해보자면,
(Plus f)(⋯, x, x, y) = (Plus f)(⋯, x, y)이거나 (Plus f)(⋯, x, e, y) = (Plus f)(⋯, x, y)이여야,
(Star f)(x, x) = Star(x) = x이거나, (Star f)(x, e) = x로, Plus f연산의 인자 수를 줄이는 연산으로 타당하기 때문이다.
가환 반군의 경우, Star의 인자는 무순서 튜플이라, 사실상 중복집합과 다를바가 없고, 멱등 반군(멱등법칙을 만족시키는 반군을 줄인 내가만든 줄임말)은, 축약시 인자가 연속될일이 없다.
그러므로, 가환 멱등 반군의 경우, 인자가 집합과 다를바게 없게 된다 
다를바가 없다는건 비유적 표현이지. 동형이라는게 더 맞는말인것 같다.

그래서, 멱등 반군이나 모노이드가 아니면, L × L+여야 하고... 아 그렇네 ㅋㅋ 지금까지 내 정의가 조금 망ㅎ이 잘못됬다 암튼. (Param을 L × L+로, Plus를 L+로, Star를 L*로 다시 대응시켜야겠네...)
멱등 반군이나 모노이드는 L*로.
모노이드의 경우, 항등원 e에 대해 규칙 (Star f)(⋯, e) = (Star f)(⋯)가 문법규칙마냥 적용되므로, (Star f)() = (Star f)(e) = Star(e, e) = e로, 정의역을 L⁰으로 제한하면, 프로그래밍할때 많이 쓰이고, 나도 자주 쓰는 그 엔도펑터가 되는데, 막상 공역은 한번도 제한되거나 확장된적이 없어서, 공역은 f의 domain인 L이 된다.

이번엔, Star와 유사한데, FSM버전으로 바꾼 Star로,
L°⁰° = L⁰
L°ⁿ° = (L × L°⁽ⁿ ⁻ ¹⁾)? (n ≠ 0)
로 정의된 L°ⁿ°에 대해,
Starₙ f = {(Star f)|}_{L°ⁿ°}
Starₙ <L*, ε, Star f, .> = <L°ⁿ°, ε, Starₙ f, .>
Starₙ <L, e, f> = Starₙ <L*, ε, Star f, .>

즉,

Star₀ <L, e, f> = Star₀ <L*, ε, Star f, .> = <L⁰, ε, Star₀ f, .>
이고, L⁰ = {ε}이다.

그리고, 다음을 정의하겠다.
RET = ReversibleET = ReversibleEndofunctorType s.t. ReversibleEndofunctorType <L, e, f> = Star₀ <L, e, f>
RET <{ε}, ε, Star₀ f, .> = Star₀ f
CET = CoreofET = CoreofEndofunctorType s.t. CET Star₀ f = codom Star₀ f
ET = EndofunctorType
(y = RET x or y = CET x) ifi (y = ET x)
라고 정의하겠다.
또한,
(x :: T) : (x() ∈ T)
라 정의한다
이것이, 엔도펑터 타입 시스템.
선택함수 choose에 대하여, T ET choose = <T, choose(T), f>라는 모노이드를 반환한다.
엔도펑터 타입 시스템은, AC가 보장되어야, 임의의 집합 T에 대해서, T ET choose가 잘 정의되기 때문에, AC가 필요하며, 해당 모노이드를 다룸에 있어서, 엔도펑터와 동형인 형식적 작동이 존재하기에,

ET ({()}, (), x, ({()}², {()}, {()})) = x로 간단히 대수적인 의미의 대상으로 포메팅되기도 하며, 사실상, 문자열 format마냥 당연하게 일대일대응이다.
엔도펑터 자체로도 ET x = T이고, x()가 값이고, x() ∈ ET x라서, 타입 시스템도 된다.
또한 사용함에 있어서, C++의 스마트포인터가 lock해제로 접근하듯, 여기도 이러한 방식을 활용하여, 편리한 사용도 가능한것 같아서, 개인적으로 뿌듯하다.

T ET choose = T ET choose(T) 이며,
T ET x = <T, x, f>인 모노이드로 정의된다고 해두겠다.

이상으로, EndofunctorTypesystem의 정의를 마친다.
````

### 성질 목록

아래 술어들은, Lava M 혹은 특별한 대상 M에 대해, 

M ⊨ Φ : "M이 성질 Φ를 만족한다"

라고 하는 술어 Φ들이고, 성질이라고 부른다.

사실 술어랍시고 써놨는데

1. 죄다 자유변항만있고, 종속변항은 없는것은 "참성질"이라고 부르고, 걍 사실상 문장명명이다.
2. 자유변항이 존재하고, 종속변항도 존재하는것을, "가성질"이라거 부르고 걍 사실상 술어다.

참성질과 가성질의 `참-`, `가-`는 참다랑어와 가다랑어에서 따왔다.

참성질을 법칙성질, 가성질을 성질부분이라고도 한다. (이것도 근데 방금 만든 조어다)

~배고프니까 천장에서 다랑어가 쏳아졌으면 좋겠다~

참고로 특별한 대상 M에 대해 다루는 경우는 `특-`을 붙여서 "특성질"라고 한다. 왜냐하면 이 특별한 대상은 "대수구조가 아니라 집합이나 순서쌍 혹은 함수다"

#### 결합법칙 (associative property)

결합법칙 Associative는 다음과 같은 법칙성질(참성질)이다.

Associative : "(a * b) * c = a * (b * c)"

#### 중가환 법칙 (medial property)

중가환 법칙 Medial은 다음과 같은 법칙성질(참성질)이다.

Medial : "(m * n) * (p * q) = (m * p) * (n * q)"

#### 교환법칙 (commutative property), 혹은 가환(commutative)

교환법칙 Commutative는 다음과 같은 법칙성질(참성질)이다.

Commutative : "a * b = b * a"

#### 좌역원임-가술어 (tunal is-leftinvers-of Predicate)

좌역원임-가술어 tunalIsLeftinversOf는 내가 방금전에 명명한 가성질이다.

가술어를 tunal 서술어를 붙이는 이유는 tunna-al (다랑어-적)이라는 뜻으로 가술어임을 말하기 위해서다. 이유는 가성질 • 참성칠 명명 유래 참고.

tunalIsLeftinversOf(e, b, a) : "b * a = e"

e = eₗ으로 대입해서 생각한다면, 좌항등원이 항등원인 좌역원임-가술어라고 하며, e = eᵣ이면 우항등원이 항등원인 좌항등원-가술어라고 한다.

해당사항은 하단의 우역원임-가술어에서도 통용된다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 우역원임-가술어 (tunal is-rightinvers-of Predicate)

우역원임-가술어 tunalIsRightinversOf는 내가 방금전에 명명한 가성질이다.

tunalIsRightinversOf(e, b, a) : "a * b = e"

#### 좌역원임-술어 (is-leftinverse-of Predicate)

좌역원임-술어 isLeftinverseOf는 내가 방금전에 명명한 가성질이다.

b isLeftinverseOf a : isLeftinverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsLeftinverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 좌역원임-가술어이다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 우역원임-술어 (is-rightinverse-of Predicate)

우역원임-술어 isRightinverseOf는 내가 방금전에 명명한 기성질이다.

b isRightinverseOf a : isRightinverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsRightinverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 우역원임-가술어이다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 역원임-가술어 (tunal is-inverse-of Predicate)

역원임-가술어 tunalIsInverseOf는 내가 방금전에 명명한 가성질이다.

tunalIsInverseOf(e, a, b) : tunalIsLeftinversOf(e, a, b), tunalIsRightinversOf(e, a, b)

로, 좌역원임-가술어와 우역원임-가술어를 모두 만족시키는, 즉, 역원인 경우로써,

이경우도 e에 따라, 항등원이 좌/우 항등원인 역원임-가술어로 말할 수 있다.

### 역원임-술어(is-inverse-of Predicate)

역원임-술어 isInverseOf는 내가 방금전에 명명한 가성질이다.

b isInverseOf a : isInverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsInverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 역원임-가술어이다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 가역원임-가술어 (tunal checking-does-it invertible-element Predicate)

가역원임 가술어 isInvertibleAs는 방금전에 내가 만든 가성질로,

역원 판별논리식 Φ에 대해,

x isInvertibleAs Φ : isInvertibleAs(x, Φ) : ∃y s.t. Φ(x, y)

인 isInvertibleAs로, FOL에서는 술어가 아닌 성질꼴로, 여러가지 성질의 접두사로 동작하며, 그 경우 Φ과 isInvertibleAs를 붙여쓴다.

그러나 권장사항은 SOL에서의 사용이다.

왜냐하면, 내가 FOL로 만들기 디껍고 귀찮기 때문이다.

다만 한가지 주의하기 위해 참고할 점은, ∃y라는 y는 해당 구조의 도메인 위에 있어야 하므로, 닫혀있는 원소인 조건이라는것이고, 따라서, 구조위에서의 의미해석을 해야함에 주의하자.

#### 가역원임-술어 (checking-does-it invertible-element Predicate)

가역원임 술어 isInvertible는 방금전에 내가 만든 가성질로,

x isInvertible : isInvertible(x)

이며,

isInvertible : isInvertibleAs isInverseOf

로써,

x = y, y = z, x = z에서

x isInvertible : isInvertible(x) : x isInvertibleAs isInverseOf : isInvertibleAs(x, isInverseOf)

인 isInvertible로, isInverseOf조건의 isInvertibleAs로 볼수 있으며,

가역원인지 확인하는 술어이다.

#### 전가역성 (Entire-Invertiblity)

전가역성 EntireInvertiblity는 내가 방금전에 만든 참성질 개념으로, "모든 원소가 가역원"을 말하기 귀찮아, 귀차니즘히 심히 많이 도져 귀찮고 괴로워서, 만든 개념이다.

EntireInvertiblity : "x isInvertible"

로써, 모든 x에 대해서 isInvertible인 일반명제임을 술어 Commutative과 같은 경우로 표기했다는 사실로써 능히 알 수 있다.

#### 전사성 특성질 (Surject, 전사성)

전사성 Surject는 치역과 공역이 같은 성질을 말하며,

Surject(f) : codom f = f[dom f]

로써, 모든 정의역 dom f에 대한 상 f,

즉, 치역 Y가 Y = 공역인 경우다.

#### 단사성 특성질 (Inject, 단사성)

단사성 Inject는 정의역과 치역이 일대일로 대응되는 성질을 말하며,

Inject(f) : ∀x, y ∈ dom f, f(x) = f(y) → x = y

로써,

함수 f는 항상 ∀x, y ∈ dom f, x = y → f(x) = f(y)이기에,

Inject(f) ↔ (∀x, y ∈ dom f, x = y ↔ f(x) = f(y))이다.

즉, graph f에서, y값에 대해 x값이 유일하다.

단사성을 만족시키는 함수를 일대일함수라고 한다.

#### 전단사성 특성질 (Biject, 전단사성)

전단사성 Biject는 정의역에 대해 공역이 하나도 빠짐없이 일대일로 대응되는 성질을 말하며, 

모든 공역에 대해 정의역이 하나도 빠짐없이 대응되고,

Biject : Surject, Inject

이다.

즉, 전사이며 단사인것이 전단사다.

전단사성을 만족시키는 함수를 일대일대응이라고 한다.

#### 왼쪽 함자 전단사성 (BijectiveLeftFunctor)

왼쪽 힘자 전단사상이란, 다음과 같은 법칙성질이다.

BijectiveLeftFunctor : "Biject((x *))"

말 그대로 왼쪽 함자가 전단사임을 말하는거다.
참고로, 저기서는 모든 x이 대한 왼쪽 함자이다.
쌍따옴표가 있으니, sentence로써 작동하는것이다.

#### 오른쪽 함자 전단사성 (BijectiveRightFunctor)

오른쪽 힘자 전단사상이란, 다음과 같은 법칙성질이다.

BijectiveRightFunctor : "Biject((* x))"

말 그대로 오른쪽 함자가 전단사임을 말하는거다.
참고로, 저기서는 모든 x에 대한 오른쪽 함자이다.
쌍따옴표가 있으니, sentence로써 작동하는것이다.

### 초실수상 수렴 (convergenceOfℝ*)

초실수상의 수렴은 발산하더라도 무한대로써 유한초실수가 아닌 초실수로 수렴하므로, 도약(jump)하는 경우가 유일한 수렴이 아닌 경우다.

convergenceOfℝ* : "f*(x - ε) = f*(x + ε)"

참고로, 발산이나 진동의 경우에는 모든 양의 무한소ε에 대해 값이 일정하지 아니한 경우이다.

다가함수가 아니려면, 함숫값이 유일하게 결정되야하므로, 자세한건 함수 사용전에 어떻게 범위를 설정하는지에 달렸다.

#₩# 연속 (continuous)

연속 (continuous)이란, 함숫값과 극한값이 같음을 말한다

continuous : (lime f)(x) = f(x)

등호도 관계이므로, 함숫값과 극한값이 정의되어야(다른말로 "x = y ⊨ ∃x, ∃y" 등호 관계가 성립함음 그 대상이 존재해야하는 경우가 전제되기에, 귀결이다, 그 역은 x ≠ y를 만족하는 경우로 부등호 관계도 존재를 전제하기에 아님.) , 등호의 동등관계가 작동한다.

### 연산 목록

#### 왼쪽 역연산 (LeftInverse)

왼쪽 역연산 LeftInverse은

x LeftInverseOf(`*`) y ≜ (x `*`)⁻¹(y)

으로, 왼쪽 연산에 대한 역연산으로,

역함수가 존재할 조건인 일대일대응일것임을 만족하기위해

왼쪽 함자 전단사성을 만족시켜야 한다.

#### 오른쪽 역연산 (RightInverse)

오른쪽 역연산 RightInverse은

x RightInverseOf(`*`) y ≜ (`*` y)⁻¹(x)

으로, 오른쪽 연산에 대한 역연산으로,

역함수가 존재할 조건인 일대일대응일것임을 만족하기위해

오른쪽 함자 전단사성을 만족시켜야 한다.

### 관계 목록

n항 관계 Φ는 집합 D에 대해, Φ ⊆ Dⁿ이다.

술어 Φ는 집합 D에 대해, Φ ⊆ D이다.

즉, 술어는 단항관계이다.

술어 Φ가 집합 S에 대해, Φ ⊆ S일때,

S = Dⁿ이면 Φ는 n항관계이다.

그렇다. 나는 관계와 술어에 구분을 두지 않을것이고,

따라서, 관계는 나에게 그저 튜플이 만족시키는 술어일 뿐이라는거다.

아래 관계들은, FunctionalRelationship을 이용하여, 이루어지는 관계들에 대해 다룬다.

FunctionalRelationship이란

FunctionalRelationship(f, P, Q) : f[P] = Q

인 술어로, P에 대한 f의 상이 Q인 관계이다.

즉, (∃f, FunctionalRelationship(f, P, Q)) ⊨ R을 만족시키는 R들이다.

(참고 : 앞으로, "학부 수준의 통상적 대수구조에서의~"가 붙을 말은, 에초에 학부 수준을 넘어서 범주론까지 설명하는건 뇌절이라고 보고, 대화 맥락과 주제가 "학부 수준의 통상적 대수구조에서의~"를 전제로 하는 경우를 대부분으로 하여 서술하고싶기에, "다루고자 하는~"이라고 하겠다.

#### 등수관계 (equinumous)

등수관계 equinumous란,

P equinumous Q : (∃FunctionalRelationship(f, P, Q))(Biject(f))

인 관계로, P에서 Q로가는 일대일대응이 존재하는 관계이다.

P equinumous Q ↔ card P = card Q이다.

#### 준동형 (Homomorphism)

준동형 Homomorphism이란, 대게의 경우에는 다음을 만족한다.

Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`) Homomorphism Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`) : (∃FunctionalRelationship(f, P, Q))(homomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)) [i := card P][j := card Q]

저건 P와 Q사이의 준동형사상 f가 존재하는 관계이다.

<br>

준동형사상 homomorphism은

homomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)) : dom f = P, codom f = Q, (∀x, y ∈ dom f, f(x `*` y) = f(x) `◦` f(y)) [i := card P][j := card Q]

이다.

<br>

마그마 이상을 이루는 P, Q에 대해, P에서 Q로 가는 사상 f가 (에초에 처음부터 함수인지 뭔지 제안하거나 명시하지 않았었음) 각각의 연산 `*`, `◦`에 대해, f(x `*` y) = f(x) `◦` f(y)를 만족시키므로, 준동형사상은 대수구조의 성질을 보존한다, 즉, 대수구조의 성질은 준동형사상에 양변을 대입하여, 다른 대수구조로 옮길수 있다.

참고로 모델은 튜플이므로, first(x, y) = x와 last(x, y) = y에 대해,

P와 Q는 first로 구해지며, sym을 넘어서 `*`와 `◦`는 last를 각각 i + 1번, j + 1번 하여 얻어지며, i, j는 P, Q의 카디널리티로 얻어지므로, 정의에서 Volcanoₖ,₁사용부분에 결정성에 문제가 생기는지는 걱정하지 않아도 좋다.

범주론에서 대수적 구조 = 아벨 범주이다.
준동형사상은 아벨 범주 위의 사상으로, 범주론을 다루지 않고자 한 지금의 설명에서는 엄밀한 준동형사상의 정의를 다루기 위해 아벨 범주를 다루고싶지 않기에, 다루지 않겠다.

#### 자기 사상을 낀 관계 (Endomorphism)

솔찍히 이게 등호랑 뭐가 다른지 원.....

Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`) Endomorphism Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`) : (∃FunctionalRelationship(f, P, Q))(endomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`))) [i := card P][j := card Q]

인 관계로, P와 Q사이에 자기 사상이 존재하는 관계이다.

자기 사상 endomorphism이란,

endomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)) : homomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)), dom f = codom f [i := card P][j := card Q]

이다. 즉, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`) = Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`))이다.

#### 다루고자 하는 단사 사상을 낀 관계 (Monomorphism)

다루고자 하는 단사 사상을 낀 관계 (Monomorphism) (이)란,

Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`) Monomorphism Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`) : (∃FunctionalRelationship(f, P, Q))(monomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`))) [i := card P][j := card Q]

인 관계로, P와 Q사이의 다루고자 하는 단사 사상이 존재하는 관계이다.

다루고자 하는 단사 사상 monomorphism은,

monomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)) : homomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)), Surject(f) [i := card P][j := card Q]

으로, 단사성을 가지는 준동형사상을 말한다.

#### 다루고자 하는 전사 사상을 낀 관계 (Epimorphism)

다루고자 하는 전사 사상을 낀 관계 (Epimorphism) (이)란,

Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`) Epimorphism Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`) : (∃FunctionalRelationship(f, P, Q))(epimorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`))) [i := card P][j := card Q]

인 관계로, P와 Q사이의 다루고자 하는 전사 사상이 존재하는 관계이다.

다루고자 하는 전사 사상 epimorphism은,

epimorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)) : homomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`)), Surject(f) [i := card P][j := card Q]

으로, 단사성을 가지는 준동형사상을 말한다.

#### 동형 (Isomorphism)

동형 Isomorphism이란,

Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`) Isomorphism Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`) : (∃FunctionalRelationship(f, P, Q))(isomorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`))) [i := card P][j := card Q]

인 관계로, P와 Q사이의 동형사상이 존재하는 관계이다.

동형사상 isomorphism이란,

isomorphism : monomorphism, monomorphism

으로, 전사 사상이고 단사 사상인 사상으로,

걍 일대일대응인 준동형사상이라고 보면 된다.

동형인 두 대수구조에서, P, Q는 등수관계이므로,

i = j이다.

k = i = j라고 하면,

Sym₁, ..., Symₖ가 동형사상을 통하여 일대일대응되어, y = f(x)에서, z ∈ {x, y} 로 잡으면, x와 y의 대수구조 종류가 같고, 성질이 같으며, 심볼의 모든 대수구조상의 특성이 동등함(=동치임)을 알수있다.

요컨데, 동형임은 대수적 구조로서 완벽하게 동일함을 말한다.

#### 자기동형 관계 (Automorphism)

자기동형 관계 Automorphism(이)란,

Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`) Automorphism Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`) : (∃FunctionalRelationship(f, P, Q))(automorphism(f, Volcanoᵢ,₁(P, Sym₁, ..., Symᵢ, `*`), Volcanoⱼ,₁(Q, Sym₁, ..., Symⱼ, `◦`))) [i := card P][j := card Q]

인 관계로, P와 Q사이의 자기동형사상이 존재하는 관계이다.

지기동형사상 automorphism이란,

automorphism : isomorphism, endomorphism

으로, 동형 사상이고 자기 사상인 사상으로,

동형이고, 자기사상을 낀 관계이다.

#### 위상동형사상 관계 (homeomorphic)

위상동형사상 (Homeomorphism)

Homeomorphism(fn) : Biject(fn), (x ∈ dom fn, f = fn ⊨ continuous), (x ∈ codom fn, f = f⁻¹ ⊨ continuous)

### 심볼 목록

아래 심볼은, Volcano에서 사용 목적이 정해진 특수한 심볼이다

#### 항등원 (identity element)

이항연산 `*`의 항등원은

 - 좌항등원 eₗ
 - 우항등원 eᵣ

이 존재하고,

각각

+ eₗ * x = x
+ x * eᵣ = x

를 만족하며, (이게 바로 정의)

다음 술어

항등원이존재함(eₗ, eᵣ) : eₗ = eᵣ

에 대해,

항등원이존재함(eₗ, eᵣ) ⊨ ∃e s.t. eₗ = e = eᵣ

인, 즉, 좌항등원과 우항등원이 같으면, "항등원이 존재한다"고 하고, 좌항등원과 우항등원이 같으니, 그것을 "항등원"이라고 하며, 이것의 존재조건인 좌항등원과 우항등원이 같을것이 항등원의 존재 조건이다.

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 이하에서, 좌항등원 및 우항등원 기호도 여기에서 정의했으므로, 여기를 참고해야한다는걸 강조하고 또 경고하겠다.

### Laval 대수구조 명칭 목록

**Laval은 Lava + -al이라서, Lava + -적(的) 이라는 뜻이다. `Laval == Lava적(的)`인것이다. (오타아님, 중요)**

어떤 Laval 대수구조 명칭 (= Lava식 대수구조 명칭) K란,

K(Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ)) : "대수구조 Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ)가 그 Laval 대수구조 명칭 K가 지칭하는 대수구조를 이룬다"

인 K를 말한다.

예컨데, Magma(Volcanoₘ,₁(D, `*`))은 항진인것이, lava는 기본적으로 닫혀있기에, 그 대수구조 위에 연산이 정의되어있디면 마그마다.

요컨데, Laval 대수구조 명칭은 술어이다.

예컨데 마그마의 Laval 대수구조 명칭 Magma는

Magma라는 영문 명칭 술어이다

#### 1. 1. 단위 마그마 (unit magma)

이항연산 `*`가

Volcano₁,₁(D, e, `*`) ⊨ "이항연산 `*`가 (D, `*`, e)를 이룸"

인 `*`라면, 즉, 항등원을 가진다면,

이를 단위 마그마라고 부른다

Laval 대수구조 명칭은 UnitMagma 이다.

#### 1. 3. 중가환 마그마 (medial magma)

이항연산 `*`가

Volcanoₘ,₁(D, Sym₁, ..., Symₘ, `*`) ⊨ "이항연산 `*`가 (D, `*`)를 이룸", Medial

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가 중가환법칙을 만족시킨다면,

이를 중가환 마그마라고 부른다.

Laval 대수구조 명칭은 MedialMagma 이다.

#### 1. 2. 가환 마그마 (commutative magma)

이항연산 `*`가

Volcanoₘ,₁(D, Sym₁, ..., Symₘ, `*`) ⊨ "이항연산 `*`가 (D, `*`)를 이룸", Commutative

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가 교환법칙을 만족시킨다면, 즉, 가환이라면,

Laval 대수구조 명칭은 CommutativeMagma 이다.

이를 가환 마그마라고 부른다.

#### 2. 1. 반군 (semigroup)

이항연산 `*`

Volcanoₘ,₁(D, Sym₁, ..., Symₘ, `*`) ⊨ "이항연산 `*`가 (D, `*`)를 이룸", Associative

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가, 결합법칙을 만족하면,

이를 반군이라고 한다.

Laval 대수구조 명칭은 Semigroup 이다.

#### 2. 2. 모노이드 (monoid)

이항연산 `*`가

UnitMagma(Volcano₁,₁(D, e, `*`)), Semigroup(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 (D, `*`, e)를 이룸"

인 `*`라면,

즉, 이항연산 `*`가 반군을 이루며, 단위 마그마를 이루면, 

이를 모노이드 (monoid)라 한다.

Laval 대수구조 명칭은 Monoid 이다.

#### 2. 3. 군 (Group)

이항연산 `*`가

(⊨ Monoid(Volcano₁,₁(D, e, `*`)) ⊨ EntireInvertiblity) ⊨ "이항연산 `*`가 <D, `*`>를 이룸"

인 `*`라면,

즉, 이항연산 `*`가 반군을 이루며, 전가역이면 (= 전가역성을 띄면 = 전가역성을 만족하면)

이를, 군이라 한다.

Laval 대수구조 명칭은 Group 이다.

#### 2. 4. 아벨 군 (Abelian Group) • 가환군 (Commutative Group)

> 솔찍히 중학교때 생각한 생각인대 소신발언 하자면, 오차방정식의 근의공식이 없다는걸 밝힌 위대한 수학자 아벨(Abel)님이 너무 고생하고 비참하긴 한데, 대학못간새끼만큼 비참한건 아니니까, (반대하면 인신공격하고싶... 크흠..), 우리 학생들을 위해 과감히 버리고, 가환군이라고 부르는게 좋다고 본다. 소신발언임 주의.

이항연산 `*`가

CommutativeMagma(VoLeftQuasigrouplcano₁,₁(D, e, `*`)), Group(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 <D, `*`>를 이룸"

인 `*`라면,

즉, 이항연산 `*`가 군을 이루는 동시에 가환 마그마를 이룬다면,

이를, 가환군 • 아벨군 이라고 하며,

(또한, AbelianGroup = CommutativeGroup 이고)

Laval 대수구조 명칭을 CommutativeGroup로 한다.

(당연히 AbelianGroup = CommutativeGroup이므로, AbelianGroup로 해도 된다. 왜 대입이 되는지는 "Laval명칭"의 정의 참고. (술어임))

#### 2. 5. 자명군 (trivial group)

이항연산 `*`가 

Group(Volcano₁,₁(D, e, `*`)) s.t. D = {e} ⊨ "이항연산 `*`가 <{e}, `*`>를 이룸"

일때, 이를 자명군이라고 하고, Laval 대수구조 명칭을 TrivialGroup 이라 한다

#### 2. 6. 환 (rig)

Volcano₂,₂(D, 0, 1, +, ×) ⊨ CommutativeGroup(Volcano₁,₁(D, 0, +)), Monoid(Volcano₁,₁(D, 1, ×)) ⊨ 

...작성중...

#### 3. 1. 1. 왼쪽 유사군 (LeftQuasigroup)

Volcanoₘ,₂(D, Sym₁, ..., Symₘ, `*`, `◦`) [`◦` := LeftInverseOf(`*`)] ⊨ "이항연산 `*`가 (D, `*`, `◦`)를 이룸", BijectiveLeftFunctor

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가, 왼쪽 함자 전단사성을 만족시킨다면, 이를 왼쪽 유사군이라고 한다.

#### 3. 1. 2. 오른쪽 유사군 (RightQuasigroup)

Volcanoₘ,₂(D, Sym₁, ..., Symₘ, `*`, `◦`) [`◦` := RightInverseOf(`*`)] ⊨ "이항연산 `*`가 (D, `*`, `◦`)를 이룸", BijectiveRightFunctor

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가, 오른쪽 함자 전단사성을 만족시킨다면, 이를 오른쪽 유사군이라고 한다.

#### 3. 1. 유사군 (Quasigroup)

LeftQuasigroup(Volcanoₘ,₂(D, Sym₁, ..., Symₘ, `*`, `◦`)), RightQuasigroup(Volcanoₘ,₂(D, Sym₁, ..., Symₘ, `*`, `◦`)) ⊨ "이항연산 `*`가 (D, `*`, `◦`)을 이룸"

왼쪽 유사군이자 오른쪽 유사군인것.

즉, 함자가 bijection이면 유사군이다

유사군의 Laval 대수구조 명칭을 Quasigroup라 하자.

<br>

`=== well... ===`

<br>

시실 쉽게말해서, 항상 역연산이 성립하는건게, 항등원 개념이 없어도 된다.

역연산의 특성은 유사군에서 오고, 왼쪽•오른쪽 함자에서 역함자가 존재해서 역연산이 정의되는거다.

어떤 함자 방정식의 해가 유일하게 결정되기 때문이다.

군이라서 역연산이 있는게 아니다.

군이 유사군을 이루기 때문이다.

왜?

전가역성 때문에, a에 대해 그 가역원 b에 대해, (* b)가 (* a)의 역연산으로 정의 가능하기 때문에, 그리고 실제로 일대일대응이 되버리기 때문에, 군은 유사군을 이룬다.

#### 3. 2. 고리 (Loop, 위키백과에선 고리라고 했다만, 수학계에서는 루프라고 부른다고 카더라)

이항연산 `*`가

Quasigroup(Volcano₁,₁(D, e, `*`)), UnitMagma(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 <D, `*`>를 이룸"

일때, 이를 고리라고 하고, Laval 대수구조 명칭으로 Loop 이라 한다.

Quasigroup에 대해서는 최근 설명을 추가했으니, 위 항목 참고

### 성질, 예약 심볼, 대수구조에 대한 해설

#### 결합법칙에 대해 해설하며 ; Associatival Extension과 반군

m항연산 f가 Associative를 만족한다면, m < n인 n에 대해,

f(x₁, ..., xₙ) ≜ f(x₁, ..., xₘ₋₁, f(xₘ, ..., xₙ))

로 제귀적으로 정의하며,

이러한 구조의 작동 원리는 결합법칙에 근거한다.

이러한 제귀적 정의를 결합적 확장 (Associatival Extension)이라고 부르며, 내가 방금 만들어낸 조어이다

m, n은 무한해도 좋을거다. 아마도.

Associatival Extension에 의해, m항연산과 가변항연산의 경계가 허물어지는 특징을 보이기에, 반군인 연산은 k항연산이라면, 최소 항의 수를 k로 간주한다.

#### 역원임-술어에 대해 설명하기 : 좌역원이자 우역원이면 역원임 정리

좌역원이자 우역원이면 역원임 정리는 내가 만든 정리로, 사실 정리라고 하기에도 존나 애매한 난이도다.

+ p' = p ∧ r
+ q' = q ∧ r
+ s = p ∧ q
+ s' = s ∧ r

에서,

p' ∧ q' = s'임은 당연히 안다.

이때,

+ p = 좌역원임-가술어이고
+ q = 우역원임-가술어이고,
+ r = 항등원이존재함(eₗ, eᵣ)일때,

좌역원임-술어, 우역원임-술어, 역원임-가술어, 역원임-술어의 정의에 따라, 

좌역원임-술어 ∧ 우역원임-술어 = 역원임-술어

이라는것이다.

## 의미해석

(작성중; 규칙도입계와 기초적 파악이 어떻게 작동하는지를 먼저 적겠음. 나중에.)

### 규칙도입계

(작성중)

### 기초적 파악

앞으로 말할 L은 모델론적 언어라는 맥락에서 말하는거다.

또한, (작성중)

#### 명세관계 ; isInterfaceOf

T isInterfaceOf L : isInterface(L, T) : (L ⊨ T) s.t. (∀T' ⊨ L)(T ⊨ T')

T는 L의 명세인 관계로, L의 기초임을 알리는 관계다.

L의 정의 ⋅ 규칙을 담당하는 부분으로, 논리 언어 Lₗₒₛᵢₖ (저 및첨자들은 원래 "losik"이 아닌 "logic"로 쓰려고 했지만, 유니코드의 한계상 포기)이 자연 연역(Natural Deduction)하는걸 제외한, 규칙계형 파트로 전반적 논리를 구성한다.

예를들어 L은 TensorFlow, T는 그 공식 document로, 기능은 L에 있고, 그 원리가 T이다.

예를들어,

L = 페아노 산술, T = peano axioms and defines이면,

L"1 + 1 = 2"에서,

정의는, T에서,

```markdown
## DEFINITION

### 덧셈 `+`의 정의

1. x + 1 = x⁺
2. x⁺ + y = (x + y)⁺

여기에서, 정의 2번에 1번을 대입하면, (x + 1) + y = (x + y) + 1로, 결론을 부정하는 조건을 만족하는 명제를 역산해보자면, 그것이 바로 교환법칙의 부정과 결합법칙의 부정이므로, 부정한 결론이 틀림에 근거하여, 이중부정을 통해, 덧셈은 가환반군을 이룸을 알 수 있다. 참고로, 0을 정의하지 않은 버전에서는 모노이드도 아니고 걍 반군이다.

## AXIOMS

다음 다섯 공리를 만족하는 상수 1과 집합 ℕ이 존재한다.

1. 1 ∈ ℕ
2. n ∈ ℕ ⇒ n⁺ ∈ ℕ
3. ∀n ∈ ℕ, n⁺ ≠ 1
4. ∀n ∈ ℕ ∀m ∈ ℕ, n⁺ = m⁺ ⇒ n = m
5. ∀S ⊂ ℕ, (1 ∈ S ∧ (n ∈ S ⇒ n⁺ ∈ S)) ⇒ (S = ℕ)

공리 5를 자연수의 귀납적 정의라고 하며, 이는 무한공리에서 말하는 무한집합 중 최소의 크기를 가지는 집합이라는 뜻이다. 또한, 저기에서 수학적 귀납원리가 나온다.

저걸 함수의 언어로 바꾸면, 어떻게 모델을 구축해야할지 보인다.

4번 공리를 보아하니, 다음수 연산 `⁺`는 단사(일대일함수)이다. 그런데, 치역이 1 이상의 자연수 전체이므로, 해당 자연수를 정의역으로 하고 치역이 1이상의 자연수를 치역으로 한다면, 전단사함수(일대일대응)일것이고, 따라서, 다음수 연산은 역함수인 이전수 `⁻`를 가진다. (이 설명의 근걸는 2번 공리 함고)

3번, 1번, 5번 공리를 보면, 자연수는 1에서 시작해서 연쇠적으로 세어나가면서 나오는 수들의 집합이다.

참고로 5번 공리를 보지 말고, 2번 공리만 보더라도 알 수 있다.

사실 5번 공리에 1번 공리에 쓰인 텍스트와, 2번 공리에 쓰인 텍스트가 전부 들어간 점에서, 우리는 자연수 집합 S = ℕ을 다룰떄, 1번, 2번, 3번 공리를 보면 됨을 쉽게 알 수 있다.

사실은, 이것의 모델에서 1은 상수 심볼인데, 번외에서 신기한 특징을 다루겠다.

## 번외

다음 술어 ℙ₁, ℙ₂, ℙ₃, ℙ₄, ℙ₅를 DEFINE하자.

ℙ₁(k, ℕₖ) : k ∈ ℕₖ
ℙ₂(k, ℕₖ) : n ∈ ℕₖ ⇒ n⁺ ∈ ℕₖ
ℙ₃(k, ℕₖ) : ∀n ∈ ℕₖ, n⁺ ≠ k
ℙ₄(k, ℕₖ) : ∀n ∈ ℕₖ ∀m ∈ ℕₖ, n⁺ = m⁺ ⇒ n = m
ℙ₅(k, ℕₖ) : ∀S ⊂ ℕₖ, (ℙ₁(k, S) ∧ ℙ₂(k, S)) ⇒ (S = ℕₖ)

다음은 AXIOMS이다.

다음 공리를 만족하는 상수 k와 집합 ℕ이 존재한다.

1. ℙ₁(k, ℕₖ)
2. ℙ₂(k, ℕₖ)
3. ℙ₃(k, ℕₖ)
4. ℙ₄(k, ℕₖ)
5. ℙ₅(k, ℕₖ)

여기에서도, 4번공리를 통해 다음수의 특징이 유추되며,
1, 2, 3번공리를 통해, k부터 시작하는 자연수(서수) ℕₖ를 정의함을 알 수 있다.

참고로, 덧셈의 정의를 통해서 다름수의 뜻을 알수 있음은 너무 당연한 사실이고, 여기서도 동일하다.

참고로 ℕ₀를 범자연수라고 하며, 𝕎 = ℕ₀로 표기하기도 한다.

참고로,

수가 0, 수가 null(=Null), 수가 NaN인것의 차이가 뭐냐하면,

0은 잔액이 0,
null은 잔액이 없음 (= 그런거 없음)
NaN은 잔액이 수가 아님 (= 0/0꼴)
인것이라서,

0은 통장 잔액이 텅장
null은 통장이 없음
NaN은 통장 잔액이란 개념이 없음

이었던가...? 그랬다.

그런데 잔액이 없는거 (수량을 보는데 그값이 없음(=null))랑 잔액이 0인거 (수량이 0인것)가 무슨 차이인가?

수량으로써 0은 그것이 수량으로 있어야 한다.

0은 없는것을 의미하는, 즉, 1 - 1을 의미하는 수량이고,

이게 자연수가 되야하는지는 논란이었다. (= 자연에 있는 수인지, 자연으로부터 나오는지 논란)

그러나, 수라는게 자연을 설명하는것이고, 셈을 시도했을때, 무조건 ℕ₀(= 𝕎)나 NaN(=원래는 실수에서 정의역 벗어남이지만, 여기서는 범자연수로 치자.)으로 세어지므로, 범자연수로 다룬다고 합리화하는것 같다.

솔찍히 나도 뭐가 맞는지 모르겠고, 걍 범자연수로 구축하는게 용이한건 확실하다.

그래서 실제로, 페아노 공리계를 구축할때는, 범자연수를 쓴다고 한다.
```

이므로, 해당 언어는 모델론이 의미하는 규칙에 따라, L"1 + 1 = 2"가 L"1⁺ = 2"로 치환되서 (덧셈의 정의), 심볼 '2'가 의미하는 바가 1의 다음수를 표기하는 Notation임을 알 수 있다.

그러니까 십진법 기호 표기법은,
1. 2 = 1⁺
2. 3 = 2⁺
3. 4 = 3⁺
4. 5 = 4⁺
5. 6 = 5⁺
6. 7 = 6⁺
7. 8 = 7⁺
8. 9 = 8⁺
   
를 만족하는 모델론적 언어로 볼 수 있다.

십육진법에서는
1. 추가규칙 아님, 상단참고
2. 추가규칙 아님, 상단참고
3. 추가규칙 아님, 상단참고
4. 추가규칙 아님, 상단참고
5. 추가규칙 아님, 상단참고
6. 추가규칙 아님, 상단참고
7. 추가규칙 아님, 상단참고
8. 추가규칙 아님, 상단참고
9. A = 9⁺
10. B = A⁺
11. C = B⁺
12. D = C⁺
13. E = D⁺
14. F = E⁺
    
인 추가 규칙이 생기는것이고 말이다.

참고로, 범자연수식으로 보자면, 1 = 0⁺로 정의된다.

물론 이에 대해, 항상 참인거 아니냐고 물을 수 있을텐데, 무한공리를 허용하지 않으면, 이러한 구축방법은 참이 아니고, 이런식으로 정의와 공리를 적고 나서 그를 만족시키는 모델이 존재하지 않는...

예컨데, 공리에 1 = 2를 추가하면 배중률을 어기는데, 이를 만족하는 모델은, 더이상 형식논리가 아니므로, 항상 참은 아니다.

하필 자연수의 덧셈을 가져와서 항상 참이지만

하필.

#### 구현관계 ; isImplementOf

M isImplementOf T : isImplementOf(T, M) : T isInterfaceOf L, M ⊨ T ⊨ L

M이 T의 구현 (Tip : 구현체로 이해해도 좋음)인 관계로, M은 T인 체계를 구성한다.

L언어와 그것을 이룰 요건인 기초 T를 만족하는 M은 구조모델이고, M은 기초 T와 Pre와 Fun, Sym정의 등을 구현(=구성)하며, M ⊨ L ⊨ T인 측면이 있다.

그러나 T의 본질이 M인지 확신할 수 없으며, 당장 FOL에서 뢰벤하임-스콜렘 정리 (Löwenheim–Skolem theorem)등에 따라서, 본질이라기 보다는, 수학적 • 구조적 정합성 측면에서 본질로 볼 수 있는 측면이 있는 구현(=형식화, 사실 정의 되는지도 모르겠는걸 분석 후 모델로써 정의하는것같은 원리다)이지, 유일한, 그리고 절대적인 진리 따위가 아니다.

뢰벤하임 스콜렘 정리에 따라서, 여러가지 모델로 본질을 표현할 수 있다고 하고, 당장에 실수에 대해서, Łoś's theorem으로 만든 `ℝ*` (초실수체, hyperreal field) 만 봐도, 알 수 있다.

그러나 겉모습만 보여주고 그걸 본질이냐고 묻는데에 대해서는 전혀 그렇게 확신할 근거가 없다고 단언한다. 근거를 가져와야한다.



다시 돌아와서, T와 M에 대해 말하자.

예컨데 T는 TensorFlow의 document, M은 일게 그 구현체,

혹은 T는 C언어나 LISP, M은 gcc나 Racket을 예로 들수 있을것이다.



다시한번 이전에 peano공리계로 예를 들었듯 peano공리계 T와 체르멜로(Zermelo)의 구성(Constructure) M과, 폰 노이만 (von Neumann)의 구성 `M'`으로 예를 들어보자 

먼저 M은

```markdown
s(x) = x⁺에서,

0 := ∅
s(x) := {x}

즉,

M = <ℕ₀, 0 = ∅, s(x) = {x} s.t. codom s = ℕ>

인 체계로,

16진수 표기법은,

0 := ∅에서,

1. 1 := {0}
2. 2 := {1}
3. 3 := {2}
4. 4 := {3}
5. 5 := {4}
6. 6 := {5}
7. 7 := {6}
8. 8 := {7}
9. 9 := {8}
10. A := {9}
11. B := {A}
12. C := {B}
13. D := {C}
14. E := {D}
15. F := {E}

로 볼 수 있다.

덧셈은, 범자연수에 대해 가환 모노이드를 이룬다.

> 
> pf.
> 
> 기본적으로 덧셈은 가환 반군을 이룬다.
> 
> 집합 중간에 구멍을 송송내서 닫히지조 못하게 고문하는 경우는 제외하고 말이다.
> 
> 그런 비정상정임경우를 가져오는 미친놈은 아마 없을것이다.
> 
> ~~(가져온다면 덧셈왈 나는 입이없지만 소리를 질러야 한다 이럴듯하다)~~
> 
> 0 + 1 = 0⁺ = 1이므로,
> 
> (0 + x)⁺ = 0⁺ + x = 1 + x = x + 1 = x⁺임을 알수 있는데,
> 
> (x + 0)⁺ = x⁺이므로,
> 
> x + 0 = x임을 알 수 있다.
> 
> 즉 항등원을 가지니, 단위 마그마를 이룸을 알 수 있다.
> 
> 가환 반군이자 동시에 단위 마그마인것은, 가환이고 반군이자, 동시에 담위 마그마인것으로, 가환이고, 모노이드인것으로, 가환 모노이드이다.
> 

2 + 2 = 4인것은,

2 = 1⁺이기에,

2 + 1⁺ = 1⁺ + 2 = (1 + 2)⁺ = (2 + 1)⁺ = 3⁺ = 4로 구할 수 있다.



덧셈은,

1. Φ₁(`*`) : `x * 1 = x⁺`
2. Φ₂(`*`) : `x⁺ * y = (x * y)⁺`
3. Φ : Φ₁, Φ₂

이게 정의한 술어 Φ에서,

Φ(`+`)인 연산이다.

사실은 (+ 1) = s 이게 정의되며, 닫혀있다면 가환반군을 이룰성질을 부여해서 구축했다고도 볼 수 있다.

근데, 이러면, 단점이 좀 있어서, 충분히 나은 폰 노이만 방식을 택한다.

당연히 최대효율을 택하는 한계효용 생각해보면 합리적으로 보인다.
```

`M'`은

```markdown

자연수가 서수(ordinal) 이게도 만들어주는 장점많은, 삐까뻔쩍한 구성이다.

s(x) = x⁺에서,

0 := ∅
s(x) := x ∪ {x}

식으로 구성한다.

즉,

`M'` = <ℕ₀, 0 = ∅, s(x) = x ∪ {x} s.t. codom s = ℕ>

사실 도매인(정의역, 모델의 닫여야하는 집합)이 ℕ₀일떼, codom s = ℕ임은 전부 그렇다.

이 점에서, 자연수가 간단히 나오니 걍 범자연수 구축이라도 왜 이래야 하는지 따지지 말고 받아들여줬으면 좋겠다.



자, 폰 노이만 구성에서 16진수 표기법은

0 := ∅ (= {}) 에서,

1. 1 = {0}
2. 2 = {0, 1}
3. 3 = {0, 1, 2}
4. 4 = {0, 1, 2, 3}
5. 5 = {0, 1, 2, 3, 4}
6. 6 = {0, 1, 2, 3, 4, 5}
7. 7 = {0, 1, 2, 3, 4, 5, 6}
8. 8 = {0, 1, 2, 3, 4, 5, 6, 7}
9. 9 = {0, 1, 2, 3, 4, 5, 6, 7, 8}
10. A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
11. B = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A}
12. C = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B}
13. D = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C}
14. E = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D}
15. F = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E}

이다.

마찬가지로 반군을 이루고, 덧셈의 구성 방법도 같다.



폰 노이만 식이든 체르멜로 식이든

Rank x = x 임은 같고,

x ∈ x⁺임도 같지만

폰 노이만 방식은

0, 1, ..., x ∈ x⁺

이며,

card x = x (단. 이 문장은 엄밀하지 못하다. 범자연수와 기수와 서수는 다른것이, 기수(카디널리티, 카디널)는 "××집합의 카니덜은"이라고 말하는데에서 알수 있듯, 집합에 대한것이다 (정의상), 집합의 카디널리티는 일대일대응이 있으면 같은것이므로, 카디널리티(기수)를 범자연수로 정의하지 아니하였다면, 카디널이 같은지 여부에서는, 에초에 관계의 정의역에 들어가지 못하는 불상사다 일어나, 항위일것이니, 카디널리티가 범자연수인 경우에 맞는 문장이다)

이라는것이 특징이다.

또한, y ≤ x에서,

y ⊂ x으로,

외연공리를 이용하여 같은지 다른지를 알 수 있는 장점이 있다.

사실 범자연수 집합의 존재성은, 무한 공리에서 보장한다.

ZF공리계에서 초한수의 최소이자 초한기수의 최소는 자연수번째 무한 혹은 자연수의 카디널, 즉 자연수 크기의 무한인데,

무한 공리에서 말하는 최소 크기의 무한집합이 자연수이기 때문이다. (자연수의 정의)

그리고 이게 표준 방법이다.

비표준이라고 틀린건 아니지만, 권총과 망치로 인해 표준이 맞는것처럼 치도록 강제할수 있다.

사회라는 약속으로.
```

위와같이 모델을 만들수 있어도, 이것이 왜 그 구현이여야 하는지 잘 모르겠지 않나?

진짜 자연수는, 그 본질이 공리계에 있을것이다.

(사실 굳이 그 공리계로 잡지 않아도, 다른 공리계가 그 공리계를 만족시킨다.)

아마도 말이다. 이것은 본질이라기에는 실용적 구현에 가까워보이니, 함부로 명세가 본질이네 구현이 본질이네 할 증거가 없다고 단언한것이다.

그 증거를 더 가져와야 한단것을.

그리고, 자연수의 두 구현체를 보고, 당연히 그런식으로 약속했으니 그렇게 되는것 아니냐고 묻는다면 말하겠다.

당신은 Lisp(언어)와 Racket(구현체)이 완전히 동일하다고 생각하는가?

#### 상속자 : Extender

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT :  자, 이제부터 다루는 내용이 핵심이다. isInterfaceOf나 isImplementOf는 일게 모델론적 개념의 표기법용 노트의 설명에 불과하다.

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 내가 설명항 내용은 지금부터 시작이고, 의미해석의 핵심 파트는 상속사, 피상속자, 참피상속자, 섹터, 명제귀결, 구조귀결, 폼페이 함수를 이용한, 기초적 파악이고, 이중 피상속사 참피상속자, 섹터같은 구조가 상속자에서 나온다.
N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 그러나 핵심적인 논리흐름은 명제귀결, 구조귀결을 알아야 하고,
N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 다루는 대상은 기초적 파악이다.

자, 본론으로 들어가보자.

Interface, Implement, Extend... 사실 이것들은 다 Object Oriented Programming Language인 Java에서 따온 명칭이다.

뭐... 그냥 그렇다는거다.

Extenderₙ(M₁, ..., Mₙ) ≜ M s.t. M₁, ..., Mₙ ⊨ M

Extender(상속자)란 n개의 Implement들을 상속한 Structure Model을 주는 함수로 Extender의 용법의 대표적 예시로는, DustunalExtenderalObject와 Sector가 있다.

상속자를 아래 예시로 살펴보자.

```python

class CORE(bool):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    def __gen_my_type(self, ob):
        return type(self)(ob)

class ConjuntionLattice(CORE):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    def __and__(self, other):
        return self.__gen_my_type(self and other)

class ANF(ConjuntionLattice):
    def __init__(self, value) -> None:
        super().__init__(value)
    
    def __xor__(self, other):
        return self.__gen_my_type(int(self) ^ int(other))

class NagationStructureModel(CORE):
    
    def __init__(self, value) -> None:
        super().__init__(value)
    
    def __invert__(self):
        return self.__gen_my_type(not self)

class CNF(NagationStructureModel, ConjuntionLattice):
    def __init__(self, value) -> None:
        super().__init__(value)

class DNF(NagationStructureModel):
    def __init__(self, value) -> None:
        super().__init__(boolean)
    
    def __or__(self, value):
        return self.__gen_my_type(self or other)

class PsudoAngdeAlgebra(ConjuntionLattice):
    '''
    # diffrence between PsudoAngdeAlgebra and Angde Algebra
    
    while Angde Algebra is defined by me, and also it only use imply and use boolean value , not using conjuntion, but PsudoAngdeAlgebra is using Conjunction to form the logical operated.
    
    model theory to make an logical language or gödel numbering's logical operand.. blablabla

    it used in past as whole diffrent forms. that's an critical diffrence betwean AngdeAlgera
    '''

    def __init__(self, value) -> None:
        super().__init__(value)
    
    def __le__(self, value):
        '''
        letter `<=` seems like reversed implication operator `⇐`, so it will coded as `<=` means `←` which implication symbol s.t. `x ← y` means `y implies x` s.t. `x ← y = y → x = (¬y ∨ x)`
        '''
        return self.__gen_my_type(self or not value)

class HighschoolLevelLogicalOperator(PsudoAngdeAlgebra, CNF, DNF, ANF):
    '''
    L = {'~', '&&', '||', '^', '<='}
    '''
    
    def __init__(self, value):
        super().__init__(value)
```

이처럼 상속 구조는 필드(구조체 상수)및 메서드(구조체 함수)를 가져오는데,

다음 c/c++코드를 보라.

```cpp

struct intSizeTyp {
    int main_value;
    
    intSizeTyp(int main_value) {
        this.main_value = main_value;
    }
}

struct MathmaticalStructure : intSizeTyp;

struct MathmaticalStructure {
    const MathmaticalStructure Sym1 = MathmaticalStructure(0);
    const MathmaticalStructure Sym2 = MathmaticalStructure(1);
    
    MathmaticalStructure Fun1(intSizeTyp x) {
        return x + this.Sym2
    }
    
    MathmaticalStructure Fun2(void) {
        /* null-ary operand */
        return this.Sym1
    }
};
```

저 구조체는 다음과 같은 튜플이다.

MathmaticalStructure = <constructer, Sym1, Sym2, Fun1, Fun2, main_value>

각각 도메인(이라고 치자고 ㅋㅋ ㅠㅠ) 상수기호 Sym1, Sym2, 함수기호 Fun1, Fun2, 변수기호 main_value가 차례대로 담긴 그저 튜플이다.

그리고 이건 시벙 놀랍게도 C의 구조체의 역할인 그냥 이름붙여 묶기를 잘 수행하는 튜플이다.

예를 들어보자.

```cpp
struct cardesian_coordinate {
    double x; //8B = 64bit
    double y; //8B = 64bit
};

cardesian_coordinate v;
```

위 코드는 다음과 같이 메모리에 적제될것이다. (컴파일 예시지 실제로 저러진 않는다.

```
memory addr : 0000 0000 0000 07B4 | v.x
memory addr : 0000 0000 0000 07BC | v.y
```

그러면 저 필드가 가르키는건 순전히 <x, y>인 튜플의 원소다.

실제로 SIMD vectorization연산도 이와 유사하다.

이와같이, 어떤 구조체 M, N이 있어서, M ⊨ N의 만족관계를 가지면, 상속된다고 비유적으로 이해할 수 있다.

#### 피상속자 ; ExtenderalObject

피상속자 ExtenderalObject는 External과 반대로, 부모를 쫒아간다 생각하면 편하다. (편하다고 했지, 꼭 그런건 아닌게, 피상속 관계를 만족시키는걸 뱉는 다가함수로, 부모 모델들의 집합을 뱉지만 그걸 여러개 뱉으므로, M, N, L을 상속했더라도 `M'`, `N'`, `L'`이 나오지 않으리란 보장이 없다. 사실 둘다 다가로 나오는 함수니까. (이가라고 한정한 적 없음))

ExtenderalObjectₙ ≜ (Extenderₙ)⁻¹

ExtenderalObject는 다가함수로, M이 상속된 자식이게 하는 M₁, ..., Mₙ들의 모임 `M'`을 뱉는 다가함수로, M'이 여러개이기에, 튜플(=구조체)집합(=모임)(=M')의 집합족(M'들의 모임)으로 가는 치역을 가진다.

ExtenderObject는 결국 M을 만족시키기에, 자신을 낳을(=모델링할) 부모를 파악하는 함수이다. 또한, 

(작성중)

#### 참피상속자 ; DistunalExtenderalObject

(작성중)

#### Sector

(작성중)

#### 명제귀결 ; ProposolalConsequence

(작성중)

#### 명제귀결도입기반 구조귀결 ; ProposolalConsequenceIntroduceSystemicConsequence

(작성중)

#### 폼페이 함수 ; Pompeii

(작성중)

#### 기초적 파악

(작성중)

## NOTE

으아....