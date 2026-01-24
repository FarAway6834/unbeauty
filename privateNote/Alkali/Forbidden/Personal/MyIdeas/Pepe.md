# **P**epe : **E**bnfible**P**crew - **E**bnf (EBNF that used on EBNFiblePCREW)

**P**epe : **E**bnfible**P**crew - **E**bnf (EBNF that used on EBNFiblePCREW)

## PSSL (Pepe Syntax Sugar Layer)

Pepe의 문법 설탕 파트다. 사실은 Pepe는 많는 부분이 문법 설탕으로 되어있다.

예컨데,

```EBNF
(□)<○|●>
```

는 PCRE기준

```PCRE
(□){○,●}
```

에 해당한다.

왜 bra-cket의 내적의 기호를 썼냐면,

원래 EBNF에서, ...문장 작성중...

...작성중...

## PwP (Pepe without PSSL)

PSSL에서 지원하는 문법이 결어된 Pepe로, 문법 설탕으로 만들어진 다수의 문법이 존재하지 않는다.

여기서 지원되는 문법이라고는, BNF의 문법과 그룹, 그리고 '!'밖에 없다.

...작성중...

## Pepe Core

Pepe Core란, Pepe를 구성하는 최소 문법이다. Pepe를 구성하는 문법 자체가 제한되어있지만, Pepe Core문법에 해당하는 문법으로 Pepe의 모든 문법이 에초에 표현 가능하다.

그래서, Pepe는 Pepe Core로 컴파일된다.

PwP에서 알수 있듯, Pepe는 사실 그룹이 별로 필요 없다.

그렇다는 점에서 착안해서, 그룹은 전부 랙싱해서 전개해버리면 그만이라는 사실을 알 수 있다.

그렇기에, Pepe는 파싱하기에 편한, 튜플의 제귀적 정의를 이용해서,

문법명(부가요소1, 부가요소2, ..., 부가요소n)을

문법명(부가요소1, 문법명(부가요소2, ..., 문법명(부가요소n-1, 부가요소n) ... ))로 이항관계마냥 단순화시킨다.

에초에, regex 문자열셋의 합타입 • 곱타입 • 에러문법타입이라는 세가지 타입에 있어서, 합타입 • 곱타입만이 두가지 이상의 인자를 받고, 멱등 가환반군(합타입은 가환반군, 곱타입은 가환 모노이드 (왜냐하면 empty가 항등원이다))이기 때문이다. 사실상 집합 S에서 선택함수로 요소를 하나씩 빼는 이항 연산을 취해주는거나 다름없다. (유한집합에 대해서는 선택함수가 존재한다는거 누구나 알거다)

### Pepe Core의 문법

빈칸 □, ○, ●에 대하여,

0. 문자열 (사실상 PCRE의 캡쳐를 문자열로 취급한다)

```EBNF
<□> := "○"
```

PCRE를 문자열로 취급하는 발상이라, 문자열들의 집합타입에 가까운데, 문자열 타입이라니 솔찍히 내가만들었지만 유쾌하다 ㅋㅋ

1. 합타입

```EBNF
<□> := <○>|<●>
```

2. 곱타입

```EBNF
<□> := <○><●>
```

3. 에러 타입

```EBNF
<□> := <○> ! <●>
```

이렇게 내가지 구문으로 단순화 가능하며, 이는 PCREW의 서브루틴이자 캡쳐 객체로 다루고 싶었기 때문이었고, 그래서 여러가지 트리 내 객체 접근자와, 플래그을 이용한 Pepe Core Runtime을 만들었다.

이 트리 모델은 이항트리가 되니까 갓벽하다고 생각했기 때문이고,

트리의 각 오브젝트는, 패턴의 역할을 해야한다고 봤기 때문이다.

왜냐? : Leftwise식으로 Rightwise식이 분류된다는 방식이니까

### Pepe Core Runtime

* 들어가기 앞서 : darkside에 대한 설명

곧 설명할거지만, 에러가 나는 상황에서 특별하게 side-effect를 만들어주는 일회용 서브루틴 매치 표현식이다.

C++에서 에러가 나면 스택 트레이스가 많다고 투덜거리는데, 그건 에러 관리를 잘못했기 때문이라고 지적할수 있다.

물론 그 스택트레이스는 짜증난다. "ぶっ殺す"라고 외치면서 개빡칠만큼.

여기도 그런식이다. 에초에, 작성자가 PCRE로 코딩하는건 오늘(2026.01.24)이 처음이라서 별로 죄책감이 없다.

에러가 났다면, darkside에서 이미 탐색을 마친 뒤다.

(?:(?<darkside 이름>))의 방식으로 이용되는데, darksize자체의 캡쳐값은 사용하지 않고, darksize에 매칭되면, darksize내의 서브트리가 정의된다.

darksize는 "?>"와 달리 "?:"가 서브트리를 기록하는 side-effect를 가지기 위해 존재한다.

그렇기에, darkside는 호출하면 안되는 pepe내부 시스템의 함수인것이다. (내부꺼고 호출하면 안된다는게 에초부터 너무 당연하지만 (~~이름부터가 바로 SF냄새난다~~))

만일, EBNF에서, '!'로 인한 에러가 났다면, darkside의 side-effect가 실행된다.

