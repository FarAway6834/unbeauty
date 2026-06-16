# Slow Tree

아 ㅅㅂ 수정해야함. 근데, 데드라인까지 3분 남아서 임시저장.

## tool

first(x, y) = x
last(x, y) = y
partal(f, x)(y) ≜ f(x, y)
ObTreeObAwait(L, f, g) ≜ ϝ (n, x) : {(n, x) ∈ ℕ₀ × S | 0 ≤ n < L ∧ S = dom f ∪ (L = 1)?∅:((L = 2)?(dom g):({y | ∃k, (k, y) ∈ ObTreeObAwait(L - 1, g)})) ∧ x ∈ ((n = 1 ∨ n = 2)?(dom f):((L > 2)?({y | ∃k, (k, y) ∈ ObTreeObAwait(L - 1, g)}):(dom g)))}. (((L - 1, g) ∉ dom ObTreeObAwait ∧ n > 1 ∧ L > 2)?0:((L = 1)?(f(x)):(((L = 2)?((n=0)?(f(x)):(g(x))):((n = 0)?(f(x)):ObTreeObAwait(L - 1, g)(n - 1, x)))))) : ((L = 1)?(codom f):((L = 2)?(codom f ∪ codom g):(codom f ∪ codom ObTreeObAwait(L - 1, g)))
Numering(n, f) ≜ ϝ x : dom f. (n, f(x)) : ℕ₀ × codom f
NumberingAll(n, x) ≜ ((n≠1)?(Numering(n, first(x)), NumberingAll(n + 1, last(x))):Numbering(n, x))
numedObTreeObAwait(L, x) ≜ ObTreeObAwait(L, NumberingAll(0, x))
MergeOTOA(L, f, g) ≜ ϝ (n, x) : dom f ∪ {(n, x) | (n - L, x) ∈ dom g)}. ((n<L)?f(n, x):g(n + L, x)) : codom f ∪ codom g
MergeNOTOA(L, f, g) ≜ MergeOTOA(L, f, ϝ (n, x) : dom g. (first(g(n, x)) + L, last(g(n, x))) : {(n + L, y) | (n, y) ∈ codom g})
SplitOTOA(p, L, f) ≜ p?({(n, x) ∈ dom f | n < L}, codom f, graph f ∩ {(n, x) ∈ dom f | n < L} × codom f):(ϝ (n, x) : {(n, x) | (n + L, x) ∈ dom f}. f(n + L, x) : codom f)
SplitNOTOA(p, L, f) ≜ (ϝ y : codom f. (p?y:(first(y) - L, last(y))) : (p?(codom f):({(n, v) | (n - L, v) ∈ codom f})))◦SplitOTOA(p, L, f)

## main

domOfStackLike(T) ≜ {(push, pop, tup) ∈ 𝔉(T × T*, T × T* ∪ {0}) × 𝔉(T*, T* ∪ {0}) × T* | ∀(x, y) ∉ ker push, push(x, y) = (x, y) ∧ ∀(x, y) ∉ ker pop, pop(x, y) = y}
domOfValueOfStackLike(T) ≜ Surj (push, pop, tup) : domOfStackLike(T). {arg ∈ 𝔹 × (T?) | (arg ↔ F ∨ ∀x ∈ T, arg = (isPush, x)  ∧ isPush)}
codomOfValueOfStackLike(T) ≜ Surj (push, pop, tup) : domOfStackLike(T). {(isPush ∧ arg ∈ ker push, ¬isPush ∧ (tup, x) ∈ ker pop, value) | isPush → (((tup, x) ∈ ker push → value = tup) ∧ (arg ∉ ker push → value = push(tup, x))) ∧ (¬isPush) → ((tup ∈ ker pop → value = tup) ∧ (tup ∈ ker pop → value = pop(tup))) ∧ (arg ↔ F ∨ arg = (isPush, x)  ∧ isPush) ∧ arg ∈ domOfStackLike(T)(push, pop, tup)}
isValueOfStackLike(T) ≜ Surj (push, pop, tup) : domOfStackLike(T). 𝔉(domOfValueOfStackLike(T)(push, pop, tup), codomOfValueOfStackLike(T)(push, pop, tup))
codomOfStackLike(T) ≜ isValueOfStackLike(T)[domOfStackLike(T)]
StackLike(T) ≜ ϝ (push, pop, tup) : domOfStackLike(T). (ϝ (isPush, probablyNonEmpthyOrMaybeEmpty) : domOfValueOfStackLike(T)(push, pop, tup). (ϝ p : 𝔹. (isPush?(p, 0, p?tup:push()):(0, p, p?tup:pop(tup))) : codomOfValueOfStackLike(T)(push, pop, tup))(isPush?tup, probablyNonEmpthyOrMaybeEmpty) ∈ ker push:tup, probablyNonEmpthyOrMaybeEmpty) ∈ ker pop) : codomOfValueOfStackLike(T)(push, pop, tup)) : codomOfStackLike(T)

domOfStackLikeObjectSLOW(T) ≜ 𝔹² × domOfStackLike(T)
codomOfValueOfStackLikeObjectSLOW(T) ≜ Surj (isOverflow, isUnderflow, coreValue) : domOfStackLikeObjectSLOW(T). {((isOverflow ∨ isUnderflow)?(isOverflow, isUnderflow, coreValue):(StackLike(isOverflow, isUnderflow, coreValue)(arg))) | arg ∈ domOfValueOfStackLike(T)(coreValue)}
isValueOfStackLikeObjectSLOW(T) ≜ Surj (isOverflow, isUnderflow, coreValue). 𝔉(domOfValueOfStackLike(T)(isOverflow, isUnderflow, coreValue), codomOfValueOfStackLikeObjectSLOW(T)(isOverflow, isUnderflow, coreValue))
codomOfStackLikeObjectSLOW(T) ≜ isValueOfStackLikeObjectSLOW(T)[domOfStackLikeObjectSLOW(T)]
StackLikeObjectSLOW(T) ≜ ϝ (isOverflow, isUnderflow, coreValue) : domOfStackLikeObjectSLOW(T). (ϝ arg : domOfValueOfStackLike(T)(coreValue). ((isOverflow ∨ isUnderflow)?(isOverflow, isUnderflow, coreValue):(StackLike(isOverflow, isUnderflow, coreValue)(arg))) : codomOfValueOfStackLikeObjectSLOW(T)(isOverflow, isUnderflow, coreValue)) : codomOfStackLikeObjectSLOW(T)
SlowTree(T) ≜ MergeNOTOA(1, StackLikeObjectSLOW(T), StackLikeObjectSLOW(T))

## insight

아, 이 스택 산술의 인사이트를 다루려고 보다보니 젠장

아 ㅅㅂ 잠만, 이거 인자가 ㅈ됬다 개씨발...
인자 몇번 후에 넘버링하는지, 메니저를 넘겨야지 ㅂㅅ아...