#!/usr/bin/python3

import sys
import struct
import random

from hashlib import md5


def prepare_flag(flag):
    pad = 4 - len(flag) % 4
    flag = flag.encode() + b'\x80' + b'\x00' * (pad - 1)
    parts = []
    for i in range(0, len(flag), 4):
        part = struct.unpack('<I', flag[i:i+4])[0]
        parts.append(part)
    return parts


def shuffle_parts(parts):
    order = list(range(len(parts)))
    random.shuffle(order)
    for i in order:
        yield i, parts[i]


def extend_number(n):
    return (n << 24) | (n << 16) | (n << 8) | (n)


def transform(flag):
    parts = prepare_flag(flag)
    template = '    XX(a,b,c,d,m[{0:2}],{1:3},{2});'
    lines = []
    for i, part in shuffle_parts(parts):
        number = random.randint(150, 250)
        line = template.format(i, number, hex(extend_number(number) - part))
        lines.append(line)
    return '\n'.join(lines)


def make_define(flag):
    template = '    BYTE expected[MD5_BLOCK_SIZE] = {{{}}};'
    digest = md5(flag.encode()).digest()
    numbers = []
    for byte in digest:
        numbers.append('0x' + hex(byte)[2:].zfill(2))
    return template.format(', '.join(numbers))


def main():
    if len(sys.argv) < 2:
        print('usage: {} <your_flag>'.format(sys.argv[0]))
        sys.exit(1)
    flag = sys.argv[1]
    print(make_define(flag))
    print()
    print(transform(flag))


if __name__ == '__main__':
    main()
