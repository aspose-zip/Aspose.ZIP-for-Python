from io import BytesIO
from pathlib import Path

from aspose.zip.saving import SevenZipAESEncryptionSettings, SevenZipEntrySettings
from aspose.zip.sevenzip import SevenZipArchive


def run():
    example = Path(__file__).resolve()
    root = example.parents[2]
    output_dir = root / "Output" / example.parent.name / example.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    settings = SevenZipEntrySettings(None, SevenZipAESEncryptionSettings("p@s$"))

    with BytesIO(b"\x00\xff") as source:
        with SevenZipArchive(settings) as archive:
            archive.create_entry("data.bin", source)
            archive.save(str(output_dir / "archive.7z"))

    print("Successfully Created a Seven Zip File with AES Encryption Settings")


if __name__ == "__main__":
    run()
