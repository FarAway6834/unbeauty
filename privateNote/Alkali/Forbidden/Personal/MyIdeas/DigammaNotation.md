# DigammaNotation 정의

ϝ를 구문론적으로 정의하는 노테이션이다.
보통을 L을 ZFC로 놓는다. 왜냐? 이건 함수를 표기하기 위한 용도이기에, 수학에서 많이 쓰일수밖에 없다. 수학을 L로 놓기 때문이다. 물론, 왜 하필 그 많은 공리계중 ZFC냐면, ZFC가 가장 많이 쓰이는 수학 공리계니까 그런거다.

## 서론

서술에 앞서 미리 요약하자면

dom (ϝx : X. y : Y) = X
codom (ϝx : X. y : Y) = Y
ran (ϝx : X. y : Y) = {y | x ∈ dom (ϝx : X. y : Y)}
graph (ϝx : X. y : Y) = {(x, y) | x ∈ dom (ϝx : X. y : Y)}
(ϝx : X. y : Y)(x) = y

인 기호 ϝ로 함수를 표기하는거다.

## 본론

TRS랑 자유 모노이드를 미리 정의한 후 DigammaNotation을 정의하겠다.

### 튜플 제귀 분할 모델 TRS(S)

들어가기 앞서, 
벡터에 대해서는 1도 생각 않고 기획했다는점을 기억하자, 벡터에 주어지는 dim은 결코 튜플의 길이가 될수 없다. 외냐면 모든 튜플은 최대길이가 L인 경우, 길이 1~L이나 L로 길이를 해석해도 무리가 없기 때문에, 하나로 정해졌다 하기 애매하다.

왜냐? 제귀적 정의에 따라서, n-tuple은 (n-1)-tuple의 일종이기 때문이다.

이제부턴 본론으로 들어간다.

TRS(S) ≜ <S*, ε, I, first, last, LengthEq>

I : S* ↦ S*
I(x) = x
first : S* ↦ S*
first|_{(S×S+)×(S×S+)}(x, y) = x
first|_{S¹}(x) = x
first|_{S⁰}() = ε
last : S* ↦ S*
last|_{(S×S+)×(S×S+)}(x, y) = y
last|_{S¹}(x) = ε
last|_{S⁰}() = ε

$LengthEqCore(p, f, x, y) : \begin{cases} f(x) = ε ↔ f(y) = ε, &(p), \ LengthEqCore(¬p, f, x, y) ∨ LengthEq(p, last◦f, x, y), &(¬p) \end{cases}$
LengthEq(x, y) : LengthEqCore(T, I, x, y)

LengthEq가 재대로 작동하는지는 근데 페아노 공리계에서 증명가능함.

에초에 LengthEq(x, y) ↔ ∃n ∈ ℕ₀, lastⁿ(x) = ε ↔ lastⁿ(y)임. ㅋㅋㅋ

### 자유모노이드 F(X)

F(X) ≜ <X*, ε, juxtaposition>

k는 튜플이 아닌 constant로, 아무거나 ㄱㄴ. k = {{∅}, {{∅}}}로 놓으면 이해하기 쉬워짐.

juxtaposition : X* × X* ↦ X*
$x juxtaposition y = \begin{cases} x, &(y = ε), \ y, &(x = ε), \ (x, y), &(LengthEq(x, last(k, k))), \ first(x) juxtaposition last(x) juxtaposition y, &(¬LengthEq(x, last(k, k))) \end{cases} $

### 디감마 표기법 DigammaNotation

parentheses ≜ {'(', ')', ','}

DigammaNotationStartSymbol ≜ 'ϝ'
DigammaNotationNonVarname ≜ parentheses ∪ DigammaNotationNonterminal
DigammaNotationNonterminal ≜ {'ϝ', ':', '.'}
DigammaNotationTerminal(L) ≜ L ∪ parentheses
CompileTargetOfDigammaNotationLang ≜ DigammaNotationTerminal
DigammaNotationLang(L) ≜ DigammaNotationTerminal(L) ∪ DigammaNotationNonterminal
DigammaNotationLformation(L) ≜ F(DigammaNotationLang(L))

