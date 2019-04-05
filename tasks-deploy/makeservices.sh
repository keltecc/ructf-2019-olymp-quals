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

chmod -R 777 "./web-100/service/files/"
chmod -R 777 "./web-200/service/files/"
chmod -R 777 "./web-300/service/data/"

mkdir "./web-200/flag/"
mv "./web-200/service/flag.txt" "./web-200/flag/flag.txt"
