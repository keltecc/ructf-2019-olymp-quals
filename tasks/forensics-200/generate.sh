#!/bin/bash

flag=$(cat flag.txt)

./write_text.py "$flag" "bliss.png" "secret.png"

password=$(pwgen -1 -s 50)

echo "$password" > password.txt

zip "secret.zip" -0 "secret.png" --password "$password"

rm "secret.png"
