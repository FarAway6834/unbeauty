# unbeauty
````
# LAFTF1.1 공식문서 스크랩
```markdown
ol{margin:0;padding:0}table td,table th{padding:0}.c0{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c11{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:26pt;font-family:"Arial";font-style:normal}.c3{padding-top:0pt;padding-bottom:3pt;line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.c6{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:center}.c1{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c5{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:right}.c12{text-decoration-skip-ink:none;-webkit-text-decoration-skip:none;color:#1155cc;text-decoration:underline}.c10{background-color:#ffffff;max-width:451.4pt;padding:72pt 72pt 72pt 72pt}.c4{margin-left:36pt;text-indent:36pt}.c7{color:inherit;text-decoration:inherit}.c2{height:11pt}.c8{margin-left:36pt}.c9{color:#202122}.title{padding-top:0pt;color:#000000;font-size:26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-size:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}

LAFTF 1.1Logic-Algebra Formular TransForm 1.1

def)

    ⎧ To : {x|Set(x))} × {x|Set(x))} → {z|z={f:x → y | p(x, y)}}

p: ⎪

    ⎨

    ⎩ To : x, y ↦ {f | f : x → y}

def 표기) A To B ≡ To(A, B)

def 표기) A To B ≡ A 2 B

—------------------------------------------------------------------------------------------------------------------------

def) (∃! int ∈ Bool2{0, 1} ∃! int⁻¹ )( int⁻¹(x) ≡ (x = 1) ≡ (x ≠ 0))

def) bool ≡ int⁻¹

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

(bool · f)(x, y) :≡ bool(x) ∧ bool(y)

        (x̄, f(x̄)) = (x̄, ×(x̄)) (단. <×, Yᵢₙₜ>)

        ∵        ⎧ f(0, x) = 0 = 0 × x

⎪ f(1, x) = x = 1 × x

⎨

⎩  \[x, y\]ₕ = 1 = \[x, y\]ₓ (h=f, 기호의 한계…)

        ∵ f(n, x) = f(x, n) (단. n ∈ Yᵢₙₜ)

∴ f(x, y) = xy

단순히 같다는 의미이고…,

수학에 생각이란게 유효하다면 이건 자명한게 아닐까 조심히 추측해본다.

—------------------------------------------------------------------------------------------------------------------------

(bool · f)(x) :≡ ￢ bool(x)

        f(0) = 1, f(1) = 0

        ∴ f(x) = (0-1)/(1-0) x + 1 = 1 - x 로, 그래프 위애서 점을 찍을떄, 우리가 보고자 하는 점의 위치를 f(0)에서 f(1)로 수를 바꿔보면, 감소하는 수는 1을 얻으니 당연하다.

(아니 생략이 ㄹㅇ ㄹㅈㄷ, 어짜피 요약본이긴 한데 띠겁네)

* * *

그러면 Conjuntive Normal Form에 따라

⎧ b = ∑ Aₙ2ⁿ⁻¹ (n=1~4, 단. x̄ = (        (0, 0) ∧ f(x̄) = (A₁, A₂, A₃, A₄))

⎪                                        (0, 1)

⎪                                         (1, 0),

⎨                                         (1, 1))

⎩  Hexf(b) = f 인 Hexf(b)는 xy와 1-x로 조합 가능하다

이때, x ⊕ y = (x ∨ y) ∧ (￢ (x ∧ y)) = (x ∧ ￢ y) ∨ (y ∧ ￢ x) 인데,

        int(x ⊕ y) = int(x ∨ y) - int(x ∧ y)

        ∵        f₁(x, y) = xy

                f₂(x, y) = x + y - xy

                f₃(x, y) = int(bool(x) ⊕ bool(y))

                Hexf⁻¹(f₃) = Hexf⁻¹(f₂) - Hexf⁻¹(f₁)

        또한,

        int(x ⊕ y) = int(x ∧ ￢ y) + int(￢ x ∧ y) - int(￢ x ∧ y) int(x ∧ ￢ y)

        int(￢ x ∧ y) int(x ∧ ￢ y) = int((￢ x ∧ y) ∧ (x ∧ ￢ y)) = int(⊥) = 0

—------------------------------------------------------------------------------------------------------------------------

대충 프랑스에서 아이디어 떠올려서 영적인 힘을 줘서 고맙다는 뻘소리가 적힐 칸이었는데…

씨발이런또라이같은인생아지랄난개가타서존나못참아죽겠네미친어떻게씨발내가개고생해서얻은LAFTF1.0이씨발이미있냐위키백과에서xor기호얻으려고씨발들어가봤더니나중에찾는건다른곳에서했고씨벌아진짜개같이영문위키백과에씨벌아니거기를먼저들어갔더니얻은기호가아니진짜개얼탱이가없어가지고하아 제칼킨 식이라고 ㅈㄴ좋은 이론이 선행으로 있었는데 이거 모르고 위에 내용 씨발 혼자 하나하나 유도한 내가 병신이지 병신이야 존나 인생 절반 손해봤네 ㅋㅋㅋ 미친 뭐 앞으로 서술할 비트연산도 마찬가지겠지 뭐 하 시발 인생.

shlᵦ(x) = shlᵦ(2ᴮ⁻¹ + x) (β = B (Bits) 동일하게, 기호의 한계, 참고로 겹쳐가시고 씨벌 한번 더 a서 β로 수정함. 아이고야 ㅠㅠ)

(shlᵦ)ₗₘ (Λ ≡ lm, 동일한 한계로 이런식으로 표기하겠음, ⁽\*⁾)

(shlᵦ)ₐ (아랫첨자 a가 없는 관계로… 씨벌 ⁽\*⁾)

* * *

원래는 (=필기 원문대로 쓰면은) “그런대 아름다운 사실,” 이라고 써야하는데 ㅈ같네 기분이 아직도 ㅋㅋ 이런 씨발 아름다운 새상

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

또한, 동일하게 그래프나 함수 버전, 방금전 버전 유도도 있지만, 단순하게도, shl = ⌊x/2⌋ 다. x ÷ 2  = y … r, x ≡ y (mod. 2)고, ⌊x/2⌋ = (x-r)/2 다.  (아 아래로 …화되는거 ㅈㄴ 띄껍내 개씨발 (딥빡))

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

참고 : f(x) = x - ⌊x⌋ 는 톱늬파의 일종으로, actan(tan(x/π))도 톱늬파의 일종으로, 가우스 함수는 ㄹㅇ로 그냥 ㅈㄴ 초딩도 이해가능한 ㅈㄴ 자명한 산술연산이라고 ㅋㅋㅋ

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

def) (∃! boolf ∈ {x | Set(x)}2{f:U→{0,1}} ∃! boolf⁻¹)(boolf⁻¹(p) ≡ {x | p(x)})

def) setize ≡ boolf⁻¹

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

Laftf 1.1 (이거)를 쓰는 튜링 머신에서 작동하는 명제 p는

산술, 논리, 비트연산에 대한 명제일 수 있고, setize(p)는 집합이고, 결국에 집합은 S = {a₁, …, aₙ} 일시 x = a₁ ∨ … ∨ x = aₙ  일 수도 있어 모든 집합 S는 boolf(S)로 p로 환원가능함으로, 집합은 여기서 말한 전체 집합의 모임의 집합에 한정해서 다룰수 있다.

사실상 명제 =(= 방정식)임으로 말 다헀음, 그냥 ㅆㄱㄴ

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

# Unbeauty 공식문서
```
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
sqrt = cacher[1](λx. x**0.5)
abs = cacher[1](λx. this.sqrt(x**2))
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
_bpucc_ = cacher[1](λb, cod,i,x,y.this.lpu(cod, this.idx)(b, x, i), this.idx)(b, y, i)) * (2^i))
_bpuc_ = cacher[1](λb, cod,i,x,y.this._bpucc_(b, i,x,y) + this.bits2bool(i)×this._bpuc_(b,i-1,x,y))
bpu = cacher[1](λb,cod,x,y.this._bpuc_(b,cod,b-1,x,y))
```

ex2.ubt - extend not base cls, ex1 cls.
```
:noptlib
fibo = cacher[1](λb, x.this.conditional(this.beq0(b, x), 0, this.conditionalidx(this.beq(b, x, 1), 1, this.fibo(b, x - 1) + this.fibo(b, x - 2))))
```

## [coding plan 24.02.24 ~ ...](./plan)

### lazy evil optimizing

`[○×]this.__NAME__(□)` -> `([○×]this.__NAME__)(□)`
```

