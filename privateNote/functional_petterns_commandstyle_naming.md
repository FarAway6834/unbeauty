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