from pathlib import Path
from shutil import copyfileobj

from aspose.zip.gzip import GzipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    # Extract the archive and copy its contents to a file stream.
    with GzipArchive(str(data_dir / "archive.gz")) as archive:
        with open(output_dir / "data.bin", "wb") as extracted:
            with archive.open() as unpacked:
                copyfileobj(unpacked, extracted, length=8192)

    print("Successfully Opened GZip Archive")


if __name__ == "__main__":
    run()
