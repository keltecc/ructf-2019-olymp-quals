#!/usr/bin/python3

import sys

from gmpy2 import next_prime
from random import randint


def make_modulus(bits):
    bits >>= 1
    p = next_prime(randint(2**(bits-1), 2**bits))
    q = next_prime(randint(2**(bits-1), 2**bits))
    return p * q


def encrypt(message, key):
    exponent, modulus = key
    plaintext = int.from_bytes(message.encode('utf-8'), 'big')
    assert plaintext ** exponent > modulus
    return pow(plaintext, exponent, modulus)


def main():
    exponent, bits = 3, 900

    if len(sys.argv) < 2:
        print('usage: {} <your_flag>'.format(sys.argv[0]))
        sys.exit(-1)

    plaintext = sys.argv[1]
    modulus = make_modulus(bits)
    ciphertext = encrypt(plaintext, (exponent, modulus))

    known_part = '0x' + (plaintext.encode()[:-32] + b'\x00' * 32).hex()
    print('exponent = ' + str(exponent))
    print('modulus = ' + str(modulus))
    print('ciphertext = ' + str(ciphertext))
    print('known_part = ' + str(known_part))


if __name__ == '__main__':
    main()
