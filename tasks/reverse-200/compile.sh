#!/bin/bash

gcc -o numbers -m32 -O0 -s numbers.c md5_modified.c md5.h
