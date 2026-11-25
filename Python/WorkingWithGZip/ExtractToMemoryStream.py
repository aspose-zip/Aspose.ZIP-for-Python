from io import BytesIO
from pathlib import Path
from shutil import copyfileobj

from aspose.zip.gzip import GzipArchive


def run():
    data_dir = Path(__file__).resolve().parents[2] / "Data"

    # Open an archive from a stream and extract it to a memory stream.
    with BytesIO() as ms:
        with open(data_dir / "sample.gz", "rb") as source:
            with GzipArchive(source) as archive:
                with archive.open() as unpacked:
                    copyfileobj(unpacked, ms)
                print(archive.name)

    print("Successfully Extractd to Memory Stream")


if __name__ == "__main__":
    run()
