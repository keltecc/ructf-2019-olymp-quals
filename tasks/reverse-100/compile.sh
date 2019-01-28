#!/bin/bash

movcc movie.c -o movie -s
upx -9 movie
