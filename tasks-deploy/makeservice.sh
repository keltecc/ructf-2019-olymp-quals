#/bin/bash

if [[ "$1" == "" ]]; then
    task="$(basename `pwd`)"
    original="../../tasks/$task/"
    this="./"
else
    task="$1"
    original="../tasks/$task/"
    this="./$task/"
    mkdir $task
fi

mkdir "$this/service/"

files="$(cat $original/service.txt)"
for file in $files; do
    cp "$original/$file" "$this/service/"
done
