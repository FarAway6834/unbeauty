# F I N I T E ; 포스트 아포칼립스 소설에 넣을 형식언어 몽상 스케치.

[UJT 파일명] ptr DATA = &[고를 메모리 구역];
[F1N 파일명]<[UJT 파일명]> PROCESSER = [F1N 파일명]<[UJT 파일명]>(DATA);

이딴식으로 대충 구해준 callible객체가, 각 프로세스를 동작시키는거다.

물론 이건 시뮬레이션용 SW구현체이고, 이건 아포칼립스 이후, 전산 기계의 설계도용으로 표기하기 위한 언어이다.

여러대의 FSM들이 통신하여 튜링 머신이 되거나, 모든 FSM들을 O1 = I1 NOR I2 = O2인 기계를 만들어서 "AUTO NEC NEC"이라고 부르거나, 아니면 함수의 역할인 FSM들이 그래프를 그리도록 묶어서, 유향 그래프가 되거나....

그런식이다. 그런 사양을 명령어처럼 쓰는게 재미있다.

그러나 구상하는데만 3h가 가버렸으니 ㅅㅂ 이제 어쩔것인가.

## nihilcqkf에 대한것 (by cqkf & BVN2BL & nihilcc)

이 부분은 C와 관련된 의사코드로, 난 재미삼아 몽상하면서, 소설 소재로 쓰일 프로그램의 구현가능한 구채적 명세놀이를 한다는점을 잊지말자.

### nihilcqkf

cqkf 언어인데 컴파일러가 nihilcc인거다 ㅋㅋㅋㅋㅋㅋㅋ

### cqkf언어의 컴파일러인 cqkf.perl은 대충 다음과 같이 동작한다 ; 주의할점은 완성된 코드가 아니라 설계사항 명세이다.

* `--auto` 옵션 : C컴파일러 명령어 명세로 작동하다가 호출시 잘 링킹되게 해주거나, 아니면 있다는걸 알았을때 컴파일을 미리 다 마처주는 만능 비서

 * 동일한 확장자로 취급하는 목록 ;
1. *.cqkf = *.cqkf.cqk = *_cqkf.cqk
2. *.cqkh = *.cqkh.cqk = *_cqkh.cqk
3. *.cqki = *.cqki.cqk = *_cqki.cqk
4. *.cqkm = *.cqkm.cqk = *_cqkm.cqk
5. *.cqkp = *.cqkp.cqk = *_cqkp.cqk
6. *.cqks = *.cqks.cqk = *_cqks.cqk
7. *.cqk = *.cqk.txt = *_cqk.txt
 + 어떻게 동일하게 취급하는지는, 수학적으로 이미 당연하지 않는가? 동일하게 취급한다는건 저 확장자를 다 같은 의미로 언어 차원에서 본다는거고, 그것의 구현은 그 언어의 모델로서, 언어를 만족시킴에 충실하기만 하면 된다.

 * `#!/bin/cqkf.perl`로 확장자가 컴파일되는 모든 양상 ;
1. *.cqkf -> *.c
2. *.cqkh -> *.h
3. *.cqki -> *.ixx
4. *.cqkm -> *.cppm
5. *.cqkp -> *.cpp
6. *.cqks -> *.cs
7. *.cqk -> error
 + 이것이 진짜 컴파일이고, 이 컴파일 과정이 후술할 컴파일 과정 알고리즘임. 참고로 출력된 프로그램엔 `#!/bin/cqkf.perl`를 `#ifdef Cqkf`이후 `#undef Cqkf` 그리고, `#endif`이고, 그 다음 `#define Cqkf(macro, ...) macro(__VA_ARGS__)`이 나오게 설정된다.

 * `#!/bin/cqkf.perl □`인 빈칸에 ASCII 문자 하나가 들어있을때 ;
1. *.cqk -> *_cqk□.cqk (단. □는 `[A-Z]`)
2. *.cqk -> *.cqk□.cqk (단. □는 `[a-z]`)
 + `#!/bin/cqkf.perl □` -> `#!/bin/cqkf.perl` 로 컴파일됨

 * C언어 컴파일러 명령인 어절을 명시해뒀다면 (근데 2음절 이상), 알아서 컴파일까지 자동으로 진행 해준다.

