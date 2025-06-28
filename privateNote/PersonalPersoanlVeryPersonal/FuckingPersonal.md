# 개인용 요약본

## Web Files 

### [CSFB대수](https://faraway6834.github.io/unbeauty/privateNote/Proof/CSFBAlgebra)

````markdown
"계산 -(공리계로 확장) -> 수학"형태로 계획된, 수학체계 겸 형식증명 시스템

# CSFBAlgebra

## CSFBA-ARE-BARE-Axiomos

ℙ₁. Calculus Shorized Formular Bind Axiom : 
`x = y ↔ (Φ ↔ (Φ [x := y])))`

ℙ₂. AoI-Rid-Empty SetTheory Axiom : 
`SetTheory is AoI(AdjointMetrixExpression of InfiniteDirectedAcyclicTree) s.t. "(x ∈ y) ≜ SetTheory_{Rid⁻¹(x), Rid⁻¹(y)} (s.t. Rid (Sequnce of Every Object; Reversed id))" also "⊭ (x ∈ ∅) but ∃∅"`

(Rid는 의도적으로 정의하지 않음, 따로 계산을 따지지 않겠다는거임. 따라서 행렬로 구성되지만, 그 행렬을 알기 힘듬, 대신에, `∈`를 집합론 없이 선행대수만으로 정의하고, `∈`함수를 이용할수 있음)

### Proofmood-CSFBA

CSFBA (Calculus Shorized Formular Bind Axiom)에 따라서, 

 > 
 > 규칙 `using x = y → (Φ ↔ (Φ [x := y])))`
 > 
 > 원리 : `x = y ↔ (Φ ↔ (Φ [x := y])))`서 `x = y`가 결론 (5번 라인)과 같음을 보임
 > 
 > ```Proofmood-CSFBA
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
 > ```Proofmood-CSFBA
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
 > 규칙 : `HPCSFBAristotel-y` (nonHyperVersion 형식증명 only)
 > 
 > HPCSFBA Theorem이라는 외부정리를 이용하여서, y = x이고 y = z이면 x = z임을 보임
 >
 > 규칙 : `HPCSFBAristotel-z` (nonHyperVersion 형식증명 only)
 > HPCSFBA Theorem이라는 외부정리를 이용하여서, x = z이고 y = z이면 y = x임을 보임
 > 

### HPCSFBA Theorem (Hyper PCSFBA Theorem)

Proof CSFBA nonHyperVersion 형식증명의 근거.

동시에 유일한 Proof CSFBA HyperVersion에서의 형식증명

`y = x`, `y = z`가 가설일때,

규칙 `using x = y → (Φ ↔ (Φ [x := y])))`를 통하여, `y = z ↔ x = z`를 보인다, 즉,

문법상, `y = z ↔ (y = z ↔ (y = z [y := x]))` = `y = z ↔ (y = z ↔ x = z)`이므로, 

y = z ↔ (y = z ↔ x = z)를 표현하기 위한 잉여적인 체계다.

## Proofmood-CSFBA (Power Up - Version)

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

마크다운 문서 내부에 위치했다면, PCSFBAH(Hyper Version), PCSFBA(일반 버전), PCSFBAP(Power Up버전)으로 코드 이름인 부분만 읽는다. 또한, 마크다운 부분에 부분증명 코드부분은, 부분증명으로 렌더링한다.

마지막으로 그렇게 html화되어 정리된 렌더링 뷰는, LaTeX 표기 기능을 추가해야만 할것이다.

