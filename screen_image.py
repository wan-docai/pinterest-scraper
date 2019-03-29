from PIL import Image
import argparse
import os

def screen_image(directory):
    for image in os.listdir(directory):
        try:
            img  = Image.open(image)
        except IOError:
            os.remove(os.path.join(directory, image))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--directory',
        type=str,
        required=True,
        help='image path to check'
    )

    args = parser.parse_args()

    screen_image(args.directory)
