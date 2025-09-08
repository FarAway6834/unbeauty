# TWaMLang : Language for TWaML(TalkWith_a_MathematicalLogic)

TWaMLang에 대해 소개하겠다.

~~JOKE : not TWaML-wise Argument Markup Language~~

| 성질명 | 성질값 |
| :---: | :---: |
| 정체 | 단순언어†문법 Based Langauge-like |
| 유형 | 굳이 따지자면 고립어 겸 형식언어-like |
| 어순 | Polandian Notation이라 굳이 따지자면 VSO |
| 서자방향 | 좌행서를 쓰되, 유니코드에서 우행서 리터럴이 나오면, 표준적인 유니코드 렌더링을 따름 |
| 문자 | 로마자 |
| 목적 | TWaML("수리논리로 말하기"의 준말임)용 언어‡ |
| 계통 | 영어랑 로지반에서 단어 몇게 쌔벼옴, 수리논리상 술어논리 기반, 일부 양상논리 기반 |
| 추구가치 | TWaML 적합성 (1순위), 논리적 사용의 유용성을 위한 언어별 엄밀성 제어 (2순위), 간단한 난이도의 여유롭게 이야기하기 좋은 양에 층분히 실용적인 수의 어휘 (3순위) |

그래서 굳이굳이 쓸대없이 많은 진리함수화된 술어화 연결사를 제공하고, 양화사도 여유만만하게 두개 주고, 진리값이 풍부한데도 두가지, 사인칭같은 쓸대없는 논점률 명사 존재, 로마자 표기법같은게 있는거다.
개인적으로 이 언어 내의 추론으로 이 언어를 최소한으로 구성하는것이 존재하며, 그 의미가 곧, 어떤 연결사는 다른 연결사로 서술되는지에 대한 본질이 없고 단지 이 체계가 구현중심적인 촤고스팩이 아닌 더 추상적이고 뭘 하려는지 모르는 스팩의 성질을 띔을 증명하고 싶다.

