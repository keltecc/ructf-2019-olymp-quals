#!/usr/bin/python3

from Crypto.Util.number import inverse


class RSA(object):
    def __init__(self, p, q, e):
        self._n = p * q
        self._e = e
        self._d = inverse(e, (p-1)*(q-1))

    def set_firewall(self):
        self.encrypt = RSA._firewall(self.encrypt)
        self.decrypt = RSA._firewall(self.decrypt)

    def encrypt(self, m):
        return pow(m, self._e, self._n)
    
    def decrypt(self, c):
        return pow(c, self._d, self._n)

    @staticmethod
    def _firewall(func):
        def inner_func(*args, **kwargs):
            return func(*args, **kwargs) & 1
        return inner_func
