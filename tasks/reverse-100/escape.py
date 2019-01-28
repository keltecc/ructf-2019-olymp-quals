#!/usr/bin/python3

XOR = 0xFF


def main():
    data = input()
    binary = bytes(ord(x) ^ XOR for x in data)
    print(repr(binary)[2:-1])


if __name__ == '__main__':
    main()
