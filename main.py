from PIL import Image

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)


def get_image_color(filename):
    im = Image.open(filename, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())

    print("\n", end="")
    for i, color in enumerate(pixel_values):
        print(get_color_escape(color[0], color[1], color[2]) + get_color_escape(color[0], color[1], color[2], True) + f"  {RESET}", end="")
        if i % width == 0:
            print("")
    print("\n")

get_image_color(input("file (test) > "))