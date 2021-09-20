#!/usr/bin/python3

import click
from PIL import Image

class PixelPrinter:
    def __init__(self):
        self.RESET = '\033[0m'

    def get_color_escape(self, r, g, b, background=False):
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

    def error_msg(self, msg):
        return f'\033[38;2;255;0;0mERROR: {msg}'

    def show(self, filename, downscale):
        ### HANDLING ERRORS
        try:
            int(downscale)
        except:
            print(self.error_msg("--downscale is not int!"))
            exit(0)
        if int(downscale) <= 0:
            print(self.error_msg("--downscale can't be zero or smaller!"))
            exit(0)

        ### Load image
        im = Image.open(filename, 'r')
        width, height = im.size
        # (further error handling here)
        if int(downscale) > width or int(downscale) > height:
            print(self.error_msg("--downscale can't larger than height/width of image!"))
            exit(0)

        im = im.resize((int(width / downscale), int(height / downscale)), Image.LANCZOS)
        width, height = im.size
        pixel_values = list(im.getdata())



        for i, color in enumerate(pixel_values):
            if i % width == 0:
                print("")
            print(self.get_color_escape(color[0], color[1], color[2], True) + f"  {self.RESET}", end="")
        print("\n")


@click.command()
@click.option("--image", "-i", "image", required=True, help="Path to image to display")
@click.option("--downscale", "-d", "downscale", default="1", help="Downscale displayed image by n")
def process(image, downscale):
    pp = PixelPrinter()
    pp.show(image, int(downscale))

process()