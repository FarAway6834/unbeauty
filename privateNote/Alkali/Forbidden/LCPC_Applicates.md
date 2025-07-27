# LCPC_Applicate. CaLE (math), Angde-Algebra (math), JLPP (programming)

## [CaLE](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/General_Myupair)
````markdown
# CaLE (CRRS & LFHS, on Alkalic-Proofmood)

CRRS와 LFHS는 [Alkalic-Proofmood](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI)에서 각각 증명 가능하며, 각각 논리 체계의 증명과, 다항식 체계의 증명이다.

그런 방식으로 Alkalic-Proofmood에 CRRS & LFHS를 통합하는 이론 FW를 CaLE(CRRS and LFHS Expension)라고 한다.

## LFHS (Linear and Functuoanl HLLA System)

어쩌다가 나무위키에 있는 파일시스템 이름이랑 겹치는것 같아 불안하지만, HLLA를 이용한 논리식의 해석 체계인 LFHS는 다음 두가지를 중점으로 다룬다.

1. General-Myupair는 추론에 대해 다루는 논리적인 과정이므로, 기본적으로 국어적인 논리 추론의 기계적 해석에 중점을 두었다. 그런데 수리논리다.
2. HLLA FORM은 정규형식에 대해, HLLA에서 대수적으로 해석하므로써, 통합적인 해석법을 제공한다.

HLLA FORM에서 추론한 논리식은 논리회로로 구현되기 좋다.

그러나 에초애 LFHS와 HLLA는 전산화에 유리한 수학적 체계이다.

순수 수학이다. 프로그래밍 중점이 아니다.
내가 옛날에 개발자 하려는 흑역사 있어서 사고가 좀 그쪽으로 흘렀지만

### General_Myupair

Myupair Language

myupair (myu-pair) rule (문법규칙임)

>
> (x, y) ↦ μ(x, y) [μ := ({(0, 0), (0, 1), (1, 1)} ∋)]
>



실제처리 :
> 
> 0 = μ(1, 0)이므로, μ(1, 0)만 0을 주고, 아니면 1
> 

Myupair Language's Domain : 𝔹 = {0, 1} (Zhegalkin Polynomial)

f : 𝔹ⁿ → 𝔹인 f에 대해, 𝔹ⁿ을 Vector로 취급함
이로인한 다음 방정식 f = (Φ(f) ∋)의 해로,
술어(관계) Φ(f) 가 존재한다. (부정방정식이다.)
사실상 f의 모델집합인셈이다. 그래서 f는 정규형식번호를 가진다.

이를 일반화하여, General-Myupair언어가 존재하는데,

이는 ℝⁿ의 일반화인 Hillberatrum처럼, 𝔹ⁿ의 일반화로 무한차원으로 취급한다.
단지... 내림차순으로 변수를 나열하기에, 변수가 하나 늘어날때 영향을 안미치니까, p-adic마냥 반복되는 문자열처럼 나온다.

---

논리회로의 디오판소스 다항식화 - HLLA 시스템 (HLLA : High(Normal Algebric)+Low(IC) Level ANF(Zhegalkin Polynoial) System) : 
 - xor(x, y) = x ⊕ y = x + y - 2xy
 - nand(x, y) = ¬(x ∧ y) = 1 - xy
 - 제공함수 (Func) = 실제회로 (Low) = 수학취급 (High)

