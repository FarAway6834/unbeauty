# unbeauty

unbeauty esolang

## example

[tip (lang=ko)](https://FarAway6834.github.io/LAFTF1.1)

ex1.unbe
```unbeauty
sqrt = cacher[1](λx. x**0.5)
abs = cacher[1](λx. this.sqrt(x**2))
factorialtlqkf = cacher[1](λx. 0^x + x×f(x))
partial_beq0c = cacher[1](λx, n, p. ((0^n) + n×(x + ((-1)^p)×n) ÷ (0^n + n^2)) × f(x, n - 1, p))
partial_beq0 = cacer(λx, b, p. this.partial_beq0(x, 2^b - p, p))
beq0 = cacher[1](λx, b. this.partial_beq0(x, b, 0) × this.partial_beq0(x, b, 1)
beq = cacher[1](λx, y, b. this.beq0(this.abs(x - y), b))
dose_it_positive = cacher[1](λx, b. this.beq0(this.abs(x - this.abs(x)), b))
__cmp__ = cacher[1](λx, b. this.beq(x, b) + (-1)^(this.dose_it_positive(x, b)+1))
__le__ = cacher[1](λx, y, b. this.dose_it_positive(x - y, b))

conditionalidx = cacher[1](λp,x,y.p×(x-y)+y)
_4bit_eqer_ = cacher[1](λx,y.this.beq(x,y,4))
_4bit_idxer = cacher[1](λi,a0,a1,a2,a3,a4,a5,a6,a8,a9,aA,aB,aC,aD,aE,aF.this._4bit_eqer_(i,0)×a0+this._4bit_eqer_(i,1)×a1+this._4bit_eqer_(i,2)×a2+this._4bit_eqer_(i,3)×a3+this._4bit_eqer_(i,4)×a4+this._4bit_eqer_(i,5)×a5+this._4bit_eqer_(i,6)×a6+this._4bit_eqer_(i,7)×a7+this._4bit_eqer_(i,8)×a8+this._4bit_eqer_(i,9)×a9+this._4bit_eqer_(i,10)×aA+this._4bit_eqer_(i,11)×aB+this._4bit_eqer_(i,12)×aC+this._4bit_eqer_(i,13)×aD+this._4bit_eqer_(i,14)×aE+this._4bit_eqer_(i,15)×aF)

not = cacher[1](λx.1-x)
and = cacher[1](λx,y.x×y)
sor = cacher[1](λs,x,y.x+y-(1+s)*this.and(x, y))
or = cacher[1](λx,y.this.sor(0,x,y))
xor = cacher[1](λx,y.this.sor(1,x,y))
nand = cacher[1](λx,y.this.not(this.and(x,y)))
nor = cacher[1](λx,y.this.not(this.or(x,y)))
nxor = cacher[1](λx,y.this.not(this.xor(x,y)))
sub =  cacher[1](λx,y.this.and(x,this.not(y)))
rsub = cacher[1](λx,y.this.sub(y,x))
rimp = cacher[1](λx,y.this.not(this.rsub(x,y)))
imp = cacher[1](λx,y.this.not(this.sub(x,y)))
a = cacher[1](λx,y.x)
b = cacher[1](λx,y.y)
nota = cacher[1](λx,y.this.not(x))
notb = cacher[1](λx,y.this.not(y))
logicalerr = cacher[1](λx,y.0)
alwaystruth = cacher[1](λx,y.1)
lpu = cacher[1](λcod,x,y.this._4bit_idxer(cod,this.logicalerr(x,y), this.and(x,y), this.sub(x,y), this.b(x,y), this.rsub(x,y), this.a(x,y), this.xor(x,y), this.or(x,y), this.nor(x,y), this.nxor(x,y), this.nota(x,y), this.rimp(x,y), this.notb(x,y), this.imp(x,y), this.nand(x,y), this.alwaystruth(x,y)))

__gt__ = cacher[1](λx, y, b. this.not(this.__le__(x, y, b)))
__lt__ = cacher[1](λx, y, b, this.__gt__(y, x, b))
__ge__ = cacher[1](λx, y, b. this.__le__(y, x, b))

bne = cacher[1](λx, y, b. this.not(this.beq(x, y, b)))
bits2bool = cacher[1](λb, x. this.not(this.beq0(x, b)))

shr = cacher[1](λx,n.x÷(2^n))
shl = cacher[1](λx,n,b.(2^b)×x-(2^b)×(x÷(2^(b-n))))
idx = cacher[1](λx,i,b.this.shr(this.shl(x, i, b), b))
_bpucc_ = cacher[1](λcod,i,x,y,b.this.lpu(cod, this.idx)(x, i, b), this.idx)(y, i, b)) * (2^i))
_bpuc_ = cacher[1](λcod,i,x,y,b.this._bpucc_(i,x,y,b) + this.bits2bool(i)×this._bpuc_(i-1,x,y,b))
bpu = cacher[1](λcod,x,y,b.this._bpuc_(cod,b-1,x,y,b))
```

ex2.unbe - extend not base cls, ex1 cls.
```
:ex1
fibo = cacher[1](λx.this.conditionalidx(this.beq0(x, b), 0, this.conditionalidx(this.beq(x, 1, b), 1, this.fibo(x - 1) × this.fibo(x - 2))))
```

## [coding plan 24.02.24 ~ ...](./plan)
