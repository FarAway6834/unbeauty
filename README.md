# unbeauty

unbeauty esolang

## example

```unbeauty
conditionalidx = cacher[1](λp,x,y.p×(x-y)+y)

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
imp = cacher[1](λx,y._self__getitem_(not)(_self__getitem_(rsub)(x,y)))
nimp = cacher[1](λx,y._self__getitem_(not)(_self__getitem_(sub)(x,y)))
a = cacher[1](λx,y.x)
b = cacher[1](λx,y.y)
nota = cacher[1](λx,y._self__getitem_(not)(x))
notb = cacher[1](λx,y._self__getitem_(not)(y))
lpu = cacher[1](λcod,x,y.~)

shr = cacher[1](λx,n.x÷(2^n))
shl = cacher[1](λx,n,b.(2^b)×x-(2^b)×(x÷(2^(b-n))))
idx = cacher[1](λx,i,b._self__getitem_(shr)(_self__getitem_(shl)(x, i, b), b))
bpu = cacher[1](λcod,x,y,b.~)
```
