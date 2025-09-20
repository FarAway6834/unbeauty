Step 1. 기본 도구 제작

술어 Φ와 함수 f를 다음과 같이 놓자.

Φ(x) : 2|x
f(n) = (1 + (-1)ⁿ)/2

나는 뭐 못난 학생이므로, 학교에서 배운 증명 말투로 비형식적으로 서술해보자.

첫번째로 (-1) = e^{iπ} 이므로
f(n) = (1 + e^{iπn})/2 이다.
두번째로 g(x) = eⁱˣ인 g는 g(x mod τ) = g(x)인 주기함수이므로, g(πx mod 2) = g(πx)이다.
따라서, f(n) = f(n mod 2)이고, 전해석이다.

Boolean Domain 𝔹 = {0, 1}로 놓고,
논리를 Zhegalkin Polynomial로 놓으면,

Φ(x) = {1_{Mod(Φ}}(x)가 된다.

두식 f(0) = 1, f(1) = 0을 가지고 f(n) = f(n mod 2)로 정수범위에서의 f의 값을 일반화하면,
f(x) : x mod 2 = 0
이므로, f(x) : x ≡ 0 (mod.2)
한마디로, f(x) : 2|x이다.

즉, 정수범위 하에서 f, Φ의 치역이 각각 {0, 1} (즉 𝔹) 및 𝔹이기에,
하나, Mod(f) = Mod(Φ) (𝔹반환 함수 (즉 술어) 혹은 술어의 진리집합 Mod에 대해서 정수범위에서 같음)
둘, graph 1_{Mod(Φ)} = graph f (따라서, 0을 뱉는 부분마저 graph f와 겹쳐서, 지시함수의 그래프를 그리며)
셋. 1_{Mod(Φ)} = f 이다. (마지막으로, 정의역과 치역이 같으므로, 정수범위에서 동일)

(참고로 나는 방금전에 "~이여야 한다"라고 말하지 않았다. 언제나 정수범위에서 1_{Φ} = f이다.)

참고로, 정수범위가 아니라면, Φ가 모든 정수에 대해 서술할때, Φ ⊨ Mod⁻¹(Mod(f))이고,
실수범위애서 Φ는 정수범위가 아닌 부분에 대하여 항위이기 때문에, 항상 정수일 조건이 붙어있는것과 비슷하게 동작한다.

Zhgalkin Polynimal에서 1 - x = ¬x (mod. 2)이고, 일반적으로도 1 - x (mod. 2) = 1 - x이기에,
1 - f(n)은 ¬Φ(n)이다.

1 - f(n) = 2/2 - (1 + e^{iπx})/2 = (1 - e^{iπx})/2에서, 1 - f(n)가 n이 홀수인지 확인하는 전해석함수이다.

𝔹 = {0, 1}로 Truthy • Falsy Value를 정하면,

배중률 p ∨ ¬p에서,

```cpp
# psudo code lang = cpp

auto f(bool p, auto x, auto y) {
    if (p) {
        return x;
    } else {
        return y;
    }
};
```

역할을 하는 식은,

∀p ∈ 𝔹, f(p, x, y) = {p}x + {¬p}y = \begin{cases} x, & p, \\ y & ¬p \end{cases}

이가 된다.

왜냐하면, f(1, x, y) = x 이면이 f(0, x, y) = y이기 때문에, 그렇다.

사실 위 psudo code를 더 단축해서

```cpp
# psudo code lang = cpp

auto f(bool p, auto x, auto y) {
    return p?x:y,
};
```

인 f가 f(p, x, y) = px + (1 - p)y인것이기도 하다.

따라서, 이때 p ∈ 𝔹인 p가 Boolean Algebra와 동형이고, 이에따라 f(p, x, y) = px + (1 - p)y가 조각적 정의문 역할을 수행하므로, f는 조각적 정의문에다가, 동형사상을 통해, p ∈ {0, 1}을 𝔹 = {F, T}인 Boolean Domain으로 바꿔서 조각적 정의인 식을 수행하는 함수를 이용하는 함수로 동작하고, 실제로 그련 함수를 온전히 대수학에서 사용 가능하게 p에 대해 Boolean Domain으로 바꾸는 동형사상을 달아준 함수이기도 하다.

참고로, "에초에" 해당 동형사상은 다음과 같은 단순한 과거 어떤 프로그래머 지망생이 고용한 구성가능한 증명을 위한 함수 내지는 술어일 뿐이다.

bool(x) : x = 1
bool(x) : x ≠ 0
int(x) = \begin{cases} 1, & x, \\ 0, & ¬x \end{cases}

인 bool및 int
즉, 수식으로 하는 프로그래밍에서 bool및 int인것 뿐이다.

걍 단순한 초심자의 타입 케스팅 연산자다.

그러므로, f(p, x, y) = px + (1 - p)y = p(x - y) + y = \begin{cases} x, & p, \\ y & ¬p \end{cases} 이다.

지금까지의 말을 종합하면 다음을 얻는다.

isEven(x) : 2|x

홀수는 짝수가 아닌 정수이므로,

Fact) isEven(x) : x ≡ 0 (mod. 2)

