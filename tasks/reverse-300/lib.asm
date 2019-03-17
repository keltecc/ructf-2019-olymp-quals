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
