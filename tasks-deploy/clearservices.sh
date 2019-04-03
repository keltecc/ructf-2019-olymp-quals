#!/bin/bash

tasks="$(ls -1d ./*/)"

for task in $tasks; do
    rm -rf "$task/service"
done
