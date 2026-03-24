# toy project

무한곱같은 반군 연산을 무한연쇠한거를 100%명시적인 논리를 통해서 구축하기 위한 고전적인 스타일의 정의 제작중...

## 3월 모의고사 보면서 떠오른거

충분히 대수적인 방법과 해석적인 방법을 섞어서, 모델론적인 방법을 쓰면, 실수를 만들수 있을듯?

```python
#n.b. 이건 python코드가 아닌 수학의 numpyic notation (numpy와 lambda랑 조건부 표현식만을 가지고, 선형대수적 객체에 대한 상수나 함수를 정의하는 notation)임.
#n.b. numpyic notation은 비형식적이고 엄밀하지 않은 표기임. 코드를 어떤 수학적 객체로 해석할지는 주석을 참고할것. (무려 정의역을 명시 안할정도로 비형식적이다.)

from functools import wraps as __smart_deco_wraps

def TailRequationOptimization(func):
	Φ, f = func()
	@__smart_deco_wraps(func)
	def wrapper(ret):
		while p: p = Φ(ret := f(ret))
		return ret
	return wrapper

#n.b. TailRequationOptimization는 numpyic notation의 처음에 항상 명시하는 메직넘버이므로 무시하도록 하자. 심지어 이 소개 주석까지도 메직넘버임

from numpy import array as tensor # 스칼라가 정수라면 unsigned인것마냥 간주하는 비형식적인 직관중심 전개를 할거니 주의하고 따라오자.
from numpy.linalg import matrix_rank as rank

xhat = tensor([[1, 0]]) # 열벡터 x hat
yhat = tensor([[0, 1]]) # 열백터 y hat
RevRow = tensor([
	[0, 1],
	[1, 0]
]) # 선형사상으로써의 2×2행렬 RevRow
RevColumn = lambda M : (RevRow @ M.T).T # 2×2행렬에서 2×2행렬로 가는 2×2행렬이라는 대수구조 모델의위 함수 RevColumn
FirstVector = lambda M : M[:, 0].reshape(1, 2) # "2×2행렬의 도메인 = 1×2행렬의 도메인에 1×2행렬의 도메인을 탠서곱"으로 보고, 1×2행렬을 kuratowski-pair에 스칼라를 담은걸로 보면, ((M[0][0], M[1][0]), (M[1][0], M[1][1]))이므로, first <x, y> = x인 연산을 가해준것 뿐.
LastVector = lambda M : FirstVector(RevColumn(M)) # "2×2행렬의 도메인 = 1×2행렬의 도메인에 1×2행렬의 도메인을 탠서곱"으로 보고, 1×2행렬을 kuratowski-pair에 스칼라를 담은걸로 보면, ((M[0][0], M[1][0]), (M[1][0], M[1][1]))이므로, last <x, y> = x인 연산을 가해준것 뿐.
acess11 = lambda M : xhat @ FirstVector(M).T # 2×2행렬에서 1×1행렬로 가는 함수
acess21= lambda M : yhat @ FirstVector(M).T # 2×2행렬에서 1×1행렬로 가는 함수
acess12 = lambda M : xhat @ LastVector(M).T # 2×2행렬에서 1×1행렬로 가는 함수
acess22 = lambda M : yhat @ LastVector(M).T # 2×2행렬에서 1×1행렬로 가는 함수
untensorize = lambda M : M[0][0] # 1×1행렬에서 스칼라로 가는 함수
min = lambda v : untensorize(xhat @ v.T) if untensorize(xhat @ v.T) > untensorize(yhat @ v.T) else untensorize(yhat @ v.T) # 작은 원소를 뽑는 함수 # 에초에 bultin method min을 사용하지 않는 이유는, 수학적으로 최소한의 정의를 쓰려했기 때문이고, builtin method는 키워드가 아니고, builtin스코프에 선언되어, 따로 해당 이름으로 정의되지 않을때 호출되는거라 이 구문은 유효함.
max = lambda v : untensorize(yhat @ v.T) if untensorize(xhat @ v.T) > untensorize(yhat @ v.T) else untensorize(xhat @ v.T) # 작은 원소를 뽑는 함수 # 에초에 bultin method max을 사용하지 않는 이유는, 수학적으로 최소한의 정의를 쓰려했기 때문이고, builtin method는 키워드가 아니고, builtin스코프에 선언되어, 따로 해당 이름으로 정의되지 않을때 호출되는거라 이 구문은 유효함.
ZeroInterger = tensor([[1, 1], [1, 1]]) # 2×2 행렬
zero = lambda v : min(v) * ZeroInterger # min(v)로 상수배했을 뿐인 2×2행렬.
iszero = lambda M : acess11(M) == acess12(M) == acess21(M) == acess22(M) # M이 ZeroInterger 인지 확인하는 2×2 행렬의 대수구조 모델 위의 술어
isInteger = lambda M : FirstVector(M) == LastVector(RevRow(M)) # M이 Integer라는 정수의 범자연수 행렬표현인지 확인하는 2×2 행렬의 대수구조 모델 위의 술어
isSameInteger = lambda x, y : iszero(x - y) # 동일한 Integer인지 확인하는 2×2 행렬의 대수구조 모델 위의 술어
normalize = lambda M : M - zero(FirstVector(M)) # Integer의 정규화 ㅋ... 뭐... 그냥 기약뺄셈형으로 바꾸는거.
isWholeNumberInteger = lambda M : isInteger(M) and untensorize(acess12(normalize(M))) == 0 # 그 Interger가 WholeNumber(범자연수)인지
@TailRequationOptimization
NaturalLogMachine = lambda : [lambda v : v[1] % v[0] == 0, lambda v : [v[1] // v[0], v[0], v[2] + 1]] # [a, x1, y1]을 입력으로, [a, x2, y2]를 출력으로 가지고, log_a (x1 × a^y1) = log_a (x2 × a^y2) 인 함수 ㅋㅋㅋ (무한히 나누어 떨어지지 않는다면 base condition이 정의되므로 well defined임)
def NextPrime(x, cache = [2]): #내가 곧 수정할껀데, 수정하기 전까지. while이라 쓰인 부분을 알아서 @TailRequationOptimization로 치환해서 생각해주셈. while을 @TailRequationOptimization로 옮기는 수정을 이따가 할거라
	if x == 1: return 2
	elif x in cache: # elif든 if듴 else든 걍 조건부 표현식으로 설명 됨.
		if cache.index(x) == len(cache) - 1:
			i = x #@TailRequationOptimization에 넣을때 에초에 기본값을 이렇게 하면 되는거.
			while len(tuple(filter(lambda v : v % i != v, cache))): i += 1
			cache.append(i) #구하고 난 값을 append한 뒤에 리턴하는건 (첫 명령, 리턴값)[-1]로 ㅆㄱㄴ ㅋㅋㅋ (사실 이경우는 그것보다, (lambda x : (첫 명령, x)[-1])인 편이 낫다.)
			return cache[-1]
		else:
			return cache[cache.index(x) + 1]
	else:
		while x not in cache: NextPrime(cache[-1])
		return NextPrime(x) #ㅋㅋㅋㅋ 뭐... 되자마자 노빠꾸로 구해서 리턴해버리는거.
@lambda f : lambda x : tensor(f([x, 1])[2:])
@TailRequationOptimization
fac = lambda : [lambda v : v[0] != 1, lambda v : (lambda t : [t[1], t[0], *v[2:], t[2]])(NaturalLogMachine([NextPrime(v[1]), v[0], 0]))] # 자연수에서 소인수분해 백터 로 가는 함수 ㅋㅋ
@lambda f : lambda sgn, x : f([sgn, 1, *x])[0]
@TailRequationOptimization
unfac = lambda : [lambda v : len(v) != 2, lambda v : (lambda optvar : [v[0] * pow(optvar, v[2]), optvar, *v[3:]])(NextPrime(v[1]))] # 소인수분해 백터에서, 자연수로 가는 함수
addr = lambda x, y : x + y if type(x) == int == type(y) and x >= 0 =< y else (x + y if rank(x) - 1 > 0 < rank(y) - 1 else np.pad(x if min(len(x), len(y)) == len(x) else y, (0, max(len(x), len(y)) - min(len(x), len(y))), mode='constant') + x if max(len(x), len(y)) == len(x) else y) #합 등을 구하는 법.

# NOTE 1 : 원래 행렬표현한 정수는, 내부 덧셈이 자연수이도록, 자연수 타입을 만들어야 하는대, 개을러서 안함.
# NOTE 2 : 원래 fac벡터화시킨 유리수의 경우, 각 벡터의 자료향이 행렬표현 정수여야 하며, 또한, a라는 수를 표현하고 싶다면 lambda x : addr(x, a)으로 함자화하여 관리해야한다. 그래야만, unfac • fac를 가했음에도 타당한 형식일수 있다. 에초에, (+a)를 가지고, 다항식의 성질로써 관리하는거라, 정의역이 유동적이게 해준다. 일단 특수 합성 연산 comp(f, g)에 대해, f랑 g가 역함수 관계라면, 항등함수 I로 만들고, comp(f, I) = f = comp(I, f)인 모노이드여야 한다. 이렇게 극단적인 comp없이는 체계 구축 못한다.
# NOTE 3 : 실수는 코시 수열에 극한을 취한것이므로, lime(f) = lim_{x ⟶ ∞} f(x)인 범함수 lime을 통해서 정의되는거고, lime이 사실상, 함수와 극한값간의 준동형사상이고, 극한이 같은 함수를 같은 값으로 간주하도록 동치관계를 주면, 해당 동치류 집합 R은 실수와 동형이다. (에초에 정수랑 유리수같은 경우도, 정수는 행렬표현에서, isSameInterger라는 동치관계의 동치류고, 유리수는, fac랑 unfac를 동형사상으로 해서, 정수 행렬표현을 스칼라로 가지는 벡터를 상수항으로써 더해주는 다항함수로 다루는 짓거리를 하는지라, 실수에서 저따구로 정의해도 딱히 이상하지 않다.)
```

부언설명)

fac은 사실상 자연수 로그와 동형임

여기서 질문은 곱같은 경우는, 벡터로 계산되는데, 기존 정수 시스템과의 호환이 되냐? 

ㅋㅋㅋㅋ 그래서 fac에 부호 기능이 존재하는거임 ㅋㅋㅋ 정수가 이미 정의되어있어, 그 부분집합으로써 자연수가 input이거든 ㅋㅋㅋ 에초에 유리수를 덧셈 파생 함자로 정의함에서 말 다함 ㅋㅋㅋ 그냥 ㅋㅋㅋ 분모(x - |수|) 이런 경우에도 쌉가능이라고 ㅋㅋㅋ 저기서 정의되는 자연수 x가 존재하니 ㅋㅋㅋㅋ

ㅋㅋㅋㅋㅋ 유리수랑 동형이라 유리수의 크기비교 시스템을 그대로 가져오지 당연히 ㅋㅋㅋ. 양수와 음수의 곱셈과 덧셈에서 크기비교를 통해, 추론됨 ㅋ

ㅋㅋㅋㅋ 이 코시수열 체계 돌았네 ㅋㅋㅋㅋ