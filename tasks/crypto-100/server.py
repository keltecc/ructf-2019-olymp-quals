#!/usr/bin/python3

from basex import BaseX
from random import shuffle

from signal import alarm


NOTES = list('♩♪♫♬')
shuffle(NOTES)

basex = BaseX(NOTES)
flag = open('flag.txt').read()


def encode(data):
    base = basex.bxencode(data.encode())
    return ' '.join(base)

    
def main():
    print('— Umm, hello? Wait, wait, I hear something...')
    print()
    print(encode(flag))
    print()
    print('— Nevermind, give me some text!')
    result = encode(input())
    print()
    print('— Okay, and... Here is your melody:')
    print(result)
    print()
    print('— Bye.')


if __name__ == '__main__':
    alarm(10)
    main()
