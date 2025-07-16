import builtins as __builtins__

class infinite:

    __slots__ = ("__f", "__a")
    
    def __init__(self, f):
        self.__f, self.__a = f, 1

    def __mul__(self, a):
        self.__a *= a
        return self

    def __rmul__(self, a):
        return self * a

    def __call__(self, *argv):
        print(self.__f, self.__a, *argv)
        return self.__a * self.__f(*argv) if self.__a else 0

__builtins__.infinite = infinite
