# CoffeeFunctions & analytic

C⁰(S)(f) : S ⊆ dom f ∧ (∀a ∈ S, ∀ε > 0, ∃δ > 0, ∀x ∈ S, |x - a| < δ → |f(x) - f(a)| < ε)
D¹(S)(f) : C⁰(S)(f) ∧ (∀a ∈ S, ∀ε > 0, ∃δ > 0, ∀x ∈ S, 0 < |x - a| < δ → |((f(x) - f(a))/(x - a)) - (((d f)/(d x))(x))| < ε)
Dⁿ(S)(f) : C⁽ⁿ⁻¹⁾(S)(f), D¹(S)((d⁽ⁿ⁻¹⁾ f)/(d x⁽ⁿ⁻¹⁾))
Cⁿ(S)(f) : Dⁿ(S)(f) ∧ C⁽ⁿ⁻¹⁾(S)(df/dx)

Coffee<S>ₙ(f)(a)ₖ ≜ (ϝ n : ℕ₀. (ϝ f : Cⁿ(S). (ϝ a : S. (ϝ k : [0, n + 1) ∩ ℕ₀. ((dᵏ f)/(d xᵏ))(a)/(k!) : ∪ₘ₌₀ⁿ codom ((dᵐ f)/(d xᵐ))) : 𝔉([0, n + 1) ∩ ℕ₀, ∪ₘ₌₀ⁿ codom ((dᵐ f)/(d xᵐ)))) : {y ∈ 𝔉(S, 𝔉([0, n + 1) ∩ ℕ₀, ∪ₘ₌₀ⁿ codom ((dᵐ f)/(d xᵐ)))) | Cⁿ(S)(f)}) : 𝔉(ℕ₀, {y ∈ 𝔉(S, 𝔉([0, n + 1) ∩ ℕ₀, ∪ₘ₌₀ⁿ codom ((dᵐ f)/(d xᵐ)))) | Cⁿ(S)(f)))(n)(f)(a)(k)

커피밖에 왜 생각이 안나지 (MyBrainIsFuckingCoffee<<퍽퍽)

Base<S>ₙ(f)(a)ₖ ≜ (ϝ n : ℕ₀. (ϝ f : Cⁿ(S). (ϝ a : S. (ϝ k : [0, n + 1) ∩ ℕ₀. (ϝ x : S. (x - a)ᵏ : codom f) : 𝔉(S, codom f)) : 𝔉([0, n + 1) ∩ ℕ₀, 𝔉(S, codom f))) : {y ∈ 𝔉(S, 𝔉([0, n + 1) ∩ ℕ₀, 𝔉(S, codom f))) | Cⁿ(S) f}) : 𝔉(ℕ₀, ∪ₘ₌₀ⁿ 𝔉(Cⁿ(S), {y ∈ 𝔉(S, 𝔉([0, n + 1) ∩ ℕ₀, 𝔉(S, codom f))) | Cⁿ(S) f})))(n)(f)(a)ₖ

Coffee2Func<S>ₙ(f)(a)(cof) ≜ (ϝ n : ℕ₀. (ϝ f : Cⁿ(S). (ϝ a : S. (ϝ cof : codom Coffee<S>ₙ(f)(a). Σₖ₌₀ⁿ cofₖ × Base<S>ₙ(f)(a)ₖ : 𝔉(S, codom f)) : {y ∈ 𝔉(S, codom Coffee<S>ₙ(f)(a)) | a ∈ S}) : {y ∈ 𝔉(S, {y ∈ 𝔉(S, codom Coffee<S>ₙ(f)(a)) | a ∈ S}) | Cⁿ(S) f}) : ∪ₘ₌₀ⁿ 𝔉(Cⁿ(S), {y ∈ 𝔉(S, {y ∈ 𝔉(S, codom Coffee<S>ₙ(f)(a)) | a ∈ S}) | Cⁿ(S) f}))(n)(f)(a)(cof)

DotProductCoffee<S>ₙ(a)(f, g)ₖ ≜ (ϝ n : ℕ₀. (ϝ a : S. (ϝ (f, g) : Cⁿ(S)². (ϝ k : ℕ₀. Coffee<S>ₙ(f)(a)ₖ Coffee<S>ₙ(g)(a)ₖ : {xy | x ∈ codom Coffee<S>ₙ(f)(a) ∧ y ∈ codom Coffee<S>ₙ(g)(a)}) : {y ∈ 𝔉([0, n + 1) ∩ ℕ₀, {xy | x ∈ codom Coffee<S>ₙ(f)(a) ∧ y ∈ codom Coffee<S>ₙ(g)(a)}) | Cⁿ(S)²(f, g)}) : {y ∈ 𝔉(Cⁿ(S)²(f, g), {y ∈ 𝔉([0, n + 1) ∩ ℕ₀, {xy | x ∈ codom Coffee<S>ₙ(f)(a) ∧ y ∈ codom Coffee<S>ₙ(g)(a)}) | Cⁿ(S)²(f, g)}) | a ∈ S}) : ∪ₘ₌₀ⁿ 𝔉(S, {y ∈ 𝔉([0, n + 1) ∩ ℕ₀, {xy | x ∈ codom Coffee<S>ₙ(f)(a) ∧ y ∈ codom Coffee<S>ₙ(g)(a)}) | Cⁿ(S)²(f, g)}) : {y ∈ 𝔉(Cⁿ(S)²(f, g), {y ∈ 𝔉([0, n + 1) ∩ ℕ₀, {xy | x ∈ codom Coffee<S>ₙ(f)(a) ∧ y ∈ codom Coffee<S>ₙ(g)(a)}) | Cⁿ(S)²(f, g)}) | a ∈ S}))(n)(a)(f, g)(k)

ScalaOf<X, Y>ₙ ≜ (ϝ n : ℕ₀. {y ∈ codom Coffee<X>ₙ(x) | x ∈ 𝔉(X, Y)} : {y ⊆ codom Y | Y = codom Coffee<X>ₙ ∧ n ∈ ℕ₀})(n)
SpaceOf<X, Y>ₙ ≜ (ϝ n : ℕ₀. {f ∈ 𝔉(X, Y) | Cⁿ(X) f ∧ Coffee2Func<X>ₙ(f)(a)(Coffee<X>ₙ(f)(a))} : {f ∈ 𝔉(X, Y) | Cⁿ(X) f ∧ n ∈ ℕ₀})(n)

DotProjecter<S>ₙ(a)(f, g) ≜ h s.t. h = (Coffee2Func<S>ₙ(a)(h) ◦ DotProductCoffee<S>ₙ(a))(f, g)

CoffeeFunctions<X, Y>ₙ(a) ≜ (ϝ n : ℕ₀. (ϝ a : X. <F = ScalaOf<X, Y>ₙ, V = SpaceOf<X, Y>ₙ, +, -, DotProjecter<X>ₙ(a)> : InnerProductSpace) : 𝔉(X, InnerProductSpace))(n)

CoffeeFunctions는 유한차원이다.

analytic<X, Y>(a) ≜ (ϝ a : X. lim_{n ⟶ ∞} CoffeeFunctions<X, Y>ₙ(a) : InnerProductSpace)(a)

analytic는 무한차원이다.

이제 난 C^∞랑 analytic의 차이를 배워야 한다.