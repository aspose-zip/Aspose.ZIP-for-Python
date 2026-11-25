from io import BytesIO
from pathlib import Path

from aspose.zip.saving import (
    SevenZipAESEncryptionSettings,
    SevenZipEntrySettings,
    SevenZipLZMACompressionSettings,
)
from aspose.zip.sevenzip import SevenZipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    settings = SevenZipEntrySettings(
        SevenZipLZMACompressionSettings(),
        SevenZipAESEncryptionSettings("test1"),
    )

    with open(output_dir / "archive.7z", "wb") as seven_zip_file:
        with BytesIO(b"\x00\xff") as source:
            with SevenZipArchive() as archive:
                archive.create_entry("entry1.bin", source, settings)
                archive.save(seven_zip_file)

    print("Successfully Created a Seven Zip File with AES Encryption Settings")


if __name__ == "__main__":
    run()
