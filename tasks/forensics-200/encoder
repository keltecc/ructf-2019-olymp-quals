#!/usr/bin/python3

import sys

from os import urandom
from PIL import Image, ImageChops


def randbits(length):
    for byte in urandom(length):
        yield byte & 1


def rand_image(size):
    img = Image.new('1', (size[0] // 2, size[1] // 2))
    bits = randbits(img.width * img.height)
    for x in range(img.width):
        for y in range(img.height):
            img.putpixel((x, y), next(bits))
    return img.resize(size)


def main():
    if len(sys.argv) < 3:
        print('usage: {} <image.png> <result.png>'.format(sys.argv[0]))
        sys.exit(1)
    img = Image.open(sys.argv[1])
    rand = rand_image(img.size)
    result = ImageChops.logical_xor(img, rand)
    result.save(sys.argv[2])


if __name__ == '__main__':
    main()
