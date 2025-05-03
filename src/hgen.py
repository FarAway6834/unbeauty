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
    if target = '-h':
        print('''
# personal `hgen.py`

```shell
$ python hgen.py
inputfilename.h
#pragma once
#ifndef _INPUTFILENAME_H
# define _INPUTFILENAME_H



#endif
$ python hgen.py argvfilename.h
#pragma once
#ifndef _ARGVFILENAME_H
# define _ARGVFILENAME_H



#endif
$ ls
hgen.py
$ python hgen.py -h argvfilename.h
$ ls
hgen.py    argvfilename.h
$ cat argvfilename.h
#pragma once
#ifndef _ARGVFILENAME_H
# define _ARGVFILENAME_H




#endif
$ 
```
''')
    shell(f'echo "{target}" | python hgen.py')

def hgen():
    target = argv[2]
    shell(f'python hgen.py {target} > {target}')

def main(L = len(argv)):
    [core, pipe, hgen][L - 1]()

if __name__ == "__main__": main()
