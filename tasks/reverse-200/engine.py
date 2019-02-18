#!/usr/bin/python3

import gmpy2
import numpy as np

from random import randint


def np_matrix(func):
    def inner_func(self, *args, **kwargs):
        np_args = [np.matrix(arg) if isinstance(arg, list) else arg for arg in args]
        result = func(self, *np_args, **kwargs)
        return result.round().astype('int').tolist()
    return inner_func


class Engine(object):
    def __init__(self, size):
        self._size = size

    def do(self, name):
        func = getattr(self, '_{0}'.format(name), None)
        return func

    def reverse(self, name):
        func = getattr(self, '_{0}_reversed'.format(name), None)
        return func

    @np_matrix
    def _matrix_transpose(self, matrix):
        return matrix.transpose()

    @np_matrix
    def _matrix_transpose_reversed(self, expected):
        return expected.transpose()

    @np_matrix
    def _matrix_sum(self, matrix1, matrix2):
        return matrix1 + matrix2

    @np_matrix
    def _matrix_sum_reversed(self, matrix, expected):
        return expected - matrix

    @np_matrix
    def _matrix_intsum(self, matrix, value):
        return matrix + value

    @np_matrix
    def _matrix_intsum_reversed(self, value, expected):
        return expected - value

    @np_matrix
    def _matrix_xor(self, matrix1, matrix2):
        return matrix1 ^ matrix2

    @np_matrix
    def _matrix_xor_reversed(self, matrix, expected):
        return expected ^ matrix

    @np_matrix
    def _matrix_intxor(self, matrix, value):
        return matrix ^ value

    @np_matrix
    def _matrix_intxor_reversed(self, value, expected):
        return expected ^ value

    @np_matrix
    def _matrix_mul(self, matrix1, matrix2):
        return matrix1 * matrix2

    @np_matrix
    def _matrix_mul_reversed(self, matrix, expected):
        return expected * (matrix ** -1)

    @np_matrix
    def _matrix_intmul(self, matrix, value):
        return matrix * value

    @np_matrix
    def _matrix_intmul_reversed(self, value, expected):
        return expected // value

    @np_matrix
    def _matrix_mod(self, matrix1, matrix2):
        def solve(x, y):
            return matrix1[x, y] % matrix2[x, y]
        return self._foreach(solve)

    @np_matrix
    def _matrix_mod_reversed(self, matrix, expected):
        def solve(x, y):
            return self._rand() * matrix[x, y] + expected[x, y]
        return self._foreach(solve)

    @np_matrix
    def _matrix_intmod(self, matrix, value):
        def solve(x, y):
            return matrix[x, y] % value
        return self._foreach(solve)

    @np_matrix
    def _matrix_intmod_reversed(self, value, expected):
        def solve(x, y):
            return self._rand() * value + expected[x, y]
        return self._foreach(solve)

    @np_matrix
    def _matrix_modmul(self, matrix1, matrix2, matrix3):
        def solve(x, y):
            return (matrix1[x, y] *  matrix2[x, y]) % matrix3[x, y]
        return self._foreach(solve)

    @np_matrix
    def _matrix_modmul_reversed(self, matrix1, matrix2, expected):
        def solve(x, y):
            return expected[x, y] * gmpy2.invert(int(matrix1[x, y]), int(matrix2[x, y]))
        return self._foreach(solve)

    @np_matrix
    def _matrix_intmodmul(self, matrix1, matrix2, value):
        def solve(x, y):
            return (matrix1[x, y] * matrix2[x, y]) % value
        return self._foreach(solve)

    @np_matrix
    def _matrix_intmodmul_reversed(self, value, matrix1, expected):
        def solve(x, y):
            return expected[x, y] * gmpy2.invert(int(matrix1[x, y]), int(value))
        return self._foreach(solve)

    def _foreach(self, func):
        result = np.zeros((self._size, self._size), 'int')
        for y in range(self._size):
            for x in range(self._size):
                result[x, y] = func(x, y)
        return result        

    def _rand(self):
        return gmpy2.next_prime(randint(50, 100))
