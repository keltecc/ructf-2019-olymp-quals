#!/usr/bin/python3

from os import urandom
from hashlib import md5


class UI(object):
    def __init__(self, rsa, message):
        self._rsa = rsa
        self._message = message
    
    def interact(self):
        # if not self._check_proof():
        #     return
        self._welcome(self._message)
        self._menu()
        print('[*] Bye')

    def _menu(self):
        while True:
            option = self._select('Enter the ENCRYPTION mode', 'Enter the DECRYPTION mode', 'Exit')
            if option == 1:
                self._encryption()
            elif option == 2:
                self._decryption()
            else:
                break

    def _encryption(self):
        print('[*] Send me a plaintexts (numbers) in separate lines. Leave empty line to exit.')
        while True:
            plaintext = self._read_int()
            if plaintext is None:
                break
            print(self._rsa.encrypt(plaintext))

    def _decryption(self):
        print('[*] Send me a ciphertexts (numbers) in separate lines. Leave empty line to exit.')
        while True:
            ciphertext = self._read_int()
            if ciphertext is None:
                break
            print(self._rsa.decrypt(ciphertext))

    def _read_int(self):
        while True:
            line = input('> ').strip()
            if len(line) == 0:
                return None
            try:
                return int(line)
            except ValueError:
                print('[-] You should input an integer!')

    def _select(self, *options):
        print('[?] Please, select an option:')
        for i, option in enumerate(options):
            print('[{0}] {1}'.format(str(i + 1), option))
        while True:
            try:
                choice = int(input().strip())
                if 0 <= choice - 1 < len(options):
                    break
                print('[-] You should select an existing option!')
            except ValueError:
                print('[-] You should input an integer!')
        return choice

    def _welcome(self, message):
        print('[*] Hello! I have a message for you. Please, decrypt it:')
        print('[*] {0}'.format(message), end='\n\n')

    def _check_proof(self):
        task = md5(urandom(16)).hexdigest()[:6]
        print('[*] Please, give me a string so that md5(string).hexdigest()[:6] == {0}:'.format(task))
        string = input('> ')
        if md5(string.encode()).hexdigest()[:6] != task:
            print('[-] Wrong string!')
            return False
        print('[+] Accepted!', end='\n\n')
        return True
