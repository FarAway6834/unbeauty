# LinguaFormalisLatina

Quick DB : CountingFilter에 x가 있다면, bool hash map에 x번째 인덱스를 가져오고 아니면 false를 반환하는 DB를 이르는 말.
Declinato Exceptio DB : Declinato Exceptio를 등록한 DB

LinguaFormalisLatina : 완전히 형식화된 라틴어 
1. Declinato 강제(forse)
2. Declinato Exceptio : 실제 Lingua Latina상에서 Declinato의 예외인 단어을 이르는 말. 대표적으로 라틴어 단어중 `puer`가 있다.
3. `#pragma LinguaFormalisLatina(Exceptio, ...)` : `...` 자리에 Declinato Exceptio DB에 등록된, 라틴어의 Declinato Exceptio를 넣어주면, 해당 Declinato Exceptio에 대해서는, Declinato Exceptio를 잡지 않는다.
4. Declinato Exceptio DB에 해당 어휘가 없는 걍우 `Exceptio Ignota I: Nescire Declinato Exceptio`라고 오류를 낸다. 컴파일러가 Declinato Exceptio를 모를 가능성을 염두해 둔거라 메세지가 약한거다.
5. `#pragma LinguaFormalisLatina(Compulsio, ...)`로 Exception허용을 그 라인부터 취소 가능하다.
6. `#pragma LinguaFormalisLatina(Compulsio, __VA_ARGS__)`나 `#pragma LinguaFormalisLatina(Exceptio, __VA_ARGS__)`는 Declinato Exceptio DB에 등록된 모든 단어들에 대해서 해당 작업을 진행한다.
7. `#pragma LinguaFormalisLatina(Declinato Exceptio DB, ...)`는 Declinato Exceptio DB에 해당 단어들이 정의되었다면, `#if LinguaFormalisLatina(Declinato Exceptio DB, ...)`를 참으로 정의한다.
8. `#pragma LinguaFormalisLatina(illud / id est violatio intentionalis, falsum • verum)`으로, 의도된 위반인지 아닌지를 제약한다. 기본값을 전체스코프 falsum, 그래서 기본적으로 모든 에러를 잡아낸다.
9. pragma중에서 Declinato Exceptio는 기본적으로 전부 Compulsio인게 기본 설정이다. 근데 라틴어를 이만큼만 제한해도 문법을 형식화 가능하진 않아서, `#pragma LinguaFormalisLatina(Intrudere / Extrahere, n.b. 라틴어 의미론에 대한 힌트 스크립트)`를 통해서, 자연어 의미론을 어떻게 해석해야하는지 힌트를 주는 부분을 만들었다.
10. 문장 중간에 `/`를 놓으면 이스케이핑된다.
11. `#define`을 이용한 메크로가, PCRE-substituate식으로 정의하는게 허용된다. 예컨데, `#define @이름 = 값`식이면 PCRE-substituate나 PCRE-match로 허용된다.` PCRE내부에서, 다른 `@이름`을 서브루틴으로 활용할수 있기에, PCRE-substituate 말고도, `subrootine</PCRE식/치환식/>`형태의 작성도 허용한다. 참고로, subrootine템플릿이 아닐시 define함수는 기본적으로 `${}`로 호출된다 갱각하면 된다.
12. `#define`에 EBNF의 비단말기호를 `@<이름>`으로 정의 가능하다. 내부적으로 PCRE로 컴파일된다.
13. #define에서 전처리기 지시어가 사용 가능하다.
14. 하스켈처럼 벡틱을 써서, define으로 정의한 함수를 중위표기법으로 사용 가능하다.
15. 심지어는 apply함수가 존재해서, 전위 표기법으로 "f `apply` •••"가 되고, revapply함수가 존재해서, "••• `revapply` f"로 역순도 가능하다. 심지어, 함수 인자 자체가 튜플이라, 인덱싱 • 슬라이싱 가능하다. 내부적으로 `@ARGV`가 `${}`로 접근하는 함수 인자다.
16. 문법 중간에 `\`를 작성하고 개행하면, 그 개행은 없언던거 취급 가능하다. (마지막줄에서 `\\`를 쓰면, `\`로 취급 안하니까, 이스케이핑 안됨 주의)