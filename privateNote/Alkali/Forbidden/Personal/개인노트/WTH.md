# What The Hell?

준동형 사상 (Homomorphism) 을 배우고 있었는데

이 요망한 물건 (Homomorphism) 이 하는 짓거리가 심히... 아니 존나 놀랍다.

Φ₀(S, op₁, ..., opₙ) : Volcano₀,ₙ(S, op₁, ..., opₙ) ⊨ (X, op₁, ..., opₙ)

ψ₀(f, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) : (xᵢ, xⱼ, xₖ ∈ dom f), (yᵢ = f(xᵢ)), (yⱼ = f(xⱼ)), (yₖ = f(xₖ))

Φ₁(f, op₁, ..., opₙ) : Φ₀(dom f, op₁, ..., opₙ), Φ₀(codom f, op₁, ..., opₙ)

ψ₁(f, op, n, p, q, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) : ∀m ∈ ℕ ∩ [1, n], ψ₀(f, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ), (p→(xₖ = xᵢ opₘ xⱼ)), (q→(yₖ = yᵢ opₘ yₖ))

인 Φ₀, Φ₁, Ψ₀, Ψ₁를 정의하고,

P(f, op, n, p, q, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) : Φ₁(f, op₁, ..., opₙ), ψ₁(f, op, n, p, q, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ)

인 P에서

P(f, op, n, 1, 0, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) ⊨ f(xᵢ * xⱼ) = f(xₖ) = yₖ

이므로,

준동형사상의 정의가 f(xᵢ * xⱼ) = f(xᵢ) * f(xⱼ)란 점에서,

f(xᵢ * xⱼ) = f(xᵢ) * f(xⱼ) = yᵢ * yⱼ = yₖ로,

P(f, op, n, 1, 0, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ)에서,

P(f, op, n, 1, 1, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ)일것을 만족하고,

P(f, op, n, 1, 1, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ)일때

f(xᵢ * xⱼ) = f(xᵢ) * f(xⱼ) = yᵢ * yⱼ = yₖ 이므로,

P(f, op, n, 1, 0, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) ⊨ (P(f, op, n, 1, 1, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) ↔ f(xᵢ * xⱼ) = f(xᵢ) * f(xⱼ) = yᵢ * yⱼ = yₖ)

으로, 준동형사상 f는

(Volcano₀,ₙ(X, op₁, ..., opₙ) ⊨ sentence) → (Volcano₀,ₙ(Y, op₁, ..., opₙ) ⊨ sentence)

즉, 대수구조의 연산법칙을 보존한다.

와... 이런식으로 간단하게 구조화되는거였다니

초등학교 6학년짜리도 능히 이해할 개념이었던것같다.

아 아무리 그래도 혼자서 형식언어 만들어본적 없을 나이인 6학년은 애바다. 중3이면 혼자서 형식언어정도는 만들수 있었겠지만.

이러니 동형사상에서는 각 원소끼리 대응해서 서로가 서로를 설명하는 binjection이니, 두 연산체계를 거의 같게 볼수 있었던거군 싶다.

단순히 동일한 원시 바이트 타입에 타입케스팅 binjection을 넣어서 보았을 때, 모든 성질이 다 보존되고, 값도 일일히 일대일대응되면, 와... 미친 ㅋㅋㅋ 그거야말로 동치같네.

동형사상 f가 X에서 Y로 간다면 f⁻¹은 Y에서 X로 간다.

그렇다면 f⁻¹은

(Volcano₀,ₙ(Y, op₁, ..., opₙ) ⊨ sentence) → (Volcano₀,ₙ(X, op₁, ..., opₙ) ⊨ sentence)

를 만족하므로, 

f, f⁻¹이 존재하는데에서

(Volcano₀,ₙ(X, op₁, ..., opₙ) ⊨ sentence) ↔ (Volcano₀,ₙ(Y, op₁, ..., opₙ) ⊨ sentence)

를 만족하기 위해 어느 한방향의 함의가 존재할것을 요구하며, 보장하는 사상 f, f⁻¹두가지가 존재하여, 대수구조의 성질과 대상도 보존한다.

걍

∃f⁻¹ = g, {p | Volcanoₘ,ₙ(X, x₁, ..., xₘ, op₁, ..., opₙ) ⊨ p} = {q | Volcanoₘ,ₙ(X, x₁, ..., xₘ, op₁, ..., opₙ) ⊨ q}, Volcanoₘ,ₙ({x₁, ..., xₘ}, x₁, ..., xₘ, op₁, ..., opₙ) = Volcanoₘ,ₙ(X, x₁, ..., xₘ, op₁, ..., opₙ), Volcanoₘ,ₙ({f(x₁), ..., f(xₘ)}, f(x₁), ..., f(xₘ), op₁, ..., opₙ) = Volcanoₘ,ₙ(Y, f(x₁,) ..., f(xₘ), op₁, ..., opₙ), {p | Volcanoₘ,ₙ(X, f⁻¹(y₁), ..., f⁻¹(yₘ), op₁, ..., opₙ) ⊨ p} = {q | Volcanoₘ,ₙ(Y, y₁, ..., yₘ, op₁, ..., opₙ) ⊨ q}, Volcanoₘ,ₙ({y₁, ..., yₘ}, x₁, ..., xₘ, op₁, ..., opₙ) = Volcanoₘ,ₙ(X, x₁, ..., xₘ, op₁, ..., opₙ), Volcanoₘ,ₙ({f(x₁), ..., f(xₘ)}, f(x₁), ..., f(xₘ), op₁, ..., opₙ) = Volcanoₘ,ₙ(Y, f(x₁,) ..., f(xₘ), op₁, ..., opₙ)