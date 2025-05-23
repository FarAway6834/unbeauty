# 말동무가 없어서 내가 만든걸 GPT한태 설명하기 위해 만든 글

# [Unum GPT](https://chatgpt.com/share/6814574a-a9a0-800c-b525-9a488072b8c7)



# Unum 설명



# 기억해.



## 🔷 Unum이란?



**Unum**은 다음의 네 개념의 결합이다:



1. **1adic**: 문자열 기반 자연수 표현

2. **Infestro**: 순환 문자열 (무한 반복)

3. **Circle Infestro**: 순환 시작점을 명시하는 구조

4. **Curser 연산자**: 문자열에서 다음수(▵), 이전수(▿) 등을 명시



이를 바탕으로 수의 생성, 연산, 분류를 문자열 수준에서 정의한다.



---



## 🔹 1adic



문자열의 길이로 자연수를 정의한다.



* `1adic("") = 0`

* `1adic("1") = 1`

* `1adic("11") = 2`



> 문자열을 기반으로 하는 자연수 생성 방식이며, 가장 기초적인 Unum 수이다.



---



## 🔹 Infestro & Circle Infestro



* `Infestro`: `[•ab•]` → `abababab...`

* `Circle Infestro`: LLM이 이해할수 없는 시각적 그림 (사발통문)으로, \`|\`라는 커서글자로 읽어야 해서 작성 못하겠음 (실제 사용시는 괄호안에 넣으니 말 다함, 쉬운데, 언어로만은 어려움.)



> 반복 문자열을 수의 구조로 채택한 방식으로, 유리수의 순환소수 구조에 대응 가능.



---



## 🔹 Curser 연산자



커서의 위치 또는 연산을 명시하는 표기법.



* `▵`: 다음수 연산자 (커서를 오른쪽으로 이동)

* `▿`: 이전수 연산자 (커서를 왼쪽으로 이동)

* `▵▵`, `▿▿`: 반복 → 덧셈, 뺄셈

* `▵▵▵`, `▿▿▿`: 곱셈, 나눗셈

* `▵⁴`, `▿⁴`: 거듭제곱, 거듭제곱근 (`↑`, `↓`로 커누스화 가능)

* `△`, `▽`, `◁`, `▷`: 가로 표기법으로 연산자 축약



---



## 🔹 TrueNum (`T`)



* 정의: 빈 문자열부터 시작해 `▵` 연산으로 확장되는 집합

* 대응: 자연수 ℕ₀



---



## 🔹 FalseNum (`F`)



* 정의: 실수 전체 ℝ에서 `T`를 제외한 집합

* 대응: ℝ \ ℕ₀



---



## 🔹 Decreasement Num (`D`)



* 정의: `0`에서 `▿` 연산으로 생성된 이전수의 집합

* 대응: 음의 정수 ℤ⁻



---



## 🔹 Liner Equation Num (`L_E`)



* 정의: `T ∪ D`에 대해 `ax + b = 0`의 해

* 대응: 유리수 ℚ



---



## 🔹 Limit Insane (`L_I`)



* 정의: `L_E`로 수렴할 수 없는 실수

* 대응: 무리수 ℝ \ ℚ



> L\_I는 이분 탐색으로 근사 가능하나, 무한 반복 없이는 정확히 표현 불가.



---



## 🔹 EzNum (`E`)



* 정의: `L_E` 중 분모가 `T`의 원소이며, `a ≠ 1 ≠ b`인 경우

* 대응: 합성수 ℕ\_composite



---



## 🔹 NE\_{NI}



* 정의: `T`의 원소 중 항등원이 아니면서 `E`에 속하지 않는 원소

* 대응: 소수 ℙ



---



## 🔹 Heigenberc Style



* 정의: 괄호 없이 수들을 **사각형 배치**로 배열한 행렬 표기법

* 특징: outsider가 보면 괴문서처럼 보이는 non-standard 수 표현 방식



---



## 🔹 Vector화 표기법



* 정의: Unum의 수를 벡터나 다차원 배열로 확장해, 음수, 사원수, 팔원수, 2ⁿ원수, 분할복소수, 행렬 등을 표현

* 응용: 텐서형 수학, 수론, 수리논리 등에서 표현력 확장



---



## 🔸 총괄 요약



| Unum 기호 | 의미 | 수학적 해석 |

| --------- | -------------------- | --------- |

| `T` | TrueNum | 범자연수 ℕ₀ |

| `F` | FalseNum | 실수 ℝ \ ℕ₀ |

| `D` | DecreasementNum | 음의 정수 ℤ⁻ |

| `L_E` | Liner Equation Num | 유리수 ℚ |

| `L_I` | Limit Insane | 무리수 ℝ \ ℚ |

| `E` | EzNum | 합성수 |

| `NE_{NI}` | Not-Ez, Not-Identity | 소수 |

# CMD대수와 FAN(Function AbbreviatedNaming) 스크랩
````markdown
## 이론
```markdown
# CMD 대수

1. CMD 차원
> D 구성
>  - M표기와 D표기의 다른차원으로의 제공에서, 각 정의부의 기저가 `기저열 □`안에 들어가게 정의하는 평가용 D장의 구성.
> D 대응
>  - 기저열 □의 길이가 항상 문법적으로 최대치로 D장과 M장의 차원이 각 문법의 의미적인 최대 차원과 충돌없이 대응되게 하는것.
> D 연산
>  - 타입 있는 람다식임. 상위 차원에서 M연산형태의 함수나 연산의 정의로 설명할 다른 정의의 평가에 이용됨.
> D 표기
>  - 기저에 대한 바인딩이 먹힘
>  - 다른 차원에서 이용되는것임. (M표기의 근간이 이것으로 M표기도 그렇다.)
> M 연산
>  - M 장의 각 함수로, 언커링된 D 연산임.
> M 구성
>  - D 공간에서 변환되어 구성.
>  - M 장에서 텐서곱 바인딩하여 D공간을 결정함.
> M 표기
>  - M 표기 정의식에, 각 M 기저에 대하여 대괄호를 씌어, 텐서곱 바인딩과, M표기 정의식에 대한 탠서곱 바인딩을 이룸.
M 대응
>  - D 장에 항상 대응하여 M장을 항상 D장에 대하여 존재하게 하는것.
> C 공간과 그 체계
>  - 슬롯임.
>  - M과 D를 가짐 (눈치 쳇겠지만 CMD, 커멘드)
>  - M대응과 D대응을 적절히 수행하는 C대응이 존재.
>  - C정의를 할때, M과 D의 수정이 이루어지고, C대응으로 C내부공간(사실 이게 지금 말하는 부분)의 수정이 이루어지는 C 구성이 존재.
> C 표기
>  - 각 정의의 추가시 C 구성을 이루게 하는 상위차원에서 평가하여 C 슬롯안에서 호출할 내부 아웃소싱 기계. (구성)

