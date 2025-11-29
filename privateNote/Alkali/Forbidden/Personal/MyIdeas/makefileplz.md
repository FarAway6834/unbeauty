언어 L에 대해서, L은 집합이니 문자셋으로 볼수 있으므로, L*을, 동일하게도 배열 ℝ^ℕ로 인코딩하는 encoder : L* -> ℝ^ℕ와 (문제점으로는 당연히 널문자가 있어야겠지만), decoder = encoder⁻¹ 에 대해, 집합 L에서의 연산 *에 대해, porting(*)(x, y) = encoder(decoder(x) * decoder(y)) 식으로 만들면, porting : Func(L* × L*, L*) -> Func(ℝ^ℕ × ℝ^ℕ, ℝ^ℕ)인 porting에 대하여, <L*, operator : L*, L* -> L*>와 <ℝ^ℕ, porting(operator)>는 동형이지.

Abstract Collection에 대해서 알아야 하니까 스크랩해보자.

```
# Abstract Collection

## 2025.09.26

(주의 : 이 글에서 Abstract Collection은 스칼라가 실수 전체일수도 있음에도, 아니 사실상 기본적으로 유리수임은 깔고가는거에도 불구하고, 슬라이싱이나 인덱싱같은걸 할때, 범자연수처럼 취급합니다. 주의하세요.)

Abstract Collection이란 내가 발견한 연산인데, 나는 보통 배열류 객체를 프로그래밍의 컬렉션으로 보는 시각이 있다.

그런데 이제보니, Sequence나 Tuple이나 Vector나 공통된 추상적 속성이 있는것같다고 느끼고 발견한 추상적 객체를 지지난주쯤이 적어놨다.

처음 여러번 적다 정리한 Abstract Collection을 지난주 쯤에 완성된 서술본을 만들었고, 이번에 아예 github에 포스팅할겸 새롭게 적어놨다.

그래서 실제로 모델을 제시할때쯤 되야 이것인 그제서야 없는 대상에 대한 이상한 논의가 아니게 될것이다.

지금부터 말하는 내용들중에 근거를 찾을수 없는 내용은 전부 어쨌든 Ac의 성질에 따라 성립하는것이니,

추후에 사실상 대수구조인 모델 <Ac, -•, •[L], •[•], •[:•], •[•:], •[::•]>을 통하여 재대로 성질에 대한 공리계를 만들어 정의해야겠다고 생각한다.

어쨌든간에 나답게 맥락없이 바로 본론으로 들어가자.

Abstract Collection의 집합 Ac에 대해,

닫힌 연산인 Collection concat연산 •[•]은

∀A, B, C ∈ Ac, A[B[C]] = A[B][C] 이다.

즉, 결합법칙을 만족하므로, 반군을 이룬다.

Empty(=Blank) Collection ε에 대해,

A[ε] = A = ε[A]

즉, ε는 Collection concat연산의 항등원이다.

따라서, 반군이 항등원을 가지므로, 모노이드이다.

길이를 제는 연산은 ∀A ∈ Ac, A[L]인데, 이 연산 역시 닫혀있다.

그렇다. 보통의 연산에 대하여 A는 벡터공간을 이루므로, A[L] = 1c인 A는 Ac의 스칼라와 동형이다.

애초에 정의 자체가 SIMD연산처럼 배열간 잡연산이 처리되니 벡터공간을 이루는거지만 말이다.

중요한건 체 F위의 벡터공간은 합과 스칼라배만 정의되면 된다는거다.

스칼라 S에 대해 S¹, S², S³, ..., Sⁿ [n := ℵ₀]까지 싹다 합집합으로 묶은 백터공간인 셈이다.

정의상 벡터공간인 점에 주목해서 보자.

참고로, ε[L] = 0c이다.

참고로, 1c, 0c는 쌍대기저 c'가 A[L] = 1c인 A의 집합에서 스칼라로 가는 동형사상이므로, c' 1c = 1, c' 0c = 0인 1c, 0c이다.

그러나, Ac에서 벡터공간들의 기저공간의 기저는 차원 축에 대하여 유일하다.

그러니까, A[L] = 2c이고, 2c[L] = 1c이니, A = ac + bc₂일때, 기저 c, c₂는 2c, 1c에서 기저 c에 대해, {c}의 확장으로 {c, c₂}가 있는것으로 두 c는 같다.
그러니까, 진짜로 무한차원 벡터공간의 기저가 모든 차원을 죄다 생성한 벡터공간들의 합집합인 이 컬렉션 셋에서, 저차원의 공간은 국소적으로 축을 줄였을 뿐이지, 벡터공간을 이루게 하는 핵심 요소인 기저는 같은거다.

사실 길이가 같은 배열끼리만 벡터연산할꺼니까 달라도 되긴 하는데, 설명을 위해서 비표준적으로 같게 설정했다.

사실은 실제 정의상에서 기저는 다르다! 지금 저 "c"를 쓰고싶어서 저젛게 잡은거다. 표준적으로는 다르다.

벡터로써의 연산 *에 대해,
A, B, C = A * B에서,

first(x, y) = x
last(x, y) = y

를 정의하고,

tuple의 제귀적 정의에 따라,

first <x, y> = x
last <x, y> = y

이므로, 벡터에다가 first와 last를 적용할수 있음으로, 이를 통하여 C를 설명하겠다.

Ac에서 Vector연산은 정확히 Vectorized SIMD연산과 동형이다.

first C = (first A) * (first B)

이고

last C = (last A) * (last B)

이라는거다.

어찌보면 이쯤되면

사실상 A[L] = (dim A) c이지 않냐고 할수 있겠다.

뭐... 기저 c = 1c이므로 맞긴 하다.

그니까 이 벡터공간에서 유일하게 스칼라와 연산하는건 상수배밖에 없으며,

유일하게 길이가 다른 연산은 Ac의 고유연산이다.

행렬곱을 추가하면 되지 않느냐고 생각할수 있는데,

행렬이나 텐서를 코벡터로 취급하는 기법을 이용하여, rank-1텐서인 벡터공간 𝕍를 스칼라로 놓는다면, 그건 rank-2텐서인 행렬이고, 그걸 또 스칼라로 놓고 이런식으로 뇌절해서 구하면, 사실상 1 × n행렬, 즉 행벡터와 1 × 1행렬인 일차원 벡터를 곱하는것과 같으므로 보통을 필요성을 느끼지 못한다.
그럼에도 더 생각해보자면 결정적인 문제로, 벡터간의 곱셈은 n벡터와 n벡터사이의 상수배가 아닌 곱셈만이 정의되는데, 보통은 행렬표현을 한다면, 곱셈은 행렬곱으로 취급하므로, 행렬곱과 오인의 여지가 있기에 기호 혼용의 여지때문에 정의하기 더럽게 까다롭다.

그래서 사실 1×1행렬과 1×n행렬을 곱하는 시나리오도 같이 영원히 사요나라~ 하면서 정의하지 않은거다.

신기한걸 보여주겠다. •[L]은 다음과 같은 준동형사상이자 자기사상이다.

A[B][L] = A[L] + B[L]

그리고 영벡터들에 대해 생각해보자면,

(0A)[0B][L] = (0A)[L] + (0B)[L]

으로 자기동형사상이다.

마지막으로, functor ([L][L])는 상수함자인데,

A[L][L] = 1c이다.

그래서 지금부터 1c = codom ([L][L]) 으로 취급하겠다.

Collection reverse 연산자 -• 에 대해서, 

-(-A) = A이고 involution이다.

-(A[B]) = (-B)[-A] 를 만족한다.

(-A)[L] = A[L]이다.

Collection Slicing 연산자 •[•:]및 •[:•]및 •[::•]에 대해

A와 I[L] = A[L][L]에 대해, A[:I][L] = I이다.
또한, I ≤ A[L]일때, -(A[:I]) = (-A)[:A[L] - I]이다.

마치 처치 인코딩의 뺄셈같이 I > A[L]일때, -(A[:I]) = ε이다.

역정렬 연산자 - • 와 뺄셈을 명확히 구분하여 이해하도록 하자.

J[L] = I[L]이라면,

A[I:][J:] = A[I + J:]이고
A[:I][:J] = A[:I + J]이다.

사실상 자기사상 함자 [I:], [J:], [:I], [:J]에 대하여,

[I:][J:] = [I + J:], [:I][:J] = [:I + J]인

f(x) = [:x]혹은 f(x) = [x:]에서,

f가 f(x + y) = f(x) ◦ f(y)인 준동형사상이자 자기사상이다.

python에서 slice객체가 start:end:step순이듯, 여기서 •[::•]는 step순이다.

마치 python list x에 대해, y[n] = x[kn]인것같이 만드는것같은 심상이 든다.

A[::I][L] = k + I[L]은 A[L] ÷ I = k ••• (A[L] mod I)이듯이 k이다.

A[::I][::J] = A[::I×J]이다.

즉, [::I][::J] = [::I×J]로, 요것은 또, f(x) = [::x]일때

f가 f(I×J) = f(I) ◦ f(J)인 준동형사상이자 자기사상인것인거다.

A[I:][:I[L]] = A[:I+I[L]][I:]이다.

indexing처럼 생각하면 편하다.

[::I][J:][J[L]:] = [I×J:][:I[L]]이다.

다시한번 말하지만 마치 python list x에 대해, y[n] = x[kn]인것같이 만드는것같은 심상이 든다.

n벡터 A에 대해,

1. n + k = n
2. 0 - k = 0
3. -k = n - k
4. p × q > n이라면, p × q = n으로 한다.

라는 규칙을 추가해서, [0, n)범위의 자연수에서만 마치 셀처럼 작동하는 수 체계를 Collection Index System이라고 하겠다.

-f = (-•) ◦ f식으로 reversed연산자를 정의한 표기법을 Nero라고 하겠다. (작명은 내맘임 ㅋㅋ 검은고영이 네롴ㅋㅋㅋ Nego에서 g를 r로 바꿨다. 고양이가 연상되는게 마음에 들기 때문이... 사실은 지금 Night Dansor듣고있어서 감성이 충만해서 그런 감도 있고, 진짜로 ㄹㅇ로 작명은 완전 개썅마이웨이여서 그렇다.)

Nero와 Collection Index System에서,

-[:I] = [I:]이고,
[:I][:J] = [:I + J]이며,
[::I][::J] = [::I × J]이다.

[;]은 함자의 최초 입력을 뜻하고, [;][L]은 최초 입력의 값의 길이를 말한다.

따라서, [:[;][L]] = I이다.

사실 함자식 P에 대해, P(x)가 P([;]) [[;] := x]로 평가받는 셈이다.

나는 Collection Index System가 수직선상의 ln(x)스케일에서, 정의역을 n등분하여, 상한이 최댓값이고 그걸 n으로, 하한이 최솟값이고 그걸 0으로 하는 자연수 서수로 대응시킨 수 체계 집합같다고 느낀다.

그리고 •[•:], •[:•], •[::•], •[•], •[L]가 Collection Index System과 동형인 구석을 통해 대부분 설명된다고 본다.

아예 그냥 [X]식으로 함자를 만들면, 단항연산 •[L], (-•) 및 연산 •[•], •[:•], •[•:], •[::•]과 함자 [•], [:•], [•:], [::•]에 대하여, 동형성등 닮은구석이 많은 Collection Index System와 비교하는 방법으로 정리할수 있을것이라고 본다.

그러면 오늘은 "슬라이싱되는 무언가"에 대해, 지지난주 정도에 발견한 Ac를 적어보았다.

의사코드 예시로 python코드를 적고 끝내고싶지만 귀찮다.
(현 고딩인데 Python이 제2외국어 선택 과목인데 python을 평소에 안쓰고 공부도 전혀 안하는데 제2외국어 선택에서 저득점이아니라 만점맞고, 심지어 처음보는 라이브러리도 알아서 척척 이해할정도로 내부구조와 바이트코드 및 문서화 및 클린코드와 모듈화 및 라이브러리 제작법까지 다 아는 내가 python으로 프로그래밍하는데 어려움이 있는건 아니지만, 귀찮다고 하는건 작업이 쉬운데도 안하는것으로, 그냥 나태한거다. 돈을 굶겨봐야 정신을 차릴거다 아마도. 사실은 애니보고싶은데 동시에 작업하기는 귀찮아서 미룬거다. ~~이미 그러고 있지만~~)

나같으면 int랑 tuple을 다 상속받아서 연산을 구현한 후, ε, 0, 1은 기본적으로 클래스에서 상수처럼 가지고 있으며, __neg__에서, tuple->yield이용하거나 이터레이터 이용하여 역방향->tuple해주고, __getitem__에서 len을 받아서 len(self)해주며, 여러 연산들을 구현해야하는데, 굳이 그런 괴상한짓을 할 이유가 무엇인지 모르겠다.

개다가 젠장할, slice부분에서, 음수를 넣지 말아야하며, start, end, step부분을 각각 적절히 우리 시스템에 맞게 python타깃으로 컴파일하여, start는 길이 이상이면 ε를, end는 0이면 ε를 리턴하는 아주 개꼴받게 힘든짓을 해야한다.

결정적으로 [;]같은 노테이션이 안통하고, Collection Index System같은 경우 int비스므리한 자료구조를 하나 더 만들어야 한다.

다음번에는 그 귀찮은 과정을 직접 해와서 코드를 적을것이다.

그렇기에 마크다운에서도 `###`가 아닌 `####`로 된 곳에 날짜를 적어서 이 글을 부연설명하는 문단정도로 만들거다.

