#!/usr/env/python python3
from os import system as s

def main():
    s('git add .')
    s(f'git commit -m {input()}')
    s('git push')

if __name__ == "__main__": main()