에서 ℤ/2ℤ = {0, 1}에서, 짝수는 0이고, 짝수가 아닌 정수는 1일것이므로, 

isOdd(x) : x ≡ 1 (mod. 2)

TernaryOperator(p, x, y) = px + (1 - p)y = p(x - y) + y = \begin{cases} x, & p, \\ y & ¬p \end{cases}

이다. 그리고 앞서 말할 내용에 따라서, 

checkIsOdd(x) = int(isOdd(x))

checkIsEven(x) = int(isEven(x))

인 checkIsEven, checkIsOdd에 대해서,

checkIsEven(x) = (1 + e^{iπx})/2

checkIsOdd(x) = (1 - e^{iπx})/2

이다.

에초에 ℤ/2ℤ = {0, 1}에서, 짝수와 홀수를 단 하나의 기호 0, 1로 배정해서 생각 가능하도록 나눠지므로

⊨ ¬checkIsEven = checkIsOdd이고,

⊨ ¬checkIsOdd = checkIsEven이며,

이중부정을 통해서 checkIsEven, checkIsOdd를 만들때, 필연적으로 먼저 구성될 필요 있는 함수는 없다. 즉, 구성에 있어서 A와 B가 서로가 서로를 구성하는 동일한 모양의 구성, 즉, 모든 {C, D} = {A, B}을 만족하는 C, D에 대해, C가 D를 구성하는 방법이 단 하나의 방법으로 C가 A, B인 두 경우 다 서술되는 경우가 되므로, 서로 쌍으로 구성하는 관계에 놓여있다.

분명 수학은 이런것도 이름을 붙이고 추상화할텐데...

Step 2. 우박수열 제작

Hₙ = \begin{cases} 3n + 1, & isOdd(n), \\, n/2, & isEven(n) \end{cases}

에서, ~~even하게도~~

Hₙ

 = TernaryOperator(checkIsEven(n), n/2, 3n + 1)

 = checkIsEven(n)(½n - (3n + 1)) + (3n + 1)

(3 = 6 ÷ 2이므로, 3 = 6 × ½)

 = checkIsEven(n)(½n - 6(½n) - 1) + 3n + 1

(교환법칙을 이용해서)

 = 3n + 1 + checkIsEven(n)(-5(½n) -1)

(분배법칙으로 인수분해하여)

 = 3n + 1 - checkIsEven(n)((5/2)n + 1)

(대입하고)

 = 3n + 1 - ((1 + e^{iπx})/2)((5/2)n + 1)

((1 + e^{iπx})/2 = ½ + ½e^{iπx}에서)

 = 3n + 1 -(½ + ½e^{iπx})((5/2)n + 1)

(전개하고)

 = 3n + 1 - (5n/4) - ½ - (5n/4)e^{iπx} - ½e^{iπx}

