#!/usr/bin/python3

import sys

from random import randrange


def to_number(message):
    h_message = bytes(message, 'utf-8').hex()
    return int(h_message, 16)


def make_modulus(bits):
    bits >>= 1
    return randrange(2**bits) * randrange(2**bits)


def encrypt(message, key):
    exponent, modulus = key
    plaintext = to_number(message)
    assert plaintext ** exponent > modulus
    return pow(plaintext, exponent, modulus)


def main():
    exponent, bits = 3, 1280

    if len(sys.argv) < 2:
        print('usage: {} <your_flag>'.format(sys.argv[0]))
        sys.exit(-1)

    plaintext = '[*] Your secret flag is ' + sys.argv[1]
    modulus = make_modulus(bits)
    key = exponent, modulus
    ciphertext = encrypt(plaintext, key)

    known_part = '0x' + (plaintext.encode()[:-32] + b'\x00' * 32).hex()
    print('exponent = ' + str(exponent))
    print('modulus = ' + str(modulus))
    print('ciphertext = ' + str(ciphertext))
    print('known_part = ' + str(known_part))


if __name__ == '__main__':
    main()
