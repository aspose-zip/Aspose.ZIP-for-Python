from pathlib import Path

from aspose.zip.saving import (
    SevenZipAESEncryptionSettings,
    SevenZipEntrySettings,
    SevenZipStoreCompressionSettings,
)
from aspose.zip.sevenzip import SevenZipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    data_dir = root / "Data"
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    file1 = data_dir / "alice29.txt"
    file2 = data_dir / "asyoulik.txt"
    file3 = data_dir / "fields.c"

    settings1 = SevenZipEntrySettings(
        SevenZipStoreCompressionSettings(),
        SevenZipAESEncryptionSettings("test1"),
    )
    settings2 = SevenZipEntrySettings(
        SevenZipStoreCompressionSettings(),
        SevenZipAESEncryptionSettings("test2"),
    )
    settings3 = SevenZipEntrySettings(
        SevenZipStoreCompressionSettings(),
        SevenZipAESEncryptionSettings("test3"),
    )

    with open(output_dir / "archive.7z", "wb") as seven_zip_file:
        with SevenZipArchive() as archive:
            archive.create_entry("entry1.bin", file1, False, settings1)
            archive.create_entry("entry2.bin", file2, False, settings2)
            archive.create_entry("entry3.bin", file3, False, settings3)
            archive.save(seven_zip_file)

    print("Successfully Created a Seven Zip File with AES Encryption Settings")


if __name__ == "__main__":
    run()
