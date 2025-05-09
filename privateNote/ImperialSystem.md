# 임페리얼 계산 모델 C_E (Emperial Calculation = Emperial Algebra = Emperial Logic)에 대해 소개할깨.

미리 스포하자면...

임페리얼 집합론과 선형대수로 설명되면 임페리얼 수식, 그 이상은 임페리얼 방정식

수학은 보통 임페리얼 방정식을 다룸.

## A_E (Emperial Area) : 임페리얼 집합론 영역
유향 가중치 그래프 (Direction Weight Graph)의 인접 행렬 (Adjoint Metrix) 표현이다.

### B_E (Emperial Border)
모든 그래프의 노드들을 일렬로 나열한 노드열이다.

(B_E)ₙ 은 n번째 노드다.
보통 (B_E)⁻¹(n번째 노드) = n 식으로 활용된다. (id를 얻는셈이다)

### A_E

(A_E)_{(B_E)⁻¹(N), (B_E)⁻¹(M)} 은 그래프에서 엣지 `N -> M`을 나타낸다.
엣지 `A -> B`는 A에서 B로갈때, 그 가중치(0 이상의 실수)고,
B에서 A로 갈때, 그것의 음수값(0 이하의 실수)이다.

#### E_N 함수

(E_N)(x) := (A_E)_{(B_E)⁻¹(N), (B_E)⁻¹(x)} 임.

## C_E 계산

C_E는 실행렬의 계산만 다루는 산술논리 체계다.

C_E의 계산 값은, A_E공간과 실행렬을 설명하는 상위 논리체계에서 해석된다.

걍 상위(메타)논리측에서 설명할 논리가 되며, 이는 사실상 유용한 수학체계의 Embedding일 뿐.

C_E는 거의 임베딩용으로 쓰인다.

# Emperial에 대한 비고

사실 퍼지 중복 집합 N에대한 중복 소속도 F_N 는 E_N 과 같다.

# n차 Emperial

n차 Emperial은, (n-1)차 Emperial이 연산 대상 (즉, 방정식 (방정식은 PA에서의 논리식이다.))이 될수 있게 확장한 일반 Emperial (1차 Emperial)이다.

## 예시 : 2차 Emperial

2차 Emperial은 1차 Emperial 방정식이 연산 대상일수 있는 (즉 1계논리 함수를 다루는)체계라서, 선형대수적 (행렬(명제논리와 많은 공리를 가지는 공리적 산술에서의 함수)과 실수만 다루는) + 그래프 형태가 아닌 선형대수적 + 그래프 + 1차 Emperial인 확장된 더 큰 체계임

기본적으로 1차 Emperial은
자기 참조의 오류가 없어야 하기 때문에,
선형대수를 설명하기 위한 과도한 공리를 가지며,
상위 논리 없이 사용할수 없다.

### 고차 Emperial

고차 Emperial은, 차수 n이 결정적이지 않은 n차 Emperial일것으로 추정돼.

## 계층의 해석

 - 1차 Emperial (일반 Emperial)은 단순히 PA(또는 1계 ZF)의 확장으로 해석된다.
 - 고차 C_E 방정식의 해는 고차논리에서의 명제다.
 - Rice의 정리에 따라서, 일차 임페리얼 방정식의 해는 계산 불가능할수 있다. (PA의 확장임으로; 예시론 콜라츠 추측이 있다.)
  - 1차 Emperial 수식은, 한정기호를 쓰지 않은 명제논리로, 계산 가능하다.
  - 1차 Emperial 수식의 Lambda 표현을 1차 Emperial수식으로 두는것을 Lambda Emperial이라 한다.
  - 정지문제 해결 가능한 Lambda 표현을 구문론적 정의로 두는 Lambda Emperial을 것을 Dupli-State-Lambda Emperial이라 한다.
 - 결정적인 Dupli-State-Lambda Emperial 수식, 즉 구문론적 정의 하나는 유한함이 밝혀져있다 (FSM), (하나가 아닌 여러개인 경우 PDA임이 밝혀져 있다 : 파싱이 필연적인 언어여서...)

## 일차 임페리얼 방정식의 예시