(† 튜링 이상의 형식언어를 말한다. [내 독자탐구 내용상의 의외성정리](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/Abstract#%EC%9A%A9%EC%96%B4-%EC%A0%95%EC%9D%98)상 "단순언어"다.)

(‡ TWaML을 일상적인 용도로도 쓸것이기 때문에, 술어를 가져온다. 절대 규칙 참고. 또한 이 언어는 엄밀히 말하자면 [나의 비결절성 추성어관련 탐구 (기본어휘언어에 대해서 탐구하는 주제만 저장한 섹인임)](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/TWaMLang/%EC%B4%88%EB%8B%A8%EC%88%9C%EC%96%B8%EC%96%B4_%EB%B0%8F_%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%8F%85%EC%9E%90%ED%83%90%EA%B5%AC/)의 "기본어휘언어"에다가 단순언어†문법 기초 제공 품사(「the some predicates」)들 및 활용규정을 지정해서 푸는걸로 흡사 프레임워크와 그 프레임워크에서 제어역전 라이브러리(여기서는 기초 제공 품사의 역할)를 제공하는것과 같다.)

NOTE : 위의 해설에 대해 수정하고 전체적으로 왜 그런지 보충설명좀 할것. 아니 그게 가정되어있다고 전제하명 어쩌자는고임

그렇다. 이건 걍 제미로 단어 몇게 명명해놓고 언어라고 우기는거다. 형식언어지, 자연어나 인공어급은 아니다.

**그래서 모든 단어들은 너가 술어를 집적 가져와야한다.**

## 절대적 규칙 (이 규칙을 어기면 분화한 방언으로 취급하겠다. 내 독자표기법을 리스프 페밀리 만들고 싶지 않다)

>
> "rule 1. Predicate is Free. it's up to you.. except for 「the some predicates」"
>
> "rule 2. using TWaMLang in any logical sentense is `⊥` because it couldn't define in logical way"
> 
> "rule 3. as 「Loj System」 if logical sentence got error by predicate s.t. which not 「the some predicates」, then set that logical system as 「The Subjectal Language Logic System」"
> 

제 1 규칙에 대해 해설하자면, 수학에서 누가 술어 지정하는거 방해하지 않는것처럼 여기서도 자유이다.

그리고 제 2 규칙과 제 3 규칙은 *수학적 맥락 혹은 그 외의 맥락등지의 맥락*†에서, 논리적 일관성을 가지는 대화를 위함이다

핵심 : 사실 저 규칙들이 있다는 지점에서 「the some predicates」이외의 어휘에 애해 valid한 문법 규칙을 지정하는것이다
1. 그 근거로, 1번 규칙은 처음에 말한 초단순언어

(† 위에 명시한 의외성정리 관련 링크 참고)

쓸대없는 말이긴 한데, 나는,

이것도 나중에 구현 제작하기 전에, **형식문법 및 모델언어를 통하여 구체적으로 명세화 할 생각이다.** (형식문법을 통해 어떤 모델의 언어로 바뀐 후, 그 모델에서 돌아가는 방식이다.)

그리고 현제 그 구현은 "✅️ not yet, ☑️ processing, ☑️complete" 중 `✅️`에 해당하는 상태이다.

### 「the some predicates」 (기초어휘를 배우려면 이곳으로)

이 부분에서는 단어를 좀 리스트업 할꺼다.

언어상에서 모델론적으로 의미를 이미 정의한 술어나 상수나 함수 혹은, 문법적으로 그 의미가 규정된 문법사 (문법사라고는 했지만, lojban `cu`와는 달리, 양화사같은것이거나 괄호용 문자같은거다.)

여기서 문법사는 영어로 "「the math based literal charactor」"로 당연히 이것도 조어다. ㅋㅋㅋ

N.B. 참고로 난 연언명제를 이 체계에 넣지 않겠다고 한 적 없다. 열린 식이 나오거나 자연어를 술어로 쓰는 미친짓거리를 이 안에서 할 수 있음에 주의하자.

#### WARNING : 작성자 날먹주의보 발령 ㅋㅋ

일부러 죄다 적어야 하는 표에, 술어를 통해서 그 뜻을 얼렁뚱땅 넘어가게 모델론적으로 구현한게 있는데 날먹이다.
다 평가해서 넣어야 하는걸 내가 날먹한거다.

#### list of constant literal

 ¤ 참고로 빈칸 (Blanked Box) `□` 안의 값은 어떤 한자리 이진수 숫자도 다 체울수 있더록 허용되었다는 뜻이다.

| TWaMLang | ZFC or Modal Logic or English or Lojban |
| :---: | --- |
| øTWaMLang | the word s.t. exactly meanung [this language](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/TWaMLang) |
| øTWaML | the word which mean TalkWith a MathmaticalLanguage |
| ø□ | DoseItNumberOne(□) |
| øpa | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 1인칭 |
| øre | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 2인칭 |
| øsi | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 3인칭 |
| øvo | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 4인칭 |

참고로, "x가 주제이다"는 `x ø: øpa` 로 쓸 수 있다. 왜냐하먄, "x : 주제"라고 말하는것이기 때문이다

하핳! 이러니 Amongus없는 주제 설정이 되겠지 ㅋㅋ

추가해설 : 위 술어가 정 궁금하면 아래를 볼것. (나는 네이밍 잘했다고 보는데...)
```

DoseItNumberOne(x) : x = 1

```

#### list of predicate literal

 ¤ 참고로 빈칸 (Blanked Box) `□` 안의 값은 어떤 한자리 십육진수 숫자도 다 체울수 있더록 허용되었다는 뜻이다.

형식문법으로 작성하기 귀찮 ㅠㅠ 아서 ㅠㅠ 이랬다.

| TWaMLang | ZFC or Modal Logic or English or Lojban |
| :---: | --- |
| ñ□ | GenNormalForm(□) |
| øcoi | coi |
| øcoho | co'o |
| øwow | it was an interjection |

추가해설 : 위 함수에 대해 알고싶으면 다음을 참고할것. (솔찍히 GenNormalForm은 이름 직관적이라 봄)
```

shr(x, n) ≜ ⌊x/(2ⁿ)⌋
shl_once(x) ≜ 2x - 2⌊x⌋
shl(x, n) ≜ shl_onceⁿ(x)
idx(n, x, i) ≜ shr(shl(x, i), n - 1)

HexToBinTuple(x) ≜ (idx(4, x, 0), idx(4, x, 1), idx(4, x, 2), idx(4, x, 3))

on_off_the_x(flag_on, x) : x ∧ ((¬x) ∨ flag_on)
PredicateWhichNormalFormIs1(p, q) : p ∧ q
PredicateWhichNormalFormIs2(p, q) : p ∧ ¬q
PredicateFactorWhichNormalFormIs4(p, q) : ¬p ∧ q
PredicateFactorWhichNormalFormIs8(p, q) : ¬p ∧ ¬q

FactorWhichNormalFormIs1(r, p, q) : on_off_the_x(r, PredicateWhichNormalFormIs1(p, q))
FactorWhichNormalFormIs2(r, p, q) : on_off_the_x(r, PredicateWhichNormalFormIs2(p, q))
FactorWhichNormalFormIs4(r, p, q) : on_off_the_x(r, PredicateWhichNormalFormIs4(p, q))
FactorWhichNormalFormIs8(r, p, q) : on_off_the_x(r, PredicateWhichNormalFormIs8(p, q))

Wait(t, a, b, c, d) : FactorWhichNormalFormIs1(a, t) ∨ FactorWhichNormalFormIs2(b, t) ∨ FactorWhichNormalFormIs4(c, t) ∨ FactorWhichNormalFormIs8(d, t)

GenNormalForm(x) ≜ {t | Wait(t, HexToBinTuple(x))}

```

~~아니 미친 무려 술어를 리턴한다.~~

저게 왜 저렇게 되는지는 최하단의 "부록"에서 "투털투덜"에서 "순서쌍에 대한 투털투덜"참고. [shl, shr, idx는 중학교때 탐구해서 고등학교 1학년때 정리한 내용이고, 사실 별로 중요하지 않은거며, 그냥 툴이다](https://faraway6834.github.io/LAFTF1.1)... 중요한건 정규형식의 각 비트를 다음과 같은 구조체의 pair

```c++
typedef struct {
    struct HexFirst {
        bool l : 1;
        bool m : 1;
        bool n : 1;
        bool o : 1;
    } : 4;
    struct HexLast {
        bool l : 1;
        bool m : 1;
        bool n : 1;
        bool o : 1;
    } : 4;
} Structures_Pair;
```

Structures_Pair에 대해서

Structures_Pair타입에 Structures_Pair_type_vector = <x, y>에 대해,

first(Structures_Pair_type_vector) = Structures_Pair_type_vector.HexFirst
last(Structures_Pair_type_vector) = Structures_Pair_type_vector.HexLast에서

`S = {x | typeof(x) == typeof(Structures_Pair_type_vector.HexFirst)}`인 스칼라 S에 대해 S²이 Structures_Pair타입일때,

S 즉, 튜플(= n-열)집합 (그게 S임) 이, 저 HexToBinTuple가 내뱉는 원소의 치역이라는거.

위 내용에 대해서 말하자면,

(우연히 구조체라는 친구가 모델에서 말하는 구조체와 비슷한 구조라서 이렇게 설명할수 있기에) 누구나 이해 할 수 있으며, 코딩같이 쓰여서 이해하기도 편하다 (는점이 참 다행이라고 본다.)

~~단점은 프로그래밍 능력 있는 수학 애호가를 전재했다는 점. `<<` 퍽퍽 ~~

정규형식을 이해하기 위해서는 다음 진리표를 보자.

| p | q | | Φ(p, q) |
| :---: | :---: | --- | :---: |
| 1 | 1 | | l |
| 1 | 0 | | m |
| 0 | 1 | | n |
| 0 | 0 | | o |

이건 Φ가 논리적 연결사의 술어화로 치고 가는거다, 이러한 방식으로 형식화하는걸 논리적 연결사의 진리함수적 정의라고 한다.

Φ의 에 번호를 붙이자면 `0blnmo`이 좋지 않겠는가?
놀랍게도 Φ의 정규형식은 2³l + 2²m + 2¹n + 2⁰o란다.
아름답지 않나? (~~나만그럴지도~~)

참고로 이때, x̄를 진리값배정이라 하니, Φ(x̄)랑 비교하자면,

```
x̄ = ((1, 1), (1, 0),
     (0, 1), (0, 0))

Φ(x̄) = (l, m, n, o)
```

이다. (정주희 저 수리논리와 집합론 입문 참고 (최고의 책이라고 생각함. 내가 중학교때 입문한 책. 물론 그 이후 논리학 책중에 이병덕 교수님이 쓰신 코어논리학 보고, 정말 쉽게 설명해주셔서, 지금은 그 책을 추천목록 1순위로 꼽지 않음.) (~~에초에 내 자아가 얼마나 비대하면 추천목록이 있냐 ㅉㅉ~~))

뭔소린지 쉽게 가늠할수 있을것이라고 본다.

#### list of function

제공되는 함수가 이것밖에 없다고 안삼할만하지 않다.
사실 이거는 특성 서술아 전부이기에 유일성의 구성적 증명을 좋아하는 분들에겐 재앙이다.
그러나 지금 나는 구채적이지 않은 논리적 구조를 구성하는것에 관삼있지 구성주의에는 관심없다. 히히...
사실 문법사의 의미가 아니만 진짜 ㄹㅇ "Actually Grammer Part", 그니까 사실상 문법파트다.

크하핳

| TWaMLang | ZFC or Modal Logic or English or Lojban |
| :---: | :---: |
| la | la |
| Hint | (λx. (Hint x)) |

지금보니 la는 너무 겉멋인것 같다. 그러나 Hint보다 더 오래 애용한 발명품으로(그래봤자 함수지만) 바꾸기 골치아프다.

저기서 람다표기를 썻지만, 저건 함자를 만드는 **함자**목적임에 유의하라.

함수와 동일한 역할을 하는 이유는, 람다임애도 저것이 명백히 사상이니, 여기서는 사실 혼동을 줄이기 위해, 함수로 따로 쓰는게 나을수 있는 선택으로 볼 수 있고, 사실 걍 이건 함수의 의미로 쓴거다. 한마디로 귀차나즘.

아래에 이것이 어케 정의되는지 보이갰다, 자. 보라.

```
DecoeatingSyntax ≡ x s.t. Φ(x)
la Φ = DecoeatingSyntax
x Hint Φ = DecoeatingSyntax
```

식으로 술어가 취할 명사 지정인 la와, Hint-Operator연산 Hint를 통한 서술언 혹은 한정사 Functor `(Hint Φ)`가
1. 형용사
2. 부사
3. 한정사

의 역할을 할것이므로, 문제없다.

관형사는 그 구조가 아름답지만 한국어 특색의 문법이라(일본어에 유사 문법인 연체사도 있다. 일본인이시라도 연체사 자제해주기면 좋겠슴요.), 편협한 논리기호 패턴의 반복을 우려하니, 고려하지 않았다... 그러니...

사실은 되도록이면 관형사를 쓰지 말것을 권고한다.

사실 에초에 `(Hint (:　성상관형사 목적의 서술하는 술어)) ∘ (Hint (= N으로 수관형사 역할이니 기수사면 기수 서수사면 서수)) ∘ (Hint (: 지시관형사 용도의 논점률 명사))`의 페턴이 우리 한일 동아시아권(= 극동아권, 근데 중국은 관형사 없보네 언급이 왜 없지? 뭐... 알바 아니지만)에서만 쓰는거여셔, 저 형식에 같히는걸 권장하고 싶지 않다.

결정적으로 관형사가 매력적인 이유는 한정사인지 서술언인지가 두 속성을 다 가지므로, 모호하다는것에 있다.

#### list of 「the math based literal charactor」

여기서 문자 쓸때 벡틱은 마크다운에서 렌더링에 오류를 낼까 겁나서 내가 하남자라서 적은거임 ㅅㄱ (Tip : 벡틱은 마크다운에서 코드블럭으로 렌더링되기에, 마크다운 소스를 뜯지 않는 이상 안보이니 ㄱㅊㄱㅊ)

| TWaMLang | ZFC or Modal Logic or English or Lojban | Charactor Type | 
| :---: | --- | :---|
| `ø(` | `(` | parentheses charactorset L s.t. what written in last of this section |
| `ø;` | `,` | parentheses charactorset L s.t. what written in last of this section |
| `ø)` | `)` | parentheses charactorset L s.t. what written in last of this section |
| `ø:` | `:` | predicate or relationship or sentense or proposol declare symbol what can use to naming |
| `øA` | `∀` | Quantifier |
| `øE` | `∃` | Quantifier |

parentheses charactorset L s.t. what written in last of this section이라고 말했던 `L = {'(', ',', ')'}`

predicate or relationship or sentense or proposol declare symbol what can use to naming이란, 예시를 들면 바로 알것이다.

```

Φ(P) : x s.t. P(x)
먹다(x) : "x를 먹다"

먹는거 = Φ(먹다)

```

이계논리인거에 불만이 없을것이다 가정한다.

나는 존나 귀찮기 때문이다... 🔥 (~~귀찮은게 자랑이냐?~~)

(Tip : 콜론으로 선언하는 표기법은 내 기억이 맞다면 표준이다. 아님 ㅋ 말구 ㅋ)

#### 로마자 표기법

사실 유니코드로 표기하는게 직관적이라서 "심볼이라는 약속"의 조작에 알맞다고 봐서 저런데, 발음은 해야하니, 로마자 표기가 따로 있는 문자들이 있다.

| 고유 표기법 | SPQR(로마) Notation(자) | 로마자 명명 이유 |
| :---: | :---: | :---: |
| `ø(` | øp | p ~ q 형태의 구문이 균형감 있어서, `p ω q`가 이모티콘같고 좌우대칭으로 귀엽다는점은 누구나 저걸 보면 파악할 수 있다. 인간이 미적인 조화를 느끼는 좌우대칭은 눈에 띄므로, `p ~ q`표정도 입에 글이 달리더라되 좌우 대칭이라 괄호처럼 균형감을 줘, 읽을시에 괄호로 인식하게 도움이 되니 이랬다. 사실는 에초에 걍 보기 좋은 합리적인 이유가 본능이라면 잘만 읽여서 자주 채택하는 기법인게 이유. 에초에 øp ~ øq 형태에서 ø의 의미는 이 「the some predicates」단락 최하단에 접미사에 대한 설명들을 할때 말햇으니, 걍 실제로 볼때는 p, q에 주목되고, 그런 세세한 디테일은 잠정적으로 「the some predicates」이겠구나 싶은 정도로 변할거다. (요약하자면 좌우대칭은 눈에 잘띔을 이모티콘에서 알아냈고, 실제로 이걸 삼볼화해도 이해하기 편하다는 뜻)|
| `ø;` | øn | "me <and> you" 같이, and의미의 접속사 역할로써, 여러 단어들을 무식하게 접속사구로 묶어서 튜플화시키는 미친 역할을 하는 친구기에 `N[en]`과 발음이 유사한 `[and]`발음을 `N`으로 취급했다. 만약 구린 발음으로 "엔드"를 발음하면 충분히 그렇게 ㅋㅋㅋㅋ컼ㅋㅋㅋ 들린닼ㅋㅋㅋㅋ |
| `ø)` | øq | "øp"명명 이유 참고 |
| `ø:` | øw | **이건 에초에 단순이 비결정성 추상어에서 "기본어휘언어"를 쓸때부터 쓸수밖에 없지 않는가? 위의 링크한 탐구내용 색인에서, "초단순언어"섹션의 "초단순언어"가 사전을 명명하듯, 콜론으로 뜻을 표기하는것이 순리라는 의도다.**...... 아 이건 동문서답이구나? øw로 표기하는 이유를 쓰는칸이었지?.... 으헤헤 깜빡하? øw로 쓰는 이유는 w("word")가 연상하는 단어 word에서 따서 나온걸로, 저것이 사실상 사용되는 의미상 w가 적정하여 그렇개 부른다는거다. 에초에 술어정의구문이지만서도, 인간 언어란것은, 저런 명제에 대한 의미선언문같은 의미 대입•등호바교의 역할에서, 대부분 사전 제작용으로 쓰는게 아마도 실사용시 de-facto의 용도가 될꺼라 본다... 사실 에초에 당연해보인다. |

그냥 Roman Alphabet하면 멋이 죽어서, 로마제국ㅋㅋㅋㅋ 표기법ㅋㅋㅋ 같이 거창함 이름을 붙였다 ㅋㅋㅋㅋㅋ 앜ㅋㅋㅋ

### 감탄사에 대한 주의점

이 언어에는 품사가 절대적으로 부족한게 맞다!

에초에 술어를 서술하는 술어에서,


필요없는 문법 싫어해서 많이 뺀건 맞지만 감탄사는 좀 다르다.

여기서는 감탄사에 대한 규칙이 있다.

그 이유를 설명하겠다

감탄사는 특정 상황에서 즉각적인 감정으로 인해 즉흥적으로 조어될 수 있다(예: 갑자기 놀라서 입 밖으로 "으애엥어오어악"이라는 소리가 나오는 것). 구어에서 감탄사는 정형화된 언어보다는 감정적인 소리에 가깝다. 따라서 대부분의 감탄사가 인간이 동물적으로 낸 소리가 언어의 한 품사로 굳어진 것 마냥 취급되기에, 이 언어에서는 감탄사에 대해 제한하지 않는것이다.

또한 이러한 조어 현상을 "「즉각적 감탄현상」"이라고 명명하고 (검색을 실폐했기에 표준용어를 못찾음 ㅠㅠ) 「즉각적 감탄현상」이 가능한 감탄사의 성질이자 특징을 "「즉각감탄가능성」"이라 명명하겠다.

### 감탄사에 한정된 절대규칙 (절대적 제 0 규칙)

> 
> "rule 0. 감탄사는 「즉각감탄가능성」을 가지기에, 「즉각적 감탄현상」을 허용하고, 모든 종류의 즉각적 감탄에 대해 감탄사로 치고, 이로인해, 감탄해서 조어가 생기는것은 valid하다고 보고, 이러한 조어행위는 불가피하기에 아예 자유화하고 권장한다. 모든 감탄사는 「즉각적 감탄현상」으로 충분히 생겨날 수 있다고 보는거다. 외래어 감탄사 빼고."
>  

## Loj System과 논리 시스템 및 증명시 요구될 사항

## 부록

### 투덜투덜

누구나 아는 사실에 대해 아무생각없이 불평하며, 그 사실을 보충설명하는 문단.

#### 순서쌍에 대한 투덜투덜

Vector가 카데시안 곱인 집합에 덧셈과 상수배가 정의되어 군을 이루는 대수구조라는 대에서, 솔찍히 뇌절로 느껴지고 차라리 선형사상이라는 훌륭한 준동형사상이 더 직관적으로 다가왔다. (구현이 문제다. 사실은 직관적이긴 해도 기초론 후보감으로는 당연히 군으로 만드는게 맞다.)

그래서 망할 벡터랑 튜플의 차이가 없고, 튜플중에 덧셈과 상수배가 정의되어 군을 이루면... 아아 ㅠㅠ 그게 벡터란다 ㅠㅠ

게다가 [카데시안 곱인 집합](https://namu.wiki/w/%EC%A7%91%ED%95%A9#s-4.1), 그러니까 곱집합은 더 골때리는게 집합론에서 이 순서쌍을 쓴다. 순서쌍의 집합론적 정의에 대해선 제시한 겁집합 나무위키 문서의 순서쌍 하이퍼링크를 참고하자. 사실 곧 그 이야기를 할것이지만 말이다.

집합 A₁, ..., Aₙ이 대해, `A₁ × ... × Aₙ = {(a₁, ..., aₙ) | a₁ ∈ A₁, ..., aₙ ∈ Aₙ}` 이고

아니... 미친...

A₁ × ... × Aₙ = A₁ × (A₂ × ... × Aₙ)

이란다... 그전에 말한 곱집합 정의는 오케인데, 이건 왜?

아니, 저렇게 되면 벡터공간의 차원이나 코벡터는 어떻게 하냔 말인가?

하... 놀랍게도...

그냥 벡터는 에러가 안날것인디유... 코벡터의 경우는

<<a, b>, <c, d>>같이 되지 않는가?

아, 간단하다.

1. 실제 접근은 연산으로 한다.
2. 이건 어디까지나 구체적인 구현으로 모델일 뿐이다.
3. 이론에선 잘 정의된다. 연산이 잘 정의된다.
4. 따라서 연산이 모델에 맞게 잘 정의된다.
5. 해피~~

미친것같지 않는가?

어짜피 우리가 튜플을 접근할 때, `a₁, ..., aₙ = t`식으로 접근하면 ㅠㅠ 당연히 선택도 아주 잘 우리가 원하는대로 선택이 될것이다. ㅠㅠ

아... 그렇다면 함수에서 다룰때는 어떨다는건가.

그것보다 왜 이런 이상한 정의가 에러를 안내는가?

그렇다. 여기서 끝이 아니다. 저렇게 골때리는 구조가 되는 이유가 대박이다.

튜플의 제귀적 정의 (Recursive definition of a tuple)가 골때린다.

class of tuple what classified by arity | expression orform |
| :---: | :---: |
| 0-tuple | () (= ε) |
| 1-tuple | (x, )† |
| 2-tuple (pair, ko : 순서쌍) | (x, y) |
| n-tuple (n > 2) | (x₁, ..., xₙ) |

쌍(pair)의 경우 `(x, y) ≜ { {x}, {x, y} }` (Kuratowski-쌍 방식)

> **튜플의 귀납적 정의**
>
> "n-tuple y에 대해 (x, y)는 (n + 1)-tuple"
>

망할.... 이래서, (x, y, z) = (x, (y, z)) 가 성립한다. ‡

이것만 그랬으면, 걍 `("arity", "tuple")`꼴로 표기하는 명세를 만들어 다른 모델을 만든 후 만족했을것이다.
그러나, 골때리는게 아직 하나 남아있다,

[다변수 함수](https://namu.wiki/w/%EC%88%9C%EC%84%9C%EC%8C%8D#s-4.3)란, 변수가 여러개인 함수를 말하는데, 놀랍게도 f(x, y, z)같은 애들 말고 내적도 다변수함수다.

다변수 함수의 함수집합(함수공간)은, 무려, Func(X₁ × ... × Xₙ)이다.

이야 ㅋㅋㅋㅋ 이러면 람다 함수 f = λg. λx. g(x)에 대해서ㅣ h = f(+)에 대해, h(x, y) = h((x, y))로 먹힌다는, 이런 튜플이 입력되어, 그것이 다변수 미지수를 사스템 내에서 석정하는 방법의 모델이라는 것이다.

크하핳 미친것같아!!

요약하자면, 저렇게 다변수 함수를 만들어도, 어짜피 (x₁, ...  xₙ) = t 형식으로의 대입이니까 어짜피 잘 원하는데로 격리되서 얻어진단거잖앜 ㅠㅠㅠ 미쳐버리갰어 ㅠㅠ

따라서,

```
first(x, y) ≜ x
last(x, y) ≜ y

tuple_index(t, length, idx) ≜ firstᵖ(lastⁿ(t)) [p := {length - 1 = n}][n := idx = n]
```

가 참이되는게 튜플의 정의다 이거다.

골때리지 않는가? 이러면 다변수함수도 강제로 n-항으로 정의하고 싶어도, 굳이 내가 따로, arity가 n일때를 강제하는 구조를 만들 필요가 없어진다.

f(x, y, z) = x + y + z

에서, z가 튜플이면, x, y튜플일때 작동하고 (한마디로, 넣을 정의역이 알맞게 넣기 딱 좋다)
튜플이 인자여야 하는 상황에서도, 예외사항은 오직 z가 튜플인건 마찬가지일텐데, z가 튜플이면 튜플로 해석해도 좋다;;

와... 미친... 그냥 다 해결된다.

변수 수를 준수하지 않을시 페널티를 주고싶다면,
따로 정의되지 않게 코딩하면 되는 미친 상황......
....

(† 표기법에 대해 햇갈리지만 뭐 ㅋ 아님 말구 ㅋ)
(‡ 이 예시가 만족되는 경우, n-tuple에 대한 제귀적 정의식이 유일히 결정되기에, 저 예시가 이해하기 쉬운 예시라고 생각한다, 예시를 이해하지 못하는 사람이라면, 단순히 저기서 말하는 바는, "첫 항목 이외의 항목은 (n-1)튜플로 n-tuple의 첫 항목 이외의 항목인것이다.)

#### 술어를 정의하는 방식에 대한 아쉬움과 투덜투덜및 그래도 좋다고 주절주절하는 말

# 마치며

미친 깃헙 페이지가 내가 쓴 수학적 집합 표가법을 변수로 판단하는 바람에, 집합은 왠만하면 백틱 안의 텍스트에 있다. 이 글을 소스를 뜯어서 본다면 주의할것.

~~아니 근데 이게 CSS나 LaTeX도 아니고 HTML보다 불친절하게 시리 하.... 와 ... 미친..... 링크랑 벡틱같은 사소한것만 깨져도 빌드 • 디플롭 에러나나보노;;~~

아 시바 깃헙 미친놈들, 무슨 중괄호 두개를 명령어로 쓰냐고!!! 텍스트 스타일이 중간에 `{ { } }`면 거창하게 떨어져있는게 보기가 불편하고, 신경쓰이고 너무 넓어보이거나, 근데 넓어보여서 필요없으면 빈칸 제거하면 또 띄어져있는곤 보기않좋고 시바 걍 알관된 가독성 표기를 못쓰고, 나무위키에도 저런식으로 잘만 쓰는대 ㅠㅠ 여기서는 ㅠㅠ 연속 `{` + `{`못쓰고 `{ {`써먹게 만드는건 아오 ㅠㅠ 그냥 개인블로그인데 ㅠㅠ

그래도 스크립트 엔진까지 준비해줘서 깃헙측 너무 사랑합니다.
