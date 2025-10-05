# Quatro (미완성)

## ideas

`<ℝ ∪ ℝ*, *, ᵤ, st>`인 대수구조는 전달원리, 울트라곱 구성, 표준부분원리까지 세가지 함수가 정의된 신기한 대수구조네? ㅋㅋㅋ
`o.o* ≜ <ℝ ∪ ℝ*, *, ᵤ, st>`로 정의하자.
p-adic은 언어(문자셋)를 L = Z/pₖZ를 놓았을네, 기수법에서의 덧셈 • 뻴셈 • 곱셈 • 나눗셈 • 로그 • 지수 • 기타 하이퍼연산 등이 정의된 무한 문자 시퀀스와 동형이네? ㅋㅋㅋ 이런 언어 L을 `adₖ`라고 할께. 수열인 이유는 pₖⁿ [n := ∞]와 동형이니까.

```
Φ₁(v, w, *) : v₁ * w₂= w₁ * v₂
G(a, *, k) : {b | Φₖ(a, b, *)}
Φ₂(v, w, *) : ∀k ∈ ℕ, Φ₁(<vₖ, wₖ>, <v₁, w₁>, *)

a ; b ≜ G(<a, b>, +, 1)
v₁ ; ... ; vₙ ≜ G(Σₖ vₖ [k := 1 ~ n], +, 1
a : b ≜ G(<a, b>, ×, 1)
v₁ : ... : vₙ ≜ G(Σₖ vₖ [k := 1 ~ n], ×, 1)
```
이거 만드려고...

이러니까 확실히, v₁ ; ... ; vₙ가 각 차가 일정하고, 벡터 위치가 달라도 같으니까, 아핀 공간의 원소네

G(<v₁, ..., vₙ>, pow, k)는? 항상Φ₁(log(v₁, w₁), log(vₙ, wₙ), pow)니까, 자연로그의 비네.

에초에,
G(<a, b>, ×, k)는, G(<ln a, ln b>, +, k)와 동형이고,
G(<a, b>, ↑, k)는, G(<ln a, ln b>, ×, k)와 동형이고,
G(<a, b>, ↑ⁿ, k)는, G(<ln a, ln b>, ↑ⁿ⁻¹, k)와 동형이니까, 모든 하이퍼연산에 대해 성립하네.

동형인 이유는 동치류는 집합 S인데, 집합 P, Q에 대해,
Q = f(P) = {ln x | x ∈ P}
인 동형사상이 존재하니까.

그러면 이러한 G를 Grandpiano라고 할께.

에초에 ZFC에서 정수와 유리수의 정의를 보면, 역산으로 간주할 튜플의 동치류로 구성하니까, Grandpiano는 그러한 하이퍼연산의 역연산들을 닫혀있게 구성해주는 함수네?

잠시만, 그러면 유리수체에서, Cauchy Sequence를 만들어 놓으면, `o.o*`를 구성할 수 있고, `o.o*`에서는 `adₖ`를 구성할 수 있는데?

잘생각해봤는데 말이야, 무한 문자 시퀀스 t에 대해, f(x) = tₕ pₖʰ로 놓고, f는 자연수에서 정의된 함수이므로, 극한을 취한 무한합의 역할을 해줄만함건 부정적분이므로, ∫ f(x) dx가 p-adic을 원래대로 되돌리는 함수같은데?

그러면 daₖ(t) ≜ f(pₖ) [n! (dⁿ/dxⁿ) f(x) := tʰ]인 메클로린 급수 f에 대해서 잘만 표현되네.

이렇게 p-adic의 의미하는 값으로 수렴하는 함수를 da라고 하겠음

