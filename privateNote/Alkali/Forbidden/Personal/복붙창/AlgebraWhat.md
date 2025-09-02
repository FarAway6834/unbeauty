# AlgebraWhat

## Alkalic
````markdown
# Alalic Preview

이걸 아주 아주 잘 발전시킬거임, 깃헙 커밋으로 ㄱㄱ

거의 됬네 기분좋다.

## DEFINIRION : Alkalic : Alkalic Linear-algebra + Königsberg Axiom + Lambda Incoding Calculate (구문론적 문제로 lambda형식만 유지하고, 폐지, 람다 지분은 없음)

### Alkalic Algbra

∀x (각각 유일)∃!n(x) s.t. n = ObjectID(x) ∈ Scala

 - AlkalicVectorSpace = Scalaᵗ [t := |Scala|]
 - AlkalicMetrixSpace = AlkalicVectorSpaceᵗ [t := |Scala|]
 - SetTheorem ∈ AlkalicMetrixSpace
 - Notation Definition m ∈ n ≡ SetTheoremₒᵢ₍ₘ₎ₒᵢ₍ₙ₎ [oi := ObjectID]

Alkalraum은 여기서, Scala가 객체의 집합으로 확장되어서, |Scala| = κ가 된다.

### Lambda Including Calculate (구문론적 문제로 lambda형식만 유지하고, 폐지, 람다 지분은 없음)

Alkalic Algbra서 AlkalicVectorSpace나 oidfield = Σᵢ ObjectID eᵢ에 대해, 입력받는 Tensor입력으로 ~~람다~~, 대수함수, Alkalic Algbra서 다가함수를 포함한 함수 구현.

---

폐지되었기 때문에

람다를 아예 삭제해서, 람다가 아닌 걍 연산 과정인 Subrootine으로 바꿨다.

Alkalic Algbra서 AlkalicVectorSpace나 oidfield = Σᵢ ObjectID eᵢ에 대해, 입력받는 Tensor입력으로 대수함수, Alkalic Algbra서 다가함수를 포함한 함수 구현.

하는 체계로 바뀜.

연산 괴정이다.

모든 미지수는 이 람다 체계에서 함수 내부변항으로 고정되어서, 두 함수의 합성에서 초기화되어 창출되거나, 아니면 인자로 된다. 따라서, 어떤 수학 이론은 인자를 가지며, 모델이나 진리값배정은 그 값을 넣는다. (어떻게든 대입됨)

변항은 이론에 인자로 설명 가능

### Königsberg Axiom, VectorAxiom, InaccessibleCardinalExistanceAxiom

⊢ KönigsbergAxiom(x, y, Φ) := (x = y → (Φ ↔ (Φ [x := y])))

이때 [x := y]는 단순히 의미론적 대입 연산자.

⊢ VectorAxiom : "모든 벡터 공간은 기저를 가진다"

다음 글을 읽어 보라.
```
먼저 중위표기결합자 * 에 대해, 다음과 같은 표기법을 도입한다, (*x)(y) ≡ y * x
f(x) ≡ (∈x)라고 공역이 치역으로 정의된 f와 g(x) ≡ (=x)라고 공역이 치역으로 정의된 g를 정의하겠다, 이떄, f와 g의 전사함수임이 당연하며, `≡`는 구문론적 등호다, 참고로 정의역은 집합임으로, 해당 집합이 존재해야 들어갈 수 있다, 또한 f와 g는 표기법이기 때문에, 실제 대수적 객체가 아니며, x ∈ f⁻¹(Φ)가 Φ(x)임은 당연하다, 참고로 공역을 치역으로 정의했다는 뜻은, 저 표기법이 표기하는 수학적 객체의 집합은 저 표기법이 표기하는 수학적 객체의 집합이지, 표기법에서 따로 정의하지 않기에, 최소한의 응용이 아닌 공역이 치역이 되지 않는 큰 응용을 하는것을 형식 언어 형식 문법 수준에서 금지한다고 하는것이다. (당연하다고 말한 내용들은 정의가 아니다, 태클을 걸수 있다.), 마지막으로 h̅는 h의 진리값배정이다. 진리값배정을 뜻하는 표기법이다.
외연 공리(Axiom of Extensionality)와 같은뜻인 명제를 보자, `(∀A∀B)(((x∈A) = (x∈B)) → (A = B))` ≡ `(∀A∀B)((f(A) = f(B)) → (A = B))`이기에, 외연공리는 f가 (전)단사함수임과 동치로, 외연 공리에 따라, 외연공리꼴의 다른 표현인 `f가 (전)단사함수이다`는건 외연 공리가 참일떄 참이다.
외연 공리가 의미하는 바는, 외연 공리가 만족되는 조건은, f가 일대일대응으로 동작하도록 정의된것과 같다,
따라서, 지금부터 f는 외연공리를 만족하는 f인 F로 재정의된다, F⁻¹도 외연 공리를 만족하는 f⁻¹과 같음이, f에 대한 F의 정의상 당연하다

짝 공리(Axiom of Pairing)와 같은뜻인 명제를 보자, ∃{A, B} = ∃{x | (x=A)∨(x=B)}인데 (x=A)∨(x=B) ≡ g(A)(x)∨g(B)(x) = (g(A)∨g(B))(x)로, ∃{A, B} = ∃{x | (x=A)∨(x=B)} = ∃{x | (g(A)∨g(B))(x)}이고, ∃{A, B} f({A, B})(x) = f({x | (g(A)∨g(B))(x)})(x) = (g(A)∨g(B))(x)으로, ∃{A, B}  f({A, B}) = g(A)∨g(B)이기에, {A, B} = f⁻¹(g(A)∨g(B))에서, ∃f⁻¹(g(A)∨g(B))가 짝 공리와 동치로, 짝 공리에 따라, 짝 공리의 다른 표현 `∃f⁻¹(g(A)∨g(B))`은 짝  보장될때, 항진이다.
합집합 공리(Axiom of Union)와 같은뜻인 명제를 보자, ∃{x | (x∈A)∨(x∈B)} ≡ ∃{x | f(A)(x)∨f(B)(x)} = ∃{x | (f(A)∨f(B))(x)}에서, ∃{x | (x∈A)∨(x∈B)} f({x | (x∈A)∨(x∈B)})(x) = f({x | (f(A)∨f(B))(x)}) = (f(A)∨f(B))(x)이므로, ∃{x | (x∈A)∨(x∈B)} f({x | (x∈A)∨(x∈B)}) = (f(A)∨f(B))서, ∃f⁻¹(f(A)∨f(B))임이 합집합 공리와 같은 뜻이고, 합집합 공리에 따라, 합집합 공리의 다른 표현 `∃f⁻¹(f(A)∨f(B))`은 합집합 공리가 보장될때, 항진이다.
이때, 합집합 공리과 짝 공리가 다 참이라는 "합집합 공리와 짝 공리가 보장됨 공리"라는 공리를 세우겠다, 이 공리는 합집합 공리는 합집합 공리의 논리식 표현 p와 짝 공리의 논리식 표현 q에 대해 p와 q가 항진이라는 뜻으로 정의된다. 합집합 공리와 짝 공리가 보장됨 공리와 같은 명제를 보자, "합집합 공리와 짝 공리가 보장됨 공리" = "`∃f⁻¹(g(A)∨g(B))`와, `∃f⁻¹(f(A)∨f(B))`임이 보장됨 공리" = "`∃f⁻¹(g(A)∨g(B)), ∃f⁻¹(f(A)∨f(B))`"으로, , 이는, h̅ = (f, g) ⊨ (∃f⁻¹(h(A)∧h(B)))과 같으므로, 우리가 가정한 "합집합 공리와 짝 공리가 보장됨 공리"에 대해 "합집합 공리와 짝 공리가 보장됨 공리"에 따라, "합집합 공리와 짝 공리가 보장됨 공리"의 다른 표현인 `h̅ = (f, g) ⊨ (∃f⁻¹(h(A)∨h(B)))`는 "합집합 공리와 짝 공리가 보장됨 공리"가 참일때 참이다.
멱집합 공리(Axiom of Power Set)는 멱집합의 존재성을 보장한다.

사실 이는 f가 아닌 F에서도 동일하기에, "합집합 공리와 짝 공리가 보장됨 공리"는 외연공리가 성립하는 F에 대해서 다룰수 있다면, "`h̅ = (F, g) ⊨ (∃F⁻¹(h(A)∨h(B)))`"이다.

치환 공리꼴(Axiom Schema of Replacement)의 다른 표현을 보자, 치환 공리꼴이란 무엇일까? 한마디로 치환 공리꼴은 함수 h에 대해, {h(x) | x ∈ A}의 존재성은 A가 존재해야 보장돼야한다는것이다. 한마디로, ∃A ⇒ ∃{h(x) | x ∈ A}이다. 이때, f({h(x) | x ∈ A})(x) = (∃v ∈ A)((h(v) =)(x)) = ((∃v ∈ A)(h(v) =))(x) 이므로, {h(x) | x ∈ A} = f⁻¹(((∃v ∈ A)(h(v) =)))에서, ∃A ⇒ ∃f⁻¹(((∃v ∈ A)(h(v) =)))임이 치환 공리꼴과 동치이다, 따라서, 치환 공리꼴에 따라 치환 공리꼴의 다른 표현 `∃A ⇒ ∃f⁻¹(((∃v ∈ A)(h(v) =)))`은 치환 공리꼴이 보장될때 항진이다.

치환 공리꼴도 f가 아닌 F에서도 동일하기에, 외연공리가 성립하는 F에 대해서 다룰수 있다면 "∃A ⇒ ∃F⁻¹(((∃v ∈ A)(h(v) =)))"이다.

분류 공리꼴(Axiom Schema of Separation/Specification)은 성질 Φ를 만족하는 부분집합이 존재한다는거다, 성질 Φ를 만족하는 부분집합이 존재한다는뜻은 ∀S ∃{x |(Φ(x)) ∧ (x∈S)}이며, ∀S ∃{x |(Φ(x)) ∧ (x∈S)} ≡ ∀S ∃{x |(Φ(x)) ∧ f(S)(x)}이고, ∀S ∃{x |(Φ(x)) ∧ f(S)(x)}라는건 ∀S ∃f(P) = Φ∧f(S)임과 동치이기에, 분류공리꼴에 따라 분류공리꼴의 다른 표현 `f(P) = Φ∧f(S)`은 분류 공리꼴이 보장될때 항진이다, 이후에 분류 공리꼴을 이용하여 집합론에 대해 논하겠다.

ZF안에 ZF를 만든다고 가정하면, 범주론적으로(함자에 대한 서술로) 접근할때, "∃A ⇒ ∃F⁻¹(((∃v ∈ A)(h(v) =)))"안에서 "h̅ = (f, g) ⊨ (∃f⁻¹(h(A)∨h(B)))", "∃A ⇒ ∃F⁻¹(((∃v ∈ A)(h(v) =)))"가 성립한다, 그러나 이것은 ZF내의 ZF에서만 성립한다. `"메타언어가 서술하는 "내부언어에 관한" 구문"`꼴이기 때문이다.

따라서,
ℙ1 : "∃A ⇒ ∃F⁻¹(((∃v ∈ A)(h(v) =)))"
ℙ2 : "h̅ = (f, g) ⊨ (∃f⁻¹(h(A)∨h(B)))"
를 따로 정의하겠다.

공집합 공리(Axiom of Empty Set)와 같은뜻인 명제를 보자, `(∃S ∀x)(￢(x∈S))` ≡ `(∃S ∀x)(￢f(S)(x))` 이고 `(∃S ∀x)(￢f(S)(x))`와 같은뜻인 명제 `(∃S ∀x)(f(S)(x) = F)`는 `x⊥y = x⊥ = ⊥y = ⊥ = F`인 `⊥`정의에따라서, `(∃S)(f(S) = ⊥)`임과 동치이다, 즉, `∃f⁻¹(⊥)`은 공집합공리와 동치이기에, 공집합 공리에 따라, 공집합 공리의 다른 표현 `∃f⁻¹(⊥)`은 공집합 공리가 보장될때, 항진이다.
무한 공리 (Axiom of Infinity)는 자연수 집합의 존재성을 보장하는 공리이다. "모든 자연수 x에 대해, (∃ℕ)(f(ℕ)(x))"는 무한공리와 같다,

정칙 공리 (Axiom of Regularity / Foundation)는 랭크 함수 Rank의 존재성을 보장한다.

이때, 무한 유향 비순환 가중 그래프 preZFSetThoeremModel에 대한 중복도 W를 정의하고, W(x, y) := int(x ∈ y)로 정의하면, (또한, 동시에, 멱집합의 존재도 보장하여 구성하면,)

멤버십 관계 ∈는 분류 공리꼴을 이용하여, 다음과 같이 재정의된다 ((x ∈ y) s.t. (x ∈ y) when (h(x) = Φ(x))) := F(y)(x) s.t. (∀P ∈ 2ᴬ)(F(P) = h(P)∧F(A)) (단. F는 가능한 한 전단사인 표기법이며, 현제의 정의에서 (∃h(P), F(A) ⇒ ∃(x ∈ y)라고 치역이 정의된다)
이는 분류 공리꼴을 만족시키는 정의이다.

preZFSetThoeremModel들 중에서, ℙ1, ℙ2를 만족시키는 preZFSetThoeremModel를 ZFSetThoeremModel라 할수 있는데, 이들 중 공집합과 자연수를 이론 내부에서 논하는 집합으로 가지는 ZFSetThoeremModel는 메타 언어로 동작할 수 있고, ℙ1를 만족시키는 preZFSetThoeremModel들 중에서 공집합과 자연수를 가지는 preZFSetThoeremModel는 ZFSetThoeremModel와 위계 이외엔 동등하다.

더 나아가서, 상수로써 자연수와 공집합을 가지고, 멱집합 연산과 ℙ1, ℙ2를 구성하는 연산이 정의되는 튜링 언어를 이용하는 형식문법 G 문법의 형식언어 L의 모델은 preZFSetThoeremModel이다. 따라서 FOL에서 HOL로 확장가능한 대수공리계에서 모델론과 구문론과 집합론과 논리까지 싹다 서술 가능하다면, preZFSetThoeremModel도 서술 가능하므로, 그런 대수공리계는 ZF와 동등하다. (이러한 모델의 존재성이 참이 된다는 전제하에)
```

