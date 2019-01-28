#!/bin/bash

hash=$(head /dev/urandom | md5sum)
echo "RuCTF_${hash:0:32}"
