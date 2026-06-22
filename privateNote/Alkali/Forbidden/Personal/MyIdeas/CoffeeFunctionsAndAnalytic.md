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

CoffeeScript<S>ₙ(f)(a) ≜ (ϝ n : ℕ₀. (ϝ f : Cⁿ(S). (ϝ a : S. Coffee2Func<X>ₙ(f)(a)(Coffee<X>ₙ(f)(a)) : Cⁿ(S)) : 𝔉(S, Cⁿ(S))) : ∪ₘ₌₀ⁿ 𝔉(Cⁿ(S), 𝔉(S, Cⁿ(S))))(n)(f)(a)

커피스크립트가 왜나와.... 아무말 대잔치 ㅋㅋㅋ 너무 피곤하거든. 그리고 스크립트라 하니까, 뭔가 글로 적은것같아서 좋기도 하고. 무책임쾌락임.

ScalaOf<X, Y>ₙ ≜ (ϝ n : ℕ₀. {y ∈ codom Coffee<X>ₙ(x) | x ∈ 𝔉(X, Y)} : {y ⊆ codom Y | Y = codom Coffee<X>ₙ ∧ n ∈ ℕ₀})(n)
SpaceOf<X, Y>ₙ(a) ≜ (ϝ n : ℕ₀. (ϝ a : X. {f ∈ 𝔉(X, Y) | Cⁿ(X) f ∧ CoffeeScript<S>(f)(a) = f} : {f ∈ 𝔉(X, Y) | Cⁿ(X) f ∧ a ∈ X}) : ∪ₘ₌₀ⁿ 𝔉(X, {f ∈ 𝔉(X, Y) | Cⁿ(X) f ∧ a ∈ X}))(n)(a)

DotProjecter<S>ₙ(a)(f, g) ≜ h s.t. h = (Coffee2Func<S>ₙ(a)(h) ◦ DotProductCoffee<S>ₙ(a))(f, g)

CoffeeFunctions<X, Y>ₙ(a) ≜ (ϝ n : ℕ₀. (ϝ a : X. <F = ScalaOf<X, Y>ₙ, V = SpaceOf<X, Y>ₙ(a), +, -, DotProjecter<X>ₙ(a)> : InnerProductSpace) : 𝔉(X, InnerProductSpace))(n)

CoffeeFunctions는 유한차원이다.

AnalyticCore<X, Y>(a) ≜ (ϝ a : X. lim_{n ⟶ ∞} CoffeeFunctions<X, Y>ₙ(a) : InnerProductSpace)(a)

AnalyticCore는 무한차원이다.

## Step. 2. 드디어 나온 궁금증.

isCoffeScriptIsWorks(f, a) : CoffeeScript<S>ₙ(f)(a) = f

preanalytic(f) : (∃a, isCoffeScriptIsWorks(f, a))
analytic(f) : (∀a, isCoffeScriptIsWorks(f, a))

IntuitiveHunchOfCoffeeScript : ∀f, preanalytic(f) → analytic(f)

## Step. 3. 드디어 나온 질문칸

IntuitiveHunchOfCoffeeScript가 은근히 거짓일것같다. 해석학에서 항상 직관가지고 억측하면 틀리니까 아마 직관적으로 맞아보이는데 불확실한 IntuitiveHunchOfCoffeeScript는 거짓이 아닐까...

 -> 아니란다. Base란 기저간에 변환이 되지않는가? 아이고 역시 난 바보야.
 -> 아니 또 아니란다, 유명한 반례 f(x) = 1/(1-x)는 a = 0에서 preanalytic(f)이지만, (-1, 1)사이의 a에서만 isCoffeScriptIsWorks가 참이다. 근데 dom f ≠ (-1, 1)이란 말임 ㅠㅠ

하하... 미치것군. 너무 골때려서 할 말이 없다. IntuitiveHunchOfCoffeeScript가 참이라니 (해당 정리가 참이 되서, preanalytic과 analytic은 같게된다. 역방향 함의는 에초에, 주사가 공집합이 아니면 함축되기때문.)

이제 난 C^∞랑 analytic의 차이를 배워야 한다.

해석함수 알아야해...