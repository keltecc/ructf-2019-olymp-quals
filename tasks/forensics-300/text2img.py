#!/usr/bin/python3

import sys

from PIL import Image, ImageDraw, ImageFont
from math import sqrt


SIZE = 1024
FONT = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 32)

BLACK = 0
WHITE = 1


def text_to_image(text):
    text_width, text_height = FONT.getsize(text)
    img_size = int(max(text_width, text_height) * sqrt(2))
    img = Image.new('1', (img_size, img_size), WHITE)
    draw = ImageDraw.Draw(img)
    center_x = (img_size - text_width) // 2
    center_y = (img_size - text_height) // 2
    draw.text((center_x, center_y), text, font=FONT, fill=BLACK)
    img = img.rotate(45, expand=True)
    crop_pos = img.width - img_size
    img = img.crop((crop_pos, crop_pos, img_size, img_size))
    img = img.resize((SIZE, SIZE))
    return img


def main():
    if len(sys.argv) < 3:
        print('usage: {} <text> <image.png>'.format(sys.argv[0]))
        sys.exit(1)
    image = text_to_image(sys.argv[1])
    image.save(sys.argv[2])


if __name__ == '__main__':
    main()
