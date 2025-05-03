from sys import argv
from os import system as shell

def main():
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

if __name__ == "__main__": main()
