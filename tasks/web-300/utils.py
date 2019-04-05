#!/usr/bin/python3

import re

from os import environ, makedirs
from glob import glob
from string import printable
from hashlib import sha256

from os.path import curdir, isfile, isdir, dirname, realpath, join, basename


def check_username(username):
    return username != 'admin'


def check_filename(filename):
    pattern = '^\w{1,20}(\.\w{1,4})?$'
    match = re.match(pattern, filename)
    return bool(match)


def check_content(content):
    return len(content) < 100 and all(symbol in printable for symbol in content)


def enumerate_files(username):
    return list(map(basename, glob(_build_path(username, '*'))))


def read_file(username, filename):
    path = _build_path(username, filename)
    if not _check_path(path):
        return 'error: hacking attempt detected!'
    if not isfile(path):
        return 'error: file does not exist!'
    try:
        with open(path, 'rb') as file:
            return file.read()
    except Exception:
        return ''


def write_file(username, filename, content):
    path = _build_path(username, filename)
    try:
        _create_dir_if_not_exist(dirname(path))
        with open(path, 'wb') as file:
            file.write(content.encode())
    except Exception:
        pass


def _create_dir_if_not_exist(path):
    if not isdir(path):
        makedirs(path)


def _check_path(path):
    pathdir = dirname(realpath(path))
    current = realpath(curdir)
    return pathdir.startswith(current) and pathdir != current


def _build_path(username, filename):
    return join(curdir, 'data', _calculate_hash(username), filename)


def _calculate_hash(username):
    salt = ''.join(map(''.join, environ.items()))
    data = salt + username + salt
    return sha256(data.encode()).hexdigest()
