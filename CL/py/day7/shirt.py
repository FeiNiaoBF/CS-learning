import csv
import sys
from PIL import Image

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    before_file = sys.argv[1]
    after_file = sys.argv[2]
    if not (before_file.lower().endswith(".jpg") or before_file.lower().endswith(".png") or before_file.lower().endswith(".jpeg")):
        sys.exit("Invalid output")
    if not (after_file.lower().endswith(".jpg") or after_file.lower().endswith(".png") or after_file.lower().endswith(".jpeg")):
        sys.exit("Invalid output")
    if before_file.lower().split(".")[-1] != after_file.lower().split(".")[-1]:
        sys.exit("Input and output have different extensions")
    fix_shirt(before_file, after_file)



def fix_shirt(before_file, after_file):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(before_file) as image:
            size = image.size
            shirt = shirt.resize(size)
            image.paste(shirt, shirt)
            image.save(after_file)
    except FileExistsError:
        sys.exit(f"Could not read {before_file}")



if __name__ == "__main__":
    main()
