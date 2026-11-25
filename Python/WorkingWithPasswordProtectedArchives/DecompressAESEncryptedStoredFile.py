from pathlib import Path
from shutil import copyfileobj

from aspose.zip import Archive, ArchiveLoadOptions
from StoreMultipleFilesWithoutCompressionWithPassword import run as store_with_password


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    store_with_password(output_dir)

    load_options = ArchiveLoadOptions()
    load_options.decryption_password = "p@s$"

    with open(output_dir / "StoreMultipleFilesWithoutCompressionWithPassword_out.zip", "rb") as source:
        with open(output_dir / "alice_aesextracted_out.txt", "wb") as extracted:
            with Archive(source, load_options) as archive:
                with archive.entries[0].open() as decompressed:
                    copyfileobj(decompressed, extracted, length=8192)


if __name__ == "__main__":
    run()
