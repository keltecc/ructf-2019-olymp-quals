#!/usr/bin/python3

from base64 import b64encode
from random import getrandbits
from hashlib import md5

from Crypto.Cipher import AES


class Cipher(object):
    def __init__(self, key):
        self._key = md5(key.encode('utf-8')).digest()
        self._aes = AES.new(self._key, mode=AES.MODE_ECB)

    def encrypt(self, plaintext):
        plaintext = self._pad(plaintext)
        return self._aes.encrypt(plaintext)

    def decrypt(self, ciphertext):
        plaintext = self._aes.decrypt(ciphertext)
        return self._unpad(plaintext)

    def _pad(self, data):
        byte = 16 - (len(data) % 16)
        return data + bytes([byte] * byte)

    def _unpad(self, data):
        byte = data[-1]
        return data[:-byte]


class PasswordGenerator(object):
    def __init__(self, length):
        self._length = length * 3 // 4
        self._hexlen = 2 * self._length
        self._bitlen = 4 * self._hexlen
        self._additional = b'@$'

    def generate(self):
        random = hex(getrandbits(self._bitlen))[2:].zfill(self._hexlen)
        return b64encode(bytes.fromhex(random), self._additional).decode()
