# semiProbability

일단 말하기 앞서 다음과 같이 공리적 확률론을 분할할 생각임.

Kolmogorov’s axioms
 - Probability (including contingent proposition)
 - semiProbability (allow only formal proposition)

## semiProbability on DiscreteUniformDistribution (DUD-semiProb)

표본공간 Ω가 이산균등분포인 경우다.
이 경우 역시 두가지로 나누겠다.

DUD-semiProb
 - Finite-DUDSemiProb (|Ω| < ℵ₀)
 - infinite-DUDSemiProb (|Ω| = ℵ₀)

### Finite-DUDSemiProb (F-DUD-SmPr)

이 경우에는 매우 특이한 상황이 된다.

P(Φ)가 Φ일 확률이라고 치면,

P(Φ) = |Mod(Φ)|/|Ω|

를 만족하기 때문이다.

따라서 이때 두가지를 정의하겠다.

ㄴSIZE ≜ |Ω|
ㄴNumberOfCase ≜ ㄴSIZE P

굳이 `ㄴ`을 쓴 이유는 원래는 `ㄱSIZE`, `ㄱNumberOfCase`와 같이 써서 혹시모를 중복을 피하려고 했는데, `ㄱ`이 부정(Nagation) 기호같이 생긴 탓에 `ㄴ`을 골랐다.

표본공간의 측도가 ㄴSIZE이 되고, 경우의 수가 ㄴNumberOfCase가 되는데, P(Φ) = |Mod(Φ)|/|Ω|이기에,
이런 P를 ㄴSIZE배 해준 ㄴSIZE P는  |Mod(Φ)|이기에, ㄴNumberOfCase는 |Mod(Φ)|이다.

이렇게 두가지 심볼 ㄴSIZE 및 ㄴNumberOfCase가 정의된 모델을 ㄴStatisticalMetaSystem 이라 하겠다.

#### ㄴStatisticalMetaSystem

ㄴStatisticalMetaSystem는 다음 Symbol이 정의되고 다음 Axiom이 만족된 Kolmogorov’s Axioms & ZFC 위의 Model Structure이다.

1. Constant Symbol Assignment

ㄴSIZE ≜ |Ω|

2. Function Symbol Assignment

ㄴNumberOfCase ≜ ㄴSIZE P

3. ㄴStatisticalMetaSystem Axioms

∀A ⊆ Ω, P(A) = |A|/|Ω|

4. ㄴSMS Notation (선택사항, 그냥 표기 방식 명시)

ㄴNumberOfCase(Predicate)
 = ㄴNumberOfCase(Predicate ∩ Ω
 = ㄴNumberOfCase(Mod(Predicate) ∩ Ω)

식으로, 어떤 명제를 술어로 다루겠다는거. 어짜피 술어가 집합이니까 이 표기법은 옳은 표기법이지만, 명확히 할 필요가 있음.

이하에서, ㄴSIZE = t면, 그 ㄴStatisticalMetaSystem을 t-ㄴSMS 라고 하겠다.

t-ㄴSMS에서, 케이스의 수 (ㄴNumberOfCase)는 술어(=문장)가 만족되는 케이스의 수이기에, 모델집합의 카디널을 다루는것이다.

또한 이건, 