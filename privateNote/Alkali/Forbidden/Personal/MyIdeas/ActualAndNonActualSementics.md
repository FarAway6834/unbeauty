# 속뜻•겉뜻 의미론

## 1. DFM++ EXPRESSION과 의외성 정리

이 장에서는, 겉뜻에 대한 형식화와, 실제 언어 사용에 있어서, 속뜻의 정의를 다른다.

### DFM++ EXPRESSION

````
# DFM++ EXPRESSION : DFM Language과 감탄음 용어를 통한 품사의 표기

DFM Language : DFM의 모델론적 언어

## DFM Language과 감탄음 용어를 통한 품사의 표기

형식품사 (DFM++ EXPRESSION에서 발음가능하고 형식화된 품사) : 자연어나 술어논리 공리계의 언어 L에 대하여, DFM Language에서 표현되는 품사
비형식품사 (DFM++ EXPRESSION에서 발음가능하지만 즉흥적인 품사) : 감탄음 용어에 "la"를 이용해, 존재론적으로 언질되는 표상, 즉 감탄사 어절이라는 문자열. (그 외에도 라틴어의 호격이 진감탄의 성격을 가지는지는 잘 모르겠어서, 탐구해보고 싶다.)

DFM++ EXPRESSION에서는 형식품사와 비형식품사를 통해 겉뜻의미론을 분석한다.

그러나, 속뜻의미론은 

## 감탄음 가설

> 
> 감탄음 가설
> 
> "감탄사는 입밖으로 조음했는지와 무관히, 화용론적으로 진감탄사와 가감탄사로 나뉜다."
> 

용어)

감탄감 : 감탄사를 낼때 느끼는 감정
감탄동기 : 감탄사를 뱉은 동기

진감탄사 : 감탄음이 진감탄음인 감탄사
가감탄사 : 감탄음이 가감탄음인 감탄사

감탄음 : 감탄사의 음
진감탄음 : 감탄이 진감탄인 감탄음
가감탄음 : 감탄이 가감탄인 감탄음

감탄 : 감탄음을 내는 것 (= 감탄음을 내는 행위)
진감탄 : 감탄동기가 감탄감인 감탄
가감탄 : 감탄동기가 감탄감이 아닌 감탄

## DFM을 통한 품사의 표기

미리 알아둘 점 : DFM Language은 DFM의 모델론적 언어를 말한다.

1. 주사는 빈사 Φ에 대해, la Φ로 정의된다.
2. Hint-Operator연산 Hint로 서술언 혹은 한정사를 Functor의 Hint표기로 정의한다.
3. 언어 L에서 기능사 집합 S는 상 operator[S]이거나, 기능사 x에 대하여, 함자 (noncompile(ε) operator(x))나 함자 (operator(x) noncompile(ε))이다. (또한 전치사나 후치사는 regex token 경계 구분자 `\b` 기준으로 split된것이므로, `\b\s\b`나 `\b`가 접하는 방향에 존재한다.)
4. 언어 L(G)에 대하여, L(G)상의 자연어 술어라는 함수는 모델 compiled(L(G))위의 함수다.
5. 그러한 함수를 이용하여, 자연어 문자열을 Funcional하게 표기하면, 여러 자연어 품사를, 겉뜻 의미론 기준으로 명확하게 분해 가능하다.

### Decorating Function Model

임의의 Domain에 대해 Decorating Functions를 정의한 모델이다.

미리 알아둘 점)

 * first(x, y) = x
 * last(x, y) = y

로 튜플의 제귀적 정의를 이용하여 본 문단을 서술할 예정임.

NOTATION)
```
DecoratingSyntax ≡ x s.t. Φ(x)
```

Decorating Functions)
```
la Φ = DecoratingSyntax
x Hint Φ = DecoratingSyntax
```