그러면, `<ℝ ∪ ℝ* ∪ {adₖ | k ∈ ℕ} ∪ {{{adₖ | k ∈ ℕ}}, *, ᵤ, st, da, ad>`는 함수 ad를 이용하여 언어를 만들수 있고, da를 이용하여 복귀할수 있는 기능을 `o.o*`에 추가시킨 셈이니, 이를 `σ.σ* ≜ <ℝ ∪ ℝ* ∪ {adₖ | k ∈ ℕ} ∪ {{{adₖ | k ∈ ℕ}}, *, ᵤ, st, da, ad>`로 정의해서, `σ.σ*`라 하겠음.

Grandpiano로 구성된 유리수체 모델을 구현이 특별하는 특별히 `comQ`라고 하겠음

comQ위에서 정의된 `σ.σ*`를 특별히 `α.α*`라고 하겠음.

(a : b) ± (c : d)는, 에초에 <a, b>, <c, d>라는 베이수 수준에서,
Gigachad(±, <a, b>, <c, d>) ≜ <ad ± bc, bd>로 정의한 기가차드 함수에서, Gigachader := λx. λy. Gigachad(x, y)로 정의하면, kuratowski 쌍의 제귀적 정의를 이용하면, Gigachader(±)(x, y) = Gigachad(±, x, y)이므로, 연산자답게 중위표기해주면,
x Gigachader(±) y = Gigachad(±, x, y)
따라서, (a : b) ± (c : d) = G(<a, b> Gigachader(±) <c, d>, ×, 1)로 연산을 정의해서, 연산을 준다.

사실은 곱셈은 루프(Loop, 가환인 유사군)와 가환환을 동시에 이루므로, 역연산이라는 툴으로, 함수의 이항을 구현해서, 비례식과 동형임을 증명할 수 있어, 일관성이 깨지지 않기에, 저런식으로 정의하는것.

에초에 유클리드 공간에서 단위길이의 선분 OX와, 선분 OX에서 X방향으로 무한히 연장한 반직선 OX에 대해, 선분 OX위에 없고, 반직선 OX위에 있는 점 P에 대해, 선분 OP의 길이를 t로 두자.
직각을 유일하므로, 컴퍼스를 통해 이미 구성되어있는 직각을 작도하여 (구성주의적으로 할수있을거라 가정한것 뿐), 반직선 OX와 수직인 반직선 OX`을 그린다. 그리고 선분 OP를 컴퍼스를 이용하여 원호를 그리고, 반직선 OX`와 만나는 점을 P`이라고 하자, 이제 자를 통해 선분 PX`및 XP`를 그리면, 직각삼각형 ΔOX`P와 직각삼각형 ΔOXP`은 합동이다. 즉, 우리는 ΔOX`P에 대해, 이를 y=x에 대해 대칭이동한것을 작도한것이다. 마지막으로, 선분 P`X와 평행하고, 점 X`을 지나는 직선 X`T를 그어주고, 직선 X`T가 선분 OX와 만나는 점이 T이다.
이러한 과정을 통해 단위선분 OX의 1:P-1 외분점 P가 존재하여, OP에 대해, 그것의 역수 길이 선분은, OT로 작도 가능하여 존재하고, OT는 기하학적 선분으로 t배하면, OX이므로, 합과 곱을 아름답게 정의할 수 있다.

사실 딱히 아름답다고 생각하지 않지만, "잘 정의되됨"과 "잘 작동함"을 동시에 쓰기 귀찮아서 아름답게 정의된다고 말함.

정수에서 다음 단항연산을 정의함.
-x ≜ 0 - x

x = x ↔ x - x = 0임.

정수에서 덧셈, 뺄셈이 정의된다 가정하면 다음을 만족한다.

1.1. x = -|x| ↔ x - (-|x|) = -|x| - (-|x|) = 0 ↔ - (-|x|) = |x|임. 따라서, 범자연수 x에 대해, -(-x) = x
1.2. 음의 정수 x에 대해, x = -|x|에서, -(-x) = -(-(-|x|)) = -(|x|) = x
1.3. 따라서, 1.1. 및 1.2.에 따라서, 정수 x에 대해, -(-x) = x이며, 특히, -(-1) = 1
2.1. 범자연수 x에 대해, (-1)x = -x
2.2. 음의 정수 x에 대해, (-1)|x| = -|x| = x에서, -(-1)|x| = -x = |x| = -(-|x|) = -((-1)|x|)에서,

