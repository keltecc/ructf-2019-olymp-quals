#!/usr/bin/python3

import json
import random

from base64 import b64encode
from string import ascii_uppercase, ascii_lowercase, digits
from Crypto.Cipher import AES


class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        self._secret = None

    def check_password(self, password):
        return password == self._password

    def place_secret(self, secret):
        secret = self._pad(secret)
        self._secret = self._cipher().encrypt(secret)

    def extract_secret(self):
        if not self._secret:
            return b''
        secret = self._cipher().decrypt(self._secret)
        return self._unpad(secret)

    def get_info(self):
        info = {'username': self.username, 'secret': b64encode(self._secret or b'').decode()}
        return json.dumps(info)

    def _cipher(self):
        return AES.new(self._password.encode('utf-8'), AES.MODE_ECB)

    def _pad(self, data):
        byte = 16 - (len(data) % 16)
        return data + bytes([byte] * byte)

    def _unpad(self, data):
        byte = data[-1]
        return data[:-byte]


class Storage:
    def __init__(self):
        self._storage = dict()

    def add_user(self, user):
        if not self.get_user(user.username):
            self._storage[user.username] = user

    def get_user(self, username):
        return self._storage.get(username, None)

    def generate_password(self):
        password_length = 16
        alpabet = ascii_uppercase + ascii_lowercase + digits + '_'
        return ''.join(random.choice(alpabet) for i in range(password_length))
