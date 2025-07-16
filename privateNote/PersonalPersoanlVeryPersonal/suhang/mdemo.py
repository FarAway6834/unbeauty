from mruntime import *

abs = lambda x :  (x**2)**(1/2)
C = lambda n :  (n % 2) * ((3 * n + 1) - (n / 2)) + (n / 2)
H = infinite(lambda x :  ((1 - 0**abs(x - 1)) * H)(C(x)))
main = lambda x :  H(x)