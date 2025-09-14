# Quatro

## 유리수체 ℚ를 구성하는 모델 Quatro

Quatro = <𝔻, QMinus, Qrev, Qadder, Qmuler, Qcmp, Qeq>

Quatro는 Polandian-Notation인 연산을 지원한다. 프로그래밍에도 용이해보이고, 선형사상이므로 자연스럽고, 연산자도 중위표기라는 거북한 표기가 아닌, 커링된 함수 표기여서, 훨씬 통쾌한것같다.

텐서 렝크가 3이 넘어가냐고 묻는다면 그건 아니고, 집합 렝크가 그렇냐고 묻는다면 모르겠다.
이름이 Quatro인 이유는 그냥 그게 멋있어서.

사실은 Quatro는 Quatro Real을 만들기 위해서 "Quatro다!"라고 ~~개소리~~ 하기 위해서 Quatro로 지었고 하겠다.

0. Domain

𝔻 ≜ ((𝕍²)² ∪ 𝕍² ∪ 𝕍 [𝕍 := ℤ²]

도메인에서 `(𝕍²)²)²`는 이항연산자 `(𝕍²)²`는 단항연산자고, 𝕍에 대해서, 동치관계 Qeq에 대한 동치류, v ∈ 𝕍, {w | Qeq(v, w)} ∈ ℚ 이도록, 유리수를 구성할 수 있다.

1. Constants

QMinus = <<-1, 0>, <0, 1>>
Qrev = <<0, 1>, <1, 0>>

앞서 말한 기준에서, QMinus와 Qrev는 단항연산자임을 알 수 있다. `QMinus x`는 `-x`를 의미하고, `Qrev x`는 `1/x`를 의미한다.

Qadder = <<<0, 1>, <1, 0>>, <<0, 0>, <0, 1>>>
Qmuler = <<<1, 0>, <0, 0>>, <<0, 0>, <0, 1>>>

앞서 말한 기준에서, Qadder와 Qmuler는 이항연산자임을 알 수 있다. `Qadder x y`는 `x + y`이고, `Qmuler x y`는 `xy`를 의미함도 알 수 있다.

2. Functions

Qcmp(v, w) = ((Qadder (QMinus w)) v) • e₁

Qcmp는 단순히 v - w의 분모는 저리치우고, 분자를 따진다. 이건 더이상 선형이 아니다.

3. Relation

Qeq(v, w) : Qcmp(v, w) = 0

겉보기엔 Qcmp의 근을 나타내는 방정식의 해집합 Qeq로 술어 내지 관계를 만든것 같지만, Qcmp의 근은 유리수체에서 `v = w`를 의미하므로, 동치관걔임을 알 수 있다.

유리수 p, q에 대해, p - q = 0시, p - q = 0 = q - p이므로, 가환이고, p = a/b이고, q = c/d 일시,
p - q = (ad - bc)/bd 이므로, 완전히 비율로 취급하고 계산하는것이라서, a:b = c:d이면, Qeq(<a, b>, <c, d>)이므로,

a:b:c = d:e:f에서,

Qeq(<a, d>, <b, e>), Qeq(<b, e>, <c, f>) ⊨ Qeq(<a, d>, <c, f>)임은,

r = a:b, R = b:c에서,
a = br, b = cR, a = crR에서,

에초에, w:x = y:z부터, t = w:x로 잡았을때,

xy = xzt = xtz = wz 이므로,

a = br에서도, b = cR에서도, a = c(rR)에서도 마찬가지임을 알 수 있고,

이런식으로 계산되는것이 애초에 비례식과 분수의 덧•뺄셈의 본질적인(Immediatly) 부분이므로, 

a:b:c = d:e:f에서 당연하다는 한마디로 정리된다.

### 선설명 : Qrev, Qadder, Qcmp, Qmuler, QMinus, Qeq

첫번째 쳅터로, 연산자들을 정의해보자.

Qadder ≜ <<<0, 1>, <1, 0>>, <<0, 0>, <0, 1>>>

열벡터에 대해, 
<0, 1>, <1, 0> | a | b, a
<0, 0>, <0, 1> | b | 0, b

즉,
Qadder <a, b> = <<b, a>, <0, b>>

따라서, 이에 <c, d>를 적용하면,

b, a | c | bc + ad
0, b | d | bd

아주 훌륭하게 연산자가 정의된다.

Qmuler ≜ <<<1, 0>, <0, 0>>, <<0, 0>, <0, 1>>>

열벡터에 대해,
<1, 0>, <0, 0> | a | a, 0
<0, 0>, <0, 1> | b | 0, b

즉,

Qmuler <a, b> = <<a, 0>, <0, b>>

따라서, 이에 <c, d>를 적용하면,

a 0 | c | ac
0 b | d | bd

아주 훌륭하게 연산자가 정의된다.

두번째 쳅터로, 동치관계를 주는 부분을 해보고 싶다.

(a : b = c : d) : ad = bc 로,
(a : b = c : d) : ad - bc = 0 이므로,

아주 정확히 v - w = 0일시 동등하므로,

뺄셈 연산자를 구해야 한다.

Qmuler <-1, 1> = <<-1, 0>, <0, 1>>

혹은

QMinus ≜ Qmuler <1, -1> = <<1, 0>, <0, -1>>

애서, QMinus가 -x 역할을 하는 연산자이므로,

(Qadder QMinus w) 가 (-w) 일것이므로,

해당 연산자를 구하면 된다. 젠장 함수합성시 선형이 아니라서, 선형사상이 아니다...

뭐 그럴만도 하지...

앞으로 QMinus는 여기서 정의한거다.

다음 함수를 보자.

Qcmp(v, w) ≜ ((Qadder (QMinus w)) v) • e₁

이건 비교 함수이다.

이제 우리는 Qadder, Qcmp, Qmuler QMinus를 모두 정의하였다.

참고로, Qrev = <<0, 1>, <1, 0>> 에서, Qrev x는 x의 역수를 구해주는 함수이다.

이렇게 우리는 이제 우리는 Qrev, Qadder, Qcmp, Qmuler, QMinus를 모두 정의하개 될 수 있는것이다.

그리고 이제야말로 진짜로 두번째 쳅터인 동치관계 정의로 넘어간다.

사실은 아까전에는 훼이크였기 때문이다.

두번째 쳅터로, 동치관계를 정의해보자.

v = <a, b> 이고, w = <c, d> 일때,

a : b = c : d 인 동치관계는,

다음 방정식 Φ로 서술된다.

Qeq(v, w) : Qcmp(v, w) = 0

위 방정식은 어떻게 보면 술어이자 관계이다.

의미론적으로 볼때, 유리수체 위의 뺄셈 함수의 방정식에 대해, x - y = 0 ↔ x = y이기에
방정식을 만족하는 해집합 Qeq에 대해, (v, w) ∈ Qeq ↔ ((v, w) ⊨ Qeq) ↔ Qeq(v, w)이기에, 이 술어이자 관계 Qeq는 유리수체 위의 동치관계를 노리고 코딩하였음을 쉽게 알 수 있다.

이하에서 Qrev, Qadder, Qcmp, Qmuler, QMinus, Qeq를 모두 설명했다.

### 후명세 : Qrev, Qadder, Qcmp, Qmuler, QMinus, Qeq

0. Domain

𝔻 ≜ ((𝕍²)²)² ∪ (𝕍²)² ∪ 𝕍² ∪ 𝕍 [𝕍 := ℤ²]

1. Constants

Qminus = <<-1, 0>, <0, 1>>
Qrev = <<0, 1>, <1, 0>>
Qadder = <<<0, 1>, <1, 0>>, <<0, 0>, <0, 1>>>
Qmuler = <<<1, 0>, <0, 0>>, <<0, 0>, <0, 1>>>

2. Functions

Qcmp(v, w) = ((Qadder (QMinus w)) v) • e₁

3. Relation

Qeq(v, w) : Qcmp(v, w) = 0

이렇게 Qrev, Qadder, Qcmp, Qmuler, QMinus, Qeq가 명세된다.

## Quatro Real

Quatro Real은 두가지 파트로 구성된다.

1. Quatro Relation System Metrix
2. Quatro Number

그리고,

Quatro Relation System Metrix와 Quatro Number도 두가지로 구성된다.

먼저, Quatro Relation System Metrix는
1. QRSM FakeLog Model
2. QRSM Standard Inclusive Model

그리고, Quatro Number는,
1. QN Cauchy Sequence
2. QN Ultraproduct Sequence

QRSM FakeLog Model부터 보자.

### QRSM FakeLog Model

QRSM FakeLog Model은 다음과 같은 모델이다.

(근데 내가보기에는 Lava시스템 기준에서는 걍 대수구조급으로 단순힌 모델인데)

QFLM ≜ <ℚ ∪ ℤⁿ ∪ {S | S ⊆ ℕ}, ¥, gcd, lcm, fac, p, ₩, $, €, FakeLog> [n := ∞]

#### QFLM 선명세

이번엔 명세가 먼저다.

0. Domain

1. Constants

¥ ≜ Σ $

¥가 무한합인데, 정의되는 이유는 $를 참고하라.

2. Functions

gcd S ≜ if (|S| = 1) {
    return x s.t. x ∈ S
} else if (|S| = 2) {
   if (0 ∈ S) {
       return x s.t. 0 ≠ x ∈ S
   } else {
       return gcd {min S, (max S) mod (min S)}
   }
} else {
    return gcd {gcd (S - {min S}), min S}
}

와... 함수 분기가 너무 많아가지고, 거의 psudo code급.. ㄷㄷ

gcd가 집합을 인자로 받은 이유는, 가환 반군을 이루기 때문이다. 사실 가환군을 이루는지 가환군을 이루는지는, 잘 모르겠고, 에초에 군을 이루면 반군도 이루니까....

암튼 gcd에서, |S| = 2일때의 처리는 유클리드 호제법의 처리이다. base condition은 0 ∈ S이며, 이때는 인자를 리턴해주므로, Tail Requation이다.

lcm S ≜ (Π S)/(gcd S)

이렇게 정의한 이유는,
Π S = (lcm S)(gcd S)이기 때문이다.

수열의 곱인 파이 `Π`가 집합을 받은 이유는, 시그마 `Σ`처럼, 집합 내를 일괄적으로 계산하는걸 나타냈기 때문이다.

에초에 시그마와 파이가 기존의 gcd(x, y)및 lcm(x, y)처럼 적어도 기환반군을 이루는 연산자들은 저런식으로, 집합을 인자로 두어 코딩할수 있기에, 의미론적으로 동일한 feature를 만들수 있다는거다.

참고로, 나는 feature를 코딩하는 관점에서, 어떤 객체의 구성을 설명할수 있다는 사실에서, 엘런 튜링이 생각했듯, 수학을 코딩처럼 보고 정리하는 방식도 탁월하다고 본다.

pₙ ≜ if (n = 0) {
    return 1
} else {
    return min {x | ∀k ∈ ℕ₀ ∩ (, k), gcd {pₖ, x} = 1}
}

이렇게 정의하면 p₀ = 1이 소수인지 아닌지는, 수열 인자에 0부터 시작할것인지 정하는것과 같다.

그리고 0이 Natural한지 혹은 1이 소수인지는 재미없는 주제이니 넘어가자.

₩ₙ ≜ if (n = 0) {
    return -1
} else {
    return pₙ
}

위에 있는 유사소수열 ₩ₙ에서, ₩₀ = -1 이므로, 정수의 소인수분해에 매우 유용하다.
특히 𝕍 = 𝔹 × ℕ₀ⁿ [𝔹 := {0, 1}][n := ∞]인 𝕍로 소인수분해할것이라면 금상첨화.

그런데 같은방법으로, 유리수를 소인수분해할수 있다는 사실은 우리를 소름돋게 한다.

$ₙ ≜ FakeLog(₩ₙ₋₁)eₙ

그렇다. $ₙ은 fac에서 말할 친구이다.

€ ≜ (• ¥)

€가 내적 기호에 대한 Functor를 쓴걸 알 수 있는데, ¥가 뭔지는 상수 목록 참고.

FakeLog(x) ≜ €(fac(x))

이게 뭘 의미하는지는 곧 알게 될거다. fac을 통해서 말이다.

fac(x) ≜ if (x < 0) {
    return <1, f(x)>
} else {
    return <0, f(x)>
} [f(x) := if (x ∈ ℕ) {
    return g(x, 1, Σₖ 0eₖ)
} else {
   return f(first(x)) - f(last(x))
}] [g(x, k, ret) ≜ if(x = 1) {
    retuen ret
} else if (gcd(x, pₖ) = pₖ) {
    return gcd(x/pₖ, k, ret + $ₙ)
} else {
    return gcd(x, k + 1, ret)
}] [first(x, y) := x] [last(x, y) := y] [COMMENT := ("g는 평범한 자연수 소인수분해 알고리즘이다... 원래는 while문을 이용해서, pₖ으로 나눠지지 않을때까지 나누면서, 리턴값인 벡터에, 소인수의 지수를 적어야하는데, 여기는 그런거 없으니, tail Requation의 flow를 이용했다. 솔찍히 어떻게 되더라도, 명세만 만족하멷 된다. (Tip : fac(1) = <0, ..., 0>이기에, 인자로 받은 리턴값 ret을 리턴하는거다. (Tip : 마지막 else는 나눠지지 않을때, 다음 소수에 대한 처리다. (Tip : 의도한대로 실행되는 이유는 처리 흐름을 따라가보면 알 수 있다.))", "x < 0인경우는 따로 음수 비트를 활성화하는것 뿐이니 나머지 부분을 설명해보자. f에서, 자연수가 아니면 f(first(x)) - f(last(x))로 처리하는걸 보았을것이다. 이걸 해설해보이겠다.", "벡터는 튜플이므로, first(<x, y>) = x이며, last(<x, y>) = y에서, f(first(x : y)) - f(last(x : y)) = f(x) - f(y)인것이다. 이게 `핵심`")]