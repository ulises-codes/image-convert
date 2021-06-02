from wand.image import Image
from pathlib import Path
import getopt
import sys


def pathIsDirectory(path):
    p = Path(path)

    return p.is_dir()


def convertImageType(path, original_format="*", new_format="webp"):
    is_path = pathIsDirectory(path)

    if is_path:
        for img_path in list(Path(path).glob(f'*.{original_format}')):
            with Image(filename=img_path) as image:
                image.format = new_format
                new_path = ".".join(str(img_path).split('.')
                                    [:-1]) + f".{new_format}"
                print(f"Writing {new_path} to filesystem...")
                image.save(filename=new_path)
                print("Done")


if __name__ == "__main__":
    options, arguments = getopt.getopt(
        sys.argv[1:],
        "pon:", ["path", "original_format", "new_format"])

    convertImageType(*arguments)
