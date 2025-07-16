from sys import argv as _a
from mdemo import main

if __name__ == "__main__": print(main(*map(int, _a[1:])))