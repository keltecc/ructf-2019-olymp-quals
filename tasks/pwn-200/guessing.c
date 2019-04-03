#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define ALARM_SECONDS 60
#define GUESSING_LIMIT 10
#define MAX_STRING_LENGTH 255


// gcc -o guessing -O0 guessing.c


typedef struct
{
    int length;
    char* content;
} string;

void input_string(string* str)
{
    int length;

    gets(str->content);
    length = strlen(str->content);

    if (length <= MAX_STRING_LENGTH)
    {
        str->length = length;
        str->content[length] = 0;
        return;
    }

    puts("[-] Error: string is too long!");
    exit(1);
}

void welcome(string* name, string* city)
{
    puts("[!] Welcome to another guessing challenge!");
    puts("[!] You need to guess as many numbers as you can.\n");

    puts("[*] Before the challenge begins we need to know something about you:");

    puts("[?] Please, input your name");
    input_string(name);
    
    puts("[?] Please, input a city where are you from");
    input_string(city);

    fputs("[+] Hello, ", stdout);
    fputs(name->content, stdout);
    fputs(" from ", stdout);
    fputs(city->content, stdout);
    fputs("!\n\n", stdout);
}

void start_guessing()
{
    int i;
    int count;
    int input;
    int guess;

    puts("[*] Ok, now it's time to guess:");
    count = 0;
    
    for (i = 0; i < GUESSING_LIMIT; i++)
    {
        puts("[?] Please, input a number: ");
        scanf("%d", &input);
        guess = rand();

        if (input == guess)
        {
            puts("[+] Yay, you're right!");
            count += 1;
        }
        else
        {
            puts("[-] Sorry, but you're wrong. Try again!");
        }
    }

    if (count == GUESSING_LIMIT)
        puts("[+] Confirmed, you are a guessing master!");
    else
        puts("[-] Your guessing skills aren't good enough :(");
}

void setup()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    alarm(ALARM_SECONDS);

    srand(time(NULL));
}

void main(int argc, char** argv, char** envp)
{
    string* name;
    string* city;
    
    setup();

    name = malloc(sizeof(string));
    name->content = malloc(MAX_STRING_LENGTH + 1);

    city = malloc(sizeof(string));
    city->content = malloc(MAX_STRING_LENGTH + 1);    

    welcome(name, city);
    start_guessing();

    free(name->content);
    free(name);

    free(city->content);
    free(city);
}
