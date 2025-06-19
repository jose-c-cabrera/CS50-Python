import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

valid_exts = [".jpg", ".jpeg", ".png"]

if not any(output_file.lower().endswith(ext) for ext in valid_exts):
    sys.exit("Invalid output")

if "." not in input_file or "." not in output_file:
    sys.exit("Invalid file name")

input_ext = input_file.rsplit(".", 1)[1].lower()
output_ext = output_file.rsplit(".", 1)[1].lower()

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size

input_image = ImageOps.fit(input_image, size)

input_image.paste(shirt, shirt)

input_image.save(output_file)