## [coding plan 24.02.24 ~ ...](./plan) 내용
```
it sucks

<runtime>

[typ]
 - subcls typic
 - duck typic
     - *.operator+ : this auto& morphism
     - *.operator- : this auto& morphism
     - *.operator* : this auto& morphism
     - *.operator/ : this auto& morphism
     - *.operator^ : this auto& morphism
     - additional : ==,!=,>,<,>=,=<,&,|,^,&&,||

data must placed before the function or fixing __optlib_handle__ using alias to fix optlib bit type give using

[cls]
 - subcls<upper self>
     - [super super                    final] *.operator[] : operator() with cache
     - [super using introduce almost virtual] T::##__TMP__ : template var
     - [super super                    final] *.operator() : template user
     - [protected super virtual 2      final] *.cache()    : user implements
     - by mecro (sucks)
         - PROMISSERN is mecro, not defed
           template <__supert__<T> this>
           struct __MANGELED_NAME__ : idxof<T, subclstyps, __typechekced_super__> {
               template <__VA_ARGS__, promiss<T> V = PROMISSER(__SRC__)>
               using __TMP__ = V; //well it's real name
           }
           inline auto __NAME__(void) { return __MANGELED_NAME__<T>(); } // `a×this.__NAME__(~)` ≡ `(a × this.__NAME__)(~)`
 - corcls<typ T, subclstyp<T>... subclstyps>
     - by mecro
     - cls attr by mecro `THISOBJTER <- _self__getattr__` => `THISOBJTER(ob, attr) ob::attr<ob>()`
 - entrypoints
     - `::` to `_s_`
     - inline function.
     - by mecro
 
<compile>

`<f> = cacher[<num>](λ<argv>.<src>)` as parse argv and set `T` or consexpr const
also it can use `main = ~` to set `operator()`

-----

base struct (default super cls)
`:filename` to can extend
```

