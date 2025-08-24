# 성분 선택기 혹은 켤래 구성기

실수성분 re(z)와 허수성분 im(z)를 다음과 같이 놓겠음.

(re, im) ≜ ri
[ri := (re, im)
  [re := λz. (z + z̄)/2]
  [im := λz. (z - z̄)/2]
]

z̄는 복소수 z의 켤래복소수임.

혹은 다음 정의

z̄ ≜ re(z) - im(z)

로 하여도 좋음.

*텔레그라피체 re와 im이 내 중학교 시절 추억이 녹은 기호인데 못적어놓는게 ㄹㅇ 인생 최대의 한이다 이거 레알 진짜 실화냐 ㅠㅠ*

두번째 정의에 첫번째 정의를 대입해보면 항진이고, 반대로 첫번째 정의에 두번째 정의를 대입해봐도 항진으로...

둘 다 동등. (동치라는 일본식표현을 자제하라고 정주희 저 수리논리와 집합론 입문에서 저술해 놓아서 이렇게 적음. 절대 정치적 성향땜에 그렇게 적는건 아니고, 어릴때부터 일본식 문화 자제하는걸 교육받아서 그럼)

# characteristic log

## f s.t. characteristic log

f(xy) ≜ f(x) + f(y)

f(y/x) + f(x) = f(y) ↔ f(y/x) = f(y) - f(x)

[g := λk. λx. Σ f(x) [i := 1 ~ k]]

g(x) = kf(x) = f(xᵏ)

## f s.t. peano-style exponention

기가 빨리고 시간이 딸려서 미룸.

# sct function tuple

(sin, cos, tan) ≜ sct
[sct := (sin, cos, tan)
  [tan := sin/cos]
  [cos := λx. sin(½π - θ)]
  s.t.
    sin θ = √(1 - (cos θ)²)
]

에서 sin의 부호가 아주 잘 결정되므로,
이것이 삼각비의 핵심 성질이라고 단언할 수 있음.

단위원 위에서 삼각비는 더 큰 삼각형에 대햐 닮으므로, 그냥 단위원 위에서 파악해도 무방하기 때문에 x² + y² = r²을 응용할 수 있음.

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

z = cis(θ)의 켤래 z̄ = cis(-θ)임.

cis(½π - θ) = sin θ + i cos θ = t̄ [t := -z̄]임.

이런식으로 성질을 생각해 보자면,
