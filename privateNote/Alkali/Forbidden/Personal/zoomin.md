# characteristic log

## f s.t. characteristic log

f(xy) ≜ f(x) + f(y)

f(y/x) + f(x) = f(y) ↔ f(y/x) = f(y) - f(x)

[g := λk. λx. Σ f(x) [i := 1 ~ k]]

g(x) = kf(x) = f(xᵏ)

## f s.t. peano-style exponention

기가 빨리고 시간이 딸려서 미룸.

# zoomin

EulersEquation(x) : eix(x) = cis(x)
[eix := eⁱˣ]
[floor := λx. ⌊ x ⌋]
[cis := cos + i sin]
[wave := λx. x mod 1]
[zoomin := λz. λf. λx. zf(x/z)]


cis(θ + φ) = cis θ cis φ

p.f.

> cis(θ + φ)
> 
>  = cos(θ ± φ) + i sin(θ ± φ)
> 
>  = cos θ cos φ - sin θ sin φ + i (sin θ cos φ + cos θ sin φ)
> 
>  = cos θ cos φ + i² sin θ sin φ + i (sin θ cos φ + cos θ sin φ)
> 
>  = (cos θ + i sin θ)(cos φ + i sin φ)
> 
>  = cis θ cis φ

즉, cis는 주기함수이자 지수 함수임

(sin, cos, tan) = sct
[sct := (sin, cos, tan)
  [tan := sin/cos]
  [cos := λx. sin(½π - θ)]
  s.t.
    sin θ = √(1 - (cos θ)²)
]
에서 sin의 부호가 아주 잘 결정되므로,
이것이 삼각비의 핵심 성질이라고 단언할 수 있음.

단위원 위에서 삼각비는 더 큰 삼각형에 대햐 닮으므로, 그냥 단위원 위에서 파악해도 무방하디 때문에 x² + y² = r²을 응용할 수 있음.