저러한 대수 공리계는 존재한다, 예컨데 alkalic이 그렇다.

Königsberg Axiom은 alkalic을 구성하여, 저 조건을 만족한다. 따라서 ZF공리계와 Königsberg Axiom체제 (25.07.16 커밋 이전)는 ZFC랑 그 능력이 동등하다. (상호 서술)

VectorAxiom은 AC와 동치이다, 따라서 Königsberg Axiom + VectorAxiom은 ZFC와 동등하다. (상호 서술)

이때 다음 공리를 도입하자, 아래 공리계는 Alkalic-LinearAlgebra의 ZFC로 구성되었다
⊢ InaccessibleCardinalExistanceAxiom : ∃κ cf(κ) = κ ∧ κ > ℵ₀ ∀λ<κ, 2^λ < κ [cf(x) := least δ ∈ Ord s.t. ∃f : δ → x, (∀i < δ)(f(i) < x) ∧ (∀α < x)(∃i < δ)(α < f(i))]

이때 κ가 Alkalraum의 구성에 쓰인다.

Alkalraum은 κ로 그 크기가 확장된 Alkalic-LinearAlgebra의 객체를 Scala에 포함하는 Hilbertraum같은 (((Scala^κ)^κ)^....)^κ식으로 구성된 κ Rank Covector공간이며, 복소수나 분발복소수/이원수나 2ⁿ원수 등의 행렬표현에서 그 원래 집합의 원소 역할을 하는 객체로의 대응된것 등이 있을수 있는 실수 및 함수 및 객체들로 된 선형대수 텐서공간인데, κ크기를 보장하기에, Grothendieck 우주가 존재하는 ZFC를 표현할수 있어, 여기서 SetTheorem은 자동으로 Grothendieck 우주가 존재하는 ZFC로, 범주론이 서술된다.

## About

이전에 나온 CSFBAlgebra에서 모델론이 안먹히나 했는데 먹힘, 그래서 아이 새로 CSFBAlgebra를 정리(바꿈), 그게 Alkalic.

M = (ℕ, 0 = ∅, s(x) = x ∪ {x}) 대신

수열의 곱을 다가함수로 써서,

M = Π<ℕ, [0 := ∅], [s := λx. x ∪ {x}]>

같은 서수의 정의가 가능하다는 점에서,

이제 Structure와 변수 대입까지 함수 안에서 됬음.

이제 구조체도 non-structial 논리적 귀결에서 씀으로 쓸수있음

에초에 CSFBAlgebra를 대체할 목적으로 만든거니

나머지는 이하 생략.

### Alkalic-Proofmood

KönigsbergAxiom 에 따라서, 

 > 
 > 규칙 `using x = y → (Φ ↔ (Φ [x := y])))`
 > 
 > 원리 : `x = y → (Φ ↔ (Φ [x := y])))`서 `x = y`가 결론 (5번 라인)과 같음을 보임
 > 
 > ```Alkalic-Proofmood
 > □.1. using x = y → (Φ ↔ (Φ [x := y])))
 > □.2. x = y
 > □.3. Φ
 > □.4. Φ [x := y]
 > □.5. Φ ↔ (Φ [x := y])
 > ```

모든 추론은 규칙 `using x = y → (Φ ↔ (Φ [x := y])))`에서 시작되며, 규칙 `using x = y → (Φ ↔ (Φ [x := y])))`는 기본적으로 modus ponens 추론 규칙을 따르기에 타당 (valid)하다. (심지어 Königsberg Axiom이 항진인데, Königsberg Axiom을 제외하고는 대수 연산밖에 활용하지 않기에, alkalic은 건전하다)

(전건부정의 오류 하나 있어서 삭제함)

내부적으로 결론(5번 라인)이 참일때만 계속 동작함, 또한 결론은 리스트에 쌓이면서, 마지막 줄인 Theorem에 도달할때까지 Lemma가 리스트업되서, 문장이 참인지는 Lemma로 보임.

 > 
 > 규칙 : `Starting Listup Hyperthesis`
 > 
 > 미리 Hyperthesis나열을 시작함
 > 
 > 규칙 : `Quit Listup Hyperthesis`
 > 
 > 더이상 Hyperthesis를 받지 아니함
 > 
 > 규칙 : `Starting Another Subproof`
 > 
 > 새 스택프레임을 만들어, 새로운 부분증명을 시작함
 > 
 > 규칙 : `Quit Another Subproof`
 > 
 > 부분증명을 끝내, Lemma List에 추가하고, 스택프레임을 pop함
 > 
 > 규칙 : `APAristotel-y` (nonHyperVersion 형식증명 only)
 > 
 > HAPA Theorem이라는 외부정리를 이용하여서, y = x이고 y = z이면 x = z임을 보임
 >
 > 규칙 : `APAristotel-z` (nonHyperVersion 형식증명 only)
 > HAPA Theorem이라는 외부정리를 이용하여서, x = z이고 y = z이면 y = x임을 보임
 > 

### HAPA Theorem (Hyper Alkalic-Proofmood Theorem)

Alkalic-Proofmood nonHyperVersion 형식증명의 근거.

동시에 유일한 Alkalic-Proofmood HyperVersion에서의 형식증명

`y = x`, `y = z`가 가설일때,

규칙 `using x = y → (Φ ↔ (Φ [x := y])))`를 통하여, `y = z ↔ x = z`를 보인다, 즉,

문법상, `y = z → (y = z ↔ (y = z [y := x]))` = `y = z ↔ (y = z ↔ x = z)`이므로, 

y = z ↔ (y = z ↔ x = z)를 표현하기 위한 잉여적인 체계다.

(그치만 이전에 있었던 전건부정 오류때문에 또 고쳐야함 ㅠㅠ)

## Alkalic-Proofmood (Power Up - Version)

증명에 앞부분에 붙여야 할 한정사가 추가되었다, 부분증명을 만들어서 중첩 가능하기에, 각 기능을 동시에 붙일수 없다.

 - AristotelProof(비 명시시 기본) : 기존 증명 방식으로 증명
 - DavidHumeProof : Φₜ에 대해, t번 라인마다 매거적 귀납법을 쓰고, 옆 열에는 Φₜ가 귀납법 증명에 쓰이는 경우, 쓰는 칸이 된다. 맨 마지막줄에, 번호 없이, 귀납법 증명의 종류를 기재할때, `∴ Φₜ, Φₜ₊₁, ..., Φₖ ⊨ Φₖ₊₁` (강함), `∴ Φₖ ⊨ Φₖ₊₁` (약함), `∴ Mod(Φ) = ℕ` (일반적인 수학적 귀납법) 으로 기제한다.
 - EuclidianProof : 귀류법 (HegelianProof랑 다르다, 귀류법이다) ; 반증 마지막에, `∴ ⊥ ∴ ⊭ ¬
Φ ∴ Φ`를 놓는다. (`¬Φ`는 결론을 뜻한다.)
 - HegelianProof : 반증 (결론이 부정이 나오므로, "결론이 아니다"를 증명할때 쓰임; 왜냐하면, 기존 버전에서는 논리적 오류가 나오면 오류위치를 지적하고 프로그램이 종료됬기 때문에, 오류를 만들어 반증한 후, 종료하지 않는 AristotelProof가 필요했음)



