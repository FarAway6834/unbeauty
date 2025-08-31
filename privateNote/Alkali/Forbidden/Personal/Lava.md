# Lava System

(내가 추상대수학 배우려고 만든 체계)

닫힌형태의 대수구조를 폐구조라고 명명하고, Lava라고 부르겠음.

관계가 주어지지 않은 n개의 함수와 m개의 심볼을 가진 Structure

M = <D, Sym₁, ..., Symₘ, fun₁, ..., funₙ>를 (m, n)-Lava라고 하겠음

(m, 0)-Lava는 (심볼을 정의한, 즉 정의용) 집합인 기본적인 대수구조이다.

참고로, (m, 1)-Lava이상은, 각 연산이 전부 D와 마그마를 이룬다.

Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ) ≜ <D, Sym₁, ..., Symₘ, fun₁, ..., funₙ>

라 하겠다.

Volcano는 (m, n)-Lava를 생성하는 무한 차원의 (= 행과 열의 총 길이가 자연수 기수 길이인) 함수행열이다.

예컨데, Volcano₂,₀(𝔹, F, T)는 부울-도메인으로 유명하다.

내가 스스로 정의한
Lava에서 확장한걸로 구조꼴 (structrue form)이라는게 있는데, 아래와 같다.

StructureFormₗ,ₘ,ₙ(D, Sym₁, ..., Symₗ, fun₁, ..., funₘ, Pre₁, ..., Preₙ) ≜ <D, Sym₁, ..., Symₘ, fun₁, ..., funₙ, Pre₁, ..., Preₙ>

Pre₁, ..., Preₙ는 술어이고, 이게 뭐하나 미스되지 않고, Lava랑은 달리 있을거 다있게 정의된 구조의 최소 단위이므로, 이를 "구조꼴"이라고 하고, 삼차원 행렬 (= 이제 텐서 ㅋㅋㅋㅋ) StructureForm를 통해 만들 수 있다.

(근데 나 멀미나와서 오늘은 여기까지 작성하겠고, 추상대수학은 여기까지 배우겠음.)

## 대수 구조 공부

### 성질 목록

아래 술어들은, Lava M에 대해, 

M ⊨ Φ : "M이 성질 Φ를 만족한다"

라고 하는 술어 Φ들이고, 성질이라고 부른다.

사실 술어랍시고 써놨는데

1. 죄다 자유변항만있고, 종속변항은 없는것은 "참성질"이라고 부르고, 걍 사실상 문장명명이다.
2. 자유변항이 존재하고, 종속변항도 존재하는것을, "가성질"이라거 부르고 걍 사실상 술어다.

참성질과 가성질의 `참-`, `가-`는 참다랑어와 가다랑어에서 따왔다.

참성질을 법칙성질, 가성질을 성질부분이라고도 한다. (이것도 근데 방금 만든 조어다)

~배고프니까 천장에서 다랑어가 쏳아졌으면 좋겠다~

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

#### 우역원임-가술어 (tunal is-rightinvers-of Predicate)

우역원임-가술어 tunalIsRightinversOf는 내가 방금전에 명명한 가성질이다.

tunalIsRightinversOf(e, b, a) : "a * b = e"

#### 좌역원임-술어 (is-leftinverse-of Predicate)

좌역원임-술어 isLeftinverseOf는 내가 방금전에 명명한 가성질이다.

b isLeftinverseOf a : isLeftinverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsLeftinverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 좌역원임-가술어이다.

#### 우역원임-술어 (is-rightinverse-of Predicate)

우역원임-술어 isRightinverseOf는 내가 방금전에 명명한 기성질이다.

b isRightinverseOf a : isRightinverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsRightinverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 우역원임-가술어이다.

#### 역원임-가술어 (tunal is-inverse-of Predicate)

역원임-가술어 tunalIsInverseOf는 내가 방금전에 명명한 가성질이다.

tunalIsInverseOf(e, a, b) : tunalIsLeftinversOf(e, a, b), tunalIsRightinversOf(e, a, b)

로, 좌역원임-가술어와 우역원임-가술어를 모두 만족시키는, 즉, 역원인 경우로써,

이경우도 e에 따라, 항등원이 좌/우 항등원인 역원임-가술어로 말할 수 있다.

### 역원임-술어(is-inverse-of Predicate)

역원임-술어 isInverseOf는 내가 방금전에 명명한 가성질이다.

b isInverseOf a : isInverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsInverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 역원임-가술어이다.

#### 가역원임-가술어 (tunal cheking-dose-it invertible-element Predicate)

가역원임 가술어 isInvertibleAs는 방금전에 내가 만든 가성질로,

역원 판별논리식 Φ에 대해,

x isInvertibleAs Φ : isInvertibleAs(x, Φ) : ∃y s.t. Φ(x, y)

인 isInvertibleAs로, FOL에서는 술어가 아닌 성질꼴로, 여러가지 성질의 접두사로 동작하며, 그 경우 Φ과 isInvertibleAs를 붙여쓴다.

