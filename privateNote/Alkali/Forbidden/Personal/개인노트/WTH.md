# What The Hell?

준동형 사상 (Homomorphism) 을 배우고 있었는데

Φ₀(S, op₁, ..., opₙ) : Volcano₀,ₙ(S, op₁, ..., opₙ) ⊨ (X, op₁, ..., opₙ)

ψ₀(f, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) : (xᵢ, xⱼ, xₖ ∈ dom f), (yᵢ = f(xᵢ)), (yⱼ = f(xⱼ)), (yₖ = f(xₖ))

Φ₁(f, op₁, ..., opₙ) : Φ₀(dom f, op₁, ..., opₙ), Φ₀(codom f, op₁, ..., opₙ)

ψ₁(f, *, p, q, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ) : ψ₀(f, yᵢ, xᵢ, yⱼ, xⱼ, yₖ, xₖ), (p→(xₖ = xᵢ * xⱼ)), (q→(yₖ = yᵢ * yₖ))

인 Φ₀, Φ₁, Ψ₀, Ψ₁를 정의하고,