#include <stdio.h>
#include <stdlib.h>

#define FILENAME "/tmp/your_favourite_movie"

#define COMMAND_SIZE 1024
#define COMMAND_MASK "(/bin/sleep 0.1 && /bin/rm %s 2>/dev/null &); /bin/bash %s"

#define SCRIPT "echo \"[*] Hello! Please, enter the flag\"; read flag; if [ \"${flag:0:1}\" == \"R\" ]; then if [ \"${flag:1:1}\" == \"u\" ]; then if [ \"${flag:2:1}\" == \"C\" ]; then if [ \"${flag:3:1}\" == \"T\" ]; then if [ \"${flag:4:1}\" == \"F\" ]; then if [ \"${flag:5:1}\" == \"_\" ]; then if [ \"${flag:6:1}\" == \"7\" ]; then if [ \"${flag:7:1}\" == \"2\" ]; then if [ \"${flag:8:1}\" == \"e\" ]; then if [ \"${flag:9:1}\" == \"d\" ]; then if [ \"${flag:10:1}\" == \"5\" ]; then if [ \"${flag:11:1}\" == \"f\" ]; then if [ \"${flag:12:1}\" == \"3\" ]; then if [ \"${flag:13:1}\" == \"c\" ]; then if [ \"${flag:14:1}\" == \"4\" ]; then if [ \"${flag:15:1}\" == \"6\" ]; then if [ \"${flag:16:1}\" == \"7\" ]; then if [ \"${flag:17:1}\" == \"3\" ]; then if [ \"${flag:18:1}\" == \"4\" ]; then if [ \"${flag:19:1}\" == \"e\" ]; then if [ \"${flag:20:1}\" == \"1\" ]; then if [ \"${flag:21:1}\" == \"d\" ]; then if [ \"${flag:22:1}\" == \"8\" ]; then if [ \"${flag:23:1}\" == \"8\" ]; then if [ \"${flag:24:1}\" == \"6\" ]; then if [ \"${flag:25:1}\" == \"8\" ]; then if [ \"${flag:26:1}\" == \"7\" ]; then if [ \"${flag:27:1}\" == \"d\" ]; then if [ \"${flag:28:1}\" == \"3\" ]; then if [ \"${flag:29:1}\" == \"e\" ]; then if [ \"${flag:30:1}\" == \"9\" ]; then if [ \"${flag:31:1}\" == \"9\" ]; then if [ \"${flag:32:1}\" == \"c\" ]; then if [ \"${flag:33:1}\" == \"e\" ]; then if [ \"${flag:34:1}\" == \"e\" ]; then if [ \"${flag:35:1}\" == \"7\" ]; then if [ \"${flag:36:1}\" == \"8\" ]; then if [ \"${flag:37:1}\" == \"e\" ]; then echo \"[+] Correct flag :)\"; exit 0; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi; fi;  echo \"[-] Wrong flag :(\"; exit 1;"

/*
movcc movie.c -o movie -s
*/


void write_script()
{
    FILE* stream = fopen(FILENAME, "w");

    if (!stream)
    {
        printf("Looks like you aren't a movie lover :(\n");
        exit(-1);
    }
    
    fputs(SCRIPT, stream);
    fclose(stream);
}

int main(int argc, char** argv, char** envp)
{
    char command[COMMAND_SIZE + 1];
    
    write_script();
    snprintf(command, COMMAND_SIZE, COMMAND_MASK, FILENAME, FILENAME);

    system(&command);
    remove(FILENAME);

    return 0;
}
