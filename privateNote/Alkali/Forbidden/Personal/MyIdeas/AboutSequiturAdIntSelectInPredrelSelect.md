# about, sequitur ad int select in predrel select

Predrel(S) ≜ S ∪ 𝔹
Select(X) ≜ <Predrel(X), •?•:•> s.t. •?•:• = (dom •?•:•, codom •?•:•, graph •?•:•) ∧ graph •?•:• = graph (•?•:•)|_{𝔹 × Prederel(X)²} ∪ graph (?•:•)|_{X × Predrel(X)²} ∧ (∀x, y ∈ Predel(X), ∀v ∈ X, (•?•:•)|_{𝔹 × Predrel(X)²}(T, x, y) = (•?•:•)|_{X × Predrel(X)²}(v, x, y) = x = graph (•?•:•)|_{𝔹 × Predrel(X)²}(F, y, x))
일 시, 모델 Select(X)에서, •?•:•는 선택 기능을 하지.

더 나아가서,

int : Predrel(X) ↦ X ∪ {0, 1}
bool : X ∪ {0, 1} ↦ Predrel(X)
int(x) ≜ (x ∈ 𝔹)?(x?1:0):x
bool(x) ≜ (x ∈ {0, 1})?((x∈[1,1])?T:F):x
에 대하여,

int(bool(x)) = x 이므로,

intSelect(X) = <X ∪ {0, 1}, •¿•:•> s.t. p¿x:y = int(bool(p)?bool(x):bool(y))

인 모델 intSelect(X)에 대해, 선택 로직은 intSelect(X)으로 처리 가능함이 귀결임.