#히히히

실수성분 a(z), 허수성분 b(z)
평탄화함수 mcrft := λf. λz. b(z) - a(f(z))
바보짓함수 ImDum := λHz. mcrft(λx. Hz x)
허수화함수 Point := λf. λx. x + i f(x)