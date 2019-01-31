#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "md5.h"

#define FLAG_LENGTH 38

/*
gcc -o numbers -static -m32 -O0 -s numbers.c md5_modified.c md5.h
*/


int check(char* buffer)
{
    BYTE result[MD5_BLOCK_SIZE];
    BYTE expected[MD5_BLOCK_SIZE] = {0xc9, 0x1a, 0x7c, 0xcd, 0xdf, 0xe2, 0x2e, 0x84, 0x39, 0xc6, 0x1b, 0x74, 0x10, 0x91, 0x68, 0xec};

    MD5_CTX ctx;
    md5_init(&ctx);
    md5_update(&ctx, buffer, FLAG_LENGTH);
    md5_final(&ctx, result);

    return !memcmp(expected, result, MD5_BLOCK_SIZE);
}

int main(int argc, char** argv, char** envp)
{
    char buffer[FLAG_LENGTH + 1];

    printf("[*] Hello! Please, enter the flag\n");
    fgets(buffer, FLAG_LENGTH + 1, stdin);

    if (check(buffer))
        printf("[+] Correct flag :)\n");
    else
        printf("[-] Wrong flag :(\n");

    return 0;
}
