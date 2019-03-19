from PIL import image

image =Image.open(args.image)

parser = argparse.ArgumentParser()

parser.add_argument(
    '--image',
    required=True,
    type=str,
    help='image file to open'
)

args = parser.parse_args()



#
# print(input_image_list)
