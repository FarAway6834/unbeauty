Zₙ ≜ (-1)⁽ⁿ ᵐᵒᵈ ²⁾⌊n/2⌋

# non-even Spec Solution

byUsingCond ≜ [cond := λp. λx. λy. p(x - y) + y]

(byUsingRobocaPoly, byUsingBinarrySearching) ≜ ([oddPoly := λp. λA. λB. (d/dx)⁻¹ evenPoly(p)(A)(B)] [evenPoly := λp. λA. λB. poly(p)(λi. (i mod 2)(Aᵢ - Bᵢ) + Bᵢ)] [poly := λp. λA. cond p λx. Σᵢ Aᵢxⁱ λx. Πᵢ (x - Aᵢ)) byUsingCond], [BS := λtarget. λstart. λend. lim BVFⁿBVFH<target, start, end> (n → ∞) (단. BVFH<target, start, end> = <target, start, ½(start + end), end>, BVFC<target, start, mid, end> = <target, st, ½(st + en), en> (단. cmp = sgn(mid - target), l = cond(sgn(1 - cmp)), r = cond(sgn(1 + cmp)), e = cond(1 - |cmp|), st = s(mid)(start), en = e(mid, end) byUsingCond))])

byUsingOddsGraφSolution ≜ [makeItEven := λA. λB. λΔt. λx. oddPoly(0)(A)(B)(t) ÷ (x - OddsGraφSolution(A)(B)(Δt)) [t := x + Δt]] [OddsGraφSolution := λA. λB. λΔt. y (단. (변곡(A)(B) ⊆ (, 0) ∧ (∃!t ∈ ℝ)(t < 0 ∧ oddPoly(0)(A)(B)(t)) [t := x + Δt] s.t. C ≠ 0 → y = BS(t)(max(변곡(A)(B)))(0)) ∧ (변곡(A)(B) ⊆ (0, ) ∧ (∃!t ∈ ℝ)(t > 0 ∧ oddPoly(0)(A)(B)(t))) [t := x - Δt] s.t. C ≠ 0 → y = BS(t)(0)(min(변곡(A)(B)))))] [변곡 := λA. λB. {(x, oddPoly(0)(A)(B)(x)) | (x, oddPoly(0)(A)(B)(x))는 graph oddPoly(0)(A)(B)의 변곡점} = Mod(λx. evenPoly(0)(A)(B)(x) = 0) byUsingRobocaPoly byUsingBinarrySearching]