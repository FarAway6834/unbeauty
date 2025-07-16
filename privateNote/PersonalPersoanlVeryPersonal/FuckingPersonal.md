# 개인용 요약본

(총 1783 line 48782 자)

## Web Files 

### [CSFB대수](https://faraway6834.github.io/unbeauty/privateNote/Proof/CSFBAlgebra) -> 폐기하고 최하단에 있는걸로 변경.

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
~~■■■■ing Korea~~

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

### [Language and Math](https://faraway6834.github.io/unbeauty/privateNote/MAD/Language_And_Math)

````markdown
# Language And Math

(총 692 line 14312 자)

목차:
 - 수학과 언어
 - 수란 무엇인가
 - 의외성 정리

## 수학과 언어

수, 수사 등은 크기 개념이다. 이러한 크기 개념은 곧 설명할 일개 사고방식에 불과하며, 이러한 수에대한 설명의 형식적 방언이 수학이다.
그러나 언어는 근본적인것들이 아니다.

시작해보자.

언어에 대한 해부를.

# 수란 무엇인가

(총 534 line 11828 자)

이야기 하기 앞서, 말하고자 한다.

나는 이 주제에 대하여, 수는 수학적으로 정의되는 추상적 대상이며, 형이상학적인 허상 취급을 했었다

아래는 그 글이다

```
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
```
이 글은 틀렸다.

해당 픽토그램을 해석함에 있어서, 우리는 기저에 깔린 지식을 이용하여 그 갯수를 알수 있다.

선험적이거나 경험적이거나 언어적이거나 본능적인것 아니냐는 질문에 틀렸다고 반박했다고 볼수 없는 글이다.

## Step 1. 생각의 선행

생각은 내용을 가진다, 여기서 생각은 그냥 직설적인 생각이며, 내용은 상자안의 내용물 같지만 추상적이라 설명할수 없다. 나는 그 내용이 글이라고 한적이 없다. 내용은 내용이며 그 내용이 무엇인지 우리는 말할수 없다.

생각의 다음 생각에 대해서도 단정하면 안된다. 생각의 다음 생각이 어떻게 되는건지 우린 모른다.

그러나 우리는 생각하려한다, 스스로 정신적인 방법으로 식물인간이 되고자 하지 않는다, 물론 의식적으로 "나는 정신적인 방법으로 식물인간이 될거야"라고 생각한다면 생각이다.

인간이 고등하다는 말에 속뜻, 그 생각을 버리자.

말의 속뜻중 의심되는건 일단 다 버리고 들어보라.

생각 다음 생각을 정해보는것, 생각을 전파하는것, 생각을 당연한 생각 다음 생각 방식으로, 나의 기본적인 능력으로 이해하는것, 그리고 외부에서 기인한 일로 생각이 추가되는것. 이러한 것을, "개척"/"전파"/"이용"/"추가"라고 하며, 우리 생각이 이러한 특성을 가진다는것이 공리이다.

여기에서 추가는 유일하게 능동적으로 하는게 불가능하다. (요청하는것도 수동적으로 받아들이게 해달라는거니)

그리고 전파는 생각을 공유하는거다. 전파를 받는거는 모른다.

그러나 이용하는것은, 당연한 생각 다음 생각을 이용한다. 이러한 당연한 생각 다음 생각으로 능력을 말위하는걸 잠재 능력이라 하여, 재능이라 한다.

우리는 대부분, 언어에 대한 재능으로 언어를 습득할 능력을 가지고 있고, 크기를 습득할 능력을 가지고 있다.

이것들은 재능인 경우가 대부분이지만 특수한 경우를 보자면 아니다.

언어와 크기는 습득하니까, 생각이다.

언어와 크기가 전파되었으니 말이다.




사실 크기같은 경우에는 전파해준 사람 없이도 사물에서 기인하여 나오기도 한다.

어떻게 된지는 몰라도 이미 존재한거고, 우리는 그것우로 생각하며 우리는 그것에 대한 관점화된 틀을 벗을수 없는 부분이 있다.




이러한 벗을수 없는 "단단한 틀"이 있다. (예시 : 윤석열 하면 계엄이 떠오른다... 농담ㅋㅋ 이런건 예시로 적절치 않군 ㅋㅋ)




이러한 개념들이 이용을 통해서 추가되는경우가 매우 많다.