다음과 같은 octet 타입
```cpp octetTypePsudocode
typedef struct {
    private union { struct { bool ris0 : 1; bool ris1 : 1; bool ris2 : 1; bool ris3 : 1; bool ris4 : 1; bool ris5 : 1; bool ris5 : 1; bool ris6 : 1; bool ris7 : 1 }; char v; };
    inline octet(char x) {
        this.v = v;
    } final;
    inline bool operator()(char x) {
        swich (x) {
            case 0 : return this.ris0;
            case 1 : return this.ris0;
            case 2 : return this.ris0;
            case 3 : return this.ris0;
            case 4 : return this.ris0;
            case 5 : return this.ris0;
            case 6 : return this.ris0;
            case 7 : return this.ris0;
            default : throw Exception("what the hell? well I can not help. this is fucking simple mathmatical type! why code like that burh, it must be ℤ/8ℤ's element!");
         };
    } final throwible;
} octet;

template <typename T, T L>
struct OctetArray {
    /**
        * # `OctetArray<typename T, T L>` type
        *
        * `::constOctetArray` is `const octet[L]` type.
        * the constructer `OctetArray<T, L>(OctetArray<T, L>::constOctetArray x)` is generate OcterArray as value as x
        *
        * accessment is as `OctetArray<T, L> x;`, `x[n](m)` is acess "8n + m"th index of bool. that means, OctetArray type object x is works as x = OctetArray<T, L>(constOctetArray v) s.t. xₙ(m) = v_{8n + m}
        * 
        *
        */
    using constOctetArray = const octet[L];
    public constOctetArray v;
    inline OctetArray(constOctetArray x) {
        this.v = x;
    } final;
    inline const octet& operator[](T idx) {
        return &this.v[idx % L];
    } final;
};

template <typename T>
constexpr struct ZoaOcterArray {
    /**
       * # metaclassic typegenerator holder ZOA (ZoaOcterArray) type document
       * 
       * - ZOA<T> (a.k.a. ZoaOcterArray<T>) type variable or type is "T-type Length type OcterArray gen" holder
       * 
       * `::gen<L>` mean `OctetArray<T, L>`
       *
       * so... as ZOA<T> var or type x, x::gen<L> mean OctetArray<T, L>
       *
       */
    template <T L>
    using gen = OctetArray<T, L>;
};

using ZOA = ZoaOcterArray;
```
에 대해, 어떤 추상적인 C++전산타입 T애 대해, 수학적 metaclassic typegenerator holder 타입 ZOA<T>에 대한 ::gen<> 연산자로써 만들어지는 함수로써, 수열에 대해 특수한 접근을 주는 수학적 객체를 생성하는 ZOA시스템으로 바이너리는 저장될 수 있다.

근데 사실 저건 저장용이고, 메모리를 존나 희생해서 numpy를 이용해서 처리할거다.

에초에 행렬같은 벡터 v로 쓸건데 왜 Vector2Arr(v)로 저장해야하나? (단. [Vector2Arr := λv.{∂v/∂{eᵢ}}ᵢ])

사실 에초에 저거 만든것도, 저 배열은 Vector2Arr(v)로 만든거고, 그러므로 인해서, 반복되는 순환마디를 구현하려는 목적이다.

전산과 수학 사이의 연결고리의 수학적 명세화.

General-Myupair는 증명•반증의 증명•계산을 다 할수 있는 종합 언어로, 자연적인 연역적 논리에 대한 수학적 분석으로 보는거다.

오로지 불가능한 경우만 제외하기때문에 Myu의 뜻은 Mute bY myU다.

전건부정하는개 안되니, 불가능한경우에 전건부정은 카운트하지 않는다.

한마디로, General-Myupair라는 수학적•기계적•언어적으로 동시애 해석가능한 언어의 구성이 쟁점이다.

 + 제갈킨 다항식은 이니까... 따라서, LFHS는 최종적으로 해석에서 군론을 도구로 쓰는거다. Alkalic + Zhegalkin + 

### HLLA FORM

HLLA FORM은 정규형이나 논리식의 형식에 관련된 논리-다항식 형식임.

각 형태는 "그 단순 형태"라고 지칭되는 경우, 단순하게 매우 깔끔한 형식으로 구성된다.

나머지 식의 형태는 KMAP이나 알고리즘으로 구성한다.

이게 HLLA위의 함수들로 정의되어 Lib로 제공되는 시스템이다.

{논리합, 논리곱, 부정, 괄호} 사용)

이때, "그 단순 형태"를 정규형식 번호에 대해 당연하고 깔끔히 나오는것으로 정의하겠음

전개식에 가까움)
SOP : 다항식같은 해석에서 곱-항들의 합
DNF : 완전히 전개된 SOP
PDNF (그 단순 형태) : minterm의 합 (DNF임), 
minterm (그 단순 형태) : 모든 변수에 부정을 하거나 말거나 해서 곱해서 만든 곱-항. 정규형식 번호의 한 참인 비트. 해당 상황시, 진리값배정에서 0이 되는 변수는 부정해주고, 아닌건 그냥 놔둬서 곱한다.