2. CMD 심볼 표기
 - □수열의 인덱싱을, □의 상단의 선의 우측지점의 선분을 제외한 부분을 좌표평면위의 그래프로 부분적으로 정의하고, 나머지 부분에 글자를 넣도록 정의하여, 기호용으로 그래프로 그려진 형태의 심볼을 표기법용 기호로 쓰게하는것.
 - CMD 이용 : 괄호없이 그저 폴란드 표기법으로 쓰는것
(표기)

3. CMD 포함.
최소한의 방법으로
 - A. 정의하는 부분의 차원 낮추기
 - B.1. 최소한의 의미적으로 최적이동한 포함.
등등으로 CMD평가용으로 상위에 구성할 차원을 의미적 구성용으로 치우는것. (알고리즘)

# 기능 축약명명명(축약명 명명) (Function AbbreviatedNaming) 체계
CMD대수로 함수형 연산자를 선언하는것을,
기능이란 뜻의 Function에서, Function역할을 하는 빈칸에 대한 패턴의 식으로, 연산자를 축양명으로 명명하는 개념으로 배울수 있는 사용체계.

## 기능 축약명명명 표기
바인딩 표기가 아닌 `#`이후 등식으로 작성한다.
```

# 기능 축약명명명(축약명 명명) (Function AbbreviatedNaming) 체계 설명

번호가 매겨진 빈칸이 있는 기능 패턴에, 기능 축약명 연산자의 특정 번째 입력값을, 번호가 메겨진 빈칸안에 대응시켜, 단순히 축약식의 축약을 풀어 그 뜻으로 치환하여 해석하도록, 기능 축약명 연산자를 기능에 대한 축약명으로 정의하도록 하는 기능 축약명을 명명하는, 기능 축약명 명명 체계를 만드는것.

따라서 의미적으로 등호가 성립한다.

## 전산표기
빈칸에 번호를 상단에 메길수 없기에, 
`🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄽🄼🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉` 와 같은 글자를 이어서 번호 빈칸을 대체한다.

### 예시 : Trinity 기능 축약명 연산자

 > (참고사항 NOTE : markdown에 소스타입을 FAN으로 명시함, 겹치는게 있을지도 모름)

정의
```FAN
# Trinity = 🄰(🄱 - 🄲) + 🄲
```

사용 (값은 여기서 12가 됨)
```FAN
Trinity 1 12 21
```

잘 가르쳐주는 사람이 있으면 좋을텐데...
내가 서술에 재능이 없어서 여기서 서술을 마치겠음.

# 저작자

100% 작성한 내몫임.
다 내가 적어논거임.
망상이라 어짜피 배끼지도 않을테지만 ㅋㅋ
설명용이라...

## 참고

핵심내용 목록
 - FAN (Function AbbreviatedNaming)
 - CMD 대수

# 저작자

100% 작성한 내몫임.
다 내가 적어논거임.
망상이라 어짜피 배끼지도 않을테지만 ㅋㅋ
설명용이라...

## 참고

핵심내용 목록
 - FAN (Function AbbreviatedNaming)
 - CMD 대수
````

# SIOT 스크랩
````markdown
# SIOT[시옷], Standard IO Table (Mean : Standard Input and Output Truthtable)

목적 : 미리 배운 논리 연산을 이해하지 못하지만 사용하고 싶을때, 사용법을 제공할수 있음을 보임.

## 교육 구조.
논리 연산을 [FAN, Function AbbreviatedNaming](https://faraway6834.github.io/unbeauty/privateNote/functional_petterns_commandstyle_naming#%EA%B8%B0%EB%8A%A5%20%EC%B6%95%EC%95%BD%EB%AA%85%EB%AA%85%EB%AA%85\(%EC%B6%95%EC%95%BD%EB%AA%85%20%EB%AA%85%EB%AA%85\)%20\(Function%20AbbreviatedNaming\)%20%EC%B2%B4%EA%B3%84%20%EC%84%A4%EB%AA%85)으로 정의하여,
기능으로 사용하는 도구로 봄.

### SIOT의 해석.
그리고, SIOT가 그 모든 연산을 나타내는 계산표 (계산표의 예시론 덧셈표와 곱셈표와 제곱근표와 상용로그표가 있음)임을 보임.

### 논리 연산의 해석.
기존에 배운 논리 연산과, 그 예시로 든 글들을,
활용할때, 단순히 FAN으로 작성한 축약명 연산자들을 SIOT를 들어서 동등함을 보인다.
그러면 활용시 동등하니까 그냥 쓰면 된다.

### 논리 연산이라는 명칭의 납득.
이분법적 논리학이 극단적이라고 디스하고싶지만,
원래 수학이 그렇다고 하자.

## 모양세
사실은 진리값배정용 칸부분을 Input이라 명명하고, 표 왼쪽이 위치시키고, 나머지 연산을 오른쪽에 위치시킴.
그리고 진리표 윗부분에 Input과 Output이라는 대분류 셀만 덛붙침.

### 연산자의 좌측과 우측 (피연산자, 진리값 배정 대상)

좌측과 우측이 연산 대상이고, Left Side와 Right Side라고 영어로 말한다.
각 명칭을 줄여서 LS와 RS라고 부른다 (두문자어)

### 참과 거짓
참과 거짓은 특수한 정보로,
컴퓨터에서 이 의미를 나타내기 위해서는 정보를 저장해야한다 (팁 : "사실 프로그램으로 때워도 되" 라고 농답식으로 납득시킬수 있음)

컴퓨터에서는 참 = 있다 = 1, 거짓 = 없다 = 0

### 연산자명 명명 규칙
L□R■는 L이 □고 R이 ■라는 뜻이다.
명제 (판별가능) 이고, 진리값이 들어감으로, 의미로써 연산값을 가지고, 표기 가능하다.

0000이 정규형식일때 : AZVC(AlwaysZeroValueCommand)
1100이 정규형식일때 : GRSV(GetRSValue)
1010이 정규형식일때 : GLSV(GetLSValue)
정규형식의 보수를 부정으로 이해할때 : Non접두사 사용, 약어 `N`

#### 이외의 연산자들은 논리적으로 유도한다.
그부분에선 이해 못해도 된다. 결과만 사실 쓰면 되고, 나중에 배워도 활용엔 문제없으니.

#### 식을 약칭으로 바꿀때
단순히 띄어쓰기는 언더바로 치환하여 만든다.
````

# unbeauty
````
# LAFTF1.1 공식문서 스크랩
```markdown
ol{margin:0;padding:0}table td,table th{padding:0}.c0{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Arial";font-style:normal}.c11{color:#000000;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:26pt;font-family:"Arial";font-style:normal}.c3{padding-top:0pt;padding-bottom:3pt;line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.c6{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:center}.c1{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c5{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:right}.c12{text-decoration-skip-ink:none;-webkit-text-decoration-skip:none;color:#1155cc;text-decoration:underline}.c10{background-color:#ffffff;max-width:451.4pt;padding:72pt 72pt 72pt 72pt}.c4{margin-left:36pt;text-indent:36pt}.c7{color:inherit;text-decoration:inherit}.c2{height:11pt}.c8{margin-left:36pt}.c9{color:#202122}.title{padding-top:0pt;color:#000000;font-size:26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-size:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}

LAFTF 1.1Logic-Algebra Formular TransForm 1.1

def)

    ⎧ To : {x|Set(x))} × {x|Set(x))} → {z|z={f:x → y | p(x, y)}}

