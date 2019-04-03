#!/usr/bin/python3

from ui import UI
from storage import Storage


def read_flag():
    with open('flag.txt', 'rb') as file:
        return file.read().strip()

def main():
    password_length = 16    
    storage = Storage(password_length)
    admin, _ = storage.add('admin')
    admin.place_secret(read_flag())
    UI(storage).interact()

if __name__ == '__main__':
    main()
