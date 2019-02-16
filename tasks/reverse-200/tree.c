#include <stdio.h>
#include "matrix.h"

char* TREE = "                            \n        # #### ####         \n      ### \\/#|### |/####    \n     ##\\/#/ \\||/##/_/##/_#  \n   ###  \\/###|/ \\/ # ###    \n ##_\\_#\\_\\## | #/###_/_#### \n## #### # \\ #| /  #### ##/##\n __#_--###`  |{,###---###-~ \n           \\ }{             \n            }}{             \n            }}{             \n       ejm  {{}             \n      , -=-~{ .-^- _        \n            `}              \n             {              \n                            ";


void generate_X(int result[])
{
    int X_1[MATRIX_SIZE * MATRIX_SIZE];
    int X_2[MATRIX_SIZE * MATRIX_SIZE];

    generate_X_1(X_1);
    generate_X_2(X_2);

    matrix_xor(X_1, X_2, result);
}

void generate_Y(int result[])
{
    int Y_1[MATRIX_SIZE * MATRIX_SIZE];
    int value = 6719;

    generate_Y_1(Y_1);
    
    matrix_intmod(X_1, value, result);
}

void generate_M(int result[])
{
    
}


int main(int argc, char** argv, char** envp)
{
    int X[MATRIX_SIZE * MATRIX_SIZE];
    int Y[MATRIX_SIZE * MATRIX_SIZE];
    int M[MATRIX_SIZE * MATRIX_SIZE];

    int result[MATRIX_SIZE * MATRIX_SIZE];
    
    generate_X(X);
    generate_Y(Y);
    generate_M(M);

    matrix_modmul(X, Y, M, result);

    int collapse = matrix_collapse(result);

    printf("%d\n", collapse);

    return 0;
}
