#!/bin/bash

tasks=$(ls -d1 ./*/)

mkdir "./tasks/"

for task in $tasks; do
    mkdir "./tasks/${task}"
    files=$(cat "${task}files.txt")
    for file in $files; do
        cp "${task}${file}" "./tasks/${task}${file}"
    done
done

zip -r "tasks.zip" "./tasks/"
rm -rf "./tasks/"
