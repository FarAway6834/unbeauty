# KyuKurarin (Esotric language) (jp : きゅうくらりん)

 > 
 > * Paradime : depressive disorder (computer = antipathy world (존재하지 않는 가능새계), 컴파일러도 형식문법이라는 허상, 기계어도 CPU에서 instruction set으로 디코딩되니 가짜, 메모리 주소도 MMU에 의해 물리 주소로 변환되니 가짜, 인터프리터는 존재하지 않는 기계가, 존재하는 기계가 만족해야할 튜링 완전성응 만족하는 가짜, 튜링 머신이라는 존재는 투스택 오토마타와 동치이지만, 현실에는 스택이 존재하지 않으니, 가상의 대상과의 동치성이 생길수 있는 가능성을, 무어 기계의 I/O로 스택을 단다는 형이상학적 상상, 존재하지 않는 복합사실(비트겐슈타인 초기)•복합관념(흄 경험론)로, 현대 컴퓨팅에 대한 관점을 노래 Phony의 가사 첫 2절 `なぜ（何故）ならば総て（すべて）は嘘（うそ）で出来（でき）てうる`로 잡는다.)
 > * 만든 계기 : 재작자가 기분이 급 공허해지고 침울해짐.
 > * 주의할점 : depressive disorder가 컴퓨터를 대하는 태도는 그냥 제작자의 우울을 쏳아내려고, 형식언어이론 • 양상논리 • 비트겐슈타인의 관점 등을 가지고 비관론을 최대한 표현한 껴맞추기다. 심오한 뜻같은거 없다. 해당 철학을 한마디로 반박한다면, "사회적 약속이니까 있다고 가정하는거고, 공학적 목적 자체가, 이론전산학적인 대상을 시뮬레이션하는게 목적이다. 에초에, 컴퓨터를 튜링 머신으로 취급하는 공학에서, 유용성을 위해서, 튜링 머신으로 취급한다는 공리가 있다는 선에서 핑계대면 되는 문제지, 실제로는, 충분히 큰 N에 대해서 매모리 용량을 N으로 취급하고, 분산 컴퓨팅과 동시에 공장을 돌리면 이론상 자원의 수만큼 서버 증설도 가능하다. 에초에 공학에다가 이론을 가져오는 순간, 공학의 목적인 유용한 대상을 제조하는것에서 벗어나서, 형이상학적인 허구를 만드는거다. 비트겐슈타인 초기식으로 비판하자면, "비트겐슈타인의 사다리를 버려야하는곳(형이상학을 사용하지 않는 곳)에서, 형이상학을 사용한것이 문재"다. 에초에 컴퓨터 공학은 이론적인 부분과 현실의 괴리가 첫번째 문제로 취급되고 시작한다.
 > * hint : 이 esolang은 그냥 사실 아무의미없는 우울감을, 억지로 가짜 의미에 껴맞춘것.
 > * tip : 우울증 완치된지 3년이나 되서 "우울증 흉내"인것이다. 컨셉이다 컨셉 ㅋㅋㅋ, 그러나 절대 유쾌한 질환은 아니다.
 > * note : Kafu(可不, かふ)가 부른 KyuKurarin과 Phony에서 영감을 얻었다. 평소에 즐겨듣는 노래다.
 > * 추가적인 관전 POV : 가상 힙을 사용할때, OS로부터 매모리를 할당받기에, 사실은 페이지를 mmap으로 불러온다)의 생산성은? (+ 정적 영역의 메모리 할당을 전부 구조체 • 공용체 기반으로, 메모리 구조도 다이어그램으로 타입을 취급하도록 하고 Haskell적 OOP같이 함수로 구조체를 인자로 받을수 있는거 외에, 정적 영역은 죄다 구조체로 다뤄야하는 지옥이라, 하나의 네임스페이스 안에 모든걸 일반화 • 구조화하려는 플라톤적 강박이라는 비형식적 아이러니
 > 

````
// KyuKurarin Documents //

/* uch type */
typedef unsigned char uch;

enum vbitfield : uch {
    B0_true = 1,
    B1_true = 2,
    B2_true = 4,
    B3_true = 8,
    B4_true = 16,
    B5_true = 32,
    B6_true = 64,
    B7_true = 128,
    B0_false = ~1,
    B1_false = ~2,
    B2_false = ~4,
    B3_false = ~8,
    B4_false = ~16,
    B5_false = ~32,
    B6_false = ~64,
    B7_false = ~128
};
/**
   * uch x와 빈칸 □에 대해,
   * x[{.b□ = (true / false), ...}]를 통해서, 마스킹 인덱스를 정할수 있다.
   * {.b□ = (true / false), ...}가 의미하는 mask는 vbitfield를 에서 .b□_(true / false)들을 불러와서, bit-or (`|`)로 합쳐준거다.
   * x[{.b□ = (true / false), ...}] ^= true/false는 각각, `x ^= {.b□ = (true / false), ...}가 의미하는 마스크`와 `x ^= ~{.b□ = (true / false), ...}가 의미하는 마스크`로 정해진다. (주의 : 저기 쓰이는 true/false는 리터럴이지 bool값이 아니다. 이건 어디까지나 문법 설탕이기에, 값처럼 쓸수는 없는것이다. 다만 예외적으로, {.b□ = (true / false), ...}에서는 bool값 대신에, b□_(true/false)를 의미하는 vbitfield타입 변수를 사용 가능하다. 그 외에 true/false대입부는 어떤 변수로도 불허한다.)
   * x[{.b□ = (true / false), ...}] = true/false는 `x |= {.b□ = (true / false), ...}가 의미하는 마스크`및 `x &= ~{.b□ = (true / false), ...}가 의미하는 마스크`로 정해진다. (주의 : 저기 쓰이는 true/false는 리터럴이지 bool값이 아니다. 이건 어디까지나 문법 설탕이기에, 값처럼 쓸수는 없는것이다. 다만 예외적으로, {.b□ = (true / false), ...}에서는 bool값 대신에, b□_(true/false)를 의미하는 vbitfield타입 변수를 사용 가능하다. 그 외에 true/false대입부는 어떤 변수로도 불허한다.)
   * 그런 문법 설탕이다
   * `#pragma KyuKurarin(enable/disable, vbitfield)`가 켜져있는동안, 해당 문법 설탕이 사용 가능하다.
   * `#pragma KyuKurarin(include, vbitfield)`를 미리 선언해야, 해당 타입을 C언어로 작성된 해더로부터 가져올수 있다.
   * 이부분에 대한 pragma컴파일은 C/C++런타임 오버해드를 소모하지 않고, 그저 단순 문자열 치환 과정인것이다. 뭐... 이 언어 문법의 거의 대부분은 (PCRE + EBNF + C/C++) 조합으로만 컴파일러를 만들 작정으로 구상되었기에, 단순 치환 문법이 주류를 이룬다. 런타임은 거짓말같고 우울하다.
   */

/* uintptr_t union type */
#pragma KyuKurarin(enable, uintptr_t union)
uintptr_t union {
    uintptr_t;
    ...;
};
#pragma KyuKurarin(disable, uintptr_t union)
/**
   * 맴버변수명은 만들수 없는 union이다.
   * 맴버변수명이 곧 타입이름이라, "uintptr_t uintptr_t;"식으로만 선언 가능
   * 실제로는 pragma에서 이를 "uintptr_t _uintptr_t;"로 컴파일함. 앞에 언더바 꼴랑 하나 붙은게 전부
   * 타입 이름과 변수명이 ""uintptr_t uintptr_t;"나, "uintptr_t _uintptr_t;"꼴이 아니면, "... rejected name ..."이라면서 warning을 뱉고, "uintptr_t _uintptr_t;"꼴로 pragma가 알아서 고침 (`#pragma KyuKurarin(enable, warning_and_edit)`가 처음부터 기본값이기에, `#pragma KyuKurarin(disable, warning_and_edit)`을 해야, warning을 뱉어 알아서 고치는걸 비활성화하고 바로 에러화할수 있다.)
   * 원래 제작자는 말아 존나 많아서, 말이 없으면 괭장히 다운된거임. 비관주의인 상태인것.
   */

/* uintptr_t union type  */
#pragma KyuKurarin(enable, uintptr_t union)
uintptr_t union myUintptrtUnion x;
x.uintptr_t //x._uintptr_t와 동일하게 취급됨
x.innerType //x._innerType과 동일하게 취급됨
x._innerType //(innerType) x.uintptr_t와 동일하게 취급됨.
#pragma KyuKurarin(disable, uintptr_t union)
/**
   * 실제로는 맴버변수로 innerType이 있는지 아닌지 여부는 무관함.
   * 제약하고싶다면 `#pragma KyuKurarin(enable, strict uintptr_t union)`라고 해야함.
   * 에초에 `strict uintptr_t union`으로 선언된 uintptr_t union은 `#pragma KyuKurarin(enable, strict uintptr_t union)`가 붙도록 pragma compiler에 의해 컴파일됨.
   * 일반 union을 uintptr_t union으로 취급하고 싶다면, "union, uintptr_t union"이라는 타입이름을 써야함. `#pragma KyuKurarin(enable, union, uintptr_t union)`라고 해야하며, `union, uintptr_t union`는 사실상 uintptr_t대신에 "uintptr_t union"을 uintptr_t 대역으로 사용하는 "uintptr_t union" 문법의 변종임. 내부에는 union변수와 uintptr_t union변수가 존재해야만 함. 오직 그 두가지여야함.
   * 그렇게 되지 않는다면, "... rejected field configuration ..." 이라면서 warning을 띄우고 알아서 고침. uintptr_t union타입은 "uintptr_t union 타입명"식으로 지정해야만 함. 아니면, "... rejected typename notation ..."이라면서 warning을 띄우고 알아서 고침 (`#pragma KyuKurarin(enable, warning_and_edit)`가 처음부터 기본값이기에, `#pragma KyuKurarin(disable, warning_and_edit)`을 해야, warning을 뱉어 알아서 고치는걸 비활성화하고 바로 에러화할수 있다.)
   * "strict union, uintptr_t union"이라던가, "union, strict uintptr_t union"라던가 "strict union, strict uintptr_t union"도 엄연히 존재함.
   * 이미 코드에 주석으로 써서 알겠지만, uintptr_t union은 "x.innerType"식으로 접근하는게 죄다 "x._innerType"으로 컴파일되기에, "x._innerType"이라고 적어도 무방함. 그중에서도, "x._uintptr_t"만 유일하게, 그대로 접근이 가능하고, 나머지는 "(innerType) x._uintptr_t"으로 캐스팅하는거에 불과함. 말하고 나니까, union흉내내는게 거짓말치는것 같아서, 살짝 불쾌하고, 침울함.
   */

/* kyukurarin structure type */
#pragma KyuKurarin(enable, kyukurarin struct)
kyukurarin struct {
    ...;
};
#pragma KyuKurarin(disable, uintptr_t union)
/* it compiles to */
#pragma pack(push, 1)
struct {
    ...;
};
#pragma pop(pop)
/* by pragma compiler */
/* 진짜 이렇게 단순할수가... 허허... */

/* value holder struct */
#pragma KyuKurarin(enable, value holder struct)
template <「들어갈 내용 자유」 T, T V>
value holder struct 「이름도 자유」 {
    using 「타입 자유 명칭」 = typename T;
    constexpr static T 「값 자유 명칭」 = V;
};
#pragma KyuKurarin(disable, value holder struct)
/* it's compiles to*/
#pragma KyuKurarin(enable, value holder struct)
template <「들어갈 내용 자유」 T, T V>
value holder struct 「이름도 자유」 {
    using 「자유 명칭」 = typename T;
    constexpr static T 「자유 명칭」 = V;
};
template <typename T>
concept typeof 「해당 자유 이름」requires {
    typename T::「타입 자유 명칭」;
    requires std::same_as<delctype(T::「값 자유 명칭」), typename T::「타입 자유 명칭」>;
    requires std::same_as<「해당 자유 이름」<typename T::「타입 자유 명칭」, T::「값 자유 명칭」>, T>;
};
#pragma KyuKurarin(disable, value holder struct)
/* it compiles to */
template <「들어갈 내용 자유」 T, T V>
struct 「이름도 자유」 {
    using 「자유 명칭」 = typename T;
    constexpr static T 「자유 명칭」 = V;
};
template <typename T>
concept _typeof_「해당 자유 이름」requires {
    typename T::「타입 자유 명칭」;
    requires std::same_as<delctype(T::「값 자유 명칭」), typename T::「타입 자유 명칭」>;
    requires std::same_as<「해당 자유 이름」<typename T::「타입 자유 명칭」, T::「값 자유 명칭」>, T>;
};
/** 
  * typeof 「해당 자유 이름」형식은 띄어쓰기를 썼다고 하지만, 실제로는, _typeof_「해당 자유 이름」로 컴파일된다.
   * 유저가 템플릿에서 typeof 「해당 자유 이름」를 사용하면, pragma 컴파일러가, 이걸 잡아내서, _typeof_「해당 자유 이름」으로 바꾼다.
   * 만약 typeof 「해당 자유 이름」가 마땅히 들어가야 할 칸데,「해당 자유 이름」이 있다면, warning으로, `... why not "typeof 「해당 자유 이름」"? ...`라고 묻는다. (`#pragma KyuKurarin(disable, please check)`가 처음부터 기본값이기에, `#pragma KyuKurarin(enable, please check)`을 해야, why not을 뭍지 않고, "... checked. come here. ..."라고 에러를 내서 알려준다. 컴파일러랑 소통하는 기분이네...)
   * 참고로, 값 자유 명칭과, 타입 자유 명칭이 존재하지 않으면, "not value holder struct"라면서, 문제가 되는 라인을 출력하고 error를 냄.
   * typename T가 아니라 그냥 T로 매칭된게 나온 경우. `... intresting... why not typename T? maybe what I want not come for me yet. ...`라면서 warning을 표함.
   */

/* name space structure type */
#pragma KyuKurarin(enable, name space struct)
「템플릿 사용 가능」
name space struct {
    ::values::
        static 「inline이나 constexpr이나 그냥 뭣도 아네거나」 「함수나 변수」; //virtual이나 final불가.
        ... //같은유형 여럿
    ::templates::
        「using이나 typedef나 template struct • union이나 concept들」
         ... //같은 유형 여럿
};
/* it sompiles to */
#pragma KyuKurarin(allow, type and value)
「템플릿 사용 가능」
struct {
    struct values {
        static 「inline이나 constexpr이나 그냥 뭣도 아네거나」 「함수나 변수」; //virtual이나 final불가.
        ... //같은유형 여럿
    };
    struct templates {
        「using이나 typedef나 template struct • union이나 concept들 • namespace struct나 strict namespace struct들을 명시하면, 외부에 namespace struct가 명시되고, using으로 namespace명만 using할 뿐」
         ... //같은 유형 여럿
    };
};
#pragma KyuKurarin(disallow, type and value)
/**
 * values나 templates앞에, kyukurarin을 붙이면 kyukurarin struct로 취급해준다.
  * name space struct가 kyukurarin name space struct면, kyukurarin struct취급해준다.
  * KyuKurarin(allow, type and value)가 붙었기에, 사실상 이 기능은 KyuKurarin(allow, type and value)기능이 핵심이다.
  * KyuKurarin(allow, type and value)는 함수나 변수 선언을 values절에서 허용하는 한정사다. pragma 컴파일러가 사용 가능한 구문을 극도로 제한하는 셈이다. 그러나, 함수 내부에선 허용 안한다.
  * KyuKurarin(allow, type and value)는 using • concept • template struct & union & using & concept • typedef struct & union을 templates절에서 허용하는 한정사다. 그러나, 정작 구조체나 공용체나 using • concept 내부에선 허용 안한다.
   * namespace struct나 strict namespace struct를 하더라도, 외부에 namespace struct • strict namespace struct가 생기고, 그저, using 「namespace struct의 namespace명」= 「namespace struct의 namespace명」; 형식으로 생긴다. [1]
   * [1] 에초에 그런 경우, name space struct자체가, namespace struct이름을 「_namespace_of_『name space struct명칭』」이라는 이름의 namespace struct를 만들고, _namespace_of_접근 자체는 pragma컴파일러가 acess deny한다. 단. 원래 name space struct가 있어야 할 자리에, using 『name space struct명칭』 = 「_namespace_of_『name space struct명칭』」:: 『name space struct명칭』로 템플릿과 함깨 불러온다.
   */

/* KyuKurarin stack */
#pragma KyuKurarin(allow, stack)
static 함수
#pragma KyuKurarin(disallow, stack)
/**
   * 저 구간에서만, 이미 정의된 명시적인 타입을 통해서, 스택에 로컬 변수를 만들수 있다.
   */

/* KyuKurarin namespace struct */
#pragma KyuKurarin(enable, strict namespace struct)
namespace struct 「이름」 {
    ...
};
#pragma KyuKurarin(disable, strict namespace struct)
/* it compiles to */
namespace 「이름」 {
    struct 「이름」{
        ...
    };
};
/**
   * name space struct같은 기능들은 재공 안되며, name space struct를 인자로 가질수 없다. 오로지 값, 타입, 비트필드만이다.
   * strict namespace struct가 아닌 namespace struct의 경우, 템플릿이 있는 name space struct를 인자로 가질수 있다.
   * 사실 이것도 어디까지나 namespace일 뿐이다.
   * 정작 「이름」이 `「이름」::「이름」`으로 컴파일되기에, `「이름」::「이름」`도 허용된다.
   */

/* TRO decorator */
#pragma KyuKurarin(allow, TRO)
@TRO struct  함수명<루프 언롤링 횟수>{
    inline 「타입명칭」 operator()(「타입명칭」 data) {
        ...
    }
    inline bool operator()(「타입명칭」 data) {
        ...
    }

    inline void operator()(「타입명칭」 data) {
        ...
    }
}
#pragma KyuKurarin(allow, TRO)
/**
   * 단순히, operator()의 코드가 루프 언롤링 횟수만큼 반복됨. return대신에, ret이라는 변수에, 미리 입출력 인자를 할당하기도 함.
   * C++최적화가 아닌 C수준으로 while/if화함 (static inline 함수인건 뭐 어쩔수 없고. 그나마, 템플릿을 사용 안하도록 프로그래밍을 잘 해주면, pragma 컴파일러가, struct내 static함수 • static변수나 namespace를 자동으로 C용으로 맹글링후 컴파일하는 좋은 기능이 default임.
   * TRO대신에 templateTRO라고 명시해야지, 템플릿 기반 TRO를 갈김
   */

NOTE : 참고사항으로, 앞서 명시한 형식의 타입 정의 구문만이 유일하게 허용된다. 모든 대상은 namespace struct내부의 name space struct 내부에 있는 디자인이 허용되며, KyuKurarin으로 정의한 대상은 KyuKurarin(use, ...)라는 pragma로 use모드여야 사용 가능하다
NOTE : 허용되지 않거나, 에러 메세지를 만들기 귀찮은거 다 싸잡아서, "... rejected form ..."이라는 error로 에러 메세지를 낸다.
NOTE :  `#pragma KyuKurarin(disable, please check)`가 처음부터 기본값이기에, `#pragma KyuKurarin(enable, please check)`을 해야, why not을 뭍지 않고, "... checked. come here. ..."라고 에러를 내서 알려준다. 컴파일러랑 소통하는 기분이네...
NOTE : `#pragma KyuKurarin(enable, warning_and_edit)`가 처음부터 기본값이기에, `#pragma KyuKurarin(disable, warning_and_edit)`을 해야, warning을 뱉어 알아서 고치는걸 비활성화하고 바로 에러화할수 있다.
NOTE : TRO데코레이터 이외에 제귀를 사용하면, "see there, it use requation without TRO. well... I feel indifferent about the idea of dying in an accident"라면서 warning을 갈김. 이건 `#pragma KyuKurarin(disable, don't suicide)` 및 `#pragma KyuKurarin(disable, accident is not die)`가 기본 옵션이라 그럼. `#pragma KyuKurarin(enable, accident is not die)`시 경고 자체를 출력을 안하고, `#pragma KyuKurarin(enable, don't suicide)`시, 경고 대신 오류를 씀. 동시에 사용하면 `don't suicide`가 우선순위가 먼저임.
NOTE : templateTRO의 경우, 아래 의사 코드와 유사하게 동작함
```
#include <concepts>
#include <type_traits>
#include <cstddef>

template <typename T, size_t L>
struct Tarr {
    using ptr = Tarr*;
    using const_ptr = const Tarr*;
    union {
        T V[L];
        #pragma pack(push, 1) 
        struct {
            T first;
            Tarr<T, L - 1> after;
        };
        struct {
            Tarr<T, L - 1> least;
            T last;
        };
        #pragma pack(pop)
    };
    
    Tarr() = default;
    
    inline auto& operator[](this auto&& self, size_t idx) {
        return self.V[idx];
    }
};

template <typename T>
struct Tarr<T, 1> {
    using ptr = Tarr*;
    using const_ptr = const Tarr*;
    T V[1];
    
    Tarr() = default;
    
    inline auto& operator[](this auto&& self, size_t idx) {
        return self.V[idx];
    }
};

template <typename T, size_t Rank, Tarr<size_t, Rank>::const_ptr Dims>;

template <typename T>
concept SelfmapicInterface = requires {
    /* one kind of functional interface */
    typename T::generic;
    requires requires(typename T::generic v) {
        { T::function(v) } ->  std::same_as<typename T::generic>;
    };
};

template <

template <SelfmapicInterface T>
concept TRONamespace = requires(typename T::generic v) {
    { T::predicate(v) } -> std::same_as<bool>;
};

typedef struct {} TROFunction;

template <TRONamespace T>
struct TRONamespace2TROFunction : TROFunction {
    using generic = typename T::generic;
    static inline typename generic TROFunction(typename generic x) {
        for (bool p = T::predicate(x); p; p = T::predicate(x)) x = T::function(x);
    }
};

template <bool isSIMD, SelfmapicInterface T, size_t N>
struct IteratedFunction {
    using generic = typename T::generic;
    using PreviousTerm = typename IteratedFunction<T, N - 1>;
    static inline typename generic function(typename generic x) {
        x = PreviousTerm::function(x);
        return T::function(x);
    }
    static inline void SIMD_function(typename generic x) {
        PreviousTerm::SIMD_function(x);
        x = T::function(x);
    }
};

template <SelfmapicInterface T>
struct IteratedFunction<T, 0> {
    using generic = typename T::generic;
    static inline typename generic function(typename generic x) {
        return x;
    }
};

template <SelfmapicInterface T>
struct IteratedFunction<T, 1> {
    using generic = typename T::generic;
    using PreviousTerm = typename IteratedFunction<T, 0>;
    static inline typename generic function(typename generic x) {
        return T::function(x);
    }
};

template <TRONamespace T, size_t unroll>
struct unrolledTRONamespace {
    using generic = typename T::generic;
    using unrolledTerm = typename IteratedFunction<T, unroll>;
    static inline bool predicate(typename generic x) {
        return T::predicate(x);
    }
    static inline typename generic function(typename generic x) {
        return unrolledTerm::function(x);
    }
};

template <TRONamespace T>
struct unrolledTRONamespace<T, 0> {
    using generic = typename T::generic;
    using unrolledTerm = typename IteratedFunction<T, 1>;
    static inline bool predicate(typename generic x) {
        return T::predicate(x);
    }
    static inline typename generic function(typename generic x) {
        return x;
    }
};

template <TRONamespace T>
struct unrolledTRONamespace<T, 1> {
    using generic = typename T::generic;
    using unrolledTerm = typename IteratedFunction<T, 1>;
    static inline bool predicate(typename generic x) {
        return T::predicate(x);
    }
    static inline typename generic function(typename generic x) {
        return T::function(x);
    }
};

template <TRONamespace T, size_t unroll>
struct unrolledTRONamespace2TROFunction : TRONamespace2TROFunction<unrolledTRONamespace<T, unroll>> {};

template <TRONamespace T>
struct unrolledTRONamespace2TROFunction<T, 0> : TROFunction {
    using generic = typename T::generic;
    static inline typename generic TROFunction(typename generic x) {
        return x;
    }
};

template <TRONamespace T>
struct unrolledTRONamespace2TROFunction<T, 1> : TROFunction {
    using generic = typename T::generic;
    static inline typename generic TROFunction(typename generic x) {
        if (T::predicate(x)) return T::function(x);
        return x;
    }
};

/* 어디까지나 의사코드일 뿐임 */
```
````

## KyuKurarin uso (うそ) : 거짓된 런타임을 제공하는 유일한 편의기능. (명목상 포지션 = 극사실주의 기법 중, 현실적인 부분을 여러군대 그리다가, 비현실적인 부분(가짜 힙)을 추가하는 기법)

 > 
 > 사용 방법은 `#pragma KyuKurarin(include, KyuKurarin うそ)`를 쓰면, SlicibleTarr의 사용이 허가되는 방식이다.
 > 
 > SlicibleTarrAlloc<T, L>의 페이지를 생성했다면; SlicibleTarrAlloc<T, L>::SlicibleTarr<L>로, SlicibleTarr을 다룰수 있고, SlicibleTarr은 인덱싱과, SlicibleTarr.sliceafter,  SlicibleTarr.split, SlicibleTarr.slicebefore, SlicibleTarr.primitive_slicebystep SlicibleTarr.slicebystep, SlicibleTarr.applyGPUShuffle등을 사용 가능하다. SlicibleTarr.primitive_slicebystep SlicibleTarr.applyGPUShuffle로 구현된다.
 > 
 > SlicibleTarr.slicebystep(k)은, SlicibleTarr.primitive_slicebystep(k)[:len(x)//k]인 것인 셈이고, 
 > 
 > SlicibleTarr.primitive_slicebystep는
 > 
 > x[:len(x)//k]에 x[::k]의 인덱스를 몰아넣고, x[len(x)//k:]에 나머지를 몰아넣는다.
 > 
 > 예컨데, {0, 1, 2, 3, 4, 5}[::3]를 하고싶을땐,
 > 
 > {0, 3, 1, 2, 4, 5}인 미리 생성된 GPUShuffle을 SlicibleTarr.applyGPUShuffle을 통해 이용하여, virtual MMU수준에서 조작한다.
 > 
 > SlicibleTarr.split(L)을 하면, L기준 first와 last에 대해, ret이
 > ``` 
 > struct {
 >     union {
 >         delctyp(self)* old;
 >         delctype(self.first)* first;
 >     };
 >    delctype(self.last)* last;
 > } ret = {.old = self, .last = (delctype(self.last)*) malloc(sizeof(delctype(self.last)))};
 > ```
 > 이면
 > `addrswap((size_t) &ret.old->last, (size_t) &ret.last);` 이후 (**fact : addrswap이 커널에 없어서, 가상 메모리를 만들기로 마음먹었다. 이 시점에서, KyuKurarin 언어는 malloc • calloc • realloc • free • new • delete가 이미 컴파일러 레벨에서 튜닝되어있다.**)
 > 
 > `ret.first = (delctype(self.first)*) realloc(ret.old, sizeof(delctype(self.first)));`을 통하여 완성하면,
 > **split 완료**
 > 
 > NOTE : 인덱싱은, split결과중에 하나를 delete하고 삭제하지 않은 하나를 반환하는거다.
 > 
 > **WARNING : 원래는 MMU를 OS가 아닌 프로그램이 직접 제어하길 원했다. 아무리 공학용 설비라고 하지만, 왜 컴퓨터의 주인이 프로그램을 제작해서 돌리는 유저가 아닌 커널인가? kernel이 컴퓨터를 지배한다는것은 이론전산학적 관점에서는 자원 관리 문제의 해법일뿐, 필연도 아니고, 그냥 한가지 공학적 관점을 전체 프로그래밍 이론에게 강요하는 권위적 독제다. 관습적으로 우리가 kernel을 당연시하는건, 자연어에 의존해, 수학(이론전산학을 포함하는 학문)이라는 형식언어에서, 비형식적인 감정인 "권위"를 들이대는, 오류를 저질렀다고 느낀다. 그냥 kernel에게서, MMU제어권을 조심히 할당해서, kernel이 허용하는 범위 네에서, 줏 조작 요청을 보내거나, 스왑 요청을 보낼때, 해당 조작이나 스왑이, 권한 • 스코프 • 위치 등 여러 측면에서 안전하면 허용하면 되지 않는가? 진짜 너무한다. 그래서 가상화한 버전으로나마 만들어봤다.**
 >
 > 아래 쓰여있는 SlicibleTarr(아직 안썼지만)을 통해, 자동 new • delete가 되는 heap을, 가상 메모리 풀 페이지를 할당하는 경우에 한해서 허용한다.
 > 
 > OS가 우리를 속이는 장치로써, heap도 비관적으로 우울하다...
 > 

```
template <typename T, T V>
struct hold {
    using type = typename T;
    constexpr static T value = V;
};

template <typename T>
concept holdTyp = requires {
    typename T::type;
    requires std::same_as<decltype(T::value), typename T::type>;
    requires std::same_as<hold<typename T::type, T::value>, T>;
};

template <typename T, holdTyp L>
struct Tarr {
    public:
        using type = typename T;
        using length = typename L;
        using indexType = Tarr<length::type, length>;
        #pragma pack(push, 1)
        struct {
            T value[length::value];
        };
        #pragma pack(pop)
        template <holdTyp N>
        struct acess requires((std::same_as<typename L::type, typename N::type>) && (L::value > N::value)) {
            public:
                using type = type;
                using length = length;
                using indexType = indexType;
                using firstLength = typename N;
                using lastLength = typename hold<length::type, (L::value - N::value)>;
                union {
                    #pragma pack(push, 1)
                    struct {
                        Tarr value;
                    };
                    #pragma pack(pop)
                    #pragma pack(push, 1)
                    struct {
                        Tarr<T, firstLength> first;
                        Tarr<T, lastLength> last;
                    };
                    #pragma pack(pop)
                };
                template <typename Self>
                inline auto& operator[](this Self&& self, length::type idx) {
                    return self.value[idx];
                };
                
                template <typename Self>
                constexpr auto& operator[](this Self&& self, length::type idx) {
                    return self.value[idx];
                };
        };
        template <typename Self>
        inline auto& operator[](this Self&& self, length::type idx) {
            return self.value[idx];
        };
        
        template <typename Self>
        constexpr auto& operator[](this Self&& self, length::type idx) {
            return self.value[idx];
        };
};

template <typename T>
concept tarrType = requires {
    typename T::type;
    typename T::value;
    requires std::same_as<Tarr<typename T::type, typename T::value>, typename T>
};

template <tarrType T>
concept tarrIndexType = requires std::same_as<T::indexType, T>;

template <tarrIndexType T, T::length::type byteL, T::length::type bitL, Tarr<T::length::type, hold<T::length::type, byteL + (bitL//8) + 1>> conf>
struct GPUShuffle {
    /* 정신놓고 짰다 */
    /**
       * GPU에 상시 대기시켜놓을 벡터
       * tarrIndexType ob가 입력으로 오면, ob[i] = ob[GPUShuffle::value::value[i]]를 GPU연산으로 하여, 인덱스 배열인 ob를 조작하는 연산을 GPUShuffle이라고 부른다.
        * GPU에 미리 로드된 GPUShuffle연산을 요청하면, 실행하는 방식이다.
        * GPUShuffle ob가 입력으로 온 경우엔, ob[i] = ob[GPUShuffle::value::value[i]]를 GPU연산으로 하여, 새로운 GPUShuffle연산을 런타임에 얻어낼 수 있다.
        */
    using confTyp = typename Tarr<T::length::type, hold<T::length::type, byteL + (bitL//8) + 1>>;
    using byteLength = typename hold<typename T::length::type, byteL + (bitL // 8)>;
    using bitLength = typename hold<typename T::length::type, bitL % 8>;
    using config = typename hold<confTyp, conf>;
    using value = hold<T, GPUShuffle::gen()>;
    constexpr static T gen(void) {
        constexpr T ret;
        for (constexpr T::length::type i = 0; i < T::length::value; i++) {
            if constexpr (byteLength::value == 0 && bitLength::value == 0) {
                ret[i] = i;
            } else if constexpr (byteLength::value == 0 && bitLength::value == 1) {
                if constexpr(conf[0] & 1) {
                    ret[i] = (i + 1) % T::length::value;
                } else {
                    ret[i] = (T::length::value - 1) - i;
                }
            } else if (byteLength::value == 0) {
                ret[i] = i
                switch (bitLength::value) {
                    case 2:
                        constexpr auto x = GPUShuffle<T, 0, 1, conf[0] & 1>();
                        constexpr auto y = GPUShuffle<T, 0, 1, conf[0] & 2>();
                        ret[i] = ret[x[i]];
                        ret[i] = ret[y[i]];
                        break;
                    case 3:
                        constexpr auto x = GPUShuffle<T, 0, 2, conf[0] & 3>();
                        constexpr auto y = GPUShuffle<T, 0, 1, conf[0] & 4>();
                        ret[i] = ret[x[i]];
                        ret[i] = ret[y[i]];
                        break;
                    case 4:
                        constexpr auto x = GPUShuffle<T, 0, 3, conf[0] & 7>();
                        constexpr auto y = GPUShuffle<T, 0, 1, conf[0] & 8>();
                        ret[i] = ret[x[i]];
                        ret[i] = ret[y[i]];
                        break;
                    case 5:
                        constexpr auto x = GPUShuffle<T, 0, 4, conf[0] & 15>();
                        constexpr auto y = GPUShuffle<T, 0, 1, conf[0] & 16>();
                        ret[i] = ret[x[i]];
                        ret[i] = ret[y[i]];
                        break;
                    case 6:
                        constexpr auto x = GPUShuffle<T, 0, 5, conf[0] & 31>();
                        constexpr auto y = GPUShuffle<T, 0, 1, conf[0] & 32>();
                        ret[i] = ret[x[i]];
                        ret[i] = ret[y[i]];
                        break;
                    case 7:
                        constexpr auto x = GPUShuffle<T, 0, 6, conf[0] & 63>();
                        constexpr auto y = GPUShuffle<T, 0, 1, conf[0] & 64>();
                        ret[i] = ret[x[i]];
                        ret[i] = ret[y[i]];
                        break;
                }
            } else if constexpr (byteLength::value == 1 && bitLength::value == 0) {
                constexpr auto x = GPUShuffle<T, 0, 1, conf[0] & 1>();
                constexpr auto y = GPUShuffle<T, 0, 1, conf[0] & 2>();
                ret[i] = ret[x[i]];
                ret[i] = ret[y[i]];
                break;
            } else if constexpr (byteLength::value > 1 && bitLength::value == 0 {
                constexpr auto x = GPUShuffle<T, byteLength::value - 1, (conf::acess<hold<byteLength::type, byteLength::value - 1>>) conf::first>();
                constexpr auto y = GPUShuffle<T, byteLength::value - 1, (conf::acess<hold<byteLength::type, byteLength::value - 1>>) conf::last>();
                ret[i] = ret[x[i]];
                ret[i] = ret[y[i]];
            } else {
                constexpr auto x = GPUShuffle<T, byteLength::value, (conf::acess<hold<byteLength::type, byteLength::value>>) conf::first>();
                constexpr auto y = GPUShuffle<T, byteLength::value, (conf::acess<hold<byteLength::type, byteLength::value>>) conf::last>();
                ret[i] = ret[x[i]];
                ret[i] = ret[y[i]];
        };
    };
}

template <typename T, hold L>
struct VirtualMemory {
    /* malloc • calloc • realloc • free • new • delete • splitlloc 은 여기서 */
    public:
        using length = typename L;
        using VRAMType = typename Tarr<typename T, typename L>
        using VMMUType = typename VRAMType::indexType;
        VRAMType VirtualRAM;
        VMMUType VirtualMMU;
        template <typename Self>
        inline auto& operator[](this Self&& self, length::type idx) {
            return self.VirtualRAM[VirtualMMU[idx]];
        };
        
        template <typename Self>
        constexpr auto& operator[](this Self&& self, length::type idx) {
            return self.VirtualRAM[VirtualMMU[idx]];
        };
        template <typename Self>
        void addrswap(this Self&& self, length::type Length, length::type x, length::type y) {
            for (length::type i = 0; i < Length; i++) {
                self.VirtualMMU[x + i] ^= self.VirtualMMU[y + i];
                self.VirtualMMU[y + i] ^= self.VirtualMMU[x + i];
                self.VirtualMMU[x + i] ^= self.VirtualMMU[y + i];
            };
        }
        template <typename Self>
        auto getMMUptr(this Self&& self, length::type L, size_t ptr) {
            auto* temp = ((self.virtualMMU::acess<(length::type) ptr>*) &self.virtualMMU)->last;
            return &((temp::acess<L>*) temp)->first;
        }
        
        template <typename Self>
        void* splitlloc(this Self&& self, length::type L, size_t ptr) {
            ...상새 구현중...
        };
};

등등 여러가지를 구현할 생각이다. SlicibleTarr은 폰 관리 앱의 핸드폰 사용시간이 모자라서 구현을 미뤄둔다..
```
