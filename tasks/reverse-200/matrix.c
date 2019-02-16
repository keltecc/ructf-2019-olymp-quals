#include <stdio.h>
#include "matrix.h"


void matrix_print(int matrix[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(matrix, x, y);
            printf("%5d ", v);
        }
        printf("\n");
    }
}

void matrix_fill(int value, int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            matrix_set(result, x, y, value);
        }
    }
}


int matrix_get(int matrix[], int x, int y)
{
    return matrix[y * MATRIX_SIZE + x];
}

void matrix_set(int matrix[], int x, int y, int value)
{
    matrix[y * MATRIX_SIZE + x] = value;
}


int matrix_collapse(int matrix[])
{
    int sum = 0;
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(matrix, x, y);
            sum += v;
        }
    }
    return sum;
}

void matrix_transpose(int matrix[], int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(matrix, x, y);
            int w = matrix_get(matrix, y, x);
            matrix_set(result, x, y, w);
            matrix_set(result, y, x, v);
        }
    }
}


void matrix_sum(int first[], int second[], int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(first, x, y);
            int w = matrix_get(second, x, y);
            matrix_set(result, x, y, v + w);
        }
    }
}

void matrix_intsum(int matrix[], int value, int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v + value);
        }
    }
}


void matrix_xor(int first[], int second[], int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(first, x, y);
            int w = matrix_get(second, x, y);
            matrix_set(result, x, y, v ^ w);
        }
    }
}

void matrix_intxor(int matrix[], int value, int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v ^ value);
        }
    }
}


void matrix_mul(int first[], int second[], int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int sum = 0;
            for (int i = 0; i < MATRIX_SIZE; i++)
            {
                int v = matrix_get(first, i, y);
                int w = matrix_get(second, x, i);
                sum += v * w;
            }
            matrix_set(result, x, y, sum);
        }
    }
}

void matrix_intmul(int matrix[], int value, int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v * value);
        }
    }
}


void matrix_mod(int first[], int second[], int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(first, x, y);
            int w = matrix_get(second, x, y);
            matrix_set(result, x, y, v % w);
        }
    }
}

void matrix_intmod(int matrix[], int value, int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(matrix, x, y);
            matrix_set(result, x, y, v % value);
        }
    }
}


void matrix_modmul(int first[], int second[], int modulus[], int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(first, x, y);
            int w = matrix_get(second, x, y);
            int m = matrix_get(modulus, x, y);
            matrix_set(result, x, y, (v * w) % m);
        }
    }
}

void matrix_intmodmul(int first[], int second[], int modulus, int result[])
{
    for (int x = 0; x < MATRIX_SIZE; x++)
    {
        for (int y = 0; y < MATRIX_SIZE; y++)
        {
            int v = matrix_get(first, x, y);
            int w = matrix_get(second, x, y);
            matrix_set(result, x, y, (v * w) % modulus);
        }
    }
}
