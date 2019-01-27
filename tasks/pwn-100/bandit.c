#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define ALARM_SECONDS 5

#define BUFFER_SIZE 0x1000

#define FLAG_LENGTH 38
#define FLAG_FILENAME "flag.txt"

/*
gcc bandit.c -o bandit -O0 -Wno-format-security
*/


int flag_size = FLAG_LENGTH;
char flag[FLAG_LENGTH + 1];

void read_flag()
{
    FILE* stream = fopen(FLAG_FILENAME, "r");
    
    if (!stream)
    {
        printf("File readling error!\n");
        exit(-1);
    }

    fgets(flag, flag_size + 1, stream);
    fclose(stream);
}

void secret_weapon(char* buffer)
{
    char bandit[BUFFER_SIZE + 1];

    snprintf(bandit, BUFFER_SIZE, buffer);
    memset(&bandit, 0, BUFFER_SIZE + 1);
}

void setup()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    alarm(ALARM_SECONDS);
}

int main(int argc, char** argv, char** envp)
{
    setup();
    read_flag();

    printf("[*] Hello! Please, enter the flag\n");
    
    char buffer[BUFFER_SIZE + 1];
    fgets(buffer, BUFFER_SIZE, stdin);
    
    secret_weapon(buffer);

    if (!strncmp(flag, buffer, flag_size))
        printf("[+] Correct flag :)\n");
    else
        printf("[-] Wrong flag :(\n");

    return 0;
}