(현재 유일하게 동차수인 동류항을 가진 상수항과 일차항에 대해, 잔~~업~~계산~~노가다~~하기 위해 계수를 손봐주고)

 = (12n/4) + 2(½) - (5n/4) - ½ - (5n/4)e^{iπx} - ½e^{iπx}

(아직도 유일하게 동차수인 동류항을 가진 상수항과 일차항에 대해, 잔 계산~~을 빙자한 노가다~~ 해줘서)

 = (7n/4) + ½ - (5n/4)e^{iπx} - ½e^{iπx}

 = - ½e^{iπx} - (5n/4)e^{iπx} + (7n/4) + ½

다른 방법으로는,

Hₙ

 = TernaryOperator(checkIsOdd(n), n/2, 3n + 1)

 = checkIsOdd(n) (3n + 1 - ½n) + ½n

(나는 멍청이가 아니니, 이전에 수행항 3 - ½을 가져와서)

 = checkIsOdd(n) ((5n/2) + 1) + ½n

(이번에는 분리된 형태로 대입해서)


 = (½ - ½e^{iπx})((5n/2) + 1) + ½n

(전개하고)

= (5n/4) + ½ - (5n/4)e^{iπx} - ½e^{iπx} + ½n

(동류항인 일차항과 합해주면)

 = - (5n/4)e^{iπx} - ½e^{iπx} + (7n/4) + ½

결과는 동일하다.

혹시 모르니 다항식 계산 잘하는 기계한태 채찍질로 시켰던 식이랑 비교하면

엥?

n(1 + e^{iπx}) + 2(1 - e^{iπx})(3n + 1)/4 면...

n(1 + e^{iπx}) + 2(1 - e^{iπx})(3n + 1)/4

(어느정도 전개하고)

= (n + ne^{iπx} + 2(3n + 1 - 3ne^{iπx} - e^{iπx}))/4

(전개를 마치기 위해 분배해서)

 = (n + ne^{iπx} + 6n + 2 - 6ne^{iπx} - 2e^{iπx})/4

(동일하게 잔계산하고)

 = (7n + 2 - 5ne^{iπx} - 2e^{iπx})/4

(으헤.. 어카지.. 헤ㅔ... 아! 위 형태랑 일치하려면 ¼을 분배해야하네?)

 = (7n/4) + ½ - (5n/4)e^{iπx} - ½e^{iπx}

야호 대성공!

개다가 이번 식의 특성상 완전히 두가지 경우에 대해서, 다 불리언 분기용 인수를 다 고려한 식으로,

n(1 + e^{iπx}) + 2(1 - e^{iπx})(3n + 1)/4

(두 인수항에 ¼을 분배해서)

 = (n/2)((1 + e^{iπx})/2) + (2(1 - e^{iπx})/4)(3n + 1)

(잔계산하여)

 = (n/2)((1 + e^{iπx})/2) + ((1 - e^{iπx})/2)(3n + 1)

이런데, 솔찍히 이렇게

(a/2)(b/2) + c(d/2) = (ab + 2cd)/4 꼴로 계산되는 이유는, 굳이 검산할 가치도 못느끼겠기 때문에 넘기고 싶지만 구하자면,

l/k + m/n = (n l + k m)/kn 이라는 초등학교 수준의 공식에 대입하면

a/2 × b/2 = ab/2² = ab/4 에서,

ab/4 + cd/2 = (2ab + 4cd)/8 = (ab + 2cd)/4

이고, 그 근거는, ㄱ : ㄴ = ㄷ : ㄹ에서 외항과 내항의 곱으로 검산했을때 잘 나온다는점, 그리고 ㄱ ∓ ㄴ = ㄷ ∓ ㄹ에서, ㄱ ± ㄹ = ㄷ ± ㄴ에서도 잘 계산된다는점이 그 검산으로써의 근거다.

