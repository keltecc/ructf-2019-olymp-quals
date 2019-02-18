#include <stdio.h>
#include <stdint.h>

#include "matrix.h"
#include "X_generation.h"
#include "Y_generation.h"

#define FLAG_LENGTH 38

/*
gcc tree.c matrix.h matrix.c X_generation.h Y_generation.h -o tree -O0
*/


char* TREE = "                            \n        # #### ####         \n      ### \\/#|### |/####    \n     ##\\/#/ \\||/##/_/##/_#  \n   ###  \\/###|/ \\/ # ###    \n ##_\\_#\\_\\## | #/###_/_#### \n## #### # \\ #| /  #### ##/##\n __#_--###`  |{,###---###-~ \n           \\ }{             \n            }}{             \n            }}{             \n       ejm  {{}             \n      , -=-~{ .-^- _        \n            `}              \n             {              \n                            ";


int64_t M[MATRIX_SIZE * MATRIX_SIZE] = {10712592574553, 20314832137924, 15080025663807, 213048700069, 11036919738695, 9374880243695, 831734137607, 763621833559, 7783931313339, 24033532953359, 5878087365037, 4008171346244, 2616993397699, 18151037829956, 1687595433495, 10774182261179, 14978704017439, 5596859341695, 15028663850195, 1126161331767, 5397463204335, 5204763464599, 25168903652445, 19572671636249, 4029032412648, 2794614598907, 1077173489969, 11805801558999, 7143010586042, 10930591332065, 12571454993449, 1416782111953, 5164740627111, 9143042536191, 3422118765005, 10642766793144, 18533623993390, 5763891235101, 1431507885659, 17338602143600, 7466518612673, 7258087337369, 78391281869, 11012394366635, 14910773038524, 1250587031519, 19417832707253, 10823064499465, 12904730340306};
int64_t check()
{
	int64_t X[MATRIX_SIZE * MATRIX_SIZE];
	int64_t Y[MATRIX_SIZE * MATRIX_SIZE];
	int64_t result[MATRIX_SIZE * MATRIX_SIZE];

	generate_X_0(X);
	generate_Y_0(Y);

	matrix_modmul(X, Y, M, result);

	return matrix_collapse(result) == 49;
}

int64_t main(int argc, char** argv, char** envp)
{
    char buffer[FLAG_LENGTH + 1];

    printf("[*] Hello! Please, enter the flag\n");
    fgets(buffer, FLAG_LENGTH + 1, stdin);

    for (int64_t i = 0; i < FLAG_LENGTH; i++)
    {
        matrix_X_0_0_0_0_0_0_0[i] = buffer[i];
    }
    
    if (check())
        printf("[+] Correct flag :)\n");
    else
        printf("[-] Wrong flag :(\n");

    return 0;
}