아시바 증명이 뭔가 이상한데 ㅋㅋ 오늘은 여기까지.

오늘에서는 결과적으로 `σ.σ*`라는 거대한 수 체계를 만드는 구성인 `α.α*`을 만들었네. 그러면서 Grandpiano를 이용하여, 하이퍼연산과 그 역연산에서 닫힘을 보장하며, 이를 통해서 아핀공간의 벡터와, 비, 그리고 여러 Grandpiano류 대수들을 만들었네. 그래서 Grandpiano류 대수와 `α.α*`구성을 통한 `σ.σ*`대수를 통해서, n중차, n중비를 다루며, 동시에 p-adic • hyperrealfield까지 다룰수 있으니 일석 이조고, 이걸로 n² 행렬인 벡터의 코벡터를 만들어서, 복소수, 분할복소수, 멱등원, 사원수, 팔원수 등을 만들 수 있겠네

컴퓨터 구현시에서는 p-adic, hyperreal, real, fraction을 각각 다룰때 자료형을 만들어서 변환하는걸로 생각하면 되겠네.

소인수분해시에는 고전 소수열 pₖ = 1 if k = 0 else pₗ s.t. pₗ = inf {gcdᵢ pᵢ = 1 [i := 1 ~ k]}에, 최대공약수 gcd(x, y) ≜ x if y = 0 else gcd(y, x mod y)및 최소공배수 lcm(x, y) = xy/gcd(x, y)를 만들수 있으고 특히 최대공약수는 가환모노이드니, pₖ가 옳고 (오 시바 ㅋㅋ 삼성키보드 사용하기 뭣같아서 육성으로 욕나왔넼ㅋㅋㅋㅋ) 새로 만든 정수용 소인수열 ₩ₖ ≜ cis(π) if k = 0 else pₖ에서, 단위로그눈금자 alₖ ≜ ln(₩ₖ)에 대해, ln이 자료형인 형태로 소인수분해 결과를 뱉을수 있겠네.

함수 제작같은 경우에는, Rₘ(M)ₙ(V) ≜ Σₖ (ln(Σᵢ Vₜ) - Vₖ)eₖ [t := Mₖᵢ][k := 1 ~ m][i := 1 ~ n]에서, 음함수, Rₘ(M)ₙ(V) = 0꼴로, 실수 미지수가 V에 생기고, 요기서, V₁ ↦ V₂가 실수, V₃ ↦ V₄로 가는 실수열을 각각 코시수열과 초실수 제작용 수열로 보면 이미 있을건 다 있겠네. 이런 방식을 근본-nibble-array라는 뜻으로 NewageNibleArray라고 부르면 되겠네. 이미 이걸로 연립방정식 재작은 다 케리되니까 사실상 행렬 M이 실수 생성 행렬이 되는거고. R을 Relator라고 해야지. 그러면, 아싸존애 정의한 ln이 ln(x + y) ≜ ln(x) + ln(y)하면 자동으로 자연로그가 되기에 (복소로그의 정의상, 저런 일반화 로그는 복소로그의 정의로 귀결되어, 항상 ln임), 이전 정의도 가저온거고, 이 시스템을 Relator와 NewageNibleArray라고 부르면 되겠네, 이때 실수 • 초실수의 정의는 `α.α*`를 쓰고. 이걸 `oωo*`라고 부름 되겠군

이거완전 복잡한 부분은 거의 행렬기반이니까, 쉽게 컴퓨터에 구현 가능하고, 자동증명용 • 형식증명검증으로도 용이할듯. 나머지 부분에서 실수같은 비 대수적 부분은 자료형으로 만들기 용이하고, 타입케스팅 함수도 있으니. `oωο*`로 프로그래밍 시스템 만들면, 대박 엄밀할듯

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

 + QMinus = <<-1, 0>, <0, 1>>
 + Qrev = <<0, 1>, <1, 0>>