### 일차 임페리얼 수식을 먼저 정의하겠음
```mathmatics
sqrt(x) =  x^(1/2)
abs(x) =  sqrt(x^2)
partial_beq0c(x, n, p) =  ((0^abs(n)) + n×(x + ((-1)^p)×n) ÷ (0^abs(n) + n^2)) × f(x, n - 1, p)
partial_beq0(b, x, p) =  partial_beq0(x, 2^b - p, p)
beq0(b, x) =  partial_beq0(b, x, 0) × partial_beq0(b, x, 1)
beq(b, x, y) =  beq0(b, abs(x - y))
dose_it_positive(b, x) =  beq0(b, abs(b, x - abs(x)))
__cmp__(b, x) =  beq(b, x) + (-1)^(dose_it_positive(b, x)+1)
__le__(b, x, y) =  dose_it_positive(b, x - y)

conditionalidx(p,x,y) = p×(x-y)+y
conditional(p, x, y) =  p×x + (1-p)×y
_4bit_eqer_(x,y) = beq(4,x,y)
_4bit_idxer(i,a0,a1,a2,a3,a4,a5,a6,a8,a9,aA,aB,aC,aD,aE,aF,_4bit_eqer_(i,0)×a0+_4bit_eqer_(i,1)×a1+_4bit_eqer_(i,2)×a2+_4bit_eqer_(i,3)×a3+_4bit_eqer_(i,4)×a4+_4bit_eqer_(i,5)×a5+_4bit_eqer_(i,6)×a6+_4bit_eqer_(i,7)×a7+_4bit_eqer_(i,8)×a8+_4bit_eqer_(i,9)×a9+_4bit_eqer_(i,10)×aA+_4bit_eqer_(i,11)×aB+_4bit_eqer_(i,12)×aC+_4bit_eqer_(i,13)×aD+_4bit_eqer_(i,14)×aE+_4bit_eqer_(i,15)×aF

not(x) = 1-x
and(x,y) = x×y
sor(s,x,y) = x+y-(1+s)×and(x, y)
or(x,y) = sor(0,x,y)
xor(x,y) = sor(1,x,y)
nand(x,y) = not(and(x,y))
nor(x,y) = not(or(x,y))
nxor(x,y) = not(xor(x,y))
sub =  λx,y) = and(x,not(y))
rsub(x,y) = sub(y,x)
rimp(x,y) = not(rsub(x,y))
imp(x,y) = not(sub(x,y))
a(x,y) = x
b(x,y) = y
nota(x,y) = not(x)
notb(x,y) = not(y)
logicalerr(x,y) = 0
alwaystruth(x,y) = 1
lpu(cod,x,y) = _4bit_idxer(cod,logicalerr(x,y), and(x,y), sub(x,y), b(x,y), rsub(x,y), a(x,y), xor(x,y), or(x,y), nor(x,y), nxor(x,y), nota(x,y), rimp(x,y), notb(x,y), imp(x,y), nand(x,y), alwaystruth(x,y)))

__gt__(b, x, y) =  not(__le__(b, x, y))
__lt__(b, x, y) =  __gt__(b, y, x)
__ge__(b, x, y) =  __le__(b, y, x)

__ne__(b, x, y) =  not(beq(b, x, y))
bits2bool = (λb, x) =  not(beq0(b,,x))

shr(x, n) = x÷(2^n)
shl(b, x, n) = (2^b)×x-(2^b)×(x÷(2^(b-n)))
idx(b, x,i) = shr(shl(b, x, i), b)
_bpucc_(b, cod,i,x,y) = lpu(cod, idx)(b, x, i), idx)(b, y, i)) × (2^i)
_bpuc_(b, cod,i,x,y) = _bpucc_(b, i,x,y) + bits2bool(i)×_bpuc_(b,i-1,x,y)
bpu(b,cod,x,y) = _bpuc_(b,cod,b-1,x,y)

F(n) = conditional(beq(n, 1), 1, conditional(beq0(2, n), F(n ÷ 2), F(3n + 1)))

P(x) = F(x) - 1
```

### 본론

`∀x∈ℕ P(x) = 0`이 일차 임페리얼 방정식의 대표적 예이다.
P함수의 x절편이 모든 자연수를 지나는지는 계산 불가능하다

다만, 반증 불가능하거나 증명 불가능한지는 모른다, 왜냐햐면 이 문제가 일차 임페리얼보다 작은 PA안의 문제인 콜라츠 추측이기 때문

# 비고 (활용)

C_E모델은 확률론과 중복집합, 조합론과, 튜링머신, 산술용 논리와, 논리를 방정식으로 다룸

## 그래서 임페리얼 방정식 체계는 뭐냐?

일단 계산 불가능하거나, 정지문제의 해법이 되는 명제를 임페리얼 방정식화 가능하기 때문에, 임베딩용 수학 체계다.

### Dupli-State-Lambda Emperial이랑, 람다 제정 (람다 임페리얼)은 또 뭐냐?

