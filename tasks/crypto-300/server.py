#!/usr/bin/python3

from ui import UI
from rsa import RSA

from Crypto.Util.number import bytes_to_long


def read_flag():
    with open('flag.txt', 'rb') as file:
        return file.read()


def check_secret(secret):
    assert secret.bits == 512
    assert secret.p.bit_length() == secret.bits
    assert secret.q.bit_length() == secret.bits
    assert secret.e < secret.bits


def main():
    import secret
    check_secret(secret)
    rsa = RSA(secret.p, secret.q, secret.e)
    message = rsa.encrypt(bytes_to_long(read_flag()))
    rsa.set_firewall()
    ui = UI(rsa, message)
    ui.interact()


if __name__ == '__main__':
    main()
