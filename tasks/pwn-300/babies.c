#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define ALARM_SECONDS 30

#define BABIES_COUNT 10
#define BABY_NAME_LENGTH 100


/*
gcc -o babies -O0 -fno-stack-protector babies.c
*/


typedef struct {
    int number;
    char name[BABY_NAME_LENGTH];
} baby;

int kindergarten() {
    baby babies[BABIES_COUNT];
    int baby_number;
    char buffer[BABY_NAME_LENGTH];

    puts("[*] Hello! This stack is only for babies!");
    puts("[*] Be careful! They can execute /bin/sh");

    baby_number = 0;

    while (1) {
        puts("[?] Please, input a name for new baby (leave empty for exit):");
        
        fgets(buffer, BABY_NAME_LENGTH, stdin);

        if (strlen(buffer) > 1) {
            babies[baby_number].number = baby_number;
            memcpy(babies[baby_number].name, buffer, BABY_NAME_LENGTH);
            puts("[+] Baby was added!\n");
            baby_number++;
        }
        else {
            puts("[+] Ok, goodbye!");
            break;
        }
    }

    return baby_number;
}

void setup()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    asm ("syscall");
    alarm(30);
}

int main(int argc, char** argv, char** envp)
{
    setup();
    kindergarten();

    return 0;
}