또한 검증 프로그램 정지를 피하기 위해,

 - PreviewVersion : 이 부분•전체 증명에 대해서, 프로그램 정지 후 오류 지적을 제외하고, Preview리스트에 추가한다, 근거 없는 부분이라, 이걸 단 증명을 참고해서 에러나면, "Referance on Preview"에러 로그를 따로 뱉은 후 평상시 에러처럼 에러난다
 - DebugVersion : 오류가 나는대로, 디버그를 해주며, 훓고 지나간다, **프로그램 전체에 적용된다.**
 - ConjureVersion : 추측으로써, 정지를 피할곳에, `�`를 삽입한다, 이 부분•전체 증명은 가설(Hyperthesis)로 취급된다.
 - NormalVersion (비 명시시 기본) : 기존 방식



마지막으로, 다항식의 계산을 원활하게 하기 위해,

`Polynomial Simplify`라는 부분증명 폼을 넣고 다음을 인수분해하거나, `P(x) = 0`꼴을 풀면 (후자는 미리 `using P(x) = 0 Algorithm`이라고 명시) 오류 없이 증명을 받아들여준다.

A. `LinearSimplify`명령을 통해, LinearSimplify Theorem에 근거하여, 미지수가 여러개인 일차식을 정리한다

B. `Substracting [y := xⁿ]`명령을 통해, xⁿ을 y로 치환한 문장 `Φ`에 대해, `Substracting Variable`필드에 넣은 참인 문장 `y = xⁿ`에 따라서, Φ [y := xⁿ]가 나올때까지, 미리 일차식마냥 치환한 상태로 작업하게 해준다. (치환 변수 필드 논법; `Substracting Variable Field Proofs`)

C. `Solution (a, b, c, d, e)`명령을 통해, 2차 ~ 4차식을 인수분해(근의공식) / 전개(비에트의 정리)한다.

D. `TschirnhausTheoremSubsituate (n, a, b, x)`명령을 통해, `[x := t + b/na]`를 적용한다, 마찬가지로 증명의 원활함을 위해 Substracting명령에 근거한다 (사실 그럴 필요도 없이 구문론적으로 연산자를 정의해도 되는 간단한 문장(`[x := t + b/na]`)이지만)

E. 부분증명 문법에서 `synthetic division` 한정사로, 조립제법 이용 (생략표기가, 매거적 귀납에서 고정된 열의 다수의 행에대해 쓰이므로, 여기서는 쓸때, 행을 다항식으로, 계산 과정순이 열로 되므로, 돌려봐야하는 단점이 있다.)

F. `Alright synthetic division`한정사로, 일반적인 조립제법을 쓰고, 전처리 단계에서 synthetic division로 컴파일

G. 분배법칙을 위해서, `distribute[ 대상 ]` 안에 전부 넣어가지고, 이 증명 시스템용으로 있는 `분배법칙의 일반화 정리`에 따라, 분배함

H. `AlgebraicFormula` : 미리 증명한 곱셈공식을 이용해서, 계산되었음을 명시한다.

I. Gaussian Eimination or ERO & Subsituate : 가우스 소거 혹은 가감/대입

J. System of Quadratic Equations by Quadratic Form : 이차형식으로 연립이차방 풀이

K. System of Quadratic Equations by Cubic Form : 삼차형식으로 연립삼차방 풀이

L. Règle de Cramer : 크래머의 공식으로 풀이

M. `Extraneous Root is (□)` : 무연근 명시

N. `PolynomialFractionize` : 다항함수 분수화

O. `SolvePolynomialFraction` : 해당값 풀이

P. `Fractions Solution is (□)` : 해 명시

### 형식증명의 오토마타용 문법

`□.` 라인이 부분증명이라면, `□.line.`식으로 라인을 표기한다.
그리도, 라인과 라인 사이에 오직 whitespace및 `-`,`–`,`—`만 있을경우 해당 라인을 가독성 용도로 보고 주석처리한다.

또한, line표기에 앞선 점찍은 부분 앞에서 `|`부분이 문자열의 특정 열마다 이어지고, 끝나는 말단이 앞서 설명한 `-`꼴의 주석에 연결되어있다면, 해당 부분도 따로 오류처리하지 않는다.
그외에는, 열 구분자이기에 주석으로 보지 않는다

마지막으로, `[NOTE : ]`형식을 주석으로 본다.

마크다운 문서 내부에 위치했다면, HAlkalic-Proofmood(Hyper Version), Alkalic-Proofmood(일반 버전), PowerAP(Power Up버전)으로 코드 이름인 부분만 읽는다. 또한, 마크다운 부분에 부분증명 코드부분은, 부분증명으로 렌더링한다.

마지막으로 그렇게 html화되어 정리된 렌더링 뷰는, LaTeX 표기 기능을 추가해야만 할것이다.

