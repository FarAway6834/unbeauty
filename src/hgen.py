from sys import argv
from os import system as shell

def core():
    print(f'''\
{
"""
#pragma once
#ifndef _{0}
# define _{0}



#endif
""".format(input().replace(".", "_").upper()).strip()
}\
''')

def pipe():
    target = argv[1]
    shell(f'echo "{target}" | python hgen.py')

def hgen():
    target = argv[2]
    shell(f'python hgen.py {target} > {target}')

def main(L = len(argv)):
    [core, pipe, hgen][L - 1]()

if __name__ == "__main__": main()
