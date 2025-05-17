# unbeauty

unbeauty esolang (0⁰=1, x->0 x^x->1)

mathmatics.... beautiful 4 me....

`sementically-recursive-defined-recurrence-formular based` programming language

actually, I didn't finished this work, because of my high school exam.
~~Fucking Korea~~

## example

[tip (lang=ko)](https://FarAway6834.github.io/LAFTF1.1)

noptlib.unbe
```unbeauty
sqrt = cacher[1](λx. x^0.5)
abs = cacher[1](λx. this.sqrt(x^2))
partial_beq0c = cacher[1](λx, n, p. ((0^this.abs(n)) + n×(x + ((-1)^p)×n) ÷ (0^this.abs(n) + n^2)) × f(x, n - 1, p))
partial_beq0 = cacer(λb, x, p. this.partial_beq0(x, 2^b - p, p))
beq0 = cacher[1](λb, x. this.partial_beq0(b, x, 0) × this.partial_beq0(b, x, 1)
beq = cacher[1](λb, x, y. this.beq0(b, this.abs(x - y)))
dose_it_positive = cacher[1](λb, x. this.beq0(b, this.abs(b, x - this.abs(x))))
__cmp__ = cacher[1](λb, x. this.beq(b, x) + (-1)^(this.dose_it_positive(b, x)+1))
__le__ = cacher[1](λb, x, y. this.dose_it_positive(b, x - y))

conditionalidx = cacher[1](λp,x,y.p×(x-y)+y)
conditional = cacher[1](λp, x, y. p×x + (1-p)×y)
_4bit_eqer_ = cacher[1](λx,y.this.beq(4,x,y))
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

__gt__ = cacher[1](λb, x, y. this.not(this.__le__(b, x, y)))
__lt__ = cacher[1](λb, x, y. this.__gt__(b, y, x))
__ge__ = cacher[1](λb, x, y. this.__le__(b, y, x))

__ne__ = cacher[1](λb, x, y. this.not(this.beq(b, x, y)))
bits2bool = cacher[1](λb, x. this.not(this.beq0(b,,x)))

shr = cacher[1](λx, n.x÷(2^n))
shl = cacher[1](λb, x, n.(2^b)×x-(2^b)×(x÷(2^(b-n))))
idx = cacher[1](λb, x,i.this.shr(this.shl(b, x, i), b))
_bpucc_ = cacher[1](λb, cod,i,x,y.this.lpu(cod, this.idx)(b, x, i), this.idx)(b, y, i)) × (2^i))
_bpuc_ = cacher[1](λb, cod,i,x,y.this._bpucc_(b, i,x,y) + this.bits2bool(i)×this._bpuc_(b,i-1,x,y))
bpu = cacher[1](λb,cod,x,y.this._bpuc_(b,cod,b-1,x,y))
```

ex2.ubt - extend not base cls, ex1 cls.
```
:noptlib
fibo = cacher[1](λb, x.this.conditional(this.beq0(b, x), 0, this.conditionalidx(this.beq(b, x, 1), 1, this.fibo(b, x - 1) + this.fibo(b, x - 2))))
```

## [coding plan 24.02.24 ~ ...](./plan)

### lazy evil optimizing

`[○×]this.__NAME__(□)` -> `([○×]this.__NAME__)(□)`

 > also as `conditional` too. (when it is arguemnt, not return)
