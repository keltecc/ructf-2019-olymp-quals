GLOBAL _start

%define FLAG_SIZE 10


SECTION .text

_exit:
    mov     ebx, eax
    mov     eax, 1
    int     80h
    ret

_print:
    mov     ecx, eax
    mov     edx, ebx
    mov     eax, 4
    mov     ebx, 1
    int     80h
    ret

_scan:
    mov     ecx, eax
    mov     edx, ebx
    mov     eax, 3
    xor     ebx, ebx
    int     80h
    ret

_start:
    mov     eax, welcome
    mov     ebx, lwelcome
    call    _print

    mov     eax, flag
    mov     ebx, lflag
    call    _scan

    mov     eax, flag
    mov     ebx, lflag
    call    _print

    mov     eax, correct
    mov     ebx, lcorrect
    call    _print

    xor     eax, eax
    call    _exit


SECTION .data

    flag:       times FLAG_SIZE db 0,0
    lflag       equ $ - flag

    expected:   times FLAG_SIZE dd 0,0
    lexpected   equ $ - expected

    welcome:    db '[*] Hello! Please, enter the flag',10,0
    lwelcome    equ $ - welcome

    correct:    db '[+] Correct flag :)',10,0
    lcorrect    equ $ - correct

    wrong:      db '[-] Wrong flag :(',10,0
    lwrong      equ $ - wrong