p: ⎪

    ⎨

    ⎩ To : x, y ↦ {f | f : x → y}

def 표기) A To B ≡ To(A, B)

def 표기) A To B ≡ A 2 B

—------------------------------------------------------------------------------------------------------------------------

def) (∃! int ∈ Bool2{0, 1} ∃! int⁻¹ )( int⁻¹(x) ≡ (x = 1) ≡ (x ≠ 0))

def) bool ≡ int⁻¹

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

(bool · f)(x, y) :≡ bool(x) ∧ bool(y)

        (x̄, f(x̄)) = (x̄, ×(x̄)) (단. <×, Yᵢₙₜ>)

        ∵        ⎧ f(0, x) = 0 = 0 × x

⎪ f(1, x) = x = 1 × x

⎨

⎩  \[x, y\]ₕ = 1 = \[x, y\]ₓ (h=f, 기호의 한계…)

        ∵ f(n, x) = f(x, n) (단. n ∈ Yᵢₙₜ)

∴ f(x, y) = xy

단순히 같다는 의미이고…,

수학에 생각이란게 유효하다면 이건 자명한게 아닐까 조심히 추측해본다.

—------------------------------------------------------------------------------------------------------------------------

(bool · f)(x) :≡ ￢ bool(x)

        f(0) = 1, f(1) = 0

        ∴ f(x) = (0-1)/(1-0) x + 1 = 1 - x 로, 그래프 위애서 점을 찍을떄, 우리가 보고자 하는 점의 위치를 f(0)에서 f(1)로 수를 바꿔보면, 감소하는 수는 1을 얻으니 당연하다.

(아니 생략이 ㄹㅇ ㄹㅈㄷ, 어짜피 요약본이긴 한데 띠겁네)

* * *

그러면 Conjuntive Normal Form에 따라

⎧ b = ∑ Aₙ2ⁿ⁻¹ (n=1~4, 단. x̄ = (        (0, 0) ∧ f(x̄) = (A₁, A₂, A₃, A₄))

⎪                                        (0, 1)

⎪                                         (1, 0),

⎨                                         (1, 1))

⎩  Hexf(b) = f 인 Hexf(b)는 xy와 1-x로 조합 가능하다

이때, x ⊕ y = (x ∨ y) ∧ (￢ (x ∧ y)) = (x ∧ ￢ y) ∨ (y ∧ ￢ x) 인데,

        int(x ⊕ y) = int(x ∨ y) - int(x ∧ y)

        ∵        f₁(x, y) = xy

                f₂(x, y) = x + y - xy

                f₃(x, y) = int(bool(x) ⊕ bool(y))

                Hexf⁻¹(f₃) = Hexf⁻¹(f₂) - Hexf⁻¹(f₁)

        또한,

        int(x ⊕ y) = int(x ∧ ￢ y) + int(￢ x ∧ y) - int(￢ x ∧ y) int(x ∧ ￢ y)

        int(￢ x ∧ y) int(x ∧ ￢ y) = int((￢ x ∧ y) ∧ (x ∧ ￢ y)) = int(⊥) = 0

—------------------------------------------------------------------------------------------------------------------------

대충 프랑스에서 아이디어 떠올려서 영적인 힘을 줘서 고맙다는 뻘소리가 적힐 칸이었는데…

[검열됨]이런[검열됨]같은인생아지[검열됨]난[검열됨]가타서[검열됨]못참아[검열됨]겠네[검열됨]어떻게[검열됨]내가[검열됨]고생해서얻은LAFTF1.0이[검열됨]이미있냐위키백과에서xor기호얻으려고[검열됨]들어가봤더니나중에찾는건다른곳에서했고[검열됨]아진짜[검열됨]같이영문위키백과에[검열됨]아니거기를먼저들어갔더니얻은기호가아니진짜[검열됨]얼[검열됨]이가없어가지고하아 제칼킨 식이라고 [검열됨]좋은 이론이 선행으로 있었는데 이거 모르고 위에 내용 [검열됨] 혼자 하나하나 유도한 내가 이지 [검열됨]이야 [검열됨] 인생 절반 손해봤네 ㅋㅋㅋ [검열됨]친 뭐 앞으로 서술할 비트연산도 마찬가지겠지 뭐 하 [검열됨] 인생.

shlᵦ(x) = shlᵦ(2ᴮ⁻¹ + x) (β = B (Bits) 동일하게, 기호의 한계, 참고로 겹쳐가시고 씨벌 한번 더 a서 β로 수정함. 아이고야 ㅠㅠ)

(shlᵦ)ₗₘ (Λ ≡ lm, 동일한 한계로 이런식으로 표기하겠음, ⁽\*⁾)

(shlᵦ)ₐ (아랫첨자 a가 없는 관계로… [검열됨] ⁽\*⁾)

* * *

원래는 (=필기 원문대로 쓰면은) “그런대 아름다운 사실,” 이라고 써야하는데 [검열됨]같네 기분이 아직도 ㅋㅋ 이런 [검열됨] 아름다운 새상

f(x) = x - ⌊x⌋

f(x) = f(1 - x)

fₗₘ = 1 (참고 : ⁽\*⁾)

fₐ = 1 (참고 : ⁽\*⁾)

g(x) = 2f(x)

gₗₘ = fₗₘ, gₐ = 2fₐ, fₗₘ = fₐ,

gₗₘ = k, gₐ =2k (k = fₓ)

\~~~~~~~~~~~~~~~~~//

