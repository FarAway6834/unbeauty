#히히히

실수성분 a(z), 허수성분 b(z)

평탄화함수 mcrft := λf. λz. b(z) - a(f(z))

바보짓함수 ImDum := λw. mcrft(λx. sin(w x))

허수화함수 Point := λf. λx. x + i f(x)

(lim f를 괄호로 묶었다면, 함수값을 구하는게 아닌 극한값을 구하는 함수화한것. 즉, (lim f)(x) = lim f(t) (단. t는 x에 한없이 접근함) 이게 됨)

x = a에서 f(x)가 연속이려면
f(a)가 정의될것 ••• (1)
(lim f)(a)가 정의될것 ••• (2)
f - (lim f)가 상수함수를 미분한 함수일것 ••• (3)
이야야 하니까,
ulala := λx. mcrft(f) • Point(f)에서
(1)은 ulala(f)(a) = 0
(2)는 ulala(lim f)(a) = 0
(3)은 ulala(f - (lim f))(a) = 0
일것이여야 함.