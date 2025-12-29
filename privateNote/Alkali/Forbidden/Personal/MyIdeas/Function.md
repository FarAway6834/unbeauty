# 함수는 존재하는가?

형식언어 L의 이론 T에서, 함수로 해석되는 대상 f에 대해, xRy : f(x) = y라 하자.

FunctionalRelationship(R) : ∀x, y, z, xRy ∧ xRz → y = z
FRCall(R)(x) = εy xRy
dom FRCall = {x | FunctionalRelationship(x)}
dom FRCall(R) = {x | ∃y, xRy}
codom FRCall(R) = R[dom FRCall(R)]
codom FRCall = {f ∈ Func(X, Y) | X = {x | ∃y, xRy}, Y = R[X], FunctionalRelationship(R)}
functionize(S, R) = (dom FRCall(R), codom FRCall(R) ∪ S, R)

∃!y (FRCall(R)(x) = y)이다. 왜냐하면, FRCall의 정의역은 FunctionalRelationship이고, 모든 FunctionalRelationship은 오른쪽 유일성을 가지므로, FRCall(R)은 함수다.
FRCall(R)의 정의역은 {x | ∃y, xRy}이며, codomain은 R[dom FRCall(R)]이다. 즉, FRCall은 FunctionalRelationship에서 {f ∈ Func(X, Y) | X = {x | ∃y, xRy}, Y = R[X], FunctionalRelationship(R)}로 가는 함수이기 때문이다.

functionize함수를 보면, S ⊆ codom FRCall(R)일때, functionize(S, R)은 전사 사상이다. 즉, 정의역을 제한해서, graph가 바뀌지 않는 한에서, graph f = R에 대해, R이 그래프인 함수들은, {functionize(S, R) | Set(S)}이다.

그렇지만, 과연 "EXSTAT ALIQUIS FunctionalRelationship"인 진술이 참이될수 있는가? (해당 문장의 주사가 존재하는가?)

고1 집합과 명제 단원 이전에서는, 존재하는 대상으로 숫자만 제시했는데, 주사 "FunctionalRelationship"이 존재한다, 즉, FunctionalRelationship ≠ ∅이려면, 집합이나 함수의 존재를 허용하거나, 술어의 존재를 허용해야하는데, 중학교 수학에선 그러하지 아니하였으므로, 유명론적 관점 ; 함수라는 대상은 우리가 수학식에 대해 이름붙인 대상일 뿐이지 않는가?

예컨데, 파동함수같은건, 과학 이론의 모형(모델)로 알맞은 언어가 함수를 기술하는 언어였던것이 아닐까?