특히 살아남기 위해 필요하면 더더욱.
우리는 생각하려는 의지를 가지며, 언어와 크기는 그것의 대표격이다.

그러한 능력이 선천적인 필수 루트가 아닌 이유는, 그렇지 않은 예외경우가 존재하기 때문이다.


내가 본 대부분은 언어습득능력이나 크기습득능력을 생습적 재능으로 가진다.

그러나, 이러한것은 생각흐름을 탁! 바꿀수 있거나 그 생각흐름을 주는 경우들이 많으며,

이러한 "기저에 깔린" 생각들은 생각이지 인간의 필수 능력이 아니다.

생각이 선행한다.

## Step 2. 크기 개념

크기 개념을 생각하는것은 대부분 된다.
생각하지 못했다 해서 난산증을 차별할 근거가 되지 않는다는것도 당연하다.



정량화된 크기 개념이 수(數)이며, 수학 언어는 수를 다루는 언어이다.

그런데, 수학 언어는 형식 언어로 설명된다.

따라서, 크기 개념이나 수학을 다룸에 있어서, 크기나 수학에 기초한 서술을 접근할수 없는 사람이 있음은 매우 당연하다.



언어 혹은 수(數)나 수학적 서술이나 크기 개념은 우리가 생각할수 있도록 익혀진 상태일때야 사용 가능한 것이지, 재능이 아닌 이상 생습적이지 않다.



한 문장으로 정리하겠다.



다른 관점 말고, 생각하는 관점에 있어서,
언어나 수, 수학적 서술과 크기는, 우리가 생각하는 것에 있어서 생각이며, 재능으로 타고나지 않으면 본능이 아니다.



이걸 얼마나 더 쉽게 설명해야 할지 모르겠다.



재능이라거나 이런말보다는 생존을 위한 (사자들에게도 크기 개념은 있음) 생각, 사념체일 뿐.

이상.

# 의외성 정리

## 용어 정의

 - True Mean (참뜻) : 의외성(속뜻)
 - Shell Mean (껍대기 뜻; 쉘 민) : 겉뜻
 - 속뜻 없음 (Exceptless) : Shell Mean = True Mean
 - 초완전성 (Hyper-Completeness) : "This sentence is False"를 허용하는것.
 - Black and White Proposol : ⊢ (¬Hyper-Completeness)
 - Simply Mean Proposol : ⊢ Exceptless
 - 단순언어 : Simply Mean Proposol이 항진인 언어

### 흑백논리와 형식언어의 정체에 대한 고찰

Black and White Proposol를 공리로 하는 논리를 흑백논리라고 부를수 있음이 당연하다

또한 흑백논리중 단순언어인것이 형식언어인것이라도 보면 된다.

#### 정리 문단에 따른 보조설명

우리 언어는 보이는대로 해석해야하는것과 아닌것이 있어,

보이는대로 해석해야하는것을 단순언어 (이 경우 언어 해석에 예외가 없이 보이는대로 닥치고 그뜻이다)

그리고 단순 언어가 아닌 언어 (이 경우, 언어 해석에 여러 의외성이 끼어들기에, 단순히 보이는 뜻을 뜻으로 단정할수 없다)가 있다

또한 논리는 장자철학처럼 "갓나서 죽은 아기보다 오래 산 사람은 없으니 팽조(760살이 넘게 살았다는 전설 상의 신선)도 일찍 요절한 사람이다"가 맞을수 도 있지만,

흑백논리에서는, Black and White Proposol을 참으로 하여, x이면서 동시에 x가 아닌것은 불가능하다. (Fun Fact : 흑백논리이면 단순언어임이 논리적 귀결이다)

## 공리

1. 말의 뜻은 True Mean과 Shell Mean이 있다

## 정리

### TrueMean Theroem

Hyper-Completeness 일때도 "말의 뜻 ≠ True Mean"마저 True Mean으로 True Mean(결국 전제로 한 참인 문장에서 연역(이때는 초완전땜에 가능)으로 "말의 뜻 = True Mean")이고 (Hyper-TrueMean Lemma)

Hyper-Completeness 가 아닐때도, "말의 뜻 = True Mean"이므로, 말의 뜻 = True Mean으로 (Formal-TrueMean Lemma)

말의 뜻은 True Mean을 말한다. (TrueMean Theroem)

A. Formal-TrueMean Lemma
 - ¬Hyper-Completeness, ⊭ 말의 뜻 ≠ True Mean ⊢ 말의 뜻 = True Mean

