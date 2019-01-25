#!/usr/bin/python3

from math import floor, log


class BaseX:
    def __init__(self, alphabet):
        self._length = int(floor(log(len(alphabet), 2)))
        self._alpha = alphabet[:2**self._length]

    def bxencode(self, data):
        bits = self._data_to_bin(data)
        parts = self._split_bits(bits, self._length)
        return ''.join(self._alpha[int(part, 2)] for part in parts)
        
    def bxdecode(self, data):
        bits = self._base_to_bin(data)
        parts = self._split_bits(bits, 8)
        return bytes([int(part, 2) for part in  parts])

    def _data_to_bin(self, data):
        parts = [bin(x)[2:].zfill(8) for x in data]
        return ''.join(parts)

    def _base_to_bin(self, data):
        parts = [bin(self._alpha.index(x))[2:].zfill(self._length) for x in data]
        return ''.join(parts)

    def _split_bits(self, bits, length):
        for i in range(0, len(bits), length):
            yield bits[i:i+length]
