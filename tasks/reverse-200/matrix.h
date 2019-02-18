#include <stdint.h>

#ifndef H_MATRIX
#define H_MATRIX

#define MATRIX_SIZE 7


void matrix_print(int64_t matrix[]);
void matrix_fill(int64_t value, int64_t result[]);

int64_t matrix_get(int64_t matrix[], int64_t x, int64_t y);
void matrix_set(int64_t matrix[], int64_t x, int64_t y, int64_t value);

int64_t matrix_collapse(int64_t matrix[]);
void matrix_transpose(int64_t matrix[], int64_t result[]);

void matrix_sum(int64_t first[], int64_t second[], int64_t result[]);
void matrix_intsum(int64_t matrix[], int64_t value, int64_t result[]);

void matrix_xor(int64_t first[], int64_t second[], int64_t result[]);
void matrix_intxor(int64_t matrix[], int64_t value, int64_t result[]);

void matrix_mul(int64_t first[], int64_t second[], int64_t result[]);
void matrix_intmul(int64_t matrix[], int64_t value, int64_t result[]);

void matrix_mod(int64_t first[], int64_t second[], int64_t result[]);
void matrix_intmod(int64_t matrix[], int64_t value, int64_t result[]);

void matrix_modmul(int64_t first[], int64_t second[], int64_t modulus[], int64_t result[]);
void matrix_intmodmul(int64_t first[], int64_t second[], int64_t modulus, int64_t result[]);

#endif