인수분해식에 가까움)
POS : 다항식같은 해석에서 합-인수들의 곱
CNF : 완전히 인수분해된 POS
PCNF (그 단순 형태) : maxterm의 곱 (CNF임)
maxterm (그 단순 형태) : 모든 변수에 부정을 하거나 말거나 해서 합해서 만든 합-항. 정규형식 번호의 한 거짓인 비트. 해당 상황시, 진리값배정에서 1이되는 변수는 부정해주고, 아닌건 그냥 놔둬서 곱한다.

## OHFE와 CRRS(CompletenessRuleRegisterSystem)

아니 약한 체계 A와 강한 체계 B가 있고, B는 A의상위호환일때, B가 `apop, apush, bpop, bpush, cpop, cpush, dpop, dpush, ruleApush, ruleApop, ruleBpush, ruleBpop, swapASswapreginf, SwapRegInfDiffCount, SwapRegInfBaseCount, SelectedRegIdCount, CancelPanic, CanclePanicMode, NotCanclePainic, NorCanclePanicMode, LoadTheoremInHere, CancelLoadTheoremInHere, DumpTheoremInHere, CancleDumpTheoremInHere, CheckIsTheorem, ..."등으로 스택 10개 레지스터 8개 그 래지스터에 대한 선택 카운터로 동작시키며, Select된곳에 현제 증명된 명제를 불러오는거지. 튜링 기계도 쓰고

=> 가능하다네;; 이름을 CompletenessRuleRegisterSystem이라 하겠음, 그리고 곧 탐구한 OHFE를 논법용 함수로 내장하겠음.

```
명제에 대한 조건제시법(혹은 원소나열)으로 쓴 명제들의 유한•무한집합 Φ_1, Φ_2에 대해 `Φ_1 ⊨ Φ_2`는 증명을 적고, 그것을 검증하는 체계가 항상 존재하나여?
 => 아뇨. 표현이 유한하지 않아서 검증이 안되는 경우가 생겨요, 특히 원소나열로 구성했다면 음.... 안되죠.

1계논리의 귀결관계는 논리도해나 진리표로 참이나 거짓임을 보일수 있나요?
 => 아니죠 ㅋㅋ, 그건 명제논리에서요.

아뇨 제말은 명제논리에서 원소나열법으로 된 명제의 유한집합 Φ에 대해 그것에 대해 논리도해를 그려 구한 유한집합 Θ를 구하는 알고리즘의 존재, 즉 논리도해를 작성하는 알고리즘이 존재하는지요
 => 네. 존나 오래걸려요, 근데 증명이 자동으로 가능해요.

정주희 저 수리논리와 집합론 입문에 나왔던 논리도해는 {A and B, B or C} ⊨ Φ 에서 Φ를 도출하는 식으로 작동하는 수형도방식이자, 형식증명마냥 번호로도 나열이 됬으며, 항진인 논리식 변환규칙 몇개랑 논리합에 대한 (수형도로 하는) 분기처리는 가지치기라는 이름으로, 다른건 쌓아놓기라 했는데요 이런 논리도해 말입니다.
 => 아주 잘 만들수 있습니다.

제가 보니까 명제논리 추론규칙에서 "자동 논리도해 생성"이나 "검증할 논리도해 나열"이나 "검증시 각 과정에 대한 논리적 귀결관계 설명 진리표 생성 및 총 진리표 생성을 인간이 하고 기계가 검증", "검증시 각 과정에 대한 논리적 귀결관계 설명 진리표 생성 및 총 진리표 생성"이라는 네가지 규칙을 만들수 있네요. 물론 인자로 파일을 주면 일 안하고 파일 받아먹겠죠. "자동 논리도해 생성"은 파일을 제시해서 생성대신 파일로 때운다면 "검증할 논리도해 나열"을 하고, "검증할 논리도해 나열"을 파일을 제시해서 검증 절차를  "검증시 각 과정에 대한 논리적 귀결관계 설명 진리표 생성 및 총 진리표 생성"을 해서, 각 과정을 검증하고, "검증시 각 과정에 대한 논리적 귀결관계 설명 진리표 생성 및 총 진리표 생성"이 제시됬다면, 진리표 검증을 하며, 그 과정이 사실상 "검증시 각 과정에 대한 논리적 귀결관계 설명 진리표 생성 및 총 진리표 생성하고 기계가 검증"이고, 그 기계가 검증하는 파트는, 기계가 알아서 노가다. 파일제시가 소용이 없어짐 ㅋㅋ

