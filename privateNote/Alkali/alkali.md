# Alalic Preview

이걸 아주 아주 잘 발전시킬거임, 깃헙 커밋으로 ㄱㄱ

## DEFINIRION : Alkalic : Alkalic Linear-algebra + Königsberg Axiom + Lambda Incoding Calculate

### Alkalic Algbra

∀x (각각 유일)∃!n(x) s.t. n = ObjectID(x) ∈ Scala

 - AlkalicVectorSpace = Scalaᵗ [t := |Scala|]
 - AlkalicMetrixSpace = AlkalicVectorSpaceᵗ [t := |Scala|]
 - SetTheorem ∈ AlkalicMetrixSpace
 - Notation Definition m ∈ n ≡ SetTheoremₒᵢ₍ₘ₎ₒᵢ₍ₙ₎ [oi := ObjectID]

### Lambda Including Calculate

Alkalic Algbra서 AlkalicVectorSpace나 oidfield = Σᵢ ObjectID eᵢ에 대해, 입력받는 Tensor입력으로 람다, 대수함수, Alkalic Algbra서 다가함수를 포함한 함수 구현.

변항은 이론에 인자로 설멸 가능

### Königsberg Axiom

⊢ KönigsbergAxiom(x, y, Φ) := (x = y ↔ (Φ ↔ (Φ [x := y])))

## About

이전에 나온 CSFBAlgebra에서 모델론이 안먹히나 했는데 먹힘, 그래서 아이 새로 CSFBAlgebra를 정리(바꿈), 그게 Alkalic.

M = (ℕ, 0 = ∅, s(x) = x ∪ {x}) 대신

수열의 곱을 다가함수로 써서,

M = Π<ℕ, [0 := ∅], [s := λx. x ∪ {x}]>

같은 서수의 정의가 가능하다는 점에서,

이제 Structure와 변수 대입까지 함수 안에서 됬음.

에초에 CSFBAlgebra를 대체할 목적으로 만든거니

나머지는 이하 생략.

### Alkalic-Proofmood

KönigsbergAxiom 에 따라서, 

 > 
 > 규칙 `using x = y → (Φ ↔ (Φ [x := y])))`
 > 
 > 원리 : `x = y ↔ (Φ ↔ (Φ [x := y])))`서 `x = y`가 결론 (5번 라인)과 같음을 보임
 > 
 > ```Alkalic-Proofmood
 > □.1. using x = y → (Φ ↔ (Φ [x := y])))
 > □.2. x = y
 > □.3. Φ
 > □.4. Φ [x := y]
 > □.5. Φ ↔ (Φ [x := y])
 > ```

 > 
 > 규칙 `using (Φ ↔ (Φ [x := y]))) → x = y `
 > 
 > 원리 : `x = y ↔ (Φ ↔ (Φ [x := y])))`서 `Φ ↔ (Φ [x := y]))`이며, 그것이 결론 (5번 라인)과 같음을 보임
 > 
 > ```Alkalic-Proofmood
 > □.1. using (Φ ↔ (Φ [x := y]))) → x = y
 > □.2. Φ
 > □.3. Φ [x := y]
 > □.4. Φ ↔ (Φ [x := y])
 > □.5. x = y
 > ```
 > 

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

Proof CSFBA nonHyperVersion 형식증명의 근거.

동시에 유일한 Proof CSFBA HyperVersion에서의 형식증명

`y = x`, `y = z`가 가설일때,

규칙 `using x = y → (Φ ↔ (Φ [x := y])))`를 통하여, `y = z ↔ x = z`를 보인다, 즉,

문법상, `y = z ↔ (y = z ↔ (y = z [y := x]))` = `y = z ↔ (y = z ↔ x = z)`이므로, 

y = z ↔ (y = z ↔ x = z)를 표현하기 위한 잉여적인 체계다.

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