#!/bin/bash

flag=$(cat flag.txt)

./text2img.py "$flag" "flag_original.png"
./encoder "flag_original.png" "flag.png"

password=$(pwgen -1 -s 50)

echo "$password" > password.txt

zip "secret.zip" -0 "flag.png" --password "$password"
zip "secret.zip" -0 "encoder" --password "$password"

rm "flag_original.png" "flag.png"