앞서 말한 기준에서, QMinus와 Qrev는 단항연산자임을 알 수 있다. `QMinus x`는 `-x`를 의미하고, `Qrev x`는 `1/x`를 의미한다.

 + Qadder = <<<0, 1>, <1, 0>>, <<0, 0>, <0, 1>>>
 + Qmuler = <<<1, 0>, <0, 0>>, <<0, 0>, <0, 1>>>

Qmuler의 정체가 궁금할수 있으니 말하겠다. 이차원 벡터 v, w에 대해, Qmuler v w는 아다마르 곱 v ∘ w 이다.

앞서 말한 기준에서, Qadder와 Qmuler는 이항연산자임을 알 수 있다. `Qadder x y`는 `x + y`이고, `Qmuler x y`는 `xy`를 의미함도 알 수 있다.

2. Functions

 + Qcmp(v, w) = ((Qadder (QMinus w)) v) • e₁

Qcmp는 단순히 v - w의 분모는 저리치우고, 분자를 따진다. 이건 더이상 선형이 아니다.

3. Relation

 + Qeq(v, w) : Qcmp(v, w) = 0

겉보기엔 Qcmp의 근을 나타내는 방정식의 해집합 Qeq로 술어 내지 관계를 만든것 같지만, Qcmp의 근은 유리수체에서 `v = w`를 의미하므로, 동치관걔임을 알 수 있다.

1. 유리수 p, q에 대해, p - q = 0시, p - q = 0 = q - p이므로, 가환이고, p = a/b이고, q = c/d 일시,
2. p - q = (ad - bc)/bd 이므로, 완전히 비율로 취급하고 계산하는것이라서, a:b = c:d이면, Qeq(<a, b>, <c, d>)이므로,

a:b:c = d:e:f에서,

Qeq(<a, d>, <b, e>), Qeq(<b, e>, <c, f>) ⊨ Qeq(<a, d>, <c, f>)임은,

1. r = a:b, R = b:c에서,
2. a = br, b = cR, a = crR에서,

에초에, w:x = y:z부터, t = w:x로 잡았을때,

xy = xzt = xtz = wz 이므로,

a = br에서도, b = cR에서도, a = c(rR)에서도 마찬가지임을 알 수 있고,

이런식으로 계산되는것이 애초에 비례식과 분수의 덧•뺄셈의 본질적인(Immediatly) 부분이므로, 

a:b:c = d:e:f에서 당연하다는 한마디로 정리된다.

### 선설명 : Qrev, Qadder, Qcmp, Qmuler, QMinus, Qeq

첫번째 쳅터로, 연산자들을 정의해보자.

Qadder ≜ <<<0, 1>, <1, 0>>, <<0, 0>, <0, 1>>>

열벡터에 대해, 
```
[ <0, 1> <1, 0> ][ a ] = [ b a ]
[ <0, 0> <0, 1> ][ b ] = [ 0 b ]
```

즉,
Qadder <a, b> = <<b, a>, <0, b>>

따라서, 이에 <c, d>를 적용하면,

```
[ b, a ][ c ] = [ bc + ad ]
[ 0, b ][ d ] = [   b d   ]
```

아주 훌륭하게 연산자가 정의된다.

Qmuler ≜ <<<1, 0>, <0, 0>>, <<0, 0>, <0, 1>>>

열벡터에 대해,
```
[ <1, 0> <0, 0> ][ a ] = [ a 0 ]
[ <0, 0> <0, 1> ][ b ] = [ 0 b ]
```

즉,

Qmuler <a, b> = <<a, 0>, <0, b>>

따라서, 이에 <c, d>를 적용하면,

```
[ a 0 ][ c ] = [ ac ]
[ 0 b ][ d ] = [ bd ]
```

아주 훌륭하게 연산자가 정의된다.

