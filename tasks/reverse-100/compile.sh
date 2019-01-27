#!/bin/bash

movcc movie.c -o movie -s 2> /dev/null
upx -9 movie > /dev/null
