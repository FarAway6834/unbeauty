# Unbeauty 튜토리얼용 Edgar FW Script

## Edgar 유도
A. 계산상 시간선 인덱싱법

단계적인 장면들이 나열된 시간선을, 수열로 표현하여, "장면의 때"를 정의역으로 하는 수열로 만들어
Unbeauty처럼, 수열로 계산하고, 생각하는것.

B. 시간선과 상태변화 도입법

시간선상 어떤 속성 t가 변한다면, "계산상 시간선 인덱싱법"으로 해석하여, 상태변화를 단순히 "계산상 시간선 인덱싱법"의 인덱싱 결괏값에 따른 당연한 결과로 받아들일수 있다.

C. Edgarr Graph

Edgarr : Edg(e)-arr (엣지 가중치가 array의 값)

Edgarr의 가중치는 Array의 값이다.
Edgarr Graph의 충분하게 많은 Node가 불변이라 하자.
Edgarr Graph는 항상 Array에 대해 결정된다.
"시간선과 상태변화 도입법"을 쓰면,
모든 Edgarr Graph는 Array와 그 상태변화로 구성되기 때문에,

무한하게  Edgarr Graph를 다루지 않으면,
Edgarr Graph를 Array에 대한 Edgarr Graph로가는 계산의 결과로서 얻는다고 볼수 있다.

D. Edgarr Graph Machine

그럼 명령을 노드로, 분기를 Array의 변화로 처리하는 튜링머신과 그 언어를 생각해보자.

그때 그 튜링머신을 Edgarr Graph Machine라고 한다.

따라서, 단순히 분기는 {0, 1}의 치역을 가지는 수열을 결정해주면, 분기문이라는 Star형 그래프를 설명할수 있으므로, 수열에서 계산 가능하고, 해석 가능하다.

E. 튜링완전한 Unbeauty기반 컴파일 언어 Edgar

Edgar는
Unbeauty코드들을 저장하는 노드의 그래프를 처리하는 FW이다.

 - 노드필드 (NUL포함 문자열) : CommaSeperatedValue로 노드들의 값을 나열하고 각 인덱스를 노드로 취급.
 - AdjGraphField : AdjMetrix(인접행렬 by 2D BitMap)이나 AdjList(인접 리스트 by 2 Line CSV)로 표기되는 Edgar로, 실은 가중치가 연결여부가 되서 그걸로 표기된다.

이 언어는 정말 당연하게 Unbeauty로 컴파일 가능하며, 심지어 매우 쉽다.

 - M type : 인접행렬 AdjGraphField
 - L type : 인접 리스트 AdjGraphField
 - ML type : M과 L둘다 존재.

라이브러리적 기능)
분기문은 최적화된 코어(core) 함수로 평가된다.
사실 이게 전부지만.

## Edgar을 만든 이유.

나는 Unbeauty같은 esolang에 익숙해서 그런 분기(수식으로 분기를 구현하는 행위)가 전혀 이상하지 않지만, 그런 분기를 싫어하는 사람들이 있어서, 걍 Edgar를 만들었다.

쉽게 하라고 만든거라서 코드를 그래프로 작성하고 그리게 만든것이다.

해당 그래프는 편집이 인간이나 기계가 용이하게 만들었으니 Edgiter외에도 에디터로 작성하여도 좋다.

## Edgi Lang & Edgiter & Edgiter Data Pack

Edgi Lang은 RPN과 PN을 수학적 표기법으로 인식해서 해석하는 기능을 더한 Edgar 전처리기고 (주석지원은 뺀게, 파일에서 안읽는 부분에 추가하는 짓거리를 써서.),

Edgiter는 Edgi Lang 에디터다.

조건을 설정할때 Assistant가 있는데,
Edgiter Data Pack을 읽어서 동적으로 분기하여 작동하는 유사 AI나, Edgiter Data Pack을 실시간 개조하여 작동시키는 API로 AI랑 합쳐서 작동시킬수 있다.