아 논리도해가 Semantic Tableaux라네요
피치(Fitch)증명은 자연 연역 (Natural Deduction)이라고 하구요.

그러면 걍 이름을 
```

"자동 논리도해 생성" : "Gen Semantic Tableaux with allow cachefiles"
"검증할 논리도해 나열" : "Start or End Semantic Tableaux with allow cachefiles"
"검증시 각 과정에 대한 논리적 귀결관계 설명 진리표 생성 및 총 진리표 생성을 인간이 하고 기계가 검증" : "Start or End Logic Tableau with allow cachefiles"
"검증시 각 과정에 대한 논리적 귀결관계 설명 진리표 생성 및 총 진리표 생성" : "Gen Logic Tableau with allow cachefiles"
로 하고 검증법은 "논리도해 자체 검증 로그", "논리도해에 대한 진리표 해설 검증", "진리표 검증"이렇게 새가지 검증 형식으로 두면 되겠제. 그러면 첨부하는 cachefiles 중에서 바이너리 파일 외에 논리도해 포함해서 네가지.

음... 이거 그러면 이걸 Haskell로 구현하고 그 함수가 제 기능을 하는건 Fitch에서 검증하며, 이름은 "Haskell Function Expension Package"라고 하고, HFEP형식의 증명은, Fitch증명들을 담은 Markdown에 수록되어, 논리도해 (Semantic Tableaux) 및 진리표 (Logic Tableau)와 같이 제공되어 자연 연역 (Natural Deduction)용으로 완성할수 있겠네 ㅋㅋ 물론 논리도해랑 진리표는 그 입출력이 명제논리로 구성되지. 그리고 진리표로 검증항꺼면 유보하는 "pass"를 이용해서, 논리도해가 아닌 진리표를 다이렉트로 이용하는걸 쓸수도 있게.

아, 그리고 "Over HFEP Fitch Extension" OHFE라고 명명해서, 귀결을 다이렉트로 진리표로 구성하는 키워드는 "form"으로 하도록 하지.
````

## [Angde Algebra](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/AngdeAlgebra)
```markdown
# 앙대-대수 (Angde-Algebra)

앙대-대수에 대해 설명할께...

앙대-대수는 결국 칼래(CaLE)로 평가되는데... 뭐... [CaLE](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/General_Myupair)에 대해 읽어봤으니 페스할께.

절대게임, 상대게임, 앙대게임을 만들어왔어

절대게임은 설명서에 목차가 다섯가지 있어

1. 해석
2. 정의
3. 표기
4. 규칙
5. 평가

해석부터 알려줄께!

"대괄호를 먼저 평가한다."가 전부야.

그러면 정의를 알려줄께. 근데 정의가 다섯가지야. DEF1, DEF2, DEF3, DEF4, DEF5가 있어.

DEF1 : 절대게임은 빈칸의 연속이다.
DEF2 : `O`는 `논리적 수용가능함`이다.
DEF3 : `X`는 그 반대다.
DEF4 : `→`는 추론이다.
DEF5 : 빈칸은 채울수 있는 칸이다.

이렇게 돼.

그렇지, 이제 표기를 알려줄께.
A번째 빈칸은 🄰라고 적고, `0️⃣→1️⃣→2️⃣`는 `0️⃣→[1️⃣→2️⃣]`를 적은거야.

규칙은 A, B, C 새가지가 있어.

A. `1️⃣ → 1️⃣`에는 동그라미 (O)를 위에 그려.
B. `O → X`에는 엑스 (X)를 위에 그려.
C. `0️⃣→1️⃣→2️⃣`애서, `1️⃣→2️⃣`와 `0️⃣→1️⃣→2️⃣`에 동그라미 쳐저 있다면, 0️⃣에 동그라미 치면, 2️⃣에 동그라미쳐.