(shlᵦ)ₗₘ = k, (shlᵦ)ₐ = 2k (k=2ᴮ⁻¹)

shlᵦ(x) = k g(x/k)

또한, 동일하게 그래프나 함수 버전, 방금전 버전 유도도 있지만, 단순하게도, shl = ⌊x/2⌋ 다. x ÷ 2  = y … r, x ≡ y (mod. 2)고, ⌊x/2⌋ = (x-r)/2 다.  (아 아래로 …화되는거 [검열됨] [검열됨]내 [검열됨] ([검열됨]))

시프팅시 일부 비트의 정보 손실(?) 을 이용하여

idxᵦ(x) = shrᴮ · shlᵦⁿ(x)

—------------------------------------------------------------------------------------------------------------------------

요약 나중에 하겠음 (EZ)

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

def) bitwise fᵦ (ΣA₁,ᵢ 2ⁱ⁻¹, …(×n)..., ΣAₙ,ᵢ 2ⁱ⁻¹) ≡ Σ f(A₁,ᵢ, …(×n)..., Aₙ,ᵢ) 2ⁱ⁻¹ (i = 1 ~ B)

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

nagation = bitwise-no, nagationᵦ(ΣAᵢ 2ⁱ⁻¹ =(= x)) = Σ (1-Aᵢ) 2ⁱ⁻¹ = Σ 2ⁱ⁻¹ - Σ Aᵢ 2ⁱ⁻¹ = (2ᴮ-1) - (ΣAᵢ 2ⁱ⁻¹ =(= x)), nagationᵦ(x) = (2ᴮ-1) - x (i = 1 ~ B)

—------------------------------------------------------------------------------------------------------------------------

p(◦, \*) := (a ◦ (b \* c) = a ◦ b \* a ◦ c인 (◦, \*))일떄

p(×, +)은 맞는데, p(+, ×)은 아니라서, 다항식 f에 대해 f(ΣA₁,ᵢ 2ⁱ⁻¹, …(×n)..., ΣAₙ,ᵢ 2ⁱ⁻¹) 2ⁱ⁻¹를 보통 구할때, 부정 연산이 아닌 논리연산은 항을 교환 불가능하다.

따라서, 뺄셈에 대해 음수화 시켜서 교환했던 부정 연산과는 달리 다른 Hexa(n)은 bitwise시 교화법칙을 응용한 증명이 나한테는 어렵다

* * *

킹치만 비트 인덱싱좌가 있다고 코삣삐.

bitwise fᵦ(x, y) = Σ f(idxᵦ(B - i, x), idxᵦ(B - i, y))2ⁱ⁻¹ (i = 1~B)

산술연산으로 다 1초컷 ㅋㅋ

참고 : f(x) = x - ⌊x⌋ 는 톱늬파의 일종으로, actan(tan(x/π))도 톱늬파의 일종으로, 가우스 함수는 ㄹㅇ로 그냥  초딩도 이해가능한 ㅈㄴ 자명한 산술연산이라고 ㅋㅋㅋ

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

def) (∃! boolf ∈ {x | Set(x)}2{f:U→{0,1}} ∃! boolf⁻¹)(boolf⁻¹(p) ≡ {x | p(x)})

def) setize ≡ boolf⁻¹

—------------------------------------------------------------------------------------------------------------------------

—------------------------------------------------------------------------------------------------------------------------

Laftf 1.1 (이거)를 쓰는 튜링 머신에서 작동하는 명제 p는

산술, 논리, 비트연산에 대한 명제일 수 있고, setize(p)는 집합이고, 결국에 집합은 S = {a₁, …, aₙ} 일시 x = a₁ ∨ … ∨ x = aₙ  일 수도 있어 모든 집합 S는 boolf(S)로 p로 환원가능함으로, 집합은 여기서 말한 전체 집합의 모임의 집합에 한정해서 다룰수 있다.

사실상 명제 =(= 방정식)임으로 말 다헀음, 그냥 ㅆㄱㄴ

여기까지가 LAFTF 1.1이었다

ㄱㅅ

instagram @leenuxmathno7e