아래 함수 DigammaNotationLFormat(L) / DigammaNotationRFormat(L)는 자유모노이드 DigammaNotationLformation(L)위에서 조합논리로써 조합된 함수다.
DigammaNotationLFormat(L) : (DigammaNotationLang(L)*)⁴↦DigammaNotationLang(L)*
DigammaNotationLFormat(L)(x, X, y, Y) ≜ "ϝ" juxtaposition x juxtaposition ":" juxtaposition X juxtaposition "." juxtaposition y juxtaposition ":" juxtaposition Y
DigammaNotationRFormat(L)(L) : (DigammaNotationLang(L)*)⁴↦DigammaNotationLang(L)*
DigammaNotationRFormat(L)(x, X, y, Y) ≜ "(" juxtaposition X juxtaposition "," juxtaposition Y juxtaposition "," juxtaposition "{(" juxtaposition x juxtaposition "," juxtaposition y juxtaposition ") | " juxtaposition x juxtaposition "∈" juxtaposition X juxtaposition "})"
모노이드 DigammaNotationLformation(L)에 대한건 여기까지다.

DigammaNotationFormationRule(L) ≜ {(DigammaNotationLFormat(L)(x, X, y, Y), DigammaNotationRFormat(L)(x, X, y, Y)) | X, x ∈ (DigammaNotationLang(L) ∖ DigammaNotationNonVarname)* ∧ Y, y ∈ DigammaNotationLang(L)*}
DigammaNotationFormalGrammer(L) ≜ (DigammaNotationNonterminal, DigammaNotationTerminal(L), DigammaNotationFormationRule(L), DigammaNotationStartSymbol)

이를통해 DigammaNotationFormalGrammer(L)가 변형행성문법임을 알수 있다.

Formation Rule이 사실상 PCRE(PCRE에 없는 문자집합 DigammaNotationLang(L), DigammaNotationNonVarname를 쓴건 양해해주길)코드 s/ϝ(?<x> [[DigammaNotationLang(L)]--[DigammaNotationNonVarname]]*?)[\s\t]*:[\s\t]*(?<X> [[DigammaNotationLang(L)]--[DigammaNotationNonVarname]]*?)[\s\t]*\.[\s\t]*(?<y>[DigammaNotationLang(L)]*?)[\s\t]*:[\s\t]*[[DigammaNotationLang(L)]--[DigammaNotationNonVarname]]*?/\($X, $Y, \{\($x, $y\) \| $x∈$X\}\)/나 다름없다. (이걸 python fstring같이 작성하자면, 변수(일수있는)기호(즉, (DigammaNotationLang(L) ∖ DigammaNotationNonVarname)*) X, x와 DigammaNotationLang(L)가 charset인 L-formula Y, y에 대하여, f"ϝ{x}:{X}.{y}:{Y}"가 감지되면 f"({X}, {Y}, {{({x}, {y}) | {x}∈{X}}})"로 치환하는거다.)

TMI : 촘스키 위계상 정규언어라고도 부른다.

변형생성문법이론에서 Lang이란 charset이다. DigammaNotation의 Lang는 DigammaNotationLang(L)이고, 그 Lang는 컴파일 타깃인 CompileTargetOfDigammaNotationLang(L)로 컴파일된다.

즉, DigammaNotation는 사실상의 메크로, 그러니까 표기법(Notation)이다. 구문론적으로 ϝ를 정의한것이다.

사실... 구문론적 등호를 =ₛ라 하면, 

임의의 모델론적언어 L에 대한 L-formula x, X, y, Y에 대하여,

ϝx : X. y : Y =ₛ (X, Y, {(x, y) | x∈X)})

라고 한줄요약 가능하다.

ㅅㅂ...

또한, f = (X, Y, {(x, y) | x∈X)})라 하면, {(x, y) | x∈X)} ⊆ X × ran f를 만족하므로,

다음 두 조건
1. ran f ⊆ Y를 만족할것.
2. {(x, y) | x∈X)}가 오른쪽 유일인 관계일것

을 만족하는 튜플 (X, Y, {(x, y) | x∈X)})은 ZFC에서 함수를 정의하는 표준 모델상 함수일 공리를 만족시킨다.

그렇다. 함수 간단하게 적겠답시고 이 ㅈㄹ 한거다.