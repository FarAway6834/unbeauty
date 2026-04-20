# NewFixedism

p means q : "p의 뜻은 q다"
EvaultingSemmetics : L♠︎(p means q) ↔ (L"p" =>* L"q")
evalmean : 언어 L에서 단어 "means"의 의미는, "p means p"가 참으로 평가되는 means다.
AffrimoOfInterpretation(G, L) : ♠︎"interpretation G, L의 문법규칙 P에 따른 means"
Tip) AffrimoOfInterpretation(G, L)는 interpretation G, L을 긍정하는것임.

human을 가능새계 의미론상 명제 V(♠︎"interpretation G, L의 문법규칙 P에 따른 means", human(h, t)) = 1를 만족시키는 human으로 정의한다. t는 시간, h는 그 사람이다.
물론, 가능새계의 존재를 긍정하는게 아니라, human이라는 Object가 필요했을 뿐이다. 프로그래밍 언어를 이상하게 골랐을 뿐, 그냥 형식적인 서술 목적으로 가능새계 의미론을 고른거다. 나는 해당 공리계에 대해 관심 없고, 동작만 배껴올 의도인거다. 참고로, ♠︎는 양상논리와 무관히 평가된다.

langof연산자)
langof(human(h, t))"p" := "V(p, human(h, t)) = 1"

fixed(h, p) : ∀t₁, ∃t₂, langof(human(h, t))"p" = langof(human(h, t))"p"
same(h, p) : ∃t₁, ∃t₂, langof(human(h, t))"p" = langof(human(h, t))"p"

LexAntiNecesse : AxiomaI ∧ AxiomaII
AxiomaI : ¬□((h, p) ⊨ fixed(h, p))
AxiomaII : ¬□((h, p) ⊨ same(h, p))

SocialPragmatics : 화자 h를 확률변수로 둘때, SP(t)"p" = E(langof(human(h, t))"p")식의 진리치를 가지는 화용론이다. 시대 t에 따라 바뀐다.
LexSocialPragmatics : SocialPragmatics는 기술주의적인 언어 L의 속뜻과 겉뜻에 영향을 준다.

LexSocialPragmaticsExLexAntiNecesse : LexSocialPragmatics ∧ LexAntiNecesse

DefineOfHuhen : 전문용어 "불변"은 시점 t에서 정의되었다면, 다음을 문장을 만족하는 단어다. SP(t)"문장 p가 불변의 진리면, ∀t, SP(t) est verum이다."
ExistanceOfHuhen : DefineOfHuhen에 따른 전문용어 "불변"은, 해당 전문용어를 쓰는 집단에서 정의된다.

어떤 interpetation혹은 형식언어등 대충 형식문법 G를 언어로 가지는 L에 대해, L♠︎ExistanceOfHuhen이라면, 그러한 L은 "불변 존재문 긍정"이라고 정의한다.

형식언어는, 고정된 해석을 가지는 언어를 말한다. 항상 형식언어 L은 그 형식문법 G가 어떤 시점 t에서도 동일하다. 물론 형식언어는 존재해야 정의 가능하다. 형식언어의 존재성을 ExistanceOfFormalLanauge라 하며, 이는 ExistanceOfHuhen의 존재성을 형식언어라는 예시로 긍정한다 다만, ExistanceOfHuhen이 가정되면 형식언어는 정의 가능하다. 어떤 형식문법 G를 모든 시간에 고정하면, 그것이 형식언어의 존재성에서 말하는 형식언어일 조건을 만족시키기 때문이다.

정의는 이만 하겠다.

