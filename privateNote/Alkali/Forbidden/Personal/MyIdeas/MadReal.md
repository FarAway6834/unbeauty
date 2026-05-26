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
1. ∀h, h(x) = (p(x)?(h◦f):g)(x) → h ∉ oper(ℚ)

Tip : 어떤 실수 x에 대해서 단 한번이라도, h가 정의 안됨은, 그 x에서 무한 루프에 갇힌다는거다.

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

Functional Programmible Halting Problem : ker TailReqOpt를 구하는 일관된 알고리즘은 존재하지 않는다.