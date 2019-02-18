#include <stdio.h>
#include <stdint.h>

#include "matrix.h"


void matrix_print(int64_t matrix[])
{
    for (int64_t y = 0; y < MATRIX_SIZE; y++)
    {
        for (int64_t x = 0; x < MATRIX_SIZE; x++)
        {
            int64_t v = matrix_get(matrix, x, y);
            printf("%5ld ", v);
        }
        printf("\n");
    }
}

void matrix_fill(int64_t value, int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            matrix_set(result, x, y, value);
        }
    }
}


int64_t matrix_get(int64_t matrix[], int64_t x, int64_t y)
{
    return matrix[y * MATRIX_SIZE + x];
}

void matrix_set(int64_t matrix[], int64_t x, int64_t y, int64_t value)
{
    matrix[y * MATRIX_SIZE + x] = value;
}


int64_t matrix_collapse(int64_t matrix[])
{
    int64_t sum = 0;
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(matrix, x, y);
            sum += v;
        }
    }
    return sum;
}

void matrix_transpose(int64_t matrix[], int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(matrix, x, y);
            int64_t w = matrix_get(matrix, y, x);
            matrix_set(result, x, y, w);
            matrix_set(result, y, x, v);
        }
    }
}


void matrix_sum(int64_t first[], int64_t second[], int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(first, x, y);
            int64_t w = matrix_get(second, x, y);
            matrix_set(result, x, y, v + w);
        }
    }
}

void matrix_intsum(int64_t matrix[], int64_t value, int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v + value);
        }
    }
}


void matrix_xor(int64_t first[], int64_t second[], int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(first, x, y);
            int64_t w = matrix_get(second, x, y);
            matrix_set(result, x, y, v ^ w);
        }
    }
}

void matrix_intxor(int64_t matrix[], int64_t value, int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v ^ value);
        }
    }
}


void matrix_mul(int64_t first[], int64_t second[], int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t sum = 0;
            for (int64_t i = 0; i < MATRIX_SIZE; i++)
            {
                int64_t v = matrix_get(first, i, y);
                int64_t w = matrix_get(second, x, i);
                sum += v * w;
            }
            matrix_set(result, x, y, sum);
        }
    }
}

void matrix_intmul(int64_t matrix[], int64_t value, int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v * value);
        }
    }
}


void matrix_mod(int64_t first[], int64_t second[], int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(first, x, y);
            int64_t w = matrix_get(second, x, y);
            matrix_set(result, x, y, v % w);
        }
    }
}

void matrix_intmod(int64_t matrix[], int64_t value, int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v % value);
        }
    }
}


void matrix_modmul(int64_t first[], int64_t second[], int64_t modulus[], int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(first, x, y);
            int64_t w = matrix_get(second, x, y);
            int64_t m = matrix_get(modulus, x, y);
            matrix_set(result, x, y, (v * w) % m);
        }
    }
}

void matrix_intmodmul(int64_t first[], int64_t second[], int64_t modulus, int64_t result[])
{
    for (int64_t x = 0; x < MATRIX_SIZE; x++)
    {
        for (int64_t y = 0; y < MATRIX_SIZE; y++)
        {
            int64_t v = matrix_get(first, x, y);
            int64_t w = matrix_get(second, x, y);
            matrix_set(result, x, y, (v * w) % modulus);
        }
    }
}
