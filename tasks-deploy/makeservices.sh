#/bin/bash

tasks="$(ls -1d ./*/)"

for task in $tasks; do
    original="../tasks/$task/"
    this="./$task/"

    if [ -d "$this/service/" ]; then
        rm -rf "$this/service/"
    fi
    mkdir "$this/service/"

    files="$(cat $original/service.txt)"
    for file in $files; do
        cp -r "$original/$file" "$this/service/"
    done
done

chmod -R 777 "./web-200/service/files/"
