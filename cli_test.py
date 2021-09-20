import click
import main as test

@click.command()
@click.option("--image", "-i", "image", required=True, help="Path to image to display")
@click.option("--downscale", "-d", "downscale", default="1", help="Downscale displayed image by n")
def process(image, downscale):
    test.show(image, int(downscale))

process()