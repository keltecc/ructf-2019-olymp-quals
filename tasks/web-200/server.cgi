i#!/bin/bash


# https://stackoverflow.com/a/37840948
urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }


if [[ "$REQUEST_URI" =~ ^([^?]*) ]]; then
    REQUEST_PATH="${BASH_REMATCH[1]}"
else
    REQUEST_PATH="${REQUEST_URI}"
fi


if [[ "${REQUEST_METHOD}" == "GET" ]]; then
    if [[ "${REQUEST_PATH}" == "/" ]]; then
        echo "Content-Type: text/html"
        echo
        cat "index.html"
    elif [[ "$REQUEST_PATH" == "/admin" ]]; then
        echo "Content-Type: text/plain"
        echo
        cat "/opt/flag.txt"
    else
        echo "Content-Type: text/html"
        echo
        cat "404.html"
    fi
elif [[ "$REQUEST_METHOD" == "POST" ]]; then
    if [[ "${REQUEST_PATH}" =~ .*/([^?]+) ]]; then
        echo "Content-Type: text/plain"
        echo
        url="${BASH_REMATCH[1]}"
        filename="$(echo ${REMOTE_ADDR} | md5sum | cut -d ' ' -f 1)"
        wget -qT1 -t1 -O "./files/${filename}" "$(urldecode ${url})"
        if [[ "$?" == "0" ]]; then
            echo "Host is up for me :)"
        else
            echo "Host is down for me :("
        fi
        rm "./files/${filename}"
    else
        echo "Location: /"
        echo
    fi
fi