(그럼에도 해당 html뷰는 아직 형식증명 검토가 안돌아갔으므로, 컴파일 상태인거지, 실행 상태가 아니다. 실행은 실행기에 돌려야, 문서 내부를 파싱해서, 부가적으로 제공된, [labare](https://faraway6834.github.io/unbeauty/privateNote/Proof/labare)•[unbare](https://faraway6834.github.io/unbeauty/privateNote/Proof/unbare) 코드와 함깨 해석하여(labare•unbare는 인터프리터 언어가 아니고, 정형 대이터 겸 사용자 편의 대이터 겸 Low Level 컴파일 언어다.), 검토된다; 이제보니 실행기보다는, 형식증명 검토기라는 명칭이 더 적합하다, 프로그래밍 언어는 하나도 실행하지 않고, 추론규칙을 재대로 활용했는지만 검사하여 검토작업(오류나 로그나 상태 표시)만 하기 때문이다.)

---

### 두번째 글 : `논리적으로 다룬다 전재할때, 대수식은 논리적으로 그 뜻이 해석 • 계산된다.`의 발췌

그렇지 아니하면, 논리적 해석 흐름에서 논리기호가 도출될수가 없다.

식의 계산은 그 값의 배정인 (x̄, f(x̄))와 같이 이루어지는데, 이 방식을 거부하는것은, 논리를 쓰지 않겠다는 말과 같다. (장자 왈 갓나서 죽은 아기보다 오래 산 사람은 없으니 팽조(760살이 넘게 살았다는 전설 상의 신선)도 일찍 요절한 사람)

#### 대수식의 논리적 해석 흐름에서 논리기호를 도출하자

먼저, 다음을 보이겠다

> 함자 `f :≜ (-F)` 를 정의해서, 여기에 대해,

`x = y 이면이 f(x) = f(y)`

이말은, 진리값 T, F를 다루는 식에서, F = 0으로 가정하고 푸는거나, F ≠ 0이 아닐때 푸는거나, 전부 x = y인 등식을 쓸때 f(x) = f(y)가 F와 무관히 동등함이 당연함으로, F = 0인 경우로 잠정적으로 취급하겠음

##### 대수식의 논리적 해석 흐름중 논리적 귀결관계의 도출

Step.1. 방정식을 만족하는 집합으로써의 모델집합이 해집합임을 보이자

먼저, 다음과 같은 다항식 함수 P를 정의하자.

> `P :≜ λA. λx. Πᵢ x - Aᵢ`

그리고 다음과 같은 방정식화 논리함수 Φ를 정의하자.

> `Φ :≜ λf. (f(x) = 0)`

그리고 마지막으로, 다항 방정식 ㅍ을 정의하겠다.

> `ㅍ :≜ φ • P`

그러면,

> `Mod(ㅍ(A)) = {x | x ⊨ (Πᵢ x - Aᵢ = 0)} = {x̄ | Πᵢ x̄ - Aᵢ = 0} = {Aᵢ | ∀i}`

임이 당연하다.

---

Step.2. 논리적 귀결관계의 도출

다항방정식 ㅍ(A), ㅍ(B)에 대해,

0. Mod(ㅍ(A)) ⊆ Mod(ㅍ(B))
1. {Aᵢ | ∀i} ⊆ {Bᵢ | ∀i}
2. ∀i Aᵢ = Bᵢ《주의 : 비약이다, 저건 배열을 정렬해야만 성립한다.》
3. ∃C P(B) = P(A)P(C)
4. P(A)|P(B)

으로,

> 
> 다항식 f, g에 대해 다항방정식 Φ(f) ⊨ Φ(g)
> 
> 이면이
> 
> f | g
>


##### 대수식의 논리적 해석 흐름중 진리값 배정되는 명제논리 결합자의 도출

¬x = T - x로 해석됨을 보이자. (경고 : 형식증명 아님)
A. proof of `x ≠ T ⊢ T ± x ≠ (1 ± 1)T`
0. `x ≠ T` (비 귀류법식 전제 문장)
1. `T ± x ≠ T ± T` (이항 by 함자 `(T ±)`)
2. `T ± x ≠ T ± T = (1 ± 1)T` (1번의 연장선에서 계산)
3. `T ± x ≠ (1 ± 1)T` (2번에서 식 요약) ⋯ ■

B. proof of `⊭ (1 + 1)T = 0 ∨ (1 + 1)T = T`
0. 먼저 part A by `⊭ (1 + 1)T = 0`와 part B bt `⊭ (1 + 1)T = T`로 나눠서 생각하자.
1.A. (1 + 1)T = 0 (귀류법식 전재 문장)
2.A. (1 + 1)T = 2T = 0 (1.A.번의 연장선에서 계산)
3.A. T = 0 ⊨ 2.A. ⊨ (1 + 1)T = 0 (연역)
4.A. ⊭ T = 0 ⊨ 2.A. ⊨ (1 + 1)T = 0 (연역)
5.A. ⊭ (1 + 1)T = 0 (연역) ⋯ ⊥
6.A. ∴ ⊭ (1 + 1)T = 0 (연역) ⋯ ■
1.B. (1 + 1)T = T (귀류법식 전재 문장)
2.B. (1 + 1)T = 2T = T (1.B.번의 연장선에서 계산)
3.B. T = 0 ⊨ 2.A. ⊨ (1 + 1)T = T (연역)
4.B. ⊭ T = 0 ⊨ 2.A. ⊨ (1 + 1)T = T (연역)
5.B. ⊭ (1 + 1)T = T (연역) ⋯ ⊥
6.B. ∴ ⊭ (1 + 1)T = T (연역) ⋯ ■

C.1. A, B ⊨ (x ≠ T ⊢ T - x ≠ (1 - 1)T) (A, B번에서 귀결)
C.2. A, B ⊨ (x ≠ T ⊢ T - x ≠ (1 - 1)T = 0T = 0) (C.1.번의 연장선에서 계산)
C.3. A, B ⊨ (x ≠ T ⊢ T - x ≠ 0)  (C.2.번에서 식 요약)
C.4. A, B ⊨ (T - x = 0 ⊨ x = T ⊨ x) (C.3.번에서 연역추론 : 대우) 《주의 : "x = T"의 의미를 "진리값 x가 참"관점으로 해석함.》
C.5. A, B ⊨ (T - x = 0 ⊨ x) (C.4.번에서 식 요약) 《주의 : 근거인 C.4.에서 "x = T"의 의미를 "진리값 x가 참"관점으로 해석함.》
C.6. C.5.번 내용 ⊢ ¬x = T - x (최종결론)《주의 : "x = T"의 의미를 "진리값 x가 참"관점으로 해석함.》
Q.E.D.

x ∧ y는 xy로 해석됨을 보이자.
T에대한 방정식 (T - x)(T - y) = 0의 해는
x = T ∨ y = T이다.
따라서, x = T ∨ y = T ⊨ T - (T - x)(T - y) = T고,
x ∨ y = T - (T - x)(T - y)로 해석된다.

이때 De Morgan's Law, ¬(¬x ∨ ¬y) = x ∧ y서

T - T + (T - T + x)(T - T + y)
 = xy이다.
 ⋯ Done.

##### 방정식의 의미 : 술어논리(함수논리)의 술어로써, 잠정적으로 특칭양화사를 사용해, 잠재적으로 전칭양화사를 사용함.

방정식 P(x) = 0이 불능이란것은

∄P(x) = 0란 뜻이며

∀P(x) ≠ 0이란 뜻이고 ⋯ ①



방정식 P(x) = 0가 불능이 아니라면

∃P(x) = 0이다. ⋯ ②



방정식 P(x) = 0이 부정이란것은,

부정방정식이므로,

∀P(x) = 0이다. ⋯ ③



①에서, 불능형 방정식 P(x) = 0에 대해,

P(x) ≠ 0은 부정형이고, ⋯ ④



부정형 방정식 P(x) = 0에 대해,

P(x) ≠ 0은 불능형이다 ⋯ ⑤


그렇다면 ③에 따라 다음을 정의하자,

> `Φ :≜ λf. (∃f(x) = 0)`
> 
> `P :≜ λf. (∃f(x) ≠ 0)

그러면 다음을 알수 있다.

④에 따라, Φ(f)가 거짓 이면이 P(f)는 부정형
⑤에 따라, Φ(f)가 부정형 이면이 P(f)는 거짓

Φ(f)가 참 이면이, f(x) = 0를 만족시키는 x존재
P(f)가 참 이면이, f(x) = 0을 불만족시키는 x존재

부정형 방정식을 만들고 싶다? 하면

¬Φ(f) = P(f), Φ(x) = ¬P(f)에서,

불능형 방정식 Φ(f)에 대해 부정하거나,
불능형 방정식 P(f)에 대해 부정하면된다.

술어 P에 대해
Mod(P) = ∅ 이면이 ∄P(x) 이면이 ⊭ P
이면이
Mod(¬P) = U 이면이 ∀¬P(x) 이면이 ⊨ ¬P

따라서, 방정식은 기본적으로 특칭 술어로써, 사용할수 있음
````

## Lava System
````markdown
# Lava System

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 만족•귀결기호 `⊨`가 존나 흥건히 나오지만, 그건 만족•귀결의 의미로 의미론적으로 같아 해석할것 • 그리고 하게 할 것의 목적이며, 정의 기호와의 혼용은 전혀, 전혀, 전혀 없이, 잘 쓰여있다. 간혹 정의같이 나온다면, 정의의 의미를 가진 귀결로, 귀결에는 오류가 없다 단언한다. (글 읽을땨마다 이곳을 참고헐것)

(내가 추상대수학 배우려고 만든 체계)

닫힌형태의 대수구조를 폐구조라고 명명하고, Lava라고 부르겠음.

관계가 주어지지 않은 n개의 함수와 m개의 심볼을 가진 Structure

M = <D, Sym₁, ..., Symₘ, fun₁, ..., funₙ>를 (m, n)-Lava라고 하겠음

(m, 0)-Lava는 (심볼을 정의한, 즉 정의용) 집합인 기본적인 대수구조이다.

참고로, (m, 1)-Lava이상은, 각 연산이 전부 D와 마그마를 이룬다.

Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ) ≜ <D, Sym₁, ..., Symₘ, fun₁, ..., funₙ>

라 하겠다.

Volcano는 (m, n)-Lava를 생성하는 무한 차원의 (= 행과 열의 총 길이가 자연수 기수 길이인) 함수행렬이다.

그래서 (=행렬이기 때문에) Volcanoₘ,ₙ식으로 표현한거다.

Volcanoₘ,ₙ은 (m, n)-Lava를 구성하는 함수이다.

이하에서 대부분 저런 행렬 형식은 인자가 무제한으로 (= 자연수 기수 크기까지인 무한정 = ℵ₀가 최대길이인것임)

예컨데, Volcano₂,₀(𝔹, F, T)는 부울-도메인으로 유명하다.

내가 스스로 정의한
Lava에서 확장한걸로 구조꼴 (structure form)이라는게 있는데, 아래와 같다.

StructureFormₗ,ₘ,ₙ(D, Sym₁, ..., Symₗ, fun₁, ..., funₘ, Pre₁, ..., Preₙ) ≜ <D, Sym₁, ..., Symₗ, fun₁, ..., funₘ, Pre₁, ..., Preₙ>

Pre₁, ..., Preₙ는 술어이고, 이게 뭐하나 미스되지 않고, Lava랑은 달리 있을거 다있게 정의된 구조의 최소 단위이므로, 이를 "구조꼴"이라고 하고, 삼차원 행렬 (= 이제 텐서 ㅋㅋㅋㅋ) StructureForm를 통해 만들 수 있다.

텐서라고 웃은 맥락은, 행렬은 이차원 텐서라고들 해서, 삼차원 행렬이 텐서라고 말한거긴 하다.

(근데 나 멀미나와서 오늘은 여기까지 작성하겠고, 추상대수학은 여기까지 배우겠음.)

StructureForm이 삼차원 행렬이기에, StructureFormₗ,ₘ,ₙ식으로 쓸 수 있었던것이다.

(l, m, n)-구조꼴을 생성하는 함수는 StructureFormₗ,ₘ,ₙ이다.

## 대수 구조 공부

### 성질 목록

아래 술어들은, Lava M에 대해, 

M ⊨ Φ : "M이 성질 Φ를 만족한다"

라고 하는 술어 Φ들이고, 성질이라고 부른다.

사실 술어랍시고 써놨는데

1. 죄다 자유변항만있고, 종속변항은 없는것은 "참성질"이라고 부르고, 걍 사실상 문장명명이다.
2. 자유변항이 존재하고, 종속변항도 존재하는것을, "가성질"이라거 부르고 걍 사실상 술어다.

참성질과 가성질의 `참-`, `가-`는 참다랑어와 가다랑어에서 따왔다.

참성질을 법칙성질, 가성질을 성질부분이라고도 한다. (이것도 근데 방금 만든 조어다)

~배고프니까 천장에서 다랑어가 쏳아졌으면 좋겠다~

#### 결합법칙 (associative property)

결합법칙 Associative는 다음과 같은 법칙성질(참성질)이다.

Associative : "(a * b) * c = a * (b * c)"

#### 중가환 법칙 (medial property)

중가환 법칙 Medial은 다음과 같은 법칙성질(참성질)이다.

Medial : "(m * n) * (p * q) = (m * p) * (n * q)"

#### 교환법칙 (commutative property), 혹은 가환(commutative)

교환법칙 Commutative는 다음과 같은 법칙성질(참성질)이다.

Commutative : "a * b = b * a"

#### 좌역원임-가술어 (tunal is-leftinvers-of Predicate)

좌역원임-가술어 tunalIsLeftinversOf는 내가 방금전에 명명한 가성질이다.

가술어를 tunal 서술어를 붙이는 이유는 tunna-al (다랑어-적)이라는 뜻으로 가술어임을 말하기 위해서다. 이유는 가성질 • 참성칠 명명 유래 참고.

tunalIsLeftinversOf(e, b, a) : "b * a = e"

e = eₗ으로 대입해서 생각한다면, 좌항등원이 항등원인 좌역원임-가술어라고 하며, e = eᵣ이면 우항등원이 항등원인 좌항등원-가술어라고 한다.

해당사항은 하단의 우역원임-가술어에서도 통용된다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 우역원임-가술어 (tunal is-rightinvers-of Predicate)

우역원임-가술어 tunalIsRightinversOf는 내가 방금전에 명명한 가성질이다.

tunalIsRightinversOf(e, b, a) : "a * b = e"

#### 좌역원임-술어 (is-leftinverse-of Predicate)

좌역원임-술어 isLeftinverseOf는 내가 방금전에 명명한 가성질이다.

b isLeftinverseOf a : isLeftinverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsLeftinverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 좌역원임-가술어이다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 우역원임-술어 (is-rightinverse-of Predicate)

우역원임-술어 isRightinverseOf는 내가 방금전에 명명한 기성질이다.

b isRightinverseOf a : isRightinverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsRightinverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 우역원임-가술어이다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 역원임-가술어 (tunal is-inverse-of Predicate)

역원임-가술어 tunalIsInverseOf는 내가 방금전에 명명한 가성질이다.

tunalIsInverseOf(e, a, b) : tunalIsLeftinversOf(e, a, b), tunalIsRightinversOf(e, a, b)

로, 좌역원임-가술어와 우역원임-가술어를 모두 만족시키는, 즉, 역원인 경우로써,

이경우도 e에 따라, 항등원이 좌/우 항등원인 역원임-가술어로 말할 수 있다.

### 역원임-술어(is-inverse-of Predicate)

역원임-술어 isInverseOf는 내가 방금전에 명명한 가성질이다.

b isInverseOf a : isInverseOf(a, b) : 항등원이존재함(eₗ, eᵣ), tunalIsInverseOf(e, a, b)

로, 좌항등원과 우항등원이 같은 경우의 역원임-가술어이다.

(좌항등원과 우항등원의 정의는 항등원을 정의한 색션을 참고하라, 물론 상식이므로 참고하지 않는게 정상이다.) (심볼정의 문단의 항등원 참고)

#### 가역원임-가술어 (tunal checking-does-it invertible-element Predicate)

가역원임 가술어 isInvertibleAs는 방금전에 내가 만든 가성질로,

역원 판별논리식 Φ에 대해,

x isInvertibleAs Φ : isInvertibleAs(x, Φ) : ∃y s.t. Φ(x, y)

인 isInvertibleAs로, FOL에서는 술어가 아닌 성질꼴로, 여러가지 성질의 접두사로 동작하며, 그 경우 Φ과 isInvertibleAs를 붙여쓴다.

그러나 권장사항은 SOL에서의 사용이다.

왜냐하면, 내가 FOL로 만들기 디껍고 귀찮기 때문이다.

다만 한가지 주의하기 위해 참고할 점은, ∃y라는 y는 해당 구조의 도메인 위에 있어야 하므로, 닫혀있는 원소인 조건이라는것이고, 따라서, 구조위에서의 의미해석을 해야함에 주의하자.

#### 가역원임-술어 (checking-does-it invertible-element Predicate)

가역원임 술어 isInvertible는 방금전에 내가 만든 가성질로,

x isInvertible : isInvertible(x)

이며,

isInvertible : isInvertibleAs isInverseOf

로써,

x = y, y = z, x = z에서

x isInvertible : isInvertible(x) : x isInvertibleAs isInverseOf : isInvertibleAs(x, isInverseOf)

인 isInvertible로, isInverseOf조건의 isInvertibleAs로 볼수 있으며,

가역원인지 확인하는 술어이다.

#### 전가역성 (Entire-Invertiblity)

전가역성 EntireInvertiblity는 내가 방금전에 만든 참성질 개념으로, "모든 원소가 가역원"을 말하기 귀찮아, 귀차니즘히 심히 많이 도져 귀찮고 괴로워서, 만든 개념이다.

EntireInvertiblity : "x isInvertible"

로써, 모든 x에 대해서 isInvertible인 일반명제임을 술어 Commutative과 같은 경우로 표기했다는 사실로써 능히 알 수 있다.

### 심볼 목록

아래 심볼은, Volcano에서 사용 목적이 정해진 특수한 심볼이다

#### 항등원 (identity element)

이항연산 `*`의 항등원은

 - 좌항등원 eₗ
 - 우항등원 eᵣ

이 존재하고,

각각

+ eₗ * x = x
+ x * eᵣ = x

를 만족하며, (이게 바로 정의)

다음 술어

항등원이존재함(eₗ, eᵣ) : eₗ = eᵣ

에 대해,

항등원이존재함(eₗ, eᵣ) ⊨ ∃e s.t. eₗ = e = eᵣ

인, 즉, 좌항등원과 우항등원이 같으면, "항등원이 존재한다"고 하고, 좌항등원과 우항등원이 같으니, 그것을 "항등원"이라고 하며, 이것의 존재조건인 좌항등원과 우항등원이 같을것이 항등원의 존재 조건이다.

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 이하에서, 좌항등원 및 우항등원 기호도 여기에서 정의했으므로, 여기를 참고해야한다는걸 강조하고 또 경고하겠다.

### Laval 대수구조 명칭 목록

**Laval은 Lava + -al이라서, Lava + -적(的) 이라는 뜻이다. `Laval == Lava적(的)`인것이다. (오타아님, 중요)**

어떤 Laval 대수구조 명칭 (= Lava식 대수구조 명칭) K란,

K(Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ)) : "대수구조 Volcanoₘ,ₙ(D, Sym₁, ..., Symₘ, fun₁, ..., funₙ)가 그 Laval 대수구조 명칭 K가 지칭하는 대수구조를 이룬다"

인 K를 말한다.

예컨데, Magma(Volcanoₘ,₁(D, `*`))은 항진인것이, lava는 기본적으로 닫혀있기에, 그 대수구조 위에 연산이 정의되어있디면 마그마다.

요컨데, Laval 대수구조 명칭은 술어이다.

예컨데 마그마의 Laval 대수구조 명칭 Magma는

Magma라는 영문 명칭 술어이다

#### 1. 1. 단위 마그마 (unit magma)

이항연산 `*`가

Volcano₁,₁(D, e, `*`) ⊨ "이항연산 `*`가 (D, `*`, e)를 이룸"

인 `*`라면, 즉, 항등원을 가진다면,

이를 단위 마그마라고 부른다

Laval 대수구조 명칭은 UnitMagma 이다.

#### 1. 3. 중가환 마그마 (medial magma)

이항연산 `*`가

Volcanoₘ,₁(D, Sym₁, ..., Symₘ, `*`) ⊨ "이항연산 `*`가 (D, `*`)를 이룸", Medial

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가 중가환법칙을 만족시킨다면,

이를 중가환 마그마라고 부른다.

Laval 대수구조 명칭은 MedialMagma 이다.

#### 1. 2. 가환 마그마 (commutative magma)

이항연산 `*`가

Volcanoₘ,₁(D, Sym₁, ..., Symₘ, `*`) ⊨ "이항연산 `*`가 (D, `*`)를 이룸", Commutative

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가 교환법칙을 만족시킨다면, 즉, 가환이라면,

Laval 대수구조 명칭은 CommutativeMagma 이다.

이를 가환 마그마라고 부른다.

#### 2. 1. 반군 (semigroup)

이항연산 `*`

Volcanoₘ,₁(D, Sym₁, ..., Symₘ, `*`) ⊨ "이항연산 `*`가 (D, `*`)를 이룸", Associative

인 `*`라면, 즉, 당연히 `*`는 마그마니까, 그 마그마가, 결합법칙을 만족하면,

이를 반군이라고 한다.

Laval 대수구조 명칭은 Semigroup 이다.

#### 2. 2. 모노이드 (monoid)

이항연산 `*`가

UnitMagma(Volcano₁,₁(D, e, `*`)), Semigroup(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 (D, `*`, e)를 이룸"

인 `*`라면,

즉, 이항연산 `*`가 반군을 이루며, 단위 마그마를 이루면, 

이를 모노이드 (monoid)라 한다.

Laval 대수구조 명칭은 Monoid 이다.

#### 2. 3. 군 (Group)

이항연산 `*`가

(⊨ Monoid(Volcano₁,₁(D, e, `*`)) ⊨ EntireInvertiblity) ⊨ "이항연산 `*`가 <D, `*`>를 이룸"

인 `*`라면,

즉, 이항연산 `*`가 반군을 이루며, 전가역이면 (= 전가역성을 띄면 = 전가역성을 만족하면)

이를, 군이라 한다.

Laval 대수구조 명칭은 Group 이다.

#### 2. 4. 아벨 군 (Abelian Group) • 가환군 (Commutative Group)

> 솔찍히 중학교때 생각한 생각인대 소신발언 하자면, 오차방정식의 근의공식이 없다는걸 밝힌 위대한 수학자 아벨(Abel)님이 너무 고생하고 비참하긴 한데, 대학못간새끼만큼 비참한건 아니니까, (반대하면 인신공격하고싶... 크흠..), 우리 학생들을 위해 과감히 버리고, 가환군이라고 부르는게 좋다고 본다. 소신발언임 주의.

이항연산 `*`가

CommutativeMagma(Volcano₁,₁(D, e, `*`)), Group(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 <D, `*`>를 이룸"

인 `*`라면,

즉, 이항연산 `*`가 군을 이루는 동시에 가환 마그마를 이룬다면,

이를, 가환군 • 아벨군 이라고 하며,

(또한, AbelianGroup = CommutativeGroup 이고)

Laval 대수구조 명칭을 CommutativeGroup로 한다.

(당연히 AbelianGroup = CommutativeGroup이므로, AbelianGroup로 해도 된다. 왜 대입이 되는지는 "Laval명칭"의 정의 참고. (술어임))

#### 2. 5. 자명군 (trivial group)

이항연산 `*`가 

Group(Volcano₁,₁(D, e, `*`)) s.t. D = {e} ⊨ "이항연산 `*`가 <{e}, `*`>를 이룸"

일때, 이를 자명군이라고 하고, Laval 대수구조 명칭을 TrivialGroup 이라 한다

#### 3. 2. 고리 (Loop, 위키백과에선 고리라고 했다만, 수학계에서는 루프라고 부른다고 카더라)

이항연산 `*`가

Quasigroup(Volcano₁,₁(D, e, `*`)), UnitMagma(Volcano₁,₁(D, e, `*`)) ⊨ "이항연산 `*`가 <D, `*`>를 이룸"

일때, 이를 고리라고 하고, Laval 대수구조 명칭으로 Loop 이라 한다.

Quasigroup에 대해서는 최하단 탐구 예정 노트 참고

### 성질, 예약 심볼, 대수구조에 대한 해설

#### 결합법칙에 대해 해설하며 ; Associatival Extension과 반군

m항연산 f가 Associative를 만족한다면, m < n인 n에 대해,

f(x₁, ..., xₙ) ≜ f(x₁, ..., xₘ₋₁, f(xₘ, ..., xₙ))

로 제귀적으로 정의하며,

이러한 구조의 작동 원리는 결합법칙에 근거한다.

이러한 제귀적 정의를 결합적 확장 (Associatival Extension)이라고 부르며, 내가 방금 만들어낸 조어이다

m, n은 무한해도 좋을거다. 아마도.

Associatival Extension에 의해, m항연산과 가변항연산의 경계가 허물어지는 특징을 보이기에, 반군인 연산은 k항연산이라면, 최소 항의 수를 k로 간주한다.

#### 역원임-술어에 대해 설명하기 : 좌역원이자 우역원이면 역원임 정리

좌역원이자 우역원이면 역원임 정리는 내가 만든 정리로, 사실 정리라고 하기에도 존나 애매한 난이도다.

+ p' = p ∧ r
+ q' = q ∧ r
+ s = p ∧ q
+ s' = s ∧ r

에서,

p' ∧ q' = s'임은 당연히 안다.

이때,

+ p = 좌역원임-가술어이고
+ q = 우역원임-가술어이고,
+ r = 항등원이존재함(eₗ, eᵣ)일때,

좌역원임-술어, 우역원임-술어, 역원임-가술어, 역원임-술어의 정의에 따라, 

좌역원임-술어 ∧ 우역원임-술어 = 역원임-술어

이라는것이다.

## 의미해석

(작성중; 규칙도입계와 기초적 파악이 어떻게 작동하는지를 먼저 적겠음. 나중에.)

### 규칙도입계

(작성중)

### 기초적 파악

앞으로 말할 L은 모델론적 언어라는 맥락에서 말하는거다.

또한, (작성중)

#### 명세관계 ; isInterfaceOf

T isInterfaceOf L : isInterface(L, T) : (L ⊨ T) s.t. (∀T' ⊨ L)(T ⊨ T')

T는 L의 명세인 관계로, L의 기초임을 알리는 관계다.

L의 정의 ⋅ 규칙을 담당하는 부분으로, 논리 언어 Lₗₒₛᵢₖ (저 및첨자들은 원래 "losik"이 아닌 "logic"로 쓰려고 했지만, 유니코드의 한계상 포기)이 자연 연역(Natural Deduction)하는걸 제외한, 규칙계형 파트로 전반적 논리를 구성한다.

예를들어 L은 TensorFlow, T는 그 공식 document로, 기능은 L에 있고, 그 원리가 T이다.

예를들어,

L = 페아노 산술, T = peano axioms and defines이면,

L"1 + 1 = 2"에서,

정의는, T에서,

```markdown
## DEFINITION

### 덧셈 `+`의 정의

1. x + 1 = x⁺
2. x⁺ + y = (x + y)⁺

여기에서, 정의 2번에 1번을 대입하면, (x + 1) + y = (x + y) + 1로, 결론을 부정하는 조건을 만족하는 명제를 역산해보자면, 그것이 바로 교환법칙의 부정과 결합법칙의 부정이므로, 부정한 결론이 틀림에 근거하여, 이중부정을 통해, 덧셈은 가환반군을 이룸을 알 수 있다. 참고로, 0을 정의하지 않은 버전에서는 모노이드도 아니고 걍 반군이다.

## AXIOMS

다음 다섯 공리를 만족하는 상수 1과 집합 ℕ이 존재한다.

1. 1 ∈ ℕ
2. n ∈ ℕ ⇒ n⁺ ∈ ℕ
3. ∀n ∈ ℕ, n⁺ ≠ 1
4. ∀n ∈ ℕ ∀m ∈ ℕ, n⁺ = m⁺ ⇒ n = m
5. ∀S ⊂ ℕ, (1 ∈ S ∧ (n ∈ S ⇒ n⁺ ∈ S)) ⇒ (S = ℕ)

공리 5를 자연수의 귀납적 정의라고 하며, 이는 무한공리에서 말하는 무한집합 중 최소의 크기를 가지는 집합이라는 뜻이다. 또한, 저기에서 수학적 귀납원리가 나온다.

저걸 함수의 언어로 바꾸면, 어떻게 모델을 구축해야할지 보인다.

4번 공리를 보아하니, 다음수 연산 `⁺`는 단사(일대일함수)이다. 그런데, 치역이 1 이상의 자연수 전체이므로, 해당 자연수를 정의역으로 하고 치역이 1이상의 자연수를 치역으로 한다면, 전단사함수(일대일대응)일것이고, 따라서, 다음수 연산은 역함수인 이전수 `⁻`를 가진다. (이 설명의 근걸는 2번 공리 함고)

3번, 1번, 5번 공리를 보면, 자연수는 1에서 시작해서 연쇠적으로 세어나가면서 나오는 수들의 집합이다.

참고로 5번 공리를 보지 말고, 2번 공리만 보더라도 알 수 있다.

사실 5번 공리에 1번 공리에 쓰인 텍스트와, 2번 공리에 쓰인 텍스트가 전부 들어간 점에서, 우리는 자연수 집합 S = ℕ을 다룰떄, 1번, 2번, 3번 공리를 보면 됨을 쉽게 알 수 있다.

사실은, 이것의 모델에서 1은 상수 심볼인데, 번외에서 신기한 특징을 다루겠다.

## 번외

다음 술어 ℙ₁, ℙ₂, ℙ₃, ℙ₄, ℙ₅를 DEFINE하자.

ℙ₁(k, ℕₖ) : k ∈ ℕₖ
ℙ₂(k, ℕₖ) : n ∈ ℕₖ ⇒ n⁺ ∈ ℕₖ
ℙ₃(k, ℕₖ) : ∀n ∈ ℕₖ, n⁺ ≠ k
ℙ₄(k, ℕₖ) : ∀n ∈ ℕₖ ∀m ∈ ℕₖ, n⁺ = m⁺ ⇒ n = m
ℙ₅(k, ℕₖ) : ∀S ⊂ ℕₖ, (ℙ₁(k, S) ∧ ℙ₂(k, S)) ⇒ (S = ℕₖ)

다음은 AXIOMS이다.

다음 공리를 만족하는 상수 k와 집합 ℕ이 존재한다.

1. ℙ₁(k, ℕₖ)
2. ℙ₂(k, ℕₖ)
3. ℙ₃(k, ℕₖ)
4. ℙ₄(k, ℕₖ)
5. ℙ₅(k, ℕₖ)

여기에서도, 4번공리를 통해 다음수의 특징이 유추되며,
1, 2, 3번공리를 통해, k부터 시작하는 자연수(서수) ℕₖ를 정의함을 알 수 있다.

참고로, 덧셈의 정의를 통해서 다름수의 뜻을 알수 있음은 너무 당연한 사실이고, 여기서도 동일하다.

참고로 ℕ₀를 범자연수라고 하며, 𝕎 = ℕ₀로 표기하기도 한다.

참고로,

수가 0, 수가 null(=Null), 수가 NaN인것의 차이가 뭐냐하면,

0은 잔액이 0,
null은 잔액이 없음 (= 그런거 없음)
NaN은 잔액이 수가 아님 (= 0/0꼴)
인것이라서,

0은 통장 잔액이 텅장
null은 통장이 없음
NaN은 통장 잔액이란 개념이 없음

이었던가...? 그랬다.

그런데 잔액이 없는거 (수량을 보는데 그값이 없음(=null))랑 잔액이 0인거 (수량이 0인것)가 무슨 차이인가?

수량으로써 0은 그것이 수량으로 있어야 한다.

0은 없는것을 의미하는, 즉, 1 - 1을 의미하는 수량이고,

이게 자연수가 되야하는지는 논란이었다. (= 자연에 있는 수인지, 자연으로부터 나오는지 논란)

그러나, 수라는게 자연을 설명하는것이고, 셈을 시도했을때, 무조건 ℕ₀(= 𝕎)나 NaN(=원래는 실수에서 정의역 벗어남이지만, 여기서는 범자연수로 치자.)으로 세어지므로, 범자연수로 다룬다고 합리화하는것 같다.

솔찍히 나도 뭐가 맞는지 모르겠고, 걍 범자연수로 구축하는게 용이한건 확실하다.

그래서 실제로, 페아노 공리계를 구축할때는, 범자연수를 쓴다고 한다.
```

이므로, 해당 언어는 모델론이 의미하는 규칙에 따라, L"1 + 1 = 2"가 L"1⁺ = 2"로 치환되서 (덧셈의 정의), 심볼 '2'가 의미하는 바가 1의 다음수를 표기하는 Notation임을 알 수 있다.

그러니까 십진법 기호 표기법은,
1. 2 = 1⁺
2. 3 = 2⁺
3. 4 = 3⁺
4. 5 = 4⁺
5. 6 = 5⁺
6. 7 = 6⁺
7. 8 = 7⁺
8. 9 = 8⁺

를 만족하는 모델론적 언어로 볼 수 있다.

십육진법에서는
1. 추가규칙 아님, 상단참고
2. 추가규칙 아님, 상단참고
3. 추가규칙 아님, 상단참고
4. 추가규칙 아님, 상단참고
5. 추가규칙 아님, 상단참고
6. 추가규칙 아님, 상단참고
7. 추가규칙 아님, 상단참고
8. 추가규칙 아님, 상단참고
9. A = 9⁺
10. B = A⁺
11. C = B⁺
12. D = C⁺
13. E = D⁺
14. F = E⁺

인 추가 규칙이 생기는것이고 말이다.

참고로, 범자연수식으로 보자면, 1 = 0⁺로 정의된다.

물론 이에 대해, 항상 참인거 아니냐고 물을 수 있을텐데, 무한공리를 허용하지 않으면, 이러한 구축방법은 참이 아니고, 이런식으로 정의와 공리를 적고 나서 그를 만족시키는 모델이 존재하지 않는...

예컨데, 공리에 1 = 2를 추가하면 배중률을 어기는데, 이를 만족하는 모델은, 더이상 형식논리가 아니므로, 항상 참은 아니다.

하필 자연수의 덧셈을 가져와서 항상 참이지만

하필.

#### 구현관계 ; isImplementOf

M isImplementOf T : isImplementOf(T, M) : T isInterfaceOf L, M ⊨ T ⊨ L

M이 T의 구현 (Tip : 구현체로 이해해도 좋음)인 관계로, M은 T인 체계를 구성한다.

L언어와 그것을 이룰 요건인 기초 T를 만족하는 M은 구조모델이고, M은 기초 T와 Pre와 Fun, Sym정의 등을 구현(=구성)하며, M ⊨ L ⊨ T인 측면이 있다.

그러나 T의 본질이 M인지 확신할 수 없으며, 당장 FOL에서 뢰벤하임-스콜렘 정리 (Löwenheim–Skolem theorem)등에 따라서, 본질이라기 보다는, 수학적 • 구조적 정합성 측면에서 본질로 볼 수 있는 측면이 있는 구현(=형식화, 사실 정의 되는지도 모르겠는걸 분석 후 모델로써 정의하는것같은 원리다)이지, 유일한, 그리고 절대적인 진리 따위가 아니다.

뢰벤하임 스콜렘 정리에 따라서, 여러가지 모델로 본질을 표현할 수 있다고 하고, 당장에 실수에 대해서, Łoś's theorem으로 만든 `ℝ*` (초실수체, hyperreal field) 만 봐도, 알 수 있다.

그러나 겉모습만 보여주고 그걸 본질이냐고 묻는데에 대해서는 전혀 그렇게 확신할 근거가 없다고 단언한다. 근거를 가져와야한다.



다시 돌아와서, T와 M에 대해 말하자.

예컨데 T는 TensorFlow의 document, M은 일게 그 구현체,

혹은 T는 C언어나 LISP, M은 gcc나 Racket을 예로 들수 있을것이다.



다시한번 이전에 peano공리계로 예를 들었듯 peano공리계 T와 체르멜로(Zermelo)의 구성(Constructure) M과, 폰 노이만 (von Neumann)의 구성 `M'`으로 예를 들어보자 

먼저 M은

```markdown
s(x) = x⁺에서,

0 := ∅
s(x) := {x}

즉,

M = <ℕ₀, 0 = ∅, s(x) = {x} s.t. codom s = ℕ>

인 체계로,

16진수 표기법은,

0 := ∅에서,

1. 1 := {0}
2. 2 := {1}
3. 3 := {2}
4. 4 := {3}
5. 5 := {4}
6. 6 := {5}
7. 7 := {6}
8. 8 := {7}
9. 9 := {8}
10. A := {9}
11. B := {A}
12. C := {B}
13. D := {C}
14. E := {D}
15. F := {E}

로 볼 수 있다.

덧셈은, 범자연수에 대해 가환 모노이드를 이룬다.

> 
> pf.
> 
> 기본적으로 덧셈은 가환 반군을 이룬다.
> 
> 집합 중간에 구멍을 송송내서 닫히지조 못하게 고문하는 경우는 제외하고 말이다.
> 
> 그런 비정상정임경우를 가져오는 미친놈은 아마 없을것이다.
> 
> ~~(가져온다면 덧셈왈 나는 입이없지만 소리를 질러야 한다 이럴듯하다)~~
> 
> 0 + 1 = 0⁺ = 1이므로,
> 
> (0 + x)⁺ = 0⁺ + x = 1 + x = x + 1 = x⁺임을 알수 있는데,
> 
> (x + 0)⁺ = x⁺이므로,
> 
> x + 0 = x임을 알 수 있다.
> 
> 즉 항등원을 가지니, 단위 마그마를 이룸을 알 수 있다.
> 
> 가환 반군이자 동시에 단위 마그마인것은, 가환이고 반군이자, 동시에 담위 마그마인것으로, 가환이고, 모노이드인것으로, 가환 모노이드이다.
> 

2 + 2 = 4인것은,

2 = 1⁺이기에,

2 + 1⁺ = 1⁺ + 2 = (1 + 2)⁺ = (2 + 1)⁺ = 3⁺ = 4로 구할 수 있다.



덧셈은,

1. Φ₁(`*`) : `x * 1 = x⁺`
2. Φ₂(`*`) : `x⁺ * y = (x * y)⁺`
3. Φ : Φ₁, Φ₂

이게 정의한 술어 Φ에서,

Φ(`+`)인 연산이다.

사실은 (+ 1) = s 이게 정의되며, 닫혀있다면 가환반군을 이룰성질을 부여해서 구축했다고도 볼 수 있다.

근데, 이러면, 단점이 좀 있어서, 충분히 나은 폰 노이만 방식을 택한다.

당연히 최대효율을 택하는 한계효용 생각해보면 합리적으로 보인다.
```

`M'`은

```markdown

자연수가 서수(ordinal) 이게도 만들어주는 장점많은, 삐까뻔쩍한 구성이다.

s(x) = x⁺에서,

0 := ∅
s(x) := x ∪ {x}

식으로 구성한다.

즉,

`M'` = <ℕ₀, 0 = ∅, s(x) = x ∪ {x} s.t. codom s = ℕ>

사실 도매인(정의역, 모델의 닫여야하는 집합)이 ℕ₀일떼, codom s = ℕ임은 전부 그렇다.

이 점에서, 자연수가 간단히 나오니 걍 범자연수 구축이라도 왜 이래야 하는지 따지지 말고 받아들여줬으면 좋겠다.



자, 폰 노이만 구성에서 16진수 표기법은

0 := ∅ (= {}) 에서,

1. 1 = {0}
2. 2 = {0, 1}
3. 3 = {0, 1, 2}
4. 4 = {0, 1, 2, 3}
5. 5 = {0, 1, 2, 3, 4}
6. 6 = {0, 1, 2, 3, 4, 5}
7. 7 = {0, 1, 2, 3, 4, 5, 6}
8. 8 = {0, 1, 2, 3, 4, 5, 6, 7}
9. 9 = {0, 1, 2, 3, 4, 5, 6, 7, 8}
10. A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
11. B = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A}
12. C = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B}
13. D = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C}
14. E = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D}
15. F = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E}

