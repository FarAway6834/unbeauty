# characteristic log



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