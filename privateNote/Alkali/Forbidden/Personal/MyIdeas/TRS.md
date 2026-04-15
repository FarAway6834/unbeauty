# 튜플 제귀 분할 모델 TRS(S)

들어가기 앞서, 
벡터에 대해서는 1도 생각 않고 기획했다는점을 기억하자, 벡터에 주어지는 dim은 결코 튜플의 길이가 될수 없다. 외냐면 모든 튜플은 최대길이가 L인 경우, 길이 1~L이나 L로 길이를 해석해도 무리가 없기 때문에, 하나로 정해졌다 하기 애매하다.

왜냐? 제귀적 정의에 따라서, n-tuple은 (n-1)-tuple의 일종이기 때문이다.

이제부턴 본론으로 들어간다.

TRS(S) ≜ <S*, ε, I, first, last, LengthEq>

I : S* ↦ S*
I(x) = x
first : S* ↦ S*
first|_{(S×S+)×(S×S+)}(x, y) = x
first|_{S¹}(x) = x
first|_{S⁰}() = ε
last : S* ↦ S*
last|_{(S×S+)×(S×S+)}(x, y) = y
last|_{S¹}(x) = ε
last|_{S⁰}() = ε

$LengthEqCore(p, f, x, y) : \begin{cases} f(x) = ε ↔ f(y) = ε, &(p), \ LengthEqCore(¬p, f, x, y) ∨ LengthEq(p, last◦f, x, y), &(¬p) \end{cases}$
LengthEq(x, y) : LengthEqCore(T, I, x, y)

LengthEq가 재대로 작동하는지는 근데 페아노 공리계에서 증명가능함.

에초에 LengthEq(x, y) ↔ ∃n ∈ ℕ₀, lastⁿ(x) = ε ↔ lastⁿ(y)임. ㅋㅋㅋ