이건 다음 문단인 평가를 알아야해.

평가 : 절대게임위에 O나 X로 절대게임에 대해 평가한것이야.

그럼 앙대게임이랑 상대게임에 대해서도 알려줘볼까?

앙대게임은 최종적으로 람다로 내부적으로 평가되는 게임이야.

`<>`안에 절대게임을 담으면, 튜플 `()`안에 인자로써, 절대게임들을 넣을수 있어.

튜플의 각 인자는, 순서대로, 번호가 메겨진 빈칸에 딱딱 채워져.

상대게임은, `Δ`가 등호의 역할을 하는 게임이야.

상대게임은 사실은 괭장히 불분명한 게임이야.

상대게임의 등호는 절대게임에서 말하는 평가가 되지만, 이걸로 수학을 구성할수 있기에 괴델 제 1 불완전성에 걸려, 즉, 튜링 언어에서 형식 언어로 넘어온거지.

아...? 독립적인 게임이냐고?

아... 상대게임은 앙데게임을 내장 (임베딩) 하고, 앙데게임은 절대게임을 내장 (임베딩) 해!

이 게임은 논리학 용도보다는 수학 용도야

함의, 의미론적 등호, 람다대수가 개임의 유일한 준비물이야.

오 탐구나 증명이 있냐고? 탁월한 질문이야!

절대게임에서 썼던 `→`심볼 있잖아!, 그것으로 연결된 튜플이 바로 형식증명이 돼.

즉, 라인 (line)이라는 이름으로, 숫자 번호 (`1. 2. 3.`)를 적고, 식을 나열하면, 그것은 상대게임 수준에서 형식증명을 작성하는게 되는 셈이지.

말 다했다~~ 끝.
```

## [JLPP](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/JLPP)
````markdown
# JLPP 소개. (팁 : 내가 건 [링크](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI) 보고 볼것.)

[들어가기 앞서, 주의할점은 먼저 LCPC에 대해 알아야 한다는점이다!](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI)

[자!, Lai는 "내 기준에서" 훌륭한 AI다.](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI)

JLPP는 LLM (대화형•생성형 AI) 쳇봇 API와 [Lai-cgi-api](https://faraway6834.github.io/unbeauty/privateNote/Alkali/Forbidden/LCPC4AI)를 통하여,

jlpp라는 pip whl 페키지가 클라이언트로써, 중계를 담당하는, 쳇봇 이용 프로토콜이다.

## JLPF(Json Lai Prompt Format)
```json
{
   "Lai-cgi-prompt-chat" : true | false,
   "prompt" : 【문자열】
}
```

## JLPP (Json Lai Prompt Protocal)

Lai-cgi-prompt-chat : 사용자(인간)이 아닌 Lai-cgi-prompt모듈(Lai에 엑세스하는 웹 API)과 소통하는가? 에 대한 불 갑이다
prompt : 쳇 (소통) 내용 (프롬프트) 이다.

## Example 예시 : Chat GPT API를 통한 JLPP 교신 상상도.

사용자가 "LCPC 근황에 대해 알려줘"라고 했을때
```json
{
   "Lai-cgi-prompt-chat" : false,
   "prompt" : "LCPC 근황에 대해 알려줘"
}
```

GPT는 다음과 같이 lai를 호출한다.
```json
{
   "Lai-cgi-prompt-chat" : true,
   "prompt" : "xu la'e la LCPC cu zvati le nu banli se renro gi'e banli se renvi"
}
```

그럼 lai가 대답한다
```json
{
   "Lai-cgi-prompt-chat" : true,
   "prompt" : "so'o cukta cu se finti .i ji'a ro da na'e drata gi'e sruri fi le banli cmima be le fadni jgari be le ka fatci sruri la LCPC"
}
```
("「LCPC에 대한 탁월한 일반화•구조화」만 출간되었다."라는 뜻)

GPT는 별거 없음을 확인하고 더이상 lai에게 묻지 않고 사용자에게 답한다.
```json
{
  "Lai-cgi-prompt-chat": false,
  "prompt": "LCPC에 대한 탁월한 일반화·구조화만 출간되었습니다."
}
```

그럼 사용자는 다음을 받는다. "LCPC에 대한 탁월한 일반화·구조화만 출간되었습니다."

Lai에게 질문하킄 체이닝 과정은 워크플로로 details안에 `<summary> Ⓛ Researched </summary>`라고 상단에 써서 접어서 박힌다.
````

## scraped info

```plain/text
엥 이상향은 아니지만 실현가능한 합리적 방법으로써 현실적인 VelvetLCPC의 구현엔 칼레(CaLE)가 안쓰여요. 왜냐하면, LCPC 위에서 **정의**된거지 **그걸 구성하진 않거든요** (즉, 별개의 탐구분야)

