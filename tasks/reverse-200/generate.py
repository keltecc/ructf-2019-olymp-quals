#!/usr/bin/python3

import sys

import gmpy2
import random
import numpy as np

from engine import Engine


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
    'matrix_transpose': 4,
    'matrix_sum': 6,
    'matrix_intsum': 4,
    'matrix_xor': 6,
    'matrix_intxor': 4,
    'matrix_mul': 6,
    'matrix_intmul': 4,
    'matrix_mod': 10,
    'matrix_intmod': 8,
    'matrix_modmul': 10,
    'matrix_intmodmul': 10
}


def rndcommand():
    commands = sum([[command] * weight for (command, weight) in WEIGHTS.items()], [])
    return random.choice(commands)

def rndprime(lower=100, upper=500):
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

def make_command(code, command, symbol, level, indexes, matrixes, exploit, matrix_names):
    current_code = []
    s_indexes = '_'.join(map(str, indexes))
    current_code.append('void generate_{0}_{1}(int64_t result[])'.format(symbol, s_indexes))
    current_code.append('{')
    args = COMMANDS[command]
    matrix_index = 0
    call_args = []
    exploit.append(command)
    for arg in args:
        if arg == ARG_MATRIX:
            indexes_ = indexes + [matrix_index]
            s_indexes_ = '_'.join(map(str, indexes_))
            matrix_name = 'matrix_{0}_{1}'.format(symbol, s_indexes_)
            matrix_decl = 'int64_t {0}[MATRIX_SIZE * MATRIX_SIZE]'.format(matrix_name)
            if level > 0:
                make_command(code, rndcommand(), symbol, level-1, indexes_, matrixes, exploit, matrix_names)
                line = '\tgenerate_{0}_{1}({2});'.format(symbol, s_indexes_, matrix_name)
                current_code.append('\t' + matrix_decl + ';')
                current_code.append(line)
            else:
                matrix = next(matrixes)
                matrix_names.append(matrix_name)
                line = '{0} = {1};'.format(matrix_decl, c_matrix(matrix))
                code.append(line)
                exploit.append(str(matrix))
            matrix_index += 1
            call_args.append(matrix_name)
        elif arg == ARG_VALUE:
            value = rndprime()
            line = '\tint64_t value = {0};'.format(value);
            exploit.append(str(value))
            call_args.append('value')
            current_code.append(line)
    call_args.append('result')
    call = '\t{0}({1});'.format(command, ', '.join(call_args))
    current_code.append(call)
    current_code.append('}\n')
    code.extend(current_code)


def calculate(engine, exploit):
    command = exploit.pop(0)
    if command not in COMMANDS:
        return command
    args = []
    for _ in range(len(COMMANDS[command])):
        args.append(calculate(engine, exploit))
    expression = 'engine.do("{0}")({1})'.format(command, ', '.join(args))
    return expression


def solve(engine, flag, exploit, funcs):
    command = exploit.pop(0)
    if command not in COMMANDS:
        if command == flag:
            command = 'FLAG'
        funcs.append(command)
        return command
    funcs.append(command)
    args = []
    for _ in range(len(COMMANDS[command])):
        args.append(solve(engine, flag, exploit, funcs))
    expression = 'engine.do("{0}")({1})'.format(command, ', '.join(args))
    if 'FLAG' not in expression:
        [funcs.pop() for _ in range(len(args) + 1)]
        result = str(eval(expression))
        funcs.append(result)
        return str(result)
    return expression    


def build_reverse(engine, need, solved):
    while len(solved) - 1:
        command = solved.pop(0)
        func = engine.reverse(command)
        args = [eval(solved.pop()) for _ in range(len(COMMANDS[command])-1)]
        args.append(need)
        need = func(*args)
    return need


