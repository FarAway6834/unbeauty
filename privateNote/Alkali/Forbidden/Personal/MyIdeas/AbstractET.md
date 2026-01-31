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

## 주의사항

타입 시스템이라는 말이 프로그래밍에 주로 쓰여서 오해를 방지하기 위해 한가지 명시하겟다.

이건 수학용 타입 시스템이다. 뭣같은 코딩이 아니고.
