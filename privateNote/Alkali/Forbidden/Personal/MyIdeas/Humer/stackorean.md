# 스택국어(stackorean)와 극단적 형식적 굴절 관점

스택국어를 만들때 사용한 나만의 개똥철학과, 나만의 타입시스템을 통해서, "스택-"접두조사를 정의했기에 사용한다.

스택국어를 만든 이유는, 내가 애니랑 보컬로이드를 좋아하는데, 일본어는 잘 몰라서, 스택국어를 먼저 정의한 후 스택일어(스택일본어)를 만드려는 목적이다.

한국어와 일본어는 Reversed Polandian Notation의 어순인 SOV어순이지만, 스택국어(stackorean)•스택일본어(StackNihongo)에서는 O* V순이다. O에 클레이니 스타가 붙은 이유는, **[주사들의 나열은 쉼표로 표기한다.](#주의사항)**

## 극단적 형식적 굴절 관점

주의 : 극단적 형식적 굴절 관점은 작성자가 포합어•교착어•굴절어를 구분하는걸 회의하는 작성자 본인의 뇌피셜이고 개똥철학이다. 음모론이라 불러도 될정도의 과학적 근거 없이, 형식적으로 같으니까, 현실에도 차이가 없을거라는 귀추법이다 (현실에 차이가 있어도 형식적으로 같을수 있다. 그럼에도 형식적으로 차이가 없으니까 묶는건 솔찍히 성급한 일반화가 맞다.)

 * 0. 극단적 형식적 굴절 관점 : 접두/접미사형 조사/접사를 이용한 교착/포합 굴절규칙도 굴절규칙이며, 토큰어 관점과 교착/포합 굴절 관점을 포함한, 굴절에 대한 극단적인 형식적 관점.
 * 1. 교착/포합 굴절 관점 : 교착(조사)/포합(문법접사)은 형식문법으로 표현시 굴절이나 다름없다는 고도의 형식주의적 관점. 교착이나 포합을 교착/포합 굴절이라고 부른다.
 * 2. 토큰어 관점 : tokenization이 프로그래밍 의미론상 굳이 어절과 regex `\b`를 도입하는 불필요한 문자 `\b`기준 split이라는 관점. 토큰어를 tokenization을 하는 언어로 간주.
 * 3. (교착 / 포합 굴절) / 굴절 규칙 : 교착/포합 굴절과 굴절을 품사의 의미적•문법적 상태를 문법규칙으로 변화시키는 (교착 / 포합 굴절) / 굴절규칙으로 형식적으로 정리된다는 교착/포합 굴절 관점 사상에 따른 형식문법으로의 교착/포합/굴절의 표현
 * 4. 접두/접미사형 조사/접사 : 어근(어원)의 머리(시작)/꼬리(끝)에 접하는(붙는) 조사/접사

## 스택국어 (한국어에 "스택-" 접두조사라는 단어를 추가한 한국어)

 * 0. 페러다임 : 극단적 형식적 굴절 관점 / RPN의 문법을 통한 의미론에 대한 회의 (Reverse Polandian Notation이 Stack Parsing에 용이하지만, Reverse Polandian Notation이 Stack Parsing의 의미론을 가지진 않을거다.) / 파싱 회의 • 우선순위 회의 • 괄호 회의 • 스택 회의 (우선순위는 괄호로 처리되는 문법규칙이며, 괄호는 스타 네트워크의 중첩인 트리라는 허상을 이용한다, 기왕 파싱이라는 허상을 쓸꺼면 괄호보다 깔끔한 스택을 쓰자, Stack 기반처리는 명확하다.)
 * 1. "스택-"접두조사 ("스-"라고 줄여서 말해도 됨 (n.b. 모호할수 있음)) : "스택-"접두조사 교착 굴절 규칙을 적용할때 쓰이는 접두사형 조사. "스택-"이라는 형태고 "스-"라고 줄여서 말해도 됨 (n.b. 모호할수 있음)
 * 2. "스택-"접두조사 교착 굴절 규칙 : "스택-x"를 "TOS x"라는 조동사형 전치사 "TOS"로 컴파일한다.
 * 3. 조동사형 전치사 "TOS" : "앞서 말한 주사들에 대하여"라는 의미의 전치사이자 조동사
 * 4. 조동사형 전치사 : 조동사로, 동사(빈사)의 의미를 더해주긴 하지만, 동시에 통사론적으로 전치사/접두조사(접두사형 조사)의 교착굴절의 역할을 한다.
 * 5. TOS형 (문법 성질) : "스택-"을 붙인 동사의 형(type).
 * 6. 순수형 (문법 성질) : "스택-"을 붙이지 않은 동사의 형(type).
 * 7. 형식적 TOS정의 : 아래 문단에 있음

국어의 언어 L에 대해, 자유모노이드 <L*, ε, concat>에서의 연산 (`concat` "그리고" `concat`)으로 언어가 구성될 뿐. 본질적으로 모든 단어의 타입은 L* (즉, str)로 동일하다.

스택국어의 언어 L에 대해, 자유모노이드 <L*, ε, concat>에서, (`concat` "TOS" `concat`)연산자를 형식문법상 TOS로 정의한다.
TOS의 입력 타입은 L*이다. 타입체크를 안하는셈이다.

문법의 타당성은 문법검사기로 하라. TOS는 문법의 타당성은 검사 안하고, 동사라는 함수를 바로 호출한다.

핵심 : "앞서 말한 주사들에 대하여, TOS연산으로 「동사」-한다."라는 자연어 문장에 있어서, 문법이 타당한지, 호출 시점에 검사하는거다.

동사에 붙은 문법이 옳은지 아닌지를 판단하는 오버해드는 여전하다.

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

## 스택일어 (スタック日本語)

한국어의 "스택-"접두조사를 "スター"로 번역했다 (발음의 편의를 위함).

(어짜피 "스택-"접두조사도 형식언어이론의 전문용어이기에, 서양놈들꺼지 교착어 어원이 아니라 번역 불확정성 문제는 이미 한국어에서도 저질렀기에 별 문제없다 생각했다. ㅋㅋ)

## 주의사항

O* V어순이란, 스택형 ("스택-"접두조사가 붙은 V의 형(type)) 동사 V가 이루는 어순으로 클레이니 스타다 보니, 사실 목적어가 없을수도 있기도 하다.

O* V어순 정규화 문법 (표준 문법) : 클래이니 스타가 붙은 목적어들의 나열은 쉼표를 통해 연결한다. 이런 정규 형태만 "형식화된 TOS"로 옮기기 용이하기 때문.

tip : 정규화 문법이 아닌 비표준 문법은 모두 결론적으로 정규화 문법으로 컴파일된다. 동형이기 때문. 자유롭게 즐기자. (C든 기계어든, 결과적으로 기계어인데 뭔상관이냐는 시선)

### 조사에 대한 주의사항

-함 (동사 to 명사), -적 (형용사 to 부사등 수식레벨을 올림), -임 (라틴어 be동사 "est"의 아이디어. 형용사 • 부사 등의 명사화), "10시임"이따구로 굳이 "-임"이나 "-함"을 붙일 필요가 없는데 "-임"이나 "-함"을 붙이는거. "역동임"은 문법적으로 틀림으로, "역동적임"으로 명사가 아닌 형용사를 명사화하거나 하는 미친놈짓을 해서 진행시킴. 제작자는 조사를 어려워하지 않음. 교착굴절로 사고하는 한국인이니까 (촘스키가 말한 "언어 = 사고"의 관점에서, 한국인은 한국어로 사고함). 단지, 스택국어는 제작자의 광적인 "저수준화 • 수학모델화 • 형식화는 형이상학적이니 허무하고 아무 권위도 없지만, 이과들에게는 조화로움의 아름다움이다."라는 집착으로 인해 탄생한 배설작임. 기본적으로 프로그래밍 언어를 만들면 esolang의 형식주의적 요소를 차용할정도의 또라이임. 에초에 조사 학습의 어려움을 지우려는 의도는 1도 없었음. 조사도 굴절의 형식화된 형태로써 아름답다고 느끼는 상 또라이임

### 형식화에 대한 나의 개똥철학 (주의사항 : 음모론급 독자해석임.)

이 체계는 자연어를 통제하려는 의도가 아니님.
자연어 의미론은 통제 불능이라고 생각함.
그러나 자연어 문법을 통제할수 있으면, ZFC위의 문자열에서, 자연어 문자열을 통제하므로써, 자연어 단어의 **실제의미론(실제의미론 관점이라고, 화용론은 속뜻이고 의미론이 겉뜻이므로, 속뜻과 겉뜻이 일치해야 겉뜻이 참뜻(진짜뜻)이며, 속뜻만이 유일한 참뜻이라는 관점으로 이사상도 작성자의 음모론에 가깝다. 실제의미론은 실제의미론 관점레서 화용론을 이르는 말이다.)**만 알고 있으면, 단어들을 적절히 배치하는 용도로 쓸수 있음.
비형식 의미론은 문자열에 격리해서 해석은 안하고, 통사론만 조작해서, 자동 작문기를 만들면 무모순-문장이나 모순-문장이 나오지 비문(문법적으로 틀린 문장)은 형식적인 문법선이서 컷할수 있임. 그걸 즐기려는거님.... 그리고 무모순-문장과 모순-문장은 형식적-무모순-문장(형식적으로 무모순), 형식적-모순-문장(형식적으로 모순), 비형식적-무모순-문장(자연어 화용론의 보편적인 고정관념상 "this is truth (이게 맞다.)"고 검증없이 우겨지는 사회 통념 (배외측 전전두피질이 처리함)으로, 형식적-모순-문장이거나, 사실에 대응하지 않고 항진인 명제이거나 (비트겐슈타인이 말한 의미 결여한 명제), "참"이라는 단어의 의미는 형식적 참이 아니라, 비형식적-무모순-문장의 집합과, 비형식적-무모순-문장중 인과관계인 문장이 있으면, 그 인과관계를 추론규칙으로 삼는 증명이론의 논리(비형식적 논리)를 사용하는 "참"임.) 비형식적-모순-문장 (비형식적 논리에서 거짓)로 나뉨.. (논리가 비형식적인 부분을 형식에서 조작해서, 넘겨주고, printf결괏값을 인간이 보는걸 할수 있잖슴. 얼마나 제어가 재미있겠음 ㅋㅋ 으히히.) 그런데, 언어의 한계는 내 새계의 한계 (비트겐슈타인)에서, 모순-문장을 참으로 긍정하는 행위도 엄연히 언어에서의 사고임. 화용론을 조작하는 행위임. 모순-문장은 언어의 한계가 아님. 대표적으로, 인간의 이데올로기같은 meme등은 고맥락 문화에서는, 보편 논리와 충돌하는 경우가 적지만, 사실 고맥락이든 저맥락이든, 충돌하는 경우가 존재함. 에초에, 비형식적-무모순-문장의 "참"이라는것 자체를 언어 사용자가 긍정하는데로 결정되기에, 자기 자신만의 의미해석을 추가하면 (언어의 사회성을 무시하는 독자적 해석의 오류), 독자적 해석의 오류를 통해서, 독자적 해석으로 변형된 언어도 쓸수있는거임. 독자적 해석으로 변형된 언어를 포함한 언어가 "내 새상의 한계 (비트겐슈타인)"임 ㅋㅋ 문법만 맞으면 형식적으로 조작하는 모든거를 허용할 필요가 있다는거임.

주변의 사람이 다 죽거나, 모두가 동의하면 언어는 바뀌지.