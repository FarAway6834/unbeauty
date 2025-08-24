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