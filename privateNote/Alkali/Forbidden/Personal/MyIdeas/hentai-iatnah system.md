# hentai-iatnah system

definition of hentai-iatnah system)
1. hentailast ≜ ϝ x : [0, 1]. hentaifirst(2(x - hentaifirst(x))) : [0, 1] s.t. hentaifirst(x) = hentaifirst(x - hentailast(x)) = hentaifirst(hentai(hentaifirst(x), 0))
2. henati⁻¹ ≜ ϝ x : [0, 1]. (hentaifirst(x), hentailast(y) : [0, 1]² s.t. hentai(x, y) = hentai(x, 0) + ½hentai(y, 0)
3. iatneh ≜ henati⁻¹
4. hent ≜ ϝ (x, y) : ℝ². tan(πhentai(actan(x)/π + ½, actan(y)/π + ½) - ½) : ℝ s.t. actan = tan⁻¹
5. tenh ≜ hent⁻¹
6. hentfirst ≜ ϝ x : ℝ. tan(πhentaifirst(actan(x)/π - ½) + ½) : ℝ
7. hentlast ≜ ϝ x : ℝ. tan(πhentailast(actan(x)/π - ½) + ½ : ℝ
8. hentup(1, x) ≜ hent(1, x)
9. hentup(n, x, y) ≜ hent(n, hent(x, hentlast(hentup(n - 1, y))))
10. hentup ≜ ϝ (n, t) : lengthedRealvec. hentup(n, t) : ℝ s.t. lengthedRealvec(v) : n = dim v ∈ ℕ ∧ v ∈ {n} × ℝⁿ
11. hentupdim ≜ hentfirst
12. hentupidx ≜ ϝ (x, i) : hentupidxible. hentupidx(hentup(hentupdim(x) - i + 1, hentlastⁱ(x)), 1) : ℝ s.t. hentupidxible(x, i) : i ≤ hentupdim(x)
13. hentupidx(hent(1, x), 1) ≜ hentlast(hent(1, x))
14. hentupidx(hent(n, x), 1) ≜ hentfirst(hentlast(hent(n, x)))
15. hentensorc ≜ ϝ (n, T, m) : rankedRealtenc. hentensorc(n, T, m) : ℝ s.t. rankedRealtenc(n, T, m) : n = rank T ∈ ℕ ∧ T ∈ ⊗ₖ₌₁ⁿ ℝᵐ⁽ᵏ⁾ ∧ dim T = Πₖ₌₁ⁿ m(k) ∧ m ∈ 𝔉(ℕ, ℕ)
16. getTensorsDim ≜ (rankedRealten, 𝔉(ℕ, ℕ), rankedRealtenc)
17. hentensor ≜ ϝ (n, T) : rankedRealten. hentensor(n, T, getTensorsDim(n, T)) : ℝ s.t. rankedRealten(n, T) : ∃!m, rankedRealtenc(n, m, T)
18. hentensorc(1, T, m) ≜ hent(1, hentup(m(1), T))
19. hentensorc(n, T, m) ≜ hentensorc(1, Σₖ₌₁ᵐ⁽ⁿ⁾ hentlast(hentensor(n - 1, <φ(n, k) | T>)) φ(1, k))
20. hentenrank ≜ hentfirst
21. hentenacess ≜ hentlast
22. hentencurryidxerₖ ≜ (ϝ k : ℕ. (ϝ T:ℝ. hent(hentenrank(T) - 1, hentupidx(hentenacess(T), k)):ℝ) : 𝔉(ℝ, ℝ))(k)
23. hentenidx ≜ ϝ (T, n) : ℝ × ℕ*. hentenidx(T, n) : ℝ
24. hentenidx(T) ≜ acess(T)
25. hentenidx(T, k, t) ≜ hentenidx(hentencurryidxerₖ(T), t)

유한랭크 유한차원 실벡터 • 실텐서는 실수와 일대일대응된다.