B. Hyper-TrueMean Lemma
 - Hyper-Completeness, 말의 뜻 ≠ True Mean ⊢ 말의 뜻 = True Mean

C. TrueMean Theroem
 - 말의 뜻 = True Mean

Proof)

1. 말의 뜻 ≠ True Mean [Hyp]
2. Hyper-Completeness [Hyp]
3. "말의 뜻 ≠ True Mean"라는 점도 True Mean임
[Paradoxic Lemma]
3. "말의 뜻 ≠ True Mean"라는 점도 True Mean이고 참이기에, 말의 뜻 = True Mean임
4. 말의 뜻 = True Mean

이하에서,

말의 뜻 ≠ True Mean, Hyper-Completeness ⊢ 말의 뜻 = True Mean ⋯ (1)

1. 말의 뜻 ≠ True Mean [Hyp]
2. ¬Hyper-Completeness [Hyp]
3. "말의 뜻 ≠ True Mean"라는 점도 True Mean임 [Paradoxic Lemma]
4. 모순

이하에서, ⊭ 말의 뜻 ≠ True Mean ⊢ 말의 뜻 = True Mean

(1), (2) ⊢ 말의 뜻 = True Mean

Q.E.D.

#### 해설

항상 True Mean만 말의 뜻임을 증명하자,

True Mean이 뜻이 아닌 말이 있다고 가정하자,
그렇다면 그 말은 True Mean이 뜻이 아니라는 뜻이 True Mean이 된다

이것이 Paradoxic Lemma다

이하에서 Hyper-Completeness에 따라 참인 경우와 거짓인 경우로 나누어 논증하자.



상황 1. Paradoxic Lemma에서, Hyper-Completeness인 상황

Paradoxic Lemma가 참이될수 있으므로, Hyper-TrueMean Lemma가 참이다

상황 1 종료



상황 2. Paradoxic Lemma에서, 비 Hyper-Completeness인 상황

Paradoxic Lemma이 모순이므로, 전재인 "말의 뜻 ≠ True Mean"이 거짓이다.

따라서, Formal-TrueMean Lemma가 참이다

상황 2 종료



이하에서,

상황 1, 상황2에 따라, 연역,
항상 True Mean이 말의 뜻이 된다.

따라서, TrueMean Theroem이 참이다

Q.E.D.

### Exceptless Thorem

Exceptless ⊢ 말의 뜻 = Shell Mean

Proof)

1. Exceptless [Hyp]
2. 말의 뜻 = True Mean [TrueMean Theroem]
3. Shell Mean = True Mean
4. 말의 뜻 = Shell Mean [결론]

이하에서, `Exceptless ⊢ 말의 뜻 = Shell Mean`임이 당연하다.

#### 해설

앞서 증명한 TrueMean Theroem에 따라,

말의 뜻 = True Mean

Shell Mean = True Mean 이면, 그리고 이때만 Shell Mean = True Mean이다

(쉽게말해 A = B = C니 A = C)
````

## 쉬운 설명용; 이전에 만든것들, 현제는 아래 내용들은 보완되어야 하거나 폐기 대상임.

