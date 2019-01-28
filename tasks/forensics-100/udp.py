#!/usr/bin/python3

import sys
import select

from socket import socket, AF_INET, SOCK_DGRAM


def main():
    length = 1024
    secret = open('secret.zip', 'rb').read()
    address = ('0.0.0.0', 31337)
    
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(address)

    while True:
        print('listening')
        data, addr = server.recvfrom(2048)
        print(data[:-1].decode())
        if b'ready' in data:
            print('sending secret')
            for i in range(0, len(secret), length):
                server.sendto(secret[i:i+length], addr)
        else:
            print('sending warning')
            server.sendto(b'You are not ready to receive a secret.\n', addr)


if __name__ == '__main__':
    main()