* 흐름은 대충 아래와 같다.
1. `*.cqk`파일을 EOF가 나올때까지 한줄씩 읽어들이이는 모드로 연다.
2. 컴파일 후 결과물로 나올 파일 *.*를 한줄씩 작성하는 모드로 연다
3. 미리 딕셔너리 역할의 해시 "map"이 존재한다, 또한 라인 넘버를 세는 숫자 카운터 "line"이 존재한다. 또한 카운팅 필터 "set"도 존재한다. 그리고 PIPE입력을 받을 문자열인 "input"도 존재하고, PIPE출력을 하기 위해 디스플래이 출력 용도로 쓸 문자열인 "output"도 존재하며, stderr용도로 콘솔 에러로 쓸 문자열인 "errmsg"도 존재한다.
4. `*.cqk`파일을 EOF가 나올때까지 while하는것 같지만, for처럼 line을 증가시키는 반복을 하는거다.
5. A (NON EOF). '#pragma Cqkf'라는 문자열이 포함되어있는지 알아보고 분기한다 (include case or else case)
6. A. A (include case). 정규표현식 `/#pragma\sCqkf\([a-zA-Z_][a-zA-Z0-9_]*(,\s[1-9][0-9]*)?\)/`으로 값 추출을 시도한다.
7. A. A. Sucess. 미리 정의된 Cqkf함수에 실행해주면, 거기서 리턴한 문자열이 빈 줄이거나 어떤 글이 적힌 줄이므로, 그걸 output하는거다.
7. A. A. Faild. 걍 input을 output해버린다. 아까전에 감지되지 않게 문법적으로 잘못 코딩한놈 탓이다... 라고 생각했지만, 실제로는 이 부분 다음에 나오는 include에서 다른 perl프로세스의 해시를 참고하게 만들거다. 그래서 실제로 "map"이나 "set"은 객체이며, 평범한척 흉내내는 기만자고, "file"이라는 애도 만들 생각이다... 젠장 다시 명세를 써야겠어.
7. A. B (else case). 캐시를 순회한다. k, v가 있는데, k는 개무시하고, v가 치환까지 할줄아는 regex니 저걸로 치환를 시도한다. (치환 실패시 아무것도 안일어난다는점이 다행) "input -> *work* -> outout" 순서
7. B (EOF). EOF인데 케시가 비어있는가?
7. B. True. 정상이다. 파일 닫고, 종료한다.
7. B. False. 미친놈이 해제를 안시킨거다. "[WRONG]"을 output하고 "error : EOF : cqkf pragma syntax PDA isn't disallocated"를 errmsg로 stderr를 히고, 종료한다.

* Cqkf함수의 흐름은 대충 아래와 같다.
1. $2가 빈 문자열인지 아닌지에 따라 동작이 다르다. (blank case or else case)
2. A (blank case). "set"에 `$1`이 있는가?
3. A. True. 있으니, "map"과 "set"에서 `$1`의 인덱스를 지운다.
3. A. False. 없으니, "[WRONG]"을 출력한다. 미친새끼 없는걸 지우려 하다니. "error : line " . line . " : cqkf pragma syntax \"" . $1 . "\" is undefined yet"을 errmsg로 stderr하고, 종료한다.
2. B (else case). ('[^\s]*') x $2 인 배열을 CqkfArgv1라는 배열 변수에 할당한다.
3. B. 해당 배열 변수의 맨 처음에 $1을 insert하므로써, 거의 준비가 끝났다.
4. B. CqkfArgv2라는 배열에, '$1' ~ '$n'까지 $2개를 생성한다.
5. B. 해당 배열에 맨 처음에 $1을 insert하므로써, 마지막 단계만 남았다.
6. B. '/' . join('\s', CqkfArgv1) '/Cqkf\(' . join(',\s', CqkfArgv2) . '\)' . '/'를 map의 `$1`인덱스에 추가하고, `set`에 `$1`를 추가한다.

### B∨¬2B lang (BVN2BL) 「custom」 `include/` ; 주의할점은 완성된 코드가 아니라 설계사항 명세이다.

이 언어는 cqk로 작성된 언어다.