[github.com/FarAway6834](https://www.google.com/url?q=http://github.com/FarAway6834&sa=D&source=editors&ust=1737545183319986&usg=AOvVaw0udQDDfIxTu4hUrjAnk67S)

/c0dk1ddy

* * *

\[번외\] ANF (산술 정규 형식), Zhegalkin 수식, 그리고 그를 응용한 비트연산을 모듈러-2 환이 아닌, 진리값 배정에 따른 연산자를 함수로 해서 그 함수만 연산으로 사용한 모듈러-2 환으로써, 내부적으로는 모듈러-2로 정리되지 않치만 추상화해서 컴퓨터에서 사용하기에는 LAFTF가 더할나위없이 좋은것 같다.

유튜브에서 무슨 티타늄합금이 스스로 수학문제를 생각해서 푼다는 헛소린지 군침이 싹도는 진짜 소식일지 모르지만 거기에 쓰였으면 좋겠다.

\-\-
```

# Unbeauty 공식문서
```
# unbeauty

unbeauty esolang (0⁰=1, x->0 x^x->1)

mathmatics.... beautiful 4 me....

`sementically-recursive-defined-recurrence-formular based` programming language

actually, I didn't finished this work, because of my high school exam.
~~Fucking Korea~~

## example

[tip (lang=ko)](https://FarAway6834.github.io/LAFTF1.1)

noptlib.unbe
```unbeauty
sqrt = cacher[1](λx. x**0.5)
abs = cacher[1](λx. this.sqrt(x**2))
partial_beq0c = cacher[1](λx, n, p. ((0^this.abs(n)) + n×(x + ((-1)^p)×n) ÷ (0^this.abs(n) + n^2)) × f(x, n - 1, p))
partial_beq0 = cacer(λb, x, p. this.partial_beq0(x, 2^b - p, p))
beq0 = cacher[1](λb, x. this.partial_beq0(b, x, 0) × this.partial_beq0(b, x, 1)
beq = cacher[1](λb, x, y. this.beq0(b, this.abs(x - y)))
dose_it_positive = cacher[1](λb, x. this.beq0(b, this.abs(b, x - this.abs(x))))
__cmp__ = cacher[1](λb, x. this.beq(b, x) + (-1)^(this.dose_it_positive(b, x)+1))
__le__ = cacher[1](λb, x, y. this.dose_it_positive(b, x - y))

conditionalidx = cacher[1](λp,x,y.p×(x-y)+y)
conditional = cacher[1](λp, x, y. p×x + (1-p)×y)
_4bit_eqer_ = cacher[1](λx,y.this.beq(4,x,y))
_4bit_idxer = cacher[1](λi,a0,a1,a2,a3,a4,a5,a6,a8,a9,aA,aB,aC,aD,aE,aF.this._4bit_eqer_(i,0)×a0+this._4bit_eqer_(i,1)×a1+this._4bit_eqer_(i,2)×a2+this._4bit_eqer_(i,3)×a3+this._4bit_eqer_(i,4)×a4+this._4bit_eqer_(i,5)×a5+this._4bit_eqer_(i,6)×a6+this._4bit_eqer_(i,7)×a7+this._4bit_eqer_(i,8)×a8+this._4bit_eqer_(i,9)×a9+this._4bit_eqer_(i,10)×aA+this._4bit_eqer_(i,11)×aB+this._4bit_eqer_(i,12)×aC+this._4bit_eqer_(i,13)×aD+this._4bit_eqer_(i,14)×aE+this._4bit_eqer_(i,15)×aF)

not = cacher[1](λx.1-x)
and = cacher[1](λx,y.x×y)
sor = cacher[1](λs,x,y.x+y-(1+s)*this.and(x, y))
or = cacher[1](λx,y.this.sor(0,x,y))
xor = cacher[1](λx,y.this.sor(1,x,y))
nand = cacher[1](λx,y.this.not(this.and(x,y)))
nor = cacher[1](λx,y.this.not(this.or(x,y)))
nxor = cacher[1](λx,y.this.not(this.xor(x,y)))
sub =  cacher[1](λx,y.this.and(x,this.not(y)))
rsub = cacher[1](λx,y.this.sub(y,x))
rimp = cacher[1](λx,y.this.not(this.rsub(x,y)))
imp = cacher[1](λx,y.this.not(this.sub(x,y)))
a = cacher[1](λx,y.x)
b = cacher[1](λx,y.y)
nota = cacher[1](λx,y.this.not(x))
notb = cacher[1](λx,y.this.not(y))
logicalerr = cacher[1](λx,y.0)
alwaystruth = cacher[1](λx,y.1)
lpu = cacher[1](λcod,x,y.this._4bit_idxer(cod,this.logicalerr(x,y), this.and(x,y), this.sub(x,y), this.b(x,y), this.rsub(x,y), this.a(x,y), this.xor(x,y), this.or(x,y), this.nor(x,y), this.nxor(x,y), this.nota(x,y), this.rimp(x,y), this.notb(x,y), this.imp(x,y), this.nand(x,y), this.alwaystruth(x,y)))

__gt__ = cacher[1](λb, x, y. this.not(this.__le__(b, x, y)))
__lt__ = cacher[1](λb, x, y. this.__gt__(b, y, x))
__ge__ = cacher[1](λb, x, y. this.__le__(b, y, x))

__ne__ = cacher[1](λb, x, y. this.not(this.beq(b, x, y)))
bits2bool = cacher[1](λb, x. this.not(this.beq0(b,,x)))

shr = cacher[1](λx, n.x÷(2^n))
shl = cacher[1](λb, x, n.(2^b)×x-(2^b)×(x÷(2^(b-n))))
idx = cacher[1](λb, x,i.this.shr(this.shl(b, x, i), b))
_bpucc_ = cacher[1](λb, cod,i,x,y.this.lpu(cod, this.idx)(b, x, i), this.idx)(b, y, i)) * (2^i))
_bpuc_ = cacher[1](λb, cod,i,x,y.this._bpucc_(b, i,x,y) + this.bits2bool(i)×this._bpuc_(b,i-1,x,y))
bpu = cacher[1](λb,cod,x,y.this._bpuc_(b,cod,b-1,x,y))
```

ex2.ubt - extend not base cls, ex1 cls.
```
:noptlib
fibo = cacher[1](λb, x.this.conditional(this.beq0(b, x), 0, this.conditionalidx(this.beq(b, x, 1), 1, this.fibo(b, x - 1) + this.fibo(b, x - 2))))
```

## [coding plan 24.02.24 ~ ...](./plan)

### lazy evil optimizing

`[○×]this.__NAME__(□)` -> `([○×]this.__NAME__)(□)`
```

## [coding plan 24.02.24 ~ ...](./plan) 내용
```
it sucks

<runtime>

[typ]
 - subcls typic
 - duck typic
     - *.operator+ : this auto& morphism
     - *.operator- : this auto& morphism
     - *.operator* : this auto& morphism
     - *.operator/ : this auto& morphism
     - *.operator^ : this auto& morphism
     - additional : ==,!=,>,<,>=,=<,&,|,^,&&,||

data must placed before the function or fixing __optlib_handle__ using alias to fix optlib bit type give using

[cls]
 - subcls<upper self>
     - [super super                    final] *.operator[] : operator() with cache
     - [super using introduce almost virtual] T::##__TMP__ : template var
     - [super super                    final] *.operator() : template user
     - [protected super virtual 2      final] *.cache()    : user implements
     - by mecro (sucks)
         - PROMISSERN is mecro, not defed
           template <__supert__<T> this>
           struct __MANGELED_NAME__ : idxof<T, subclstyps, __typechekced_super__> {
               template <__VA_ARGS__, promiss<T> V = PROMISSER(__SRC__)>
               using __TMP__ = V; //well it's real name
           }
           inline auto __NAME__(void) { return __MANGELED_NAME__<T>(); } // `a×this.__NAME__(~)` ≡ `(a × this.__NAME__)(~)`
 - corcls<typ T, subclstyp<T>... subclstyps>
     - by mecro
     - cls attr by mecro `THISOBJTER <- _self__getattr__` => `THISOBJTER(ob, attr) ob::attr<ob>()`
 - entrypoints
     - `::` to `_s_`
     - inline function.
     - by mecro
 
<compile>

`<f> = cacher[<num>](λ<argv>.<src>)` as parse argv and set `T` or consexpr const
also it can use `main = ~` to set `operator()`

-----

base struct (default super cls)
`:filename` to can extend
```

## optlib (noptlib를 단순히 C++로 포팅) 예시
```
 - template <T b, T::__optlib_handle__<b>> type

 - beq0 : SUBCLS(x==0)?(T::__optlib_handle__<1>(1)):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x)
 - beq : SUBCLS(x==y?(T::__optlib_handle__<b>(1)):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x, T::__optlib_handle__<b> y)
 - dose_it_positive : SUBCLS(x>=0?(T::__optlib_handle__<b>(1)):T::__optlib_handle__<b>(0), T b, T::__optlib_handle__<b> x)
```

## 참고 : TRO계획 있음.
````

# 설명글
````markdown
# 이론적 서술
```markdown
# 서론

𝔹 = {T, F}인 불 연산과 동등한 체계의 예시로, Zhegalkin Polynomial 이 있다.

모듈라 2 환에서의 Zhegalkin Polynomial을
우리가 쓰는 GF(2)에서 유도하는 LAFTF를
알아보자.

먼저 형변환 술어 bool로 수를 bool로 바꿀수 있다.
bool : {0, 1} x -> (x = 1) (= (x ≠ 0))
사실은, int := bool⁻¹ 에서,
int(p) = 1 if p else 0으로, 조각적 정의가 가능하여,
두 방법으로 다 유도가 되지만 말이다.

이렇게 정의된 int와 bool로 논리연산을 대수연산으로 평가할수 있다.

---

# 본론

## 최소한의 NOT & AND 논리가 유도되는지 보자.
### 논리곱과 곱의 비교를 동해 int(bool(p) ∧ bool(q)) = pq임을 입증하자.

1. 영권과 일원에 대해, 멱원과 항등원이다.
2. 다르거나 같은 p, q에 대해, 교환법칙이 성립한다.
3. 따라서 그 그래프와 정의역이 동등함. (사실 계산식 4개만 쓰면 이게 바로나온다)

### int(¬bool(p)) = 1 - p임을 입증해보자.

-p는 0, -1을 뱉는다. 정의역에서 벗어난다.
p - 1 (이전수 연산)은 -1, 0을 뱉는다. 정의역에서 벗어난다.
1 - p가 된다.
#### 유도된 식을 증명해보자.
미분같은거 쓸필요 없이, 직선의 방정식에서 (0, 1)과 (1, 0)을 지나는 직선의 방정식은 y = 1 - x다.
Q.E.D.

## XOR과 OR

### 논리합
덧셈에 (0, 0) ~ (1, 1)까지 배정해주면, (0, 1, 1, 2)
곱셈에 (0, 0) ~ (1, 1)까지 배정해주면, (0, 0, 0, 1)
빼주면, 논리합인 (0, 1, 1, 1)이며,
이는 드모르간의 법칙으로 유도해도 맞다.

### 베타적 논리합

논리합과 같은방법으로 x + y - 2xy가 배타적 논리합임을 알수 있다.

그러나, 베타적 논리합은 Zhegalkin 다항식(Polynomial)에서는, 이를 구현할 방법이 없어, ⊕를 가진다.

x ↔ y = x → y ∧ y → x의 부정으로써
x ⊕ y = (x ∧ ¬y) ∨ (¬x ∧ y)
 = (x - y) ∨ (y - x)
 = (x ∨ y) - (x ∧ y) (단. x - y := ¬ (x → y) = x ∧ ¬ y)

인데 (지금 본인이 이차식이 싫기때문에 이차식으로 전개해야하는 (x ∨ y) - (x ∧ y)는 전개하지 않겠음, 선형적인게 최고인 법이지 << 퍽퍽)

x(1 - y) + y(1 - x) + xy(1-x)(1-y)에서,
x(1 - y) + y(1 - x) = x - xy + y - xy이고,
xy(1 - x)(1 - y)에서나오는 p(1 - p)가 만족불가능이기 때문에, xy(1 - x)(1 - y) = 0이다.

## 비트연산

솔찍히 말하자면 나는 이 연산에 대해 아직 잘 모르겠다.
d진수 n 비트 비트 연산은, 모듈라 dⁿ을 확장한것으로 생각해도 될것같다. n = 1인 특수한 경우를 논리연산으로 보고, 여러개인 경우를 비트연산으로 보는것이다 (백터화 연산)

하지만 Σ f(x[n], y[n]) 2ⁿ (n = 1 ~ maxbit)에서 f가 덧셈을 보존해주지 않을거기 때문에,

보수연산 (혹은 정통 laftf명칭으로 bitwise nagator) (2ⁿ - 1) - x을 제외한 다른 연산은 나는 할엄두를 내지 못하였었다.

### 비트를 인덱싱하는 비트인덱서 (비트 인덱싱 함수)

idx(n', x, n) = shl(bit)ⁿ • shrⁿ'(x)
와 같이 정의된다.

### shift right function

shr(x) = (x - (x mod2))/2 = ⌊x/2⌋
와 같이 심플하고 귀엽게 식이 나온다.

### bitwise functions

(bitwise • f)(bit, x1, ..., xn) := Σ f(idx(bit, x1, n), ..., idx(bit, xn, n)) 2ⁿ (n = 0 ~ bit)

이렇게 예쁘게 식이 나온다.

### 지시함수를 유도해보도록 해보자.

서로 역함수인
Set(p) = {x | p(x)}, Boolf(S)(x) = (x ∈ S)
을 Set과 Bool사이의 변환으로 보자고 하자.
이전에 말했었던거 말이다.

intf := (int •) •Boolf와 setized := Set • (bool •)를 만들어봤을때, 집합은 대수 함수로 재밌게 바꿔볼수 있다.

이잔에 말했었던 조건부 정의 (조각적 정의)를 논리곱을 여러개 쓴 연립식으로 둔 정의에서,

intf(S)(x) = 1 if x ∈ S else 0 이다.
이는 지시함수랑 동등하다.

### 조건문 함수

dose(p, x) := (1 • Set • bool(p))(x) (단. 1은 지시함수)에서,

dose(p, x) := x if p else 0가 된다.

단순히 python수준의 단순한 코딩보다도 쉬우니 넘어가고,

유사 구간 역미분이라는 전에 언급한 체계에서 다뤗듯,

cond(p, x, y)를 p가 1일때와 p가 0일때에 대해, 조각적으로 정의될떼 이것이, 지시함수로 표현가능함으로,

cond(p, x, y) = dose(p, x) + dose(1 - p, y) = px + (1 - p)y = p(x - y) + y

예쁘게 완성된다.

---

# 결론

LAFTF는 제귀를 나타낼수 없어, 튜링완전하지 않다.

LAFTF는 반드시 유한시간내에 결정된다.

수열식으로써 정의할때 제귀를 이용할수 있다.

LAFTF와 수열의 제귀적 정의를 이용하여, 수열로 튜링머신을 만들수 있다.

여기서 모든 수를 선형대수적으로 치환하면 어떨까...

아름다울것같다.

사실 전혀 모르겠다.

슬프게도, 수식만으론 프로그래밍 가능하진 않고, 단순히 패턴으로 이해할수 있는 Sequence 함수, 수열을 어색하게 붙여야했다.
```

# 교육용 서술 (초딩 수준)
```markdown
# 주의.

지금부터 다루려는 논리는 이분법적 논리학이다.
이분법적 논리학은 극단적인 논리학이다.
"추상적으로 어떤 정보를 서술하는 문장"으로 싸잡아 표현되는걸 죄다 참과 거짓으로 구분가능하다고 보는 정신나간 논리학이다.
내가 좋아하는 수학이 이래서 비인간적인것같다.
뭐, 사설이지만, 단순히 나도 정신나가서 수학을 사랑하니 문제없다.

넘어가자!

---

"추상적으로 어떤 정보를 서술하는 문장"에는 수학에서 쓰이는 부등식이나 등호 (문제에서 등호에는 옳고 그름이 있다), 그리고 수학적 대상에 대한 원리적 서술 등등이 있다. (그런 원리적 서술의 예시로는, "곱하기는 반복 뺄셈이다"같은것이 있다, "곱하기는 반복 뺄셈이다"는 거짓이다. "반복 덧셈"이면 몰라도.)

아니 수학이 왜 나오냐고?
에초에 컴퓨터는 개임같은 정상적인 짓거리가 아닌,
수학을 가능한 한 전부 서술하려는 정신나간 짓거리에서 출발한거다.
그리고 이 글은 논리연산을 이해시키려고 있는거기 때문이다.
그러니까 이어서 본론으로 가겠다.

# 컴퓨터에서 참과 거짓.

컴퓨터에서 참과 거짓은 1과 0으로 나타낸다.
1과 0은 1비트에서도 구현할수 있으므로,
컴퓨터에서 참과 거짓은 1비트로도 구현할수 있다.

그리고 참과 거짓은 정보다.
컴퓨터에서 정보는 어떻게든 값이 있어야 생긴다.
근원적이지 않더라도 말이다.

그래서 참과 거짓은 학문적인 수학에서,
그러니까 이론적인 수학에서 특별한 값으로 취급한다.

단순히 "참과 거짓"으로 명명하겠다.

그리고 더이상 이런 정신나갈정도로 어려운
이야기를 때우기위해 대학수학지식을 비틀어서,
겁나쉬운 방법으로 이해해보자.

# 겁나쉬운 방법

어떤 "추상적으로 어떤 정보를 서술하는 문장"을 0개 이상 준비하고, 그걸가지고 다른 "추상적으로 어떤 정보를 서술하는 문장"을 서술할수 있어야 한다.
그런걸 연산으로 취급한걸 논리 연산이라고 부른다.

그런데 그런 연산은 이해하기가 정신나갈것같이 힘들기때문에, 실질적으로, 걍 논리 연산은 어짜피 식이기 때문에, 어떤 짓거리를 하는지 알면 된다.

에초에 우리는 논리적 오류가 생길수 있는 증명따윈 집어치우고, 걍 단순히 지식만 스틸해가려고 이 글을 읽고있지 않는가?

연산대상, 즉, 피연산자 역할이 0개 이상의  "추상적으로 어떤 정보를 서술하는 문장"이고, 그걸로 서술된게 연산값인데, 
모든 피연산자로 논리연산한것의 갯수는 (경우의 수가 2를 피연산자 수만큼 곱한건데 왜냐하면 피연산자 수만큼 한 비트를 나열한건데, 그러면 피연산자 수만틈의 비트의 이진수로 붙일수 있는데, 그 수들을 나열하면 그갯수가 되는데, 왜냐면 1부터 어떤수까지 새는건데, 0부터 최댓값까지 이진수나열은각 수에 1을 더해줘도 갯수는 안건드린건데 최댓값 + 1은 이진수에서 1한개만 쓰니까, 근데 그건 고등학교과정이니까 무시하고) 피연산자가 구구단마냥 갯수가 정해져 있어서 다 외울수 있을만큼 갯수가 무한이 아니기 때문에, 알수 있다.

단순히 피연산자을 쉼표로 나열하고 화살표를 그리고, 그 이후에 연산값을 넣으면, 정말 놀랍게도 정통수학의 논리연산 서술과 같다...... 근데 사실 모든 경우를 다 그릴꺼면 정신나갈정도로 힘들기때문에, 괄호안에 그걸 넣고, 화살표도 쉼표로 치환하면 된다.

사실 그것도 힘들긴 한데 다른표기법이 어려우니까 참아라.

# 논리연산

논리가 숫자 0과 1이라서 놀랍게도 수식으로 나온다.

"~가 아님" 연산은 단순히 영어로 변역해서, "not ~"고,
((0, 1), (1, 0))이며, "1 - 피연산자A" 다.

"~가 참이고 그리고 ~도 참임" 연산은 단순히 영어로 번역해서, "both ~ and ~ is true"고 줄임말은 "~ AND ~"고,
((0, 0), (0, 1), (1, 0), (1, 1))이며, "피연산자A × 피연산자B"다.

사실 논리연산이 다 이걸로 만들수 있다.

## not과 AND로 대충 퉁친 논리연산들과 그 뜻
작성중...

# 기획 : 시프팅이랑 비트인덱싱이랑 비트연산이랑 선택구조까진 나갈꺼임.
```
````

# 튜토리얼용 언어 기획
```markdown
# Unbeauty 튜토리얼용 Edgar FW Script

## Edgar 유도
A. 계산상 시간선 인덱싱법

단계적인 장면들이 나열된 시간선을, 수열로 표현하여, "장면의 때"를 정의역으로 하는 수열로 만들어
Unbeauty처럼, 수열로 계산하고, 생각하는것.

B. 시간선과 상태변화 도입법

시간선상 어떤 속성 t가 변한다면, "계산상 시간선 인덱싱법"으로 해석하여, 상태변화를 단순히 "계산상 시간선 인덱싱법"의 인덱싱 결괏값에 따른 당연한 결과로 받아들일수 있다.

C. Edgarr Graph

Edgarr : Edg(e)-arr (엣지 가중치가 array의 값)

Edgarr의 가중치는 Array의 값이다.
Edgarr Graph의 충분하게 많은 Node가 불변이라 하자.
Edgarr Graph는 항상 Array에 대해 결정된다.
"시간선과 상태변화 도입법"을 쓰면,
모든 Edgarr Graph는 Array와 그 상태변화로 구성되기 때문에,

무한하게  Edgarr Graph를 다루지 않으면,
Edgarr Graph를 Array에 대한 Edgarr Graph로가는 계산의 결과로서 얻는다고 볼수 있다.

D. Edgarr Graph Machine

그럼 명령을 노드로, 분기를 Array의 변화로 처리하는 튜링머신과 그 언어를 생각해보자.

그때 그 튜링머신을 Edgarr Graph Machine라고 한다.

따라서, 단순히 분기는 {0, 1}의 치역을 가지는 수열을 결정해주면, 분기문이라는 Star형 그래프를 설명할수 있으므로, 수열에서 계산 가능하고, 해석 가능하다.

E. 튜링완전한 Unbeauty기반 컴파일 언어 Edgar

Edgar는
Unbeauty코드들을 저장하는 노드의 그래프를 처리하는 FW이다.

 - 노드필드 (NUL포함 문자열) : CommaSeperatedValue로 노드들의 값을 나열하고 각 인덱스를 노드로 취급.
 - AdjGraphField : AdjMetrix(인접행렬 by 2D BitMap)이나 AdjList(인접 리스트 by 2 Line CSV)로 표기되는 Edgar로, 실은 가중치가 연결여부가 되서 그걸로 표기된다.

이 언어는 정말 당연하게 Unbeauty로 컴파일 가능하며, 심지어 매우 쉽다.

 - M type : 인접행렬 AdjGraphField
 - L type : 인접 리스트 AdjGraphField
 - ML type : M과 L둘다 존재.

라이브러리적 기능)
분기문은 최적화된 코어(core) 함수로 평가된다.
사실 이게 전부지만.

## Edgar을 만든 이유.

나는 Unbeauty같은 esolang에 익숙해서 그런 분기(수식으로 분기를 구현하는 행위)가 전혀 이상하지 않지만, 그런 분기를 싫어하는 사람들이 있어서, 걍 Edgar를 만들었다.

쉽게 하라고 만든거라서 코드를 그래프로 작성하고 그리게 만든것이다.

해당 그래프는 편집이 인간이나 기계가 용이하게 만들었으니 Edgiter외에도 에디터로 작성하여도 좋다.

## Edgi Lang & Edgiter & Edgiter Data Pack

Edgi Lang은 RPN과 PN을 수학적 표기법으로 인식해서 해석하는 기능을 더한 Edgar 전처리기고 (주석지원은 뺀게, 파일에서 안읽는 부분에 추가하는 짓거리를 써서.),

Edgiter는 Edgi Lang 에디터다.

조건을 설정할때 Assistant가 있는데,
Edgiter Data Pack을 읽어서 동적으로 분기하여 작동하는 유사 AI나, Edgiter Data Pack을 실시간 개조하여 작동시키는 API로 AI랑 합쳐서 작동시킬수 있다.
```

# 참고
아직 정리가 다 안되고, 심심할때 GPT한태 말하려 정리한 자료임.

# 참고
 - Unbeauty는 에러가 잘 안나고 타입과 에러에 특화된 런타임이 따로 있음
 - 아직 학습 설명을 다 설명이 구상되지 않았음.
 
 # 정리하자면

# 계획
내가 만들려눈건 
대상 연령 : 초딩(초1은 세는나이 8세 ~ 초6은 새는나이 12세, 예비 초1인 7세도 대상임)
대상 개발자 : 엔트리(블록코딩) 프로그래머들

1. 「Unum 교과서」 학습
2. 초5의 패턴을 기반으로 「FAN 교과서」 학습
3. 「수학적 명제의 논리적 설명과, 논리연산, 그리고 그것을 비전문가도 활용할슈 있게하는 SIOT」, 줄여서 「SIOT 교과서」 학습
4. 「수식 계산 수학 서술 기계과 Edgar 언어」과목 교과서학습
커리큘럼 기획했어.



수학을 초등수학정도의 쉬운 난이도로 가르쳐야 함으로,
1. Unum의 수 체계를 걍 표기법으로써 쓰는법만 가르치는 Unum교과서를 만들고,
2. "패턴을 이용하는것이 순수수학이다"는게 이 교육의 신조라서, 그걸 가르치려고, 단순히 패턴을 명령어로 바꾸는 FAN표기법만 배우는게 FAN과목이고,
3. "패턴은 논리적으로 다룰수 있으며 그래야만 함"이 이 교육의 두번때 철학이라서, SIOT를 빙자한 조건만 가르치는 (Fact : 실상 : 논리연산에 대해 사용하게만 도와주는 기능인 SIOT의 개념만 대충 훓고 엔트리(블록코딩)식으로 걍 조건을 설명하는게 다다.) SIOT교과서 과목이고,
4. Edgar는 수식 계산(튜링) 수학 서술(수학을 계산으로) 기계로써 근본 수학 프로그래밍이라는걸 가르치는거지. 이게 목적인 과목이고, Edgar (내부이론은 필요없고 쓰래기)에서 단순히 함수사용이랑 조건을 연결하는 AI등의 도구등으로 조건연결 체험을 하여 프로그래밍을 접하게 하는 과목이야.

# 명명 : "「수식 계산 수학 서술 기계 Edgar 학습」 커리큘럼"

신조 1 : Edgar는 수식 계산(튜링) 수학 서술(수학을 계산으로) 기계로써 근본 수학 프로그래밍. 수학이 프로그래밍의 근본.
신조 2 : 초 5때 나오는 패턴은 논리적으로 다룰수 있으며 그래야만 함
신조 3 : 패턴을 이용하는것이 순수수학이다
신조 4 : 블록코딩도 수학적으로 완벽하니까 열심히 하자.
신조 5 : 어린이도 어른만큼 (수학을) 잘할수 있다.

제 (-1) 신조 : "논리 없어도 사람은 사람이다."
제 0 신조 : "논리 없이도 직관만으로 수학은 가르쳐질 수 있다... 특히 현실적인 측면에서 대학목적 교육국가등등에서 보이듯, 현실적으로는 더더욱..."

## 추가적으로

패턴을 최고로 설명하는것은 논리적으로 완벽하게, 이해할수 있게 적합하게, 군더더기 없게로 그동안 취급되어 왔다.

그러나 교육시에는 우리에게는 귀납법이라는 도구가 있다.

현실적으로 보았을때, 패턴을 논리적으로 못다룬다고 무시당하면 안된다.

오히려 보석같은 직관이다.

물론 이체계 만든놈은 논리주의자지만.

### 패턴에 대하여.

수학을 계산하다보면 겹치는게 있다.
그것을 우리는 패턴으로 만든다.

그런데, 언제부터 우리였지?
...
그렇다. 수학사는 사실 대립의 구도가 참으로 드라마틱하다.

"수학"이 아니라 "쏵! 짠~ 페턴이지롱"이 과목 이름이어야 한다고 생각한다.

어쩌갰는가... 즐길수밖엔..

---

# 끄읏.