(그럼에도 해당 html뷰는 아직 형식증명 검토가 안돌아갔으므로, 컴파일 상태인거지, 실행 상태가 아니다. 실행은 실행기에 돌려야, 문서 내부를 파싱해서, 부가적으로 제공된, [labare](https://faraway6834.github.io/unbeauty/privateNote/Proof/labare)•[unbare](https://faraway6834.github.io/unbeauty/privateNote/Proof/unbare) 코드와 함깨 해석하여(labare•unbare는 인터프리터 언어가 아니고, 정형 대이터 겸 사용자 편의 대이터 겸 Low Level 컴파일 언어다.), 검토된다; 이제보니 실행기보다는, 형식증명 검토기라는 명칭이 더 적합하다, 프로그래밍 언어는 하나도 실행하지 않고, 추론규칙을 재대로 활용했는지만 검사하여 검토작업(오류나 로그나 상태 표시)만 하기 때문이다.)

---

CSFBAlgebra 호환 공리계 : 대수(선형대수학 포함)와 람다(λ) 산술을 기술할수 있으며, `x = y ↔ (Φ ↔ (Φ [x := y])))`가 참인 공리계

주의 : AoI-Rid-Empty SetTheory Axiom에서 말하는 집합 체계는 집합을 쓰지 않고 함수화겠다(`f(S)(x) = (x ∈ S)`로 집합을 활용하겠다)는 소리라서, 선형대수를 사용할수 있으면, AoI-Rid-Empty SetTheory를 모델링 가능하므로, AoI-Rid-Empty SetTheory Axiom은 고려할 필요조차 없다.
````

### [labare언어 계획](https://faraway6834.github.io/unbeauty/privateNote/Proof/labare)
```markdown
# labare 언어 계획

[Linear Unbeauty](https://faraway6834.github.io/unbeauty/privateNote/Proof/LinearUnbeauty)의 확장이며, 람다 산술이 지원된다.
구체적 구현은 미룰 예정이며,
성능대신 생산성이 높아보이는데, 실제로는 내 성격상 성능쪽으로 갈것같다.

형식증명에 쓰일 언어이다.

행렬 입력 / 반환을 언커링된 Input / Output으로 처리하는, Subrootine Realationship이라는 종류의 연산이 있다만, 실제로는 흉내만 내고, 아무짓도 안한다.

Proofmood 모드에서만 쓰는 기능이다

## 명칭 [유래](https://genius.com/Edna-st-vincent-millay-euclid-alone-has-looked-on-beauty-bare-annotated)

음...
```

### [LinearUnbeauty 언어 계획](https://faraway6834.github.io/unbeauty/privateNote/Proof/LinearUnbeauty)

```markdown
# LinearUnbeauty 계획

선형대수를 지원하는 [Unbeauty](https://faraway6834.github.io/unbeauty)

... 가 끝임
```


### [unbare언어 계획](https://faraway6834.github.io/unbeauty/privateNote/Proof/unbare)

```markdown
# unbare 언어 계획

형식증명용 언어이다.

실행 목적이 아닌 [labare](https://faraway6834.github.io/unbeauty/privateNote/Proof/labare)코드를 뱉는 용도이다.

output laber code의 구조 :
 - virtual pararel scadular
 - calculatible part
     - pararel scadular
     - haltible part
     - outof haltible part
 - uncalculatible part

그러니까, 수학적인 Subrootine-Relationship 코드를 만드는게 목적이다.
```

### [Unbeauty 언어](https://faraway6834.github.io/unbeauty)

````markdown
# unbeauty

unbeauty esolang (0⁰=1, x->0 x^x->1)

mathmatics.... beautiful 4 me....

`sementically-recursive-defined-recurrence-formular based` programming language

actually, I didn't finished this work, because of my high school exam.
~~Fucking Korea~~

## example

[tip (lang=ko)](https://FarAway6834.github.io/LAFTF1.1)

noptlib.unbe
```unbeauty
sqrt = cacher[1](λx. x^0.5)
abs = cacher[1](λx. this.sqrt(x^2))
partial_beq0c = cacher[1](λx, n, p. ((0^this.abs(n)) + n×(x + ((-1)^p)×n) ÷ (0^this.abs(n) + n^2)) × f(x, n - 1, p))
partial_beq0 = cacer(λb, x, p. this.partial_beq0(x, 2^b - p, p))
beq0 = cacher[1](λb, x. this.partial_beq0(b, x, 0) × this.partial_beq0(b, x, 1)
beq = cacher[1](λb, x, y. this.beq0(b, this.abs(x - y)))
dose_it_positive = cacher[1](λb, x. this.beq0(b, this.abs(b, x - this.abs(x))))
__cmp__ = cacher[1](λb, x. this.beq(b, x) + (-1)^(this.dose_it_positive(b, x)+1))
__le__ = cacher[1](λb, x, y. this.dose_it_positive(b, x - y))

conditionalidx = cacher[1](λp,x,y.p×(x-y)+y)
conditional = cacher[1](λp, x, y. p×x + (1-p)×y)
_4bit_eqer_ = cacher[1](λx,y.this.beq(4,x,y))
_4bit_idxer = cacher[1](λi,a0,a1,a2,a3,a4,a5,a6,a8,a9,aA,aB,aC,aD,aE,aF.this._4bit_eqer_(i,0)×a0+this._4bit_eqer_(i,1)×a1+this._4bit_eqer_(i,2)×a2+this._4bit_eqer_(i,3)×a3+this._4bit_eqer_(i,4)×a4+this._4bit_eqer_(i,5)×a5+this._4bit_eqer_(i,6)×a6+this._4bit_eqer_(i,7)×a7+this._4bit_eqer_(i,8)×a8+this._4bit_eqer_(i,9)×a9+this._4bit_eqer_(i,10)×aA+this._4bit_eqer_(i,11)×aB+this._4bit_eqer_(i,12)×aC+this._4bit_eqer_(i,13)×aD+this._4bit_eqer_(i,14)×aE+this._4bit_eqer_(i,15)×aF)

not = cacher[1](λx.1-x)
and = cacher[1](λx,y.x×y)
sor = cacher[1](λs,x,y.x+y-(1+s)*this.and(x, y))
or = cacher[1](λx,y.this.sor(0,x,y))
xor = cacher[1](λx,y.this.sor(1,x,y))
nand = cacher[1](λx,y.this.not(this.and(x,y)))
nor = cacher[1](λx,y.this.not(this.or(x,y)))
nxor = cacher[1](λx,y.this.not(this.xor(x,y)))
sub =  cacher[1](λx,y.this.and(x,this.not(y)))
rsub = cacher[1](λx,y.this.sub(y,x))
rimp = cacher[1](λx,y.this.not(this.rsub(x,y)))
imp = cacher[1](λx,y.this.not(this.sub(x,y)))
a = cacher[1](λx,y.x)
b = cacher[1](λx,y.y)
nota = cacher[1](λx,y.this.not(x))
notb = cacher[1](λx,y.this.not(y))
logicalerr = cacher[1](λx,y.0)
alwaystruth = cacher[1](λx,y.1)
lpu = cacher[1](λcod,x,y.this._4bit_idxer(cod,this.logicalerr(x,y), this.and(x,y), this.sub(x,y), this.b(x,y), this.rsub(x,y), this.a(x,y), this.xor(x,y), this.or(x,y), this.nor(x,y), this.nxor(x,y), this.nota(x,y), this.rimp(x,y), this.notb(x,y), this.imp(x,y), this.nand(x,y), this.alwaystruth(x,y)))

__gt__ = cacher[1](λb, x, y. this.not(this.__le__(b, x, y)))
__lt__ = cacher[1](λb, x, y. this.__gt__(b, y, x))
__ge__ = cacher[1](λb, x, y. this.__le__(b, y, x))

__ne__ = cacher[1](λb, x, y. this.not(this.beq(b, x, y)))
bits2bool = cacher[1](λb, x. this.not(this.beq0(b,,x)))

shr = cacher[1](λx, n.x÷(2^n))
shl = cacher[1](λb, x, n.(2^b)×x-(2^b)×(x÷(2^(b-n))))
idx = cacher[1](λb, x,i.this.shr(this.shl(b, x, i), b))
_bpucc_ = cacher[1](λb, cod,i,x,y.this.lpu(cod, this.idx)(b, x, i), this.idx)(b, y, i)) × (2^i))
_bpuc_ = cacher[1](λb, cod,i,x,y.this._bpucc_(b, i,x,y) + this.bits2bool(i)×this._bpuc_(b,i-1,x,y))
bpu = cacher[1](λb,cod,x,y.this._bpuc_(b,cod,b-1,x,y))
```

ex2.ubt - extend not base cls, ex1 cls.
```
:noptlib
fibo = cacher[1](λb, x.this.conditional(this.beq0(b, x), 0, this.conditionalidx(this.beq(b, x, 1), 1, this.fibo(b, x - 1) + this.fibo(b, x - 2))))
```

## [coding plan 24.02.24 ~ ...](./plan)

### compile time lazy evil optimizing

`[○×]this.__NAME__(□)` -> `([○×]this.__NAME__)(□)`

 > also as `conditional` too. (when it is arguemnt, not return)

## FUOIR Unbeauty Optimize IR

example.unbe
```unbeauty
temp = cacher[0](λx. 2 × x)
main = cacher[0](λx. this.temp(x) + 1)
```

example.auty (jsonic)
```fuior
[
        0,
        "x",
        "this.temp(x) + 1",
        {
                "temp" : [0, "x", "2 × x"],
        }
]
```

### plan change

not using macro, will use PCRE

#### symopt

just add optimizer at ir,
that sympy optimizer.

`this.□(○)` -> `base64(hash(□(○)))` to symbolize (like-lexing)
````

### LAFTF1.1말고 다른이론으로 갈아탔기에, 그 이론을 적겠음. [주장](https://faraway6834.github.io/unbeauty/privateNote/MAD/%EC%A3%BC%EC%9E%A5)

````markdown
# 주장

(총 422 line)

## 목차

 - 전제
 - 전제에 따른 함의
 - 1. 픽토그램(pictgram)에서 보존 개념(conservation)이 불필요한 이유
 - 2. 수라는 수학에서 추상적 보존 개념 (conservation)의 핵심적인 부분이 왜 형식적 논리인 수학으로 작성되어야 하는가
 - 결론

## 전제

우리는 외부새상을 감각으로밖에 인지할수밖에 없기에, 내부 새상(본인의 생각의 언어 L을 가정하고 L이 작동하는 본인)은 와부새상에 대해 귀납적인 추론밖에 할 수 없다.

## 전제에 따른 함의
그런 외부 새상에서 일관됨을 연역적으로 보일 방법은 존재하지 않으며, 따라서, 외부 새상이 형식적인 논리로 서술되는지도 연역적으로 합리화할 방법이 없다.

## 1. 픽토크램(pictgram)에서 보존 개념(conservation)이 불필요한 이유

---

---

### 첫번째 글 : 보존개념

목차
1. Defination of Unary
2. PlasticArrow
3. 시각 감각 언어 `L`을 가정하자.

#### Unary and PlasticArrow

##### Defination of Unary

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

---

사용법 : 

> `(∃UnarySystem(F) s.t. ⊢ ℙ₁)( ⊢ T)`

ℙ₁은 "†문자열은 문자의 튜플이고, ‡아래 구문론적 등호가 성립한다"는 뜻이기에, ℙ₁이 참일때, †문자열을 문자의 튜플로 정의하고, ‡제시한 구문론적 등호를 받아들이며,  ℙ₁이 거짓일때, †문자열을 문자의 튜플로 정의하지 않고, ‡제시한 구문론적 등호를 받아들이지 않는것이다.

즉 문자열의 정의와 표기법을 허용하면 참, 그러지 아니하면 거짓이지. 따라서, `s.t. ⊢ ℙ₁`이라고 하면, F에 대해, ℙ₁이 참이라고 강제하는 뜻인것이다.

###### 상수 "PlasticArrow" 정의

ℝ²나 ℝ³범위에서 다음을 정의한다

> 
> **Plastic Arrow**
> 
>  - `⮕`는 벡터공간 `𝕍 = ℕ₀¹`에서의 "기저벡터"
> 
> 참고로 Unary에서 표현하는 수는 `⮕`가 선형생성하늨 벡터공간의 스칼라이다.
> 
> **Padic Plastic Arrow**
> 
>  - `⇨`는 초실수체 벡터공간 `𝕍 = ℚ¹`에서의 "기저벡터"
> 
> **Standard Plastic Arrow**
>
>  - `➡️`는 벡터공간 `𝕍 = ℝ¹`에서의 "기저벡터"
> 

이는 유클리드 기하학에서 직선 l과 그 위의 점 O, X, P에 대해,
O를 원점으로 잡고, 반직선인, 시초선 OX, 동경 OP의 X, P를 좌표 혹은 벡터로 보는 방식으로도 유클리드 기하학에서 재서술할수 있다.

---

번외 : 실현?

> 
> 물론 현실에 저런것들을 만들려면 「플라스틱-화살표 교구」에 "단면"이 존재해야하는게 함정이다.
> 
> 그러나 "플라스틱 화살표 교구의 단면"은 "폐곡선의 방정식" `F(x, y) = 0`으로 표현하면 된다. (따라서, "플라스틱 화살표 교구의 단면의 폐곡선의 방정식 음함수 표현 F"가 존재한다.)
> 
> ---
> 
> "실현" ㅋㅋㅋㅋ... 개연성도 없거니나와, 웃긴다. ㅋㅋ
> 

####### 시각 감각 언어 `L`을 가정하자.

######## 정의

L은 pictogram 언어이다.
단순히 pictogram을 나열한다.

######### 센다는 것(算)은 pictogram을 새는것으로 정의된다.

수를 세는 함자 "산자 System"를 정의하겠다.

> `算子システム ≡ [算 := λx. RF(x)⁻¹ [R := λf.λx.λy.fyx]] (단. (∃UnarySystem(F) s.t. ⊢ ℙ₁)( ⊢ T))`

그러면,

`算(□) (算子システム)`는 **변항 □에 들어갈 pictogram을 새는 함자이다.**

> ex) `算("⮕")("⮕⮕⮕⮕⮕") = 5 (算子システム)`

이때 저 pictogram문장은, 수학언어에서 접근한것이기에, 그냥 문자열 해석이다.

문법 번역식 교수법마냥, 픽토그램을 픽토그램이 아닌 문자열로 해석했기 때문에,

이는 쐐기문으로 쓰여있는 고대 메소포타미아 문명의 언어 글자를, 숫자로 취급하는것과 같은셈이다.

따라서, pictogram과는 무관하게, 수학이 이것에 의미를 부여한 것이다.

사실 pictogram외에도 걍 문자열이면 다 셈 함수의 정의역이므로, 셈은 우리로 하여금 새상이 수로 해석될수 있다고 귀납적 추론에만 근거한 주장을 펼치게 한다.

---

---

보존 개념 (conservation)은 귀납적으로 증명되었지만, 연역적으로는 그 자체를 가정할때, 형식적 논리인 수학을 요구하기에, "증명되지 못한 (말할수 없는)것" 이며, 전조작기가 지나고, 구체적 조작기에 들어서 후천적으로 얻는, 보편적인 개념이다.

conservation을 놓고 생각해보자. 

> `🍑🍍🍍🍊🍓`라는 pictgram이 있다.

해당 픽토그램이

> `🍑🍍🍊🍓`

로 바꿔도 무방하다.

따라서, pictgram은 conservation을 요구하지 않는다.

따라서, pictogram새상에서도 conservation을 합리화할 방법은 존재하지 않는다.

따라서, 외부 새상이 pictogram으로 인식되어도, conservation을 합리화할 방법은 존재하지 않는다.

### 수라는 보편적 개념이 얼마나 보편적인 지성적인 개념일까

수에 대한 이해(「"수학적 관점에서, 외부 새상의 대상의 양이 셈으로 해석된다"는 결과를, "셈이 근본이다"라는 확대해석 • 합리화」한것이 수이다)를 보면, 수는 언어적으로 만들어진 요소이므로, 이해하지 못할수도 있다.

이러한 측면에서, 난산증은 엄청나게 보편적인 언어적 가정인 수를 이해하지 못하는 장애라고 볼수 있겠다.

Charactor/Text(String)은 Language의 Symbolization(심볼화)이며,
Symbol(기호)은 특정한 의미를 가지도록 약속된 도형(圖形)이다

그리고 이것은 정말로 엄청나게 보편적인 개념인데,

이러한 측면에서, 난독증은 엄청나게 보편적인 인간이 창조한 개념인 문자를 이해하지 못하는 장애라고 볼수 있겠다.

마지막으로, 자폐증의 경우 템플 그랜딘이 말했듯, 자폐증 내부의 언어는 그림일수도 있다.

작성자 본인도 자폐증이긴 하다 (나는 내가 자폐증이여서 자폐를 싫어하긴 하니 자폐를 변호하는게 아니지만) 자폐증의 경우, 언어를 본인 맘대로 해석하는 경항을 띄는 사람이 있다 (예시 : 본인)

언어는 그 본질이 기존의 뜻으로 결정되지 않고, 필연적으로 의외성을 수반해여만 한다.

즉 일상 언어의 본질은 인간 사고 기저에 있는 의외성과 통념(정확히는 개념에 가깝다. 예를들어, 눈을 찡그린 사람은 화난것)에 있다.

이러한 의외성은,

> 
> 인간이 보편적으로 가지는 태생적인 지능에 따른, 언어의 지능적 의외성과
> 인간이 기본적으로 가지는 통념(개념; 예를 들어 "뿌린대로 거둔다"는 하는데로 돌아온다는 뜻이라는거, 그 의외성의 핵심 개념)에 따른 언어의 통념적 의외성이 있을것이다.
> 

따라서, 인간이 사고의 근본인 언어에 있어서, 본질적인 부분에 대한 엄청난 이해 결함을 가진 장애인으로, 일부 자폐성 장애인 (예시 : 초등학생때 본인)이 있을것이다.

이러한 관점에서, 난산증에게 결핍된 능력은, 보편적인 수에 대한 개념이라고 볼 수 있다.

이러한 수 개념은 수에 대한 어느정도의 이해를 필요로 하므로,

수에 대한 보편적인 지능과 이해능력은, 난산증을 제외한 인간이 매우 발달한것일 뿐, 본질적인것이 아니라고 볼수 있다.

정상인은 에초애 많은 부분에서 선천적인 지능이 있다.

그걸 없는걸 장애라고 하고, 솔찍히 그런 당연한거를 모르니까 약간 역겨운 감도 있다.

### 과학을 가져오는것에 대한 반론

과학(자연과학, 사화과학, 형식과학 등)과 같이 귀납적으로 증명된 대상들은 지금 이 연역적인 논의에서, 귀납적이지만 연역적이지 않다고 반박하니, 과학을 예시로 반박하면 안될것이다.

그렇게 되면 새상이 과학적으로 이루어졌다는 가정으로 수학을 증명하고 다시 과학을 증명하는 순환 논증에 빠질것이고, 이러한 방식으로, 새상이 과학으로 이루어졌다는 전제로, 과학의 탐구 방식이나 수학을 합리화 하는 즉시, 그것은 수학에서 금한 자기참조를 범하는것이다 (따라서, bootstraping같은 과정은, 자기참조를 범하는 합리화이므로, 연역논증이랑은 거리가 멀다 (inference to the best explanation라고 하는것도 이해가 안된다))

또한 과학은 수학을 수반하지 않아야 될 수도 있다.

만약 과학에서 수학을 쓸수 없다는게 증명됐다고 가정하자,

그러면 과학은 수학을 사용해야 한다는 가정이 깨지므로,

페러다임 시프트가 일어날 것이다.

과학이 수학을 사용해야한다는 가정은, 과학이 형식논리를 이용해야한다는 가정과 동등한 뜻이다.

그런데 과학이 형식논리를 이용해야한다는 가정은, 해당 과학이 일관된 형식적 논리로 서술될수 있다는 가정이므로, 해당 가정이 성립하기 위해서는, 논리를 사용하기 위한 규칙 (공리계, 언어, 표기 등)과 과학이 일관된 대상을 탐구해야한다는 가정을 가지게 되므로, 공리계를 사용할수 있다는 근거와 탐구하는 대상이 과학적이라는 근거가 있어야만, 연역적으로 뒷받침될수 있다.

## 2. 수라는 수학에서 추상적 보존 개념 (conservation)의 핵심적인 부분이 왜 형식적 논리인 수학으로 작성되어야 하는가

---

---

### 두번째 글 : 논리적으로 다룬다 전재할때, 대수식은 논리적으로 그 뜻이 해석 • 계산된다.

그렇지 아니하면, 논리적 해석 흐름에서 논리기호가 도출될수가 없다.

식의 계산은 그 값의 배정인 (x̄, f(x̄))와 같이 이루어지는데, 이 방식을 거부하는것은, 논리를 쓰지 않겠다는 말과 같다. (장자 왈 갓나서 죽은 아기보다 오래 산 사람은 없으니 팽조(760살이 넘게 살았다는 전설 상의 신선)도 일찍 요절한 사람)

#### 다음 과정을 위해 이항을 먼저 증명하겠음

함수는 (다가함수 고려하지 않음)

> 정의역의 x에 대해, `∀x ∃!f(x)`이다

먼저, y랑 z을 정의하자.
 - y = f(x)
 - z = f(k)

[*작성중*]

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

---

---

따라서, 수학에서 말하는 "추상적 보존 개념 (conservation)의 핵심으로써의 수"는 수학 없이 독자적으로 성립할수 없다. (단. 언어에서 수사같은 거나 숫자같은거는 수학적으로 해석하는것이 아니기에 본인은 수로 취급하지 않았다. 언어에서는 수에 의외성을 가지고 해석할수 있기에, **실제로 일관되지 않는다**; 시에서 갑자기 하나가 두개가 될수 있다.)

## 결론

따라서, 픽토그램으로 우리가 새상을 받아들인다 쳐도, 픽토그램 새상에서도 수, 수학, 보존개념은 요구되지 않으며, 해당 개념들은 언어를 통한 부가적인 개념일 뿐이지, 비물질적 실체가 아니다.
````

## 본론

내가 「주장」에서 언급한것과는 별개로, 「CSFB대수」를 계획하고 있으며, 대수만을 이용한 연산으로 충분히 논리연산을 만들수 있음은 「주장」에서 미리 언급함.

현제의 수학(ZFC, Peano, ZF, Gödel Encoding, 표준 해석학과 비표준 해석학등등)이 CSFBAlgebra 호환 공리계일까?