## optlib (noptlib를 단순히 C++로 포팅) 예시
```
 - template <T b, T::__optlib_handle__<b>> type

 - beq0 : SUBCLS(x==0)?(T::__optlib_handle__<1>(1)):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x)
 - beq : SUBCLS(x==y?(T::__optlib_handle__<b>(1)):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x, T::__optlib_handle__<b> y)
 - dose_it_positive : SUBCLS(x>=0?(T::__optlib_handle__<b>(1)):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x)
```

## 참고 : TRO계획 있음.
````

# 설명글
````markdown
# 이론적 서술
```markdown
# 서론

𝔹 = {T, F}인 불 연산과 동등한 체계의 예시로, Zhegalkin Polynomial 이 있다.

모듈라 2 환에서의 Zhegalkin Polynomial을
우리가 쓰는 GF(2)에서 유도하는 LAFTF를
알아보자.

먼저 형변환 술어 bool로 수를 bool로 바꿀수 있다.
bool : {0, 1} x -> (x = 1) (= (x ≠ 0))
사실은, int := bool⁻¹ 에서,
int(p) = 1 if p else 0으로, 조각적 정의가 가능하여,
두 방법으로 다 유도가 되지만 말이다.

이렇게 정의된 int와 bool로 논리연산을 대수연산으로 평가할수 있다.

---

# 본론

## 최소한의 NOT & AND 논리가 유도되는지 보자.
### 논리곱과 곱의 비교를 동해 int(bool(p) ∧ bool(q)) = pq임을 입증하자.

1. 영권과 일원에 대해, 멱원과 항등원이다.
2. 다르거나 같은 p, q에 대해, 교환법칙이 성립한다.
3. 따라서 그 그래프와 정의역이 동등함. (사실 계산식 4개만 쓰면 이게 바로나온다)

### int(¬bool(p)) = 1 - p임을 입증해보자.

-p는 0, -1을 뱉는다. 정의역에서 벗어난다.
p - 1 (이전수 연산)은 -1, 0을 뱉는다. 정의역에서 벗어난다.
1 - p가 된다.
#### 유도된 식을 증명해보자.
미분같은거 쓸필요 없이, 직선의 방정식에서 (0, 1)과 (1, 0)을 지나는 직선의 방정식은 y = 1 - x다.
Q.E.D.

## XOR과 OR

### 논리합
덧셈에 (0, 0) ~ (1, 1)까지 배정해주면, (0, 1, 1, 2)
곱셈에 (0, 0) ~ (1, 1)까지 배정해주면, (0, 0, 0, 1)
빼주면, 논리합인 (0, 1, 1, 1)이며,
이는 드모르간의 법칙으로 유도해도 맞다.

### 베타적 논리합

논리합과 같은방법으로 x + y - 2xy가 배타적 논리합임을 알수 있다.

그러나, 베타적 논리합은 Zhegalkin 다항식(Polynomial)에서는, 이를 구현할 방법이 없어, ⊕를 가진다.

x ↔ y = x → y ∧ y → x의 부정으로써
x ⊕ y = (x ∧ ¬y) ∨ (¬x ∧ y)
 = (x - y) ∨ (y - x)
 = (x ∨ y) - (x ∧ y) (단. x - y := ¬ (x → y) = x ∧ ¬ y)

인데 (지금 본인이 이차식이 싫기때문에 이차식으로 전개해야하는 (x ∨ y) - (x ∧ y)는 전개하지 않겠음, 선형적인게 최고인 법이지 << 퍽퍽)

x(1 - y) + y(1 - x) + xy(1-x)(1-y)에서,
x(1 - y) + y(1 - x) = x - xy + y - xy이고,
xy(1 - x)(1 - y)에서나오는 p(1 - p)가 만족불가능이기 때문에, xy(1 - x)(1 - y) = 0이다.

## 비트연산

솔찍히 말하자면 나는 이 연산에 대해 아직 잘 모르겠다.
d진수 n 비트 비트 연산은, 모듈라 dⁿ을 확장한것으로 생각해도 될것같다. n = 1인 특수한 경우를 논리연산으로 보고, 여러개인 경우를 비트연산으로 보는것이다 (백터화 연산)

하지만 Σ f(x[n], y[n]) 2ⁿ (n = 1 ~ maxbit)에서 f가 덧셈을 보존해주지 않을거기 때문에,

보수연산 (혹은 정통 laftf명칭으로 bitwise nagator) (2ⁿ - 1) - x을 제외한 다른 연산은 나는 할엄두를 내지 못하였었다.

### 비트를 인덱싱하는 비트인덱서 (비트 인덱싱 함수)

idx(n', x, n) = shl(bit)ⁿ • shrⁿ'(x)
와 같이 정의된다.

### shift right function

shr(x) = (x - (x mod2))/2 = ⌊x/2⌋
와 같이 심플하고 귀엽게 식이 나온다.

### bitwise functions

(bitwise • f)(bit, x1, ..., xn) := Σ f(idx(bit, x1, n), ..., idx(bit, xn, n)) 2ⁿ (n = 0 ~ bit)

이렇게 예쁘게 식이 나온다.

### 지시함수를 유도해보도록 해보자.

서로 역함수인
Set(p) = {x | p(x)}, Boolf(S)(x) = (x ∈ S)
을 Set과 Bool사이의 변환으로 보자고 하자.
이전에 말했었던거 말이다.

intf := (int •) •Boolf와 setized := Set • (bool •)를 만들어봤을때, 집합은 대수 함수로 재밌게 바꿔볼수 있다.

이잔에 말했었던 조건부 정의 (조각적 정의)를 논리곱을 여러개 쓴 연립식으로 둔 정의에서,

intf(S)(x) = 1 if x ∈ S else 0 이다.
이는 지시함수랑 동등하다.

### 조건문 함수

dose(p, x) := (1 • Set • bool(p))(x) (단. 1은 지시함수)에서,

dose(p, x) := x if p else 0가 된다.

단순히 python수준의 단순한 코딩보다도 쉬우니 넘어가고,

유사 구간 역미분이라는 전에 언급한 체계에서 다뤗듯,

cond(p, x, y)를 p가 1일때와 p가 0일때에 대해, 조각적으로 정의될떼 이것이, 지시함수로 표현가능함으로,

cond(p, x, y) = dose(p, x) + dose(1 - p, y) = px + (1 - p)y = p(x - y) + y

예쁘게 완성된다.

---

# 결론

LAFTF는 제귀를 나타낼수 없어, 튜링완전하지 않다.

LAFTF는 반드시 유한시간내에 결정된다.

수열식으로써 정의할때 제귀를 이용할수 있다.

LAFTF와 수열의 제귀적 정의를 이용하여, 수열로 튜링머신을 만들수 있다.

여기서 모든 수를 선형대수적으로 치환하면 어떨까...

아름다울것같다.

사실 전혀 모르겠다.

슬프게도, 수식만으론 프로그래밍 가능하진 않고, 단순히 패턴으로 이해할수 있는 Sequence 함수, 수열을 어색하게 붙여야했다.
```