### [SIOT](https://faraway6834.github.io/unbeauty/privateNote/SIOT)
```markdown
# SIOT[시옷], Standard IO Table (Mean : Standard Input and Output Truthtable)

목적 : 미리 배운 논리 연산을 이해하지 못하지만 사용하고 싶을때, 사용법을 제공할수 있음을 보임.

## 교육 구조.
논리 연산을 [FAN, Function AbbreviatedNaming](https://faraway6834.github.io/unbeauty/privateNote/functional_petterns_commandstyle_naming#%EA%B8%B0%EB%8A%A5%20%EC%B6%95%EC%95%BD%EB%AA%85%EB%AA%85%EB%AA%85\(%EC%B6%95%EC%95%BD%EB%AA%85%20%EB%AA%85%EB%AA%85\)%20\(Function%20AbbreviatedNaming\)%20%EC%B2%B4%EA%B3%84%20%EC%84%A4%EB%AA%85)으로 정의하여,
기능으로 사용하는 도구로 봄.

### SIOT의 해석.
그리고, SIOT가 그 모든 연산을 나타내는 계산표 (계산표의 예시론 덧셈표와 곱셈표와 제곱근표와 상용로그표가 있음)임을 보임.

### 논리 연산의 해석.
기존에 배운 논리 연산과, 그 예시로 든 글들을,
활용할때, 단순히 FAN으로 작성한 축약명 연산자들을 SIOT를 들어서 동등함을 보인다.
그러면 활용시 동등하니까 그냥 쓰면 된다.

### 논리 연산이라는 명칭의 납득.
이분법적 논리학이 극단적이라고 디스하고싶지만,
원래 수학이 그렇다고 하자.

## 모양세
사실은 진리값배정용 칸부분을 Input이라 명명하고, 표 왼쪽이 위치시키고, 나머지 연산을 오른쪽에 위치시킴.
그리고 진리표 윗부분에 Input과 Output이라는 대분류 셀만 덛붙침.

### 연산자의 좌측과 우측 (피연산자, 진리값 배정 대상)

좌측과 우측이 연산 대상이고, Left Side와 Right Side라고 영어로 말한다.
각 명칭을 줄여서 LS와 RS라고 부른다 (두문자어)

### 참과 거짓
참과 거짓은 특수한 정보로,
컴퓨터에서 이 의미를 나타내기 위해서는 정보를 저장해야한다 (팁 : "사실 프로그램으로 때워도 되" 라고 농답식으로 납득시킬수 있음)

컴퓨터에서는 참 = 있다 = 1, 거짓 = 없다 = 0

### 연산자명 명명 규칙
L□R■는 L이 □고 R이 ■라는 뜻이다.
명제 (판별가능) 이고, 진리값이 들어감으로, 의미로써 연산값을 가지고, 표기 가능하다.

0000이 정규형식일때 : AZVC(AlwaysZeroValueCommand)
1100이 정규형식일때 : GRSV(GetRSValue)
1010이 정규형식일때 : GLSV(GetLSValue)
정규형식의 보수를 부정으로 이해할때 : Non접두사 사용, 약어 `N`

#### 이외의 연산자들은 논리적으로 유도한다.
그부분에선 이해 못해도 된다. 결과만 사실 쓰면 되고, 나중에 배워도 활용엔 문제없으니.

#### 식을 약칭으로 바꿀때
```

### [CMD와 FUN](https://faraway6834.github.io/unbeauty/privateNote/functional_petterns_commandstyle_naming#%EA%B8%B0%EB%8A%A5%20%EC%B6%95%EC%95%BD%EB%AA%85%EB%AA%85%EB%AA%85(%EC%B6%95%EC%95%BD%EB%AA%85%20%EB%AA%85%EB%AA%85)%20(Function%20AbbreviatedNaming)%20%EC%B2%B4%EA%B3%84%20%EC%84%A4%EB%AA%85)

