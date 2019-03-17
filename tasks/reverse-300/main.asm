GLOBAL _start

%include "lib.asm"
%include "cipher.asm"


SECTION .text

_start:
    mov     eax, welcome
    mov     ebx, lwelcome
    call    _print

    mov     eax, flag
    mov     ebx, lflag
    call    _scan

    call    _start_cipher
    call    _check_result
    
    test    eax, eax
    jz      _result_correct
    jmp     _result_wrong

_result_correct:
        
    mov     eax, correct
    mov     ebx, lcorrect
    call    _print

    xor     eax, eax
    call    _exit

_result_wrong:
        
    mov     eax, wrong
    mov     ebx, lwrong
    call    _print

    xor     eax, eax
    call    _exit


SECTION .data

    flag:       times FLAG_SIZE db 0,0
    lflag       equ $ - flag

    welcome:    db '[*] Hello! Please, enter the flag',10,0
    lwelcome    equ $ - welcome

    correct:    db '[+] Correct flag :)',10,0
    lcorrect    equ $ - correct

    wrong:      db '[-] Wrong flag :(',10,0
    lwrong      equ $ - wrong
