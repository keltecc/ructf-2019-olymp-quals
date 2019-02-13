#!/bin/bash

if [ "$1" == "" ]; then
    echo "source code filename as 1st argument"
    exit
fi

if [ "$2" == "" ]; then
    echo "executable filename as 2nd argument"
    exit
fi

nasm -o "temp.o" -f elf "$1" && ld -o "$2" -melf_i386 "temp.o" && rm "temp.o"