````markdown
## 이론
```markdown
# CMD 대수

1. CMD 차원
> D 구성
>  - M표기와 D표기의 다른차원으로의 제공에서, 각 정의부의 기저가 `기저열 □`안에 들어가게 정의하는 평가용 D장의 구성.
> D 대응
>  - 기저열 □의 길이가 항상 문법적으로 최대치로 D장과 M장의 차원이 각 문법의 의미적인 최대 차원과 충돌없이 대응되게 하는것.
> D 연산
>  - 타입 있는 람다식임. 상위 차원에서 M연산형태의 함수나 연산의 정의로 설명할 다른 정의의 평가에 이용됨.
> D 표기
>  - 기저에 대한 바인딩이 먹힘
>  - 다른 차원에서 이용되는것임. (M표기의 근간이 이것으로 M표기도 그렇다.)
> M 연산
>  - M 장의 각 함수로, 언커링된 D 연산임.
> M 구성
>  - D 공간에서 변환되어 구성.
>  - M 장에서 텐서곱 바인딩하여 D공간을 결정함.
> M 표기
>  - M 표기 정의식에, 각 M 기저에 대하여 대괄호를 씌어, 텐서곱 바인딩과, M표기 정의식에 대한 탠서곱 바인딩을 이룸.
M 대응
>  - D 장에 항상 대응하여 M장을 항상 D장에 대하여 존재하게 하는것.
> C 공간과 그 체계
>  - 슬롯임.
>  - M과 D를 가짐 (눈치 쳇겠지만 CMD, 커멘드)
>  - M대응과 D대응을 적절히 수행하는 C대응이 존재.
>  - C정의를 할때, M과 D의 수정이 이루어지고, C대응으로 C내부공간(사실 이게 지금 말하는 부분)의 수정이 이루어지는 C 구성이 존재.
> C 표기
>  - 각 정의의 추가시 C 구성을 이루게 하는 상위차원에서 평가하여 C 슬롯안에서 호출할 내부 아웃소싱 기계. (구성)

2. CMD 심볼 표기
 - □수열의 인덱싱을, □의 상단의 선의 우측지점의 선분을 제외한 부분을 좌표평면위의 그래프로 부분적으로 정의하고, 나머지 부분에 글자를 넣도록 정의하여, 기호용으로 그래프로 그려진 형태의 심볼을 표기법용 기호로 쓰게하는것.
 - CMD 이용 : 괄호없이 그저 폴란드 표기법으로 쓰는것
(표기)

3. CMD 포함.
최소한의 방법으로
 - A. 정의하는 부분의 차원 낮추기
 - B.1. 최소한의 의미적으로 최적이동한 포함.
등등으로 CMD평가용으로 상위에 구성할 차원을 의미적 구성용으로 치우는것. (알고리즘)

# 기능 축약명명명(축약명 명명) (Function AbbreviatedNaming) 체계
CMD대수로 함수형 연산자를 선언하는것을,
기능이란 뜻의 Function에서, Function역할을 하는 빈칸에 대한 패턴의 식으로, 연산자를 축양명으로 명명하는 개념으로 배울수 있는 사용체계.

## 기능 축약명명명 표기
바인딩 표기가 아닌 `#`이후 등식으로 작성한다.
```

# 기능 축약명명명(축약명 명명) (Function AbbreviatedNaming) 체계 설명

번호가 매겨진 빈칸이 있는 기능 패턴에, 기능 축약명 연산자의 특정 번째 입력값을, 번호가 메겨진 빈칸안에 대응시켜, 단순히 축약식의 축약을 풀어 그 뜻으로 치환하여 해석하도록, 기능 축약명 연산자를 기능에 대한 축약명으로 정의하도록 하는 기능 축약명을 명명하는, 기능 축약명 명명 체계를 만드는것.

따라서 의미적으로 등호가 성립한다.

## 전산표기
빈칸에 번호를 상단에 메길수 없기에, 
`🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄽🄼🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉` 와 같은 글자를 이어서 번호 빈칸을 대체한다.

### 예시 : Trinity 기능 축약명 연산자

 > (참고사항 NOTE : markdown에 소스타입을 FAN으로 명시함, 겹치는게 있을지도 모름)

정의
```FAN
# Trinity = 🄰(🄱 - 🄲) + 🄲
```

사용 (값은 여기서 12가 됨)
```FAN
Trinity 1 12 21
```

잘 가르쳐주는 사람이 있으면 좋을텐데...
내가 서술에 재능이 없어서 여기서 서술을 마치겠음.

# 저작자

100% 작성한 내몫임.
다 내가 적어논거임.
망상이라 어짜피 배끼지도 않을테지만 ㅋㅋ
설명용이라...

## 참고

핵심내용 목록
 - FAN (Function AbbreviatedNaming)
 - CMD 대수
 ````

 ### [수학이론 구버전, LAFTF1.1; 현제는 쉬운 설명용으로 준 폐기](https://faraway6834.github.io/LAFTF1.1)

 ```markdown
ol{margin:0;padding:0}table td,table th{padding:0}.c0{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c11{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:26pt;font-family:"Arial";font-style:normal}.c3{padding-top:0pt;padding-bottom:3pt;line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.c6{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:center}.c1{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c5{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:right}.c12{text-decoration-skip-ink:none;-webkit-text-decoration-skip:none;color:#1155cc;text-decoration:underline}.c10{background-color:#ffffff;max-width:451.4pt;padding:72pt 72pt 72pt 72pt}.c4{margin-left:36pt;text-indent:36pt}.c7{color:inherit;text-decoration:inherit}.c2{height:11pt}.c8{margin-left:36pt}.c9{color:#202122}.title{padding-top:0pt;color:#000000;font-size:26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-size:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}

LAFTF 1.1Logic-Algebra Formular TransForm 1.1

def)

    ⎧ To : {x|Set(x))} × {x|Set(x))} → {z|z={f:x → y | p(x, y)}}

p: ⎪

    ⎨

    ⎩ To : x, y ↦ {f | f : x → y}

def 표기) A To B ≡ To(A, B)

def 표기) A To B ≡ A 2 B

