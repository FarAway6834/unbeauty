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