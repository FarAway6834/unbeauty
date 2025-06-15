# Defination of Unary

```
표기 Unary ≡ [UnarySystem := λF. [Char := λx. "x is charactor"][
String := λx. x ∈ {c | Char(c)}ᵗ [t := |x|]
][
F := λn:ℕ₀.λx:Char. ∀y (단. y ∈ {S}ⁿ)
][x ← y := z (단. z → y = x)
][x↓ᵏ y := z (단. z ↑ᵏ y = x)
][ℙ₁ := ︷
∀String(x), "x is string"
Fₙ ≡ F(n)
x▪︎y ≡ \stackrel{x}{y}
「x」≡▪︎x
『x』₁ ≡ x
『x』₍ₙ₊₁₎ ≡ x『x』ₙ
▴「Fₙ(x)」 ≡ F(n⁺)(x)
▾「Fₙ(x))」≡ F(n⁻)(x)
Fₘ(x)『「▴」』₁「Fₙ(x)」 ≡ F₍ₙ₊ₘ₎(x)
Fₘ(x)『「▾」』₁「Fₙ(x)」 ≡ F₍ₙ₋ₘ₎(x)
Fₘ(x)『「▴」』₂「Fₙ(x)」 ≡ F₍ₙₘ₎(x)
Fₘ(x)『「▾」』₂「Fₙ(x)」 ≡ F(n÷m)(x)
Fₘ(x)『「▴」』₃「Fₙ(x)」 ≡ F(nᵐ)(x)
Fₘ(x)『「▾」』₃「Fₙ(x)」 ≡ F(ᵐ√n)(x)
Fₘ(x)『「▴」』₄「Fₙ(x)」 ≡ F(ᵐn)(x)
Fₘ(x)『「▾」』₄「Fₙ(x)」 ≡ F(super-rootₘ(n))(x)
Fₘ(x)『「▴」』₍₂₊ₖ₎「Fₙ(x)」 ≡ F(n ↑ᵏ m)(x)
Fₘ(x)『「▾」』₍₂₊ₖ₎「Fₙ(x)」 ≡ F(n ↓ᵏ m)(x)
x ▲ y ≡ y『「▴」』₁「x」
x ▼ y ≡ y『「▾」』₁「x」
x ▶ y ≡ y『「▴」』₂「x」
x ◀ y ≡ y『「▾」』₂「x」
Fₘ(x) ↑ᵏ Fₙ(x) ≡ Fₘ(x)『「▴」』₍₂₊ₖ₎「Fₙ(x)」
Fₘ(x) ↓ᵏ Fₙ(x) ≡ Fₘ(x)『「▾」』₍₂₊ₖ₎「Fₙ(x)」
Fₘ(x) → Fₙ(x) ≡ F(n → m)(x)
Fₘ(x) ← Fₙ(x) ≡ F(n ← m)(x)
︸]]
```

---

사용법 : 

> `(∃UnarySystem(F))(⊢ ℙ₁)`