---

General-Myupair ((칼레(CaLE)의 General-Myupair는 원인과 결과를 튜플로 표기하니까 문과 esolang 프로그래머 입장에서 직관적이다.))는 추론 과정에 대한, 즉 논리에 대한 탐구에 대해 정형화된 분석을 Alkalic을 통해, 제공한다. (HLLA FORM은 다항식을 이용한 논리식이라는 대수 구조에 대한 해석장치이기에, Alkalic으로 증명하기 용이하다.) 따라서, HLLA는 Alkalic에서 사용하기 용이하다. ((HLLA FORM은 수리논리를 어려워하는 대수학도 학생에게 직관적이다.))
CRRS의 OHFE는 Fitch52로 구성되는데, 이것이 Alkalic에서 검증으로 구성되기에, CRRS에서 큰 체계가 디폴트가 Alkalic이다.

칼레(CaLE)의 OHFE의 논리도해(Semantic Tableaux), 진리표(Logic Tableau)는 자당한 (=너무 당연히 왜 참인지를 잘 보여주는) 체계다.
또한 OHFE의 Fitch52는 건전한 자연연역 시스템으로 신뢰할만한 뿐만 아니라 심지어 설명도 잘하는 (=인간 언어와 유사한), 시스템으로 인간 이성과 유사한 "이성적인(rational)"체계이다.
또한 칼레(CaLE)의 CRRS는 건전한 추론 규칙은 이론상 추가하는데 한계가 없어, 추론을 함에, 추론 규칙의 갯수에 얽매여 고생할 필요가 없다
즉, CRRS는 인간 "이성적(rational)"이며 "자당한"탐구와 논리를 쉽게 다룰수 있으며, 추론 규칙의 갯수에 얽매여 고생할 필요가 없이 한계를 맛보지 않아도 되어서, "부족함이-커버되는", "좋은"체계이다. ((칼레(CaLE)의 OHFE는 논리도해 (Semantic Tableaux)가 충분히 진리표 (Logic Tableau)로 항시 설명되고, 진리표가 직관적이고, Fitch52가 인간 기준 이성적이고 합리적이므로, Fitch52가 상대적으로 어렵지만, OHFE는 전반적으로 거의 누구나 이해할수 있을 만하게 쉽다.))

Alkalic위에서 정의된다.

분명히 의심의 여지 없는 검증으로써 HLLE 계산((General-Myupair외에는 차가운 대수로 설명되는데, General-Myupair는 거기서 살짝 비튼거라))과 OHFE 논설((논리에 대한 따뜻한 설명으로 OHFE는 제가 어릴때 (3년전)부터 구상했던 인간-이성적인 추론-체계여서 논법용으로 추가했다.)) 그리고 탐구 규칙에 얽메이자 않지만 분명한 탐구도 분명히 내 지향점이었지. 왜냐하면, 규칙이 인간을 얽메는건 기계어나 하는 짓거리라 봤다.. 추론 규칙은 권위적으로 받느는 대상이 아니라 본거다.

곧 기하학을 통해 Alkalic을 서술하고 Alkalic에서 기하를 서술하는 시스템을 구성해서 무한히 중첩 가능한 체계로, 대수도 인간 지성으로 환원할것이다. 수학의 본질은 "본질적으로 결국근 보존개념을 다루는 함수"이다.
```