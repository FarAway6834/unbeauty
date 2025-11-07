# LinearUnbeauty & Labare & Unbare & Edgar

음... 뭐랄까... [PyTry](https://github.com/Tax0787Reborn/PyTry)를 내가 만들었다면 모르겠는데, 우울증 걸린 중1 쯔음에 내가 Jython•Brython에서 레포 닫지 말라 개소리하면서 깽판치는 나라망신 한거랑, 자신이 프로그램 개발 잘한다고 착각하면서 이상한 테크닉만 존나 한거랑 (근데 이상한 테크닉만 필요했어서 문제 없었음. 만능이었던 이유는 걍 내 지능이 존나 빠사사리여서 Python탓만 하면서 속도느리다 이 ㅈㄹ 했거든)
ㄹㅇ 줘 패고싶네 잼민이 ㅅㄲ 심지어 프로그래밍 언어 배워서 환경 다 연결한다고 했는데 그런 개쓸모없는 작업을 왜 약속했냐고 ㅅㅂ 새끼가...

아무튼 PyTry쓰면 NodeJS든 Python이든 JS든 Bruthkn이든 PyScript이든 Python + Entry + JS 이런거 만들기 편해서, easytry(내가 엔트리를 할 시절부터 생각했던 (당연히 Entry확장으로 하겠지만) 쉬운블럭 만드는 프로젝트; 이름 씨1발 실화냐) 뭐시기 합체해서 남들에게 Edgar소개하는 코스로는 유용할것같음.

그래프 그리는게 에초에 중고등학교 수학에서 핵심이어거 RGOmath나 Geogebra • Desmos같은 툴이 숭상받는거라, 제귀까지 가능한 unbeauty로 그래프까지 할수 있을것 같기도 하고...

뭐니뭐니해도... 아니 그전에

내가 프로그래머가 안되서 다행이다. 지금의 나를 있게 만든 내가 강해지게 만들고, 형식언어를 껌으로 하게됭 계기였디만, 그 과정이, 결과가 필요없을정도로, 존나 흑역사넹...

뭐, ProjecyBeryllium을 만든다면 Unbeauty는 연동도 좋을거고 뭐... 그러니까 뭐... 음.....

그나저나 간과한 점은, 모듈화를 못하는 사람 중에서, 함수 개념을 모를정도로 등신이면 흐름을 파악 못하는 ㅅㄲ가 많다는거다
걍 조금 머리아프면서 기저핵 쓰면 되는게 그렇게 어려운지...

그런데 Edgar는 당연히 흐름은 이해할거라고 가정하고 가고있다.

고1때 기획했다지만 죽여버리고싶네...

무책임하게 코드싸는 ㅅㄲ는 진짜 ㅅㅂ....

저러다가 내가 가진 지식을 카톡 오픈쳇에 공유하려니 정리가 필요해서 수학을 파며 궁리하다가,

어떻게 하면 나보다 바보인 놈들에게 이해시킬까 고민하다가 씨발ㅋㅋㅋㅋ 수학에 빠지고 컴퓨터 관련 진로를 포기했다.

내가 뭐가 되서 하대받아도 좋으니, 수학에 발을 들이고 싶은 마음 뿐이다.

수능이나 잘보던가 등신...,;;

## [`Unbeauty/README.md`](https://faraway6834.github.io/unbeauty)

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

 > also as `conditional` too. (when function is in arguemnt, not return, make lazy)

(when mulitypling and when arguemnt value)

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

## [`Edgar.md`](https://faraway6834.github.io/unbeauty/privateNote/Edgar)

```markdown
# Unbeauty 튜토리얼용 Edgar FW Script

## Edgar 유도
A. 계산상 시간선 인덱싱법

단계적인 장면들이 나열된 시간선을, 수열로 표현하여, "장면의 때"를 정의역으로 하는 수열로 만들어
Unbeauty처럼, 수열로 계산하고, 생각하는것.

B. 시간선과 상태변화 도입법

시간선상 어떤 속성 t가 변한다면, "계산상 시간선 인덱싱법"으로 해석하여, 상태변화를 단순히 "계산상 시간선 인덱싱법"의 인덱싱 결괏값에 따른 당연한 결과로 받아들일수 있다.

C. Edgarr Graph

Edgarr : Edg(e)-arr (엣지 가중치가 array의 값)

Edgarr의 가중치는 Array의 값이다.
Edgarr Graph의 충분하게 많은 Node가 불변이라 하자.
Edgarr Graph는 항상 Array에 대해 결정된다.
"시간선과 상태변화 도입법"을 쓰면,
모든 Edgarr Graph는 Array와 그 상태변화로 구성되기 때문에,

무한하게  Edgarr Graph를 다루지 않으면,
Edgarr Graph를 Array에 대한 Edgarr Graph로가는 계산의 결과로서 얻는다고 볼수 있다.

D. Edgarr Graph Machine

그럼 명령을 노드로, 분기를 Array의 변화로 처리하는 튜링머신과 그 언어를 생각해보자.

그때 그 튜링머신을 Edgarr Graph Machine라고 한다.

따라서, 단순히 분기는 {0, 1}의 치역을 가지는 수열을 결정해주면, 분기문이라는 Star형 그래프를 설명할수 있으므로, 수열에서 계산 가능하고, 해석 가능하다.

E. 튜링완전한 Unbeauty기반 컴파일 언어 Edgar

Edgar는
Unbeauty코드들을 저장하는 노드의 그래프를 처리하는 FW이다.

 - 노드필드 (NUL포함 문자열) : CommaSeperatedValue로 노드들의 값을 나열하고 각 인덱스를 노드로 취급.
 - AdjGraphField : AdjMetrix(인접행렬 by 2D BitMap)이나 AdjList(인접 리스트 by 2 Line CSV)로 표기되는 Edgar로, 실은 가중치가 연결여부가 되서 그걸로 표기된다.

이 언어는 정말 당연하게 Unbeauty로 컴파일 가능하며, 심지어 매우 쉽다.

 - M type : 인접행렬 AdjGraphField
 - L type : 인접 리스트 AdjGraphField
 - ML type : M과 L둘다 존재.

라이브러리적 기능)
분기문은 최적화된 코어(core) 함수로 평가된다.
사실 이게 전부지만.

## Edgar을 만든 이유.

나는 Unbeauty같은 esolang에 익숙해서 그런 분기(수식으로 분기를 구현하는 행위)가 전혀 이상하지 않지만, 그런 분기를 싫어하는 사람들이 있어서, 걍 Edgar를 만들었다.

쉽게 하라고 만든거라서 코드를 그래프로 작성하고 그리게 만든것이다.

해당 그래프는 편집이 인간이나 기계가 용이하게 만들었으니 Edgiter외에도 에디터로 작성하여도 좋다.

## Edgi Lang & Edgiter & Edgiter Data Pack

Edgi Lang은 RPN과 PN을 수학적 표기법으로 인식해서 해석하는 기능을 더한 Edgar 전처리기고 (주석지원은 뺀게, 파일에서 안읽는 부분에 추가하는 짓거리를 써서.),

Edgiter는 Edgi Lang 에디터다.

조건을 설정할때 Assistant가 있는데,
Edgiter Data Pack을 읽어서 동적으로 분기하여 작동하는 유사 AI나, Edgiter Data Pack을 실시간 개조하여 작동시키는 API로 AI랑 합쳐서 작동시킬수 있다.
```

## [`LinearUnbeauty.md`](https://faraway6834.github.io/unbeauty/privateNote/Proof/LinearUnbeauty)

```markdown
# LinearUnbeauty 계획

선형대수를 지원하는 [Unbeauty](https://faraway6834.github.io/unbeauty)

... 가 끝임
```

갠적으론 PyPy나 Python으로 Cython + Numpy조합으로 선형대수를 지원시킬 생각임. 이게 이거 만들때 든 원조 생각인데 아무곳에도 노트개 되지 않은게 참.

## [`labare.md`](https://faraway6834.github.io/unbeauty/privateNote/Proof/labare)

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

## [`unbare`](https://faraway6834.github.io/unbeauty/privateNote/Proof/unbare)

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
