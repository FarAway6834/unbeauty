# TWaMLang : Language for TWaML(TalkWith_a_MathematicalLogic)

TWaMLang에 대해 소개하겠다.

~~not TWaML-wise Argument Markup Language~~

~~취소선된 개드립은 넘기도록 하라.~~

| 성질명 | 성질값 |
| :---: | :---: |
| 유형 | 고립어 |
| 어순 | Predicate - Argument형으로 그냥 함수 모양 (Polandian Notation) |
| 서자방향 | 좌행서를 쓰되, 유니코드에서 우행서 리터럴이 나오면, 표준적인 유니코드 렌더링을 따름 |
| 문자 | 로마자 |
| 목적 | TWaML("수리논리로 말하기"의 준말임) (그니까 왜 그래야하냐고 : 의외성정리([명시된 문서는 이 링크에](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/Personal/Abstract))에서 말하는 단순의미언어중 쉬운거 제작) |
| 계통 | 영어랑 로지반에서 단어 몇게 쌔벼옴, 수리논리상 술어논리 기반, 일부 양상논리 기반 |
| 실체 | 언어인척하는 언어 확장용 형식문법, 사실상 논리학 노트 대용, (~~낚였쥬? 속았쥬?~~) |

그렇다. 이건 걍 제미로 단어 몇게 명명해놓고 언어라고 우기는거다.
그래서 모든 단어들은 너가 술어를 집적 가져와야한다.

## 절대적 규칙 (이 규칙을 어기면 분화한 방언으로 취급하겠다. 내 독자표기법을 리스프 페밀리 만들고 싶지 않다)

>
> "rule 1. Predicate is Free. it's up to you.. except for 「the some predicates」"
>
> "rule 2. using TWaMLang in any logical sentense is `⊥` because it couldn't define in logical way"
> 
> "rule 3. as 「Loj System」 if logical sentence got error by predicate s.t. which not 「the some predicates」, then set that logical system as 「The Subjectal Language Logic System」"
> 
> "

수학에서 누가 술어 지정하는거 방해하지 않는것처럼 여기서도 자유이다.

에초에 이것도 나중에 구현 제작하기 전에, **형식문법 및 모델언어를 통하여 구체적으로 명세화 할 생각이다.** (형식문법을 통해 어떤 모델의 언어로 바뀐 후, 그 모델에서 돌아가는 방식이다.)

그리고 구현은 "✅️ not yet, ☑️ processing, ☑️complete" 중 checked one's 상태이다. (~~굳이 영어로 쓴 이유는, 체크된이라고 하면 분명 구글번역기가 말썽을 피울거라고 생각하기 때문이다. 아님 말고, 근데 아니여도 고치기 귀찮음 ㅋㅋ~~)

### 「the some predicates」

언어상에서 모델론적으로 의미를 이미 정의한 술어나 상수 혹은, 문법적으로 그 의미가 규정된 문법사 (문법사라고는 했지만, lojban `cu`와는 달리, 양화사같은것이거나 괄호용 문자같은거다.)

여기서 문법사는 영어로 "「the math based literal charactor」"로 당연히 이것도 조어다. ㅋㅋㅋ

N.B. 참고로 난 연언명제를 이 체계에 넣지 않겠다고 한 적 없다. 열린 식이 나오거나 자연어를 술어로 쓰는 미친짓거리를 이 안에서 할 수 있음에 주의하자.

#### WARNING : 작성자 날먹주의보 발령 ㅋㅋ

일부러 죄다 적어야 하는 표에, 술어를 통해서 그 뜻을 얼렁뚱땅 넘어가게 모델론적으로 구현한게 있는데 날먹이다.
다 평가해서 넣어야 하는걸 내가 날먹한거다.

#### list of constant literal

참고로 빈칸 (Blanked Box) `□` 안의 값은 어떤 한자리 이진수 숫자도 다 체울수 있더록 허용되었다는 뜻이다.

| TWaMLang | ZFC or Modal Logic or English or Lojban |
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

```.

#### list of predicate literal

참고로 빈칸 (Blanked Box) `□` 안의 값은 어떤 한자리 십육진수 숫자도 다 체울수 있더록 허용되었다는 뜻이다.

형식문법으로 작성하기 귀찮 ㅠㅠ 아서 ㅠㅠ 이랬다.

| TWaMLang | ZFC or Modal Logic or English or Lojban |
| :---: | --- |
| ñ□ | GenNormalForm(□) |

위 함수에 대해 알고싶으면 다음을 참고할것. (솔찍히 GenNormalForm은 이름 직관적이라 봄)
```

shr(x, n) ≜ ⌊x/(2ⁿ)⌋
shl_once(x) ≜ 2x - 2⌊x⌋
shl(x, n) ≜ shl_onceⁿ(x)
idx(n, x, i) ≜ shr(shl(x, i), n)

HexToBinTuple(x) ≜ (shr(x, 3), shr(x, 2) - two_shr(x, 3), 
GenNormalForm(x) ≜ 

```

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