이다.

마찬가지로 반군을 이루고, 덧셈의 구성 방법도 같다.



폰 노이만 식이든 체르멜로 식이든

Rank x = x 임은 같고,

x ∈ x⁺임도 같지만

폰 노이만 방식은

0, 1, ..., x ∈ x⁺

이며,

card x = x (단. 이 문장은 엄밀하지 못하다. 범자연수와 기수와 서수는 다른것이, 기수(카디널리티, 카디널)는 "××집합의 카니덜은"이라고 말하는데에서 알수 있듯, 집합에 대한것이다 (정의상), 집합의 카디널리티는 일대일대응이 있으면 같은것이므로, 카디널리티(기수)를 범자연수로 정의하지 아니하였다면, 카디널이 같은지 여부에서는, 에초에 관계의 정의역에 들어가지 못하는 불상사다 일어나, 항위일것이니, 카디널리티가 범자연수인 경우에 맞는 문장이다)

이라는것이 특징이다.

또한, y ≤ x에서,

y ⊂ x으로,

외연공리를 이용하여 같은지 다른지를 알 수 있는 장점이 있다.

사실 범자연수 집합의 존재성은, 무한 공리에서 보장한다.

ZF공리계에서 초한수의 최소이자 초한기수의 최소는 자연수번째 무한 혹은 자연수의 카디널, 즉 자연수 크기의 무한인데,

