## Blep

### 1. BLEP(BitLevelExtendedPCRE)

`\blepbit`는 무조건 연속해서 여덟번 나와야 한다.

1. num-capture

`(\blepbit)`

2. name-capture

`(?<□> \blepbit)`

3. num-use

`\□`

4. name-use

`\k<□>`

각각이 1bit이다.

그리고 8번 연속되는 동안 : 

1. 1 ~ 4중 하나
2. 1 ~ 4중 하나
3. 1 ~ 4중 하나
4. 1 ~ 4중 하나
5. 1 ~ 4중 하나
6. 1 ~ 4중 하나
7. 1 ~ 4중 하나
8. 1 ~ 4중 하나

이렇게 놓이게 강제되기 때문에,
바이트 단위에서 비트필드처럼 사용해야만 한다.

세가지 케이스가 존재하는데,

1. cap-only : captured만 사용되었다
2. use-only : use만 사용되었다
3. the-both : 둘다 사용되었다.

#### 세가지 케이스의 내부적 처리

blepure : pure pettern of blep

```regex
(?<b0> \blepbit)(?<b1> \blepbit)(?<b2> \blepbit)(?<b3> \blepbit)(?<b4> \blepbit)(?<b5> \blepbit)(?<b6> \blepbit)(?<b7> \blepbit)
```

은 

1. num-capture

`(\blepure)`

2. name-capture

`(?<□> blepure)`

3. num-use

`b○`를 가져온다면,

`\k<□_b○>`

4. name-use

`b○`를 가져온다면,

`\k<□_b○>`

#### 구현은?

실제로는 \blepbit랑 \blepure만 존재한다. 즉, 나머지 cap-only, use-only, the-both는 syntax sugar이고 제 4 의 방법인 blepure만 존재한다.

\blepbit는 사실 \blepure로 캡쳐하고, 커서는 이동하지 않았을때, 재검사를 하는 용도로만 작동한다.

한마디로 속임수다.

즉, cap-only는 재캡쳐로 네이밍한것 뿐이고, use-only는 네이밍된 항목에 대한 조합으로, blepure의 use들의 syntax-sugar 화로, regex스타일일 뿐이다. blepure의 use가 진짜 비트의 조합을 하는거다.

the-both의 역할은,

\blepbit인 비트와, 아닌 비트가 있을텐데, 그렇게 만들어진 한 바이트는, 일반 PCRE에서 검사가 가능하다.

그렇기에 \blepbit는 일반 perl regex (PCRE)로 컴파일되는 문법 설탕일 뿐이다.

#### blepure

\blepure를 통한 use-only입력의 연쇄 이용

즉, \k<□_b○>의 연쇄 이용 문법을 blepure-use-chain이라고 부른다.

blepure의 문법은, \blepure과 blepure-use-chain이 전부인거다.

`\k<□_b○>\k<□_b○>\k<□_b○>\k<□_b○>\k<□_b○>\k<□_b○>\k<□_b○>\k<□_b○>`에서...

음... 

사실상...

```cpp
typedef struct {
    unsigned char b0 : 1;
    unsigned char b1 : 1;
    unsigned char b2 : 1;
    unsigned char b3 : 1;
    unsigned char b4 : 1;
    unsigned char b5 : 1;
    unsigned char b6 : 1;
    unsigned char b7 : 1;
} uc8bitfield;
```

캡쳐될시, uc8bitfield자료형인 셈이다.

그렇기에, blepure-use-chain으로 조합이 가능한거다.

`\C`크기의 8bit char에 대해서,

MATCHING : \C일 뿐.
INDEXING : 1, 2, 4, 8, 16, 32, 64, 128이라는 각 비트마스크로 인덱싱후 절적히 k비트 시프팅
PLACING : 1, 2, 4, 8, 16, 32, 64, 128이라는 8차원 비트 벡터 공간에 대한 기저를 곱해줘서 합해주는 방식으로 만듬

그렇다. \blepure는 컴파일 타임 타입일 뿐이다.

그저, 한 비트를 다루기 위한 타입이면, INDEXING이랑 PLACING을 컴파일 타임에 허용할 뿐이다. 그뿐이다.

#### 정체

Blep은

1. perl Blep : perl에서 PCRE에다가 ${}로 함수 호출하는걸로 컴파일되고
2. C Blep : C에서 PCRE2.h에다가, ?C로 Callout함수 호출하는걸로 컴파일된다.

### 옵션

여기서만 오리지널로 제공하는 옵션이 존재한다.

#### tri-bit runtime memory

"_bleptbrm"라는 모드가 정규식의 모드 부분에 붙어있다면...

즉, `□/□/□/□_bleptbrm` 꼴이거나, `□/□/□_bleptbrm` 꼴이면, 작동한다.

바로, 시작시 아무 8bit char (주로 ASCII)를 입력 문자열의 맨 처음에 패딩하는거다.

C의 경우 아무런 `const char padchr;` 나 쓰래기 값이라도 좋으니 참조하고,
perl의 경우, `my $const_char_padchr = "x";` 식으로, 대충대충 문자 하나 박아넣는 방식이다.

사실 내부적으로...

`s/(.*?)/x$1/gm`이딴식으로 존나 대충 구현할수 있다는게 특장점이다.

#### 펙트

이것은, Blep을 프로그래밍언어로 마개조하려는 사악한 암흑의 프로젝트를 위한 복선이다.