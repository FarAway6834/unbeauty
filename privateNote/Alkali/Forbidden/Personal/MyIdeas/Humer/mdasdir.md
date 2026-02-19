# mdasdir (markdown as directory) 파일 포멧 (확장자 `*.mad`) 구상

세줄요약 : mad에서는 마크다운이 디렉토리라고 정의했으니까, 디렉토리는 마크다운으로 취급되게 된다. mad가 High-abstract mdasdir이기에, mad디랙토리는 markdown에 서브셋으로 호환 • 호환 안되는 부분마저 markdown용으로 컴파일시 호환인 json directory의 markdown표기다.

기초 지식은
0. 핵심 구조
1. LowAbstracted mdasdir
2. HighAbstracted mdasdir
이다.

이 문서의 결론을 여기에 박겠다.
0, 1, 2에서 소개한 lmad와 hmad는 다음 세가지 컴파일러를 통해서 구현되는, 파일 아카이빙 • 개발자의 직접 Editing과 디렉토리 구조 표현식용 Expression • 문서화/프로젝트화 형식이다.
1. mad 컴파일러 (markdown화와 json파일 디렉터리화가 존재하며, 힌트를 주지 않는 한, 자동으로 lmad인지 아닌지 유무를 추론한다. lmad인데 markdown화를 요구하면, decompile불가라며 에러를 뱉는다.)
2. lmad컴파일러 : json화 컴파일러고, mad컴파일러에서, `--islmad`라고 힌트를 줘야 실행된다.
3. hmad컴파일러 : markdown화와 json파일 디렉터리화가 존재하며, markdown화는 오직 hmad컴파일시만 가능하다. `--ishmad`라고 힌트를 주면 실행되는 놈이고, `--markdownize`, `--jsonize`, `--lmadize`가 있으며, `--jsonize`는 `--lmadize`이후, lmad컴파일러로 컴파일하는 방식인데, lmad파일을 생성할세도 없이 다이렉트로 꽃아서 `--lmadize`를 경유해서 jsonize하는것보다 훨씬 좋은 방법이다.

mad는 컴파일러가 에러시 템플릿 메타 프로그래밍을 하는 경우를 제외하고 에러메세지 없이 종료되므로, 실제 에러 처리는 디버거가 먼저 유효성 검증을 하고, 템플릿 메타 프로그래밍용 사이트를 미리 방문해서, 캐시하고 (캐시했기에 다음 방문은 생략된다. 방문 요청에 대한 응답이 프록시 서버처럼 즉시 오는 셈인 방식이다) 2차 유효성 검증을 하고, 버그 목록을 출력하거나, `--nongreedy-errfind`시 목록이 아닌 가장 빠르게 발견된 버그를 출력한다.
템플릿 메타 프로그래밍 오류는, 해당 사이트에서 쿼리를 없엔 순수 path만 있는 html페이지를 반환하면, 그 페이지를 렌더링하는 방식으로 보여준다.

## 0. 핵심 구조

디렉토리용)

/$(?:\n#(*COMMIT)(*FAIL)|[\s\S]*?)```markdown\n(?<value>[\s\S]*?)\n```(?<after>[\s\S]*?)^/

파일용)