이딴 거 생각하는건 참... 죽느냐 사느냐 그것이 문제로다 ㅋㅋㅋ

이건 명세다. 구현이 아니다. 다 의사코드이다. 작동하지 않는 코드다.

#### (custom) include/be_cqkh.cqk
```cqkf
#!/bin/cqkh.perl -auto
#pragma once

#ifndef _BE_H
#define _BE_H(X) B##X
#define be _BE_H

#define EMPTY

#pragma Cqkf(be, 1)

#define EACH(T) typedef union { \
    unsigned T unsigned_one; \
    signed T signed_one; \
} each_##T

EACH(char);
EACH(short);
EACH(int);
EACH(long);
EACH(long long);

#undef EACH
#define EACH(T) each_##T
#define each EACH

#pragma Cqkf(each, 1)

typedef each_char byte1;
typedef each_short byte2;
typedef union {
    each int each_int_one;
    each long each_long_one;
} byte4;
typedef byte8;

typedef struct {
    unsigned b0 : 1;
    unsigned b1 : 1;
    unsigned b2 : 1;
    unsigned b3 : 1;
    unsigned b4 : 1;
    unsigned b5 : 1;
    unsigned b6 : 1;
    unsigned b7 : 1;
} bits;

typedef bits byte0;

#define PTR *
#define ptr PTR
#define JUST void
#define just JUST

typedef float IEEE754binary32;
typedef double IEEE754binary64;
typedef long double IEEE754binary80;

#define IEEE(X, Y, Z) IEEE##X##Y##Z

#pragma Cqkf(IEEE, 3)

typedef byte0 B0;
typedef byte1 B1;
typedef byte2 B2;
typedef byte4 B4;
typedef byte8 B8;
typedef IEEE 754 binary 32 B32;
typedef IEEE 754 binary 64 B64
typedef IEEE 754 binary 80 B80;

#endif
```

#### include/not2b_cqkh.cqk
```cqkf
#!/bin/cqkf.perl -auto
#pragma once

#ifndef _NOT2B_H
#define _NOT2B_H
#undef _BE_H
#undef be

#pragma Cqkf(be)

#undef EACH
#undef each

#pragma Cqkf(each)

#undef PTR
#undef ptr
#undef JUST
#undef just

#undef IEEE(X, Y, Z)

#pragma Cqkf(IEEE)

#endif
```

### nihilcc

void 타입의 변수를 생성할수 있으나, 그 변수명을 다시 코드에서 언급하는 순간, 즉 `□`라는 빈칸안에 들어갈 문자열인 심볼을 변수로 사용시, 해당 문자열은, 변수로 사용할수 없다. 저 빈칸 안에 들어갈 값은 영영 못쓰는거다.

이러니 만우절 버전 컴파일러인것.

기본적으로 `\b□\b`의 형태로 포착시,

"warning: □ est voidus sed adhibetur. Deus confundat hunc codicem."

이 ㅈㄹ을 하고, 그게 comment나 string같이 변수를 가르키는게 아닌 문자열이면, "warning: Homo □ invocare non licet."이고, 변수를 가르키는게 맞다면,

예컨데, `*□`같은 방식으로 쓰이면

"error: DEUS VOLT!! DEUS VOLT!! Occidamus paganum □!!"

이지랄을 하면서, 컴파일 에러가 뜬다. 런타임에서는 `void □` 같은 변수는 에초에 선언되지도 않았다. 즉, 메모리 공간도 할당하지 않은 참된 공(void)인것.

"뭐 이딴게 다 있어" 할수 있지만, 이것이야말로 참된 형식주의적 언어의 미덕이라고 생각한다.

사실은... a ~ z까지 그딴 이름들로 변수를 명명하는 놈들을 막기엔 제격인 컴파일러 아닐까...

아 참, 내부 스코프에서 새로 선언하는 경우 에러 안난다. 함수 안에서 새로 선언하므로써 뚫을수 있다. 물론 함수 안에서만 특정 심볼을 쓰는 셈이지만.

## F1N1TE (F I N I T E) ; 형식언어 (스팩)

「F I N I T E」는 tsv에서, 「F I N I T E」의 코어 언어 L이 셀에 들어갈수 있는 언어이다.

