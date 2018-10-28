import logging
import shutil
import sys
import time
import typing
from pathlib import Path


logging.Formatter.converter = time.gmtime  # Force UTC

logformat = "%(asctime)s %(levelname)s:%(module)s:%(message)s"
dateformat = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(
    filename="log.txt",
    filemode="a",
    level=logging.INFO,
    format=logformat,
    datefmt=dateformat,
)


def find_files_to_clean(filepath: Path = None) -> typing.List:
    whitelist = [".dds", ".png"]

    return [x for x in filepath.iterdir() if x.suffix.lower() not in whitelist]


def move_files(paths: typing.List = None):
    tmpfolderpath = paths[0].parent / "to_clean"
    tmpfolderpath.mkdir(exist_ok=True)

    for filepath in paths:
        shutil.move(str(filepath), str(tmpfolderpath))


def cleanpath(filepath: Path = None):
    to_clean = find_files_to_clean(filepath)
    logging.info(f"Found {len(to_clean)} files to clean in: {filepath}")

    if len(to_clean) > 0:
        move_files(to_clean)


if __name__ == "__main__":
    cleanpath(Path(sys.argv[1]))
