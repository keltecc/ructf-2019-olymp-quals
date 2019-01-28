#!/usr/bin/python3

import sys

from PIL import Image, ImageDraw, ImageFont
from math import sqrt


SIZE = 512

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 32)


def text_image(text):
    text_width, text_height = FONT.getsize(text)
    img_size = int(max(text_width, text_height) * sqrt(2))
    img = Image.new('RGB', (img_size, img_size), WHITE)
    draw = ImageDraw.Draw(img)
    center_x = (img_size - text_width) // 2
    center_y = (img_size - text_height) // 2
    draw.text((center_x, center_y), text, font=FONT, fill=BLACK)
    img = img.rotate(45, expand=True)
    start = img.width - img_size
    img = img.crop((start, start, img_size, img_size))
    img = img.resize((SIZE, SIZE)).convert('1')
    return img


def insert_text(img, text):
    img = img.copy()
    for x in range(SIZE):
        for y in range(SIZE):
            t = text.getpixel((x, y)) // 255
            t = (t + 1) % 2
            r, g, b = img.getpixel((x, y))
            pixel = r^t, g^t, b^t
            img.putpixel((x, y), pixel)
    return img


def main():
    if len(sys.argv) < 2:
        print('usage: {} <your_flag>'.format(sys.argv[0]))
        sys.exit(1)
    bliss = Image.open('bliss.png')
    text = text_image(sys.argv[1])
    result = insert_text(bliss, text)
    result.save('secret.png')


if __name__ == '__main__':
    main()