1. 변형생성문법 G랑 언어 L에 대하여, interpretation은 저런 G, L로 표현 가능하고, 랑그(기표-기의 연결)도 저런 G, L로 표현 가능하고, "acept"체계나 "긍정자"로 표현되는 지식도 G, L로 표현 가능하다.
2. ideology를, Notaion•Digagram의 정의와, 값을 할당하는 정의와, 어떤 명제의 긍정이나, 논리 체계의 제시, 용어의 정의, 빈사•주사의 정의를 하는 interpretation이라 정의하겠다. 물론 유명론적인 명명임에 주의하라.
3. 언어 L에서, L"q" = L"p" ⊨ EvaultingSemmetics이다.
4. 어떤 맥락 의존 언어는 L♠︎(p means q)의 여부가 맥락에 따라 달라진다.
5. 평가의미론이란, evalmean를 긍정하는 의미론이다. 물론 이 경우, 어떤 맥락 의존 언어의 경우, 어떤 맥락 의존 언어는 L♠︎(p means q)의 여부가 맥락에 따라 달라진다는 논지로 설명한다. (참고 : 이 의미론은 현실의 복합사실에는 관심이 없다. 그냥 의미 평가가, 평가 의미론에서 제안하는 절차랑 동일하게 작동하면 동일하다는 duck typing따위에 불과하다.)
6. 규범주의적으로 정의되는 언어 L는 L"x는 표준어이다"라는 술어로 긍정되는 언어이고, 기술주의적으로 정의되는 언어 L은, 문장 EvaultingSemmetics를 만족시키는 언어다. (물론 기술주의를 파는 사람들이 반발항수 있으나, 평가의미론자인 나는 기술주의가 EvaultingSemmetics를 만족시킨다는 duck typing적 사실만 관심있을 뿐이다. 당연히 표면적으로 일치하는거지, 동작 이외의 세부구조는 다를수도 있지 않겠는가?)
7. 비필연성 공리계란, LexAntiNecesse를 긍정하는 공리계를 말한다. 평가 의미론의 확장 공리다.
8. L이 표준어라면 means는 표준 의미/화용론이여야 하고, L가 개인의 해석이라면, 그럴필요 없다.
9. 의미론은 겉뜻이고, 화용론은 속뜻이다.
10. LexSocialPragmatics하에서, 언어의 사회성이란 SocialPragmatics의 변화에 의한것이다. LexAntiNecesse은 평가 의미론의 확장 공리다.
11. LexSocialPragmaticsExLexAntiNecesse는 평가 의미론의 확장 공리고, 언어의 변화에 대해, 필연성이 없었기에 변화가 가능했다고 설명한다.
12. LexSocialPragmaticsExLexAntiNecesse에서, DefineOfHuhen에 따라, 전문용어 "불변"이 정의되려면, 임의의 시점 t₁에서 전문용어 "불변"의 의미가, 임의의 시점 t₂에서 전문용어 "불변"의 의미여야한다.
13. LexSocialPragmaticsExLexAntiNecesse의 관점에서, 불변 존재문의 긍정은 일개 interpretation이지, fixed된 만고불변의 진리일 필연성이 없다. 이에따라, ExistanceOfFormalLanuage역시 불변 존재문ㅇ 긍정과 동일하게, fixed된 만고불변의 진리일 필연성이 없다. (UnfixedTheorem)
14. UnfixedTheorem에 따라, 본 글에 적인 모든 논의는, 참일 필연성이 없다.
15. 이 논의는 18가지 명제들을 긍정하고, 단어들을 정의하므로, ideology에 해당한다. 이 ideology는 변형생성문법의 집합론적 정의등등 형식언어로 작성된 ideology이다.
16. 이 논의 자체의 참을 보장하는 방법은 간단하다. 그냥, 이 논의 자체는 interpretation이고, interpretation과 언어의 차이(표준 interpretation을 논할수 있는 interpretation들을 가르키는 주사가 바로 언어다.)는 거의 없다. ZFC에서 AC를 그냥 참으로 도입하듯, 그냥 형식언어 자체를 참으로 도입해야 이야기가 시작된다. 그렇다. 이 이야기는 한번 증명을 마치면, 우리가 형식언어 자체를 참으로 도입할수 있다는 사실을 알려준다. 다만, 우리가 형식언어를 쓰는 중에. 형식언어를 언급한다면, 형식언어 L네에서, L을 정의하는것으로, L ≠ L"L"이기에, 자기지시 역설의 오류는 범하지 않는다.
17. 그렇다. 이건 논리적 강제성같은거 ㅈ까고, 그냥, 언어의 실체를 까발리기 위한 특수목적 언어일 뿐이다.
18. 어떻게 보면 공리계의 언어다. 긍정한 공리가 하도 많으니.