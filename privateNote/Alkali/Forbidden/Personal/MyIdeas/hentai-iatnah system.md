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

유한랭크 유한차원 실벡터 • 실텐서는 실수와 일대일대응을 쉽게 제시할수 있음. ㅇㅇ.

게다가 card 𝔉(ℕ, ℝ) = (card ℝ) ↑ (card ℕ) = ((card ℕ) ↑ (card ℕ)) ↑ (card ℕ) = (card ℕ) ↑ (card ℕ • card ℕ) = (card ℕ) ↑ (card ℕ) = card ℝ라서 무한차원에서 일대일대응이 존재할거임. ㅇㅇ.

## 덤 : hentinfvec-system

hentinfvec-system : IssueOfHentinfvecSystem의 세가지 명제가 모두 참이면 뭐라도 정의하고, 아니면 아무것도 졍의 안하는 시스템
1. FunctionalEquationOfHentinfvec(hentinfvec) : hentinfvec(a) -hentensor(1, [hentinfvec(oddArr(a)), hentinfvec(evenArr(a))]) = 0
2. FunctionalEquationOfHentinfvecidx(hentinfvecidx) : hentinfvecidx(v, i) - hentinfvecidx(hentenidx(v, iseven(i)), ⌊i/2⌋) = 0
3. oddArr(a)ₖ ≜ (ϝ a : 𝔉(ℕ, ℝ). (ϝ k : ℕ. a₍₂ₖ₋₁₎ : ℝ) : 𝔉(ℕ, ℝ))(a)ₖ
evenArr(a)ₖ ≜ (ϝ a : 𝔉(ℕ, ℝ). (ϝ k : ℕ. a₍₂ₖ₎ : ℝ) : 𝔉(ℕ, ℝ))(a)ₖ
4. hentinfvec ≜ ϝ a : 𝔉(ℕ, ℝ). hentinfvec(a) : ℝ s.t FunctionalEquationOfHentinfvec(hentinfvec)
5. iseven ≜ ϝ x : ℕ. ½(1 + ((-1) ↑ x))
6. hentinfvecidx ≜ ϝ (v, i) : ℝ × ℕ. hentinfvecidx(v, i) : ℝ
7. hentensorinf는 내일 정의하지 뭐... 내일 이전까지, 이 시스템에 hentensorinf는 존재하지 않는거임 (즉, 이건 indev ver)

### 핵심 문제 (IssueOfHentinfvecSystem)

존재성 추측 1 : FunctionalEquationOfHentinfvec는 FunctionalEquationOfHentinfvecidx가 해를 가지면 해를 가진다. (인덱싱 가능한 결과면 그걸 만드는 작업이 coding가능할것이라는 추측)
존재성 추측 2 : FunctionalEquationOfHentinfvecidx는 FunctionalEquationOfHentinfvec가 해를 가지면 해를 가진다. (그 함수가 존재하고, 인자에서 인덱싱 되니까 될거란 추측)
존재성 추측 3 : FunctionalEquationOfHentinfvec가 해를 가지거나 FunctionalEquationOfHentinfvecidx가 해를 가진다.

그렇다. 에초에, FunctionalEquationOfHentinfvecidx랑 FunctionalEquationOfHentinfvec가 해를 안가지면, 저 시스템에선 아무것도 정의 안하는거다.

#### 독자에게

해줘

![해줘티콘](https://namu.wiki/w/%ED%95%B4%EC%A4%98)

(참고 : 저 이모티콘이 찾아보니, 혐오표현으로 쓰였다는데...뭐... ㅈ도관심없고, 그 의 혐오에 ㅈ도 동조하지 않고, 이모티콘을 인용했단점.)