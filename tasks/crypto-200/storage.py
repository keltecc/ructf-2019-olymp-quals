#!/usr/bin/python3

from crypto import Cipher, PasswordGenerator


class User(object):
    def __init__(self, username, password):
        self.username = username
        self._cipher = Cipher(password)
        self._secret = None
        self._sign()

    def check_password(self, password):
        cipher = Cipher(password)
        username = cipher.decrypt(self._signature).decode('utf-8')
        return username == self.username

    def change_password(self, password):
        secret = self.extract_secret()
        self._cipher = Cipher(password)
        self._sign()
        self.place_secret(secret)

    def place_secret(self, secret):
        self._secret = self._cipher.encrypt(secret)

    def extract_secret(self):
        if not self._secret:
            return b''
        return self._cipher.decrypt(self._secret)

    def _sign(self):
        self._signature = self._cipher.encrypt(self.username.encode('utf-8'))


class Storage(object):
    def __init__(self, password_length):
        self._users = dict()
        self._pwgen = PasswordGenerator(password_length)

    def add(self, username):
        if not self.get(username):
            password = self._pwgen.generate()
            user = User(username, password)
            self._users[user.username] = user
            return user, password

    def get(self, username):
        return self._users.get(username, None)
