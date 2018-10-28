import logging
import sys
import time
from pathlib import Path
from zipfile import ZipFile

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


def unpack(zipdir: Path = None, unpackdir: Path = None):
    logging.info(f"Unpacking *.zip file(s) from '{zipdir}' to '{unpackdir}'")
    for file in zipdir.iterdir():
        logging.info(f"Unpacking: {file}")
        with ZipFile(file) as zf:
            zf.extractall(path=unpackdir)

        logging.info(f"Successfully unpacked: {file}")


if __name__ == "__main__":
    unpack(Path(sys.argv[1]), Path(sys.argv[2]))
