#!/usr/bin/python3

from os import urandom
from struct import pack
from random import shuffle, randint


def p32(number):
    return pack('<I', number)


def rand(bound):
    return randint(0, bound - 1)


def randlist(length):
    list_ = list(range(1, length))
    shuffle(list_)
    return list_


def make_xor(data1, data2):
    return bytes(x^y for x, y in zip(data1, data2))


def make_db(data):
    mask = '\\x{0:02X}'
    return '`' + ''.join(mask.format(b) for b in data) + '`'


def make_dd(data):
    mask = '\\x{0:02X}'
    data = b''.join(p32(x) for x in data)
    return '`' + ''.join(mask.format(b) for b in data) + '`'


def make_block(flag_index, expected_index, next_xor, next_cipher):
    # 0:  31 c0                   xor    eax,eax
    # 2:  8d 96 78 56 34 12       lea    edx,[esi+0x12345678]
    # 8:  8a 02                   mov    al,BYTE PTR [edx]
    # a:  31 db                   xor    ebx,ebx
    # c:  8d 97 e0 59 d1 48       lea    edx,[edi+0x48d159e0]
    # 12: 8b 1a                   mov    ebx,DWORD PTR [edx]
    # 14: 29 c3                   sub    ebx,eax
    # 16: 89 1a                   mov    DWORD PTR [edx],ebx
    # 18: b8 78 56 34 12          mov    eax,0x12345678
    # 1d: bb 78 56 34 12          mov    ebx,0x12345678
    # 22: c3                      ret

    return b'\x31\xC0' + \
           b'\x8d\x96' + p32(flag_index) + \
           b'\x8A\x02' + \
           b'\x31\xDB' + \
           b'\x8d\x97' + p32(4*expected_index) + \
           b'\x8B\x1a' + \
           b'\x29\xC3' + \
           b'\x89\x1a' + \
           b'\xB8' + p32(next_xor) + \
           b'\xBB' + p32(next_cipher) + \
           b'\xC3'


def make_coeffs(size, count):
    return [(rand(size), rand(size)) for _ in range(count)]


def make_matrix(size, coeffs):
    matrix = [[0 for y in range(size)] for x in range(size)]
    for x, y in coeffs:
        matrix[y][x] += 1
    return matrix


def make_exploit(matrix, expected):
    lines = [
        '#!/usr/bin/python3',
        '',
        'import numpy as np',
        '',
        '',
        'matrix = np.matrix({0})'.format(repr(matrix)),
        'expected = np.array({0})'.format(expected),
        '',
        'result = np.linalg.solve(matrix, expected)',
        'print(result)',
        '',
        'result = result.round().astype(int)',
        'print(\'\'.join(map(chr, result)))'
    ]
    return '\n'.join(lines)


def calculate_expected(coeffs, flag):
    expected = [0] * len(flag)
    for flag_index, expected_index in coeffs:
        expected[expected_index] += flag[flag_index]
    return expected


def write_result(xors, blocks, expected):
    lines = [
        '%define BLOCK_SIZE {0}'.format(len(blocks[0])),
        '%define BLOCKS_COUNT {0}'.format(len(blocks)),
        '',
        '%define FLAG_SIZE {0}'.format(len(expected)),
        '',
        '',
        'SECTION .data',
        '',
        '    xors:       db ' + make_db(b''.join(xors)),
        '    blocks:     db ' + make_db(b''.join(blocks)),
        '    expected:   dd ' + make_dd(expected)
    ]
    with open('blocks.asm', 'w') as file:
        file.write('\n'.join(lines))


def main():
    with open('flag.txt', 'rb') as file:
        flag = file.read().strip()
    BLOCK_SIZE = 0x23
    BLOCKS_COUNT = 8192
    xor_indexes = [0] + randlist(BLOCKS_COUNT) + [0]
    block_indexes = [0] + randlist(BLOCKS_COUNT) + [0]
    coeffs = make_coeffs(len(flag), BLOCKS_COUNT)
    xors = [None] * BLOCKS_COUNT
    blocks = [None] * BLOCKS_COUNT
    for i in range(BLOCKS_COUNT):
        xor = urandom(BLOCK_SIZE)
        block = make_block(*coeffs[i], xor_indexes[i+1], block_indexes[i+1])
        block = make_xor(block, xor)
        xors[xor_indexes[i]] = xor
        blocks[block_indexes[i]] = block
    expected = calculate_expected(coeffs, flag)
    write_result(xors, blocks, expected)
    print(make_exploit(make_matrix(len(flag), coeffs), expected))


if __name__ == '__main__':
    main()
