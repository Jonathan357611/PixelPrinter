import click
import main as test

def error_msg(msg):
    return f'\033[38;2;255;0;0m ERROR: {msg}'

@click.command()
@click.option("--image", "-i", "image", required=True, help="Path to image to display")
@click.option("--downscale", "-d", "downscale", default="1", help="Downscale displayed image by n")
def process(image, downscale):
    if not downscale.isnumeric:
        print(error_msg("--downscale is not int!"))
    test.show(image, int(downscale))

process()