#!/usr/bin/python3

import random

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
        key = self._password.encode('utf-8')[:16]
        key += b'\x00' * (16 - len(key))
        return AES.new(key, AES.MODE_ECB)

    def _pad(self, data):
        byte = 16 - (len(data) % 16)
        return data + bytes([byte] * byte)

    def _unpad(self, data):
        byte = data[-1]
        return data[:-byte]


class Storage:
    def __init__(self):
        self._storage = dict()
        self._generator = PasswordGenerator()

    def add_user(self, user):
        if not self.get_user(user.username):
            self._storage[user.username] = user

    def get_user(self, username):
        return self._storage.get(username, None)

    def generate_password(self):
        length = 8
        return self._generator.generate(length)


class PasswordGenerator:
    def __init__(self):
        self._alphabet = ''.join([
            'Ok3AaFKHLpZTEoqwd8vC3tMjjDKh2PMf',
            'pv67c9Zy@qHojoPANtaHXyeWBrigOA$V',
            'MRa0pHSzBUalVrqh8IRQTEN7wFMUzlbO',
            '5j5tXXosWW6gE6eVYwRCC@9EkJkQR7Q2',
            '4YV51$dlo9M1u9iSPVxNUKDdRr5XkpnD',
            'XUD84szJ$m3FwxU@myTqUg@SVvumDOb2',
            'J12csWHB0860QuB$vWThFezOAA6fF6EK',
            '4tiNITfnjuWIAS3iGTe9MrswOgebxFhf',
            'AGLxFgJq3LZ@1IDnjvQbg58e1nZ1fbTr',
            'smrIBzaRL9KCextG$o5ns6hZGL3kEQlC',
            '@s@uCdB5fUg1veNhGU7XblhVt0oP7EuI',
            'A2b8q5MHic0OPJid0Xlt8RiafZ9@vhHy',
            'PLVK2wLN$jdIa2yC4wdNX2PqDjFEmYRw',
            'lkWY1SMcNSyDKpId34T04ckmtb0nsqJB',
            'nZCPczGJSGLfpx8i4urkozxlWvnYgacO',
            'pKmzYr7BYyQ64p$7J$7QxmyG3ZSuHY9c'
        ])

    def generate(self, length):
        size = 2
        parts = self._parts(self._alphabet, size)
        self._shift()
        return ''.join(random.choice(parts) for _ in range(length))

    def _shift(self):
        value = 4
        self._alphabet = self._alphabet[-value:] + self._alphabet[:-value]

    def _parts(self, text, size):
        return [''.join(part) for part in zip(*(text[i::size] for i in range(size)))]