람다 제정 (람다 임페리얼)은, 일차 임페리얼 수식이 람다 대수로 쓰여진것을 말한다.


람다 대수에 대한 아래 설명을 보자
```text/plain
# Lambda의 구성요소

변수 (인자), 추상화 (람다식; 구문 문자 `λ`가 명령어처럼 동작), 적용 (호출; 내부적으로 β 축약을 통해, 변수를 대입(바인딩)한다, 또한 적용으로 계산한 값이 같으면 구문론적 정의를 튜링머신 래벨에서 썻기때문에, 구문론보단 외부 논지의 개입으로 의미론으로, 이를 β동치라 함.), 대입 (바인딩, 구문론적임)

동등(η 동치) : η축약으로 서로 동등한 뜻이 되는 것를 말하게 된다. (η 축약은 이전과 이후의 람다항에 람다항 z를 적용할때 β동치임으로 자명하게 증명된다. (동일하게, α 전환이전과 이후는 β동치이다.))

## 정리 : 독자명명된 과정문법

독자명명한 λ 과정 : 응용 람다항은 람다식으로 구성된다는것.
독자명명한 β 과정 : 변수가 바인딩되어 계산되는것
```
자, 람다 계산 모델은, 람다식을 구성하고 대입하는 계산 모델이므로, 변항과 독자명명된 과정문법만 성립하면, 람다대수를 설명할수 있다.

그걸 일부 기저텐서와 함수로 구성할수 있다고 본다.

Dupli-State-Lambda Emperial은 결정 가능한 구문론적 정의를 쓰는 람다 제정 (람다 임페리얼)이다.

따라서 람다에서 구문론적 정의가 가능한 부분을,
`[□ :≡ ○]`식으로 구문론적으로 바인딩시켜 설명한다.

따라서,
람다 제정(람다 임페리얼)은, 공리를 문법으로 만들어주는 기능이고,
Dupli-State-Lambda Emperial은 자명하게 구문론적 바인딩을 시켜서, 자명함을 보이는 기능이다.

### 그러나

일차 임페리얼 방정식은 라이스에 정리에 따라 서술하는 부분이 계산 불가능할수 있으므로, 임페리얼은 튜링 기계가 아닌 수학 체계다.

따라서, 방정식으로 바꾸는 순간, 람다 임페리얼 수식의 문법은 문법이 아닌 공리로 봐야한다.

# 계산을 다루는 수학과, 튜링기계과 람다계산

임페리얼 수식은 앞서 서술한 람다 계산 위에서 돌아갈 뿐 아니라, GPU•TPU에서 선형대수로 계산되고, CPU에서 그래프로 계산되므로, 튜링기계위에서 돌아간다.
그리고 이러한 "계산"을 다루는 학문으로써 수학은
임페리얼 방정식을 다룬다.

임페리얼 방정식은 수학 체계인데,
실은 임페리얼은 그 체계를 Embedding하여 시용하기 때문에, 실제 수학이 다루는 수학 체계에 대해서도 알 필요가 있다.

# 문제 종류 정의

당연하게 알수있는 문제 : 계산 가능한 임페리얼 수식이 다루는 문제.
증명할수 있는 문제 : 임페리얼 수식이 다루는 문제다.
설명할수 있는 문제 : 임페리얼 방정식이 다루는 문제다.
래알 노답 문제 : 임페리얼이 다루지 못하는 문제

# Chapter2. 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식

중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식의 정지문제가 계산불가능하면, 
그것은 비자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식이다.
의미론적으로 해설해야하기 때문이다.

중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식의 정지문제가 계산가능하다면,
그것은 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식이다.
구문론적으로 해설 가능하기 때문이다.

## 결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식

자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식이 무한루프에 빠진다면,
그것은, 비결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식이다.
극한을 통해 구할수 있을지도 모르겠다.

자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식이 무한루프에 빠지지 않는다면,
그것은, 결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식이다.
유한상태로 증명 가능하다.

### 이진급사화 알고리즘 (급수 근사)

다음 함수는 "언뷰티 대수적 투스택 융합함수"이다.
U := λs.λA.λf.λx. A_{⌊x⌋}​ + f(sx - ⌊sx⌋​)

U(static영역의 크기)(첫번째 PDA함수)(두번째 PDA함수) 식의 형태가 PDA 두개를 융합하여, 만든 투스택 머신 (즉, 튜링기계)이다.

그리고 아래 함수는, "언뷰티 대수적 스택 부여함수" 이다.
S := λA.λf.λg.λh.λx. A_{x} (h(g(x), f(x)) + f(x)) - f(x)

