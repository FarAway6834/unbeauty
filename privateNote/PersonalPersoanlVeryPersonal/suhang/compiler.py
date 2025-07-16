from sys import argv as _a
from os.path import splitext
from os.path import basename
from re import compile as regex
import lbdc

loader = regex(r'#syntaxial\s(.*?)')

load = lambda x : f'from m{x[11:]} import *' if loader.search(x) else x

preprocessor = lambda x : x.replace('×', '*').replace('÷', '/').replace('^', '**').replace('mod', '%')

def compiler(x):
    return '\n'.join([λ(load(line)) for line in preprocessor(x).splitlines()])

def core(fn):
    fn2 = splitext(fn)[0]
    tlqkf_time = f'm{fn2}'
    with open(f'{fn2}.py', 'w', encoding = "utf-8") as fp: fp.write(f'''\
from sys import argv as _a
from {basename(tlqkf_time)} import main

if __name__ == "__main__": print(main(*map(int, _a[1:])))\
''')
    with open(fn, encoding = "utf-8") as f:
        with open(f'{tlqkf_time}.py', 'w', encoding = "utf-8") as fp:
            fp.write(compiler(f.read()))

def main():
    core(_a[1])

if __name__ == "__main__": main()
