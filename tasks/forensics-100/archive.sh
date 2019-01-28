#!/bin/bash

cat flag.txt | xargs ./image.py
cat password.txt | xargs zip secret.zip secret.png --password

rm secret.png
