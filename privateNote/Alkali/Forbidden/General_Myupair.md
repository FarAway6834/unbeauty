# LFHS (Linear and Functuoanl HLLA System)

어쩌다가 나무위키에 있는 파일시스템 이름이랑 겹치는것 같아 불안하지만, HLLA를 이용한 논리식의 해석 체계인 LFHS는 다음 두가지를 중점으로 다룬다.

1. General-Myupair는 추론에 대해 다루는 논리적인 과정이므로, 기본적으로 국어적인 논리 추론의 기계적 해석에 중점을 두었다. 그런데 수리논리다.
2. HLLA FORM은 정규형식에 대해, HLLA에서 대수적으로 해석하므로써, 통합적인 해석법을 제공한다.

HLLA FORM에서 추론한 논리식은 논리회로로 구현되기 좋다.

그러나 에초애 LFHS와 HLLA는 전산화에 유리한 수학적 체계이다.

순수 수학이다. 프로그래밍 중점이 아니다.
내가 옛날에 개발자 하려는 흑역사 있어서 사고가 좀 그쪽으로 흘렀지만

## General_Myupair

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

## HLLA FORM

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