무한 공리에서 말하는 최소 크기의 무한집합이 자연수이기 때문이다. (자연수의 정의)

그리고 이게 표준 방법이다.

비표준이라고 틀린건 아니지만, 권총과 망치로 인해 표준이 맞는것처럼 치도록 강제할수 있다.

사회라는 약속으로.
```

위와같이 모델을 만들수 있어도, 이것이 왜 그 구현이여야 하는지 잘 모르겠지 않나?

진짜 자연수는, 그 본질이 공리계에 있을것이다.

(사실 굳이 그 공리계로 잡지 않아도, 다른 공리계가 그 공리계를 만족시킨다.)

아마도 말이다. 이것은 본질이라기에는 실용적 구현에 가까워보이니, 함부로 명세가 본질이네 구현이 본질이네 할 증거가 없다고 단언한것이다.

그 증거를 더 가져와야 한단것을.

그리고, 자연수의 두 구현체를 보고, 당연히 그런식으로 약속했으니 그렇게 되는것 아니냐고 묻는다면 말하겠다.

당신은 Lisp(언어)와 Racket(구현체)이 완전히 동일하다고 생각하는가?

#### 상속자 : Extender

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT :  자, 이제부터 다루는 내용이 핵심이다. isInterfaceOf나 isImplementOf는 일게 모델론적 개념의 표기법용 노트의 설명에 불과하다.

N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 내가 설명항 내용은 지금부터 시작이고, 의미해석의 핵심 파트는 상속사, 피상속자, 참피상속자, 섹터, 명제귀결, 구조귀결, 폼페이 함수를 이용한, 기초적 파악이고, 이중 피상속사 참피상속자, 섹터같은 구조가 상속자에서 나온다.
N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 그러나 핵심적인 논리흐름은 명제귀결, 구조귀결을 알아야 하고,
N.B. ATTENTION, WARNING, NOTE(IMPORTANT), WATCHOUT, TIP, DECLARE, READIT : 다루는 대상은 기초적 파악이다.

자, 본론으로 들어가보자.

Interface, Implement, Extend... 사실 이것들은 다 Object Oriented Programming Language인 Java에서 따온 명칭이다.

뭐... 그냥 그렇다는거다.

Extenderₙ(M₁, ..., Mₙ) ≜ M s.t. M₁, ..., Mₙ ⊨ M

Extender(상속자)란 n개의 Implement들을 상속한 Structure Model을 주는 함수로 Extender의 용법의 대표적 예시로는, DustunalExtenderalObject와 Sector가 있다.

상속자를 아래 예시로 살펴보자.

```python

