from io import BytesIO
from pathlib import Path

from aspose.zip.gzip import GzipArchive


def run():
    data_dir = Path(__file__).resolve().parents[2] / "Data"

    # Write compressed data to a memory stream.
    with BytesIO() as ms:
        with GzipArchive() as archive:
            archive.set_source(data_dir / "data.bin")
            archive.save(ms)

    print("Successfully Saved to Stream")


if __name__ == "__main__":
    run()
