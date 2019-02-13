pop eax
pop ebx

add eax, 4

xor ecx, ecx
mov cl, byte [eax]

sub eax, 4

add ebx, 6

xor edx, edx
mov edx, [ebx]

sub edx, ecx 
mov [ebx], edx

sub ebx, 6

push ebx
push eax