# 교육용 서술 (초딩 수준)
```markdown
# 주의.

지금부터 다루려는 논리는 이분법적 논리학이다.
이분법적 논리학은 극단적인 논리학이다.
"추상적으로 어떤 정보를 서술하는 문장"으로 싸잡아 표현되는걸 죄다 참과 거짓으로 구분가능하다고 보는 정신나간 논리학이다.
내가 좋아하는 수학이 이래서 비인간적인것같다.
뭐, 사설이지만, 단순히 나도 정신나가서 수학을 사랑하니 문제없다.

넘어가자!

---

"추상적으로 어떤 정보를 서술하는 문장"에는 수학에서 쓰이는 부등식이나 등호 (문제에서 등호에는 옳고 그름이 있다), 그리고 수학적 대상에 대한 원리적 서술 등등이 있다. (그런 원리적 서술의 예시로는, "곱하기는 반복 뺄셈이다"같은것이 있다, "곱하기는 반복 뺄셈이다"는 거짓이다. "반복 덧셈"이면 몰라도.)

아니 수학이 왜 나오냐고?
에초에 컴퓨터는 개임같은 정상적인 짓거리가 아닌,
수학을 가능한 한 전부 서술하려는 정신나간 짓거리에서 출발한거다.
그리고 이 글은 논리연산을 이해시키려고 있는거기 때문이다.
그러니까 이어서 본론으로 가겠다.

# 컴퓨터에서 참과 거짓.

컴퓨터에서 참과 거짓은 1과 0으로 나타낸다.
1과 0은 1비트에서도 구현할수 있으므로,
컴퓨터에서 참과 거짓은 1비트로도 구현할수 있다.

그리고 참과 거짓은 정보다.
컴퓨터에서 정보는 어떻게든 값이 있어야 생긴다.
근원적이지 않더라도 말이다.

그래서 참과 거짓은 학문적인 수학에서,
그러니까 이론적인 수학에서 특별한 값으로 취급한다.

단순히 "참과 거짓"으로 명명하겠다.

그리고 더이상 이런 정신나갈정도로 어려운
이야기를 때우기위해 대학수학지식을 비틀어서,
겁나쉬운 방법으로 이해해보자.

# 겁나쉬운 방법

어떤 "추상적으로 어떤 정보를 서술하는 문장"을 0개 이상 준비하고, 그걸가지고 다른 "추상적으로 어떤 정보를 서술하는 문장"을 서술할수 있어야 한다.
그런걸 연산으로 취급한걸 논리 연산이라고 부른다.

그런데 그런 연산은 이해하기가 정신나갈것같이 힘들기때문에, 실질적으로, 걍 논리 연산은 어짜피 식이기 때문에, 어떤 짓거리를 하는지 알면 된다.

에초에 우리는 논리적 오류가 생길수 있는 증명따윈 집어치우고, 걍 단순히 지식만 스틸해가려고 이 글을 읽고있지 않는가?

연산대상, 즉, 피연산자 역할이 0개 이상의  "추상적으로 어떤 정보를 서술하는 문장"이고, 그걸로 서술된게 연산값인데, 
모든 피연산자로 논리연산한것의 갯수는 (경우의 수가 2를 피연산자 수만큼 곱한건데 왜냐하면 피연산자 수만큼 한 비트를 나열한건데, 그러면 피연산자 수만틈의 비트의 이진수로 붙일수 있는데, 그 수들을 나열하면 그갯수가 되는데, 왜냐면 1부터 어떤수까지 새는건데, 0부터 최댓값까지 이진수나열은각 수에 1을 더해줘도 갯수는 안건드린건데 최댓값 + 1은 이진수에서 1한개만 쓰니까, 근데 그건 고등학교과정이니까 무시하고) 피연산자가 구구단마냥 갯수가 정해져 있어서 다 외울수 있을만큼 갯수가 무한이 아니기 때문에, 알수 있다.

단순히 피연산자을 쉼표로 나열하고 화살표를 그리고, 그 이후에 연산값을 넣으면, 정말 놀랍게도 정통수학의 논리연산 서술과 같다...... 근데 사실 모든 경우를 다 그릴꺼면 정신나갈정도로 힘들기때문에, 괄호안에 그걸 넣고, 화살표도 쉼표로 치환하면 된다.

사실 그것도 힘들긴 한데 다른표기법이 어려우니까 참아라.

# 논리연산

논리가 숫자 0과 1이라서 놀랍게도 수식으로 나온다.

"~가 아님" 연산은 단순히 영어로 변역해서, "not ~"고,
((0, 1), (1, 0))이며, "1 - 피연산자A" 다.

"~가 참이고 그리고 ~도 참임" 연산은 단순히 영어로 번역해서, "both ~ and ~ is true"고 줄임말은 "~ AND ~"고,
((0, 0), (0, 1), (1, 0), (1, 1))이며, "피연산자A × 피연산자B"다.

사실 논리연산이 다 이걸로 만들수 있다.

## not과 AND로 대충 퉁친 논리연산들과 그 뜻
작성중...

# 기획 : 시프팅이랑 비트인덱싱이랑 비트연산이랑 선택구조까진 나갈꺼임.
```
````

# 집적 이 글을 쓰고 이론을 만들고, 언어까지 다 설계한 지적재산권 주인 : 나
참고 : 국어엔 문외한이고 멍청이라 글은 잘 못쓰는놈임