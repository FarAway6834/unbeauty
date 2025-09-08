# TWaMLang : Language for TWaML(TalkWith_a_MathematicalLogic)

TWaMLang에 대해 소개하겠다.

~~not TWaML-wise Argument Markup Language~~

~~취소선된 개드립은 넘기도록 하라.~~

| 성질명 | 성질값 |
| :---: | :---: |
| 정체 | 단순언어†문법 Extension Framework Langauge |
| 유형 | 굳이 따지자면 고립어 겸 형식언어-like |
| 어순 | Polandian Notation이라 굳이 따지자면 VSO |
| 서자방향 | 좌행서를 쓰되, 유니코드에서 우행서 리터럴이 나오면, 표준적인 유니코드 렌더링을 따름 |
| 문자 | 로마자 |
| 목적 | TWaML("수리논리로 말하기"의 준말임)용 언어‡ |
| 계통 | 영어랑 로지반에서 단어 몇게 쌔벼옴, 수리논리상 술어논리 기반, 일부 양상논리 기반 |

(† 튜링 이상의 형식언어를 말한다. [내 독자탐구 내용상의 의외성정리](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/Abstract#%EC%9A%A9%EC%96%B4-%EC%A0%95%EC%9D%98)상 "단순언어"다.)
(‡ TWaML을 일상적인 용도로도 쓸것이기 때문에, 술어를 가져온다. 절대 규칙 참고. 또한 이 언어는 엄밀히 말하자면 [나의 초단순언어관련 탐구](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/TWaMLang/%EC%B4%88%EB%8B%A8%EC%88%9C%EC%96%B8%EC%96%B4_%EB%B0%8F_%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%8F%85%EC%9E%90%ED%83%90%EA%B5%AC/)의 "초단순 언어"에다가 단순언어†문법 Extension을 입혀서 사실상 Framework가 된거라고 볼수밖에 없다.)

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
> "

제 1 규칙에 대해 해설하자면, 수학에서 누가 술어 지정하는거 방해하지 않는것처럼 여기서도 자유이다.

그리고 제 2 규칙과 제 3 규칙은 수학적 맥락 혹은 그 외의 맥락등지의 맥락에서, 논리적 일관성을 가지는 대화를 위함이다

쓸대없는 말이긴 한데, 나는,

이것도 나중에 구현 제작하기 전에, **형식문법 및 모델언어를 통하여 구체적으로 명세화 할 생각이다.** (형식문법을 통해 어떤 모델의 언어로 바뀐 후, 그 모델에서 돌아가는 방식이다.)

그리고 구현은 "✅️ not yet, ☑️ processing, ☑️complete" 중 checked one's 상태이다.

(~~굳이 영어로 쓴 이유는, 체크된이라고 하면 분명 구글번역기가 말썽을 피울거라고 생각하기 때문이다. 아님 말고, 근데 아니여도 고치기 귀찮음 ㅋㅋ~~)

### 「the some predicates」

언어상에서 모델론적으로 의미를 이미 정의한 술어나 상수 혹은, 문법적으로 그 의미가 규정된 문법사 (문법사라고는 했지만, lojban `cu`와는 달리, 양화사같은것이거나 괄호용 문자같은거다.)

여기서 문법사는 영어로 "「the math based literal charactor」"로 당연히 이것도 조어다. ㅋㅋㅋ

N.B. 참고로 난 연언명제를 이 체계에 넣지 않겠다고 한 적 없다. 열린 식이 나오거나 자연어를 술어로 쓰는 미친짓거리를 이 안에서 할 수 있음에 주의하자.

#### WARNING : 작성자 날먹주의보 발령 ㅋㅋ

일부러 죄다 적어야 하는 표에, 술어를 통해서 그 뜻을 얼렁뚱땅 넘어가게 모델론적으로 구현한게 있는데 날먹이다.
다 평가해서 넣어야 하는걸 내가 날먹한거다.

#### list of constant literal

참고로 빈칸 (Blanked Box) `□` 안의 값은 어떤 한자리 이진수 숫자도 다 체울수 있더록 허용되었다는 뜻이다.

| øTWaMLang | ZFC or Modal Logic or English or Lojban |
| :---: | --- |
| øTWaMLang | the word s.t. exactly meanung [this language](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/TWaMLang) |
| øTWaML | the word which mean TalkWith a MathmaticalLanguage |
| ø□ | DoseItNumberOne(□) |
| øpa | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 1인칭 |
| øre | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 2인칭 |
| øsi | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 3인칭 |
| øvo | [논점률](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/%EB%AA%BD%EC%83%81/%EC%96%B8%EC%96%B4%EC%97%90_%EB%8C%80%ED%95%9C_%EB%AA%BD%EC%83%81)에서의 4인칭 |

술어가 정 궁금하면 아래를 볼것. (나는 네이밍 잘했다고 보는데...)
```

DoseItNumberOne(x) : x = 1

```

#### list of predicate literal

참고로 빈칸 (Blanked Box) `□` 안의 값은 어떤 한자리 십육진수 숫자도 다 체울수 있더록 허용되었다는 뜻이다.

형식문법으로 작성하기 귀찮 ㅠㅠ 아서 ㅠㅠ 이랬다.

| TWaMLang | ZFC or Modal Logic or English or Lojban |
| :---: | --- |
| ñ□ | GenNormalForm(□) |
| øcoi | coi |
| øcoho | co'o |
| øwow | it was an interjection |

위 함수에 대해 알고싶으면 다음을 참고할것. (솔찍히 GenNormalForm은 이름 직관적이라 봄)
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

아니 미친 무려 술어를 리턴한다.

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

S = {x | typeof(x) == typeof(Structures_Pair_type_vector.HexFirst)}인 스칼라 S에 대해 S²이 Structures_Pair타입일때,

S 즉, 튜플(= n-열)집합 (그게 S임) 이, 저 HexToBinTuple가 내뱉는 원소의 치역이라는거.

위 내용에 대해서 말하자면,

(우연히 구조체라는 친구가 모델에서 말하는 구조체와 비슷한 구조라서 이렇게 설명할수 있기에) 누구나 이해 할 수 있으며, 코딩같이 쓰여서 이해하기도 편하다 (는점이 참 다행이라고 본다.)

~~단점은 프로그래밍 능력 있는 수학 애호가를 전재했다는 점. `<<` 퍽퍽 ~~

정규형식을 이해하기 위해서는 다음 진리표를 보자.

| p | q | | Φ(p, q) |
| :---: | :---: | :---: |
| 1 | 1 | l |
| 1 | 0 | m |
| 0 | 1 | n |
| 0 | 0 | o |

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

#### list of 「the math based literal charactor」

여기서 문자 쓸때 벡틱은 마크다운에서 렌더링에 오류를 낼까 겁나서 내가 하남자라서 적은거임 ㅅㄱ (Tip : 벡틱은 마크다운에서 코드블럭으로 렌더링되기에, 마크다운 소스를 뜯지 않는 이상 안보이니 ㄱㅊㄱㅊ)

 TWaMLang | ZFC or Modal Logic or English or Lojban | Charactor Type | 
| :---: | --- | ---: |
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

나는 존나 귀찮기 때문이다.

(Tip : 콜론으로 선언하는 표기법이 내 기억이 맞다면 표준이다. 아님 ㅋ 말구 ㅋ)

### 감탄사에 대한 주의점

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

#### 순서쌍에 대한 투덜투덜

#### 술어를 정의하는 방식에 대한 아쉬움과 투덜투덜및 그대로 좋다고 주절주절하는 말
