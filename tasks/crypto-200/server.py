#!/usr/bin/python3

from storage import User, Storage


def select(*options):
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


def login(storage):
    while True:
        print('[*] Please, enter your username. Leave empty to cancel')
        username = input().strip()
        if len(username) == 0:
            return None
        user = storage.get_user(username)
        if not user:
            print('[-] User does not exist!')
            continue
        print('[*] Please, enter your password')
        password = input().strip()
        if user.check_password(password):
            break
        print('[-] Password is wrong!')
    print('[+] Logged in successfully', end='\n\n')
    return user


def create_account(storage):
    while True:
        print('[*] Please, enter your username. Leave empty to cancel')
        username = input().strip()
        if len(username) == 0:
            return None
        if storage.get_user(username):
            print('[-] User already exists!')
            continue
        password = storage.generate_password()
        user = User(username, password)
        storage.add_user(user)
        print('[*] Your password: ' + password)
        break
    print('[+] Account created successfully', end='\n\n')
    return user


def handle(user, storage):
    while True:
        option = select('Place a secret', 'Extract the secret', 'Change the password', 'Log out')
        if option == 1:
            print('[*] Please, input your secret')
            secret = input().strip().encode('utf-8')
            user.place_secret(secret)
            print('[+] Secret placed successfully', end='\n\n')
        elif option == 2:
            print('[*] Extracting your secret...')
            print(user.extract_secret(), end='\n\n')
        elif option == 3:
            print('[*] Please, enter new password')
            password = input().strip()
            user.change_password(password)
            print('[+] Password changed successfully', end='\n\n')
        elif option == 4:
            print('[+] Logging out', end='\n\n')
            break


def unauthorized(storage):
    while True:
        print('[-] You are not authorized. Please, log in or create your account', end='\n\n')
        option = select('Log in', 'Create an account', 'Exit')
        if option == 1:
            user = login(storage)
            if not user:
                continue
        elif option == 2:
            user = create_account(storage)
            if not user:
                continue
        elif option == 3:
            break
        handle(user, storage)


def main():
    with open('flag.txt', 'rb') as file:
        flag = file.read().strip()
    storage = Storage(16)
    print('[*] Hello! Welcome to the secure crypto storage!')
    admin = User('admin', storage.generate_password())
    admin.place_secret(flag)
    storage.add_user(admin)
    unauthorized(storage)
    print('[*] Bye')


if __name__ == '__main__':
    main()
