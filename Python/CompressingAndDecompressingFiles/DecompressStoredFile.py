from pathlib import Path
from shutil import copyfileobj

from aspose.zip import Archive
from StoreMultipleFilesWithoutCompression import run as store_multiple_files


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    store_multiple_files(output_dir)

    with open(output_dir / "StoreMultipleFilesWithoutCompression_out.zip", "rb") as zip_file:
        with Archive(zip_file) as archive:
            with open(output_dir / "alice_extracted_store_out.txt", "wb") as extracted:
                with archive.entries[0].open() as decompressed:
                    copyfileobj(decompressed, extracted, length=8192)

            with open(output_dir / "asyoulik_extracted_store_out.txt", "wb") as extracted:
                with archive.entries[1].open() as decompressed:
                    copyfileobj(decompressed, extracted, length=8192)


if __name__ == "__main__":
    run()
