#!/usr/bin/python3

import sys

from PIL import Image, ImageDraw, ImageFont


FONT = ImageFont.truetype('DejaVuSansMono-Bold.ttf', 20)
BLACK = (0, 0, 0)


def write_text(text, image):
    text_width, text_height = FONT.getsize(text)
    draw = ImageDraw.Draw(image)
    center_x = (image.width - text_width) // 2
    center_y = (image.height - text_height) // 2
    draw.text((center_x, center_y), text, font=FONT, fill=BLACK)


def main():
    if len(sys.argv) < 4:
        print('usage: {} <text> <container.png> <result.png>'.format(sys.argv[0]))
        sys.exit(1)
    container = Image.open(sys.argv[2])
    write_text(sys.argv[1], container)
    container.save(sys.argv[3])


if __name__ == '__main__':
    main()