그러나 권장사항은 SOL에서의 사용이다.

왜냐하면, 내가 FOL로 만들기 디껍고 귀찮기 때문이다.

다만 한가지 주의하기 위해 참고할 점은, ∃y라는 y는 해당 구조의 도메인 위에 있어야 하므로, 닫여있는 원소인 조건이라는것이고, 따라서, 구조위에서의 의미해석을 해야함에 주의하자.

#### 가역원임-술어 (cheking-dose-it invertible-element Predicate)

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

를 만족하며,

다음 술어

항등원이존재함(eₗ, eᵣ) : eₗ = eᵣ

에 대해,

항등원이존재함(eₗ, eᵣ) ⊨ ∃e s.t. eₗ = e = eᵣ

인, 즉, 좌항등원과 우항등원이 같으면, "항등원이 존재한다"고 하고, 좌항등원과 우항등원이 같으니, 그것을 "항등원"이라고 하며, 이것의 존재조건인 좌항등원과 우항등원이 같을것이 항등원의 존재 조건이다.

### Laval 대수구조 명칭 목록

어떤 Laval 대수구조 명칭 (= Lava식 대수구조 명칭) K란,

K(Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ)) : "대수구조 Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ)가 그 Laval 대수구조 명칭 K가 지칭하는 대수구조를 이룬다"

인 K를 말한다.

예컨데, Magma(Volcanoₘ,₁(D, `*`))은 항진인것이, lava는 기본적으로 닫혀있기에, 그 대수구조 위에 연산이 정의되어있디면 마그마다.

요컨데, Laval 대수구조 명칭은 술어이다.

예컨데 마그마의 Laval 대수구조 명칭 Magma는

Magma라는 영문 명칭 술어이다

#### 1. 1. 단위 마그마 (unit magma)

이항연산 `*`가

Volcano₁,₁(D, e, `*`) ⊨ 이항연산 `*`가 (D, `*`, e)를 이룸

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

CommutativeMagma(Volcano₁,₁(D, e, `*`)), Group(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 <D, `*`>를 이룸"

인 `*`라면,

즉, 이항연산 `*`가 군을 이루는 동시에 가환 마그마를 이룬다면,

이를, 가환군 • 아벨군 이라고 하며,

(또한, AbelianGroup = CommutativeGroup 이고)

Laval 대수구조 명칭을 CommutativeGroup로 한다.

(당연히 AbelianGroup = CommutativeGroup이므로, AbelianGroop로 해도 된다. 왜 대입이 되는지는 Laval명칭의 정의 참고. (술어임))

#### 2. 5. 자명군 (trivial group)

이항연산 `*`가 

Group(Volcano₁,₁(D, e, `*`)) s.t. D = {e} ⊨ "이항연산 `*`가 <{e}, `*`>를 이룸"

일때, 이를 자명군이라고 하고, Laval 대수구조 명칭을 TrivialGroup 이라 한다

#### 3. 2. 고리 (Loop)

이항연산 `*`가

Quasigroup(Volcano₁,₁(D, e, `*`)), UnitMagma(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 <D, *>를 이룸"

일때, 이를 고리라고 하고, Laval 대수구조 명칭으로 Loop 이라 한다.

Quasigroup에 대해서는 최하단 탬구 예정 노트 참고

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

### 규칙도입계

### 기초적 파악

앞으로 말할 L은 모델론적 언어라는 맥락에서 말하는거다.

#### 명세관계 ; isInterfaceOf

T isInterfaceOf L : isInterface(L, T) : (L ⊨ T) s.t. (∀T' ⊨ L)(T ⊨ T')

T는 L의 명세인 관계로, L의 기초임을 알리는 관계다.
L의 정의 ⋅ 규칙을 담당하는 부분으로, 논리 언어 Lₗₒₛᵢₖ (원래 losik가 아닌 logic로 쓰려고 했지만, 유니코드의 한계상 포기)이 Nattural Dedication하는걸 제외한, 규칙계형 파트로 전반적 논리를 구성한다.

예를들어 L은 Tensorflow, T는 그 공식 document로, 기능은 L에 있고, 그 원리가 T이다.

예를들어,

L = 페아노 산술, T = peano Axioms and defines이면,

L"1 + 1 = 2"에서,

정의는, T에서,

```markdown
## DEFINITION

### 덧셈 `+`의 정의

1. x + 1 = x⁺
2. x⁺ + y = (x + y)⁺

## AXIOMS

다음 다섯 공리를 만족하는 1 ∈ ℕ

```

## NOTE

작성중이고, 함자 (* x), (x *)가 준동형사상인 마그마가 유사군(quasigroup)이라고 하는데, 어떻게 적어야 할 지 모르겠으니, 범주론 배울때 배워보자.

유사군의 Laval 대수구조 명칭을 Quasigroup라 하자.
