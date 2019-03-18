#!/usr/bin/python3

import sys

from PIL import Image


def sum_pixels(img, x, y, area):
    result = 0
    for dx in range(area):
        for dy in range(area):
            result += img.getpixel((x + dx, y + dy))
    return result // 255


def decode_image(img):
    area = 2
    correct = [0, area ** 2]
    result = Image.new('1', (img.width // area, img.height // area))
    for x in range(result.width):
        for y in range(result.height):
            color = 255 if sum_pixels(img, x*area, y*area, area) in correct else 0
            result.putpixel((x, y), color)
    return result


def main():
    if len(sys.argv) < 2:
        print('usage: {} <image.png>'.format(sys.argv[0]))
        sys.exit(1)
    image = Image.open(sys.argv[1])
    decode_image(image).show()


if __name__ == '__main__':
    main()