def generate(engine, command, symbol, level, matrixes, correct):
    flag = matrixes[0]
    code = ['#include <stdint.h>', '#include "matrix.h"', '\n']
    exploit = []
    names = []

    make_command(code, command, symbol, level, [0], iter(matrixes), exploit, names)

    expr = calculate(engine, exploit[:])
    need = eval(expr)

    assert all(x < 2 ** 62 for x in sum(need, [])), 'bigger!'

    expr = expr.replace('engine.do("matrix_', '').replace('")', '')
    code.extend(['/* ', '* result', '* ' + c_matrix(need), '* ' + repr(need), '*/', '\n'])
    code.extend(['/* ', '* full expression', '* ' + expr, '*/', '\n'])

    if correct:
        funcs = []
        sol = solve(engine, str(flag), exploit[:], funcs)
        reverse = build_reverse(engine, need, funcs[:])
        if reverse != flag:
            raise Exception('not equal!')
        short_expr = '{0} == {1}'.format(sol.replace('engine.do("matrix_', '').replace('")', ''), str(need))
        code.extend(['/* ', '* short expression', '* ' + short_expr, '*/', '\n'])
        code.extend(['/* ', '* exploit data', '', '\n'.join(funcs), '', '*/', '\n'])
    return '\n'.join(code), need, names[0]


def find_modulus(X, Y):
    def invert(x, y):
        f = x * y
        for i in range(1, x):
            t = (f - 1) // i
            if f % t == 1:
                return t
    modulus = np.zeros((MATRIX_SIZE, MATRIX_SIZE), 'int')
    for x in range(MATRIX_SIZE):
        for y in range(MATRIX_SIZE):
            modulus[x, y] = invert(X[x][y], Y[x][y])
    return modulus.tolist()


def build_check(M):
    code = []
    code.append('int64_t M[MATRIX_SIZE * MATRIX_SIZE] = {0};'.format(c_matrix(M)))
    code.append('int64_t check()')
    code.append('{')
    code.append('\tint64_t X[MATRIX_SIZE * MATRIX_SIZE];')
    code.append('\tint64_t Y[MATRIX_SIZE * MATRIX_SIZE];')
    code.append('\tint64_t result[MATRIX_SIZE * MATRIX_SIZE];')
    code.append('')
    code.append('\tgenerate_X_0(X);')
    code.append('\tgenerate_Y_0(Y);')
    code.append('')
    code.append('\tmatrix_modmul(X, Y, M, result);')
    code.append('')
    code.append('\treturn matrix_collapse(result) == 49;')
    code.append('}')
    return '\n'.join(code)


def main(level):
    if len(sys.argv) < 2:
        print('usage: {} <your_flag>'.format(sys.argv[0]))
        sys.exit(-1)

    with open('tree.c.template', 'r') as file:
        template = file.read()

    text_flag = sys.argv[1].strip()

    flag = [ord(x) for x in text_flag] + [rndprime() for _ in range(MATRIX_SIZE*MATRIX_SIZE - len(text_flag))]
    fake_flag = [0] * len(text_flag) + flag[len(text_flag):]

    flag = np.matrix(flag).reshape(MATRIX_SIZE, MATRIX_SIZE).tolist()
    fake_flag = np.matrix(fake_flag).reshape(MATRIX_SIZE, MATRIX_SIZE).tolist()    

    engine = Engine(MATRIX_SIZE)

    count = 15 * level
    matrixes = [flag] + [rndmatrix() for i in range(2 * count)]
    parts = [matrixes[count*0:count*0+count], matrixes[count*1:count*1+count]]
    while True:
        try:
            generated = []
            names = []
            for i, symbol in enumerate('XY'):
                part = parts[i]
                code, need, name = generate(engine, rndcommand(), symbol, level, part, not bool(i))
                if c_matrix(flag) in code:
                    code = code.replace(c_matrix(flag), c_matrix(fake_flag))
                with open('{0}_generation.h'.format(symbol), 'w') as file:
                    file.write(code)
                generated.append(need)
                names.append(name)

            check = build_check(find_modulus(*generated))
            name = names[0]
            break
        except Exception as e:
            pass
            print(e, file=sys.stderr)

    with open('tree.c', 'w') as file:
        file.write(template.replace('%CHECK_FUNC%', check).replace('%MATRIX_NAME%', name))

    print('done.')


if __name__ == '__main__':
    main(5)