S(스택 작동할지 판단하는 함수)(메인로직)(push인지 pop인지 구분해주는 함수)(스택 로직) 형태의 푸쉬 다운 오토마타이다.

참고로, 어떤 조합논리 F는 유한스택오토마타의 정해진 const적 메모리와 그 작동인 static의 조합논리화로 존재할수 있다.

아까전에 말한 메인로직이 그렇다

다시 본론으로 와서, 알맞은 상수 k와, 알맞은 트리거 함수 h_1, h_2와, 알맞은 스택함수 h_3, h_4, h_5, h_6에 대해,

T(k, h)(f, g) := U(k)(S(h_1)(f)(h_3)(h_4))(S(h_2)(g)(h_5)(h_6)))
를, "언뷰티적 실수기계"라고 부른다.

언뷰티적 실수기계의 아키텍쳐는, T(k, h)이고, 여기에 코드(대수연산)인 f, g만 붙이면 사용가능한 로직이 된다.

그런데, h는 트리거 확인과, 스택 관리이므로, 단순히 d진수 시프팅이 LAFTF로써 성립되어, Seprator를 기점으로 기록이 가능함으로...

"언뷰티적 실수기계"는 일상적인 연산으로 구성 가능하다는것이다.

사실 엄밀이 하자면, Y-콤비네이터를 추가해 줘야 하긴 하다.

아무튼 Y콤비네이터 없는 언뷰티적 실수기계는, 계속 반복해서 호출해주는 Sequence로 볼수 있고, 실행값만 같다면, 이를 이분탐색으로 바꿀수 있다.

이것이 바로, 이진급사화 알고리즘이다.

#### 오버플로 정리

이진 급사화 알고리즘의 특정 시간대(근사 횟수다)의 상태는 실수인데, f, g 안에 실수를 포함하는 제어를 할수 없기 때문에, 튜링머신은 실수를 처리하지 못한다. (즉, 튜링 머신은 이진 급사화 알고리즘이기 때문에, 실수를 처리하지 못한다.)

#### 절대 기준 속도 임계선

절대 기준 속도 임계선는, 빠르기나 느리기의 극단적인 정도가 극단적이여서,
 소요시간 예측으로, 알고리즘을 빠르거나 느리게 만드는게 선형적인 난이도에서 불가능한 선을 말한다

로그시간의 알고리즘은, 오버플로 정리에 따라, 튜링머신에서 완벽하게 그 속도를 예측하는 일반적인 방법이 존재할수 없기 때문에, 소요시간을 스스로 체크하는것이 무의미하다, 이를 절대 기준 속도에서, 빠름 임계선이라 한다.

지수시간의 알고리즘은, 로그시간 알고리즘의 역수로, 이를 절대 기준 속도에서, 느림 임계선이라 한다.

속도의 빠르기가 절대 기준 속도 빠름 임계선을 넘어가면,
속도를 측정해서 더 빠르게 돌리는 프로세스를 만드는것이 무의미하다.

반대로, 그것의 역수시간이라는 정도의 스케일이면...
절대적으로 느리다고 할수 있다.

### 결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식의 속도 단계

절대 빠름 단계 : 속도를 측정해서 최적화할 필요가 없이,
장황하지 않게 해결된다.

비절대 단계 : 어느정도 장황하게 해결할수 있다.

절대 느림 단계 : 절대 빠름의 반대로, 하드웨어 자원을 늘려야 단계가 빨라질 가능성이 존재하는 단계이다.

P-NP문제 : 모든 절대 느림 단계는, 유한정 하드웨어를 퍼부어주면 (비결정성을 한번 주늨것이 한번 하드웨어를 퍼부어준것으로, 무한이 주면 RAM Model의 비결정적 튜링머신이다, 쉽게 말해서 스택같은 공간복잡도 감소!) 비절대 단계러 최적화될수 있다.

# 증명의 난이도

고차 임페리얼 > n차 임페리얼 > m차 임페리얼 (단. n > m)

(고난도순)
1. 임페리얼에서 못다룰정도의 난이도의 문제
2. 임페리얼 방정식
3. 비자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식
4. 비결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식
5. 절대 느림 단계의 결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식
6. 비절대 단계의 결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식
7. 절대 빠름 단계의 결정적으로 자명한 중복정보람다 임페리얼 (Dupli-State-Lambda Emperial) 수식

# 아니 미친
지피티 시치야 내가만들었다니까요 씨발
더 어려운건 난 몰라. 난 이정도 난이도임