만약 f(x) = x mod 2 = x - 2⌊x/2⌋에서 홀수판단 f를 만들었다면, Fuzzy Logic으로 자연스럽게 확장되니 최고였겠지만 그건 g(x) = (x - e^{iπx})/2인 f에서, f(cos(x)) = re(g(x))인 관계인지라, 나는 굳이 전해석을 깨고 복잡히 만들바에는 좀 부자연스러워도 전해석을 택했다. 사실은 (cis(x) ± cis(-x))/(2 + i^{(1 ∓ 1)/2} 가 전해석인건 알고 있지만, 걍 머리가 아파서 회피하는거다. 에초에 h(x) = e^(ln(iτx/T) + ln(iτx/T))에서, T = 2면, 그걸로도 구할수 있다.

너무 머리 아프다.

그리고 확장된 Hailstone이 전해석인거는 희망을 그리 많이 가져오지 못한다.

T(n) = Hₙ = (7n/4) + ½ - (5n/4)e^{iπx} - ½e^{iπx}에서,

BaseCondition(x) = int(x = 0)인 BaseCondition은

BaseCondition(x) = lim_{ε → 0} e^{-|x|/ε}이다.

BaseCondition(0) = e⁻⁰ = 1이지만,
x ≠ 0에서, BaseCondition(x) = lim_{n → ∞} e⁻ⁿ = 0이다.

그렇다! 어떤 0 혹은 무한에 대해서 1과 0을 뱉는 함수는 fn(n) = e⁻ⁿ인 fn인것이다! (참고로 디렉델타는 이번 용도에서 쓸수가 없대서 버렸다)

이하에서, 
Collatz(x) = (1 - BaseCondition(x - 1)) Collatz(T(x))
인 Collatz가 바로 Collatz추측을 풀 방정식용 함수다.

Φ(x) : Collatz(x) = 0에 대해서,

∀x ∈ ℕ, Φ(x)가 참이면 콜라츠 추측은 참이다.

Collatz(x) = (1 - BaseCondition(x - 1)) Collatz(T(x)) = lim_{ε → ∞} (1 - e^{-|x - 1|/ε})Collatz(T(x)) = lim_{ε → ∞} (1 - e^{-|x - 1|/ε})Collatz((7n/4) + ½ - (5n/4)e^{iπx} - ½e^{iπx})인 Collatz가 이 추측에서의 답이다.

저런 정신나간 제귀함수를 어케 만들것인가?

ReversedT(y) = \begin{cases} ∅, & x = 1, \\ {ReversedT(x) | y = T(x)}, & x ≠ 1 \end{cases}
인 체계 ReversedT에 대해,

x ∈ y → T(x) = y이다.

즉, 이 체계에서 `∈`가 하는 역할은 y = 1일때를 제외한 T와의 함수관계 여부

문제점이 하나 있다면 저 체계가 성립하려면 Collatz추측은 참이여야한다는거다.

사실 그래도 ZFC상 안되는걸로 안다.

그래서 저런 집합 비스므리한걸 집합이 아닌데 집합처럼 행동하는 객체라고 가정하자.

뭐 이래도 오류날것같지만

x ∈ T(x)이기 때문에,

Collatz(x) = (1 - BaseCondition(x - 1))Collatz(T(x))에서, 

ReqCollatz(x) = Collatz(x + 1)
에서,

어짜피 Collatz(8) = 0 = Collatz(1)이여야 하므로,

CollatzCore(x) = (1 - BaseCondition(x))x

에서, 다음수 연산 s대신에 T⁻¹를 통하여서 CollatzCore(x)를 구성하고,

Collatz(1) = 0
Collatz(T⁻¹(x)) = CollatzCore(Collatz(x))
이고,

ReqCollatz(T⁻¹(x) - 1) = CollatzCore(ReqCollatz(x - 1))
에서, 

ReqCollatz(T⁻¹(x - 1 + 1) - 1) = CollatzCore(ReqCollatz(x - 1))
이므로,

ReqCollatz(T⁻¹(y + 1) - 1) = CollatzCore(ReqCollatz(y))

ß(y) = T⁻¹(y + 1) - 1인 ß가 supressor역을 맏을수만있다면, 이렇게 다룰수만 있다면 참 좋을텐데

뭐. 나같은 바보같은 학생이 해낼리가 없다.