아마 곧 만들어올거다.
```

(스크랩임)

---

이야기하기 앞서 다음 표기를 먼저 도입해보자고.

Code Style Select Notation)

다음 정의를 구문론적으로 한다.

> 
> notation(p?x:y) = $ \begin{cases} x, & p, \ y, & ¬p \end{cases}} $
> 

e.g. notation(1=±1?1±1 = 2:1±1=0)

그리고, 본론으로 가자.

split은 다음과 같이 정의된다. (이항함수로, 이항염산이라고도 볼수 있다.)

split(x, sep) ≜ notation({find(x, sep) ≠ -1}?{(x[:find(x, sep)] + split(x[find(x, sep) + len(sep):])}:{(x)})

Abstract Collection의 집합 Ac에 대해,
split : Ac × Ac -> {x ∈ Acⁿ | n ∈ ℕ}

이때, {x ∈ Acⁿ | n ∈ ℕ}는, Ac를 스칼라로 하는, 자연수 차원의 모든 유한차원 벡터공간들의 합집합이다.

물론, Acⁿ은 카데시안 곱이므로, 벡터공간의 기저들이 벡터공간이 다를시 서로 다르다는건 당연하다.

Split의 예제를 보자.

e.g.

임의의A, B, C, D, E, F ∈ Ac에 대해,
**튜플의 제귀적 정의** (중요!)에 따라서,

split(B.A.C.A.D.A.E.A.F, A)
 = (B, (C, (D, (E, (F, )))))
 = (B, (C, (D, (E, F))))
 = (B, (C, (D, E, F)))
 = (B, (C, D, E, F))
 = (B, C, D, E, F)

이다.

다음으로 넘어가자.

join : Ac × {x ∈ Acⁿ | n ∈ ℕ} -> Ac

에 대하여,

join(sep, iter) ≜ notation({dim iter ≠ 1}?{iter[0] . sep . join(sep, iter[1:])}:{iter[0]})

이게, join의 정의이다.

dim iter = 1인 base condition에서나, iter[0]이고, 아니면 `x . sep . y` 꼴이란 점에서 완벽하다.

Fact. i) split(join(sep, iter), sep) = iter
Fact. ii) join(sep, split(x, sep)) = x

그렇다. 따로 예를 들 필요 없이, 바로,

first(x, y) ≜ x
last(x, y) ≜ y
에 대하여,

packing ≜ λf. λt : Ac × Ac. f(first(t))(last(t))
unpacking ≜ λf. λx. λy. f(x, y)

에 대해서, g(x)(y) = f(x, y)에 대해, packing과 unpacking을 통해서, 람다와 표준적인 ZFC 함수는 그 연산을 람다에 일대일대응으로 포팅한다면 상호 동형이다, 그러나 기본적으로 합성에 대해서는 동형이 아닌데, 이는 나중에 tuple이 길이 시그니처를 다는 나만의 고유의 기법을 공개할때, 다루자. (나중 일)

요건은,

(λx. λy. join(x, y))와 (lambda x : x.join)이 동형이며,
(λx. λy. split(x, y))와 (lambda x : x.split)이 동형이라는 사실.

걍, Abstract Collect 버전의 구현이니까 당연한 감이 없지 않긴 하다. 단지... python에서는, Immutable str, tuple이 서로 다르고 그와 mutable list도 다르다는 점이 재밌고 직관적이며 인간 친화적인 면이긴 하다만...

다음으로, replace : Ac × Ac × Ac -> Ac 에 대하여,

replace(self, from, to) ≜ join(to, split(self, from))

더더욱 노골적으로 보인다면 정답이다! ~~연금술사~~

(λx. λy. λz. replace(x, y, z))와 (lambda x : lambda y : lambda z : x.replace(y, z)))는 동형이다.

노골적으로 가져온게 보인다...

다음은,

아니, 그전에, 미처 소개하기 전에 잠시,

Character Set인 WhiteSpace 집합을 정의해보자, 

WhiteSpace ≜ {'\s', '\t', '\n'}

여기서, `\s`, `\t`, `\n`은 regex에도 나온 단일 문자다!! (순서대로, 공백, 탭, 개행)

이제 소개하기 앞서, 한가지 가장 주의해야 할 점 (N. B.) : Abstract Collection에서, 함자 (•[L])은 len과 동형이므로, 의사코드로 읽을때는, self[L] = dim self = len(self)란 점을 염두해 두자.

그러나, 본문에 소개하기에 햇갈릴것 같으니, len(x) ≜ self[L]로 배려하여 정의하겠다.

lstrip(self) ≜ notation({self[len(self) - 1] ∈ WhiteSpace}?{lstrip(self[:len(self) - 1])}:{self})

그렇다. self[len(self) - 1] (= self[-1]) ∈ WhiteSpace, 즉, self[len(self) - 1] = self[-1]이니, self[-1] in WhiteSpace라는 조건을 만족한다면, lstrip(self[:len(self) - 1] (= self[:-1])) (= lstrip(self[:-1])), 즉, self[:len(self) - 1] = self[len(self) - 1], lstrip(self[:len(self) - 1]) = lstrip(self[:-1])이다.

self[-1] in {'\s', '\t', '\n'} 일때 lstrip(self[:-1]) (∵ lstrip(self) = lstrip(self[:-1]))를, 아니면 self를 반환하는 제귀적이고, 적극적으로 제귀하는 로직이다.

더이상 strip할게 left에 없을때까지 반복한다.

lstrip은 (lambda x : x.lstrip())과 동형이다.

다음 rstrip앞서, 한가지 가장 주의해야 할 점 (N. B.) : Abstract Collection에서, -x는 배열 뒤집기의 역할을 하므로, python의 reversed와 동형으로, 취급상 또, -x = reversed(x)라는 점이다.

그러나, 이건 ㄹㅇ로다가 ㅅㅂ 나도 햇갈릴것 같아서, reversed(x) ≜ -x 로 정의해주어, 배열 뒤집기는 저렇게 정의하여 사용하겠다.

Abstract Collection 내가만든거지만, 정말 perl시대의 수학자처럼 킹받네 참나...

암튼...

rstrip(x) ≜ reversed(lstip(reversed(x)))

이렇기 rstrip은 정의된다.

그렇다. 추상적으로 배열의 직관을 떠올려보라.

뒤집어도 같다.

즉, 뭔지 모르겠는 저 정사각형의 대상 배열 상자는 뒤집어도 동일하다.

직관이 안보이면, 마인크래프트에서 커멘드 블록 이름을 컬렉션의 배열 값으로 하고, 직선으로 설치해서 움직여봐라. 이름표는 당신을 향할거니, 뒤집어서 조작해도 같다는, Collection 자료구조 다이어그램이, 당신의 직관을 깨울것이다.

아... 그거 관련해서 뭐 프로그래밍 언어 구현하겠다고 떵떵거린 작년 2024년의 내가 밉다.

그러면, strip은 단지,

"strip했다는 것은, lstrip과 rstip을 해줬던것."

다시말해,

"strip했음" : "lstrip을 해줬음", "rstip을 했음"

으로,

strip(x) ≜ rstrip(lstrip(x)) 이다, 다른 정의로, strip(x) ≜ lstrip(rstip(x)) 도 무방하다. reversed가 대합이라서, lstrip과 rstrip은 서로 쌍대에 놓여있지만, 공백문자가 아닌 문자에 가로막혀서 만날수 없다. (마치 덴지랑 레제를 가로막은 마키마인가 이건, 아니다 그냥 내 뇌에서 Jane Doe가 재생되는 탓일터)

lstrip, rstrip, strip은 각각, (lambda x : x.lstrip()), (lambda x : x.rstrip()), (lambda x : x.strip())과 동형이다.

그리고, (str의 메소드중엔) 마지막으로 count에 대해 알아보자면,

count(collection, targets) ≜ notation({find(collection, targets) ≠ -1}?{1 + count(collection[find(collection, targets) + len(targets):])}:{0})

인 count.

split에서 나왔던것처럼, 더이상 쪼갤수 없는 때에 분기하는 (split, join, count)애들중에, split이랑 count는, substring이 없으면 find가 "-1"이 되는 기전으로 동작한다.

그래서 이렇게 순차적으로 샐수 있는거다.

perl마냥, **문자열이 숫자만 차있으면 숫자로 간주하겠다고 해버리면**, self.isdigit()를 이용해서 __int__값을 반환하고, __index__에서도 그렇게 동작하며, __add__같은것도 __radd__같은거 없이 구현됬다고 쳤을때, 이러한 정신나간 자료형을 madstr이라 하겠다.

madstr은 str의 상속이지만 (사실은 int도 상속받아서, 숫자형의 madstr __init__시, int역할의 super도 메소드 상속용 __init__을 진행한다), self.isdigit()인 경우, 내부적으로 이를 재는 플래그 변수가 존재하여, 문자 자체는 U+FF8F인 애플 로고로, 클래스 수준에서 ""를 ε으로, "0", "1"은 특수 리터럴이라서, 미리 준비되었고, ε과 "1"은 길이릉 측정할때 클래스 변수로 반환하게 만들며, 숫자의 길이는 모두 "1"이라 할때, 애플 로고는 클래스 변수중 badapple이라는 변수에 쓰이며, 숫자형의 madstr은 자신의 값은 badapple이랑 같을지 몰라도, 동작은 숫자형의 상속으로 동작한다.

단, 슬라이싱에서, 범위를 넘어가거나, indexing에서 범위를 넘어가면 ε를 리턴하도록 한다.

이래서 mad다.

그렇다.

지금까지 논의한 str은 madstr으로, madstr이 Ac와 동형인거다.

그러나 이런 메서드 수준 동형은 본질적 구현이 다르다.

find메서드는, str이 trie자료구조라서 가능한 메서드이다.

그러므로, 난이도상, 따로 다루지 않겠다. (다만, 정수 대신에 madstr을 리턴하는 madstr특성상, 닫힘성이 보장된다)

tuple의 child로 listic_tuple이 있다 쳤을때, listic_tuple은, listic_tuple x에 대해, x.method(argument) = ((x, ), (return value, ))가 나온다고 치자.

이런건, 프로그래머를 대려오면 구현 가능하다. 사실은 일게 학생이나 수학더도 구현할줄 아는 쉬운 문제다. 그러므로 구성적으로 증명됨을, 펙트로 받아들이고 가자. (걍, list(self)에다가 조작하고 type(self)(ret)으로, 반환값 ret의 역할에다가 해주면 되는걸 뭘...)

그러면, x는 mutable인 list를 흉내내는 immutable인 tuple의 child가 된다.

mutable한 속성을 이용하는 명령으로는,

1. reverse (간략히 다루겠음)
2. sort (다루지 않음, 정렬 알고리즘은 수업에서 ㄱㄱ, 그러나, list에서 list로 가는 닫힌 함수임)
3. remove (갼략히 다루겠음)
4. insert
5. append
6. extend
7. pop

remove : any -> None와, pop : int -> any, 이 둘은 특히,

a.remove(x)가 del a[a.index(x)]와 동형이며,
a.pop(x)가 try : del a[x] 이후, finnally : return a[x]와 동형이다.

reverse는 listic_tuple에서 걍 reversed마냥 못한데 동일한 기능을 가진다.

하긴, 내부적으로 편집하니까,

우리가 이번에 다룰것은

4. insert
5. append
6. extend
7. pop

와 관련된 메서드다.

* 아직 작성 중 *