두번째 쳅터로, 동치관계를 주는 부분을 해보고 싶다.

1. (a : b = c : d) : ad = bc 로,
2. (a : b = c : d) : ad - bc = 0 이므로,

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

1. 의미론적으로 볼때, 유리수체 위의 뺄셈 함수의 방정식에 대해, x - y = 0 ↔ x = y이기에
2. 방정식을 만족하는 해집합 Qeq에 대해, (v, w) ∈ Qeq ↔ ((v, w) ⊨ Qeq) ↔ Qeq(v, w)이기에, 이 술어이자 관계 Qeq는 유리수체 위의 동치관계를 노리고 코딩하였음을 쉽게 알 수 있다.

이하에서 Qrev, Qadder, Qcmp, Qmuler, QMinus, Qeq를 모두 설명했다.

### 후명세 : Qrev, Qadder, Qcmp, Qmuler, QMinus, Qeq

0. Domain

𝔻 ≜ ((𝕍²)² ∪ 𝕍² ∪ 𝕍 [𝕍 := ℤ²]

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

¥가 무한합인데, 정의되는 이유는 $를 참고하라. (보면, $는 기저벡터 e에다가 그 차원번째 순서(0부터 시작해야하는데 축의 차원은 1부터 시작했기에, "차원번째 소수"가 아닌, "차원번매 순서의 소수"라고 한거다. 축의 차원이 t면, t - 1번째 소수인 샘이다)의 소수를 FakeLog를 취해서 곱해준다. )

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

psudo code인 python예제로는,

```python
# req : 3.10 >= version

def gcd(x : set):
    match len(x):
        case 1 :
            ret, = x
        case 2 :
            if 0 in x:
                ret, = x - {0}
            else:
                ret = gcd({min(x), max(x) % min(x)})
        case _:
            ret = gcd({gcd(x - {min(x)}), min(x)})
    
    return ret
```

lcm S ≜ (Π S)/(gcd S)

이렇게 정의한 이유는,
Π S = (lcm S)(gcd S)이기 때문이다.

수열의 곱인 파이 `Π`가 집합을 받은 이유는, 시그마 `Σ`처럼, 집합 내를 일괄적으로 계산하는걸 나타냈기 때문이다.

에초에 시그마와 파이가 기존의 gcd(x, y)및 lcm(x, y)처럼 적어도 기환반군을 이루는 연산자들은 저런식으로, 집합을 인자로 두어 코딩할수 있기에, 의미론적으로 동일한 feature를 만들수 있다는거다.

참고로, 나는 feature를 코딩하는 관점에서, 어떤 객체의 구성을 설명할수 있다는 사실에서, 엘런 튜링이 생각했듯, 수학을 코딩처럼 보고 정리하는 방식도 탁월하다고 본다.

이것도 psudo code인 python으로 보이면,

```python
from math import prod

def lcm(x : set):
    return prod(x)//gcd(x)
```

pₙ ≜ if (n = 0) {
    return 1
} else {
    return min ({x | ∀k ∈ ℕ₀ ∩ (, k), gcd {pₖ, x} = 1} - {0})
}

이렇게 정의하면 p₀ = 1이 소수인지 아닌지는, 수열 인자에 0부터 시작할것인지 정하는것과 같다.

그리고 0이 Natural한지 혹은 1이 소수인지는 재미없는 주제이니 넘어가자.

사실...

>
> 이러한
> 
> p₀ = 1
> 
> pₙ = min ({x | ∀k ∈ ℕ₀ ∩ (, k), gcd {pₖ, x} = 1} - {0})
>
> 수열의 귀납적 정의이다.
>

어떤 n에 대해서도 후자가 존재하기에 소수열은 무한하다. (**중요**) (유클리드가 소수가 무한함을 증명시에, 모든 소수와 서로소인 수를 말했다는점이 주목할것.)

₩ₙ ≜ if (n = 0) {
    return -1
} else {
    return pₙ
}

위에 있는 유사소수열 ₩ₙ에서, ₩₀ = -1 이므로, 정수의 소인수분해에 매우 유용하다.
특히 𝕍 = 𝔹 × ℕ₀ⁿ [𝔹 := {0, 1}][n := ∞]인 𝕍로 소인수분해할것이라면 금상첨화.

이것은 `-1`을 소수처럼 다뤄서, 음의 정수까지 다루기에, 진짜 졍수범위 소인수분해다.

그래서 저것은

>
> 이러한
> 
> ₩₀ = -1
> 
> ₩ₙ = pₙ
>
> 분기별 수열의 정의이다.
>

자, 그런데 같은방법으로, 유리수를 소인수분해할수 있다는 사실은 우리를 소름돋게 한다.

$ₙ ≜ FakeLog(₩ₙ₋₁)eₙ

그렇다. $ₙ은 fac에서 말할 친구이다.

그전에 먼저 €를 소개하겠다.

€ ≜ (• ¥)

€가 내적 기호에 대한 Functor를 쓴걸 알 수 있는데, ¥가 뭔지는 상수 목록 참고.

FakeLog(x) ≜ €(fac(x))

이게 뭘 의미하는지는 곧 알게 될거다. fac을 통해서 말이다.

fac(x) • ¥가 벡터인 fac(x)에 소수열을 곱해주는 모양세이다.

즉, Σ fac(x) • Sₖ 인 형태이다.

왜 이게 될까?

fac(x) ≜ if (x < 0) {
    return <1, f(x)>
} else {
    return <0, f(x)>
} [f(x) := if (x ∈ ℕ) {
    return g(x, 1, Σₖ 0 eₖ)
} else {
   return f(first(x)) - f(last(x))
}] [g(x, k, ret) ≜ if(x = 1) {
    retuen ret
} else if (gcd(x, pₖ) = pₖ) {
    return gcd(x/pₖ, k, ret + $ₙ)
} else {
    return gcd(x, k + 1, ret)
}] [first(x, y) := x] [last(x, y) := y] [COMMENT := ("g는 평범한 자연수 소인수분해 알고리즘이다... 원래는 while문을 이용해서, pₖ으로 나눠지지 않을때까지 나누면서, 리턴값인 벡터에, 소인수의 지수를 적어야하는데, 여기는 그런거 없으니, tail Requation의 flow를 이용했다. 솔찍히 어떻게 되더라도, 명세만 만족하멷 된다. (Tip : fac(1) = <0, ..., 0>이기에, 인자로 받은 리턴값 ret을 리턴하는거다. (Tip : 마지막 else는 나눠지지 않을때, 다음 소수에 대한 처리다. (Tip : 의도한대로 실행되는 이유는 처리 흐름을 따라가보면 알 수 있다.))", "x < 0인경우는 따로 음수 비트를 활성화하는것 뿐이니 나머지 부분을 설명해보자. f에서, 자연수가 아니면 f(first(x)) - f(last(x))로 처리하는걸 보았을것이다. 이걸 해설해보이겠다.", "벡터는 튜플이므로, first(<x, y>) = x이며, last(<x, y>) = y에서, f(first(x : y)) - f(last(x : y)) = f(x) - f(y)인것이다. 이게 `핵심`")]

이해을 돕기 위해 g만 특별히 psudo-code로 써보겠다.
psudo-code용 언어는 python이다.

```python
from its_せかい에_어ㅂㅅ다 import primes, inf_vector

def original_ver(x):
    p = 2
    ret = []
    while x != 1:
        if x % p:
            p += 1
        else:
            x //= p
            ret.append(p)
    return ret

def vector_ver(x, k = 1, ret = inf_vector.full_zero()):
    while x != 1:
        if x % primes(k):
            k += 1
        else:
            x //= primes(k)
            ret[k] += 1
    return ret

def finnally_tailreq_ver(x, k = 1, ret = inf_vector.full_zero()):
    if x == 1:
        return ret
    elif x % primes(k):
        return finnally_tailreq_ver(x, k = k + 1, ret = ret)
    else:
        ret[k] += 1
        return finnally_tailreq_ver(x // primes(k), k, ret)
```

휴... 이정도면 이제 쉬울것이다.

### 후설명

fac(±x/y) = <(1∓1)/2, 0, ..., 0> + fac(x) - fac(y) 이며,

fac(x) = <0, a₁, ..., aₙ> s.t. x = Πₖ (pₖ ↑ aₖ) 이다.

즉, fac(x) • (Σₖ ₩ₖ₋₁ eₖ) = x 이다.

F(x) + F(y) = F(xy)라면,

z = x/y 에 대해, x = yz이므로,

F(z) + F(y) = F(x)에서, F(z) = F(x) - F(y) 이므로,

F(x/y) = F(x) - F(y) ... (1)

Σₖ F(x) = nF(x) = F(Πₖx) = F(xⁿ) [k := 1 ~ n]

F(x) - F(y) = F(x) + F(z) = F(x + z) 에서,

x + z = x - y이므로, z = -y

-F(y) = F(-y)

따라서, 정수 n에 대해, nF(x) = F(xⁿ)

nF(ⁿ√(x)) = F(x)에서, (1/n)F(x) = F(ⁿ√(x))으로, 유리수 p에 대해, pF(x) = F(xⁿ)

유리수 p, q에 대해,
pF(x) + qF(x) = (p + q)F(x) = F(px) + F(qx) = F((p + q)x) ... (2)

이게 코시 수열을 극한으로 보내줬을때도 성립하는 이유는 잘 모른다.

아무튼 (1), (2)에서 F는 로그법칙을 만족한다.

그런데, 정수에 대한 소수 범위에서,

FakeLog(Πₖ (₩ₖ ↑ Aₖ)) = Σₖ Aₖ FakeLog(₩ₖ) 를 만족한다.

즉, 정수 Aₖ에 대해, fₖ(x) = FakeLog(₩ₖx)인 fₖ는 선형이고, 따라서, 정수 Aₖ범위에서 FakeLog는 (1), (2)의 로그법칙을 만족한다 (**중요**) (¤ 핵심임 ¤)

FakeLog(Πₘ pₘⁿ [n:= Aₘ]) = Σₘ FakeLog(pₘⁿ) [n:= Aₘ] 이기에, 유리수체 위에서 로그법칙을 만족하지만, 역함수가 지수함수라는 보장이나, 밑변환이 된다는 보장이 없으니 유사 로그함수이다.

즉, 치역은 "codom FakeLog"이고 이것은 잘 규정된 대상들의 모임이므로, 객체의 모임이고, FakeLog객체인것이다.

아무튼 이러한 방식으로 **유리수에 대해 곱셈과 덧셈과 로그법칙이 적용되는 함수 FakeLog가 정의되어서, 곱셈을 이루기 위해서 소수를 최소원으로, 그 지수를 나열한 벡터를 자료형마냥 다룰수 있는 체계가 준비되었다.**

### QRSM Standard Inclusive Model

QRSM Standard Inclusive Model은 다음과 같은 모델이다.

Quatro로 정의된 유리수 ℚ에 대해, Qrev, QMinus, Qadd, Qmul정의되었으니, Qsub, Qdiv를 각각 f(x, y) = Qadd (QMinus y) x인 f와 f(x, y) = Qmul (Qrev y) x 인 f로 정의하면, Quatro로 유리수체를 준비할 수 있다. 이러한 ℚ를 유리수체로 다루겠다.

다음은 n-QRSM Standard Inclusive Model 이다.

`Mₙ = <((ℚⁿ)ⁿ) ∪ ℚⁿ, zero_vectorₙ, QSIMImplicitFunctionₙ, L_QSIMIFₙ, R_QSIMIFₙ`....



... (작성중) ...