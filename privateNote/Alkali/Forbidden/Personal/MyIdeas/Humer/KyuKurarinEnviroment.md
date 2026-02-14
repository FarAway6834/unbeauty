# KyuKurarin (Esotric language) (jp : きゅうくらりん) (ft. 번외로 KyuKurarin Lisp 내장)

1️⃣ 이 문서에서 소개하는 첫번째 Esolang : KyuKurarin (Esotric language) (jp : きゅうくらりん) 1️⃣

 >
 > > 
 > > # 躁鬱の鬱
 > > 
 >
 > * Paradime : depressive disorder (computer = antipathy world (존재하지 않는 가능새계), 컴파일러도 형식문법이라는 허상, 기계어도 CPU에서 instruction set으로 디코딩되니 가짜, 메모리 주소도 MMU에 의해 물리 주소로 변환되니 가짜, 인터프리터는 존재하지 않는 기계가, 존재하는 기계가 만족해야할 튜링 완전성응 만족하는 가짜, 튜링 머신이라는 존재는 투스택 오토마타와 동치이지만, 현실에는 스택이 존재하지 않으니, 가상의 대상과의 동치성이 생길수 있는 가능성을, 무어 기계의 I/O로 스택을 단다는 형이상학적 상상, 존재하지 않는 복합사실(비트겐슈타인 초기)•복합관념(흄 경험론)로, 현대 컴퓨팅에 대한 관점을 노래 Phony의 가사 첫 2절 `なぜ（何故）ならば総て（すべて）は嘘（うそ）で出来（でき）てうる`로 잡는다.)
 > * 만든 계기 : 재작자가 기분이 급 공허해지고 침울해짐.
 > * 주의할점 : depressive disorder가 컴퓨터를 대하는 태도는 그냥 제작자의 우울을 쏳아내려고, 형식언어이론 • 양상논리 • 비트겐슈타인의 관점 등을 가지고 비관론을 최대한 표현한 껴맞추기다. 심오한 뜻같은거 없다. 해당 철학을 한마디로 반박한다면, "사회적 약속이니까 있다고 가정하는거고, 공학적 목적 자체가, 이론전산학적인 대상을 시뮬레이션하는게 목적이다. 에초에, 컴퓨터를 튜링 머신으로 취급하는 공학에서, 유용성을 위해서, 튜링 머신으로 취급한다는 공리가 있다는 선에서 핑계대면 되는 문제지, 실제로는, 충분히 큰 N에 대해서 매모리 용량을 N으로 취급하고, 분산 컴퓨팅과 동시에 공장을 돌리면 이론상 자원의 수만큼 서버 증설도 가능하다. 에초에 공학에다가 이론을 가져오는 순간, 공학의 목적인 유용한 대상을 제조하는것에서 벗어나서, 형이상학적인 허구를 만드는거다. 비트겐슈타인 초기식으로 비판하자면, "비트겐슈타인의 사다리를 버려야하는곳(형이상학을 사용하지 않는 곳)에서, 형이상학을 사용한것이 문재"다. 에초에 컴퓨터 공학은 이론적인 부분과 현실의 괴리가 첫번째 문제로 취급되고 시작한다.
 > * hint : 이 esolang은 그냥 사실 아무의미없는 우울감을, 억지로 가짜 의미에 껴맞춘것.
 > * tip : 우울증 완치된지 3년이나 되서 "우울증 흉내"인것이다. 컨셉이다 컨셉 ㅋㅋㅋ, 그러나 절대 유쾌한 질환은 아니다.
 > * note : Kafu(可不, かふ)가 부른 KyuKurarin과 Phony에서 영감을 얻었다. 평소에 즐겨듣는 노래다.
 > * 추가적인 관전 POV : 가상 힙을 사용할때, OS로부터 매모리를 할당받기에, 사실은 페이지를 mmap으로 불러온다)의 생산성은? (+ 정적 영역의 메모리 할당을 전부 구조체 • 공용체 기반으로, 메모리 구조도 다이어그램으로 타입을 취급하도록 하고 Haskell적 OOP같이 함수로 구조체를 인자로 받을수 있는거 외에, 정적 영역은 죄다 구조체로 다뤄야하는 지옥이라, 하나의 네임스페이스 안에 모든걸 일반화 • 구조화하려는 플라톤적 강박이라는 비형식적 아이러니
 > * 언어의 촘스키 위계 : `#pragma KyuKurarin(allow, stack)`를 코드에서 사용하지 않으면서 제귀를 안쓰는 heaplessKyuKurarin인겅우 FSM, heaplessKyuKurarin인겅우 PDA, `#pragma KyuKurarin(include, KyuKurarin うそ)`가 코드 내에 존재하면, Turing Machine.
 > * heaplessKyuKurarin와 stacklessKyuKurarin : `#pragma stacklessKyuKurarin`을 선언하면, 자동으로, `#pragma heaplessKyuKurarin`이 따라붙는다 (`#pragma KyuKurarin(allow, stack)`를 금지하는 방법이다.). 컴파일러 옵션에서, --not-stacklessKyuKurarin를 해야지, `#pragma stacklessKyuKurarin`가 코드에 존재하지 않아도 에러를 내지 않으며, --not-stacklessKyuKurarin인 상태라면, --not-heaplessKyuKurarin를 해야, `#pragma heaplessKyuKurarin`가 없어도 코드에서 에러를 안낸다. <의도 = 왠만해서는, 튜링머신으로 자신을 속인 FSM을 FSM이나 PDA로 다루라는 메시지. 일부러 번거로움을 추가하여, 정적영역 only나 heapless설계를 고려하도록 설계되어있다. 또한, `heaplessKyuKurarin`의 다른 이름은 `造花（ぞうか）`임. `#pragma ぞうか`도 인식함. "この世で（よで）造花より（ぞうかより）綺麗な（きれいな）花は（はなは）無い（ない）わ"라고 해서, `#pragma ぞうか`를 선언하면, 컴파일러는, "ああ 化石に（かせきに）なっちまうよ、 ああ 取り繕って（とりつくろって）いたいな、 ちゃんと笑え（わらえ）なきゃね、 大した（たいした）取り柄も（とりえも）無い（ない）から、 空っぽが（からっぽが）埋らない（いまらない）こと、 全部（ぜんぶ）ばれてたらとしよ。。。heap is toritsukurotta-warai（取り繕った笑い, とりつくろったわらい） not real"라면서 경고를 냄. --slime이라고 컴파일러에게 지시해야, 그런 경고를 내지 않음. `#pragma toritsukurotta-warai`라고 적으면, slime지시어의 효과를 냄.
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

 ⚠️ 주의 : heaplessKyuKurarin언어에 대해 정의함. ⚠️
  * heaplessKyuKurarin언어 : `#pragma heaplessKyuKurarin`시 `#pragma KyuKurarin(include, KyuKurarin うそ)`에 대해, `わたし きゅうくらりん`라고 에러를 내고 종료한다. 이외에난 KyuKurarin언어와 100%동일
  * 실제로 KyuKurarin은 heap을 malloc • calloc • realloc • free • new • delete • splitlloc 으로 직접 사용하는걸 금지한다. `#pragma IAmKyuKurarinCompiler`를 명시해야만 사용 가능하다.
  * SlicibleTarr는 `#pragma KyuKurarin(include, KyuKurarin うそ)`를 명시해야 include되고, 그제서야 사용 가능하다. 그 이전까지, virtual MMU는 존재하지 않고, SlicibleTarr도 존재하지 않는거다.
  * malloc • calloc • realloc • free • new • delete • splitlloc 마저도, `#pragma KyuKurarin(include, KyuKurarin うそ)`를 명시해야 include되고, 그제서야 사용 가능하다. 그 이전까지, virtual MMU는 존재하지 않고, malloc • calloc • realloc • free • new • delete • splitlloc도 존재하지 않는거다.
  * load 라는 명령이 존재하는데, "load 객체타입"시, new를 하는 대신에, SlicibleTarr에 인덱스를 추가해서 (realloc 이후 new를 하여, addrswap으로 로드하고, realloc으로 발생한 쓰래기만 delete하는 기법) 사용하는 방식으로, 사실상 new의 대용이다. SlicibleTarr를 초기에 생성하면, SlicibleTarr::load 식의 이름으로 사용 가능한 명령어다. 기본적으로, SlicibleTarr초기화 및 사용은 IAmKyuKurarinCompiler없이도 허용되기 때문. 인덱스 삭제로 슬라이싱을 통해서 구현되서, delete가 필요없던거고.
  *  SlicibleTarr가 없는 KyuKurarin은, Stack이외에 동적 할당이 없으니까, Push down Automata로 봐도 무방하다.
  *  SlicibleTarr를 `#pragma KyuKurarin(include, KyuKurarin うそ)`로 로드해야만, 튜링 완전하다.

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

### KyuKurarin PCRE : KyuKurarin Bootstrap구현시, 컴파일러 재작용.

 + SlicibleTarr<T, L>은 x.slice(size_t start = 0, size_t end = x::length::value, size_t step = 1)로, x.slice(k), x.slice(0, k), x.slice(0, x::length::value, k)가 정의되어있어서, x.slice(size_t start = 0, size_t end = x::length::value, size_t step = 1)를 y = x.slice(start, end); y.slice(0, y::length::value, step)으로, x.slice(start, end)를 x.slice(0, end).slice(start)로 취급한다.
 + 또한, SlicibleTarr<T, L>은 벡터로 변환 가능하며, SlicibleTarr<T, L> x, SlicibleTarr<T, N> y에 대해, x + y로 concat이 정의된다.

그.러.나.초.고.속.임.

 + SlicibleTarr<T, L>을 immutable하게 관리해주는 wrapper 객체를, CytarrTuple<T, L>(cython에서 T를 object로 명시시  T = PyObject)이라 하고
SlicibleTarr<T*, L>*을 mutable마냥 append나 extend를 해당 포인터의 concat값으로의 치환으로 대체하는 wrapper 객체을 CytarrList<T, L>(cython에서 T를 object로 명시시  T = PyObject)이라 하고(단. SafeCytarrList<T, L>은 SlicibleTarr<T, L>를 new로 할당해놓고, 그 객체는 new에 의한 포인터이므로, 객체 변수들을 mutable마냥 append나 extend를 concat값으로 연산한 결과로, 객체 변수를 업데이트하고, 이전 값이었던 포인터를 지우는 방식으로 작동하는 안전한 리스트. 안전한 이유는, T*의 관리가 아니라서, T*에 간접적으로 접근하면서 Free하지 않아서 안전한게 첫번째, 두번째로, 배열의 각 인덱스가 포인터처럼 다뤄지지 않아서, python list특유의 side-effect를 없엘수 있음)
 + CytarrTuple<char, L>를 bytesarray처럼 관리하는 wrapper 객체를 CytarrBytesArray<L>라 하고 (크으~ char이라 편하다.)
 1 CytarrBytesArray<L>를 bytes처럼 관리하는 wrapper객체를 CytarrBytes<L>라 하겠다. (크으~ 이것도 char이라 편하다.)

perl호환 regex를 CytarrBytes<L>로 구현한다면 역.대.급. 초고속일거다.

요약 : Cytarr은 기본 Collection이 str제외하고 고속화되어있고, pxd로 불러올때, cythonic하게 정적 타입도 가능하며, 무엇보다, bloom-filter나 union-find구현이 용이하며, 해시 맵도 만들기 용이하다. 자료구조 구현이나, perl호환 regex를 cython으로 AOT컴파일하는것도 나쁘지 않겠다.

CytarrBytes를 잘 생각해보면, pcre에 비트레벨 조작기능과 `x ~= s/(.*?)/7$1/g; x ~= 본체`를 추가해서, 이미 캡쳐한 문자를 bit-index값의 조합으로 표시하면, 그걸 C++연산취급해서, 여러가지 문자를 다룰수 있고, `x ~= s/(.*?)/7$1/g; x ~= 본체`로 "0b01010101"을 미리 제공하므로써, 공문자열 입력에도 대처가 용이한 PCRE프로그래밍이 가능할듯하다.

<고속 비트 • 문자열 처리>
 >
 > KyuKurarin PCRE를 다음과 같이 정의함.
 > 
 > + EBNF를 CytarrBytes기반 bitwise조작 •bloom filter•uniom-find를 곁들인 PCRE에 서브루틴 매치패턴으로 컴파일(EBNF비터미널 문자열이 PCRE페턴을 DEFINE한 서브루틴으로 컴파일됨)하는 방식으로 구현하면 으흐흐... 심지어는 EBNF 에러까지도 전•후방 긍정 탐색 등에 걸리면, 플래그 패턴을 정의시키는 식으로 구현 가능하다. 요컨데, "KyuKurarin PCRE"라는 `\{ebnf}`라는 이스케이프로, EBNF코드를 PCRE서브루틴으로 만드는 "언어" 다. 
 > + 그리고, PCRE substituate • pettern자체를 하나의 서브루틴으로 취급하여, ${서브루틴명}으로 실행까지 가능하다면 금☆상☆첨☆화.
 > + IO<typename T, iob G> io에 대해, G io[T channel]로 두고, G ob에 대해, CytarrBytes<L> 타입의 ob.input<L>() 및, output<L>(CytarrBytes<L> data); 인 IO객체를 입출력 함수로 가상화해서,  > + `#pragma IO<filename.h>(io)`라고 작성하고, filename.h라는 KyuKurarin에서 이를 지정해주면,
 > 1. 평범하게 C의 stdio/stderror/program parameter • exit/pipe massage • process massage • syscall 및 Aduino와의 I/O연동용으로 구현 가능
 > 2. C#과 연계하여, 네이티브 GUI용 입출력과 연계 가능
 > 3. WASM으로 컴파일시 JS와 연계 가능.
 > 4. KyuKurarin을 프로그래밍 언어로 사용
 > 5. 무슨 미친놈의 PCRE 언어가, **서브루틴•제귀가 있고, 분기가 있는** PCRE특성상, 튜링 완전하다.

Note : KyuKurarin구현 이전엔 perl로 구현된 저속 인터프리터로, KyuKurarin PCRE를 돌린다. KyuKurarin은 구현 초기부터, KyuKurarin PCRE로 짜였으니, 초기에만, Perl KyuKurarin PCRE interpreter를 Blotstrap용으로 쓰지, 나중엔, KyuKurarin PCRE는 AOT언어다. 그리고, KyuKurarinPCRE는 Perl KyuKurarin PCRE interpreter가 아닌 경우, KyuKurarinPCREibleStr를 통한 고속 검색과, x[x.find(v):x.find(v)+k]를 이용한, 슬라이싱의 이용으로, @FIND라는 데코레이터를 달아놓는 PCRE substituate는 서브루틴 입출력 타입을 KyuKurarinPCREibleStr로 간주한다. 이를 통해서, 쉬운 구현을 만들려는 전략이다. 그래서, Perl KyuKurarin PCRE interpreter가 아니더라도, KyuKurarin PCRE MAD Compiler에서는 오로지 `@FIND`만 인정하는 KyuKurarinLisp컨셉(데스노트)의 노망난 컴파일러가 있다. KyuKurarin PCRE MAD Compiler는 부트스트랩 컴파일을 위한 특수 구현일 뿐이다.

⚠️ 이 문서에서 가장 중요 : CyTarr은 Cython을 쓰지 않음. python.h를 따로 include해야만 PyObject사용 가능. 즉, 순수 KyuKurarin이고, Cython과 동형이라 CyTarr라고 불릴 뿐. ⚠️

### KyuKurarin Lisp (Esolang) : 동적 구조체를 만들기 위한 몸부림

2️⃣ 이 문서에서 소개하는 두번째 Esolang ; KyuKurarinLispDynamicStruct가 너무 훌륭해서, KyuKurarin에서 옵션 언어로 추가되었다. 다만, KyuKurarin은 컴퓨터 비관론 기반이라면, KyuKurarinLisp는, "바이너리•기계어 실시간 Rewrite로 노망나던 말건 무슨상관이야" 기반이라는 점에서, KyuKurarin은 저수준 우울증 페러다임 컨셉 esolang이고 KyuKurarinLisp는 고수준 바카야로이드 Lisp페러다임 컨셉 esolang이다. 2️⃣

 >
 > > 
 > > # 躁鬱の躁
 > > 
 >
 > 
 > Paradime : ~~바카야로이드~~ Lisp
 > 만든 계기 : `KyuKurarinLispDynamicStruct`가 필요하다.
 > 특이사항 : KyuKurarinLispDynamicStruct를 사용하기 위해서는, `#pragma KyuKurarin(open/close, deathnote)`를 통해서, 열려있는동안, KyuKurarin Lisp에서 사용하는 타입들이 잠시동안 include되어 접근이 허용된다.
 > 주의사항 : 에러 메세지 로그가, 우울증 분위기에서, 바카야로이드 분위기로 바뀐다.
 > Esolang컨셉 : 바카야로이드. 죽기 전에 노망나서 미쳐가는 단계다.
 > 

<고속 컬랙션 • 고속 리스트 프로세싱 • 고속 자가 수정 코드>
 * KyuKurarin Lisp(KyuKurarin 코드를 실행하는, aot라는 이름의 기계어 exec 바이트코드와, get 구조체 필드명으로, 구조체 필드를 가져오는 연산이 존재하는, 한마디로 요약하자면 저수준 타입으로 연산하는 리스프. PyObject나 numpy배열이 예외적으로 허용됨)는 그저 다음 타입들로 bytecode를 실행하는 자료구조로, 첫 AOT 컴파일 (코드가 바이트코드로, 전용 AOT컴파일도 동반) 이후, JIT컴파일러에 의해 돌아감.
 * 다음 자료구조 PyObject, KyuKurarinLispList<T> (Fact : bytecode • exec가 추가된 CytarrList), KyuKurarinLispTuple<T, L> (Fact : bytecode • exec가 추가된 CytarrTuple), KyuKurarinLispList<T>::bytecode, CytarrLispTuple<T, L>::bytecode, KyuKurarinLispList<T>::exec (Fact : bytecode가 담긴 collection이면 trace JIT하여 작동하는 jump table실행기. 한마디로 이 함수는 trace JIT virtual machine이다. List용 exec), KyuKurarinLispTuple<T, L>::exec (Fact : bytecode가 담긴 collection이면 trace JIT하여 작동하는 jump table실행기. 한마디로 이 함수는 trace JIT virtual machine이다. Tuple용 exec), SlicibleTarr<T, L>, KyuKurarinPCREibleBytes<static_method_structs>::methods (Fact : KyuKurarinPCRE(bloom filter and union find included)는 static inline method의 형태로 struct안에 배포되기에, KyuKurarinPCREibleBytes에 넣어주면, method로 접근 가능), KyuKurarinPCREibleBytes<static_method_structs>, KyuKurarinPCREibleBytesArray<static_method_structs>::methods와 KyuKurarinPCREibleBytesArray (ByteArray를 위해서), KyuKurarin LispListComprehension<T> (Fact : 걍 iterator인데, next요청시에 증설하는 C++식 iterator일 뿐이라서, 실제 로직은 Lisp함수 코드를 List처럼 접근할 뿐.), KyuKurarinLispTupleGenerator<T, L, bool infinity = true> (Fact : KyuKurarinLispListComprehension랑 동일한 원리.) • KyuKurarinLispDynamicStruct • KyuKurarinPCREibleStr를 이용 가능한 프로그래밍 언어다.
 * Fact : TMP에서 사용 가능
 * Fact2 : 정적 최적화가 가능한 부분은 KyuKurarin로 AOT컴파일되기에, AOT컴파일 가능한 구간에선 `@AOT`라는 데코레이터로 힌트를 단다.
 * Fact3 : 컴파일러가 슈퍼컴파일러이기에, `@AOT`를 달을수 있는 부분은 모조리 찾아내서, Native KyuKurarin로 바꾼다. 그렇다 하더라도, PyObject사용시 느려질수 있고, KyuKurarinLispList • KyuKurarinLispTuple • SlicibleTarr 사용시 슬라이싱을 쓴다면 SlicibleTarr 정도의 속도고,  KyuKurarinPCREibleBytes의 경우, KyuKurarin에서 KyuKurarinPCRE를 쓰는 속도며, KyuKurarinLispListComprehension • KyuKurarinLispTupleComprehension의 경우는, "KyuKurarin/C++Iteraoter"(C++Iterator기능을 추가한 KyuKurarin으로 순수 KyuKurarin이 아닌 C++이 추가됨.)에서 KyuKurarinLisp를 사용하는 속도다.

 * N.B. 나는 KyuKurarinLisp를 KyuKurarin으로만 구현한다 한적이 없다. JIT Engine • jump table • uintptr_tm• register강제등 여러가지 C언어의 흑마법을 이용할 생각이고, KyuKurarinLisp의 컴파일러는 슈퍼컴파일 부문은 C/KyuKurarin가, 일반적인 매칭은 KyuKurarinPCREible가 진행한다. 물론 AOT부문에서, KyuKurarinLisp도 문자열 조작이나 동적 로직에 적극 이용한다. 허나, "KyuKurarinLisp및 KyuKurarinPCRE"는 AOT에서만 쓰고, JIT애서는 쓰지 않고, 필요하면, 즉석에서, C/KyuKurarin Lisp로 모사하는 방식으로 갈 뿐이다. 부트스트랩 초기엔 perlKyuKurarinPCRE를 대용으로 쓸수밖에 없다.
 * N.B. pure interpreter버전은 bootstrapKyuKurarinLisp라는 별개의 언어다. `@AOT`등이 빠졌는데 어케 별게가 아니겠는가? bootstrapKyuKurarinLisp도 부트스트래핑을 위한 특수 언어일 뿐이다.

#### KyuKurarin에서 `#pragma KyuKurarin(enable, Lisp)`시

KyuKurarinLispList<T> (Fact : bytecode • exec가 추가된 CytarrList), KyuKurarinLispTuple<T, L> (Fact : bytecode • exec가 추가된 CytarrTuple), KyuKurarinLispList<T>::bytecode, CytarrLispTuple<T, L>::bytecode, KyuKurarinLispList<T>::exec (Fact : bytecode가 담긴 collection이면 trace JIT하여 작동하는 jump table실행기. 한마디로 이 함수는 trace JIT virtual machine이다. List용 exec), KyuKurarinLispTuple<T, L>::exec (Fact : bytecode가 담긴 collection이면 trace JIT하여 작동하는 jump table실행기. 한마디로 이 함수는 trace JIT virtual machine이다. Tuple용 exec), SlicibleTarr<T, L>, KyuKurarinPCREibleBytes<static_method_structs>::methods (Fact : KyuKurarinPCRE(bloom filter and union find included)는 static inline method의 형태로 struct안에 배포되기에, KyuKurarinPCREibleBytes에 넣어주면, method로 접근 가능), KyuKurarinPCREibleBytes<static_method_structs>, KyuKurarinPCREibleBytesArray<static_method_structs>::methods와 KyuKurarinPCREibleBytesArray (ByteArray를 위해서), KyuKurarin LispListComprehension<T> (Fact : 걍 iterator인데, next요청시에 증설하는 C++식 iterator일 뿐이라서, 실제 로직은 Lisp함수 코드를 List처럼 접근할 뿐.), KyuKurarinLispTupleGenerator<T, L, bool infinity = true> (Fact : KyuKurarinLispListComprehension랑 동일한 원리.) • KyuKurarinLispDynamicStruct • KyuKurarinPCREibleStr가 사용 가능해진다.

⚠️ 이 문서에서 가장 중요한 점 : KyuKurarinLispDynamicStruct • KyuKurarinPCREibleStr는 KyuKurarinLispTuple과 KyuKurarinLispList와 KyuKurarinLispListComprehension과 KyuKurarinLispTupleGemㅔnerator로 구현되는 응용 타입일 뿐이다. (KyuKurarinLisp는 KyuKurarin에서, KyuKurarinLispList나 KyuKurarinLispTuple을 KyuKurarinLispList<T, L>::exec • KyuKurarinLispTuple<T, L>::exec로 실행하면, 실행이 시작된다. KyuKurarinLispList<T, L>::registerWarmUp이나 KyuKurarinLispTuple<T, L>::registerWarmUp에 코드를 등록하면, exec전에 실행된다.) ⚠️

문자열 집합 L을 유저가 lang L = {집합}으로 선언하면, L집합의 클레이니스타가 구조체 필드가 되도록 하는 동적 구조체가 되게 하면 되다. 그럼 단지 구조체 포인터 내부의 구조체 포인터니까 객체지.

...이걸 KyuKurarinLisp로 다루면, 코드 변경 로직을 통해서, lang구조체의 템플릿이 런타임에 바뀌는게 표현 가능하다. (예컨데, lang x = {p, q, r};에서, x*는 ob.ppppppppqqqr같은 필드명을 다룰수 있다.)

1. lang애서 lexing기능까지 있으니, lang문자열에 대한 정보를 최적으로 관리 가능

2. 실제 trie객체에서는, lang문자셋의 문자열들이 인덱스(substring이 인덱스 노드)가 되야하기에, 구조체 맴버 변수의 접근시, 구조체 자체는 KyuKurarinLisp가 동적으로 메모리 구조를 관리하기에, 때에따라 list를 조작하여, 적절한 인덱스에 구조체 변수를 배열하는, 구조체 메모리 오프셋 최적화와, 실제 구조체 접근시, 멤버 변수의 위치는 컴파일타임에 list index로 추정된다 (컴파일러가, 최적화된 구조체 메모리 오프셋을 알고있기 때문에, 어떻게 바뀔것인지도 알고있음). 그런 방식으로 동적 구조체가 구현된다. (컴파일러가 개고생하는 이유는, 맴버 변수의 위치로 추정을 하고 나서, 맴버 변수의 위치에 따른 컴파일된 구조체 타입을 생성해서, 해당 구조체로, list를 접근해야하기에, 사실상 C컴파일러가 구조체라는 가상의 대상을 구현해주는 난이도다.) 근데 이걸 컴파일 타임에 할수 없기에, 실제로는, 그 리스트를 구조체를 입힌 가상 메모리 취급해서 (KyuKurarinLispDynamicStruct객체) 바이트코드상에서, KyuKurarinLispDynamicStruct(function)식으로, 함수를 주어줘서, 그 함수가 KyuKurarinLispDynamicStruct를 self로 받아서, 구조체 맴버를 접근하는 방식인데, KyuKurarinLispDynamicStruct는 정작 self는 안주고, function의 내부 코드를, 조작해서, 런타임에 해당 function을 현제 구조체 필드 구조에 맞게 컴파일하는 방식이라고 봐야한다.

3. 실제 substring이라고 하더라도, KyuKurarinPCREibleBytes의 탐색을 도와주는 wrapper일 뿐이라서, KyuKurarinPCREibleBytes.encoding<lang>을 통해서, trie객체 (동적 구조체라는 이름의 리스트)를 할당하여, KyuKurarinPCREibleStr라는 타입으로 접근하고, KyuKurarinPCREibleStr.decoding<lang>을 통해, KyuKurarinPCREibleBytes로 변환한다. 문자열 concat • 특정 substring삭제같은 경우는, trie작업을 먼저 진랭한 후, KyuKurarinPCREibleBytes에서 분할하는식으로 두가지 작업을 하는 방식이다. 다만, substring 탐색 • 삭제 • concat이 가능한 immutable이지 슬라이싱이나 치환은 불가하기에, KyuKurarinPCREibleBytes를 써야한다. decoding시 trie객체들을 전부 delete하는게 흠인 객체.

걍 KyuKurarinLisp에 있는 KyuKurarinLispDynamicStruct는 컴파일 타임 코드 애딧 기반이니까 약간 미친놈인것 같은데. KyuKurarinLispDynamicStruct자체는 재배열 • 엑세스시 오버해드가...
1. KyuKurarinLispDynamicStruct.unlock이전까지 immutable로 재배열 오버해드 0
2. KyuKurarinLispDynamicStruct.unlock을 통해, KyuKurarinLispDynamicStruct::unlockType으로 재배열시 재배열 오버해드는, SlicibleTarr의 조작속도이므로 빠름. (특정 멤버를 추가 • 삭제하면 재배열되는거) GPGPU Shuffle기능을 여러번 합성하는 방식이라는게 흠이지만.
3. KyuKurarinLispDynamicStruct::function • KyuKurarinLispDynamicStruct::compiled_function 으로만 엑세스 가능하고, KyuKurarinLispDynamicStruct::compiled_function은 원본인 KyuKurarinLispDynamicStruct::function를 origin으로 가지고 있으며, 런타임에 JIT 컴파일되지만, 그럼에도, 엑세스 에셋에 맞게 설정시키는 코드가 k개 존재시, O(k)오버해드가 존재. 그 이후 O(1)
4. 재배열시, KyuKurarinLispDynamicStruct::function의 맴버 변수 엑세스를, 에셋에 맞게 매핑시키는건, k = 1일시 O(1)이도록 동작해야하기에, KyuKurarinLispDynamicStruct(KyuKurarinLispDynamicStruct::function)을 하는 코드 자체를 **재배열시 조작하는 방식이다.** 요컨데, 컴파일러를 컴파일하는거다.
5. 변경이 잦다면 trie를 추천하지 않고, 접근속도를 희생해서, KyuKurarinPCREibleBytes선에서 끝내는걸 추천한다. GPGPU Shuffle을 AOT로 추가하지 않는 경우 최악의 경우 O(n) (미리 준비된 만능 Shuffle에셋을 조합하는 경우)이고, 엑세스 에셋에 맞게 컴파일할 런타임JIT Modifier를 JIT컴파일하는데 드는 비용이, 사실상 런타임에 코드를 생성하는거라, 미리 기억해둔 에셋 이름과 주소 쌍을, 코드로 구현하는데 드는 시간은, 길이 L = 1일때, O(1)로 에셋 이름과 주소와, 작성할 코드를 KyuKurarinLispListComprehension이라는 이터레이터로 O(L)에 걸쳐 생성하기에, 언젠가는 O(L)이 걸린다. O(1) 단위 생성 속도는 빠르지만. 최악의 경우 총 O(n + L)이다. (n은 Shuffle에셋 조합시 드는 횟수) 거기에다가, KyuKurarinLispDynamicStruct::function함수로 접근할때마다, k번의 작업이 존재할때, O(k)로 해야해서, KyuKurarinLispDynamicStruct::compile로 미리 이용할 KyuKurarinLispDynamicStruct::function을 JIT컴파일러로 기계어로 만들어야한다. O(n + L + k)인거다. KyuKurarinLispListComprehension자체도 JIT컴파일된다. O(L)과 O(k)가 JIT오버해드까지 동반라니 지옥이다. 참고로 굽는 시간중에, GPGPU속도는 사실, SlicibleTarr의 정의되지-않은-셔플-동작 시에 드는 비용이라, 행렬 연산 몇번하고, 통신은 input•ouput으로 한번밖에 안쓰이고, ram을 디바이스로 쓰기에 압승이긴 하다. 단지, GPU병렬연산인 Shuffle 한번에 시간 t가 소요될때, 시간 tn의 소모가 아깝다는거고, KyuKurarinLispListComprehension으로 JIT된 KyuKurarinLispDynamicStruct::compile를 생성하는 시간도, 실은, C++의 런타임에 생성돠는 iterator의 속도로 빠른데, 메모리 할당도, SlicibleTarr를 써서, 존나 빨라서 문제 없다. 해당사항이 O(1)이라도, 명령 L개에 대해서, KyuKurarinLispDynamicStruct::function에서 컴파일할것이 지시된 명령어(사실상 문자(char)열로 박혀있는 부분을 컴파일하라는 미션) 을 순회하는데 드는 시간은, 네이티브 for문으로 JIT컴파일되기에, 기계어를 런타임에 생성하는거다. 생성을 하더라도, jump table switch부분도 JIT가 개입해야하고, 그 이후에, jump table switch가 KyuKurarinLispDynamicStruct::function을 KyuKurarinLispDynamicStruct::compiled_function으로 바꿀때 하는 짓이, 상수 (KyuKurarinLispListComprehension에서 해당 상수를 박아넣는데, 그 상수는 바로, 메모리 에셋 구조체 필드가 어느 오프셋에 있는지다)의 구초제 접근으로 JIT컴파일을 라는 로직이기에, 사실상, 구조체 접근을 하는 정상적인 바이너리를 생성하는데 드는 시간이 jump table swich에 각 명령이 수행하는 기능이다. 말 그대로 jump table기반 JIT인터프리터 정도의 오버해드를 가지는 KyuKurarinLispDynamicStruct::compile를 생성하는거다. KyuKurarinLispDynamicStruct::compile은 함수를 런타임에 컴파일해주는거고, 그 함수를 읽는 과정이 인터프리터와 유사하기에 JIT되는데, 막상 KyuKurarinLispDynamicStruct::compile의 생성도 JIT로 (str.format(i, j) for i, j in asset)를 만드는 시간이라 기계어 시간이니까, 런타임 컴파일러를 제작하는 재작자 개고생한다. 실제로는, O(n + L + k)중에서, GPU부분 최적화가 응용되어 O(n + k)가 쓰일거고, 막상 재배열 이후에, function으로 접근하지 않으면 O(1)이다. O(n + k)마저 바이너리 성능이라는거. 중요한건, 최악의 경우, 기계어로 O(n + L + k)라는거, 귀중한 n + L + k명령 횟수가 날라가지 않는가 크하핫!!

## 응용 기술 : CSML

```markdown
# CSML : C-Structed Markup Language

HTML DOM을 사용하는 대신에, CSML DOM으로, WASM타깃인 Native언어(C/C++같은 언어. 어셈블리도 네이티브 언어임)에서 DOM을 고속 조작하는 방식을 이용한다.

프로그래밍 언어는 KyuKyrarin.
컴파일 옵션에서 `--fast`시 KyuKyrarinLisp를 프로그래밍 언어로 사용하지 않고, `--fast`없을시 기본적으로 KyuKyrarinLisp를 사용한다.

기본적으로 CSML은 KyuKyrarin과 KyuKyrarinLisp로 컴파일된다 (`--fast`시 결과에 KyuKyrarinLisp는 없다.)

...

...

(물론, CSML이 웹에 연결되는 방식에서 WASM부분만이 핵심이기에, 그렇게 말한거다)

...

...

## 기반 프로젝트 (의존성)

CSML프로잭트는 아닌데, CSML이 의존하는 기술들이다.

### JS • WASM target LLVM compiler of KyuKyrarin & KyuKyrarinLisp

CSML은 HTML/CSS/JS/WASM플렛폼 타깃 KyuKyrarin & KyuKyrarinLisp이다.

에초에 프로그래밍 언어가 JS(HTML/CSS/JS)랑 KyuKyrarin & KyuKyrarinLisp이다.

그리고 런타임이 WASM이다.

프로그래밍 언어는 의존성으로 달아놓기 애매하지만, 참조하는 기술은 맞기에 기재하였다.

### WebGPU • WebGL

런타임에 가장먼저,
1. WebGPU 사용 가능성 확인
2. WebGL 사용 가능성 확인
3. 알맞은 라이브러리를 WASM에서 사용하도록 연결 (KyuKyrarin은 기본적으로 GPU가 필요하기 때문에, WebGL같은 방식으로라도 가상이라도 강제로 할당해야한다.)
4. WASM WarmUp
5. 본격적인 작업 시작

을 하므로, 의존성이다.

### htmlless.js : <script src = 파일명>을 통해서 html을 생성하는 라이브러리. (서버리스가 실제로 서버를 최소화하듯, htmlless는 html을 최소화할 뿐이다.)

 > 
 >  - 정체 : 형식언어
 >  - 구현체 : 컴파일러
 >  - 결괏값 : html파일과 js파일
 > 

요약 : htmlless.js는 html의 문법에서, "필수식별자"라는 문법을 추가한 마크업 언어다.

필수식별자 : element이름 앞에 필수로 붙여야하는 식별자
1. extensible
2. sealed
3. frozen
4. nonhtmllessjs

제 1 장 : extensible

 > 
 >  - 원리 : JS가 `document.head / document.boy 등등`을 통해, element를 추가한다. (이걸 `onload-time DOM조작`이라 부른다.)
 >  - 특징 : DOM으로 해당 document element의 object를 조회해보면, `Object.isExtensible`시 true인 객체이다.
 >  - 구현 방법 : 순정 `make` (JS에서 DOM객체를 만든다) and `pack` (DOM에 추가한다) 방식
 >  - 주의사항 : make and pack방식이 이름이 거창해서 그렇지, DOM에 객체를 추가할때, "make element, and pack it!"이라는 지극히 당연한 소리다. (예컨데, 배열 초기화시, "declare array, and initialize"라고 말하는급의 황당함)
 > 

제 2 장 : sealed

 > 
 >  - 원리 : JS가 `document.head / document.boy 등등`을 통해, element를 추가한다. (이걸 `onload-time DOM조작`이라 부른다.)
 >  - 특징 : DOM으로 해당 document element의 object를 조회해보면, `Object.isSealed`시 true인 객체이다.
 >  - 주의사항 : `Object.isFrozen`시는 false다.
 >  - 구현 방법 : make결괏값을 pack하기 전에, Object.seal을 해준다 (개조된 `make` (JS에서 DOM객체를 만든다) and `pack` (DOM에 추가한다) 방식)
 >  - extensible과의 차이점 : 없다. Object.seal을 해준거 말고 없다. 솔찍히 왜 나눴는지도 모를정도로.
 > 

제 3 장 : frozen

> 
 >  - 원리 : JS가 `document.head / document.boy 등등`을 통해, element를 추가한다. (이걸 `onload-time DOM조작`이라 부른다.)
 >  - 특징 : DOM으로 해당 document element의 object를 조회해보면, `Object.isFrozen`시 true인 객체이다.
 >  - 구현 방법 : make결괏값을 pack하기 전에, Object.freeze을 해준다 (개조된 `make` (JS에서 DOM객체를 만든다) and `pack` (DOM에 추가한다) 방식)
 >  - extensible과의 차이점 : 없다. Object.freeze을 해준거 말고 없다. 솔찍히 왜 나눴는지도 모를정도로.
 > 

제 4 장 : nonhtmllessjs

 > 
 >  - 펙트 : 결과적으로 생성된 html파일에 박힐 코드다.
 >  - 그럼 왜 htmlless.js임? : 그래서 지시어 이름이 "non"htmllessjs임
 >  - 왜 필요함? : `<script src = 파일명>을 통해서 html을 생성하기 위해서` 그리고 인코딩이나 <html> • <head> • <body> 태그 명시
 > 

결론
 > 
 > 컴파일러가...
 >  * simple compiler : 앞서 설명된 내용만 충실히 실행
 >  * optimized compiler : 최적화된 html • js파일을 내놓음
 > 
 > 으로 나뉨.
 > 
 > 업대이트 유무...
 >  * 언어 설계는 simple compiler구현체인 셈이므로, simple compiler는 업데이트가 없다 (= 언어의 업데이트는 이게 끝이다.)
 >  * 이 프로젝트는, 사실상 **optimized compiler**를 어떻개 만들고 유지보수하고, **힌트용 구문을 추가하는가**이다.
 > 

#### optimized compiler의 힌트용 구문 예시

초기 설계 당시 계획된건 단 네가지밖에 없었다.

 * @conf_pragma : @pragma지시어를 통해, optimized compiler의 optimize과정을 능동적으로 통제 가능한 확장 프로그램을 명시한다 (그 확장 프로그램의 API구조는 명시되지 않았지만)
 * @pragma : 확장 프로그램이 처리하기 위해서 있는거다.
 * @alias(데코레이터로 사용할 이름, pragma기능명) : `@`문법이 확장되기 위해서.
 * @initialize_default_setting : 현제 optimized compiler가 @alias나 @conf_pragma등등 초기 optimized compiler 힌트용 구문들을 실행하게 한다. 이를 통해서, 미리, 힌트용 구문들이 설정되어서, 실제 컴파일러는 오로지 확장 프로그램을 정의하고, @initialize_default_setting를 통해서 로드하는 식으로 기능추가 • 컴파일러 버전 업데이트시 기능 제공 등 유지보수를 하는거다.

모든 데코레이터 형식의 optimized compiler 힌트용 구문은, @conf_pragma및 @pragma를 통해서 구현된다.

다만, 실제로 유저가 @conf_pragma를 쓰는 일이 없어야 하기 때문에, 실제로는, @conf_pragma는 사용시 "WARNING : use trustible compiler extension. but I'll trust your choice."이라고 경고가 뜬다. 물론 컴파일러에 내장된 확장 프로그램의 경우엔 경고가 안뜬다.

 > 
 > 요약
 >  - 핵심 : 컴파일러에서, 확장 프로그램과 API를 통해, optimizing만 전부 optimized compiler에 위탁.
 >  - 자유도 : MAX. 확장 프로그램이 결괏값을 입맛대로 조절 가능. 인증 절차가 필요할듯해서, 컴파일러 내장 확장 프로그램에 인증용 확장을 제공할 생각.
 >  - 그럼 컴파일러가 느려질텐데? : 실제로는, 구문에 `@initialize_default_setting`의 유무에 따라서, 존재하면, 확장 프로그램을 로드하는 과정을 생략하고 컴하일러가 확장 프로그램 기능을 대신하는 hot path를 준비하는 식임.
 >  - 런타임은 안느려지는가? : 컴파일타임 오버해드에 대한 이야기일 뿐, 데코레이터 문법은, 런타임이 아닌 컴파일타임 실행일 뿐이다.
 > 

## CCSS (CSML CSS)

CSS는 기본적으로, key와 value와 데코레이터 꼴의 추가구문으로 나뉘기에,
그냥 C Struct로 바꿔버린다.

**CCCS (compiled CCSS) 로 컴파일된다.**

CCCS는 struct로 객체처럼 취급된다.

## DOM 표현 방식

CSML nonasset 인터페이스(그냥 빈 struct이고, 실제로 메서드 구현 여부는 concept로 확인한다)를 상속한 경우와, CSML asset 객체인 경우로 나뉜다.

#### CSML nonasset 인터페이스(그냥 빈 struct이고, 실제로 메서드 구현 여부는 concept로 확인한다)를 상속한 경우

CASE 1 : sealed
 > 
 > 원리 : 에초에 sealed자체가 struct랑 동형이라, KyuKyrarin에서 struct로 구현된다.
 > 구현 : sealed라는 템플릿 타입의 객체로써, static영역에 할당된다.
 > 동형성 : static영역의 struct와 JavaScript seal Object는 이론전산학적으로 동형
 > 

CASE 2 : frozen
 > 
 > 원리 : const인 sealed다.
 > 구현 : sealed라는 템플릿 타입의 객체로써, const영역에 할당된다. 실은, const sealed 타입이라고 하는게 정확하겠다.
 > 동형성 : const영역의 struct와 JavaScript의 Frozen Object는 이론전산학적으로 동형
 > 

CASE 3 : extensible
 > 
 > 원리 : extensible자체가 json과 동형이고, KyuKyrarinLispDynamicStruct이 json과 동형이므로, KyuKyrarinLispDynamicStruct를 json마냥 동적 구조체로 다루는 extensible객체를 이용한다.
 > 구현 : KyuKyrarinLispDynamicStruct를 다루기에, 속성 추가•삭제가 가능한 JavaScript객체의 특성을 가진 KyuKyrarinLispDynamicStruct일 뿐이다. 그게 전부다.
 > 동형성 : 이론전산학적으로 json과 JavaScript의 Object가 동형이고, 이론전산학적으로 json과 KyuKyrarinLispDynamicStruct가 동형이다.
 > 

위 대상들은 html을 거치지 않고,
1. CCCS에 입각해서 렌더링할 대상에 대한 대이터는 이미 확보되어있다.
2. 곧장 WebGL • WebGPU를 통해 렌더링된다.
3. **이걸 CSML Viewer라 부르고, CSML Viewer가 필요하기 때문에, 대부분에 개발은 여기서 이루어진다.**

원칙 : 추상화는 지옥이니, 유지보수를 위한 저수준으로 제어 가능한 제로 코스트 추상화가 아니면 도입하지 말라. 문법설탕같은 트릭을 이용하여, 추상화하지 않고서야, 절대 안된다. CSML Viewer는 CSML과 CCCS를 읽고 (acess), 즉시 렌더링해야한다. (direct randering). Keep it simple, Keep it fast
예외 : 컴파일 결과물이 런타임 없이, CSML Viewer가 지연 없이 바로 렌더링을 조지는 2단계 스탭을 만족하면, DSL을 통해서, 추상화를 하는건 허용한다. 런타임 추상화가 아닌 컴파일 타임에 프로그래밍 언어 자체를 조작하는거기 때문에 런타임에 무관하디 때문이다.

#### asset

... 폰 사용시간 미스로 인해 이외에 정보를 적지 못했다. ...

### Simple CSML


```

## 마치며 (comment)

흥미로운 지점은, SlicibleTarr자체는, Tarr의 가상 MMU관리를 동반한 객체일 뿐이라는 점이다. Tarr을 가상 RAM을 mmap으로 실제 페이지에 연결해서 만든 가상 힙 매모리 풀에서 할당한 객체가 SlicibleTarr이다 (가능하면 vram이 아니라 진짜 ram과 mmu를 쓰고싶다... 커널 독재니까 불가능하겠네.. 울적하다.). 가상 MMU주소 변경(addrswap)과 realloc으로, split을 구현해서, x[:k], x[k:]를 구현하고, 가상 MMU주소 변경(addrswap)과 realloc으로 동일하게 split의 역과정도 가능하고, 심지어는 SlicibleTarr의 GPUShuffle을 이용해서, x[::k]슬라이싱용 split과 원소 이동을 구현했다. 이 과정만으로 슬라이싱 • concat가능한 고정길이, 배열 타입으로 슬라이싱 • concat시 타입이 변하니까, SlicibleTarr의 포인터를 관리해주는 객체만 만들면 list도 꿈이 아니다.
CyTarr이 pythonless인 이유가, python의 collection 본질적으로 slicing기반 대수학을 취하기 때문이다.

## reference : 설계할때, 참고한 내용

설계할때 내가 독자적으로 만든 수학이론으로, eval시 동작의 동형성을 가지고 기획하였기에 중요하다.

````
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
````

2026.2.13 금요일인 오늘도 "귀찮다..."는 이유로 안만들어왔지만......
