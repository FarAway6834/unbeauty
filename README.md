# unbeauty

unbeauty esolang

## example

```unbeauty
factorialtlqkf = cacher[1](λx. 0^x + x×f(x))
partial_beq0c = cacher[1](λx, n, p. ((0^n) + n×(x + ((-1)^p)×n) ÷ (0^n + n^2)) × f(x, n - 1, p))
partial_beq0 = cacer(λx, b, p. this.partial_beq0(x, 2^b - p, p))
beq0 = cacher[1](λx, b. this.partial_beq0(x, b, 0) × this.partial_beq0(x, b, 1)
beq = cacher[1](λx, y, b. this.beq0(x - y, b))

conditionalidx = cacher[1](λp,x,y.p×(x-y)+y)
_4bit_eqer_ = cacher[1](λx,y.this.beq(x,y,4))
_4bit_idxer = cacher[1](λi,a0,a1,a2,a3,a4,a5,a6,a8,a9,aA,aB,aC,aD,aE,aF.this._4bit_eqer_(i,0)×a0+this._4bit_eqer_(i,1)×a1+this._4bit_eqer_(i,2)×a2+this._4bit_eqer_(i,3)×a3+this._4bit_eqer_(i,4)×a4+this._4bit_eqer_(i,5)×a5+this._4bit_eqer_(i,6)×a6+this._4bit_eqer_(i,7)×a7+this._4bit_eqer_(i,8)×a8+this._4bit_eqer_(i,9)×a9+this._4bit_eqer_(i,10)×aA+this._4bit_eqer_(i,11)×aB+this._4bit_eqer_(i,12)×aC+this._4bit_eqer_(i,13)×aD+this._4bit_eqer_(i,14)×aE+this._4bit_eqer_(i,15)×aF)

not = cacher[1](λx.1-x)
and = cacher[1](λx,y.x×y)
sor = cacher[1](λs,x,y.x+y-(1+s)*_self__getitem_(and)(x, y))
or = cacher[1](λx,y._self__getitem_(sor)(0,x,y))
xor = cacher[1](λx,y._self__getitem_(sor)(1,x,y))
nand = cacher[1](λx,y._self__getitem_(not)(_self__getitem_(and)(x,y)))
nor = cacher[1](λx,y._self__getitem_(not)(_self__getitem_(or)(x,y)))
nxor = cacher[1](λx,y._self__getitem_(not)(_self__getitem_(xor)(x,y)))
sub =  cacher[1](λx,y._self__getitem_(and)(x,_self__getitem_(not)(y)))
rsub = cacher[1](λx,y._self__getitem_(sub)(y,x))
rimp = cacher[1](λx,y._self__getitem_(not)(_self__getitem_(rsub)(x,y)))
imp = cacher[1](λx,y._self__getitem_(not)(_self__getitem_(sub)(x,y)))
a = cacher[1](λx,y.x)
b = cacher[1](λx,y.y)
nota = cacher[1](λx,y._self__getitem_(not)(x))
notb = cacher[1](λx,y._self__getitem_(not)(y))
logicalerr = cacher[1](λx,y.0)
alwaystruth = cacher[1](λx,y.1)
lpu = cacher[1](λcod,x,y._self__getitem_(_4bit_idxer)(cod,_self__getitem_(logicalerr)(x,y), _self__getitem_(and)(x,y), _self__getitem_(sub)(x,y), _self__getitem_(b)(x,y), _self__getitem_(rsub)(x,y), _self__getitem_(a)(x,y), _self__getitem_(xor)(x,y), _self__getitem_(or)(x,y), _self__getitem_(nor)(x,y), _self__getitem_(nxor)(x,y), _self__getitem_(nota)(x,y), _self__getitem_(rimp)(x,y), _self__getitem_(notb)(x,y), _self__getitem_(imp)(x,y), _self__getitem_(nand)(x,y), _self__getitem_(alwaystruth)(x,y)))

bne = cacher[0](λx, y, b. this.not(this.beq(x, y, b)))
bits2bool = cacher[1](λb, x. this.not(this.beq0(x, b)))

shr = cacher[1](λx,n.x÷(2^n))
shl = cacher[1](λx,n,b.(2^b)×x-(2^b)×(x÷(2^(b-n))))
idx = cacher[1](λx,i,b._self__getitem_(shr)(_self__getitem_(shl)(x, i, b), b))
_bpucc_ = cacher[1](λcod,i,x,y,b._self__getitem_(lpu)(cod, _self__getitem_(idx)(x, i, b), _self__getitem_(idx)(y, i, b)) * (2^i))
_bpuc_ = cacher[1](λcod,i,x,y,b.this._bpucc_(i,x,y,b) + this.bits2bool(i)×this._bpuc_(i-1,x,y,b))
bpu = cacher[1](λcod,x,y,b.this._bpuc_(cod,b-1,x,y,b))
```

## [coding plan 24.02.24 ~ ...](./plan)
