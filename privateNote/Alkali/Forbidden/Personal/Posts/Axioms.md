# ZFC내에서 구축한 공리계 모델간의 특이한 상호서술관계 : Axiomizer

## Axiomizer System 구축 : AxiomizerModel

Defination : 연산자 삼항연산자의 정의)

> 
> $Φ?A:B = \begin{cases} A, & (Φ), \ B, & ¬(Φ) \end{cases}$
> 

Definition : 순서쌍의 정의)

> 
> (x, y) := {{a}, {a, b}}
> 

Definition : 튜플의 제귀적 정의)

> 
> (x, ...) := (x, (...))
> 

Defination : 다변수 함수 first, last의 정의)

first(x, y) ≜ x
last(x, y) ≜ y

1. dom first = dom last
2. codom first = codom last

Defination : 술어 Conjectioner의 정의)

> 
> Conjectioner(tup) : (tup ∈ dom first)?(first(tup) ∧ Conjectioner(last(tup))):(tup)
> 

Defination : 술어 Axiomizer의 정의)

> 
> Axiomizer(Axiom) : ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) ∧ Conjectioner(Axiom)
> 

Defination : 모델 ℳ으로 묶어주기)

이쯤 되면, 모델 ℳ = <codom first, first, last, Φ?A:B, Conjectioner, Axiomizer>에 대하여,

함수기호들에 대한 할당은,

1. first := (codom first², codom first, graph first)
2. last := (codom first², codom first, graph last)
3. Φ?A:B := (codom first³, codom first, graph Φ?A:B)

이고,

술어기호들에 대한 할당은,

1. ∀tup ∈ Conjectioner, tup ∈ dom first ⊢ first(tup)
2. ∀tup ∈ Conjectioner, tup ∈ dom first ⊢ (last(tup) ∈ Conjectioner)
3. ∀x ∈ Conjectioner, x ∉ dom first ⊢ x
4. Axiomizer := {Axiom | ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) ∧ Conjectioner(Axiom)}

인 모델 ℳ인거다.

참고로, 아직도 codom first의 정체는 모르겠다...
전채집합을 의도하고 만들었지만 그런게 없기에 미정으로 하겠다 아이고 내 능지.
아마 그로덴티크 우주 취급당할듯

> 
> AxiomizerModel := ℳ
> 

로 정의하겠다.

참고로, 그래프를 그려보자면,

1. graph first = {(x, y, z) | x = z}
2. graph last = {(x, y, z) | y = z}
3. graph Φ?A:B = {(a, b, c, y) | (a ⊢ y = b) ∧ (¬a ⊢ y = c)}

왜냐하면,

1. first(t) = v s.t. ∀x ∈ t, ∃!v ∈ t
2. last(t) = v s.t. ∃!x ∈ t s.t. x - {first(t)} ≠ ∅, ∃!v ∈ x - {first(t)}
3. z = p?x:y, p ⊢ z = x
4. z = p?x:y, ¬p ⊢ z = y

이기 때문이다.

이야... 진짜, ZFC요녀석, 집합 하나 정의됬다고, 엄청 많은 공리를 생략할수 있어서 편하다. 공집합 공리로 공집합이라는 대상도 상정하고, 내부 이론으로 유일성도 정의됬고, `x s.t. y`기호로, ε-operator의 역할인 `εx (y)`도 수행하고, 등호`=`나 부등호 `≠`는 외연공리로 아주 잘 정의되었고, 다변수함수와 그 활용법과, 함수까지 튜플가지고 정갈하게 정의되서, graph로 젠~~~부 파악되고, 집합의 정의를 쓸때, 페아노 공리계마냥 여러가지 조건을 붙일수 있고...

이거야말로 상상의 천국 아닌가?

## Axiomizer와 공리계.

Axiomizer Model 상

> 
> 1. BootstrapperAxiom : x ∧ y → x
> 2. BootstrappeeAxiom : Axiomizer(Axiom₁, ..., Axiomₙ)
> 

두가지 공리만 있으면,

Axiom₁, ..., Axiomₙ을 공리로 삼는 공리계와 상호 서술관계이다.

