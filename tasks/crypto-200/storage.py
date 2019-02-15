#!/usr/bin/python3

import random

from base64 import b64encode
from hashlib import md5
from Crypto.Cipher import AES


class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password
        self._secret = None

    def check_password(self, password):
        return password == self._password

    def change_password(self, password):
        secret = self.extract_secret()
        self._password = password
        self.place_secret(secret)

    def place_secret(self, secret):
        secret = self._pad(secret)
        self._secret = self._cipher().encrypt(secret)

    def extract_secret(self):
        if not self._secret:
            return b''
        secret = self._cipher().decrypt(self._secret)
        return self._unpad(secret)

    def _cipher(self):
        key = md5(self._password.encode('utf-8')).digest()
        return AES.new(key, AES.MODE_ECB)

    def _pad(self, data):
        byte = 16 - (len(data) % 16)
        return data + bytes([byte] * byte)

    def _unpad(self, data):
        byte = data[-1]
        return data[:-byte]


class Storage:
    def __init__(self, password_length):
        self._storage = dict()
        self._password_length = int(password_length * 3 / 4)

    def add_user(self, user):
        if not self.get_user(user.username):
            self._storage[user.username] = user

    def get_user(self, username):
        return self._storage.get(username, None)

    def generate_password(self):
        hexlen = 2 * self._password_length
        bitlen = 4 * hexlen
        data = hex(random.getrandbits(bitlen))[2:].zfill(hexlen)
        return b64encode(bytes.fromhex(data), b'@$').decode()