class CORE(bool):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __gen_my_type(self, ob):
        return type(self)(ob)

class ConjuntionLattice(CORE):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __and__(self, other):
        return self.__gen_my_type(self and other)

class ANF(ConjuntionLattice):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __xor__(self, other):
        return self.__gen_my_type(int(self) ^ int(other))

class NagationStructureModel(CORE):

    def __init__(self, value) -> None:
        super().__init__(value)

    def __invert__(self):
        return self.__gen_my_type(not self)

class CNF(NagationStructureModel, ConjuntionLattice):
    def __init__(self, value) -> None:
        super().__init__(value)

class DNF(NagationStructureModel):
    def __init__(self, value) -> None:
        super().__init__(boolean)

    def __or__(self, value):
        return self.__gen_my_type(self or other)

class PsudoAngdeAlgebra(ConjuntionLattice):
    '''
    # diffrence between PsudoAngdeAlgebra and Angde Algebra
    
    while Angde Algebra is defined by me, and also it only use imply and use boolean value , not using conjuntion, but PsudoAngdeAlgebra is using Conjunction to form the logical operated.
    
    model theory to make an logical language or gödel numbering's logical operand.. blablabla

    it used in past as whole diffrent forms. that's an critical diffrence betwean AngdeAlgera
    '''

    def __init__(self, value) -> None:
        super().__init__(value)

    def __le__(self, value):
        '''
        letter `<=` seems like reversed implication operator `⇐`, so it will coded as `<=` means `←` which implication symbol s.t. `x ← y` means `y implies x` s.t. `x ← y = y → x = (¬y ∨ x)`
        '''
        return self.__gen_my_type(self or not value)

class HighschoolLevelLogicalOperator(PsudoAngdeAlgebra, CNF, DNF, ANF):
    '''
    L = {'~', '&&', '||', '^', '<='}
    '''

    def __init__(self, value):
        super().__init__(value)
```

이처럼 상속 구조는 필드(구조체 상수)및 메서드(구조체 함수)를 가져오는데,

다음 c/c++코드를 보라.

```cpp

struct intSizeTyp {
    int main_value;

    intSizeTyp(int main_value) {
        this.main_value = main_value;
    }
}

struct MathmaticalStructure : intSizeTyp;

struct MathmaticalStructure {
    const MathmaticalStructure Sym1 = MathmaticalStructure(0);
    const MathmaticalStructure Sym2 = MathmaticalStructure(1);

    MathmaticalStructure Fun1(intSizeTyp x) {
        return x + this.Sym2
    }

    MathmaticalStructure Fun2(void) {
        /* null-ary operand */
        return this.Sym1
    }
};
```

저 구조체는 다음과 같은 튜플이다.

MathmaticalStructure = <constructer, Sym1, Sym2, Fun1, Fun2, main_value>

각각 도메인(이라고 치자고 ㅋㅋ ㅠㅠ) 상수기호 Sym1, Sym2, 함수기호 Fun1, Fun2, 변수기호 main_value가 차례대로 담긴 그저 튜플이다.

그리고 이건 시벙 놀랍게도 C의 구조체의 역할인 그냥 이름붙여 묶기를 잘 수행하는 튜플이다.

예를 들어보자.

```cpp
struct cardesian_coordinate {
    double x; //8B = 64bit
    double y; //8B = 64bit
};

