#!/bin/bash

nasm -o "main.o" -f elf "main.asm"
ld -o "main" -melf_i386 "main.o"
rm "main.o"

strip --strip-all "main"