—------------------------------------------------------------------------------------------------------------------------

def) (∃! int ∈ Bool2{0, 1} ∃! int⁻¹ )( int⁻¹(x) ≡ (x = 1) ≡ (x ≠ 0))

def) bool ≡ int⁻¹

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

(bool · f)(x, y) :≡ bool(x) ∧ bool(y)

        (x̄, f(x̄)) = (x̄, ×(x̄)) (단. <×, Yᵢₙₜ>)

        ∵        ⎧ f(0, x) = 0 = 0 × x

⎪ f(1, x) = x = 1 × x

⎨

⎩  \[x, y\]ₕ = 1 = \[x, y\]ₓ (h=f, 기호의 한계…)

        ∵ f(n, x) = f(x, n) (단. n ∈ Yᵢₙₜ)

∴ f(x, y) = xy

단순히 같다는 의미이고…,

수학에 생각이란게 유효하다면 이건 자명한게 아닐까 조심히 추측해본다.

—------------------------------------------------------------------------------------------------------------------------

(bool · f)(x) :≡ ￢ bool(x)

        f(0) = 1, f(1) = 0

        ∴ f(x) = (0-1)/(1-0) x + 1 = 1 - x 로, 그래프 위애서 점을 찍을떄, 우리가 보고자 하는 점의 위치를 f(0)에서 f(1)로 수를 바꿔보면, 감소하는 수는 1을 얻으니 당연하다.

(아니 생략이 ㄹㅇ ㄹㅈㄷ, 어짜피 요약본이긴 한데 ■겁네)

* * *

그러면 Conjuntive Normal Form에 따라

⎧ b = ∑ Aₙ2ⁿ⁻¹ (n=1~4, 단. x̄ = (        (0, 0) ∧ f(x̄) = (A₁, A₂, A₃, A₄))

⎪                                        (0, 1)

⎪                                         (1, 0),

⎨                                         (1, 1))

⎩  Hexf(b) = f 인 Hexf(b)는 xy와 1-x로 조합 가능하다

이때, x ⊕ y = (x ∨ y) ∧ (￢ (x ∧ y)) = (x ∧ ￢ y) ∨ (y ∧ ￢ x) 인데,

        int(x ⊕ y) = int(x ∨ y) - int(x ∧ y)

        ∵        f₁(x, y) = xy

                f₂(x, y) = x + y - xy

                f₃(x, y) = int(bool(x) ⊕ bool(y))

                Hexf⁻¹(f₃) = Hexf⁻¹(f₂) - Hexf⁻¹(f₁)

        또한,

        int(x ⊕ y) = int(x ∧ ￢ y) + int(￢ x ∧ y) - int(￢ x ∧ y) int(x ∧ ￢ y)

        int(￢ x ∧ y) int(x ∧ ￢ y) = int((￢ x ∧ y) ∧ (x ∧ ￢ y)) = int(⊥) = 0

—------------------------------------------------------------------------------------------------------------------------

대충 프랑스에서 아이디어 떠올려서 영적인 힘을 줘서 고맙다는 ■소리가 적힐 칸이었는데…

■■이런또■이같은인생아지■난■가타서■나못참아죽■네■친어떻게■■내가■고생해서얻은LAFTF1.0이■■이미있냐위키백과에서xor기호얻으려고■■들어가봤더니나중에찾는건다른곳에서했고■벌아진짜■같이영문위키백과에■■아니거기를먼저들어갔더니얻은기호가아니진짜■얼탱이가없어가지고하아 제칼킨 식이라고 ■ㄴ좋은 이론이 선행으로 있었는데 이거 모르고 위에 내용 ■■ 혼자 하나하나 유도한 내가 ■■이지 ■■이야 ■나 ■생 ■반 ■해봤네 ㅋㅋㅋ ■친 뭐 앞으로 서술할 비트연산도 마찬가지겠지 뭐 하 ■발 인생.

shlᵦ(x) = shlᵦ(2ᴮ⁻¹ + x) (β = B (Bits) 동일하게, 기호의 한계, 참고로 겹쳐가시고 ■벌 한번 더 a서 β로 수정함. 아이고야 ㅠㅠ)

(shlᵦ)ₗₘ (Λ ≡ lm, 동일한 한계로 이런식으로 표기하겠음, ⁽\*⁾)

(shlᵦ)ₐ (아랫첨자 a가 없는 관계로… ■벌 ⁽\*⁾)