Hint-Operator연산 Hint)
```
Hint란 `(`랑 술어를 겹치는 표기법이다.

임의의 술어 Φ,
임의의 이항관계 R ⊆ P × Q및
임의의 x ∈ P, y ∈ Q에 대하여

제 1 Notation)

x (Hint Φ) ≡ (Hint Φ)(x)

실제론 `(`랑 Hint의 `H`랑 겹쳐서 적는다.

제 2 Notation)

x (R y) ≡ x (Hint (R y))

실제론 `(`랑 `R`랑 겹쳐서 적는다.

제 3 Notation)

모델 M(S) = <S, I>에 대하여,

1. M(S)는 구조체이므로 2-튜플이다. (i.e. M(S) = (first(M(S), last(M(S)))
2. first(M(S)) = S고, last(M(S)) = I이다.
3. S는 모델 M(S)의 도메인, I는 모델 M(S)위의 항등관계(이항관계중 하나)로, I ⊆ S × S다.
4. 항등관계 I에 대해, ∀(x, y), x I y : x = y이다.
5. 그러니까, I = {(x, x) | x ∈ S}인거다.

그러므로, 등호에 대해서는, Hint-Operator를 다음과 같이 정의한다.

x (= y) ≡ x (last(M({x, y})) y)

실제론 `(`랑 `=`랑 겹쳐서 적는다.

Tip)

진리함자 (R y)가 술어(진리함수) Φ = (R y)라면, 함자 (Hint Φ)는 수식언 • 한정사처럼 작동한다.

그러므로, Hint-Operator는 다항관계에 대해서도 함자 (Hint Φ)를 만들수 있다.
```

TIP : 기호 `≡`는 Syntaxal Equal기호다.
TIP : Operator는 모델론적으로는, Function에 해당한다.

### L(G)에서 compiled(L(G))의 연산자로 가는 사상 operator의 정의

L(G)에서 compiled(L(G))의 연산자로 가는 사상 operator를 다음과 같이 정의한다.

operator(f)(x, y) ≜ compile(x concat noncompile(f) concat y)

#### 컴파일된 형식언어 a.k.a. compiled(L(G)) 의 정의.

자유 모노이드 F(L) = <L*, ε, concat>는 구조체 F(L)이다.

즉, 튜플이므로, 튜플의 제귀적 정의에 따라, F(L) = (L, (ε, concat)) s.t. L = first(F(L)), ε = first(last(F(L)), concat = last²(F(L)) 인거다.

다음으로 형식문법 G = <V, Σ, P, S>에 대해,

isFormalGrammer(G) : isFormalGrammer<V, Σ, P, S>

해설 : 형식문법 G가 4-튜플이므로, isFormalGrammer는 집합 3개(문자집합 2개, 문자열 이항관계 1개), 문자 1개들 담은 튜플이다.

즉, isFormalGrammer는 문자집합의 Rank가 n일때, n계논리에서 사항관계, (n+1)계논리에서 일항술어다.

isFormalGrammer<V, Σ, P, S> : S ∈ V, V ∩ Σ = ∅, P ⊆ (LangOf<V, Σ, P, S>*VLangOf<V, Σ, P, S>*) × (LangOf<V, Σ, P, S>*)

N.B. P ⊆ (LangOf<V, Σ, P, S>*VLangOf<V, Σ, P, S>*) × (LangOf<V, Σ, P, S>*)는 ∀(x, y) ∈ P, x ∈ LangOf<V, Σ, P, S>*VLangOf<V, Σ, P, S>*, y ∈ LangOf<V, Σ, P, S>*인거다.

해설 : 이는, 형식문법과 문법규칙의 정의를 적은것이다. 

형식문법과 문법의 정의로 파악해보자면
1. 비단말기호의 정의 non-terminate symbol이므로, 기호(=언어셋(char set))중 단말기호의 여집랍으로, LangOf<V ∪ Σ> - Σ다. (i.e. 서로소 집합인거다)
2. 시작 기호는 비단말기호다.
3. LangOf<V, Σ, P, S>는 언어의 문자(기표) 집합이다. (i.e. 언어셋(언어라는 집합)은 문자셋(문자 입합, char set)이다)

LangOf(G) = LangOf<V, Σ, P, S> = V ∪ Σ

해설 : 문자가 비단말기호인 문자이거나 단말기호인 문자라는건, "문자가 단말기호인 문자이거나, 아닌 문자다"라는 동어 반복이므로, 당연히 맞는 말이다.

실제로 있든 없든 바뀌든 문법규칙에 영향이 안가는 문자들은 Σ에 있다. 마치 치역이 아닌 공역처럼, 잉여스러운 문자들이다 (예를들어 이모티콘 같은것. 잉여스럽지만 정말 쓸모있다. 인간은 그런걸 많이 쓴다.)

f isCompilerOf G : dom f = LangOf(G)*, (∀x, y, z, (x =>* z, y =>* z) → f(x) = f(y))

해설 : ∀x, y, z ∈ LangOf(G)*, (x =>* z, y =>* z) → f(x) = f(y)이면 f를 컴파일러로 두는거다. 실제로는, 컴파일 결괏값이 언어 밖에 있을수도 있기에 codom은 명시되지 않았다. Func[{LangOf(G)*} × {S | S ⊆ U}]인... 놈이다. U는 전체집합으로, 공리계의 도메인이다. 공리계에서 다룰수 있는 원소에 따라 달라진다. 공리를 만족시키는 원소들의 집합이니...

same_as(f) ≜ Φ s.t. Φ(x, y) : f(x) = f(y) (i.e. Φ = {(x, y) | f(x) = f(y)}

해설 : 함숫값-동치 (제2역상에 따른 동치인), (함숫값-동치류 (제2역상에 따른 동치인 동치류)의 동치관계.)

G.same_as ≜ same_as(G.compiler)

G.compiler(x) ≜ {y | G.same_as(x, y)}

해설 : 이건 G.same_as와 G.compiler의 정의다. 위의 정의을 만족하는 G.same_as와 G.compiler가 유일함은 증명 가능하고 쉽게 보일수 있다.

L(G) ≜ <first(F(LangOf(G))), first(last(F(LangOf(G)))), last²(F(LangOf(G))), G.same_as>

해설 : G가 만드는 언어의 집합 L(G)이다. 자유 모노이드 모델에 동치관계 G.same_as를 추가했을 뿐이다.

해설 : G.same_as는 언어상 같은 뜻 (같은 해석)인 텍스트(언어 내 택스트, 문자열임)을 말한다.

noncompiled(x) ≜ {x}

해설 : 이건 해설이 따로 필요 없다 {x} = {v | v = x}니까.

compiled(L(G)) ≜ <G.compiler[first(L(G))] ∪ noncompiled(first(L(G))), noncompiled(first(last(L(G)))), (noncompiled◦first(last²(L(G)))◦<noncompiled⁻¹, noncompiled⁻¹>), compile, same_as(compile)> s.t. {compile|}_{noncompiled(first(L(G)))} = G.compiler ◦ noncompiled⁻¹, {compile|}_{G.compiler[first(L(G))]}(x) = x (단. <noncompiled⁻¹, noncompiled⁻¹>는 벡터장)

해설 : 컴파일된 compiled(L(G))의 모델. noncompiled(first(L(G)))는 컴파일되지 않은 버전이고 G.compiler[first(L(G))]는 컴파일된 버전이다. (겹치면, 그건 그 문자열이 컴파일 전후에 변하지 않은것이므로, 교집합의 존재가 무모순성에 영향을 미치지 않는다는것은 당연하고 쉽게 보일수 있다.)

추가 해설 : 
1. noncompiled(first(last(L(G))))에서 first(last(L(G)))가 자유 모노이드의 것을 그냥 가저온것이므로, noncompiled(first(last(L(G)))) = {ε}다.
2. (noncompiled◦first(last²(L(G)))◦<noncompiled⁻¹, noncompiled⁻¹>)(x, y) = noncompiled(first(last²(L(G)))(noncompiled⁻¹(x), noncompiled⁻¹(y)))이므로, noncompiled가 동형사상이고, 자유 모노이드나 L(G)의 concat이라는 모노이드 연산을 noncompiled(first(L(G)))와 noncompiled◦first(last²(L(G)))◦<noncompiled⁻¹, noncompiled⁻¹>가 이루는 모노이드로 연산을 가져온것이라는점을 알수 있다.
3. {compile|}_{noncompiled(first(L(G)))} = G.compiler ◦ noncompiled⁻¹, {compile|}_{G.compiler[first(L(G))]}(x) = x인 이유는, G.compiler[first(L(G))]가 정의역인 경우, 이미 컴파일 결과기에, 아닌 경우만 추가적으로 컴파일할 뿐이다.

마치며 : 상수기호 EMPTY는 EMPTY ≜ noncompiled(first(last(L(G))))로 모델 compiled(L(G))의 모델론적 언어의 상수기호다.

TIP : G.compiler는 G의 compiler라는 함수 method. 표기법이다. 단지 객체지향틱한 표기법일 뿐.
TIP : G.same_as는 G의 same_as라는 술어 method. 표기법이다. 단지 객체지향틱한 표기법일 뿐.
TIP : `=>*`는 Dragon Book에 나오는 표기법이다.
TIP : 상수기호 ε = "" = ()는 공문자열, 즉 공튜플이라고 불리는 기호다.
TIP : 미지수 L은 주로 언어셋(char set)을 표기할때 쓰이는 미지수다.
TIP : 별표 `*`는 클래이니 스타다.
TIP : 의미론적 등호를 통한 정의 기호 `≜` 를 사용한다. `≜`의 의미는 의미론적 등호를 통한 정의 기호다.

### 극단적 형식적 굴절 관점

주의 : 극단적 형식적 굴절 관점은 작성자가 포합어•교착어•굴절어를 구분하는걸 회의하는 작성자 본인의 뇌피셜이고 개똥철학이다. 음모론이라 불러도 될정도의 과학적 근거 없이, 형식적으로 같으니까, 현실에도 차이가 없을거라는 귀추법이다 (현실에 차이가 있어도 형식적으로 같을수 있다. 그럼에도 형식적으로 차이가 없으니까 묶는건 솔찍히 성급한 일반화가 맞다.)

극단적 형식적 굴절 관점 : 접두/접미사형 조사/접사를 이용한 교착/포합 굴절규칙도 굴절규칙이며, 토큰어 관점과 교착/포합 굴절 관점을 포함한, 굴절에 대한 극단적인 형식적 관점.
교착/포합 굴절 관점 : 교착(조사)/포합(문법접사)은 형식문법으로 표현시 굴절이나 다름없다는 고도의 형식주의적 관점. 교착이나 포합을 교착/포합 굴절이라고 부른다.
토큰어 관점 : tokenization이 프로그래밍 의미론상 굳이 어절과 regex `\b`를 도입하는 불필요한 문자 `\b`기준 split이라는 관점. 토큰어를 tokenization을 하는 언어로 간주.
(교착 / 포합 굴절) / 굴절 규칙 : 교착/포합 굴절과 굴절을 품사의 의미적•문법적 상태를 문법규칙으로 변화시키는 (교착 / 포합 굴절) / 굴절규칙으로 형식적으로 정리된다는 교착/포합 굴절 관점 사상에 따른 형식문법으로의 교착/포합/굴절의 표현
접두/접미사형 조사/접사 : 어근(어원)의 머리(시작)/꼬리(끝)에 접하는(붙는) 조사/접사

## 술어논리에서 자연어 문장 / 자연어 술어

자연어 문장의 경우 `Φ : "자연어 문자열"`인 문장 Φ이고
자연어 술어의 경우 `Φ(...) : "자연어 문자열"`인 함수 Φ이다.

1. 자연어 술어는 operator 사상을 통해서 정의되는 함수다. (자연어에서 자연어로 가는 함수다")
2. 자연어 명제는 "Φ est Verum"이 긍정되는 대상이거나 "Φ est Falsum"이 긍정되는 대상일시 Φ이다.
3. 긍정되는 대상은 형식언어에서의 긍정자 ♤에 대해, {x | ♤x}가 아닌 일반적인 언어에서의 긍정자 ♠︎데 대한 {x | ♠︎x}를 이르는 말이다.
4. 
5. 참의 비필연성 (단어로써의 참) : 형식언어에서의 {x | ♤x}는 "참은 분명하다"는 주장을 하고싶어하는데, 실제로 이론전산학적으로 컴퓨터가 정의되야, 분명한것이 현실의 실체로써 정의되어, Operation Semmentic에 따라 정의되고, 이론전산은 결국 형식언어가 이미 정의되어있어야 긍정 가능하므로 순환 논증이다. 다시말해, 형식언어와 일반적인 언어에서의 "긍정되는 명제"는 "언어의 자의성"에 따라 "hoc est verum"이라고 긍정되는 것들과, 사실 (혹은 객관적인 진실) 사이에는 아무런 필연적 관계가 없다.

### 화용론적 일반 가설

```
제 1 가설 : 보편적(일반적)으로 참인것은 일반적(보편적)으로 "긍정되는 것"(대부분의 사람이 말하는 {x | ♠︎x}로써, 대부분이 긍정하는 자연어적 명제)이다.
제 2 가설 : 사회적 공감대 • 불문율상 "긍정되는 것"이 존재하여 일반적(보편적)으로 긍정된다.
제 3 가설 : 보편적인 문법과 단어의 의미란, 최대 대수에게 긍정되었고, 사용된 문법과 의미을 의미한다.
```

가설인 이유 : 아직 내가 과학적 실험과 통계 자료로 구체적 수치로 증명하지 않았음.

#### 보편의 페러다임 시프트 가설

```
화용론적 일반 가설이 맞다면, 

A. 화자에 의해 일반적으로 긍정되는것
B. 화자에 의해 사회적 공감대 • 불문율상 "긍정되는 것
C. 화자에 의해 긍정되었고, 사용된 문법과 의미

가

언어 화자가 긍정하는 (A, B, C)의 모집단 X에 대해,

통시적인 X의 변화에 따라, 보편이 변화한다.

이를 보편의 페러다임 시프트라 한다.

보편의 페러다임 시프트 가설 : 보편의 페러다임 시프트는 존재한다 (다시 말해, 아까전에 말한 보편의 페러다임 시프트라는 현상은 실재로 있는 현상이다)
```

### 형식논리언어와 논리의 괴리 (2026년, 여기에 반박이 하나 생겼다. 2025년에 쓴 글이다)

읽어보기 전에

 + 이 글에서는 형식적인 사고는 기호의 조작일뿐이지, 논리는 logical cohereance에서 온다고 보았다.
 + 뇌과학적으로 logical cohereance를 관장하는 DLPFC없이 기저핵•측두엽•후두엽을 이용해 DLPFC없이 형식적으로 사고하는 나에게서 형식논리언어와 논리의 괴리를 찾아서 적어보았다.


표준국어대사전에 이렇게 나와있다.
```
논리 (論理) 「명사」 「1」 말이나 글에서 사고나 추리 따위를 이치에 맞게 이끌어 가는 과정이나 원리.
```

그뿐이다.

<br>

...

<br>

이제 글을 시작해 보겠다.

<br>

<br>

...

<br>

<br>

<br>

<br>

『형식논리언어는 그 언어적 사고를 하는데 있어, logical cohereance에 의존하지 않으니, logical cohereance에서 파생됬다고 보기 어렵다.』

형식논리상에서 긍정자 ♤와 일반적인 언어에서의 긍정자 ♠︎를 가정하자.

♤x : x ↔ T
♠︎x : (대충 x를 긍정하는 뜻)

나는 형식논리언어로 논리구문을 처리하기 때문에, 축소주의적 진리론을 당연하다고 착각하고 살았다.

자, 단순무식하게 새가지 펙트를 짚고 가자.

♤(x = y)

이때 x를 y로 해석해도 됨은 당연하다.

♠︎("미친놈아 참 잘하는짓이다" = "미친놈이 한 행위는 잘한 행위이다")

이것은 바보같은 해석이다. 형식문법리 아닌 속뜻과 맥락을 통한 해석이 있어야 한다.

여기서 먼저, 형식언어는 속뜻 = 겉뜻인 특성이 있어서, 그 의미론을 속뜻으로 파악하는 순간, 공리계 혹은 이론 T가 M ⊨ T인 M들에 의해 기계적으로 변환되는 대수적 사고방식으로 돌아간다는걸 알수있다.

Q1 : ♤(A가 B를 죽였다 → A는 마땅히 징역 5년을 구형받아야 한다.)가 맞나?

Q2 : ♠︎(A가 B를 죽였다 → A는 마땅히 징역 5년을 구형받아야 한다.)가 맞나?

두가지 문장 Q1, Q2는 다르다. 전자는 참일지 모르지만 후자는 맥락상 참이다. 그 이유는 전자는 가능새계에 구애받는데, 저것이 성립하는 가능세계인 「보편•사회문화맥락적 진리론」은 기본적으로 언어를 통한 사고에 깔려있기 때문이다.

우리는 여기서 형식언어가 「보편•사회문화맥락적 진리론」에 무관하다는 사실도 알 수 있다.

Q1 : ♤(A or B라면 마땅히 포함적이다)가 맞나?

Q2 : ♠︎(A or B라면 마땅히 포함적이다)가 맞나?

두가지 문장 Q1, Q2는 진리값이 다르다. Q1은 참이고 Q2는 반례를 "평생치킨 안먹기 또는 평생김치 안먹기 둘중 하나를 해야 살려주겠다"에서 "아니 두게다 안하게 해버릴수 있는 선택치를 주겠다고요? 이 나쁜놈아!"라고 할수 없는것같은 맥락에서, "또는"이 반례로 작용한다. Q2는 거짓이다.

참고로, Q1, Q2로 예시를 든 문장들은 「보편•사회문화맥락적 진리론」새계와 논리 구문 설명 예시에서, 각각 대한민국 형법과 양자택일의 상황 강요라는 부적절한 예시가 있었지만, 증명이 아닌 설명문이기에 굳이 수정할 이유가 없어보이니 넘어가자.

일단 마지막 예시를 보면 형식언어를 자연어로 번역하여 해석했을때, 형식언어로 사고했는지와 자연어로 사고했는지가 다르다.

콰인의 번역 불가능성 원리를 아는가?

> 
> "형식언어는 형식적으로 규정되는거지, 그 의미론은 형식적인 긍정자 ♤를 제외한 자연어로 규정되지 아니한다."
> 

이 문장은 번역 불가능성 정리에 의해 당연하다.

> 
> "언어 L에서 문장 Φ의 진리값은 L위에서 L의 단어로 평가된다."
> 

그렇다. 형식언어에서는 진리가 정의가 불가능하기에 절대적인 요소 ♤를 통하여 진리를 부여 가능하다.
그리고 ♤의 서술에는 ♤가 쓰인다. 즉, 올바른 설명이 아니다.

공리계인것이다.

공리계는 해당 공리계 내에서 설명 불가능하다. 어떤 설명문으로 설명하든지간에 그 근거가 될 수 없기 때문이다. 그것은 어떤 이유에서 참이지 않고 이유없이 참이기 때문리다.

따라서,

> 
> "진리 이외에 것들중에 공리계와 정의를 이론 T라고 하자. 이론 T가 형식적이면 진리는 형식적이지 않고 진리가 형식적이면 이론 T가 형식적이지 않다."
> 
> "이론 T가 형식적이지 아니하면, 그것은 형식언어가 아니다"
> 
> "따라서 이론 T는 형식적이여야 한다. 뭐... 그러나 미래에 형식언어의 정의가 바뀐다면 그렇지 아니할수도 있다... 아니 정확히 그렇지 아니할거다. 정의가 바뀐 미래에는"
> 

따라서 『형식논리는 **논리가 아니라 형식이다.**』

아스퍼거인인 나는 DLPFC를 통한 실행능력(계획•실행•사회적 사고)이 결핍되었기 때문에, 형식으로 사고한다.

그게 정말 논리적인 사고였으면 참 좋았을텐데, DLPFC라는 논리처리 프로세서를 쓰지않은 논리적 처리에서 나는 그저,

1. 몽상을 한다. 비논리적인 상태에서 증명에 로드맵을 짠다.
2. 해당 로드맵이 추론에 적합한지 형식논리를 통해 검토한다.
3. 형식논리적으로 기호를 조작한다.

순서로 사고한다.

그리고 【형식적이지 않고 진짜로 참된 관점에서의 논리적으로 일관된(logical cohereance를 가지는)】 논리는 이치에 맞아야 한다. 형식논리의 의미론(semmentics)는 언어 개임일 뿐이고,
그 이치가 구문론적인 언어 L위에서 T가 동작하기에 lang에 의해 의미론(semmentics)가 부여되어 「인간 사고」로 동작하는것이지, 인간사고이기 이전에 생각도 언어도 뭣도 의미도 아닌 형식일 뿐이다.

따라서 형식논리는 자연어의 논리와 다른 개념의 논리이다.

#### 2026년 반박.

요약 : 만약, 보편의 페러다임 시프트 가설이 맞다면...  보편적이지 않은 개인의 해석, 즉 화자간의 해석 차이 문재는, 실제로 존재하는 문제이기에, 논리 해석에 있어 예외이게 된다.

개인의 해석에 따라서, 언어 화자가 긍정하는 (A, B, C)는 개인 차가 존재한다.

물론, "화자 X의 언어 사용 방식 (A, B, C)는 맞다/틀리다"라는 문장으로 잣대를 들이대서, 모두가 보편적으로 맞게 해석한 문장을, 언어로 삼는것이 맞다.

언어의 사회성은, 표준 해석 방식인 `(A, B, C)`의 범위를 지정한다. (일반적으로 지지되는 이데올로기든 아니든, `(A, B, C)`는 여러가지다. 사람들이 새상을 보는 창에 다라, 범위도 달라진다.)

그렇기에, 혼자서 언어를 이상한식으로 해석하는, 짜증나는 친구 B가 있다면, 그 사람한테는 해당 언어가 (A, B, C)로 해석될거다.

어쩔수가 없다... 개인의 해석 차이는..

언어의 의미는 그 "사용 방식"(그 사용 방식은 여러가지가 있는데, 일반적인 인간은, 일반적인 사용 방식을 쓴다)에 있다.
````

겉뜻의미론을 통해, 함수형으로 환원된, 품사의 표기법.

그러나, 속뜻의미론은 표현하지 못한다.

### 의외성 정리

````markdown
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

위의 의외성 정리는 2025년 6월에 작성되었다. (분명 그 이전일텐데 뭔가 잘못된것 같다. 근처 파일이 죄다 6월이다.), 지금은 다른 엄밀한 정의를 쓸거다. 그니까 아래 해설을 받아들이도록 하자.

겉뜻의미론 : 의미화용론상 의미론
속뜻의미론 : 의미화용론상 화용론

위 내용을 해설해보자)

자연어 문장 s, v에 대해서, 

p : "s의 뜻은 s다."

인 p를 만족시키는 s가 존재하여, 그때의 s의 뜻을 겉뜻이라 한다.

예를들어, "지금 나는 이 내용을 노트해야겠다고 생각함"이라는 문장같이 다른 해석의 여지를 남기지 않는, 상당히 명시적인 구문이 그 예다.

그러나 p를 만족하지 않는 s가 존재한다.
p를 만족시키지 않는 s의 예시는 쉽게 들수 있으므로, 자세한 설명은 생략한다.

q : "s의 뜻은 v다"

인 q에 대해 v가 뜻인 경우다.

즉, 속뜻은 이항관계 "(s, v) ⊨ q"에서, s에 대한 v이다.

s = v일때, 속뜻이 겉뜻인거다.

## 보편명제 증명론

````markdown
# 보편명제 증명론

인과관계란 "SI P, ERGO Q"가 가지는 관계를 말한다.

N.B. 자연어에서는 "EXSTAT ALIQUIS P, Q, SI P, ERGO Q. NON HOC EST, NON L VEL Q"다. 다른 경우가 존재한다. 칸트의 정언명령과 그 공리는, 자연어가 사용하는 "맥락(CONTEXTOUS)"에 따른 인과관계를 써야한다.

함축관계 : 무맥락 인과관계
무맥락 인과관계 : "NON P VEL Q"를 이르는 말

## 절대적인 규칙 : 논리의 정의에 따라서 보편적으로 참인 문장

"SI QUOD ILLUD, SI P, ERGO Q, EST VERUM ATQUE IN ID CONTEXTOUS, SI NON P VEL Q, EST NON REPUGNAT, ERGO, NON P VEL Q"

즉, 기존 문맥과 맥락 정합적일때만, 전건긍정이 성립한다.

## 문장의 해석

자연어를 해석하는 구문을 자연어로 작성하면 "Q. p의 뜻은 q인가? A. yes"이다.

자연어에서는, 화자와 청자가 있으니, 스스로에게 질문한다면, 긍정 여부를 알수 있다.

## 증명 이론 : 문장이 함축하는 의미의 파악

그걸 자연어로 쓰면 "p이다. Q. 그렇다면 q인가? A. yes"의 형태가 된다.

보편 명제의 증명은, "SI QUOD ILLUD, SI P, ERGO Q, EST VERUM ATQUE IN ID CONTEXTOUS, SI NON P VEL Q, EST NON REPUGNAT, ERGO, NON P VEL Q"로 진행되기 때문이다.

## 문맥 스택 (Contextous Stack)

문맥 의존 언어는, 최소한 push-down automata로 작동한다.
그러므로, "ATQUE IN ID CONTEXTOUS, SI NON P VEL Q, EST NON REPUGNAT"라는것은, 이전 문맥을 참조한다.

그러므로, 문장은 Contextous Stack에 보편명제 증명론에 의해 「사고를 이치에 맞게 이끌어 가는 과정 (Step by Step)」을 타당하게 적었다 볼 수 있다.

## 형식화된 보편명제의 증명

사고에 있어서, `1. 2. 3.`이라는 스탭별로 진행한다.

문단의 리스트 Paragraph에 대해, Paragraph[i]는 i문단이고, Paragraph[i][j]가 i문단의 j문장일때,

ContextousStack[StackPointer] = "Paragraph[i][j]의 값은 p다."
ContextousStack[StackPointer + 1] = "Q. Step1 Question"
ContextousStack[StackPointer + 2] = "A. Step1 Answer, Q. Step2"
...
ContextousStack[StackPointer + n] = "UT, Step_n"
식으로 추론된다.

이는 배외측전전두피질(DLPFC)가 인간에 뇌에서, Step별로 추론을 하기 때문이다.

굳이 Step시스템을 쓸 필연성은 없다. 물론 필요성은 있을수 있다.

뇌피셜 (이론적 조망과 개연성에서, 통계 모델로의, 보편적 인식의 페러다임 시프트 가능성) : 확률적으로 추측하는게, Step시스템보다 "강한 이론 (큰 틀을 설명하거나 설명 능력이 강한 이론)"인 경우, 인간은 논리를 버리고 기꺼히 강한 이론을 택할수도 있을것같다.
````