굳이 용어풀이하자면, pepe's darkside = side effect based pepe system's non referenced named math group subrootine expr라고 이해하면 된다.

'!'위반해서 에러가 생긴 경우엔 -> darkside는 에러가 참임을 현제 객체로 기록된다.
'!'를 위반하지 않았고, 새부 내용에서 오류가 생겼을때 -> darkside는 에러가 참임을, 현제 객체고 기록한다.

그리고 마지막으로 밀봉 작업을 진행하는데, 

'!'를 위반한 경우에, 매인 표현식 내에서만 비원자적을 쑨다.

만약, flag확인 함수를 호출했다면, 캡쳐 타입이 아니라 텍스트 타입인 경우를 제외하고,

'!'를 위반한 경우, flag확인 함수 내부 : 

1.bool. 원자적 수량자로 여부를 확인한다.
2.true. 자신의 오류 원인 = 자신의 캡쳐로 할당
2.false. 오류 = 빈칸 할덩

합타입의 경우, flag확인 함수 내부 : 

1.bool. first가 select되었는가? (격리된 서브루틴이 따로 존재한다)
2.true. 자신의 오류 원인 = first
2.false. 자신의 오류 원인 = last

곱타입의 경우, flag확인 함수 내부 : 

1.bool. 원자적 수량자로, first에서 오류가 났는지 확인한다. (격리된 서브루틴이 따로 존재한다)
2.true. 자신의 오류 원인 = first
2.false. 자신의 오류 원인 = last

참고로, 격리된 서브루틴은, 조건문 처리를 위해, 참인 조건을 매치하는거다.

* 들어기기 앞서를 종료. 계속해서 본론 설명

0. emtpy

```PCRE
(?(DEFINE)
    (?<pepe_emtpy>)
)
```

로 기본 정의됨.

1. sum type

```EBNF
<□> := <○>|<●>
```

는

```PCRE
(?(DEFINE)
    (?<pepe_main_□>
        (?<pepe_group_first_□> (?&pepe_main_○)
        )|(?<pepe_group_last_□> (?&pepe_main_●))
    )
    (?<pepe_flag_□>
        (?((?>(?&pepe_main_□)))
            (?((?>(?&pepe_true)))
                (?<pepe_flag_sumtype_□>
                )|(?<pepe_flag_prodtype_□)(?<pepe_flag_texttype_□>)(?<pepe_flag_errible_type_□>)
            )
            (?(<pepe_flag_errible_type_□>)
                (?((?>(?&pepe_group_first_□)))
                    (?:(?<pepe_flag_darksideof_□>
                        (?<pepe_flag_error_true>
                            (?&pepe_main)
                        )
                    )) | (?<pepe_flag_error_false>)
                )
            )
            (?(<pepe_flag_sumtype_□>)
                (?((?>(?&pepe_group_first_□)))
                    (?<pepe_flag_first_matched_□>
                    ) | (?<pepe_flag_last_matched_□>)
                )
            )
            (?(<pepe_flag_prodtype_□>)
                (?<pepe_subtree_first_□>
                    (?((?>(?&pepe_main_□)))
                        (?&pepe_group_first_□)
                    )
                )
                (?<pepe_subtree_last_□>
                    (?((?>(?&pepe_main_□)))
                        (?>(?&pepe_group_first_□))
                        (?&pepe_group_last_□)
                    )
                )
            )
        )
    )
)
```

로

2. product type

```EBNF
<□> := <○><●>
```

는

```PCRE
(?(DEFINE)
    (?<pepe_main_□>
        (?<pepe_group_first_□> (?&pepe_main_○)
        )(?<pepe_group_last_□> (?&pepe_main_●))
    )
    (?<pepe_flag_□>
        (?((?>(?&pepe_main_□)))
            (?((?>(?&pepe_true)))
                (?<pepe_flag_prodtype_□)
                )|(?<pepe_flag_sumtype_□>(?<pepe_flag_texttype_□>)
            )
            (?(<pepe_flag_sumtype_□>)
                (?((?>(?&pepe_group_first_□)))
                    (?<pepe_flag_first_matched_□>
                    ) | (?<pepe_flag_last_matched_□>)
                )
            )
        (?(<pepe_flag_prodtype_□>)
            (?<pepe_subtree_first_□>
                (?((?>(?&pepe_main_□)))
                    (?&pepe_group_first_□)
                )
            )
            (?<pepe_subtree_last_□>
                (?((?>(?&pepe_main_□)))
                    (?>(?&pepe_group_first_□))
                    (?&pepe_group_last_□)
                )
            )
        )
    )
)
```

NOTE : 이제봐서 그런데, if-else같은 흐름을 수정할거다. 저런식의 if다발은 ㅈ도 매치 안될거다. 그러니 해당사항은 지적하지 말아달라.
NOTE : 그리고, 아직 코드를 다 짜지 않아서, 로직을 다 안적어서 그런데, errible type에서는, (?((?:(?<pepe_main_darkside_of_□> (?<pepe_group_last_□> (?&●))))) \k<pepe_group_last_□> | (?<pepe_group_first_□> (?&○)) 로 잘 내부 소스를 작성할 생각이니, 해당사항도 지적 ㄴ.

...작성중...