/$(?:\n#(*COMMIT)(*FAIL)|[\s\S]*?)```(text/plain)?\n(?<value>[\s\S]*?)\n```(?<after>[\s\S]*?)^/

/(?(DEFINE)(?<HexBin> $(?:\n#(*COMMIT)(*FAIL)|[\s\S]*?)```application/octet-stream\n(?<value> ([0-9A-F]{2}([\s\n])?)*?)\n```(?<after>[\s\S]*?)^)(?<Base64Bin> $(?:\n#(*COMMIT)(*FAIL)|[\s\S]*?)```application/octet-stream;base64\n(?<value>[0-9a-zA-Z+/=\n\s]*?)\n```(?<after>[\s\S]*?)^)|(?<main> 「base64화 알고리즘」)) (?&main)/

/(?(DEFINE)(?<HexText> $(?:\n#(*COMMIT)(*FAIL)|[\s\S]*?)```application/base64\n(?<value> ([0-9A-F]{2}([\s\n])?)*?)\n```(?<after>[\s\S]*?)^)(?<Base64Text> $(?:\n#(*COMMIT)(*FAIL)|[\s\S]*?)```text/plain;base64\n(?<value>[0-9a-zA-Z+/=\n\s]*?)\n```(?<after>[\s\S]*?)^)|(?<main> 「base64화 알고리즘」)) (?&main)/

계산 : application/octet-stream은 application/octet-stream;base64로 컴파일됨)
Hex세글자를 base64두글자로.
세 바이트당 base64 내 문자로
3n + 1바이트에서, □□== (000000)
3n + 2바이트에서, □□□= (0000)

n = 2m + 1시, 3n + 1 = 6m + 1 + 3 = 6m + 4
3n + 1핵스에서, 3m + 2바이트 패딩
n = 2m시, 3n + 2 = 6m + 2
3n + 2핵스에서, 3m + 1바이트 패딩

0. 핵스 길이가 3의 배수가 아니면, "0"을 추가하면, 플래그를 null에서 true로
1. 그랬는데도 핵스 길이가 3의 배수가 아니면, 플래그를 true에서 false로
2. 0xXYZ에서, XY를 한글자로, YZ를 한글자로 변환해서 합치는걸 핵스 길이를 3으로 나눈 몫만큼 반복
3. 플래그가 참이면, 끝에 "=="를 추가한다. 거짓이면 0xXY를 한글자로 바꿔 추가하고, 끝에 "="를 추가한다.
4. 나는 미친새끼라, 이걸 PCRE로 구현할 생각이다.

## 1. LowAbstracted mdasdir (`*.lmad` 파일)

만약 단일파일만 있는 경우라면

````markdown
# 「`*.lmad` 파일명」

```「lmad에서 허용된 MIME타입 : markdown • application/octet-stream • application/octet-stream;base64 • application/base64 • text/plain;base64 • 미명시」
「값」
```
````

여러 파일이 있는 디렉터리라면

````markdown
# 「`*.lmad` 파일명」

## 「파일명 1」

```「오로지 markdown만 허용된다. 그렇지 않으면 전역 매칭실폐를 낸다」
「값」
```

...

## 「파일명 n」

```「오로지 markdown만 허용된다. 그렇지 않으면 전역 매칭실폐를 낸다」
「값」
```
````

이런식이다. 당연히 핵심내용에서 정의한게 쓰일수밖에 없다.

디렉토리 내의 디렉토리는 내부 lmad파일에 의해 결정되는것이다.

### MIME타입 이름을 저따구로 지은 이유

1. application/base64 : 텍스트 데이터를 Base64로 인코딩한 경우 명시적으로 사용할 수 있는 이름 (표준)
2. application/octet-stream : 많이 쓰이진 않는다만, 바이너리인 경우에 쓰이는 놈이다. (표준)
3. text/plain : 이건 해명할것도 없다. 이 분야에서 바보가 되는 사람이 아니라면, 이게 텍스트용 MIME타입이라는걸 안다.
4. `;base64` : MIME에서 base64인코딩을 함은 이렇게 명시해야한다 (표준! 중요한 표준!)
5. mad파일의 형식을 markdown으로 고정한 이유는, mad의 뜻이 markdown as directory. 즉, 마크다운을 디렉토리로 취급하는 형식이기 때문이다. 마크다운이 디렉토리라고 정의했으니까, 디렉토리는 마크다운이다

## HighAbstracted mdasdir (`*.hmad` 파일)

hmad는 lmad로 컴파일되는 lmad의 문법설탕이다.
즉, hmad는 lmad의 확장이며, mad라 함은 hmad를 칭하는거다.

### MIME 타입 명시

hmad URI라고, 다음형식을 가지는 URI에서 lmad타깃으로 컴파일시 컴파일할 MIME 타입명을 미리 정의한다. (세가지 종류가 있다)
1. `hmad://「http서버명」/「path」?「MIME 타입명」 = 「lmad상 MIME 타입 대응 / 인코딩 대응 (인코딩 대응시 "base64 + 인코딩명"이거나 "인코딩명"이다.) 」`
2. `hmad://「http서버명」/「path」?「MIME 타입명」 = 「lmad상 MIME 타입 대응 / 인코딩 대응 (인코딩 대응시 "base64 + 인코딩명"이거나 "인코딩명"이다.) 」# hmad://「http서버명」/「단축된 hmad 타입선언 URI의 path • query string • fragment」`
3. `hmad://「http서버명」/「단축된 hmad 타입선언 URI의 path • query string • fragment」`

한 파일에 hmad URI는 여러줄 선언할수 있으며, JS fetch로 가저오는 과정에서, 해당 사이트를 실행하는 셈이므로, hmad를 제공하는 http서버 (사실상 https서버지만 http로 접속시 리다이렉트되는것을 포함) 는 구글사급의 권위를 가지고 있지 않으면 사용하지 말라는 보안 권장사항이 존재함.

1번의 경우, 쿼리대로 선언됨
2번의 경우, fragments부분과 아닌 부분을 굳이 1번과 3번을 동시에 두가지 나열하지 않고도 한줄에 나열할수 있게 해줌. (fragments부분이 먼저 선언됨)
3번의 경우 JS fetch를 통해서, 1번이나 2번의 형식으로 리다이렉트되는 주소를 추적함. 3번의 형식에서 쿼리가 되는 이유는 "템플릿 메타 프로그래밍"같은 추상화 기능 제공 가능성을 열어둘 목적이기 때문. (물론 규격은 서버마다 다르다. 자기맘대로 구현하라는거다)

### 다중 중첩 hmad 디랙토리 컴파일

1. 인용블럭을 이용한 sub-docuement
2. `#`깊이 1 ~ k를 이용한 sub-docuement
3. markdown타입 sub-docuement를 통한 sub-docuement

#### 1. 인용블럭을 이용한 sub-docuement

만약 기존 `#` 사용 깊이가 k일때

```markdown
 > 
 > # 「key」
 > 
 > 「value」
 > 
```

를 쓰면, 

```markdown

#{k}#  「key」

「value」

```

이렇게, k개의 `#`이 박제된다.

정확히는,

1. k개의 `#`이 markdown타깃 컴파일시 인용블럭으로 변하고 ••• 【markdownize】
2. 인용블럭이 lmad타깃 컴파일시 k개의 `#`으로 변하기에
3. 인용블럭이든 k개의 `#`이든 문법적으로 동치다.

#### `#`깊이 1 ~ k를 이용한 sub-docuemen

기존 markdown에서는 `#`의 깊이가 5가 최대였다면, hmap에서는, 5이상인 경우, 강제 인용문 취급된다.

3 ~ 5인 경우는 1 ~ 2인 부모 도큐먼트가 존재하게 된다.

예컨데,

```markdown
#{k=1~n} 「디렉토리명」

#{k + 1} 「파일명 1」

...

#{k + 1} 「파일명 n」
```
식으로도 가능해서, lmad로 컴파일시, **해당 디렉터리를 파일로 만든다**

그러므로 컴파일 방식은 두가지다.
1. 저번에 소개한 markdown 타깃이면, k > 5에 대해서만, k개의 `#`이 markdown타깃 컴파일시 인용블럭으로 변한다.
2. 이번에 소개한 lmad 타깃이면, **해당 디렉터리용 `#`블럭을 mad 파일 코드블럭으로 바꾼다 (제귀적으로)**
3. 그러므로, 컴파일시 동치인 동치관계를 주었을때 동치인거지, 컴파일러에따라 다르므로, 구문론적으로 다르고 의미론적으로만 동치다.

#### markdown타입 sub-docuement를 통한 sub-docuement

알다시피 mad에서 markdown타입 코드블럭은, 디렉토리 대신 mad파일을 써서, 파일을 작성하는걸로 디렉토리를 표시하는 방법이다.

그러므로, hmad파일의 소스코드를 적거나 lmad파일의 소스코드를 적지 않으면 문법 오류다.

근디 에초에, 코드블럭이랑 블럭문단 제목이 아니면 죄다 주석처리하니까 마크다운처럼 쓸수있다는게 펙트지만...

**이부분의 컴파일은 오직 한가지만 있으며, 두 경로가 있다. **
1. hmad파일 소스코드라면 내부 디렉토리들을 hamd 파일로 변환한다
2. 1번을 통하서 hamd파일을 중첩한 hmad이 될순 있어도 lmad은 아니므로, 파일들을 수평적으로 모아놓은 hmad파일 내부의 hmapd일을 1번 과정을 제귀적으로 반복하여, 결과적으로 lmad파일을 만든다.

### 컴파일 과정의 요약

요컨데, hmad의 lmad로의 컴파일은, 확장인 문법설탕을, 확장이 아닌 문법의 조합논리로 컴파일하는 수렴 과정이다.

그러므로, hmad는 사실상 lmad의 문법설탕이다

왜냐하면, 모든 hmad 구문은 템플릿 메타 프로그래밍을 제외하고는, 그냥 PDA수준의 문법설탕일 뿐이다. MIME타입 대응도, 그냥
1. 링크 접속 (쿼리로 리다이렉트되는 과정이 템플릿 메타프로그래밍이든 아니든 개무시하고 일단 점속(=실행) 한다)
2. 쿼리 받음
3. 쿼리를 박아넣늠
일 뿐이다.
그러므로, JS fetch를 외부 서브루틴으로 쓰는 PCRE를 통해서, PCRE match group subrootine들로 프로그래밍될 예정이다.
