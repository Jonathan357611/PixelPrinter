from PIL import Image

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)


def show(filename, downscale):
    im = Image.open(filename, 'r')
    width, height = im.size
    im = im.resize(int((width * downscale)), int((height / downscale)))
    width, height = im.size
    pixel_values = list(im.getdata())

    for i, color in enumerate(pixel_values):
        if i % width == 0:
            print("")
        print(get_color_escape(color[0], color[1], color[2], True) + f"  {RESET}", end="")

    print("\n")

if __name__ == '__main__':
    show(input("file (test) > "))