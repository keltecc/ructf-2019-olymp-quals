#!/usr/bin/python3

import gmpy2
import random

import numpy as np


MATRIX_SIZE = 7

ARG_MATRIX = 1
ARG_VALUE = 2

COMMANDS = {
    'matrix_transpose': (ARG_MATRIX,),
    'matrix_sum': (ARG_MATRIX, ARG_MATRIX),
    'matrix_intsum': (ARG_MATRIX, ARG_VALUE),
    'matrix_xor': (ARG_MATRIX, ARG_MATRIX),
    'matrix_intxor': (ARG_MATRIX, ARG_VALUE),
    'matrix_mul': (ARG_MATRIX, ARG_MATRIX),
    'matrix_intmul': (ARG_MATRIX, ARG_VALUE),
    'matrix_mod': (ARG_MATRIX, ARG_MATRIX),
    'matrix_intmod': (ARG_MATRIX, ARG_VALUE),
    'matrix_modmul': (ARG_MATRIX, ARG_MATRIX, ARG_MATRIX),
    'matrix_intmodmul': (ARG_MATRIX, ARG_MATRIX, ARG_VALUE)
}

WEIGHTS = {
    'matrix_transpose': 9,
    'matrix_sum': 3,
    'matrix_intsum': 6,
    'matrix_xor': 3,
    'matrix_intxor': 6,
    'matrix_mul': 3,
    'matrix_intmul': 6,
    'matrix_mod': 3,
    'matrix_intmod': 6,
    'matrix_modmul': 1,
    'matrix_intmodmul': 0
}


def rndcommand():
    commands = sum([[command] * weight for (command, weight) in WEIGHTS.items()], [])
    return random.choice(commands)

def rndprime(lower=100, upper=1000000):
    number = random.randint(lower, upper)
    return int(gmpy2.next_prime(number))

def rndmatrix():
    matrix = []
    for y in range(MATRIX_SIZE):
        matrix.append([rndprime() for x in range(MATRIX_SIZE)])
    return matrix

def c_matrix(matrix):
    matrix = sum(matrix, [])
    return '{{{0}}}'.format(', '.join(map(str, matrix)))

def make_command(code, command, symbol, level, matrixes, indexes):
    current_code = []
    current_code.append('void generate_{0}_{1}(int result[])'.format(symbol, '_'.join(map(str, indexes))))
    current_code.append('{')
    args = COMMANDS[command]
    matrix_index = 0
    call_args = []
    for arg in args:
        if arg == ARG_MATRIX:
            matrix_name = 'matrix{0}'.format(matrix_index)
            current_code.append('\tint {0}[MATRIX_SIZE * MATRIX_SIZE];'.format(matrix_name))
            if level > 0:
                indexes_ = indexes + [matrix_index]
                make_command(code, rndcommand(), symbol, level-1, matrixes, indexes_)
                line = '\tgenerate_{0}_{1}({2});'.format(symbol, '_'.join(map(str, indexes_)), matrix_name)
            else:
                line = '\t{0} = {1};'.format(matrix_name, c_matrix(next(matrixes)))
            matrix_index += 1
            call_args.append(matrix_name)
        elif arg == ARG_VALUE:
            line = '\tint value = {0};'.format(rndprime());
            call_args.append('value')
        current_code.append(line)
    call_args.append('result')
    call = '\t{0}({1});'.format(command, ', '.join(call_args))
    current_code.append(call)
    current_code.append('}\n')
    code.extend(current_code)
    print(level, '_'.join(map(str, indexes)))


code = []
matrixes = (rndmatrix() for i in range(10000))
make_command(code, 'matrix_intmodmul', 'X', 3, matrixes, [0])
make_command(code, 'matrix_intmodmul', 'Y', 3, matrixes, [0])
make_command(code, 'matrix_intmodmul', 'M', 3, matrixes, [0])

# print('\n'.join(code))
