#!/usr/bin/python3

class UI(object):
    def __init__(self, storage):
        self._storage = storage
        self._user = None

    def interact(self):
        print('[*] Hello! Welcome to the secure crypto storage!')
        while True:
            print('[-] You are not authorized. Please, log in or create your account', end='\n\n')
            option = self._select('Log in', 'Create an account', 'Exit')
            if (option == 1 and not self._login()) or (option == 2 and not self._register()):
                continue
            elif option == 3:
                break
            self._menu()
        print('[*] Bye')

    def _menu(self):
        while True:
            option = self._select('Place a secret', 'Extract the secret', 'Change the password', 'Log out')
            if option == 1:
                print('[*] Please, input your secret')
                secret = input().strip().encode('utf-8')
                self._user.place_secret(secret)
                print('[+] Secret placed successfully', end='\n\n')
            elif option == 2:
                print('[*] Extracting your secret...')
                print(self._user.extract_secret(), end='\n\n')
            elif option == 3:
                print('[*] Please, enter new password')
                password = input().strip()
                self._user.change_password(password)
                print('[+] Password changed successfully', end='\n\n')
            elif option == 4:
                print('[+] Logging out', end='\n\n')
                self._logout()
                break

    def _login(self):
        while True:
            print('[*] Please, enter your username. Leave empty to cancel')
            username = input().strip()
            if len(username) == 0:
                return False
            user = self._storage.get(username)
            if not user:
                print('[-] User does not exist!')
                continue
            print('[*] Please, enter your password')
            password = input().strip()
            if user.check_password(password):
                print('[+] Logged in successfully', end='\n\n')
                self._user = user
                return True
            print('[-] Password is wrong!')

    def _register(self):
        while True:
            print('[*] Please, enter your username. Leave empty to cancel')
            username = input().strip()
            if len(username) == 0:
                return False
            if self._storage.get(username):
                print('[-] User already exists!')
                continue
            user, password = self._storage.add(username)
            print('[*] Your password: ' + password)
            print('[+] Account created successfully', end='\n\n')
            self._user = user
            return True

    def _logout(self):
        self._user = None

    def _select(self, *options):
        print('[?] What do you want to do?')
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
