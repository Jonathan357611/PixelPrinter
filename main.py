from PIL import Image

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def error_msg(msg):
    return f'\033[38;2;255;0;0mERROR: {msg}'

def show(filename, downscale):
    ### HANDLING ERRORS
    try:
        int(downscale)
    except:
        print(error_msg("--downscale is not int!"))
        exit(0)
    if int(downscale) <= 0:
        print(error_msg("--downscale can't be zero or smaller!"))
        exit(0)

    ### Load image
    im = Image.open(filename, 'r')
    width, height = im.size
    # (further error handling here)
    if int(downscale) > width or int(downscale) > height:
        print(error_msg("--downscale can't larger than height/width of image!"))
        exit(0)
    # Loading image again
    im = im.resize((int(width / downscale), int(height / downscale)))
    width, height = im.size
    pixel_values = list(im.getdata())


    for i, color in enumerate(pixel_values):
        if i % width == 0:
            print("")
        print(get_color_escape(color[0], color[1], color[2], True) + f"  {RESET}", end="")
    print("\n")

if __name__ == '__main__':
    show(input("file (test) > "))