BootstrappeeAxiom = ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) ∧ Conjectioner(Axiom) 이므로,

BootstrapperAxiom에 따라서,

> 
> 1. x ∧ y → x (Hyp : BootstrapperAxiom)
> 2. ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) ∧ Conjectioner(Axiom) (Hyp : BootstrappeeAxiom)
> 3. ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) (Monus Ponens)
> 
> Conjunction's Charactoristic Lemma : ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z))
> 

BootstrapperAxiom의 전건을 BootstrappeeAxiom로 취급하여, 전건긍정을 조져줄수 있으며,

재탕해보면 (i.e. in id est)

> 
> 1. x ∧ y → x (Hyp : BootstrapperAxiom)
> 2. ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) (Hyp : Conjunction's Charactoristic Lemma)
> 3. x ∧ y = y ∧ x (Monus Ponens)
> 
> Conjunction's Commutative Law (Theorem) : x ∧ y = y ∧ x
> 

x = y : (x → y)∧(y → x)로 정의되었기 때문에

> 
> 1. x ∧ y → x (Hyp : BootstrapperAxiom)
> 2. (x ∧ y → y ∧ x)∧(y → x ∧ y) (Hyp : Conjunction's Commutative Law)
> 3. x ∧ y → y ∧ x (Monus Ponens)
> 
> Conjunction's Commutative Lemma : x ∧ y → y ∧ x
> 

이렇게 Conjunction's Commutative Lemma를 얻는데, 이번엔 이거를 Conjunction's Charactoristic Lemma에 대한 추론규칙마냥, Conjunction's Charactoristic Lemma를 전건으로, 전건긍정을 조져주면,

> 
> 1. x ∧ y → y ∧ x (Hyp : Conjunction's Commutative Lemma)
> 2. (x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z) (Hyp : Conjunction's Commutative Lemma)
> 3. x ∧ y → x (Hyp : BootstrapperAxiom)
> 4. (x ∧ (y ∧ z) = (x ∧ y) ∧ z) ∧ (x ∧ y = y ∧ x) (Monus Ponens : (1, 2))
> 5. (x ∧ (y ∧ z) = (x ∧ y) ∧ z) (Monus Ponens : (3, 4)
> 
> Conjunction's Associative Law (Theorem) : x ∧ (y ∧ z) = (x ∧ y) ∧ z
> 
> 덤으로,
> 
> 1. x ∧ y → x (Hyp : BootstrapperAxiom)
> 2. (x ∧ (y ∧ z) → (x ∧ y) ∧ z) ∧ ((x ∧ y) ∧ z → x ∧ (y ∧ z)) (Hyp : Conjunction's Associative Law)
> 3. x ∧ (y ∧ z) → (x ∧ y) ∧ z (Monus Ponens)
> 
> Conjunt Associate Right2Left Lemma : x ∧ (y ∧ z) → (x ∧ y) ∧ z
> 
> 1. x ∧ y → y ∧ x (Hyp : Conjunction's Commutative Lemma)
> 2. (x ∧ (y ∧ z) → (x ∧ y) ∧ z) ∧ ((x ∧ y) ∧ z → x ∧ (y ∧ z)) (Hyp : Conjunction's Associative Law)
> 3. x ∧ y → x (Hyp : BootstrapperAxiom)
> 4. ((x ∧ y) ∧ z → x ∧ (y ∧ z)) ∧ (x ∧ (y ∧ z) → (x ∧ y) ∧ z) (Monus Ponens : (1, 2))
> 5. (x ∧ y) ∧ z → x ∧ (y ∧ z) (Monus Ponens : (3, 4))
> 
> Conjunt Associate Left2Right Lemma : (x ∧ y) ∧ z → x ∧ (y ∧ z)
> 

같은방법을 BootstrappeeAxiom에 적용해주면,

> 
> 1. x ∧ y → y ∧ x (Hyp : Conjunction's Commutative Lemma)
> 2. ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) ∧ Conjectioner(Axiom) (Hyp : BootstrappeeAxiom)
> 3. x ∧ y → x (Hyp : BootstrapperAxiom)
> 4. Conjectioner(Axiom) ∧ ((x ∧ y = y ∧ x) ∧ (x ∧ (y ∧ z) = (x ∧ y) ∧ z)) (Monus Ponens : (1, 2))
> 5. Conjectioner(Axiom) (Monus Ponens : (3, 3)
> 
> Axiom Lemma : Conjectioner(Axiom)
> 

드디어 Axiom Lemma라는 논리식을 얻었다.

이 과정에서, 여러가지 형식논리적 문장을, 명제변항에 할당하였는데, 내 구린 작명센스로 모두들 Oh My Eyes라고 외치고 있을것 같다.

우윽... 내가 생각해도 구리다. 존재하지도 않는 허상에 이름을 붙였는데, 이건 최애의 아이 만화책 (그런 만화는 존재하지 않아야 해 ㅠㅠ, 카나짱의 그 행동은 아직 애니에 존재하지 않는다) 앤딩처럼 존재하지 말아야할 설정이었던것 같다.

그치만, 이제와서 저 심볼들을 바꿀수는 없으니, 작명센스가 좋은 사람이 도움좀 줬으면 좋겠다!

어짜피 논리 전개에 1도 영향 안간다. 이름 붙일수 없으면 가독성이 난잡해지는것 뿐.

> 
> 1. x ∧ y → y ∧ x (Hyp : Conjunction's Commutative Lemma)
> 2. x ∧ y (Hyp)
> 3. y ∧ x (Monus Ponens)
> 
> 에서, 이건 "SI ~, ERGO ...; DICO ID EST;"라는 논리전개방식이기에 이 서브증명이 증명하는 바를 잘 생각해보면 알수 있듯, 여기서 나오는 바는,
> inference ruled Conjunction's Commutative Lemma : x ∧ y ⊢ y ∧ x
> 
> 1. x ∧ (y ∧ z) → (x ∧ y) ∧ z (Hyp : Conjunt Associate Right2Left Lemma)
> 2. x ∧ (y ∧ z) (Hyp)
> 3. (x ∧ y) ∧ z (Monus Ponens)
> 
> 에서,
> inference ruled Conjunt Associate Right2Left Lemma : x ∧ (y ∧ z) ⊢ (x ∧ y) ∧ z
> 
> 1.  (x ∧ y) ∧ z → x ∧ (y ∧ z) (Hyp : Conjunt Associate Left2Right Lemma)
> 2. (x ∧ y) ∧ z (Hyp)
> 3. x ∧ (y ∧ z) (Monus Ponens)
> 
> 에서,
> inference ruled Conjunt Associate Left2Right Lemma : (x ∧ y) ∧ z ⊢ x ∧ (y ∧ z)
> 
> 뭐... 생략삼단논법처럼 대전재를 생략해서 쓰고싶었을 뿐이다. 에초에 커뮤니케이션 문재가 있는 놈들에게 사회에 대전재도 안알려주는, 의미 결여된 썩은 언데드 좀비들같은 사람들이 이러한 내 불친절한 놀이 스타일에 내로남불로 뭐라할 개연성도 없겠지만 ㅋㅋㅋ
> 
> 코딩컨벤션이니 맥락 정합성에 맞는 전개이니, 쉽고 간단한 증명이 좋은 증명이니... 말같지도 않은 사회적 룰을 가지고 형식논리를 판단하려 드는것은, 형식논리를 논리로 착각했다는건데, 정말~ ㅋㅋㅋ 타락의 끝판왕이다. 
> 뭐, 증명프로그램이나 프로그래밍언어에서 그걸 형식적으로 규정한적이나 있나? 형식언어라는 허상이 기계로 검증된다는걸 쳐 염두해 두고 생각좀 해야한다 진짜.
> 
> 규칙? 그런건, 등록시스템을 형식체계에 만들면 그만이다. 사실 규칙이 아니라, 서브증명을 통해서, 함축관계를 불러오는 편법이다. 아... 메타논리기호를 가져오다니, 메타논리 너무 허술하다.
> 

이어서,

...(작성중)...