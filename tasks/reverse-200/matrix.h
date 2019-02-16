#ifndef H_MATRIX
#define H_MATRIX

#define MATRIX_SIZE 3


void matrix_print(int matrix[]);
void matrix_fill(int value, int result[]);

int matrix_get(int matrix[], int x, int y);
void matrix_set(int matrix[], int x, int y, int value);

int matrix_collapse(int matrix[]);
void matrix_transpose(int matrix[], int result[]);

void matrix_sum(int first[], int second[], int result[]);
void matrix_intsum(int matrix[], int value, int result[]);

void matrix_xor(int first[], int second[], int result[]);
void matrix_intxor(int matrix[], int value, int result[]);

void matrix_mul(int first[], int second[], int result[]);
void matrix_intmul(int matrix[], int value, int result[]);

void matrix_mod(int first[], int second[], int result[]);
void matrix_intmod(int matrix[], int value, int result[]);

void matrix_modmul(int first[], int second[], int modulus[], int result[]);
void matrix_intmodmul(int first[], int second[], int modulus, int result[]);

#endif
