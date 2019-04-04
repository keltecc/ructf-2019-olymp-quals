#!/usr/bin/python3

import sys


def xor(x, y):
    return bytes(a^b for a, b in zip(x, y))

def main():
    if len(sys.argv) < 2:
        print('usage: {0} <flag>'.format(sys.argv[0]))
        sys.exit(1)
    key = b'flag{yoO_k1ddo_y0U_waNna_s0m3_h4ck??}\x00'
    flag = sys.argv[1].encode()
    assert len(key) == len(flag)
    expected = xor(key, flag)
    print('char expected[FLAG_LENGTH] = {{{0}}};'.format(', '.join(map(str, expected))))

if __name__ == '__main__':
    main()
