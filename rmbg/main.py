#!/usr/bin/env python3

from rembg import remove
from PIL import Image


if __name__ == '__main__':
    input_path = 'jess.png'
    output_path = 'jess-alone.png'

    img = Image.open(input_path)
    output = remove(img)
    output.save(output_path)