cardesian_coordinate v;
```

위 코드는 다음과 같이 메모리에 적제될것이다. (컴파일 예시지 실제로 저러진 않는다.

```
memory addr : 0000 0000 0000 07B4 | v.x
memory addr : 0000 0000 0000 07BC | v.y
```

그러면 저 필드가 가르키는건 순전히 <x, y>인 튜플의 원소다.

실제로 SIMD vectorization연산도 이와 유사하다.

이와같이, 어떤 구조체 M, N이 있어서, M ⊨ N의 만족관계를 가지면, 상속된다고 비유적으로 이해할 수 있다.

#### 피상속자 ; ExtenderalObject

피상속자 ExtenderalObject는 External과 반대로, 부모를 쫒아간다 생각하면 편하다. (편하다고 했지, 꼭 그런건 아닌게, 피상속 관계를 만족시키는걸 뱉는 다가함수로, 부모 모델들의 집합을 뱉지만 그걸 여러개 뱉으므로, M, N, L을 상속했더라도 `M'`, `N'`, `L'`이 나오지 않으리란 보장이 없다. 사실 둘다 다가로 나오는 함수니까. (이가라고 한정한 적 없음))

ExtenderalObjectₙ ≜ (Extenderₙ)⁻¹

ExtenderalObject는 다가함수로, M이 상속된 자식이게 하는 M₁, ..., Mₙ들의 모임 `M'`을 뱉는 다가함수로, M'이 여러개이기에, 튜플(=구조체)집합(=모임)(=M')의 집합족(M'들의 모임)으로 가는 치역을 가진다.

ExtenderObject는 결국 M을 만족시키기에, 자신을 낳을(=모델링할) 부모를 파악하는 함수이다. 또한, 

(작성중)

#### 참피상속자 ; DistunalExtenderalObject

(작성중)

#### Sector

(작성중)

#### 명제귀결 ; ProposolalConsequence

(작성중)

#### 명제귀결도입기반 구조귀결 ; ProposolalConsequenceIntroduceSystemicConsequence

(작성중)

#### 폼페이 함수 ; Pompeii

(작성중)

#### 기초적 파악

(작성중)

## NOTE

작성중이고, 함자 (* x), (x *)가 준동형사상인 마그마가 유사군(quasigroup)이라고 하는데, 어떻게 적어야 할 지 모르겠으니, 범주론 배울때 배워보자.

유사군의 Laval 대수구조 명칭을 Quasigroup라 하자.
````

## 과학구조
````markdown
# 과학구조 (유추 구조, 가정구조공리술어, 통계구조생성자, 귀추 구조)

유추 구조, 가정 구조, 귀추 구조는 각각 수학적 수식 혹은 술어이거나 대수 구조이다.

그러니까 과학구조는 탐구방법론같은 시시콜콜한 과학자들의 좆 비스무리한 개쓰래기 똥 씨발 멍청한 찐따같은 씨발 좆이 아니라 그냥 Fuck도 아니고 과학이라는 Fuck 똥 씨발 좆 좆 좆이 아니라 씨발 그런 개같은게 아니라, 술어 혹은 시시콜콜하고 좆같은 술어보다는 사실은 대수구조 및 대수에서 구성한 함수(연산)이다. 그러니까 모델론 및 범주론 및 추상대수학적인 연구 대상이다.

통계 구조는 유추 구조로 만들어지며 그러지 않는다면 빛 좋은 개살구다. (통계적 구조는 퍼지논리 공리계의 모델을 제시하는 전혀 다른 통계의 언어로 구성한 수학 언어를 쓰는데 이것이 무려 일반 수학의 확장이다. 따라서 나는 연역법 만능주의자기 때문에 이런걸 좆같아해서 통계적 구조를 유추 구조로 환원해서 연역화하지 않고 제시한다면 내가 당신 목따러 달려갈수도 있다.)

N.B. 씨발씨발 좆좆같네 아아아악이거는 절대 좆 shit 등신같은 과학이 아니라 과학처럼 보이는 ZFC및 Alkalic공리계 공통기반 공리이용 추론 혹은 자연연역법을 통한 특정한 추론(유추 구조에서 말하는 추론, 가정구조에서 말하는 추론, 귀추구조에서 말하는 추론)의 대수구조화라고 보면, 어느정도 맞는데 틀리다. 이거는 추론의 대수구조화 그 똥같은게 아니라, 그냥 대수구조다. 여기서 추론을 붙이는것은 금지된다. 의미론적으로 추론으로 규정해버리는 순간 대수구조의 의미가 아니기에, 여기서 정의하는 내용은 대수구조지 좆같이 추론에 간섭하는게 아니라고 해두겠다.

씨발 좆좆좆같은 추론내용에 대한 간섭 싫어

## 유추 구조

Zhegalkin Polynomial에서,

Φₙ : "n번째 관측된 결과"에서,

Ψₙ(Φ) ≜ Πₖ Φₖ [k := 1 ~ n]로 정의하고,

lim Ψₖ(Φ) : ∀n ∈ ℕ, Φₙ (k → ∞)
이므로, 이러한 Ψ를 유추 구조라 한다.

## 통계 구조

정해진 y에 대해, x ↔ y를 FuzzyLogic으로 쓰면,

x ↔ y ~ B(n, pmf(x))이므로,

부울 도메인을 실수로 확장한 Alkalic논리는 실수로 확장됬으니까, 이 경우에 한정하여 원래 불 도메인인 {0, 1}에서와 달리 FuzzyLogic및 확률과 통계의 확률 개념과 동형이다.

따라서,

Alkalic논리에서의 (x ↔ y) = (x = y)로 놓는 순간, Alaklic이 FuzzyLogic을 따르고, x와 y는 확률과 통계의 연언명제가 될 수 있음이 당연하다.

따라서,

H : (x ↔ y) = (x = y)에 대해,

Alkalic에서 논리언어의 모델을 H로 바꿔놓는 개짓거리를 하는 순간, 유추 구조를 통계 구조라고 하고, 이는 수학을 모호하게 만든다. (그니까 H를 공리화하는 좆같은거다, 이게 통계 구조의 포괄적 정의다, 즉, 쓸모없는 좆을 포함한 포괄적 정의.)

통계 구조의 정의는 아래 참고.

### 왜 쓰나?

통계 구조 S(X)에 대해, 이 통계 구조가 본래의 부울 도메인 {0, 1}에서 정상작동할것이므로,

일반적인 Alkalic수학에서 유추구조를 정의한 모델 X만을 정의역으로 하는 S에 대해, (S는 statistics)

S(X) = Y s.t. Alkalic에서 논리언어의 모델을 H로 바꿔놓는 개짓거리를 한것

이고, 이때,

A)
항상 우연명제일줄 알았던 참인 가정을 입력시키는데에 있어 적절한 추론을 썻다면, S(X)가 디렉델타함수의 평행이동으로 동작하며, 동시에, 당연히 이분논리적인 결과가 나오기 때문에

B)
즉, 확률적 추측이 아닌, 통계적 관찰에서 통계는 빼고 관찰만 가지고 연역적 추론을 한 이분논리적 연역법이기에, 건전하게 되는 상황과 동등하기에 (Tip : A ↔ B임)

이에따라서, 무한시도의 무한발생이라는 보편양화적인 과정에 따라서 참이 될 수 있다.

즉, X에서의 Ψ를 S(X)에서의 Ψ로 옮기면, 이것 역시 큰 수의 법칙을 따르며, 심지어 극한을 보내면 연역법이다.

함수 S가 바로 "통계구조생성자"이며, 이것이 통계구조의 정의이다.

#### 그래서 왜 큰 수의 법칙을 따르는걸 만들어놓느냐?

귀추 구조로 유추 구조 Ψ가 의미하는 바가 가설이라는 귀추 구조를 만들수 있기 때문이다.

## 가정 구조

다음 술어 μ를 보라.
μ(H) : Ψ(Φ) = H ∧ (⊨Ψ(Φ))

μ(H)를 가설로 놓아 공리를 설정하는 귀추 구조를 가정 구조하고 한다.

그리고 μ는 "가정구조공리술어"라고 한다.

### 가정구조 한줄요약 = 가정구조공리술어 한줄요약

"유추구조에서 계량하는 명제가 바로 가설 H이다."는 귀추구조용 공리.

원래 유추구조에서 판단 불가능한걸 의미해석 중간에 빼돌려서 가능하게 함.

## 귀추 구조

가설을 공리로 증명하는 규칙도입계 모델 M을 만들고,

1. M이 일관됬는가?
2. M이 증명하고자 하는 공리계와 호환되는가?
3. M이 증명하고자 하는 공리계에서 증명가능한가?

절차로 만족시키면, 증명될것이므로, 이러한 M을 귀추 구조라고 한다.

## 마치며

Q. 추론의 모델링인가요?
A. 그냥 대수구조가지고 추론을 모델링했다? 지랄하네 목적에 벗어나는 과대해석이지? 그냥 어떤 추론과정을 모델링한것과 같은 결과라고 하면 뭐 맞긴한데 그게 핵심이 아니라고. 핵심은, 내가 추론에 대해서 탐구하는중에 대수구조를 하나 발견한거고, 저건 추론이 아니라 대수구조야. 씨발 추론을 모델링한 목적에 충실하지 않은데 뮤ㅓㄴ 개소리야? 에초에 만들어진 이유가 우연히 발견한 대수구조이고, 그 대수구조는 추론의 목적의 충실하지 않으니 수정해야하네가 개소리된다 죽어버려 개씨발아!! 개소리하지마!! 거짓 거짓 거짓!! 추론의 모델링? 아니오 아니오아니오 씨발아 아닙니다!
Q. 추론 과정을 모델링한것과 같은 결과네요?
A. 개씨발새끼야 그럼 미적분은 미분소로 하는게 참이고 무한소쓰는게 표준해석하기겠지 죽어라!! 미적분이 역사적으로 무한소를 쎴지, 초실수체를 다루는 연상이 아닌 δ-ε논법적 연산인것처럼, 과학구조도, 전혀 추론과정따위 좆을 다루능게 아니라 그냥 평범하게 규칙도입계 대수를 이용한 대수구조라고요!!

이 저주받은건 이름부터 "우연이발견한대수구조"(UBDG : U연이 Bar견한 Desu gujo)로 해서 UBDG₀, UBDG₁, UBDG₂, UBDG₃로 고쳐여겠어. 이름이 하느님아버지와 예수님의 분노를 사서 저주받았기에 이렇게 오해받는걸꺼야.
````