* * *

원래는 (=필기 원문대로 쓰면은) “그런대 아름다운 사실,” 이라고 써야하는데 ■같네 기분이 아직도 ㅋㅋ 이런 ■■ 아■다운 새상

f(x) = x - ⌊x⌋

f(x) = f(1 - x)

fₗₘ = 1 (참고 : ⁽\*⁾)

fₐ = 1 (참고 : ⁽\*⁾)

g(x) = 2f(x)

gₗₘ = fₗₘ, gₐ = 2fₐ, fₗₘ = fₐ,

gₗₘ = k, gₐ =2k (k = fₓ)

\~~~~~~~~~~~~~~~~~//

(shlᵦ)ₗₘ = k, (shlᵦ)ₐ = 2k (k=2ᴮ⁻¹)

shlᵦ(x) = k g(x/k)

또한, 동일하게 그래프나 함수 버전, 방금전 버전 유도도 있지만, 단순하게도, shl = ⌊x/2⌋ 다. x ÷ 2  = y … r, x ≡ y (mod. 2)고, ⌊x/2⌋ = (x-r)/2 다.  (아 아래로 …화되는거 ■ㄴ 띄껍내 개■■ (딥■))

시프팅시 일부 비트의 정보 손실(?) 을 이용하여

idxᵦ(x) = shrᴮ · shlᵦⁿ(x)

—------------------------------------------------------------------------------------------------------------------------

요약 나중에 하겠음 (EZ)

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

def) bitwise fᵦ (ΣA₁,ᵢ 2ⁱ⁻¹, …(×n)..., ΣAₙ,ᵢ 2ⁱ⁻¹) ≡ Σ f(A₁,ᵢ, …(×n)..., Aₙ,ᵢ) 2ⁱ⁻¹ (i = 1 ~ B)

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

nagation = bitwise-no, nagationᵦ(ΣAᵢ 2ⁱ⁻¹ =(= x)) = Σ (1-Aᵢ) 2ⁱ⁻¹ = Σ 2ⁱ⁻¹ - Σ Aᵢ 2ⁱ⁻¹ = (2ᴮ-1) - (ΣAᵢ 2ⁱ⁻¹ =(= x)), nagationᵦ(x) = (2ᴮ-1) - x (i = 1 ~ B)

—------------------------------------------------------------------------------------------------------------------------

p(◦, \*) := (a ◦ (b \* c) = a ◦ b \* a ◦ c인 (◦, \*))일떄

p(×, +)은 맞는데, p(+, ×)은 아니라서, 다항식 f에 대해 f(ΣA₁,ᵢ 2ⁱ⁻¹, …(×n)..., ΣAₙ,ᵢ 2ⁱ⁻¹) 2ⁱ⁻¹를 보통 구할때, 부정 연산이 아닌 논리연산은 항을 교환 불가능하다.

따라서, 뺄셈에 대해 음수화 시켜서 교환했던 부정 연산과는 달리 다른 Hexa(n)은 bitwise시 교화법칙을 응용한 증명이 나한테는 어렵다

* * *

킹치만 비트 인덱싱좌가 있다고 코삣삐.

bitwise fᵦ(x, y) = Σ f(idxᵦ(B - i, x), idxᵦ(B - i, y))2ⁱ⁻¹ (i = 1~B)

산술연산으로 다 1초컷 ㅋㅋ

참고 : f(x) = x - ⌊x⌋ 는 톱늬파의 일종으로, actan(tan(x/π))도 톱늬파의 일종으로, 가우스 함수는 ㄹㅇ로 그냥 ■ㄴ 초딩도 이해가능한 ■ㄴ 자명한 산술연산이라고 ㅋㅋㅋ

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

def) (∃! boolf ∈ {x | Set(x)}2{f:U→{0,1}} ∃! boolf⁻¹)(boolf⁻¹(p) ≡ {x | p(x)})

def) setize ≡ boolf⁻¹

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

Laftf 1.1 (이거)를 쓰는 튜링 머신에서 작동하는 명제 p는

산술, 논리, 비트연산에 대한 명제일 수 있고, setize(p)는 집합이고, 결국에 집합은 S = {a₁, …, aₙ} 일시 x = a₁ ∨ … ∨ x = aₙ  일 수도 있어 모든 집합 S는 boolf(S)로 p로 환원가능함으로, 집합은 여기서 말한 전체 집합의 모임의 집합에 한정해서 다룰수 있다.

