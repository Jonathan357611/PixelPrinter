import click
import main as test

@click.command()
@click.option("--image", "-i", "image", required=True, help="Path to image to display")
@click.option("--downscale", "-d", "downscale", default="0", help="Downscale displayed image by n")
def process(image):
    test.get_image_color(image)

process()