헤더는 ANTECEDENTE및 CONSEQUENTIA로 두가지여야만 한다.

ANTECEDENTE에 있는 문자열 키들을 순서대로 읽어서, CONSEQUENTIA에 있는 문자열 값들에 대응시킬수 있는데 이렇게

"ANTECEDENTE = CONSEQUENTIA"꼴의 구문들로 컴파일된다.

L의 형성규칙은 다음과 같다.

1. UJTL에서 말한 타입케스팅을 따를것
2. UJTL언어만 사용 가능
3. 온점 이전의 부호는 this만 허용
4. ptr기호는 보다 자유롭게 활용해도 좋다.
5. 인덱싱의 역할의 기호인 []의 경우에도 자유롭게 사용해도 좋다. 사실 jq언어에서, *.*나 *[숫자]식으로 하니까, 그런 기호가 자유인거다.

### UJTL : Jqible Type Lang

기본적으로

typedef union 소스코드 파일명; 식으로 만들 생각이여서, 초기값이 있다면, 그건 이미 C++이라는 소리임.

json으로 하면 struct부분이랑 union부분을 짜는데 문제가 되지 않을까 생각할수도 있는데, 그러나, `struct EMPTY { ~ }` 가 `struct { ~ }`로 평가 ㅋㅋㅋ 되기에 ㅋㅋㅋㅋ

깊이가 2n이면 struct, 2n-1이면 union인것이다.

타입은 대부분 `*.ujtl`/`*.ujt`같이 이 언어의 파일 형식이지만, `be`를 쓸수 있다..... (ㅅㅂ) 는 점이... 특이점이다.

타입케스팅시 허용되는 타입은 더 가관인데, be.h에서 사용한 타입은 다 오케이다...

number, string, bool외의 null이나 array를 보면,

array는 기존 타입명을 자동으로 배열로 바꿔주도록 컴파일할꺼고, null은 기본값 안설정한다는 뜻이다.

뭐... 이정도면 잘 요약한거 같은데.....

근데, 사실 C++지원 안하고, 초기화란게, 이 객체놈들은 기본적으로 초기화시켜주는 `void (*)(void*)` 형의 함수를 가지게 컴파일시킬거라서 그럼.

`typedef void (*ujtf)(just ptr)`식으로 이미 정의되어있는 bjtf.h를 쓰고, bjtf.h는 n2bjtf로 해제한다.

그렇다. 이건 cqkf형식이다. 그것도 nihilcc의 cqkf으로, nihilcqkf

에초에, json형식에서 js로 컴파일시킬려 하는것들이기 때문에

하아.... 뭐...

### 「F I N I T E」런타임

이건 무려 런타임이 C++이다... 아 현타와... 이런거 만드는거 싫어 ㅋㅋ

참고로 inhaltity라는 심볼은 기존에 void타입으로 선언되어있다. 예약어처럼 쓰려는 심보 보소 ㅋㅋㅋ

그리고, shared라는 심볼도 void로...

"NON HALT"는 NON을 이용하여, NON_HALT로, 그것은 "Boolean inhaltity = true; //"로 해석되고 (참고 ; 여기서 Boolean은 int에 비트마스크 1을 적용해준것 뿐, 이후를 주석처리한대에서, 확고한 설정이 가능 ㅋㅋㅋ ㄹㅇㅋㅋ)

SHARE라는 심볼은 void* share로 해석된다.

예를들어 ○.f1n은

```cqkh
#define F1N1TE(NAME, SRC) template <typename T> struct NAME : T; \
template <typename T> struct NAME { \
    template <typename G> finite NAME<G> operator()(void) { return (NAME<G>) this; } \
    finite void operator()(void) { \
        while (this.inhaltity) { \
            SRC
        } \
    } \
    finite static NAME<T>* operator()(T* x) { return (NAME<T>*) x; } \
};

F1N1TE(○, □)
```

여기에 빈칸에 코드가 들어가는거다.

저 의사코드 비스므리한 명세가 작동할거라 생각하는건 아니겠제?

암튼 `this()`같은놈들을 허용한다.

# 끝.

솔찍히 소설 설정 역겹네...