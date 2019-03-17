%include "blocks.asm"


SECTION .text

_decrypt_block:
    push    ecx
    mov     ecx, BLOCK_SIZE
    jmp     _decrypt_block_loop

_decrypt_block_loop:
    xor     eax, eax
    xor     ebx, ebx
    mov     al, byte [esi]
    mov     bl, byte [edi]
    xor     al, bl
    mov     [edi], al
    inc     esi
    inc     edi
    loop    _decrypt_block_loop
    pop ecx
    ret

_start_cipher:
    mov     ecx, BLOCKS_COUNT
    xor     eax, eax
    xor     ebx, ebx
    jmp     _start_cipher_loop

_start_cipher_loop:
    mov     edx, BLOCK_SIZE
    mul     edx
    lea     esi, [xors + eax]
    mov     eax, ebx
    mov     edx, BLOCK_SIZE
    mul     edx
    lea     edi, [blocks + eax]
    push    edi
    call    _decrypt_block
    mov     esi, flag
    mov     edi, expected
    pop     eax
    call    eax
    loop    _start_cipher_loop
    ret

_check_result:
    mov     ecx, FLAG_SIZE
    xor     eax, eax
    xor     edx, edx
    jmp     _check_result_loop

_check_result_loop:
    mov     ebx, [expected + 4*edx]
    or      eax, ebx
    inc     edx
    loop    _check_result_loop
    ret