사실상 명제 =(= 방정식)임으로 말 다헀음, 그냥 ■ㄱㄴ

여기까지가 LAFTF 1.1이었다

ㄱㅅ

instagram @leenuxmathno7e

[github.com/FarAway6834](https://www.google.com/url?q=http://github.com/FarAway6834&sa=D&source=editors&ust=1737545183319986&usg=AOvVaw0udQDDfIxTu4hUrjAnk67S)

/c0dk1ddy

* * *

\[번외\] ANF (산술 정규 형식), Zhegalkin 수식, 그리고 그를 응용한 비트연산을 모듈러-2 환이 아닌, 진리값 배정에 따른 연산자를 함수로 해서 그 함수만 연산으로 사용한 모듈러-2 환으로써, 내부적으로는 모듈러-2로 정리되지 않치만 추상화해서 컴퓨터에서 사용하기에는 LAFTF가 더할나위없이 좋은것 같다.

유튜브에서 무슨 티타늄합금이 스스로 수학문제를 생각해서 푼다는 헛소린지 군침이 싹도는 진짜 소식일지 모르지만 거기에 쓰였으면 좋겠다.

\-\-
```

## 싹다 대체할 용도 : [Alkali](https://faraway6834.github.io/unbeauty/privateNote/Alkali/alkali)
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
⊢ InaccessibleCardinalExistanceAxiom : ∃κ cf(κ) = κ ∧ κ > ℵ₀ ∀λ<κ, 2^λ < κ [cf(x) := least δ ∈ Ord s.t. ∃f : δ → x, (∀i < δ)(f(i) < x) ∧ (∀α < x)(∃i < δ)(α < f(i))]

이때 κ가 Alkalraum의 구성에 쓰인다.

Alkalraum은 Grothendieck 우주가 존재하는 ZFC를 구성하는 확장된 크기의 Alkalic-LinearAlgebra내의 SetTheorem이다.

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

# 그러면

「Alkali Mathmatics with easy explanation by SIOT, CMD, FAN and LAFTF1.1」의 난이도는 쉽다 본다

내가 Alkalic이 쉽다 생각하는 이유는 단순하지.

Alkalic을 방정식 ■나 잘하는 사람이 와서 푼다 가정하자. 정수론 올림피아드정도 나간 학생한태, 태입이 뭔지 설교한 후에 가르치면, 논리를 대수로 바꿔줘서 고맙다 할껄?

근데 사실은 정수론 올림피아드 나간 사람들 특징은 방정식이나 함수를 ■나 쉽게 풀어낸다는거야, 그말은 즉슨, 우리는 단순히 추상적인 연산과정인 함수 f, g, h에 대해, f(x) = g(x)나 h(x) = const. 꼴의 방정식 문제를 내는것으로 연산의 계산에 대한 서술 (두 계산이 같거나, 어떤 계산이 상수화됨)으로 방정식을 표현할수 있고, 이는 방정식이 본질적으로 함수(연산)에 대한 서술임를 나타냄, 그래서 이 FAN의 빈칸인 인자를, 단순히 연산해주는걸 가르쳐 주는거라서, 초등학생한태도 잘 설명할수 있는 중학고 수준으로 설명할수 있다는거지.

끝, 쉽지.

-----

---

-----

**목표**

 - 「Alkalic Geogebra Sciance and Formal Explation of IT」이라는 책을 언젠가는 만들어서, 수학, 과학, 형식과학, 자연과학, 사화과학까지 다 Alkalic으로 서술 후 수학을 다시 formal하게 텍스트로 풀어낼것임. 
 - 크기개념같은 오만한 자기가 설명될거라고 믿는 합리화를 깨부수고, 그 개념이 더 humble하게, "나는 이렇게 생각합니다"로 말하게 하는것

**최종 목표**

 - 언어 사상을 언어 재능이 결핍된 이들이나 속뜻 해석 능력이 결핍된 이들도 이해할수 있게 한다.
 - 재능을 당연시하는 기존 방식보다는 기본적 사고 재능이 떨어지는 인간이 배울수 있는 방식을 쓴다
 - 근거없는 멸시; 무재능자에 대한 멸시; 이•문과의 근거없는 비합리적 배타를 구축해 없엔다.
 
 Edit : This is filtered version; I didn't know that I use too many f-words s.t. like this oh...